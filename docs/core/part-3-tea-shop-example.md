# Explaining the "Tea Shop" Map Using Our Mathematical Model

This explanation highlights **why** the kettle evolves from a **custom** solution into a **commodity** product, along with the pros and cons of each approach. We'll reference our **Visibility vs. Evolution** framework and **dependency graph** model throughout.

---

## 1. Our Wardley Map Model (Quick Recap)

1. **Components**
   We define a set of components $V = \{ c_1, c_2, \dots, c_n \}$, each representing an element in delivering value (e.g., "Kettle," "Power," "Water").

2. **Dependencies**
   A directed edge $(c_i, c_j) \in E$ means "**$c_i$** depends on **$c_j$**." In the Tea Shop example:
   - "Kettle" depends on "Power."
   - "Cup of Tea" depends on "Hot Water," etc.

3. **Visibility (Vertical Axis)**
   We assign each component a **visibility** score, $\nu(c_i)$, based on **graph distance** from the user:
   - Let $\mathrm{dist}(c_i)$ be the shortest path distance from the user (or top-level need) to $c_i$.
   - Then normalize:

     $$\nu(c_i) = 1 - \frac{\mathrm{dist}(c_i)}{\max_{c_j}\mathrm{dist}(c_j)}$$

   - Components **closer** to the user appear **higher** on the map.

4. **Evolution (Horizontal Axis)**
   We define each component's **evolution** via $\varepsilon(c_i)$, measuring how **ubiquitous** and **well-understood** it is (not just "age"):
   - $\mathrm{ubiq}(c_i)$ = how widespread the component is in the market.
   - $\mathrm{cert}(c_i)$ = how standardized or certain it is (well-known best practices).
   - We combine them:

     $$\varepsilon(c_i) = \frac{\mathrm{ubiq}(c_i) + \mathrm{cert}(c_i)}{2}$$

Putting it all together, each component $c_i$ maps to $(\varepsilon(c_i), \nu(c_i))$.

---

## 2. Overview of the Tea Shop Map

In the **Tea Shop** scenario, the top-level users are:

- **Business**
- **Public**

At the bottom-right (highly evolved, less visible to the customer) are **Power** and **Water**, both considered **commodities**.

Between these layers, we see elements like **Kettle**, **Cup**, **Tea**, and **Hot Water** arranged based on their distance from the user (vertical) and how standardized they are (horizontal).

---

## 3. The Kettle's Position

1. **Visibility (Vertical)**
   - The kettle is not the final product ("Cup of Tea")—the user doesn't "buy a kettle" from the tea shop.
   - It's still somewhat visible (the user *knows* a kettle is used), so it's below "Cup of Tea" but above pure back-end commodities like "Power."

2. **Evolution (Horizontal)**
   - Kettles are generally **mass-produced** and standardized, but there is still room for brand/design differences.
   - Thus, it's placed in **"Product"** territory—beyond "custom-built" but not as purely commodity as "Water" or "Power."

---

## 4. Evolution of the Kettle: From Custom to Commodity

### Why Is a Commodity Kettle Generally Better?

- **Lower Costs**
  Mass production reduces unit prices. Customers benefit from cheaper, more reliable kettles; shops spend less to source or replace them.

- **Standardization**
  Kettles leverage **standardized electricity** (commodity "Power"). No need for special wiring; just plug and boil.

- **Predictability**
  Commodity kettles follow consistent safety and performance standards. Less risk for the tea shop—repairs and replacements are straightforward.

By applying our **Evolution** function,

$$\varepsilon(\text{Kettle}) = \frac{\mathrm{ubiq}(\text{Kettle})+\mathrm{cert}(\text{Kettle})}{2}$$

we see that high **ubiquity** (common product on the market) and moderate/high **certainty** (safety standards, known design) push it well into the "product" zone.

### Downsides of Commodity vs. Upsides of Custom

- **Less Differentiation**
  If the kettle is fully commoditized, profit margins can become razor-thin, and every kettle is mostly the same.

- **Innovation**
  A **custom** kettle could explore new tech (e.g., IoT kettle or unique brewing temps). This might stand out in a **niche or premium** market.

In standard, high-volume retail scenarios, though, the benefits of a commodity kettle (low cost, interoperability, reliability) outweigh the potential gains from custom.

---

## 5. Dependencies & Flow

The map's **edges** reflect the directed graph:

1. **Cup of Tea** → needs **Hot Water**, **Cup**, **Tea**.
2. **Hot Water** → depends on **Kettle** + **Water**.
3. **Kettle** → depends on **Power**.

In terms of our **distance** measure:
- "Power" is multiple steps away from the user (lowest in visibility).
- "Business" or "Public" is distance=0 from themselves (highest in visibility).

Thus,

$$y_i = \nu(c_i) = 1-\frac{\mathrm{dist}(c_i)}{\max \mathrm{dist}(c_j)}$$

puts "Power" near the bottom and "Cup of Tea" near the top.

---

## 6. Conclusion & Takeaway

1. **Vertical Axis**: "Business" and "Public" at the top have zero distance; "Power" and "Water" at the bottom have longer paths.
2. **Horizontal Axis**: Commoditized elements (Power, Water) far right. Kettle is a **product**—standard but not purely commodity.
3. **Custom vs. Commodity**:
   - Commodity kettles lower cost, minimize risk, and simplify the tea-making chain.
   - A custom kettle can offer unique features but also increases cost, risk, and may require specialized infrastructure.

Overall, **the Wardley Map** clarifies how each component—**including the Kettle**—delivers **value** to the end users while illustrating **where** standardization (commodity) is beneficial and **where** custom solutions might differentiate or innovate.
