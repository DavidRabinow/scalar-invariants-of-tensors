"""Contraction evaluation backends (optimized einsum + slow nested loops)."""

from __future__ import annotations

from typing import Callable

import numpy as np

from .contraction_compiler import compile_graph, make_evaluator
from .graph_enumeration import ContractionGraph


def evaluate_einsum(graph: ContractionGraph, tensor: np.ndarray) -> float:
    _, ev = make_evaluator(graph)
    return float(ev(tensor))


def evaluate_nested_loops(graph: ContractionGraph, tensor: np.ndarray) -> float:
    """
    Slow reference contraction by explicit nested index loops.

    Only practical for small graphs (N<=4, dim<=6). Used to cross-check einsum.
    """
    compiled = compile_graph(graph)
    n = graph.n_vertices
    r = graph.form_rank
    dim = tensor.shape[0]
    # Build slot -> shared letter id mapping from pairing
    n_slots = n * r
    slot_letter = [-1] * n_slots
    for lid, (a, b) in enumerate(compiled.pairing):
        slot_letter[a] = lid
        slot_letter[b] = lid
    n_letters = len(compiled.pairing)

    # For each letter, the two slots that share it
    letter_slots = [[] for _ in range(n_letters)]
    for s, lid in enumerate(slot_letter):
        letter_slots[lid].append(s)

    total = 0.0
    # Iterate all assignments of indices to letters
    # Recursively assign letter values
    idx_of_slot = [0] * n_slots

    def rec(letter: int) -> None:
        nonlocal total
        if letter == n_letters:
            # Evaluate product of tensor components
            prod = 1.0
            for v in range(n):
                coords = tuple(idx_of_slot[r * v + k] for k in range(r))
                prod *= float(tensor[coords])
            total += prod
            return
        for val in range(dim):
            for s in letter_slots[letter]:
                idx_of_slot[s] = val
            rec(letter + 1)

    rec(0)
    return float(total)


def make_reference_evaluator(graph: ContractionGraph) -> Callable[[np.ndarray], float]:
    def fn(T: np.ndarray) -> float:
        return evaluate_nested_loops(graph, T)

    return fn
