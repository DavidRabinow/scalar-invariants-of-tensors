"""macOS power / battery detection helpers (no sudo, no permanent settings)."""

from __future__ import annotations

import platform
import re
import subprocess
from dataclasses import dataclass


@dataclass
class PowerStatus:
    os_name: str
    is_macos: bool
    on_battery: bool | None  # None if unknown / not macOS
    raw: str = ""


def is_macos(uname: str | None = None) -> bool:
    name = uname if uname is not None else platform.system()
    return name == "Darwin"


def caffeinate_path() -> str:
    return "/usr/bin/caffeinate"


def caffeinate_exists(path: str | None = None) -> bool:
    from pathlib import Path

    return Path(path or caffeinate_path()).exists()


def detect_battery(pmset_output: str | None = None) -> PowerStatus:
    """Detect AC vs battery via `pmset -g batt` when available."""
    macos = is_macos()
    if not macos:
        return PowerStatus(os_name=platform.system(), is_macos=False, on_battery=None)

    raw = pmset_output
    if raw is None:
        try:
            raw = subprocess.check_output(
                ["pmset", "-g", "batt"],
                stderr=subprocess.STDOUT,
                text=True,
                timeout=5,
            )
        except Exception as exc:
            return PowerStatus(
                os_name="Darwin",
                is_macos=True,
                on_battery=None,
                raw=str(exc),
            )

    # Typical: "Now drawing from 'Battery Power'" or "'AC Power'"
    on_battery: bool | None
    if re.search(r"Battery Power", raw, re.I):
        on_battery = True
    elif re.search(r"AC Power", raw, re.I):
        on_battery = False
    else:
        on_battery = None
    return PowerStatus(os_name="Darwin", is_macos=True, on_battery=on_battery, raw=raw)


def build_caffeinate_command(
    inner_argv: list[str],
    *,
    flags: str = "-dimsu",
    caffeinate_bin: str | None = None,
) -> list[str]:
    """
    Construct argv that runs ``inner_argv`` under caffeinate.

    Flags (documented for operators):
      -d  prevent display sleep
      -i  prevent idle system sleep
      -m  prevent disk idle sleep
      -s  prevent system sleep while on AC power (conservative plugged-in mode)
      -u  declare user activity
    """
    bin_path = caffeinate_bin or caffeinate_path()
    return [bin_path, flags, "--", *inner_argv]


def should_refuse_battery_run(
    *,
    allow_battery: bool,
    power: PowerStatus | None = None,
    wall_hours: float = 0.0,
    long_run_hours: float = 1.0,
) -> tuple[bool, str]:
    """Return (refuse?, message). Refuse long runs on battery unless explicitly allowed."""
    if allow_battery:
        return False, ""
    status = power or detect_battery()
    if status.on_battery is True and wall_hours >= long_run_hours:
        return (
            True,
            "Mac appears to be on battery. Pass --allow-battery to proceed with a long run, "
            "or plug in AC power (preferred for overnight).",
        )
    if status.on_battery is True and wall_hours > 0:
        return (
            False,
            "WARNING: Mac appears to be on battery. Prefer AC power for long research runs.",
        )
    return False, ""
