# Urban Mobility Landscape — May 2022

## Strategic context

**Strategic question.** *Where should city authorities and mobility operators concentrate investment, regulatory effort, and platform-build vs. partner decisions across the urban-mobility stack, given that COVID-era habit shifts have partially settled, micromobility has scaled, ride-hail is post-IPO under profitability pressure, EV adoption is accelerating, and hybrid work has permanently altered commuter peaks?*

**User anchors (3).**
- **City Dweller** — discretionary urban trips (errands, leisure, social).
- **Commuter** — recurring trips to a hybrid workplace (2–3 days/week in office, not 5).
- **Municipality** — supply-side authority responsible for streets, transit, regulation, and emissions targets.

**Core needs.** Get across the city; commute to a hybrid workplace; reduce emissions & congestion; affordable, safe travel.

**Scope.** Urban mobility *landscape* — the full multi-stakeholder system in a typical western-European or North American city in May 2022. Not a single operator's product map. Density target ~45–55 nodes.

**Assumptions (flag for the user):**
1. "City" = mid-to-large western metropolis (London, Berlin, Toronto, San Francisco). Less applicable to dense Asian megacities (Tokyo/Seoul transit-dominant), or to car-dependent US sunbelt cities.
2. Hybrid-work assumption: roughly 2–3 days/week in-office for knowledge workers, lower & flatter peaks than 2019.
3. Demand-Responsive Transit is treated as Custom-Built (Stage II); a few US pilots are Stage III but the market is still early.

---

## The map

### OWM block

```
title Urban Mobility Landscape — May 2022
style wardley

// Anchors — three user types whose decisions shape the landscape
anchor City Dweller [0.96, 0.52]
anchor Commuter [0.96, 0.58]
anchor Municipality [0.96, 0.45]

// User-visible needs / outcomes
component Get Across The City [0.88, 0.62]
component Commute To Hybrid Workplace [0.88, 0.55]
component Reduce Emissions & Congestion [0.88, 0.42]
component Affordable Travel [0.83, 0.70]
component Safe Travel [0.82, 0.55]

// Decision drivers (mid-chain demand signals)
component Trip Planning App [0.74, 0.72]
component Real-Time Arrival Info [0.70, 0.78]
component Fare / Price Comparison [0.68, 0.74]
component Sustainability Signal [0.66, 0.40]
component Perceived Safety [0.65, 0.53]

// Modes consumed by users (the visible transport menu)
component Private Car [0.62, 0.86]
component Public Transit (Bus/Metro/Rail) [0.62, 0.78]
component Ride-Hail [0.60, 0.72]
component Taxi [0.58, 0.85] inertia
component Shared E-Scooter [0.58, 0.60]
component Shared E-Bike [0.57, 0.58]
component Personal Bicycle [0.56, 0.82]
component Walking [0.55, 0.95]
component Car-Share / Pool [0.54, 0.55]
component Demand-Responsive Transit [0.52, 0.38]

// Mobility-as-a-Service layer (aggregators)
component MaaS Aggregator App [0.50, 0.42]
component In-App Payment / Wallet [0.48, 0.78]
component Booking & Reservation [0.47, 0.68]
component Driver / Rider Matching [0.42, 0.62]

// Operator-side platforms
component Ride-Hail Platform (Uber/Lyft/Bolt) [0.44, 0.66]
component Micromobility Operator (Lime/Tier/Voi) [0.43, 0.55]
component Transit Operator (Public Authority) [0.42, 0.78]
component Fleet Management Software [0.38, 0.65]
component Dynamic Pricing Engine [0.39, 0.58]
component Driver / Gig Workforce [0.38, 0.55]

// Vehicles & physical assets
component Autonomous Vehicle Stack [0.34, 0.18]
component EV (Battery Electric Vehicle) [0.36, 0.48]
component ICE Vehicle [0.36, 0.88] inertia
component E-Scooter / E-Bike Hardware [0.34, 0.55]
component Vehicle Manufacturing [0.32, 0.72]
component Battery Cell [0.28, 0.55]
component Charging Hardware [0.18, 0.53]

// Enabling tech infrastructure
component GPS / GNSS [0.22, 0.92]
component Mobile Connectivity (4G/5G) [0.22, 0.90]
component Digital Mapping (OSM/Google Maps) [0.24, 0.78]
component Routing & ETA Engine [0.30, 0.66]
component IoT / Telematics [0.26, 0.62]

// Energy & charging
component Public Charging Network [0.20, 0.42]
component Electricity Grid [0.12, 0.90]
component Liquid Fuel Distribution [0.14, 0.95] inertia

// Physical infrastructure (municipality side)
component Roads & Streets [0.18, 0.96]
component Cycle Lanes & Parking [0.20, 0.55]
component Curb-Space Allocation [0.22, 0.38]
component Transit Right-of-Way [0.20, 0.80]

// Regulation & governance
component Micromobility Regulation [0.30, 0.42]
component Ride-Hail Regulation [0.32, 0.58]
component Low-Emission Zone Policy [0.30, 0.38]
component Driver Licensing & Safety Rules [0.28, 0.92]

// Cloud & data plumbing
component Cloud Utilities [0.08, 0.92]
component Payment Rails (Card / A2A) [0.04, 0.96]
component Mobility Data Standards (GTFS/MDS) [0.16, 0.58]

// User anchor edges
City Dweller->Get Across The City
City Dweller->Affordable Travel
City Dweller->Safe Travel
City Dweller->Sustainability Signal
Commuter->Commute To Hybrid Workplace
Commuter->Affordable Travel
Commuter->Safe Travel
Municipality->Reduce Emissions & Congestion
Municipality->Safe Travel

// Needs depend on planning + price + mode options
Get Across The City->Trip Planning App
Get Across The City->Public Transit (Bus/Metro/Rail)
Get Across The City->Ride-Hail
Get Across The City->Walking
Get Across The City->Shared E-Scooter
Commute To Hybrid Workplace->Public Transit (Bus/Metro/Rail)
Commute To Hybrid Workplace->Private Car
Commute To Hybrid Workplace->Personal Bicycle
Commute To Hybrid Workplace->Trip Planning App
Reduce Emissions & Congestion->Low-Emission Zone Policy
Reduce Emissions & Congestion->Public Transit (Bus/Metro/Rail)
Reduce Emissions & Congestion->Cycle Lanes & Parking
Reduce Emissions & Congestion->EV (Battery Electric Vehicle)
Reduce Emissions & Congestion->Micromobility Regulation
Affordable Travel->Fare / Price Comparison
Affordable Travel->Public Transit (Bus/Metro/Rail)
Affordable Travel->Shared E-Bike
Safe Travel->Perceived Safety
Safe Travel->Driver Licensing & Safety Rules

// Decision drivers depend on apps & data
Trip Planning App->Routing & ETA Engine
Trip Planning App->Real-Time Arrival Info
Trip Planning App->Digital Mapping (OSM/Google Maps)
Trip Planning App->Mobile Connectivity (4G/5G)
Real-Time Arrival Info->Mobility Data Standards (GTFS/MDS)
Real-Time Arrival Info->IoT / Telematics
Fare / Price Comparison->MaaS Aggregator App
Fare / Price Comparison->In-App Payment / Wallet
Sustainability Signal->Low-Emission Zone Policy
Sustainability Signal->EV (Battery Electric Vehicle)
Perceived Safety->Driver Licensing & Safety Rules
Perceived Safety->Cycle Lanes & Parking

// Modes depend on vehicles, operators, infrastructure
Private Car->ICE Vehicle
Private Car->EV (Battery Electric Vehicle)
Private Car->Roads & Streets
Private Car->Liquid Fuel Distribution
Public Transit (Bus/Metro/Rail)->Transit Operator (Public Authority)
Public Transit (Bus/Metro/Rail)->Transit Right-of-Way
Public Transit (Bus/Metro/Rail)->Mobility Data Standards (GTFS/MDS)
Ride-Hail->Ride-Hail Platform (Uber/Lyft/Bolt)
Ride-Hail->Driver / Gig Workforce
Ride-Hail->Booking & Reservation
Ride-Hail->Ride-Hail Regulation
Taxi->Driver / Gig Workforce
Taxi->Ride-Hail Regulation
Taxi->Roads & Streets
Shared E-Scooter->Micromobility Operator (Lime/Tier/Voi)
Shared E-Scooter->E-Scooter / E-Bike Hardware
Shared E-Scooter->Micromobility Regulation
Shared E-Scooter->Curb-Space Allocation
Shared E-Bike->Micromobility Operator (Lime/Tier/Voi)
Shared E-Bike->E-Scooter / E-Bike Hardware
Shared E-Bike->Cycle Lanes & Parking
Personal Bicycle->Cycle Lanes & Parking
Personal Bicycle->Roads & Streets
Walking->Roads & Streets
Car-Share / Pool->Fleet Management Software
Car-Share / Pool->Booking & Reservation
Car-Share / Pool->EV (Battery Electric Vehicle)
Demand-Responsive Transit->Transit Operator (Public Authority)
Demand-Responsive Transit->Routing & ETA Engine
Demand-Responsive Transit->Dynamic Pricing Engine

// MaaS layer depends on payments, matching, booking
MaaS Aggregator App->In-App Payment / Wallet
MaaS Aggregator App->Booking & Reservation
MaaS Aggregator App->Mobility Data Standards (GTFS/MDS)
MaaS Aggregator App->Driver / Rider Matching
In-App Payment / Wallet->Payment Rails (Card / A2A)
In-App Payment / Wallet->Cloud Utilities
Booking & Reservation->Cloud Utilities
Driver / Rider Matching->Routing & ETA Engine
Driver / Rider Matching->Cloud Utilities

// Operator platforms depend on plumbing
Ride-Hail Platform (Uber/Lyft/Bolt)->Autonomous Vehicle Stack
Ride-Hail Platform (Uber/Lyft/Bolt)->Dynamic Pricing Engine
Ride-Hail Platform (Uber/Lyft/Bolt)->Driver / Rider Matching
Ride-Hail Platform (Uber/Lyft/Bolt)->Fleet Management Software
Ride-Hail Platform (Uber/Lyft/Bolt)->Cloud Utilities
Micromobility Operator (Lime/Tier/Voi)->Fleet Management Software
Micromobility Operator (Lime/Tier/Voi)->IoT / Telematics
Micromobility Operator (Lime/Tier/Voi)->Public Charging Network
Transit Operator (Public Authority)->Transit Right-of-Way
Transit Operator (Public Authority)->Vehicle Manufacturing
Transit Operator (Public Authority)->Driver / Gig Workforce
Fleet Management Software->Cloud Utilities
Fleet Management Software->IoT / Telematics
Dynamic Pricing Engine->Cloud Utilities
Driver / Gig Workforce->Driver Licensing & Safety Rules

// Vehicles depend on manufacturing, batteries, charging
EV (Battery Electric Vehicle)->Vehicle Manufacturing
EV (Battery Electric Vehicle)->Battery Cell
EV (Battery Electric Vehicle)->Charging Hardware
EV (Battery Electric Vehicle)->Public Charging Network
ICE Vehicle->Vehicle Manufacturing
ICE Vehicle->Liquid Fuel Distribution
E-Scooter / E-Bike Hardware->Battery Cell
E-Scooter / E-Bike Hardware->Vehicle Manufacturing

// Charging depends on grid
Public Charging Network->Charging Hardware
Public Charging Network->Electricity Grid
Charging Hardware->Electricity Grid

// Tech infra
Routing & ETA Engine->Digital Mapping (OSM/Google Maps)
Routing & ETA Engine->GPS / GNSS
Routing & ETA Engine->Cloud Utilities
Digital Mapping (OSM/Google Maps)->Cloud Utilities
IoT / Telematics->Mobile Connectivity (4G/5G)
IoT / Telematics->GPS / GNSS

// Municipality side
Cycle Lanes & Parking->Roads & Streets
Curb-Space Allocation->Roads & Streets
Transit Right-of-Way->Roads & Streets
Low-Emission Zone Policy->Curb-Space Allocation
Micromobility Regulation->Curb-Space Allocation

// Evolution arrows — components moving right
evolve EV (Battery Electric Vehicle) 0.62
evolve MaaS Aggregator App 0.60
evolve Shared E-Scooter 0.72
evolve Mobility Data Standards (GTFS/MDS) 0.75
evolve Public Charging Network 0.62
evolve Demand-Responsive Transit 0.55

note Post-2018 micromobility scaled; many cities still finalising MDS / curb rules [0.42, 0.50]
note Ride-hail post-IPO: profitability pressure → dynamic pricing & driver-supply tension [0.46, 0.66]
note Hybrid work has flattened peak demand; permanent shift in commuter rhythms [0.90, 0.55]
```

**Validator status:** `OK: 59 components/anchors, 116 edges — no violations.`
**Layout status:** `LAYOUT OK: 3 anchors, 56 components — no layout warnings.`

---

### Component evolution rationale

| Component | Stage | ε | ν | Evidence |
|---|---|---|---:|---:|---|
| Get Across The City | Product (+rental) | 0.62 | 0.88 | User-facing outcome; behaviour & expectations highly standardised in 2022. |
| Commute To Hybrid Workplace | Product (+rental) | 0.55 | 0.88 | Hybrid-work routines are now common but the rhythm (split-week) is still settling — newer than pre-2020 commuting. |
| Reduce Emissions & Congestion | Custom Built | 0.42 | 0.88 | Climate-driven mandate is universal in spirit, but city-by-city interventions are still bespoke (varies London/Paris/Berlin). |
| Affordable Travel | Product (+rental) | 0.70 | 0.83 | Standard user need; fare structures and price-comparison expectations are mature. |
| Safe Travel | Product (+rental) | 0.55 | 0.82 | Mature need; Vision Zero and safety-design frameworks now common but uneven. |
| Trip Planning App | Product (+rental) | 0.72 | 0.74 | Citymapper, Google Maps, Apple Maps — multiple feature-competing products. |
| Real-Time Arrival Info | Product (+rental) | 0.78 | 0.70 | GTFS-realtime feeds widespread; ETA APIs are an expected feature. |
| Fare / Price Comparison | Product (+rental) | 0.74 | 0.68 | Common via aggregators (Google Maps shows prices across modes since 2020). |
| Sustainability Signal | Custom Built | 0.40 | 0.66 | Carbon/eco labels per trip are emerging (Google Maps eco-route 2021) but not standardised. |
| Perceived Safety | Product (+rental) | 0.53 | 0.65 | Established concept; women's-safety and night-trip features are still in product evolution. |
| Private Car | Commodity (+utility) | 0.86 | 0.62 | The dominant mode for decades; commoditised product market with utility-like dependence on roads & fuel. |
| Public Transit | Product (+rental) | 0.78 | 0.62 | Mature utility-like service in mature cities; some markets still industrialising. |
| Ride-Hail | Product (+rental) | 0.72 | 0.60 | Post-IPO (Uber 2019, Lyft 2019, Didi 2021) — multiple vendors, feature competition, regulated, profitability under pressure. |
| Taxi | Commodity (+utility) | 0.85 | 0.58 | Century-old service, regulated everywhere; flagged inertia — under structural decline. |
| Shared E-Scooter | Product (+rental) | 0.60 | 0.58 | Scaled hugely 2018–2022 (Lime, Bird, Tier, Voi, Dott); multi-vendor competition with shakeout underway. |
| Shared E-Bike | Product (+rental) | 0.58 | 0.57 | Similar dynamics; Lyft Citibike, Lime, Tier; growing but slightly behind scooters. |
| Personal Bicycle | Commodity (+utility) | 0.82 | 0.56 | Mature consumer goods; e-bike variant still industrialising. |
| Walking | Commodity (+utility) | 0.95 | 0.55 | The original mode; pure utility, just needs streets. |
| Car-Share / Pool | Product (+rental) | 0.55 | 0.54 | Zipcar (now 22 yrs old), Share Now, Free2Move — mature operators but market still evolving. |
| Demand-Responsive Transit | Custom Built | 0.38 | 0.52 | Via Transportation, ArrivaClick — early pilots; bespoke per agency; no dominant vendor. |
| MaaS Aggregator App | Custom Built | 0.42 | 0.50 | Whim (Helsinki), Jelbi (Berlin), Free Now — each is bespoke, no dominant standard model. |
| In-App Payment / Wallet | Product (+rental) | 0.78 | 0.48 | Apple Pay, Google Pay, Stripe Checkout — well-productised, near commodity. |
| Booking & Reservation | Product (+rental) | 0.68 | 0.47 | Well-understood pattern; multiple SDKs and platforms. |
| Driver / Rider Matching | Product (+rental) | 0.62 | 0.42 | Uber's original IP, now widely replicated; available as a service (RideOS, HERE). |
| Ride-Hail Platform | Product (+rental) | 0.66 | 0.44 | Uber/Lyft/Bolt/Didi/Grab — mature product category. |
| Micromobility Operator | Product (+rental) | 0.55 | 0.43 | Multi-vendor (Lime, Tier, Voi, Bird, Dott); operating model still evolving. |
| Transit Operator | Product (+rental) | 0.78 | 0.42 | Public authorities operate as mature service providers; very few cities innovate the operational model. |
| Fleet Management Software | Product (+rental) | 0.65 | 0.38 | Geotab, Samsara, Verizon Connect — multiple competing products. |
| Dynamic Pricing Engine | Product (+rental) | 0.58 | 0.39 | Surge pricing pioneered by Uber, now widely productised (Sift, Yieldify, in-platform). |
| Driver / Gig Workforce | Product (+rental) | 0.55 | 0.38 | Mature labour pool with platform-specific terms; legal classification still in flux (AB5, EU PWD). |
| Autonomous Vehicle Stack | Genesis | 0.18 | 0.34 | Waymo, Cruise — limited geofenced pilots in 2022 (SF, Phoenix); no commercial generalisation; literature still describing the wonder. |
| EV (Battery Electric Vehicle) | Custom Built | 0.48 | 0.36 | Multiple OEMs (Tesla, VW, Hyundai, BYD, Stellantis), but production still constrained, ~10% of new-car sales globally, supply chains immature. |
| ICE Vehicle | Commodity (+utility) | 0.88 | 0.36 | Century-old commodity; flagged inertia — declining but vast installed base. |
| E-Scooter / E-Bike Hardware | Product (+rental) | 0.55 | 0.34 | Multiple Asian OEMs (Segway-Ninebot, Okai); component-level commoditising. |
| Vehicle Manufacturing | Product (+rental) | 0.72 | 0.32 | Highly industrialised but vast scale; not a true utility. |
| Battery Cell | Product (+rental) | 0.55 | 0.28 | CATL, LG, Samsung SDI, Panasonic — multi-vendor product market; supply-constrained; gigafactory investments accelerating. |
| Charging Hardware | Product (+rental) | 0.53 | 0.18 | ChargePoint, ABB, EVBox, Tesla Supercharger — competing products, standards (CCS vs NACS) still fluid in May 2022. |
| GPS / GNSS | Commodity (+utility) | 0.92 | 0.22 | Global utility; multiple constellations (GPS, Galileo, GLONASS, BeiDou). |
| Mobile Connectivity (4G/5G) | Commodity (+utility) | 0.90 | 0.22 | Standardised utility; 5G rollout still industrialising in 2022 but 4G fully commodity. |
| Digital Mapping | Product (+rental) | 0.78 | 0.24 | Google Maps, Apple Maps, HERE, OSM — mature multi-vendor. |
| Routing & ETA Engine | Product (+rental) | 0.66 | 0.30 | Mapbox, Google Directions API, OSRM, Valhalla — productised. |
| IoT / Telematics | Product (+rental) | 0.62 | 0.26 | Particle, Geotab, Samsara — mature product/service market. |
| Public Charging Network | Custom Built | 0.42 | 0.20 | Patchy coverage in May 2022; geographic gaps; rapid build-out underway (NEVI in US, Fit for 55 in EU). |
| Electricity Grid | Commodity (+utility) | 0.90 | 0.12 | National utility; well over a century old. |
| Liquid Fuel Distribution | Commodity (+utility) | 0.95 | 0.14 | Universal commodity; flagged inertia — declining demand horizon. |
| Roads & Streets | Commodity (+utility) | 0.96 | 0.18 | Public-goods utility; centuries old. |
| Cycle Lanes & Parking | Product (+rental) | 0.55 | 0.20 | Rapidly industrialising post-2020; city-by-city pop-up infrastructure became permanent. |
| Curb-Space Allocation | Custom Built | 0.38 | 0.22 | Coordinated Mobility Data Specification (MDS) curb-management efforts emerging; mostly bespoke per city. |
| Transit Right-of-Way | Commodity (+utility) | 0.80 | 0.20 | Established municipal asset class. |
| Micromobility Regulation | Custom Built | 0.42 | 0.30 | Each city writes its own rules in 2022 (caps, geofences, helmet laws); some convergence but no standard. |
| Ride-Hail Regulation | Product (+rental) | 0.58 | 0.32 | Multi-decade regulatory patterns established post-2014; AB5, EU Platform Work Directive in flight. |
| Low-Emission Zone Policy | Custom Built | 0.38 | 0.30 | London ULEZ, Paris ZFE, German Umweltzonen — each implementation bespoke. |
| Driver Licensing & Safety Rules | Commodity (+utility) | 0.92 | 0.28 | Century-old regulatory commodity. |
| Cloud Utilities | Commodity (+utility) | 0.92 | 0.08 | AWS / GCP / Azure — utility billing, full commodity. |
| Payment Rails | Commodity (+utility) | 0.96 | 0.04 | Visa/Mastercard/SEPA/A2A — full utility. |
| Mobility Data Standards (GTFS/MDS) | Product (+rental) | 0.58 | 0.16 | GTFS is mature (Google-originated, now Open Mobility Foundation); MDS is industrialising in 2022 with active OMF working groups. |

---

## Strategic analysis

### a. Differentiation opportunities (top 3)

1. **Autonomous Vehicle Stack (Genesis)** — only true Genesis component in the landscape. Whoever cracks robotaxi unit-economics in a major metro before 2026 captures a generational moat. In May 2022 Waymo and Cruise have geofenced pilots; no operator-grade deployment yet. The differentiation pressure is the highest in the map.
2. **Demand-Responsive Transit (Custom Built)** — re-imagines low-density transit using fleet-optimisation. Visible to commuters; immature operator landscape; few cities have integrated it with public-transit fares. Real differentiation play for a transit authority that can partner with Via, Spare, or build in-house.
3. **MaaS Aggregator App (Custom Built)** — Whim/Jelbi-style apps haven't found product-market fit in 2022. A municipality or transit authority that ships a usable, multi-mode, single-ticket experience first wins the user relationship and pulls operators into a downstream commodity position.

### b. Commodity-leverage candidates (top 3)

1. **Cloud Utilities (Commodity +utility)** — rent. No mobility operator should be running its own datacentre in 2022.
2. **Payment Rails (Commodity +utility)** — use Stripe/Adyen/Mollie. Don't build PSP capability.
3. **Routing & ETA Engine (Product +rental)** — most operators should consume Mapbox/Google/HERE rather than build. Reserved for the largest platforms whose volume justifies in-house (Uber's marketplace already does this).

### c. Dependency risks (top 3)

1. **Trip Planning App → Real-Time Arrival Info → Mobility Data Standards (GTFS/MDS)** — the visible commuter experience hinges on a Custom-Built-edge-of-Product standard (MDS) that many cities have not adopted. If MDS adoption stalls, multimodal aggregation also stalls.
2. **Ride-Hail → Driver / Gig Workforce → Driver Licensing & Safety Rules** — visible mode depends on a workforce whose legal status is genuinely in flux in May 2022 (California AB5 fallout; EU Platform Work Directive draft late 2021). One ruling could reprice the whole product.
3. **Reduce Emissions & Congestion → EV (Battery Electric Vehicle) → Battery Cell + Public Charging Network** — the municipal climate goal depends on an industrialising vehicle category that itself depends on a supply-constrained battery market and a patchy charging network. Fragile foundation under a high-visibility outcome.

### d. Build / Buy / Outsource recommendations

| Component | Stage | Recommendation | Why |
|---|---|---|---|
| Autonomous Vehicle Stack | Genesis | **Build (well-funded) or stay out** | No vendor market; only viable for tier-1 capital like Alphabet, GM, or established OEMs. |
| MaaS Aggregator App | Custom Built | **Build (public sector) / Open-source collaborate** | Cities should build (or jointly fund) the user-facing aggregator rather than concede the relationship to a private platform. |
| Demand-Responsive Transit | Custom Built | **Buy external expertise** (Via, Spare) | Patterns are emerging; vendors exist but the integration is still bespoke. |
| EV (Battery Electric Vehicle) | Custom Built → Product | **Buy** | Fleet operators should procure, not co-develop, except for very large fleets (Amazon-Rivian model). |
| Public Charging Network | Custom Built | **Public-private partnership** | Capital-intensive infrastructure; partnerships are how this scales (NEVI in US, AFIR in EU). |
| Cycle Lanes & Parking | Product (+rental) | **Build (municipal)** | Public infrastructure — municipalities have built before, vendors are surveyors/contractors not platform builders. |
| Mobility Data Standards (GTFS/MDS) | Product (+rental) | **Open-source collaborate** | Open Mobility Foundation already exists; municipalities should join, not fork. |
| Ride-Hail Platform | Product (+rental) | **Use existing** | Multi-vendor competitive market; no city or new operator should build a clone in 2022. |
| Fleet Management Software | Product (+rental) | **Buy** | Mature product market (Geotab, Samsara). |
| Driver / Rider Matching | Product (+rental) | **Buy** (RideOS, HERE) | Replicable; build only if you're top-5 by volume. |
| Cloud Utilities | Commodity (+utility) | **Rent** | AWS/GCP/Azure; do not run your own. |
| Payment Rails | Commodity (+utility) | **Rent** (Stripe / Adyen / Mollie) | Utility. |
| Digital Mapping | Product (+rental) | **Buy** / use OSM for cost-sensitive cases | Mapbox / Google / HERE for SLA; OSM for budget. |

### e. Suggested gameplays (from Wardley's 61-play catalogue)

- **#1 Sensible expansion / land-grab on micromobility** — micromobility is mid-Product and consolidating; remaining operators should consolidate aggressively before margins compress further.
- **#15 Open Approaches** on **Mobility Data Standards (GTFS/MDS)** — accelerate the Product→Commodity transition that benefits aggregators and cities equally.
- **#26 Standards Game** on **Charging Hardware** (CCS, NACS, MCS) — whichever connector wins controls the rails for a decade.
- **#41 Embrace and Extend** on **MaaS** — cities should embrace open mobility data standards then extend with municipal branding & integrated fares so private aggregators don't capture the user.
- **#33 Pricing Policy / Yield management** on **Ride-Hail Platform** — post-IPO platforms are doing this aggressively (dynamic pricing, driver-supply signals) to find profitability.
- **#10 Tower and Moat** on **Autonomous Vehicle Stack** — Waymo / Cruise / Tesla are each trying to build a deep proprietary stack with a regulatory moat (operating permits per metro).
- **#7 Use of FUD (gameplay, not inertia)** against **Shared E-Scooter** by **Taxi** lobbies — well-documented in 2018–2022 cities (Paris referendum in 2023 is the punctuation point).
- **#22 Misdirection / Confusion of choice** — risk for cities: micromobility operator proliferation creates user fatigue; municipalities should consolidate to 2–3 operators per city via permit caps.

### f. Doctrine violations

- **Doctrine #1 ("Focus on user needs")** — many municipal mobility strategies in 2022 still anchor on the *mode* (more buses, more bike lanes) rather than the *trip outcome* (door-to-door reliability). The map is built around the trip outcomes to model this correctly.
- **Doctrine #18 ("Distribute power & decision-making")** — curb-space allocation is centralised in most cities and creates a bottleneck for micromobility, deliveries, accessible vehicles. Devolving to district level is a clear doctrine alignment.
- **Doctrine #23 ("Have a systematic mechanism of learning")** — most cities lack standardised mobility-data exchange with operators; MDS adoption is the lever.
- **Doctrine #30 ("Use appropriate methods for each stage")** — observed in the wild: cities and operators routinely apply Stage-III metric-driven management to Stage-II/Genesis components (Demand-Responsive Transit, Autonomous Vehicle Stack), starving learning loops.

### g. Climatic context (which of the 27 patterns are actively shaping this map)

- **#3 Everything evolves** — micromobility, ride-hail, EV, MaaS are visibly mid-evolution; no part of the map is static.
- **#15–17 Inertia (multiple forms)** — Taxi (Past success success, sunk-cost), ICE Vehicle (Past success, supplier inertia), Liquid Fuel Distribution (supplier asset-base inertia). Marked with `inertia` in the OWM.
- **#27 Product-to-utility punctuated equilibrium** — Charging Hardware, Battery Cell, EV are entering this transition. Expect dramatic price drops and shakeout 2024–2028.
- **#23 Co-evolution of practice with activity** — agile / cellular / spatial fleet ops co-evolving with on-demand mobility platforms.
- **#26 Componentisation enables higher-order systems** — productised routing, payments, and matching make MaaS aggregation cheap to assemble; this is why MaaS is feasible in 2022 in a way it wasn't in 2012.
- **#18 You cannot measure evolution over time or adoption** — explicitly: micromobility is only 4 years old but already mid-Product; EV is 100+ years old but only just exiting Custom-Built for cars.
- **COVID shock (climate event, not a pattern strictly)** — durable changes in commuter peaks, walk/cycle preference, and last-mile delivery demand.

### h. Deep-placement notes

Five components received deep-placement analysis beyond the cheat-sheet pass:

1. **Autonomous Vehicle Stack** — initial cheat-sheet leaned Stage II (some commercial activity from Waymo, Cruise). After review: in May 2022 these are *geofenced research deployments*, not commercial service in a generalised sense; literature is still "describing the wonder", failure modes are "betting on the wrong approach" — Stage I confirmed at ε=0.18.

2. **EV (Battery Electric Vehicle)** — initial cheat-sheet split between Stage II and Stage III. Vendor count in May 2022 is large (Tesla, VW, Hyundai-Kia, BYD, Stellantis, GM, Ford) but per-OEM EV volumes are still <20% of car output; supply chains are constrained; profitability uneven. Settled on **late Stage II** at ε=0.48, just below the Product boundary, with an `evolve` arrow to 0.62.

3. **Mobility Data Standards (GTFS/MDS)** — initial reading would put data standards at Commodity. But MDS specifically is only ~5 years old in 2022 (created 2018 by LADOT) and adoption is uneven. Combined with mature GTFS, the bundle sits at ε=0.58 (Product, industrialising) — much earlier than `Cloud Utilities` or `Payment Rails`.

4. **Shared E-Scooter / Micromobility Operator** — vendor concentration check: Lime, Bird, Tier, Voi, Dott, Spin, Helbiz, plus Asian players. That's mid-Product with a shakeout underway, not Stage IV. Confirmed at ε=0.60.

5. **Demand-Responsive Transit** — Via, Spare, ArrivaClick, Padam, ViaVan exist as vendors but municipal deployments are bespoke and pilot-scale. Cheat-sheet flagged transition. Settled **Stage II** at ε=0.38 with an `evolve` arrow to 0.55 (the multiple-vendor signal pulls it close to Stage III).

### i. Caveat

Evolution trajectories on this map are scenarios, not forecasts. Wardley's climatic pattern #18: *"you cannot measure evolution over time or adoption."* The `evolve` arrows represent directional pressure given the May 2022 climate (post-IPO ride-hail pricing pressure, post-2018 micromobility scale, accelerating EV mandates, hybrid-work commuter shift) — not a calendar prediction. Re-score in 12 months.

---

### Mermaid render (for GitHub viewing)

```mermaid
wardley-beta
    title Urban Mobility Landscape — May 2022
    anchor "City Dweller": [0.52, 0.96]
    anchor "Commuter": [0.58, 0.96]
    anchor "Municipality": [0.45, 0.96]
    component "Get Across The City": [0.62, 0.88]
    component "Commute To Hybrid Workplace": [0.55, 0.88]
    component "Reduce Emissions & Congestion": [0.42, 0.88]
    component "Affordable Travel": [0.70, 0.83]
    component "Safe Travel": [0.55, 0.82]
    component "Trip Planning App": [0.72, 0.74]
    component "Real-Time Arrival Info": [0.78, 0.70]
    component "Fare / Price Comparison": [0.74, 0.68]
    component "Sustainability Signal": [0.40, 0.66]
    component "Perceived Safety": [0.53, 0.65]
    component "Private Car": [0.86, 0.62]
    component "Public Transit (Bus/Metro/Rail)": [0.78, 0.62]
    component "Ride-Hail": [0.72, 0.60]
    component "Taxi": [0.85, 0.58]
    component "Shared E-Scooter": [0.60, 0.58]
    component "Shared E-Bike": [0.58, 0.57]
    component "Personal Bicycle": [0.82, 0.56]
    component "Walking": [0.95, 0.55]
    component "Car-Share / Pool": [0.55, 0.54]
    component "Demand-Responsive Transit": [0.38, 0.52]
    component "MaaS Aggregator App": [0.42, 0.50]
    component "In-App Payment / Wallet": [0.78, 0.48]
    component "Booking & Reservation": [0.68, 0.47]
    component "Driver / Rider Matching": [0.62, 0.42]
    component "Ride-Hail Platform (Uber/Lyft/Bolt)": [0.66, 0.44]
    component "Micromobility Operator (Lime/Tier/Voi)": [0.55, 0.43]
    component "Transit Operator (Public Authority)": [0.78, 0.42]
    component "Fleet Management Software": [0.65, 0.38]
    component "Dynamic Pricing Engine": [0.58, 0.39]
    component "Driver / Gig Workforce": [0.55, 0.38]
    component "Autonomous Vehicle Stack": [0.18, 0.34]
    component "EV (Battery Electric Vehicle)": [0.48, 0.36]
    component "ICE Vehicle": [0.88, 0.36]
    component "E-Scooter / E-Bike Hardware": [0.55, 0.34]
    component "Vehicle Manufacturing": [0.72, 0.32]
    component "Battery Cell": [0.55, 0.28]
    component "Charging Hardware": [0.53, 0.18]
    component "GPS / GNSS": [0.92, 0.22]
    component "Mobile Connectivity (4G/5G)": [0.90, 0.22]
    component "Digital Mapping (OSM/Google Maps)": [0.78, 0.24]
    component "Routing & ETA Engine": [0.66, 0.30]
    component "IoT / Telematics": [0.62, 0.26]
    component "Public Charging Network": [0.42, 0.20]
    component "Electricity Grid": [0.90, 0.12]
    component "Liquid Fuel Distribution": [0.95, 0.14]
    component "Roads & Streets": [0.96, 0.18]
    component "Cycle Lanes & Parking": [0.55, 0.20]
    component "Curb-Space Allocation": [0.38, 0.22]
    component "Transit Right-of-Way": [0.80, 0.20]
    component "Micromobility Regulation": [0.42, 0.30]
    component "Ride-Hail Regulation": [0.58, 0.32]
    component "Low-Emission Zone Policy": [0.38, 0.30]
    component "Driver Licensing & Safety Rules": [0.92, 0.28]
    component "Cloud Utilities": [0.92, 0.08]
    component "Payment Rails (Card / A2A)": [0.96, 0.04]
    component "Mobility Data Standards (GTFS/MDS)": [0.58, 0.16]
```

(Authoritative coordinates are in the OWM block above; this Mermaid is a rendering target.)
