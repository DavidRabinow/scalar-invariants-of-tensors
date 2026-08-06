"""Blind 6D generator counts must match the paper (no answer key in algorithm)."""

from __future__ import annotations

import json
import unittest
from pathlib import Path

from tensor_invariants.generator_selection import reproduce_6d
from tensor_invariants.validation import check_orthogonal_invariance


ROOT = Path(__file__).resolve().parents[1]
EXPECTED = json.loads((ROOT / "benchmarks" / "paper_6d_expected.json").read_text())


class TestGeneratorCounts6D(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # N=8 enumeration ~100s; run once for the class with moderate samples
        cls.state = reproduce_6d(max_degree=10, n_samples=60, seed=7, backend="svd")

    def test_graph_counts(self):
        got = {r.degree: r.n_graphs for r in self.state.reports}
        for k, v in EXPECTED["graph_counts"].items():
            self.assertEqual(got[int(k)], v, msg=f"graphs at {k}")

    def test_connected_ranks(self):
        got = {r.degree: r.connected_rank for r in self.state.reports}
        for k, v in EXPECTED["connected_ranks"].items():
            self.assertEqual(got[int(k)], v, msg=f"connected rank at {k}")

    def test_new_generators(self):
        got = {r.degree: r.n_new for r in self.state.reports}
        for k, v in EXPECTED["new_generators"].items():
            self.assertEqual(got[int(k)], v, msg=f"new gens at {k}")

    def test_final_degrees(self):
        self.assertEqual(self.state.degrees, EXPECTED["generator_degrees"])

    def test_degree8_monomial_count(self):
        r8 = next(r for r in self.state.reports if r.degree == 8)
        self.assertEqual(r8.n_lower_monomials, EXPECTED["degree8_lower_monomial_count"])

    def test_orthogonal_invariance_smoke(self):
        report = check_orthogonal_invariance(seed=0)
        self.assertTrue(report["pass"], msg=report)


if __name__ == "__main__":
    unittest.main()
