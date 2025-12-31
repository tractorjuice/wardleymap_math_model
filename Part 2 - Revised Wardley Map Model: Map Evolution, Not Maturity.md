# Revised Wardley Map Model: "Map Evolution, Not Maturity"

Below is an **updated** mathematical model that reflects the insight from
["Map Evolution, Not Maturity"](https://medium.com/mappingpractice/map-evolution-not-maturity-bae6ea1a2743).
In other words, **Evolution** isn't merely "age" or "time in market," but rather how **competition** (supply & demand) drives a component from a novel idea to a widely available commodity.

---

## 1. Original Setup (Recap)

We have a set of **components**:

$$\mathcal{C} = \{c_1, c_2, \dots, c_n\}$$

along with **dependencies** forming a directed graph. An edge

$(c_i, c_j) \in \mathcal{E}$

means $c_i$ depends on $c_j$.

We also define two mappings:

1. **Visibility** (vertical axis) $V(c_i)$ — how obvious or "close" a component is to the user.

2. **Evolution** (horizontal axis) $E(c_i)$ — how far along the path from novel/uncertain to commodity/standardized a component is.

Each component becomes a point:

$$M(c_i) = \bigl(E(c_i), V(c_i)\bigr)$$

---

## 2. Visibility (Vertical)

One way to measure **visibility**:

1. Let $\mathrm{dist}(c_i)$ be the shortest path distance from the **User** to $c_i$.

2. Normalize this distance to produce $V(c_i)$:

   $$V(c_i) = 1 - \frac{\mathrm{dist}(c_i)}{\max \mathrm{dist}(c_j)}$$

- If $c_i$ is the user, then distance is 0 → **visibility** = 1.
- If $c_i$ is far from the user, $V(c_i)$ approaches 0.

Hence, the **vertical coordinate** is: $y_i = V(c_i)$.

---

## 3. Evolution (Horizontal) — Updated

Per the article, **Evolution** shouldn't be reduced to "maturity" or "time in market." Instead, it's driven by:

- **Ubiquity** (how widespread a component is, i.e. supply & demand competition)
- **Certainty** (how standardized or well-understood it is)

Let $\mathrm{ubiq}(c_i)$ and $\mathrm{cert}(c_i)$ both range in $[0, 1]$.

- 0 = rare, unknown, no best practices
- 1 = commodity, ubiquitous, highly standardized

Then define:

$$E(c_i) = \frac{\mathrm{ubiq}(c_i) + \mathrm{cert}(c_i)}{2}$$

1. Low ubiquity + low certainty → near 0 (leftmost = "Genesis / Custom").
2. High ubiquity + high certainty → near 1 (rightmost = "Commodity / Utility").

Thus, the **horizontal coordinate** is: $x_i = E(c_i)$.

---

## 4. Final Coordinates

Each component $c_i$ sits at:

$$M(c_i) = (E(c_i), V(c_i))$$

- **Left → Right** = Movement from novel, uncertain to widespread, standardized.
- **Bottom → Top** = Movement from invisible to user to highly visible.

---

## 5. Interpretation & Rationale

- **Evolution** tracks market‐driven changes in **certainty** & **ubiquity**, reflecting how competition shifts components over time.
- **Visibility** helps you see how these components relate to user needs and **where** each sits in the overall value chain.

**Strategic Takeaway**:
1. **Innovate** on the left (high uncertainty, potential for differentiation).
2. **Leverage commodities** on the right (high ubiquity, low risk, lower cost).
3. Watch how components **move** horizontally over time as the market evolves.

---

### Conclusion

By incorporating **ubiquity** and **certainty** into the **Evolution** function, we align with the principle that **"Evolution is driven by competitive forces, not just age."** This helps teams build **Wardley Maps** that better capture real‐world dynamics of how components shift from **Genesis** to **Utility** as they become ubiquitous and well understood.
