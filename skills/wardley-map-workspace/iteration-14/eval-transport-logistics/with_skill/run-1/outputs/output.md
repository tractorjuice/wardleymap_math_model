# Wardley Map: Modern Logistics Landscape

**Scenario:** Map the landscape of modern logistics (freight and parcel across road, rail, sea, air). Include demand signals, carrier networks, warehousing, last-mile, tracking, customs, regulation, and digital platforms. What's differentiating vs. commoditising, and where is the chain fragile?

This is a multi-stakeholder industry-landscape map, so the density target is ~40-55 components. The final map has 2 anchors + 49 components + 84 dependency edges, validated clean against the visibility rule.

---

## Map

```owm
title Modern Logistics Landscape
style wardley

// Anchors (two user types: the party paying to ship and the party receiving)
anchor Shipper [0.98, 0.60]
anchor Consignee [0.96, 0.65]

// User-facing outcomes and interactions
component Parcel / Freight Delivery [0.90, 0.70]
component Shipment Tracking UX [0.88, 0.75]
component Booking & Rate Quoting [0.86, 0.55]
component Proof of Delivery [0.84, 0.78]
component Returns Handling [0.80, 0.55]
component Customer Service / Claims [0.78, 0.60]

// Demand signals and orchestration layer
component E-commerce Demand Signals [0.68, 0.65]
component Shipper TMS [0.70, 0.60]
component Digital Freight Marketplaces [0.65, 0.35]
component Freight Forwarder Orchestration [0.66, 0.55]
component API / EDI Integration [0.54, 0.75]

// Carrier networks (mode choice happens here)
component Last-Mile Delivery [0.72, 0.55]
component Parcel Carrier Network [0.64, 0.80]
component Road Freight Carrier [0.58, 0.78]
component Air Freight Carrier [0.50, 0.72]
component Ocean Freight Carrier [0.48, 0.82]
component Rail Freight Carrier [0.44, 0.80]
component Gig Courier Network [0.60, 0.50]

// Physical nodes
component Urban Pickup Points / Lockers [0.55, 0.55]
component Sorting / Parcel Hub [0.45, 0.78]
component Warehousing & Fulfilment [0.52, 0.65]
component Cross-Dock Terminal [0.40, 0.70]
component Cargo Airport [0.32, 0.85]
component Seaport / Container Terminal [0.30, 0.85]
component Rail Intermodal Yard [0.28, 0.82]

// Tracking, data, visibility
component Real-Time Visibility Platform [0.56, 0.45]
component GPS / Telematics [0.30, 0.85]
component IoT Cold-Chain Sensors [0.34, 0.40]
component Scan Events / Barcode [0.50, 0.92]
component Route Optimisation [0.34, 0.55]
component Load Planning & Consolidation [0.36, 0.50]

// Customs and trade
component Customs Clearance [0.46, 0.70]
component Customs Brokerage [0.38, 0.65]
component HS Code Classification [0.30, 0.55]
component Trade Compliance / Sanctions Screening [0.32, 0.60]
component Single-Window Customs Filing [0.26, 0.45]

// Regulation and standards
component Transport Regulation & Safety [0.22, 0.65]
component Emissions Regulation [0.20, 0.35]

// Labour (knowledge-heavy)
component HGV / Van Drivers [0.35, 0.60]
component Warehouse Labour [0.30, 0.55]
component Warehouse Automation / Robotics [0.25, 0.30]

// Physical assets
component Truck / Van Fleet [0.20, 0.85]
component Containers (ISO) [0.16, 0.95]
component Shipping Lanes / Air Corridors / Roads [0.08, 0.95]

// Utilities and commodity inputs
component Cargo Insurance [0.24, 0.80]
component Payment Rails [0.22, 0.92]
component Fuel (Diesel / Bunker / Jet) [0.12, 0.93]
component Electricity / Power Grid [0.06, 0.96]
component Cloud Compute & Storage [0.10, 0.92]

// Dependencies -- user-facing
Shipper->Booking & Rate Quoting
Shipper->Shipment Tracking UX
Shipper->Parcel / Freight Delivery
Shipper->Customer Service / Claims
Shipper->Returns Handling
Consignee->Parcel / Freight Delivery
Consignee->Shipment Tracking UX
Consignee->Proof of Delivery
Consignee->Returns Handling
Consignee->Customer Service / Claims

// Booking & demand -> orchestration
Booking & Rate Quoting->Digital Freight Marketplaces
Booking & Rate Quoting->Shipper TMS
Booking & Rate Quoting->Freight Forwarder Orchestration
Shipper TMS->API / EDI Integration
Shipper TMS->E-commerce Demand Signals
Digital Freight Marketplaces->API / EDI Integration
Freight Forwarder Orchestration->API / EDI Integration
E-commerce Demand Signals->API / EDI Integration

// Delivery -> carriers
Parcel / Freight Delivery->Last-Mile Delivery
Parcel / Freight Delivery->Parcel Carrier Network
Parcel / Freight Delivery->Road Freight Carrier
Parcel / Freight Delivery->Air Freight Carrier
Parcel / Freight Delivery->Ocean Freight Carrier
Parcel / Freight Delivery->Rail Freight Carrier

// Last-mile composition
Last-Mile Delivery->Gig Courier Network
Last-Mile Delivery->Urban Pickup Points / Lockers
Last-Mile Delivery->Parcel Carrier Network
Last-Mile Delivery->Route Optimisation

// Orchestrators allocate across carriers
Freight Forwarder Orchestration->Road Freight Carrier
Freight Forwarder Orchestration->Air Freight Carrier
Freight Forwarder Orchestration->Ocean Freight Carrier
Freight Forwarder Orchestration->Rail Freight Carrier
Freight Forwarder Orchestration->Customs Clearance
Digital Freight Marketplaces->Road Freight Carrier

// Carriers -> physical nodes
Parcel Carrier Network->Sorting / Parcel Hub
Road Freight Carrier->Cross-Dock Terminal
Road Freight Carrier->Truck / Van Fleet
Rail Freight Carrier->Rail Intermodal Yard
Ocean Freight Carrier->Seaport / Container Terminal
Ocean Freight Carrier->Containers (ISO)
Air Freight Carrier->Cargo Airport

// Warehousing feeds multiple carriers
Warehousing & Fulfilment->Warehouse Labour
Warehousing & Fulfilment->Warehouse Automation / Robotics
Warehousing & Fulfilment->Load Planning & Consolidation
Parcel Carrier Network->Warehousing & Fulfilment

// Tracking dependencies
Shipment Tracking UX->Real-Time Visibility Platform
Real-Time Visibility Platform->GPS / Telematics
Real-Time Visibility Platform->Scan Events / Barcode
Real-Time Visibility Platform->IoT Cold-Chain Sensors
Real-Time Visibility Platform->API / EDI Integration
Proof of Delivery->Scan Events / Barcode

// Route / load optimisation
Route Optimisation->GPS / Telematics
Load Planning & Consolidation->Route Optimisation

// Customs chain
Customs Clearance->Customs Brokerage
Customs Clearance->HS Code Classification
Customs Clearance->Trade Compliance / Sanctions Screening
Customs Clearance->Single-Window Customs Filing
Ocean Freight Carrier->Customs Clearance
Air Freight Carrier->Customs Clearance

// Drivers / labour
Road Freight Carrier->HGV / Van Drivers
Last-Mile Delivery->HGV / Van Drivers
Gig Courier Network->HGV / Van Drivers

// Regulation
Road Freight Carrier->Transport Regulation & Safety
Air Freight Carrier->Transport Regulation & Safety
Ocean Freight Carrier->Emissions Regulation
Road Freight Carrier->Emissions Regulation

// Assets
Truck / Van Fleet->Fuel (Diesel / Bunker / Jet)
Rail Freight Carrier->Fuel (Diesel / Bunker / Jet)
Ocean Freight Carrier->Fuel (Diesel / Bunker / Jet)
Air Freight Carrier->Fuel (Diesel / Bunker / Jet)
Truck / Van Fleet->Shipping Lanes / Air Corridors / Roads
Rail Freight Carrier->Shipping Lanes / Air Corridors / Roads
Ocean Freight Carrier->Shipping Lanes / Air Corridors / Roads
Air Freight Carrier->Shipping Lanes / Air Corridors / Roads

// Utilities
Warehousing & Fulfilment->Electricity / Power Grid
Sorting / Parcel Hub->Electricity / Power Grid
Seaport / Container Terminal->Electricity / Power Grid
API / EDI Integration->Cloud Compute & Storage
Real-Time Visibility Platform->Cloud Compute & Storage
Shipper TMS->Cloud Compute & Storage
Digital Freight Marketplaces->Cloud Compute & Storage

// Payments & insurance
Booking & Rate Quoting->Payment Rails
Parcel / Freight Delivery->Cargo Insurance
Customer Service / Claims->Cargo Insurance

// Evolution arrows
evolve Digital Freight Marketplaces 0.60
evolve Real-Time Visibility Platform 0.70
evolve Route Optimisation 0.70
evolve IoT Cold-Chain Sensors 0.65
evolve Warehouse Automation / Robotics 0.55
evolve Single-Window Customs Filing 0.70
evolve Emissions Regulation 0.60

// Notes
note Differentiation zone [0.65, 0.30]
note Commodity utilities [0.10, 0.92]
```

**Validator:** `OK: 51 components/anchors, 84 edges — no violations.`

---

## Strategic analysis

### a. Differentiation opportunities (top 3)

1. **Real-Time Visibility Platform** (Custom Built → Product (+rental)) — the user-visible UX advantage of "where is my shipment, ETA-accurate, proactive exception alerts" is still being built. This is the single biggest lever for premium pricing in B2B freight today: project44, FourKites and Shippeo have shown shippers will pay for it. Highest differentiation leverage because it sits high in the value chain (ν = 0.56) on top of commoditising inputs.
2. **Digital Freight Marketplaces** (Custom Built) — Convoy collapsed, Uber Freight has struggled, Flexport has pivoted repeatedly. The category is still uncharted, volatile, and the algorithmic moat (matching loads to trucks with empty-mile optimisation) has not yet been won. High D because ε is low and ν is high (users are actively choosing between platforms).
3. **Route Optimisation & Load Planning** (Custom Built) — while open-source and vendor products exist, real-time dynamic optimisation with live traffic, ELD hours-of-service constraints, multi-drop parcel stops, and cold-chain windows is still where Amazon Logistics and the Chinese cross-border players differentiate. This is mid-chain (ν = 0.34) but wins translate directly into unit-economics advantage that competitors can't replicate quickly.

Honourable mentions: **Warehouse Automation / Robotics** (Genesis → Custom) is a harder, capex-heavy differentiator that works at scale (Amazon, Ocado, Symbotic). **IoT Cold-Chain Sensors** matter only in cold-chain / pharma segments but are a step-function differentiator there.

### b. Commodity-leverage candidates (top 3)

1. **Cloud Compute & Storage** (Commodity (+utility)) — rent from hyperscalers; never operate your own data-centre infra for a logistics platform.
2. **Payment Rails** (Commodity (+utility)) — Stripe / Adyen / banks; do not build.
3. **Fuel (Diesel / Bunker / Jet)** (Commodity (+utility)) — hedge, don't "produce". Also **Electricity / Power Grid**, **Containers (ISO)**, and **Scan Events / Barcode** (a decades-old commodity standard — GS1). The road freight Carrier itself is also highly commoditised in most geographies, which is precisely why the marketplace and orchestration layers are where the IP sits.

### c. Dependency risks (top 3)

Edges where a user-visible component rides on a fragile or under-industrialised foundation:

1. **Shipment Tracking UX → Real-Time Visibility Platform → API / EDI Integration** — the consumer/shipper tracking experience ultimately depends on hundreds of carrier integrations; EDI is decades-old, formats vary per carrier, and data quality is notoriously patchy. The visibility is only as good as the weakest carrier API. This is the single most fragile chain in the landscape.
2. **Last-Mile Delivery → Gig Courier Network → HGV / Van Drivers** — the user-facing delivery step depends on a Custom-Built labour-model (gig) resting on a labour pool with acute shortage (HGV/van drivers in EU/UK/US). Any regulatory reclassification (AB5, EU Platform-Workers Directive) recalibrates unit economics overnight.
3. **Freight Forwarder Orchestration → Customs Clearance → Customs Brokerage** — cross-border freight hinges on customs, which is only partially industrialised (Single-Window Customs Filing is still Custom Built). Trade-policy shocks (tariffs, sanctions, Brexit, Red-Sea re-routing) hit this edge first. Sanctions screening in particular is a compliance liability that the forwarder carries.

Others worth naming: **Ocean Freight Carrier → Seaport / Container Terminal** is a choke-point risk (Suez closures, port strikes, dock-worker contracts); **Road Freight Carrier → HGV / Van Drivers** is the driver-shortage risk; all carriers → **Fuel** is a commodity-price exposure; all carriers → **Shipping Lanes / Air Corridors / Roads** is geopolitical and climate-disruption risk.

### d. Suggested gameplays

- **#45 Two Factor Market** on Digital Freight Marketplaces — carrier side and shipper side must be co-built; single-sided liquidity collapses (Convoy 2023 lesson).
- **#16 Exploiting Network Effects** on Real-Time Visibility Platform — each carrier integration adds value to every shipper; deliberate land-grab of the integration surface.
- **#36 Directed Investment** on Real-Time Visibility + Route Optimisation + Warehouse Automation — the three highest-D components; starve everything else before starving these.
- **#15 Open Approaches (open-source / open API)** on API / EDI Integration — do not own the integration standard; accelerate its commoditisation so the value moves up into visibility UX and analytics. This is Shopify/Uber's playbook.
- **#29 Harvesting** on carrier and gig-driver layers — let the commoditised carrier market race to the bottom; harvest capacity through the orchestration layer.
- **#41 Alliances (co-operation)** on Customs Single-Window, Emissions Regulation — industry consortia to co-author the standard, not resist it.
- **#56 First Mover** on Emissions Regulation (CBAM, CORSIA, FuelEU Maritime) — regulatory deadlines create a narrow window where being early on carbon accounting and green-fuel transitions is a durable position.
- **#43 Sensing Engines (ILC)** on the marketplace data — every load matched is a market-price data point; use it to enter adjacent markets (insurance, factoring, fuel hedging).
- **#26 Differentiation** on verticalised last-mile (cold chain, healthcare, white-glove) — where commoditised parcel networks can't follow.

### e. Doctrine notes

- **#1 Focus on user needs** (Phase I): satisfied — the map is anchored on Shipper and Consignee with clearly distinct user-visible chains.
- **#10 Know your users** (Phase I): satisfied — two anchors correctly represent the two sides of the logistics transaction; lumping them would hide the fact that tracking and returns are consignee-dominant needs while booking and rate quoting are shipper-dominant.
- **#13 Manage inertia** (Phase II): flagged. Incumbent freight forwarders and asset-heavy carriers carry at least four inertia forms: sunk-capital on fleets and terminals (#2), skill-acquisition costs in driver and customs workforces (#8), re-architecture costs moving from EDI to API (#9), and strategic-control loss worries when shippers demand open data (#14). The map shows why Maersk's "end-to-end integrator" pivot has been so hard: the existing value chain is deeply scored for asset-light orchestration but the incumbent is asset-heavy.
- **#14 Think about value flow** (Phase II): satisfied — dependency structure traces value from demand signals through orchestration to physical movement to utilities.
- **#18 Be pragmatic about purchasing** (Phase II): implied — the build/buy/outsource call collapses cleanly along the ε axis.
- **#7 Use appropriate methods** (Phase I): flagged — the map currently under-represents the **Knowledge** and **Practice** layers (customs expertise, dangerous-goods handling, refrigerated-chain SOPs). A follow-up pass with the τ component-type function would surface these.

### f. Climatic context

The active climatic patterns shaping this map (see `references/climatic-patterns.md`):

- **#3 Everything evolves** — the landscape is mid-transition across multiple components simultaneously: EDI → API, human drivers → eventually autonomous, manual warehouses → robotics, paper customs → single-window digital.
- **#15-17 (inertia patterns)** — asset-heavy incumbents (Maersk, DHL, FedEx, UPS, Hapag-Lloyd) have enormous capital and organisational inertia that digital-native players exploit.
- **#27 Product-to-utility punctuated equilibrium** — Real-Time Visibility is mid-transition from Custom Built toward an industry-utility, and the winners will consolidate the market within 3-5 years. Warehouse Automation may be 5-10 years behind that transition.
- **#18 You cannot measure evolution over time or adoption** — the `evolve` arrows are scenarios, not schedules. A shock (pandemic, war, trade war) can accelerate or reverse direction-of-travel on any node.
- **#11 Componentisation accelerates change** — the modular cloud / API pattern that transformed retail in the 2010s is now playing out in logistics: the moment customs, rate-APIs, and visibility become composable, a generation of new orchestrators emerges.
- **#24 Efficiency enables innovation** — cheaper cloud, ubiquitous GPS, and commodity sensors are what make visibility-as-a-service viable at all.

### g. Deep-placement notes

I flagged and researched (desk-judgment from the training corpus rather than live search in this run) four components where the cheat-sheet rows disagreed or strategic weight was high:

- **Digital Freight Marketplaces** — initial cheat-sheet placement wanted 0.55 (early Product) based on ubiquity signals (Uber Freight, Convoy, Flexport). But certainty and publication-type rows argued for Custom Built (Convoy 2023 collapse, Flexport repeated pivots, no dominant matching-model). Settled at ε = 0.35 (late Custom Built) with wide uncertainty. This shifted the strategic call from "harvest" to "differentiate or exit".
- **Real-Time Visibility Platform** — cheat-sheet initially suggested ε = 0.55 (Product). A handful of serious vendors (project44, FourKites, Shippeo, Tive) and accelerating API-integration counts put ubiquity and publication-type at Stage III, but certainty (data-quality variance between carriers) and user-perception (still considered novel by mid-market shippers) pulled it back. Settled at ε = 0.45 with an `evolve` target of 0.70 — this is the fastest-moving component in the map.
- **Warehouse Automation / Robotics** — deliberately kept at ε = 0.30 (Genesis → Custom) despite the loud press around Amazon, Ocado, Symbotic, Covariant. Outside the largest handful of operators, warehouse automation is still bespoke integration work; publication type is mostly "describe the wonder" and case-study-heavy, not operations-handbook heavy. If the question were specifically about tier-1 grocery or Amazon-scale fulfilment, I would place it higher.
- **Single-Window Customs Filing** — initial placement wanted Stage III based on regulatory push (EU Customs Union Data Hub, UK Single Trade Window, US ACE). Held at ε = 0.45 because implementation maturity varies wildly by jurisdiction, and publication type is still "build / construct" rather than "operations". Evolve target 0.70 reflects the strong regulatory pull.

### h. Caveat

Evolution trajectories and `evolve` arrows in this map are strategic scenarios, not forecasts. Wardley's climatic pattern #18 is explicit: *"you cannot measure evolution over time or adoption."* The logistics landscape is also unusually exposed to exogenous shocks — pandemics, wars, climate events, tariff regimes, driver regulation — any of which can reverse direction-of-travel on individual components for a year or more. Use the map to reason about strategic posture, not to time investments.

---

## Summary: what is differentiating vs. commoditising, and where is the chain fragile?

**Differentiating (build, protect IP):**
- Real-Time Visibility Platforms and the API mesh that feeds them.
- Digital Freight Marketplaces with genuine matching IP.
- Route Optimisation, Load Planning, and Warehouse Automation at scale.
- Verticalised last-mile (cold chain, healthcare, white-glove).

**Commoditising (rent, harvest):**
- Road freight capacity, parcel networks at the base tier.
- Cloud, payments, containers, scan/barcode standards, fuel.
- Increasingly: customs single-window filing and emissions reporting (regulatorily forced toward utility).

**Fragile (watch, hedge, dual-source):**
- The visibility UX → carrier-API chain (data quality is the ceiling).
- Last-mile → gig labour → driver supply (labour regulation is a step-function risk).
- Cross-border orchestration → customs → brokerage (trade-policy shocks).
- Carrier → physical infrastructure choke-points (ports, airspace, canals).
- All carriers → fuel and lane access (commodity price and geopolitical exposure).
