# Telecoms Sovereignty — Wardley Map (October 2022)

## Map

```owm
title Telecoms Sovereignty (October 2022)
style wardley

// Anchors — three user types
anchor Nation-State (Security & Control) [0.99, 0.40]
anchor Citizen (Connectivity) [0.97, 0.70]
anchor Business (Enterprise Connectivity) [0.96, 0.60]

// State-facing sovereignty controls
component Supplier Designation Regime (TSA 2021) [0.88, 0.20]
component Telecoms Security Code of Practice [0.82, 0.30]
component National Security Review (Ofcom/DCMS) [0.80, 0.22]
component Lawful Intercept Capability [0.78, 0.55]
component Critical-Infrastructure Resilience Policy [0.75, 0.25]

// Citizen / business user-facing services
component Mobile Voice & Data Service [0.88, 0.80]
component Fixed Broadband Service [0.86, 0.82]
component Enterprise Private Connectivity [0.80, 0.60]
component Private 5G Network (Enterprise) [0.70, 0.35]
component Emergency / Resilient Comms [0.90, 0.50]

// Access layer
component 5G Radio Access Network (RAN) [0.65, 0.55]
component OpenRAN Deployment [0.62, 0.30]
component 4G RAN [0.60, 0.85]
component Fibre Access (FTTP/FTTH) [0.58, 0.70]
component DOCSIS / Copper Access [0.55, 0.88]

// Core / control plane
component 5G Standalone Core [0.50, 0.45]
component 4G/EPC Core [0.48, 0.80]
component Network Management & Orchestration [0.45, 0.55]
component Subscriber Identity (SIM/eSIM) [0.52, 0.78]

// Transport and interconnect
component National Backbone Transport [0.42, 0.75]
component Internet Exchange Points (IXPs) [0.38, 0.82]
component Subsea Cable Systems [0.35, 0.70]
component Satellite Backhaul (GEO) [0.45, 0.80]
component LEO Satellite Broadband (Starlink) [0.55, 0.30]
component BGP Routing / Internet Peering [0.30, 0.88]
component DNS Infrastructure [0.25, 0.92]

// Spectrum and physical assets
component Spectrum Allocation (Ofcom) [0.48, 0.72]
component Mast / Tower Sites [0.40, 0.85]
component Data Centres & Landing Stations [0.30, 0.78]
component Grid Electricity / Backup Power [0.15, 0.95]

// Equipment supply chain
component RAN Vendor Equipment (Ericsson/Nokia/Samsung) [0.32, 0.65]
component Restricted Vendor Equipment (Huawei legacy) [0.30, 0.70]
component Optical Transport Equipment [0.22, 0.80]
component Network Silicon / ASICs [0.15, 0.55]
component Advanced Semiconductor Fabrication [0.10, 0.40]
component Semiconductor Industrial Policy (CHIPS / EU Chips) [0.08, 0.22]

// Standards and software
component 3GPP Standards [0.28, 0.82]
component O-RAN Alliance Specifications [0.35, 0.35]
component Network Function Virtualisation (NFV/CNF) [0.30, 0.65]

// Security / trust
component Threat Intelligence & NCSC Guidance [0.55, 0.40]
component Post-Quantum / Encryption Stack [0.40, 0.30]
component Cable & Infrastructure Monitoring [0.32, 0.35]

// Knowledge / workforce
component Telecoms Engineering Workforce [0.22, 0.50]
component International Alliances (Five Eyes / NATO) [0.50, 0.45]

// Dependencies — citizen / business / state to user-facing services
Nation-State (Security & Control)->Supplier Designation Regime (TSA 2021)
Nation-State (Security & Control)->Telecoms Security Code of Practice
Nation-State (Security & Control)->National Security Review (Ofcom/DCMS)
Nation-State (Security & Control)->Lawful Intercept Capability
Nation-State (Security & Control)->Critical-Infrastructure Resilience Policy
Nation-State (Security & Control)->Emergency / Resilient Comms
Nation-State (Security & Control)->International Alliances (Five Eyes / NATO)
Citizen (Connectivity)->Mobile Voice & Data Service
Citizen (Connectivity)->Fixed Broadband Service
Citizen (Connectivity)->Emergency / Resilient Comms
Business (Enterprise Connectivity)->Enterprise Private Connectivity
Business (Enterprise Connectivity)->Mobile Voice & Data Service
Business (Enterprise Connectivity)->Private 5G Network (Enterprise)
Business (Enterprise Connectivity)->Fixed Broadband Service

// Regime → targets
Supplier Designation Regime (TSA 2021)->RAN Vendor Equipment (Ericsson/Nokia/Samsung)
Supplier Designation Regime (TSA 2021)->Restricted Vendor Equipment (Huawei legacy)
Telecoms Security Code of Practice->5G Radio Access Network (RAN)
Telecoms Security Code of Practice->5G Standalone Core
National Security Review (Ofcom/DCMS)->Subsea Cable Systems
National Security Review (Ofcom/DCMS)->Data Centres & Landing Stations
Critical-Infrastructure Resilience Policy->Subsea Cable Systems
Critical-Infrastructure Resilience Policy->Grid Electricity / Backup Power
Critical-Infrastructure Resilience Policy->Cable & Infrastructure Monitoring
Lawful Intercept Capability->5G Standalone Core
Lawful Intercept Capability->4G/EPC Core

// Services → access
Mobile Voice & Data Service->5G Radio Access Network (RAN)
Mobile Voice & Data Service->4G RAN
Mobile Voice & Data Service->5G Standalone Core
Mobile Voice & Data Service->4G/EPC Core
Mobile Voice & Data Service->Subscriber Identity (SIM/eSIM)
Fixed Broadband Service->Fibre Access (FTTP/FTTH)
Fixed Broadband Service->DOCSIS / Copper Access
Enterprise Private Connectivity->National Backbone Transport
Enterprise Private Connectivity->Fibre Access (FTTP/FTTH)
Private 5G Network (Enterprise)->OpenRAN Deployment
Private 5G Network (Enterprise)->5G Standalone Core
Private 5G Network (Enterprise)->Spectrum Allocation (Ofcom)
Emergency / Resilient Comms->LEO Satellite Broadband (Starlink)
Emergency / Resilient Comms->Satellite Backhaul (GEO)
Emergency / Resilient Comms->Mobile Voice & Data Service

// Access → core / transport
5G Radio Access Network (RAN)->5G Standalone Core
5G Radio Access Network (RAN)->Mast / Tower Sites
5G Radio Access Network (RAN)->Spectrum Allocation (Ofcom)
5G Radio Access Network (RAN)->RAN Vendor Equipment (Ericsson/Nokia/Samsung)
OpenRAN Deployment->O-RAN Alliance Specifications
OpenRAN Deployment->Network Silicon / ASICs
OpenRAN Deployment->Network Function Virtualisation (NFV/CNF)
OpenRAN Deployment->Mast / Tower Sites
4G RAN->Mast / Tower Sites
4G RAN->Spectrum Allocation (Ofcom)
4G RAN->RAN Vendor Equipment (Ericsson/Nokia/Samsung)
4G RAN->Restricted Vendor Equipment (Huawei legacy)
Fibre Access (FTTP/FTTH)->National Backbone Transport
Fibre Access (FTTP/FTTH)->Optical Transport Equipment
DOCSIS / Copper Access->National Backbone Transport

// Core / orchestration
5G Standalone Core->Network Function Virtualisation (NFV/CNF)
5G Standalone Core->Network Management & Orchestration
5G Standalone Core->3GPP Standards
4G/EPC Core->3GPP Standards
4G/EPC Core->Network Management & Orchestration
Network Management & Orchestration->Data Centres & Landing Stations

// Transport chain
National Backbone Transport->Optical Transport Equipment
National Backbone Transport->Data Centres & Landing Stations
National Backbone Transport->BGP Routing / Internet Peering
Internet Exchange Points (IXPs)->BGP Routing / Internet Peering
Internet Exchange Points (IXPs)->Data Centres & Landing Stations
Subsea Cable Systems->Data Centres & Landing Stations
Subsea Cable Systems->Cable & Infrastructure Monitoring
Satellite Backhaul (GEO)->National Backbone Transport
LEO Satellite Broadband (Starlink)->Network Silicon / ASICs
LEO Satellite Broadband (Starlink)->Spectrum Allocation (Ofcom)
BGP Routing / Internet Peering->DNS Infrastructure

// Equipment → silicon
RAN Vendor Equipment (Ericsson/Nokia/Samsung)->Network Silicon / ASICs
RAN Vendor Equipment (Ericsson/Nokia/Samsung)->3GPP Standards
Restricted Vendor Equipment (Huawei legacy)->Network Silicon / ASICs
Optical Transport Equipment->Network Silicon / ASICs
Network Silicon / ASICs->Advanced Semiconductor Fabrication
Advanced Semiconductor Fabrication->Semiconductor Industrial Policy (CHIPS / EU Chips)

// Physical
Mast / Tower Sites->Grid Electricity / Backup Power
Data Centres & Landing Stations->Grid Electricity / Backup Power

// Security / knowledge
Threat Intelligence & NCSC Guidance->International Alliances (Five Eyes / NATO)
Lawful Intercept Capability->Threat Intelligence & NCSC Guidance
Post-Quantum / Encryption Stack->3GPP Standards
Cable & Infrastructure Monitoring->Data Centres & Landing Stations
Subscriber Identity (SIM/eSIM)->3GPP Standards

// Workforce underpins access/core build
5G Radio Access Network (RAN)->Telecoms Engineering Workforce
5G Standalone Core->Telecoms Engineering Workforce
OpenRAN Deployment->Telecoms Engineering Workforce

// Evolve arrows — October 2022 forward-looking
evolve OpenRAN Deployment 0.55
evolve 5G Standalone Core 0.65
evolve LEO Satellite Broadband (Starlink) 0.55
evolve Semiconductor Industrial Policy (CHIPS / EU Chips) 0.45
evolve Post-Quantum / Encryption Stack 0.50

note Sovereignty moat (build / regulate) [0.78, 0.22]
note Utility commodity layer [0.18, 0.90]
```

---

## Strategic analysis

### a. Differentiation opportunities (top 3)

Top rank leads with stage labels; D heuristic used only as an attention prompt.

1. **Supplier Designation Regime / TSA 2021 (Genesis → Custom Built)** — the UK's novel legal instrument is the most sovereignty-defining lever on the map. Few peer regimes exist; the October 2022 designation notices on Huawei make this the live experiment. This is national-level IP, not just regulation.
2. **OpenRAN Deployment (Custom Built)** — first commercial deployments in 2022 make OpenRAN the sharpest bet for a sovereign, multi-vendor alternative to the three-vendor RAN oligopoly. High visibility for enterprise private-5G users, still pre-product.
3. **Cable & Subsea Infrastructure Monitoring (Custom Built)** — post-Nord Stream, surveillance of subsea assets is a Custom-Built capability that nations are scrambling to industrialise. Limited vendor landscape; bespoke integrations per landing station.

Runner-up: **Post-Quantum / Encryption Stack (Custom Built)** — NIST's first PQC candidates were finalised around this window; still Custom Built for telecoms use.

### b. Commodity-leverage candidates (top 3)

Stage III/IV components — rent, don't build.

1. **DNS Infrastructure, BGP Routing / Internet Peering, Grid Electricity / Backup Power (Commodity +utility)** — treat as utilities. Sovereignty concerns here are about *resilience and provenance*, not about building them.
2. **3GPP Standards, 4G/EPC Core, DOCSIS / Copper Access (Commodity +utility / late Product +rental)** — mature globally-standardised layers; any nation trying to re-invent these is burning money.
3. **Mobile Voice & Data / Fixed Broadband services (Commodity +utility)** — the end-user experience layer is itself commoditised. Nations don't compete on bandwidth; they compete on the trust and security underneath.

### c. Dependency risks (top 3)

Visible components sitting on fragile or concentrated foundations.

1. **Mobile Voice & Data Service → 5G Standalone Core (Commodity +utility service on a still-Custom-Built core)** — ~29 CSPs live with SA core in Oct 2022 means the dependency is on an emerging, vendor-concentrated stack that carries lawful-intercept obligations under the Code of Practice.
2. **5G RAN / 4G RAN → RAN Vendor Equipment (Ericsson/Nokia/Samsung)** — post-Huawei designation the UK is down to effectively two-and-a-half trusted vendors. Supplier concentration is the headline sovereignty risk; OpenRAN is the intended mitigation but is not yet a production substitute.
3. **Subsea Cable Systems → Data Centres & Landing Stations, with Cable Monitoring still immature** — Nord Stream sabotage has just demonstrated that physical sabotage of subsea infrastructure is now part of the threat model; monitoring capability is nowhere near commoditised.

Honourable mention: **Network Silicon → Advanced Semiconductor Fabrication** — a single-digit number of leading-edge fabs (TSMC, Samsung, soon Intel) underpins every RAN/core/optical component. CHIPS and EU Chips Acts are the national response; the risk persists for at least a decade.

### d. Suggested gameplays (named from Wardley's 61-play catalogue)

- **#15 Open Approaches — OpenRAN & O-RAN Alliance.** Accelerate the shift of RAN from Product (+rental) duopoly to Commodity (+utility) by backing open specs and reference implementations.
- **#36 Directed Investment — OpenRAN, 5G SA Core, Cable Monitoring, PQC.** Public funding at Custom-Built components where the state is an anchor user.
- **#41 Alliances — Five Eyes / NATO and the CHIPS/EU-Chips pact.** Share supply-chain risk and intel at components no single nation can afford to own.
- **#56 First Mover — TSA 2021 supplier designation.** The UK is a first mover in codifying high-risk vendor exclusion into primary legislation; export the template via alliances.
- **#29 Harvesting — LEO Satellite Broadband.** Don't build a UK Starlink; license capacity and shape the regulatory terms as the market consolidates.
- **#43 Sensing Engines (ILC) — threat intelligence feeding designation.** Use NCSC observations to identify the next class of components (optical, cloud, edge) that need regulatory attention before they become systemic.
- **#26 Differentiation — Sovereign-grade managed service.** For the business anchor, offer a UK-trusted-vendor managed connectivity bundle; a national-security-graded product does not exist today.

### e. Doctrine notes (against Wardley's 40)

- Pass — **#1 Focus on user needs** and **#10 Know your users**: three anchors (Nation-State, Citizen, Business) correctly encode the three conflicting user needs. A single-anchor map of this domain would collapse the strategic tension.
- Watch — **#13 Manage inertia**: the 4G/Huawei legacy is an explicit inertia node. Re-architecture cost (inertia form #9) and sunk-capital cost (form #2) will dominate CSP behaviour through 2027.
- Watch — **#2 Use a systematic mechanism of learning**: Cable & Infrastructure Monitoring has no feedback loop to Threat Intelligence / NCSC Guidance yet; the ILC path is under-built for subsea.
- Gap — **Knowledge layer under-specified**: Telecoms Engineering Workforce is a single node but real sovereignty requires several (RAN engineers, core-network engineers, security-cleared ops staff). Flagged rather than over-decomposed.

### f. Climatic context (from Wardley's 27 patterns)

Actively shaping this map in Oct 2022:

- **#3 Everything evolves** — the whole RAN/core stack is mid-industrialisation; the state is trying to shape the evolution rate via TSA 2021 and industrial policy.
- **#15-17 Inertia (past success, sunk capital, re-architecture)** — the installed Huawei 4G base and legacy EPC core are the dominant inertia sources.
- **#27 Product-to-utility punctuated equilibrium** — RAN is being pushed from Product (+rental) toward Commodity (+utility) via OpenRAN; a classic Wardley inflection.
- **#13 Competitors actions (capital-flight geopolitics)** — Nord Stream sabotage, US/EU chip legislation, and Starlink's Ukraine deployment are all competitor / adversary moves reshaping the map within months.
- **#18 You cannot measure evolution over time or adoption** — see caveat.

### g. Deep-placement notes

Targeted research was not run for this blind-benchmark pass; placements are cheat-sheet-driven with priors grounded in the Oct 2022 context given. Components I would have flagged for deep placement given budget:

- **5G Standalone Core**: cheat-sheet puts this at the Custom→Product boundary (0.45). The "~29 CSPs live" figure is a Stage-II→III transition signal — vendor-count search (Ericsson/Nokia/Samsung/Mavenir/Huawei-excluded, plus cloud-native entrants) would likely confirm ~0.45 but could nudge to 0.50.
- **OpenRAN**: placed at 0.30 (Custom Built). Commercial deployments are a Stage-II signal but they are still bespoke integrations; vendor-count and case-study searches (Vodafone UK, Rakuten, DISH) would be the test.
- **LEO Satellite Broadband (Starlink)**: placed at 0.30. Ukraine operational use is a Stage-I→II proof point; SpaceX is essentially sole-source commercial LEO at this date. OneWeb/Kuiper activity would be the indicator to watch — today it confirms Custom Built.
- **Cable & Infrastructure Monitoring**: placed at 0.35. Nord Stream just happened; a search on vendors (Sonardyne, HGH, naval-grade SONAR integrators) would likely widen the uncertainty rather than resolve it.

No placements were shifted from cheat-sheet priors in this run.

### h. Caveat

Evolution trajectories shown via `evolve` arrows are scenarios, not forecasts. Wardley's climatic pattern #18: *"you cannot measure evolution over time or adoption."* The October-2022 snapshot is a mapping of where components sit given the signals available at that moment — the designation regime is new, OpenRAN is unproven at scale, Starlink's strategic role is still being discovered, and CHIPS/EU Chips Act effects will not show for years. Re-map on each major signal (new designation, major cable incident, fab commissioning) rather than treating this as a roadmap.

---

## Validator output (Step 5.5)

```
OK: 47 components/anchors, 88 edges — no violations.
```
