"""Fast autonomous controller smoke (no overnight wall time)."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT))


class TestAutonomousSmoke(unittest.TestCase):
    def test_tiny_run_completes_with_checkpoint(self):
        from invariant_engine import autonomous as auto_mod
        from invariant_engine.autonomous import AutonomousController
        from invariant_engine import paths as path_mod

        with tempfile.TemporaryDirectory() as td:
            td_path = Path(td)
            # Redirect research state into temp.
            for attr, name in [
                ("RESEARCH_STATE", ""),
                ("LIVE_PROGRESS", "live_progress.json"),
                ("EVENTS_LOG", "events.jsonl"),
                ("CHECKPOINT_DIR", "checkpoints"),
                ("CONTROL_DIR", "controls"),
                ("LOG_DIR", "logs"),
                ("RUN_META", "run_meta.json"),
                ("PID_FILE", "autonomous.pid"),
            ]:
                if name:
                    setattr(path_mod, attr, td_path / name)
                else:
                    setattr(path_mod, attr, td_path)

            # Also patch modules that imported paths at load time.
            import invariant_engine.progress as prog
            import invariant_engine.checkpoint as cp
            import invariant_engine.controls as ctl

            prog.LIVE_PROGRESS = path_mod.LIVE_PROGRESS
            prog.EVENTS_LOG = path_mod.EVENTS_LOG
            cp.CHECKPOINT_DIR = path_mod.CHECKPOINT_DIR
            ctl.CONTROL_DIR = path_mod.CONTROL_DIR
            auto_mod.LOG_DIR = path_mod.LOG_DIR
            auto_mod.RUN_META = path_mod.RUN_META

            path_mod.ensure_state_dirs()

            ctrl = AutonomousController(
                {
                    "wall_hours": 0.05,  # 3 minutes max; usually finishes sooner
                    "max_degree": 4,
                    "workers": 1,
                    "ram_ceiling_gb": 4,
                    "checkpoint_minutes": 0.01,
                    "validate": True,
                    "checkpoint_resume_test": True,
                    "advance_uncertified": False,
                    "offline": True,
                    "preset": "smoke-test",
                }
            )
            # Skip full hodge1000 for unit speed: mock validation.
            ctrl._run_validation = lambda: None  # type: ignore[method-assign]
            rc = ctrl.run()
            self.assertEqual(rc, 0)
            live = json.loads(path_mod.LIVE_PROGRESS.read_text())
            self.assertIn(live["status"], {"COMPLETE", "STOPPED"})
            self.assertTrue(path_mod.EVENTS_LOG.exists())
            self.assertTrue(any(path_mod.CHECKPOINT_DIR.glob("*_latest.json")))
            self.assertTrue(ctrl.work.get("resume_tested") or live["status"] == "COMPLETE")


class TestPauseResumeControl(unittest.TestCase):
    def test_pause_flag_from_control(self):
        from invariant_engine.autonomous import AutonomousController
        import invariant_engine.paths as path_mod
        from invariant_engine import controls as ctl
        import tempfile

        with tempfile.TemporaryDirectory() as td:
            path_mod.CONTROL_DIR = Path(td)
            ctrl = AutonomousController(
                {
                    "wall_hours": 1,
                    "max_degree": 2,
                    "validate": False,
                    "checkpoint_minutes": 60,
                }
            )
            ctl.write_control("pause")
            ctrl._poll_controls()
            self.assertTrue(ctrl._pause)
            ctl.write_control("resume")
            ctrl._poll_controls()
            self.assertFalse(ctrl._pause)


if __name__ == "__main__":
    unittest.main()
