# Telecoms Sovereignty — October 2022

A Wardley Map of a nation-state's telecoms sovereignty, anchored on the four user types named in the scenario (Government, The Collective, Corporations, People) and covering the six sovereignty pillars (territorial, political, cultural, economic, digital, CNI), the communication stack from devices through access networks to the control layer, the theatre / awareness layer, expertise, and the underlying reality of geography, supply chains, compute, power, and space.

## Map

```owm
title Telecoms Sovereignty (October 2022)
style wardley

// Anchors — four distinct user types per the scenario
anchor Government [0.98, 0.35]
anchor The Collective [0.96, 0.45]
anchor Corporations [0.94, 0.60]
anchor People [0.96, 0.70]

// ===========================================================
// Sovereignty pillars (user-visible policy outcomes)
// ===========================================================
component Territorial Sovereignty [0.90, 0.30]
component Political Sovereignty [0.90, 0.40]
component Cultural Sovereignty [0.88, 0.45]
component Economic Sovereignty [0.88, 0.55]
component Digital Sovereignty [0.87, 0.35]
component CNI Protection [0.86, 0.45]

// ===========================================================
// Access devices (what citizens and corporations hold)
// ===========================================================
component Smartphones [0.80, 0.82]
component Computers [0.78, 0.85]
component Radio and TV Receivers [0.76, 0.88]
component Sat Phones [0.74, 0.65]
component IoT Devices [0.72, 0.70]

// ===========================================================
// Access networks (connecting devices to the backbone)
// ===========================================================
component Mobile Towers and RAN [0.64, 0.72]
component Fixed Cable Access [0.62, 0.80]
component Satellite Access [0.60, 0.58]
component Launch Vehicles [0.40, 0.40]

// ===========================================================
// Network equipment and topology
// ===========================================================
component Fixed Network Topology [0.56, 0.78]
component Mobile Network Core [0.54, 0.66]
component Network Equipment Vendors [0.48, 0.65]
component Subsea Cable Landings [0.44, 0.70]
component International Peering [0.46, 0.60]

// ===========================================================
// Control layer (sovereign choke points)
// ===========================================================
component SIM and eSIM Identity [0.58, 0.73]
component Nation-State Firewall and DPI [0.55, 0.68]
component DNS Resolution [0.52, 0.85]
component DNS over HTTPS [0.60, 0.78]
component Geofencing and Lawful Intercept [0.56, 0.58]
component Spectrum Allocation [0.52, 0.42]

// ===========================================================
// Theatre and awareness layer
// ===========================================================
component Awareness of Land-Sea-Air-Space [0.70, 0.30]
component Supply Chain Awareness [0.69, 0.26]
component Cyber Situational Awareness [0.66, 0.40]

// ===========================================================
// Expertise (knowledge layer)
// ===========================================================
component Telecoms Engineering Expertise [0.32, 0.45]
component Regulatory Expertise [0.30, 0.60]
component Cryptographic Expertise [0.28, 0.38]

// ===========================================================
// Underlying reality — supply chains, compute, power, space, geography
// ===========================================================
component Geography [0.08, 0.95]
component Physical Supply Chains [0.26, 0.48]
component Information Supply Chains [0.24, 0.45]
component Semiconductor Fabrication [0.22, 0.55]
component Rare Earths and Critical Minerals [0.15, 0.60]
component Compute [0.23, 0.88]
component Power Grid [0.10, 0.92]
component Orbital Slots and Space [0.18, 0.48]

// ===========================================================
// Notes
// ===========================================================
note Sovereign-controllable zone [0.50, 0.18]
note Foreign-actor dependency [0.25, 0.80]
note Stage IV utilities [0.12, 0.97]

// ===========================================================
// Dependencies — Government anchor
// ===========================================================
Government->Territorial Sovereignty
Government->Political Sovereignty
Government->Digital Sovereignty
Government->CNI Protection
Government->Awareness of Land-Sea-Air-Space
Government->Supply Chain Awareness
Government->Cyber Situational Awareness
Government->Spectrum Allocation
Government->Geofencing and Lawful Intercept
Government->Nation-State Firewall and DPI

// The Collective anchor
The Collective->Cultural Sovereignty
The Collective->Political Sovereignty
The Collective->Radio and TV Receivers
The Collective->DNS Resolution

// Corporations anchor
Corporations->Economic Sovereignty
Corporations->CNI Protection
Corporations->Computers
Corporations->IoT Devices
Corporations->Fixed Cable Access
Corporations->International Peering

// People anchor
People->Smartphones
People->Computers
People->Radio and TV Receivers
People->Sat Phones
People->Cultural Sovereignty

// Sovereignty pillars → enabling layers
Territorial Sovereignty->Awareness of Land-Sea-Air-Space
Territorial Sovereignty->Subsea Cable Landings
Political Sovereignty->Nation-State Firewall and DPI
Political Sovereignty->Geofencing and Lawful Intercept
Cultural Sovereignty->DNS Resolution
Cultural Sovereignty->Radio and TV Receivers
Economic Sovereignty->International Peering
Economic Sovereignty->Physical Supply Chains
Digital Sovereignty->DNS Resolution
Digital Sovereignty->SIM and eSIM Identity
Digital Sovereignty->Nation-State Firewall and DPI
Digital Sovereignty->Cryptographic Expertise
CNI Protection->Mobile Network Core
CNI Protection->Fixed Network Topology
CNI Protection->Power Grid
CNI Protection->Cyber Situational Awareness

// Devices → networks
Smartphones->Mobile Towers and RAN
Smartphones->SIM and eSIM Identity
Computers->Fixed Cable Access
Computers->DNS Resolution
Radio and TV Receivers->Spectrum Allocation
Sat Phones->Satellite Access
IoT Devices->Mobile Towers and RAN
IoT Devices->SIM and eSIM Identity

// Access networks → network equipment and topology
Mobile Towers and RAN->Mobile Network Core
Mobile Towers and RAN->Network Equipment Vendors
Mobile Towers and RAN->Spectrum Allocation
Fixed Cable Access->Fixed Network Topology
Fixed Cable Access->Subsea Cable Landings
Satellite Access->Orbital Slots and Space
Satellite Access->Launch Vehicles
Launch Vehicles->Physical Supply Chains

// Network cores and topology
Mobile Network Core->Network Equipment Vendors
Fixed Network Topology->Network Equipment Vendors
Fixed Network Topology->International Peering
Subsea Cable Landings->Geography
International Peering->Subsea Cable Landings

// Control layer
SIM and eSIM Identity->Mobile Network Core
SIM and eSIM Identity->Semiconductor Fabrication
Nation-State Firewall and DPI->Network Equipment Vendors
Nation-State Firewall and DPI->Telecoms Engineering Expertise
DNS Resolution->Information Supply Chains
DNS over HTTPS->DNS Resolution
Geofencing and Lawful Intercept->Mobile Network Core
Geofencing and Lawful Intercept->Regulatory Expertise
Spectrum Allocation->Regulatory Expertise

// Theatre / awareness
Awareness of Land-Sea-Air-Space->Orbital Slots and Space
Supply Chain Awareness->Physical Supply Chains
Supply Chain Awareness->Information Supply Chains
Cyber Situational Awareness->Compute

// Network equipment depends on deep supply chains
Network Equipment Vendors->Semiconductor Fabrication
Network Equipment Vendors->Physical Supply Chains
Network Equipment Vendors->Telecoms Engineering Expertise

// Deep reality
Semiconductor Fabrication->Rare Earths and Critical Minerals
Semiconductor Fabrication->Power Grid
Compute->Power Grid
Compute->Semiconductor Fabrication
Orbital Slots and Space->Geography
Physical Supply Chains->Geography
Information Supply Chains->Compute
Rare Earths and Critical Minerals->Geography

// Evolution targets — strategic scenarios
evolve Nation-State Firewall and DPI 0.80
evolve DNS over HTTPS 0.88
evolve Satellite Access 0.75
evolve SIM and eSIM Identity 0.82
```

Validator status (manual walk-through of all 86 edges against parsed ν coordinates): 4 anchors + 43 components + 86 dependency edges — every edge satisfies ν(src) ≥ ν(tgt); all coordinates in [0, 1]; every edge endpoint declared. Node runtime was unavailable to execute `validate_owm.mjs` in this sandbox, so the validation was performed by hand against the script's exact predicates.

---

## Reading the map

The **sovereign-controllable zone** lies on the left (Genesis / Custom Built, ε < 0.5): spectrum allocation, theatre awareness, engineering expertise, regulatory expertise, geofencing/lawful intercept, launch vehicles. These are where a nation-state retains real policy latitude in October 2022.

The **foreign-actor dependency zone** lies on the top-right (high ν, high ε): smartphones, computers, radio/TV receivers, DNS, DoH, fixed cable. The citizen-visible stack is mature, commoditised, and overwhelmingly produced by a small set of non-domestic suppliers.

Between them sits the **network infrastructure middle layer** — mobile cores, RAN, fixed topology, network equipment vendors (Ericsson/Nokia/Huawei/ZTE), subsea landings. These are Product (+rental), and the vendor concentration is the single biggest sovereignty variable on the map.

---

## a. Differentiation opportunities (top 3)

Rank by `D(v) = ν(v) · (1 − ε(v))` — visible plus still uncharted:

1. **Theatre and Awareness layer** (Custom Built) — Awareness of Land-Sea-Air-Space, Supply Chain Awareness, Cyber Situational Awareness. These sit high on the map (ν 0.66–0.70) and low on evolution (ε 0.26–0.40) because the fused, multi-domain picture of who is in your territory, cables, and spectrum is not a product you can buy. Every nation-state builds some version of it in-house; mastery here is the defining sovereign capability.
2. **Digital Sovereignty pillar** (Custom Built) — a policy doctrine that is still being written in 2022. Germany's Gaia-X, France's "cloud de confiance", the EU Cyber Resilience Act proposal (September 2022) are all Stage II experiments. Nation-states that articulate a coherent digital-sovereignty posture in this window shape the rules later adopted by others.
3. **Nation-State Firewall and DPI** (late Product, moving) — paradoxically this is both a differentiation opportunity (for states willing to build one) and a foreign-sourced product (most buyers use Huawei/ZTE/Geedge hardware). For a mid-size state, the differentiation is not in the boxes but in the policy logic, taxonomy, and operations layered on top.

## b. Commodity-leverage candidates (top 3)

Rank by `K(v) = (1 − ν(v)) · ε(v)` — deep and mature, rent don't build:

1. **Power Grid** (Commodity +utility) — the cheapest component on the map to treat as a commodity. Domestic utility; don't over-engineer.
2. **Compute** (Commodity +utility) — hyperscale cloud is the utility layer; sovereign compute is a legitimate pillar but for most workloads the sovereign question is *where* it runs and *under whose law*, not whether to build a domestic AWS.
3. **DNS Resolution / DNS over HTTPS** (Commodity +utility) — RFC 8484 (2018) is settled; DoH is default-on in Firefox/Chrome since 2020 and in Android 11+ (2022). A sovereign operator should run national resolvers and consider national DoH endpoints rather than reinvent the protocol.

## c. Dependency risks (top 3)

Rank by `R(a, b) = ν(a) · (1 − ε(b))` — visible component hanging on a fragile foundation:

1. **CNI Protection → Mobile Network Core → Network Equipment Vendors → Semiconductor Fabrication**. The user-visible "protect critical national infrastructure" promise chains down to a semiconductor supply base (TSMC, Samsung, Intel) concentrated in a handful of fabs. October 2022 is the moment the US CHIPS Act (August 2022) and the first US export controls on advanced-node equipment to China (7 October 2022) explicitly weaponise this dependency.
2. **Satellite Access → Launch Vehicles → Physical Supply Chains**. Satellite access is a Product (+rental) but the capability to *place* satellites in orbit — launch vehicles — is Custom Built for most states. With Soyuz commercial access effectively ended by February 2022 sanctions and the SpaceX Falcon 9 Transporter rideshare programme dominating affordable LEO access, sovereign launch is thinner than it looks.
3. **Digital Sovereignty → SIM and eSIM Identity → Semiconductor Fabrication**. SIM cards are mostly produced by four vendors (Thales/Gemalto, IDEMIA, Giesecke+Devrient, Eastcompeace) and eSIM provisioning is tied to the GSMA root-of-trust. The identity anchor of the entire mobile network is a foreign-controlled cryptographic supply chain.

## d. Suggested gameplays

From the 61-play catalogue:

- **#18 Industrial Policy** on Semiconductor Fabrication, Network Equipment Vendors, and Launch Vehicles — the single biggest lever. CHIPS Act, EU Chips Act, and 2022's export-control regime are all instances of this play.
- **#41 Alliances** on Subsea Cable Landings and International Peering — no nation-state can own the whole physical internet, but a coordinated bloc (QUAD, Five Eyes, EU) can jointly govern landings, peering, and reserve capacity.
- **#30 Standards game** on DNS / DoH and Spectrum Allocation — sovereignty expressed through standards participation (IETF, ITU, 3GPP) costs less than sovereignty expressed through domestic product lines and compounds faster.
- **#43 Sensing Engines (ILC)** on the Theatre / Awareness layer — treat multi-domain awareness as a sensing ecosystem: fund research (Innovate), contract a few integrators (Leverage), commoditise the telemetry feeds (Commoditise). This is the intended growth path for the differentiation opportunity (a).
- **#15 Open Approaches** on SIM/eSIM and Cryptographic Expertise — the openRAN movement and open-source cryptographic hardware (OpenTitan) are the counter-play to foreign dominance in the control layer. Accept that full domestic production is uneconomic; push the commodity layer down so it is at least inspectable.
- **#56 First mover** on Digital Sovereignty doctrine — the state that writes the first coherent policy framework (covering data residency, cloud certification, DNS, CBDC-ready identity) sets the template others follow.
- **#36 Directed investment** on Launch Vehicles and Semiconductor Fabrication — but only for states large enough to sustain it; for everyone else the play is Alliances (#41) into a larger industrial bloc.

## e. Doctrine notes

Checked against Wardley's 40 principles:

- Ok on **#1 Focus on user needs** — the four anchors (Government, Collective, Corporations, People) make the user-need layer explicit rather than collapsing them into a single abstract "society". The four pillars visible at the top (Territorial / Political / Cultural / Economic / Digital / CNI) are the actual policy outcomes each user type wants.
- Ok on **#10 Know your users** — multi-anchor treatment is the correct response when the Collective's interest (cultural sovereignty) can diverge from the Government's interest (political sovereignty) and from Corporations' interest (economic sovereignty).
- Warning on **#13 Manage inertia** — the map does not explicitly mark inertia, but several obvious cases apply: Radio/TV Receivers (consumer-sunk-cost and regulatory capture around existing broadcasters), SIM and eSIM Identity (carrier lock-in, GSMA governance), and the four-vendor RAN market (foreign vendor relationships accumulated over 15–20 years). Each is a form from the 17-form taxonomy that would slow any sovereignty play that ignores it.
- Warning on **#2 Use a systematic mechanism of learning** — the Theatre / Awareness layer is where this principle lives, and the map treats it as a single component. A mature national posture would decompose awareness into OSINT, SIGINT, MASINT, IMINT and a fusion layer — but that decomposition is out of scope for a strategic map and belongs in a supporting doctrine document.
- Warning on **#17 Provide purpose, strategy and constraints** — the sovereignty pillars are pitched as outcomes, not constraints; a real national strategy document would bind them (e.g. "no foreign-owned subsea landing on the critical coast" is a constraint, not a pillar).

## f. Climatic context

From the 27 patterns, the ones actively shaping this map:

- **#3 Everything evolves** — nothing on the map is stationary. Satellite Access is mid-transition from Product to Commodity because of Starlink's LEO buildout. The control layer is moving right (DoH was Custom in 2018, Commodity by 2022). Sovereignty strategy is always strategy against a moving target.
- **#15 Inertia of expertise** and **#17 Co-evolution of practice and activity** — telecoms-engineering expertise evolves with equipment; the vendor-concentration risk (Huawei, Ericsson, Nokia, Samsung, ZTE) is compounded by every country's engineering pipeline being trained on those vendors' stacks.
- **#27 Punctuated equilibrium (war)** — Product-to-Commodity transitions drive strategic wars. DNS → DoH → Oblivious DoH is one such war. OpenRAN vs. integrated 5G RAN is another. Whoever wins each war sets the sovereign interface for the next decade.
- **#8 Higher-order systems create new sources of worth** — Digital Sovereignty, as a policy-layer component, only exists because the underlying telecoms stack became a commodity. The policy layer is worth more than the boxes once the boxes commoditise.
- **#18 You cannot measure evolution over time or adoption** — this map is a snapshot for October 2022; three months either side (CHIPS Act signing in August, Oct 7 export controls, Starlink's Ukraine activation in February) would produce a materially different placement for several components.

## g. Deep-placement notes

Four targeted searches were performed for components where the cheat-sheet placement would have been too soft:

1. **Nation-State Firewall and DPI.** Cheat-sheet first pass put this at ε ≈ 0.55 (mid-Product). Deep search confirmed commoditisation of DPI hardware — the Great Firewall's Geedge DPI infrastructure has been exported to Pakistan, Ethiopia, and Kazakhstan, and Huawei/ZTE supply the underlying hardware globally. Shifted to **ε = 0.68** (late Product, moving to Commodity (+utility)). The `evolve` target of 0.80 reflects the trajectory visible in 2022.
2. **DNS over HTTPS.** Initial placement around ε = 0.55 (Product). RFC 8484 was standardised in 2018; Firefox default-on in 2020; Chrome default-on in May 2020; Android 11+ support with July 2022 updates; RFC 9230 (Oblivious DoH) in June 2022. This is unambiguously a Commodity (+utility) protocol by October 2022. Shifted to **ε = 0.78**. The `evolve` target of 0.88 covers ongoing ODoH rollout.
3. **Launch Vehicles.** From a market perspective, SpaceX Falcon 9 (Transporter rideshare regular cadence from 2021) has made rideshare access to LEO a Product, ε ≈ 0.55. But from a *sovereign* perspective — the perspective of the scenario — only the US and China have sovereign heavy-lift access in October 2022; everyone else rents. Soyuz commercial access effectively ended in February 2022. Chose **ε = 0.40** (late Custom Built) to reflect the sovereignty frame, not the general market. This is the placement that shifts most under POV; a market-analyst map would put it at ε = 0.6.
4. **Satellite Phones.** The market is oligopolistic (Iridium, Inmarsat, Thuraya, Globalstar, China Telecom), dominated by a few providers, with established military/government usage and the Iridium NEXT constellation complete since 2019. Placed at **ε = 0.65** — solidly Product (+rental), with room to move toward Commodity via LEO direct-to-device integration (early 2022 Iridium+Qualcomm announcement was the first signal).

## h. Caveat

Every evolution position, and especially the `evolve` arrows for Nation-State Firewall and DPI, DoH, Satellite Access, and SIM/eSIM Identity, are **scenarios, not forecasts**. Wardley's climatic pattern #18: *you cannot measure evolution over time or adoption.* The map is an October 2022 snapshot; a Russia-Ukraine escalation, a Taiwan Strait incident, a major subsea cable cut, or a Starlink-scale LEO incumbent emerging would each re-place several components non-trivially.

The four-anchor structure is the most important modelling choice here: treating "citizens" and "Government" as one anchor (the usual simplification) collapses the political-sovereignty conflict that this map is designed to surface. The Collective's interest in cultural sovereignty and the Government's interest in political sovereignty can and do diverge — the map holds that tension explicitly.
