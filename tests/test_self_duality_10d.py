"""10D self-duality and convention tests."""

from __future__ import annotations

import unittest

from tensor_invariants.configuration import load_config
from tensor_invariants.self_duality import (
    N_COMPONENTS_5FORM,
    N_SELF_DUAL,
    validate_self_duality,
)
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class TestSelfDuality10D(unittest.TestCase):
    def test_component_counts(self):
        self.assertEqual(N_COMPONENTS_5FORM, 252)
        self.assertEqual(N_SELF_DUAL, 126)

    def test_star_squared_and_projection(self):
        report = validate_self_duality(n_samples=12, seed=0)
        self.assertTrue(report.passed, msg=report.message)
        self.assertEqual(report.star_squared, 1)

    def test_config_conventions(self):
        cfg = load_config(ROOT / "configs" / "self_dual_five_form_10d.yaml")
        self.assertEqual(cfg.dim, 10)
        self.assertEqual(cfg.form_degree, 5)
        self.assertEqual(cfg.signature, "lorentzian")
        self.assertTrue(cfg.self_dual)
        self.assertEqual(cfg.hodge_star_squared, 1)
        self.assertEqual(cfg.metric_signature[0], -1)
        self.assertTrue(all(s == 1 for s in cfg.metric_signature[1:]))


if __name__ == "__main__":
    unittest.main()
