"""
Compile a ContractionGraph into an einsum (or tensordot plan) for rank-r forms.

Index slots: vertex v owns slots (r*v, …, r*v + r - 1).
Each edge of weight w between u,v pairs w slots from u with w slots from v.
"""

from __future__ import annotations

from dataclasses import dataclass
from string import ascii_letters
from typing import Callable

import numpy as np
from opt_einsum import contract

from .graphs import ContractionGraph


ALPHABET = ascii_letters  # 52 letters; enough for N*r <= 52 (e.g. N=8,r=5 → 40)


@dataclass(frozen=True)
class CompiledContraction:
    graph_id: str
    n_vertices: int
    form_rank: int
    einsum_subscripts: str  # e.g. "abc,ade,..."
    pairing: tuple[tuple[int, int], ...]  # paired slot indices

    def evaluate_dense(self, tensors: list[np.ndarray]) -> float:
        if len(tensors) != self.n_vertices:
            raise ValueError("tensor count mismatch")
        return float(contract(self.einsum_subscripts, *tensors, optimize=True))


def compile_graph(graph: ContractionGraph) -> CompiledContraction:
    n = graph.n_vertices
    r = graph.form_rank
    free = {v: list(range(r * v, r * v + r)) for v in range(n)}
    pairs: list[tuple[int, int]] = []
    for i, j, w in graph.edge_list():
        for _ in range(w):
            if not free[i] or not free[j]:
                raise RuntimeError("degree mismatch while pairing slots")
            pairs.append((free[i].pop(), free[j].pop()))
    if any(free[v] for v in range(n)):
        raise RuntimeError("unused slots — graph not regular of degree r")

    n_slots = r * n
    if n_slots > len(ALPHABET):
        raise ValueError(f"need {n_slots} letters, alphabet has {len(ALPHABET)}")

    letters = [""] * n_slots
    next_i = 0
    for a, b in pairs:
        ch = ALPHABET[next_i]
        next_i += 1
        letters[a] = ch
        letters[b] = ch

    subs = []
    for v in range(n):
        subs.append("".join(letters[r * v : r * v + r]))
    einsum = ",".join(subs) + "->"
    return CompiledContraction(
        graph_id=graph.canonical_id,
        n_vertices=n,
        form_rank=r,
        einsum_subscripts=einsum,
        pairing=tuple(pairs),
    )


def make_evaluator(
    graph: ContractionGraph,
) -> tuple[CompiledContraction, Callable[[np.ndarray], float]]:
    """
    Return compiled plan and a function that evaluates the scalar on one dense
    tensor T (shape (d,)*r) by using N identical copies.
    """
    compiled = compile_graph(graph)

    def eval_fn(T: np.ndarray) -> float:
        return compiled.evaluate_dense([T] * compiled.n_vertices)

    return compiled, eval_fn
