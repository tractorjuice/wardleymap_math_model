# A Mathematical Model for Wardley Mapping

Wardley Mapping is a way to model a value chain: **what the user needs**, the **capabilities** that satisfy that need, and the **dependencies** beneath them. The map is drawn on a 2D plane:

- **Y-axis (Visibility / Position):** how close something is to the user.
- **X-axis (Evolution):** how evolved the thing is, from novel and uncertain to standardized and commodity-like.

This article introduces a **math-first model** of a Wardley Map so you can:
- generate maps from data,
- validate maps with constraints,
- quantify "where to act,"
- simulate movement over time.

---

## 1) The Wardley Map as a formal object

We model a Wardley Map as a tuple:

$$\mathcal{M} = (V, E, U, \nu, \varepsilon, t)$$

Where:

- $V$ is a set of components (capabilities, activities, data, systems, suppliers, practices, etc.).
- $E \subseteq V \times V$ is a set of directed dependency edges.
  - An edge $(a,b) \in E$ means "**a** depends on **b**".
- $U \subseteq V$ is the **anchor set** — one or more user-need nodes. Real maps routinely have multiple user needs (e.g., *business* and *public* in Wardley's Tea Shop example), so $|U| \ge 1$. When $|U|=1$ we often write the single element as $u$.
- $\nu: V \to [0,1]$ assigns each component a **visibility score** (Y-axis).
- $\varepsilon: V \to [0,1]$ assigns each component an **evolution score** (X-axis).
- $t$ is time (optional; used if you want dynamics).

This is the minimum structure needed to make a Wardley Map machine-usable: a graph + two placement functions.

---

## 2) Dependencies: the value chain is a directed graph

A Wardley Map is a value chain, and a value chain is naturally a graph.

- Nodes: "things" that exist and matter.
- Edges: "depends-on" relationships.

Typical shapes:
- A top user need node.
- A chain or tree flowing downward into foundational components.
- Shared utilities that many nodes depend on.

From here, the "picture" becomes math: the axes are just functions over the graph.

---

## 3) The Y-axis (Visibility): position in the value chain

Visibility in a Wardley Map is a **judgment about value chain position**, not a pure graph property. Wardley frames it as "visibility to the user, which is a natural outcome of a component's relative position within the value chain, **manually adjusted as needed**" ([learnwardleymapping.com/landscape](https://learnwardleymapping.com/landscape/)).

So in the mathematical model, $\nu(v) \in [0,1]$ is the **primitive** — assigned by the mapper. What follows are ways to **seed** $\nu$ computationally. The mapper is free to override the seed when judgment about value to the user disagrees with topology.

### 3.1 Seed: shortest dependency distance

Define distance from the anchor set $U$ (one or more user-need nodes):

$$d(v) = \min_{u \in U} \{\text{path length}(u \to v)\}$$

Interpretation:
- $d(u)=0$ for any $u \in U$
- Things directly supporting a user need have $d=1$
- Deeper dependencies have larger $d$

### 3.2 Map distance to a [0,1] visibility seed
Two simple choices:

**Option A: reciprocal decay**

$$\nu(v) = \frac{1}{1+d(v)}$$

**Option B: exponential decay**

$$\nu(v) = e^{-\alpha d(v)} \quad \text{with } \alpha>0$$

Both have the right behavior:
- higher visibility near the user,
- lower visibility further down the dependency chain.

### 3.3 Enforce the "dependencies go downward" rule
In Wardley Maps, a component is typically placed **above** the things it depends on. That becomes a constraint:

For every edge $(a,b)\in E$,

$$\nu(a) \ge \nu(b) + \delta$$

Where $\delta \ge 0$ is a minimum vertical separation.

If raw distances violate this (because real graphs have shortcuts), compute $\nu$ by optimization:

$$\min_{\nu:V\to[0,1]} \sum_{(a,b)\in E} \left(\nu(a) - \nu(b) - \delta\right)^2 \quad \text{s.t. } 0\le \nu(v)\le 1$$

This gives a consistent vertical layout even in messy graphs.

### 3.4 Which option should I use?

| Option | Formula | Use when |
|---|---|---|
| **A. Reciprocal decay** | $\nu(v) = \frac{1}{1+d(v)}$ | Default choice. Simple, smooth, parameter-free. Works well for tree-like value chains where distances are small. |
| **B. Exponential decay** | $\nu(v) = e^{-\alpha d(v)}$ | Deep graphs where you want to tune the vertical spread. Larger $\alpha$ pushes deep nodes closer to 0; smaller $\alpha$ keeps the chain visible. |
| **C. Constraint optimization** | minimize the quadratic above | Graphs with cross-links or shortcuts that break the "deeper = lower" rule. Produces a layout that respects every edge constraint even when raw distances don't. |

Default to A unless you have a specific reason to switch. If the resulting map violates $\nu(a) \ge \nu(b)$ for some edge $(a,b)$ (a "shortcut" above its dependency), move to C.

An alternative layer-based formulation — counting discrete dependency layers rather than raw distance — is covered in Part 5.

### 3.5 Override: the mapper has the final word

Whichever option produces the seed, the mapper may adjust any $\nu(v)$ by hand to reflect judgment about value chain position that the topology doesn't capture. Examples:

- A component is technically a deep dependency but the user *thinks* about it (e.g., a branded payment widget) — raise its $\nu$.
- A component is reachable directly from the user but is architecturally invisible (e.g., a CDN) — lower its $\nu$.

The only hard rule is the edge constraint $\nu(a) \ge \nu(b)$ for every dependency $(a,b)$. Within that, $\nu$ is a judgment call that the math seeds but does not dictate.

---

## 4) The X-axis (Evolution) as a continuous score

> **Evolution is not maturity.** Wardley spent a Medium post arguing this: ["Map Evolution, Not Maturity"](https://medium.com/mappingpractice/map-evolution-not-maturity-bae6ea1a2743). Maturity tracks a single product's diffusion curve; evolution tracks the shifting *certainty and ubiquity of an underlying act* across multiple product generations. A model that scores evolution as "how mature is this" is making the error Wardley warns against.

The evolution axis is a **continuous score** $\varepsilon(v)\in[0,1]$, then optionally bucketed into classic stages.

### 4.1 Stage bands (optional)

Wardley's four canonical stages (the parenthesized suffixes are part of the names):

- **Genesis**: $[0, 0.25)$
- **Custom Built**: $[0.25, 0.5)$
- **Product (+rental)**: $[0.5, 0.75)$
- **Commodity (+utility)**: $[0.75, 1]$

Stage III covers both products and rental/licensing; Stage IV covers both commoditization and utility services (electricity, cloud). The boundaries are conventional — Wardley himself does not fix them at exact quartiles.

### 4.2 Estimating evolution from observable signals

The canonical way to estimate $\varepsilon(v)$ is Wardley's **cheat sheet** — a table of characteristic dimensions (ubiquity, certainty, publication type, user perception, etc.) with per-stage descriptors. See **Part 6 — Cheat-sheet evolution scoring** for the full table and a formal scoring procedure.

For a quick numeric seed, let $x(v)\in\mathbb{R}^k$ be measurable signals — e.g. standardization level, number of suppliers, price transparency, change rate, ubiquity-in-market, switching costs. Then:

$$\varepsilon(v) = \sigma(w^\top x(v)) = \frac{1}{1 + e^{-w^\top x(v)}}$$

Where $w$ are weights (defined or learned) and $\sigma$ squashes to $[0,1]$. This gives an explicit, repeatable, calibratable number — but it is a **seed**, not the canonical placement. Always cross-check against the cheat sheet; if the two disagree, trust the cheat sheet.

---

## 5) Dynamics: make evolution move over time

> **Caveat up front.** Wardley is explicit — one of his 23 climatic patterns states *"you cannot measure evolution over time or adoption."* Evolution is determined against the cheat sheet (ubiquity, certainty, publication type, user perception, etc. — see Part 6), not by a clock. The ODE below is a **stylized extension** for simulation and scenario exploration only. Treat it as a what-if tool, not a forecast, and don't let it override cheat-sheet judgment.

If you want to model how maps might change, treat evolution as a dynamical system. The standard **logistic (S-curve)** form is:

$$\frac{d\varepsilon_v}{dt} = r_v(t)\,\varepsilon_v(t)\,(1-\varepsilon_v(t)), \quad r_v(t)\ge 0$$

Interpretation:
- Movement is slow at both extremes (nothing to spread from near 0, saturated near 1).
- Movement is fastest near the middle, where adoption momentum peaks.

This produces the canonical S-shape. If you want a simpler "bounded drift right" instead — monotone approach to 1 with no inflection — drop the $\varepsilon_v$ factor:

$$\frac{d\varepsilon_v}{dt} = r_v(t)\,(1-\varepsilon_v(t))$$

(This is exponential approach to 1, not an S-curve. Use it when you don't want the slow-start phase.)

Let strategy act through the rate:

$$r_v(t)=r_{0,v} + u_v(t) - c_v(t)$$

- $r_{0,v}$: baseline evolutionary pressure (market forces)
- $u_v(t)$: your actions (standardize, productize, platformize, outsource, open-source) — see the gameplay catalogue for a richer action vector
- $c_v(t)$: inertia (see the Inertia doc for Wardley's 16 forms, which this scalar flattens)

Now your "plays" become levers — but remember the caveat: this simulates a plausible path, it does not predict evolution.

---

## 6) Uncertainty: use distributions instead of single points

Mapping is about revealing assumptions. So model coordinates as probability distributions:

$$\varepsilon(v)\sim \text{Beta}(\alpha_v,\beta_v) \quad,\quad \nu(v)\sim \text{Beta}(\gamma_v,\delta_v)$$

- Mean = plotted coordinate
- Variance = how confident you are

This supports "error bars" on a map and makes debate concrete:
- "We disagree on where it is."
- "Fine. Show your uncertainty and update it with evidence."

---

## 7) Derived metrics: turn the map into decision signals

> **Note on authority.** The three metrics below — differentiation pressure, commodity leverage, dependency risk — are **heuristics proposed by this repository**, not concepts from Simon Wardley's own writing. They're simple products of $\nu$ and $\varepsilon$ that tend to highlight regions of a map a strategist would flag anyway. Use them as prompts for attention, not as validated decision criteria. Wardley's catalogue of plays and his doctrine are the authoritative strategic primitives; see the Gameplay docs and doctrine pages on [learnwardleymapping.com](https://learnwardleymapping.com/).

Once everything is numeric, you can compute helpful scores.

### 7.1 Differentiation pressure (visible + immature)

$$D(v)=\nu(v)\,(1-\varepsilon(v))$$

High $D$ suggests:
- user-visible,
- not yet evolved,
- potential advantage zone.

### 7.2 Commodity leverage (invisible + mature)

$$K(v)=(1-\nu(v))\,\varepsilon(v)$$

High $K$ suggests:
- deep utility,
- mature and standardized,
- strong candidate for buying, outsourcing, automating, or treating as a utility.

### 7.3 Dependency risk (visible depends on immature)
For edge $(a,b)$:

$$R(a,b)=\nu(a)\,(1-\varepsilon(b))$$

High $R$ suggests:
- top-of-chain value depends on fragile foundations,
- likely reliability, cost, or delivery risk.

---

## 8) A tiny worked example

Suppose we have:

- User Need $u$
- Online Purchase (A)
- Payments (B)
- Fraud Detection (C)
- Cloud Compute (D)

Dependencies:
- A depends on B and C
- B depends on D
- C depends on D

Edges:
- (A,B), (A,C), (B,D), (C,D)

### 8.1 Visibility via distance
Distances from $u$:
- $d(u)=0$
- $d(A)=1$
- $d(B)=2$, $d(C)=2$
- $d(D)=3$

Using $\nu(v)=1/(1+d(v))$:
- $\nu(u)=1$
- $\nu(A)=1/2=0.5$
- $\nu(B)=\nu(C)=1/3\approx0.333$
- $\nu(D)=1/4=0.25$

That already respects "depends-on goes downward" (A above B/C above D).

### 8.2 Evolution as scores
Assume:
- Fraud detection (C) is bespoke-ish: $\varepsilon(C)=0.35$
- Payments (B) is productized: $\varepsilon(B)=0.65$
- Cloud compute (D) is commodity: $\varepsilon(D)=0.9$
- Online purchase workflow (A) is mixed: $\varepsilon(A)=0.5$

Now you can compute:
- Differentiation pressure $D(C)=0.333*(1-0.35)\approx0.216$ (interesting!)
- Commodity leverage $K(D)=(1-0.25)*0.9=0.675$ (treat as utility)

---

## 9) Practical workflow for using the model

1. **Define nodes $V$**
   Keep them concrete. Use nouns, not slogans.

2. **Define dependencies $E$**
   "A depends on B" should be testable.

3. **Compute or fit visibility $\nu$**
   Start with distance, then enforce constraints if needed.

4. **Estimate evolution $\varepsilon$**
   Use a rubric (signals) and make weights explicit.

5. **Plot points**
   Each node becomes $(\varepsilon(v), \nu(v))$.

6. **Compute metrics**
   Use $D, K, R$ to prioritize.

7. **Run scenarios** (optional)
   Change $u_v(t)$ to model strategic plays and see which components move right.

---

## 10) What this model gives you

- A Wardley Map that can live in code and data, not just in a workshop.
- Repeatable placement rules for both axes.
- The ability to quantify assumptions and uncertainty.
- Decision support metrics that highlight where to focus.
- A foundation for automation: map generation, drift simulation, and play recommendation.

---

## 11) Minimal definition to remember

A Wardley Map is:

- a directed dependency graph $(V,E)$,
- plus two functions:
  - $\nu:V\to[0,1]$ for visibility (Y),
  - $\varepsilon:V\to[0,1]$ for evolution (X),
- optionally extended with time dynamics and uncertainty.

That's it. The rest is calibration and judgement.
