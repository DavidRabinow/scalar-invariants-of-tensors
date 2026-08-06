#!/usr/bin/env python3
"""
One-command entry point for the tensor invariants research package.

Usage:
  python run_pipeline.py reproduce-6d
  python run_pipeline.py verify-6d
  python run_pipeline.py explore-10d
  python run_pipeline.py verify-all
"""

from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def _setup_logging(verbose: bool = False) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )


def cmd_reproduce_6d(args: argparse.Namespace) -> int:
    from tensor_invariants.generator_selection import reproduce_6d
    from tensor_invariants.reporting import write_6d_markdown, write_6d_outputs
    from tensor_invariants.syzygies import discover_syzygies_at_degree

    expected = json.loads((ROOT / "benchmarks" / "paper_6d_expected.json").read_text())
    print("=== Blind 6D discovery (graphs → P_N|C_N ranks) ===")
    state = reproduce_6d(
        max_degree=args.max_degree,
        n_samples=args.samples,
        seed=args.seed,
        backend=args.backend,
    )
    for r in state.reports:
        print(
            f"  N={r.degree}: graphs={r.n_graphs} connected_rank={r.connected_rank} "
            f"P={r.rank_P} PC={r.rank_PC} n_new={r.n_new} monos={r.n_lower_monomials}"
        )
    print(f"Generator degrees: {state.degrees}")

    syzygies = []
    if args.syzygies:
        print("=== Syzygy discovery (modular; validated on fresh samples) ===")
        for n in (6, 8):
            graphs = state.graphs_by_degree.get(n, [])
            # Use generators strictly below n
            gens = [g for g in state.generators if g.degree < n]
            if not graphs:
                continue
            rels = discover_syzygies_at_degree(
                n,
                graphs,
                gens,
                n_discovery=max(32, args.samples // 2),
                n_validation=max(32, args.samples // 2),
                discovery_seed=args.seed + 17,
                validation_seed=args.seed + 91,
            )
            print(f"  N={n}: {len(rels)} candidate relations")
            syzygies.extend(rels)

    out = ROOT / "outputs" / "6d"
    bundle = write_6d_outputs(out, state, syzygies=syzygies, expected=expected)
    write_6d_markdown(ROOT / "reports" / "6d_reproduction.md", bundle)

    ok = all(
        [
            bundle["comparison"]["graph_counts"]["ok"],
            bundle["comparison"]["connected_ranks"]["ok"],
            bundle["comparison"]["new_generators"]["ok"],
            bundle["comparison"]["generator_degrees"]["ok"],
        ]
    )
    print(json.dumps(bundle["comparison"], indent=2))
    print(f"\n=== VERDICT: 6D reproduction {'PASS' if ok else 'FAIL'} ===")
    if not ok:
        return 1
    return 0


def cmd_verify_6d(args: argparse.Namespace) -> int:
    import pytest

    scientific = [
        "tests/test_tensor_antisymmetry.py",
        "tests/test_graph_weighted_degree.py",
        "tests/test_graph_canonicalization.py",
        "tests/test_graph_counts_6d.py",
        "tests/test_contraction_evaluation.py",
        "tests/test_monomial_generation.py",
        "tests/test_rank_backends.py",
        "tests/test_generator_counts_6d.py",
        "tests/test_syzygy_validation.py",
        "tests/test_self_duality_10d.py",
    ]
    rc = pytest.main(["-q", "--tb=line", *scientific])
    return 0 if rc == 0 else 1


def cmd_explore_10d(args: argparse.Namespace) -> int:
    from tensor_invariants.configuration import load_config
    from tensor_invariants.explore_10d import explore_10d, write_10d_reports

    cfg = load_config(ROOT / "configs" / "self_dual_five_form_10d.yaml")
    results = explore_10d(
        cfg,
        out_dir=ROOT / "outputs" / "10d",
        checkpoint_dir=ROOT / "outputs" / "10d" / "checkpoints",
        max_degree=args.max_degree,
    )
    write_10d_reports(results, ROOT / "reports")
    print(json.dumps({k: results[k] for k in ("self_duality", "graphs", "literature")}, indent=2, default=str))
    if not results["self_duality"]["passed"]:
        print("=== VERDICT: 10D self-duality FAIL ===")
        return 1
    print("=== VERDICT: 10D exploration checkpointed (self-duality PASS) ===")
    return 0


def cmd_verify_all(args: argparse.Namespace) -> int:
    rc = cmd_verify_6d(args)
    if rc != 0:
        return rc
    # Also run reproduce quickly at reduced samples if --quick
    repro = argparse.Namespace(
        max_degree=6 if args.quick else 10,
        samples=40 if args.quick else 64,
        seed=1,
        syzygies=not args.quick,
        backend="svd",
        verbose=getattr(args, "verbose", False),
    )
    rc = cmd_reproduce_6d(repro)
    if rc != 0:
        return rc
    if args.quick:
        return 0
    explore = argparse.Namespace(max_degree=4, verbose=getattr(args, "verbose", False))
    return cmd_explore_10d(explore)


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Tensor invariants research pipeline")
    p.add_argument("-v", "--verbose", action="store_true")
    sub = p.add_subparsers(dest="command", required=True)

    r = sub.add_parser("reproduce-6d", help="Blind 6D paper reproduction")
    r.add_argument("--max-degree", type=int, default=10)
    r.add_argument("--samples", type=int, default=80)
    r.add_argument("--seed", type=int, default=1)
    r.add_argument("--backend", choices=["svd", "modp"], default="svd")
    r.add_argument("--syzygies", action="store_true", default=True)
    r.add_argument("--no-syzygies", action="store_false", dest="syzygies")
    r.set_defaults(func=cmd_reproduce_6d)

    v = sub.add_parser("verify-6d", help="Run unit/regression tests")
    v.set_defaults(func=cmd_verify_6d)

    e = sub.add_parser("explore-10d", help="Checkpointed 10D exploration")
    e.add_argument("--max-degree", type=int, default=4)
    e.set_defaults(func=cmd_explore_10d)

    a = sub.add_parser("verify-all", help="Tests + 6D reproduce + 10D smoke")
    a.add_argument("--quick", action="store_true")
    a.set_defaults(func=cmd_verify_all)

    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    _setup_logging(args.verbose)
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
