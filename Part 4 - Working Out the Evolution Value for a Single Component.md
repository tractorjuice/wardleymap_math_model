# Working Out the "Evolution" Value for a Single Component

---

## 1. Model Recap

We use the following formula for **Evolution**:

$$\varepsilon(c_i) = \frac{\mathrm{ubiq}(c_i) + \mathrm{cert}(c_i)}{2}$$

Where:

- $\mathrm{ubiq}(c_i) \in [0,1]$:
  - **0** means extremely rare or unknown in the market.
  - **1** means widely available, used everywhere.

- $\mathrm{cert}(c_i) \in [0,1]$:
  - **0** means highly uncertain, no stable best practices, "frontier" territory.
  - **1** means fully standardized, best practices well understood.

Thus, **Evolution** is the average of two **key factors**: **ubiquity** and **certainty**.

---

## 2. Example: "AI-Enhanced Kettle"

Let's say you have an **AI-Enhanced Kettle** that uses humidity sensors and AI to adjust the boil temperature. You want to **place** it on your Wardley Map.

### 2.1. Ubiquity

- It's only in a few specialty stores, so it's **not** widespread.
- You might assign $\mathrm{ubiq}(\text{AI-Kettle}) = 0.2$.

### 2.2. Certainty

- There are **no** clear industry standards for AI-based kettle features; it's new.
- You might assign $\mathrm{cert}(\text{AI-Kettle}) = 0.3$.

### 2.3. Compute Evolution

Using

$$\varepsilon(\text{AI-Kettle}) = \frac{\mathrm{ubiq}(\text{AI-Kettle}) + \mathrm{cert}(\text{AI-Kettle})}{2}$$

we have:

$$\varepsilon(\text{AI-Kettle}) = \frac{0.2 + 0.3}{2} = 0.25$$

Hence, **Evolution** = **0.25**.

---

## 3. Interpretation

- A value of **0.25** indicates your kettle is still **far left** on the "Genesis → Commodity" continuum.
- **Low ubiquity** = not common in stores or homes yet.
- **Low/moderate certainty** = no well-established best practices or standards.

Therefore, it resides in a **custom / emerging** zone, not yet a stable or widely adopted product.

---

## 4. Changing Over Time

If **market adoption** increases (ubiquity ↗) and **standardization** (certainty ↗) solidifies, the AI-Kettle's **evolution** moves rightward:

- Suppose after 2 years, you measure:
  - $\mathrm{ubiq}(\text{AI-Kettle}) = 0.7$
  - $\mathrm{cert}(\text{AI-Kettle}) = 0.6$

Then:

$$\varepsilon(\text{AI-Kettle}) = \frac{0.7 + 0.6}{2} = 0.65$$

positioning it closer to a **product / commodity** status.

---

## 5. Summary

1. Determine $\mathrm{ubiq}(c_i) \in [0,1]$.
2. Determine $\mathrm{cert}(c_i) \in [0,1]$.
3. Calculate $\varepsilon(c_i) = \frac{\mathrm{ubiq}(c_i) + \mathrm{cert}(c_i)}{2}$.

The result $\varepsilon(c_i)$ defines how far along your component is on the **"Genesis → Commodity"** scale, providing a clear **horizontal** coordinate on your **Wardley Map**.
