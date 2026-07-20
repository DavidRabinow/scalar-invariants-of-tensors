#!/usr/bin/env python3
"""Reproduce the 6D three-form invariant count (Elamaran–Ferko–Scarlett §4.1)."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from invariants.three_form_6d import (  # noqa: E402
    paper_generators,
    smoke_evaluate_generators,
    verify_appendix_syzygies,
    verify_paper_generators_independent,
)


def main() -> None:
    print("=== Smoke: evaluate paper generators on one random H ===")
    vals = smoke_evaluate_generators(seed=0)
    for name, v in vals.items():
        print(f"  {name:10s} = {v:.6e}")

    print("\n=== Numerical HSOP independence (expect new: 1,2,1,1,0,0 at N=2..12) ===")
    report = verify_paper_generators_independent(n_draws=60, seed=42)
    print(json.dumps(report, indent=2))

    rank_ok = report["generator_matrix_rank"] == 5
    expected_new = {2: 1, 4: 2, 6: 1, 8: 1, 10: 0, 12: 0}
    news = {
        o: report["orders"][o]["new_independent"]
        for o in expected_new
        if o in report["orders"]
    }
    print(f"\nNew independents by order: {news}")
    print(f"Expected:                 {expected_new}")
    match = all(news.get(o) == expected_new[o] for o in expected_new)

    print("\n=== Appendix A syzygies ===")
    syz = verify_appendix_syzygies(n_draws=100, seed=11)
    print(json.dumps(syz, indent=2))

    ok = rank_ok and match and syz["pass"]
    print(f"\n=== VERDICT: 6D reproduction {'PASS' if ok else 'FAIL'} ===")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
