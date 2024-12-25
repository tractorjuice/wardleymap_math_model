```markdown
# Explaining the “Tea Shop” Map Using Our Mathematical Model

This explanation highlights **why** the kettle evolves from a **custom** solution into a **commodity** product, along with the pros and cons of each approach. We’ll reference our **Visibility vs. Evolution** framework and **dependency graph** model throughout.

---

## 1. Our Wardley Map Model (Quick Recap)

1. **Components**  
   We define a set of components  
   ![](https://latex.codecogs.com/png.latex?%5Cmathcal%7BC%7D%20%3D%20%5C%7B%20c_1%2C%20c_2%2C%20%5Cdots%2C%20c_n%20%5C%7D),  
   each representing an element in delivering value (e.g., “Kettle,” “Power,” “Water”).

2. **Dependencies**  
   A directed edge  
   ![](https://latex.codecogs.com/png.latex?(c_i%2C%20c_j)%20%5Cin%20%5Cmathcal%7BE%7D)  
   means “\(c_i\) depends on \(c_j\).” In the Tea Shop example:
   - “Kettle” depends on “Power.”  
   - “Cup of Tea” depends on “Hot Water,” etc.

3. **Visibility (Vertical Axis)**  
   We assign each component a **visibility** score,  
   ![](https://latex.codecogs.com/png.latex?V(c_i)),  
   based on **graph distance** from the user:
   - Let  
     ![](https://latex.codecogs.com/png.latex?%5Cmathrm%7Bdist%7D(c_i))  
     be the shortest path distance from the user (or top-level need) to  
     ![](https://latex.codecogs.com/png.latex?c_i).  
   - Then normalize:  
     ![](https://latex.codecogs.com/png.latex?V(c_i)%20%3D%201%20-%20%5Cfrac%7B%5Cmathrm%7Bdist%7D(c_i)%7D%7B%5Cmax_%7Bc_j%7D%5Cmathrm%7Bdist%7D(c_j)%7D).  
   - Components **closer** to the user appear **higher** on the map.

4. **Evolution (Horizontal Axis)**  
   We define each component’s **evolution** via  
   ![](https://latex.codecogs.com/png.latex?E(c_i)),  
   measuring how **ubiquitous** and **well-understood** it is (not just “age”):
   - ![](https://latex.codecogs.com/png.latex?%5Cmathrm%7Bubiq%7D(c_i))  
     = how widespread the component is in the market.  
   - ![](https://latex.codecogs.com/png.latex?%5Cmathrm%7Bcert%7D(c_i))  
     = how standardized or certain it is (well-known best practices).  
   - We combine them:  
     ![](https://latex.codecogs.com/png.latex?E(c_i)%20%3D%20%5Cfrac%7B%5Cmathrm%7Bubiq%7D(c_i)%20%2B%20%5Cmathrm%7Bcert%7D(c_i)%7D%7B2%7D).

Putting it all together, each component  
![](https://latex.codecogs.com/png.latex?c_i)  
maps to  
![](https://latex.codecogs.com/png.latex?(E(c_i)%2C%20V(c_i))).

---

## 2. Overview of the Tea Shop Map

In the **Tea Shop** scenario, the top-level users are:

- **Business**  
- **Public**

At the bottom-right (highly evolved, less visible to the customer) are **Power** and **Water**, both considered **commodities**.

Between these layers, we see elements like **Kettle**, **Cup**, **Tea**, and **Hot Water** arranged based on their distance from the user (vertical) and how standardized they are (horizontal).

---

## 3. The Kettle’s Position

1. **Visibility (Vertical)**  
   - The kettle is not the final product (“Cup of Tea”)—the user doesn’t “buy a kettle” from the tea shop.  
   - It’s still somewhat visible (the user *knows* a kettle is used), so it’s below “Cup of Tea” but above pure back-end commodities like “Power.”

2. **Evolution (Horizontal)**  
   - Kettles are generally **mass-produced** and standardized, but there is still room for brand/design differences.  
   - Thus, it’s placed in **“Product”** territory—beyond “custom-built” but not as purely commodity as “Water” or “Power.”

---

## 4. Evolution of the Kettle: From Custom to Commodity

### Why Is a Commodity Kettle Generally Better?

- **Lower Costs**  
  Mass production reduces unit prices. Customers benefit from cheaper, more reliable kettles; shops spend less to source or replace them.

- **Standardization**  
  Kettles leverage **standardized electricity** (commodity “Power”). No need for special wiring; just plug and boil.

- **Predictability**  
  Commodity kettles follow consistent safety and performance standards. Less risk for the tea shop—repairs and replacements are straightforward.

By applying our **Evolution** function,
![](https://latex.codecogs.com/png.latex?E%28%5Ctext%7BKettle%7D%29%20%3D%20%5Cfrac%7Bubiq%28%5Ctext%7BKettle%7D%29%2Bcert%28%5Ctext%7BKettle%7D%29%7D%7B2%7D),
we see that high **ubiquity** (common product on the market) and moderate/high **certainty** (safety standards, known design) push it well into the “product” zone.

### Downsides of Commodity vs. Upsides of Custom

- **Less Differentiation**  
  If the kettle is fully commoditized, profit margins can become razor-thin, and every kettle is mostly the same.

- **Innovation**  
  A **custom** kettle could explore new tech (e.g., IoT kettle or unique brewing temps). This might stand out in a **niche or premium** market.

In standard, high-volume retail scenarios, though, the benefits of a commodity kettle (low cost, interoperability, reliability) outweigh the potential gains from custom.

---

## 5. Dependencies & Flow

The map’s **edges** reflect the directed graph:

1. **Cup of Tea** → needs **Hot Water**, **Cup**, **Tea**.  
2. **Hot Water** → depends on **Kettle** + **Water**.  
3. **Kettle** → depends on **Power**.

In terms of our **distance** measure:
- “Power” is multiple steps away from the user (lowest in visibility).  
- “Business” or “Public” is distance=0 from themselves (highest in visibility).

Thus,  
![](https://latex.codecogs.com/png.latex?y_i%20%3D%20V(c_i)%20%3D%201-%5Cfrac%7Bdist(c_i)%7D%7B%5Cmax%20dist(c_j)%7D)
puts “Power” near the bottom and “Cup of Tea” near the top.

---

## 6. Conclusion & Takeaway

1. **Vertical Axis**: “Business” and “Public” at the top have zero distance; “Power” and “Water” at the bottom have longer paths.  
2. **Horizontal Axis**: Commoditized elements (Power, Water) far right. Kettle is a **product**—standard but not purely commodity.  
3. **Custom vs. Commodity**:  
   - Commodity kettles lower cost, minimize risk, and simplify the tea-making chain.  
   - A custom kettle can offer unique features but also increases cost, risk, and may require specialized infrastructure.

Overall, **the Wardley Map** clarifies how each component—**including the Kettle**—delivers **value** to the end users while illustrating **where** standardization (commodity) is beneficial and **where** custom solutions might differentiate or innovate.
```
