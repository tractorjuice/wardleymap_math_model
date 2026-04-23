# Wardley Value Chain — Energy Disruption (July 2022)

**Command**: `arckit-wardley.value-chain`
**Scope**: Value chain decomposition only. Evolution axis (ε) set to 0.50 placeholder for every component, to be assigned by a subsequent `$arckit-wardley` run.

## 1. Executive Summary

The anchor is the energy consumer caught between **today's behaviour** (driven largely by price and reliability) and **tomorrow's behaviour** (shaped by sustainability, security of supply, and education). Both anchors share the chain below them but weight it differently: today leans on retail price, markets, and fossil/gas generation; tomorrow leans on CO2 accounting, supply-chain awareness, renewables, storage, and reserves. Thirty components are identified across six visibility levels, terminating at the externality commodity. Strategic insight: **storage and supply-chain awareness sit in the deep middle of the chain** — they are the pivot points that convert a brittle fossil-weighted generation mix into a resilient renewables-weighted one, which is why they are where disruption is most likely. Capital intensity of production, transmission, and distribution is the source of the lock-in that makes the transition slow.

## 2. Users and Personas

| User | Primary need |
|---|---|
| Household consumer (today) | Keep the lights on at a bill they can pay |
| Household consumer (tomorrow) | Energy that is secure, sustainable, and understood |
| Business / industrial consumer | Predictable price, reliable supply, CO2 reporting |
| Regulator / state | Public good delivery, security, CO2 targets |
| Generator / utility | Return on capital, market access, licence to operate |

## 3. Value Chain

### ASCII outline (visibility top → bottom)

```
0.98  Today Behaviour ────┐               ┌──── Tomorrow Behaviour  0.96
                          │               │
0.92  Affordability       │               │     Sustainability      0.88
0.90  Reliability         │               │     Security of Supply  0.86
                                                 Education          0.84
0.78  Retail Price
0.72  Spot Mkt   0.70 OTC Mkt   0.68 Public Good   0.66 Regulation
0.64  Control (Grid Balancing)     0.62 CO2 Accounting
0.60  Cost w/ Externalities        0.58 Supply-Chain Awareness
0.50  Distribution
0.44  Transmission
0.40  Production (Generation Ops)
0.36  Capital Intensity
0.34  Generation Mix
0.28  Wind   0.27 Solar µgen   0.26 Gas   0.24 Nuclear   0.22 Fossil
0.20  Storage
0.16  Batteries  0.14 Hydrogen  0.13 Pumped Hydro  0.12 Strategic Reserves
0.08  Externalities (Air, Climate, Land)
```

### OWM syntax

```owm
title Energy Disruption — July 2022

anchor Today Behaviour [0.98, 0.50]
anchor Tomorrow Behaviour [0.96, 0.50]

component Affordability [0.92, 0.50]
component Reliability [0.90, 0.50]
component Sustainability [0.88, 0.50]
component Security of Supply [0.86, 0.50]
component Education [0.84, 0.50]

component Retail Price [0.78, 0.50]
component Spot Market [0.72, 0.50]
component OTC Market [0.70, 0.50]
component Public Good Framing [0.68, 0.50]
component Regulation [0.66, 0.50]
component Control (Grid Balancing) [0.64, 0.50]
component CO2 Accounting [0.62, 0.50]
component Cost with Externalities [0.60, 0.50]
component Supply Chain Awareness [0.58, 0.50]

component Distribution [0.50, 0.50]
component Transmission [0.44, 0.50]
component Production (Generation Ops) [0.40, 0.50]
component Capital Intensity [0.36, 0.50]

component Generation Mix [0.34, 0.50]
component Renewables (Wind) [0.28, 0.50]
component Solar Microgen [0.27, 0.50]
component Gas Generation [0.26, 0.50]
component Nuclear Generation [0.24, 0.50]
component Fossil Generation [0.22, 0.50]

component Storage [0.20, 0.50]
component Electrical Storage (Batteries) [0.16, 0.50]
component Hydrogen Storage [0.14, 0.50]
component Potential Energy Storage (Pumped Hydro) [0.13, 0.50]
component Strategic Reserves [0.12, 0.50]

component Externalities (Air, Climate, Land) [0.08, 0.50]

Today Behaviour -> Affordability
Today Behaviour -> Reliability
Today Behaviour -> Retail Price
Tomorrow Behaviour -> Sustainability
Tomorrow Behaviour -> Security of Supply
Tomorrow Behaviour -> Education

Affordability -> Retail Price
Reliability -> Control (Grid Balancing)
Reliability -> Distribution
Sustainability -> CO2 Accounting
Sustainability -> Cost with Externalities
Security of Supply -> Supply Chain Awareness
Security of Supply -> Strategic Reserves
Education -> Public Good Framing

Retail Price -> Spot Market
Retail Price -> OTC Market
Retail Price -> Regulation
Spot Market -> Production (Generation Ops)
OTC Market -> Production (Generation Ops)
Public Good Framing -> Regulation
Regulation -> Control (Grid Balancing)
Regulation -> CO2 Accounting
Control (Grid Balancing) -> Transmission
Control (Grid Balancing) -> Generation Mix
CO2 Accounting -> Generation Mix
CO2 Accounting -> Externalities (Air, Climate, Land)
Cost with Externalities -> Externalities (Air, Climate, Land)
Supply Chain Awareness -> Generation Mix
Supply Chain Awareness -> Capital Intensity

Distribution -> Transmission
Transmission -> Production (Generation Ops)
Production (Generation Ops) -> Generation Mix
Production (Generation Ops) -> Capital Intensity
Capital Intensity -> Generation Mix

Generation Mix -> Renewables (Wind)
Generation Mix -> Solar Microgen
Generation Mix -> Gas Generation
Generation Mix -> Nuclear Generation
Generation Mix -> Fossil Generation
Generation Mix -> Storage

Storage -> Electrical Storage (Batteries)
Storage -> Hydrogen Storage
Storage -> Potential Energy Storage (Pumped Hydro)
Storage -> Strategic Reserves

Renewables (Wind) -> Externalities (Air, Climate, Land)
Solar Microgen -> Externalities (Air, Climate, Land)
Gas Generation -> Externalities (Air, Climate, Land)
Nuclear Generation -> Externalities (Air, Climate, Land)
Fossil Generation -> Externalities (Air, Climate, Land)

style wardley
```

### Mermaid equivalent

<details>
<summary>Mermaid wardley-beta block</summary>

```mermaid
wardley-beta
title Energy Disruption July 2022
size [1100, 800]

anchor "Today Behaviour" [0.98, 0.50]
anchor "Tomorrow Behaviour" [0.96, 0.50]

component Affordability [0.92, 0.50]
component Reliability [0.90, 0.50]
component Sustainability [0.88, 0.50]
component "Security of Supply" [0.86, 0.50]
component Education [0.84, 0.50]

component "Retail Price" [0.78, 0.50]
component "Spot Market" [0.72, 0.50]
component "OTC Market" [0.70, 0.50]
component "Public Good Framing" [0.68, 0.50]
component Regulation [0.66, 0.50]
component "Control (Grid Balancing)" [0.64, 0.50]
component "CO2 Accounting" [0.62, 0.50]
component "Cost with Externalities" [0.60, 0.50]
component "Supply Chain Awareness" [0.58, 0.50]

component Distribution [0.50, 0.50]
component Transmission [0.44, 0.50]
component "Production (Generation Ops)" [0.40, 0.50]
component "Capital Intensity" [0.36, 0.50]

component "Generation Mix" [0.34, 0.50]
component "Renewables (Wind)" [0.28, 0.50]
component "Solar Microgen" [0.27, 0.50]
component "Gas Generation" [0.26, 0.50]
component "Nuclear Generation" [0.24, 0.50]
component "Fossil Generation" [0.22, 0.50]

component Storage [0.20, 0.50]
component "Electrical Storage (Batteries)" [0.16, 0.50]
component "Hydrogen Storage" [0.14, 0.50]
component "Potential Energy Storage (Pumped Hydro)" [0.13, 0.50]
component "Strategic Reserves" [0.12, 0.50]

component "Externalities (Air, Climate, Land)" [0.08, 0.50]

"Today Behaviour" -> Affordability
"Today Behaviour" -> Reliability
"Today Behaviour" -> "Retail Price"
"Tomorrow Behaviour" -> Sustainability
"Tomorrow Behaviour" -> "Security of Supply"
"Tomorrow Behaviour" -> Education

Affordability -> "Retail Price"
Reliability -> "Control (Grid Balancing)"
Reliability -> Distribution
Sustainability -> "CO2 Accounting"
Sustainability -> "Cost with Externalities"
"Security of Supply" -> "Supply Chain Awareness"
"Security of Supply" -> "Strategic Reserves"
Education -> "Public Good Framing"

"Retail Price" -> "Spot Market"
"Retail Price" -> "OTC Market"
"Retail Price" -> Regulation
"Spot Market" -> "Production (Generation Ops)"
"OTC Market" -> "Production (Generation Ops)"
"Public Good Framing" -> Regulation
Regulation -> "Control (Grid Balancing)"
Regulation -> "CO2 Accounting"
"Control (Grid Balancing)" -> Transmission
"Control (Grid Balancing)" -> "Generation Mix"
"CO2 Accounting" -> "Generation Mix"
"CO2 Accounting" -> "Externalities (Air, Climate, Land)"
"Cost with Externalities" -> "Externalities (Air, Climate, Land)"
"Supply Chain Awareness" -> "Generation Mix"
"Supply Chain Awareness" -> "Capital Intensity"

Distribution -> Transmission
Transmission -> "Production (Generation Ops)"
"Production (Generation Ops)" -> "Generation Mix"
"Production (Generation Ops)" -> "Capital Intensity"
"Capital Intensity" -> "Generation Mix"

"Generation Mix" -> "Renewables (Wind)"
"Generation Mix" -> "Solar Microgen"
"Generation Mix" -> "Gas Generation"
"Generation Mix" -> "Nuclear Generation"
"Generation Mix" -> "Fossil Generation"
"Generation Mix" -> Storage

Storage -> "Electrical Storage (Batteries)"
Storage -> "Hydrogen Storage"
Storage -> "Potential Energy Storage (Pumped Hydro)"
Storage -> "Strategic Reserves"

"Renewables (Wind)" -> "Externalities (Air, Climate, Land)"
"Solar Microgen" -> "Externalities (Air, Climate, Land)"
"Gas Generation" -> "Externalities (Air, Climate, Land)"
"Nuclear Generation" -> "Externalities (Air, Climate, Land)"
"Fossil Generation" -> "Externalities (Air, Climate, Land)"
```

</details>

## 4. Component Inventory

| # | Component | Visibility | Description | Depends on |
|---|---|---|---|---|
| A1 | Today Behaviour | 0.98 | Anchor: how the consumer uses energy now | Affordability, Reliability, Retail Price |
| A2 | Tomorrow Behaviour | 0.96 | Anchor: how the consumer will use energy post-transition | Sustainability, Security of Supply, Education |
| 1 | Affordability | 0.92 | Bill the consumer can afford | Retail Price |
| 2 | Reliability | 0.90 | Always-on supply | Control, Distribution |
| 3 | Sustainability | 0.88 | Low-carbon consumption | CO2 Accounting, Cost with Externalities |
| 4 | Security of Supply | 0.86 | Domestic resilience to shocks | Supply Chain Awareness, Strategic Reserves |
| 5 | Education | 0.84 | Consumer literacy about the transition | Public Good Framing |
| 6 | Retail Price | 0.78 | Tariff seen on the bill | Spot Market, OTC Market, Regulation |
| 7 | Spot Market | 0.72 | Real-time wholesale | Production |
| 8 | OTC Market | 0.70 | Bilateral forward contracts | Production |
| 9 | Public Good Framing | 0.68 | Energy as a shared civic good, not purely private | Regulation |
| 10 | Regulation | 0.66 | Licences, codes, price caps, obligations | Control, CO2 Accounting |
| 11 | Control (Grid Balancing) | 0.64 | Frequency, balancing, ancillary services | Transmission, Generation Mix |
| 12 | CO2 Accounting | 0.62 | Scope 1/2/3 reporting, carbon pricing | Generation Mix, Externalities |
| 13 | Cost with Externalities | 0.60 | Full-social-cost pricing | Externalities |
| 14 | Supply Chain Awareness | 0.58 | Where fuels / parts / critical minerals come from | Generation Mix, Capital Intensity |
| 15 | Distribution | 0.50 | Low-voltage delivery to premises | Transmission |
| 16 | Transmission | 0.44 | High-voltage long-haul | Production |
| 17 | Production (Generation Ops) | 0.40 | Operating generating assets | Generation Mix, Capital Intensity |
| 18 | Capital Intensity | 0.36 | Financing / amortisation of long-lived assets | Generation Mix |
| 19 | Generation Mix | 0.34 | Portfolio of generating technologies | Wind, Solar µgen, Gas, Nuclear, Fossil, Storage |
| 20 | Renewables (Wind) | 0.28 | Onshore/offshore wind | Externalities |
| 21 | Solar Microgen | 0.27 | Rooftop PV, behind-the-meter | Externalities |
| 22 | Gas Generation | 0.26 | CCGT, peakers | Externalities |
| 23 | Nuclear Generation | 0.24 | Fission baseload | Externalities |
| 24 | Fossil Generation | 0.22 | Coal, oil | Externalities |
| 25 | Storage | 0.20 | Buffer between intermittent generation and demand | Batteries, Hydrogen, Pumped Hydro, Reserves |
| 26 | Electrical Storage (Batteries) | 0.16 | Grid-scale Li-ion | — |
| 27 | Hydrogen Storage | 0.14 | Green/blue H2 as energy carrier | — |
| 28 | Potential Energy (Pumped Hydro) | 0.13 | Long-duration mechanical | — |
| 29 | Strategic Reserves | 0.12 | State-held gas, oil | — |
| 30 | Externalities | 0.08 | Air, climate, land, water impacts — the commodity "sink" | — |

## 5. Dependency Matrix (high-level; X = direct)

| parent\child | Price | Markets | Regulation | Control | CO2 | Supply Chain | Distribution | Transmission | Production | Capital | Gen Mix | Storage | Externalities |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Today Behaviour | X | | | | | | | | | | | | |
| Tomorrow Behaviour | | | | | X (via Sust.) | X (via Sec.) | | | | | | | |
| Affordability | X | | | | | | | | | | | | |
| Reliability | | | | X | | | X | | | | | | |
| Sustainability | | | | | X | | | | | | | | X |
| Security of Supply | | | | | | X | | | | | | X (reserves) | |
| Retail Price | | X | X | | | | | | | | | | |
| Regulation | | | | X | X | | | | | | | | |
| Control | | | | | | | | X | | | X | | |
| Supply Chain | | | | | | | | | | X | X | | |
| Production | | | | | | | | | | X | X | | |
| Gen Mix | | | | | | | | | | | | X | X |
| Storage | | | | | | | | | | | | | — |

## 6. Critical Path Analysis

**Spine (anchor → commodity)**:

Today Behaviour → Retail Price → Spot Market → Production → Generation Mix → Gas Generation → Externalities

**Where disruption is most likely** (pressure building in July 2022):

- **Storage** (v=0.20) — underbuilt relative to a wind-heavy mix; batteries + hydrogen + pumped hydro are all racing.
- **Supply Chain Awareness** (v=0.58) — exposed by the Russia/gas shock; cross-cuts Generation Mix and Capital Intensity.
- **Solar Microgen** (v=0.27) — consumer-behind-the-meter economics flip when retail prices spike.

**Infrastructure lock-in** (capital-intensive, slow-moving):

- **Transmission** (v=0.44), **Distribution** (v=0.50), **Production** (v=0.40), **Capital Intensity** (v=0.36), **Nuclear Generation** (v=0.24), **Gas Generation** (v=0.26). These are the parts of the chain that explain why the transition takes decades despite clear user demand.

**Externality picture**:

Every generation technology terminates at a single `Externalities (Air, Climate, Land)` sink, plus a direct link from `CO2 Accounting` and `Cost with Externalities`. This makes externalities the terminal commodity of the map — pricing them in is what rewires everything above.

**Single points of failure**:

- Transmission: a single high-voltage backbone; failure blacks out distribution.
- Regulation: every market behaviour and control action routes through it.
- Generation Mix: all storage and all externalities hang off it.

## 7. Validation Checklist

- [x] Chain starts with a genuine user need (Today/Tomorrow Behaviour), not a product
- [x] All significant dependencies captured (30 nodes, ~55 edges)
- [x] Chain reaches a commodity sink (Externalities)
- [x] No orphan components — every node connects up and/or down
- [x] Components are capabilities/activities, not actors
- [x] Dependencies reflect real energy-system structure (generation → transmission → distribution → retail → consumer)
- [x] Visibility ordering is consistent with dependency direction (parent ≥ child for every edge)
- [x] Granularity appropriate for strategic mapping (30 components — at the top of the recommended 8–25 band; retained because the scenario explicitly asks to cover five generation types and four storage types)
- [x] DAG acyclicity — manually verified; no back-edges
- [x] Anchor visibility ≥ 0.90 (0.98 and 0.96)

## 8. Visibility Assessment Rationale

| Component | v | Why |
|---|---|---|
| Today / Tomorrow Behaviour | 0.98 / 0.96 | Anchors — directly experienced by the consumer |
| Affordability, Reliability, Sustainability, Security, Education | 0.84–0.92 | The qualities the consumer names when asked |
| Retail Price | 0.78 | The single number on the bill |
| Markets / Public Good / Regulation | 0.66–0.72 | One step from price, visible in news coverage |
| Control, CO2, Cost, Supply Chain | 0.58–0.64 | Operational layers, visible only when they fail |
| Distribution / Transmission / Production | 0.40–0.50 | Classic grid middle — only visible on outage |
| Capital Intensity / Generation Mix | 0.34–0.36 | Structural, invisible in daily life |
| Generation technologies | 0.22–0.28 | Deeper still; visible only via policy debate |
| Storage & its children | 0.12–0.20 | Behind-the-scenes buffer |
| Externalities | 0.08 | The commodity sink the whole chain feeds |

## 9. Assumptions and Open Questions

**Assumptions**

1. The user is the end consumer (household/business); the map is not from the operator or state perspective.
2. `Today Behaviour` and `Tomorrow Behaviour` are modelled as **two anchors** rather than one, because the scenario explicitly contrasts them. Both share the chain below.
3. July 2022 context (Russia/gas shock, cost-of-living) motivates keeping Supply Chain Awareness and Strategic Reserves as first-class nodes.
4. `Storage` is modelled as a sibling of the generation technologies under `Generation Mix`, because the modern grid treats storage as a dispatchable generator-equivalent.
5. `Externalities` is the terminal commodity. CO2 Accounting and Cost-with-Externalities are the mechanisms that price it.

**Open questions for the subsequent `$arckit-wardley` run**

- Evolution positions for each generation technology in July 2022 (expectation: Fossil/Gas commodity, Nuclear product w/ inertia, Wind product, Solar µgen product→commodity, Hydrogen storage genesis/custom).
- Whether Storage should split into sub-anchors for long-duration vs short-duration.
- Whether `Public Good Framing` should be upgraded to a doctrine/gameplay artefact rather than a component.

---

**Note on scope**: This output is a **value chain only**. Every component carries the placeholder ε=0.50. A full Wardley Map — with evolution positions, movement arrows, and climatic-pattern annotations — is produced by a separate `$arckit-wardley` step that consumes this chain.
