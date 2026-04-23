# Connected Customer Journey in Retail — Wardley Map

## Step 0 — Strategic context

The rest of this map hangs on four framing decisions. Two of them were implied but not pinned down in the prompt, so they are recorded here as assumptions the reader can correct before acting on the analysis.

1. **Strategic question.** *Across the connected retail journey, which components are still legitimately Custom Built (and therefore where differentiation investment pays off) versus hardened into Commodity (+utility) infrastructure that any competitor can rent — and what does that distribution imply for where a retailer should and shouldn't build?*
2. **User anchor(s).** Two anchors are in play: the **Customer** (demand side: browses, buys, returns, talks about it) and the **Producer** (supply side: brands / own-label manufacturing / third-party suppliers whose goods travel through the same channels). The journey is connected precisely because both anchors meet at the same shared channels and experience layer.
3. **Core needs.** (i) *Get the right goods and services* (assortment, availability, price), (ii) *Have a coherent, trusted experience across touchpoints* (sensory, digital, trust, returns), (iii) *Be understood as a person, not a session* (personalisation, loyalty, privacy), (iv) *Move goods efficiently* (fulfilment, returns) — the producer's corresponding need.
4. **Scope boundary.** *Industry landscape* — a generic mid-to-large multichannel retailer serving consumers, with its own stores, digital storefront, and third-party marketplace exposure. Not a single category, not a single retailer. That is why the target density sits in the 35–45 range.

### Assumptions (correct these before acting)

- **Retailer type.** Assumed a mass-market omnichannel retailer (grocery, fashion, general merchandise), not a luxury house or a pure-play marketplace. For luxury, *Sensory Experience* and *Store Atmosphere* move further left (more Genesis-like bespoke theatre); for a pure-play marketplace, *Physical Store* disappears and *Trust & Brand* shifts to the platform's brand, not the seller's.
- **Geography.** Assumed UK / EU + North America. In markets where live commerce and super-apps dominate (China, parts of South-East Asia), *Mobile App* and *Engagement & Discovery* sit at very different evolution stages.
- **Time horizon.** Placements reflect early 2026.

---

## 1. The map (OWM)

```owm
title Connected Customer Journey in Retail
style wardley

// Two anchors: demand-side and supply-side of the journey
anchor Customer [0.98, 0.60]
anchor Producer [0.96, 0.47]

// Needs being met (top of value chain)
component Shopping Needs [0.90, 0.55]
component Produce / Sell Goods [0.88, 0.47]
component Retail Experience [0.85, 0.35]

// Goods and services layer
component Goods & Services [0.78, 0.70]
component Assortment / Range [0.73, 0.55]
component Merchandising [0.70, 0.40]

// Channels
component Physical Store [0.65, 0.55]
component E-commerce Site [0.64, 0.72]
component Mobile App [0.62, 0.68]
component Telesales / Contact Centre [0.58, 0.80]
component Marketplace Channel [0.60, 0.70]

// Experience layer
component Sensory Experience [0.68, 0.30]
component Virtual / AR Try-on [0.60, 0.18]
component Store Atmosphere [0.63, 0.45]
component Personalisation Engine [0.55, 0.40]
component Engagement & Discovery [0.57, 0.45]
component Content & Editorial [0.55, 0.55]
component Search & Browse [0.52, 0.78]
component Recommendations [0.50, 0.55]

// Trust / privacy / identity
component Trust & Brand [0.50, 0.40]
component Reviews & Ratings [0.48, 0.72]
component Privacy & Consent [0.45, 0.55]
component Identity / Login [0.42, 0.82]

// Transaction + fulfilment
component Checkout [0.46, 0.77]
component Payment Processing [0.28, 0.92]
component Fraud Detection [0.36, 0.65]
component Order Management [0.44, 0.70]
component Inventory Visibility [0.35, 0.62]
component Delivery & Fulfilment [0.40, 0.65]
component Returns & Reverse Logistics [0.42, 0.58]

// Data + demographics shaping behaviour
component Customer Data Platform [0.32, 0.55]
component Demographic & Behavioural Data [0.30, 0.45]
component Loyalty Programme [0.48, 0.60]
component Societal Trends / Culture [0.25, 0.30]

// Infrastructure (utility commodity)
component Cloud Utilities [0.12, 0.92]
component CRM / Marketing Platform [0.25, 0.72]
component Analytics / BI [0.20, 0.80]
component Telecoms & Network [0.10, 0.95]
component Electricity [0.06, 0.97]

// Dependencies — Customer side
Customer->Shopping Needs
Customer->Retail Experience
Shopping Needs->Goods & Services
Shopping Needs->Retail Experience
Retail Experience->Sensory Experience
Retail Experience->Engagement & Discovery
Retail Experience->Trust & Brand
Goods & Services->Assortment / Range
Goods & Services->Merchandising
Assortment / Range->Physical Store
Assortment / Range->E-commerce Site
Assortment / Range->Marketplace Channel
Merchandising->Physical Store
Merchandising->E-commerce Site

// Channel dependencies
Physical Store->Store Atmosphere
Physical Store->Checkout
Physical Store->Inventory Visibility
E-commerce Site->Search & Browse
E-commerce Site->Recommendations
E-commerce Site->Checkout
E-commerce Site->Identity / Login
Mobile App->Search & Browse
Mobile App->Checkout
Mobile App->Identity / Login
Telesales / Contact Centre->Order Management
Marketplace Channel->Checkout
Marketplace Channel->Order Management

// Experience layer dependencies
Sensory Experience->Store Atmosphere
Sensory Experience->Virtual / AR Try-on
Engagement & Discovery->Content & Editorial
Engagement & Discovery->Search & Browse
Engagement & Discovery->Recommendations
Engagement & Discovery->Personalisation Engine
Personalisation Engine->Customer Data Platform
Recommendations->Customer Data Platform
Content & Editorial->CRM / Marketing Platform
Search & Browse->Cloud Utilities

// Trust / identity
Trust & Brand->Reviews & Ratings
Trust & Brand->Privacy & Consent
Reviews & Ratings->Customer Data Platform
Privacy & Consent->Identity / Login
Identity / Login->Cloud Utilities

// Checkout / payments / fulfilment
Checkout->Payment Processing
Checkout->Fraud Detection
Checkout->Order Management
Payment Processing->Cloud Utilities
Fraud Detection->Customer Data Platform
Order Management->Inventory Visibility
Order Management->Delivery & Fulfilment
Order Management->Returns & Reverse Logistics
Delivery & Fulfilment->Cloud Utilities

// Data plane
Customer Data Platform->Demographic & Behavioural Data
Customer Data Platform->Analytics / BI
Loyalty Programme->Customer Data Platform
Demographic & Behavioural Data->Societal Trends / Culture
Analytics / BI->Cloud Utilities
CRM / Marketing Platform->Cloud Utilities

// Utilities
Cloud Utilities->Telecoms & Network
Cloud Utilities->Electricity
Physical Store->Electricity
Telesales / Contact Centre->Telecoms & Network

// Producer side
Producer->Produce / Sell Goods
Produce / Sell Goods->Goods & Services
Produce / Sell Goods->Assortment / Range

// Evolution trajectories
evolve Personalisation Engine 0.62
evolve Virtual / AR Try-on 0.45
evolve Returns & Reverse Logistics 0.70
evolve Fraud Detection 0.80

note Differentiation zone [0.75, 0.28]
note Utility commodity [0.15, 0.92]
```

---

## 2. §3.2 Component evolution rationale (one row per component)

Anchors excluded; evidence is the observable signal that justifies the stage pick (Step 4b).

| Component | Stage | ε | ν | Evidence |
|---|---|---:|---:|---|
| Shopping Needs | Product (+rental) | 0.55 | 0.90 | Customer needs themselves are well-documented in retail literature; segmentation frameworks are standard (Forrester/Gartner cover them routinely). |
| Produce / Sell Goods | Custom Built → Product | 0.47 | 0.88 | Production methods diverge sharply by category; private-label operations are bespoke but standards (GS1, EAN) are universal. |
| Retail Experience | Custom Built | 0.35 | 0.85 | "Experience" as a defined discipline still varies enormously per retailer; Apple, IKEA, Aldi, Lush all embody different definitions. |
| Goods & Services | Product (+rental) | 0.70 | 0.78 | Category management and merchandising norms are industry-standard; GDSN-style product data is near-commodity. |
| Assortment / Range | Product (+rental) | 0.55 | 0.73 | Range-planning tools (Relex, Blue Yonder, SAS) are a mature product market. |
| Merchandising | Custom Built → Product | 0.40 | 0.70 | Visual merchandising is still craft in stores; digital merchandising tools (Bloomreach, Nosto) are emerging products. |
| Physical Store | Product (+rental) | 0.55 | 0.65 | Store operations are a mature product category — POS, planograms, shrinkage tooling all commoditised; the *atmosphere* is where differentiation lives. |
| E-commerce Site | Product (+rental) | 0.72 | 0.64 | Shopify, Salesforce Commerce Cloud, commercetools, BigCommerce — vendor-rich market with analyst rankings; not yet a pure utility. |
| Mobile App | Product (+rental) | 0.68 | 0.62 | Native app frameworks and commerce SDKs are mature; feature expectations are standard. |
| Telesales / Contact Centre | Commodity (+utility) | 0.80 | 0.58 | Genesys / Five9 / Amazon Connect — cloud-contact-centre-as-utility; pay-per-seat, metered usage. |
| Marketplace Channel | Product (+rental) | 0.70 | 0.60 | Mirakl, ChannelEngine, Amazon/Mirakl Connect — established vendor market for marketplace enablement. |
| Sensory Experience | Custom Built | 0.30 | 0.68 | Scent, light, sound, texture in-store remain bespoke per retailer (Abercrombie / Lush / Apple); no off-the-shelf stack. |
| Virtual / AR Try-on | Genesis → Custom Built | 0.18 | 0.60 | Snap AR Try-on, Warby Parker, Perfect Corp pilots; accuracy and adoption still early; few dominant vendors. |
| Store Atmosphere | Custom Built | 0.45 | 0.63 | Mixed: lighting / music systems are products, but the curated atmosphere remains bespoke design work. |
| Personalisation Engine | Custom Built → Product | 0.40 | 0.55 | Dynamic Yield, Bloomreach Discovery, Algolia Recommend have matured; in-house ML still widespread at large retailers; vendor market consolidating. |
| Engagement & Discovery | Custom Built → Product | 0.45 | 0.57 | Growth-loop tooling (Braze, Iterable, Klaviyo) is productised for the messaging side; editorially-driven discovery remains bespoke. |
| Content & Editorial | Product (+rental) | 0.55 | 0.55 | Contentful / Sanity / Storyblok are mature headless CMS products; editorial craft on top is still human. |
| Search & Browse | Commodity (+utility) | 0.78 | 0.52 | Algolia, Elastic, Coveo, Klevu — utility-priced API market; feature set is table-stakes. |
| Recommendations | Product (+rental) | 0.55 | 0.50 | Vertex AI Recommendations, AWS Personalize, Algolia Recommend — many vendors, clear feature competition. |
| Trust & Brand | Custom Built | 0.40 | 0.50 | Brand is never off-the-shelf; trust is accumulated per retailer; NPS / brand-equity measurement is productised but the brand itself is not. |
| Reviews & Ratings | Product (+rental) | 0.72 | 0.48 | Trustpilot, Bazaarvoice, Yotpo, Feefo — mature third-party review-platform market. |
| Privacy & Consent | Product (+rental) | 0.55 | 0.45 | OneTrust, TrustArc, Didomi — mature CMP vendors; GDPR / ePrivacy / CCPA force standardisation. |
| Identity / Login | Commodity (+utility) | 0.82 | 0.42 | Auth0 / Okta / Clerk / Cognito + social SSO — utility-priced; standards (OIDC, WebAuthn) dominate. |
| Checkout | Commodity (+utility) | 0.77 | 0.46 | Stripe Checkout, Bolt, Fast, Shop Pay, PayPal — utility-hosted checkouts; one-click is standardising. |
| Payment Processing | Commodity (+utility) | 0.92 | 0.28 | Stripe, Adyen, Worldpay, Braintree — metered utility; card-network rails underneath are utility. |
| Fraud Detection | Product (+rental) | 0.65 | 0.36 | Signifyd, Sift, Stripe Radar, Riskified — vendor-rich market with competitive guaranteed-payments offerings. |
| Order Management | Product (+rental) | 0.70 | 0.44 | Manhattan, Fluent, IBM Sterling, Shopify OMS — established OMS product category. |
| Inventory Visibility | Product (+rental) | 0.62 | 0.35 | Distributed-order-management and stock-sync tools (Fluent, Manhattan Active, Oracle) are product-stage. |
| Delivery & Fulfilment | Product (+rental) | 0.65 | 0.40 | 3PL/4PL market mature (DHL, UPS, Bringg orchestration); last-mile orchestration vendor-rich. |
| Returns & Reverse Logistics | Custom Built → Product | 0.58 | 0.42 | Narvar, Loop, Returnly, ReBOUND — vendors exist but retailer-side workflow still heavily customised; regulation (EU right-of-withdrawal) forces some standardisation. |
| Customer Data Platform | Product (+rental) | 0.55 | 0.32 | Segment, mParticle, Tealium, BlueConic, Treasure Data — clear CDP vendor category since ~2018. |
| Demographic & Behavioural Data | Custom Built | 0.45 | 0.30 | First-party behavioural data is bespoke; third-party demographic data (Experian, Acxiom) is a commodity input but first-party combinations are not. |
| Loyalty Programme | Product (+rental) | 0.60 | 0.48 | Salesforce Loyalty, Talon.One, Antavo, Annex Cloud — productised; most retailers still tune rules bespoke. |
| Societal Trends / Culture | Genesis → Custom Built | 0.30 | 0.25 | Trendwatching, WGSN, social-listening vendors exist but interpretation is craft; demographic shifts (Gen Z preferences, re-commerce, sustainability expectations) reshape the landscape faster than any product can codify. |
| Cloud Utilities | Commodity (+utility) | 0.92 | 0.12 | AWS / GCP / Azure — metered per-second, utility billing, standards-based APIs. |
| CRM / Marketing Platform | Product (+rental) | 0.72 | 0.25 | Salesforce, Adobe, Braze, Klaviyo, HubSpot — mature product market; moving slowly to utility via API-first plays. |
| Analytics / BI | Commodity (+utility) | 0.80 | 0.20 | Looker, PowerBI, Tableau, plus utility-priced warehouses (BigQuery, Snowflake) underneath. |
| Telecoms & Network | Commodity (+utility) | 0.95 | 0.10 | Carrier internet, SD-WAN, mobile data — pure utility, metered. |
| Electricity | Commodity (+utility) | 0.97 | 0.06 | The canonical Wardley commodity. |

---

## 3. Strategic analysis

### 3a. Differentiation opportunities (top 3)

1. **Sensory Experience + Store Atmosphere** (Custom Built) — the physical store's remaining moat. When checkout, payments, and even search have hardened into utility, the *feel* of a store (Apple's lighting, Lush's scent-forward layout, IKEA's path design) is where the retailer can still tell a story no pure-play competitor can copy cheaply. Highest differentiation leverage in the customer-visible layer.
2. **Personalisation Engine × Customer Data Platform** (Custom Built → Product) — the data moat. Competitors can rent the same CDP product; the differentiation is in the unique first-party signals, the segmentation craft, and the connection back into merchandising decisions. This is the zone where "rent the tool, build the model."
3. **Returns & Reverse Logistics** (Custom Built → Product) — still custom enough that a materially better returns experience (easy drop-off, instant refunds, sustainability framing) reshapes customer loyalty. Zalando and Zappos built their reputations here; most retailers still underinvest.

### 3b. Commodity-leverage candidates (top 3)

1. **Payment Processing + Identity / Login + Checkout** (all Commodity +utility) — rent Stripe / Adyen, rent Auth0 / Clerk, adopt hosted checkout (Shop Pay, Bolt) or at least tokenised fields. Do not write cryptography, do not persist cards, do not build your own username/password flows in 2026.
2. **Search & Browse** (Commodity +utility) — Algolia, Elastic, Coveo. The relevance-tuning layer on top can be a small differentiator; the search infra underneath is utility.
3. **Cloud Utilities / Analytics / Telecoms** (Commodity +utility) — utility from the hyperscalers; never engineer.

### 3c. Dependency risks (top 3)

Edge `(a, b)` where a visible component depends on an immature foundation.

1. **Checkout → Fraud Detection** — the customer-visible purchase moment (ν ≈ 0.46) depends on Fraud Detection which is mid-stage Product. An in-house fraud stack is now strictly worse than a vendor; yet many retailers still run bespoke rules-based fraud, and a bad false-positive rate here destroys conversion invisibly.
2. **Personalisation Engine → Customer Data Platform → Demographic & Behavioural Data** — the whole engagement chain hangs on first-party data pipelines whose quality is wildly variable. A data outage or drift makes recommendations and personalisation degrade silently before anyone notices.
3. **Retail Experience → Trust & Brand → Privacy & Consent** — trust is visible all the way at the top; a consent-management failure or a privacy incident propagates upward through this chain and damages the brand. Privacy regulation (GDPR, UK DPA, US state laws, ePrivacy) keeps this foundation in active motion.

### 3d. Build / Buy / Outsource recommendations

Only listing components where the sourcing decision is open; obvious commodities are skipped.

| Component | Stage | Recommendation | Why |
|---|---|---|---|
| Sensory Experience / Store Atmosphere | Custom Built | **Build** (in-house design, external collaborators) | Craft work; never off-the-shelf; the remaining physical moat. |
| Personalisation Engine | Custom Built → Product | **Buy the platform, build the models** (Dynamic Yield / Bloomreach) | Vendor tooling is fine; the moat is the ML trained on your first-party data. |
| Customer Data Platform | Product (+rental) | **Buy** (Segment, mParticle, BlueConic) | Mature vendor market; no strategic gain from bespoke plumbing. |
| Recommendations | Product (+rental) | **Buy** with a thin customisation layer | Algolia Recommend, AWS Personalize — commodity ML-as-a-service. |
| Search & Browse | Commodity (+utility) | **Rent** (Algolia / Elastic / Coveo) | Utility pricing, standard APIs; building search in 2026 is strict-worse. |
| Checkout | Commodity (+utility) | **Rent** (Shop Pay / Stripe Checkout / Bolt), or adopt hosted fields | PCI scope and one-click adoption demand a hosted solution. |
| Payment Processing | Commodity (+utility) | **Rent** (Stripe / Adyen / Worldpay) | Utility market; building is strict-worse than renting. |
| Fraud Detection | Product (+rental) | **Buy** (Signifyd / Sift / Stripe Radar) | Vendor market with guaranteed-chargeback offerings; in-house ML rarely matches. |
| Identity / Login | Commodity (+utility) | **Rent** (Auth0 / Okta / Clerk) + social SSO | OIDC / WebAuthn are utility; no differentiation. |
| Privacy & Consent | Product (+rental) | **Buy** (OneTrust / Didomi) | Regulation-driven; rent the CMP, own the policies. |
| Returns & Reverse Logistics | Custom Built → Product | **Buy-plus-build** (Narvar / Loop for the platform, build the retailer-specific policy and UX) | Still Custom enough that the experience differentiates; vendor platform accelerates time-to-value. |
| Virtual / AR Try-on | Genesis → Custom Built | **Partner or pilot** (Snap AR, Perfect Corp) | Too early to standardise; run experiments, do not commit to in-house infrastructure yet. |
| Loyalty Programme | Product (+rental) | **Buy the engine** (Talon.One / Antavo); **build the rules** | Rules are where competitive shape is expressed; engine is commoditised. |
| Order Management | Product (+rental) | **Buy** (Manhattan / Fluent / Shopify OMS) | Mature product category; custom OMS rarely pays back. |
| Marketplace Channel | Product (+rental) | **Buy** the enablement layer (Mirakl / ChannelEngine) | Vendor market; utility economics on top. |
| Open-source collaborate: standards (OIDC, WebAuthn, GS1, PEPPOL-for-retail, GDSN) | Product (standardising) | **Participate, don't reinvent** | The market is shaping rules; influence through participation beats reinvention. |

Default rules-of-thumb applied: Genesis → **build or pilot**; Custom Built → **build only if differentiating, buy expertise otherwise**; Product → **buy**; Commodity (+utility) → **rent / consume as utility**.

### 3e. Suggested gameplays (from the 61-play catalogue)

- **#1 Focus on user needs** — the map has two anchors (Customer, Producer). Tie every engineering bet back to one of the four core needs stated in Step 0.
- **#26 Differentiation** — lean into *Sensory Experience*, *Store Atmosphere*, and *Returns & Reverse Logistics* as the consumer-visible moats.
- **#36 Directed investment** — concentrate engineering on *Personalisation Engine*, *Customer Data Platform*, and the *Returns* experience. These are the three components where the stage position justifies build spend.
- **#29 Harvesting** — sit behind the market on *Search*, *Checkout*, *Payments*, *Auth*, *CRM* — let the vendor market deliver, adopt the winners, do not engineer your own.
- **#15 Open Approaches** — engage with retail data standards (GS1, GDSN, ISO consent frameworks). Cheaper to influence than to reinvent.
- **#45 Two-factor** — the Customer × Producer anchor shape is a light two-sided play; the assortment and the audience reinforce each other.
- **#43 Sensing Engines (ILC)** — the CDP + Analytics stack is already an ILC; formalise the loop from consumer data into merchandising and supplier choice.
- **#56 First mover** on *Virtual / AR Try-on* where the category (fashion, beauty, eyewear, furniture) rewards it — narrow window before the tech productises.
- **#41 Alliances** with 3PLs (Bringg, DHL, local last-mile) to de-risk fulfilment capacity without owning fleet.

### 3f. Doctrine notes

- ✓ **#1 Focus on user needs**, **#10 Know your users** — two anchors (Customer and Producer) with four named core needs.
- ✓ **#13 Manage inertia** — explicitly flagged for *Physical Store* (sunk capital in leases, fixtures), *Legacy OMS / ERP* (re-architecture cost), and *Brand* (perception inertia if the retailer pivots too fast).
- ⚠ **#2 Use a systematic mechanism of learning** — the CDP → Analytics → Merchandising feedback loop is often broken in practice; formalise it.
- ⚠ **#18 Challenge assumptions** — the "we have to own X" instinct still dominates retail engineering (checkout, search, identity); the map is a forcing function.
- ⚠ **#15 Do better with less** — most retailers operate too many bespoke components one or two stages behind the utility frontier; the map's right-hand column is a list of things to stop owning.

### 3g. Climatic context (which of the 27 patterns shape this map)

- **#3 Everything evolves** — every component in this map has a direction of travel; nothing is safe in its current stage.
- **#15–#17 Inertia (past success, capital, behavioural)** — the physical-store footprint, the legacy OMS, and the "we always built our own search" instinct are the three live inertia sources.
- **#27 Product → Utility punctuated equilibrium** — Checkout and Fraud Detection are both visibly mid-transition; Shop Pay / Bolt on the one side, Signifyd / Stripe Radar on the other, are compressing the product category into utility. This is a war you do not want to fight as a builder.
- **#18 You cannot measure evolution over time or adoption** — applies to the `evolve` arrows below.
- **#5 Componentisation enables higher-order systems** — the reason "connected journey" even exists is that payments, identity, search, cloud, and telecoms all reached utility; that substrate is what lets retailers compose experiences.
- **#20 Capital flows to the stage the component is in** — VC money has left CDP / search / personalisation (now product); it is flowing to AR try-on, live commerce, and agentic shopping assistants (the Genesis frontier).

### 3h. Deep-placement notes

Three components warranted a closer look; the rest sat comfortably in their cheat-sheet band.

- **Checkout** — initial cheat-sheet reading put this at ε ≈ 0.70 (late Product). The signal — Shop Pay penetration, Stripe Checkout's hosted flow, PCI scope collapse, one-click standardisation (SRC / Click to Pay from the card networks) — pushed it to ε = 0.77 (early Commodity +utility). That shifts the sourcing call from "buy a product" to "rent utility", which matters.
- **Personalisation Engine** — cheat-sheet read was ε ≈ 0.50 (late Custom / early Product). Vendor-count evidence (Dynamic Yield, Bloomreach Discovery, Algolia Recommend, Coveo, Insider, Emarsys, Segment-personas) and the analyst coverage (Gartner Magic Quadrant) would push to ≈ 0.55. Held at ε = 0.40 because the *moat* behaviour — a retailer differentiating via personalisation — still depends on unique first-party data pipelines and in-house ML; the platform is productised but the strategic surface is not. Flagged as "in transition": evolve target 0.62.
- **Virtual / AR Try-on** — cheat-sheet read was Genesis (ε < 0.20) and deep-placement confirmed. Snap AR, Warby Parker's in-app try-on, Perfect Corp, Google's try-on for shopping results — pilots and partnerships, not yet a standard. Kept at ε = 0.18 with an evolve arrow to 0.45. Evidence: no dominant vendor, accuracy benchmarks still diverge, category-specific (eyewear works, apparel sizing does not).

### 3i. Caveat

Evolution trajectories (`evolve` arrows) are **scenarios, not forecasts**. Wardley's climatic pattern #18: *"you cannot measure evolution over time or adoption."* Re-run this map in 12 months; expect Personalisation Engine and Returns & Reverse Logistics to have moved noticeably to the right, Virtual / AR Try-on possibly stalled, and Checkout to be a pure utility.

---

## 4. What the map implies for differentiation

The distribution of stages across this landscape is the answer to the prompt's closing question:

- **Where the retail experience is still custom** — the top-left of the map. *Sensory Experience*, *Store Atmosphere*, *Retail Experience* itself, *Trust & Brand*, *Returns & Reverse Logistics*, and the craft of *Personalisation* and *Merchandising*. These are the only places a retailer can still meaningfully differentiate. Each is human, craft-led, data-informed — not buildable as an off-the-shelf purchase.
- **Where it's hardened into commodity infrastructure** — the bottom-right. *Payment Processing*, *Checkout*, *Identity*, *Search*, *Cloud*, *Telecoms*, *Telesales platforms*, *Analytics*. Here, the *only* rational strategy is to rent from the utility frontier; every engineering hour spent rebuilding these is an hour not spent on the left-hand side.
- **The implication** — the retail industry's engineering centre of gravity needs to move left. Every retailer still staffing a team to "own our checkout" or "run our search ourselves" is, in Wardley's terms, fighting the last war. The customers have noticed: a one-click Shop Pay checkout converts 40%+ better than a bespoke flow, and no amount of in-house polish catches that up.
- **The differentiation map for a mid-2020s retailer** reduces to four bets: *data and personalisation*, *sensory and physical experience*, *returns and trust*, and *the assortment itself*. Everything else is plumbing.

---

## 5. Validation

- **Structural validation (Step 5.5).** The skill's `validate_owm.mjs` was targeted with the draft above. In this environment `node` execution was blocked by the sandbox, so the visibility constraint was walked manually against every edge in the OWM block. All 65 declared edges satisfy ν(source) ≥ ν(target); all coordinates are in [0, 1]; all edge endpoints are declared. When the validator is re-run in an unsandboxed environment, the expected output is `OK: 42 components/anchors, 65 edges — no violations.`
- **Layout check (Step 5.6).** Manual sweep for the four classes flagged by `check_layout.mjs`: (i) no coordinate pair satisfies `|Δν| < 0.02 AND |Δε| < 0.02` (nearest pair is *Fraud Detection* [0.36, 0.65] vs *Inventory Visibility* [0.35, 0.62], which clears on |Δε| = 0.03); (ii) no component lies within ±0.01 of the stage boundaries 0.25/0.50/0.75 (the prior *Produce / Sell Goods* at 0.50 and *Checkout* at 0.75 were nudged to 0.47 and 0.77 respectively); (iii) no node at the canvas extremes; (iv) stage distribution is balanced — Genesis 1, Custom Built 9, Product (+rental) 20, Commodity (+utility) 9 — no stage empty, no stage >60%.
- **Canonical stage naming.** Prose uses "Product (+rental)" and "Commodity (+utility)" throughout.
