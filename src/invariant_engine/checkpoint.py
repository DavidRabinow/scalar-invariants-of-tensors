"""Checkpoint save/load for autonomous runs."""

from __future__ import annotations

import time
from pathlib import Path
from typing import Any

from .atomic_io import atomic_write_json


def checkpoint_path(run_id: str, tag: str = "latest") -> Path:
    from . import paths as _paths

    _paths.ensure_state_dirs()
    return _paths.CHECKPOINT_DIR / f"{run_id}_{tag}.json"


def save_checkpoint(
    *,
    run_id: str,
    stage: str,
    config: dict[str, Any],
    live: dict[str, Any],
    work: dict[str, Any],
    tag: str = "latest",
) -> Path:
    from . import paths as _paths

    _paths.ensure_state_dirs()
    path = _paths.CHECKPOINT_DIR / f"{run_id}_{tag}.json"
    payload = {
        "run_id": run_id,
        "saved_at": time.time(),
        "stage": stage,
        "config": config,
        "live": live,
        "work": work,
        "valid": True,
    }
    atomic_write_json(path, payload)
    stamped = _paths.CHECKPOINT_DIR / f"{run_id}_{time.strftime('%Y%m%dT%H%M%S')}.json"
    atomic_write_json(stamped, payload)
    return path


def load_checkpoint(path: Path) -> dict[str, Any]:
    import json

    data = json.loads(path.read_text(encoding="utf-8"))
    if not data.get("valid"):
        raise ValueError(f"Checkpoint marked invalid: {path}")
    return data


def latest_checkpoint(run_id: str | None = None) -> Path | None:
    from . import paths as _paths

    _paths.ensure_state_dirs()
    files = sorted(_paths.CHECKPOINT_DIR.glob("*_latest.json"), key=lambda p: p.stat().st_mtime)
    if run_id:
        files = [p for p in files if p.name.startswith(f"{run_id}_")]
    return files[-1] if files else None
