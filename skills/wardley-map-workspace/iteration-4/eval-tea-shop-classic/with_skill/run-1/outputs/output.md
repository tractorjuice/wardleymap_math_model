# Wardley Map — Small Tea Shop

**Scenario:** A small tea shop that serves cups of tea to customers, handles payment, and sources tea leaves from suppliers.

**Market framing:** small UK independent tea shop, 2026. (Market-relative ubiquity matters — see caveat #1 in the cheat sheet.)

---

## 1. Components and anchors

**Anchor set `U`** — one user type (the walk-in customer). One anchor is appropriate for a single-sided B2C shop, though we flag below that "takeaway" vs "sit-in" could justify two anchors in a larger workshop pass.

**Components `V`** grouped by layer:

- *User-facing:* Cup of Tea, Service / Hospitality, Payment
- *Craft mid-chain:* Barista, Brewing, Menu / Tea Selection, Cup & Saucer, Milk / Sugar / Accompaniments
- *Ingredients & equipment:* Tea Leaves, Hot Water, Kettle / Urn, Shop Premises, Furniture / Ambience
- *Payment layer:* Till / POS, Card Payment Processing
- *Utilities:* Electricity, Water, Internet
- *Supply chain:* Tea Sourcing, Tea Supplier Relationship, Sustainability Certification

---

## 2. Cheat-sheet evolution scores (quick 4-row)

For each component, `ε` is the mean of row picks at band midpoints (Stage I=0.125, II=0.375, III=0.625, IV=0.875). `Var(ε) > 0.03` flags a component for deep placement (step 4.5).

| Component | Ubiq | Cert | UserPerc | PubType | ε (mean) | Var |
|---|---|---|---|---|---|---|
| Cup of Tea | IV | III | III | III | 0.6875 | 0.012 |
| Service / Hospitality | III | II | III | II | 0.500 | 0.016 |
| Payment (the act) | IV | IV | IV | IV | 0.875 | 0 |
| Barista | III | III | III | III | 0.625 | 0 |
| Brewing | III | III | III | III | 0.625 | 0 |
| Menu / Tea Selection | III | II | III | III | 0.5625 | 0.012 |
| Cup & Saucer | IV | IV | IV | IV | 0.875 | 0 |
| Milk / Sugar / Accompaniments | IV | IV | IV | IV | 0.875 | 0 |
| Tea Leaves (generic) | IV | IV | IV | IV | 0.875 | 0 |
| Tea Leaves (specialty) | III | III | III | III | 0.625 | 0 |
| Hot Water | IV | IV | IV | IV | 0.90 | 0 |
| Kettle / Urn | IV | IV | IV | IV | 0.90 | 0 |
| Shop Premises | III | IV | III | III | 0.6875 | 0.012 |
| Furniture / Ambience | III | III | III | III | 0.625 | 0 |
| Till / POS | III → IV | III → IV | IV | IV | **0.72** | **0.035** |
| Card Payment Processing | IV | IV | IV | IV | 0.90 | 0 |
| Electricity | IV | IV | IV | IV | 0.95 | 0 |
| Water | IV | IV | IV | IV | 0.95 | 0 |
| Internet | IV | IV | IV | IV | 0.90 | 0 |
| Tea Sourcing (broker/wholesale) | III | III | III | III | 0.625 | 0 |
| Tea Supplier Relationship (direct trade) | II | II | II | II | 0.375 | 0 |
| Sustainability Certification | III | III | III | II | **0.5625** | 0.012 |

Two components flagged: **Till / POS** (Var > 0.03, plus strategically moving) and **Tea Supplier Relationship** (strategically critical for differentiation). I also researched **Service / Hospitality** (top D) and **Specialty Tea Leaves / Certification** (specialised domain with regulatory flavour). Deep-placement notes in section 4g.

---

## 3. OWM output

```owm
title Small Tea Shop (UK, 2026)
style wardley

// Anchor
anchor Customer [0.98, 0.55]

// User-facing
component Cup of Tea [0.90, 0.69]
component Service / Hospitality [0.84, 0.50]
component Payment [0.82, 0.88]

// Craft mid-chain
component Menu / Tea Selection [0.74, 0.56]
component Barista [0.72, 0.62]
component Brewing [0.66, 0.62]
component Cup & Saucer [0.58, 0.88]
component Milk / Sugar / Accompaniments [0.52, 0.88]

// Ingredients & equipment
component Specialty Tea Leaves [0.48, 0.62]
component Hot Water [0.42, 0.90]
component Kettle / Urn [0.30, 0.90]
component Shop Premises [0.32, 0.68]
component Furniture / Ambience [0.36, 0.62]

// Payment layer
component Till / POS [0.55, 0.72]
component Card Payment Processing [0.44, 0.90]

// Supply chain
component Tea Sourcing [0.28, 0.62]
component Tea Supplier Relationship [0.18, 0.38]
component Sustainability Certification [0.22, 0.56]

// Utilities
component Internet [0.20, 0.90]
component Electricity [0.12, 0.95]
component Water [0.10, 0.95]

// Dependencies
Customer->Cup of Tea
Customer->Service / Hospitality
Customer->Payment

Cup of Tea->Brewing
Cup of Tea->Cup & Saucer
Cup of Tea->Milk / Sugar / Accompaniments
Cup of Tea->Menu / Tea Selection

Service / Hospitality->Barista
Service / Hospitality->Shop Premises
Service / Hospitality->Furniture / Ambience

Menu / Tea Selection->Specialty Tea Leaves
Menu / Tea Selection->Tea Sourcing

Brewing->Specialty Tea Leaves
Brewing->Hot Water
Brewing->Barista

Barista->Shop Premises

Hot Water->Kettle / Urn
Hot Water->Water
Kettle / Urn->Electricity

Payment->Till / POS
Payment->Card Payment Processing
Till / POS->Electricity
Till / POS->Internet
Card Payment Processing->Internet
Card Payment Processing->Electricity

Specialty Tea Leaves->Tea Sourcing
Tea Sourcing->Tea Supplier Relationship
Tea Sourcing->Sustainability Certification

Shop Premises->Electricity
Shop Premises->Water
Shop Premises->Internet

// Evolution scenarios (not forecasts)
evolve Till / POS 0.88
evolve Tea Supplier Relationship 0.55
evolve Sustainability Certification 0.72

note Differentiation zone [0.74, 0.40]
note Utility commodity [0.15, 0.92]
note Moat: direct trade + craft [0.30, 0.30]
```

---

## 4. Strategic analysis

### a. Top 3 by differentiation pressure `D = ν · (1 − ε)`

1. **Service / Hospitality** — `0.84 · 0.50 = 0.42`. Visible to every customer, still Stage II–III (emerging good practice, not commoditised). The core user-facing differentiator; a small tea shop competes on service and atmosphere, not on boiling water.
2. **Menu / Tea Selection** — `0.74 · 0.44 = 0.33`. A curated selection (matcha, hojicha, single-estate) is in Stage II–III and is what gets customers back. This is the craft curator's moat.
3. **Barista** — `0.72 · 0.38 = 0.27`. Barista skill (water temperature per varietal, steep time, ceremony) is Stage III and firmly in the differentiation zone. Specialty tea preparation is "third-wave" territory — parallel to specialty coffee.

### b. Top 3 by commodity leverage `K = (1 − ν) · ε`

1. **Water** — `0.90 · 0.95 = 0.86`. Pure utility. Do not engineer.
2. **Electricity** — `0.88 · 0.95 = 0.84`. Same.
3. **Card Payment Processing** — `0.56 · 0.90 = 0.50`. Rent from SumUp (1.69%), Square (1.75%) or Stripe (1.5% + 20p). Never build.

Close runners-up: Kettle / Urn (`0.70 · 0.90 = 0.63`), Internet (`0.80 · 0.90 = 0.72`), Milk / Sugar (`0.48 · 0.88 = 0.42`).

### c. Top 3 dependency risks `R(a, b) = ν(a) · (1 − ε(b))`

1. **(Service / Hospitality, Barista)** = `0.84 · 0.38 = 0.32` — the whole user-facing experience hangs on a single skilled barista. Human-capital fragility (inertia form #4).
2. **(Brewing, Barista)** = `0.66 · 0.38 = 0.25` — same barista dependency seen from the brewing side.
3. **(Tea Leaves, Tea Supplier Relationship)** = `0.48 · 0.62 = 0.30` — specialty tea is only as good as the one estate / broker relationship. Single-source risk on the ingredient that most differentiates you.

Also notable: (Menu / Tea Selection, Tea Sourcing) = `0.74 · 0.38 = 0.28`.

### d. Suggested gameplays (from Wardley's 61-play catalogue)

- **#1 Focus on user needs** — trivially true but worth restating: the map is anchored correctly; the whole business is Service / Hospitality + Cup of Tea, not the back-office.
- **#26 Differentiation** on *Service / Hospitality*, *Menu / Tea Selection*, and *Barista* — lean into ceremony, tastings, rare varietals, educational moments. Bidfood's 53% "would pay more for a premium tea experience" figure is directly actionable here.
- **#41 Alliances** on *Tea Supplier Relationship* — second-source from at least two direct-trade partners or a Fairtrade wholesaler (Clipper, Equal Exchange) as backstop. Reduces single-estate risk (R above).
- **#42 Co-creation** on *Menu / Tea Selection* — run tastings / workshops with regulars and let the menu evolve from what they respond to. Compounds Differentiation and builds switching cost via relationship.
- **#29 Harvesting** on *Till / POS*, *Card Payment Processing*, *Kettle / Urn* — let the market develop these; pick the cheapest reliable commodity. Do not engineer custom POS or payment flows.
- **#34 Procrastination** on utilities (Electricity, Water, Internet) — literally do nothing strategic. Pay the bill.
- **#56 First mover** (narrow) on *Sustainability Certification* — if direct-trade + transparent supply chain is heading to Stage III industrialisation (my deep-placement finding), being the local shop that leads with it wins while the wave is still forming.

### e. Doctrine notes (violations / reminders from Wardley's 40 principles)

- ✓ **#1 Focus on user needs** — anchor = Customer, chain traces back cleanly.
- ⚠ **#10 Know your users** — single anchor is a simplification. A workshop-grade pass should add a second anchor for *Takeaway Customer* (who weights Speed higher and Service / Hospitality lower) versus *Sit-in Customer* (who weights ambience and ceremony). Flagging not fixing.
- ⚠ **#13 Manage inertia** — dominant inertia here is **form #4 (human capital)**: Barista skill is hard to hire, hard to replicate. Forms **#2 (sunk capital)** in the lease and fit-out, and **#8 (skill acquisition)** in customer habit ("I always get the Darjeeling") also apply.
- ✓ **#22 Use standards where appropriate** — Card Payment Processing and POS should use standard vendors, not bespoke.
- ⚠ **#15 Think FIRE** — if experimenting with new menu items or ceremonies, keep them fast, inexpensive, restrained, elegant. A small shop can't afford costly menu experiments.

### f. Climatic context (which of the 27 patterns are active)

- **#3 Everything evolves** — Till / POS is visibly moving Genesis → Commodity on a multi-decade arc (till → electronic POS → tablet POS → fully cloud utility on shared hardware). Do not fight this.
- **#15–17 Inertia** — human capital around the barista, sunk capital in the lease, and habit-based consumer inertia all bind the shop to its current location and people. These are moats as well as risks.
- **#27 Product → Utility punctuated equilibrium** — actively shaping Till / POS right now. SumUp / Square / Stripe Terminal have turned card acceptance into a pure utility in the UK market in the last five years; the POS layer above it is finishing that transition in 2026. This is the exact pattern Wardley warns to *act on quickly* when you see it.
- **#11 Future value is inversely proportional to certainty** — the Menu / Tea Selection and Supplier Relationship are the uncertain parts of the chain, which is precisely why they hold the option value.

### g. Deep-placement notes

I ran targeted searches on four components. Summary of what shifted:

1. **Till / POS — initial cheat-sheet 0.625 (mid Product). Shifted to 0.72 (late Product, close to Commodity).**
   Vendor-landscape search (April 2026) showed SumUp, Square, Stripe Terminal, POSApt and ~5 other dominant entry-level UK providers; all offer no-monthly-fee entry points, plug-in readers, and free POS software with inventory management. What Epos and POSApt 2026 buyer guides treat POS selection as a "pick the cheapest reliable one" decision — pure Stage III → IV publication pattern (operations / use, not wonder). The Var > 0.03 in the cheat-sheet was the rows capturing this transition. `evolve` arrow to 0.88 reflects the utility endpoint this component is visibly moving toward.

2. **Tea Supplier Relationship — initial 0.375 (mid Custom Built). Confirmed at 0.38.**
   For a *small specialty shop* doing direct trade the relationship genuinely is custom-built: long-term producer relationships, non-standardised contracts, geographic specificity. For a generic tea shop buying from Tetley / Twinings wholesale, the same component would sit at Stage IV (0.90+). Map is correctly split between generic *Tea Sourcing* (wholesale Stage III) and *Tea Supplier Relationship* (direct-trade Stage II). `evolve` to 0.55 reflects gradual standardisation of direct-trade templates (certifications, digital traceability) moving this toward Product over 5–10 years.

3. **Service / Hospitality — initial cheat-sheet 0.50 (mid Custom → early Product). Confirmed at 0.50.**
   Search on specialty tea trends found an explicit "third-wave tea" movement in 2026 parallel to specialty coffee: ceremonies, single-estate pairings, workshops, hojicha / matcha / functional blends — and a 53% Bidfood willingness-to-pay-more signal. This is exactly the Stage II–III "domain of experts / leading edge / emerging" cheat-sheet picture. Position held. Crucially, "service in a generic café" would be Stage III (0.625); *specialty* tea hospitality is earlier on the curve and therefore a real differentiation zone.

4. **Sustainability Certification — initial 0.5625 (early Product). Held at 0.56.**
   Fairtrade, Rainforest Alliance, and organic are well-established Product-stage offerings with mature UK auditors and consumer recognition. Publication pattern is "how to adopt / comparison" (Stage III). But emerging **digital-traceability / transparent-supply-chain regulation** (EU CSRD, UK reporting) is pulling this toward Stage IV. `evolve` to 0.72 reflects that likely regulatory industrialisation. Treat as "buy the certificate, rent the traceability tool, don't build either."

(The remaining ~16 components are either obvious commodities — Electricity, Water, Card Processing, Cup & Saucer, Milk — or obvious craft — Brewing, Barista — and did not warrant research under the skill's step 4.5 budget guidance.)

### h. Caveat

Evolution trajectories (the `evolve` arrows on Till / POS, Tea Supplier Relationship, Sustainability Certification) are **scenarios, not forecasts**. Per Wardley's climatic pattern #18: *"you cannot measure evolution over time or adoption."* The map shows where components are now and plausibly where market forces are pulling them; it does not say when they'll arrive. A regulatory shock (certification standards), a new utility entrant (a consolidated POS-on-phone play), or a supply disruption (climate-driven tea yield collapse in Assam or Kenya) could rewrite any of these arrows in a year.

---

## Sources (for deep-placement research)

- [How to Choose the Best POS System for UK Coffee Shops in 2026 (Compared) — What Epos](https://www.whatepos.co.uk/how-to-choose-the-best-pos-system-for-uk-coffee-shops-in-2026-compared/)
- [4 Cheapest POS Systems for Small Businesses in UK (2026) — POSApt](https://posapt.co.uk/cheapest-pos-systems-uk/)
- [SumUp vs Square UK 2026 — WeTranxact](https://www.wetranxact.co.uk/sumup-vs-square-uk-comparison/)
- [Stripe Fees UK 2026: Complete Pricing Guide — wearefounders.uk](https://www.wearefounders.uk/stripe-fees-uk-2026/)
- [Credit card processing fees in the UK: a complete guide for 2026 — money.co.uk](https://www.money.co.uk/business/card-payment-solutions/credit-card-processing-fees)
- [Tea and Coffee Certification Schemes — Ethical Consumer](https://www.ethicalconsumer.org/food-drink/tea-coffee-certification-schemes)
- [United Kingdom's Tea Market Report 2026 — IndexBox](https://www.indexbox.io/store/the-united-kingdom-tea-market-analysis-forecast-size-trends-and-insights/)
- [Fairtrade Tea — Fairtrade UK](https://www.fairtrade.net/uk-en/products-and-producers/fairtrade-products/tea.html)
- [New tea trends for 2026 — Alveus](https://www.alveus.eu/blog/new-tea-trends/)
- [2026 Tea Trends — Royal New York](https://www.royalny.com/blogs/2026-tea-trends/)
- [5 Tea Trends Foodservice Operators Should Watch in 2026 — Gavina Coffee Solutions](https://www.gavinacoffeesolutions.com/5-tea-trends-in-foodservice-for-2024/)
- [Specialty Tea – The Yin to Coffee's Yang in the 3rd Wave — The Tea Spot](https://www.theteaspot.com/blogs/steep-it-loose/specialty-tea-the-yin-to-coffee-s-yang-in-the-3rd-wave)
