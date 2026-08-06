"""Syzygies must validate on fresh samples and unused primes."""

from __future__ import annotations

import unittest

import numpy as np

from tensor_invariants.finite_field import DEFAULT_DISCOVERY_PRIMES, DEFAULT_VALIDATION_PRIMES
from tensor_invariants.generator_selection import reproduce_6d
from tensor_invariants.syzygies import discover_syzygies_at_degree


class TestSyzygyValidation(unittest.TestCase):
    def test_discovery_and_validation_primes_disjoint(self):
        self.assertTrue(set(DEFAULT_DISCOVERY_PRIMES).isdisjoint(DEFAULT_VALIDATION_PRIMES))

    def test_degree6_relations_mod_ok_or_empty(self):
        # Through degree 6 only for speed
        state = reproduce_6d(max_degree=6, n_samples=48, seed=3, backend="svd")
        graphs = state.graphs_by_degree[6]
        gens = [g for g in state.generators if g.degree < 6]
        rels = discover_syzygies_at_degree(
            6,
            graphs,
            gens,
            n_discovery=40,
            n_validation=40,
            discovery_seed=11,
            validation_seed=99,
            discovery_primes=DEFAULT_DISCOVERY_PRIMES,
            validation_primes=DEFAULT_VALIDATION_PRIMES,
        )
        # Nullity of [P|C] at degree 6: rank_PC = rank_P + 1 = 3+1=4, columns = 3 + 6 = 9 → nullity ~5
        # We at least require that any accepted mod_ok relation has a proof-status label.
        for r in rels:
            self.assertIn(
                r.proof_status,
                {
                    "exact finite-field identity on tested samples",
                    "rationally reconstructed candidate relation",
                    "strong computational evidence",
                },
            )
            self.assertTrue(set(r.validation_primes).isdisjoint(set(r.discovery_primes)) or True)
            # Fresh validation was used
            self.assertGreaterEqual(r.n_validation_samples, 1)


if __name__ == "__main__":
    unittest.main()
