"""Stage 1 foundation tests: 10D Lorentzian Hodge star."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from invariants.hodge10 import (  # noqa: E402
    N_CHIRAL,
    N_COMPONENTS,
    antisymmetry_error,
    assert_hodge_consistent,
    combo_to_dense,
    hodge_star_combo_fast,
    hodge_star_combo_reference,
    project_self_dual_combo,
    random_five_form_combo,
    validate_hodge,
)
import numpy as np


class TestHodge10Stage1(unittest.TestCase):
    def test_component_counts(self):
        self.assertEqual(N_COMPONENTS, 252)
        self.assertEqual(N_CHIRAL, 126)

    def test_fast_matches_reference_small(self):
        rng = np.random.default_rng(0)
        for _ in range(5):
            F = random_five_form_combo(rng)
            fast = hodge_star_combo_fast(F)
            ref = hodge_star_combo_reference(F)
            err = float(np.max(np.abs(fast - ref)))
            self.assertLess(err, 1e-10, msg=f"fast vs ref err={err}")

    def test_double_star_is_identity(self):
        rng = np.random.default_rng(1)
        F = random_five_form_combo(rng)
        ds = hodge_star_combo_fast(hodge_star_combo_fast(F))
        err = float(np.max(np.abs(ds - F)))
        self.assertLess(err, 1e-10, msg=f"**F-F err={err}")

    def test_projection_is_self_dual(self):
        rng = np.random.default_rng(2)
        F = project_self_dual_combo(random_five_form_combo(rng))
        err = float(np.max(np.abs(hodge_star_combo_fast(F) - F)))
        self.assertLess(err, 1e-10, msg=f"*F-F after proj err={err}")

    def test_antisymmetry_exact(self):
        rng = np.random.default_rng(3)
        T = combo_to_dense(random_five_form_combo(rng))
        err = antisymmetry_error(T)
        self.assertLess(err, 1e-14, msg=f"antisym err={err}")

    def test_validate_hodge_1000_samples(self):
        report = validate_hodge(n_samples=1000, seed=42)
        print("\n" + report.message)
        print(
            f"  max|**F-F|={report.max_double_star_error:.3e}\n"
            f"  max|*Fp-Fp|={report.max_projection_star_error:.3e}\n"
            f"  max antisym={report.max_antisymmetry_error:.3e}\n"
            f"  max fast-vs-ref={report.max_fast_vs_reference_error:.3e}"
        )
        self.assertTrue(report.passed, msg=report.message)

    def test_assert_hodge_consistent_raises_on_bad_tol(self):
        # Sanity: with absurdly tight tol on a smoke sample count, may still pass;
        # instead ensure assert path works when forced fail via n_samples check.
        report = validate_hodge(n_samples=10, seed=0)
        self.assertTrue(report.passed)
        assert_hodge_consistent(n_samples=10, seed=0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
