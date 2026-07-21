"""CLI entry: python -m invariant_engine …"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def _ensure_paths() -> None:
    root = Path(__file__).resolve().parents[2]
    src = root / "src"
    for p in (str(root), str(src)):
        if p not in sys.path:
            sys.path.insert(0, p)


def main(argv: list[str] | None = None) -> int:
    _ensure_paths()
    parser = argparse.ArgumentParser(
        prog="invariant_engine",
        description="Local Lorentz-invariant research engine (offline-capable).",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("check-offline", help="Verify offline readiness")

    dash = sub.add_parser("dashboard", help="Start local dashboard on 127.0.0.1:8765")
    dash.add_argument("--host", default="127.0.0.1")
    dash.add_argument("--port", type=int, default=8765)

    from invariant_engine.presets import PRESETS

    run = sub.add_parser("run", help="Run autonomous research controller")
    run.add_argument("--preset", choices=sorted(PRESETS.keys()))
    run.add_argument("--wall-hours", type=float, default=None)
    run.add_argument("--max-degree", type=int, default=None)
    run.add_argument("--workers", type=int, default=None)
    run.add_argument("--ram-ceiling-gb", type=float, default=None)
    run.add_argument("--checkpoint-minutes", type=float, default=None)
    run.add_argument("--offline", action="store_true")
    run.add_argument("--allow-battery", action="store_true")
    run.add_argument("--resume", type=str, default=None)

    args = parser.parse_args(argv)

    if args.command == "check-offline":
        from invariant_engine.offline import check_offline, print_report

        report = check_offline()
        print_report(report)
        return 0 if report.ok else 1

    if args.command == "dashboard":
        from invariant_engine.dashboard import run_dashboard

        run_dashboard(host=args.host, port=args.port)
        return 0

    if args.command == "run":
        from invariant_engine.autonomous import main as run_main

        # Rebuild argv for autonomous parser.
        forward: list[str] = []
        if args.preset:
            forward += ["--preset", args.preset]
        if args.wall_hours is not None:
            forward += ["--wall-hours", str(args.wall_hours)]
        if args.max_degree is not None:
            forward += ["--max-degree", str(args.max_degree)]
        if args.workers is not None:
            forward += ["--workers", str(args.workers)]
        if args.ram_ceiling_gb is not None:
            forward += ["--ram-ceiling-gb", str(args.ram_ceiling_gb)]
        if args.checkpoint_minutes is not None:
            forward += ["--checkpoint-minutes", str(args.checkpoint_minutes)]
        if args.offline:
            forward.append("--offline")
        if args.allow_battery:
            forward.append("--allow-battery")
        if args.resume:
            forward += ["--resume", args.resume]
        return run_main(forward)

    parser.error(f"Unknown command {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
