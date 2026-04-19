# Extending Wardley Maps: Layer-Based Visibility and Sigmoid Evolution

Wardley Maps are a powerful tool for visualizing **value chains** and **strategic evolution**. Part 1 established the core model with graph-distance visibility and a continuous evolution score. This part explores two refinements that better fit real-world systems:

1. **Layer-Based Visibility** on the vertical axis
2. A **Sigmoid (S-Curve) Evolution** function for the horizontal axis

These adaptations help when the dependency graph has multiple value streams, layered dependencies, or when adoption follows an S-curve rather than a linear progression.

---

## 1. Recap: The Essentials of Wardley Maps

### 1.1. Basic Coordinates

A Wardley Map places components $v \in V$ in two dimensions:

- **Vertical axis ($\nu$, visibility)**: How "close" each component is to the user. The user (or customer) is typically at the top, deep infrastructure at the bottom.
- **Horizontal axis ($\varepsilon$, evolution)**: Tracks progression from a **new, unproven** or **custom-built** stage (far left) to a **ubiquitous**, **standardized**, **commodity** state (far right).

### 1.2. Traditional Approach (from Part 1)

1. **Visibility** is often approximated by graph distance from the user node, e.g. $\nu(v) = 1/(1+d(v))$.
2. **Evolution** may be scored by a simple function like $\varepsilon(v) = (\mathrm{ubiq}(v) + \mathrm{cert}(v))/2$, combining how widespread ("ubiquity") and well-understood ("certainty") a component is.

These linear formulations can over-simplify reality when you have multiple value streams or when adoption follows an S-curve.

---

## 2. Layer-Based Visibility

### 2.1. Why Layers?

In many systems, simply counting graph distance to the user is too coarse. Components may share dependencies; a user-facing system might have multiple value streams. Rather than just counting edges, identify **discrete layers** of dependencies.

- **Layer 0**: The user (or top-level "user" proxy).
- **Layer 1**: Components directly consumed by the user.
- **Layer 2**: Components that feed Layer 1, etc.

### 2.2. Implementation

1. **Topological sort** the dependency graph (or do a BFS from the user node $u$).
2. Assign each component $v$ a **layer index** $\ell(v)$ based on how many layers sit between it and the user.
3. Define visibility as:

$$\nu(v) = 1 - \frac{\ell(v)}{\max_{v' \in V} \ell(v')}$$

- Components closer to the user (lower $\ell$) get higher $\nu$.
- Deep infrastructure with high $\ell$ gets lower $\nu$.

### 2.3. Value Streams

When multiple user types or product flows exist, you can:

- **Focus** each Wardley Map on one user type at a time (reassigning layers for that user's perspective).
- Or unify them into a single map — but note each user might have a different maximum layer count.

This ensures the vertical axis truly reflects how the user sees the system layers, rather than a purely numeric "distance."

---

## 3. Sigmoid (S-Curve) Evolution

### 3.1. The S-Curve in Real Adoption

Wardley observes that components evolve from **Genesis** to **Utility** following an **S-curve**: slow uptake at first, rapid adoption in the middle, flattening as the market saturates. This is well modeled by the **logistic (sigmoid) function**.

### 3.2. The Logistic Function

A common logistic form is:

$$\varepsilon(v) = \frac{1}{1 + \exp[-\alpha(\mathrm{input}(v) - \beta)]}$$

Where:

- $\mathrm{input}(v)$ might be $\mathrm{ubiq}(v) + \mathrm{cert}(v)$ (or another combination).
- $\alpha > 0$ sets the **steepness** of the curve.
- $\beta$ sets the **midpoint**.

### 3.3. Normalizing Inputs

A weighted combination of ubiquity and certainty works well:

$$\mathrm{input}(v) = w_1 \cdot \mathrm{ubiq}(v) + w_2 \cdot \mathrm{cert}(v)$$

Then:

1. If $\mathrm{input}(v) \approx \beta$, we're around the **midpoint** of the S-curve.
2. Above that, we rapidly approach the **commodity** end. Below that, we remain in **custom** or **genesis** territory.

Large $\alpha$ produces a sharp transition; small $\alpha$ produces a gentle one.

---

## 4. Combining the Ideas

**Layer-based vertical** + **sigmoid-based horizontal** = a more accurate representation:

- **Vertical**: Clarifies how many "layers" a component is removed from direct user interaction.
- **Horizontal**: Reflects **S-curve adoption** patterns rather than a simplistic linear scale.

---

## 5. Practical Steps

1. **Define your value stream(s)**
   - Identify which user(s) you want to map.
   - Extract relevant components and dependencies for that user flow.

2. **Layer assignment**
   - Perform a BFS or topological sort from the user node $u$.
   - $\ell(v)$ = how many layers from user to $v$.
   - $\nu(v) = 1 - \ell(v) / \max_{v'} \ell(v')$.

3. **Adoption data**
   - Rate each component's **ubiquity** (0 = rare, 1 = widespread).
   - Rate each component's **certainty** (0 = unproven, 1 = fully standardized).

4. **Sigmoid evolution**
   - Combine those scores, feed them into a logistic function.
   - Tune $\alpha$ and $\beta$ to match your domain's adoption dynamics.

5. **Plot the map**
   - Each component → $(\varepsilon(v), \nu(v))$.
   - Draw dependencies accordingly.

---

## 6. Advantages and Caveats

### 6.1. Advantages

1. **Layered clarity**: The vertical axis is more intuitive (Layer 1, Layer 2, etc.).
2. **Realistic adoption**: The S-curve captures how technology actually transitions.
3. **Value stream focus**: Different user flows, each with its own layering, can be mapped precisely.

### 6.2. Caveats

1. **Data collection**: More overhead in computing layers and determining logistic parameters.
2. **Subjectivity**: Deciding $\alpha$, $\beta$, or the weighting of ubiquity vs. certainty remains subjective.
3. **Multiple maps**: If you have many user types, you may generate multiple partial Wardley Maps.

---

## 7. Conclusion

When the default Wardley Map approach feels too simplistic — especially with layered systems or S-curve adoption dynamics — consider:

1. **Layer-based** vertical scaling for each user.
2. A **sigmoid** function for the horizontal evolution measure.

These refinements better match real-world user journeys (vertical) and more accurately reflect market and technology evolution (horizontal), leading to more robust strategic insights when deciding where to innovate and how to leverage commodities in your value chain.
