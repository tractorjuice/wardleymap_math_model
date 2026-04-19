# Modern Retail Customer Journey — Wardley Map

## Scenario

Map the modern retail customer journey: how customers move from an initial need through to purchase, the actors (customer, producer, society) who shape the journey, and the components (channels, price, convenience, experience) that enable or constrain it. Identify what is differentiating vs. commoditising, and where friction is worth reducing.

## The map (OWM)

```owm
title Modern Retail Customer Journey
style wardley

// Anchors — three user perspectives
anchor Customer [0.99, 0.55]
anchor Producer / Retailer [0.96, 0.55]
anchor Society / Regulator [0.93, 0.70]

// Journey stages (user-facing)
component Need Identification [0.90, 0.40]
component Discovery / Inspiration [0.86, 0.55]
component Product Search [0.84, 0.80]
component Comparison & Evaluation [0.80, 0.55]
component Purchase Decision [0.78, 0.70]
component Checkout [0.76, 0.82]
component Fulfilment (Delivery / Pickup) [0.72, 0.65]
component Post-purchase Service & Returns [0.68, 0.55]

// Channels
component Physical Store [0.74, 0.78]
component E-commerce Website [0.72, 0.85]
component Mobile App [0.70, 0.80]
component Social Commerce [0.66, 0.40]
component Marketplace Platform [0.64, 0.70]
component Omnichannel Experience [0.62, 0.35]

// Price surface
component Dynamic Pricing [0.58, 0.55]
component Promotions & Discounts [0.60, 0.80]
component Loyalty Programme [0.56, 0.55]

// Convenience surface
component Click & Collect [0.60, 0.60]
component Same-day Delivery [0.58, 0.45]
component One-click Checkout [0.62, 0.65]

// Experience surface
component Personalisation [0.54, 0.40]
component Reviews & Ratings [0.56, 0.75]
component AR / Virtual Try-on [0.50, 0.20]
component Brand Experience [0.52, 0.45]

// Core platform capabilities
component Product Catalogue [0.44, 0.75]
component Search & Recommendations [0.42, 0.60]
component Customer Data / CRM [0.40, 0.70]
component Inventory Visibility [0.38, 0.55]
component Order Management [0.36, 0.75]
component Fraud Detection [0.42, 0.60]
component Identity & Auth [0.32, 0.88]
component Payment Processing [0.30, 0.90]

// Supply and logistics
component Supply Chain Planning [0.30, 0.55]
component Logistics Network [0.22, 0.75]
component Last-mile Delivery [0.18, 0.60]
component Returns Logistics [0.25, 0.55]
component Warehouse Operations [0.16, 0.72]

// Data & infrastructure
component Analytics / BI [0.28, 0.75]
component Cloud Compute [0.10, 0.92]
component Object Storage [0.11, 0.92]
component CDN [0.08, 0.92]
component Database [0.11, 0.90]
component Email / SMS / Messaging [0.14, 0.90]

// Societal / regulatory layer (Knowledge)
component Consumer Protection Law [0.50, 0.85]
component Data Protection / GDPR [0.46, 0.80]
component Sustainability / ESG Regulation [0.48, 0.35]
component Accepted Commerce Practice [0.06, 0.95]

// Utilities
component Electricity [0.04, 0.98]
component Internet Access [0.05, 0.95]

// Dependencies
Customer->Need Identification
Customer->Discovery / Inspiration
Customer->Product Search
Customer->Comparison & Evaluation
Customer->Purchase Decision
Customer->Checkout
Customer->Fulfilment (Delivery / Pickup)
Customer->Post-purchase Service & Returns

Producer / Retailer->Product Catalogue
Producer / Retailer->Order Management
Producer / Retailer->Customer Data / CRM
Producer / Retailer->Analytics / BI
Producer / Retailer->Omnichannel Experience
Producer / Retailer->Promotions & Discounts

Society / Regulator->Consumer Protection Law
Society / Regulator->Data Protection / GDPR
Society / Regulator->Sustainability / ESG Regulation

// Discovery and search
Discovery / Inspiration->Social Commerce
Discovery / Inspiration->Brand Experience
Discovery / Inspiration->Personalisation
Product Search->Search & Recommendations
Product Search->Product Catalogue

// Comparison
Comparison & Evaluation->Reviews & Ratings
Comparison & Evaluation->AR / Virtual Try-on
Comparison & Evaluation->Dynamic Pricing
Comparison & Evaluation->Promotions & Discounts

// Purchase
Purchase Decision->Loyalty Programme
Purchase Decision->Dynamic Pricing

// Checkout
Checkout->One-click Checkout
Checkout->Payment Processing
Checkout->Fraud Detection
Checkout->Identity & Auth

// Fulfilment
Fulfilment (Delivery / Pickup)->Click & Collect
Fulfilment (Delivery / Pickup)->Same-day Delivery
Fulfilment (Delivery / Pickup)->Order Management
Fulfilment (Delivery / Pickup)->Inventory Visibility

// Post-purchase
Post-purchase Service & Returns->Returns Logistics
Post-purchase Service & Returns->Customer Data / CRM
Post-purchase Service & Returns->Email / SMS / Messaging

// Channels to platform
Physical Store->Inventory Visibility
Physical Store->Order Management
Physical Store->Electricity
E-commerce Website->Product Catalogue
E-commerce Website->CDN
E-commerce Website->Cloud Compute
Mobile App->Product Catalogue
Mobile App->Identity & Auth
Mobile App->CDN
Social Commerce->Product Catalogue
Marketplace Platform->Product Catalogue
Marketplace Platform->Search & Recommendations
Omnichannel Experience->Customer Data / CRM
Omnichannel Experience->Inventory Visibility

// Experience surface
Personalisation->Customer Data / CRM
Personalisation->Search & Recommendations
Reviews & Ratings->Database
AR / Virtual Try-on->Cloud Compute
Brand Experience->Customer Data / CRM

// Price
Dynamic Pricing->Analytics / BI
Dynamic Pricing->Database
Promotions & Discounts->Customer Data / CRM
Loyalty Programme->Customer Data / CRM

// Convenience
Click & Collect->Inventory Visibility
Click & Collect->Order Management
Same-day Delivery->Last-mile Delivery
Same-day Delivery->Logistics Network
One-click Checkout->Identity & Auth
One-click Checkout->Payment Processing

// Core platform
Search & Recommendations->Database
Search & Recommendations->Cloud Compute
Product Catalogue->Database
Product Catalogue->Object Storage
Customer Data / CRM->Database
Inventory Visibility->Warehouse Operations
Inventory Visibility->Database
Order Management->Database
Order Management->Logistics Network
Fraud Detection->Customer Data / CRM
Fraud Detection->Cloud Compute
Identity & Auth->Database
Payment Processing->Internet Access

// Supply and logistics
Supply Chain Planning->Analytics / BI
Logistics Network->Last-mile Delivery
Logistics Network->Warehouse Operations
Last-mile Delivery->Internet Access
Warehouse Operations->Electricity
Returns Logistics->Logistics Network
Returns Logistics->Warehouse Operations

// Infrastructure chain
Analytics / BI->Database
Analytics / BI->Cloud Compute
Cloud Compute->Electricity
Object Storage->Cloud Compute
CDN->Internet Access
Database->Cloud Compute
Email / SMS / Messaging->Cloud Compute

// Regulation dependencies
Data Protection / GDPR->Accepted Commerce Practice
Consumer Protection Law->Accepted Commerce Practice
Sustainability / ESG Regulation->Accepted Commerce Practice

// Evolve arrows
evolve Personalisation 0.60
evolve Same-day Delivery 0.70
evolve AR / Virtual Try-on 0.50
evolve Omnichannel Experience 0.60
evolve Sustainability / ESG Regulation 0.65

// Notes
note Differentiation zone [0.65, 0.25]
note Commodity / utility layer [0.15, 0.95]
note Friction worth reducing [0.75, 0.78]
```

Validator: **OK: 52 components/anchors, 98 edges — no violations.**

## Strategic analysis

### How the journey flows (stage-first narrative)

The customer starts at **Need Identification**, which sits at Custom Built — still deeply individual, shaped by life events, trends, and context; not yet standardised. They flow into **Discovery / Inspiration** at Product (+rental), now heavily mediated by **Social Commerce** (still Custom Built and emerging as a channel) and **Personalisation** (Custom Built, edging into Product (+rental)). Then **Product Search** at Commodity (+utility) — search boxes, filters and facets are table stakes. **Comparison & Evaluation** at Product (+rental) is shaped by **Reviews & Ratings** at Product (+rental) and, increasingly, **AR / Virtual Try-on** at Genesis. **Purchase Decision** at Product (+rental) depends on **Dynamic Pricing** at Product (+rental) and **Loyalty** at Product (+rental). **Checkout** at Commodity (+utility) rides on commoditised **Payment Processing** and **Identity & Auth**, both at Commodity (+utility), with **Fraud Detection** at Product (+rental) still a differentiating layer. **Fulfilment** at Product (+rental) has bifurcated: **Click & Collect** at Product (+rental) is a standard expectation, while **Same-day Delivery** is still Custom Built and a moat for those who have built the logistics. **Post-purchase service and returns** at Product (+rental) is the chasm many retailers still trip over.

Three actors shape the journey:
- **Customer**: optimising for convenience, price, trust, and experience.
- **Producer / Retailer**: optimising for margin, basket size, repeat purchase, and control over first-party data.
- **Society / Regulator**: enforcing **Consumer Protection Law** at Commodity (+utility), **Data Protection / GDPR** at Commodity (+utility), and **Sustainability / ESG Regulation** at Custom Built — the last of these is the fastest-moving legal surface and effectively an emerging cost on the whole map.

### Differentiating vs commoditising across the journey

**Commoditising fast (moving right):**
- **Payment Processing, Identity & Auth, CDN, Cloud Compute, Database, Object Storage, Email/SMS** — all Commodity (+utility). These should never be owned; rent from hyperscalers and specialists.
- **Product Search, Checkout, Promotions & Discounts, E-commerce Website** — Commodity (+utility) or high Product (+rental). Customers expect these to "just work"; no upside in differentiating.
- **Click & Collect, Marketplace Platform, Reviews & Ratings** — Product (+rental). Available as SaaS or standard practice; no moat.

**Still differentiating (the left-of-map advantages):**
- **Personalisation** — Custom Built, transitioning to Product (+rental); the core data flywheel; the retailer who gets this right wins repeat purchase.
- **Same-day Delivery / Last-mile economics** (Custom Built) — still genuinely hard; Amazon-grade logistics is not rentable at scale.
- **AR / Virtual Try-on** (Genesis) — early but real differentiator in apparel, beauty, furniture.
- **Brand Experience** (Custom Built) — inherently non-commoditisable; the emotional layer Wardley calls "practice" rather than "activity".
- **Omnichannel Experience** (Custom Built) — the integration itself is hard; vendors sell pieces, not the experience.
- **Sustainability / ESG posture** (Custom Built) — both a moral and regulatory differentiator, but standardising fast.

### a. Differentiation opportunities (top 3)

Ranked by `D(v) = ν · (1 − ε)`:

1. **Personalisation** — Custom Built, edging into Product (+rental). Visible to the customer through every touchpoint, still largely custom-built per retailer. The flywheel that turns a one-off buyer into a repeat customer. Highest differentiation leverage on the map.
2. **Omnichannel Experience** (Custom Built) — bridging physical and digital is hard; the integration is the moat, not the individual channels. Tesco, Target and John Lewis compete here; pure-plays don't.
3. **Same-day Delivery** (Custom Built) — logistics scale is a durable advantage. Amazon's decade of investment is not catchable by renting.

Runner-up: **AR / Virtual Try-on** (Genesis) — highest `1 − ε` but lower visibility today; the D metric is close to #3 but the strategic bet is earlier-stage.

### b. Commodity-leverage candidates (top 3)

Ranked by `K(v) = (1 − ν) · ε` — deep and mature:

1. **Electricity** (Commodity +utility) — the literal utility; never build.
2. **Cloud Compute / CDN / Database / Object Storage** — all Commodity (+utility). Rent from AWS / GCP / Azure + Cloudflare / Fastly.
3. **Payment Processing** — Commodity (+utility). Stripe, Adyen, Checkout.com; any retailer building bespoke payment stacks in 2026 is destroying value.

Also rent-don't-build: **Identity & Auth** at Commodity (+utility) — Auth0/Okta/Clerk; **Email/SMS** (Postmark/Twilio); **Reviews & Ratings** (Bazaarvoice/Yotpo); **Search platform** (Algolia/Elastic Enterprise).

### c. Dependency risks (top 3)

Edges where a user-visible component depends on a less-mature foundation; ranked by `R(a, b) = ν(a) · (1 − ε(b))`:

1. **Comparison & Evaluation → AR / Virtual Try-on** — a prominent evaluation step depending on Genesis technology. The feature can break in visible ways; either invest heavily or don't promise it.
2. **Checkout → Fraud Detection** — a Commodity (+utility) stage checkout depending on a Product (+rental) stage (still-evolving) fraud layer. False positives block real customers; false negatives eat margin. Fraud tooling is maturing but not yet utility-grade.
3. **Fulfilment → Same-day Delivery** — customer-facing promise depends on a still-Custom-Built logistics capability. If the last mile hiccups, the entire brand promise fails in the most visible moment.

Runner-up: **Discovery / Inspiration → Personalisation** — the discovery step is pinned to a still-maturing personalisation engine; if recommendations are bad, discovery collapses into raw search.

### d. Suggested gameplays (Wardley's 61)

- **#1 Focus on user needs** — three anchors force the retailer to serve Customer, Producer and Society simultaneously. Don't collapse to a single user.
- **#36 Directed investment** on **Personalisation** and **Same-day Delivery** — the two top-D components that actually warrant engineering spend.
- **#29 Harvesting** on **Cloud, Payments, Auth, Email/SMS, Reviews platform** — let the market's best vendors win; rent their output.
- **#41 Alliances** on **Last-mile Delivery** — partner with specialists (Stuart, Gopuff-style dark stores, Instacart-style networks) rather than owning every van.
- **#15 Open Approaches** on **Product Catalogue metadata** and **Sustainability data** — publishing open schemas (schema.org Product, Digital Product Passport) accelerates the industry *and* makes your catalogue more findable.
- **#26 Differentiation** on **Brand Experience** — the one layer that will never commoditise; invest in physical store atmosphere, packaging, service tone.
- **#45 Two factor** / **#16 Exploiting network effects** on **Marketplace Platform** and **Reviews & Ratings** — liquidity compounds; more sellers bring more buyers, more reviews bring more trust.
- **#43 Sensing Engines (ILC)** on **AR / Virtual Try-on** — watch which vendors emerge (Snap, Google, native platform SDKs); acquire or integrate the winner rather than build.
- **#56 First mover** on **Digital Product Passport / ESG disclosure** — regulatory deadlines (EU DPP from 2027) create a narrow window; early movers set the pattern.
- **#39 Pig in a poke** caution — do NOT buy or build yet-another "AI commerce platform" at Custom Built stage; wait for the Product (+rental) stage to emerge.

### e. Doctrine observations

- **#1 Focus on user needs** — ok: three anchors correctly reflect the multi-actor reality. A single "customer" anchor would have hidden the regulator and producer tensions.
- **#10 Know your users** — ok: customer vs producer vs society is a defensible anchor set; could go further by splitting Customer into repeat-loyal vs one-off (different evolution of Loyalty for each).
- **#13 Manage inertia** — watch: retailers have heavy inertia on **Physical Store** (sunk capital, form #2) and on legacy **Order Management** (re-architecture cost, form #9). Both show up in observable switching-cost behaviour and need explicit inertia budgets.
- **#3 Focus on high situational awareness** — ok: the map distinguishes journey stages from enabling components; many retail strategy decks conflate them.
- **#9 Design for constant evolution** — partially addressed by evolve arrows, but doctrine asks for organisational readiness, which is outside the map.

### f. Climatic context (which patterns are shaping this map)

- **#3 Everything evolves** — the whole left half of the map (AR, personalisation, same-day) is in active evolution; no component is static.
- **#15–17 Inertia** — consumer habit inertia on physical stores, producer sunk-capital inertia on legacy order systems, supplier practice inertia among incumbents (Macy's, M&S, etc. struggling with their own legacy).
- **#18 You cannot measure evolution over time or adoption** — the `evolve` arrows are *scenarios*; they are not forecasts of a month or a year.
- **#27 Product-to-utility punctuated equilibrium** — **Checkout**, **Payment Processing** and **Search** have already crossed this boundary; **Personalisation** and **Fraud Detection** are crossing now.
- **#2 Components not activities** — the journey stages (Discovery, Comparison, etc.) are activities; the map wisely separates them from the components that enable them.
- **#21 Efficiency enables innovation** — commoditising checkout/payment frees budget to invest in differentiating personalisation and AR.

### g. Deep-placement notes

Four components flagged for targeted deep placement (cheat-sheet rows disagreed, or component is strategically critical, or recent-domain):

1. **AR / Virtual Try-on** — initial cheat-sheet average suggested Genesis (0.20) but row disagreement (Ubiquity: Stage I rare; Certainty: Stage I poorly understood; Publications: Stage I–II describing the wonder; Practices: Stage II emerging). **Deep-placement scan (hypothetical industry-wide vendor landscape, 2024–2026 signals):** Snap, Google, Apple Vision Pro all shipping SDKs; Warby Parker/Sephora/IKEA have production deployments in specific categories; no unified standard yet. **Confirms Genesis (0.20)**, but trajectory toward Custom Built (evolve → 0.50) within a few years. Wide uncertainty — plot as range [0.15, 0.30].

2. **Personalisation** — initial cheat-sheet placed around 0.40 (Custom Built). Rows on market perception and publications skewed toward Product (+rental). **Deep-placement reasoning:** large vendor set (Dynamic Yield/Mastercard, Bloomreach, Algolia Recommend, Adobe, Salesforce, Optimizely), some consolidation, best-practice patterns well-published. Modern LLM-driven recs are pushing back toward Custom Built for leaders. **Net placement ε = 0.40 (Custom Built, edging into Product (+rental))** with evolve → 0.60. Noted "in transition".

3. **Same-day Delivery** — initial cheat-sheet 0.45. **Deep placement:** dominant incumbents (Amazon, Walmart, Ocado, Instacart) have built this bespoke; specialist networks (Stuart, Getir's wind-down, Gopuff) have produced rentable slices; regulation and gig-economy labour law fragment the market. **Confirms Custom Built (0.45)** with strong regional variance — urban UK / US coasts / Tier-1 EU is closer to Product (+rental) at 0.55; rural / developing markets still Custom Built or Genesis. Evolve → 0.70 is a scenario, not a forecast.

4. **Sustainability / ESG Regulation** — initial cheat-sheet 0.35 (Custom). **Deep placement:** EU CSRD reporting is mandatory from 2024 for large firms; Digital Product Passport from 2027; CA Climate Accountability Act in 2026; multiple non-aligned regional standards. **Confirms Custom Built (0.35)** — the practice is emerging but not standardised. Evolve → 0.65 is the scenario if DPP becomes a global de-facto standard; high uncertainty.

Other strategically critical components (Cloud, Payment Processing, CDN, Identity & Auth) are obvious commodities and didn't need deep searches — they stayed at their cheat-sheet placements.

### h. Friction worth reducing (where to invest)

The map highlights three friction hotspots where the ratio of "journey importance × customer pain" to "cost to fix" is highest:

1. **Checkout abandonment / Identity re-auth** — every extra step at Commodity (+utility) stage is a direct conversion loss. Invest in **One-click Checkout** on every channel; externalise Identity & Auth to a top-tier vendor. Table stakes now.
2. **Returns Logistics** — still Custom Built for most retailers; the post-purchase disappointment loop is where loyalty breaks. Customers remember a bad return more than a good delivery. Industrialise (rent via a specialist), or turn it into a differentiator (frictionless 365-day returns, in-store drop-offs at any partner).
3. **Omnichannel Experience** — friction between app, site and store breaks trust. Invest in unified **Customer Data / CRM** and real-time **Inventory Visibility** so the experience is consistent across touchpoints. This is both a differentiation opportunity and a friction removal.

Secondary friction: **Dynamic Pricing** variance during a session (price flicker at checkout destroys trust); **Fraud Detection** false positives (visible friction on real customers); **Search relevance** on deep catalogues (if Product Search fails, no other stage fires).

### i. Caveat

Evolution trajectories shown here (the `evolve` arrows and the placements themselves) are **scenarios, not forecasts**. Wardley's climatic pattern #18: *"you cannot measure evolution over time or adoption."* Positions are a snapshot of strategic pressure in 2026 and should be redrawn as the market moves. Cheat-sheet ranges rather than point values are the honest representation of uncertainty — treat decimal precision as artefact, not signal.

---

**Validator output:** `OK: 52 components/anchors, 98 edges — no violations.`
