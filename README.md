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
- **A Prototype Math Model** — early exploratory draft. Kept for historical context; superseded by Part 1.

---

## Documents

### Core Model
| Document | Description |
|----------|-------------|
| [A Prototype Math Model for Wardley Mapping](A%20Prototype%20Math%20Model%20for%20Wardley%20Mapping.md) | Exploratory prototype introducing S-curve evolution dynamics and game-theoretic extensions |

### Comprehensive Framework
| Document | Description |
|----------|-------------|
| [The Mathematical Framework of Wardley Mapping](The%20Mathematical%20Framework%20of%20Wardley%20Mapping.md) | Extended treatment covering graph theory, game theory, probability, and machine learning applications |

### Progressive Series
| Document | Description |
|----------|-------------|
| [Part 1 - Core Mathematical Model](Part%201%20-%20Core%20Mathematical%20Model%20for%20Wardley%20Mapping.md) | The formal tuple model $\mathcal{M} = (V, E, U, \nu, \varepsilon, t)$ with computed visibility, evolution scoring, and derived metrics |
| [Part 2 - Revised Model: Map Evolution, Not Maturity](Part%202%20-%20Revised%20Wardley%20Map%20Model%3A%20Map%20Evolution%2C%20Not%20Maturity.md) | Refining the evolution axis interpretation |
| [Part 3 - Explaining the Tea Shop Map](Part%203%20-%20Explaining%20the%20Tea%20Shop%20Map%20Using%20Our%20Mathematical%20Model.md) | Applying the model to a classic Wardley Map example |
| [Part 4 - Working Out Evolution Values](Part%204%20-%20Working%20Out%20the%20Evolution%20Value%20for%20a%20Single%20Component.md) | Methods for computing evolution scores |
| [Part 5 - Layer-Based Visibility and Sigmoid Evolution](Part%205%20-%20Extending%20Wardley%20Maps%3A%20Layer-Based%20Visibility%20and%20Sigmoid%20Evolution.md) | Extended model using discrete dependency layers for visibility and a sigmoid (logistic) curve for evolution |
| [Part 6 - Cheat-Sheet Evolution Scoring](Part%206%20-%20Cheat-Sheet%20Evolution%20Scoring.md) | Wardley's canonical 19-row cheat sheet with a formal scoring procedure that produces $\varepsilon(v)$ with uncertainty |

### Model Extensions
| Document | Description |
|----------|-------------|
| [Inertia - Forms of Resistance to Evolution](Inertia%20-%20Forms%20of%20Resistance%20to%20Evolution.md) | Wardley's 17 forms of inertia (14 consumer + 3 supplier) with a structured drag term $c_v(t) = \sum \lambda_i \iota_i$ replacing the single scalar |
| [Multi-Wave Evolution and Punctuated Equilibrium](Multi-Wave%20Evolution%20and%20Punctuated%20Equilibrium.md) | Replaces single-logistic dynamics with multiple diffusion curves per component (generations + chasms), matching Wardley's "evolution is multi-wave" framing |
| [Component Types and the Type Function](Component%20Types%20and%20the%20Type%20Function.md) | Extends the tuple with $\tau: V \to \{A, P, D, K\}$ (Activities, Practices, Data, Knowledge) and type-dependent evolution rates |

### Strategy & Gameplay
| Document | Description |
|----------|-------------|
| [Gameplay Catalogue - 61 Plays with Math-Model Effects](Gameplay%20Catalogue%20-%2061%20Plays%20with%20Math-Model%20Effects.md) | Wardley's 61 gameplays across 12 categories, each mapped to a structured effect on $r_v, c_v, \nu, \varepsilon$ or $E$ |
| [Doctrine - 40 Principles as Model Constraints](Doctrine%20-%2040%20Principles%20as%20Model%20Constraints.md) | Wardley's 40 doctrine principles (4 phases × 6 categories) with math-model readings of each |
| [Strategic Mastery: Creating Math Models for Wardley Mapping Gameplays](Strategic%20Mastery%3A%20Creating%20Math%20Models%20for%20Wardley%20Mapping%20Gameplays.md) | Quantitative approaches to strategic plays and decision-making |
| [Mathematical Models for Wardley Mapping Gameplay](Mathematical%20Models%20for%20Wardley%20Mapping%20Gameplay%3A%20A%20Quantitative%20Approach%20to%20Strategic%20Decision%20Making.md) | Detailed gameplay modeling methodology |

### Specialized Topics
| Document | Description |
|----------|-------------|
| [Wardley Strategy Cycle - Core Model](Wardley%20Strategy%20Cycle%20-%20Core%20Model%20-%20Part%201.md) | Modeling strategic cycles |
| [Wardley Strategy Cycle - Example](Wardley%20Strategy%20Cycle%20-%20Example%20-%20Part%202.md) | Applied example of strategy cycles |
| [Weak Signals & Evolution - Core](Weak%20Signals%20%26%20Evolution%20-%20Core%20-%20Part%201.md) | Detecting and modeling weak signals |
| [Weak Signals & Evolution - Example](Weak%20Signals%20%26%20Evolution%20-%20Example%20-%20Part%202.md) | Applied example of weak signal detection |

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
