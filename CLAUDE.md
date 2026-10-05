# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

Two layers live here:

1. **Theory (`docs/`)** — markdown research documents formalising Wardley Mapping as a quantitative mathematical framework. The core tuple $\mathcal{M} = (V, E, U, \nu, \varepsilon, t)$ and extensions to it.
2. **Practice (`skills/`)** — a portable Claude Code skill that applies the theory to generate Wardley Maps from free-form scenarios, plus a benchmark workspace evaluating the skill against Simon Wardley's own published maps.

There is no build system, `package.json` or Python requirements file. The scripts are plain Node (ESM, no dependencies) and plain Python 3 (stdlib, plus `matplotlib`/`numpy` for the chart renderers and `anthropic` for `model-thinking-bench/run_bench.py`).

## Directory layout

```
/
├── README.md                              # repo index
├── CLAUDE.md                              # this file
├── llms.txt                               # linked doc list for LLM assistants
├── docs/
│   ├── core/                              # canonical Part 1-6 series + Mathematical Framework
│   ├── extensions/                        # inertia / multi-wave / component-types
│   ├── catalogues/                        # Wardley's doctrine (40) + gameplay (61) tables
│   ├── strategy/                          # strategy cycle, weak signals, older gameplay treatments
│   ├── examples/wardley-maps/             # 5 Wardley reference maps rendered as Mermaid wardley-beta
│   └── articles/                          # published write-ups of the benchmark
├── prompts/
│   └── wardley_map_generator.md           # standalone LLM prompt (also benchmarked as "prompt-baseline")
├── scripts/owm_to_mermaid.mjs             # identical copy of the skill's converter — keep both in sync
├── tools/tidy-hook.mjs                    # PostToolUse hook (see below) + tidy-hook.test.mjs
└── skills/
    ├── wardley-map/                       # production skill: SKILL.md + references/ + scripts/*.mjs + evals/
    └── wardley-map-workspace/
        ├── BENCHMARK-REPORT.md            # primary report
        ├── BENCHMARK-METHODOLOGY.md       # how the benchmark works
        ├── BENCHMARK-AUDIT.md             # known grader bugs (A1-A6) and their fixes
        ├── benchmark-25-summary.json      # machine-readable aggregate
        ├── compare_all_25.py              # aggregator
        ├── iteration-1/ … iteration-14/   # 10-14 are the active benchmark corpus; 1-9 are dev history
        ├── arc-kit-compare/               # older head-to-head vs tractorjuice/arc-kit
        ├── competitor-compare/            # N-way comparison: mathmodel, arc-kit, haberlah, prompt-baseline, …
        └── model-thinking-bench/          # model × thinking-mode matrix (calls the Anthropic API)
```

## Commands

```bash
# Structural validation of an OWM map (exit 1 on violations)
node skills/wardley-map/scripts/validate_owm.mjs path/to/map.owm

# Advisory layout check (overlaps, stage-boundary straddling, edge clipping); --strict makes warnings fail
node skills/wardley-map/scripts/check_layout.mjs [--strict] path/to/map.owm

# OWM -> Mermaid wardley-beta
node skills/wardley-map/scripts/owm_to_mermaid.mjs path/to/map.owm > out.mermaid

# Tests for the tidy hook (pass the file; `node --test tools/` fails on Node 23)
node --test tools/tidy-hook.test.mjs
node --test --test-name-pattern='non-wardley' tools/tidy-hook.test.mjs   # single test

# Benchmark a competitor skill against the 25 Wardley reference maps (run from competitor-compare/)
cd skills/wardley-map-workspace/competitor-compare && python3 compare_competitor.py mathmodel
python3 compare_competitor.py prompt-baseline --output-subdir with_prompt-mathmodel
```

## Content structure — `docs/`

- **Core** (`docs/core/`):
  - `part-1-core-model.md` — defines the tuple $\mathcal{M} = (V, E, U, \nu, \varepsilon, t)$ where V is components, E is dependency edges, U ⊆ V is the anchor set, $\nu$ is visibility (Y-axis), $\varepsilon$ is evolution (X-axis).
  - `part-2-evolution-not-maturity.md` through `part-5-layer-visibility-sigmoid.md` — progressive development of the core model.
  - `part-6-cheat-sheet-scoring.md` — Wardley's 19-row cheat sheet with a formal scoring procedure $\varepsilon(v) = \sum_r w_r \cdot m(s_r(v))$ and per-row-disagreement uncertainty.
  - `mathematical-framework.md` — long encyclopedic reference covering graph theory, game theory, probability, and ML applications.

- **Extensions** (`docs/extensions/`):
  - `inertia.md` — Wardley's 17 forms (14 consumer + 3 supplier) replacing the single $c_v(t)$ scalar with a structured sum. Note: FUD, Lobbying, and Bundling are **gameplays**, not inertia — don't confuse the taxonomies.
  - `multi-wave-evolution.md` — per-generation S-curves, cross-generation cannibalisation, chasms.
  - `component-types.md` — extends the tuple with $\tau: V \to \{A, P, D, K\}$ and type-dependent evolution rates.

- **Catalogues** (`docs/catalogues/`):
  - `gameplay.md` — 61 gameplays with structured effects on model parameters.
  - `doctrine.md` — 40 doctrine principles with math-model readings.

- **Strategy** (`docs/strategy/`):
  - `strategy-cycle-core.md` / `-example.md` — purpose → landscape → climate → doctrine → leadership.
  - `weak-signals-core.md` / `-example.md` — detecting imminent evolution.
  - `strategic-mastery.md` / `gameplay-math-models.md` — older companion treatments of gameplay that predate `catalogues/gameplay.md`.

## The skill — `skills/wardley-map/`

- `SKILL.md` is the procedure (Steps 0–6, with 4.5 deep placement, 5.5 validation and 5.6 layout check). `references/` bundles the 19-row cheat sheet, 27 climatic patterns, 40 doctrine principles, 61 gameplays, 17 inertia forms, 3 worked examples and condensed formalism. Scripts are Node because Claude Code ships Node and Python isn't guaranteed; `SKILL.md` invokes them as `node "${CLAUDE_SKILL_DIR}/scripts/…"`.
- `validate_owm.mjs` enforces coordinate range, edge-endpoint declaration and the hard rule $\nu(a) \ge \nu(b)$ for every edge. `check_layout.mjs` is advisory only. Moving a node to satisfy the layout check can break the visibility rule, so re-run the validator afterwards.
- **OWM coordinates are `[visibility, evolution]`**, i.e. `[y, x]`, both in `[0, 1]`. Getting the order backwards is the most common way to produce a map that validates but is wrong.
- `owm_to_mermaid.mjs` always double-quotes names, because Mermaid's `wardley-beta` lexer treats keyword prefixes (`label…`, `evolve…`) and pure-digit names as errors. It drops OWM-only directives and links to undeclared endpoints.

## Tidy hook

`.claude/settings.json` runs `node tools/tidy-hook.mjs` after every `Write`/`Edit`. For `.md` files it rewrites only fenced ```` ```mermaid ```` blocks whose body starts with `wardley-beta`, leaving prose and OWM blocks byte-identical. A `.mmd` file is tidied whole. Tidying shells out to `npx --yes github:tractorjuice/wardley-maps-mermaid wardley-tidy`, which you can override with `WARDLEY_TIDY_PKG`. That means network access and a fetch on first use, and it can move label offsets in a Mermaid block right after you write it. The hook always exits 0 and silently leaves the file alone if tidying fails.

## Benchmark workspace — `skills/wardley-map-workspace/`

- Iterations 10–14 hold the 25 `(wardley-reference.owm, with_skill/run-1/outputs/output.md)` pairs drawn from `swardley/WARDLEY-MAP-REPOSITORY`. Every comparator imports `parse_owm` and `fuzzy_match` from `iteration-10/compare.py`, so a parser change there moves every benchmark number.
- In a benchmark run, a subagent gets only a scenario prompt and must **not** read `wardley-reference.owm` (the blind contract in `BENCHMARK-METHODOLOGY.md` §2a).
- **Hardcoded paths:** `compare_all_25.py`, `compare_all_*.py`, `grade.py`, `compare_graph.py`, `compare_inversions.py`, `iteration-10/compare.py`, `arc-kit-compare/*.py` and a few others use `/workspaces/wardleymap_math_model/…` (a Codespace/devcontainer path), so they fail in a local checkout unless you patch them or symlink that path. `competitor-compare/compare_competitor.py` resolves paths relative to itself and runs anywhere.
- **Comparators overwrite committed results.** `compare_all_25.py` writes `benchmark-25-summary.json` and `compare_competitor.py` writes `competitor-compare/<name>/competitor-summary-<name>.json`. Some committed summaries predate the A5 grader fixes in `compare.py`, so a re-run changes them. Check `git diff` afterwards and only commit the regenerated numbers on purpose.

## Key mathematical concepts

- **Visibility (Y-axis)**: $\nu(v) = 1/(1+d(v))$ where $d(v)$ is graph distance. The production skill uses an exponential variant $\nu(v) = e^{-0.6 \cdot d(v)}$ by default (calibrated from the 25-map benchmark to reduce systematic visibility over-placement).
- **Evolution (X-axis)**: $\varepsilon(v) \in [0,1]$ mapping to stages — Genesis $[0, 0.25)$, Custom Built $[0.25, 0.5)$, Product (+rental) $[0.5, 0.75)$, Commodity (+utility) $[0.75, 1]$. Canonical determination is by cheat sheet, not by time — see the climatic pattern *"you cannot measure evolution over time or adoption."*
- **Evolution dynamics**: logistic S-curve $d\varepsilon/dt = r\varepsilon(1-\varepsilon)$ labeled as a stylized extension; Wardley's climatic patterns say evolution cannot be measured over time.
- **Dependencies**: directed graph where $(a,b) \in E$ means "a depends on b", with the hard constraint $\nu(a) \ge \nu(b)$.
- The decision metrics (differentiation pressure, commodity leverage, dependency risk) are this repo's heuristics, not canonical Wardley concepts. Keep labelling them that way.

## Working with this repository

When editing documents:

- Mathematical notation uses GitHub-native LaTeX: inline `$...$`, display `$$...$$`.
- Maintain consistent terminology: *evolution* (X-axis), *visibility* (Y-axis), *components* (nodes).
- Markdown filenames are kebab-case. Cross-document links between `docs/` subdirectories use relative paths (e.g., `../catalogues/gameplay.md`).
- When adding a new doc, also add it to `README.md`'s table and to `llms.txt`.

When editing the skill:

- The validator script is the first-line defense against structural errors — keep it authoritative for OWM well-formedness.
- `scripts/owm_to_mermaid.mjs` and `skills/wardley-map/scripts/owm_to_mermaid.mjs` are identical copies; change both.
- Any change to placement behaviour (seeds, density guidance, cheat-sheet weighting) should be checked against the 25-map benchmark before being committed.
