# Doctrine — 40 Principles as Model Constraints

Wardley's **doctrine** is a set of universal principles — things a strategist should do **regardless of the map**, in contrast to gameplays which depend on context. The mature form from Simon Wardley's [Medium book](https://medium.com/wardleymaps) organises **40 principles** into **4 phases** (progressive maturity stages) and **6 categories** (Communication, Development, Learning, Leading, Operations, Structure).

This doc presents the full list with a math-model reading of each: either how it constrains the mapping process, how it modifies parameters in the dynamics, or how it scores map quality. Not every principle has a mathematical encoding — some are organisational practices that sit outside the model. Where that's true, the entry says so.

> **Historical note.** Wardley's [2016 blog post](https://blog.gardeviance.org/2016/05/wardleys-doctrine.html) on doctrine listed only ~15–16 principles with no phase structure. The 40-principle / 4-phase / 6-category taxonomy is the mature form from his Medium book. If a paper cites the 2016 blog, expect ~15 principles; if it cites the current Medium version, expect 40.

---

## 1. The four phases

Doctrine progresses through four maturity phases. An organisation is rarely uniform — parts may be in Phase III while others are still in Phase I.

| Phase | Name | Meaning |
|---|---|---|
| I | **Stop Self-Destructive Behaviour** | Get basics right: alignment, language, transparency |
| II | **Becoming More Context Aware** | Understand users, inertia, failure; act appropriately |
| III | **Better for Less** | Optimise flow, seek talent, continuous improvement |
| IV | **Continuously Evolving** | Design for permanent change; ecosystems, no core |

Doctrine is cumulative — a Phase III org still applies Phase I and II principles.

---

## 2. The 40 principles

### Phase I — Stop Self-Destructive Behaviour (9)

| # | Principle | Category | Description | Math-model reading |
|---|---|---|---|---|
| 1 | Focus on user needs | Development | Prioritise stakeholder requirements | Constrain $U$ to real user-need nodes; reject maps anchored at internal outputs |
| 2 | Use a systematic mechanism of learning | Learning | Bias towards data | Calibrate $\varepsilon$ against observed signals (Part 6 cheat sheet); update priors in Part 1 §6 |
| 3 | Use a common language | Communication | Necessary for collaboration | Standardise the notation ($\nu, \varepsilon, \tau$); the notation sweep in this repo is itself an application of this principle |
| 4 | Be transparent | Communication | Bias towards open | Make $w_r$ weights in cheat-sheet scoring visible; publish $\iota_i$ inertia severities |
| 5 | Challenge assumptions | Communication | Speak up and question | Use Part 1 §6 Beta priors to surface disagreement on coordinates |
| 6 | Remove bias and duplication | Development | Eliminate redundancy and prejudiced thinking | Check $V$ for duplicate components; check $E$ for implied duplicates |
| 7 | Use appropriate methods | Development | e.g. agile vs lean vs six sigma | Method choice depends on $\tau$ and $\varepsilon$ — agile for Genesis/Custom Activities, six sigma for Commodity |
| 8 | Focus on high situational awareness | Communication | Understand what is being considered | The whole map is the situational-awareness artifact; prioritise completing $V$ and $E$ |
| 9 | Think small (as in know the details) | Operations | Detailed knowledge of the system | Decompose coarse components into finer-grained $V$; validate with cheat sheet row by row |

### Phase II — Becoming More Context Aware (15)

| # | Principle | Category | Description | Math-model reading |
|---|---|---|---|---|
| 10 | Know your users | Development | Customers, shareholders, regulators, staff | Multi-anchor $U$ rather than a single $u$; different anchors give different visibility orderings |
| 11 | Focus on the outcome not a contract | Development | e.g. worth-based development | Value $J$ should be over map-state outcomes, not action budgets |
| 12 | Use appropriate tools | Development | e.g. mapping, financial models | Part 1 model is *a* tool; don't force every analysis through it |
| 13 | Manage inertia | Operations | Existing practices, political capital, previous investment | Direct pointer to the [Inertia doc](../extensions/inertia.md) — $c_v(t)$ must be actively monitored |
| 14 | Manage failure | Operations | Address unsuccessful outcomes constructively | Treat $\varepsilon$ regressions as signal, not noise |
| 15 | Think FIRE (fast, inexpensive, restrained, elegant) | Development | Formerly FIST | Applied to experimentation and gameplay #37 |
| 16 | Be pragmatic | Development | Results over ideology | Override any of these principles when map evidence warrants |
| 17 | Effectiveness over efficiency | Operations | Impact over resource optimisation | Penalise pure cost-minimisation in $J$ when it harms user visibility $\nu$ |
| 18 | A bias towards action | Learning | Learn by playing the game | Pick a play and observe the map response; don't optimise forever |
| 19 | Think aptitude and attitude | Structure | Capability and mindset | Organisational, outside the model |
| 20 | Think small (as in teams, two pizza) | Structure | Small cross-functional teams | Organisational; affects $r_v$ indirectly through delivery speed |
| 21 | Distribute power and decision making | Structure | Decentralise authority | Organisational; relates to gameplay #4 (Structure & Culture) |
| 22 | Use standards where appropriate | Development | Apply standardisation selectively | Only standardise components with $\varepsilon \ge 0.75$; see Part 1 §4.1 for bands |
| 23 | Strategy is iterative not linear | Leading | Fast reactive cycles | Multi-step play selection; see Gameplay doc §3 on sequences |
| 24 | Move fast | Leading | "Imperfect plan today beats perfect plan tomorrow" | Raise $u_v(t)$ magnitude; accept uncertainty $\text{Var}(\varepsilon)$ |

### Phase III — Better for Less (11)

| # | Principle | Category | Description | Math-model reading |
|---|---|---|---|---|
| 25 | Set exceptional standards | Operations | Great is not good enough | Raise threshold stage for acceptance from Product to Commodity where feasible |
| 26 | Optimise flow | Operations | Remove bottlenecks | Gameplay #5; applied as $r_v$ boost on own chain |
| 27 | Do better with less | Operations | Continual improvement | Minimise resource use per unit $\varepsilon$ gained |
| 28 | Seek the best | Structure | Recruit and retain top talent | Organisational; relates to gameplay #38 (Centres of Gravity) |
| 29 | A bias towards the new | Learning | Be curious, take risks | Raise exploration weight in Multi-Wave doc's generation search |
| 30 | Provide purpose, mastery & autonomy | Structure | Meaningful work and self-direction | Organisational |
| 31 | Strategy is complex | Leading | There will be uncertainty | Use Part 1 §6 uncertainty distributions, not point estimates |
| 32 | Commit to the direction, be adaptive along the path | Leading | "Crossing the river by feeling the stones" | Fix a gameplay *sequence*, not individual plays |
| 33 | There is no one culture | Structure | e.g. Pioneers, Settlers, Town Planners | Different $\varepsilon$ bands of your map need different cultures; partition $V$ by $\varepsilon$-band and assign leadership style |
| 34 | Be humble | Leading | Listen, be selfless, have fortitude | Organisational |
| 35 | Be the owner | Leading | Take responsibility | Organisational |

### Phase IV — Continuously Evolving (5)

| # | Principle | Category | Description | Math-model reading |
|---|---|---|---|---|
| 36 | Think big | Leading | Inspire others, provide direction | $U$ should anchor on *ambitious* user needs, not existing products |
| 37 | Exploit the landscape | Leading | Leverage environmental opportunities | Active play selection across the whole $V$, not just own components |
| 38 | There is no core | Leading | Everything is transient | Accept that today's Commodity was yesterday's Genesis; plan for generation transitions (Multi-Wave doc) |
| 39 | Listen to your ecosystems | Learning | Act as future-sensing engines | Gameplay #43 (Sensing Engines / ILC) |
| 40 | Design for constant evolution | Structure | Build adaptability in | Treat $\varepsilon$ and $V$ as time-varying; avoid architectures that assume fixed maps |

**Totals check:** 9 + 15 + 11 + 5 = **40** ✓

---

## 3. Using doctrine as a map-quality score

Given a map $\mathcal{M}$ and an organisational state, compute a doctrine score:

$$S_{\text{doctrine}}(\mathcal{M}, \text{org}) = \sum_{i=1}^{40} w_i \cdot \chi_i(\mathcal{M}, \text{org})$$

Where:

- $\chi_i(\mathcal{M}, \text{org}) \in \{0, 1\}$ indicates whether principle $i$ is satisfied.
- $w_i$ weights principles by phase — Phase I principles weight heaviest because failing them is self-destructive.

A default weighting: $w_i = 1/\text{phase}(i)$. Phase I principles weight 1.0, Phase IV weight 0.25.

This gives a single 0–40 scalar that correlates (claimed by Wardley, not validated) with strategic maturity. Treat it as a diagnostic prompt, not a benchmark.

---

## 4. Doctrine vs. gameplay: the key distinction

| | Doctrine | Gameplay |
|---|---|---|
| Number | ~40 | 61 |
| Context-dependent | **No** (universal) | **Yes** |
| When applied | Always | When the map suggests it |
| Effect on math | Constraints on the mapping process | Transformations of the map |
| Source | Wardley's [Medium book](https://medium.com/wardleymaps) | [Gardeviance 2015](https://blog.gardeviance.org/2015/05/on-61-different-forms-of-gameplay.html) |

An organisation that applies a gameplay without satisfying Phase I doctrine is pretending — it's picking advanced moves on a broken foundation. The [Strategic Mastery](../strategy/strategic-mastery.md) doc covers gameplay selection; the current doc complements it by describing the always-on substrate.

---

## 5. Caveats

1. **Phase/category assignments are not stable.** Cross-referencing Wardley's current Medium book against the 2016 Gardeviance post shows several principles shifting phase or category over time. For two principles in particular — "Be transparent" (Phase I vs II) and "Think big" (Phase III vs IV) — the placement has varied across versions. The assignments in this doc reflect the most recent snapshot but should be verified against Wardley's current text.

2. **"Think small" appears twice on purpose.** #9 ("as in know the details", Phase I Operations) and #20 ("as in teams, two pizza", Phase II Structure) are distinct principles with the same name. Not a typo.

3. **FIRE, not FIST.** Wardley updated the acronym from FIST (fast, inexpensive, simple, tiny) to FIRE (fast, inexpensive, restrained, elegant). Older documentation may use FIST.

4. **Doctrine is claims, not proofs.** Wardley derived doctrine from his own consulting experience and a reading of military strategy, particularly Sun Tzu. It is not empirically validated as a set of principles whose adoption correlates with organisational outcomes. Use accordingly.

5. **The map model cannot fully encode doctrine.** Several principles (#19, #20, #28, #30, #34, #35) are about organisational practices that sit outside the $(V, E, U, \tau, \nu, \varepsilon, t)$ tuple. The "Math-model reading" column honestly marks these "organisational, outside the model" rather than pretending the math captures them.
