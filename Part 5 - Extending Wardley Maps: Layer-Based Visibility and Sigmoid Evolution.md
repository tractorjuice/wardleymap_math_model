## 1. Vertical Axis: Layer-Based Visibility

### 1.1. Counting Layers Above Each Node

Instead of the simple "distance from the user" approach, you could measure **how many 'layers' of nodes** exist above a given component in the value chain. One method:

1. Perform a **topological sort** (or multiple sorts if multiple user entry points exist).
2. Identify each node's **layer number** — i.e., how many layers of dependencies sit above it.

Then define a **visibility function** $V(c_i) = 1 - \frac{\ell(c_i)}{\max\ell(c_j)}$, where:

- $\ell(c_i) = 0$ if the component **is** the user (or top-level user proxy).
- $\max_{c_j}\ell(c_j)$ is the maximum layer index in the **entire** graph (the "deepest" node).

> **Rationale**:
> - **Visibility** becomes "How many steps are you from direct user interaction, in terms of discrete layers of dependencies?"
> - The user node(s) have $V \approx 1$, the deepest nodes near $V \approx 0$.
> - You can also adapt it per **value stream**, if each user defines a different top-level context.

---

## 2. Horizontal Axis: Sigmoid (Logistic) Evolution

### 2.1. Why a Sigmoid?

Wardley's "Genesis → Commodity" progression often follows **S-curve adoption**:
- **Slow** adoption at first (new, uncertain).
- **Accelerated** in the middle.
- **Flattening** near saturation (commodity).

A **logistic (sigmoid) function** matches this shape. Consider something like:

$$E(c_i) = \frac{1}{1 + \exp[-\alpha(\mathrm{input}_i - \beta)]}$$

Where:
- **input** might be some combination of **ubiquity** and **certainty**.
- $\alpha > 0$ controls **steepness** of the S-curve.
- $\beta$ shifts the **center** along the input axis.

### 2.2. Normalizing Inputs

First, combine **ubiquity** (U) and **certainty** (C) into a single value. For example:

$$\mathrm{input}_i = w_1 \cdot U(c_i) + w_2 \cdot C(c_i)$$

Then plug into the logistic equation:

$$E(c_i) = \frac{1}{1 + \exp[-\alpha(\mathrm{input}_i - \beta)]}$$

- Large $\alpha$ ⇒ sharp transition.
- $\beta$ ⇒ sets the midpoint of the S-curve.

Hence, the evolution axis better represents an **accelerating** shift from custom to commodity.

---

## 3. Value Stream–Specific Vertical Scale

You mentioned the vertical scale is **relative to each value stream**. When you have multiple user "entry points" or varied service flows:

1. Choose **one** user node (or a small set) for each value stream.
2. Compute layers/distances only for the **subgraph** relevant to that stream.
3. The result: each value chain has a top at $V = 1$ (the user), and a bottom near $V = 0$ for the farthest hidden infrastructure.

Sometimes you **merge** all users into a single "map," but for clarity you might produce **partial** maps, each focusing on a different user journey.

---

## 4. Summary

1. **Layer-based (or distance-based) Vertical**

   $$V(c_i) = 1 - \frac{\ell(c_i)}{\max\ell(c_j)}$$

   or

   $$V(c_i) = 1 - \frac{d(\text{User}, c_i)}{d_{\mathrm{max}}}$$

2. **Sigmoid-based Horizontal**

   $$E(c_i) = \frac{1}{1 + \exp[-\alpha(\mathrm{input}_i - \beta)]}$$

   $$\mathrm{input}_i = w_1 \cdot U(c_i) + w_2 \cdot C(c_i)$$

3. **Normalize**
   - Adjust $\alpha$ and $\beta$ to match real-world adoption patterns.

4. **Value Stream–Specific**
   - Each user or user group can define a separate "distance" or layer scale if needed.

By combining **layer-based visibility** (vertical) and **sigmoid-based evolution** (horizontal), you can achieve a **more realistic** Wardley Map that mirrors **S-curve adoption** while respecting the **unique value streams** and **layering** of your system.
