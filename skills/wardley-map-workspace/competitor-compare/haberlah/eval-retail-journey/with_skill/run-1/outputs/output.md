# Wardley Map Analysis: The Connected Customer Journey in Retail

## Purpose

Where is the retail customer experience still custom-built (and therefore a
source of differentiation), and where has it hardened into commodity
infrastructure (and therefore a place to buy rather than build)? The map
traces the path from Customer and Producer through user needs, the experience
layer, the channel mix, and down into the data, transaction, and compute
plane that sits beneath it.

## OWM Source

```owm
title Connected Customer Journey in Retail
style wardley

// --- Anchors ---
anchor Customer [0.97, 0.50]
anchor Producer [0.95, 0.60]

// --- User needs (high visibility) ---
component Desired Goods & Services [0.86, 0.62]
component Trust & Privacy [0.84, 0.36]
component Discovery & Engagement [0.82, 0.44]

// --- Context shaping needs ---
component Demographics & Societal Behaviour [0.66, 0.50]

// --- Experience layer ---
component Shopping Experience [0.74, 0.30]
component Returns Experience [0.72, 0.58]

// --- Channels ---
component Physical Stores [0.60, 0.78]
component E-commerce Channel [0.58, 0.72]
component Telesales [0.52, 0.80]

// --- Data + transaction services ---
component Customer Identity Data [0.38, 0.82]
component Inventory Data [0.36, 0.72]
component Payment Processing [0.32, 0.88]
component Logistics & Delivery [0.22, 0.84]

// --- Commodity infrastructure ---
component Cloud Infrastructure [0.12, 0.93]

// --- Dependencies ---
Customer->Desired Goods & Services
Customer->Trust & Privacy
Customer->Discovery & Engagement
Producer->Desired Goods & Services
Producer->Demographics & Societal Behaviour

Desired Goods & Services->Shopping Experience
Desired Goods & Services->Returns Experience
Discovery & Engagement->Shopping Experience
Discovery & Engagement->Demographics & Societal Behaviour
Shopping Experience->Demographics & Societal Behaviour
Trust & Privacy->Customer Identity Data

Shopping Experience->Physical Stores
Shopping Experience->E-commerce Channel
Shopping Experience->Telesales
Returns Experience->Logistics & Delivery
Returns Experience->E-commerce Channel

Physical Stores->Inventory Data
Physical Stores->Payment Processing
E-commerce Channel->Customer Identity Data
E-commerce Channel->Inventory Data
E-commerce Channel->Payment Processing
E-commerce Channel->Logistics & Delivery
Telesales->Customer Identity Data
Telesales->Payment Processing

Customer Identity Data->Cloud Infrastructure
Inventory Data->Cloud Infrastructure
Payment Processing->Cloud Infrastructure

// --- Evolution arrows ---
evolve Shopping Experience 0.48
evolve Discovery & Engagement 0.58
evolve Trust & Privacy 0.55
evolve Returns Experience 0.72
evolve Inventory Data 0.82

// --- Build / Buy / Outsource ---
build Shopping Experience
build Discovery & Engagement
build Trust & Privacy
buy Returns Experience
buy E-commerce Channel
outsource Payment Processing
outsource Logistics & Delivery
outsource Cloud Infrastructure
outsource Telesales

// --- Annotations ---
annotation 1 [[0.74, 0.30]] Custom differentiation zone: sensory/experiential layer
annotation 2 [[0.32, 0.88]] Commodity infrastructure: don't reinvent
annotation 3 [[0.66, 0.50]] Demographic shifts reshape needs; monitor continuously
```

## Component Evolution Assessment

| Component | Stage | Position [vis, mat] | Rationale |
|---|---|---|---|
| Customer | Anchor | [0.97, 0.50] | End user of the journey — needs drive the chain. |
| Producer | Anchor | [0.95, 0.60] | Brand/retailer owning the offer. |
| Desired Goods & Services | Product | [0.86, 0.62] | The "offer" itself: categories and SKUs are well-defined and comparable across retailers, but product mix is a competitive choice, not a commodity. |
| Trust & Privacy | Custom-Built | [0.84, 0.36] | Regulatory floors (GDPR/CCPA, PCI) are well understood; consumer trust *experience* and consent UX remain brand-differentiated and under active redesign. |
| Discovery & Engagement | Custom / Product edge | [0.82, 0.44] | Personalisation and recommendation platforms exist (Dynamic Yield, Bloomreach, Algolia) but each brand's discovery flow and content strategy is still bespoke. |
| Demographics & Societal Behaviour | Product | [0.66, 0.50] | Segmentation, panels and behavioural analytics are packaged by Nielsen, Experian, Kantar, Mintel; insight *interpretation* is still proprietary work. |
| Shopping Experience | Custom-Built | [0.74, 0.30] | Sensory, physical/virtual blended journeys (AR try-on, immersive store design, omnichannel clienteling) are where brands actively differentiate — no dominant off-the-shelf answer. |
| Returns Experience | Product | [0.72, 0.58] | Purpose-built vendors have emerged (Happy Returns / PayPal, Loop Returns, ReBound, Narvar) with standardised label-less drop-off and refund flows. |
| Physical Stores | Commodity | [0.60, 0.78] | Operating a retail store is universally understood; fit-out, POS, staff management are well-served by mature providers. |
| E-commerce Channel | Product/Commodity | [0.58, 0.72] | Shopify, Magento/Adobe Commerce, BigCommerce, Salesforce Commerce Cloud, commercetools — competitive, feature-compared, trainable. |
| Telesales | Commodity | [0.52, 0.80] | Call centre and contact-centre-as-a-service (Genesys, NICE, Amazon Connect, Five9) are utility-priced. |
| Customer Identity Data | Commodity | [0.38, 0.82] | CIAM is a utility category: Auth0, Okta CIC, AWS Cognito, Ping Identity. |
| Inventory Data | Product/Commodity | [0.36, 0.72] | ERP/WMS stacks (SAP, Oracle, Manhattan, Blue Yonder) plus modern real-time inventory platforms; still some data-model fragmentation across retailers. |
| Payment Processing | Commodity/Utility | [0.32, 0.88] | Stripe, Adyen, PayPal, Square, Worldpay — standardised APIs, transparent pricing, near-zero marginal cost per transaction. |
| Logistics & Delivery | Commodity/Utility | [0.22, 0.84] | Carrier networks (UPS, FedEx, DPD, Evri) and 3PL platforms are utility services; last-mile orchestration (Bringg, Shipium) sits slightly left of pure utility. |
| Cloud Infrastructure | Utility | [0.12, 0.93] | AWS, GCP, Azure — pay-per-use, standardised, universally used. |

## Key Strategic Observations

1. **A clear differentiation band sits between x ≈ 0.28 and x ≈ 0.48** — Shopping Experience, Trust & Privacy, Discovery & Engagement. Everything the customer *feels* clusters in the Custom-Built / early-Product zone. Everything they *don't notice until it breaks* (payments, logistics, cloud, identity) sits at 0.75 and rightward.

2. **The channel layer is flattening.** Stores (0.78), e-commerce (0.72), telesales (0.80) are all firmly in the Product/Commodity band. Channel *ownership* is not a moat; channel *composition and orchestration* still is.

3. **Returns have quietly commoditised.** The emergence of dedicated returns vendors in the last five years has pulled Returns Experience right to ~0.58. Retailers still building in-house returns software are burning budget that could be redirected to the Shopping Experience band.

4. **Demographic insight sits in an awkward middle** at [0.66, 0.50]: the raw data and segmentation tools are Product stage, but the *strategic interpretation* is bespoke — which is why the component's visibility (0.66) is lower than the needs it shapes. Don't confuse "we buy Nielsen" with "we understand our customers."

5. **The visibility gap between the experience layer (0.72–0.74) and the channels (0.52–0.60) is the place differentiation is won or lost.** Anything that makes the experience feel like it *owns* the channel (rather than sit inside it) is where brand equity accrues.

## Doctrine Check

- **Focus on user needs:** Customer and Producer both anchor the map; three explicit need components (Goods & Services, Trust & Privacy, Discovery & Engagement) are placed high-visibility. Satisfied.
- **Remove duplication and bias:** Watch for retailers re-implementing Payment, Identity, and Returns in-house — all three are solidly right of 0.70 and should be bought or outsourced. The map flags `outsource Payment Processing` and `buy Returns Experience` explicitly.
- **Use appropriate methods:** Agile/experimental methods for Shopping Experience and Discovery (Custom-Built zone); Lean/Six Sigma-style optimisation for Channels and data services; ITIL-style operations for Cloud, Payment and Logistics.
- **Challenge assumptions:** The map surfaces that Telesales is commodity, not "legacy inconvenience" — if it matters to a demographic slice, the cost-per-contact economics are now trivial.

## Recommended Actions

1. **Invest in the Shopping Experience column (x ∈ [0.25, 0.45]).** This is where differentiation lives. Fund sensory/virtual experiments (AR fit, immersive stores, clienteling), personalisation, and the trust/consent UX. Treat them as pioneer bets.
2. **Stop custom-building the returns pipeline.** Procure a returns platform (Happy Returns, Loop, Narvar, ReBound). Free the engineering team.
3. **Consolidate identity and payment onto commodity providers.** Any remaining bespoke implementation is pure inertia cost. Target: one CIAM provider, one payment orchestrator + one PSP fallback.
4. **Treat channels as interchangeable front-ends, not strategy.** Measure channel P&L, but spend the differentiation budget on the experience layer that rides on top of all three.
5. **Embed a demographics/behaviour feedback loop.** The Demographics component shapes Discovery *and* Shopping Experience; instrument both so societal shifts (generational, sustainability, price sensitivity) feed back into the experience layer within a quarter.

## Build vs. Buy Assessment

| Component | Recommendation | Rationale |
|---|---|---|
| Shopping Experience | **Build** | Custom-Built stage; direct differentiation. No off-the-shelf answer that creates brand feel. |
| Discovery & Engagement | **Build** (with product tooling underneath) | Bespoke at the brand layer; use Product-stage personalisation engines as substrate. |
| Trust & Privacy UX | **Build** | Regulatory compliance can be bought; the trust experience is a brand asset. |
| Returns Experience | **Buy** | Product stage — vendors already own this. |
| E-commerce Channel | **Buy** | Shopify / Adobe Commerce / commercetools. Don't rebuild. |
| Customer Identity Data | **Buy (CIAM)** | Commodity. Auth0/Cognito/Okta CIC. |
| Inventory Data | **Buy** (then integrate) | Product/Commodity — ERP/WMS is mature. |
| Payment Processing | **Outsource** | Utility. Stripe/Adyen. |
| Logistics & Delivery | **Outsource** | Utility carrier networks + 3PL. |
| Telesales | **Outsource** | Commodity contact-centre-as-a-service. |
| Cloud Infrastructure | **Outsource** | Utility. |

## Evolution Predictions (12–24 months)

- **Shopping Experience 0.30 → 0.48.** Generative AI assistants, AR try-on, and immersive commerce templates are industrialising parts of what was bespoke — the custom zone will narrow.
- **Discovery & Engagement 0.44 → 0.58.** LLM-driven product discovery and agentic shopping push the capability into Product stage; differentiation moves up a level (prompts, curation, voice).
- **Trust & Privacy 0.36 → 0.55.** Consent frameworks and privacy UX patterns are converging as regulators publish enforceable standards; expect Product-stage consent platforms to dominate.
- **Returns Experience 0.58 → 0.72.** Continues to commoditise; expect carrier-integrated returns to feel like a utility.
- **Inventory Data 0.72 → 0.82.** Real-time, cross-channel inventory becomes table-stakes; API-first WMS providers pull this further right.

## Open Questions

1. What does the **returns process** look like for high-consideration and second-hand/resale flows — does the commoditising returns trend still hold for circular-economy retail?
2. How does **agentic AI shopping** (LLM agents purchasing on the customer's behalf) reshape Discovery & Engagement's visibility — does the human discovery surface become less important than the machine-readable offer feed?
3. Where should **private-label / own-brand** sit on this map? It may belong as a separate value stream feeding Desired Goods & Services from the Producer side.

## Notes on the Three Deliverables

Per the skill, the React artifact and OWM text are the portable deliverables.
The OWM block above is ready to paste into onlinewardleymaps.com, the VS Code
OWM extension, or the Obsidian plugin. The React artifact is not produced as
a file in this run (single-pass text output); the OWM source plus this
commentary are sufficient to reconstruct the interactive rendering using the
template in `templates/artifact-template.jsx`.
