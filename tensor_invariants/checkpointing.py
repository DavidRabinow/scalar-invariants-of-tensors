"""Checkpointing for resumable degree-by-degree exploration."""

from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any


def ensure_dir(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path


def checkpoint_path(root: Path, name: str) -> Path:
    return ensure_dir(root) / f"{name}.json"


def save_checkpoint(root: Path, name: str, payload: dict[str, Any]) -> Path:
    path = checkpoint_path(root, name)
    data = dict(payload)
    data["_saved_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(data, indent=2, default=str), encoding="utf-8")
    tmp.replace(path)
    return path


def load_checkpoint(root: Path, name: str) -> dict[str, Any] | None:
    path = checkpoint_path(root, name)
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))
