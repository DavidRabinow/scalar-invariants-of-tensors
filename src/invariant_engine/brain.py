"""
Autonomous 'brain' decisions for the 10D climb toward ~81.

Called by the monitor loop and optionally by the controller. Decides whether
to keep waiting, start N=8, skip catalog, heal, or restart.
"""

from __future__ import annotations

import json
import time
from pathlib import Path
from typing import Any

from .paths import LIVE_PROGRESS, RESEARCH_STATE, ensure_state_dirs

N8_CACHE = RESEARCH_STATE / "cache" / "graphs_N8_r5.json"
N8_ENUM_PROG = RESEARCH_STATE / "cache" / "enum_n8_r5_progress.json"
BRAIN_STATE = RESEARCH_STATE / "brain_state.json"
LITERATURE_TARGET = 81


def _load_live() -> dict[str, Any]:
    if not LIVE_PROGRESS.exists():
        return {}
    try:
        return json.loads(LIVE_PROGRESS.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _load_brain() -> dict[str, Any]:
    if not BRAIN_STATE.exists():
        return {"decisions": [], "best_found": 0}
    try:
        return json.loads(BRAIN_STATE.read_text(encoding="utf-8"))
    except Exception:
        return {"decisions": [], "best_found": 0}


def _save_brain(state: dict[str, Any]) -> None:
    ensure_state_dirs()
    BRAIN_STATE.write_text(json.dumps(state, indent=2), encoding="utf-8")


def decide() -> dict[str, Any]:
    """
    Inspect live progress + N=8 enum status; return an action recommendation.

    Actions:
      - hold: healthy, still useful work (or waiting on N8)
      - skip_catalog_pivot: catalog stalled; should wait/climb N8 instead
      - n8_ready_climb: N=8 cache ready — restart/resume climb including N=8
      - heal_restart: process dead / stale RUNNING
      - celebrate_progress: found_count increased
    """
    ensure_state_dirs()
    live = _load_live()
    brain = _load_brain()
    now = time.time()

    fr = (live.get("certified_frontier") or {}).get("spacetime_10d") or {}
    found = int(fr.get("found_count") or 0)
    # Prefer graph climb number when present
    graphs = (live.get("invariant_classification") or {}).get("10d_graphs") or {}
    if graphs.get("found_count") is not None:
        found = max(found, int(graphs["found_count"]))

    best = int(brain.get("best_found") or 0)
    improved = found > best
    if improved:
        brain["best_found"] = found

    task = (live.get("current_task") or "")
    status = live.get("status")
    hb = live.get("heartbeat_at")
    hb_age = (now - float(hb)) if hb else None

    n8_ready = N8_CACHE.exists()
    n8_prog = {}
    if N8_ENUM_PROG.exists():
        try:
            n8_prog = json.loads(N8_ENUM_PROG.read_text(encoding="utf-8"))
        except Exception:
            n8_prog = {}

    pid = live.get("pid")
    alive = False
    if pid:
        try:
            import os

            os.kill(int(pid), 0)
            alive = True
        except Exception:
            alive = False

    action = "hold"
    reason = "nominal"
    if status in {"RUNNING", "PAUSED", "CHECKPOINTING"} and not alive:
        action = "heal_restart"
        reason = "live says RUNNING but process is dead"
    elif n8_ready and found < LITERATURE_TARGET and not brain.get("n8_climb_launched"):
        action = "n8_ready_climb"
        reason = "N=8 graph cache ready — climb next rung"
    elif "catalog chunk" in task and found <= max(best, 12) and not n8_ready:
        action = "skip_catalog_pivot"
        reason = "catalog stalled; wait for N=8 enum instead of re-rolling catalog"
    elif improved:
        action = "celebrate_progress"
        reason = f"found_count rose to {found}"
    elif n8_prog.get("status") == "running":
        action = "hold"
        reason = f"N=8 enum still running; found={found}"
    else:
        action = "hold"
        reason = f"status={status} found={found} n8_ready={n8_ready}"

    decision = {
        "t": now,
        "action": action,
        "reason": reason,
        "found": found,
        "best_found": brain.get("best_found"),
        "target": LITERATURE_TARGET,
        "n8_ready": n8_ready,
        "n8_enum": n8_prog,
        "status": status,
        "task": task[:160],
        "alive": alive,
        "hb_age": hb_age,
        "progress_pct_count": round(100.0 * found / LITERATURE_TARGET, 1),
    }
    hist = list(brain.get("decisions") or [])
    hist.append(decision)
    brain["decisions"] = hist[-40:]
    brain["last"] = decision
    _save_brain(brain)
    return decision
