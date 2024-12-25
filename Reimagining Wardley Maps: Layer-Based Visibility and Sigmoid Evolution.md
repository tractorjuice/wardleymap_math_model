# Reimagining Wardley Maps: Layer-Based Visibility and Sigmoid Evolution

Wardley Maps are a powerful tool for visualizing **value chains** and **strategic evolution**. Traditionally, they rely on:

1. A **vertical axis (visibility)** measured by “distance from the user.”  
2. A **horizontal axis (evolution)** capturing how components move from **Genesis** to **Commodity** over time.

However, real-world systems can be complex. You may have multiple **value streams**, layered dependencies, and nuanced adoption curves. Below we explore **two** adaptations:

1. **Layer-Based Visibility** on the vertical axis  
2. A **Sigmoid (S-Curve) Evolution** function for the horizontal axis

These tweaks can yield **deeper insights** and better reflect how technology actually evolves in practice.

---

## 1. Recap: The Essentials of Wardley Maps

### 1.1. Basic Coordinates

A Wardley Map places **components** in two dimensions:

- **Vertical axis (Visibility)**: How “close” each component is to the user. The user (or customer) is typically at the top, and deep infrastructure is at the bottom.  
- **Horizontal axis (Evolution)**: Tracks progression from a **new, unproven** or **custom-built** stage (far left) to a **ubiquitous**, **highly standardized**, or **commodity** state (far right).

### 1.2. Traditional Approach

1. **Visibility** is often approximated by the distance (in edges) from the user to the component in the dependency graph.  
2. **Evolution** may be scored by a simple function (like \((\mathrm{ubiq} + \mathrm{cert})/2\)), combining how widespread (“ubiquity”) and well-understood (“certainty”) a component is.

But this linear approach can **over-simplify** reality when you have **multiple value streams** or when **adoption** follows an **S-curve**.

---

## 2. Layer-Based Visibility

### 2.1. Why Layers?

In many systems, simply counting graph distance to the user is too coarse. Some components may share dependencies; a user-facing system might have multiple value streams. Rather than just counting edges, you can identify **discrete layers** of dependencies.

- **Layer 0**: The user (or top-level “user” proxy).  
- **Layer 1**: Components directly consumed by the user.  
- **Layer 2**: Components that feed Layer 1, etc.

### 2.2. Implementation

1. **Topological Sort** your dependency graph (or do a BFS from the user node).  
2. Assign each node a **layer index** \(\ell(c)\) based on how many layers sit between it and the user.  
3. Define **visibility** as:

![](https://latex.codecogs.com/png.latex?V%28c%29%20%3D%201%20-%20%5Cfrac%7B%5Cell%28c%29%7D%7B%5Cmax_%7Bc_j%7D%20%5Cell%28c_j%29%7D)

- Components **closer** to the user (lower \(\ell\)) get higher \(V\).  
- “Deep” infrastructure with high \(\ell\) gets lower \(V\).

### 2.3. Value Streams

Often, you have multiple user types or product flows. You can:

- **Focus** each Wardley Map on **one** user type at a time (reassigning layers for that user’s perspective).  
- Or unify them into a single map — but note each user might have a different maximum layer count.

This ensures the vertical axis **truly** reflects how the user sees the system layers, instead of a purely numeric “distance.”

---

## 3. Sigmoid (S-Curve) Evolution

### 3.1. The S-Curve in Real Adoption

Simon Wardley frequently notes that components evolve from **Genesis** to **Utility** following an **S-curve**: slow uptake at first, rapid adoption in the middle, flattening as the market saturates. This is well modeled by the **logistic (sigmoid) function**.

### 3.2. The Logistic Function

A common logistic form is:

![](https://latex.codecogs.com/png.latex?E%28c%29%20%3D%20%5Cfrac%7B1%7D%7B1%20+%20%5Cexp%5B-%5Calpha%20%28%5Cmathrm%7Binput%7D_c%20-%20%5Cbeta%29%5D%7D)

Where:

- **\(\mathrm{input}_c\)** might be \(\mathrm{ubiq}(c) + \mathrm{cert}(c)\) (or another combination).  
- \(\alpha\) sets the **steepness** of the curve.  
- \(\beta\) sets the **midpoint**.

### 3.3. Example

Let’s define \(\mathrm{input}_c = \mathrm{ubiq}(c) + \mathrm{cert}(c)\). Then:

1. If \(\mathrm{ubiq}(c) + \mathrm{cert}(c) = 1.0\), we’re around the **midpoint** of the S-curve.  
2. Above that, we rapidly approach the **commodity** end. Below that, we remain in **custom** or **genesis** territory.

---

## 4. Combining the Ideas

**Layer-based vertical** + **sigmoid-based horizontal** = a more **accurate** representation:

- **Vertical**: Clarifies how many “layers” a component is removed from direct user interaction.  
- **Horizontal**: Reflects **S-curve adoption** patterns, rather than a simplistic linear scale.

---

## 5. Practical Steps

1. **Define Your Value Stream(s)**  
   - Identify which user(s) you want to map.  
   - Extract relevant components and dependencies for that user flow.

2. **Layer Assignment**  
   - Perform a BFS or topological sort from the user node.  
   - \(\ell(c)\) = how many layers from user to \(c\).  
   - ![](https://latex.codecogs.com/png.latex?V%28c%29%20%3D%201%20-%20%5Cfrac%7B%5Cell%28c%29%7D%7B%5Cmax%20%5Cell%28%5Ccdot%29%7D)

3. **Adoption Data**  
   - Rate each component’s **ubiquity** (0=rare, 1=widespread).  
   - Rate each component’s **certainty** (0=unproven, 1=fully standardized).

4. **Sigmoid Evolution**  
   - Combine those scores, feed them into a logistic function.  
   - Tweak parameters (\(\alpha,\beta\)) to suit your domain’s reality.

5. **Plot the Map**  
   - Each component → \((E(c),V(c))\).  
   - Draw **dependencies** accordingly.

---

## 6. Advantages & Caveats

### 6.1. Advantages

1. **Layered Clarity**: The vertical axis is more intuitive (Layer 1, Layer 2, etc.).  
2. **Realistic Adoption**: The S-curve captures how technology actually transitions.  
3. **Value Stream Focus**: Different user flows, each with its own layering, can be mapped precisely.

### 6.2. Caveats

1. **Data Collection**: More overhead in computing layers and determining logistic parameters.  
2. **Subjectivity**: Deciding \(\alpha\), \(\beta\), or weighting of ubiquity vs. certainty can be subjective.  
3. **Multiple Maps**: If you have many user types, you may generate multiple partial Wardley Maps.

---

## 7. Conclusion

If you find the **default** Wardley Map approach too simplistic—especially with **layered** systems or **S-curve** adoption dynamics—consider:

1. **Layer-based** vertical scaling for each user.  
2. A **sigmoid** function for the horizontal evolution measure.

By doing so, you can **better match** real-world user journeys (vertical) and **more accurately** reflect market/technology evolution (horizontal). This ultimately leads to **more robust** strategic insights when deciding **where to innovate** and **how to leverage** commodities in your value chain.
