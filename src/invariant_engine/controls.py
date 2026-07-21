"""Localhost-only control requests consumed at safe atomic boundaries."""

from __future__ import annotations

import time
from pathlib import Path
from typing import Any

from .atomic_io import atomic_write_json

ALLOWED = frozenset(
    {
        "pause",
        "resume",
        "checkpoint",
        "stop",
        "open_report",
        "open_generators",
        "open_errors",
    }
)


def control_request_path() -> Path:
    from . import paths as _paths

    _paths.ensure_state_dirs()
    return _paths.CONTROL_DIR / "request.json"


def control_ack_path() -> Path:
    from . import paths as _paths

    return _paths.CONTROL_DIR / "ack.json"


def write_control(action: str, *, source: str = "dashboard", detail: str = "") -> dict[str, Any]:
    if action not in ALLOWED:
        raise ValueError(f"Disallowed control action: {action}")
    req = {
        "action": action,
        "requested_at": time.time(),
        "source": source,
        "detail": detail,
        "id": f"{action}-{int(time.time() * 1000)}",
    }
    atomic_write_json(control_request_path(), req)
    return req


def read_control() -> dict[str, Any] | None:
    path = control_request_path()
    if not path.exists():
        return None
    import json

    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def clear_control() -> None:
    path = control_request_path()
    if path.exists():
        path.unlink()


def ack_control(req: dict[str, Any], *, applied: bool, message: str) -> None:
    atomic_write_json(
        control_ack_path(),
        {
            "request": req,
            "applied": applied,
            "message": message,
            "acked_at": time.time(),
        },
    )
    clear_control()
