# Wardley Value Chain — Transport Demand & Changing Consumer Behaviour (May 2022)

**Skill used:** `arckit-wardley.value-chain` — a value-chain decomposition skill. Evolution (X-axis) is NOT assigned at this stage; every component is pinned to ε=0.50 as a placeholder. A follow-on `$arckit-wardley` command would add the evolution axis.

---

## 1. Executive Summary

The anchor of this value chain is the **transport public's need to get from A to B**, with **government** and **transport operators** as co-stakeholders whose obligations shape the chain (regulation, infrastructure, operations). May 2022 is a specific moment: post-pandemic hybrid working has normalised virtual-space alternatives (Zoom) as a genuine *displacer* of physical trips, not merely a complement; fuel prices and cost-of-living have sharpened the cost dimension; rail strikes and climate commitments sit in tension with regulation and sustainability.

The chain decomposes 28 components across 7 visibility tiers, from user-facing journey attributes down to critical national infrastructure. Consumer behaviour is pulling **mode choice**, **virtual alternatives**, and **mobility hubs** forward; **regulation**, **city planning**, and **public infrastructure** show the lag.

## 2. Users and Personas (Anchors)

| Anchor | Primary need |
|---|---|
| Transport Public | Get from A to B reliably, safely, affordably, with awareness of options |
| Transport Operators | Serve demand profitably across private/shared/public modes |
| Government | Deliver a transport system that is safe, sustainable, resilient, and economically enabling |

## 3. Anchor Statement

```text
Anchor: The transport public can get from A to B (with acceptable ease, cost, access, safety, awareness), with the choice they make shaping the demand that operators serve and government regulates.
User: Transport Public (primary), Transport Operators and Government (co-anchors on the supply/regulatory side)
Outcome: A journey completed (physically, or substituted by a virtual alternative) whose mode is consistent with the user's behaviour, the operator's offer, and the government's policy envelope.
```

## 4. Value Chain Diagram (ASCII)

```
Vis    Component                                Tier
────   ──────────────────────────────────────   ─────────────
0.98   Government                               Anchor
0.96   Transport Public                         Anchor
0.94   Transport Operators                      Anchor
0.90   A-to-B Journey                           L1 user need
0.84   Ease of Use / Cost / Access / Safety / Awareness  L2 journey attributes
0.76   Mode Choice                              L3 decision
0.72   Virtual Space Alternatives               L3 substitution
0.70   Private / Shared / Distributed Public    L4 mode families
0.68   Demand Shocks                            L3 exogenous
0.66   Transport Information Stack              L4 information
0.64   Zoom                                     L5 virtual product
0.60   Transport Integration / Situational Svcs L5 info services
0.58   Mobility Hubs                            L5 nodes
0.54   Vehicles                                 L5 physical
0.50   Regulation                               L5 governance
0.48   Car / Train                              L6 vehicle types
0.46   Sustainability and Climate               L6 policy driver
0.44   City Planning                            L6 spatial
0.40   Connectivity                             L7 utility
0.38   Cybersecurity                            L7 utility
0.34   Public Infra / Private Infra             L7 build
0.22   Critical National Infrastructure         L8 CNI
```

## 5. OWM Source

```owm
title Transport Demand — Changing Consumer Behaviour (May 2022)

anchor Government [0.98, 0.50]
anchor Transport Public [0.96, 0.50]
anchor Transport Operators [0.94, 0.50]

component A to B Journey [0.90, 0.50]
component Ease of Use [0.84, 0.50]
component Cost [0.84, 0.50]
component Access to Service [0.84, 0.50]
component Personal and Physical Safety [0.84, 0.50]
component Awareness [0.84, 0.50]

component Mode Choice [0.76, 0.50]
component Private Transport [0.70, 0.50]
component Shared Transport [0.70, 0.50]
component Distributed Public Transport [0.70, 0.50]

component Virtual Space Alternatives [0.72, 0.50]
component Zoom [0.64, 0.50]

component Transport Information Stack [0.66, 0.50]
component Transport Integration [0.60, 0.50]
component Situational Services [0.60, 0.50]
component Mobility Hubs [0.58, 0.50]

component Vehicles [0.54, 0.50]
component Car [0.48, 0.50]
component Train [0.48, 0.50]

component Connectivity [0.40, 0.50]
component Cybersecurity [0.38, 0.50]

component City Planning [0.44, 0.50]
component Public Infrastructure [0.34, 0.50]
component Private Infrastructure [0.34, 0.50]
component Critical National Infrastructure [0.22, 0.50]

component Regulation [0.50, 0.50]
component Sustainability and Climate [0.46, 0.50]
component Demand Shocks [0.68, 0.50]

Government -> Regulation
Government -> Critical National Infrastructure
Government -> City Planning
Government -> Sustainability and Climate

Transport Public -> A to B Journey
Transport Public -> Virtual Space Alternatives
Transport Operators -> Mode Choice
Transport Operators -> Transport Information Stack
Transport Operators -> Vehicles

A to B Journey -> Ease of Use
A to B Journey -> Cost
A to B Journey -> Access to Service
A to B Journey -> Personal and Physical Safety
A to B Journey -> Awareness
A to B Journey -> Mode Choice
A to B Journey -> Demand Shocks

Ease of Use -> Transport Information Stack
Access to Service -> Mode Choice
Awareness -> Transport Information Stack

Virtual Space Alternatives -> Zoom
Zoom -> Connectivity

Mode Choice -> Private Transport
Mode Choice -> Shared Transport
Mode Choice -> Distributed Public Transport

Private Transport -> Car
Shared Transport -> Car
Distributed Public Transport -> Train

Transport Information Stack -> Transport Integration
Transport Information Stack -> Situational Services
Transport Information Stack -> Mobility Hubs
Transport Integration -> Connectivity
Situational Services -> Connectivity
Mobility Hubs -> Public Infrastructure

Vehicles -> Car
Vehicles -> Train
Car -> Private Infrastructure
Train -> Public Infrastructure
Car -> Connectivity
Train -> Connectivity

Connectivity -> Cybersecurity
Connectivity -> Critical National Infrastructure
Cybersecurity -> Critical National Infrastructure

City Planning -> Public Infrastructure
City Planning -> Private Infrastructure
Public Infrastructure -> Critical National Infrastructure
Private Infrastructure -> Critical National Infrastructure

Regulation -> Sustainability and Climate
Regulation -> Cybersecurity
Mode Choice -> Sustainability and Climate

Mode Choice -> Demand Shocks
Virtual Space Alternatives -> Demand Shocks

style wardley
```

<details>
<summary>Mermaid (wardley-beta) equivalent</summary>

```mermaid
wardley-beta
title Transport Demand — Changing Consumer Behaviour (May 2022)
size [1100, 800]

anchor Government [0.98, 0.50]
anchor "Transport Public" [0.96, 0.50]
anchor "Transport Operators" [0.94, 0.50]

component "A to B Journey" [0.90, 0.50]
component "Ease of Use" [0.84, 0.50]
component Cost [0.84, 0.50]
component "Access to Service" [0.84, 0.50]
component "Personal and Physical Safety" [0.84, 0.50]
component Awareness [0.84, 0.50]

component "Mode Choice" [0.76, 0.50]
component "Private Transport" [0.70, 0.50]
component "Shared Transport" [0.70, 0.50]
component "Distributed Public Transport" [0.70, 0.50]

component "Virtual Space Alternatives" [0.72, 0.50]
component Zoom [0.64, 0.50]

component "Transport Information Stack" [0.66, 0.50]
component "Transport Integration" [0.60, 0.50]
component "Situational Services" [0.60, 0.50]
component "Mobility Hubs" [0.58, 0.50]

component Vehicles [0.54, 0.50]
component Car [0.48, 0.50]
component Train [0.48, 0.50]

component Connectivity [0.40, 0.50]
component Cybersecurity [0.38, 0.50]

component "City Planning" [0.44, 0.50]
component "Public Infrastructure" [0.34, 0.50]
component "Private Infrastructure" [0.34, 0.50]
component "Critical National Infrastructure" [0.22, 0.50]

component Regulation [0.50, 0.50]
component "Sustainability and Climate" [0.46, 0.50]
component "Demand Shocks" [0.68, 0.50]

Government -> Regulation
Government -> "Critical National Infrastructure"
Government -> "City Planning"
Government -> "Sustainability and Climate"

"Transport Public" -> "A to B Journey"
"Transport Public" -> "Virtual Space Alternatives"
"Transport Operators" -> "Mode Choice"
"Transport Operators" -> "Transport Information Stack"
"Transport Operators" -> Vehicles

"A to B Journey" -> "Ease of Use"
"A to B Journey" -> Cost
"A to B Journey" -> "Access to Service"
"A to B Journey" -> "Personal and Physical Safety"
"A to B Journey" -> Awareness
"A to B Journey" -> "Mode Choice"
"A to B Journey" -> "Demand Shocks"

"Ease of Use" -> "Transport Information Stack"
"Access to Service" -> "Mode Choice"
Awareness -> "Transport Information Stack"

"Virtual Space Alternatives" -> Zoom
Zoom -> Connectivity

"Mode Choice" -> "Private Transport"
"Mode Choice" -> "Shared Transport"
"Mode Choice" -> "Distributed Public Transport"

"Private Transport" -> Car
"Shared Transport" -> Car
"Distributed Public Transport" -> Train

"Transport Information Stack" -> "Transport Integration"
"Transport Information Stack" -> "Situational Services"
"Transport Information Stack" -> "Mobility Hubs"
"Transport Integration" -> Connectivity
"Situational Services" -> Connectivity
"Mobility Hubs" -> "Public Infrastructure"

Vehicles -> Car
Vehicles -> Train
Car -> "Private Infrastructure"
Train -> "Public Infrastructure"
Car -> Connectivity
Train -> Connectivity

Connectivity -> Cybersecurity
Connectivity -> "Critical National Infrastructure"
Cybersecurity -> "Critical National Infrastructure"

"City Planning" -> "Public Infrastructure"
"City Planning" -> "Private Infrastructure"
"Public Infrastructure" -> "Critical National Infrastructure"
"Private Infrastructure" -> "Critical National Infrastructure"

Regulation -> "Sustainability and Climate"
Regulation -> Cybersecurity
"Mode Choice" -> "Sustainability and Climate"

"Mode Choice" -> "Demand Shocks"
"Virtual Space Alternatives" -> "Demand Shocks"
```

</details>

## 6. Component Inventory

| # | Component | Visibility | Description | Depends on |
|---|---|---:|---|---|
| 1 | Government | 0.98 | Policy-setting anchor | Regulation, CNI, City Planning, Sustainability and Climate |
| 2 | Transport Public | 0.96 | End-user anchor (travellers) | A to B Journey, Virtual Space Alternatives |
| 3 | Transport Operators | 0.94 | Supply anchor (rail, bus, taxi, MaaS) | Mode Choice, Information Stack, Vehicles |
| 4 | A to B Journey | 0.90 | The user need to move between two locations | Ease of Use, Cost, Access, Safety, Awareness, Mode Choice, Demand Shocks |
| 5 | Ease of Use | 0.84 | Frictionless planning, booking, paying | Information Stack |
| 6 | Cost | 0.84 | Price paid by the traveller | (terminal at this level) |
| 7 | Access to Service | 0.84 | Can the user reach a usable service from where they are | Mode Choice |
| 8 | Personal and Physical Safety | 0.84 | Felt and actual safety in transit | (terminal) |
| 9 | Awareness | 0.84 | Does the user know what options exist right now | Information Stack |
| 10 | Mode Choice | 0.76 | The decision of which transport mode to take | Private / Shared / Distributed Public |
| 11 | Virtual Space Alternatives | 0.72 | Replacing the trip with a virtual meeting | Zoom |
| 12 | Private Transport | 0.70 | Owned-vehicle modes | Car |
| 13 | Shared Transport | 0.70 | Ride-hail, car-share, bike-share | Car |
| 14 | Distributed Public Transport | 0.70 | Bus, metro, rail network | Train |
| 15 | Demand Shocks | 0.68 | Exogenous shifts (pandemic, fuel price, conflict) | Mode Choice, Virtual Alternatives |
| 16 | Transport Information Stack | 0.66 | Integrated journey-planning + real-time data | Integration, Situational Svcs, Hubs |
| 17 | Zoom | 0.64 | Named virtual-meeting product | Connectivity |
| 18 | Transport Integration | 0.60 | Cross-operator ticketing and routing | Connectivity |
| 19 | Situational Services | 0.60 | Real-time disruption, crowding, weather feeds | Connectivity |
| 20 | Mobility Hubs | 0.58 | Physical interchange nodes | Public Infrastructure |
| 21 | Vehicles | 0.54 | Operator-owned stock | Car, Train |
| 22 | Regulation | 0.50 | Rules: safety, subsidy, competition, emissions | Sustainability and Climate, Cybersecurity |
| 23 | Car | 0.48 | Road vehicle | Private Infra, Connectivity |
| 24 | Train | 0.48 | Rail vehicle | Public Infra, Connectivity |
| 25 | Sustainability and Climate | 0.46 | Net-zero and air-quality pressure | Mode Choice |
| 26 | City Planning | 0.44 | Land-use and network topology | Public Infra, Private Infra |
| 27 | Connectivity | 0.40 | Mobile/data networks for apps, vehicles, hubs | Cybersecurity, CNI |
| 28 | Cybersecurity | 0.38 | Protect connected vehicles, ticketing, CNI | CNI |
| 29 | Public Infrastructure | 0.34 | Roads (public), rail, stations | CNI |
| 30 | Private Infrastructure | 0.34 | Driveways, private rail, charging estates | CNI |
| 31 | Critical National Infrastructure | 0.22 | Grid, ports, trunk rail, strategic roads | (terminal) |

## 7. Dependency Matrix (highlights)

Direct edges (X) — showing the strategically-loaded rows. Full edge list is in the OWM above.

| From \ To | A-to-B | Mode Choice | Info Stack | Vehicles | Connectivity | CNI |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| Transport Public | X | I | I | I | I | I |
| Transport Operators | I | X | X | X | I | I |
| Government | I | I | I | I | I | X |
| A-to-B Journey | - | X | I | I | I | I |
| Mode Choice | - | - | I | I | I | I |
| Info Stack | - | I | - | I | X | I |
| Vehicles | - | I | I | - | X | I |

## 8. Critical Path Analysis

**Primary critical path (physical trip):**
`Transport Public → A-to-B Journey → Mode Choice → Distributed Public Transport → Train → Public Infrastructure → Critical National Infrastructure`

**Displacement path (virtual substitution):**
`Transport Public → Virtual Space Alternatives → Zoom → Connectivity → Cybersecurity → Critical National Infrastructure`

**Governance path:**
`Government → Regulation → Sustainability and Climate → Mode Choice`

**Bottlenecks / single points of failure:**

- **Connectivity** is a shared dependency for Info Stack, Zoom, Cars, Trains. An outage cascades across both physical and virtual paths.
- **Critical National Infrastructure** is the terminal commodity: every path ends here.
- **City Planning** is the only component coupling public and private infrastructure; re-zoning decisions unlock or block mobility-hub rollout.

**Resilience gaps (May 2022 reading):**

- Cybersecurity is a shallow branch off Connectivity rather than a first-class layer around vehicles, hubs, and ticketing — an understatement given the connected-vehicle threat surface.
- Mobility Hubs depend on Public Infrastructure only; private-infra funding (charging, kerbside) is not wired to hubs here, which matches the real policy gap.

## 9. Validation Checklist

**Completeness**
- [x] Anchor is a genuine user need (A-to-B), not a solution
- [x] Significant dependencies captured
- [x] Chain reaches commodity level (Critical National Infrastructure)
- [x] No orphan components
- [x] Components are activities/capabilities (Government/Public/Operators are modelled as anchors per the user prompt)

**Accuracy**
- [x] Dependencies reflect real-world technical/operational relationships
- [x] Visibility ordering consistent (parent >= child for every edge)
- [x] No component straddles user-facing and deep-infra tiers

**Usefulness**
- [x] Granularity supports strategic decisions
- [x] Each component is positionable on the evolution axis in a follow-on map
- [x] Chain exposes at least three strategic insights (see §11)

**Mathematical constraints (`tractorjuice/wardleymap_math_model`)**
- [x] DAG — no cycles
- [x] Visibility ordering ν(parent) >= ν(child) for all edges
- [x] Anchors >= 0.90

## 10. Visibility Assessment

| Band | Components |
|---|---|
| 0.90–1.00 (User-facing anchors & primary need) | Government 0.98, Transport Public 0.96, Transport Operators 0.94, A-to-B Journey 0.90 |
| 0.70–0.89 (High) | Journey attributes 0.84, Mode Choice 0.76, Virtual Alternatives 0.72, Private/Shared/Public modes 0.70 |
| 0.50–0.69 (Medium-high) | Demand Shocks 0.68, Info Stack 0.66, Zoom 0.64, Integration/Situational 0.60, Hubs 0.58, Vehicles 0.54, Regulation 0.50 |
| 0.30–0.49 (Medium) | Car/Train 0.48, Sustainability 0.46, City Planning 0.44, Connectivity 0.40, Cybersecurity 0.38, Public/Private Infra 0.34 |
| 0.10–0.29 (Low) | Critical National Infrastructure 0.22 |

## 11. Strategic Insights (what the prompt asked for)

**Where consumer behaviour is driving real evolution:**

1. **Virtual-space substitution is now a first-class branch of the value chain, not a footnote.** In pre-2020 maps, Zoom/telepresence would have been a weak signal; in May 2022 it sits next to Mode Choice as a peer, and Demand Shocks feed directly into it. The operator view of "transport demand" has been structurally reduced by a consumer-behaviour change that looks irreversible on hybrid-work timescales.
2. **Mobility Hubs and Transport Integration are pulled upward by user expectations of one-tap, multi-modal journeys** (the MaaS pattern), faster than the public-infrastructure layer below them can respond.
3. **Cost has been promoted to a top-tier journey attribute** by fuel prices and cost-of-living pressure — consumers now re-evaluate mode choice on price more actively than on time.

**Where regulation and infrastructure are lagging:**

1. **Regulation sits only at visibility 0.50** in the supply-side lane, below consumer-visible journey attributes, yet it gates Sustainability/Climate and Cybersecurity. This positional mismatch (low visibility, high leverage) is the lag: consumer behaviour moves in months, regulatory change in years.
2. **Public Infrastructure (0.34) and Critical National Infrastructure (0.22)** are correctly deep, but the chain shows that Mobility Hubs and Distributed Public Transport depend on them — meaning operator and user-level innovation is rate-limited by build cycles measured in decades.
3. **City Planning (0.44)** is the single coupling point between public and private infrastructure and is itself lagging both the hub rollout above it and the climate mandate beside it.

## 12. Assumptions and Open Questions

**Assumptions:**

- Treating Government, Transport Public, and Transport Operators as three co-anchors (per the user's explicit instruction) rather than a single anchor. The A-to-B journey is the *primary* user need the other two are organised around.
- "Zoom" is modelled as a named stand-in for the virtual-meeting category; a full map would likely generalise to "Remote Collaboration Platform" with Zoom as an instance.
- "Demand Shocks" is modelled as a component rather than an environmental variable because the prompt explicitly names it; in a climate-pattern pass it might migrate to a separate layer.
- Evolution positions are placeholders (ε = 0.50) — this skill is value-chain-only.

**Open questions for a follow-on map:**

- Should Cybersecurity be a layer wrapping Vehicles, Information Stack, and CNI rather than a child of Connectivity?
- Should there be an explicit Energy/Grid component distinct from CNI, given the EV transition?
- Active-travel modes (walking, cycling) were not called out in the prompt and are absent; worth adding for a real strategy conversation.
