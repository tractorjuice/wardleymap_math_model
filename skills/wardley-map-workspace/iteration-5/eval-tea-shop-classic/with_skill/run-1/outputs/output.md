# Wardley Map — Small Tea Shop

**Scenario:** A small tea shop that serves cups of tea to customers, needs to handle payment, and sources tea leaves from suppliers.

---

## Map (OWM)

```owm
title Small Tea Shop
style wardley

// Anchor
anchor Customer [0.98, 0.55]

// User-facing
component Cup of Tea [0.90, 0.68]
component Payment [0.85, 0.82]
component In-shop Experience [0.82, 0.40]

// Mid-chain craft
component Brewing Process [0.72, 0.62]
component Barista [0.68, 0.38]
component Menu / Recipe [0.60, 0.50]

// Ingredients and consumables
component Tea Leaves [0.52, 0.75]
component Milk / Sugar / Accompaniments [0.48, 0.88]
component Cups / Crockery [0.45, 0.88]
component Hot Water [0.40, 0.92]

// Equipment and premises
component Kettle / Urn [0.32, 0.90]
component Shop Premises [0.28, 0.55]

// Payment layer
component Till / POS System [0.58, 0.78]
component Card Payment Processing [0.45, 0.92]

// Supply chain
component Inventory Management [0.25, 0.70]
component Tea Sourcing Process [0.30, 0.55]
component Supplier Relationship [0.22, 0.45]

// Utilities
component Electricity [0.12, 0.95]
component Water Supply [0.10, 0.95]

// Dependencies
Customer->Cup of Tea
Customer->Payment
Customer->In-shop Experience
Cup of Tea->Brewing Process
Cup of Tea->Menu / Recipe
Cup of Tea->Tea Leaves
Cup of Tea->Milk / Sugar / Accompaniments
Cup of Tea->Cups / Crockery
In-shop Experience->Barista
In-shop Experience->Shop Premises
Brewing Process->Tea Leaves
Brewing Process->Hot Water
Brewing Process->Barista
Menu / Recipe->Tea Leaves
Hot Water->Kettle / Urn
Hot Water->Water Supply
Kettle / Urn->Electricity
Payment->Till / POS System
Payment->Card Payment Processing
Till / POS System->Electricity
Card Payment Processing->Electricity
Tea Leaves->Tea Sourcing Process
Tea Leaves->Inventory Management
Tea Sourcing Process->Supplier Relationship
Shop Premises->Electricity
Shop Premises->Water Supply

// Evolution intentions (scenarios, not forecasts)
evolve Supplier Relationship 0.58
evolve Till / POS System 0.90

note Differentiation zone [0.75, 0.30]
note Utility commodity [0.18, 0.93]
```

---

## Strategic analysis

### a. Top 3 by differentiation pressure D = ν·(1 − ε)

1. **In-shop Experience** — D = 0.82 × 0.60 = **0.49**. The atmosphere, ritual, hospitality, cosiness. A small tea shop competes on this against supermarkets, chains, and home-brewed tea. It is the single most valuable place to invest.
2. **Barista** — D = 0.68 × 0.62 = **0.42**. Human craft: recommending a blend, steeping correctly, remembering regulars. Tightly coupled to In-shop Experience and non-substitutable by commodity suppliers.
3. **Menu / Recipe** — D = 0.60 × 0.50 = **0.30**. A curated tea list with seasonal blends and provenance stories is a low-cost differentiator. Moves to Stage III over time as copycats imitate, so keep innovating.

### b. Top 3 by commodity leverage K = (1 − ν)·ε

1. **Water Supply** — K = 0.90 × 0.95 = **0.86**. Utility. Never build; pay the bill.
2. **Electricity** — K = 0.88 × 0.95 = **0.84**. Utility. Never build.
3. **Card Payment Processing** — K = 0.55 × 0.92 = **0.51**. Utility-model Stage IV (+utility). Rent from SumUp/Stripe/Square; do not design a payment flow from scratch.

Honourable mentions with high K: Hot Water (0.55), Kettle / Urn (0.61), Milk / Sugar (0.46), Cups / Crockery (0.48) — all commodities that should be bought, not engineered.

### c. Top 3 dependency risks R = ν(a)·(1 − ε(b))

1. **(Brewing Process → Barista)** — R = 0.72 × 0.62 = **0.45**. A small shop with one or two baristas has a true single-point-of-failure in skill and availability. Training pipeline, retention, and written SOPs are mitigations.
2. **(In-shop Experience → Barista)** — R = 0.82 × 0.62 = **0.51**. The core differentiator rests on a human. Illness, turnover, or a bad shift directly damages the thing the customer is paying extra for.
3. **(Cup of Tea → Tea Leaves)** — R = 0.90 × 0.25 = **0.22**, and by extension **(Tea Leaves → Tea Sourcing Process)** R = 0.52 × 0.45 = **0.23**. Specialty supply is concentrated; a single supplier with one crop failure is a strategic risk.

### d. Suggested gameplays (from Wardley's 61-play catalogue)

- **#1 Focus on user needs** — anchor everything on the Customer; reinforce that the sit-in cup-and-atmosphere is the real user need, not just liquid.
- **#26 Differentiation** — lean into premium loose-leaf, tea ceremony, cultural events. Target the high-D components (In-shop Experience, Barista, Menu).
- **#36 Directed investment** — put discretionary spend (training, interior, menu R&D) into the top-three D components, not into re-engineering commodities.
- **#41 Alliances / Co-operation** — second-source specialty tea suppliers; align with a local roaster or bakery for cross-traffic. Reduces the Tea Leaves / Supplier Relationship risk.
- **#29 Harvesting** — let the market do the work for Kettle / Urn, Cups / Crockery, POS, and Card Payment Processing. Buy the best commodity; do not design.
- **#15 Open Approaches** is **not** recommended here — a small tea shop has no reason to open-source menus or suppliers; its moat is local, physical, and relational.

### e. Doctrine notes (Wardley's 40 principles)

- Checked: **#1 Focus on user needs** — map is anchored on Customer; dependencies flow from the user need.
- Checked: **#6 Use appropriate methods** — the map mixes Stage II (craft, bespoke) and Stage IV (utility) components, and the gameplays above follow that grain rather than one-size-fits-all.
- Watch: **#10 Know your users** — a single Customer anchor is a simplification. In practice, sit-in customers, takeaway customers, and (sometimes) wholesale/online buyers are distinct user types. A fuller map would add anchors.
- Watch: **#13 Manage inertia** — Barista human-capital inertia (inertia form #4 *skill acquisition cost*) and the owner's emotional attachment to particular suppliers (inertia form #5 *past success*) are real and should be surfaced, not denied.
- Watch: **#35 Think small (as in teams)** — fine for a small tea shop today; only relevant if the shop scales into multiple sites.

### f. Climatic context (27 climatic patterns)

- **#3 Everything evolves** — the Till / POS System has already moved from bespoke cash-register + ledger to Stage IV cloud POS (Square, Toast, Lightspeed, SumUp); Card Payment Processing has moved to a utility-model Commodity (+utility). These evolutions already happened to the tea shop, whether or not the owner noticed.
- **#15–17 Inertia patterns** — incumbents (and small-shop owners) resist moves to utility services, especially around trusted supplier relationships. Expect to feel this when asked to second-source tea.
- **#18 You cannot measure evolution over time or adoption** — the canonical placement of components here is from the cheat sheet, not from calendar time.
- **#27 Product to utility (punctuated equilibrium)** — the POS and Payments shifts are textbook examples; the kettle and crockery commoditisation happened long ago; the *next* wave will probably touch Tea Sourcing (B2B marketplace platforms for speciality tea).

### g. Deep-placement notes

I ran targeted web searches on four components where the cheat-sheet placement either sat near a boundary or felt worth verifying for 2026.

- **Till / POS System** — initial cheat-sheet read put this around 0.70 (late Product (+rental)). A 2026 vendor-landscape search showed Square, Toast, Clover, Lightspeed, Shopify POS and SumUp all offering free or near-free cloud POS software with stabilising feature sets, and cloud-native installations now dominating new deployments. Publication type has moved from how-to-build to operations/use guides. Shifted to **0.78** (early Commodity (+utility)); the `evolve` target of 0.90 reflects the likely next-wave shift where POS becomes a free accessory to the payment processor.
- **Card Payment Processing** — cheat-sheet put this at 0.90. Search confirmed a mature UK landscape (SumUp flat 1.69%, Stripe 1.5%+20p, multiple hardware options from £25) with many interchangeable providers and flat-rate utility-like pricing. Confirms **0.92** — solidly Commodity (+utility).
- **Tea Leaves / Tea Sourcing Process** — cheat-sheet instinct put Tea Leaves at 0.85 (Commodity (+utility)) and Sourcing at 0.45 (Custom Built). A specialty-supplier search showed a crowded UK market of independent wholesalers (Rare Tea Company, Shibui, The Tea Makers of London, Wee Tea Company) sourcing single-origin leaves — for a *small tea shop that differentiates on quality*, leaves belong in Stage III Product (+rental), not Stage IV Commodity (+utility), because variety, provenance, and freshness still drive competition. Shifted Tea Leaves to **0.75** (late Product (+rental)) and kept Sourcing at **0.55** (mid Product (+rental)) to reflect relationship-based rather than spot-market buying.
- **In-shop Experience / Barista** — cheat-sheet placed these in Stage II. A 2026 hospitality-trends search reinforced that human hospitality is treated as a competitive advantage in an automated world, and that small independents win on staff relationships rather than menu or aesthetic. Confirms **0.40** and **0.38** — early-to-mid Custom Built.

Components not researched (obvious commodities or direct utilities): Electricity, Water Supply, Hot Water, Kettle / Urn, Cups / Crockery, Milk / Sugar. The cheat-sheet placement is not in doubt for any of these.

### h. Caveat

Evolution positions and the `evolve` arrows above are scenarios, not forecasts. Wardley's climatic pattern #18 stands: *"you cannot measure evolution over time or adoption."* The cheat-sheet places each component *now*, based on the characteristics of its market today; the trajectory is a plausible story of how the market could shift, not a prediction.

---

## Verification (Step 5.5)

**1. Visibility constraint re-check** — every `A → B` edge below satisfies `ν(A) ≥ ν(B)`:

| Edge | ν(A) | ν(B) | OK |
|---|---|---|---|
| Customer → Cup of Tea | 0.98 | 0.90 | ✓ |
| Customer → Payment | 0.98 | 0.85 | ✓ |
| Customer → In-shop Experience | 0.98 | 0.82 | ✓ |
| Cup of Tea → Brewing Process | 0.90 | 0.72 | ✓ |
| Cup of Tea → Menu / Recipe | 0.90 | 0.60 | ✓ |
| Cup of Tea → Tea Leaves | 0.90 | 0.52 | ✓ |
| Cup of Tea → Milk / Sugar / Accompaniments | 0.90 | 0.48 | ✓ |
| Cup of Tea → Cups / Crockery | 0.90 | 0.45 | ✓ |
| In-shop Experience → Barista | 0.82 | 0.68 | ✓ |
| In-shop Experience → Shop Premises | 0.82 | 0.28 | ✓ |
| Brewing Process → Tea Leaves | 0.72 | 0.52 | ✓ |
| Brewing Process → Hot Water | 0.72 | 0.40 | ✓ |
| Brewing Process → Barista | 0.72 | 0.68 | ✓ |
| Menu / Recipe → Tea Leaves | 0.60 | 0.52 | ✓ |
| Hot Water → Kettle / Urn | 0.40 | 0.32 | ✓ |
| Hot Water → Water Supply | 0.40 | 0.10 | ✓ |
| Kettle / Urn → Electricity | 0.32 | 0.12 | ✓ |
| Payment → Till / POS System | 0.85 | 0.58 | ✓ |
| Payment → Card Payment Processing | 0.85 | 0.45 | ✓ |
| Till / POS System → Electricity | 0.58 | 0.12 | ✓ |
| Card Payment Processing → Electricity | 0.45 | 0.12 | ✓ |
| Tea Leaves → Tea Sourcing Process | 0.52 | 0.30 | ✓ |
| Tea Leaves → Inventory Management | 0.52 | 0.25 | ✓ |
| Tea Sourcing Process → Supplier Relationship | 0.30 | 0.22 | ✓ |
| Shop Premises → Electricity | 0.28 | 0.12 | ✓ |
| Shop Premises → Water Supply | 0.28 | 0.10 | ✓ |

All 26 edges satisfy ν(A) ≥ ν(B).

**2. Canonical stage naming re-check** — every stage reference in the analysis prose above uses the parenthesised forms "Product (+rental)" and "Commodity (+utility)", never the bare "Product" or "Commodity" as stage names. ("Product" is used once or twice below in the sense of a physical product, not the stage — those are fine.)
