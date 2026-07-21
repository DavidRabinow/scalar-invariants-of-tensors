"""Tests for caffeinate command construction, battery gate, and power helpers."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from invariant_engine.power import (  # noqa: E402
    PowerStatus,
    build_caffeinate_command,
    caffeinate_exists,
    detect_battery,
    is_macos,
    should_refuse_battery_run,
)


class TestMacOSDetection(unittest.TestCase):
    def test_is_macos_darwin(self):
        self.assertTrue(is_macos("Darwin"))

    def test_is_macos_linux(self):
        self.assertFalse(is_macos("Linux"))


class TestCaffeinateCommand(unittest.TestCase):
    def test_command_construction(self):
        cmd = build_caffeinate_command(
            ["python3", "-m", "invariant_engine", "run", "--preset", "smoke"],
            flags="-dimsu",
            caffeinate_bin="/usr/bin/caffeinate",
        )
        self.assertEqual(
            cmd[:4],
            ["/usr/bin/caffeinate", "-dimsu", "--", "python3"],
        )
        self.assertIn("run", cmd)

    def test_missing_caffeinate_detection(self):
        self.assertFalse(caffeinate_exists("/nonexistent/caffeinate"))


class TestBatteryGate(unittest.TestCase):
    def test_refuse_long_run_on_battery(self):
        power = PowerStatus(os_name="Darwin", is_macos=True, on_battery=True)
        refuse, msg = should_refuse_battery_run(
            allow_battery=False, power=power, wall_hours=12.0
        )
        self.assertTrue(refuse)
        self.assertIn("battery", msg.lower())

    def test_allow_battery_override(self):
        power = PowerStatus(os_name="Darwin", is_macos=True, on_battery=True)
        refuse, _ = should_refuse_battery_run(
            allow_battery=True, power=power, wall_hours=12.0
        )
        self.assertFalse(refuse)

    def test_ac_power_ok(self):
        power = PowerStatus(os_name="Darwin", is_macos=True, on_battery=False)
        refuse, _ = should_refuse_battery_run(
            allow_battery=False, power=power, wall_hours=12.0
        )
        self.assertFalse(refuse)

    def test_pmset_parse_battery(self):
        status = detect_battery("Now drawing from 'Battery Power'\n")
        self.assertTrue(status.on_battery)

    def test_pmset_parse_ac(self):
        status = detect_battery("Now drawing from 'AC Power'\n")
        self.assertFalse(status.on_battery)


if __name__ == "__main__":
    unittest.main()
