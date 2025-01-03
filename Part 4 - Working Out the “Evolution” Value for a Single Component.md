# Working Out the “Evolution” Value for a Single Component

---

## 1. Model Recap

We use the following formula for **Evolution**:

![](https://latex.codecogs.com/png.latex?E%28c_i%29%20%3D%20%5Cfrac%7B%5Cmathrm%7Bubiq%7D%28c_i%29%20+%20%5Cmathrm%7Bcert%7D%28c_i%29%7D%7B2%7D)

Where:

- ![](https://latex.codecogs.com/png.latex?%5Cmathrm%7Bubiq%7D%28c_i%29) ![](https://latex.codecogs.com/png.latex?%5Cin%20%5B0%2C1%5D):  
  - **0** means extremely rare or unknown in the market.  
  - **1** means widely available, used everywhere.

- ![](https://latex.codecogs.com/png.latex?%5Cmathrm%7Bcert%7D%28c_i%29) ![](https://latex.codecogs.com/png.latex?%5Cin%20%5B0%2C1%5D):  
  - **0** means highly uncertain, no stable best practices, “frontier” territory.  
  - **1** means fully standardized, best practices well understood.

Thus, **Evolution** is the average of two **key factors**: **ubiquity** and **certainty**.

---

## 2. Example: “AI-Enhanced Kettle”

Let’s say you have an **AI-Enhanced Kettle** that uses humidity sensors and AI to adjust the boil temperature. You want to **place** it on your Wardley Map.

### 2.1. Ubiquity

- It’s only in a few specialty stores, so it’s **not** widespread.  
- You might assign ![](https://latex.codecogs.com/png.latex?%5Cmathrm%7Bubiq%7D%28AI%5Ctext{-}Kettle%29) = 0.2.

### 2.2. Certainty

- There are **no** clear industry standards for AI-based kettle features; it’s new.  
- You might assign ![](https://latex.codecogs.com/png.latex?%5Cmathrm%7Bcert%7D%28AI%5Ctext{-}Kettle%29) = 0.3.

### 2.3. Compute Evolution

Using

![](https://latex.codecogs.com/png.latex?E%28AI%5Ctext{-}Kettle%29%20%3D%20%5Cfrac%7B%5Cmathrm%7Bubiq%7D%28AI%5Ctext{-}Kettle%29%20+%20%5Cmathrm%7Bcert%7D%28AI%5Ctext{-}Kettle%29%7D%7B2%7D),

we have:

![](https://latex.codecogs.com/png.latex?E%28AI%5Ctext{-}Kettle%29%20%3D%20%5Cfrac%7B0.2%20+%200.3%7D%7B2%7D%20%3D%200.25).

Hence, **Evolution** = **0.25**.

---

## 3. Interpretation

- A value of **0.25** indicates your kettle is still **far left** on the “Genesis → Commodity” continuum.  
- **Low ubiquity** = not common in stores or homes yet.  
- **Low/moderate certainty** = no well-established best practices or standards.

Therefore, it resides in a **custom / emerging** zone, not yet a stable or widely adopted product.

---

## 4. Changing Over Time

If **market adoption** increases (ubiquity ↗) and **standardization** (certainty ↗) solidifies, the AI-Kettle’s **evolution** moves rightward:

- Suppose after 2 years, you measure:
  - ![](https://latex.codecogs.com/png.latex?%5Cmathrm%7Bubiq%7D%28AI%5Ctext{-}Kettle%29%20%3D%200.7)  
  - ![](https://latex.codecogs.com/png.latex?%5Cmathrm%7Bcert%7D%28AI%5Ctext{-}Kettle%29%20%3D%200.6)

Then:

![](https://latex.codecogs.com/png.latex?E%28AI%5Ctext{-}Kettle%29%20%3D%20%5Cfrac%7B0.7%20+%200.6%7D%7B2%7D%20%3D%200.65),

positioning it closer to a **product / commodity** status.

---

## 5. Summary

1. Determine ![](https://latex.codecogs.com/png.latex?%5Cmathrm%7Bubiq%7D%28c_i%29) ![](https://latex.codecogs.com/png.latex?%5Cin%20%5B0%2C1%5D).  
2. Determine ![](https://latex.codecogs.com/png.latex?%5Cmathrm%7Bcert%7D%28c_i%29) ![](https://latex.codecogs.com/png.latex?%5Cin%20%5B0%2C1%5D).  
3. Calculate ![](https://latex.codecogs.com/png.latex?E%28c_i%29%20%3D%20%5Cfrac%7B%5Cmathrm%7Bubiq%7D%28c_i%29%20+%20%5Cmathrm%7Bcert%7D%28c_i%29%7D%7B2%7D).

The result ![](https://latex.codecogs.com/png.latex?E%28c_i%29) defines how far along your component is on the **“Genesis → Commodity”** scale, providing a clear **horizontal** coordinate on your **Wardley Map**.
