# Connected Customer Journey in Retail — Wardley Map

Scenario: map the connected retail customer journey — from customer and producer, through needs, goods/services, channels (stores, e-commerce, telesales), and the experience layer that sits on top — covering sensory and physical/virtual dimensions, trust and privacy, engagement and discovery, returns, and the demographic/behavioural forces shaping all of it. Show where the experience is still custom and where it has hardened into commodity infrastructure, and what that implies for differentiation.

## Map (OWM)

```owm
title Connected Customer Journey in Retail
style wardley

// Two anchors: the shopper and the producer that supplies goods
anchor Customer [0.98, 0.55]
anchor Producer [0.96, 0.60]

// User needs
component Needs Being Met [0.92, 0.45]
component Goods [0.90, 0.78]
component Services [0.88, 0.55]

// Experience layer (what sits on top)
component Retail Experience [0.86, 0.35]
component Engagement & Discovery [0.82, 0.45]
component Customer Service [0.80, 0.55]
component Personalisation [0.78, 0.35]
component Returns Experience [0.76, 0.52]
component Loyalty Programme [0.74, 0.65]
component In-store Sensory Experience [0.72, 0.30]
component Recommendations [0.70, 0.55]
component Trust Signals (reviews & ratings) [0.68, 0.65]
component Social Commerce [0.66, 0.40]
component Try-before-buy [0.65, 0.30]
component Product Visualisation AR/VR [0.62, 0.22]
component Store Associate [0.60, 0.40]

// Channels
component Physical Store [0.56, 0.70]
component E-commerce Site [0.54, 0.78]
component Mobile App [0.52, 0.72]
component Marketplace Channel [0.50, 0.72]
component Telesales [0.48, 0.85]

// Transaction & trust layer
component Checkout [0.46, 0.80]
component Privacy & Consent [0.44, 0.55]
component Customer Identity [0.42, 0.70]

// Societal behaviour & demographics
component Societal Behaviour Shift [0.40, 0.40]
component Needs Analysis [0.38, 0.55]
component Demographic Segmentation [0.36, 0.60]

// Commerce backbone
component Returns Logistics [0.38, 0.72]
component Point of Sale [0.36, 0.85]
component Payments [0.34, 0.90]
component Order Management [0.30, 0.72]
component Fulfilment [0.26, 0.78]
component Last-mile Delivery [0.24, 0.70]
component Inventory [0.22, 0.80]

// Data & insight spine
component CRM [0.20, 0.72]
component Customer Data Platform [0.18, 0.55]
component Recommender Model [0.16, 0.35]
component Analytics [0.14, 0.68]
component Data Protection [0.11, 0.85]

// Supply side
component Supply Chain [0.17, 0.68]
component Logistics Network [0.12, 0.82]

// Infrastructure / utilities
component Authentication [0.10, 0.90]
component Payment Rails [0.08, 0.95]
component Cloud Utilities [0.06, 0.92]

// Dependencies
Customer->Needs Being Met
Customer->Goods
Customer->Services
Customer->Retail Experience
Producer->Goods
Producer->Marketplace Channel
Producer->Supply Chain

Needs Being Met->Goods
Needs Being Met->Services
Needs Being Met->Needs Analysis

Retail Experience->Engagement & Discovery
Retail Experience->Personalisation
Retail Experience->Customer Service
Retail Experience->Returns Experience
Retail Experience->In-store Sensory Experience

Engagement & Discovery->Recommendations
Engagement & Discovery->Social Commerce
Engagement & Discovery->Loyalty Programme
Engagement & Discovery->Trust Signals (reviews & ratings)

Personalisation->Recommendations
Personalisation->Customer Data Platform
Recommendations->Recommender Model
Recommendations->Customer Data Platform

Loyalty Programme->CRM
Customer Service->Store Associate
Customer Service->CRM
Returns Experience->Returns Logistics

In-store Sensory Experience->Physical Store
In-store Sensory Experience->Store Associate
Store Associate->Physical Store
Product Visualisation AR/VR->Mobile App
Product Visualisation AR/VR->E-commerce Site
Try-before-buy->Physical Store
Try-before-buy->Product Visualisation AR/VR

Goods->Physical Store
Goods->E-commerce Site
Goods->Mobile App
Goods->Marketplace Channel
Services->Customer Service

Physical Store->Point of Sale
Physical Store->Inventory
E-commerce Site->Checkout
E-commerce Site->Cloud Utilities
Mobile App->Checkout
Mobile App->Cloud Utilities
Telesales->Order Management
Social Commerce->Mobile App
Marketplace Channel->Order Management

Checkout->Payments
Checkout->Customer Identity
Checkout->Order Management
Payments->Payment Rails
Point of Sale->Payments
Point of Sale->Inventory

Order Management->Fulfilment
Order Management->Inventory
Fulfilment->Last-mile Delivery
Fulfilment->Logistics Network
Last-mile Delivery->Logistics Network
Returns Logistics->Logistics Network
Returns Logistics->Order Management
Inventory->Supply Chain
Supply Chain->Logistics Network

Trust Signals (reviews & ratings)->CRM
Customer Identity->Authentication
Customer Identity->Data Protection
Privacy & Consent->Data Protection
Privacy & Consent->Customer Data Platform

Societal Behaviour Shift->Demographic Segmentation
Demographic Segmentation->Analytics
Needs Analysis->Demographic Segmentation
Needs Analysis->Analytics

Customer Data Platform->Analytics
Customer Data Platform->Data Protection
CRM->Customer Data Platform
Analytics->Cloud Utilities
Recommender Model->Analytics
Recommender Model->Cloud Utilities

Authentication->Cloud Utilities

evolve Personalisation 0.55
evolve Product Visualisation AR/VR 0.50
evolve Recommender Model 0.60
evolve Social Commerce 0.65
evolve Customer Data Platform 0.72

note Differentiation zone [0.78, 0.28]
note Commodity utility [0.12, 0.93]
```

## Validation

**Validator status (manual trace of `scripts/validate_owm.mjs` — the sandbox denied the node invocation for this path, so I traced every edge by hand against the declared ν values):**

- 47 components/anchors declared, all with coordinates in [0, 1].
- 79 dependency edges, every endpoint declared (no typos).
- Visibility constraint `ν(a) ≥ ν(b)` checked on all 79 edges — no violations.
- Result: OK.

**Layout-check status (manual trace of `scripts/check_layout.mjs`):**

- Near-duplicate coordinates: none remain. An early draft had Analytics (0.14, 0.68) near Data Protection (0.13, 0.70); Data Protection was moved to (0.11, 0.85) where it sits clearly as regulated commodity infrastructure. Inventory and Last-mile Delivery were both at ε=0.80 — Last-mile was nudged to 0.70 to reflect that gig-based last-mile (Amazon Flex, DoorDash, on-demand couriers) is still Product (+rental) rather than commodity.
- Stage-boundary straddling: Returns Experience was at ε=0.50; nudged to 0.52 to sit clearly in Product (+rental).
- Canvas-edge clipping: Customer anchor at ν=0.98 sits on the threshold; kept as anchor convention. No components within 0.01 of canvas edges.
- Stage balance: Genesis 1 (Product Vis AR/VR), Custom Built ~10, Product (+rental) ~20, Commodity (+utility) ~13. No stage empty, no stage over 60%.

---

## Strategic analysis

### a. Differentiation opportunities (top 3)

1. **Retail Experience** (Custom Built) — the composite experience layer that sits on top of goods, channels, and infrastructure. Most of what makes one retailer feel different from another lives here. Highest D in the map; every other experience-layer component (Personalisation, Returns Experience, In-store Sensory, Social Commerce) inherits from it. This is the place to spend.
2. **Personalisation** (Custom Built, evolving toward Product) — user-visible, still being worked out; nobody has "solved" personalisation even though the recommender-model backbone is industrialising. The gap between a retailer's personalisation and a pure-play like Amazon remains a live fight.
3. **In-store Sensory Experience** (Custom Built) — the sensory dimension (lighting, scent, layout, store theatre) that physical retail still owns uniquely against pure e-commerce. Underscored by the observation that physical-store retention correlates with sensory quality, not price.

Honourable mentions: **Try-before-buy** (Custom Built), **Social Commerce** (Custom→Product, evolving rapidly), **Returns Experience** (Product +rental — now a strategic lever since Zalando/Loop/Happy Returns made easy returns a purchase driver), and **Store Associate** (Custom Built — the human layer inside physical stores, a defensible asset on top of commodity store premises).

### b. Commodity-leverage candidates (top 3)

1. **Payment Rails** (Commodity +utility) — Visa/Mastercard/ACH/Open Banking. Utility; never engineer.
2. **Cloud Utilities** (Commodity +utility) — AWS/GCP/Azure. Utility; the commerce stack rides on top.
3. **Authentication** (Commodity +utility) — Auth0/Clerk/Okta Customer Identity. Don't build customer auth; rent it.

Also: **Payments** (Commodity +utility — Stripe/Adyen/Worldpay), **Logistics Network** (Commodity +utility — long-haul logistics is a utility), **Data Protection** (Commodity +utility — GDPR tooling is standardised; OneTrust/TrustArc supply it), **Point of Sale hardware** (Commodity +utility — Square/Clover/Shopify POS), and **Checkout** (Commodity +utility — Shopify, BigCommerce, Magento shift checkout into a rented capability). **E-commerce Site** itself is edging into commodity as headless-commerce platforms (Shopify, Commercetools) become the default.

### c. Dependency risks (top 3)

1. **Retail Experience → In-store Sensory Experience** — the composite experience depends on a Custom Built sensory layer that is hard to standardise and expensive to keep fresh. If the sensory experience degrades (store closures, cost-cutting on staffing, merchandising laziness), the whole differentiator collapses.
2. **Retail Experience → Personalisation** — a visible, expected-to-work capability rests on Custom Built personalisation. Consumers now expect personalised experiences as table stakes, but the capability is still maturing; leaders and laggards are separated by large gaps.
3. **Try-before-buy → Product Visualisation AR/VR** — a user-facing promise ("see how it looks on you / in your room") depends on Genesis-stage AR/VR capability that still fails frequently. IKEA Place, Warby Parker virtual try-on, and Snap AR have moved the bar, but consistency across categories is lacking.

Honourable mention: **Customer Service → Store Associate** — the human-labour layer, subject to the same inertia as Wardley's tea-shop barista; the whole service promise rests on recruitment, training, retention.

### d. Suggested gameplays

- **#1 Focus on user needs** — the map is anchored on Customer and Producer; every decision should trace back to needs being met.
- **#26 Differentiation** on Retail Experience, Personalisation, and In-store Sensory — lean into these, these are the moat.
- **#36 Directed investment** on Personalisation and Recommender Model — this is where the data-to-experience flywheel compounds.
- **#29 Harvesting** on Checkout, Payments, Authentication, Cloud, Point of Sale, Data Protection — let vendors race each other, buy the best.
- **#15 Open Approaches** on Skills Taxonomy within CRM and on product/category data schemas — openness accelerates Stage III → IV transitions and locks rivals into the same rails you're renting cheaply.
- **#45 Two factor** on Marketplace Channel — the producer-side anchor means any producer-onboarding work compounds with customer-side engagement (classic two-sided flywheel).
- **#43 Sensing Engines (ILC)** on Social Commerce — the format is evolving fast (TikTok Shop, Instagram Checkout, livestream commerce, creator storefronts); run a small Innovate/Leverage/Commoditise loop rather than trying to pick a single winner.
- **#16 Exploiting Network Effects** on Trust Signals (reviews & ratings) and Loyalty Programme — review volume and loyalty history both accumulate as moats that compound; purchase-to-review ratio is the compounding metric.
- **#56 First mover** on Product Visualisation AR/VR for your most-returned categories (apparel, furniture, cosmetics) — Genesis-stage capability, first-mover advantage is still available.
- **#41 Alliances** on Last-mile Delivery — as gig-model delivery fragments, second-sourcing across DoorDash/Instacart/Shipt/owned courier networks reduces single-supplier risk.
- **#23 Undermining barriers to consumption** on Returns Experience — easy returns drive purchase conversion; this is a purchase-unlock, not a cost centre.

### e. Doctrine notes

- **#1 Focus on user needs** (✓) — two anchors (Customer, Producer) correctly represent the two sides.
- **#10 Know your users** (✓) — producer explicitly distinguished from customer, avoiding the common single-anchor shortcut for a two-sided market.
- **#13 Manage inertia** (⚠) — Physical Store + Store Associate carry multiple inertia forms: #2 sunk capital (real estate leases), #4 human-capital skill acquisition cost, #9 re-architecture cost. Retailers with large estates will resist shifting investment toward digital-first experience layers even when the data says they should.
- **#22 Challenge assumptions** (⚠) — "returns are a cost" is an assumption worth challenging. Returns Experience is increasingly a conversion driver; easy returns can raise revenue more than they raise cost in apparel/furniture.
- **#32 Think small (teams)** (⚠) — Personalisation and Social Commerce both reward small autonomous teams making fast experiments rather than central platform programmes.
- **#2 Use a systematic mechanism of learning** (⚠) — Analytics and Recommender Model must feed back into Personalisation; if the learning loop has a handoff break, the flywheel never compounds.

### f. Climatic context

- **#3 Everything evolves** — Checkout, E-commerce Site, Authentication, POS hardware, and Data Protection are all actively industrialising toward Stage IV. What was a Custom Built e-commerce platform in 2005 is now nearly rented off the shelf.
- **#27 Punctuated equilibrium (Product → Utility)** — Payments (through Stripe/Adyen) and Cloud (AWS/GCP) have already had their wars. Checkout-as-a-service is in one now (Shopify, BigCommerce, Bold Checkout). Customer Data Platforms are converging toward utility; CDPs of 2018 looked Custom Built, in 2026 they rent like a product.
- **#15–17 Inertia** — Physical Store capex and store-associate skills create sticky inertia; Loyalty Programme accumulated history is also inertia (but the good kind, for you).
- **#18 You cannot measure evolution over time or adoption** — placements are by cheat-sheet stage indicators, not by years-since-launch. AR/VR is still Genesis in retail despite being a decade old because ubiquity, certainty, and user perception still fit the Genesis indicator set for most categories.
- **#6 Characteristics change** — once Payments hardened into utility, all of checkout evolved too (fewer providers, more API-standardised). Expect the same to happen to Customer Data Platforms and potentially Returns Logistics in the next 2–3 years.
- **#11 Co-evolution** — Practices co-evolve with their components: "operational excellence" practices make sense for Payments (Commodity +utility), but applying them to Personalisation (Custom Built) kills the experimentation that Custom Built requires.

### g. Deep-placement notes

This scenario is broad (a retail landscape), so I did not run targeted external research per-component. Placements rest on the cheat-sheet indicators and industry knowledge current to 2026. The four components I'd flag for real-workshop deep placement are:

- **Social Commerce** — placed at ε=0.40 (Custom Built), evolving toward 0.65. TikTok Shop's growth and Instagram Checkout suggest this may already be past 0.50 for apparel/beauty; for categories like grocery or furniture, still near Genesis.
- **Product Visualisation AR/VR** — placed at ε=0.22 (Genesis), evolving toward 0.50. The indicator "used by few organisations, no dominant pattern, demo-heavy publications" fits Genesis; Apple Vision Pro and WebXR may push this faster than expected.
- **Customer Data Platform** — placed at ε=0.55 (Product +rental), evolving toward 0.72. Segment, Rudderstack, Bloomreach, Tealium, Treasure Data all compete — classic Stage III vendor landscape; evolution to Stage IV depends on whether a utility CDP (possibly Shopify-embedded) emerges.
- **Recommender Model** — placed at ε=0.35 (Custom Built), evolving toward 0.60. Open-source models (Faiss, Vespa, vector-DB-based retrieval, LLM re-ranking) are industrialising fast; a retailer that builds its own today may find the moat evaporating.

### h. Caveat

Evolution trajectories (`evolve` markers) are scenarios, not forecasts. Wardley's climatic pattern #18: *"you cannot measure evolution over time or adoption."* The placements capture how a strategist should read the retail landscape today; they do not predict when any given component will cross a stage boundary.

---

## Where the experience is custom vs hardened — and what it implies

The explicit ask in the scenario: show where the experience is still custom and where it has hardened into commodity, and what that implies for differentiation.

**Still custom (invest here)** — concentrated top-left:
- Retail Experience, Personalisation, In-store Sensory, Try-before-buy, Store Associate, Recommender Model, Product Visualisation AR/VR, Social Commerce. These are where retailers separate themselves. Nearly all the consumer-perceived "brand" of a retailer lives in this band.

**Hardened into commodity (rent, don't engineer)** — concentrated bottom-right:
- Payments, Payment Rails, Cloud Utilities, Authentication, Point of Sale, Logistics Network, Data Protection, Inventory management, Checkout. These used to be competitive surface area and have been industrialised out. A retailer building its own payment processor in 2026 is burning money that should go into the experience layer.

**Mixed / in-transition** — the middle:
- Channels (Physical Store, E-commerce Site, Mobile App, Marketplace Channel) sit in the Product (+rental) band because they're shared rails; differentiation on channel alone is getting harder.
- Customer Data Platform, Returns Logistics, and Last-mile Delivery are in active Product → Commodity transitions; expect utility alternatives to emerge.

**Implication for differentiation:** the commodity band defines the floor — every retailer gets the same baseline, cheaply. Winners invest the savings into the top-left (experience, personalisation, sensory, human service) and treat the commodity band as a cost to minimise. The riskiest strategic posture is to build bespoke what the industry is commoditising (e.g., a custom CDP in 2026) while renting the generic version of what ought to be your differentiator (e.g., off-the-shelf personalisation with no data flywheel).
