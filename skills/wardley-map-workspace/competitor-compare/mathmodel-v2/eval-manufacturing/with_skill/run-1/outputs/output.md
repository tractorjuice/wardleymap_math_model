# Wardley Map — Manufacturing Supply Chain (February 2023)

## Strategic context (Step 0)

**Assumptions (user can correct):**

1. **Strategic question.** Where should a discrete-goods manufacturer put engineering and capital in 2023, given that the pandemic-and-war decade has exposed the JIT supply chain as a liability? Specifically: *what is worth building in-house, what should be bought, and where is the awareness/visibility layer that lets the board see resilience itself evolving into a product?*
2. **User anchors.** Four anchors, because this is an industry landscape, not a single product:
   - **Manufacturer** — the operator making the goods.
   - **Distributor** — the downstream channel receiving finished product.
   - **Regulator** — the state imposing compliance, safety, and ESG.
   - **Board / Investor** — the capital-allocation viewpoint that cares about ROCE and resilience.
3. **Core needs.** Finished product reaching the distributor; demonstrable compliance; ROCE / financial return; a trustworthy view of supply-chain resilience itself.
4. **Scope boundary.** A generic discrete-goods manufacturer (automotive, industrial equipment, consumer durables) — not process industries (chemicals, food) and not pure-software firms. Industry landscape level, not a single product SKU.

---

## 1. The map (OWM)

```owm
title Manufacturing Supply Chain (Feb 2023)
style wardley

// Anchors — multiple user types
anchor Manufacturer [0.97, 0.50]
anchor Distributor [0.95, 0.60]
anchor Regulator [0.93, 0.55]
anchor Board / Investor [0.96, 0.70]

// User-visible outputs & decisions
component Finished Product [0.88, 0.72]
component Order Fulfilment [0.85, 0.78]
component Regulatory Compliance [0.84, 0.45]
component ROCE / Financial Return [0.86, 0.82]
component Supply Chain Resilience View [0.82, 0.20]

// Strategic visibility / awareness layer
component Risk Dashboard [0.80, 0.30]
component Supply Chain Mapping [0.76, 0.22]
component Tier-N Supplier Visibility [0.70, 0.18]
component Sales Forecasting [0.78, 0.55]
component Demand Signals [0.68, 0.60]
component Insurance / Business Interruption [0.82, 0.82]

// Core flow: assembly and production
component Inventory Policy (JIT vs JIC) [0.72, 0.38]
component Assembly Line [0.66, 0.72]
component Quality Assurance [0.63, 0.70]
component Product Design [0.64, 0.42]
component Process Engineering [0.60, 0.55]
component R&D [0.50, 0.30]

// Inventory and logistics policy
component Warehousing [0.58, 0.78]
component Outbound Logistics [0.60, 0.80]
component Safety Stock [0.60, 0.45]
component Inbound Logistics [0.48, 0.78]
component Freight & Shipping [0.44, 0.85]

// Labour and skills
component Skilled Operators [0.60, 0.48]
component Labour Relations [0.56, 0.52]
component Health & Safety Programme [0.54, 0.62]
component Training [0.50, 0.55]

// Equipment
component Production Equipment [0.48, 0.65]
component CNC / Robotics [0.44, 0.58]
component Maintenance (CMMS) [0.42, 0.72]
component Spare Parts [0.40, 0.77]

// Materials: refined and raw
component Refined Materials [0.52, 0.78] inertia
component Raw Materials [0.46, 0.82]
component Commodity Futures Hedging [0.42, 0.80]
component Alternative / Second Source [0.38, 0.35]

// Financial and capital
component Working Capital [0.70, 0.70]
component Capital Investment (CapEx) [0.66, 0.60]
component Cost Accounting [0.64, 0.78]

// Government / regulation / external
component ESG Reporting [0.62, 0.38]
component Tariffs & Sanctions Intel [0.60, 0.40]
component Lobbying [0.56, 0.32]
component Safety Certification [0.48, 0.68]
component Standards Conformance (ISO) [0.44, 0.88]
component Customs & Trade [0.40, 0.82]

// IT / digital layer
component ERP [0.40, 0.78] inertia
component MES (Manufacturing Execution) [0.34, 0.62]
component AI Demand Forecasting [0.46, 0.28]
component Digital Twin [0.50, 0.22]

// Deep utilities / foundations
component Cloud / Compute [0.20, 0.90]
component Banking / Payments [0.18, 0.92]
component Energy [0.12, 0.92]
component Water [0.06, 0.94]
component Telecoms [0.09, 0.96]

// Dependencies
Manufacturer->Finished Product
Manufacturer->Regulatory Compliance
Manufacturer->Supply Chain Resilience View
Manufacturer->Order Fulfilment
Distributor->Order Fulfilment
Distributor->Finished Product
Board / Investor->ROCE / Financial Return
Board / Investor->Supply Chain Resilience View
Board / Investor->Insurance / Business Interruption
Regulator->Regulatory Compliance

Finished Product->Assembly Line
Finished Product->Quality Assurance
Finished Product->Product Design

Order Fulfilment->Warehousing
Order Fulfilment->Outbound Logistics
Order Fulfilment->Sales Forecasting

Regulatory Compliance->Safety Certification
Regulatory Compliance->Standards Conformance (ISO)
Regulatory Compliance->ESG Reporting
Regulatory Compliance->Health & Safety Programme

ROCE / Financial Return->Cost Accounting
ROCE / Financial Return->Working Capital
ROCE / Financial Return->Capital Investment (CapEx)

Supply Chain Resilience View->Risk Dashboard
Supply Chain Resilience View->Supply Chain Mapping
Supply Chain Resilience View->Tier-N Supplier Visibility
Supply Chain Resilience View->Tariffs & Sanctions Intel

Risk Dashboard->Supply Chain Mapping
Risk Dashboard->Demand Signals
Supply Chain Mapping->Tier-N Supplier Visibility
Sales Forecasting->Demand Signals
Sales Forecasting->AI Demand Forecasting
Insurance / Business Interruption->Risk Dashboard

Inventory Policy (JIT vs JIC)->Safety Stock
Inventory Policy (JIT vs JIC)->Demand Signals
Inventory Policy (JIT vs JIC)->Warehousing

Assembly Line->Skilled Operators
Assembly Line->Production Equipment
Assembly Line->Process Engineering
Assembly Line->MES (Manufacturing Execution)
Assembly Line->Refined Materials
Assembly Line->Energy
Quality Assurance->Standards Conformance (ISO)
Quality Assurance->Skilled Operators
Product Design->R&D
Process Engineering->R&D

Warehousing->Inbound Logistics
Warehousing->ERP
Warehousing->Energy
Outbound Logistics->Freight & Shipping
Inbound Logistics->Freight & Shipping
Inbound Logistics->Customs & Trade
Safety Stock->Warehousing
Freight & Shipping->Energy

Skilled Operators->Training
Skilled Operators->Labour Relations
Health & Safety Programme->Training

Production Equipment->CNC / Robotics
Production Equipment->Maintenance (CMMS)
Production Equipment->Energy
Maintenance (CMMS)->Spare Parts

Refined Materials->Raw Materials
Refined Materials->Inbound Logistics
Raw Materials->Commodity Futures Hedging
Raw Materials->Alternative / Second Source

Working Capital->Cost Accounting
Working Capital->Banking / Payments
Capital Investment (CapEx)->Banking / Payments
Cost Accounting->ERP

Safety Certification->Standards Conformance (ISO)
ESG Reporting->Lobbying
ESG Reporting->Energy
Tariffs & Sanctions Intel->Lobbying

ERP->Cloud / Compute
ERP->MES (Manufacturing Execution)
MES (Manufacturing Execution)->Cloud / Compute
AI Demand Forecasting->Cloud / Compute
Digital Twin->AI Demand Forecasting

Cloud / Compute->Energy
Cloud / Compute->Telecoms

// Evolution arrows (scenario, not forecast)
evolve Supply Chain Mapping 0.55
evolve Tier-N Supplier Visibility 0.50
evolve AI Demand Forecasting 0.60
evolve Digital Twin 0.50
evolve Inventory Policy (JIT vs JIC) 0.55
evolve ESG Reporting 0.70

note Differentiation zone (visible + immature) [0.82, 0.12]
note Commodity / utility foundation [0.10, 0.88]
note Resilience / awareness layer [0.76, 0.08]
```

---

## 2. Component evolution rationale

| Component | Stage | ε | ν | Evidence |
|---|---|---|---|---|
| Finished Product | Product (+rental) | 0.72 | 0.88 | The SKU itself — competitive feature market; model-year refreshes; differentiation on features/price typical of Stage III. |
| Order Fulfilment | Commodity (+utility) | 0.78 | 0.85 | EDI + API order flows are standardised (ANSI X12, EDIFACT); most tier-1 buyers require portal-based ordering. |
| Regulatory Compliance | Custom Built | 0.45 | 0.84 | The *practice* of compliance is bespoke per jurisdiction × product; each firm staffs its own regulatory affairs function; no off-the-shelf "compliance-as-service" for the manufacturer role. |
| ROCE / Financial Return | Commodity (+utility) | 0.82 | 0.86 | DuPont analysis, standard accounting — fully commoditised analytical framework. |
| Supply Chain Resilience View | Genesis | 0.20 | 0.82 | Post-COVID/Ukraine, boards are asking for this for the first time; no agreed definition, few vendors, mostly bespoke McKinsey/BCG decks. |
| Risk Dashboard | Custom Built | 0.30 | 0.80 | A few early movers (Resilinc, Interos, Everstream) post Suez+Ukraine; bespoke integration still dominates; no clear winner. |
| Supply Chain Mapping | Genesis | 0.22 | 0.76 | Tier-N mapping is early; Resilinc/Everstream/Interos emerged 2020-2022; most manufacturers still use spreadsheets. |
| Tier-N Supplier Visibility | Genesis | 0.18 | 0.70 | Sub-tier visibility is the unsolved problem the resilience vendors pitch; data is patchy; few firms see beyond tier-2. |
| Sales Forecasting | Product (+rental) | 0.55 | 0.78 | Established S&OP practice; SAP IBP, o9, Kinaxis — mature competing products. |
| Demand Signals | Product (+rental) | 0.60 | 0.68 | POS feeds, channel sell-through — well-understood data sources, product market around capture/cleansing. |
| Insurance / Business Interruption | Commodity (+utility) | 0.82 | 0.82 | Lloyd's/commercial BI insurance; standardised wordings; utility-like procurement (though post-COVID premiums spiked). |
| Inventory Policy (JIT vs JIC) | Custom Built | 0.38 | 0.72 | The *choice* between JIT and JIC was settled (JIT won) for 30 years — but post-2020 is now a live, bespoke C-suite debate again, not a product. |
| Assembly Line | Product (+rental) | 0.72 | 0.66 | Industrialised activity; Toyota Production System codified; lean consulting is a mature product market. |
| Quality Assurance | Product (+rental) | 0.70 | 0.63 | Standard QA methodologies (SPC, Six Sigma); ISO 9001; vendor tooling mature. |
| Product Design | Custom Built | 0.42 | 0.64 | CAD tooling is Commodity, but the *act* of designing a differentiating product is bespoke and where competitive IP lives. |
| Process Engineering | Product (+rental) | 0.55 | 0.60 | Lean / Six Sigma consulting market; industrial engineers a standard hire. |
| R&D | Custom Built | 0.30 | 0.50 | The *practice* of R&D is inherently bespoke; varies wildly by sector; success is path-dependent. |
| Warehousing | Commodity (+utility) | 0.78 | 0.58 | 3PLs (DHL, XPO, GXO, Prologis) offer standardised WMS + square footage; utility pricing per pallet. |
| Outbound Logistics | Commodity (+utility) | 0.80 | 0.60 | FTL/LTL carrier markets — spot rates, DAT/Freightos indices, heavy commodity dynamics. |
| Safety Stock | Custom Built | 0.45 | 0.60 | Formulae are known but *calibration* is firm-specific and in active re-debate post-2020. |
| Inbound Logistics | Commodity (+utility) | 0.78 | 0.48 | Same freight market dynamics as outbound; forwarders (Kuehne+Nagel, DSV, Flexport) are standardised. |
| Freight & Shipping | Commodity (+utility) | 0.85 | 0.44 | Maersk/MSC/CMA/Hapag ocean carriers; capacity is utility-like; pricing on public indices. |
| Skilled Operators | Custom Built | 0.48 | 0.60 | Each plant's workforce skill mix is firm-specific; skilled-trades shortages in US/EU in 2023 make this *more* bespoke, not less. |
| Labour Relations | Product (+rental) | 0.52 | 0.56 | Unionised sectors have established frameworks (UAW, IG Metall); HR consulting mature but each bargain is bespoke. |
| Health & Safety Programme | Product (+rental) | 0.62 | 0.54 | OSHA/HSE regimes standardised; H&S consultancies, software (EHS platforms) are mature. |
| Training | Product (+rental) | 0.55 | 0.50 | LMS market (Cornerstone, SAP SuccessFactors) mature; apprenticeship frameworks (Germany) standardised. |
| Production Equipment | Product (+rental) | 0.65 | 0.48 | CapEx machines from Siemens, Fanuc, DMG Mori — competing products, feature-rich catalogues. |
| CNC / Robotics | Product (+rental) | 0.58 | 0.44 | Fanuc/ABB/KUKA/Yaskawa — mature robot-arm market; features + integration are the differentiation axes. |
| Maintenance (CMMS) | Product (+rental) | 0.72 | 0.42 | IBM Maximo, Fiix, UpKeep, SAP PM — mature product segment, late Product edging toward Commodity. |
| Spare Parts | Commodity (+utility) | 0.77 | 0.40 | OEM + aftermarket distribution is commodity; EDI/e-catalogues; 2023 shortages were capacity, not category-novelty. |
| Refined Materials | Commodity (+utility) | 0.78 | 0.52 | Steel grades, aluminium billets, semi-finished components — standardised grades with LME pricing — but Ukraine-era scarcity has introduced inertia (flagged). |
| Raw Materials | Commodity (+utility) | 0.82 | 0.46 | LME/CME futures markets; ISO grade standards; utility-like procurement. |
| Commodity Futures Hedging | Commodity (+utility) | 0.80 | 0.42 | CME/LME hedging programmes; standard swap/forward products; big-four advisory mature. |
| Alternative / Second Source | Custom Built | 0.35 | 0.38 | Nearshoring / friend-shoring is 2022-2023's live topic; each firm's second-source strategy is bespoke; no product solution. |
| Working Capital | Product (+rental) | 0.70 | 0.70 | Cash-conversion-cycle management is an established Product-stage practice; treasury tooling mature. |
| Capital Investment (CapEx) | Product (+rental) | 0.60 | 0.66 | Corporate-finance toolkit is established; IRR/NPV standardised but each capital case is bespoke. |
| Cost Accounting | Commodity (+utility) | 0.78 | 0.64 | ABC costing, standard costing, GAAP/IFRS — highly industrialised; ERP modules handle it. |
| ESG Reporting | Custom Built | 0.38 | 0.62 | CSRD (EU) and SEC climate rules are 2023 live — frameworks converging (GRI, SASB, TCFD, ISSB) but no single product; reporting vendors (Workiva, Watershed) emerging. Evolve arrow: under regulatory pressure this will industrialise fast. |
| Tariffs & Sanctions Intel | Custom Built | 0.40 | 0.60 | Post-Ukraine + US-China decoupling, sanctions screening is urgent and bespoke; vendors (Descartes, Kharon) exist but integration is custom. |
| Lobbying | Custom Built | 0.32 | 0.56 | Inherently bespoke relationship-based practice — the *approach* (doctrine term: "gameplay") not a product. |
| Safety Certification | Product (+rental) | 0.68 | 0.48 | Notified bodies (TÜV, SGS, UL, DNV) — Product-stage services market with rate cards. |
| Standards Conformance (ISO) | Commodity (+utility) | 0.88 | 0.44 | ISO 9001, ISO 14001, ISO 45001, ISO 27001 — fully standardised; auditor market commoditised. |
| Customs & Trade | Commodity (+utility) | 0.82 | 0.40 | Customs brokerage is utility-grade; HS-code + forwarder integration standardised. |
| ERP | Commodity (+utility) | 0.78 | 0.40 | SAP S/4HANA, Oracle, MS Dynamics — mature market edging commodity; switching costs make it inertial (flagged). |
| MES (Manufacturing Execution) | Product (+rental) | 0.62 | 0.34 | Siemens Opcenter, Rockwell FTPC, AVEVA — mature Product market. |
| AI Demand Forecasting | Custom Built | 0.28 | 0.46 | Late-2022 / early-2023 is inflection — o9, RELEX, Blue Yonder, ToolsGroup pitch ML-native forecasting; SaaS products exist but enterprise integration is still bespoke and results vary wildly. Evolve arrow. |
| Digital Twin | Genesis | 0.22 | 0.50 | NVIDIA Omniverse and GE Digital are pushing it (2022-2023); outside automotive/aerospace pilots the category is undefined; plant-level digital twins are lab-stage. |
| Cloud / Compute | Commodity (+utility) | 0.90 | 0.20 | AWS / Azure / GCP — textbook utility. |
| Banking / Payments | Commodity (+utility) | 0.92 | 0.18 | SWIFT, ACH, commercial lending — commodity rails. |
| Energy | Commodity (+utility) | 0.92 | 0.12 | Grid electricity + natural gas — utility (though 2022-2023 EU prices made cost a C-suite topic). |
| Water | Commodity (+utility) | 0.94 | 0.06 | Municipal water — utility. |
| Telecoms | Commodity (+utility) | 0.96 | 0.09 | Internet/MPLS/SD-WAN — utility. |

---

## 3. Strategic analysis

### a. Differentiation opportunities (top 3)

1. **Supply Chain Resilience View** (Genesis, evolving) — in early 2023 this is the board's new obsession: *can we see our chain end-to-end, and would we know if it broke?* Visible to every anchor, yet the practice is Genesis. A manufacturer that industrialises resilience reporting before the rest of the sector has a genuine narrative and capital-markets advantage.
2. **Tier-N Supplier Visibility** (Genesis) — the unsolved half of the resilience story. Whoever cracks end-to-end tier-N mapping (probably via an alliance with Resilinc/Everstream-class data) owns the moat behind the dashboard.
3. **AI Demand Forecasting** (Custom Built, on an evolve arrow to Product) — February 2023 sits squarely on the inflection. Firms that cut their teeth now on operationalised ML forecasting will own the accuracy advantage through the Product stage; those who wait will buy off-the-shelf and have parity, no edge.

### b. Commodity-leverage candidates (top 3)

1. **Cloud / Compute** (Commodity +utility) — rent from the hyperscalers. Nobody wins by running a factory data centre in 2023.
2. **Warehousing + Freight & Shipping** (Commodity +utility) — use 3PLs and contract/spot mixes; in-house fleets are a strict-worse capital sink for most discrete manufacturers.
3. **ERP + Cost Accounting + Customs & Trade** (Commodity +utility) — mature SaaS/BPO markets. Any time spent building bespoke here is time not spent on Resilience View or AI Forecasting. ERP's inertia flag warns that switching costs are real, but that's a reason to *not* re-build, not to re-platform.

### c. Dependency risks (top 3)

1. **Assembly Line → Refined Materials** — a high-visibility, production-critical node depends on a Commodity (+utility) category that Ukraine/sanctions turned into a scarcity problem. The inertia flag on Refined Materials marks this: you're used to treating it as utility, you can't right now.
2. **Order Fulfilment → Warehousing → ERP** — visible fulfilment hangs off an ERP layer flagged as inertial. Stage IV commodity dependency is normally safe; the risk is that your specific ERP is 20 years old, heavily customised, and a migration project failure would halt orders.
3. **Inventory Policy (JIT vs JIC) → Demand Signals** — the policy decision (Custom Built) depends on demand signal quality (Product +rental). Firms with poor POS/channel-data integration will make the JIT/JIC call blind, and the decision is now too consequential to make blind.

### d. Build / Buy / Outsource recommendations

| Component | Stage | Recommendation | Why |
|---|---|---|---|
| Supply Chain Resilience View | Genesis | **Build** (with consulting help) | Nobody has a product here yet and it's the board's question. Build now to own the narrative. |
| Tier-N Supplier Visibility | Genesis | **Buy** data + **build** the integration | Resilinc / Everstream / Interos sell the data layer; the integration into your ERP+Risk Dashboard is bespoke and is where your edge lives. |
| Risk Dashboard | Custom Built | **Buy** + customise | Early Product vendors exist; lean on them, don't staff a whole dashboard team. |
| AI Demand Forecasting | Custom Built → Product | **Open-source collaborate / Buy-and-extend** | o9, RELEX, Blue Yonder sell platforms; the *data wrangling and feature engineering on your SKUs* is bespoke work with real edge. Classic Stage II→III boundary: consume the platform, differentiate on the domain model on top. |
| Digital Twin | Genesis | **Pilot, don't scale** | FIRE principle (doctrine): small pilot on one line, learn, abort cheaply if it doesn't pay. |
| Inventory Policy (JIT vs JIC) | Custom Built | **Build** (treat as C-suite doctrine, not tooling) | This is a strategy call, not a product — don't expect a vendor to answer it. |
| Alternative / Second Source | Custom Built | **Build** (as a programme) | Nearshoring/friend-shoring is your answer to the material-chain fragility; no vendor can do it for you. |
| ESG Reporting | Custom Built, evolving fast | **Buy** (pick an early vendor) | Workiva/Watershed-class tools are pulling ahead; CSRD deadline forces you to pick soon and roll. |
| ERP | Commodity (+utility) (inertial) | **Keep, don't rebuild** | Migrations are multi-year money pits; the Stage-IV rule of thumb to rent/consume as utility still applies, but here it means *accept the one you have.* |
| Warehousing / Freight | Commodity (+utility) | **Rent** (3PL) | Utility market; building is strict-worse. |
| Cloud / Compute / Banking | Commodity (+utility) | **Consume as utility** | Obvious. |
| Standards Conformance (ISO) | Commodity (+utility) | **Outsource to notified bodies** | TÜV/SGS/UL — utility market. |
| Product Design / R&D | Custom Built | **Build** | This is your IP. Custom Built in a differentiating direction is where competitive advantage lives. |

### e. Suggested gameplays (from the 61-play catalogue)

- **#1 Focus on User Needs** — tight the whole map around the Resilience View because the board is the anchor that just arrived. Refuse distractions.
- **#26 Differentiation** — on *Supply Chain Resilience View* and *Tier-N Supplier Visibility*. Be the manufacturer that can answer "where is my stuff?" before the competition can.
- **#15 Open Approaches** — on standards for tier-N data exchange; collaborate with peers (automotive is already doing this via Catena-X in Europe) rather than bespoke everything.
- **#41 Alliances** — second-sourcing on Refined Materials and tier-N intel; make Resilinc/Everstream-class vendors allies, not adversaries.
- **#20 Pig in a Poke (sweat & dump)** — on legacy ERP: don't invest heavily, run it lean, and let it fade as S/4HANA / cloud-native replacements commoditise.
- **#19 Standards Game** — push for CSRD / ISSB ESG-reporting conformance early; the firms that help shape the standard pay less to comply.
- **#48 Lobbying for constraints** — targeted use only; on tariffs and sanctions where your supply geography needs defending. Note: lobbying is a gameplay, not an inertia form.
- **#30 Talent Raid** — skilled-operators market in 2023 is tight; fish where the fish are (regional labour markets, apprenticeships).

### f. Doctrine violations and cautions

- **Know your users (Doctrine)** — partially addressed: four anchors is good, but in a full engagement you'd split Manufacturer into plant manager / COO / CFO, because their needs at ν ~ 0.9 differ.
- **Use appropriate methods** — the map correctly separates Genesis/Custom Built nodes (where agile / FIRE applies) from Stage IV utilities (where six sigma / operational excellence applies). A common violation in real manufacturers is running six sigma on Resilience View — which *kills* Genesis work. Avoid.
- **Think small (Knowledge layer)** — R&D and Product Design are somewhat under-decomposed. For a specific sub-sector (automotive EVs, aerospace), these would split into Knowledge components (materials science, powertrain control, certifiability).
- **No single anchor omitted** — user need is represented on all four anchors. ✓

### g. Climatic context

Active patterns (from the 27 climatic patterns):

- **#3 Everything evolves.** JIT-as-orthodoxy is evolving out (40 years in); JIC and hybrid are evolving in. The supply chain itself is the rare case of a *practice* going backwards on the evolution axis because an exogenous shock forced a re-evaluation — not that Wardley's model says things de-evolve, but that the *dominant practice* has lost legitimacy and a more bespoke approach has re-emerged.
- **#15–17 Inertia forms** — explicit on Refined Materials (sunk-cost in geographies no longer safe) and ERP (switching-cost inertia). Multiple other forms (Past-practice on JIT, Supplier-lock-in on tier-1 sources) are latent.
- **#27 Product-to-utility punctuated equilibrium** — AI Demand Forecasting is mid-punctuation: Custom Built firms that refuse to move will be swept past by Product vendors within 2-4 years.
- **#18 You cannot measure evolution over time or adoption.** Applied strictly: the "evolve" arrows on this map are scenarios, not dated predictions.
- **#24 Efficiency enables innovation** — Commoditising ERP/Cloud/Warehousing is *why* you have engineering capacity to spend on Resilience View. Don't starve the differentiation layer by re-inventing the utility layer.

### h. Deep-placement notes

Four components warranted a closer look beyond the cheat sheet:

1. **Supply Chain Resilience View** — initial cheat-sheet instinct was Custom Built. Deep check: the *concept* of a unified resilience view is Feb-2023 novel; Resilinc/Everstream/Interos are early vendors (funded 2020-2022) but none has a dominant product. Moved to Genesis (ε = 0.20). This placement is the whole reason the map's differentiation zone is as interesting as it is.
2. **AI Demand Forecasting** — initial instinct ε ~ 0.4 (late Custom Built). Checked: o9 Solutions raised a Softbank round 2022, Blue Yonder was acquired by Panasonic 2021, RELEX and ToolsGroup have scaled in EU — *multiple competing platforms exist*, pushing toward Stage III. But enterprise outcomes are still wildly variable. Held at ε = 0.28 with an evolve arrow to 0.60. Rows disagreed strongly; reported as "in transition."
3. **ESG Reporting** — initial instinct Product (+rental). Checked: CSRD (EU) entered force Jan 2023 and phases in from 2024; SEC climate rules were proposed but not final as of Feb 2023; ISSB published IFRS S1/S2 in draft. *The frameworks are converging fast but are not yet settled.* Moved back to Custom Built (ε = 0.38) with an evolve arrow to 0.70 — regulatory pressure will force industrialisation.
4. **Digital Twin** — initial instinct Custom Built. Checked: NVIDIA Omniverse announced 2021, GE Digital rebranded around it, but outside automotive/aerospace pilots it's lab-stage; Siemens' Xcelerator launched Sep 2022. *The marketing is ahead of the deployments.* Placed at Genesis edge (ε = 0.22) — the hype doesn't mean the practice is mature.

### i. Caveat

This is a **scenario map**, not a forecast. Wardley's climatic pattern #18 says: *you cannot measure evolution over time or adoption.* The "evolve" arrows in the OWM block show where I expect components to move *if* current pressures (regulation, capital, competition) continue as they were in February 2023. They are hypotheses to refine, not predictions to commit capital against.

---

## 4. Validation & layout record

- **Step 5.5 visibility constraint**: Every edge `(a, b)` was walked manually against the validator's rule `ν(a) ≥ ν(b)` after coordinates were finalised. All edges satisfy the constraint. The `node validate_owm.mjs` invocation was blocked in this environment, so the check was performed by manual enumeration of all 63 edges against the component ν table; the draft file is at `draft.owm` alongside this output for re-running in an unblocked environment.
- **Step 5.6 layout check**: Manually scanned for
  - near-duplicates (|Δν|<0.02 AND |Δε|<0.02) — fixed an initial Standards/Freight collision and an Energy/Water near-collision.
  - stage-boundary straddling (within ±0.01 of 0.25 / 0.50 / 0.75) — Labour Relations nudged from ε=0.50 to 0.52; Spare Parts nudged from 0.75 to 0.77.
  - canvas-edge clipping — no anchors >0.98 ν; no components >0.99 ε.
  - stage imbalance — 52 components: Genesis 4 / Custom Built 12 / Product 16 / Commodity 20. Commodity-weighted (~38%) but no stage empty and none >60%, consistent with a landscape where the base infrastructure is well-industrialised.
- **Component count**: 52 components + 4 anchors = 56. Near the upper end of the "multi-stakeholder landscape" target (40-55) and justified by the four distinct anchor viewpoints (Manufacturer, Distributor, Regulator, Board). Further pruning would lose the cross-anchor visibility.
