# A Possible Mathematical Model for the Wardley Strategy Cycle

Below is one way to capture the Wardley “strategy cycle” in a **discrete‐time, dynamical‐systems** style model—mixing John Boyd’s OODA Loop, Sun Tzu’s Five Factors, and Wardley’s “two whys.” Real‐world strategy is, of course, far more nuanced, but this sketch illustrates one mathematical formalization.

---

## 1. State Variables

Let time evolve in discrete steps ![](https://latex.codecogs.com/png.latex?t%20%3D%200%2C%201%2C%202%2C%20%5Cdots). Define:

- **External (environmental) state**  
  ![](https://latex.codecogs.com/png.latex?X%28t%29)  
  This represents market conditions, competitor positions, user behavior, tech shifts, etc.

- **Internal (organizational) state**  
  ![](https://latex.codecogs.com/png.latex?Y%28t%29)  
  This could include resources, competencies, structures, culture, and more.

- **Why of Purpose**  
  ![](https://latex.codecogs.com/png.latex?P%28t%29)  
  The overarching mission or reason for the organization’s existence.

- **Why of Movement**  
  ![](https://latex.codecogs.com/png.latex?M%28t%29)  
  The tactical rationale for _how_ and _why_ you move from one state to another in the near term.

To align with **Sun Tzu’s Five Factors**:

1. **Purpose** → already captured by ![](https://latex.codecogs.com/png.latex?P%28t%29).  
2. **Climate** → part of ![](https://latex.codecogs.com/png.latex?X%28t%29) (external forces, market trends).  
3. **Landscape** → also part of ![](https://latex.codecogs.com/png.latex?X%28t%29) (competitor maps, value chains).  
4. **Doctrine** → included in ![](https://latex.codecogs.com/png.latex?Y%28t%29) (principles, best practices).  
5. **Leadership** → also embedded in ![](https://latex.codecogs.com/png.latex?Y%28t%29) (decision‐making structure, style).

---

## 2. OODA‐Based Cycle

We capture **Observe → Orient → Decide → Act** as four functions each step.

1. **Observe**  
   ![](https://latex.codecogs.com/png.latex?O%28t%29%20%3D%20%5Cmathrm%7BObs%7D%28X%28t%29%2C%20Y%28t%29%29)  
   A function extracting relevant data from both external and internal states.

2. **Orient**  
   ![](https://latex.codecogs.com/png.latex?R%28t%29%20%3D%20%5Cmathrm%7BOri%7D%28O%28t%29%2C%20P%28t%29%2C%20M%28t%29%29)  
   Incorporates the observation plus the two whys (purpose and movement) into an updated “mental model.”

3. **Decide**  
   ![](https://latex.codecogs.com/png.latex?D%28t%29%20%3D%20%5Cmathrm%7BDec%7D%28R%28t%29%29)  
   A function that produces a decision or plan based on the oriented model ![](https://latex.codecogs.com/png.latex?R%28t%29).

4. **Act**  
   ![](https://latex.codecogs.com/png.latex?A%28t%29%20%3D%20%5Cmathrm%7BAct%7D%28D%28t%29%29)  
   A function that converts the decision into a real‐world action ![](https://latex.codecogs.com/png.latex?A%28t%29).

---

## 3. Evolution of the System

After **Act**, both external and internal states update:

![](https://latex.codecogs.com/png.latex?%5BX%28t%2B1%29%2C%20Y%28t%2B1%29%5D%20%3D%20T%28X%28t%29%2C%20Y%28t%29%2C%20A%28t%29%29)

where ![](https://latex.codecogs.com/png.latex?T) captures how the environment and organization change in response to the action ![](https://latex.codecogs.com/png.latex?A%28t%29).

We also update our “two whys”:

![](https://latex.codecogs.com/png.latex?P%28t%2B1%29%20%3D%20%5Cmathrm%7BUpdatePurpose%7D%28P%28t%29%2C%20X%28t%2B1%29%2C%20Y%28t%2B1%29%29)

![](https://latex.codecogs.com/png.latex?M%28t%2B1%29%20%3D%20%5Cmathrm%7BUpdateMovement%7D%28M%28t%29%2C%20D%28t%29%2C%20A%28t%29%29)

- **Why of Purpose** may evolve slowly (rare major pivots).  
- **Why of Movement** updates frequently, explaining tactical rationale for each move.

---

## 4. Possible Objective Functions

To make it an **optimization** problem, define a utility or performance function:

![](https://latex.codecogs.com/png.latex?J%20%3D%20%5Csum_%7Bt%3D0%7D%5E%7BT-1%7D%20U%28X%28t%29%2C%20Y%28t%29%2C%20P%28t%29%29)

where ![](https://latex.codecogs.com/png.latex?U) measures strategic performance. We can also penalize misalignment with doctrine or leadership constraints:

![](https://latex.codecogs.com/png.latex?J%20%3D%20%5Csum_%7Bt%3D0%7D%5E%7BT-1%7D%20%5B%20U%28X%28t%29%2C%20Y%28t%29%2C%20P%28t%29%29%20-%20%5Clambda%20%5Cmathrm%7BPenalty%7D%28D%28t%29%2C%20%5Ctext%7BDoctrine%7D%2C%20%5Ctext%7BLeadership%7D%29%20%5D)

The **Decide** step might pick ![](https://latex.codecogs.com/png.latex?D%28t%29) to maximize expected future utility:

![](https://latex.codecogs.com/png.latex?D%28t%29%20%3D%20%5Cunderset%7Bd%7D%7B%5Cmathrm%7Barg%5C%2Cmax%7D%7D%5C%2C%20%5Cmathbb%7BE%7D%5BU%28X%28t%2B1%29%2C%20Y%28t%2B1%29%2C%20P%28t%2B1%29%29%20%7C%20X%28t%29%2C%20Y%28t%29%2C%20P%28t%29%2C%20M%28t%29%5D)

subject to constraints (e.g., doctrine, leadership).

---

## 5. Tying It All Together

- **Sun Tzu’s Five Factors** appear as internal/external states or constraints.  
- **Wardley’s Two Whys** →  
  ![](https://latex.codecogs.com/png.latex?P%28t%29) (purpose) and  
  ![](https://latex.codecogs.com/png.latex?M%28t%29) (movement).  
- The **OODA loop** runs as a closed‐loop cycle:

  1. ![](https://latex.codecogs.com/png.latex?O%28t%29%20%3D%20%5Cmathrm%7BObs%7D%28X%28t%29%2C%20Y%28t%29%29)
  2. ![](https://latex.codecogs.com/png.latex?R%28t%29%20%3D%20%5Cmathrm%7BOri%7D%28O%28t%29%2C%20P%28t%29%2C%20M%28t%29%29)
  3. ![](https://latex.codecogs.com/png.latex?D%28t%29%20%3D%20%5Cmathrm%7BDec%7D%28R%28t%29%29)
  4. ![](https://latex.codecogs.com/png.latex?A%28t%29%20%3D%20%5Cmathrm%7BAct%7D%28D%28t%29%29)
  5. ![](https://latex.codecogs.com/png.latex?%5BX%28t%2B1%29%2C%20Y%28t%2B1%29%5D%20%3D%20T%28X%28t%29%2C%20Y%28t%29%2C%20A%28t%29%29)
  6. ![](https://latex.codecogs.com/png.latex?P%28t%2B1%29%20%3D%20%5Cmathrm%7BUpdatePurpose%7D%28P%28t%29%2C%20X%28t%2B1%29%2C%20Y%28t%2B1%29%29%2C%20%20M%28t%2B1%29%20%3D%20%5Cmathrm%7BUpdateMovement%7D%28M%28t%29%2C%20D%28t%29%2C%20A%28t%29%29

**Repeat for** ![](https://latex.codecogs.com/png.latex?t%20%5Cto%20t%2B1).

---

## 6. Conclusion

This discrete‐time model casts the Wardley strategy cycle (with OODA, Sun Tzu’s five factors, and Wardley’s two whys) as a **closed‐loop dynamical system**. By specifying how the organization observes, orients, decides, and acts—and how its states update—one can apply everything from **control theory** to **reinforcement learning** to formalize strategic decision‐making. Of course, real strategy is more nuanced, but this provides a framework for systematic analysis.
