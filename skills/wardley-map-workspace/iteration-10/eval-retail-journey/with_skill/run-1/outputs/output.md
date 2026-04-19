# Wardley Map — Modern Retail Customer Journey

**Scenario:** How customers move from an initial need through to purchase in modern retail; the actors (customer, producer, society) that shape the journey; the components (channels, price, convenience, experience) that enable or constrain it; and what is differentiating versus commoditising, with guidance on where friction is worth reducing.

---

## Map (OWM)

```owm
title Modern Retail Customer Journey
style wardley

// Anchors (three user types)
anchor Customer [0.99, 0.55]
anchor Producer [0.96, 0.55]
anchor Society [0.95, 0.45]

// User-facing journey steps (what the customer experiences)
component Need Trigger [0.92, 0.50]
component Discovery [0.88, 0.60]
component Consideration [0.85, 0.55]
component Purchase Decision [0.83, 0.60]
component Checkout [0.82, 0.78]
component Fulfilment [0.80, 0.70]
component Post-Purchase Support [0.78, 0.65]

// Channels (where the journey happens)
component Physical Store [0.75, 0.82]
component D2C Website [0.73, 0.78]
component Online Marketplace [0.72, 0.80]
component Mobile App [0.70, 0.80]
component Social Commerce [0.68, 0.60]
component Voice Commerce [0.62, 0.35]
component AR / Virtual Try-On [0.60, 0.45]

// Experience enablers (producer-controlled, user-visible)
component Product Content / Catalogue [0.68, 0.70]
component Pricing [0.66, 0.70]
component Reviews & Ratings [0.64, 0.72]
component Personalisation [0.62, 0.65]
component Loyalty Programme [0.60, 0.60]
component Convenience [0.84, 0.55]
component Customer Experience [0.86, 0.45]
component Brand [0.80, 0.50]

// Payment stack
component Payment Method Choice [0.58, 0.75]
component Buy Now Pay Later [0.55, 0.70]
component Payment Processing [0.40, 0.92]
component Card Networks [0.32, 0.94]
component Fraud Detection [0.45, 0.72]

// Fulfilment & logistics
component Last-Mile Delivery [0.55, 0.72]
component Click & Collect [0.52, 0.65]
component Returns Processing [0.50, 0.60]
component Warehouse / Fulfilment Centres [0.44, 0.75]
component Inventory / Stock Availability [0.40, 0.68]
component Logistics Carriers [0.35, 0.88]

// Discovery & intelligence
component Search [0.58, 0.85]
component Recommendation Engine [0.56, 0.65]
component Advertising / Paid Media [0.54, 0.78]
component Influencer / Creator Content [0.52, 0.55]
component Customer Data Platform [0.38, 0.60]
component Analytics [0.28, 0.80]

// Producer-side activities
component Merchandising [0.70, 0.55]
component Assortment Planning [0.48, 0.55]
component Supplier Relationships [0.38, 0.55]

// Infrastructure (commodity)
component Identity / Auth [0.28, 0.90]
component Email / SMS / Push [0.26, 0.90]
component CDN [0.22, 0.93]
component Database [0.18, 0.90]
component Cloud Compute [0.12, 0.92]

// Society-shaped constraints
component Trust [0.88, 0.40]
component Sustainability Expectations [0.34, 0.35]
component Consumer Protection Law [0.30, 0.60]
component Data Privacy Regulation [0.26, 0.55]

// Dependencies
Customer->Need Trigger
Customer->Discovery
Customer->Consideration
Customer->Purchase Decision
Customer->Checkout
Customer->Fulfilment
Customer->Post-Purchase Support
Customer->Customer Experience
Customer->Trust
Customer->Convenience

Producer->Brand
Producer->Customer Experience
Producer->Merchandising
Producer->Pricing
Producer->Product Content / Catalogue

Society->Consumer Protection Law
Society->Data Privacy Regulation
Society->Sustainability Expectations
Society->Trust

// Journey flow
Need Trigger->Discovery
Discovery->Consideration
Consideration->Purchase Decision
Purchase Decision->Checkout
Checkout->Fulfilment
Fulfilment->Post-Purchase Support

// Discovery channels
Discovery->Physical Store
Discovery->D2C Website
Discovery->Online Marketplace
Discovery->Mobile App
Discovery->Social Commerce
Discovery->Voice Commerce
Discovery->Advertising / Paid Media
Discovery->Influencer / Creator Content
Discovery->Search

// Consideration support
Consideration->Reviews & Ratings
Consideration->Product Content / Catalogue
Consideration->Pricing
Consideration->AR / Virtual Try-On
Consideration->Recommendation Engine
Consideration->Personalisation

// Purchase Decision
Purchase Decision->Pricing
Purchase Decision->Reviews & Ratings
Purchase Decision->Loyalty Programme
Purchase Decision->Inventory / Stock Availability

// Checkout
Checkout->Payment Method Choice
Checkout->Fraud Detection
Checkout->Identity / Auth
Payment Method Choice->Buy Now Pay Later
Payment Method Choice->Payment Processing
Payment Processing->Card Networks
Buy Now Pay Later->Payment Processing
Fraud Detection->Analytics

// Fulfilment chain
Fulfilment->Last-Mile Delivery
Fulfilment->Click & Collect
Fulfilment->Warehouse / Fulfilment Centres
Last-Mile Delivery->Logistics Carriers
Warehouse / Fulfilment Centres->Inventory / Stock Availability
Inventory / Stock Availability->Supplier Relationships

// Post-purchase
Post-Purchase Support->Returns Processing
Post-Purchase Support->Email / SMS / Push
Returns Processing->Logistics Carriers

// Channels depend on infra
Physical Store->Payment Processing
D2C Website->Cloud Compute
D2C Website->CDN
Online Marketplace->Cloud Compute
Mobile App->Cloud Compute
Mobile App->Identity / Auth
Social Commerce->Influencer / Creator Content
Social Commerce->Payment Processing
Voice Commerce->Identity / Auth
AR / Virtual Try-On->Cloud Compute

// Experience and brand
Customer Experience->Convenience
Customer Experience->Personalisation
Customer Experience->Brand
Customer Experience->Reviews & Ratings
Brand->Product Content / Catalogue
Convenience->Fulfilment
Convenience->Checkout

// Merchandising
Merchandising->Assortment Planning
Merchandising->Pricing
Merchandising->Product Content / Catalogue
Assortment Planning->Supplier Relationships

// Personalisation depends on data
Personalisation->Recommendation Engine
Recommendation Engine->Customer Data Platform
Customer Data Platform->Analytics
Customer Data Platform->Database
Analytics->Database

// Search & discovery infra
Search->Database
Search->Cloud Compute
Advertising / Paid Media->Analytics

// Identity, email infra
Identity / Auth->Database
Email / SMS / Push->Cloud Compute
CDN->Cloud Compute
Database->Cloud Compute

// Trust is shaped by constraints
Trust->Consumer Protection Law
Trust->Data Privacy Regulation
Trust->Reviews & Ratings
Trust->Brand

// Society shapes data handling
Personalisation->Data Privacy Regulation
Customer Data Platform->Data Privacy Regulation
Buy Now Pay Later->Consumer Protection Law
Brand->Sustainability Expectations

evolve AR / Virtual Try-On 0.60
evolve Voice Commerce 0.55
evolve Social Commerce 0.75
evolve Buy Now Pay Later 0.82
evolve Recommendation Engine 0.80

note Differentiation zone [0.75, 0.30]
note Utility / commodity [0.20, 0.92]
```

---

## Strategic analysis

### Reading the map (stage-first)

The journey splits cleanly into three horizontal bands.

**User-visible, still evolving (left-of-centre, top).** Customer Experience, Brand, Trust, Convenience, Need Trigger, Consideration, and the Society-shaped notion of Sustainability Expectations sit in Stage II (Custom Built) territory. These are the dimensions customers can feel but that no retailer has standardised. This is where the differentiating work happens.

**User-visible, fast-industrialising (centre and top-right).** Most of the operational journey — Discovery, Purchase Decision, Checkout, Fulfilment, Post-Purchase Support, the channels (Physical Store, D2C Website, Online Marketplace, Mobile App), and the experience enablers (Catalogue, Pricing, Reviews, Loyalty) — sits in Stage III (Product +rental). Customers now expect these to work; feature parity is assumed. Retailers compete on execution, not novelty.

**Deep, commoditised (bottom-right).** Payment Processing, Card Networks, Logistics Carriers, Identity / Auth, Email / SMS / Push, CDN, Database, and Cloud Compute are all Stage IV (Commodity +utility). Nobody should be building these.

**The interesting in-transition zone** contains three channels (Social Commerce, Voice Commerce, AR / Virtual Try-On) and two enablers (Recommendation Engine, Buy Now Pay Later) — these are the components that the deep-placement research (below) homed in on.

### a. Top 3 differentiation opportunities

1. **Customer Experience** (Custom Built) — the single most visible, least commoditised component on the map. Every retailer wrestles with it; nobody has productised it. The whole "convenience + trust + brand feel" bundle is where a retailer wins repeat custom. This is BUILD.
2. **Trust** (Custom Built) — visible at the anchor boundary, poorly understood in aggregate. A retailer who compounds trust through consistent returns, honest reviews, and visible privacy practices creates a moat the commodity channels cannot replicate.
3. **AR / Virtual Try-On** (Custom Built → Product) — still early and unevenly adopted (~$12B market, vendors like Zalando, Adidas, Macy's piloting, Gartner forecasting 80% brand adoption). High visibility for the Consideration step in fashion, furniture, cosmetics. Investment window is open for the next 18–24 months before it becomes table-stakes Stage III.

### b. Top 3 commodity-leverage candidates

1. **Cloud Compute, CDN, Database** (Commodity +utility) — collapse as a group. Rent from AWS/GCP/Cloudflare. Any engineering effort here is misallocated.
2. **Payment Processing + Card Networks** (Commodity +utility) — use Stripe/Adyen/Checkout.com. Do not engineer.
3. **Logistics Carriers** (Commodity +utility) — outsource to DHL/Royal Mail/UPS/DPD, or to aggregators (ShipBob, Shippo). Invest only in the *orchestration layer* on top, not the carrier itself. Similarly Identity / Auth and Email / SMS / Push (Clerk, Auth0, Twilio, Postmark) are utilities.

### c. Top 3 dependency risks

1. **Checkout → Fraud Detection** — Checkout is the highest-value user-visible step; Fraud Detection is still early Product (+rental) and in many retailers is home-rolled. If fraud rules misfire, checkout rejects legitimate customers (the single most expensive journey failure). Buy or rent a mature provider (Sift, Signifyd, Stripe Radar) rather than hand-building.
2. **Personalisation → Data Privacy Regulation** — personalisation is a key differentiator but its legal foundation (GDPR, UK DPA, state laws, upcoming AI Act provisions) is actively tightening. A retailer building personalisation on consent mechanics that will not survive 2026–2027 regulation is accumulating re-work debt.
3. **Buy Now Pay Later → Consumer Protection Law** — BNPL is user-visible and commercially important (~20%+ of sales in some categories), but from 15 July 2026 the UK FCA regulates it as Deferred Payment Credit, and New York and EU rules are following. Retailers with BNPL woven tightly into checkout flow will need compliance retrofits; plan the redesign now.

### d. Suggested gameplays

- **#1 Focus on user needs** — three anchors (Customer, Producer, Society) is already applying this; the analysis is grounded in what the customer is trying to do, not what the retailer wants to sell.
- **#36 Directed investment** — on Customer Experience, Convenience, Trust, and AR / Virtual Try-On. These are the Custom Built components closest to the user. Concentrate engineering there.
- **#26 Differentiation** — lean into brand, service, sustainability narrative. For commodity categories (grocery, essentials), differentiation is primarily Convenience; for considered purchases (fashion, home, electronics), it is Experience + AR + Reviews.
- **#29 Harvesting** — on the commodity utility layer: let Stripe/Adyen win payments, let Twilio win messaging, let AWS win compute, let Sift/Signifyd win fraud. Do not compete.
- **#41 Alliances** — for Last-Mile Delivery, carrier aggregation deals plus a click-and-collect partnership (e.g., parcel-locker networks) widen Convenience without capex.
- **#43 Sensing Engines (ILC)** — use the Customer Data Platform to detect which nascent channel (Social Commerce, Voice Commerce, AR) is breaking out; Innovate → Leverage → Commoditise internally.
- **#45 Two factor** — for retailers running marketplace-style commerce (third-party sellers), this is the defining play.
- **#15 Open Approaches** — for Product Content / Catalogue (adopt shared feed standards such as GS1, schema.org Product) to let social commerce and AR vendors ingest without bespoke integrations.
- **#56 First mover** — on UK BNPL compliance (July 2026 FCA deadline) and on EU AI Act personalisation disclosures. Regulatory deadlines create a narrow window where compliant retailers win trust.
- **#16 Exploiting Network Effects** — on Reviews & Ratings and Loyalty Programme. Both compound with accumulated history.

### e. Doctrine notes

- **Doctrine #1 Focus on user needs** — satisfied; journey is anchored on the customer.
- **Doctrine #10 Know your users** — satisfied with three anchors. The Society anchor is unusual but defensible: regulators and sustainability norms shape the space customers operate in, and pretending they do not is a common mapping error in retail.
- **Doctrine #13 Manage inertia** — real risk here. Physical Store (sunk capital, skills), legacy POS, long-running supplier contracts, and loyalty programmes that customers already depend on all create inertia (forms #2 sunk capital, #4 skill capital, #8 skill acquisition cost, #14 strategic-control loss). Any channel-shift strategy must budget for these.
- **Doctrine #2 Use a systematic mechanism of learning** — partly violated if the Customer Data Platform is treated as a reporting tool rather than a closed-loop learning system. The Recommendation Engine should feed outcomes back to training.
- **Doctrine #34 Think small (as in teams)** — relevant for AR / Virtual Try-On; ship with a small focused team before the category industrialises.

### f. Climatic context

The map is being shaped by at least six of Wardley's 27 climatic patterns:

- **#3 Everything evolves** — every channel on this map is at a different point on its own curve, which is why the map has a wide stage distribution.
- **#15–17 Inertia** — physical store footprints, ingrained customer habits, and legacy merchandising processes slow the migration into Stage III/IV channels.
- **#18 You cannot measure evolution over time or adoption** — the `evolve` targets below are scenarios, not forecasts (see caveat).
- **#20 Higher-order systems create new sources of worth** — Social Commerce, AR, and voice each sit on top of mature commerce infra and create new value that pure e-com could not.
- **#23 Efficiency enables innovation** — commodity cloud/payments/logistics is *why* retailers can now afford to run AR pilots; the utility layer funds the experimental layer.
- **#27 Product-to-utility punctuated equilibrium ("war")** — Recommendation Engine and Buy Now Pay Later are both in this transition right now. BNPL in particular is on the Stage III → IV cliff driven by regulation plus the maturity of Affirm/PayPal/Klarna infrastructure.

### g. Deep-placement notes

Five components were flagged for targeted research (Step 4.5). Findings:

- **Social Commerce** — initial cheat-sheet put it at roughly 0.50 (late Custom Built). Research showed US social commerce is projected at $101B in 2026 (7.2% of e-commerce), Meta controls ~52%, TikTok Shop is growing 87% YoY with $23.4B US GMV and a 4.7% conversion rate. Multiple mature vendors, rapidly-increasing consumption, buyer expectations forming — that is unambiguously Stage III (Product +rental). Shifted to **0.60** and set `evolve` target at 0.75 (edge of Commodity) reflecting the velocity.
- **Buy Now Pay Later** — initial cheat-sheet at roughly 0.55 (early Product +rental). Research: Affirm, PayPal Pay Later, Klarna, Afterpay are the concentrated set; GMV growth decelerating (27% → 19% → 14%); UK FCA regulates BNPL as Deferred Payment Credit from 15 July 2026; New York state law enacted; EU tightening. Regulation is a classic Stage III → IV signal. Placed at **0.70** and `evolve` target 0.82 — regulation-driven industrialisation will push it to commodity within 24 months.
- **Recommendation Engine / AI Personalisation** — initial cheat-sheet at roughly 0.55 (late Custom Built). Research: eight-plus major vendors (Algolia, Bloomreach, Coveo, Dynamic Yield, Constructor, Experro, Nosto, Optimizely), 2026 Gartner Magic Quadrant has multiple Leaders, personalisation is 33% of the AI-in-retail segment by revenue. Feature parity emerging, implementation is the differentiator. Placed at **0.65** (mid Product +rental) with `evolve` 0.80. Still leaves room for IP-level differentiation in the ranking models, but the category itself is not novel.
- **AR / Virtual Try-On** — initial cheat-sheet at roughly 0.35 (mid Custom Built). Research: $12B 2025 → $15B 2026 market; Gartner forecasts 80% retail brand adoption; Zalando, Net-a-Porter, ASOS, Macy's, Adidas, Warby Parker all running production AR; vendor ecosystem forming but not consolidated. Multiple case studies plus growing consumption puts it at the Custom Built → Product boundary. Placed at **0.45** with `evolve` target 0.60 — expect this to be Stage III within 18–24 months. Widened the uncertainty range in prose: still a differentiation bet for the next year, commoditising fast after that.
- **Voice Commerce** — initial cheat-sheet at roughly 0.35 (mid Custom Built). Research: 35.7% of US adults use voice for some shopping activity but only 11.3% complete purchase by voice; Alexa is the only assistant that directly completes transactions; grocery and household skew dominates (38%). Adoption is real but thin; the "exciting / surprising" user perception still holds for full checkout. Kept at **0.35** (Custom Built, with Genesis tail for the full-purchase use case) and `evolve` target 0.55 — slower curve than AR because of the voice-first UX problem, not the tech. Lowest-priority bet of the five.

### h. Caveat

Evolution positions (the `evolve` targets above) are **scenarios, not forecasts**. Wardley's climatic pattern #18 stands: *"you cannot measure evolution over time or adoption."* The numerical ε values here are seeds for judgement, not verdicts — stages and relative ranks are what matter for strategy. The research cited above reflects conditions observable in early 2026; real placements will depend on the retailer's specific market, geography, and customer segment.

---

## Validator output

```
OK: 54 components/anchors, 102 edges — no violations.
```

Ran the bundled validator (`scripts/validate_owm.py`) against the draft OWM block. Initial run flagged 10 visibility violations (inventory/warehouse ordering, convenience above checkout, CDN/DB above cloud, society constraints above the components using them, and merchandising above its artifacts). All fixed by re-ordering ν coordinates; validator clean on rerun.

---

## Where friction is worth reducing (direct answer to the question)

Ranked, from highest payoff to lowest:

1. **Checkout friction** — fraud false-positives, forced account creation, card-network failures, BNPL compliance friction. Every point of checkout abandonment is money on the floor. Buy mature fraud tooling, buy BNPL compliance now, remove forced-signup.
2. **Returns friction** — a bad returns experience kills lifetime value even if the purchase went well. Click-and-collect returns, pre-printed labels, drop-off networks are all Stage III; adopt them.
3. **Discovery-to-consideration friction** — especially for considered purchases: Reviews and AR / Virtual Try-On reduce uncertainty and move customers faster. Invest here.
4. **Personalisation-to-privacy friction** — customers want relevance but distrust surveillance. A visible, clean consent UX plus a narrower, better-consented data footprint is both a trust moat and regulatory insurance.
5. **Channel-switching friction** — customers treat retailer as one brand across store/web/app/social; they resent re-authentication, missing basket, unclear price parity across channels. Unified identity, basket, and price state is the single most important cross-channel investment.

Deliberately *not* worth reducing: friction that exists to protect the customer (two-factor auth on high-value orders, consent confirmations, returns identity checks). Friction removal is not a universal good — strategic friction *is* the trust signal.
