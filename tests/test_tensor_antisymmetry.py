"""Antisymmetry of randomly generated p-forms."""

from __future__ import annotations

import unittest

import numpy as np

from tensor_invariants.antisymmetric_tensors import (
    antisymmetry_error,
    random_antisymmetric_form,
)
from tensor_invariants.tensor_spaces import n_independent_components


class TestAntisymmetry(unittest.TestCase):
    def test_independent_component_count_6d(self):
        self.assertEqual(n_independent_components(6, 3), 20)

    def test_sign_under_permutations(self):
        rng = np.random.default_rng(0)
        H = random_antisymmetric_form(6, 3, rng, mode="float")
        self.assertLess(antisymmetry_error(H), 1e-12)

    def test_integer_mode(self):
        rng = np.random.default_rng(1)
        H = random_antisymmetric_form(6, 3, rng, mode="int", int_bound=5)
        self.assertLess(antisymmetry_error(H), 1e-12)


if __name__ == "__main__":
    unittest.main()
