"""Offline readiness and dashboard asset locality."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from invariant_engine.offline import (  # noqa: E402
    _cdn_assets,
    check_offline,
    enable_offline_mode,
    offline_enabled,
)
from invariant_engine.paths import DASHBOARD_STATIC  # noqa: E402


class TestOffline(unittest.TestCase):
    def test_check_offline_passes(self):
        report = check_offline(min_disk_gb=0.01)
        if not report.ok:
            fails = [c for c in report.checks if not c.ok]
            self.fail(f"Offline checks failed: {fails}")

    def test_no_cdn_in_dashboard(self):
        bad = _cdn_assets(DASHBOARD_STATIC)
        self.assertEqual(bad, [])

    def test_dashboard_files_local(self):
        self.assertTrue((DASHBOARD_STATIC / "index.html").exists())
        self.assertTrue((DASHBOARD_STATIC / "app.js").exists())
        self.assertTrue((DASHBOARD_STATIC / "style.css").exists())
        html = (DASHBOARD_STATIC / "index.html").read_text()
        self.assertNotIn("https://", html)
        self.assertNotIn("http://fonts", html)

    def test_offline_guard_blocks_connect(self):
        enable_offline_mode()
        self.assertTrue(offline_enabled())
        import socket

        with self.assertRaises(RuntimeError):
            s = socket.socket()
            try:
                s.connect(("example.com", 80))
            finally:
                s.close()


if __name__ == "__main__":
    unittest.main()
