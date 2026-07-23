"""Atomic file writes so the dashboard never reads a partial JSON document."""

from __future__ import annotations

import json
import os
import time
from pathlib import Path
from typing import Any


def atomic_write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    last_err: Exception | None = None
    for _ in range(5):
        tmp = path.parent / f".{path.name}.tmp.{os.getpid()}.{int(time.time() * 1e6)}"
        try:
            tmp.write_text(text, encoding="utf-8")
            os.replace(tmp, path)
            return
        except OSError as exc:
            # Rare race under SIGTERM / concurrent heal; retry with a new tmp.
            last_err = exc
        finally:
            if tmp.exists():
                try:
                    tmp.unlink()
                except OSError:
                    pass
    if last_err is not None:
        raise last_err
    raise RuntimeError(f"atomic_write_text failed for {path}")


def atomic_write_json(path: Path, data: Any, *, indent: int = 2) -> None:
    atomic_write_text(path, json.dumps(data, indent=indent, default=str) + "\n")


def append_jsonl(path: Path, record: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    line = json.dumps(record, default=str) + "\n"
    with path.open("a", encoding="utf-8") as fh:
        fh.write(line)
        fh.flush()
        os.fsync(fh.fileno())
