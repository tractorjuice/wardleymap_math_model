# Wardley Map: Small Tea Shop

Scenario: A small tea shop that serves cups of tea to customers, handles payment, and sources tea leaves from suppliers.

---

## 1. OWM map

```
title Small Tea Shop
style wardley

// Anchor
anchor Customer [1.00, 0.50]

// Visible value-chain
component Cup of Tea [0.90, 0.88]
component Payment [0.88, 0.88]

// Near-user activities / practices
component Brewing [0.72, 0.87]
component Hospitality / Service [0.68, 0.65]
component Staff (Barista) [0.66, 0.70]
component Shop Premises [0.62, 0.78]
component Cup (Crockery) [0.70, 0.90]
component Milk & Sugar [0.58, 0.92]
component Till / POS [0.60, 0.62]

// Intermediate
component Hot Water [0.55, 0.95]
component Tea Leaves [0.54, 0.85]
component Card Payment Processing [0.50, 0.85]

// Deeper layer
component Kettle / Boiler [0.36, 0.88]
component Tea Sourcing (Procurement) [0.30, 0.65]
component Tea Blending Knowledge [0.26, 0.55]

// Supplier / foundation layer
component Tea Supplier Relationship [0.18, 0.45]
component Electricity [0.15, 0.95]
component Water (mains) [0.13, 0.95]

// Dependencies (a -> b  means "a depends on b")
Customer->Cup of Tea
Customer->Payment
Customer->Hospitality / Service

Cup of Tea->Brewing
Cup of Tea->Cup (Crockery)
Cup of Tea->Milk & Sugar

Brewing->Tea Leaves
Brewing->Hot Water
Brewing->Staff (Barista)

Hospitality / Service->Staff (Barista)
Hospitality / Service->Shop Premises

Staff (Barista)->Shop Premises
Shop Premises->Electricity
Shop Premises->Water (mains)

Hot Water->Kettle / Boiler
Hot Water->Water (mains)
Kettle / Boiler->Electricity

Payment->Till / POS
Payment->Card Payment Processing
Till / POS->Electricity
Card Payment Processing->Electricity

Tea Leaves->Tea Sourcing (Procurement)
Tea Sourcing (Procurement)->Tea Supplier Relationship
Tea Sourcing (Procurement)->Tea Blending Knowledge

// Notes
note Utilities form the industrialised foundation [0.08, 0.92]
note Supplier relationship is the one custom element [0.18, 0.40]

// Evolution arrows (scenario, not forecast)
evolve Till / POS 0.80
evolve Tea Supplier Relationship 0.60
```

---

## 2. Strategic analysis

### a. Top 3 by differentiation pressure D(v) = ν · (1 − ε)

| Rank | Component | ν | ε | D |
|---|---|---|---|---|
| 1 | Hospitality / Service | 0.68 | 0.65 | **0.238** |
| 2 | Staff (Barista) | 0.66 | 0.70 | **0.198** |
| 3 | Till / POS | 0.60 | 0.62 | **0.228** |

Reasoning: Hospitality and the barista experience are what a small tea shop can genuinely differentiate on — visible to the customer and not yet fully commoditised. Till/POS is high-visibility and mid-evolution; the **product choice** (paper receipts vs. app receipts, loyalty features) still carries differentiation weight, but it is fading fast — see point (b) below.

Honourable mention: Tea Sourcing (D = 0.30 · 0.35 = 0.105) — low visibility but deep bespoke potential if the shop leans into a "single-estate tea" identity.

### b. Top 3 by commodity leverage K(v) = (1 − ν) · ε

| Rank | Component | ν | ε | K |
|---|---|---|---|---|
| 1 | Electricity | 0.15 | 0.95 | **0.808** |
| 2 | Water (mains) | 0.13 | 0.95 | **0.826** |
| 3 | Card Payment Processing | 0.50 | 0.85 | **0.425** |

Reasoning: Electricity and water should be bought as utilities — no in-house alternative makes sense. Card processing (Stripe / SumUp / Square / iZettle) is a utility-grade service; a small tea shop should rent, never build. Kettle/Boiler (K = 0.563) and Hot Water (K = 0.428) are also strong rental/utility candidates (boiler-as-a-service lease, plumbed water).

### c. Top 3 dependency risks R(a, b) = ν(a) · (1 − ε(b))

| Rank | Edge (a → b) | ν(a) | ε(b) | R |
|---|---|---|---|---|
| 1 | Tea Sourcing → Tea Supplier Relationship | 0.30 | 0.45 | 0.165 |
| 2 | Tea Sourcing → Tea Blending Knowledge | 0.30 | 0.55 | 0.135 |
| 3 | Cup of Tea → Brewing (via Staff dependency chain) | 0.90 | 0.70 (Staff) | 0.270 |

Reasoning:
- **#3 is the largest raw R**: the highly-visible Cup of Tea inherits risk from the Stage-III Staff (Barista) component. A single barista off sick closes the shop.
- **#1 / #2 sit at the supplier end**: the whole chain rests on *one* supplier relationship at ε ≈ 0.45 (Stage II / III border). If that supplier fails, sources a bad crop, or raises prices unilaterally, the shop has no second source.

### d. Suggested Wardley gameplays (from the 61-play catalogue)

Targeting the highlighted components:

1. **#1 Focus on user needs** (Basic Operations) — targets *Hospitality / Service* and *Cup of Tea*. The highest-D component is the service experience; make that the explicit organising principle.
2. **#26 Differentiation** (Market) — targets *Tea Leaves* and *Tea Sourcing*. Turn the supplier relationship from risk into story: single-estate / speciality-blend positioning.
3. **#41 Alliances** (Ecosystem) — targets *Tea Supplier Relationship*. A formal alliance (multi-year contract, co-marketing) with one or two suppliers removes the single-point-of-failure without industrialising the relationship.
4. **#17 Co-operation** (Accelerators) — targets *Tea Sourcing*. Buying-group co-operation with other independent tea shops improves buyer power without losing boutique identity.
5. **#28 Exploiting buyer / supplier power** (Market) — targets *Tea Supplier Relationship* as a counter-move if the supplier tries to raise prices.
6. **#22 Standards game / Use standards where appropriate** — targets *Card Payment Processing* and *Till / POS*. Adopt an industry-standard utility rather than building bespoke. (Doctrine #22 backs this.)
7. **#56 First mover / #57 Fast follower** — targets *Till / POS* on its evolve trajectory. Adopt contactless / QR-pay / tap-to-phone early as a visible modernisation signal.
8. **#7 Education** (User Perception) — targets *Tea Blending Knowledge*. Tasting notes, staff-led mini-sessions turn tacit knowledge into a visible asset.

### e. Doctrine observations (from the 40 principles)

- **#1 Focus on user needs** — satisfied: anchor is the Customer, and the top-D play above is aligned.
- **#10 Know your users** — the map uses a single anchor; in reality "dine-in customer", "takeaway customer" and possibly "wholesale buyer" could be separate anchors. *Mild violation* — consider adding a second anchor if takeaway volume matters.
- **#12 Use appropriate tools / #22 Use standards where appropriate** — reinforces the commodity-leverage recommendations in (b); do not build what you can rent.
- **#13 Manage inertia** — the supplier relationship carries classic inertia forms: **#1 Supplier relationship change**, **#7 Supplier-trust concerns** and **#14 Strategic-control loss** (see `inertia.md`). Any move to switch or add a supplier should be planned against these.
- **#14 Manage failure** — the Staff-sick-shop-closes single-point-of-failure is not addressed on the map. Add a second-barista / key-holder arrangement or cross-training.
- **Knowledge layer is thin** — only *Tea Blending Knowledge* is explicit. If hospitality practice or service recipes are central to differentiation, they deserve explicit Practice nodes (τ = P).

### f. Caveat

Evolution positions are a **placement now**, not a forecast. Wardley's climatic pattern states: *"you cannot measure evolution over time or adoption."* The two `evolve` arrows above (Till/POS → 0.80, Supplier Relationship → 0.60) are **scenarios**, not predictions — they describe a plausible direction if the recommended plays succeed, nothing more.

---

## 3. Evolution scoring notes (audit trail)

Components where the 4-row cheat-sheet rows disagree were flagged and a range reported:

- **Staff (Barista)**: Ubiquity IV (widespread), Certainty IV (common), User Perception III–IV, Publication IV. ε ∈ [0.625, 0.875], midpoint ≈ 0.75 — adjusted down to 0.70 to reflect that *service quality* still varies (i.e., the underlying practice is not fully best-practice / Stage IV in a small independent context).
- **Tea Leaves**: Baseline tea is Stage IV commodity (Tesco PG Tips). Speciality single-estate leaf is Stage II–III. Placed at 0.85 assuming the shop uses mainly commodity-grade leaf; if they pivot to speciality, this drops to ~0.55 and D rises sharply.
- **Tea Supplier Relationship**: The *market* of tea suppliers is Stage IV, but a *specific bilateral relationship* with a chosen supplier is Stage II (Custom Built) — bespoke terms, personal trust, non-standard SLA. Placed at 0.45 as the relationship-level score.
- **Till / POS**: In transition. Traditional tills are Stage IV; cloud POS (Square, Lightspeed) is Stage III being absorbed into Stage IV utilities. Placed at 0.62 with an evolve arrow to 0.80.

All other components scored as clear Stage IV commodity / utility (Electricity, Water, Hot Water, Cup, Milk & Sugar, Kettle, Card Payment Processing, Brewing as an activity).
