"""Einsum vs nested-loop contraction cross-check."""

from __future__ import annotations

import unittest

import numpy as np

from tensor_invariants.antisymmetric_tensors import random_antisymmetric_form
from tensor_invariants.contraction_compiler import make_evaluator
from tensor_invariants.contraction_evaluator import evaluate_nested_loops
from tensor_invariants.graph_enumeration import enumerate_contraction_graphs
from tensor_invariants.validation import check_graph_relabeling_invariance


class TestContractionEvaluation(unittest.TestCase):
    def test_quadratic_einsum_vs_loops(self):
        rng = np.random.default_rng(0)
        H = random_antisymmetric_form(6, 3, rng)
        g = enumerate_contraction_graphs(2, 3)["graphs"][0]
        v1 = make_evaluator(g)[1](H)
        v2 = evaluate_nested_loops(g, H)
        self.assertTrue(np.allclose(v1, v2), msg=f"{v1} vs {v2}")

    def test_quartic_einsum_vs_loops(self):
        rng = np.random.default_rng(1)
        H = random_antisymmetric_form(4, 3, rng)  # smaller dim for loops
        # Still use 6D graphs but evaluate on dim=4 tensor of rank 3
        # Actually graphs are dimension-agnostic; use dim=4 for speed
        for g in enumerate_contraction_graphs(4, 3)["graphs"]:
            v1 = make_evaluator(g)[1](H)
            v2 = evaluate_nested_loops(g, H)
            self.assertTrue(np.allclose(v1, v2, rtol=1e-8, atol=1e-8), msg=f"{v1} vs {v2}")

    def test_relabeling_invariance(self):
        rng = np.random.default_rng(2)
        H = random_antisymmetric_form(6, 3, rng)
        g = enumerate_contraction_graphs(4, 3)["graphs"][0]
        report = check_graph_relabeling_invariance(g, H, n_perms=6, seed=3)
        self.assertTrue(report["pass"], msg=report)


if __name__ == "__main__":
    unittest.main()
