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

from .checkpointing import load_checkpoint, save_checkpoint
from .configuration import TensorConfig, load_config
from .generator_selection import discover_10d
from .reporting import write_json
from .self_duality import (
    N_COMPONENTS_5FORM,
    N_SELF_DUAL,
    validate_self_duality,
)

logger = logging.getLogger(__name__)

# External literature targets (Cederwall et al. arXiv:2509.14350). Used only for
# post-hoc comparison — never as an answer key inside discovery.
LITERATURE_HILBERT = {2: 0, 4: 1, 6: 2, 8: 7, 10: 14}
LITERATURE_NEW_BALANCE = {2: 0, 4: 1, 6: 2, 8: 6, 10: 12}


def explore_10d(
    config: TensorConfig | None = None,
    *,
    out_dir: Path | None = None,
    checkpoint_dir: Path | None = None,
    max_degree: int | None = None,
    n_samples: int | None = None,
) -> dict[str, Any]:
    """
    Checkpointed discovery for a self-dual 5-form in d=10.

    Runs blind graph→rank→generator selection with Lorentzian metric contractions
    on self-dual samples. Literature Hilbert numbers are compared only after the fact.
    """
    if config is None:
        config = load_config(Path("configs/self_dual_five_form_10d.yaml"))
    root = Path(".")
    out_dir = out_dir or (root / "outputs" / "10d")
    checkpoint_dir = checkpoint_dir or (out_dir / "checkpoints")
    max_degree = max_degree or config.max_degree
    n_samples = n_samples or config.n_discovery_samples

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
    if not sd.passed:
        raise RuntimeError(f"self-duality validation failed: {sd.message}")

    logger.info(
        "Starting 10D blind discovery max_degree=%s samples=%s seed=%s",
        max_degree,
        n_samples,
        config.seed,
    )
    state = discover_10d(
        max_degree=max_degree,
        n_samples=n_samples,
        seed=config.seed,
        backend="svd",
        cache_dir=checkpoint_dir / "graphs",
    )

    graph_info: dict[str, Any] = {}
    ranks: dict[str, Any] = {}
    for report in state.reports:
        n = report.degree
        graphs = state.graphs_by_degree.get(n, [])
        payload = {
            "n_vertices": n,
            "form_rank": 5,
            "nonisomorphic_count": report.n_graphs,
            "canonical_ids": [g.canonical_id for g in graphs],
            "elapsed_sec": report.elapsed_sec,
            "proof_status": "exact combinatorial enumeration"
            if n <= 6
            else "sampled or partial census",
            "note": "5-regular loopless connected multigraphs; metric η contractions; self-dual samples",
        }
        save_checkpoint(checkpoint_dir, f"graphs_N{n}", payload)
        graph_info[str(n)] = payload
        lit_total = LITERATURE_HILBERT.get(n)
        lit_new = LITERATURE_NEW_BALANCE.get(n)
        ranks[str(n)] = {
            "n_graphs": report.n_graphs,
            "connected_rank": report.connected_rank,
            "rank_P": report.rank_P,
            "rank_PC": report.rank_PC,
            "n_new": report.n_new,
            "selected_graph_ids": report.selected_graph_ids,
            "monomial_names": report.monomial_names,
            "backend": report.backend,
            "proof_status": report.proof_status,
            "literature_singlet_dim": lit_total,
            "literature_new_balance": lit_new,
            "matches_literature_total": (
                None if lit_total is None else report.connected_rank == lit_total
            ),
            "matches_literature_new": (
                None if lit_new is None else report.n_new == lit_new
            ),
        }

    generators = {
        "degrees": state.degrees,
        "names": [g.name for g in state.generators],
        "selected_graph_ids_by_degree": {
            str(r.degree): r.selected_graph_ids for r in state.reports if r.n_new
        },
        "count": len(state.generators),
        "proof_status": "strong computational evidence",
        "note": (
            "Blind metric-graph discovery on self-dual samples. "
            "Not a complete classification of the invariant ring."
        ),
    }

    comparison = {
        "hypothesis_primary_invariants_krull": 81,
        "status": "external literature hypothesis — not independently re-derived here",
        "proof_status": "unresolved",
        "degree_table": ranks,
        "computed_generator_degrees": state.degrees,
        "i4_crosscheck": state.extras.get("i4_crosscheck"),
    }

    # Honest completion gate: what we actually established this run
    established = []
    unresolved = [
        "Full ~81-parameter generating set / Hironaka decomposition",
        "Degree ≥8 complete connected census + new-generator extraction",
        "Epsilon-tensor reduction certificate (metric-only completeness)",
        "Minimal syzygy resolution",
    ]
    for n_str, info in ranks.items():
        if info["matches_literature_total"] is True and info["matches_literature_new"] is True:
            established.append(
                f"Degree {n_str}: connected_rank={info['connected_rank']}, "
                f"n_new={info['n_new']} (matches cited Hilbert / Euler balance)"
            )
        elif info["connected_rank"] == 0 and LITERATURE_HILBERT.get(int(n_str)) == 0:
            established.append(f"Degree {n_str}: vanishing (connected_rank=0)")
        else:
            unresolved.append(
                f"Degree {n_str}: computed connected_rank={info['connected_rank']}, "
                f"n_new={info['n_new']} vs literature "
                f"{info['literature_singlet_dim']}/{info['literature_new_balance']}"
            )

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
        "ranks": ranks,
        "generators": generators,
        "syzygies": [],
        "literature": comparison,
        "established_this_run": established,
        "unresolved": unresolved,
        "elapsed_sec": time.time() - t0,
        "limitations": [
            "Results are finite-sample SVD ranks on self-dual draws — strong computational evidence, not symbolic proof.",
            "Metric-only graphs; epsilon completeness unresolved.",
            "Do not treat the literature count 81 as an answer key for discovery.",
            "Degree ≥8 not completed in the default max_degree=6 run.",
        ],
    }

    write_json(out_dir / "graphs.json", graph_info)
    write_json(out_dir / "ranks.json", ranks)
    write_json(out_dir / "generators.json", generators)
    write_json(out_dir / "syzygies.json", results["syzygies"])
    write_json(out_dir / "explore_summary.json", results)
    save_checkpoint(checkpoint_dir, "discovery_summary", {
        "degrees": state.degrees,
        "ranks": ranks,
        "established_this_run": established,
        "elapsed_sec": results["elapsed_sec"],
    })
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
- Contractions: metric \(\eta\) on every identified index pair (not Kronecker).

## Strategy

1. Validate Hodge / self-duality numerically.
2. Enumerate connected 5-regular loopless multigraphs (exact through N=6).
3. Blind degree-by-degree rank / new-generator selection on self-dual samples.
4. Compare afterward to Cederwall et al. Hilbert targets — never as answer key.
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
        "## Ultimate goal",
        "",
        "Independent Lorentz-scalar polynomial invariants of a real self-dual 5-form "
        "in 10D (generating set + syzygies). Literature Krull dimension ≈ 81 "
        "(Cederwall et al.) — **not achieved in this run**.",
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
        "## Degree ladder (computed this run)",
        "",
        "| N | graphs | connected_rank | n_new | lit singlets | lit new | match? |",
        "|---|--------|----------------|-------|--------------|---------|--------|",
    ]
    for n, info in sorted(results.get("ranks", {}).items(), key=lambda kv: int(kv[0])):
        match = (
            "yes"
            if info.get("matches_literature_total") and info.get("matches_literature_new")
            else (
                "yes (vanish)"
                if info.get("connected_rank") == 0 and info.get("literature_singlet_dim") == 0
                else "NO / partial"
            )
        )
        lines.append(
            f"| {n} | {info.get('n_graphs')} | {info.get('connected_rank')} | "
            f"{info.get('n_new')} | {info.get('literature_singlet_dim')} | "
            f"{info.get('literature_new_balance')} | {match} |"
        )

    gens = results.get("generators", {})
    lines += [
        "",
        "## Generators (blind discovery)",
        "",
        f"- Degrees: `{gens.get('degrees')}`",
        f"- Names: `{gens.get('names')}`",
        f"- Graph IDs: `{gens.get('selected_graph_ids_by_degree')}`",
        f"- Proof-status: `{gens.get('proof_status')}`",
        f"- Note: {gens.get('note')}",
        "",
        "## I4 cross-check",
        "",
        f"- {results.get('literature', {}).get('i4_crosscheck')}",
        "",
        "## Established this run",
        "",
    ]
    for item in results.get("established_this_run", []):
        lines.append(f"- {item}")
    if not results.get("established_this_run"):
        lines.append("- (none yet)")
    lines += ["", "## Unresolved", ""]
    for item in results.get("unresolved", []):
        lines.append(f"- {item}")
    lines += ["", "## Limitations", ""]
    for lim in results.get("limitations", []):
        lines.append(f"- {lim}")
    lines.append("")
    (reports_dir / "10d_results.md").write_text("\n".join(lines), encoding="utf-8")
