# Wardley Value Chain: Manufacturing Supply Chain (February 2023)

## Executive Summary

**Anchor**: A manufacturer needs to deliver a compliant, cost-effective product to distributors through a supply chain whose resilience, cost position, and regulatory standing can be understood and acted upon.

The chain decomposes into 19 components plus the anchor, spanning four concurrent lenses that all converge on the manufacturer-to-distributor flow: (1) the physical product path (raw materials → refined materials → equipment + labour + R&D → assembly → distributor), (2) the regulatory lens (compliance, safety certification, lobbying), (3) the financial lens (ROCE management, cost accounting, capital financing, sales forecasting), and (4) the inventory / logistics and awareness lens (inventory strategy, warehousing, logistics transport, chain resilience visibility).

Three strategic insights surface. First, **Chain Resilience Visibility** — the awareness layer asked about in the scenario — is itself a high-visibility component that consumes forecasting, inventory state, and logistics telemetry, which is why supply-chain "control towers" have become a category in their own right since 2020-2022. Second, the **Inventory Strategy** node is the explicit locus of the just-in-time vs just-in-case trade-off and depends on both warehousing and logistics, so changing the JIT/JIC stance cascades through two layers below. Third, the supply chain as an **integrated capability** sits in the bespoke / custom-built half of the evolution axis for most manufacturers — resilience-aware orchestration across suppliers is not yet a commodity — while its constituent infrastructure (refined materials, energy, logistics transport) is already product or commodity. Evolution positions are placeholders (ε = 0.50) in this value chain artifact; they are resolved in the subsequent `$arckit-wardley` step.

## Users and Personas

| User / Persona | Primary Need |
|---|---|
| Manufacturer (operations leadership) | Get product to distributors reliably, on time, at target cost |
| CFO / Finance | ROCE stays within target, capital deployment is justified, cost is controlled |
| Head of Supply Chain | Know whether the chain is resilient; choose JIT vs JIC deliberately |
| Regulatory / Compliance lead | Maintain certification, satisfy safety regimes, shape regulation where possible |
| R&D lead | Feed new product definitions into assembly without breaking the chain |
| Distributor (downstream customer) | Receive product meeting spec, on schedule, with predictable lead times |

## Value Chain Diagram

### ASCII Placeholder

```
Y ^  (visibility)
  |
0.97 +  [Distributor Delivery]                                         (anchor)
  |        |        |            |                 |             |
0.88 + [Product Assembly]        |                 |             |
0.84 +        [Sales Forecasting]|                 |             |
0.82 +                    [Regulatory Compliance]  |             |
0.80 +                           [Chain Resilience Visibility]
0.78 +                                       [Quality Assurance]
0.76 +                                                     [ROCE Management]
0.72 + [Inventory Strategy]
0.70 + [Product R&D]
0.68 + [Safety Certification]
0.66 + [Lobbying]
0.64 + [Cost Accounting]
0.60 + [Warehousing]
0.56 + [Skilled Labour]
0.52 + [Production Equipment]
0.48 + [Logistics Transport]
0.44 + [Capital Financing]
0.32 + [Refined Materials]
0.22 + [Energy Supply]
0.16 + [Raw Materials]
  |
  +------------------------------------------------------------> X (evolution)
           Genesis     Custom       Product       Commodity
           (ε positions are placeholders — 0.50 for all — at value chain stage)
```

### OWM (https://create.wardleymaps.ai)

```text
title Manufacturing Supply Chain Value Chain (February 2023)

anchor Distributor Delivery [0.97, 0.50]

component Product Assembly [0.88, 0.50]
component Sales Forecasting [0.84, 0.50]
component Regulatory Compliance [0.82, 0.50]
component Chain Resilience Visibility [0.80, 0.50]
component Quality Assurance [0.78, 0.50]
component ROCE Management [0.76, 0.50]
component Inventory Strategy [0.72, 0.50]
component Product R&D [0.70, 0.50]
component Safety Certification [0.68, 0.50]
component Lobbying [0.66, 0.50]
component Cost Accounting [0.64, 0.50]
component Warehousing [0.60, 0.50]
component Skilled Labour [0.56, 0.50]
component Production Equipment [0.52, 0.50]
component Logistics Transport [0.48, 0.50]
component Capital Financing [0.44, 0.50]
component Refined Materials [0.32, 0.50]
component Energy Supply [0.22, 0.50]
component Raw Materials [0.16, 0.50]

Distributor Delivery->Product Assembly
Distributor Delivery->Sales Forecasting
Distributor Delivery->Regulatory Compliance
Distributor Delivery->Chain Resilience Visibility
Distributor Delivery->Quality Assurance
Distributor Delivery->ROCE Management
Product Assembly->Product R&D
Product Assembly->Skilled Labour
Product Assembly->Production Equipment
Product Assembly->Refined Materials
Product Assembly->Inventory Strategy
Regulatory Compliance->Safety Certification
Regulatory Compliance->Lobbying
Quality Assurance->Safety Certification
Quality Assurance->Skilled Labour
ROCE Management->Cost Accounting
ROCE Management->Capital Financing
Sales Forecasting->Chain Resilience Visibility
Chain Resilience Visibility->Inventory Strategy
Chain Resilience Visibility->Logistics Transport
Inventory Strategy->Warehousing
Inventory Strategy->Logistics Transport
Warehousing->Logistics Transport
Product R&D->Skilled Labour
Production Equipment->Capital Financing
Refined Materials->Raw Materials
Refined Materials->Energy Supply
Production Equipment->Energy Supply
Warehousing->Energy Supply

style wardley
```

### Mermaid (wardley-beta)

<details>
<summary>Mermaid value-chain map</summary>

```mermaid
wardley-beta
title Manufacturing Supply Chain Value Chain (February 2023)
size [1100, 800]

anchor "Distributor Delivery" [0.97, 0.50]

component "Product Assembly" [0.88, 0.50]
component "Sales Forecasting" [0.84, 0.50]
component "Regulatory Compliance" [0.82, 0.50]
component "Chain Resilience Visibility" [0.80, 0.50]
component "Quality Assurance" [0.78, 0.50]
component "ROCE Management" [0.76, 0.50]
component "Inventory Strategy" [0.72, 0.50]
component "Product R&D" [0.70, 0.50]
component "Safety Certification" [0.68, 0.50]
component Lobbying [0.66, 0.50]
component "Cost Accounting" [0.64, 0.50]
component Warehousing [0.60, 0.50]
component "Skilled Labour" [0.56, 0.50]
component "Production Equipment" [0.52, 0.50]
component "Logistics Transport" [0.48, 0.50]
component "Capital Financing" [0.44, 0.50]
component "Refined Materials" [0.32, 0.50]
component "Energy Supply" [0.22, 0.50]
component "Raw Materials" [0.16, 0.50]

"Distributor Delivery" -> "Product Assembly"
"Distributor Delivery" -> "Sales Forecasting"
"Distributor Delivery" -> "Regulatory Compliance"
"Distributor Delivery" -> "Chain Resilience Visibility"
"Distributor Delivery" -> "Quality Assurance"
"Distributor Delivery" -> "ROCE Management"
"Product Assembly" -> "Product R&D"
"Product Assembly" -> "Skilled Labour"
"Product Assembly" -> "Production Equipment"
"Product Assembly" -> "Refined Materials"
"Product Assembly" -> "Inventory Strategy"
"Regulatory Compliance" -> "Safety Certification"
"Regulatory Compliance" -> Lobbying
"Quality Assurance" -> "Safety Certification"
"Quality Assurance" -> "Skilled Labour"
"ROCE Management" -> "Cost Accounting"
"ROCE Management" -> "Capital Financing"
"Sales Forecasting" -> "Chain Resilience Visibility"
"Chain Resilience Visibility" -> "Inventory Strategy"
"Chain Resilience Visibility" -> "Logistics Transport"
"Inventory Strategy" -> Warehousing
"Inventory Strategy" -> "Logistics Transport"
Warehousing -> "Logistics Transport"
"Product R&D" -> "Skilled Labour"
"Production Equipment" -> "Capital Financing"
"Refined Materials" -> "Raw Materials"
"Refined Materials" -> "Energy Supply"
"Production Equipment" -> "Energy Supply"
Warehousing -> "Energy Supply"
```

</details>

## Component Inventory

| # | Component | Visibility | Description | Depends On |
|---|---|---|---|---|
| A | Distributor Delivery | 0.97 | Anchor — product handed to distributor meeting spec, on time, at target margin | Product Assembly; Sales Forecasting; Regulatory Compliance; Chain Resilience Visibility; Quality Assurance; ROCE Management |
| 1 | Product Assembly | 0.88 | Converting refined materials + designs into finished product via equipment and labour | Product R&D; Skilled Labour; Production Equipment; Refined Materials; Inventory Strategy |
| 2 | Sales Forecasting | 0.84 | Demand signal driving volume, mix, and lead-time targets | Chain Resilience Visibility |
| 3 | Regulatory Compliance | 0.82 | Meeting statutory regimes across jurisdictions (product, environment, trade) | Safety Certification; Lobbying |
| 4 | Chain Resilience Visibility | 0.80 | The awareness layer — "control tower" for supplier health, inventory state, logistics flow | Inventory Strategy; Logistics Transport |
| 5 | Quality Assurance | 0.78 | In-line and outgoing QA that certifies the product is fit to ship | Safety Certification; Skilled Labour |
| 6 | ROCE Management | 0.76 | Managing return-on-capital-employed as the financial control loop | Cost Accounting; Capital Financing |
| 7 | Inventory Strategy | 0.72 | Explicit JIT vs JIC stance; stock levels, safety stock, buffer policy | Warehousing; Logistics Transport |
| 8 | Product R&D | 0.70 | Designs and BOMs that assembly consumes | Skilled Labour |
| 9 | Safety Certification | 0.68 | Product/plant-level safety approvals (CE/UKCA, UL, sector-specific) | — |
| 10 | Lobbying | 0.66 | Influence on regulatory direction; gameplay, not inertia | — |
| 11 | Cost Accounting | 0.64 | Standard cost, variance, absorption — the numbers ROCE is calculated on | — |
| 12 | Warehousing | 0.60 | Storage nodes holding raw, WIP, and finished goods | Logistics Transport; Energy Supply |
| 13 | Skilled Labour | 0.56 | Operators, engineers, QA staff — the scarce human input | — |
| 14 | Production Equipment | 0.52 | Capex plant and tooling | Capital Financing; Energy Supply |
| 15 | Logistics Transport | 0.48 | Inbound and outbound freight (road, rail, sea, air) | — |
| 16 | Capital Financing | 0.44 | Debt/equity funding for capex and working capital | — |
| 17 | Refined Materials | 0.32 | Processed inputs (sheet, forgings, resins, chemicals, components) | Raw Materials; Energy Supply |
| 18 | Energy Supply | 0.22 | Grid electricity, gas, and on-site generation | — |
| 19 | Raw Materials | 0.16 | Extracted or harvested inputs (ore, crude, pulp, aggregate) | — |

## Dependency Matrix

Legend: X = direct dependency, I = indirect (transitive), . = none. Rows depend on columns.

|                          | Assy | Sales | RegC | CRV | QA | ROCE | Inv | R&D | SafeC | Lob | CostAcc | Whse | Labr | Equip | Logx | CapFin | Refd | Enrg | Raw |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Distributor Delivery      | X | X | X | X | X | X | I | I | I | I | I | I | I | I | I | I | I | I | I |
| Product Assembly          | — | . | . | . | . | . | X | X | . | . | . | I | X | X | I | I | X | I | I |
| Sales Forecasting         | . | — | . | X | . | . | I | . | . | . | . | I | . | . | I | . | . | I | . |
| Regulatory Compliance     | . | . | — | . | . | . | . | . | X | X | . | . | . | . | . | . | . | . | . |
| Chain Resilience Vis.     | . | . | . | — | . | . | X | . | . | . | . | I | . | . | X | . | . | I | . |
| Quality Assurance         | . | . | . | . | — | . | . | . | X | . | . | . | X | . | . | . | . | . | . |
| ROCE Management           | . | . | . | . | . | — | . | . | . | . | X | . | . | . | . | X | . | . | . |
| Inventory Strategy        | . | . | . | . | . | . | — | . | . | . | . | X | . | . | X | . | . | I | . |
| Product R&D               | . | . | . | . | . | . | . | — | . | . | . | . | X | . | . | . | . | . | . |
| Warehousing               | . | . | . | . | . | . | . | . | . | . | . | — | . | . | X | . | . | X | . |
| Production Equipment      | . | . | . | . | . | . | . | . | . | . | . | . | . | — | . | X | . | X | . |
| Refined Materials         | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | — | X | X |

(Terminal commodities — Safety Certification, Lobbying, Cost Accounting, Skilled Labour, Logistics Transport, Capital Financing, Energy Supply, Raw Materials — have no outbound dependencies inside the scope of this chain and are not shown as rows.)

## Critical Path Analysis

**Longest path (anchor → deepest commodity)**:

```
Distributor Delivery → Product Assembly → Refined Materials → Raw Materials
(4 levels; 3 edges)
```

A secondary critical path runs through the awareness lens:

```
Distributor Delivery → Sales Forecasting → Chain Resilience Visibility → Inventory Strategy → Warehousing → Logistics Transport
(6 levels; 5 edges)
```

**Bottlenecks and single points of failure**:

- **Refined Materials** is the single chokepoint for the physical chain — every assembled unit passes through it, and it in turn depends on both Raw Materials and Energy Supply. Post-2022 energy shocks make this the most exposed edge.
- **Skilled Labour** is a shared dependency of Assembly, Quality Assurance, and R&D. A labour shortage degrades three parallel capabilities simultaneously.
- **Logistics Transport** is shared by Inventory Strategy, Warehousing, and Chain Resilience Visibility — freight disruption affects both the physical flow and the observability of the chain.
- **Safety Certification** is a shared dependency of Regulatory Compliance and Quality Assurance; a withdrawn certification closes two parallel paths.
- **Energy Supply** sits under Refined Materials, Production Equipment, and Warehousing — a commodity today but a resilience risk given the 2022-2023 European gas situation.

**Resilience gaps**:

- No explicit **supplier diversification** component — resilience is currently expressed only through Chain Resilience Visibility and Inventory Strategy. Multi-sourcing could be surfaced as its own component in a refinement pass.
- No **cybersecurity / OT security** component despite manufacturing being a heavy target in 2022-2023. Would attach under Production Equipment and Chain Resilience Visibility.
- No explicit **supplier finance / trade credit** node; Capital Financing is treated only from the manufacturer side.

## Validation Checklist

### Completeness

- [x] Chain starts with a genuine user need (product reaches distributor — not "we need an ERP")
- [x] All significant dependencies between components are captured (29 edges over 20 nodes)
- [x] Chain reaches commodity level — Energy Supply, Raw Materials, Logistics Transport
- [x] No orphan components — every node is reachable from the anchor
- [x] All components are activities/capabilities/practices, not actors (e.g., "Skilled Labour" is the capability; the person is not named)

### Accuracy

- [x] Dependencies reflect real operational relationships (Assembly genuinely consumes Refined Materials; ROCE is genuinely calculated from Cost Accounting)
- [x] Visibility ordering consistent with dependency direction — every edge A→B has ν(A) >= ν(B); verified node-by-node
- [x] No component is simultaneously user-facing and infrastructure

### Usefulness

- [x] Granularity is strategic (19 components — inside the 8-20 target band)
- [x] Each component can be positioned independently on the evolution axis in the next step
- [x] Chain reveals strategic insight — the awareness layer (Chain Resilience Visibility) is itself a first-class component and the JIT/JIC choice has visible cascade effects

### Mathematical Constraints

- [x] DAG — no cycles (dependencies all flow toward lower visibility)
- [x] Anchor visibility 0.97 (>= 0.90 requirement)
- [x] Visibility ordering ν(parent) >= ν(child) holds on all 29 edges

## Visibility Assessment

| Component | ν | Rationale |
|---|---|---|
| Distributor Delivery | 0.97 | Anchor — the outcome the manufacturer is judged on by its direct customer |
| Product Assembly | 0.88 | The manufacturer's defining activity; a failure here halts delivery immediately |
| Sales Forecasting | 0.84 | Drives every downstream commitment; visible at exec level weekly |
| Regulatory Compliance | 0.82 | Board-visible; a recall or ban is existential |
| Chain Resilience Visibility | 0.80 | The explicitly-asked-about awareness layer; reports into operations leadership |
| Quality Assurance | 0.78 | A QA failure is immediately visible through returns and distributor complaints |
| ROCE Management | 0.76 | CFO dashboard; reviewed monthly |
| Inventory Strategy | 0.72 | JIT vs JIC is a named, deliberated policy — not hidden |
| Product R&D | 0.70 | Roadmap is known to the business; individual projects are visible |
| Safety Certification | 0.68 | Shared dependency; treated as a known gate rather than a surface |
| Lobbying | 0.66 | Known but slow-cycle; effects surface over quarters not days |
| Cost Accounting | 0.64 | Essential but infrastructural for finance — users see outputs, not the process |
| Warehousing | 0.60 | Visible through stockouts and fill rate, not directly by customers |
| Skilled Labour | 0.56 | Hidden unless scarce; a labour shortage becomes visible abruptly |
| Production Equipment | 0.52 | Capex-level asset; breakdowns are operationally visible |
| Logistics Transport | 0.48 | Visible only through late deliveries and freight cost |
| Capital Financing | 0.44 | Treasury function; invisible in normal operations |
| Refined Materials | 0.32 | Input commodity; visible only under shortage |
| Energy Supply | 0.22 | Infrastructure — normally unseen; 2022 shocks made it briefly visible |
| Raw Materials | 0.16 | Deep upstream; visible only through price indices |

## Assumptions and Open Questions

**Assumptions**:

1. "Manufacturer" is generic — the chain would sharpen if the sector were specified (automotive, pharma, and process industries differ in where R&D and regulation sit).
2. The manufacturer sells **to distributors** (not direct-to-consumer); "Distributor Delivery" is the anchor rather than "Consumer receives product."
3. "Chain Resilience Visibility" is treated as an internal capability, not as a purchased SaaS service. Stage of evolution (placeholder 0.50 here) will matter in the next step — see open question 3.
4. The financial lens is represented through ROCE, Cost, Capital Financing, and Sales Forecasting. A tax/transfer-pricing node has been omitted for granularity.
5. Lobbying is listed as a regulated-industry component in its own right (consistent with the scenario prompt), not folded into Regulatory Compliance. It is a gameplay, not inertia — do not conflate the two in the subsequent mapping step.
6. Just-in-time vs just-in-case is modelled as the *content* of Inventory Strategy rather than as two separate components; the position of Inventory Strategy on the evolution axis will reflect which regime is chosen.

**Open questions** (for the $arckit-wardley step):

1. What sector / what product? — This determines whether Product R&D sits nearer Genesis (pharma, aerospace) or Product (consumer goods with incremental R&D).
2. What is the current JIT/JIC stance? — 2020-2022 disruption pushed many manufacturers back toward JIC; the stance changes the evolution position of Inventory Strategy and Warehousing.
3. Is Chain Resilience Visibility built in-house, bought as a control tower SaaS, or not present? — This is the most important build/buy question in the chain.
4. Is Skilled Labour a constraint? — If yes, Product R&D and QA inherit the same ceiling.
5. What jurisdiction(s)? — Regulatory Compliance, Safety Certification, and Lobbying all shift by geography.
6. Is there a cybersecurity / OT-security gap to surface as a component?
7. Supplier diversification — add as its own component, or keep as a property of Inventory Strategy?

---

## Notes on Skill Scope

This is a **partial-map** skill — it produces the value chain (axes, components, visibility, dependencies) but leaves evolution positions as a placeholder (ε = 0.50) for every component. The next step in the ArcKit workflow (`$arckit-wardley`) assigns evolution positions using the cheat sheet and completes the Wardley Map. Do not interpret the horizontal positions in this file as evolution claims.
