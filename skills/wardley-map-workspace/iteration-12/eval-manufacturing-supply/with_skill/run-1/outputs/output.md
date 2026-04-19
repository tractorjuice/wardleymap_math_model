# Wardley Map — Modern Manufacturing Supply Chain (Feb 2023 context)

## Scope and anchors

The map uses **two anchors**, because a manufacturing supply chain has two distinct user needs that often pull in different directions:

- **End Customer** — wants finished goods delivered on time, in full, at the promised quality and (increasingly) with verifiable provenance / sustainability claims.
- **Operations Planner** — an internal user who runs production planning, S&OP, and exception management. Maps without this second anchor tend to under-weight the internal-tooling side of the chain where most of the build/buy decisions actually sit.

Time context matters. Feb 2023 sits at a specific inflection: COVID-era shock still raw, chip shortages easing but not resolved, war in Ukraine one year in, ESG and Scope-3 reporting regulation (EU CSRD) just finalised, and ChatGPT three months old (so "GenAI in the supply chain" is conversation but not product). The placements below reflect that moment.

---

## The map (OWM)

```owm
title Modern Manufacturing Supply Chain (Feb 2023)
style wardley

// Anchors — two users: the end customer and the internal operator
anchor End Customer [0.99, 0.70]
anchor Operations Planner [0.96, 0.55]

// User-facing outputs and planner-facing cockpit
component Finished Goods [0.88, 0.88]
component Delivery Promise OTIF [0.82, 0.69]
component Production Plan Schedule [0.78, 0.75]
component Exception Control Tower [0.72, 0.44]

// Mid-chain domains
component Demand Forecasting [0.62, 0.44]
component S&OP Process [0.66, 0.69]
component Inventory Management [0.60, 0.75]
component Supplier Management [0.58, 0.625]
component Production Execution MES [0.55, 0.625]
component Quality Assurance [0.50, 0.75]
component Outbound Logistics [0.46, 0.875]
component Compliance Reporting [0.42, 0.375]

// Deeper supporting layer
component BOM Product Data [0.38, 0.75]
component Supplier Risk Platform [0.36, 0.48]
component Incoming Inspection [0.34, 0.625]
component WMS [0.33, 0.81]
component TMS [0.32, 0.625]
component Regulatory Rules Corpus [0.08, 0.625]
component Tier-N Supplier Mapping [0.28, 0.375]
component IoT Sensor Data [0.25, 0.625]

// Infrastructure layer
component Digital Product Passport [0.22, 0.22]
component Inbound Logistics Freight [0.20, 0.875]
component ERP [0.18, 0.875]
component EDI API Integrations [0.17, 0.875]
component Data Warehouse Lakehouse [0.15, 0.83]
component Labour Workforce [0.14, 0.75]
component Barcode RFID [0.13, 0.90]
component Shipping Carriers [0.12, 0.90]
component Raw Materials [0.11, 0.88]
component Customs Clearance [0.10, 0.85]
component Cloud Compute [0.09, 0.92]

// Foundational commodity
component Ports Shipping Lanes [0.06, 0.92]
component Electricity [0.05, 0.95]
component Lean Six Sigma [0.04, 0.92]
component Safety Stock Theory [0.03, 0.92]

// ---- Dependencies ----
// End Customer needs
End Customer->Finished Goods
End Customer->Delivery Promise OTIF
End Customer->Compliance Reporting

// Operations Planner needs
Operations Planner->Production Plan Schedule
Operations Planner->Exception Control Tower
Operations Planner->S&OP Process

// Finished Goods chain
Finished Goods->Production Execution MES
Finished Goods->Quality Assurance
Finished Goods->Outbound Logistics
Finished Goods->Raw Materials

// Delivery Promise chain
Delivery Promise OTIF->Inventory Management
Delivery Promise OTIF->Outbound Logistics
Delivery Promise OTIF->Production Plan Schedule

// Production Plan chain
Production Plan Schedule->Demand Forecasting
Production Plan Schedule->Inventory Management
Production Plan Schedule->Supplier Management
Production Plan Schedule->Production Execution MES
Production Plan Schedule->S&OP Process

// Exception / Control Tower chain
Exception Control Tower->Supplier Risk Platform
Exception Control Tower->IoT Sensor Data
Exception Control Tower->Data Warehouse Lakehouse

// S&OP feeds planning
S&OP Process->Demand Forecasting
S&OP Process->Inventory Management
S&OP Process->Supplier Management

// Demand Forecasting
Demand Forecasting->Data Warehouse Lakehouse
Demand Forecasting->ERP

// Inventory Management
Inventory Management->WMS
Inventory Management->ERP
Inventory Management->Safety Stock Theory

// Supplier Management
Supplier Management->Supplier Risk Platform
Supplier Management->Incoming Inspection
Supplier Management->EDI API Integrations
Supplier Management->Tier-N Supplier Mapping

// Production Execution (MES)
Production Execution MES->BOM Product Data
Production Execution MES->IoT Sensor Data
Production Execution MES->Labour Workforce
Production Execution MES->Electricity
Production Execution MES->Raw Materials
Production Execution MES->Lean Six Sigma

// Quality Assurance
Quality Assurance->Incoming Inspection
Quality Assurance->BOM Product Data
Quality Assurance->IoT Sensor Data
Quality Assurance->Lean Six Sigma

// Outbound Logistics
Outbound Logistics->TMS
Outbound Logistics->WMS
Outbound Logistics->Shipping Carriers
Outbound Logistics->Customs Clearance

// Compliance Reporting
Compliance Reporting->Regulatory Rules Corpus
Compliance Reporting->Digital Product Passport
Compliance Reporting->BOM Product Data
Compliance Reporting->Supplier Risk Platform
Compliance Reporting->Tier-N Supplier Mapping

// BOM Product Data
BOM Product Data->ERP
BOM Product Data->Digital Product Passport

// Supplier Risk Platform
Supplier Risk Platform->Tier-N Supplier Mapping
Supplier Risk Platform->Data Warehouse Lakehouse
Supplier Risk Platform->EDI API Integrations

// Incoming Inspection
Incoming Inspection->Inbound Logistics Freight
Incoming Inspection->Labour Workforce

// WMS
WMS->Barcode RFID
WMS->Labour Workforce
WMS->Cloud Compute

// TMS
TMS->Shipping Carriers
TMS->Cloud Compute
TMS->EDI API Integrations

// Tier-N Supplier Mapping
Tier-N Supplier Mapping->EDI API Integrations
Tier-N Supplier Mapping->Data Warehouse Lakehouse

// IoT Sensor Data
IoT Sensor Data->Cloud Compute
IoT Sensor Data->Data Warehouse Lakehouse

// Inbound Logistics Freight
Inbound Logistics Freight->Shipping Carriers
Inbound Logistics Freight->Customs Clearance
Inbound Logistics Freight->Ports Shipping Lanes

// ERP
ERP->Cloud Compute

// EDI API Integrations
EDI API Integrations->Cloud Compute

// Data Warehouse Lakehouse
Data Warehouse Lakehouse->Cloud Compute

// Shipping Carriers
Shipping Carriers->Ports Shipping Lanes
Shipping Carriers->Electricity

// Customs Clearance
Customs Clearance->Regulatory Rules Corpus

// Cloud Compute
Cloud Compute->Electricity

// Evolution arrows (scenarios)
evolve Demand Forecasting 0.65
evolve Supplier Risk Platform 0.68
evolve Digital Product Passport 0.50
evolve Exception Control Tower 0.62
evolve Tier-N Supplier Mapping 0.55

// Notes
note Differentiation zone [0.70, 0.30]
note Rent / Utility [0.15, 0.90]
note Compliance front [0.30, 0.25]
```

**Validator:** `OK: 37 components/anchors, 79 edges — no violations.`

---

## Strategic analysis

### a. Differentiation opportunities (top 3)

In rank order of where a manufacturer can meaningfully out-build competitors:

1. **Exception Control Tower (Custom Built)** — the ability to fuse IoT telemetry, supplier-risk signals, logistics events and production status into a *predictive* cockpit is the single biggest differentiation prize on this map. The 2020-22 shocks made every board ask "why didn't we see that coming?" — the winners of the next cycle will have answered it. Highest D on the chart.
2. **Demand Forecasting (Custom Built, transitioning toward Product +rental)** — the AI/ML variant is still Custom Built as of Feb 2023: 45 % adoption with another 43 % planning, but "still in early stages" with LSTM-style bespoke models dominating. If you are building, your forecasting stack is where reducing the 20-50 % error reduction McKinsey cites actually gets realised. Where you can beat the generic vendor.
3. **Compliance Reporting (Custom Built, edging Genesis on the DPP side)** — this looks like a cost centre, but in Feb 2023 it is a narrow differentiation window. EU CSRD is locked, Scope-3 disclosures are mandatory, Digital Product Passports are coming via ESPR. Whoever digitises product-level provenance first sells to Tier-1 OEMs who must pass the requirement down their chain.

### b. Commodity-leverage candidates (top 3)

These are Commodity (+utility) layers — rent them, do not build them:

1. **Electricity (Commodity +utility)** — utility; never engineer. Only strategic lever is energy sourcing (PPA / renewables) for Scope-2 reporting.
2. **Cloud Compute (Commodity +utility)** — AWS / Azure / GCP. Ending up on-prem in 2023 for anything other than regulated edge is a form of inertia, not a strategy.
3. **Ports & Shipping Lanes / Shipping Carriers (Commodity +utility)** — physical infrastructure. Use TMS to arbitrage carriers; do not try to own port capacity unless you are a Maersk-scale player.

Honourable mention: **ERP (Commodity +utility)** — SAP / Oracle / Microsoft / Infor are all Stage IV as systems; it is the *configuration* of your ERP, not the ERP itself, that has value.

### c. Dependency risks (top 3)

Edges where a visible component rests on an immature foundation:

1. **End Customer → Compliance Reporting (immature target, Custom Built at ε=0.375)** — the end customer (regulators, enterprise buyers, consumers) now demands provenance and sustainability disclosures, but the chain's ability to produce them rests on a Custom Built capability. This is the single highest R on the map: very visible user need, immature foundation.
2. **Production Plan Schedule → Demand Forecasting (Custom Built target)** — the entire production schedule rests on a forecasting layer that is still learning. When the forecast misses, everything downstream (inventory, supplier POs, logistics) misses too. This was the defining failure of 2020-22 for most manufacturers — the bullwhip went unchecked.
3. **Compliance Reporting → Digital Product Passport (Genesis target, ε=0.22)** — compliance depends on a data structure (DPP) that does not yet exist as a standardised layer. Battery Passport pilots running; ESPR framework set; but no universal implementation. Whoever scales first dictates the schema.

### d. Suggested gameplays (Wardley's 61)

- **#36 Directed investment** — concentrate engineering spend on **Exception Control Tower** and **Demand Forecasting** (the two highest-D components). This is where the moat forms.
- **#43 Sensing Engines (ILC)** — use **Supplier Risk Platform** data (Interos / Resilinc / Everstream) as your sensing engine for Tier-N disruption. Incubate an internal response playbook; harvest the best predictive signals.
- **#29 Harvesting** — let the **TMS** and **WMS** markets consolidate and buy the winners' APIs rather than building. Same for **Supplier Risk Platform** if you are a mid-cap — these vendors will consolidate post-Gartner Market Guide.
- **#15 Open Approaches** on **Digital Product Passport** / **Tier-N Supplier Mapping** — standardise the data schema with peers; do not try to own it. Regulation is the accelerant; move with the grain.
- **#41 Alliances** on **Raw Materials** (dual-source, near-shore options) and **Shipping Carriers** (multi-modal contingency). Direct response to the 2020-22 single-source fragility.
- **#45 Two factor** acknowledges the two-anchor shape: align the End Customer roadmap (delivery promise + compliance) with the Operations Planner roadmap (planning + exceptions). Features that serve both anchors have the highest leverage.
- **#56 First mover** on **Digital Product Passport** — ESPR and CSRD deadlines create a narrow window where compliance-as-a-feature becomes sales-as-a-feature to regulated buyers.
- **#26 Differentiation** via the **Exception Control Tower** experience — this is the user-facing cockpit your Operations Planner lives in.

### e. Doctrine notes

- ✓ **#1 Focus on user needs** — anchoring on End Customer and Operations Planner is correct; a single anchor would have suppressed the build/buy signal on internal tooling.
- ✓ **#10 Know your users** — two anchors, matched to the two-sided decision problem (delivery + compliance on one side, planning + exceptions on the other).
- ⚠ **#11 Use appropriate methods** — many manufacturers still apply Stage III/IV methods (six sigma, fixed budgets, stage-gate) to Stage I/II components like DPP and AI-forecasting. This is the classic doctrine violation in industrial IT.
- ⚠ **#13 Manage inertia** — ERP sunk-cost (inertia form #2 *past-capital*, #9 *re-architecture cost*) will block your Exception Control Tower if you try to make the ERP vendor build it. Build the tower as a separate plane, reading from ERP via integration.
- ⚠ **#2 Use a systematic mechanism of learning** — if Demand Forecasting errors are not being fed back to retrain the model, the forecast layer cannot move toward Stage III. Shut the loop.
- ⚠ **#30 Think small** — "one forecasting platform" is usually wrong; different SKU classes need different models. Modularise.

### f. Climatic context

Which of the 27 climatic patterns are visibly shaping this map in Feb 2023:

- **#3 Everything evolves** — the chain is mid-transition across multiple components (forecasting, risk platforms, DPP, control towers). No part stays still.
- **#15-17 Inertia** — the 2020-22 shock *broke* inertia on supplier diversification, near-shoring, and visibility tooling. Budgets that were unavailable in 2019 are flowing in 2023. Seize the window.
- **#18 You cannot measure evolution over time or adoption** — directly relevant: the `evolve` arrows below are scenarios, not forecasts.
- **#19 Efficiency enables innovation** — commoditising the logistics layer (TMS, WMS, carriers) frees engineering capacity for the control tower and forecasting differentiation.
- **#27 Product-to-utility punctuated equilibrium** — two active wars: MES (Product → early utility via cloud SaaS) and Supplier Risk (Custom Built → Product, with vendor consolidation looming).
- **#22 Change is not always linear** — chip shortage behaviour 2020-22 is a textbook example. The map must support non-linear shock scenarios, which is why Exception Control Tower is a Stage II bet, not a Stage IV dashboard.
- **#26 Most competitors have poor situational awareness** — the same reason mapping the chain at all is a competitive act.

### g. Deep-placement notes

Four components warranted targeted research; the initial cheat-sheet placements were checked against current evidence.

1. **Demand Forecasting — confirmed in transition, kept at ε ≈ 0.44 (Custom Built).** Research confirmed 45 % adoption with 43 % planning (so ubiquity is rising fast — Stage III on that row), but the literature explicitly states "AI in demand planning is still in its early stages of development" and LSTM-style bespoke modelling dominates (Certainty row, Publication row both Stage II). Rows disagreed — kept the placement at Custom Built with a short `evolve` arrow to 0.65 (early Product +rental) over the next ~3 years. This is a component where "in transition" is the correct label, not a point estimate.

2. **Supplier Risk Platform — kept at ε ≈ 0.48 (boundary Custom/Product).** Gartner's *2023 Market Guide* for Supplier Risk Management Solutions names Interos, Resilinc, Everstream and peers as representative vendors; a *Market Guide* rather than a *Magic Quadrant* is the signal that the category is pre-consolidation (Stage II late / Stage III early). Features are converging (multi-tier visibility, risk scoring) but vendor shake-out has not yet happened. Evolution arrow to 0.68 reflects expected consolidation.

3. **Digital Product Passport — kept at ε ≈ 0.22 (late Genesis / early Custom).** EU Ecodesign for Sustainable Products Regulation (ESPR) is the master framework; the Battery Passport is the first live pilot, with textiles, construction products and other categories scheduled. This is a component where "publication types describe the wonder" (Stage I Pub row) coexists with "regulatory deadlines create a forced implementation" (Stage II–III Market row). The regulatory forcing function is why the evolve arrow is aggressive (to 0.50 — Product +rental) over 3-5 years.

4. **Manufacturing Execution System (MES) — confirmed at ε ≈ 0.625 (Product +rental).** $15 B 2023 market, 10 %+ CAGR, 5+ major vendors (Siemens, Rockwell/Plex, SAP, Dassault, Honeywell, GE Vernova) plus cloud-native entrants like Tulip. Cloud/SaaS variant growing fastest but still minority of deployments. Product (+rental) placement is stable; no shift needed.

### h. Caveat

All evolution trajectories (the `evolve` arrows — Demand Forecasting → 0.65, Supplier Risk → 0.68, DPP → 0.50, Control Tower → 0.62, Tier-N Mapping → 0.55) are **scenarios, not forecasts**. Wardley's climatic pattern #18 stands: *you cannot measure evolution over time or adoption.* They are where the map *suggests* these components will sit if current forcing functions (regulation, post-COVID budget priorities, AI/ML vendor maturation) hold. They are not commitments and they will drift as reality drifts.

---

## Where the chain is fragile — and what is differentiating vs commoditising

**Fragile (the short answer):**
- **Tier-N visibility** — most manufacturers still do not know who their suppliers' suppliers are. The chain breaks at the tier you cannot see. Stage II component carrying Stage IV obligations.
- **Demand signal** — the link from market reality to production plan is still Custom Built and failing under non-linear shocks (chip allocation, pandemic, war-driven commodity spikes). Where 2020-22 broke the industry and is still the biggest single leverage point.
- **Raw materials and energy** — geopolitically exposed inputs with no buffers. The map places them as Commodity +utility because that is what they *are* — but commodity pricing can spike non-linearly, and a single-source commodity is still a single point of failure.
- **Labour / workforce** — scored as Product-stage because in most jurisdictions skilled manufacturing labour is scarce (not yet commoditised through automation). Quietly fragile.
- **Compliance layer** — now user-visible (End Customer → Compliance Reporting) but built on Custom / Genesis foundations (DPP, Tier-N mapping, Scope-3 accounting).

**Differentiating (build here):**
- Exception Control Tower
- Demand Forecasting (AI/ML variant)
- Compliance Reporting (as a compete-for-regulated-buyer feature, not a cost centre)
- Supplier Management (the process, not the platform)

**Commoditising (rent, do not build):**
- MES (Product +rental — active Product → Commodity transition via cloud SaaS)
- TMS, WMS (Product +rental, trending Commodity)
- Supplier Risk Platforms (Custom / Product — rent the platform, own the response playbook)
- ERP, Cloud, EDI, Electricity, Ports, Shipping Carriers, Customs — Commodity (+utility) all the way down.

The honest answer to "where is the moat?" in a modern manufacturing chain is: **in the prediction and response layer that sits above a rented operational stack.** Everything under Production Execution MES is either already commodity or heading there fast; the value is in seeing sooner and responding smarter than the competitor whose stack looks identical to yours.
