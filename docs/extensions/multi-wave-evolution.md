# Multi-Wave Evolution and Punctuated Equilibrium

Part 1 §5 models evolution as a single logistic S-curve per component. Wardley's actual position is sharper: evolution of an *act* spans **multiple generations**, each with its own diffusion curve, separated by **chasms** (punctuated equilibria). This doc replaces the single-curve dynamics with a multi-wave model that matches Wardley's framing.

---

## 1. Why one S-curve is wrong

Wardley's [*Map Evolution, Not Maturity*](https://medium.com/mappingpractice/map-evolution-not-maturity-bae6ea1a2743) gives the canonical example. The act "compute" has passed through (at least):

| Generation | Era | Peak ubiquity |
|---|---|---|
| Mainframes | 1960s–1970s | Custom Built |
| Minicomputers | 1970s–1980s | Product |
| Personal computers | 1980s–1990s | Product → Commodity |
| Client-server / x86 servers | 1990s–2000s | Commodity |
| Virtualisation | 2005–2015 | Commodity |
| Public cloud / utility | 2015– | Utility |

A single logistic curve fitted to "compute" is a fiction. Each generation has its own S-curve; the *act* moves rightward because each successive generation is more commoditised than the last. Fitting one curve to the aggregate gives the error Wardley calls out: you conclude cloud is "immature" because you are on a *new* adoption curve, when the underlying act is well into utility.

Wardley's climatic pattern *"Shifts from product to utility tend to demonstrate a punctuated equilibrium"* (from his [Medium book chapter on climate](https://medium.com/wardleymaps)) names this directly — evolution is stepwise, not smooth.

---

## 2. The multi-wave model

### 2.1 Generations as first-class objects

Let component $v$ have a set of **generations** $G_v = \{g_1, g_2, \ldots, g_{n_v}\}$, ordered by appearance. Each generation has:

- $t_g^{\text{start}}$: when it became technically possible.
- $A_g(t) \in [0, 1]$: its **adoption fraction** at time $t$ (how much of the relevant market uses generation $g$).
- $\varepsilon_g \in [0, 1]$: the evolution stage the generation **tops out at** in the absence of successors (e.g., mainframes topped out at ~Custom Built because no one tried to commoditise them before minicomputers arrived).

Adoption follows its own logistic inside the generation:

$$\frac{dA_g}{dt} = k_g \, A_g(t) \, \bigl(1 - A_g(t)\bigr) \, \mathbb{1}[t \ge t_g^{\text{start}}]$$

where $k_g$ is the per-generation adoption rate.

### 2.2 Aggregating to component evolution

The component's evolution is the adoption-weighted mean of its generations' topped-out stages:

$$\varepsilon(v, t) = \frac{\sum_{g \in G_v} A_g(t) \cdot \varepsilon_g}{\sum_{g \in G_v} A_g(t)}$$

Properties:

- When only gen 1 is adopted, $\varepsilon(v, t) = \varepsilon_{g_1}$.
- When gen $n$ has fully displaced earlier generations, $\varepsilon(v, t) = \varepsilon_{g_n}$.
- During a transition (e.g., 40% cloud, 60% on-prem server), the score is a mixture — which is *exactly* what you want on a map in 2018, not a single point pretending the transition is complete.

### 2.3 Cross-generation cannibalisation

A new generation pulls adoption from old ones. Model this with a coupled ODE:

$$\frac{dA_g}{dt} = k_g \, A_g(t) \, \bigl(1 - A_g(t)\bigr) - \sum_{g' > g} \mu_{g',g} \, A_{g'}(t) \, A_g(t)$$

The $\mu_{g',g}$ term is the cannibalisation rate of generation $g'$ on generation $g$. Earlier generations lose adoption as later ones grow.

For simplicity, uniform cannibalisation $\mu_{g',g} = \mu$ for $g' > g$ is a reasonable first pass. Per-pair rates matter when specific generations particularly threaten specific predecessors (e.g., cloud cannibalises colocation faster than it cannibalises mainframes).

---

## 3. Chasms

### 3.1 The shape of a chasm

Between generations $g$ and $g+1$ there is typically a period where:

- $g$ has saturated ($A_g \approx 1$ in its niche) but is declining.
- $g+1$ is nascent ($A_{g+1} \ll 0.5$).
- Net adoption of *the act* looks stalled, even though evolution is still progressing under the surface.

On the map, the component appears stuck — which is misleading. The evolution score $\varepsilon(v, t)$ sits between $\varepsilon_g$ and $\varepsilon_{g+1}$ and barely moves during the chasm, then jumps as $g+1$ takes off.

### 3.2 Chasm depth as a parameter

Define the **chasm depth** between gens $g$ and $g+1$:

$$\Delta_{g,g+1} = t_{g+1}^{\text{takeoff}} - t_g^{\text{saturation}}$$

where $t_g^{\text{saturation}}$ is the time $A_g$ first exceeds some high threshold (e.g., 0.9) and $t_{g+1}^{\text{takeoff}}$ is when $A_{g+1}$ first exceeds a low threshold (e.g., 0.1).

Deep chasms (large $\Delta$) produce long flat regions in $\varepsilon(v, t)$. Shallow chasms produce near-continuous evolution.

### 3.3 Inertia lives in the chasm

The 17 forms of inertia (see the Inertia doc) operate primarily during chasms. A consumer with sunk capital in generation $g$ delays adopting generation $g+1$; suppliers whose business model depends on $g$ resist building $g+1$. Inertia is the chasm-widening force.

In the coupled dynamics:

$$k_{g+1}(t) = k_{0,g+1} - c_v(t)$$

where $c_v(t)$ is the structured inertia term from the Inertia doc. Higher inertia slows the new generation's adoption, deepening the chasm.

---

## 4. The Peace / War / Wonder cycle

Wardley overlays a three-phase cycle on each chasm-transition, tied to the generational wave:

- **Wonder**: A new generation emerges; uncertainty is high, custom solutions abound. Mapped to Genesis/Custom Built.
- **Peace**: The generation is productised; competition on features. Mapped to Product stage.
- **War**: The generation commoditises; a few utility providers dominate, and the war is over who owns the utility. Mapped to Commodity/Utility.

At the end of War, a new Wonder begins with the next generation, and the cycle repeats one band to the right.

Mathematically, a generation's phase at time $t$ is determined by its adoption level:

$$\mathrm{phase}(g, t) = \begin{cases}
\text{Wonder} & A_g(t) < 0.25 \\
\text{Peace} & 0.25 \le A_g(t) < 0.75 \\
\text{War} & A_g(t) \ge 0.75
\end{cases}$$

A component is in the phase of its most-recent active generation. This gives a principled reading of *strategic tempo* — what a player should be doing depends on which phase their components are in.

---

## 5. Backwards compatibility with Part 1

The single-logistic model in Part 1 §5 is recovered as the special case $|G_v| = 1$:

$$\varepsilon(v, t) = A_{g_1}(t) \cdot \varepsilon_{g_1}$$

which, when $\varepsilon_{g_1} = 1$, collapses to the Part 1 logistic.

For workshops and scenario exercises, Part 1's single curve is often good enough — it's a readable approximation. Switch to the multi-wave model when:

- You are reasoning about a specific chasm (e.g., "will our customers actually move to the new platform?").
- Your horizon exceeds one generation (multi-year strategic planning).
- You're debugging why a component appears stuck.

---

## 6. Worked example — "storage" 2000–2030

A rough reconstruction of generations for the "storage" act:

| Generation | $t^{\text{start}}$ | $\varepsilon_g$ | Note |
|---|---|---|---|
| On-prem SAN | 1995 | 0.65 | Product (+rental), never commoditised |
| DAS / commodity arrays | 2005 | 0.80 | Commodity hardware |
| Cloud object storage (S3-class) | 2008 | 0.90 | Utility |

Suppose at $t = 2020$, adoption fractions are $A_{SAN} = 0.3$, $A_{DAS} = 0.3$, $A_{cloud} = 0.8$. Then:

$$\varepsilon(\text{storage}, 2020) = \frac{0.3 \cdot 0.65 + 0.3 \cdot 0.80 + 0.8 \cdot 0.90}{0.3 + 0.3 + 0.8} = \frac{1.155}{1.4} \approx 0.825$$

Mid-Commodity, skewed toward Utility — matching industry sense at that time. A single-logistic fit would place "storage" at maybe 0.7 (misleadingly conservative) or at 0.9 (misleadingly utility-only).

By 2028, assume $A_{SAN} \to 0.05$, $A_{DAS} \to 0.15$, $A_{cloud} \to 0.95$. Then $\varepsilon \approx 0.88$ — nearly full utility. The chasm for SAN has deepened to the point of near-irrelevance.

---

## 7. Caveats

1. **Generations are judgment calls.** What counts as a distinct generation vs. an incremental upgrade is the mapper's decision. Over-decomposition gives meaningless multi-wave structure; under-decomposition reproduces the single-curve error.

2. **The model smooths real chasms.** Actual technology transitions have spikes, reversals, and exogenous shocks (regulation, supply crises). The logistic-per-generation is a first-order model; calibrate against history before trusting it forward.

3. **Still not a forecast.** The climatic caveat from Part 1 §5 applies here too — *"you cannot measure evolution over time or adoption."* The multi-wave model is a better narrative tool than the single curve; it is not a validated predictive system.

4. **Adoption is market-relative.** "Adoption fraction" of a generation is a fraction of *what market*? The same caveat as ubiquity in the cheat sheet (Part 6 §5). Define the market before you score.
