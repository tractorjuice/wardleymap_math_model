# Wardley Map — Small Tea Shop

## OWM Map

```owm
title Small Tea Shop
style wardley

// Anchor(s)
anchor Customer [0.98, 0.55]

// Components — Activities
component Cup of Tea [0.88, 0.62]
component Payment [0.80, 0.88]
component Seating / Ambience [0.78, 0.70]
component Brewing [0.62, 0.70]
component Hot Water [0.55, 0.90]
component Tea Leaves [0.50, 0.78]
component Cups & Crockery [0.48, 0.90]
component Milk & Sugar [0.46, 0.92]
component Till / POS System [0.42, 0.80]
component Card Payment Gateway [0.38, 0.85]
component Supplier Relationship [0.32, 0.55]
component Barista Labour [0.30, 0.72]
component Shop Premises / Lease [0.22, 0.80]
component Electricity [0.18, 0.95]
component Water Utility [0.16, 0.95]
component Tea Blending Knowledge [0.14, 0.45]

// Dependencies (a -> b  means a depends on b)
Customer->Cup of Tea
Customer->Payment
Customer->Seating / Ambience

Cup of Tea->Brewing
Cup of Tea->Cups & Crockery
Cup of Tea->Milk & Sugar

Brewing->Hot Water
Brewing->Tea Leaves
Brewing->Barista Labour
Brewing->Tea Blending Knowledge

Hot Water->Electricity
Hot Water->Water Utility

Payment->Till / POS System
Payment->Card Payment Gateway

Seating / Ambience->Shop Premises / Lease
Seating / Ambience->Barista Labour

Tea Leaves->Supplier Relationship
Cups & Crockery->Supplier Relationship
Milk & Sugar->Supplier Relationship

Till / POS System->Electricity
Card Payment Gateway->Electricity

// Notes
note Core differentiator lives here [0.60, 0.45]
note Utility layer — buy, don't build [0.18, 0.92]
```

---

## Strategic Analysis

### a. Top 3 by Differentiation Pressure D = ν · (1 − ε)

1. **Seating / Ambience** — D ≈ 0.78 · 0.30 = **0.234**. Highly visible to the customer and still craft-shaped (layout, music, service tone). A real source of repeat-visit advantage.
2. **Cup of Tea** — D ≈ 0.88 · 0.38 = **0.334**. The headline offer. Although "a cup of tea" is a common concept, *this* tea shop's cup (blend, brew quality, presentation) is where users perceive difference.
3. **Brewing** — D ≈ 0.62 · 0.30 = **0.186**. Visible through the cup and still dependent on craft (water temperature, steep time, leaf-to-water ratio). Where mastery pays.

(Tea Blending Knowledge also scores well on the *craft* side — D ≈ 0.14 · 0.55 = 0.077 — low because it sits deep, but it is the underlying knowledge that powers the top three.)

### b. Top 3 by Commodity Leverage K = (1 − ν) · ε

1. **Electricity** — K ≈ 0.82 · 0.95 = **0.779**. Pure utility; buy from the cheapest reliable supplier.
2. **Water Utility** — K ≈ 0.84 · 0.95 = **0.798**. Same logic; already a regulated utility.
3. **Card Payment Gateway** — K ≈ 0.62 · 0.85 = **0.527**. A commoditised service (Stripe, SumUp, Square). No reason to build or heavily customise.

### c. Top 3 Dependency Risks R(a, b) = ν(a) · (1 − ε(b))

1. **Cup of Tea → Tea Blending Knowledge** — R ≈ 0.88 · 0.55 = **0.484**. The most visible product depends on the least-evolved component. If the person holding this knowledge leaves, product quality craters.
2. **Brewing → Tea Blending Knowledge** — R ≈ 0.62 · 0.55 = **0.341**. Same root cause; brewing quality is tacit-knowledge dependent.
3. **Tea Leaves → Supplier Relationship** — R ≈ 0.50 · 0.45 = **0.225**. Supplier Relationship is still bespoke (one or two trusted importers). A single-source failure stops the shop.

### d. Suggested Gameplays (from Wardley's 61)

- **#1 Focus on user needs** (Basic Ops) — applied to *Seating / Ambience* and *Cup of Tea*. These are what the customer came for.
- **#26 Differentiation** (Market) — applied to *Cup of Tea* and *Tea Blending Knowledge*. Signature blends, house-recipe brews. Make the difference visible.
- **#17 Co-operation / #41 Alliances** (Accelerators / Ecosystem) — applied to *Supplier Relationship* and *Tea Leaves*. A preferred-partner arrangement with one or two growers secures supply and can become a marketable story.
- **#28 Exploiting buyer / supplier power** (Market) — applied to *Milk & Sugar*, *Cups & Crockery*. These are standard inputs; shop around and let suppliers compete.
- **#43 Sensing Engines (ILC)** (Ecosystem) — *lightweight version*: use the till's sales data to see which blends sell out; industrialise the winners (fixed menu) and innovate new ones behind the counter.
- **#42 Co-creation** (Ecosystem) — applied to *Cup of Tea*. Let regulars suggest and name blends; builds loyalty and feeds the signal loop.
- **#7 Education** (User Perception) — applied to *Tea Leaves* and *Tea Blending Knowledge*. Tasting notes, origin cards, staff-led explanations convert a commodity drink into a perceived-craft product.
- **#6 Channel Conflict** (Basic Ops) — explore takeaway / delivery / loose-leaf retail as an adjacent channel that reuses the same supplier chain.

### e. Doctrine Notes / Violations

Things the map does handle:
- **#1 Focus on user needs** — anchor is the Customer with explicit top-level needs (tea, payment, ambience).
- **#10 Know your users** — only one user type modelled; reasonable for a tea shop but see caveats.

Things to watch:
- **#13 Manage inertia** — the Tea Blending Knowledge component is tacit and person-dependent. Without documentation, succession is an inertia risk (training, recipes, standard operating procedures).
- **#22 Use standards where appropriate** — don't try to build the *Till / POS* or *Card Payment Gateway*; accept the industry standard and go.
- **#17 Effectiveness over efficiency** — resist the urge to industrialise *Brewing* (e.g., automatic machines, push-button) before the craft differentiator is strong enough. Efficiency can erase what the customer actually pays for.
- **Under-specified user layer** — a real business likely has at least two user types (walk-in customer, regular / member) and possibly a staff user (the barista has a need: usable tools). Consider adding anchors if the plan grows.

### f. Caveat

The evolution positions above are *scenarios, not forecasts.* Per Wardley's climatic pattern: **you cannot measure evolution over time or adoption.** The X-axis is a judgment about ubiquity, certainty, perception and publication characteristics *as of now*; arrows drawn later (e.g., "brewing may evolve towards Product") are hypotheses to test, not predictions. The heuristics D, K, R are attention prompts proposed by this skill's math model — they are **not** canonical Wardley concepts, and their rank order should be sanity-checked against judgment before any decision is made on them.
