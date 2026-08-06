"""
Ten-dimensional chiral self-dual 5-form exploration (Phase II).

Proceed degree-by-degree with checkpointing. Do not invent conclusions.
Label every claim with an explicit proof-status.
"""

from __future__ import annotations

import logging
import time
from pathlib import Path
from typing import Any

import numpy as np

from .checkpointing import load_checkpoint, save_checkpoint
from .configuration import TensorConfig, load_config
from .graph_enumeration import enumerate_contraction_graphs
from .reporting import write_json
from .self_duality import (
    N_COMPONENTS_5FORM,
    N_SELF_DUAL,
    combo_to_dense,
    random_self_dual_5form_combo,
    validate_self_duality,
)

logger = logging.getLogger(__name__)


def explore_10d(
    config: TensorConfig | None = None,
    *,
    out_dir: Path | None = None,
    checkpoint_dir: Path | None = None,
    max_degree: int | None = None,
) -> dict[str, Any]:
    """
    Checkpointed low-degree exploration for a self-dual 5-form in d=10.

    Full enumeration at high degree is computationally heavy (5-regular graphs).
    This routine validates conventions, enumerates feasible small N, and records
    scaling notes with proof-status labels.
    """
    if config is None:
        config = load_config(Path("configs/self_dual_five_form_10d.yaml"))
    root = Path(".")
    out_dir = out_dir or (root / "outputs" / "10d")
    checkpoint_dir = checkpoint_dir or (out_dir / "checkpoints")
    max_degree = max_degree or config.max_degree

    t0 = time.time()
    sd = validate_self_duality(n_samples=16, seed=config.seed)
    save_checkpoint(
        checkpoint_dir,
        "self_duality",
        {
            "passed": sd.passed,
            "max_double_star_error": sd.max_double_star_error,
            "max_projection_star_error": sd.max_projection_star_error,
            "n_components": sd.n_components,
            "n_self_dual_dof": sd.n_self_dual_dof,
            "star_squared": sd.star_squared,
            "signature": sd.signature,
            "proof_status": sd.proof_status,
        },
    )

    # Smoke: random self-dual tensor
    rng = np.random.default_rng(config.seed)
    F = random_self_dual_5form_combo(rng)
    dense = combo_to_dense(F)

    graph_info: dict[str, Any] = {}
    # Only enumerate small N where handshaking allows 5-regular graphs: N even.
    # N=2 is feasible (one 5-fold edge). N=4 is larger but doable.
    for n in range(2, min(max_degree, 4) + 1, 2):
        ck = load_checkpoint(checkpoint_dir, f"graphs_N{n}")
        if ck is not None:
            graph_info[str(n)] = ck
            continue
        t1 = time.time()
        enum = enumerate_contraction_graphs(n, form_rank=5, connected_only=True)
        payload = {
            "n_vertices": n,
            "form_rank": 5,
            "nonisomorphic_count": enum["nonisomorphic_count"],
            "canonical_ids": enum["canonical_ids"],
            "elapsed_sec": time.time() - t1,
            "proof_status": "exact combinatorial enumeration",
            "note": "5-regular loopless connected multigraphs; not yet quotiented by self-duality identities",
        }
        save_checkpoint(checkpoint_dir, f"graphs_N{n}", payload)
        graph_info[str(n)] = payload
        logger.info("10D N=%s graphs=%s (%.2fs)", n, enum["nonisomorphic_count"], payload["elapsed_sec"])

    # Quadratic invariant on chiral form often vanishes in Lorentzian chiral theories
    from opt_einsum import contract

    q = float(contract("abcde,abcde->", dense, dense))
    # Raised contraction with metric
    from .tensor_spaces import metric_diagonal

    g = metric_diagonal(10, "lorentzian")
    # Build raised dense naively for smoke
    # F·F with η: sum F_{i} F^{i}
    # Using combo: already in self_duality / legacy five_form

    results = {
        "conventions": config.to_dict(),
        "self_duality": {
            "passed": sd.passed,
            "n_generic_components": N_COMPONENTS_5FORM,
            "n_self_dual_dof": N_SELF_DUAL,
            "star_squared": sd.star_squared,
            "signature": sd.signature,
            "proof_status": sd.proof_status,
        },
        "graphs": graph_info,
        "smoke": {
            "euclidean_style_raw_contraction_F_F": q,
            "note": "Raw Kronecker contraction of lowered self-dual 5-form; Lorentzian raised contraction differs.",
            "proof_status": "strong computational evidence",
        },
        "literature": {
            "hypothesis_primary_invariants": 81,
            "status": "external literature hypothesis — not independently re-derived here",
            "proof_status": "unresolved",
        },
        "ranks": {},
        "generators": {
            "degrees": [],
            "names": [],
            "note": "No generators claimed yet beyond convention checks and small-graph censuses.",
            "proof_status": "unresolved",
        },
        "syzygies": [],
        "elapsed_sec": time.time() - t0,
        "limitations": [
            "Full degree ladder toward ~81 invariants requires large 5-regular graph censuses and self-duality reductions.",
            "N>=6 exact enumeration for 5-forms is expensive; use sampling + checkpointing.",
            "Do not treat the literature count 81 as an answer key for discovery.",
        ],
    }

    write_json(out_dir / "graphs.json", graph_info)
    write_json(out_dir / "ranks.json", results["ranks"])
    write_json(out_dir / "generators.json", results["generators"])
    write_json(out_dir / "syzygies.json", results["syzygies"])
    write_json(out_dir / "explore_summary.json", results)
    return results


def write_10d_reports(results: dict[str, Any], reports_dir: Path) -> None:
    reports_dir.mkdir(parents=True, exist_ok=True)
    method = r"""# Ten-dimensional methodology

## Object

Chiral (self-dual) 5-form \(F^+_{\mu_1\ldots\mu_5}\) in \(d=10\).

## Conventions (explicit)

- Signature: **Lorentzian** \(\eta=\mathrm{diag}(-1,+1^{\times 9})\).
- Levi-Civita: \(\varepsilon_{0123456789}=+1\).
- Hodge star on lowered 5-forms as in `self_duality.py`.
- On 5-forms in this signature: \(\star^2 = +1\), enabling real self-dual forms.
- Independent generic components: \(C(10,5)=252\); self-dual projection → 126 real DOF.
- Epsilon contractions: allowed by configuration (`allow_epsilon: true`) but not yet used in the low-degree census.

Do **not** mix Euclidean and Lorentzian conventions.

## Strategy

1. Validate Hodge / self-duality numerically.
2. Enumerate small connected 5-regular loopless multigraphs (exact for tiny N).
3. Degree-by-degree evaluation with product quotienting (same algebra as 6D).
4. Checkpoint after each degree; resume safely.
5. Label every scientific claim with proof-status.

## Proof-status vocabulary

- independently reproduced established result
- exact finite-field computation
- exact combinatorial enumeration
- rationally reconstructed identity
- strong computational evidence
- conjectural generator
- unresolved
"""
    (reports_dir / "10d_methodology.md").write_text(method, encoding="utf-8")

    lines = [
        "# Ten-dimensional results",
        "",
        "## Self-duality validation",
        "",
        f"- Passed: **{results['self_duality']['passed']}**",
        f"- Generic components: {results['self_duality']['n_generic_components']}",
        f"- Self-dual DOF: {results['self_duality']['n_self_dual_dof']}",
        f"- ★²: {results['self_duality']['star_squared']}",
        f"- Signature: {results['self_duality']['signature']}",
        f"- Proof-status: `{results['self_duality']['proof_status']}`",
        "",
        "## Graph censuses (5-regular)",
        "",
    ]
    for n, info in sorted(results.get("graphs", {}).items(), key=lambda kv: int(kv[0])):
        lines.append(
            f"- N={n}: {info.get('nonisomorphic_count')} non-isomorphic connected graphs "
            f"({info.get('proof_status')})"
        )
    lines += [
        "",
        "## Generators",
        "",
        f"- {results['generators']}",
        "",
        "## Literature comparison",
        "",
        f"- {results['literature']}",
        "",
        "## Limitations",
        "",
    ]
    for lim in results.get("limitations", []):
        lines.append(f"- {lim}")
    lines.append("")
    (reports_dir / "10d_results.md").write_text("\n".join(lines), encoding="utf-8")
