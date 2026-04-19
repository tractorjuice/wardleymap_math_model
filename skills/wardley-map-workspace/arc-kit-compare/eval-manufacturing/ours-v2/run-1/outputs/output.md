# Manufacturing Supply Chain — Wardley Map (Feb 2023)

Scenario: Discrete-manufacturing OEM (electronics / automotive / industrial equipment), mid-2023 vantage. Two user needs, two anchors:

- **End-Customer** — cost & reliability of the finished product
- **Supply-Chain Org** — resilience & agility of the sourcing / production / logistics network

## Map (OWM)

```owm
title Manufacturing Supply Chain (Feb 2023)
style wardley

// Two anchors — two distinct user needs
anchor End-Customer (Cost & Reliability) [0.98, 0.80]
anchor Supply-Chain Org (Resilience & Agility) [0.97, 0.35]

// User-facing outcomes / differentiators
component Finished Product Delivery [0.88, 0.70]
component Order Fulfilment & Lead Time [0.85, 0.55]
component Aftermarket & Spares [0.80, 0.60]
component Supplier Risk & Resilience Program [0.82, 0.25]
component Demand & S&OP Planning [0.78, 0.45]
component Supply Chain Control Tower [0.75, 0.30]
component Scenario Modelling & Digital Twin [0.72, 0.22]

// Production
component Final Assembly [0.68, 0.60]
component Sub-assembly & Kitting [0.62, 0.65]
component Contract Manufacturing (EMS/ODM) [0.58, 0.70]
component Quality & Inspection [0.55, 0.65]
component Plant MES / Shop-floor Control [0.52, 0.55]
component Industrial Automation & Robotics [0.48, 0.70]
component Factory IIoT Sensing [0.40, 0.35]
component Predictive Maintenance [0.45, 0.35]

// Sourcing
component Strategic Sourcing & Contracts [0.65, 0.55]
component Tier-1 Supplier Relationships [0.60, 0.40]
component Tier-N Supplier Mapping [0.55, 0.25]
component Dual / Multi-sourcing Strategy [0.52, 0.30]
component PCBAs & Passives [0.55, 0.78]
component Semiconductors (MCU/Analog/Power) [0.50, 0.55]
component Leading-edge Logic Chips [0.48, 0.30]
component Raw Materials (Steel, Al, Cu, Plastics) [0.45, 0.85]
component Critical Minerals (Li, Co, Ni, REE) [0.38, 0.25]

// Logistics
component Ocean Freight [0.35, 0.80]
component Air Freight [0.32, 0.82]
component Road & Rail Haulage [0.30, 0.85]
component Warehousing & 3PL [0.42, 0.75]
component Customs Brokerage & Trade Compliance [0.38, 0.70]
component Inventory Buffers & Safety Stock [0.48, 0.55]

// Digital tooling (supply-chain-org facing)
component ERP (SAP/Oracle) [0.40, 0.75]
component PLM (Siemens/PTC/Dassault) [0.38, 0.65]
component Supplier Relationship Mgmt / e-Sourcing [0.48, 0.60]
component Supply Chain Visibility Platform [0.42, 0.40]
component AI Demand Forecasting [0.40, 0.30]
component EDI / API Integration [0.28, 0.75]

// Compliance
component ESG / Scope-3 Reporting [0.58, 0.30]
component Conflict-minerals & Forced-labour Due Dil. [0.58, 0.35]
component Export Controls (ITAR/EAR/China) [0.35, 0.55]
component IRA / CHIPS Act Compliance [0.68, 0.20]

// Utility / commodity foundations
component Cloud Compute & Storage [0.18, 0.92]
component Connectivity (4G/5G/Fibre) [0.15, 0.95]
component Electricity & Energy [0.10, 0.95]
component Shipping Containers & Ports [0.20, 0.90]

// Inertia
component Legacy ERP Customisations [0.45, 0.55] inertia

// Dependencies — End-customer side (cost/reliability)
End-Customer (Cost & Reliability)->Finished Product Delivery
End-Customer (Cost & Reliability)->Order Fulfilment & Lead Time
End-Customer (Cost & Reliability)->Aftermarket & Spares
Finished Product Delivery->Final Assembly
Finished Product Delivery->Road & Rail Haulage
Order Fulfilment & Lead Time->Warehousing & 3PL
Order Fulfilment & Lead Time->Demand & S&OP Planning
Aftermarket & Spares->Warehousing & 3PL
Aftermarket & Spares->Contract Manufacturing (EMS/ODM)

// Dependencies — Supply-chain-org side (resilience/agility)
Supply-Chain Org (Resilience & Agility)->Supplier Risk & Resilience Program
Supply-Chain Org (Resilience & Agility)->Supply Chain Control Tower
Supply-Chain Org (Resilience & Agility)->Scenario Modelling & Digital Twin
Supply-Chain Org (Resilience & Agility)->Demand & S&OP Planning
Supply-Chain Org (Resilience & Agility)->Dual / Multi-sourcing Strategy
Supplier Risk & Resilience Program->Tier-N Supplier Mapping
Supplier Risk & Resilience Program->Dual / Multi-sourcing Strategy
Supplier Risk & Resilience Program->Strategic Sourcing & Contracts
Supply Chain Control Tower->Supply Chain Visibility Platform
Supply Chain Control Tower->AI Demand Forecasting
Scenario Modelling & Digital Twin->AI Demand Forecasting
Scenario Modelling & Digital Twin->Supply Chain Visibility Platform
Demand & S&OP Planning->AI Demand Forecasting
Demand & S&OP Planning->ERP (SAP/Oracle)
Demand & S&OP Planning->Inventory Buffers & Safety Stock
Demand & S&OP Planning->Legacy ERP Customisations

// Production chain
Final Assembly->Sub-assembly & Kitting
Final Assembly->Contract Manufacturing (EMS/ODM)
Final Assembly->Quality & Inspection
Final Assembly->Plant MES / Shop-floor Control
Final Assembly->Industrial Automation & Robotics
Sub-assembly & Kitting->PCBAs & Passives
Sub-assembly & Kitting->Raw Materials (Steel, Al, Cu, Plastics)
Contract Manufacturing (EMS/ODM)->Plant MES / Shop-floor Control
Plant MES / Shop-floor Control->Factory IIoT Sensing
Predictive Maintenance->Factory IIoT Sensing
Industrial Automation & Robotics->Electricity & Energy
Quality & Inspection->PLM (Siemens/PTC/Dassault)

// Sourcing chain
Strategic Sourcing & Contracts->Tier-1 Supplier Relationships
Strategic Sourcing & Contracts->Supplier Relationship Mgmt / e-Sourcing
Tier-1 Supplier Relationships->Tier-N Supplier Mapping
Tier-1 Supplier Relationships->Semiconductors (MCU/Analog/Power)
Tier-1 Supplier Relationships->PCBAs & Passives
Tier-1 Supplier Relationships->Raw Materials (Steel, Al, Cu, Plastics)
PCBAs & Passives->Semiconductors (MCU/Analog/Power)
PCBAs & Passives->Leading-edge Logic Chips
Semiconductors (MCU/Analog/Power)->Critical Minerals (Li, Co, Ni, REE)
Leading-edge Logic Chips->Critical Minerals (Li, Co, Ni, REE)
Raw Materials (Steel, Al, Cu, Plastics)->Critical Minerals (Li, Co, Ni, REE)

// Logistics chain
Warehousing & 3PL->Ocean Freight
Warehousing & 3PL->Air Freight
Warehousing & 3PL->Road & Rail Haulage
Warehousing & 3PL->Customs Brokerage & Trade Compliance
Ocean Freight->Shipping Containers & Ports
Air Freight->Shipping Containers & Ports
Customs Brokerage & Trade Compliance->Export Controls (ITAR/EAR/China)
Inventory Buffers & Safety Stock->Warehousing & 3PL

// Digital tooling chain
ERP (SAP/Oracle)->Cloud Compute & Storage
PLM (Siemens/PTC/Dassault)->Cloud Compute & Storage
Supplier Relationship Mgmt / e-Sourcing->ERP (SAP/Oracle)
Supply Chain Visibility Platform->EDI / API Integration
Supply Chain Visibility Platform->Cloud Compute & Storage
AI Demand Forecasting->Cloud Compute & Storage
EDI / API Integration->Connectivity (4G/5G/Fibre)
Factory IIoT Sensing->Connectivity (4G/5G/Fibre)
Plant MES / Shop-floor Control->ERP (SAP/Oracle)

// Compliance chain
ESG / Scope-3 Reporting->Tier-N Supplier Mapping
ESG / Scope-3 Reporting->Supply Chain Visibility Platform
Conflict-minerals & Forced-labour Due Dil.->Tier-N Supplier Mapping
IRA / CHIPS Act Compliance->Strategic Sourcing & Contracts
IRA / CHIPS Act Compliance->Critical Minerals (Li, Co, Ni, REE)

// Inertia dependency
Legacy ERP Customisations->ERP (SAP/Oracle)

// Evolve targets (scenarios, not forecasts)
evolve AI Demand Forecasting 0.55
evolve Supply Chain Visibility Platform 0.60
evolve ESG / Scope-3 Reporting 0.60
evolve Leading-edge Logic Chips 0.55
evolve Tier-N Supplier Mapping 0.50

note BUILD moat zone [0.75, 0.20]
note RENT / utility [0.15, 0.92]
note Chip & mineral risk [0.48, 0.22]
```

Validator: **OK — 47 components/anchors, 71 edges, no visibility violations.**

---

## Strategic Analysis

### a. Differentiation opportunities (top 3)

1. **Supplier Risk & Resilience Program** (Genesis / Custom Built, ε ≈ 0.25) — high-visibility node for the supply-chain org, still Genesis-ish in Feb 2023. Post-COVID and Ukraine, every OEM is scrambling to build it; very few have a mature one. Doing this well is a *strategic control point* for the OEM because it touches Tier-N mapping, dual-sourcing, and compliance simultaneously. Highest differentiation leverage on the map.
2. **Scenario Modelling & Digital Twin** (Genesis, ε ≈ 0.22) — visible to the supply-chain-org anchor, no settled methodology in discrete manufacturing. Vendors are emerging (Kinaxis RapidResponse, o9, Coupa LLamasoft) but this is still Genesis-to-Custom. A proprietary digital twin of the OEM's own network is a durable moat.
3. **Supply Chain Control Tower** (Custom Built, ε ≈ 0.30) — consolidates visibility, risk and response. Vendor landscape is fragmenting; OEM-specific integration work still highly bespoke. On the Custom Built → Product boundary; early-mover advantage available.

### b. Commodity-leverage candidates (top 3)

1. **Cloud Compute & Storage** (Commodity +utility, ε ≈ 0.92) — rent from hyperscalers; never build.
2. **Electricity & Energy** and **Connectivity (4G/5G/Fibre)** (Commodity +utility) — pure utility; procure, don't engineer. (Energy price volatility in 2023 is a procurement question, not a commoditisation question.)
3. **Raw Materials (Steel, Al, Cu, Plastics)** (Commodity +utility, ε ≈ 0.85) — traded commodities with spot / futures markets; hedging beats vertical integration. **Road & Rail Haulage** and **Shipping Containers & Ports** also sit here and should be bought as utility services.

(Honourable mention: **Ocean Freight** / **Air Freight** are Commodity +utility in the steady state but experienced Stage III-like pricing spikes in 2021–2022; Feb 2023 is on the easing side of that.)

### c. Dependency risks (top 3)

1. **Final Assembly → Leading-edge Logic Chips → Critical Minerals** — a user-visible production step ultimately resting on Genesis-placed upstream nodes concentrated in a handful of geographies. This is the defining risk of 2023. The chip shortage in Feb 2023 is partially eased on automotive MCUs but ongoing on leading-edge logic; and the minerals that feed both are in Genesis/Custom with very concentrated geography (lithium in Chile/Australia, cobalt in DRC, rare earths in China).
2. **Order Fulfilment & Lead Time → Demand & S&OP Planning → Legacy ERP Customisations** — a highly visible customer-outcome node hangs on an inertia-flagged legacy ERP layer. Re-architecture cost (inertia form #9) blocks any adoption of modern forecasting.
3. **Supplier Risk & Resilience Program → Tier-N Supplier Mapping** — the whole resilience narrative depends on visibility into sub-tier suppliers, which is still Genesis. You cannot manage what you cannot see; most OEMs have visibility to Tier-1 and guess below that.

Other notable risks: **Finished Product Delivery → Road & Rail Haulage** is actually *low* risk (commodity utility) but **Aftermarket & Spares → Contract Manufacturing** carries concentration risk on a handful of EMS/ODM vendors (Foxconn, Jabil, Flex).

### d. Suggested gameplays (from the 61)

- **#41 Alliances** on **Tier-1 Supplier Relationships** and **Semiconductors** — long-term supply agreements + equity stakes are the Feb 2023 pattern (Ford–GlobalFoundries, VW–ST, Stellantis–minerals).
- **#36 Directed investment** on **Supplier Risk & Resilience Program**, **Scenario Modelling & Digital Twin**, and **Supply Chain Control Tower** — these are the three highest-D nodes on the map.
- **#45 Two factor** — recognise the map's intrinsic two-sided shape (end-customer cost/reliability vs. supply-chain-org resilience/agility) and invest in both anchors, not just one.
- **#15 Open Approaches** on **ESG / Scope-3 Reporting** and **Tier-N Supplier Mapping** — industry-wide schemas (Catena-X in automotive, PACT network for carbon, WBCSD PIF) accelerate Custom Built → Product and force competitors onto the same standard.
- **#29 Harvesting** on **AI Demand Forecasting** and **Supply Chain Visibility Platform** — let vendors (o9, Project44, FourKites, Kinaxis) fight it out; buy the winner's API, don't build the engine.
- **#56 First mover** on **IRA / CHIPS Act Compliance** — 2022 legislation, 2023–2024 procurement deadlines; early claimants capture subsidy flows and preferential supplier status.
- **#46 Pricing policy / sensibility** on **Inventory Buffers & Safety Stock** — the JIT-to-JIC shift is a cost-structure decision; price it explicitly rather than letting inventory accumulate.
- **#9 Embrace constraint** on **Critical Minerals** — do not pretend you can solve mineral concentration; instead design around it (LFP cathodes, sodium-ion, cobalt-free chemistries).

### e. Doctrine violations / notes

- ✓ **#1 Focus on user needs** and **#10 Know your users** — two anchors correctly model the two distinct user needs (end-customer cost/reliability vs. supply-chain-org resilience/agility).
- ✓ **#13 Manage inertia** — explicit inertia flag on **Legacy ERP Customisations**, with the dependency edge showing the planning layer is captured by it.
- ⚠ **#14 Use appropriate methods** — risk of running commodity logistics with bespoke processes (six-sigma fits; agile doesn't) while running Supplier Risk with a waterfall (should be FIRE / small teams). Check the method allocation matches each stage.
- ⚠ **#19 Use standards where appropriate** — if the OEM builds its own ESG Scope-3 data model instead of adopting Catena-X / PACT, it violates this doctrine.
- ⚠ **#23 Be pragmatic** — some OEMs are tempted to re-shore everything. Don't. Reshore the high-D nodes (leading-edge chips, critical minerals) and keep the commodity logistics utility-sourced.
- ⚠ **#25 Think small (team / contract / component)** — Supplier Risk & Digital Twin should be small-team FIRE work, not a multi-year SI engagement.

### f. Climatic context (which of the 27 patterns are active)

- **#3 Everything evolves** — driving the Custom-Built → Product shift in visibility platforms, demand forecasting, and Scope-3.
- **#11 Change is not always linear** — the chip shortage is a *punctuated* event, not smooth evolution.
- **#13 No choice over evolution** — OEMs cannot opt out of ESG Scope-3 once the EU CSRD mandates it; cannot opt out of IRA FEOC rules if they want US EV tax credits.
- **#15 Inertia** — legacy ERP and decades of single-sourcing relationships resist the resilience pivot. Explicitly modelled on the map.
- **#17 Co-evolution of practice with activity** — lean / JIT practices co-evolved with globally-commoditised logistics; both are being rewritten together toward JIC / nearshoring / multi-sourcing.
- **#18 You cannot measure evolution over time or adoption** — explicitly applies to every `evolve` arrow on this map.
- **#22 Capital flows from old to new** — IRA + CHIPS Acts are *policy-induced* capital redirection from legacy geography to new geography; the map's location dimension is being rewritten.
- **#27 Product-to-utility (punctuated equilibrium)** — actively shaping Supply Chain Visibility Platforms and Scope-3 reporting: both are transitioning from Custom Built implementations to Product / SaaS.

### g. Deep-placement notes

Four targeted placements reviewed beyond the default cheat-sheet priors:

- **Leading-edge Logic Chips** (placed ε = 0.30, Custom Built). Initial instinct "these are products, so Stage III". Correction: *leading-edge* (≤5nm) logic in Feb 2023 has effectively one supplier at volume (TSMC) with US/EU/JP fabs being built under CHIPS Act subsidy — ubiquity is low, market is forming/re-forming, certainty of supply is poor. That's Custom Built, not Product. **Mature** silicon (automotive MCUs, analog, power) is separate and sits at ε ≈ 0.55 (Product +rental).
- **ESG / Scope-3 Reporting** (placed ε = 0.30, Custom Built with evolve → 0.60). EU CSRD adopted Nov 2022, applying from FY2024; vendor landscape (Watershed, Sweep, Persefoni, Plan A, SAP Sustainability Footprint Mgmt, Salesforce Net Zero Cloud) is fragmenting fast; Catena-X (automotive) going live 2023. Publication types are still "build/construct/awareness" — firmly Custom Built, but mandatory timelines are forcing rapid industrialisation. Evolve to 0.60 in a 2-3-year horizon.
- **AI Demand Forecasting** (placed ε = 0.30, Custom Built with evolve → 0.55). Vendors exist (o9, Blue Yonder Luminate, Kinaxis, SAP IBP) but each deployment is still a bespoke model-tuning exercise; industry case studies emerging but no "best practice" playbook. Genesis-era differentiation on the model itself is ending as foundation-model-based time-series forecasting arrives. Moving towards Product.
- **Critical Minerals (Li, Co, Ni, REE)** (placed ε = 0.25). Counter-intuitive — minerals are an ancient commodity in principle, but for EV-grade battery inputs at the volumes needed post-2022, the supply chains, refinement capacity, and geographic concentration are not yet a mature utility. Pricing is volatile, contracts are bespoke, new mines have 8-12-year lead times. Treat this closer to Custom than to Commodity for planning purposes — the "mineral" is commodity, the "secure EV-grade supply at scale" is not.

### h. Caveat

Every `evolve` arrow on this map is a **scenario, not a forecast**. Wardley's climatic pattern #18 stands: *"you cannot measure evolution over time or adoption."* The Feb 2023 vantage means IRA / CHIPS effects, CSRD mandates, and chip-shortage easing are still in early innings; a 2024 or 2025 snapshot will place several of these components differently.
