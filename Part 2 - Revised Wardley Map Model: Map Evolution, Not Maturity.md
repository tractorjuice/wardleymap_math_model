# Revised Wardley Map Model: “Map Evolution, Not Maturity”

Below is an **updated** mathematical model that reflects the insight from  
[“Map Evolution, Not Maturity”](https://medium.com/mappingpractice/map-evolution-not-maturity-bae6ea1a2743).  
In other words, **Evolution** isn’t merely “age” or “time in market,” but rather how **competition** (supply & demand) drives a component from a novel idea to a widely available commodity.  

---

## 1. Original Setup (Recap)

We have a set of **components**:

![](https://latex.codecogs.com/png.latex?%5Cmathcal%7BC%7D%20%3D%20%5C%7Bc_1%2C%20c_2%2C%20%5Cdots%2C%20c_n%5C%7D)

along with **dependencies** forming a directed graph. An edge

![](https://latex.codecogs.com/png.latex?(c_i%2C%20c_j)%20%5Cin%20%5Cmathcal%7BE%7D)

means  
![](https://latex.codecogs.com/png.latex?c_i)  
depends on  
![](https://latex.codecogs.com/png.latex?c_j).

We also define two mappings:

1. **Visibility** (vertical axis)  
   ![](https://latex.codecogs.com/png.latex?V(c_i))  
   — how obvious or “close” a component is to the user.

2. **Evolution** (horizontal axis)  
   ![](https://latex.codecogs.com/png.latex?E(c_i))  
   — how far along the path from novel/uncertain to commodity/standardized a component is.

Each component becomes a point:

![](https://latex.codecogs.com/png.latex?M(c_i)%20%3D%20%5Cbigl(E(c_i)%2C%20V(c_i)%5Cbigr))

---

## 2. Visibility (Vertical)

One way to measure **visibility**:

1. Let  
   ![](https://latex.codecogs.com/png.latex?%5Cmathrm%7Bdist%7D(c_i))  
   be the shortest path distance from the **User** to  
   ![](https://latex.codecogs.com/png.latex?c_i).  

2. Normalize this distance to produce  
   ![](https://latex.codecogs.com/png.latex?V(c_i)):  

   ![](https://latex.codecogs.com/png.latex?V(c_i)%20%3D%201%20-%20%5Cfrac%7B%5Cmathrm%7Bdist%7D(c_i)%7D%7B%5Cmax%5Cmathrm%7Bdist%7D(c_j)%7D).

- If  
  ![](https://latex.codecogs.com/png.latex?c_i)  
  is the user, then distance is 0 → **visibility** = 1.  
- If  
  ![](https://latex.codecogs.com/png.latex?c_i)  
  is far from the user,  
  ![](https://latex.codecogs.com/png.latex?V(c_i))  
  approaches 0.

Hence, the **vertical coordinate** is:  
![](https://latex.codecogs.com/png.latex?y_i%20%3D%20V(c_i)).

---

## 3. Evolution (Horizontal) — Updated

Per the article, **Evolution** shouldn’t be reduced to “maturity” or “time in market.” Instead, it’s driven by:

- **Ubiquity** (how widespread a component is, i.e. supply & demand competition)  
- **Certainty** (how standardized or well-understood it is)

Let  
![](https://latex.codecogs.com/png.latex?%5Cmathrm%7Bubiq%7D(c_i))  
and  
![](https://latex.codecogs.com/png.latex?%5Cmathrm%7Bcert%7D(c_i))  
both range in  
![](https://latex.codecogs.com/png.latex?[0%2C%201]).  

- 0 = rare, unknown, no best practices  
- 1 = commodity, ubiquitous, highly standardized

Then define:

![](https://latex.codecogs.com/png.latex?E(c_i)%20%3D%20%5Cfrac%7B%5Cmathrm%7Bubiq%7D(c_i)%20+%20%5Cmathrm%7Bcert%7D(c_i)%7D%7B2%7D).

1. Low ubiquity + low certainty → near 0 (leftmost = “Genesis / Custom”).  
2. High ubiquity + high certainty → near 1 (rightmost = “Commodity / Utility”).

Thus, the **horizontal coordinate** is:  
![](https://latex.codecogs.com/png.latex?x_i%20%3D%20E(c_i)).

---

## 4. Final Coordinates

Each component  
![](https://latex.codecogs.com/png.latex?c_i)  
sits at:

![](https://latex.codecogs.com/png.latex?M(c_i)%20%3D%20%28E(c_i)%2C%20V(c_i)%29).

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

By incorporating **ubiquity** and **certainty** into the **Evolution** function, we align with the principle that **“Evolution is driven by competitive forces, not just age.”** This helps teams build **Wardley Maps** that better capture real‐world dynamics of how components shift from **Genesis** to **Utility** as they become ubiquitous and well understood.
