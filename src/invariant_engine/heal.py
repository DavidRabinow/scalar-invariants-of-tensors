"""Heal stale run state when the process died without a clean STOP."""

from __future__ import annotations

import atexit
import os
import time
from pathlib import Path
from typing import Any

from .atomic_io import atomic_write_json
from .paths import LIVE_PROGRESS, PID_FILE, ensure_state_dirs
from .progress import baseline_live_progress, load_live_progress


def pid_alive(pid: int | None) -> bool:
    if not pid:
        return False
    try:
        os.kill(int(pid), 0)
        return True
    except OSError:
        return False
    except Exception:
        return False


def read_pid_file_dict(path: Path = PID_FILE) -> dict[str, str]:
    if not path.exists():
        return {}
    out: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or "=" not in line:
            continue
        k, v = line.split("=", 1)
        out[k.strip()] = v.strip().strip("'").strip('"')
    return out


def heal_stale_state(*, reason: str = "stale process") -> dict[str, Any]:
    """
    If live_progress says RUNNING but the PID is dead (or missing), mark STOPPED/ERROR
    and remove a stale PID file so a new run can start.
    """
    ensure_state_dirs()
    report: dict[str, Any] = {"healed": False, "actions": []}
    meta = read_pid_file_dict()
    file_pid = None
    for key in ("PYTHON_PID", "PID", "WRAPPER_PID"):
        if meta.get(key):
            try:
                file_pid = int(meta[key])
                break
            except ValueError:
                continue

    live = load_live_progress(LIVE_PROGRESS) if LIVE_PROGRESS.exists() else {}
    live_pid = live.get("pid")
    try:
        live_pid_i = int(live_pid) if live_pid is not None else None
    except (TypeError, ValueError):
        live_pid_i = None

    status = live.get("status")
    any_alive = pid_alive(file_pid) or pid_alive(live_pid_i)

    if status in {"RUNNING", "PAUSED", "CHECKPOINTING"} and not any_alive:
        live["status"] = "ERROR"
        live["error"] = f"Auto-heal: {reason} (process gone; last task: {live.get('current_task')})"
        live["current_task"] = f"Crashed / interrupted — {reason}. Will resume from checkpoint if restarted."
        live["current_task_beginner"] = (
            "The research process stopped unexpectedly. The system will try again from the last saved checkpoint."
        )
        live["heartbeat_at"] = time.time()
        atomic_write_json(LIVE_PROGRESS, live)
        report["healed"] = True
        report["actions"].append("marked_live_progress_ERROR")

    if PID_FILE.exists() and not any_alive:
        PID_FILE.unlink(missing_ok=True)
        report["healed"] = True
        report["actions"].append("removed_stale_pid_file")

    if not LIVE_PROGRESS.exists():
        atomic_write_json(LIVE_PROGRESS, baseline_live_progress())
        report["actions"].append("wrote_baseline")

    return report


def install_crash_marker() -> None:
    """On interpreter exit, if still marked RUNNING, flip to ERROR (covers most crashes except SIGKILL)."""

    def _atexit() -> None:
        try:
            if not LIVE_PROGRESS.exists():
                return
            live = load_live_progress(LIVE_PROGRESS)
            if live.get("status") in {"RUNNING", "PAUSED", "CHECKPOINTING"}:
                # Only mark if we are the recorded pid (or pid missing).
                try:
                    recorded = int(live.get("pid") or -1)
                except (TypeError, ValueError):
                    recorded = -1
                if recorded in (-1, os.getpid()) or not pid_alive(recorded):
                    live["status"] = "ERROR"
                    live["error"] = "Process exited while still RUNNING (crash or kill)."
                    live["current_task"] = "Interrupted — auto-heal marker written"
                    live["heartbeat_at"] = time.time()
                    atomic_write_json(LIVE_PROGRESS, live)
            if PID_FILE.exists():
                meta = read_pid_file_dict()
                try:
                    p = int(meta.get("PYTHON_PID") or meta.get("PID") or -1)
                except ValueError:
                    p = -1
                if p in (-1, os.getpid()) or not pid_alive(p):
                    PID_FILE.unlink(missing_ok=True)
        except Exception:
            pass

    atexit.register(_atexit)
