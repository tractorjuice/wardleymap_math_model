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

$$\mathcal{M} = (V, E, u, \nu, \varepsilon, t)$$

Where:

- $V$ is a set of components (capabilities, activities, data, systems, suppliers, practices, etc.).
- $E \subseteq V \times V$ is a set of directed dependency edges.
  - An edge $(a,b) \in E$ means "$a$ depends on $b$".
- $u \in V$ is the anchor node representing the **user / user need**.
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

## 3) The Y-axis (Visibility) as distance from the user

The visibility axis can be made computable by using **graph distance from the user**.

### 3.1 Shortest dependency distance
Define:

$$d(v) = \min \{\text{path length}(u \to v)\}$$

Interpretation:
- $d(u)=0$
- Things directly supporting the user have $d=1$
- Deeper dependencies have larger $d$

### 3.2 Map distance to a [0,1] visibility score
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

---

## 4) The X-axis (Evolution) as a continuous maturity score

The evolution axis can be modeled as a **continuous score** $\varepsilon(v)\in[0,1]$, then optionally bucketed into classic stages.

### 4.1 Stage bands (optional)
You can interpret $[0,1]$ as stages:

- Genesis: $[0, 0.25)$
- Custom Built: $[0.25, 0.5)$
- Product: $[0.5, 0.75)$
- Commodity/Utility: $[0.75, 1]$

This keeps the familiar Wardley language while remaining quantitative.

### 4.2 Estimating evolution from observable signals
Let $x(v)\in\mathbb{R}^k$ be measurable signals for a component, for example:

- standardization level (interfaces, specs, compliance)
- number of suppliers / substitutes
- price transparency
- change rate (high change tends to be less evolved)
- ubiquity (how widely used it is)
- switching costs (often correlate with maturity patterns)

Then define a score:

$$\varepsilon(v) = \sigma(w^\top x(v)) = \frac{1}{1 + e^{-w^\top x(v)}}$$

Where:
- $w$ are weights you define (or learn from examples),
- $\sigma$ squashes the score into $[0,1]$.

This makes evolution:
- explicit,
- repeatable,
- calibratable.

---

## 5) Dynamics: make evolution move over time

If you want to model how maps change, treat evolution as a dynamical system. A simple monotone "drift right" model is:

$$\frac{d\varepsilon_v}{dt} = r_v(t)\,(1-\varepsilon_v(t)), \quad r_v(t)\ge 0$$

Interpretation:
- Movement is faster when something is immature.
- It slows as it approaches commodity.

Let strategy act through the rate:

$$r_v(t)=r_{0,v} + u_v(t) - c_v(t)$$

- $r_{0,v}$: baseline evolutionary pressure (market forces)
- $u_v(t)$: your actions (standardize, productize, platformize, outsource, open-source)
- $c_v(t)$: constraints/friction (regulation, inertia, lack of standards, supply limits)

Now your "plays" become levers.

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
