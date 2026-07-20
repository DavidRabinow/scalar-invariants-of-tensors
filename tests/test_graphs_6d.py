"""Stage 2–3: graph enumeration + contraction compiler; 6D regression."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from invariants.contraction import compile_graph, make_evaluator  # noqa: E402
from invariants.graphs import enumerate_contraction_graphs, summarize_orders  # noqa: E402
from invariants.three_form_6d import paper_generators, random_three_form  # noqa: E402
from opt_einsum import contract  # noqa: E402


class TestGraphEnumeration(unittest.TestCase):
    def test_3regular_counts_match_paper(self):
        # Elamaran–Ferko–Scarlett §4.1: connected non-iso 3-regular at N=2,4,6
        # (N=8 = 20 is slower; covered separately with a longer timeout if needed)
        expected = {2: 1, 4: 2, 6: 6}
        for n, exp in expected.items():
            result = enumerate_contraction_graphs(n, form_rank=3)
            self.assertEqual(
                result["nonisomorphic_count"],
                exp,
                msg=f"N={n}: got {result['nonisomorphic_count']} connected={result['connected_count']}",
            )

    def test_3regular_n8_count(self):
        result = enumerate_contraction_graphs(8, form_rank=3)
        self.assertEqual(result["nonisomorphic_count"], 20)

    def test_5regular_handshaking_odd_impossible(self):
        result = enumerate_contraction_graphs(3, form_rank=5)
        self.assertEqual(result["nonisomorphic_count"], 0)

    def test_5regular_n2_exists(self):
        result = enumerate_contraction_graphs(2, form_rank=5)
        self.assertEqual(result["nonisomorphic_count"], 1)
        g = result["graphs"][0]
        self.assertEqual(g.edge_list(), [(0, 1, 5)])


class TestContractionCompiler6D(unittest.TestCase):
    def test_quadratic_matches_paper(self):
        result = enumerate_contraction_graphs(2, form_rank=3)
        self.assertEqual(result["nonisomorphic_count"], 1)
        compiled, ev = make_evaluator(result["graphs"][0])
        rng = np.random.default_rng(0)
        H = random_three_form(rng)
        # paper x^(2) = H_abc H^abc
        x2 = float(contract("abc,abc->", H, H))
        val = ev(H)
        self.assertTrue(np.allclose(val, x2), msg=f"{val} vs {x2}")

    def test_quartic_two_inequivalent(self):
        result = enumerate_contraction_graphs(4, form_rank=3)
        self.assertEqual(result["nonisomorphic_count"], 2)
        gens = {g.name: g for g in paper_generators()}
        rng = np.random.default_rng(1)
        H = random_three_form(rng)
        vals = []
        for g in result["graphs"]:
            _, ev = make_evaluator(g)
            vals.append(ev(H))
        # The two graph values should match the two paper quartics up to order
        # (possibly scaled/signed). Check they span the same 2D space as paper gens
        # together with (x2)^2 on many draws.
        rows = []
        for _ in range(30):
            H = random_three_form(rng)
            x2 = gens["x^(2)"].fn(H)
            x41 = gens["x^(4)_1"].fn(H)
            x42 = gens["x^(4)_2"].fn(H)
            gvals = [make_evaluator(g)[1](H) for g in result["graphs"]]
            rows.append([x41, x42, x2 * x2, *gvals])
        M = np.array(rows)
        # Columns 0,1 (paper) and 3,4 (graphs) should have same span mod col 2
        # Rank of [paper1, paper2, graphs...] should equal rank of [paper1, paper2]
        # after removing (x2)^2 dependence — simpler: each graph is linear combo
        # of paper quartics and (x2)^2 numerically.
        from invariants.utils import numerical_rank

        paper = M[:, :2]
        graphs = M[:, 3:]
        lower = M[:, 2:3]
        for j in range(graphs.shape[1]):
            base = np.column_stack([paper, lower])
            trial = np.column_stack([base, graphs[:, j]])
            self.assertEqual(
                numerical_rank(trial, tol=1e-6),
                numerical_rank(base, tol=1e-6),
                msg=f"graph {j} not in span of paper quartics + (x2)^2",
            )

    def test_compile_slot_count(self):
        result = enumerate_contraction_graphs(4, form_rank=3)
        for g in result["graphs"]:
            c = compile_graph(g)
            self.assertEqual(c.n_vertices, 4)
            self.assertEqual(len(c.pairing), 6)  # 4*3/2


class TestSummarize(unittest.TestCase):
    def test_summarize_3form(self):
        rows = summarize_orders(form_rank=3, max_order=6)
        counts = {r["N"]: r["nonisomorphic_count"] for r in rows}
        self.assertEqual(counts[2], 1)
        self.assertEqual(counts[4], 2)
        self.assertEqual(counts[6], 6)


if __name__ == "__main__":
    unittest.main(verbosity=2)
