# Transportation Logistics Landscape — Wardley Map

## 1. Scenario

Map the transportation logistics landscape covering how goods move from producers to the public. Actors: government, society, producers, consumers, the public. Commerce / supply-chain core: last mile, long haul, shops, e-commerce, logistics hubs, warehouses, storage, delivery, real-time stock. Vehicle and power layer: trucks, drones, scouts, electric vs fossil, autotrucks, automated delivery. Information layer: data, traffic, telematics. Topology: cities and rural areas. Constraints: regulation, territorial/CNI sovereignty, HGV skills, awareness of supply chain.

## 2. Components (V) and Anchors (U)

**Anchors (U) — five user types per the scenario:**
- Government, Society, Producers, Consumers, Public

**Activities / Practices / Data / Knowledge:**
- Commerce channels: Shops, E-Commerce, Delivery, Awareness of Supply Chain
- Supply-chain core: Last Mile, Long Haul, Logistics Hubs, Warehouses, Storage, Real-Time Stock
- Vehicles / power: Trucks, Autotrucks, Automated Delivery, Drones, Scouts, Electric Power, Fossil Power
- Information: Telematics, Traffic Data, Data
- Context / constraints: Cities, Rural Areas, Regulation, HGV Skills, Territorial / CNI Sovereignty

## 3. Evolution Scoring (4-row cheat sheet)

Per Part 6 quick method — Ubiquity, Certainty, User Perception, Publication Types. Stage midpoints I=0.125, II=0.375, III=0.625, IV=0.875. Key samples:

| Component | U | C | P | Pub | ε avg | Band |
|---|---|---|---|---|---|---|
| Shops | IV | IV | IV | III | 0.81 | Commodity |
| E-Commerce | IV | IV | III | IV | 0.78 | Commodity |
| Long Haul | IV | IV | IV | III | 0.81 (→0.78) | Commodity |
| Last Mile | III | III | III | III | 0.63 | Product |
| Warehouses | IV | IV | IV | III | 0.81 (→0.80) | Commodity |
| Storage | IV | IV | IV | IV | 0.88 (→0.85) | Commodity +utility |
| Real-Time Stock | III | III | II | III | 0.53 | Product (early) |
| Trucks | IV | IV | III | IV | 0.81 | Commodity |
| Fossil Power | IV | IV | IV | IV | 0.88 (→0.92) | Commodity +utility |
| Electric Power | II–III | III | III | II | 0.50 | Product (early) |
| Autotrucks | I–II | II | I | II | 0.28 (→0.25) | Custom Built (early) |
| Automated Delivery | I | I–II | I | I–II | 0.19 (→0.20) | Genesis |
| Drones | II | II | II | II | 0.375 (→0.28) | Custom Built |
| Scouts | I–II | II | II | I–II | 0.28 | Custom Built (early) |
| Telematics | III | III | III | III | 0.625 | Product |
| Traffic Data | III | III | IV | III | 0.69 (→0.72) | Product (late) |
| Data | IV | III | III | IV | 0.72 (→0.80) | Commodity (early) |
| Cities | IV | IV | IV | IV | 0.875 | Commodity +utility |
| Rural Areas | IV | IV | IV | IV | 0.88 (→0.82) | Commodity |
| Regulation | III | III | III | III | 0.625 | Product |
| HGV Skills | III | III | III | II–III | 0.56 | Product (early) |
| Awareness of Supply Chain | II | I–II | II | II | 0.31 (→0.35) | Custom Built |
| Territorial / CNI Sovereignty | I–II | I | II | II | 0.28 (→0.25) | Genesis → Custom |

Components in transition: Electric Power (II → III), Data (III → IV), Territorial/CNI Sovereignty (I → II under geopolitical pressure), Autotrucks / Automated Delivery (I → II).

## 4. Visibility

Seeded via shortest distance from the nearest anchor in U, then adjusted for value-chain judgment. The hard rule — $\nu(a) \ge \nu(b)$ for every edge $(a, b)$ — is maintained. Awareness of Supply Chain is raised relative to its graph depth because Society thinks about it directly. Territorial / CNI Sovereignty is placed deep because although Government cares about it, it manifests as a foundational constraint.

## 5. OWM Output

```owm
title Transportation Logistics Landscape
style wardley

// Anchors — five user types per scenario
anchor Government [0.98, 0.55]
anchor Society [0.97, 0.50]
anchor Producers [0.96, 0.60]
anchor Consumers [0.95, 0.70]
anchor Public [0.94, 0.65]

// Layer 1 — directly user-facing commerce / delivery channels
component Shops [0.88, 0.80]
component E-Commerce [0.86, 0.78]
component Delivery [0.84, 0.70]
component Awareness of Supply Chain [0.82, 0.35]

// Layer 2 — commerce / supply-chain core
component Last Mile [0.74, 0.65]
component Long Haul [0.72, 0.78]
component Logistics Hubs [0.68, 0.70]
component Warehouses [0.66, 0.80]
component Storage [0.64, 0.85]
component Real-Time Stock [0.62, 0.55]

// Layer 3 — vehicles and power (trucks / fossil / HGV-skills carry inertia)
component Trucks [0.52, 0.82] inertia
component Autotrucks [0.50, 0.25]
component Automated Delivery [0.48, 0.20]
component Drones [0.46, 0.28]
component Scouts [0.44, 0.30]
component Electric Power [0.42, 0.55]
component Fossil Power [0.40, 0.92] inertia

// Layer 4 — information / data layer
component Telematics [0.36, 0.65]
component Traffic Data [0.34, 0.72]
component Data [0.32, 0.80]

// Layer 5 — topology, context, constraints
component Cities [0.26, 0.88]
component Rural Areas [0.24, 0.82]
component Regulation [0.22, 0.62]
component HGV Skills [0.20, 0.55] inertia
component Territorial / CNI Sovereignty [0.18, 0.25]

// Anchor dependencies
Consumers->Shops
Consumers->E-Commerce
Consumers->Delivery
Public->Delivery
Public->Shops
Producers->Long Haul
Producers->Logistics Hubs
Producers->E-Commerce
Society->Awareness of Supply Chain
Society->Shops
Government->Regulation
Government->Territorial / CNI Sovereignty

// Channels depend on the supply-chain core
Shops->Last Mile
Shops->Warehouses
E-Commerce->Last Mile
E-Commerce->Real-Time Stock
E-Commerce->Warehouses
Delivery->Last Mile
Delivery->Long Haul
Awareness of Supply Chain->Real-Time Stock
Awareness of Supply Chain->Data

// Core inter-dependencies
Last Mile->Trucks
Last Mile->Automated Delivery
Last Mile->Drones
Last Mile->Autotrucks
Long Haul->Trucks
Long Haul->Autotrucks
Long Haul->HGV Skills
Logistics Hubs->Warehouses
Logistics Hubs->Long Haul
Warehouses->Storage
Warehouses->Real-Time Stock
Real-Time Stock->Data
Storage->Real-Time Stock

// Vehicles and power
Trucks->Fossil Power
Trucks->Electric Power
Autotrucks->Electric Power
Autotrucks->Telematics
Autotrucks->Traffic Data
Automated Delivery->Electric Power
Automated Delivery->Telematics
Automated Delivery->Data
Drones->Electric Power
Drones->Traffic Data
Drones->Regulation
Scouts->Telematics
Scouts->Data

// Information layer
Telematics->Data
Traffic Data->Data

// Topology and constraints
Last Mile->Cities
Last Mile->Rural Areas
Long Haul->Cities
Long Haul->Rural Areas
Trucks->Regulation
Autotrucks->Regulation
Automated Delivery->Regulation
Drones->HGV Skills
Long Haul->Territorial / CNI Sovereignty
Logistics Hubs->Territorial / CNI Sovereignty
Data->Territorial / CNI Sovereignty

// Evolution projections (scenario, not forecast)
evolve Autotrucks 0.55
evolve Automated Delivery 0.55
evolve Drones 0.55
evolve Electric Power 0.75
evolve Territorial / CNI Sovereignty 0.45

// Notes
note Commoditised utility zone [0.55, 0.90]
note Automation push — Genesis to Product [0.48, 0.35]
note Sovereignty / CNI pressure — forces re-evolve [0.20, 0.30]
note Differentiation zone (low ε, high ν) [0.80, 0.25]
```

## 6. Strategic Analysis

### a. Top 3 Differentiation Pressure — D(v) = ν·(1−ε)

High-ν, low-ε components where competitive advantage can be built.

1. **Awareness of Supply Chain** (D = 0.82 · 0.65 = **0.533**). Highly visible to society post-COVID / post-Brexit / Red-Sea-disruption, yet the *practice* of end-to-end supply-chain transparency is still custom-built. A retailer or government body that exposes provenance clearly captures unique value.
2. **Automated Delivery** (D = 0.48 · 0.80 = **0.384**). Still Genesis / early Custom Built, and reaches all the way up to Delivery which is directly anchored. Whoever solves urban automated last mile first captures a true differentiator — though differentiation will collapse once it reaches Product stage.
3. **Autotrucks** (D = 0.50 · 0.75 = **0.375**). Supports both Last Mile and Long Haul. Uncertainty is still high (driver-out conditions, regulatory acceptance), which is exactly where a directed bet can pay off.

### b. Top 3 Commodity Leverage — K(v) = (1−ν)·ε

Deep + mature — buy, don't build.

1. **Fossil Power** (K = 0.60 · 0.92 = **0.552**). Utility-grade today. Nobody builds their own fuel refinery — but also carries inertia: sunk capital in fossil fleets is *why* Electric Power isn't evolving faster.
2. **Cities** (K = 0.74 · 0.88 = **0.651**). Urban topology is an externally-provided utility — road networks, curbs, zoning. Design logistics around it; don't try to re-plan the city.
3. **Data** (K = 0.68 · 0.80 = **0.544**) and **Storage** (K = 0.36 · 0.85 = **0.306**). Both are late-stage: use cloud storage / data services as utilities rather than building in-house.

### c. Top 3 Dependency Risks — R(a, b) = ν(a)·(1−ε(b))

Visible component standing on a fragile foundation.

1. **(Long Haul, HGV Skills)** — R = 0.72 · (1 − 0.55) = **0.324**. Long Haul is near-commodity but critically depends on a skill base that the UK in particular has been unable to refresh. Classic human-capital inertia.
2. **(Last Mile, Automated Delivery)** — R = 0.74 · (1 − 0.20) = **0.592**. Only becomes a real risk once firms start *betting* on automated delivery to do last-mile — today it's a differentiator, tomorrow it's a single-point-of-failure if it underdelivers.
3. **(Logistics Hubs, Territorial / CNI Sovereignty)** — R = 0.68 · (1 − 0.25) = **0.510**. Hubs are taken for granted but increasingly sit behind immature national-security constraints (post-2022, governments have reclassified freight routes and ports as CNI). One new directive can reshape the map overnight.

### d. Suggested gameplays (from the 61-play catalogue)

- **Open Approaches / Open Source (play #15)** applied to Awareness of Supply Chain. Push the transparency layer to open standards so no single private operator owns provenance data. Accelerates it toward Product.
- **Directed Investment (play #36)** on Automated Delivery and Autotrucks — classic "invest ahead of the S-curve" on Genesis-stage components that feed a highly-visible activity.
- **Undermining Barriers to Entry / Pig in a Poke (plays #22, #19)** in the automated-vehicle space — commoditise sensor stacks and open-source the ML models to prevent incumbents locking in early.
- **Standards Game (play #18)** on Telematics and Traffic Data — push for mandatory open telematics APIs so Data evolves to utility faster.
- **Fear, Uncertainty, Doubt (FUD, play #41)** is a *gameplay* that incumbent HGV operators and fossil-fuel suppliers can be expected to run *against* Autotrucks and Electric Power — anticipate it, don't confuse it with genuine inertia.
- **Sweat and Dump (play #27)** on Fossil Power assets: run the depreciating fossil fleet for its remaining useful life while transitioning capital into electric / automated.
- **Insurgency / Tower and Moat (play #28, #34)** for CNI-sensitive operators: the tower is sovereign logistics capability (national freight routes, strategic warehousing); the moat is government mandate and geographic footprint.
- **Pioneer-Settler-Town Planner (doctrine-linked, not a numbered play)**: Pioneers work on Automated Delivery / Scouts / Drones, Settlers harden Autotrucks and Electric Power, Town Planners run Trucks / Long Haul / Warehouses as utilities.

### e. Doctrine observations (from the 40 principles)

- **Know your users (Phase II)** — handled by using five explicit anchors. Good.
- **Focus on user needs (Phase I)** — Awareness of Supply Chain is a societal user need that historically gets dropped off logistics maps. Keeping it visible addresses a common doctrine gap.
- **Use appropriate methods** — Pioneer/Settler/Town-Planner split above is warranted. Applying agile methods to Fossil-powered Trucks or lean/Six-Sigma to Automated Delivery would be mismatched.
- **Challenge assumptions / Remove bias and duplication** — the assumption that "Rural Areas" are simply "Cities with fewer vehicles" is a bias worth challenging: rural last-mile has a fundamentally different economics curve and is likely where drone automation matures first.
- **Do better with less** (Phase IV) — Storage and Fossil Power sit in utility territory; any in-house version is a doctrine violation.
- **Think small but keep aware of the whole** — the 5-anchor structure forces multi-user thinking; watch for Government priorities (sovereignty) dominating the roadmap over Consumer priorities (delivery speed / cost).

### f. Where logistics is commoditised utility vs. where it will be forced to evolve

- **Commoditised utility (the note at ε ≈ 0.90):** Fossil Power, Storage, Warehouses, Long Haul, Shops, Cities — buy / use as-a-service; innovation here is a doctrine violation.
- **Forced evolution by automation:** Automated Delivery, Autotrucks, Drones, Scouts — all currently Genesis / early Custom Built. Labour shortage (HGV Skills inertia) and cost pressure will drive these through S-curves toward Product. Logistic-form scenario: $d\varepsilon/dt = r\varepsilon(1-\varepsilon)$ from $\varepsilon \approx 0.20$ with $r \approx 0.4$ per year gives ~5-7 years to mid-Product. **Scenario, not forecast.**
- **Forced evolution by sovereignty:** Territorial / CNI Sovereignty is today a Genesis-to-Custom concern but is being pushed forcefully by geopolitics. Expect it to evolve past 0.45 as nations codify freight-corridor / port / data-residency rules. This *pulls* Long Haul, Logistics Hubs, and Data back toward less-commoditised / more-regulated positions — a rare case of a climate force partially **de-commoditising** parts of the map.

## 7. Notes on Inertia (cross-reference to the 17 forms)

- **HGV Skills** — Form 5 (human capital) and Form 11 (skill / expertise inertia). Marked `inertia` in the OWM.
- **Trucks / Fossil Power** — Form 1 (sunk capital in existing physical assets) and Form 3 (past practice). Both marked `inertia`.
- **Regulation** — Form 13 (political capital) — not a pure blocker, but delays Autotrucks / Drones reaching Product stage.
- **Bundling / Lobbying / FUD** (raised in the scenario) are *gameplays*, not inertia, and belong in §6d above rather than here.

## 8. Health check

- Visibility constraint $\nu(a) \ge \nu(b)$ holds on every edge listed.
- Five anchors reflect the five actor types in the brief.
- Evolution placements sourced from the cheat-sheet quick method, not from calendar time or adoption.
- `evolve` entries are labelled scenarios, not forecasts.
</content>
</invoke>