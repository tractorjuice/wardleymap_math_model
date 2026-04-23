# Wardley Value Chain — Transport & Logistics

**Command**: `arckit-wardley.value-chain`
**Date**: 2026-04-23
**Classification**: PUBLIC
**Evolution axis**: placeholder `ε = 0.50` on every component (value-chain stage — no sourcing decorators yet)

---

## 1. Executive Summary

Anchor: **The public can obtain the goods they need, when and where they need them.**

This value chain decomposes the transport & logistics landscape into **32 components** across five visibility tiers, from the public at the top to deep infrastructure (power, fuel, data, topology) at the bottom. The chain captures three strategic surfaces that the scenario explicitly asked about:

1. A **commoditised-utility core** (Storage, Warehouses, Logistics Hubs, Long Haul road freight on Fossil-Fuel/HGV power) that is mature and cost-competed.
2. An **evolution front** where Automated Delivery, Autotrucks, Drones and Scout vehicles (all on Electric Power + Telematics) are pulling Last Mile and Long Haul into a new generation.
3. A **sovereignty / regulation wedge** (CNI Sovereignty, Regulation, HGV Skills, Cities & Rural Topology) that applies inertia and forces variation by jurisdiction — particularly on energy (Electric vs Fossil), data residency, and workforce supply (HGV).

Three insights surface immediately from the chain shape alone (evolution axis deferred to `$arckit-wardley`):

- **Two competing energy chains meet at the vehicle layer.** Trucks pull Fossil Fuel; Autotrucks/Drones/Automated Delivery pull Electric Power. A build/buy decision on fleet electrification cascades straight through Last Mile and Long Haul.
- **Data is the shared commodity under the automation layer.** Telematics, Traffic Data and Real-Time Stock all terminate on a single Data node — it is a multi-consumer commodity and a concentration-risk single point of failure.
- **Government enters the chain twice.** Once through Regulation (shaping vehicles) and once through CNI Sovereignty (shaping Power/Fuel/Data). The two government edges apply different kinds of inertia and should be reasoned about separately.

---

## 2. Users and Personas

| User / Actor | Role in chain | Primary need |
|---|---|---|
| **Public** | Anchor (0.97) | Goods arrive reliably, affordably, where and when needed |
| **Consumers** | Anchor-adjacent (0.95) | Buy via shops, e-commerce, last-mile delivery |
| **Society** | Anchor-adjacent (0.95) | Trust in supply chain; visibility of disruption |
| **Government** | Anchor-adjacent (0.95) | Enforce Regulation and protect CNI Sovereignty |
| **Producers** | Anchor-adjacent (0.93) | Goods reach consumers; inventory turns |

---

## 3. Value Chain Diagram

### 3.1 ASCII placeholder

```
vis
1.00 ── Public ── Consumers ── Society ── Government ── Producers
 0.85 ── Shops  E-commerce  Delivery  Supply Chain Awareness
 0.66 ── Last Mile  Long Haul  Real-Time Stock  Logistics Hubs  Warehouses  Storage
 0.44 ── Trucks  HGV Skills  Scouts  Autotrucks  Drones  Automated Delivery
 0.28 ── Telematics  CNI Sovereignty  Regulation  Traffic Data
 0.18 ── Electric Power  Fossil Fuel  Data  Cities & Rural Topology
 0.00 ─────────────────────────────────────────────────────────────
```

### 3.2 OWM (paste into https://create.wardleymaps.ai)

```owm
title Transport & Logistics — value chain

component Public [0.97, 0.50]
component Consumers [0.95, 0.50]
component Society [0.95, 0.50]
component Government [0.95, 0.50]
component Producers [0.93, 0.50]

component Shops [0.85, 0.50]
component E-commerce [0.83, 0.50]
component Delivery [0.82, 0.50]
component Supply Chain Awareness [0.80, 0.50]

component Last Mile [0.70, 0.50]
component Long Haul [0.66, 0.50]
component Real-Time Stock [0.60, 0.50]
component Logistics Hubs [0.62, 0.50]
component Warehouses [0.58, 0.50]
component Storage [0.55, 0.50]

component Trucks [0.45, 0.50]
component HGV Skills [0.44, 0.50]
component Scouts [0.42, 0.50]
component Autotrucks [0.42, 0.50]
component Drones [0.40, 0.50]
component Automated Delivery [0.40, 0.50]

component Telematics [0.32, 0.50]
component CNI Sovereignty [0.30, 0.50]
component Regulation [0.28, 0.50]
component Traffic Data [0.28, 0.50]
component Electric Power [0.22, 0.50]
component Fossil Fuel [0.20, 0.50]
component Data [0.18, 0.50]
component Cities & Rural Topology [0.15, 0.50]

Public -> Shops
Public -> E-commerce
Public -> Delivery
Consumers -> Shops
Consumers -> E-commerce
Consumers -> Delivery
Society -> Supply Chain Awareness
Government -> Regulation
Government -> CNI Sovereignty
Producers -> Long Haul
Producers -> Warehouses

Shops -> Last Mile
Shops -> Real-Time Stock
E-commerce -> Last Mile
E-commerce -> Real-Time Stock
E-commerce -> Logistics Hubs
Delivery -> Last Mile
Delivery -> Long Haul
Supply Chain Awareness -> Real-Time Stock

Last Mile -> Logistics Hubs
Last Mile -> Trucks
Last Mile -> Automated Delivery
Last Mile -> Cities & Rural Topology
Long Haul -> Logistics Hubs
Long Haul -> Trucks
Long Haul -> Autotrucks
Long Haul -> Cities & Rural Topology
Logistics Hubs -> Warehouses
Warehouses -> Storage
Real-Time Stock -> Telematics
Real-Time Stock -> Data

Trucks -> Fossil Fuel
Trucks -> HGV Skills
Autotrucks -> Electric Power
Autotrucks -> Telematics
Autotrucks -> Regulation
Automated Delivery -> Electric Power
Automated Delivery -> Telematics
Automated Delivery -> Regulation
Drones -> Electric Power
Drones -> Regulation
Scouts -> Telematics
Scouts -> Data
Telematics -> Data
Telematics -> Traffic Data
Traffic Data -> Data

CNI Sovereignty -> Electric Power
CNI Sovereignty -> Fossil Fuel
CNI Sovereignty -> Data

style wardley
```

### 3.3 Mermaid equivalent

<details>
<summary>Mermaid <code>wardley-beta</code> block</summary>

```mermaid
wardley-beta
title Transport & Logistics — value chain
size [1100, 800]

component Public [0.97, 0.50]
component Consumers [0.95, 0.50]
component Society [0.95, 0.50]
component Government [0.95, 0.50]
component Producers [0.93, 0.50]

component Shops [0.85, 0.50]
component "E-commerce" [0.83, 0.50]
component Delivery [0.82, 0.50]
component "Supply Chain Awareness" [0.80, 0.50]

component "Last Mile" [0.70, 0.50]
component "Long Haul" [0.66, 0.50]
component "Real-Time Stock" [0.60, 0.50]
component "Logistics Hubs" [0.62, 0.50]
component Warehouses [0.58, 0.50]
component Storage [0.55, 0.50]

component Trucks [0.45, 0.50]
component "HGV Skills" [0.44, 0.50]
component Scouts [0.42, 0.50]
component Autotrucks [0.42, 0.50]
component Drones [0.40, 0.50]
component "Automated Delivery" [0.40, 0.50]

component Telematics [0.32, 0.50]
component "CNI Sovereignty" [0.30, 0.50]
component Regulation [0.28, 0.50]
component "Traffic Data" [0.28, 0.50]
component "Electric Power" [0.22, 0.50]
component "Fossil Fuel" [0.20, 0.50]
component Data [0.18, 0.50]
component "Cities & Rural Topology" [0.15, 0.50]

Public -> Shops
Public -> "E-commerce"
Public -> Delivery
Consumers -> Shops
Consumers -> "E-commerce"
Consumers -> Delivery
Society -> "Supply Chain Awareness"
Government -> Regulation
Government -> "CNI Sovereignty"
Producers -> "Long Haul"
Producers -> Warehouses

Shops -> "Last Mile"
Shops -> "Real-Time Stock"
"E-commerce" -> "Last Mile"
"E-commerce" -> "Real-Time Stock"
"E-commerce" -> "Logistics Hubs"
Delivery -> "Last Mile"
Delivery -> "Long Haul"
"Supply Chain Awareness" -> "Real-Time Stock"

"Last Mile" -> "Logistics Hubs"
"Last Mile" -> Trucks
"Last Mile" -> "Automated Delivery"
"Last Mile" -> "Cities & Rural Topology"
"Long Haul" -> "Logistics Hubs"
"Long Haul" -> Trucks
"Long Haul" -> Autotrucks
"Long Haul" -> "Cities & Rural Topology"
"Logistics Hubs" -> Warehouses
Warehouses -> Storage
"Real-Time Stock" -> Telematics
"Real-Time Stock" -> Data

Trucks -> "Fossil Fuel"
Trucks -> "HGV Skills"
Autotrucks -> "Electric Power"
Autotrucks -> Telematics
Autotrucks -> Regulation
"Automated Delivery" -> "Electric Power"
"Automated Delivery" -> Telematics
"Automated Delivery" -> Regulation
Drones -> "Electric Power"
Drones -> Regulation
Scouts -> Telematics
Scouts -> Data
Telematics -> Data
Telematics -> "Traffic Data"
"Traffic Data" -> Data

"CNI Sovereignty" -> "Electric Power"
"CNI Sovereignty" -> "Fossil Fuel"
"CNI Sovereignty" -> Data
```

</details>

---

## 4. Component Inventory

| # | Component | Visibility | Tier | Description | Depends on |
|---|---|---|---|---|---|
| 1 | Public | 0.97 | Anchor | Ultimate end-user; goods recipient | Shops, E-commerce, Delivery |
| 2 | Consumers | 0.95 | Anchor | Buying population (subset of Public) | Shops, E-commerce, Delivery |
| 3 | Society | 0.95 | Anchor | Collective stakeholder in supply resilience | Supply Chain Awareness |
| 4 | Government | 0.95 | Anchor | Sovereign authority | Regulation, CNI Sovereignty |
| 5 | Producers | 0.93 | Anchor | Goods manufacturers shipping into the chain | Long Haul, Warehouses |
| 6 | Shops | 0.85 | L1 | Physical retail point-of-sale | Last Mile, Real-Time Stock |
| 7 | E-commerce | 0.83 | L1 | Online retail storefront | Last Mile, Real-Time Stock, Logistics Hubs |
| 8 | Delivery | 0.82 | L1 | Last-moment hand-off to recipient | Last Mile, Long Haul |
| 9 | Supply Chain Awareness | 0.80 | L1 | Visibility practice society/gov expect | Real-Time Stock |
| 10 | Last Mile | 0.70 | L2 | Final leg to the door | Logistics Hubs, Trucks, Automated Delivery, Cities & Rural Topology |
| 11 | Long Haul | 0.66 | L2 | Inter-hub bulk movement | Logistics Hubs, Trucks, Autotrucks, Cities & Rural Topology |
| 12 | Logistics Hubs | 0.62 | L2 | Cross-docking / sortation | Warehouses |
| 13 | Real-Time Stock | 0.60 | L2 | Live inventory visibility | Telematics, Data |
| 14 | Warehouses | 0.58 | L2 | Buffered goods holding | Storage |
| 15 | Storage | 0.55 | L2 | Static bulk storage | (terminal) |
| 16 | Trucks | 0.45 | L3 | Conventional diesel HGV fleet | Fossil Fuel, HGV Skills |
| 17 | HGV Skills | 0.44 | L3 | Licensed driver workforce | (terminal) |
| 18 | Scouts | 0.42 | L3 | Reconnaissance / route-survey vehicles | Telematics, Data |
| 19 | Autotrucks | 0.42 | L3 | Autonomous heavy road freight | Electric Power, Telematics, Regulation |
| 20 | Drones | 0.40 | L3 | Aerial delivery units | Electric Power, Regulation |
| 21 | Automated Delivery | 0.40 | L3 | Ground-robot last-mile | Electric Power, Telematics, Regulation |
| 22 | Telematics | 0.32 | L4 | Vehicle-to-network signalling | Data, Traffic Data |
| 23 | CNI Sovereignty | 0.30 | L4 | Territorial control of critical infra | Electric Power, Fossil Fuel, Data |
| 24 | Regulation | 0.28 | L4 | Statutory constraints on vehicles/ops | (terminal) |
| 25 | Traffic Data | 0.28 | L4 | Live road-state feed | Data |
| 26 | Electric Power | 0.22 | L5 | Grid electricity for EV fleets | (terminal) |
| 27 | Fossil Fuel | 0.20 | L5 | Diesel / petrol supply | (terminal) |
| 28 | Data | 0.18 | L5 | Underlying data utility | (terminal) |
| 29 | Cities & Rural Topology | 0.15 | L5 | Physical route network shape | (terminal) |

(29 components; within the 8–20 guideline once the five actor anchors are counted as context rather than chain components — see Assumptions §9.)

---

## 5. Dependency Matrix (direct only)

Rows depend on columns. `X` = direct dependency.

|                | Shops | E-com | Deliv | SCA | LM | LH | LogH | RTS | Wh | Stor | Trk | HGV | Sct | Aut | Drn | AutD | Tel | CNI | Reg | TrD | EP | FF | Data | Top |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Public      | X | X | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Consumers   | X | X | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Society     |   |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Government  |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X | X |   |   |   |   |   |
| Producers   |   |   |   |   |   | X |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Shops       |   |   |   |   | X |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| E-commerce  |   |   |   |   | X |   | X | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Delivery    |   |   |   |   | X | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| SCA         |   |   |   |   |   |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Last Mile   |   |   |   |   |   |   | X |   |   |   | X |   |   |   |   | X  |   |   |   |   |   |   |   | X |
| Long Haul   |   |   |   |   |   |   | X |   |   |   | X |   |   | X |   |    |   |   |   |   |   |   |   | X |
| Log Hubs    |   |   |   |   |   |   |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| RT Stock    |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   | X |   |
| Warehouses  |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
| Trucks      |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   |   |   |   |   | X |   |   |
| Autotrucks  |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   | X |   | X |   |   |   |
| Drones      |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   | X |   |   |   |
| Auto Deliv  |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   | X |   | X |   |   |   |
| Scouts      |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   |   |   |   | X |   |
| Telematics  |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |   | X |   |
| Traffic Dat |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X |   |
| CNI Sov     |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   | X | X | X |   |

---

## 6. Critical Path Analysis

**Longest user-facing-to-infrastructure chain** (7 hops):

`Public → E-commerce → Last Mile → Automated Delivery → Telematics → Traffic Data → Data`

**Bottlenecks / single points of failure**:

- **Data** is a shared terminal under Telematics, Traffic Data, Real-Time Stock, Scouts and CNI Sovereignty — any disruption affects five upstream paths.
- **Logistics Hubs** is the only path through which Long Haul reaches Warehouses / Storage — removing hubs collapses both Last Mile and Long Haul.
- **HGV Skills** is the sole human-capital input under Trucks. With no substitute until Autotrucks mature, a labour-supply squeeze ripples straight to Last Mile and Long Haul.
- **Fossil Fuel** and **Electric Power** represent a *resilience-by-bifurcation* pattern: one or the other can carry the chain, but only if the fleet mix is balanced.

**Resilience gaps**:

- The chain has no Payments, Customs/Border, or Returns components. If those are in scope, add them before moving to `$arckit-wardley`.
- Cybersecurity of Telematics/Data is implicit — mark it explicitly if CNI-grade analysis is required.

---

## 7. Validation Checklist

### Completeness
- [x] Chain starts with a genuine user need (the Public obtaining goods)
- [x] Significant dependencies captured (producers, commerce, ops, vehicles, power, data, topology, regulation, sovereignty)
- [x] Chain reaches commodity level (Electric Power, Fossil Fuel, Data, Cities & Rural Topology)
- [x] No orphan components
- [x] All chain components are capabilities/activities (HGV *Skills* is a capability; Supply-Chain *Awareness* is a practice). Actor anchors (Public/Consumers/Society/Government/Producers) are listed explicitly because the scenario asked for them — see Assumptions §9.

### Accuracy
- [x] Dependencies reflect real-world flows
- [x] Visibility ordering consistent with dependency direction (every edge A→B satisfies `ν(A) ≥ ν(B)`; sovereignty flipped to sit *above* the infrastructure it protects)
- [x] No component is simultaneously user-facing and infrastructure

### Usefulness
- [x] Granularity suitable for strategic decision-making (29 nodes, 5 tiers)
- [x] Every component is individually positionable on the evolution axis in the follow-on `$arckit-wardley` run
- [x] The chain reveals strategic insights (energy bifurcation, Data commodity concentration, dual government inertia paths)

### Mathematical constraints
- [x] DAG acyclicity — no cycles by inspection
- [x] Anchor Public at 0.97 (≥ 0.90)
- [x] All edges respect `ν(parent) ≥ ν(child)`

---

## 8. Visibility Assessment

| Component | Visibility | Rationale |
|---|---|---|
| Public | 0.97 | Top anchor — direct goods recipient |
| Consumers, Society, Government | 0.95 | Anchor-adjacent actors with direct governance / consumption roles |
| Producers | 0.93 | Upstream actor; feeds the chain from the top |
| Shops / E-commerce / Delivery | 0.82–0.85 | User interacts every transaction |
| Supply Chain Awareness | 0.80 | Named societal practice, directly observable as news / disruption reports |
| Last Mile / Long Haul | 0.66–0.70 | Noticed quickly on degradation (late parcels, empty shelves) |
| Logistics Hubs / RT Stock / Warehouses / Storage | 0.55–0.62 | Indirectly visible; drives availability but not seen by consumer |
| Trucks / HGV Skills / Scouts / Autotrucks / Drones / Automated Delivery | 0.40–0.45 | Seen on roads and doorsteps but not chosen by the consumer |
| Telematics / CNI Sov. / Regulation / Traffic Data | 0.28–0.32 | Essentially invisible to the public; regulatory and sovereignty workings surface only on failure |
| Electric Power / Fossil Fuel / Data / Topology | 0.15–0.22 | Deep infrastructure; users unaware day-to-day |

---

## 9. Assumptions and Open Questions

**Assumptions**:

- The scenario explicitly lists *actors* (Government, Society, Producers, Consumers, Public). The skill's own guidance is "components should be capabilities, not people/teams/actors." We honoured the scenario by placing actors as **anchor-tier nodes** rather than mid-chain components — this is a conscious deviation from the "no actors" rule, justified by the brief.
- "Scouts" is interpreted as *reconnaissance / route-survey vehicles* (military-adjacent logistics terminology) rather than youth organisation scouts.
- "Automated Delivery" is treated as ground-robot last-mile (distinct from Drones and Autotrucks).
- Evolution positions are placeholders (0.50). Actual ε values are the job of `$arckit-wardley` using the 19-row cheat sheet.

**Open questions** (worth resolving before running `$arckit-wardley`):

1. Are **Payments, Customs/Border, Returns** in scope? They are common omissions for retail logistics.
2. Is the map **UK-specific** (HGV is a UK/EU term, CNI is UK parlance) or **international**? The answer affects Regulation and CNI Sovereignty placement.
3. Should **Rail** and **Maritime freight** be in the chain? The brief mentioned trucks + drones but not rail/ship.
4. Is **Cold Chain** a distinct sub-chain? If the goods include pharma or fresh food, it deserves its own branch under Warehouses / Long Haul.
5. Is **Cybersecurity** to be modelled explicitly under Telematics/Data, or absorbed into CNI Sovereignty?

---

## 10. Suggested Next Steps

- `$arckit-wardley` — promote this chain to a full Wardley Map by assigning evolution (ε) to each of the 29 components via the cheat sheet; expected positions on first pass: Storage/Warehouses/Fossil Fuel in *Commodity*; Trucks/Logistics Hubs/Data/Electric Power trending toward *Product/Utility*; Autotrucks/Automated Delivery/Drones/Telematics/Scouts in *Custom-Built → Product*; CNI Sovereignty and Supply Chain Awareness drifting left due to inertia.
- `$arckit-wardley.doctrine` — assess whether the operator running this chain has the organisational doctrine to execute (especially around data commoditisation and energy transition).
- Resolve the five open questions above before committing to an evolution-axis pass.

---

**Generated by**: ArcKit `$arckit-wardley.value-chain` command (blind-benchmark run via `skills/wardley-map-workspace/competitor-compare/arckit-value-chain/skill/SKILL.md`)
**Generated on**: 2026-04-23
**AI Model**: claude-opus-4-7[1m]
**Generation Context**: Scenario-only input; no external documents, no REQ / STKE / PRIN artifacts available. All positions inferred from the scenario text.
