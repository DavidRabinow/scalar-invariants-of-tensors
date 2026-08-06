"""Regression: connected 3-regular multigraph counts for the 6D paper."""

from __future__ import annotations

import unittest

from tensor_invariants.graph_enumeration import (
    EXPECTED_CONNECTED_COUNTS_3FORM,
    enumerate_contraction_graphs,
)


class TestGraphCounts6D(unittest.TestCase):
    def test_counts_2_4_6(self):
        for n, exp in ((2, 1), (4, 2), (6, 6)):
            got = enumerate_contraction_graphs(n, 3)["nonisomorphic_count"]
            self.assertEqual(got, exp)

    def test_count_8(self):
        got = enumerate_contraction_graphs(8, 3)["nonisomorphic_count"]
        self.assertEqual(got, EXPECTED_CONNECTED_COUNTS_3FORM[8])


if __name__ == "__main__":
    unittest.main()
