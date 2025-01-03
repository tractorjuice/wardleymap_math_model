Below is one way to wrap the Wardley “strategy cycle” into a (somewhat simplified) discrete‐time, dynamical‐systems model. The idea is to capture the cyclical nature of **Observe → Orient → Decide → Act**, while incorporating Sun Tzu’s Five Factors (purpose, climate, landscape, doctrine, leadership) and Wardley’s “two whys” (why of purpose, why of movement). Of course, real‐world strategy is far more nuanced, but this at least sketches one mathematical formalization.

---

## 1. State Variables

We’ll model the organization and its environment at discrete time steps \(t = 0, 1, 2, \dots\). Let

- \(X(t)\) = **external (environmental) state** at time \(t\).  
  - This might encode things like market conditions, competitor positions, user behaviors, technology shifts, etc.

- \(Y(t)\) = **internal (organizational) state** at time \(t\).  
  - This might include resources, competencies, structures, culture, and so on.

- \(P(t)\) = **“why of purpose”** at time \(t\).  
  - A stable or slowly evolving expression of the organization’s overarching mission or reason for being.

- \(M(t)\) = **“why of movement”** at time \(t\).  
  - A more tactical rationale: why we are moving from one state to another in the near term.

We can also decompose the internal/external states further if we wish to track **Sun Tzu’s Five Factors**:

1. **Purpose** \(\to P(t)\) (already a separate variable).  
2. **Climate** \(\subseteq X(t)\) (environmental trends, external constraints).  
3. **Landscape** \(\subseteq X(t)\) (value‐chain positions, competitor mapping, user segments).  
4. **Doctrine** \(\subseteq Y(t)\) (organizational principles/best practices).  
5. **Leadership** \(\subseteq Y(t)\) (leadership style, decision‐making structure).

---

## 2. The OODA‐Based Cycle

We want to capture the four steps **Observe**, **Orient**, **Decide**, and **Act** in each time step. One approach:

1. **Observe**  
   \[
   O(t) \;=\; \mathrm{Obs}\bigl(X(t), Y(t)\bigr)
   \]  
   A function \(\mathrm{Obs}\) that extracts relevant data from both the external and internal state.  

2. **Orient**  
   \[
   R(t) \;=\; \mathrm{Ori}\!\bigl(O(t), P(t), M(t)\bigr)
   \]  
   A function \(\mathrm{Ori}\) that incorporates the current observation \(O(t)\), the long‐term mission \(P(t)\), and short‐term rationale \(M(t)\) into an updated “mental model” \(R(t)\).  

3. **Decide**  
   \[
   D(t) \;=\; \mathrm{Dec}\!\bigl(R(t)\bigr)
   \]  
   A function \(\mathrm{Dec}\) that maps the oriented model \(R(t)\) into a decision or plan \(D(t)\). Decision logic might also consider risk, cost, payoff estimates, or constraints from doctrine and leadership structures.  

4. **Act**  
   \[
   A(t) \;=\; \mathrm{Act}\!\bigl(D(t)\bigr)
   \]  
   A function \(\mathrm{Act}\) that converts the decision into an actual, real‐world action \(A(t)\).  

---

## 3. Evolution of the System

Once we have chosen an action \(A(t)\), both the environment and the organization’s internal state **update** for the next cycle:

\[
\bigl(X(t+1),\,Y(t+1)\bigr) \;=\; T\!\bigl(X(t),\,Y(t),\,A(t)\bigr).
\]

Here, \(T\) is a transition function that models:

- How the environment responds to our action (e.g., changes in market share, competitor responses).  
- How our own organization changes internally (e.g., resource consumption, morale shift, knowledge gained).  

We also want to update the two whys:

\[
P(t+1) \;=\; \mathrm{UpdatePurpose}\bigl(P(t), Y(t+1), X(t+1)\bigr),
\]
\[
M(t+1) \;=\; \mathrm{UpdateMovement}\bigl(M(t), D(t), A(t)\bigr).
\]

- The **why of purpose** may evolve slowly—if at all—based on major strategic pivots or external shocks.  
- The **why of movement** may update more frequently, reflecting ongoing tactical reasoning behind each step.

---

## 4. Possible Objective Functions

To make it more of an **optimization** problem, define an objective or “fitness” function:

\[
J = \sum_{t=0}^{T-1} U\!\bigl(X(t), Y(t), P(t)\bigr),
\]

where \(U\) measures how well the system is performing given the purpose \(P(t)\). You could also penalize decisions misaligned with the organization’s doctrine or leadership constraints:

\[
J = \sum_{t=0}^{T-1} 
\Bigl[
  U\!\bigl(X(t), Y(t), P(t)\bigr)
  \;-\;\lambda \,\mathrm{Penalty}\!\bigl(D(t), \text{Doctrine}, \text{Leadership}\bigr)
\Bigr].
\]

Under this formulation, the \(\mathrm{Dec}\) function in “Decide” might attempt:

\[
D(t) 
= \underset{d}{\mathrm{arg\,max}} 
\;\mathbb{E}\Bigl[\,U\!\bigl(X(t+1), Y(t+1), P(t+1)\bigr) \,\big|\; X(t), Y(t), P(t), M(t)\Bigr]
\]

subject to various constraints. This is akin to a **closed‐loop control** or **model‐predictive control** approach.

---

## 5. Tying It Back to Sun Tzu’s Five Factors

1. **Purpose**: Already captured as \(P(t)\).  
2. **Climate**: Part of \(X(t)\).  
3. **Landscape**: Also part of \(X(t)\).  
4. **Doctrine**: Baked into the internal structure \(Y(t)\) and the penalty/feasibility constraints in \(\mathrm{Dec}\).  
5. **Leadership**: Reflected in how \(\mathrm{Dec}\) is computed, how decisions are authorized, and how the penalty (or feasibility constraints) is shaped.

---

## 6. Summary Diagram

Putting it all together in one cycle step:

1. **Observe**: \(O(t) = \mathrm{Obs}(X(t),\,Y(t))\)
2. **Orient**: \(R(t) = \mathrm{Ori}\bigl(O(t),\,P(t),\,M(t)\bigr)\)
3. **Decide**: \(D(t) = \mathrm{Dec}\bigl(R(t)\bigr)\)
4. **Act**: \(A(t) = \mathrm{Act}\bigl(D(t)\bigr)\)
5. **State Update**: \(\bigl[X(t+1),\,Y(t+1)\bigr] = T\bigl(X(t),\,Y(t),\,A(t)\bigr)\)
6. **Purpose/Movement Update**:
   \[
   P(t+1) = \mathrm{UpdatePurpose}\bigl(P(t), X(t+1), Y(t+1)\bigr), \quad
   M(t+1) = \mathrm{UpdateMovement}\bigl(M(t), D(t), A(t)\bigr).
   \]

Repeat for \(t = t+1\).

---

## Concluding Remarks

1. **Discrete‐time cycles** capture the iterative, feedback‐driven nature of Wardley’s strategy cycle, reminiscent of Boyd’s OODA loop.  
2. **Sun Tzu’s Five Factors** naturally become parts of your internal (\(Y\)) and external (\(X\)) state or shape constraints and utility.  
3. **Wardley’s Two Whys** (\(P(t)\) and \(M(t)\)) enter as either explicit state variables or parameters in your decision/orientation functions.  
4. The entire loop becomes a **closed‐loop dynamical system** in which we can formalize “strategy” as an ongoing series of decisions that evolve with the environment.

No single formula will perfectly represent all the richness of strategy, but this model gives you a starting point: a way to encode strategic considerations in an iterative, math‐friendly structure.
