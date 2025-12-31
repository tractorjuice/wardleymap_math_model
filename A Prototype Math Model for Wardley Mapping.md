# A Prototype Math Model for Wardley Mapping

Below is a **prototype** of how one might formalize aspects of **Wardley Mapping** within a mathematical model. Note that **Wardley Mapping** was originally conceived by Simon Wardley as a visual and conceptual technique—not as a purely quantitative or algorithmic framework—so any "math model" will necessarily be a **stylized abstraction** of the real practice. Nevertheless, creating such a model can help clarify assumptions, enable simulations, and potentially guide strategic decision-making in a more formal manner.

---

## 1. Conceptual Recap of Wardley Mapping

A **Wardley Map** is typically drawn on a 2D plane:

- **Vertical (Y-axis)**: Roughly captures "visibility to the user" (or proximity to the user).
- **Horizontal (X-axis)**: Captures the **evolution** of a component from "Genesis" to "Commodity."

We also have:
1. **Nodes (Components)**: Functions, activities, practices, or data that make up a value chain.
2. **Directed Edges ("Uses")**: A relationship that states "Component A uses (or depends on) Component B."
3. **Movement Over Time**: Components can evolve (move along the X-axis) from a novel, uncertain stage to a well-defined, industrialized commodity.

A Wardley Map is designed to show **position** and **movement** of strategic components so that an organization can anticipate how they (or their competitors) might respond, invest, divest, or collaborate.

---

## 2. Defining the Model Components

Let us define a finite set of components:

$$\mathcal{C} = \{1, 2, \dots, n\}$$

Each component $i \in \mathcal{C}$ has two principal attributes:

1. **Visibility (or Value)** $V_i$
   - This is a real number capturing how close to the end-user (or how crucial to user value) the component is.
   - In a Wardley map, $V_i$ might be plotted on the **vertical axis**.
   - For modeling convenience, we can assume $V_i \in [0,1]$ or some bounded interval $[0, V_{\text{max}}]$.

2. **Evolution** $E_i(t)$
   - A real-valued variable indicating how far along the **evolution axis** the component is at time $t$.
   - Typically, Wardley maps conceptualize four broad stages (Genesis, Custom-Built, Product/Rental, Commodity/Utility). We can abstract this to a continuous range, e.g. $E_i(t)\in[0,1]$, where 0 = "Genesis" and 1 = "Fully Commodity."
   - Over time, $E_i(t)$ generally increases (components move toward more industrialized forms).

Additionally, each component $i$ has **dependencies** on other components. Let

$$\mathcal{D} \subseteq \mathcal{C} \times \mathcal{C}$$

be a set of directed edges. A pair $(i, j) \in \mathcal{D}$ means "Component **$i$** uses or depends on component **$j$**."


---

## 3. Positioning Components on the Wardley Map

A **Wardley Map** at time $t$ can be represented by the set of points

$$\Bigl\{\bigl(E_i(t), V_i\bigr) \Bigm| i \in \mathcal{C}\Bigr\}$$

together with the directed edges $\mathcal{D}$ drawn from $\bigl(E_i(t), V_i\bigr)$ to $\bigl(E_j(t), V_j\bigr)$ whenever $(i,j)\in \mathcal{D}$.

- **X-coordinate**: $E_i(t)$ (evolution stage).
- **Y-coordinate**: $V_i$ (visibility or value to the user).

---

## 4. Modeling Evolution Over Time

One core idea in Wardley Mapping is that **competitive pressure**, **supply/demand effects**, **user adoption**, and **standardization** drive a component from left (Genesis) to right (Commodity). We can capture this with **evolution dynamics**. A typical example is an **S-curve**:

$$\frac{d E_i(t)}{d t} = \alpha_i \bigl(E_i(t)\bigr)\bigl(1 - E_i(t)\bigr)$$

where
- $0 \le E_i(t) \le 1$.
- $\alpha_i$ is a rate parameter that might itself depend on external factors (competition, open source availability, investment, etc.).

A simpler discrete-time version (e.g., if we measure yearly) might be:

$$E_i(t+1) = E_i(t) + \alpha_i \bigl(E_i(t)\bigr) \bigl(1 - E_i(t)\bigr)$$

This ensures $E_i$ stays in $[0,1]$, moving slowly at the beginning, accelerating in mid-stages, and flattening out near 1.

### 4.1 External Influence Factors
To reflect **market or organizational decisions**, we can let $\alpha_i$ be a function of:

- **Investment** $I_i(t)$: Extra resources poured into maturing the component.
- **Market Competition** $C_i(t)$: If there are many competitors, or a strong open-source community, evolution may speed up.
- **Tech Shifts** $T_i(t)$: For instance, a new underlying technology might disrupt or accelerate evolution.

Hence,

$$\alpha_i = \alpha_i\bigl(I_i(t), C_i(t), T_i(t)\bigr)$$

In practice, you might specify something like:

$$\alpha_i = \beta_0 + \beta_1 I_i(t) - \beta_2 C_i(t) + \beta_3 T_i(t)$$

with positivity constraints ensuring it remains a valid rate.

---

## 5. Strategic Interaction: A Simple Game-Theoretic Extension

While Wardley Mapping is often used for **qualitative** strategy, we can add a **game-theoretic** layer by assuming multiple **players** (e.g., firms, organizations, or product teams) each control certain decisions that affect the evolution of some subset of components.

### 5.1 Players, Actions, and Payoffs

Let

$$\mathcal{P} = \{1,2,\dots,P\}$$

be the set of players. Each player $p$ can choose an **action** (or **strategy**) $a_p(t)$ at each time step $t$. For instance, $a_p(t)$ might describe how much to invest in certain components, or whether to open-source them, or whether to commoditize them quickly.

- **Investment Vector**: $I_i^{(p)}(t)$ is the investment from player $p$ into component $i$. Then total investment in $i$ is

  $$I_i(t) = \sum_p I_i^{(p)}(t)$$

- **Control Over Components**: Each component $i$ may be influenced by multiple players or only by one (e.g., a product is owned by a single firm).

The **payoff** to each player $p$ depends on:

1. **Revenue or Value** extracted from certain components' usage.
2. **Costs** of investment or maintenance.
3. Possibly **strategic advantages** from forcing a competitor to rely on a less evolved (higher-cost) resource, or from accelerating commoditization to disrupt a competitor's revenue model.

Symbolically, define a **per-period payoff** function

$$\Pi_p\bigl(\mathbf{E}(t), \mathbf{I}^{(p)}(t)\bigr)$$

where $\mathbf{E}(t)$ is the vector of all evolution states at time $t$.

### 5.2 Equilibrium or Optimization

If the players move simultaneously, one can seek a **Nash equilibrium** for the investments:

$$\{I_i^{(p)*}\}_{i,p}$$

such that no player can unilaterally deviate and improve their expected payoff.

Alternatively, if there is a clear hierarchy (e.g., a major vendor as a **leader** deciding on open-sourcing a commodity, then smaller companies reacting), you can embed these dynamics in a **Stackelberg** or **bilevel** model.

---

## 6. Incorporating Dependency (Value Chain) Effects

Wardley Maps emphasize how a **higher-level component** uses a **lower-level component**. This can be modeled in the **payoffs** or **evolution** equations:

1. **Payoff Dependence**: If component $j$ is crucial to $i$, then the "value" or "functionality" of $i$ might be limited until $j$ is sufficiently evolved. For example:

   $$\Pi_p(\ldots) \propto \min\bigl(E_j(t), E_i(t)\bigr)$$

   or some function that ties $E_i$ to the evolving state of its dependencies.

2. **Cascade Effects**: If a lower-level component $j$ becomes a well-established commodity ($E_j \approx 1$), it might **accelerate** the evolution of the higher-level $i$. This can be factored into the S-curve rate for $i$:

   $$\frac{dE_i}{dt} = f\Bigl(E_i(t), \{E_k(t)\mid (i,k)\in \mathcal{D}\}, \alpha_i\Bigr)$$

3. **Cost Structures**: If a company invests heavily to commoditize $j$, it might reduce the overall cost or friction for $i$. This again modifies $\alpha_i$ or the payoff terms accordingly.

---

## 7. Example of a Simple Discrete-Time Model

Let us sketch a minimal **discrete-time** system to see how it might work in practice:

1. **Initialize**:
   - $E_i(0)$ for all $i\in\mathcal{C}$.
   - Visibility $V_i$.
   - Dependency graph $\mathcal{D}$.
   - Players' initial budgets, strategies, etc.

2. **At each time step** $t=0,1,2,\ldots$:
   1. **Players choose investments**: $\{I_i^{(p)}(t)\}$ or other strategic actions.
   2. **Compute total investment** in each component $i$:

      $$I_i(t) = \sum_{p} I_i^{(p)}(t)$$

   3. **Update evolution states**:

      $$E_i(t+1) = E_i(t) + \alpha_i\bigl(I_i(t), C_i(t)\bigr) E_i(t) \bigl(1-E_i(t)\bigr)$$

      Possibly incorporate dependency terms or synergy factors from other components $k$ that $i$ uses.

   4. **Compute payoffs** for each player:

      $$\Pi_p(t+1) = \sum_{i\in\mathcal{C}_p} \text{Revenue}_p\bigl(E_i(t+1)\bigr) - \text{Cost}_p\bigl(\{I_i^{(p)}(t)\}\bigr)$$

      where $\mathcal{C}_p$ is the set of components relevant to player $p$.

3. **End Condition**: Continue until a steady state or for a fixed horizon. Analyze final states $\{E_i(T)\}$, player payoffs, and the structure of the "map" to derive strategic insights.

This cycle provides a **simulation-based** approach where you can adjust assumptions about how quickly components evolve and see how the Wardley map changes over time.

---

## 8. Possible Extensions and Uses

1. **Scenario Planning**: Vary exogenous parameters (e.g., market disruptions, technology leaps) to see how the X-axis positions shift.
2. **Sensitivity Analysis**: Identify which investments or dependencies have the biggest impact on final payoffs.
3. **Comparative Strategies**: Evaluate different player strategies (e.g., quickly commoditizing a key component vs. differentiating it) and measure outcomes.
4. **Agent-Based Simulations**: Instead of a purely game-theoretic approach, let each player or "agent" follow heuristics (e.g., invests proportionally to ROI) and observe emergent Wardley map patterns.

---

## 9. Limitations and Cautions

- **Qualitative to Quantitative**: In real Wardley Mapping, the Y-axis (visibility) is not always a strict, numeric measure. Attempts to "force" everything into a precise scale can lose important **context** or lead to oversimplification.
- **Complex Dynamics**: True evolution involves feedback loops, exogenous shocks, and intangible factors (e.g., brand perception, organizational culture). A single equation might be too simplistic.
- **Data Scarcity**: Calibrating $\alpha_i$ or payoff functions requires historical data or expert judgment.
- **Interpretation**: Even with a formal model, the strategic insights often come from **visual**, **iterative**, and **creative** use of the map—so the math is an aid, not a replacement for strategic sense-making.

---

## Concluding Remarks

By **translating** the conceptual elements of Wardley Mapping into states, investments, payoff functions, and evolution dynamics, we can create a **stylized mathematical model** that:

- Places each component on a continuous scale of **evolution** (X-axis).
- Fixes or estimates a **visibility** or **value** parameter (Y-axis).
- Updates evolution over time via **S-curves** or other functional forms.
- Incorporates **strategic interactions** (investments, open-sourcing, competition) in a game-theoretic or agent-based simulation framework.

Such a model can help with **scenario testing**, **simulation-based planning**, and deeper analysis of **how organizational choices** might shift the map. However, it is crucial to remember that **Wardley Maps** were designed primarily as a **visual sense-making tool**—the rigor of a math model should augment, not overshadow, the map's original purpose of helping teams see where their strategic components are heading and why that matters.
