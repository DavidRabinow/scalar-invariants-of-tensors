"""Lower-degree product monomial generation."""

from __future__ import annotations

import unittest

from tensor_invariants.monomial_basis import NamedGenerator, expected_degree8_monomial_names, weighted_monomials


class TestMonomialGeneration(unittest.TestCase):
    def test_degree8_has_seven_monomials(self):
        gens = [
            NamedGenerator("x^(2)", 2, lambda T: 0.0),
            NamedGenerator("x^(4)_1", 4, lambda T: 0.0),
            NamedGenerator("x^(4)_2", 4, lambda T: 0.0),
            NamedGenerator("x^(6)", 6, lambda T: 0.0),
        ]
        monos = weighted_monomials(gens, 8)
        self.assertEqual(len(monos), 7)
        names = {m.name for m in monos}
        for expected in expected_degree8_monomial_names():
            self.assertIn(expected, names)

    def test_degree6_products(self):
        gens = [
            NamedGenerator("x^(2)", 2, lambda T: 0.0),
            NamedGenerator("x^(4)_1", 4, lambda T: 0.0),
            NamedGenerator("x^(4)_2", 4, lambda T: 0.0),
        ]
        monos = weighted_monomials(gens, 6)
        self.assertEqual(len(monos), 3)
        names = {m.name for m in monos}
        self.assertIn("x^(2)*x^(2)*x^(2)", names)
        self.assertIn("x^(2)*x^(4)_1", names)
        self.assertIn("x^(2)*x^(4)_2", names)


if __name__ == "__main__":
    unittest.main()
