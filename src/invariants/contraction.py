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


ALPHABET = ascii_letters + "".join(
    chr(c) for c in range(0x00C0, 0x00C0 + 80)
)  # >= 60 chars for N=12, r=5


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
        return float(contract(self.einsum_subscripts, *tensors, optimize="greedy"))


def compile_graph(
    graph: ContractionGraph,
    *,
    slot_policy: str = "pop",
) -> CompiledContraction:
    """
    slot_policy:
      - pop: take slots from the end of each vertex's free list (default)
      - pop0: take from the front
      - reverse: reverse free lists then pop
    Different policies = different index wirings of the same multigraph.
    """
    n = graph.n_vertices
    r = graph.form_rank
    free = {v: list(range(r * v, r * v + r)) for v in range(n)}
    if slot_policy == "reverse":
        for v in free:
            free[v].reverse()
    pairs: list[tuple[int, int]] = []
    for i, j, w in graph.edge_list():
        for _ in range(w):
            if not free[i] or not free[j]:
                raise RuntimeError("degree mismatch while pairing slots")
            if slot_policy == "pop0":
                pairs.append((free[i].pop(0), free[j].pop(0)))
            else:
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


LORENTZ_MODES = ("alt", "half", "first", "last")


def _lorentz_tensor_list(
    mode: str, n: int, Td: np.ndarray, Tu: np.ndarray
) -> list[np.ndarray]:
    if mode == "alt":
        return [Td if (v % 2 == 0) else Tu for v in range(n)]
    if mode == "half":
        cut = n // 2
        return [Td if v < cut else Tu for v in range(n)]
    if mode == "first":
        return [Td] + [Tu] * (n - 1)
    if mode == "last":
        return [Tu] * (n - 1) + [Td]
    raise ValueError(f"unknown Lorentz mode {mode!r}")


def make_evaluator_lorentz(
    graph: ContractionGraph,
    *,
    mode: str = "alt",
    slot_policy: str = "pop",
) -> tuple[CompiledContraction, Callable[[np.ndarray, np.ndarray], float]]:
    """
    Lorentzian-style evaluator with optional raise-pattern and slot wiring.

    Call as ``eval_fn(Td, Tu)`` where ``Tu = raise_dense(Td)``.
    """
    compiled = compile_graph(graph, slot_policy=slot_policy)
    n = compiled.n_vertices

    def eval_fn(Td: np.ndarray, Tu: np.ndarray) -> float:
        return compiled.evaluate_dense(_lorentz_tensor_list(mode, n, Td, Tu))

    return compiled, eval_fn


def estimate_largest_intermediate(
    graph: ContractionGraph,
    Td: np.ndarray,
    Tu: np.ndarray,
    *,
    mode: str = "alt",
    slot_policy: str = "pop",
) -> float:
    """Peak einsum intermediate size for the Lorentzian evaluator (elements)."""
    from opt_einsum import contract_path

    compiled = compile_graph(graph, slot_policy=slot_policy)
    tensors = _lorentz_tensor_list(mode, compiled.n_vertices, Td, Tu)
    _, info = contract_path(
        compiled.einsum_subscripts, *tensors, optimize="greedy"
    )
    return float(info.largest_intermediate)