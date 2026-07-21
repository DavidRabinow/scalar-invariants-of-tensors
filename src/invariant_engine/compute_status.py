"""Host compute metrics without privileged APIs."""

from __future__ import annotations

import os
import shutil
from typing import Any


def collect_compute(*, workers: int = 1, ram_ceiling_gb: float | None = None) -> dict[str, Any]:
    out: dict[str, Any] = {
        "workers": workers,
        "ram_ceiling_gb": ram_ceiling_gb,
        "cpu_percent": None,
        "physical_ram_gb": None,
        "ram_used_gb": None,
        "disk_free_gb": None,
        "cache_size_mb": None,
        "thermal": None,
        "stage_timing_sec": {},
        "projected_completion": {
            "eta_sec": None,
            "uncertainty": "high — projection from incomplete stage timing only",
        },
    }
    try:
        import psutil

        out["cpu_percent"] = psutil.cpu_percent(interval=0.05)
        vm = psutil.virtual_memory()
        out["physical_ram_gb"] = round(vm.total / (1024**3), 2)
        out["ram_used_gb"] = round(vm.used / (1024**3), 2)
    except Exception:
        pass

    try:
        usage = shutil.disk_usage(os.getcwd())
        out["disk_free_gb"] = round(usage.free / (1024**3), 2)
    except Exception:
        pass

    # Thermal: best-effort, non-privileged (often unavailable).
    try:
        import subprocess

        raw = subprocess.check_output(
            ["pmset", "-g", "therm"],
            stderr=subprocess.DEVNULL,
            text=True,
            timeout=3,
        )
        out["thermal"] = raw.strip()[:500] or None
    except Exception:
        out["thermal"] = None

    return out
