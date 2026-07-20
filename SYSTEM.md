# How we build a system to solve this (Algebra 2 version)

## Do we need AlphaGo / our own neural net?

**Not first.** AlphaGo’s superpower was: huge search + a brain that guesses *which moves to try*.

Our problem’s “moves” are candidate formulas. The engine we need first is:

1. **Propose** many candidate ingredients  
2. **Test** them on random numbers  
3. **Delete** rewrites / fakes  
4. **Keep** the short list  
5. **Grade** on easy levels where the answer is known  
6. Only then climb to 10D  

That *is* a system. The paper’s “machine learning” is mostly step 2–3 (data + linear algebra).

### Where AlphaGo-style AI comes in later

| AlphaGo | Our project |
|---------|-------------|
| Legal Go moves | Candidate invariant formulas |
| Play games | Plug random fields into formulas |
| Who won? | Was this formula new or a rewrite? |
| Policy network (“try this move”) | Optional neural net: rank which formulas to try first when there are millions |
| Value network | Optional: guess “are we missing ingredients?” |

So: **create our own discovery engine now; optionally add a “policy” model later when 10D search gets too big.**

## What we use (tools)

- **Python + NumPy** — random tests + matrix rank (the checker)
- **opt_einsum** — evaluate big formulas fast
- **Our code** in `src/invariants/` — the system
- **Later (optional):** PyTorch for a ranker network — not required to start 10D

We do **not** need to train AlphaFold-scale models to begin.

## What exists in this repo

| Script | What it does |
|--------|----------------|
| `scripts/run_6d.py` | Checks the known 6D answer (practice with answer key visible) |
| `scripts/run_ladder.py` | **Blind** rediscovery on easy levels, then grades |
| `scripts/run_10d.py` | Builds chiral 5-form on your Mac + low-order discovery |

## Run the system

```bash
cd ~/Projects/UPRSXxXCEL/Research/research
python3 scripts/run_ladder.py   # easy blind levels
python3 scripts/run_6d.py       # medium check
python3 scripts/run_10d.py      # real 10D engine (starter formulas)
```

Why not “finished ~81” in one run: we need many more auto-generated
candidate formulas. The engine and the 10D object are real; the candidate
factory is the remaining bottleneck.

## Build order (your curriculum)

1. Ladder levels with known answers (vector → 4D 2-form → 6D 3-form blind)  
2. Auto-generate candidates (graphs), not hand-typed lists  
3. 10D chiral object + same engine  
4. Only if search explodes: add ML ranker (AlphaGo policy idea)
