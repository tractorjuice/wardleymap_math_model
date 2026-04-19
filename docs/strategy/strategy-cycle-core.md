# A Possible Mathematical Model for the Wardley Strategy Cycle

Below is one way to capture the Wardley "strategy cycle" in a **discrete-time, dynamical-systems** style model—mixing John Boyd's OODA Loop, Sun Tzu's Five Factors, and Wardley's "two whys." Real-world strategy is, of course, far more nuanced, but this sketch illustrates one mathematical formalization.

---

## 1. State Variables

Let time evolve in discrete steps $t = 0, 1, 2, \dots$. Define:

- **External (environmental) state** $X(t)$
  This represents market conditions, competitor positions, user behavior, tech shifts, etc.

- **Internal (organizational) state** $Y(t)$
  This could include resources, competencies, structures, culture, and more.

- **Why of Purpose** $P(t)$
  The overarching mission or reason for the organization's existence.

- **Why of Movement** $M(t)$
  The tactical rationale for _how_ and _why_ you move from one state to another in the near term.

To align with **Sun Tzu's Five Factors**:

1. **Purpose** → already captured by $P(t)$.
2. **Climate** → part of $X(t)$ (external forces, market trends).
3. **Landscape** → also part of $X(t)$ (competitor maps, value chains).
4. **Doctrine** → included in $Y(t)$ (principles, best practices).
5. **Leadership** → also embedded in $Y(t)$ (decision-making structure, style).

---

## 2. OODA-Based Cycle

We capture **Observe → Orient → Decide → Act** as four functions each step.

1. **Observe**

   $$O(t) = \mathrm{Obs}(X(t), Y(t))$$

   A function extracting relevant data from both external and internal states.

2. **Orient**

   $$R(t) = \mathrm{Ori}(O(t), P(t), M(t))$$

   Incorporates the observation plus the two whys (purpose and movement) into an updated "mental model."

3. **Decide**

   $$D(t) = \mathrm{Dec}(R(t))$$

   A function that produces a decision or plan based on the oriented model $R(t)$.

4. **Act**

   $$A(t) = \mathrm{Act}(D(t))$$

   A function that converts the decision into a real-world action $A(t)$.

---

## 3. Evolution of the System

After **Act**, both external and internal states update:

$$[X(t+1), Y(t+1)] = T(X(t), Y(t), A(t))$$

where $T$ captures how the environment and organization change in response to the action $A(t)$.

We also update our "two whys":

$$P(t+1) = \mathrm{UpdatePurpose}(P(t), X(t+1), Y(t+1))$$

$$M(t+1) = \mathrm{UpdateMovement}(M(t), D(t), A(t))$$

- **Why of Purpose** may evolve slowly (rare major pivots).
- **Why of Movement** updates frequently, explaining tactical rationale for each move.

---

## 4. Possible Objective Functions

To make it an **optimization** problem, define a utility or performance function:

$$J = \sum_{t=0}^{T-1} U(X(t), Y(t), P(t))$$

where $U$ measures strategic performance. We can also penalize misalignment with doctrine or leadership constraints:

$$J = \sum_{t=0}^{T-1} \left[ U(X(t), Y(t), P(t)) - \lambda \mathrm{Penalty}(D(t), \text{Doctrine}, \text{Leadership}) \right]$$

The **Decide** step might pick $D(t)$ to maximize expected future utility:

$$D(t) = \underset{d}{\mathrm{arg\,max}}\, \mathbb{E}[U(X(t+1), Y(t+1), P(t+1)) | X(t), Y(t), P(t), M(t)]$$

subject to constraints (e.g., doctrine, leadership).

---

## 5. Tying It All Together

- **Sun Tzu's Five Factors** appear as internal/external states or constraints.
- **Wardley's Two Whys** → $P(t)$ (purpose) and $M(t)$ (movement).
- The **OODA loop** runs as a closed-loop cycle:

  1. $O(t) = \mathrm{Obs}(X(t), Y(t))$
  2. $R(t) = \mathrm{Ori}(O(t), P(t), M(t))$
  3. $D(t) = \mathrm{Dec}(R(t))$
  4. $A(t) = \mathrm{Act}(D(t))$
  5. $[X(t+1), Y(t+1)] = T(X(t), Y(t), A(t))$
  6. $P(t+1) = \mathrm{UpdatePurpose}(P(t), X(t+1), Y(t+1))$, $M(t+1) = \mathrm{UpdateMovement}(M(t), D(t), A(t))$

**Repeat for** $t \to t+1$.

---

## 6. Conclusion

This discrete-time model casts the Wardley strategy cycle (with OODA, Sun Tzu's five factors, and Wardley's two whys) as a **closed-loop dynamical system**. By specifying how the organization observes, orients, decides, and acts—and how its states update—one can apply everything from **control theory** to **reinforcement learning** to formalize strategic decision-making. Of course, real strategy is more nuanced, but this provides a framework for systematic analysis.
