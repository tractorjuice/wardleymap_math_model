# Mathematical Models for Wardley Mapping

A condensed, self-contained formalisation of Wardley Mapping. Detailed treatments of each extension are in the [parent repo](https://github.com/tractorjuice/wardleymap_math_model); this file distils what the skill needs to reason about maps rigorously.

---

## 1. The tuple

A Wardley Map is a tuple

$$\mathcal{M} = (V, E, U, \nu, \varepsilon, t)$$

- **V** = set of components (capabilities, activities, practices, data, systems, suppliers, knowledge).
- **E ⊆ V × V** = directed dependency edges. `(a, b) ∈ E` means "a depends on b".
- **U ⊆ V** = anchor set — one or more user-need nodes. Real maps often have multiple user types (e.g., customer AND artisan in a marketplace).
- **ν: V → [0, 1]** = visibility function. Higher = closer to the user.
- **ε: V → [0, 1]** = evolution function. Higher = more commoditised.
- **t** = time (optional; used only for dynamics).

Optional type function: **τ: V \ U → {A, P, D, K}** — Activity, Practice, Data, Knowledge.

---

## 2. Visibility ν (Y-axis)

**Visibility is a judgment primitive**, not a topological property. Wardley treats it as a natural outcome of value-chain position, manually adjusted as needed.

### Seeding from distance

$$d(v) = \min_{u \in U} \{\text{path length}(u \to v)\}$$

Three seed options:

| Option | Formula | Use when |
|---|---|---|
| Reciprocal decay | $\nu(v) = 1/(1 + d(v))$ | Default — smooth, parameter-free. |
| Exponential decay | $\nu(v) = e^{-\alpha d(v)}$ | Deep graphs where vertical spread matters. |
| Constraint optimisation | Solve $\min \sum_{(a,b)} (\nu(a) - \nu(b) - \delta)^2$ subject to $0 \le \nu \le 1$ | Graphs with shortcuts that violate the depth rule. |

### Hard rule

For every edge `(a, b) ∈ E`:

$$\nu(a) \ge \nu(b)$$

Components must sit above their dependencies. If the seed violates this, move to constraint optimisation or adjust by hand.

### Override

The mapper may adjust any `ν(v)` by hand to reflect value-chain judgment:
- Raise `ν` for a component the user thinks about directly (e.g., branded payment widget).
- Lower `ν` for a component that's architecturally invisible (e.g., a CDN).

---

## 3. Evolution ε (X-axis)

**Evolution ≠ maturity.** Wardley's canonical position: *"you cannot measure evolution over time or adoption"*. Evolution is a property of a *market's* collective progress against ubiquity and certainty, not a clock.

### Stages

| Stage | Band | Key descriptor |
|---|---|---|
| Genesis | [0, 0.25) | Rare, poorly understood, high-risk exploration |
| Custom Built | [0.25, 0.5) | Emerging learning, bespoke solutions |
| Product (+rental) | [0.5, 0.75) | Rapidly increasing consumption, fit-for-purpose |
| Commodity (+utility) | [0.75, 1.0] | Widespread, standardised, commoditised |

The parenthesised suffixes matter: Stage III covers *products AND rental/licensing*; Stage IV covers *commodities AND utility services*.

### Scoring

**Canonical method: the cheat sheet** (see `evolution-stages.md`). For each of 19 rows, pick the stage (1–4) that best describes the component. Convert via band midpoints:

$$m(s) = \frac{s - \tfrac{1}{2}}{4}$$

- Stage I → 0.125
- Stage II → 0.375
- Stage III → 0.625
- Stage IV → 0.875

Aggregate:

$$\varepsilon(v) = \sum_{r \in R} w_r \cdot m(s_r(v)), \quad \sum_r w_r = 1$$

Default: unweighted mean over all 19 rows (or a quick 4-row subset).

### Uncertainty

Variance across rows = uncertainty:

$$\mathrm{Var}(\varepsilon) = \sum_r w_r \cdot (m(s_r) - \varepsilon)^2$$

High variance means the component is in transition (e.g., ubiquity has jumped but certainty hasn't caught up). Plot as a Beta-distributed region, not a point.

---

## 4. Dynamics (stylised extension — not Wardley-endorsed)

> **Caveat.** Wardley's climatic pattern "you cannot measure evolution over time or adoption" directly conflicts with any ODE-based forecast. Use dynamics for **scenario exploration**, never prediction.

### Logistic S-curve

$$\frac{d\varepsilon_v}{dt} = r_v(t) \cdot \varepsilon_v(t) \cdot (1 - \varepsilon_v(t))$$

Slow at extremes, fast in the middle. Produces the canonical S-shape.

### Strategy decomposition

$$r_v(t) = r_{0,v} + u_v(t) - c_v(t)$$

- `r₀`: baseline market pressure
- `u(t)`: strategic actions (named gameplays — see `gameplay-patterns.md`)
- `c(t)`: inertia (17 structured forms — see `inertia.md`)

Clamp `r_v(t) ≥ 0` — evolution is monotonic-forward per the climatic patterns.

### Multi-wave evolution

A component often has multiple generations (e.g., compute: mainframe → minicomputer → PC → server → VM → cloud). Each has its own S-curve. Aggregate evolution:

$$\varepsilon(v, t) = \frac{\sum_g A_g(t) \cdot \varepsilon_g}{\sum_g A_g(t)}$$

where $A_g(t)$ is the adoption fraction of generation $g$ and $\varepsilon_g$ is the stage it tops out at. Chasms appear between generations — periods where the old gen is saturating but the new gen hasn't taken off.

---

## 5. Derived heuristics

> **These three metrics are proposed by this skill's math model, not canonical Wardley concepts.** Treat as attention prompts.

| Metric | Formula | High value signals |
|---|---|---|
| Differentiation pressure | $D(v) = \nu(v) \cdot (1 - \varepsilon(v))$ | Visible + immature = advantage zone |
| Commodity leverage | $K(v) = (1 - \nu(v)) \cdot \varepsilon(v)$ | Deep + mature = outsource / utility |
| Dependency risk | $R(a,b) = \nu(a) \cdot (1 - \varepsilon(b))$ | Visible component on fragile foundation |

---

## 6. Inertia as structured drag

Part 1's `c_v(t)` scalar flattens 17 distinct forms of inertia Wardley enumerates:

$$c_v(t) = \sum_{i=1}^{17} \lambda_i \cdot \iota_i(v, t)$$

where `ι_i ∈ [0, 1]` is the severity of inertia form `i` for component `v`, and `λ_i ≥ 0` is its weight. See `inertia.md` for the full list and a decomposition into consumer-side (14 forms) vs supplier-side (3 forms).

---

## 7. Component types and co-evolution

One of Wardley's climatic patterns: **practices co-evolve with activities**. Formally:

$$\forall p \text{ with } \tau(p) = P : \exists\, a \text{ with } \tau(a) = A, \, (a, p) \in E, \, \mathrm{corr}(\varepsilon_a(t), \varepsilon_p(t)) > 0$$

Type-dependent evolution rates (typical ordering):

$$r_A > r_P > r_D > r_K$$

Activities evolve fastest (direct customer demand). Knowledge slowest (careers-timescale acceptance cycles).

---

## 8. Gameplay as transformations

A gameplay `G: M → M` is a transformation on the map restricted to a target set `T_G ⊆ V`. Mechanisms align with model parameters:

| Mechanism | Primary effect | Example play |
|---|---|---|
| `r_v` boost | Accelerate evolution | Open Approaches (#15) |
| `r_v` suppress | Decelerate evolution | Patents & IPR (#20) |
| `c_v` up on competitor | Raise rival's drag | Reinforcing inertia (#50) |
| `ν` shift | Change user perception | Bundling (#8) |
| Edge mutation | Add/remove dependencies | Two factor (#45) |

All 61 gameplays catalogued with mechanisms in `gameplay-patterns.md`.

---

## 9. Doctrine as constraints

Doctrine principles are universal (context-free) constraints on the *mapping process* rather than the map itself. Examples:

- **Focus on user needs** (#1) → constrain `U` to real user-need nodes.
- **Know your users** (#10) → use `|U| ≥ 2` when relevant (multi-anchor).
- **Manage inertia** (#13) → monitor `c_v(t)` actively, don't bundle into one scalar.
- **Think small** (#9) → decompose coarse components into finer-grained `V`.

Full list in `doctrine.md`.

---

## 10. What this model does NOT claim

1. **No prediction.** ε-over-t is a scenario tool.
2. **Not validated.** These formalisations are research-grade, not empirically validated against real-world mapping outcomes.
3. **Not endorsed by Wardley.** Simon Wardley has not endorsed quantitative formalisations of his framework.
4. **Mapper judgment wins.** Every formula here seeds a quantity; human judgment about value-chain position and strategic context overrides the numbers.

The math makes the framework machine-readable and supports scenario simulation and decision heuristics. It does not replace mapping as a thinking practice.
