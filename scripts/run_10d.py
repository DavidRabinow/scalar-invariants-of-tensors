#!/usr/bin/env python3
"""
Run the 10D chiral 5-form engine on this computer.

This builds the chiral object, checks the mirror rule, and runs blind
discovery on a starter set of formulas. It does NOT claim to finish all ~81.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from invariants.five_form_10d import (  # noqa: E402
    run_low_order_discovery,
    sanity_checks,
)


def main() -> None:
    print("=== 10D chiral 5-form engine ===")
    print("Building the object + mirror rule check...\n")
    sanity = sanity_checks(seed=0)
    print(json.dumps(sanity, indent=2))

    if not sanity["is_self_dual"]:
        print("\nFAIL: chiral projection broken")
        sys.exit(1)

    print("\n=== Blind discovery on starter formulas (slow-ish) ===")
    print("Not the full ~81 — first independent pieces from our starter list.\n")
    disc = run_low_order_discovery(seed=1, n_draws=20)
    print(json.dumps(disc, indent=2))

    print("\n=== STATUS ===")
    print("PASS: 10D chiral object exists on your computer and discovery ran.")
    print(
        f"Found {disc['discovered_count']} independent starter ingredient(s) "
        f"(literature expects ~{disc['literature_target']} total with a full candidate list)."
    )
    print("\nNext: auto-generate many more contractions so discovery can climb toward ~81.")
    sys.exit(0)


if __name__ == "__main__":
    main()
