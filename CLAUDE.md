# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with this repository.

## Repository Overview

Two layers live here:

1. **Theory (`docs/`)** — markdown research documents formalising Wardley Mapping as a quantitative mathematical framework. The core tuple $\mathcal{M} = (V, E, U, \nu, \varepsilon, t)$ and extensions to it.
2. **Practice (`skills/`)** — a portable Claude Code skill that applies the theory to generate Wardley Maps from free-form scenarios, plus a benchmark workspace evaluating the skill against Simon Wardley's own published maps.

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
│   └── strategy/                          # strategy cycle, weak signals, older gameplay treatments
├── prompts/
│   └── wardley_map_generator.md           # standalone LLM prompt
└── skills/
    ├── wardley-map/                       # production skill: SKILL.md + references/ + scripts/validate_owm.py + evals/
    └── wardley-map-workspace/             # iteration history + 25-map benchmark + arc-kit-compare
        ├── BENCHMARK-REPORT.md            # primary report
        ├── BENCHMARK-METHODOLOGY.md       # how the benchmark works
        ├── benchmark-25-summary.json      # machine-readable aggregate
        ├── compare_all_25.py              # aggregator
        ├── iteration-1/ … iteration-14/   # 10-14 are the active benchmark corpus; 1-9 are dev history
        └── arc-kit-compare/               # head-to-head vs tractorjuice/arc-kit's wardley-mapping skill
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

## The skill and workspace — `skills/`

- `skills/wardley-map/` is the production skill. `SKILL.md` is the procedure (7 steps). `references/` bundles the 19-row cheat sheet, 27 climatic patterns, 40 doctrine principles, 61 gameplays, 17 inertia forms, 3 worked examples, condensed formalism. `scripts/validate_owm.py` is a structural validator (enforces $\nu(a) \ge \nu(b)$, coordinate range, edge-endpoint declaration).
- `skills/wardley-map-workspace/` contains every iteration of the skill and the benchmark. Iterations 10-14 are the active benchmark corpus (25 maps from `swardley/WARDLEY-MAP-REPOSITORY`); iterations 1-9 are skill-development history. `BENCHMARK-REPORT.md` is the primary summary; `BENCHMARK-METHODOLOGY.md` documents how the benchmark works.

## Key mathematical concepts

- **Visibility (Y-axis)**: $\nu(v) = 1/(1+d(v))$ where $d(v)$ is graph distance. The production skill uses an exponential variant $\nu(v) = e^{-0.6 \cdot d(v)}$ by default (calibrated from the 25-map benchmark to reduce systematic visibility over-placement).
- **Evolution (X-axis)**: $\varepsilon(v) \in [0,1]$ mapping to stages — Genesis $[0, 0.25)$, Custom Built $[0.25, 0.5)$, Product (+rental) $[0.5, 0.75)$, Commodity (+utility) $[0.75, 1]$. Canonical determination is by cheat sheet, not by time — see the climatic pattern *"you cannot measure evolution over time or adoption."*
- **Evolution dynamics**: logistic S-curve $d\varepsilon/dt = r\varepsilon(1-\varepsilon)$ labeled as a stylized extension; Wardley's climatic patterns say evolution cannot be measured over time.
- **Dependencies**: directed graph where $(a,b) \in E$ means "a depends on b", with the hard constraint $\nu(a) \ge \nu(b)$.

## Working with this repository

When editing documents:

- Mathematical notation uses GitHub-native LaTeX: inline `$...$`, display `$$...$$`.
- Maintain consistent terminology: *evolution* (X-axis), *visibility* (Y-axis), *components* (nodes).
- Markdown filenames are kebab-case. Cross-document links between `docs/` subdirectories use relative paths (e.g., `../catalogues/gameplay.md`).
- When adding a new doc, also add it to `README.md`'s table and to `llms.txt`.

When editing the skill:

- The validator script is the first-line defense against structural errors — keep it authoritative for OWM well-formedness.
- Benchmark numbers are reproduced by `skills/wardley-map-workspace/compare_all_25.py` against the committed reference `.owm` files; any change to placement behaviour should be checked against the benchmark before being committed.
