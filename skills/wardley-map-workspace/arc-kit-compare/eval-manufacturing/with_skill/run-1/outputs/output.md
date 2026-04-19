# Wardley Map: Modern Manufacturing Supply Chain (Feb 2023)

## Pre-flight: Assumptions (standing in for AskUserQuestion)

The skill uses AskUserQuestion in Step 1; no human user is available. Frozen assumptions for this run:

- Org: Discrete-manufacturing OEM (electronics / automotive / industrial equipment), mid-large, multi-national.
- Two anchors (from scenario brief): End Customer (cost / reliability) + Supply-Chain Organisation (resilience / agility).
- Scope: Entire supply chain - sourcing, production, logistics, digital tooling, compliance, supplier relationships.
- Primary goal: competitive-position + dependency-risk + investment-priority assessment.
- Depth: deep (~34 components) with gameplay + climatic commentary.
- Feb-2023 context: chip shortage partially eased, mature-node MCU/power/analog still constrained; Ukraine war year-two (energy, neon, palladium, wiring harnesses); IRA + CHIPS (both Aug 2022) reshaping US fab/EV/battery investment; CSRD adopted late 2022 making scope-3 mandatory for large EU-operating firms.
- Evolution positioning based on global market maturity, not internal familiarity.

---

## Arc-Kit YAML Output

```yaml
wardley_map:
  metadata:
    title: "Modern Manufacturing Supply Chain - Discrete OEM (Feb 2023)"
    author: "Benchmark run - arc-kit-compare skill"
    date: "2023-02-15"
    version: "1.0"
    scope: "End-to-end supply chain: sourcing, production, logistics, digital, compliance, supplier relationships."

  anchors:
    - user: "End Customer"
      need: "Reliable finished product at expected cost, quality, and lead time"
    - user: "Supply-Chain Organisation"
      need: "Resilience + agility - continuity of supply through shocks, ability to reconfigure rapidly"

  components:
    - {name: "Finished Product", evolution: Product, position: 0.65, visibility: 0.92, depends_on: ["Final Assembly","Order Fulfilment and Last-Mile","Quality Assurance"], movement: evolving}
    - {name: "Order Fulfilment and Last-Mile", evolution: Product, position: 0.72, visibility: 0.88, depends_on: ["Outbound Logistics 3PL","Warehousing and DCs"], movement: evolving}
    - {name: "Demand Forecasting and SOP", evolution: Product, position: 0.60, visibility: 0.85, depends_on: ["ERP","Supplier Collaboration Portal","AI/ML Demand Sensing"], movement: evolving}
    - {name: "Supply-Chain Risk Management", evolution: Custom, position: 0.42, visibility: 0.90, depends_on: ["Supplier Risk Intelligence","Digital Twin of Supply Chain","Multi-Sourcing and Nearshoring","Inventory Buffering Policy"], movement: accelerating}
    - {name: "Multi-Sourcing and Nearshoring", evolution: Custom, position: 0.38, visibility: 0.86, depends_on: ["Supplier Qualification","Geopolitical Intelligence"], movement: accelerating}
    - {name: "Final Assembly", evolution: Product, position: 0.66, visibility: 0.75, depends_on: ["Sub-Assembly Manufacturing","MES","Skilled Production Labour","Factory Energy Supply"], movement: evolving}
    - {name: "Sub-Assembly Manufacturing", evolution: Product, position: 0.64, visibility: 0.65, depends_on: ["Tier-1 Suppliers","Components and Parts Inventory","CNC IM SMT Lines"], movement: evolving}
    - {name: "MES", evolution: Product, position: 0.68, visibility: 0.55, depends_on: ["Industrial IoT Sensors","OT Network"], notes: "Siemens Opcenter, Rockwell, AVEVA", movement: evolving}
    - {name: "Industrial IoT Sensors", evolution: Product, position: 0.70, visibility: 0.40, depends_on: ["OT Network"], movement: evolving}
    - {name: "Digital Twin of Supply Chain", evolution: Custom, position: 0.32, visibility: 0.62, depends_on: ["ERP","Industrial IoT Sensors","AI/ML Demand Sensing"], movement: accelerating}
    - {name: "AI/ML Demand Sensing", evolution: Custom, position: 0.40, visibility: 0.70, depends_on: ["ERP","Cloud Compute"], movement: accelerating}
    - {name: "Tier-1 Suppliers", evolution: Product, position: 0.60, visibility: 0.55, depends_on: ["Tier-N Suppliers","Critical Raw Materials","Semiconductors"], movement: evolving}
    - {name: "Tier-N Suppliers", evolution: Commodity, position: 0.78, visibility: 0.35, depends_on: ["Critical Raw Materials"], notes: "Hide concentration risk - neon, harnesses, REEs", movement: evolving}
    - {name: "Semiconductors", evolution: Product, position: 0.58, visibility: 0.45, depends_on: ["TSMC Global Fabs","Critical Raw Materials"], notes: "DEPENDENCY RISK - mature-node MCU/power/analog still constrained Feb 2023", movement: accelerating}
    - {name: "TSMC Global Fabs", evolution: Commodity, position: 0.82, visibility: 0.20, depends_on: ["Critical Raw Materials","Factory Energy Supply"], notes: "SINGLE-SOURCE RISK - TSMC ~90% leading-edge + Taiwan geopolitical", movement: inertia}
    - {name: "Critical Raw Materials", evolution: Commodity, position: 0.85, visibility: 0.15, depends_on: [], notes: "DEPENDENCY RISK - DRC cobalt, China REEs, Russia palladium, Ukraine neon", movement: evolving}
    - {name: "Supplier Qualification", evolution: Product, position: 0.55, visibility: 0.50, depends_on: ["ESG Scope-3 Compliance","Quality Assurance"], movement: evolving}
    - {name: "Supplier Collaboration Portal", evolution: Product, position: 0.68, visibility: 0.58, depends_on: ["ERP","Cloud Compute"], movement: evolving}
    - {name: "Supplier Risk Intelligence", evolution: Custom, position: 0.45, visibility: 0.72, depends_on: ["Geopolitical Intelligence","Cloud Compute"], notes: "Everstream, Resilinc, Interos - emerging product category", movement: accelerating}
    - {name: "Geopolitical Intelligence", evolution: Custom, position: 0.30, visibility: 0.55, depends_on: [], movement: accelerating}
    - {name: "Inbound Logistics and Freight", evolution: Commodity, position: 0.80, visibility: 0.50, depends_on: ["Container Shipping Ocean Freight"], movement: evolving}
    - {name: "Container Shipping Ocean Freight", evolution: Commodity, position: 0.88, visibility: 0.30, depends_on: [], notes: "LONG LEAD TIMES structural risk", movement: evolving}
    - {name: "Outbound Logistics 3PL", evolution: Commodity, position: 0.82, visibility: 0.78, depends_on: ["Container Shipping Ocean Freight"], movement: evolving}
    - {name: "Warehousing and DCs", evolution: Product, position: 0.72, visibility: 0.68, depends_on: [], movement: evolving}
    - {name: "Components and Parts Inventory", evolution: Product, position: 0.62, visibility: 0.50, depends_on: ["Tier-1 Suppliers","Warehousing and DCs"], notes: "JIT -> just-in-case transition", movement: inertia}
    - {name: "Inventory Buffering Policy", evolution: Custom, position: 0.40, visibility: 0.75, depends_on: ["Components and Parts Inventory","AI/ML Demand Sensing"], notes: "Classic inertia site", movement: accelerating}
    - {name: "ERP", evolution: Product, position: 0.70, visibility: 0.45, depends_on: ["Cloud Compute"], notes: "SAP S/4, Oracle, MS Dynamics", movement: evolving}
    - {name: "Cloud Compute", evolution: Commodity, position: 0.90, visibility: 0.15, depends_on: [], movement: none}
    - {name: "OT Network", evolution: Product, position: 0.72, visibility: 0.25, depends_on: [], movement: evolving}
    - {name: "ESG Scope-3 Compliance", evolution: Custom, position: 0.35, visibility: 0.65, depends_on: ["Supplier Collaboration Portal"], notes: "CSRD late 2022 mandates scope-3 in EU", movement: accelerating}
    - {name: "Quality Assurance", evolution: Product, position: 0.70, visibility: 0.60, depends_on: ["MES"], notes: "IATF 16949, ISO 9001", movement: evolving}
    - {name: "Skilled Production Labour", evolution: Custom, position: 0.30, visibility: 0.50, depends_on: [], notes: "Post-COVID shortages - regional, scarce, inertia source", movement: inertia}
    - {name: "Factory Energy Supply", evolution: Commodity, position: 0.82, visibility: 0.30, depends_on: [], notes: "Ukraine war made EU energy volatile", movement: inertia}
    - {name: "CNC IM SMT Lines", evolution: Product, position: 0.72, visibility: 0.45, depends_on: [], notes: "Fanuc, Haas, ASM - long lead times", movement: evolving}

  analysis:
    opportunities:
      - "Productise supplier risk intelligence - multi-tier visibility shifting custom-to-product."
      - "Digital twin of supply chain: custom-stage, differentiator candidate for resilience."
      - "Nearshoring / dual-sourcing under IRA + CHIPS subsidies 2023-25."
      - "AI/ML demand sensing: GenAI accelerates custom-to-product; early adopters gain 18-24 months."
      - "Scope-3 / ESG reporting tooling: CSRD mandate makes this both compliance AND differentiation."
    threats:
      - "Single-source risk on advanced-node semiconductors (TSMC ~90%) + Taiwan geopolitical tail risk."
      - "Critical raw materials concentration - DRC cobalt, China REEs, Russia palladium, Ukraine neon."
      - "Mature-node MCU/power/analog chip shortage still biting Feb 2023."
      - "Long ocean-freight lead times + price volatility undermine JIT dogma."
      - "Skilled production labour scarcity blocks nearshoring plans."
      - "Scope-3 mandate creates compliance overhead without immediate revenue upside."
    inertia_points:
      - {component: "Inventory Buffering Policy", reason: "Two decades of lean/JIT orthodoxy and CFO KPIs"}
      - {component: "TSMC Global Fabs", reason: "Structural - no western replacement before 2025-26; fabs take 4-5y"}
      - {component: "Skilled Production Labour", reason: "Demographic - trade-skill pipeline hollowed out for 30 years"}
      - {component: "Factory Energy Supply", reason: "EU energy cost structure broken by 2022 war"}
      - {component: "Components and Parts Inventory", reason: "JIT capex/working-capital incentives fight buffer stock"}

  recommendations:
    immediate:
      - "Multi-tier supplier visibility for top 50 Tier-1s - fastest ROI on resilience."
      - "Dual-source any single-source Tier-2 chip exposure, 12-month roadmap."
      - "CSRD / scope-3 data plumbing project - reporting lands 2024/25 first cohort."
    short_term:
      - "Digital twin pilot on one product family, 12-month payback via inventory optimisation."
      - "Nearshoring feasibility study under IRA / CHIPS subsidies."
      - "Shift inventory policy from pure JIT to tiered just-in-case for strategic components."
    long_term:
      - "Treat geopolitical intelligence as first-class capability."
      - "AI/ML demand sensing on ERP data - table-stakes by 2025-26."
      - "Skilled-trade pipeline via apprenticeships and vocational partnerships."

  gameplay_patterns:
    - "Supplier diversification (defensive)."
    - "Strategic inventory / buffering (defensive) - against JIT orthodoxy."
    - "Co-evolution with IRA/CHIPS policy (offensive)."
    - "Productisation play on digital twin / supply-chain risk."
    - "Open-source / standards play on ESG reporting."

  climatic_patterns:
    - "Everything evolves."
    - "Co-evolution of practice and activity (JIT -> just-in-case; scope-3 reporting)."
    - "Punctuated equilibrium (COVID + Ukraine + IRA + CHIPS)."
    - "Past success breeds inertia (JIT, lean orthodoxy)."
    - "Efficiency-vs-resilience rebalanced toward resilience."
```

---

## Analysis Checklist Verification

- Completeness: 2 anchors defined; 34 components across sourcing/production/logistics/digital/compliance/people; dependencies encoded; movement flags on every component.
- Positioning: commodity-right (Cloud, Ocean Freight, Raw Materials, Fabs, Energy), custom-left (Digital Twin, Supplier Risk Intel, Geopolitical Intel, ESG, Inventory Buffering Policy).
- Insights: inertia (JIT inventory, TSMC, skilled labour, EU energy, components inventory); commoditisation opportunities (supplier risk intel, digital twin); single-source risks (chips, minerals, TSMC).
- Strategic: gameplay + climatic patterns captured.

---

## OWM Text Format (for comparator)

```owm
title Modern Manufacturing Supply Chain - Discrete OEM (Feb 2023)
anchor End Customer [0.98, 0.65]
anchor Supply-Chain Organisation [0.97, 0.42]

component Finished Product [0.92, 0.65]
component Order Fulfilment and Last-Mile [0.88, 0.72]
component Demand Forecasting and SOP [0.85, 0.60]
component Supply-Chain Risk Management [0.90, 0.42]
component Multi-Sourcing and Nearshoring [0.86, 0.38]
component Inventory Buffering Policy [0.75, 0.40]
component Supplier Risk Intelligence [0.72, 0.45]
component AI ML Demand Sensing [0.70, 0.40]
component Quality Assurance [0.60, 0.70]
component Outbound Logistics 3PL [0.78, 0.82]
component Warehousing and DCs [0.68, 0.72]
component Digital Twin of Supply Chain [0.72, 0.32]
component ESG Scope-3 Compliance [0.65, 0.35]
component Final Assembly [0.75, 0.66]
component Sub-Assembly Manufacturing [0.72, 0.64]
component Supplier Collaboration Portal [0.58, 0.68]
component Geopolitical Intelligence [0.55, 0.30]
component MES [0.55, 0.68]
component Supplier Qualification [0.66, 0.55]
component Skilled Production Labour [0.50, 0.30]
component Components and Parts Inventory [0.70, 0.62]
component Inbound Logistics and Freight [0.50, 0.80]
component Tier-1 Suppliers [0.55, 0.60]
component Semiconductors [0.45, 0.58]
component CNC IM SMT Lines [0.45, 0.72]
component ERP [0.45, 0.70]
component Industrial IoT Sensors [0.40, 0.70]
component Tier-N Suppliers [0.35, 0.78]
component Factory Energy Supply [0.30, 0.82]
component Container Shipping Ocean Freight [0.30, 0.88]
component OT Network [0.25, 0.72]
component TSMC Global Fabs [0.32, 0.82]
component Critical Raw Materials [0.15, 0.85]
component Cloud Compute [0.15, 0.90]

End Customer -> Finished Product
End Customer -> Order Fulfilment and Last-Mile
End Customer -> Demand Forecasting and SOP
Supply-Chain Organisation -> Supply-Chain Risk Management
Supply-Chain Organisation -> Multi-Sourcing and Nearshoring
Supply-Chain Organisation -> Demand Forecasting and SOP
Supply-Chain Organisation -> Inventory Buffering Policy
Supply-Chain Organisation -> ESG Scope-3 Compliance
Finished Product -> Final Assembly
Finished Product -> Order Fulfilment and Last-Mile
Finished Product -> Quality Assurance
Order Fulfilment and Last-Mile -> Outbound Logistics 3PL
Order Fulfilment and Last-Mile -> Warehousing and DCs
Demand Forecasting and SOP -> ERP
Demand Forecasting and SOP -> Supplier Collaboration Portal
Demand Forecasting and SOP -> AI ML Demand Sensing
Supply-Chain Risk Management -> Supplier Risk Intelligence
Supply-Chain Risk Management -> Digital Twin of Supply Chain
Supply-Chain Risk Management -> Multi-Sourcing and Nearshoring
Supply-Chain Risk Management -> Inventory Buffering Policy
Multi-Sourcing and Nearshoring -> Supplier Qualification
Multi-Sourcing and Nearshoring -> Geopolitical Intelligence
Supplier Risk Intelligence -> Geopolitical Intelligence
Supplier Risk Intelligence -> Cloud Compute
Digital Twin of Supply Chain -> ERP
Digital Twin of Supply Chain -> Industrial IoT Sensors
Digital Twin of Supply Chain -> AI ML Demand Sensing
AI ML Demand Sensing -> ERP
AI ML Demand Sensing -> Cloud Compute
ESG Scope-3 Compliance -> Supplier Collaboration Portal
Final Assembly -> Sub-Assembly Manufacturing
Final Assembly -> MES
Final Assembly -> Skilled Production Labour
Final Assembly -> Factory Energy Supply
Sub-Assembly Manufacturing -> Tier-1 Suppliers
Sub-Assembly Manufacturing -> Components and Parts Inventory
Sub-Assembly Manufacturing -> CNC IM SMT Lines
MES -> Industrial IoT Sensors
MES -> OT Network
Industrial IoT Sensors -> OT Network
Quality Assurance -> MES
Tier-1 Suppliers -> Tier-N Suppliers
Tier-1 Suppliers -> Critical Raw Materials
Tier-1 Suppliers -> Semiconductors
Tier-N Suppliers -> Critical Raw Materials
Semiconductors -> TSMC Global Fabs
Semiconductors -> Critical Raw Materials
TSMC Global Fabs -> Critical Raw Materials
TSMC Global Fabs -> Factory Energy Supply
Supplier Qualification -> ESG Scope-3 Compliance
Supplier Qualification -> Quality Assurance
Supplier Collaboration Portal -> ERP
Supplier Collaboration Portal -> Cloud Compute
ERP -> Cloud Compute
Inbound Logistics and Freight -> Container Shipping Ocean Freight
Outbound Logistics 3PL -> Container Shipping Ocean Freight
Components and Parts Inventory -> Tier-1 Suppliers
Components and Parts Inventory -> Warehousing and DCs
Inventory Buffering Policy -> Components and Parts Inventory
Inventory Buffering Policy -> AI ML Demand Sensing
```
