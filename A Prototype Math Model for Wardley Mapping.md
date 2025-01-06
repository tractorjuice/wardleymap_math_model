# A Prototype Math Model for Wardley Mapping

Below is a **prototype** of how one might formalize aspects of **Wardley Mapping** within a mathematical model. Note that **Wardley Mapping** was originally conceived by Simon Wardley as a visual and conceptual technique—not as a purely quantitative or algorithmic framework—so any “math model” will necessarily be a **stylized abstraction** of the real practice. Nevertheless, creating such a model can help clarify assumptions, enable simulations, and potentially guide strategic decision-making in a more formal manner.

---

## 1. Conceptual Recap of Wardley Mapping

A **Wardley Map** is typically drawn on a 2D plane:

- **Vertical (Y-axis)**: Roughly captures “visibility to the user” (or proximity to the user).  
- **Horizontal (X-axis)**: Captures the **evolution** of a component from “Genesis” to “Commodity.”  

We also have:
1. **Nodes (Components)**: Functions, activities, practices, or data that make up a value chain.  
2. **Directed Edges (“Uses”)**: A relationship that states “Component A uses (or depends on) Component B.”  
3. **Movement Over Time**: Components can evolve (move along the X-axis) from a novel, uncertain stage to a well-defined, industrialized commodity.  

A Wardley Map is designed to show **position** and **movement** of strategic components so that an organization can anticipate how they (or their competitors) might respond, invest, divest, or collaborate.

---

## 2. Defining the Model Components

Let us define a finite set of components:

![](https://latex.codecogs.com/gif.latex?\mathcal{C}%20=%20\%7B1,%202,\%20\dots,%20n\%7D).

Each component ![](https://latex.codecogs.com/gif.latex?i%20\in%20\mathcal{C}) has two principal attributes:

1. **Visibility (or Value)** ![](https://latex.codecogs.com/gif.latex?V_i)  
   - This is a real number capturing how close to the end-user (or how crucial to user value) the component is.  
   - In a Wardley map, ![](https://latex.codecogs.com/gif.latex?V_i) might be plotted on the **vertical axis**.  
   - For modeling convenience, we can assume ![](https://latex.codecogs.com/gif.latex?V_i%20\in%20%5B0,1%5D) or some bounded interval ![](https://latex.codecogs.com/gif.latex?\%5B0,%20V_{\text{max}}\%5D).

2. **Evolution** ![](https://latex.codecogs.com/gif.latex?E_i(t))  
   - A real-valued variable indicating how far along the **evolution axis** the component is at time ![](https://latex.codecogs.com/gif.latex?t).  
   - Typically, Wardley maps conceptualize four broad stages (Genesis, Custom-Built, Product/Rental, Commodity/Utility). We can abstract this to a continuous range, e.g. ![](https://latex.codecogs.com/gif.latex?E_i(t)\in%5B0,1%5D), where 0 = “Genesis” and 1 = “Fully Commodity.”  
   - Over time, ![](https://latex.codecogs.com/gif.latex?E_i(t)) generally increases (components move toward more industrialized forms).

Additionally, each component ![](https://latex.codecogs.com/gif.latex?i) has **dependencies** on other components. Let

![](https://latex.codecogs.com/gif.latex?\mathcal{D}%20\subseteq%20\mathcal{C}%20\times%20\mathcal{C}),

be a set of directed edges. A pair ![](https://latex.codecogs.com/gif.latex?(i,%20j)%20\in%20\mathcal{D}) means “Component ![](https://latex.codecogs.com/gif.latex?i) **uses** or **depends on** component ![](https://latex.codecogs.com/gif.latex?j).”


---

## 3. Positioning Components on the Wardley Map

A **Wardley Map** at time ![](https://latex.codecogs.com/gif.latex?t) can be represented by the set of points

![](https://latex.codecogs.com/gif.latex?\%5CBigl\%7B\bigl(E_i(t),%5C,%20V_i\bigr)%20\%5CBigm%7C%5C;%20i%20\in%20\mathcal{C}\%5CBigr\%7D),

together with the directed edges ![](https://latex.codecogs.com/gif.latex?\mathcal{D}) drawn from ![](https://latex.codecogs.com/gif.latex?\bigl(E_i(t),%20V_i\bigr)) to ![](https://latex.codecogs.com/gif.latex?\bigl(E_j(t),%20V_j\bigr)) whenever ![](https://latex.codecogs.com/gif.latex?(i,j)\in%20\mathcal{D}).

- **X-coordinate**: ![](https://latex.codecogs.com/gif.latex?E_i(t)) (evolution stage).  
- **Y-coordinate**: ![](https://latex.codecogs.com/gif.latex?V_i) (visibility or value to the user).

---

## 4. Modeling Evolution Over Time

One core idea in Wardley Mapping is that **competitive pressure**, **supply/demand effects**, **user adoption**, and **standardization** drive a component from left (Genesis) to right (Commodity). We can capture this with **evolution dynamics**. A typical example is an **S-curve**:

![](https://latex.codecogs.com/gif.latex?\frac%7Bd%20E_i(t)%7D%7Bd%20t%7D%20=%20\alpha_i%20%5Cbigl(E_i(t)%5Cbigr)%5Cbigl(1%20-%20E_i(t)%5Cbigr)),

where  
- ![](https://latex.codecogs.com/gif.latex?0%20\le%20E_i(t)%20\le%201).  
- ![](https://latex.codecogs.com/gif.latex?\alpha_i) is a rate parameter that might itself depend on external factors (competition, open source availability, investment, etc.).

A simpler discrete-time version (e.g., if we measure yearly) might be:

![](https://latex.codecogs.com/gif.latex?E_i(t+1)%20=%20E_i(t)%20+%20\alpha_i%20\bigl(E_i(t)\bigr)%20\bigl(1%20-%20E_i(t)\bigr).)

This ensures ![](https://latex.codecogs.com/gif.latex?E_i) stays in ![](https://latex.codecogs.com/gif.latex?\%5B0,1\%5D), moving slowly at the beginning, accelerating in mid-stages, and flattening out near 1.

### 4.1 External Influence Factors
To reflect **market or organizational decisions**, we can let ![](https://latex.codecogs.com/gif.latex?\alpha_i) be a function of:

- **Investment** ![](https://latex.codecogs.com/gif.latex?I_i(t)): Extra resources poured into maturing the component.  
- **Market Competition** ![](https://latex.codecogs.com/gif.latex?C_i(t)): If there are many competitors, or a strong open-source community, evolution may speed up.  
- **Tech Shifts** ![](https://latex.codecogs.com/gif.latex?T_i(t)): For instance, a new underlying technology might disrupt or accelerate evolution.

Hence,

![](https://latex.codecogs.com/gif.latex?\alpha_i%20=%20\alpha_i\bigl(I_i(t),%5C,%20C_i(t),%5C,%20T_i(t)\bigr).)

In practice, you might specify something like:

![](https://latex.codecogs.com/gif.latex?\alpha_i%20=%20\beta_0%20+%20\beta_1%5C,%20I_i(t)%20-%20\beta_2%5C,%20C_i(t)%20+%20\beta_3%5C,%20T_i(t),)

with positivity constraints ensuring it remains a valid rate.

---

## 5. Strategic Interaction: A Simple Game-Theoretic Extension

While Wardley Mapping is often used for **qualitative** strategy, we can add a **game-theoretic** layer by assuming multiple **players** (e.g., firms, organizations, or product teams) each control certain decisions that affect the evolution of some subset of components.

### 5.1 Players, Actions, and Payoffs

Let

![](https://latex.codecogs.com/gif.latex?\mathcal{P}%20=%20\%7B1,2,\dots,P\%7D)

be the set of players. Each player ![](https://latex.codecogs.com/gif.latex?p) can choose an **action** (or **strategy**) ![](https://latex.codecogs.com/gif.latex?a_p(t)) at each time step ![](https://latex.codecogs.com/gif.latex?t). For instance, ![](https://latex.codecogs.com/gif.latex?a_p(t)) might describe how much to invest in certain components, or whether to open-source them, or whether to commoditize them quickly.

- **Investment Vector**: ![](https://latex.codecogs.com/gif.latex?I_i^{(p)}(t)) is the investment from player ![](https://latex.codecogs.com/gif.latex?p) into component ![](https://latex.codecogs.com/gif.latex?i). Then total investment in ![](https://latex.codecogs.com/gif.latex?i) is 

  ![](https://latex.codecogs.com/gif.latex?I_i(t)%20=%20\sum_p%20I_i^{(p)}(t).)

- **Control Over Components**: Each component ![](https://latex.codecogs.com/gif.latex?i) may be influenced by multiple players or only by one (e.g., a product is owned by a single firm).

The **payoff** to each player ![](https://latex.codecogs.com/gif.latex?p) depends on:

1. **Revenue or Value** extracted from certain components’ usage.  
2. **Costs** of investment or maintenance.  
3. Possibly **strategic advantages** from forcing a competitor to rely on a less evolved (higher-cost) resource, or from accelerating commoditization to disrupt a competitor’s revenue model.

Symbolically, define a **per-period payoff** function

![](https://latex.codecogs.com/gif.latex?\Pi_p\bigl(\mathbf{E}(t),%20\mathbf{I}^{(p)}(t)\bigr),)

where ![](https://latex.codecogs.com/gif.latex?\mathbf{E}(t)) is the vector of all evolution states at time ![](https://latex.codecogs.com/gif.latex?t).

### 5.2 Equilibrium or Optimization

If the players move simultaneously, one can seek a **Nash equilibrium** for the investments:

![](https://latex.codecogs.com/gif.latex?\%7BI_i^{(p)*}\%7D_{i,p}),

such that no player can unilaterally deviate and improve their expected payoff.

Alternatively, if there is a clear hierarchy (e.g., a major vendor as a **leader** deciding on open-sourcing a commodity, then smaller companies reacting), you can embed these dynamics in a **Stackelberg** or **bilevel** model.

---

## 6. Incorporating Dependency (Value Chain) Effects

Wardley Maps emphasize how a **higher-level component** uses a **lower-level component**. This can be modeled in the **payoffs** or **evolution** equations:

1. **Payoff Dependence**: If component ![](https://latex.codecogs.com/gif.latex?j) is crucial to ![](https://latex.codecogs.com/gif.latex?i), then the “value” or “functionality” of ![](https://latex.codecogs.com/gif.latex?i) might be limited until ![](https://latex.codecogs.com/gif.latex?j) is sufficiently evolved. For example:

   ![](https://latex.codecogs.com/gif.latex?\Pi_p(\ldots)%20\propto%20\min\bigl(E_j(t),%20E_i(t)\bigr))

   or some function that ties ![](https://latex.codecogs.com/gif.latex?E_i) to the evolving state of its dependencies.

2. **Cascade Effects**: If a lower-level component ![](https://latex.codecogs.com/gif.latex?j) becomes a well-established commodity (![](https://latex.codecogs.com/gif.latex?E_j%20\approx%201)), it might **accelerate** the evolution of the higher-level ![](https://latex.codecogs.com/gif.latex?i). This can be factored into the S-curve rate for ![](https://latex.codecogs.com/gif.latex?i):

   ![](https://latex.codecogs.com/gif.latex?\frac%7BdE_i%7D%7Bdt%7D%20=%20f\Bigl(E_i(t),\%20\%7BE_k(t)\mid%20(i,k)\in%20\mathcal{D}\%7D,\%20\alpha_i\Bigr).)

3. **Cost Structures**: If a company invests heavily to commoditize ![](https://latex.codecogs.com/gif.latex?j), it might reduce the overall cost or friction for ![](https://latex.codecogs.com/gif.latex?i). This again modifies ![](https://latex.codecogs.com/gif.latex?\alpha_i) or the payoff terms accordingly.

---

## 7. Example of a Simple Discrete-Time Model

Let us sketch a minimal **discrete-time** system to see how it might work in practice:

1. **Initialize**:  
   - ![](https://latex.codecogs.com/gif.latex?E_i(0)) for all ![](https://latex.codecogs.com/gif.latex?i\in\mathcal{C}).  
   - Visibility ![](https://latex.codecogs.com/gif.latex?V_i).  
   - Dependency graph ![](https://latex.codecogs.com/gif.latex?\mathcal{D}).  
   - Players’ initial budgets, strategies, etc.

2. **At each time step** ![](https://latex.codecogs.com/gif.latex?t=0,1,2,\ldots):  
   1. **Players choose investments**: ![](https://latex.codecogs.com/gif.latex?\%7BI_i^{(p)}(t)\%7D) or other strategic actions.  
   2. **Compute total investment** in each component ![](https://latex.codecogs.com/gif.latex?i):  
      
      ![](https://latex.codecogs.com/gif.latex?I_i(t)%20=%20\sum_{p}%20I_i^{(p)}(t)).  
      
   3. **Update evolution states**:

      ![](https://latex.codecogs.com/gif.latex?E_i(t+1)%20=%20E_i(t)%20+%20\alpha_i\bigl(I_i(t),%5C,%20C_i(t)\bigr)%20E_i(t)%20\bigl(1-E_i(t)\bigr).)

      Possibly incorporate dependency terms or synergy factors from other components ![](https://latex.codecogs.com/gif.latex?k) that ![](https://latex.codecogs.com/gif.latex?i) uses.  

   4. **Compute payoffs** for each player:

      ![](https://latex.codecogs.com/gif.latex?\Pi_p(t+1)%20=%20\sum_{i\in\mathcal{C}_p}%20\text{Revenue}_p\bigl(E_i(t+1)\bigr)%20-%20\text{Cost}_p\bigl(\%7BI_i^{(p)}(t)\%7D\bigr),)

      where ![](https://latex.codecogs.com/gif.latex?\mathcal{C}_p) is the set of components relevant to player ![](https://latex.codecogs.com/gif.latex?p).

3. **End Condition**: Continue until a steady state or for a fixed horizon. Analyze final states ![](https://latex.codecogs.com/gif.latex?\%7BE_i(T)\%7D), player payoffs, and the structure of the “map” to derive strategic insights.

This cycle provides a **simulation-based** approach where you can adjust assumptions about how quickly components evolve and see how the Wardley map changes over time.

---

## 8. Possible Extensions and Uses

1. **Scenario Planning**: Vary exogenous parameters (e.g., market disruptions, technology leaps) to see how the X-axis positions shift.  
2. **Sensitivity Analysis**: Identify which investments or dependencies have the biggest impact on final payoffs.  
3. **Comparative Strategies**: Evaluate different player strategies (e.g., quickly commoditizing a key component vs. differentiating it) and measure outcomes.  
4. **Agent-Based Simulations**: Instead of a purely game-theoretic approach, let each player or “agent” follow heuristics (e.g., invests proportionally to ROI) and observe emergent Wardley map patterns.

---

## 9. Limitations and Cautions

- **Qualitative to Quantitative**: In real Wardley Mapping, the Y-axis (visibility) is not always a strict, numeric measure. Attempts to “force” everything into a precise scale can lose important **context** or lead to oversimplification.  
- **Complex Dynamics**: True evolution involves feedback loops, exogenous shocks, and intangible factors (e.g., brand perception, organizational culture). A single equation might be too simplistic.  
- **Data Scarcity**: Calibrating ![](https://latex.codecogs.com/gif.latex?\alpha_i) or payoff functions requires historical data or expert judgment.  
- **Interpretation**: Even with a formal model, the strategic insights often come from **visual**, **iterative**, and **creative** use of the map—so the math is an aid, not a replacement for strategic sense-making.

---

## Concluding Remarks

By **translating** the conceptual elements of Wardley Mapping into states, investments, payoff functions, and evolution dynamics, we can create a **stylized mathematical model** that:

- Places each component on a continuous scale of **evolution** (X-axis).  
- Fixes or estimates a **visibility** or **value** parameter (Y-axis).  
- Updates evolution over time via **S-curves** or other functional forms.  
- Incorporates **strategic interactions** (investments, open-sourcing, competition) in a game-theoretic or agent-based simulation framework.

Such a model can help with **scenario testing**, **simulation-based planning**, and deeper analysis of **how organizational choices** might shift the map. However, it is crucial to remember that **Wardley Maps** were designed primarily as a **visual sense-making tool**—the rigor of a math model should augment, not overshadow, the map’s original purpose of helping teams see where their strategic components are heading and why that matters.
