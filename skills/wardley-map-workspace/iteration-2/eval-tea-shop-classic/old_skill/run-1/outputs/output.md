# Wardley Map — Small Tea Shop

Scenario: A small tea shop serves cups of tea to customers, handles payment, and sources tea leaves from suppliers.

---

## OWM Map

```
title Small Tea Shop
style wardley

// Anchor (user need)
anchor Customer [1.00, 0.90]

// Components — user-visible
component Cup of Tea [0.92, 0.88]
component Payment Processing [0.85, 0.88]
component Customer Service Practice [0.85, 0.625]

// Components — serving layer
component Barista [0.65, 0.625]
component Brewing [0.70, 0.875]
component Cups & Crockery [0.72, 0.88]
component Milk & Sugar [0.68, 0.92]
component Card Terminal [0.65, 0.85]
component Shop Premises [0.60, 0.6875]

// Components — supply layer
component Tea Leaves [0.50, 0.78]
component Hot Water [0.45, 0.875]
component Brewing Knowledge [0.30, 0.88]
component Kettle [0.30, 0.90]
component Supplier Relationship [0.25, 0.625]
component Water Supply [0.18, 0.95]
component Electricity [0.12, 0.95]

// Dependencies (a -> b means "a depends on b")
Customer->Cup of Tea
Customer->Payment Processing
Customer->Customer Service Practice
Cup of Tea->Brewing
Cup of Tea->Cups & Crockery
Cup of Tea->Milk & Sugar
Cup of Tea->Shop Premises
Brewing->Tea Leaves
Brewing->Hot Water
Brewing->Brewing Knowledge
Brewing->Barista
Customer Service Practice->Barista
Barista->Brewing Knowledge
Hot Water->Kettle
Hot Water->Water Supply
Kettle->Electricity
Tea Leaves->Supplier Relationship
Payment Processing->Card Terminal
Shop Premises->Electricity
Shop Premises->Water Supply

// Notes
note Specialty leaves possibly in transition (III↔IV) [0.52, 0.72]
note Card terminals fully utility via Stripe / SumUp [0.67, 0.90]
```

---

## Strategic Analysis

### a. Top 3 by differentiation pressure D = ν · (1 − ε)

| Rank | Component | ν | ε | D |
|---|---|---|---|---|
| 1 | Customer Service Practice | 0.85 | 0.625 | **0.319** |
| 2 | Barista | 0.65 | 0.625 | **0.244** |
| 3 | Shop Premises | 0.60 | 0.6875 | **0.188** |

**Reasoning.** These are the components that are visible to the customer AND not yet commodity. Customer-facing service quality, the barista's craft, and the physical "third-place" ambience are where a small tea shop can actually stand apart — the tea itself, the payment, the crockery are table-stakes commodities.

### b. Top 3 by commodity leverage K = (1 − ν) · ε

| Rank | Component | ν | ε | K |
|---|---|---|---|---|
| 1 | Electricity | 0.12 | 0.95 | **0.836** |
| 2 | Water Supply | 0.18 | 0.95 | **0.779** |
| 3 | Kettle (+ Brewing Knowledge tied with Card Terminal) | 0.30 | 0.90 | **0.630** |

**Reasoning.** These are deep, mature components — rent the utility, don't build it. Electricity and water are already utility, as they should be. The kettle and card terminal are commodity appliances (buy, don't design); brewing knowledge is embedded in training rather than developed internally. A small tea shop should spend zero strategic energy here beyond reliable sourcing.

### c. Top 3 dependency risks R = ν(a) · (1 − ε(b))

| Rank | Edge (a → b) | ν(a) | ε(b) | R |
|---|---|---|---|---|
| 1 | Customer Service Practice → Barista | 0.85 | 0.625 | **0.319** |
| 2 | Tea Leaves → Supplier Relationship | 0.50 | 0.625 | **0.188** |
| 3 | Brewing → Tea Leaves | 0.70 | 0.78 | **0.154** |

**Reasoning.**
- **Service → Barista.** The high-visibility service experience depends on a single (often one or two) human role that is far from a commodity. Staff illness, turnover, or a bad hire degrades the most differentiating layer immediately.
- **Tea Leaves → Supplier Relationship.** A small shop typically has 1–2 suppliers. That upstream is still Stage III (product/rental-ish), so price, quality, and availability are not fully stabilised — a single supplier outage or price hike is felt directly at the counter.
- **Brewing → Tea Leaves.** Specialty-leaf variants are still in transition between Stage III and IV; quality and provenance of leaves materially changes the cup the customer tastes.

### d. Suggested gameplays (named, from Wardley's 61)

| Play | # | Target component(s) | Why |
|---|---|---|---|
| **Focus on user needs** | 1 | Customer / Cup of Tea / Customer Service | Doctrine-grade default; the whole map anchors on this |
| **Differentiation** | 26 | Customer Service Practice, Shop Premises, Barista | Make the visible, low-ε layer meaningfully distinct (ambience, service, signature blends) |
| **Co-operation** | 17 | Supplier Relationship | Work with specialty-leaf suppliers to secure supply, provenance, and pricing |
| **Exploiting buyer / supplier power** | 28 | Supplier Relationship, Tea Leaves | Evaluate whether to consolidate to one strong supplier (lower cost) or diversify (reduce risk) |
| **Alliances** | 41 | Supplier Relationship, Shop Premises (e.g., local bakery) | Bundle with a local bakery/roaster to widen user-need coverage without new capex |
| **Standards game** (lightweight) | 30 | Payment Processing | Adopt the dominant consumer-payment standard (contactless, QR, wallet) rather than resisting |
| **Two factor** | 45 | Customer Service Practice | Bring regulars and staff together via loyalty / community events — marginal value rises with regulars |
| **Harvesting** | 29 | Tea Leaves | Let specialty-tea startups mature, then take on the ones that prove themselves with your customers |
| **Education** | 7 | Tea Leaves, Brewing Knowledge | Tasting events / menu storytelling convert Stage III specialty leaves into perceived value |
| **Effective & Efficient** | 3 | Kettle, Card Terminal, Electricity, Water Supply | Commoditise the commodities — use the cheapest reliable utility option, don't over-engineer |

### e. Doctrine violations / cautions

- **#1 Focus on user needs** — satisfied (customer anchor present).
- **#10 Know your users** — partially satisfied. The map has only a single *buying customer* anchor. A real tea shop usually has at least three user segments: (i) the grab-and-go commuter, (ii) the sit-in regular / community-seeker, (iii) the corporate/catering buyer. These have different ν profiles (e.g., the sit-in regular values Shop Premises and Customer Service far more than the commuter). **Recommendation:** add per-segment anchors before making final strategic bets.
- **#7 Use appropriate methods** / **#22 Use standards where appropriate** — the utility layer (Electricity, Water, Card Terminal, Kettle) is correctly treated as commodity; no violation, but note the temptation to over-customise the POS — resist it.
- **#13 Manage inertia** — *Human capital* inertia (form #4 in `inertia.md`) is a real risk on the Barista dependency: losing a trained barista visibly harms the most-differentiating layer. Plan for cross-training and written recipes (turning tacit Brewing Knowledge into codified practice).
- **Knowledge layer under-specified.** Only *Brewing Knowledge* appears. A fuller map would add *Customer preferences / order history* (Data) and *Local demand patterns* (Knowledge) — both currently missing.

### f. Caveat

Evolution positions here are **a snapshot, not a forecast**. Wardley's climatic pattern is explicit: *"you cannot measure evolution over time or adoption."* Specialty tea leaves and the customer-service layer are genuinely *in transition* — the ε values for those components should be read as a current midpoint with a band of uncertainty, not as a prediction of where they will land. Revisit the map when any of: a new supplier channel opens, card-present payment regulations change, or the shop's customer mix shifts materially.
