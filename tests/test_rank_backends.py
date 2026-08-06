"""Compare SVD, rational, and finite-field rank backends."""

from __future__ import annotations

import unittest

import numpy as np

from tensor_invariants.nullspace import nullspace_mod_p, rank_mod_p
from tensor_invariants.numerical_rank import rational_rank, svd_rank
from tensor_invariants.rational_reconstruction import crt_combine, normalize_integer_vector, rational_reconstruct


class TestRankBackends(unittest.TestCase):
    def test_small_matrix_agreement(self):
        M = np.array([[1, 2, 3], [2, 4, 6], [0, 1, 1]], dtype=object)
        self.assertEqual(rational_rank(M), 2)
        self.assertEqual(svd_rank(np.asarray(M, dtype=float)), 2)
        for p in (97, 101, 1000033):
            self.assertEqual(rank_mod_p(M, p), 2)

    def test_nullspace_dimension(self):
        M = np.array([[1, 2, 3], [2, 4, 6]], dtype=object)
        N = nullspace_mod_p(M, 97)
        self.assertEqual(N.shape[1], 2)  # rank 1, n=3 → nullity 2

    def test_crt_and_rational_recon(self):
        # 3/2 mod primes
        primes = [101, 103, 107]
        target = rational_reconstruct(
            crt_combine([pow(2, -1, p) * 3 % p for p in primes], primes),
            101 * 103 * 107,
        )
        self.assertEqual(target.numerator, 3)
        self.assertEqual(target.denominator, 2)

    def test_normalize(self):
        self.assertEqual(normalize_integer_vector([0, -2, 4]), [0, 1, -2])


if __name__ == "__main__":
    unittest.main()
