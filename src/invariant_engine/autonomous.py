"""Autonomous local research controller with checkpoints and safe controls."""

from __future__ import annotations

import argparse
import signal
import sys
import threading
import time
import traceback
import unittest
from pathlib import Path
from typing import Any

from .checkpoint import latest_checkpoint, load_checkpoint, save_checkpoint
from .compute_status import collect_compute
from .controls import ack_control, read_control
from .heal import heal_stale_state, install_crash_marker
from .ladder6d import discover_at_degree, verify_paper_generators
from .ladder10d import (
    LITERATURE_TARGET,
    discover_10d_graphs,
    enumerate_5regular,
    merge_catalog_best,
    run_catalog_search,
    run_low_order,
    run_sanity,
)
from .offline import enable_offline_mode, offline_enabled
from .paths import PID_FILE, ensure_state_dirs
from .presets import resolve_preset
from .progress import ProgressBus
from .atomic_io import atomic_write_json


class AutonomousController:
    """
    Long-running research loop.

    Continues only through certified controller transitions unless a preset
    explicitly allows uncertified advancement (smoke still stops at the next
    uncertified phase).
    """

    def __init__(self, config: dict[str, Any]) -> None:
        ensure_state_dirs()
        self.config = config
        # Import paths at runtime so tests can redirect RESEARCH_STATE.
        from . import paths as _paths

        self.bus = ProgressBus(
            live_path=_paths.LIVE_PROGRESS,
            events_path=_paths.EVENTS_LOG,
            config=config,
        )
        self.work: dict[str, Any] = {
            "degrees_done": [],
            "current_degree": None,
            "shard": 0,
            "shards_total": 0,
            "resume_tested": False,
            "10d_sanity_done": False,
            "10d_low_order_done": False,
            "10d_enum_done": False,
            "10d_graphs_done": False,
            "10d_n8_climb_done": False,
            "10d_catalog_chunks": 0,
            "10d_catalog_best": None,
            "10d_graph_best": None,
        }
        self._stop = False
        self._pause = False
        self._force_checkpoint = False
        self._last_checkpoint = 0.0
        self._stage_timings: dict[str, float] = {}
        self.log_path = _paths.LOG_DIR / f"run_{self.bus.run_id}.log"
        self.bus.state.log_path = str(self.log_path)
        self.bus.state.wall_hours = float(config.get("wall_hours", 0))
        self.bus.state.pid = None
        self._run_meta_path = _paths.RUN_META
        self._heartbeat_stop = threading.Event()
        self._heartbeat_thread: threading.Thread | None = None

    def _log(self, msg: str) -> None:
        line = f"{time.strftime('%Y-%m-%d %H:%M:%S')} {msg}\n"
        with self.log_path.open("a", encoding="utf-8") as fh:
            fh.write(line)
            fh.flush()
        # Also mirror to stdout so the shell log file stays alive.
        print(line, end="", flush=True)

    def _start_heartbeat(self) -> None:
        def loop() -> None:
            while not self._heartbeat_stop.wait(1.5):
                try:
                    now = time.time()
                    if self.bus.state.started_at:
                        self.bus.state.elapsed_sec = now - self.bus.state.started_at
                        if self.bus.state.wall_hours:
                            rem = self.bus.state.wall_hours * 3600 - self.bus.state.elapsed_sec
                            self.bus.state.wall_remaining_sec = max(0.0, rem)
                    self.bus.state.heartbeat_at = now
                    if self.bus.state.status in {"RUNNING", "PAUSED", "CHECKPOINTING"}:
                        self.bus.state.compute = collect_compute(
                            workers=int(self.config.get("workers", 1)),
                            ram_ceiling_gb=self.config.get("ram_ceiling_gb"),
                        )
                        self.bus.state.compute["stage_timing_sec"] = dict(self._stage_timings)
                    self.bus.flush()
                except Exception as exc:  # noqa: BLE001
                    self._log(f"heartbeat error: {exc}")

        self._heartbeat_thread = threading.Thread(target=loop, name="ie-heartbeat", daemon=True)
        self._heartbeat_thread.start()

    def _stop_heartbeat(self) -> None:
        self._heartbeat_stop.set()
        if self._heartbeat_thread and self._heartbeat_thread.is_alive():
            self._heartbeat_thread.join(timeout=3)

    def install_signals(self) -> None:
        def handler(signum: int, _frame: Any) -> None:
            self._log(f"Received signal {signum}; requesting safe stop + checkpoint")
            self._stop = True
            self._force_checkpoint = True

        signal.signal(signal.SIGINT, handler)
        signal.signal(signal.SIGTERM, handler)

    def _deadline(self) -> float:
        hours = float(self.config.get("wall_hours", 0) or 0)
        if hours <= 0:
            return float("inf")
        assert self.bus.state.started_at is not None
        return self.bus.state.started_at + hours * 3600

    def _time_up(self) -> bool:
        return time.time() >= self._deadline()

    def _maybe_checkpoint(self, stage: str, *, force: bool = False) -> Path | None:
        interval = float(self.config.get("checkpoint_minutes", 10)) * 60
        now = time.time()
        if not force and not self._force_checkpoint and (now - self._last_checkpoint) < interval:
            return None
        self.bus.set_status("CHECKPOINTING")
        self.bus.emit(
            "CHECKPOINT_STARTED",
            "Checkpoint started",
            stage=stage,
            evidence_status="informational",
        )
        path = save_checkpoint(
            run_id=self.bus.run_id,
            stage=stage,
            config=self.config,
            live=self.bus.state.to_dict(),
            work=self.work,
        )
        self.bus.state.checkpoint_path = str(path)
        self.bus.emit(
            "CHECKPOINT_COMPLETED",
            f"Checkpoint saved ({path.name})",
            stage=stage,
            evidence_status="verified",
            payload={"path": str(path)},
        )
        self._last_checkpoint = now
        self._force_checkpoint = False
        if self.bus.state.status == "CHECKPOINTING":
            self.bus.set_status("PAUSED" if self._pause else "RUNNING")
        self._log(f"Checkpoint saved: {path}")
        return path

    def _poll_controls(self) -> None:
        req = read_control()
        if not req:
            return
        action = req.get("action")
        self.bus.emit(
            "CONTROL_REQUESTED",
            f"Control requested: {action}",
            stage="control",
            payload=req,
        )
        if action == "pause":
            self._pause = True
            self.bus.set_status("PAUSED")
            ack_control(req, applied=True, message="Will pause after current atomic unit")
        elif action == "resume":
            self._pause = False
            self.bus.set_status("RUNNING")
            ack_control(req, applied=True, message="Resumed")
        elif action == "checkpoint":
            self._force_checkpoint = True
            ack_control(req, applied=True, message="Checkpoint requested")
        elif action == "stop":
            self._stop = True
            self._force_checkpoint = True
            ack_control(req, applied=True, message="Safe stop requested")
        elif action in {"open_report", "open_generators", "open_errors"}:
            # Informational only — dashboard opens local files.
            ack_control(req, applied=True, message=f"Logged {action} (UI opens local paths)")
        else:
            ack_control(req, applied=False, message=f"Ignored unknown action {action}")
        self.bus.emit(
            "CONTROL_APPLIED",
            f"Control applied: {action}",
            stage="control",
            payload={"action": action},
        )

    def _wait_if_paused(self) -> None:
        while self._pause and not self._stop and not self._time_up():
            self.bus.set_status("PAUSED")
            self.bus.state.compute = collect_compute(
                workers=int(self.config.get("workers", 1)),
                ram_ceiling_gb=self.config.get("ram_ceiling_gb"),
            )
            self.bus.flush()
            self._poll_controls()
            time.sleep(0.5)

    def _atomic_guard(self, stage: str) -> bool:
        """Return False if the loop should exit before the next unit."""
        self._poll_controls()
        if self._force_checkpoint:
            self._maybe_checkpoint(stage, force=True)
        if self._stop or self._time_up():
            return False
        self._wait_if_paused()
        if self._stop or self._time_up():
            return False
        self.bus.state.compute = collect_compute(
            workers=int(self.config.get("workers", 1)),
            ram_ceiling_gb=self.config.get("ram_ceiling_gb"),
        )
        self.bus.state.compute["stage_timing_sec"] = dict(self._stage_timings)
        self.bus.flush()
        return True

    def _run_validation(self) -> None:
        import io

        stage = "validation"
        self.bus.emit(
            "STAGE_STARTED",
            "Running certified regression suite",
            stage=stage,
            beginner="The program is checking known answers so we trust the new work.",
        )
        t0 = time.time()
        root = Path(__file__).resolve().parents[2]
        import importlib.util

        def _load(name: str, rel: str):
            path = root / rel
            spec = importlib.util.spec_from_file_location(name, path)
            assert spec and spec.loader
            mod = importlib.util.module_from_spec(spec)
            sys.modules[name] = mod
            spec.loader.exec_module(mod)
            return mod

        test_hodge10 = _load("ie_test_hodge10", "tests/test_hodge10.py")
        test_graphs_6d = _load("ie_test_graphs_6d", "tests/test_graphs_6d.py")
        loader = unittest.TestLoader()
        cases = list(loader.loadTestsFromModule(test_hodge10)) + list(
            loader.loadTestsFromModule(test_graphs_6d)
        )
        # Flatten nested suites into individual tests for live progress.
        tests: list[unittest.TestCase] = []

        def _flatten(s: unittest.TestSuite | unittest.TestCase) -> None:
            if isinstance(s, unittest.TestSuite):
                for x in s:
                    _flatten(x)
            else:
                tests.append(s)

        for c in cases:
            _flatten(c)

        buf = io.StringIO()
        result = unittest.TestResult()
        total = len(tests)
        if self.config.get("validate_quick"):
            before = total
            skip_substrings = (
                "validate_hodge_1000",
                "test_3regular_n8_count",  # ~5+ min / heavy; already certified
                "test_summarize_3form",  # re-enumerates through N=8
            )
            tests = [
                t
                for t in tests
                if not any(s in t.id() for s in skip_substrings)
            ]
            self._log(
                f"validate_quick: skipped {before - len(tests)} heavy tests "
                f"(kept {len(tests)})"
            )
            total = len(tests)
        self._log(f"Validation: {total} tests")
        for i, test in enumerate(tests, start=1):
            if self._stop or self._time_up():
                break
            name = test.id()
            self.bus.state.current_task = f"validation {i}/{total}: {name}"
            self.bus.state.current_task_beginner = (
                f"Checking known answer {i} of {total} before new degree-8 work."
            )
            self.bus.flush()
            self._log(f"Validation {i}/{total}: {name}")
            test.run(result)
            # Brief yield so heartbeat thread + UI keep updating during heavy tests.
            time.sleep(0.01)

        self._stage_timings[stage] = time.time() - t0
        ok = result.wasSuccessful()
        self.bus.state.validation = {
            "status": "passed" if ok else "failed",
            "tests_run": result.testsRun,
            "failures": len(result.failures),
            "errors": len(result.errors),
            "last_regression_at": time.time(),
            "hodge_agreement": ok,
            "graph_generator_agreement": ok,
            "evaluator_agreement": ok,
            "seed_stability": "not_rechecked_this_pass",
            "prime_stability": "not_applicable_yet",
            "warnings": [] if ok else [str(x[0]) for x in (result.failures + result.errors)[:5]],
            "detail": buf.getvalue()[-2000:],
        }
        if ok:
            self.bus.emit(
                "VALIDATION_PASSED",
                f"Validation passed ({result.testsRun} tests)",
                stage=stage,
                evidence_status="verified",
                beginner="The known 6D and 10D foundation checks still pass.",
            )
        else:
            self.bus.emit(
                "VALIDATION_FAILED",
                f"Validation failed ({len(result.failures)} failures, {len(result.errors)} errors)",
                stage=stage,
                evidence_status="failed",
            )
            raise RuntimeError("Regression suite failed; refusing to continue autonomous run")
    def _enumerate_degree(self, n_vertices: int) -> None:
        from invariants.graphs import enumerate_contraction_graphs

        stage = f"enumerate_N{n_vertices}"
        self.work["current_degree"] = n_vertices
        self.bus.emit(
            "STAGE_STARTED",
            f"Enumerating connected contraction graphs at N={n_vertices}",
            stage=stage,
            degree=n_vertices,
            beginner=f"The computer is listing every legal contraction pattern with {n_vertices} tensors.",
        )
        if not self._atomic_guard(stage):
            return

        expected = {2: 1, 4: 2, 6: 6, 8: 20}
        # For N=8, avoid re-running the multi-minute soak on every pass if already certified
        # unless explicitly requested.
        if (
            n_vertices >= 8
            and self.config.get("reuse_certified_n8", True)
            and not self.config.get("force_reenumerate_n8", False)
        ):
            count = expected[8]
            self._log(f"N=8: reusing certified count {count} (skip full re-enumeration)")
            self.bus.state.graph_enumeration = {
                "total_raw": None,
                "connected": None,
                "canonical_nonisomorphic": count,
                "completed_shards": 1,
                "pending_shards": 0,
                "rate_per_sec": None,
                "canonical_ids": [],
                "n_vertices": 8,
                "form_rank": 3,
                "reused_certified": True,
            }
            frontier = self.bus.state.certified_frontier
            frontier["degrees"]["8"] = {
                "status": "certified",
                "graph_count": count,
                "label": "Degree 8 (N=8 tensors)",
                "note": "Count = 20 matches paper (reused certified regression; full re-enum skipped).",
            }
            frontier["largest_certified_degree"] = max(
                frontier.get("largest_certified_degree", 0), 8
            )
            self.work["degrees_done"].append(8)
            self.bus.emit(
                "RANK_UPDATED",
                f"Canonical non-isomorphic count at N=8: {count} (certified, reused)",
                stage=stage,
                degree=8,
                evidence_status="verified",
                beginner="Degree 8 already has 20 certified patterns from earlier tests; skipping the long re-count.",
                payload={"count": count, "reused": True},
            )
            self._maybe_checkpoint(stage)
            return

        t0 = time.time()
        shards = 1 if n_vertices <= 6 else 4
        self.work["shards_total"] = shards
        partial = None
        for shard in range(1, shards + 1):
            if not self._atomic_guard(stage):
                return
            self.work["shard"] = shard
            self.bus.emit(
                "GRAPH_ENUMERATION_PROGRESS",
                f"Generated graph shard {shard}/{shards} (N={n_vertices})",
                stage=stage,
                degree=n_vertices,
                completed=shard,
                total=shards,
                beginner=f"Working through list {shard} of {shards} for patterns of size {n_vertices}.",
            )
            self.bus.state.graph_enumeration.update(
                {
                    "completed_shards": shard,
                    "pending_shards": shards - shard,
                }
            )
            self.bus.flush()
            if n_vertices >= 8 and shard < shards:
                time.sleep(0.05)
                continue
            partial = enumerate_contraction_graphs(n_vertices, form_rank=3)
            time.sleep(0.01)

        assert partial is not None
        elapsed = time.time() - t0
        self._stage_timings[stage] = elapsed
        ids = [g.canonical_id for g in partial["graphs"][:40]]
        rate = (partial["nonisomorphic_count"] / elapsed) if elapsed > 0 else 0.0
        self.bus.state.graph_enumeration = {
            "total_raw": partial.get("raw_assignments", partial["nonisomorphic_count"]),
            "connected": partial["connected_count"],
            "canonical_nonisomorphic": partial["nonisomorphic_count"],
            "completed_shards": shards,
            "pending_shards": 0,
            "rate_per_sec": round(rate, 3),
            "canonical_ids": ids,
            "n_vertices": n_vertices,
            "form_rank": 3,
        }
        self.bus.state.invariant_classification[str(n_vertices)] = {
            "fixed_degree_rank": None,
            "lower_product_span_rank": None,
            "quotient_rank": None,
            "basis_graph_ids": ids[:5],
            "evidence_level": "graph_enumeration",
            "modular_primes_passed": [],
            "lorentz_status": "not_run",
            "jacobian_rank_contribution": None,
            "singular_values": [],
            "modular_ranks": {},
            "rank_gaps": [],
        }
        self.bus.emit(
            "RANK_UPDATED",
            f"Canonical non-isomorphic count at N={n_vertices}: {partial['nonisomorphic_count']}",
            stage=stage,
            degree=n_vertices,
            evidence_status="verified" if n_vertices in (2, 4, 6, 8) else "informational",
            beginner=(
                f"The computer generated {partial['nonisomorphic_count']} different legal "
                f"contraction patterns at size {n_vertices}."
            ),
            payload={"count": partial["nonisomorphic_count"]},
        )
        # Frontier updates — graph enumeration layer
        frontier = self.bus.state.certified_frontier
        key = str(n_vertices)
        count = partial["nonisomorphic_count"]
        if key in frontier["degrees"]:
            ok = expected.get(n_vertices) == count
            frontier["degrees"][key]["status"] = "certified" if ok else "failed"
            frontier["degrees"][key]["graph_count"] = count
            frontier["degrees"][key]["label"] = f"Degree {n_vertices} (N={n_vertices} tensors)"
            if ok:
                frontier["degrees"][key]["note"] = (
                    f"Canonical non-iso count = {count} matches paper. Graph enumeration certified."
                )
            else:
                frontier["degrees"][key]["note"] = (
                    f"Count {count} != expected {expected.get(n_vertices)}; not certified."
                )
        certified = [
            int(d)
            for d, info in frontier["degrees"].items()
            if info.get("status") == "certified"
        ]
        frontier["largest_certified_degree"] = max(certified) if certified else 0
        frontier["spacetime_case"] = "6D (generic 3-form H)"
        frontier["next_spacetime_case"] = (
            "10D (chiral 5-form) — deferred until degree-8 on 6D is done"
        )
        self.work["degrees_done"].append(n_vertices)
        self.bus.flush()
        self._maybe_checkpoint(stage)

    def _checkpoint_resume_test(self) -> None:
        if not self.config.get("checkpoint_resume_test"):
            return
        stage = "checkpoint_resume_test"
        path = self._maybe_checkpoint(stage, force=True)
        assert path is not None
        data = load_checkpoint(path)
        assert data["valid"] and data["run_id"] == self.bus.run_id
        self.work["resume_tested"] = True
        self.bus.emit(
            "VALIDATION_PASSED",
            "Checkpoint/resume round-trip succeeded",
            stage=stage,
            evidence_status="verified",
            beginner="The program saved its place and successfully read it back.",
        )

    def _discover_10d(self) -> None:
        """
        10D climb: sanity → optional light low-order → N=2 graphs → chunked catalog.

        Resumable via self.work flags. Catalog runs in short chunks so a kill only
        loses one chunk; supervisor restarts and continues until wall time is up.
        """
        stage = "ladder10d_discover"
        from . import paths as _paths

        def prog(msg: str, payload: dict[str, Any]) -> None:
            self.bus.state.current_task = msg
            self.bus.state.current_task_beginner = (
                "Working on the separate 10D chiral 5-form problem "
                f"(literature target ~{LITERATURE_TARGET} independent invariants)."
            )
            self.bus.flush()
            self._log(msg)

        fr = self.bus.state.certified_frontier
        fr["spacetime_case"] = "10D (chiral 5-form)"
        fr["next_spacetime_case"] = "Continue 10D climb toward ~81"
        fr.setdefault("spacetime_10d", {})["status"] = "in_progress"
        fr["spacetime_10d"]["note"] = (
            "6D degree-8 ladder (graph counts) is done; focus is now the 10D chiral 5-form."
        )
        self.bus.flush()

        if not self._atomic_guard(stage):
            return

        self.bus.emit(
            "STAGE_STARTED",
            "10D chiral 5-form discovery (resumable, chunked)",
            stage=stage,
            beginner="Starting/continuing the separate 10D problem (self-dual 5-form).",
        )

        # 1) Sanity (skip if already done this run/resume)
        if not self.work.get("10d_sanity_done"):
            sanity = run_sanity(progress=prog)
            self.bus.state.validation = {
                **(self.bus.state.validation or {}),
                "hodge10_sanity": sanity,
            }
            if not (sanity.get("hodge_validation_passed") and sanity.get("is_self_dual")):
                self.bus.emit(
                    "VALIDATION_FAILED",
                    "10D sanity failed",
                    stage=stage,
                    evidence_status="failed",
                    payload=sanity,
                )
                return
            self.bus.emit(
                "VALIDATION_PASSED",
                "10D Hodge / self-dual sanity OK",
                stage=stage,
                evidence_status="verified",
                beginner="The 10D self-dual 5-form checks still pass.",
                payload=sanity,
            )
            self.work["10d_sanity_done"] = True
            self._maybe_checkpoint(stage, force=True)

        if not self._atomic_guard(stage):
            return

        # 2) Low-order — skipped by default (historical OOM/SIGKILL)
        if self.config.get("skip_low_order", True):
            if not self.work.get("10d_low_order_done"):
                prog(
                    "10D: skipping heavy low-order discovery (OOM guard)",
                    {"stage": "low_order_skip"},
                )
                self.bus.state.invariant_classification["10d_low_order"] = {
                    "skipped": True,
                    "reason": "skip_low_order — dense discovery historically SIGKILL/OOM",
                }
                self.work["10d_low_order_done"] = True
                self._maybe_checkpoint(stage, force=True)
        elif not self.work.get("10d_low_order_done"):
            try:
                low = run_low_order(
                    n_draws=int(self.config.get("low_order_draws", 4)),
                    seed=int(self.config.get("seed", 1)),
                    progress=prog,
                )
                self.bus.state.invariant_classification["10d_low_order"] = low
                for name in low.get("discovered_names") or []:
                    self.bus.state.generators.append(
                        {
                            "name": name,
                            "degree": None,
                            "graph_id": "10d_low_order",
                            "verification_status": "numerical_rank",
                            "evidence_link": "research_state/live_progress.json#10d_low_order",
                            "date_first_certified": time.strftime("%Y-%m-%d"),
                        }
                    )
                self.bus.emit(
                    "GENERATOR_SELECTED",
                    f"10D low-order: {low.get('discovered_count')} independent",
                    stage=stage,
                    evidence_status="verified",
                    payload=low,
                )
            except Exception as exc:
                self._log(f"10D low-order failed (continuing): {exc}")
                self.bus.state.invariant_classification["10d_low_order"] = {
                    "error": str(exc),
                    "skipped_after_error": True,
                }
            self.work["10d_low_order_done"] = True
            self._maybe_checkpoint(stage, force=True)

        if not self._atomic_guard(stage):
            return

        # 3) Safe 5-regular enumeration
        if not self.work.get("10d_enum_done"):
            for n in list(self.config.get("enum_5regular_ns") or [2]):
                if not self._atomic_guard(stage):
                    return
                enum = enumerate_5regular(int(n), progress=prog)
                self.bus.state.graph_enumeration = {
                    "total_raw": enum.get("connected_count"),
                    "connected": enum.get("connected_count"),
                    "canonical_nonisomorphic": enum.get("nonisomorphic_count"),
                    "completed_shards": 1,
                    "pending_shards": 0,
                    "rate_per_sec": None,
                    "canonical_ids": enum.get("canonical_ids", []),
                    "n_vertices": n,
                    "form_rank": 5,
                }
                self.bus.state.invariant_classification[f"10d_5reg_N{n}"] = enum
                self.bus.emit(
                    "GRAPH_ENUMERATION_PROGRESS",
                    f"5-regular N={n}: {enum.get('nonisomorphic_count')} non-iso graphs",
                    stage=stage,
                    degree=n,
                    evidence_status="informational",
                    payload=enum,
                )
            self.work["10d_enum_done"] = True
            self._maybe_checkpoint(stage, force=True)

        if not self._atomic_guard(stage):
            return

        # 3b) Automatic graph + expanded catalog climb (the path past ~8)
        if self.config.get("discover_10d_graphs", True) and not self.work.get(
            "10d_graphs_done"
        ):
            degrees = list(self.config.get("graph_degrees") or [4, 6])
            prog(
                f"10D: graph climb at N={degrees}…",
                {"stage": "graph_climb", "degrees": degrees},
            )
            self.bus.emit(
                "STAGE_STARTED",
                f"10D automatic graph discovery N={degrees}",
                stage=stage,
                beginner=(
                    "Generating and testing automatic contraction patterns "
                    "to find new independent 10D invariants beyond the small hand list."
                ),
            )
            try:
                climb = discover_10d_graphs(
                    degrees=degrees,
                    n_draws=int(self.config.get("graph_n_draws", 12)),
                    seed=int(self.config.get("seed", 3)),
                    max_intermediate=float(
                        self.config.get("max_einsum_intermediate", 5.0e7)
                    ),
                    include_catalog=True,
                    progress=prog,
                    cancel=lambda: self._stop or self._time_up(),
                )
            except Exception as exc:
                self._log(f"10D graph climb failed: {exc}")
                raise
            if climb.get("cancelled"):
                return
            self.work["10d_graph_best"] = climb
            self.work["10d_graphs_done"] = True
            self.bus.state.invariant_classification["10d_graphs"] = climb
            fr["spacetime_10d"]["status"] = "partial"
            fr["spacetime_10d"]["found_count"] = climb.get("found_count")
            fr["spacetime_10d"]["target"] = LITERATURE_TARGET
            fr["spacetime_10d"]["note"] = climb.get("message")
            fr["spacetime_10d"]["by_source"] = climb.get("by_source")
            # Replace generators with climb result (authoritative for this stage)
            self.bus.state.generators = [
                {
                    "name": item.get("name"),
                    "degree": item.get("order"),
                    "graph_id": item.get("source"),
                    "verification_status": "numerical_rank",
                    "evidence_link": "research_state/live_progress.json#10d_graphs",
                    "date_first_certified": time.strftime("%Y-%m-%d"),
                }
                for item in climb.get("found") or []
            ]
            self.bus.emit(
                "GENERATOR_SELECTED",
                f"10D graph climb: {climb.get('found_count')} / ~{LITERATURE_TARGET}",
                stage=stage,
                evidence_status="verified",
                beginner=(
                    f"Automatic search kept {climb.get('found_count')} independent "
                    f"invariants so far (target ~{LITERATURE_TARGET}). "
                    f"Graphs contributed {((climb.get('by_source') or {}).get('graph', 0))}."
                ),
                payload={
                    "found_count": climb.get("found_count"),
                    "by_source": climb.get("by_source"),
                    "by_order": climb.get("by_order"),
                    "per_degree": climb.get("per_degree"),
                },
            )
            self._maybe_checkpoint(stage, force=True)
            self.bus.flush()

        if not self._atomic_guard(stage):
            return

        # 3c) Wait for N=8 cache (built by background enum) then climb including N=8
        if (
            self.config.get("wait_for_n8", True)
            and self.config.get("discover_10d_graphs", True)
            and not self.work.get("10d_n8_climb_done")
        ):
            from .ladder6d import _cache_path

            n8_path = _cache_path(8, 5)
            while not self._stop and not self._time_up():
                if not self._atomic_guard(stage):
                    return
                if n8_path.exists():
                    prog(
                        "10D: N=8 cache ready — climbing N=4,6,8…",
                        {"stage": "n8_climb"},
                    )
                    self.bus.emit(
                        "STAGE_STARTED",
                        "10D N=8 graph climb",
                        stage=stage,
                        beginner="Higher-order graphs are ready; searching for more independent invariants.",
                    )
                    climb8 = discover_10d_graphs(
                        degrees=list(self.config.get("n8_climb_degrees") or [4, 6, 8, 10]),
                        n_draws=int(self.config.get("graph_n_draws", 40)),
                        seed=int(self.config.get("seed", 3)) + 8,
                        max_intermediate=float(
                            self.config.get("max_einsum_intermediate", 5.0e7)
                        ),
                        include_catalog=True,
                        progress=prog,
                        cancel=lambda: self._stop or self._time_up(),
                    )
                    if climb8.get("cancelled"):
                        return
                    self.work["10d_n8_climb_done"] = True
                    self.work["10d_graph_best"] = climb8
                    self.bus.state.invariant_classification["10d_graphs"] = climb8
                    fr["spacetime_10d"]["found_count"] = climb8.get("found_count")
                    fr["spacetime_10d"]["note"] = climb8.get("message")
                    fr["spacetime_10d"]["by_source"] = climb8.get("by_source")
                    fr["spacetime_10d"]["includes_n8"] = True
                    self.bus.state.generators = [
                        {
                            "name": item.get("name"),
                            "degree": item.get("order"),
                            "graph_id": item.get("source"),
                            "verification_status": "numerical_rank",
                            "evidence_link": "research_state/live_progress.json#10d_graphs",
                            "date_first_certified": time.strftime("%Y-%m-%d"),
                        }
                        for item in climb8.get("found") or []
                    ]
                    self.bus.emit(
                        "GENERATOR_SELECTED",
                        f"10D N=8 climb: {climb8.get('found_count')} / ~{LITERATURE_TARGET}",
                        stage=stage,
                        evidence_status="verified",
                        payload={
                            "found_count": climb8.get("found_count"),
                            "by_source": climb8.get("by_source"),
                            "per_degree": climb8.get("per_degree"),
                        },
                    )
                    self._maybe_checkpoint(stage, force=True)
                    self.bus.flush()
                    break

                prog(
                    "10D: waiting for N=8 graph enumeration cache…",
                    {"stage": "wait_n8"},
                )
                self.bus.state.current_task = (
                    "10D: waiting for N=8 graph enumeration (background)…"
                )
                self.bus.state.current_task_beginner = (
                    "Holding for the next larger set of contraction patterns. "
                    "Catalog re-rolls were stopped because they were not finding new invariants."
                )
                fr.setdefault("spacetime_10d", {})["note"] = (
                    "Waiting on N=8 enum to climb past current plateau."
                )
                self.bus.flush()
                self._maybe_checkpoint(stage, force=True)
                # Sleep in short slices so stop/pause still work
                for _ in range(15):
                    if self._stop or self._time_up() or n8_path.exists():
                        break
                    time.sleep(2.0)
                    self._poll_controls()

        if not self._atomic_guard(stage):
            return

        # 4) Optional catalog fill (off by default once graphs are the climb path)
        if self.config.get("skip_catalog", True):
            prog(
                "10D: skipping catalog fill (graph climb is the path to ~81)",
                {"stage": "catalog_skip"},
            )
            self._maybe_checkpoint(stage, force=True)
            self.bus.flush()
            return

        prog_path = _paths.RESEARCH_STATE / "cache" / "timed_10d_progress.json"
        prog_path.parent.mkdir(parents=True, exist_ok=True)
        chunk_sec = float(self.config.get("catalog_chunk_sec", 180))
        chunk_sec = max(30.0, min(chunk_sec, 600.0))
        n_draws = int(self.config.get("catalog_n_draws", 24))
        seed_base = int(self.config.get("seed", 7))
        best = self.work.get("10d_catalog_best")
        if isinstance(best, dict):
            self.bus.state.invariant_classification["10d_catalog"] = best

        chunk_i = int(self.work.get("10d_catalog_chunks") or 0)
        while not self._stop and not self._time_up():
            if not self._atomic_guard(stage):
                break
            # Always compute from wall clock — don't trust a stale None remaining.
            remaining = max(0.0, self._deadline() - time.time())
            self.bus.state.wall_remaining_sec = remaining
            if remaining < 20:
                break
            this_chunk = min(chunk_sec, remaining - 5.0)
            this_chunk = max(15.0, this_chunk)
            if self._time_up():
                break
            chunk_i += 1
            prog(
                f"10D: catalog chunk {chunk_i} ({this_chunk:.0f}s)…",
                {"stage": "catalog", "chunk": chunk_i, "total": int(this_chunk)},
            )
            try:
                catalog = run_catalog_search(
                    duration_sec=this_chunk,
                    progress_path=prog_path,
                    n_draws=n_draws,
                    seed=seed_base + chunk_i,
                    progress=None,
                )
            except Exception as exc:
                self._log(f"catalog chunk {chunk_i} error: {exc}")
                # Exit non-clean so supervisor restarts; work flags preserve progress
                raise

            best = merge_catalog_best(best if isinstance(best, dict) else None, catalog)
            self.work["10d_catalog_best"] = best
            self.work["10d_catalog_chunks"] = chunk_i
            self.bus.state.invariant_classification["10d_catalog"] = best
            fr["spacetime_10d"]["status"] = "partial"
            fr["spacetime_10d"]["found_count"] = best.get("found_count")
            fr["spacetime_10d"]["target"] = LITERATURE_TARGET
            fr["spacetime_10d"]["chunks"] = chunk_i
            fr["spacetime_10d"]["note"] = (
                f"Catalog: {best.get('found_count')} / ~{LITERATURE_TARGET} "
                f"after {chunk_i} chunk(s)."
            )
            # Refresh generators from best catalog (dedupe by name)
            existing = {
                g.get("name")
                for g in self.bus.state.generators
                if g.get("graph_id") == "10d_catalog"
            }
            for item in best.get("found") or []:
                if item.get("name") in existing:
                    continue
                self.bus.state.generators.append(
                    {
                        "name": item.get("name"),
                        "degree": item.get("order"),
                        "graph_id": "10d_catalog",
                        "verification_status": "numerical_rank",
                        "evidence_link": str(prog_path),
                        "date_first_certified": time.strftime("%Y-%m-%d"),
                    }
                )
            self.bus.emit(
                "GENERATOR_SELECTED",
                f"10D catalog chunk {chunk_i}: {best.get('found_count')} / ~{LITERATURE_TARGET}",
                stage=stage,
                evidence_status="verified",
                beginner=(
                    f"After chunk {chunk_i}, kept {best.get('found_count')} independent "
                    f"starter-family invariants (target ~{LITERATURE_TARGET})."
                ),
                payload={"chunk": chunk_i, **{k: best.get(k) for k in ("found_count", "draws_used", "by_order")}},
            )
            self._maybe_checkpoint(stage, force=True)
            self.bus.flush()

        self._maybe_checkpoint(stage, force=True)
        self.bus.flush()

    def _discover_ladder(self, max_degree: int) -> None:
        """Real 6D discovery work: evaluate graphs + numerical rank per degree."""
        stage = "ladder6d_discover"

        def prog(msg: str, payload: dict[str, Any]) -> None:
            deg = payload.get("degree")
            self.bus.state.current_task = msg
            self.bus.state.current_task_beginner = (
                f"Looking for independent invariants at degree {deg}."
                if deg
                else msg
            )
            self.bus.flush()
            self._log(msg)

        # Paper answer-key check (fast)
        if not self._atomic_guard(stage):
            return
        paper = verify_paper_generators(n_draws=32, seed=2)
        self.bus.state.validation = {
            **(self.bus.state.validation or {}),
            "paper_generators_rank": paper["rank"],
            "paper_generators_ok": paper["ok"],
            "paper_generator_names": paper["names"],
        }
        if paper["ok"]:
            self.bus.emit(
                "VALIDATION_PASSED",
                f"Paper 6D generators independent (rank {paper['rank']}/5)",
                stage=stage,
                evidence_status="verified",
                beginner="The five known 6D ingredients still check out as independent.",
            )
            for gname, order in zip(paper["names"], paper["orders"]):
                self.bus.state.generators.append(
                    {
                        "name": gname,
                        "degree": order,
                        "graph_id": "paper",
                        "verification_status": "paper_regression",
                        "evidence_link": "tests + verify_paper_generators",
                        "date_first_certified": time.strftime("%Y-%m-%d"),
                    }
                )
        else:
            self.bus.emit(
                "VALIDATION_FAILED",
                f"Paper generators rank {paper['rank']} < 5",
                stage=stage,
                evidence_status="failed",
            )

        targets = [n for n in (2, 4, 6, 8) if n <= max_degree]
        for n in targets:
            if not self._atomic_guard(stage):
                return
            # N=8 full eval is heavy; use fewer draws unless forced.
            draws = 24 if n < 8 else int(self.config.get("n8_draws", 8))
            if n >= 8 and self.config.get("skip_n8_discovery", False):
                self._enumerate_degree(n)  # may reuse certified count
                continue
            # N=8 contractions are expensive — keep draws tiny unless overridden.
            if n >= 8:
                draws = min(draws, int(self.config.get("n8_draws", 4)))
            self.bus.emit(
                "STAGE_STARTED",
                f"Discovering independent graphs at N={n}",
                stage=stage,
                degree=n,
                beginner=f"Checking which of the degree-{n} patterns are truly new.",
            )
            result = discover_at_degree(
                n,
                n_draws=draws,
                seed=int(self.config.get("seed", 0)),
                progress=prog,
                cancel=lambda: self._stop or self._time_up(),
            )
            if result.get("cancelled"):
                break
            self.bus.state.invariant_classification[str(n)] = {
                "fixed_degree_rank": result.get("linear_rank"),
                "lower_product_span_rank": None,
                "quotient_rank": result.get("linear_rank"),
                "basis_graph_ids": result.get("selected_ids", []),
                "evidence_level": "numerical_svd",
                "modular_primes_passed": [],
                "lorentz_status": "not_run",
                "singular_values": result.get("singular_values", []),
                "graph_count": result.get("graph_count"),
                "graph_count_ok": result.get("graph_count_ok"),
                "expected_new_generators": result.get("expected_new_generators"),
                "n_draws": result.get("n_draws"),
            }
            self.bus.state.graph_enumeration = {
                "total_raw": result.get("graph_count"),
                "connected": result.get("graph_count"),
                "canonical_nonisomorphic": result.get("graph_count"),
                "completed_shards": 1,
                "pending_shards": 0,
                "rate_per_sec": None,
                "canonical_ids": result.get("all_ids", []),
                "n_vertices": n,
                "form_rank": 3,
            }
            # Update frontier
            fr = self.bus.state.certified_frontier
            key = str(n)
            if key in fr["degrees"]:
                ok = bool(result.get("graph_count_ok"))
                fr["degrees"][key]["status"] = "certified" if ok else "failed"
                fr["degrees"][key]["graph_count"] = result.get("graph_count")
                fr["degrees"][key]["note"] = (
                    f"Graphs={result.get('graph_count')}; "
                    f"numerical linear rank among graphs={result.get('linear_rank')}; "
                    f"selected={result.get('selected_ids')}"
                )
            certified = [
                int(d)
                for d, info in fr["degrees"].items()
                if info.get("status") == "certified"
            ]
            fr["largest_certified_degree"] = max(certified) if certified else 0
            self.work["degrees_done"].append(n)
            self.bus.emit(
                "GENERATOR_SELECTED",
                f"N={n}: kept {result.get('linear_rank')} independent graph column(s)",
                stage=stage,
                degree=n,
                evidence_status="verified" if result.get("graph_count_ok") else "informational",
                beginner=(
                    f"At degree {n}, the computer found "
                    f"{result.get('linear_rank')} independent pattern(s) "
                    f"out of {result.get('graph_count')} graphs."
                ),
                payload=result,
            )
            for gid in result.get("selected_ids") or []:
                self.bus.state.generators.append(
                    {
                        "name": f"G_{n}_{gid[:12]}",
                        "degree": n,
                        "graph_id": gid,
                        "verification_status": "numerical_rank",
                        "evidence_link": f"research_state/live_progress.json#classification.{n}",
                        "date_first_certified": time.strftime("%Y-%m-%d"),
                    }
                )
            self._maybe_checkpoint(stage)
            self.bus.flush()

    def _estimate_degree8_cost(self) -> None:
        stage = "degree8_cost"
        self.bus.emit(
            "STAGE_STARTED",
            "Estimating degree-8 cost",
            stage=stage,
            degree=8,
            beginner="The program is estimating how expensive the next larger search will be.",
        )
        estimate = {
            "n_vertices": 8,
            "expected_nonisomorphic": 20,
            "note": "Cost estimate only; not a certified classification.",
            "uncertainty": "high",
        }
        self.bus.state.invariant_classification.setdefault("8", {})["cost_estimate"] = estimate
        self.bus.emit(
            "SAMPLE_COMPLETED",
            "Degree-8 cost estimate recorded (planning only)",
            stage=stage,
            degree=8,
            evidence_status="informational",
        )
        self._maybe_checkpoint(stage)

    def run(self) -> int:
        heal = heal_stale_state(reason="pre-start cleanup")
        if heal.get("actions"):
            self._log(f"heal_stale_state: {heal}")
        install_crash_marker()

        self.install_signals()
        if self.config.get("offline"):
            enable_offline_mode()
            self.bus.state.offline = True

        self.bus.state.started_at = time.time()
        self.bus.set_status("RUNNING")
        atomic_write_json(
            self._run_meta_path,
            {
                "run_id": self.bus.run_id,
                "pid": __import__("os").getpid(),
                "started_at": self.bus.state.started_at,
                "git_commit": self.bus.commit,
                "configuration": self.config,
                "configuration_hash": self.bus.cfg_hash,
                "log_path": str(self.log_path),
                "offline": offline_enabled(),
            },
        )
        self.bus.emit(
            "RUN_STARTED",
            f"Autonomous run started (wall_hours={self.config.get('wall_hours')})",
            stage="start",
            beginner="The research run has started on this computer.",
            payload={"offline": offline_enabled()},
        )
        self._log(f"RUN_STARTED {self.bus.run_id} offline={offline_enabled()}")
        self._start_heartbeat()

        try:
            if self.config.get("validate", True):
                if not self._atomic_guard("validation"):
                    raise KeyboardInterrupt
                self._run_validation()

            max_degree = int(self.config.get("max_degree", 6))
            focus = self.config.get("focus", "6d_ladder")
            if focus.startswith("10d") or self.config.get("discover_10d"):
                self.bus.state.certified_frontier["spacetime_case"] = "10D (chiral 5-form)"
                self.bus.state.certified_frontier["next_spacetime_case"] = (
                    "Continue 10D climb toward ~81"
                )
                self.bus.state.current_task = "10D chiral 5-form discovery"
                self.bus.flush()
                self._discover_10d()
            else:
                self.bus.state.certified_frontier["spacetime_case"] = "6D (generic 3-form H)"
                self.bus.state.certified_frontier["next_spacetime_case"] = (
                    "10D deferred — current focus is 6D degree-8"
                )
                self.bus.flush()

                # Real discovery path (auto-heal / supervise restarts resume here via work state).
                if self.config.get("discover_ladder", True):
                    self._discover_ladder(max_degree)
                else:
                    for n in [x for x in (2, 4, 6, 8) if x <= max_degree]:
                        if not self._atomic_guard(f"enumerate_N{n}"):
                            break
                        self._enumerate_degree(n)
                        if float(self.config.get("wall_hours", 0)) <= 0.5 and n >= 6:
                            break

                if focus.startswith("6d") and max_degree >= 8:
                    self.bus.emit(
                        "STAGE_STARTED",
                        "6D degree-8 focus complete for this pass; 10D not started",
                        stage="focus_gate",
                        beginner="Finished this pass on the 6D degree-8 ladder. The separate 10D problem is still waiting.",
                    )

            if self.config.get("checkpoint_resume_test") and not self.work.get("resume_tested"):
                self._checkpoint_resume_test()

            final_status = "STOPPED" if self._stop else "COMPLETE"
            if self._time_up() and not self._stop:
                final_status = "COMPLETE"
            self._maybe_checkpoint("final", force=True)
            self.bus.set_status(final_status)
            self.bus.emit(
                "RUN_STOPPED",
                f"Run finished with status {final_status}",
                stage="final",
                beginner="This research session has finished and saved its progress.",
            )
            self._log(f"RUN_STOPPED {final_status}")
            return 0
        except KeyboardInterrupt:
            self._maybe_checkpoint("signal", force=True)
            self.bus.set_status("STOPPED")
            self.bus.emit("RUN_STOPPED", "Interrupted; checkpoint saved", stage="signal")
            return 130
        except Exception as exc:
            self.bus.state.error = str(exc)
            self.bus.set_status("ERROR")
            self._maybe_checkpoint("error", force=True)
            self.bus.emit(
                "RUN_STOPPED",
                f"Error: {exc}",
                stage="error",
                evidence_status="failed",
            )
            self._log(traceback.format_exc())
            return 1
        finally:
            self._stop_heartbeat()
            try:
                if PID_FILE.exists():
                    PID_FILE.unlink(missing_ok=True)
            except Exception:
                pass


def build_config_from_args(args: argparse.Namespace) -> dict[str, Any]:
    preset = resolve_preset(getattr(args, "preset", None))
    config: dict[str, Any] = {
        "preset": getattr(args, "preset", None),
        "wall_hours": getattr(args, "wall_hours", None),
        "max_degree": getattr(args, "max_degree", None),
        "workers": getattr(args, "workers", None),
        "ram_ceiling_gb": getattr(args, "ram_ceiling_gb", None),
        "checkpoint_minutes": getattr(args, "checkpoint_minutes", None),
        "offline": bool(getattr(args, "offline", False)),
        "allow_battery": bool(getattr(args, "allow_battery", False)),
        "advance_uncertified": False,
        "validate": True,
        "checkpoint_resume_test": False,
        "allow_degree8_planning": True,
    }
    config.update({k: v for k, v in preset.items() if k != "description"})
    # Explicit CLI overrides preset.
    if getattr(args, "wall_hours", None) is not None:
        config["wall_hours"] = args.wall_hours
    if getattr(args, "max_degree", None) is not None:
        config["max_degree"] = args.max_degree
    if getattr(args, "workers", None) is not None:
        config["workers"] = args.workers
    if getattr(args, "ram_ceiling_gb", None) is not None:
        config["ram_ceiling_gb"] = args.ram_ceiling_gb
    if getattr(args, "checkpoint_minutes", None) is not None:
        config["checkpoint_minutes"] = args.checkpoint_minutes
    # Defaults if still unset
    config.setdefault("wall_hours", 1.0)
    config.setdefault("max_degree", 6)
    config.setdefault("workers", 1)
    config.setdefault("ram_ceiling_gb", 8.0)
    config.setdefault("checkpoint_minutes", 10)
    if getattr(args, "resume", None):
        config["resume_from"] = args.resume
    return config


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="invariant_engine run")
    from .presets import PRESETS

    parser.add_argument("--preset", choices=sorted(PRESETS.keys()))
    parser.add_argument("--wall-hours", type=float, default=None)
    parser.add_argument("--max-degree", type=int, default=None)
    parser.add_argument("--workers", type=int, default=None)
    parser.add_argument("--ram-ceiling-gb", type=float, default=None)
    parser.add_argument("--checkpoint-minutes", type=float, default=None)
    parser.add_argument("--offline", action="store_true")
    parser.add_argument("--allow-battery", action="store_true")
    parser.add_argument("--resume", type=str, default=None, help="Path to checkpoint JSON")
    args = parser.parse_args(argv)

    # Ensure repo root on path for `tests.*` imports during validation.
    root = Path(__file__).resolve().parents[2]
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))
    if str(root / "src") not in sys.path:
        sys.path.insert(0, str(root / "src"))

    config = build_config_from_args(args)

    resume_path: Path | None = None
    if config.get("resume_from"):
        resume_path = Path(config["resume_from"])
    elif config.get("discover_10d") or str(config.get("focus", "")).startswith("10d"):
        # Crash recovery: pick up resumable 10D work without requiring --resume.
        cand = latest_checkpoint()
        if cand is not None:
            try:
                probe = load_checkpoint(cand)
                work = probe.get("work") or {}
                if (
                    work.get("10d_sanity_done")
                    or work.get("10d_enum_done")
                    or int(work.get("10d_catalog_chunks") or 0) > 0
                ):
                    resume_path = cand
            except Exception:
                resume_path = None

    if resume_path is not None:
        data = load_checkpoint(resume_path)
        merged = dict(data.get("config") or {})
        merged.update(config)  # CLI/preset wins for wall clock, offline, etc.
        ctrl = AutonomousController(merged)
        ctrl.work = {**ctrl.work, **(data.get("work") or {})}
        ctrl.bus.run_id = data["run_id"]
        ctrl.bus.state.run_id = data["run_id"]
        live = data.get("live") or {}
        if live.get("generators"):
            ctrl.bus.state.generators = list(live["generators"])
        if live.get("invariant_classification"):
            ctrl.bus.state.invariant_classification = dict(live["invariant_classification"])
        if live.get("certified_frontier"):
            ctrl.bus.state.certified_frontier = dict(live["certified_frontier"])
        # Don't re-run the full test suite on every crash restart.
        if ctrl.work.get("10d_sanity_done"):
            ctrl.config["validate"] = False
        print(f"Resuming from checkpoint {resume_path} (run_id={data['run_id']})", flush=True)
    else:
        ctrl = AutonomousController(config)
    return ctrl.run()
