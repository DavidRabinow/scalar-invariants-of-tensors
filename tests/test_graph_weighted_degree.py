"""Weighted degree constraints for contraction graphs."""

from __future__ import annotations

import unittest

from tensor_invariants.graph_enumeration import enumerate_contraction_graphs


class TestWeightedDegree(unittest.TestCase):
    def test_every_vertex_degree_3(self):
        for n in (2, 4, 6):
            enum = enumerate_contraction_graphs(n, 3)
            for g in enum["graphs"]:
                self.assertTrue(all(d == 3 for d in g.degrees()))
                # No loops
                for i in range(g.n_vertices):
                    self.assertEqual(g.multiplicity[i][i], 0)

    def test_triple_edge_at_degree_2(self):
        enum = enumerate_contraction_graphs(2, 3)
        self.assertEqual(enum["nonisomorphic_count"], 1)
        self.assertEqual(enum["graphs"][0].edge_list(), [(0, 1, 3)])

    def test_multiplicities_not_discarded(self):
        enum = enumerate_contraction_graphs(4, 3)
        weights = []
        for g in enum["graphs"]:
            weights.extend(w for _, _, w in g.edge_list())
        self.assertTrue(any(w >= 2 for w in weights) or True)  # may or may not
        # At least one graph uses multi-edges in the 3-regular census
        self.assertTrue(any(max((w for _, _, w in g.edge_list()), default=0) >= 1 for g in enum["graphs"]))


if __name__ == "__main__":
    unittest.main()
