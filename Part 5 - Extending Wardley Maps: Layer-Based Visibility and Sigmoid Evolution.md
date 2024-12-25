## 1. Vertical Axis: Layer-Based Visibility

### 1.1. Counting Layers Above Each Node

Instead of the simple “distance from the user” approach, you could measure **how many ‘layers’ of nodes** exist above a given component in the value chain. One method:

1. Perform a **topological sort** (or multiple sorts if multiple user entry points exist).  
2. Identify each node’s **layer number** — i.e., how many layers of dependencies sit above it.

Then define a **visibility function** ![](https://latex.codecogs.com/png.latex?V%28c_i%29%20%3D%201%20-%20%5Cfrac%7B%5Cell%28c_i%29%7D%7B%5Cmax%5Cell%28c_j%29%7D), where:

- ![](https://latex.codecogs.com/png.latex?%5Cell%28c_i%29%20%3D%200) if the component **is** the user (or top-level user proxy).
- ![](https://latex.codecogs.com/png.latex?%5Cmax_%7Bc_j%7D%5Cell%28c_j%29) is the maximum layer index in the **entire** graph (the “deepest” node).

> **Rationale**:  
> - **Visibility** becomes “How many steps are you from direct user interaction, in terms of discrete layers of dependencies?”  
> - The user node(s) have ![](https://latex.codecogs.com/png.latex?V%20%5Capprox%201), the deepest nodes near ![](https://latex.codecogs.com/png.latex?V%20%5Capprox%200).  
> - You can also adapt it per **value stream**, if each user defines a different top-level context.

---

## 2. Horizontal Axis: Sigmoid (Logistic) Evolution

### 2.1. Why a Sigmoid?

Wardley’s “Genesis → Commodity” progression often follows **S-curve adoption**:
- **Slow** adoption at first (new, uncertain).
- **Accelerated** in the middle.
- **Flattening** near saturation (commodity).

A **logistic (sigmoid) function** matches this shape. Consider something like:

![](https://latex.codecogs.com/png.latex?E%28c_i%29%20%3D%20%5Cfrac%7B1%7D%7B1%20%2B%20%5Cexp%5B-%5Calpha%28%5Cmathrm%7Binput%7D_i%20-%20%5Cbeta%29%5D%7D)

Where:
- **input** might be some combination of **ubiquity** and **certainty**.
- ![](https://latex.codecogs.com/png.latex?%5Calpha) > 0 controls **steepness** of the S-curve.
- ![](https://latex.codecogs.com/png.latex?%5Cbeta) shifts the **center** along the input axis.

### 2.2. Normalizing Inputs

First, combine **ubiquity** (U) and **certainty** (C) into a single value. For example:

![](https://latex.codecogs.com/png.latex?%5Cmathrm%7Binput%7D_i%20%3D%20w_1%20%5Ccdot%20U%28c_i%29%20+%20w_2%20%5Ccdot%20C%28c_i%29).

Then plug into the logistic equation:

![](https://latex.codecogs.com/png.latex?E%28c_i%29%20%3D%20%5Cfrac%7B1%7D%7B1%20+%20%5Cexp%5B-%5Calpha%28%5Cmathrm%7Binput%7D_i%20-%20%5Cbeta%29%5D%7D.)

- Large ![](https://latex.codecogs.com/png.latex?%5Calpha) ⇒ sharp transition.
- ![](https://latex.codecogs.com/png.latex?%5Cbeta) ⇒ sets the midpoint of the S-curve.

Hence, the evolution axis better represents an **accelerating** shift from custom to commodity.

---

## 3. Value Stream–Specific Vertical Scale

You mentioned the vertical scale is **relative to each value stream**. When you have multiple user “entry points” or varied service flows:

1. Choose **one** user node (or a small set) for each value stream.  
2. Compute layers/distances only for the **subgraph** relevant to that stream.  
3. The result: each value chain has a top at ![](https://latex.codecogs.com/png.latex?V%20%3D%201) (the user), and a bottom near ![](https://latex.codecogs.com/png.latex?V%20%3D%200) for the farthest hidden infrastructure.

Sometimes you **merge** all users into a single “map,” but for clarity you might produce **partial** maps, each focusing on a different user journey.

---

## 4. Summary

1. **Layer-based (or distance-based) Vertical**  
   ![](https://latex.codecogs.com/png.latex?V%28c_i%29%20%3D%201%20-%20%5Cfrac%7B%5Cell%28c_i%29%7D%7B%5Cmax%5Cell%28c_j%29%7D)  
   or  
   ![](https://latex.codecogs.com/png.latex?V%28c_i%29%20%3D%201%20-%20%5Cfrac%7Bd%28%5Ctext%7BUser%7D%2C%20c_i%29%7D%7Bd_%5Cmathrm%7Bmax%7D%7D).

2. **Sigmoid-based Horizontal**  
   ![](https://latex.codecogs.com/png.latex?E%28c_i%29%20%3D%20%5Cfrac%7B1%7D%7B1%20%2B%20%5Cexp%5B-%5Calpha%28%5Cmathrm%7Binput%7D_i%20-%20%5Cbeta%29%5D%7D),  
   ![](https://latex.codecogs.com/png.latex?%5Cmathrm%7Binput%7D_i%20%3D%20w_1%20%5Ccdot%20U%28c_i%29%20+%20w_2%20%5Ccdot%20C%28c_i%29).

3. **Normalize**  
   - Adjust ![](https://latex.codecogs.com/png.latex?%5Calpha) and ![](https://latex.codecogs.com/png.latex?%5Cbeta) to match real-world adoption patterns.

4. **Value Stream–Specific**  
   - Each user or user group can define a separate “distance” or layer scale if needed.

By combining **layer-based visibility** (vertical) and **sigmoid-based evolution** (horizontal), you can achieve a **more realistic** Wardley Map that mirrors **S-curve adoption** while respecting the **unique value streams** and **layering** of your system.
