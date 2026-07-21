"""Progress schema, atomic writes, checkpoint-on-exit, controls."""

from __future__ import annotations

import json
import os
import signal
import sys
import tempfile
import time
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT))

from invariant_engine.atomic_io import append_jsonl, atomic_write_json  # noqa: E402
from invariant_engine.checkpoint import load_checkpoint, save_checkpoint  # noqa: E402
from invariant_engine.controls import read_control, write_control  # noqa: E402
from invariant_engine.progress import ProgressBus  # noqa: E402


class TestAtomicIO(unittest.TestCase):
    def test_atomic_json_roundtrip(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "x.json"
            atomic_write_json(path, {"a": 1})
            self.assertEqual(json.loads(path.read_text())["a"], 1)

    def test_jsonl_append(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "e.jsonl"
            append_jsonl(path, {"n": 1})
            append_jsonl(path, {"n": 2})
            lines = path.read_text().strip().splitlines()
            self.assertEqual(len(lines), 2)


class TestProgressBus(unittest.TestCase):
    def test_emit_events(self):
        with tempfile.TemporaryDirectory() as td:
            live = Path(td) / "live.json"
            events = Path(td) / "events.jsonl"
            bus = ProgressBus(live_path=live, events_path=events, config={"wall_hours": 0.1})
            bus.state.started_at = time.time()
            bus.set_status("RUNNING")
            bus.emit("RUN_STARTED", "hello", stage="start")
            bus.emit("GRAPH_ENUMERATION_PROGRESS", "shard 1", completed=1, total=2)
            data = json.loads(live.read_text())
            self.assertEqual(data["status"], "RUNNING")
            self.assertTrue(events.exists())
            self.assertGreaterEqual(len(events.read_text().splitlines()), 2)


class TestCheckpoint(unittest.TestCase):
    def test_checkpoint_valid(self):
        with tempfile.TemporaryDirectory() as td:
            import invariant_engine.paths as path_mod

            old = path_mod.CHECKPOINT_DIR
            path_mod.CHECKPOINT_DIR = Path(td)
            try:
                path = save_checkpoint(
                    run_id="abc",
                    stage="test",
                    config={"x": 1},
                    live={"status": "RUNNING"},
                    work={"shard": 1},
                )
                data = load_checkpoint(path)
                self.assertTrue(data["valid"])
                self.assertEqual(data["run_id"], "abc")
            finally:
                path_mod.CHECKPOINT_DIR = old


class TestControls(unittest.TestCase):
    def test_write_read_control(self):
        with tempfile.TemporaryDirectory() as td:
            import invariant_engine.paths as path_mod

            old = path_mod.CONTROL_DIR
            path_mod.CONTROL_DIR = Path(td)
            try:
                write_control("pause", source="test")
                req = read_control()
                self.assertEqual(req["action"], "pause")
            finally:
                path_mod.CONTROL_DIR = old


class TestSignalCheckpoint(unittest.TestCase):
    def test_controller_checkpoints_on_sigterm(self):
        """Install signal handler and ensure force-checkpoint flag is set."""
        from invariant_engine.autonomous import AutonomousController

        with tempfile.TemporaryDirectory() as td:
            # Point state dirs into temp via env is hard; use short wall and mock.
            ctrl = AutonomousController(
                {
                    "wall_hours": 0.0001,
                    "max_degree": 2,
                    "workers": 1,
                    "validate": False,
                    "checkpoint_minutes": 60,
                    "offline": False,
                }
            )
            ctrl.install_signals()
            # Simulate SIGTERM
            os.kill(os.getpid(), 0)  # sanity
            ctrl._stop = False
            handler = signal.getsignal(signal.SIGTERM)
            self.assertTrue(callable(handler))
            # Call handler directly
            handler(signal.SIGTERM, None)  # type: ignore[operator]
            self.assertTrue(ctrl._stop)
            self.assertTrue(ctrl._force_checkpoint)


class TestShellHelpers(unittest.TestCase):
    def test_stale_pid_handling(self):
        import subprocess

        script = ROOT / "scripts" / "lib" / "autonomous_common.sh"
        with tempfile.TemporaryDirectory() as td:
            pid_file = Path(td) / "autonomous.pid"
            pid_file.write_text(
                "PID=99999999\nSTART_TIME=t\nGIT_COMMIT=x\nCONFIGURATION=y\n"
                "LOG_PATH=z\nCHECKPOINT_PATH=c\n"
            )
            bash = (
                f"source '{script}'\n"
                f"PID_FILE='{pid_file}'\n"
                f"remove_stale_pid_file\n"
                f"test ! -f '{pid_file}'\n"
            )
            proc = subprocess.run(["bash", "-c", bash], capture_output=True, text=True)
            self.assertEqual(proc.returncode, 0, proc.stderr + proc.stdout)

    def test_command_construction_flags(self):
        script = ROOT / "scripts" / "lib" / "autonomous_common.sh"
        bash = f"""
        source '{script}'
        is_macos() {{ return 0; }}
        caffeinate_available() {{ return 0; }}
        CAFFEINATE_BIN=/usr/bin/caffeinate
        CAFFEINATE_FLAGS=-dimsu
        wrap_with_caffeinate python3 -m invariant_engine run --preset smoke
        """
        import subprocess

        out = subprocess.check_output(["bash", "-c", bash], text=True)
        self.assertIn("/usr/bin/caffeinate -dimsu -- python3 -m invariant_engine run", out)


if __name__ == "__main__":
    unittest.main()
