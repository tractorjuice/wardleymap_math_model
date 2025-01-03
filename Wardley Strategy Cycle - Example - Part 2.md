# Example Scenario Using the Two “Whys” in the Wardley Strategy Cycle

Below is a **example** illustrating how **Why of Purpose** and **Why of Movement** might evolve in a discrete‐time, Wardley‐style model. This example is intentionally simplified to show how each step (OODA) might look in practice.

---

## Initial Setup (Time \( t = 0 \))

- **External State**  
  ![](https://latex.codecogs.com/png.latex?X%280%29) =  
  - _Market Demand_: moderate but growing for small‐business accounting software  
  - _Competitor Behavior_: one major competitor has 60% market share  

- **Internal State**  
  ![](https://latex.codecogs.com/png.latex?Y%280%29) =  
  - _Runway_: 12 months of funding  
  - _Team_: 1 founder + 2 developers + 1 marketing person  
  - _Doctrine_: “Focus on user needs,” “Iterate quickly”  
  - _Leadership_: Founder is both CEO and product visionary  

- **Why of Purpose**  
  ![](https://latex.codecogs.com/png.latex?P%280%29) =  
  - _Mission Statement_: **“Help small businesses easily track finances and reduce bookkeeping overhead.”**  
  - This “why of purpose” is fairly stable—“We exist to simplify finance for small businesses.”

- **Why of Movement**  
  ![](https://latex.codecogs.com/png.latex?M%280%29) =  
  - _Current Rationale_: **“Focus on building a minimum viable product (MVP) for basic accounting features to onboard our first paying customers.”**  
  - This is more tactical—it explains the near‐term reason behind our chosen direction (building an MVP).

---

## Cycle at \( t=0 \)

### 1. Observe
![](https://latex.codecogs.com/png.latex?O%280%29%20%3D%20%5Cmathrm%7BObs%7D%28X%280%29%2C%20Y%280%29%29)

- We observe that competitor is dominant; the overall market is still growing.  
- Internally, we’re a small team but have enough runway to build an MVP.

### 2. Orient
![](https://latex.codecogs.com/png.latex?R%280%29%20%3D%20%5Cmathrm%7BOri%7D%28O%280%29%2C%20P%280%29%2C%20M%280%29%29)

- Incorporate the data:
  - External: Growth in demand, big competitor.  
  - Internal: We have modest resources, small but agile team.  
  - **Why of Purpose**: _Simplify finance for small business_.  
  - **Why of Movement**: _Build MVP for basic accounting_.  

- Our oriented “mental model” ( \( R(0) \) ) concludes we should keep focusing on a simple MVP that captures immediate user needs quickly.

### 3. Decide
![](https://latex.codecogs.com/png.latex?D%280%29%20%3D%20%5Cmathrm%7BDec%7D%28R%280%29%29)

- **Decision**: _Allocate 80% of dev resources to building an MVP for invoicing & expense tracking; 20% on marketing to attract early adopters._  
- This aligns with our near‐term rationale (MVP first) and our overall mission.

### 4. Act
![](https://latex.codecogs.com/png.latex?A%280%29%20%3D%20%5Cmathrm%7BAct%7D%28D%280%29%29)

- **Action**:
  1. Start coding the MVP features.  
  2. Launch a small ad campaign targeting local small businesses.  
  3. Prepare alpha testing with a handful of friendly customers.

### 5. Update States
![](https://latex.codecogs.com/png.latex?%5BX%281%29%2C%20Y%281%29%5D%20%3D%20T%28X%280%29%2C%20Y%280%29%2C%20A%280%29%29)

- **External State** \( X(1) \):
  - Market remains relatively the same, but a few early customers are now aware of our product.  
  - Competitor is launching advanced analytics (potentially raising the bar for “advanced” features).

- **Internal State** \( Y(1) \):
  - Runway: Now 11 months (some funds used for the ad campaign).  
  - Team morale: Generally positive after seeing early user interest.  
  - MVP progress: Invoicing module ~30% complete.

### 6. Update “Two Whys”
![](https://latex.codecogs.com/png.latex?P%281%29%20%3D%20%5Cmathrm%7BUpdatePurpose%7D%28P%280%29%2C%20X%281%29%2C%20Y%281%29%29)

- **Why of Purpose** \( P(1) \): Remains mostly unchanged. We still want “to simplify finance for small businesses.”  
  - Possibly we refine the wording: “Focus on micro‐businesses with fewer than 10 employees.”

![](https://latex.codecogs.com/png.latex?M%281%29%20%3D%20%5Cmathrm%7BUpdateMovement%7D%28M%280%29%2C%20D%280%29%2C%20A%280%29%29)

- **Why of Movement** \( M(1) \): Shifts slightly:  
  - _“We’re continuing the MVP approach but must consider adding analytics or reporting features to remain competitive.”_

---

## Cycle at \( t=1 \)

With the updated states, we run **Observe → Orient → Decide → Act** again, now at time \( t=1 \).

1. **Observe**  
   ![](https://latex.codecogs.com/png.latex?O%281%29%20%3D%20%5Cmathrm%7BObs%7D%28X%281%29%2C%20Y%281%29%29)  
   - External: Competitor’s advanced analytics might become a selling point for them.  
   - Internal: MVP development is partial, runway is still okay, but we need traction soon.

2. **Orient**  
   ![](https://latex.codecogs.com/png.latex?R%281%29%20%3D%20%5Cmathrm%7BOri%7D%28O%281%29%2C%20P%281%29%2C%20M%281%29%29)  
   - Incorporate updated “why of purpose”: still about small‐business finance.  
   - Incorporate updated “why of movement”: we’re building an MVP but might need analytics next.  

3. **Decide**  
   ![](https://latex.codecogs.com/png.latex?D%281%29%20%3D%20%5Cmathrm%7BDec%7D%28R%281%29%29)  
   - **Decision**: We decide to split dev time 70/30 between finishing the MVP core features and beginning a basic reporting module.  
   - Marketing is directed at alpha testers who value quick invoicing (not advanced analytics yet).

4. **Act**  
   ![](https://latex.codecogs.com/png.latex?A%281%29%20%3D%20%5Cmathrm%7BAct%7D%28D%281%29%29)  
   - **Action**:  
     1. Continue building the MVP invoicing module.  
     2. Start user research on what “basic analytics” should look like.  
     3. Publish a landing page highlighting “simple invoicing + basic insights” coming soon.

5. **Update States**  
   ![](https://latex.codecogs.com/png.latex?%5BX%282%29%2C%20Y%282%29%5D%20%3D%20T%28X%281%29%2C%20Y%281%29%2C%20A%281%29%29)  
   - **External** \( X(2) \): A few more sign‐ups from local groups, competitor is marketing their analytics heavily.  
   - **Internal** \( Y(2) \): MVP ~50% complete, runway 10 months, user interest in analytics is moderate but growing.

6. **Update “Two Whys”**  
   - **Why of Purpose** \( P(2) \): Still consistent—“Empower micro‐businesses.” (No radical pivot yet.)  
   - **Why of Movement** \( M(2) \):  
     _“We must finish core accounting to deliver value quickly, yet we’re beginning analytics to stay relevant.”_

---

## Observations

1. **Why of Purpose** (![](https://latex.codecogs.com/png.latex?P%28t%29)) remains mostly stable, adjusting only slightly to clarify or refine scope (micro‐businesses).  
2. **Why of Movement** (![](https://latex.codecogs.com/png.latex?M%28t%29)) evolves more rapidly, reflecting short‐term tactical shifts—finishing the MVP, deciding whether to add analytics, etc.  
3. Each cycle of **Observe → Orient → Decide → Act** leads to **state updates** (both external and internal) plus incremental **refinement** of the two whys.  
4. By capturing this in a formal model, you could attempt to optimize decisions for maximum “strategic utility” (for instance, balancing speed to market vs. advanced features vs. runway constraints).

In this scenario, we see **how** and **why** the organization’s near‐term tactics (why of movement) change over time, while the overarching mission (why of purpose) remains the guiding star—both embedded in a Wardley‐style cycle of **continuous sensing and adaptation**.
