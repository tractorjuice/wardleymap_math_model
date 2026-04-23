# Manufacturing Supply Chain — Wardley Map (February 2023)

**Anchor:** A manufacturer delivering finished product to distributors, while keeping the chain resilient against disruption.
**Scope:** End-to-end manufacturing value chain — from raw materials through operations into distribution — overlaid with regulation, finance, inventory strategy, and resilience-visibility.
**Author:** wardley-mapping skill (arc-kit)
**Date:** 2023-02-15
**Version:** 1.0

---

## 1. Context gathered (Step 1)

| Question | Answer |
|---|---|
| Primary user | The manufacturer's operations / supply-chain leadership, ultimately serving distributors and end-customers. |
| User need | Reliable, resilient delivery of finished product to distributors. |
| Scope | Entire manufacturing organisation and its immediate upstream (suppliers) and downstream (distributors) tiers. |
| Primary goal | Understand where the supply chain itself sits on evolution and which links are industrialised vs bespoke judgment. |
| Industry | Discrete / process manufacturing (generic; positioning applies broadly to Feb-2023 manufacturers post-COVID, mid Ukraine-war, chip-crunch tail). |
| Depth | Standard map — ~22 components with inertia + movement analysis. |

---

## 2. Value chain (Step 2)

Working backwards from the anchor:

- **Anchor:** Product delivered to distributors.
- Immediate visible layer: **Distributors**, **Sales Forecasting**, **Supply Chain Resilience Awareness**, **Finished Product**.
- Operations layer: **Quality Control**, **Manufacturing Operations**, **Product Certification**, **Safety & Compliance**.
- Inventory/logistics decisions: **Inventory Strategy (JIT vs JIC)**, **Warehousing**, **Logistics & Freight**.
- Financial lens: **ROCE / Capital Efficiency**, **Cost Accounting**, **Capital Investment**.
- Inputs: **Skilled Labour**, **Manufacturing Equipment**, **R&D / Process Innovation**.
- Materials: **Refined Materials**, **Raw Materials**.
- Utilities / data underlays: **Energy**, **Transport Fuel**, **ERP / MRP Systems**, **Supplier Data & Telemetry**.
- Influence/soft-power: **Regulatory Lobbying**.

---

## 3. Visual map (Step 3 + 4)

```text
Title: Manufacturing Supply Chain
Anchor: Product delivered to distributors
Date: 2023-02-15

                    Genesis    Custom     Product    Commodity
                       │          │          │          │
Visible            ┌───┼──────────┼──────────┼──────────┼───┐
                   │   │          │          │          │   │
 User Need         │   │          │          ● Product delivered to distributors
                   │   │          │          │                │
                   │   │          ↓          ↓                ↓
                   │   │ Resilience   Sales Forecast    Distributors ──→ ●
                   │   │ Awareness ●→    ● (→ Product)         │
                   │   │     ↓         ↓     │                 ↓
                   │   │          │          ● Finished Product          │
                   │   │          │          │      │                    │
                   │   │          │          ● Safety & Compliance       │
                   │   │          │       QC ●                           │
                   │   │          ● Cert.    │                           │
                   │   │     ↓             Mfg Ops ●                     │
                   │   │ Inv. Strategy ×→   │       │                    │
                   │   │ (JIT vs JIC)       │       │    ● Warehousing   │
                   │   │ Lobbying ●→        │       │    ● Logistics/Freight
                   │   │          │         │       │                    │
                   │   │          │   Capital  ROCE/Cap Eff ●  Cost Acct ●×
                   │   │          │   Invest ●                           │
                   │   │          │          │       │                   │
                   │   │          │   Skilled Labour  ● Equipment        │
                   │   │          │          ●         │                 │
                   │   │     R&D ●→          │         │                 │
                   │   │          │          │ Supplier Data/Tele  ERP ● │
                   │   │          │          │       ●                   │
                   │   │          │          │  Refined Materials ●      │
                   │   │          │     Raw Materials ●                  │
Hidden             │   │          │                  │  Energy ●         │
                   │   │          │                  │  Transport Fuel ● │
                   │   │          │                  │                   │
                   └───┴──────────────────────────────────────────┘

Legend: ● Current position, → Evolution direction, × Inertia
```

---

## 4. Structured output

```yaml
wardley_map:
  metadata:
    title: "Manufacturing Supply Chain"
    author: "arc-kit wardley-mapping skill"
    date: "2023-02-15"
    version: "1.0"
    scope: "Full manufacturing value chain, regulation, finance, inventory, resilience-visibility"

  anchor:
    user: "Manufacturer / operations leadership"
    need: "Deliver product to distributors with a resilient chain"

  components:
    - name: "Product delivered to distributors"
      evolution: "Product"
      position: 0.60
      visibility: 0.96
      depends_on: ["Distributors", "Sales Forecasting", "Supply Chain Resilience Awareness", "Finished Product"]
      notes: "Anchor — the user need."
      movement: "none"

    - name: "Distributors"
      evolution: "Product → Commodity"
      position: 0.75
      visibility: 0.88
      depends_on: ["Logistics & Freight", "Warehousing"]
      notes: "Known channel; some regions more commoditised (3PL), some bespoke."
      movement: "evolving"

    - name: "Sales Forecasting"
      evolution: "Custom → Product"
      position: 0.55
      visibility: 0.85
      depends_on: ["ERP / MRP Systems", "Supplier Data & Telemetry"]
      notes: "ML-forecasting products exist, but most manufacturers still tune bespoke models in spreadsheets / SAP IBP."
      movement: "evolving"

    - name: "Supply Chain Resilience Awareness"
      evolution: "Genesis → Custom"
      position: 0.20
      visibility: 0.86
      depends_on: ["Supplier Data & Telemetry", "Inventory Strategy (JIT vs JIC)", "Sales Forecasting"]
      notes: "Post-COVID / chip-crunch / Ukraine: n-tier visibility is still genesis — every firm is building their own, very few off-the-shelf answers. This is the explicit 'is my chain resilient?' lens."
      movement: "accelerating"

    - name: "Finished Product"
      evolution: "Product"
      position: 0.70
      visibility: 0.80
      depends_on: ["Quality Control", "Manufacturing Operations", "Product Certification"]
      notes: "Well-understood output, differentiated by brand and spec."
      movement: "none"

    - name: "Quality Control"
      evolution: "Product"
      position: 0.65
      visibility: 0.74
      depends_on: ["Safety & Compliance"]
      notes: "Standard QMS tooling (ISO 9001, SPC) — mature."
      movement: "none"

    - name: "Manufacturing Operations"
      evolution: "Product"
      position: 0.60
      visibility: 0.72
      depends_on: ["Manufacturing Equipment", "Skilled Labour", "Refined Materials", "Energy", "ERP / MRP Systems"]
      notes: "Lean/Six-Sigma is product-stage; plant-level tuning keeps differentiation."
      movement: "none"

    - name: "Inventory Strategy (JIT vs JIC)"
      evolution: "Custom"
      position: 0.35
      visibility: 0.70
      depends_on: ["Warehousing", "Logistics & Freight"]
      notes: "Still a judgment call in Feb 2023 — COVID shocks and chip crunch have reopened JIT orthodoxy. No commodity answer."
      movement: "evolving"

    - name: "Warehousing"
      evolution: "Product → Commodity"
      position: 0.78
      visibility: 0.66
      depends_on: ["Logistics & Freight"]
      notes: "3PL market is mature; cold-chain / specialised still product stage. Note: inertia from sunk capex on owned DCs."
      movement: "inertia"

    - name: "Logistics & Freight"
      evolution: "Commodity"
      position: 0.80
      visibility: 0.64
      depends_on: ["Transport Fuel"]
      notes: "Commoditised capacity market; utility-priced per TEU / pallet-km."
      movement: "none"

    - name: "Safety & Compliance"
      evolution: "Product"
      position: 0.72
      visibility: 0.68
      depends_on: ["Regulatory Lobbying"]
      notes: "Compliance-as-a-function is well-understood; GRC tooling vendor-rich."
      movement: "none"

    - name: "Product Certification"
      evolution: "Product"
      position: 0.68
      visibility: 0.62
      depends_on: ["Safety & Compliance"]
      notes: "Defined regimes (CE/UKCA/UL) — procedural, industrialised."
      movement: "none"

    - name: "Regulatory Lobbying"
      evolution: "Custom"
      position: 0.30
      visibility: 0.60
      depends_on: []
      notes: "Bespoke per jurisdiction / issue; relationships-based. Not commoditisable."
      movement: "evolving"

    - name: "ROCE / Capital Efficiency"
      evolution: "Product"
      position: 0.60
      visibility: 0.58
      depends_on: ["Cost Accounting", "Capital Investment"]
      notes: "Standard executive KPI; pattern of measurement well-understood."
      movement: "none"

    - name: "Cost Accounting"
      evolution: "Commodity"
      position: 0.82
      visibility: 0.56
      depends_on: ["Energy", "Raw Materials", "Skilled Labour"]
      notes: "Activity-based costing is mature. Inertia: ERP chart-of-accounts legacy."
      movement: "inertia"

    - name: "Capital Investment"
      evolution: "Product"
      position: 0.55
      visibility: 0.54
      depends_on: ["Manufacturing Equipment", "R&D / Process Innovation"]
      notes: "CAPEX decisioning is productised (NPV / IRR gates)."
      movement: "none"

    - name: "Skilled Labour"
      evolution: "Custom → Product"
      position: 0.50
      visibility: 0.50
      depends_on: []
      notes: "Scarce in Feb 2023 — machinists, welders, process engineers in shortage across EU/US."
      movement: "none"

    - name: "Manufacturing Equipment"
      evolution: "Product"
      position: 0.70
      visibility: 0.46
      depends_on: ["R&D / Process Innovation"]
      notes: "CNC, robotics, automation-cell vendors mature."
      movement: "none"

    - name: "R&D / Process Innovation"
      evolution: "Genesis → Custom"
      position: 0.20
      visibility: 0.44
      depends_on: ["Skilled Labour"]
      notes: "Process innovation is still exploratory at each firm; differentiator."
      movement: "evolving"

    - name: "Refined Materials"
      evolution: "Product → Commodity"
      position: 0.72
      visibility: 0.36
      depends_on: ["Raw Materials", "Energy"]
      notes: "Steel, plastics pellets, semis — commodity markets with quality bands."
      movement: "none"

    - name: "Raw Materials"
      evolution: "Commodity"
      position: 0.85
      visibility: 0.24
      depends_on: ["Transport Fuel"]
      notes: "Ores, grain, crude — exchange-traded."
      movement: "none"

    - name: "Energy"
      evolution: "Commodity"
      position: 0.88
      visibility: 0.18
      depends_on: []
      notes: "Utility — but February 2023 pricing volatility is a climate factor."
      movement: "none"

    - name: "Transport Fuel"
      evolution: "Commodity"
      position: 0.90
      visibility: 0.16
      depends_on: []
      notes: "Utility."
      movement: "none"

    - name: "ERP / MRP Systems"
      evolution: "Product"
      position: 0.72
      visibility: 0.30
      depends_on: []
      notes: "SAP / Oracle / Dynamics / NetSuite — mature vendor market; configure-not-code."
      movement: "none"

    - name: "Supplier Data & Telemetry"
      evolution: "Custom"
      position: 0.40
      visibility: 0.28
      depends_on: []
      notes: "n-tier visibility platforms (Everstream, Resilinc, Interos) are emergent, not yet commodity. The raw nerve ending for resilience."
      movement: "evolving"

  analysis:
    opportunities:
      - "Industrialise Logistics, Warehousing, Cost Accounting, ERP/MRP — treat as utility and stop over-investing."
      - "Invest pioneers into Supply Chain Resilience Awareness and Supplier Data & Telemetry — still genesis/custom, differentiation is up for grabs."
      - "Treat Inventory Strategy (JIT vs JIC) as a live doctrine decision, not a fixed belief — hedge with dual-inventory playbook."
      - "Process R&D is the durable moat; don't let planners run it."
      - "Regulatory Lobbying can be used offensively (raise barriers on safety) once certification posture is strong."

    threats:
      - "Energy and Transport Fuel volatility (post-Ukraine) collapse ROCE assumptions — sales forecasting models trained on pre-2020 data are unreliable."
      - "Skilled Labour shortage (custom-stage) is a hard bottleneck — equipment alone won't bridge it."
      - "JIT orthodoxy is inertia disguised as efficiency — single-source bets still dominate many BOMs."
      - "Supplier telemetry blind spots below tier-2 mean 'resilience' is theatre at most firms."
      - "Refined Materials are mid-commoditising — any in-house custom refining steps are on the wrong side of the curve."

    inertia_points:
      - component: "Warehousing"
        reason: "Sunk capex in owned DCs prevents shift to 3PL/utility model."
      - component: "Cost Accounting"
        reason: "Legacy ERP chart-of-accounts and SOX controls freeze methodology."
      - component: "Inventory Strategy (JIT vs JIC)"
        reason: "Decades of lean-manufacturing orthodoxy bias toward JIT even after 2020-2022 shocks."
      - component: "Regulatory Lobbying"
        reason: "Relationship-based, jurisdiction-specific — resists standardisation even when the underlying certification regime matures."

  recommendations:
    immediate:
      - "Stand up a resilience-awareness capability: n-tier supplier mapping + telemetry pilot (pioneers, not planners)."
      - "Re-forecast with post-2022 energy/FX/fuel scenarios; mark down the old sales-forecast model's confidence bands."
      - "Inventory: move explicitly to dual-policy — JIT on A-class low-risk SKUs, JIC buffer on single-sourced or geopolitically-exposed inputs."
    short_term:
      - "Shift non-differentiating warehousing to 3PL where DC lease cycles allow; release capital to R&D / Process Innovation."
      - "Consolidate compliance and certification onto a productised GRC platform; redirect headcount to supplier-visibility analytics."
      - "Benchmark ROCE sensitivity to a +/- 30% swing in each commodity input; include Energy and Transport Fuel as first-class variables, not flat assumptions."
    long_term:
      - "Build proprietary Process Innovation as the durable moat — it is the only genuinely custom-built layer you control."
      - "Productise the internal resilience-awareness tool; in 2-3 years this layer will commoditise, and early movers set the data schema."
      - "Invest in apprenticeships/automation to de-bottleneck Skilled Labour — it will not commoditise on its own."
```

---

## 5. Answer to the user's two specific questions

> **Where does the supply chain itself sit on the evolution axis?**

The *value chain* is hybrid. The **physical flow** — materials, logistics, warehousing, cost accounting — is solidly **Product → Commodity** (position ~0.70-0.90). The **awareness / decision layer** — resilience visibility, inventory strategy, forecasting, process R&D — is still **Genesis to Custom** (position ~0.20-0.55). In February 2023, the manufacturer's competitive surface has shifted *leftward*: moving atoms is a utility; knowing what's happening to them across n-tiers and deciding how much buffer to hold is bespoke judgment.

> **What's industrialised vs still bespoke judgment?**

| Industrialised (Product/Commodity, right side) | Bespoke judgment (Genesis/Custom, left side) |
|---|---|
| Logistics & Freight, Transport Fuel, Energy | Supply Chain Resilience Awareness |
| Warehousing (3PL available) | Supplier Data & Telemetry (n-tier visibility) |
| ERP/MRP Systems | Inventory Strategy (JIT vs JIC) |
| Cost Accounting | R&D / Process Innovation |
| Manufacturing Equipment, QC tooling | Regulatory Lobbying |
| Safety & Compliance, Product Certification | Sales Forecasting (mid-transition) |
| Raw / Refined Materials (exchange-traded) | Skilled Labour (custom-stage, scarce) |
| Manufacturing Operations (lean is mature) | |

Strategic read: the industrialised layers are where cost discipline lives; the bespoke layers are where 2023 resilience and 2025-2028 competitive advantage will be won or lost. Don't let town-planners manage the left side, don't let pioneers keep running the right side.

---

## 6. Gameplay & climate cross-reference

- **Climatic patterns in play (Feb 2023):** *Everything evolves* (resilience tooling is pre-transition), *Past success breeds inertia* (JIT orthodoxy), *Efficiency enables innovation* (commodity logistics frees capital for R&D), *Shocks happen* (COVID + Ukraine + chip crunch are the proximate drivers of the resilience-awareness push).
- **Applicable gameplays:**
  - *Exploiting constraint* on Skilled Labour (apprenticeships, automation).
  - *Harvesting* in Logistics/Warehousing.
  - *Pig in a poke / First Mover* on internal resilience-awareness platform.
  - *Raising barriers to entry* via Safety/Certification + Lobbying once own posture is strong.
- **Doctrine weaknesses most firms will exhibit here:** weak *Know your users* (n-tier suppliers are users too), weak *Use appropriate methods* (applying lean-manufacturing doctrine to genesis-stage resilience tooling), weak *Think small* (over-centralising forecasting).

---

## 7. Notes on limitations

- This is a generic map of a manufacturer — real maps should be per-firm (BOM-specific, jurisdiction-specific).
- Positions on the evolution axis are qualitative Feb-2023 reads; a quantitative Ubiquity x Certainty scoring pass would tighten each by ~0.05.
- Movement arrows reflect 3-5 year expected drift; shocks can move components left (resilience-awareness became more salient *because* the world got more uncertain).
