# Mathematical Models for Wardley Mapping

This repository contains research and theoretical frameworks for formalizing [Wardley Mapping](https://medium.com/wardleymaps) as a mathematical model. The goal is to transform Wardley Maps from a purely visual and qualitative strategic tool into a quantitative framework that enables computation, simulation, and data-driven strategic decision-making.

## What is Wardley Mapping?

Wardley Mapping, created by Simon Wardley, is a visual technique for mapping business strategy. A Wardley Map plots components on two axes:

- **Y-axis (Visibility)**: How close a component is to the end user
- **X-axis (Evolution)**: How mature/commoditized a component is, from Genesis → Custom → Product → Commodity

Components are connected by dependency relationships forming a value chain.

## The Mathematical Approach

This repository explores how to formalize these concepts mathematically. A Wardley Map becomes:

$$\mathcal{M} = (V, E, U, \nu, \varepsilon, t)$$

Where:
- $V$ = set of components
- $E \subseteq V \times V$ = directed dependency edges
- $U \subseteq V$ = anchor set (one or more user-need nodes)
- $\nu: V \to [0,1]$ = visibility function (Y-axis)
- $\varepsilon: V \to [0,1]$ = evolution function (X-axis)
- $t$ = time parameter for dynamics

This formalization enables:
- Generating maps from data
- Validating maps with constraints
- Quantifying strategic positions
- Simulating evolution over time
- Computing decision metrics (differentiation pressure, commodity leverage, dependency risk)

## Recommended Reading Order

The repo has 20+ docs. Not all are on the critical path. If you're new:

**Start here (the core):**
1. **Part 1** — Core Mathematical Model. Read this first. Everything else extends it.
2. **Part 2** — "Map Evolution, Not Maturity". Deepens the evolution axis interpretation.
3. **Part 3** — Tea Shop worked example. Grounds the math in a concrete map.
4. **Part 4** — Simple evolution scoring via ubiquity + certainty.
5. **Part 5** — Layer-based visibility and sigmoid evolution (refinements).
6. **Part 6** — Canonical cheat-sheet scoring (19 rows). Supersedes Part 4's 2-factor method.

**Then pick the extensions relevant to your problem:**
- **Inertia** — if you're modelling why components get stuck (structured drag).
- **Multi-Wave Evolution** — if your horizon spans multiple technology generations.
- **Component Types** — if you want to distinguish Activities / Practices / Data / Knowledge.

**Then the strategy layer:**
- **Gameplay Catalogue** — reference list of the 61 plays with math-model effects.
- **Doctrine** — the 40 universal principles and how they constrain the model.
- **Strategic Mastery** and **Mathematical Models for Wardley Mapping Gameplay** — older, longer companion treatments (applied and formal respectively) to the Gameplay Catalogue.

**Specialised applications (read if the topic applies):**
- **Weak Signals & Evolution** — detecting when evolution is about to happen.
- **Wardley Strategy Cycle** — formalising the OODA-loop-style strategy cycle.

**Not on the main path:**
- **The Mathematical Framework** — long encyclopedic reference (1200+ lines). Browse for specific techniques, don't read front-to-back.

---

## Documents

All docs live under [`docs/`](docs/) organised by role.

### Core — the canonical progressive series (`docs/core/`)
| Document | Description |
|----------|-------------|
| [Part 1 — Core Mathematical Model](docs/core/part-1-core-model.md) | The formal tuple model $\mathcal{M} = (V, E, U, \nu, \varepsilon, t)$ with computed visibility, evolution scoring, and derived metrics |
| [Part 2 — Evolution, Not Maturity](docs/core/part-2-evolution-not-maturity.md) | Refining the evolution axis interpretation |
| [Part 3 — The Tea Shop Worked Example](docs/core/part-3-tea-shop-example.md) | Applying the model to a classic Wardley Map |
| [Part 4 — Single-Component Evolution](docs/core/part-4-single-component-evolution.md) | Methods for computing evolution scores |
| [Part 5 — Layer Visibility & Sigmoid Evolution](docs/core/part-5-layer-visibility-sigmoid.md) | Discrete dependency layers for visibility and a sigmoid logistic curve for evolution |
| [Part 6 — Cheat-Sheet Evolution Scoring](docs/core/part-6-cheat-sheet-scoring.md) | Wardley's canonical 19-row cheat sheet with a formal scoring procedure that produces $\varepsilon(v)$ with uncertainty |
| [Mathematical Framework](docs/core/mathematical-framework.md) | Long encyclopedic reference (1200+ lines). Browse for specific techniques, don't read front-to-back |

### Extensions — additions to the Part-1 tuple (`docs/extensions/`)
| Document | Description |
|----------|-------------|
| [Inertia](docs/extensions/inertia.md) | Wardley's 17 forms of inertia (14 consumer + 3 supplier) with a structured drag term $c_v(t) = \sum \lambda_i \iota_i$ replacing the single scalar |
| [Multi-Wave Evolution](docs/extensions/multi-wave-evolution.md) | Replaces single-logistic dynamics with multiple diffusion curves per component (generations + chasms) |
| [Component Types](docs/extensions/component-types.md) | Extends the tuple with $\tau: V \to \{A, P, D, K\}$ (Activities, Practices, Data, Knowledge) and type-dependent evolution rates |

### Catalogues — reference tables Wardley published (`docs/catalogues/`)
| Document | Description |
|----------|-------------|
| [Gameplay](docs/catalogues/gameplay.md) | Wardley's 61 gameplays across 12 categories, each mapped to a structured effect on $r_v, c_v, \nu, \varepsilon$ or $E$ |
| [Doctrine](docs/catalogues/doctrine.md) | Wardley's 40 doctrine principles (4 phases × 6 categories) with math-model readings of each |

### Strategy — cycles, signals, older gameplay treatments (`docs/strategy/`)
| Document | Description |
|----------|-------------|
| [Strategy Cycle — Core](docs/strategy/strategy-cycle-core.md) | Modeling strategic cycles |
| [Strategy Cycle — Example](docs/strategy/strategy-cycle-example.md) | Applied example of strategy cycles |
| [Weak Signals — Core](docs/strategy/weak-signals-core.md) | Detecting and modeling weak signals |
| [Weak Signals — Example](docs/strategy/weak-signals-example.md) | Applied example of weak signal detection |
| [Strategic Mastery](docs/strategy/strategic-mastery.md) | Older companion treatment of gameplay selection (predates `catalogues/gameplay.md`) |
| [Gameplay Math Models](docs/strategy/gameplay-math-models.md) | Older quantitative treatment of plays (predates `catalogues/gameplay.md`) |

### Tools & Prompts
| Document | Description |
|----------|-------------|
| [Wardley Map Generator Prompt](prompts/wardley_map_generator.md) | AI prompt for generating Wardley Maps in OWM format compatible with [create.wardleymaps.ai](https://create.wardleymaps.ai) |
| [`wardley-map` Claude Code skill](skills/wardley-map/) | Portable skill package — copy to `~/.claude/skills/` and invoke `/wardley-map <scenario>`. `SKILL.md` + `references/` (7 files: climatic-patterns, doctrine, evolution-stages, gameplay-patterns, inertia, mapping-examples, mathematical-models) |

## Key Formulas

**Visibility from graph distance:**

$$\nu(v) = \frac{1}{1 + d(v)}$$

where $d(v)$ is the shortest path length from user to component.

**Evolution dynamics (logistic S-curve):**

$$\frac{d\varepsilon}{dt} = r(t) \cdot \varepsilon(t) \cdot (1 - \varepsilon(t))$$

where $r(t)$ incorporates market forces and strategic actions.

> **Caveat.** Wardley's climatic patterns state *"you cannot measure evolution over time or adoption."* The ODE above is a stylized extension for simulation and scenario exploration, not a Wardley-endorsed forecast model.

**Evolution stages** (canonical names, quartile bands are conventional):
- Genesis: $[0, 0.25)$
- Custom Built: $[0.25, 0.50)$
- Product (+rental): $[0.50, 0.75)$
- Commodity (+utility): $[0.75, 1.0]$

**Decision metrics** (heuristics proposed in this repo — not canonical Wardley concepts):
- Differentiation pressure: $D(v) = \nu(v) \cdot (1 - \varepsilon(v))$
- Commodity leverage: $K(v) = (1 - \nu(v)) \cdot \varepsilon(v)$
- Dependency risk: $R(a,b) = \nu(a) \cdot (1 - \varepsilon(b))$

## License

This repository contains theoretical research and documentation.

## Acknowledgments

Based on the Wardley Mapping framework created by Simon Wardley.
