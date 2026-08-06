"""Canonicalization must preserve edge weights and agree with brute force."""

from __future__ import annotations

import unittest

from tensor_invariants.graph_canonicalization import (
    are_isomorphic,
    brute_force_canonical,
    canonical_label,
    canonical_multiplicity,
)
from tensor_invariants.graph_enumeration import enumerate_contraction_graphs


class TestCanonicalization(unittest.TestCase):
    def test_fast_matches_brute_force_through_6(self):
        for n in (2, 4, 6):
            enum = enumerate_contraction_graphs(n, 3)
            for g in enum["graphs"]:
                a = canonical_multiplicity(g.multiplicity)
                b = brute_force_canonical(g.multiplicity)
                self.assertEqual(a, b, msg=f"N={n} {g.canonical_id}")

    def test_relabeling_same_canonical_id(self):
        enum = enumerate_contraction_graphs(4, 3)
        g = enum["graphs"][0]
        # Swap vertices 0 and 1
        M = [list(row) for row in g.multiplicity]
        n = len(M)
        perm = list(range(n))
        perm[0], perm[1] = perm[1], perm[0]
        P = [[M[perm[i]][perm[j]] for j in range(n)] for i in range(n)]
        self.assertEqual(canonical_label(g.multiplicity), canonical_label(P))
        self.assertTrue(are_isomorphic(g.multiplicity, P))


if __name__ == "__main__":
    unittest.main()
