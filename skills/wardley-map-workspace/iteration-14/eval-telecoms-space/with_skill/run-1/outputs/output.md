# Wardley Map — Telecoms via Space (February 2023)

## Scenario

The landscape of telecoms via space as of February 2023: low-earth-orbit (LEO) satellite broadband (Starlink-class) now scaling commercially; satellite-to-phone direct connectivity emerging as the next wave (AST SpaceMobile's BlueWalker 3 launched Sept 2022; T-Mobile + Starlink partnership announced Aug 2022; Apple Emergency SOS via Globalstar went live Nov 2022); competition with terrestrial mobile and fixed networks across rural, enterprise, maritime, aviation, and defence markets.

The strategic question is **what's differentiating vs. commoditising, and where does space-telecom disrupt the terrestrial model?**

---

## Map

```owm
title Telecoms via Space (Feb 2023)
style wardley

// Anchors — multiple user types; this is a multi-stakeholder landscape
anchor Rural / Remote Consumer [0.99, 0.35]
anchor Enterprise / Maritime / Aviation [0.97, 0.45]
anchor Government / Defense [0.95, 0.40]
anchor Mobile Network Operator (MNO) [0.93, 0.55]

// Primary user-facing services
component LEO Broadband Service [0.86, 0.42]
component Satellite-to-Phone Direct Connectivity [0.84, 0.12]
component Mobile Voice / SMS (terrestrial) [0.82, 0.92]
component In-Flight / Maritime Connectivity [0.80, 0.55]
component Defense Secure Comms [0.78, 0.35]
component Backhaul to Remote Cell Sites [0.76, 0.48]

// Terminals & customer-edge hardware
component LEO User Terminal (Dish) [0.70, 0.45]
component Phased-Array Antenna [0.64, 0.28]
component Unmodified Smartphone [0.72, 0.95]
component Ruggedised Enterprise Terminal [0.66, 0.50]

// Terrestrial alternatives (for comparison / inertia)
component Fiber Broadband Service [0.78, 0.88]
component Fixed Wireless Access (FWA) [0.76, 0.65]
component 4G/5G Macro Cellular Service [0.74, 0.82]
component Cell Tower Infrastructure [0.56, 0.85]
component Fiber Backhaul (terrestrial) [0.40, 0.90]

// Core network & service orchestration
component Service Activation & Billing [0.55, 0.78]
component MNO Roaming / IMSI Handling [0.52, 0.80]
component Network Operations Centre [0.50, 0.72]

// Space segment — constellation & satellites
component LEO Constellation (Starlink-class) [0.46, 0.40]
component Direct-to-Cell Satellite (large aperture) [0.42, 0.10]
component Inter-Satellite Laser Links [0.38, 0.25]
component Satellite Bus Platform [0.32, 0.58]
component Ion / Hall-effect Thrusters [0.28, 0.55]
component Satellite Payload Electronics [0.30, 0.45]

// Ground segment
component Ground Station / Gateway Network [0.36, 0.60]
component Teleport Real Estate & Siting [0.24, 0.60]
component Fiber Backhaul from Gateway [0.20, 0.92]

// Launch
component Launch Services [0.26, 0.50]
component Reusable Launch Vehicle [0.22, 0.40]
component Rocket Propellant / Pad Ops [0.14, 0.78]

// Spectrum, orbits, regulation
component Spectrum Rights (Ku / Ka / V band) [0.40, 0.30]
component Spectrum Rights (Mobile / MSS bands) [0.44, 0.35]
component Orbital Slot / Priority Filing (ITU) [0.34, 0.30]
component National Landing Rights / Market Access [0.32, 0.25]
component Space Debris / Collision Avoidance [0.18, 0.28]
component FCC / National Regulator Approval [0.30, 0.55]

// Practices / knowledge
component Orbital Mechanics & Station-Keeping [0.16, 0.70]
component RF Link Budget Engineering [0.14, 0.85]
component Mega-Constellation Ops Practice [0.12, 0.30]

// Commodity utilities
component Cloud Compute & Storage [0.10, 0.92]
component Power (Ground Sites) [0.08, 0.95]
component DNS / Internet Peering [0.06, 0.95]

// Dependencies
Rural / Remote Consumer->LEO Broadband Service
Rural / Remote Consumer->Satellite-to-Phone Direct Connectivity
Rural / Remote Consumer->Mobile Voice / SMS (terrestrial)
Enterprise / Maritime / Aviation->In-Flight / Maritime Connectivity
Enterprise / Maritime / Aviation->LEO Broadband Service
Enterprise / Maritime / Aviation->Ruggedised Enterprise Terminal
Government / Defense->Defense Secure Comms
Government / Defense->LEO Broadband Service
Mobile Network Operator (MNO)->Backhaul to Remote Cell Sites
Mobile Network Operator (MNO)->Satellite-to-Phone Direct Connectivity
Mobile Network Operator (MNO)->4G/5G Macro Cellular Service

// Service -> terminal / edge
LEO Broadband Service->LEO User Terminal (Dish)
LEO User Terminal (Dish)->Phased-Array Antenna
Satellite-to-Phone Direct Connectivity->Unmodified Smartphone
In-Flight / Maritime Connectivity->Ruggedised Enterprise Terminal
Ruggedised Enterprise Terminal->Phased-Array Antenna
Defense Secure Comms->Ruggedised Enterprise Terminal
Backhaul to Remote Cell Sites->LEO User Terminal (Dish)

// Terrestrial chain
Mobile Voice / SMS (terrestrial)->4G/5G Macro Cellular Service
4G/5G Macro Cellular Service->Cell Tower Infrastructure
Cell Tower Infrastructure->Fiber Backhaul (terrestrial)
Fixed Wireless Access (FWA)->4G/5G Macro Cellular Service
Fiber Broadband Service->Fiber Backhaul (terrestrial)

// Service orchestration
LEO Broadband Service->Service Activation & Billing
Satellite-to-Phone Direct Connectivity->MNO Roaming / IMSI Handling
LEO Broadband Service->Network Operations Centre
In-Flight / Maritime Connectivity->Service Activation & Billing

// Service -> space segment
LEO Broadband Service->LEO Constellation (Starlink-class)
Backhaul to Remote Cell Sites->LEO Constellation (Starlink-class)
In-Flight / Maritime Connectivity->LEO Constellation (Starlink-class)
Defense Secure Comms->LEO Constellation (Starlink-class)
Satellite-to-Phone Direct Connectivity->Direct-to-Cell Satellite (large aperture)

// Constellation internals
LEO Constellation (Starlink-class)->Satellite Bus Platform
LEO Constellation (Starlink-class)->Satellite Payload Electronics
LEO Constellation (Starlink-class)->Inter-Satellite Laser Links
LEO Constellation (Starlink-class)->Ion / Hall-effect Thrusters
Direct-to-Cell Satellite (large aperture)->Satellite Bus Platform
Direct-to-Cell Satellite (large aperture)->Satellite Payload Electronics
Direct-to-Cell Satellite (large aperture)->Inter-Satellite Laser Links

// Ground segment
LEO Constellation (Starlink-class)->Ground Station / Gateway Network
Direct-to-Cell Satellite (large aperture)->Ground Station / Gateway Network
Ground Station / Gateway Network->Teleport Real Estate & Siting
Ground Station / Gateway Network->Fiber Backhaul from Gateway
Network Operations Centre->Ground Station / Gateway Network

// Launch chain
LEO Constellation (Starlink-class)->Launch Services
Direct-to-Cell Satellite (large aperture)->Launch Services
Launch Services->Reusable Launch Vehicle
Reusable Launch Vehicle->Rocket Propellant / Pad Ops

// Spectrum / regulation / orbit
LEO Broadband Service->Spectrum Rights (Ku / Ka / V band)
Satellite-to-Phone Direct Connectivity->Spectrum Rights (Mobile / MSS bands)
Backhaul to Remote Cell Sites->Spectrum Rights (Ku / Ka / V band)
LEO Constellation (Starlink-class)->Orbital Slot / Priority Filing (ITU)
Direct-to-Cell Satellite (large aperture)->Orbital Slot / Priority Filing (ITU)
LEO Broadband Service->National Landing Rights / Market Access
Satellite-to-Phone Direct Connectivity->National Landing Rights / Market Access
LEO Broadband Service->FCC / National Regulator Approval
Satellite-to-Phone Direct Connectivity->FCC / National Regulator Approval
LEO Constellation (Starlink-class)->Space Debris / Collision Avoidance
Direct-to-Cell Satellite (large aperture)->Space Debris / Collision Avoidance

// Practices / knowledge
LEO Constellation (Starlink-class)->Orbital Mechanics & Station-Keeping
LEO Constellation (Starlink-class)->Mega-Constellation Ops Practice
Direct-to-Cell Satellite (large aperture)->Orbital Mechanics & Station-Keeping
Direct-to-Cell Satellite (large aperture)->Mega-Constellation Ops Practice
Satellite Payload Electronics->RF Link Budget Engineering
Ground Station / Gateway Network->RF Link Budget Engineering

// Utilities
Network Operations Centre->Cloud Compute & Storage
Service Activation & Billing->Cloud Compute & Storage
Ground Station / Gateway Network->Power (Ground Sites)
Cell Tower Infrastructure->Power (Ground Sites)
Fiber Backhaul from Gateway->DNS / Internet Peering

// Evolution arrows — where we expect movement
evolve Satellite-to-Phone Direct Connectivity 0.45
evolve LEO Broadband Service 0.65
evolve Reusable Launch Vehicle 0.62
evolve Mega-Constellation Ops Practice 0.55
evolve Backhaul to Remote Cell Sites 0.65
evolve Direct-to-Cell Satellite (large aperture) 0.35

note Differentiation / Wonder [0.80, 0.10]
note Terrestrial inertia zone [0.78, 0.90]
note Commodity utilities [0.12, 0.92]
```

Validator: **OK: 46 components/anchors, 70 edges — no violations.**

---

## Strategic analysis

### a. Differentiation opportunities (top 3)

1. **Satellite-to-Phone Direct Connectivity** (Genesis) — the headline opportunity. As of Feb 2023, three distinct engineering approaches are live but unproven at scale: AST SpaceMobile's BlueWalker 3 (massive phased-array aperture, full broadband ambition), Lynk Global (store-and-forward text), and Apple + Globalstar (Emergency SOS only). Nothing here is "a product" yet — publication type is *"describe the wonder"*, user perception is *novel / exciting*. Whoever makes the direct-to-unmodified-handset link work at scale with usable economics owns a multi-billion-user addressable base.
2. **Direct-to-Cell Satellite (large aperture)** (Genesis) — the enabling spacecraft class. Building a low-orbit satellite that closes a link budget to a 1-watt handset is a physics-heavy, capital-intensive craft problem. BlueWalker 3 is ~64 m² of phased array; this is not a cloneable product in 2023. The spacecraft IS the moat for the service above it.
3. **Mega-Constellation Ops Practice** (Genesis → Custom Built) — the operational knowledge of flying 4,000+ satellites, doing 40,000+ daily manoeuvres, and keeping conjunction rates survivable. SpaceX has a three-year head start on this muscle memory; nobody else has flown at that scale. Classic co-evolved practice (climatic pattern #9): as the activity industrialises, the practice has to emerge with it.

### b. Commodity-leverage candidates (top 3)

1. **Cloud Compute & Storage** (Commodity +utility) — rent from AWS / GCP / Azure for the NOC, billing, and mission-control back-end. Building your own data centre to run a space business is a doctrine #17 violation.
2. **Fiber Backhaul from Gateway** (Commodity +utility) and **DNS / Internet Peering** (Commodity +utility) — standard internet plumbing between gateways and the public internet. Buy transit; don't build a carrier.
3. **Power (Ground Sites)** and **Rocket Propellant / Pad Ops** (both Commodity +utility territory) — buy, don't engineer. The interesting question is what sits *above* these utilities, not the utilities themselves.

A fourth candidate worth naming despite being a non-obvious case: **Phased-Array Antenna** (Custom Built, 0.28) is *not yet* a commodity in Feb 2023 — user-terminal dishes remain expensive (~$600 hardware cost for Starlink dish, reportedly sold below cost). But the trajectory is clear; this is a **Directed investment** target (gameplay #36) if your strategy is consumer scale, because terminal cost is the gating constraint on total addressable market.

### c. Dependency risks (top 3)

1. **LEO Broadband Service → LEO Constellation (Starlink-class)** — a Product (+rental)–trajectory service anchored on a single-vendor, Custom Built space asset. For a non-SpaceX entrant (OneWeb, Kuiper, Telesat), the failure mode is stark: the service depends on a capital-intensive constellation where the economics work only at SpaceX's launch cost. Expressed as R = ν(source) × (1 − ε(target)): visible service on an immature foundation.
2. **Satellite-to-Phone Direct Connectivity → Spectrum Rights (Mobile / MSS bands)** — the service only works if regulators let you reuse terrestrial mobile spectrum from orbit. This is a novel regulatory concept; FCC's Supplemental Coverage from Space framework was only proposed in March 2023. The entire service value depends on a contested regulatory decision per-jurisdiction.
3. **LEO Constellation → Orbital Slot / Priority Filing (ITU)** and **→ Space Debris / Collision Avoidance** — the long-term viability of the whole space segment depends on orbital-shell governance that is itself in early Custom Built. The Kessler-cascade risk and the slot-overcrowding risk are both real and under-instrumented.
4. (Honourable mention) **Backhaul to Remote Cell Sites → LEO Constellation** — an MNO's reach into rural areas now rides on a single vendor with whom they are also competitors (Starlink sells direct to consumer). Classic supplier-power trap.

### d. Suggested gameplays

Two strategic archetypes dominate this map — a **scaling incumbent** (SpaceX-Starlink), and **challengers / telco incumbents reacting**.

For the scaling incumbent:
- **#55 Land grab** — already executed on orbital slots and LEO volumes. Priority ITU filings are the pre-positioning move.
- **#40 Fool's mate** — force-industrialise Launch Services. Reusable launch turned launch from Custom Built to early Product (+rental); this forces every competitor's economics.
- **#43 Sensing Engines (ILC)** — Starlink uses its own adoption data across geographies to decide where to deploy terminals and which services (maritime, aviation, direct-to-cell) to productise next. Classic ILC.
- **#16 Exploiting Network Effects** — less obvious but real: each additional satellite improves coverage and capacity for every existing user, a supply-side network effect.
- **#19 Exploiting existing constraints** — reusable-rocket capacity is the real constraint SpaceX owns. No competitor can match $/kg to LEO in 2023.

For the MNO / telco incumbent deciding how to respond:
- **#41 Alliances** — the T-Mobile + Starlink and AT&T + AST partnerships are textbook alliance plays. The MNO brings spectrum and customer base; the space player brings satellites.
- **#57 Fast follower** — for OneWeb, Kuiper, Telesat: do not try to out-innovate Starlink on the Genesis/Custom parts; follow into the Product (+rental) band with differentiated verticals (enterprise, government, maritime) where margin is higher.
- **#50 Reinforcing inertia** — for terrestrial telcos facing Starlink in rural markets, ironically the winning move is to *not* try to match Starlink on rural fixed wireless. Redirect capex to urban 5G where terrestrial still wins.

For policy / regulator-side plays that are emerging:
- **#13 Lobbying** is active on multiple fronts: MNOs lobbying against D2C spectrum reallocation; environmental groups lobbying on debris; national regulators deciding landing rights (some denying — see Russia, China, India).
- **#15 Open Approaches** — not yet happening but available: an open standard for D2C modems (3GPP NTN in Release 17/18 is the beginning) could commoditise the service faster than any single vendor wants.

For all players:
- **#36 Directed investment** on **Phased-Array Antenna** (the terminal-cost constraint on TAM) and on **Mega-Constellation Ops Practice** (the operational knowledge gap).

### e. Doctrine notes

- Principle **#10 Know your users**: satisfied. Four anchors (consumer, enterprise, government/defence, MNO) correctly represent a multi-sided market where the same infrastructure serves fundamentally different needs at different price points. Single-anchor treatment would hide the MNO-as-customer / MNO-as-competitor tension.
- Principle **#1 Focus on user needs**: mostly satisfied, but risk of violation — some Genesis components (Inter-Satellite Laser Links, Ion Thrusters) risk becoming engineering vanity if pursued without a clear user-need pull. Laser links serve polar coverage and reduced gateway dependence; worth calling that out explicitly.
- Principle **#13 Manage inertia**: critical and active. Three of the 17 structured inertia forms are dominant here (see section f below).
- Principle **#22 Use standards where appropriate**: under tension. 3GPP NTN standards (Release 17, frozen mid-2022) push toward early standardisation of NTN, which is arguably premature for the direct-to-cell variant (still Genesis). Standards may lock in a suboptimal architecture.
- Principle **#33 There is no one culture**: for a vertically integrated player, the spread across the map — Genesis-stage D2C through Commodity (+utility) cloud utilities — means Pioneer-Settler-Town-Planner partitioning is essential. Flying a mega-constellation operationally is a Town Planner function; designing the next satellite generation is a Pioneer/Settler function.

### f. Climatic context

Active patterns on this map:

- **#3 Everything evolves through supply and demand competition** — the whole map is on the move. LEO Broadband Service is transitioning Custom Built → Product (+rental); launch is Custom Built → Product (+rental); direct-to-cell is Genesis → Custom Built.
- **#4 Evolution consists of multiple waves of diffusion with many chasms** — this is the dominant climatic pattern for this map. LEO broadband IS the "next wave" after GEO VSAT; D2C is the next wave after LEO broadband. Multi-wave dynamics are more informative here than a single S-curve.
- **#22 Two forms of disruption** — we see both forms simultaneously:
  - **Product-to-utility disruption** on Launch (reusable rockets industrialised launch) and on Broadband (LEO industrialising rural broadband). These are *predictable*.
  - **Genesis-driven disruption** on D2C (an uncharted component emerging from the smartphone connectivity gap). *Unpredictable.*
- **#27 Product-to-utility punctuated equilibrium** — rural fixed-wireless is experiencing this right now. The collapse of rural DSL and the rapid rise of Starlink in the 2021–2023 window is compressed, not gradual. Rural telcos that waited are being stranded.
- **#15–17 Inertia patterns** — terrestrial-MNO inertia is visible: MNOs have hundreds of billions sunk into cell-tower capital (inertia form #2 sunk capital), they are politically committed to the 5G story (#3 political capital), their customer-care processes and billing systems are built for terrestrial (#9 re-architecture cost), and re-architecting toward hybrid terrestrial-satellite is hard. This is precisely what creates the Starlink + T-Mobile style partnership opportunity: the MNO outsources the new-wave inertia problem to a new-wave player.
- **#11 Future value is inversely proportional to certainty** — the Genesis-stage D2C service has the highest future value *and* the highest uncertainty. Treat as an option, not a plan.
- **#18 You cannot measure evolution over time or adoption** — the `evolve` arrows in the map are scenarios, not forecasts. See caveat.

### g. Deep-placement notes

Of the 42 non-anchor components, four were flagged for closer placement because of cheat-sheet disagreement or strategic criticality (rules from skill step 4.5: top-3 by differentiation / top-3 by commodity leverage / strategically-critical). Notes below; where I did not run a live web search, I relied on state-of-play as of Feb 2023 and flagged uncertainty accordingly.

- **Satellite-to-Phone Direct Connectivity (ε = 0.12)** — flagged as strategically critical (top-D) and as a recent domain. Evidence supporting Genesis placement: publication type in late-2022 press is *"describe the wonder"* (BlueWalker 3 launch coverage treats it as revolutionary, not iterative); vendor count is tiny and incompatible (AST, Lynk, Globalstar each use different architectures); user perception is *novel / exciting* (Apple marketed Emergency SOS as a halo feature, not an expected utility); certainty is *poorly understood* (can it actually close a link to a 1-watt handset reliably?). Cheat-sheet rows agree on Genesis. Placement confirmed.
- **LEO Broadband Service (ε = 0.42)** — flagged for cheat-sheet disagreement. Ubiquity row says Stage II (slowly increasing — roughly 1M Starlink subscribers globally by Feb 2023); Certainty row says Stage II (still rapid learning, Starlink is adding new capabilities); User Perception row says Stage II–III (early adopters still talk about it but expectations are forming); Publication row says Stage II (*build / construct / awareness*, though ops guides are appearing). Mean lands around 0.42 (late Custom Built, on the threshold of Product (+rental)). The `evolve` arrow to 0.65 reflects the expected transition as Kuiper, OneWeb commercial launches, and Eutelsat-OneWeb-Viasat mergers all land in 2023–2024.
- **Reusable Launch Vehicle (ε = 0.40)** — flagged as strategically critical (underpins the whole map's economics). Cheat-sheet disagreement: Falcon 9 is clearly in Custom Built / early Product (SpaceX has productised reuse at ~200+ reflights as of Feb 2023) but there is still only one vendor at scale (Rocket Lab's Neutron, Blue Origin's New Glenn, Ariane 6 reusability not yet flying; Chinese players in Custom). Placement at 0.40 reflects this single-vendor reality — it is product-like *for SpaceX* and Custom Built *for everyone else*. Published roadmaps through 2025 (Neutron, Terran-R, New Glenn) justify the `evolve` arrow to 0.62.
- **Spectrum Rights (Mobile / MSS bands) (ε = 0.35)** — flagged because the regulatory status in Feb 2023 is in active flux. The FCC's Supplemental Coverage from Space NPRM is imminent (it arrived in March 2023). ITU-level coordination for NGSO-in-terrestrial-spectrum is unresolved. Vendor count is by definition small (a handful of MNO-SatelliteCo partnerships). This is a custom-per-jurisdiction regime right now. Placement at 0.35 reflects that.

Three components I deliberately did NOT deep-research because they were confidently placeable:
- **Cloud Compute & Storage**, **DNS / Internet Peering**, **Power (Ground Sites)** — all unambiguously Stage IV utilities; deep search would add cost without information.

### h. Where does space-telecom disrupt the terrestrial model?

Synthesising the map: space-telecom disrupts terrestrial at three distinct boundaries, each with a different disruption type and time horizon.

1. **Rural fixed broadband** (happening now, product-to-utility disruption). LEO Broadband Service is displacing DSL, WISPs, and geostationary broadband in rural markets. This is mechanically inevitable once reusable launch + phased-array terminals + LEO latency hit their cost curves. The climatic pattern is #27 (punctuated equilibrium); rural telcos that haven't already moved are stranded.

2. **Remote backhaul and hard-to-reach cell sites** (happening now, alliance-driven). MNOs can't economically reach every rural cell site with fibre; LEO backhaul is already commercially viable. This is *complementary* rather than disruptive — the MNO keeps the customer relationship and buys backhaul capacity.

3. **Direct-to-phone connectivity for mobile coverage gaps** (emerging, Genesis disruption). This is the interesting frontier. At minimum, it is a feature (Emergency SOS, off-grid text). At maximum — if AST-class architecture works at scale with sensible economics — it is a partial bypass of the cell-tower economic model for low-density areas. That scenario is highly uncertain. MNOs' best move is the alliance play (T-Mobile + Starlink) because it converts a disruption threat into a supplier relationship.

**What the map says about differentiation vs. commoditisation, at a glance:**

- **Left / top (differentiating):** Direct-to-cell satellites and the direct-to-phone service; phased-array antennas; mega-constellation ops practice; reusable launch; orbital priority; inter-satellite links.
- **Right / top (commoditising, visible):** Mobile voice/SMS, fiber broadband, 4G/5G — the terrestrial incumbents. Also: unmodified smartphone (the device is a commodity; the question is what services reach it).
- **Right / bottom (commodity utilities, deep):** Cloud, power, DNS, peering, fiber backhaul. Rent these. Don't build.
- **Left / bottom (specialist knowledge):** Orbital mechanics, RF link-budget engineering, propellant handling. Hire expertise; don't attempt to reinvent.

### i. Inertia watch

From the 17 structured forms of inertia, these three dominate the Feb 2023 map:

- **Form #2 Sunk capital (consumer-side)** — MNOs' cell-tower investment base; incumbent satellite operators' GEO fleets (Viasat, Intelsat) represent sunk capital that makes moving to LEO architecturally expensive.
- **Form #9 Re-architecture cost (consumer-side)** — moving an MNO's core network, OSS/BSS, and roaming systems to integrate satellite access is non-trivial. This inertia is why the T-Mobile + Starlink integration timeline is multi-year, not quarters.
- **Form #14 Strategic-control loss (consumer-side)** — MNOs partnering with Starlink worry about being disintermediated. Starlink's consumer-direct business means the MNO is buying capacity from a competitor. This inertia suppresses partnership speed and creates the opening for AST-style "MNO-friendly" architectures.

Supplier-side inertia (forms #15–17) is visible in the established GEO operators' slow response to LEO — Viasat-3's decade-long development and 2023 deployment is fighting the last war. The pending Viasat-Inmarsat merger is partly an answer to this inertia.

### j. Caveat

Evolution trajectories (the `evolve` arrows, and the narrative "will industrialise" claims above) are **scenarios, not forecasts**. Wardley's climatic pattern #18: *"you cannot measure evolution over time or adoption."* The map reflects the landscape as of February 2023 with these specific signals:

- Reusable launch industrialised (Falcon 9 at ~200+ reflights by late 2022).
- Starlink past 1M subscribers globally (announced December 2022).
- BlueWalker 3 launched September 2022 — full-size D2C antenna on orbit but service not yet commercial.
- Apple + Globalstar Emergency SOS live November 2022 (limited service).
- T-Mobile + Starlink direct-to-cell partnership announced August 2022; service targeted for 2023 beta.
- 3GPP NTN (Release 17) frozen mid-2022, starting to appear in silicon roadmaps.
- FCC NPRM on Supplemental Coverage from Space *imminent* at the time of this map (it arrived March 2023).

Major discontinuities that could rewrite the map — debris cascade (Kessler), loss of orbital coordination (ITU priority disputes with China/Russia), spectrum-rule reversal on D2C, a major D2C launch failure, or a reusable-rocket second mover arriving faster than expected — are all known unknowns and none are priced in the `evolve` arrows.
