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
| **Exponential decay (default)** | $\nu(v) = e^{-\alpha d(v)}$ with $\alpha = 0.6$ | Default — lets deep infrastructure reach $\nu < 0.1$, matching Wardley's own maps. Seeds: d=1→0.55, d=2→0.30, d=3→0.17, d=4→0.09, d=5→0.05. |
| Reciprocal decay | $\nu(v) = 1/(1 + d(v))$ | Alternative — gentler; caps at $\nu \approx 0.2$ for d=4. Use for shallow maps. |
| Constraint optimisation | Project estimates: $\min \sum_v w_v(\nu(v)-\hat\nu(v))^2$, $w_v>0$, subject to bounds, anchors at 1 and $\nu(a)\ge\nu(b)+\delta$ on every edge | Shortcuts; check feasibility first. Default $\delta=0$. |

Default changed from reciprocal to exponential ($\alpha = 0.6$) in response to benchmark testing against Wardley's own published maps (`ai/TRUST`, `retail/connected journey`, etc.). Reciprocal decay systematically compressed deep-infrastructure components to $\nu \ge 0.2$, whereas Wardley routinely places components at $\nu = 0.04 \text{ to } 0.10$. Exponential decay produces the correct depth spread at minimal cost.

### Hard rule

For every edge `(a, b) ∈ E`:

$$\nu(a) \ge \nu(b)$$

Components must sit at or above their dependencies. If the seed violates this, use the constrained projection or adjust by hand. With $\delta=0$, cycles force equal visibility; positive separation makes cycles infeasible. A path of $L$ edges requires $L\delta\le1$. Report unreachable nodes for scope/dependency review; a zero-valued seed for an unreachable node is not evidence of invisibility. The repository specifies the projection but supplies no numerical solver.

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

**Placement reference: Wardley's cheat sheet** (see `evolution-stages.md`). Select supported, applicable characteristics; rows 1–4 are alternative type vocabularies, not four independent observations. This repository proposes a numerical seed using band midpoints:

$$m(s) = \frac{s - \tfrac{1}{2}}{4}$$

- Stage I → 0.125
- Stage II → 0.375
- Stage III → 0.625
- Stage IV → 0.875

Aggregate:

$$\varepsilon(v) = \sum_{r \in R} w_r \cdot m(s_r(v)), \quad w_r\ge0,\quad \sum_r w_r = 1$$

Default: unweighted mean over the chosen applicable rows (often a quick 4-row subset). Record excluded/missing rows, sources, market and date. Equal spacing is an ordinal plotting convention, not a validated interval scale; midpoint-only means lie in [0.125,0.875].

### Uncertainty

Row disagreement is a separate diagnostic:

$$H(v) = \sum_r w_r \cdot (m(s_r) - \varepsilon)^2.$$

It can indicate a mixed profile or conflicting assessments, not estimator variance. Record evidence quality, source dependence, missing observations and independent mapper disagreement separately. Agreement across weak or correlated rows does not imply confidence. Elicit stage alternatives or ranges if confidence is unmeasured.

A Beta approximation needs independently justified mean $\mu\in(0,1)$ and variance $0<s^2<\mu(1-\mu)$. Set $\kappa=\mu(1-\mu)/s^2-1$, $\alpha=\mu\kappa$, $\beta=(1-\mu)\kappa$. Zero variance has no finite Beta parameters; endpoints need a different representation. Label elicited distributions and use their quantiles, not an assumed confidence interval from row spread.

---

## 4. Dynamics (stylised extension — not Wardley-endorsed)

> **Caveat.** Wardley's climatic pattern "you cannot measure evolution over time or adoption" directly conflicts with any ODE-based forecast. Use dynamics for **scenario exploration**, never prediction.

### Logistic S-curve

$$\frac{d\varepsilon_v}{dt} = r_v(t) \cdot \varepsilon_v(t) \cdot (1 - \varepsilon_v(t))$$

For constant positive rate and an interior initial value, this produces a logistic S-shape. Time-varying rates need not have that calendar-time shape. This scenario equation does not measure adoption or calibrate an evolution forecast.

### Strategy decomposition

$$r_v(t) = \max(0,r_{0,v} + u_v(t) - c_v(t))$$

- `r₀`: baseline market pressure
- `u(t)`: strategic actions (named gameplays — see `gameplay-patterns.md`)
- `c(t)`: inertia (17 structured forms — see `inertia.md`)

Nonnegative rates impose monotonic drift as a scenario assumption. Rate terms use inverse-time units. Logistic trajectories at exactly 0 or 1 remain there; specify interior initial values for growth scenarios.

### Multiple adoption waves

Keep adoption $A_g(t)$ separate from independently assessed generation scores $\varepsilon_g(t)$. Adoption can follow logistic diffusion, with a positive seed $A_g(t_g^{\mathrm{start}})=a_{0,g}\in(0,1)$ at introduction; a start-time indicator cannot make a zero-initialized trajectory grow.

A descriptive composition index is

$$C(v,t)=\frac{\sum_g A_g(t)\varepsilon_g(t)}{\sum_g A_g(t)},\qquad \sum_g A_g(t)>0.$$

$C$ summarizes adopted implementations, not the underlying act's evolution placement. Specify whether penetrations overlap; these dynamics do not conserve exclusive market shares. If no generation is adopted, $C$ is undefined. With one generation, adoption cancels and $C=\varepsilon_g$; this does not recover Part 1's evolution logistic. Assess evolution and competitive phases from market evidence, not adoption quartiles.

---

## 5. Derived heuristics

> **These three metrics are proposed by this skill's math model, not canonical Wardley concepts.** Treat as attention prompts.

| Metric | Formula | High value signals |
|---|---|---|
| Differentiation pressure | $D(v) = \nu(v) \cdot (1 - \varepsilon(v))$ | Visible + immature = advantage zone |
| Commodity leverage | $K(v) = (1 - \nu(v)) \cdot \varepsilon(v)$ | Deep + mature = outsource / utility |
| Dependency exposure prompt | $R(a,b) = \nu(a) \cdot (1 - \varepsilon(b))$ | Visible component relying on a less-evolved dependency |

---

Actual risk requires failure likelihood, impact, substitutes and recovery evidence; lower evolution alone is not fragility. Build/buy/utility decisions also require costs and capabilities. Test ranking sensitivity to coordinate conventions before acting on D, K or R.

## 6. Inertia as structured drag

Part 1's `c_v(t)` scalar flattens 17 distinct forms of inertia Wardley enumerates:

$$c_v(t) = \sum_{i=1}^{17} \lambda_i \cdot \iota_i(v, t)$$

where `ι_i ∈ [0, 1]` is the severity of inertia form `i` for component `v`, and `λ_i ≥ 0` is its weight. See `inertia.md` for the full list and a decomposition into consumer-side (14 forms) vs supplier-side (3 forms).

---

## 7. Component types and co-evolution

One of Wardley's climatic patterns: **practices co-evolve with activities**. Formally:

$$\forall p \text{ with } \tau(p) = P : \exists\, a \text{ with } \tau(a) = A, \, (a, p) \in E, \, \mathrm{corr}(\varepsilon_a(t), \varepsilon_p(t)) > 0$$

Type-dependent evolution rates (unvalidated scenario hypothesis):

$$r_A > r_P > r_D > r_K$$

This ordering is a scenario assumption requiring domain evidence, not a canonical rule or a measured rate hierarchy. The correlation expression also needs observed time series; it is undefined for constant trajectories and does not establish causation.

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
