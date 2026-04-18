# Wardley Map — Small Tea Shop

**Scenario:** A small tea shop that serves cups of tea to customers, handles payment, and sources tea leaves from suppliers.

The map is expressed as the tuple $\mathcal{M} = (V, E, U, \nu, \varepsilon, t)$. Evolution scores are seeded from the 4-row cheat-sheet subset (Ubiquity, Certainty, User Perception, Publication Types) and then adjusted where judgment disagrees. Visibility is seeded from graph distance to the Customer anchor and then adjusted.

---

## 1. OWM Map

```owm
title Small Tea Shop
style wardley

// Anchor — single user type (walk-in customer)
anchor Customer [0.98, 0.55]

// User-facing value
component Cup of Tea [0.90, 0.68]
component Service / Hospitality [0.82, 0.42]
component Payment [0.86, 0.82]

// Craft and mid-chain
component Barista / Tea-maker [0.72, 0.40]
component Brewing [0.68, 0.60]
component Menu / Tea Selection [0.70, 0.50]
component Cup & Teapot [0.58, 0.85]
component Milk & Sugar [0.50, 0.88]

// Ingredients
component Tea Leaves [0.48, 0.72]
component Hot Water [0.42, 0.92]
component Kettle / Urn [0.28, 0.90]

// Premises and utilities
component Shop Premises [0.30, 0.55]
component Electricity [0.12, 0.95]
component Water [0.10, 0.95]

// Payment rails
component Till / POS [0.55, 0.70]
component Card Payment Processing [0.45, 0.90]
component Cash Handling [0.40, 0.92]

// Supply chain
component Tea Sourcing [0.26, 0.48]
component Tea Supplier Relationship [0.16, 0.42]

// Dependencies (a -> b  means "a depends on b")
Customer->Cup of Tea
Customer->Service / Hospitality
Customer->Payment
Cup of Tea->Brewing
Cup of Tea->Cup & Teapot
Cup of Tea->Milk & Sugar
Cup of Tea->Menu / Tea Selection
Service / Hospitality->Barista / Tea-maker
Service / Hospitality->Shop Premises
Brewing->Tea Leaves
Brewing->Hot Water
Brewing->Barista / Tea-maker
Hot Water->Kettle / Urn
Hot Water->Water
Kettle / Urn->Electricity
Shop Premises->Electricity
Shop Premises->Water
Payment->Till / POS
Payment->Card Payment Processing
Payment->Cash Handling
Till / POS->Electricity
Card Payment Processing->Electricity
Tea Leaves->Tea Sourcing
Tea Sourcing->Tea Supplier Relationship

// Evolution trajectories (scenarios, not forecasts)
evolve Tea Supplier Relationship 0.55
evolve Till / POS 0.88
evolve Card Payment Processing 0.95

// Annotations
note Differentiation zone [0.75, 0.32]
note Utility commodity [0.15, 0.92]
note Tea-sourcing moat (optional) [0.20, 0.45]
```

---

## 2. Cheat-sheet scoring (selected components)

Quick 4-row scoring at band midpoints (I = 0.125, II = 0.375, III = 0.625, IV = 0.875).

| Component | Ubiquity | Certainty | User Perception | Publication | Mean ε | Stage |
|---|---|---|---|---|---|---|
| Cup of Tea | IV (0.875) | III (0.625) | III (0.625) | III (0.625) | 0.688 | Product (+rental) |
| Service / Hospitality | II (0.375) | II (0.375) | II (0.375) | II–III (0.500) | 0.406 | Custom Built |
| Brewing | III (0.625) | III (0.625) | III (0.625) | III (0.625) | 0.625 | Product (+rental) |
| Tea Leaves | III (0.625) | III (0.625) | III (0.625) | IV (0.875) | 0.688 | Product (+rental) |
| Card Payment Processing | IV (0.875) | IV (0.875) | IV (0.875) | IV (0.875) | 0.875 | Commodity (+utility) |
| Electricity | IV (0.875) | IV (0.875) | IV (0.875) | IV (0.875) | 0.875 | Commodity (+utility) |
| Barista / Tea-maker | II (0.375) | II (0.375) | II (0.375) | II–III (0.500) | 0.406 | Custom Built |
| Tea Supplier Relationship | II (0.375) | II (0.375) | II (0.375) | II (0.375) | 0.375 | Custom Built |

Rows agree closely — low variance, no components flagged "in transition" except Tea Supplier Relationship, which is moving as aggregators (e.g., wholesale tea platforms) industrialise the segment.

---

## 3. Strategic Analysis

### a. Top 3 by differentiation pressure — $D(v) = \nu(v)\cdot(1-\varepsilon(v))$

| Rank | Component | ν | ε | D | Why it matters |
|---|---|---|---|---|---|
| 1 | **Service / Hospitality** | 0.82 | 0.42 | **0.476** | Highly visible to Customer and still Custom Built. Warmth, attentiveness, ritual — this is the real moat for a small shop competing against chains and supermarket tea. |
| 2 | **Barista / Tea-maker** | 0.72 | 0.40 | **0.432** | Skill-based craft (brewing ratios, steeping, latte art for tea). The human behind the counter is where differentiation compounds. |
| 3 | **Menu / Tea Selection** | 0.70 | 0.50 | **0.350** | Curation of leaves, blends, seasonal additions. A well-curated menu is visible to Customer and not yet commoditised for speciality shops. |

*Reasoning:* D is highest in the upper-left region — visible to the user and not yet commoditised. This is the **build / invest** zone.

### b. Top 3 by commodity leverage — $K(v) = (1-\nu(v))\cdot\varepsilon(v)$

| Rank | Component | ν | ε | K | Decision |
|---|---|---|---|---|---|
| 1 | **Water** | 0.10 | 0.95 | **0.855** | Utility — pay the meter, do not engineer. |
| 2 | **Electricity** | 0.12 | 0.95 | **0.836** | Utility — same. |
| 3 | **Card Payment Processing** | 0.45 | 0.90 | **0.495** | Rent from Stripe / Square / SumUp — do not build, do not negotiate proprietary terminals. |

Honorable mentions: **Cash Handling** (0.552), **Hot Water** (0.534), **Kettle / Urn** (0.648) — all utility-like. *Don't* spend engineering energy here; spend only on selecting the right supplier.

### c. Top 3 dependency risks — $R(a,b) = \nu(a)\cdot(1-\varepsilon(b))$

| Rank | Edge (a, b) | ν(a) | 1−ε(b) | R | Why it's risky |
|---|---|---|---|---|---|
| 1 | **(Service / Hospitality, Barista / Tea-maker)** | 0.82 | 0.60 | **0.492** | The whole user-facing experience pivots on a single craft role. If the barista quits or is ill, the differentiator evaporates. |
| 2 | **(Brewing, Barista / Tea-maker)** | 0.68 | 0.60 | **0.408** | Same dependency surfacing through a second edge — reinforces the fragility. |
| 3 | **(Tea Leaves, Tea Sourcing)** | 0.48 | 0.52 | **0.250** | Single-supplier concentration. Harvest failure, shipping disruption, or price shock on one origin breaks the menu. |

### d. Suggested gameplays (named from Wardley's 61-play catalogue)

- **#1 Focus on user needs** — map is correctly anchored on Customer; keep re-anchoring decisions there. The "cup of tea" is the transactional output, but the *service* is the need.
- **#26 Differentiation on Service / Hospitality and Menu / Tea Selection** — lean into ceremony, provenance stories, seasonal single-estate leaves. These are the two highest-D components.
- **#36 Directed investment on Barista / Tea-maker** — training, progression, retention pay. Human capital is your moat; treat it as an investment, not a cost line.
- **#38 Creating centres of gravity** — make the shop a known destination for tea enthusiasts. Hosting cuppings / tastings compounds #26 and #36.
- **#41 Alliances on Tea Sourcing** — second-source across at least two origins / agents to defuse the supply-chain risk (addresses R-ranked edge #3).
- **#29 Harvesting on Till / POS and Card Payment Processing** — let the market (Square, SumUp, Stripe Terminal) do the engineering; buy the cheapest reliable option and switch freely.
- **#34 Procrastination on Kettle / Urn and utilities** — deliberately do nothing here. Evolution is doing the work for you; buying commodity equipment is the right move.
- **#15 Open Approaches — NOT recommended** on the Service / Hospitality or Menu components — do not open-source your moat. Noted here for completeness because doctrine #22 applies.

### e. Doctrine notes (against Wardley's 40 principles)

- **#1 Focus on user needs** — satisfied. Anchor is Customer.
- **#3 Use a common language** — satisfied. Components are concrete nouns.
- **#9 Think small (know the details)** — satisfied. Utilities, payment rails, and supply chain are decomposed to the level where each can be cheat-sheet-scored.
- **#10 Know your users** — *partially violated.* The map uses a single Customer anchor. In reality a tea shop has at least two user types: **walk-in / sit-in customer** (values atmosphere, service, ritual) vs **takeaway / commuter customer** (values speed, consistency, payment friction). If either segment is strategically material, add a second anchor.
- **#13 Manage inertia** — worth flagging. The Barista component carries **inertia form #4 (Human capital / skill acquisition)** — losing or replacing the craft role is costly. Form #11 (Suitability doubt from customers) also applies if the brand is tied to one person.
- **#22 Use standards where appropriate** — satisfied. Standards applied to Stage IV components (electricity, water, payment processing); not forced onto Service / Hospitality.
- **#7 Use appropriate methods** — worth checking. Commodity parts of the map (payments, utilities) want operational-excellence methods; the Service / Hospitality side wants agile / experimentation. Don't standardise the whole shop on one management style.

### f. Climatic context (patterns actively shaping this map)

- **#3 Everything evolves through supply and demand competition** — Tea Supplier Relationship and Till/POS are both drifting rightward; the `evolve` arrows capture that scenario.
- **#7 Characteristics change as components evolve** — justifies why Service (Stage II) should be run differently from Card Payment Processing (Stage IV).
- **#8 No single method fits all** — operationalises #7 in management terms; underpins the doctrine note on #7.
- **#15–17 Inertia patterns** — the single-barista dependency and single-supplier concentration are concrete instances.
- **#18 You cannot measure evolution over time or adoption** — binding caveat on all `evolve` arrows.
- **#27 Product-to-utility punctuated equilibrium** — visible on Card Payment Processing (already past) and creeping on Till / POS (tap-to-phone utility models are the next wave).

### g. Caveat

Evolution trajectories are **scenarios, not forecasts**. Wardley's climatic pattern #18: *"you cannot measure evolution over time or adoption."* The `evolve` arrows in the OWM block and the stage placements in the cheat-sheet table reflect a judgment made now, against present signals; they should be re-scored when the market sends new signals (e.g., a major tea-aggregator entering the UK market, a step-change in tap-to-phone payment adoption, or a local labour-market shift for craft baristas). The derived heuristics D, K, and R are attention prompts proposed by this skill's math model, not canonical Wardley concepts — treat them as a way to prioritise conversations, not as ground truth.
