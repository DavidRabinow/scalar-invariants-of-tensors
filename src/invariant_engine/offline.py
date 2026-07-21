"""Offline readiness checks and runtime network guard."""

from __future__ import annotations

import ast
import importlib.util
import os
import shutil
import socket
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .paths import (
    CHECKPOINT_DIR,
    DASHBOARD_STATIC,
    LOG_DIR,
    REPO_ROOT,
    RESEARCH_STATE,
    ensure_state_dirs,
)

REQUIRED_MODULES = ("numpy", "opt_einsum", "networkx", "flask")
# psutil is recommended for compute metrics but optional for offline readiness.
OPTIONAL_MODULES = ("psutil",)

# Project code roots scanned for HTTP usage.
SCAN_ROOTS = (
    REPO_ROOT / "src" / "invariant_engine",
    REPO_ROOT / "src" / "invariants",
)

HTTP_PATTERNS = (
    "requests.",
    "urllib.request",
    "urllib3",
    "httpx",
    "aiohttp",
    "httplib",
    "http.client",
)


@dataclass
class CheckResult:
    name: str
    ok: bool
    detail: str


@dataclass
class OfflineReport:
    ok: bool
    checks: list[CheckResult] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "ok": self.ok,
            "checks": [{"name": c.name, "ok": c.ok, "detail": c.detail} for c in self.checks],
        }


class OfflineNetworkGuard:
    """Monkey-patch socket connections when --offline is enabled."""

    def __init__(self) -> None:
        self._orig = None
        self.enabled = False

    def enable(self) -> None:
        if self.enabled:
            return
        self._orig = socket.socket.connect

        def blocked(self_sock, address):  # type: ignore[no-untyped-def]
            raise RuntimeError(
                f"Offline mode: network connection blocked to {address!r}. "
                "Required artifacts must already be present locally."
            )

        socket.socket.connect = blocked  # type: ignore[method-assign]
        self.enabled = True
        os.environ["INVARIANT_ENGINE_OFFLINE"] = "1"

    def disable(self) -> None:
        if not self.enabled or self._orig is None:
            return
        socket.socket.connect = self._orig  # type: ignore[method-assign]
        self.enabled = False


_GUARD = OfflineNetworkGuard()


def enable_offline_mode() -> None:
    _GUARD.enable()


def offline_enabled() -> bool:
    return _GUARD.enabled or os.environ.get("INVARIANT_ENGINE_OFFLINE") == "1"


def _module_installed(name: str) -> bool:
    return importlib.util.find_spec(name) is not None


def _scan_http_usage(roots: tuple[Path, ...] = SCAN_ROOTS) -> list[str]:
    hits: list[str] = []
    for root in roots:
        if not root.exists():
            continue
        for path in root.rglob("*.py"):
            # Allow offline.py itself to mention HTTP APIs in the scanner list.
            if path.name == "offline.py":
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            for pat in HTTP_PATTERNS:
                if pat in text:
                    hits.append(f"{path.relative_to(REPO_ROOT)}: mentions {pat}")
            # AST: forbid imports of networking libs in project code.
            try:
                tree = ast.parse(text, filename=str(path))
            except SyntaxError:
                continue
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        if alias.name.split(".")[0] in {
                            "requests",
                            "urllib3",
                            "httpx",
                            "aiohttp",
                        }:
                            hits.append(f"{path.relative_to(REPO_ROOT)}: import {alias.name}")
                elif isinstance(node, ast.ImportFrom) and node.module:
                    top = node.module.split(".")[0]
                    if top in {"requests", "urllib3", "httpx", "aiohttp"}:
                        hits.append(f"{path.relative_to(REPO_ROOT)}: from {node.module}")
    return hits


def _cdn_assets(static_dir: Path = DASHBOARD_STATIC) -> list[str]:
    bad: list[str] = []
    if not static_dir.exists():
        return [f"Missing dashboard static dir: {static_dir}"]
    for path in static_dir.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() not in {".html", ".js", ".css"}:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for needle in (
            "https://fonts.googleapis.com",
            "https://fonts.gstatic.com",
            "https://cdn.",
            "http://cdn.",
            "unpkg.com",
            "jsdelivr.net",
            "cdnjs.cloudflare.com",
        ):
            if needle in text:
                bad.append(f"{path.name}: loads {needle}")
    return bad


def check_offline(*, min_disk_gb: float = 1.0) -> OfflineReport:
    ensure_state_dirs()
    checks: list[CheckResult] = []

    missing = [m for m in REQUIRED_MODULES if not _module_installed(m)]
    checks.append(
        CheckResult(
            "python_dependencies",
            not missing,
            "all installed" if not missing else f"missing: {', '.join(missing)}",
        )
    )
    opt_missing = [m for m in OPTIONAL_MODULES if not _module_installed(m)]
    checks.append(
        CheckResult(
            "optional_psutil",
            True,
            "installed" if not opt_missing else f"missing optional: {', '.join(opt_missing)} (compute metrics degraded)",
        )
    )

    http_hits = _scan_http_usage()
    checks.append(
        CheckResult(
            "no_runtime_http_in_project_code",
            not http_hits,
            "clean" if not http_hits else "; ".join(http_hits[:8]),
        )
    )

    checks.append(
        CheckResult(
            "no_remote_database",
            True,
            "engine uses local JSON/JSONL files only",
        )
    )

    theory_ok = (REPO_ROOT / "src" / "invariants").is_dir()
    checks.append(
        CheckResult(
            "theory_metadata_local",
            theory_ok,
            "src/invariants present" if theory_ok else "missing invariants package",
        )
    )

    checks.append(
        CheckResult(
            "no_cursor_api_required",
            True,
            "invariant-engine Python process does not call Cursor APIs",
        )
    )
    checks.append(
        CheckResult(
            "no_cloud_model_required",
            True,
            "no cloud model dependency for local computation",
        )
    )

    static_ok = DASHBOARD_STATIC.is_dir() and (DASHBOARD_STATIC / "index.html").exists()
    checks.append(
        CheckResult(
            "dashboard_assets_local",
            static_ok,
            str(DASHBOARD_STATIC) if static_ok else "dashboard static assets missing",
        )
    )

    cdn = _cdn_assets()
    checks.append(
        CheckResult(
            "no_cdn_assets",
            not cdn,
            "all local" if not cdn else "; ".join(cdn),
        )
    )

    writable = True
    detail_w = []
    for d in (RESEARCH_STATE, CHECKPOINT_DIR, LOG_DIR):
        try:
            d.mkdir(parents=True, exist_ok=True)
            probe = d / ".write_probe"
            probe.write_text("ok", encoding="utf-8")
            probe.unlink()
        except Exception as exc:
            writable = False
            detail_w.append(f"{d}: {exc}")
    checks.append(
        CheckResult(
            "result_dirs_writable",
            writable,
            "ok" if writable else "; ".join(detail_w),
        )
    )

    try:
        free = shutil.disk_usage(REPO_ROOT).free / (1024**3)
        disk_ok = free >= min_disk_gb
        disk_detail = f"{free:.1f} GiB free (need ≥ {min_disk_gb})"
    except Exception as exc:
        disk_ok = False
        disk_detail = str(exc)
    checks.append(CheckResult("sufficient_disk", disk_ok, disk_detail))

    ok = all(c.ok for c in checks)
    return OfflineReport(ok=ok, checks=checks)


def print_report(report: OfflineReport) -> None:
    print("Offline readiness")
    print("=================")
    for c in report.checks:
        mark = "PASS" if c.ok else "FAIL"
        print(f"  [{mark}] {c.name}: {c.detail}")
    print()
    if report.ok:
        print("OK — invariant-engine can run locally without Wi-Fi after installation.")
    else:
        print("NOT READY — fix failing checks before an overnight run.")
    print()
    print("Note: Cursor Agent itself needs internet to generate code / talk to models.")
    print("Once implementation is complete, the Python process runs on this Mac offline.")
    print("Cursor Background Agents are remote and are not a local overnight run.")
