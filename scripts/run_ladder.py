#!/usr/bin/env python3
"""
Blind practice ladder — rediscover known answers without being told them mid-run.

This is the system skeleton:
  candidates → random tests → keep non-redundant ingredients → grade vs answer key

Later upgrades (AlphaGo-like):
  - bigger candidate generator (graphs)
  - optional neural net that ranks which candidates to try first
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from invariants.ladder import run_ladder  # noqa: E402


def main() -> None:
    print("=== Blind discovery ladder ===")
    print("The engine is NOT given the answers while searching.")
    print("We only grade afterward.\n")

    reports = run_ladder(seed=42)
    all_pass = True
    for r in reports:
        status = "PASS" if r["passed"] else "FAIL"
        if not r["passed"]:
            all_pass = False
        print(f"[{status}] {r['name']}")
        print(f"  discovered ({r['discovered_count']}): {r['discovered_names']}")
        print(f"  expected count: {r['expected_count']}")
        print(f"  new by order: {r['by_order']}")
        print()

    print(json.dumps(reports, indent=2))
    print(f"\n=== LADDER VERDICT: {'PASS' if all_pass else 'FAIL'} ===")
    print(
        "\nNext upgrades: (1) auto-generate more candidates, "
        "(2) add 6D 3-form blind level, (3) optional ML ranker for 10D search."
    )
    sys.exit(0 if all_pass else 1)


if __name__ == "__main__":
    main()
