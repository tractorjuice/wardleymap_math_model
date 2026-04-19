# Wardley Map — Telecoms Sovereignty (October 2022)

**Scenario.** Map the landscape of telecoms sovereignty — a nation's ability to control its own telecommunications infrastructure. October 2022 context: UK Telecommunications (Security) Act 2021 in force with Oct 2022 legal notices naming Huawei; Nord Stream 1 & 2 sabotage in the Baltic (Sep 2022) sharpening subsea-cable concerns; Starlink deployed operationally in Ukraine; first commercial OpenRAN deployments (Rakuten Japan, Dish US, Vodafone Germany); 5G Standalone Core past early-adopter (~29 CSPs live); US CHIPS and Science Act and EU Chips Act just signed.

**Anchors.** Three — reflecting the three user types a sovereignty discussion actually serves: the nation-state (security and control), citizens (day-to-day connectivity), and businesses (enterprise connectivity). Doctrine #10 ("Know your users") fails if you collapse these to one.

---

## Map (OWM)

```owm
title Telecoms Sovereignty (October 2022)
style wardley

// Anchors — a nation's interests in its telecoms estate
anchor Nation-State (National Security) [0.99, 0.40]
anchor Citizen Connectivity [0.97, 0.70]
anchor Business / Enterprise Connectivity [0.95, 0.65]

// --- User-facing services ---
component Mobile Voice & Data Service [0.88, 0.85]
component Wi-Fi / Enterprise LAN [0.87, 0.90]
component Fixed Broadband Service [0.86, 0.82]
component Emergency Services Network (999/112) [0.82, 0.55]
component Government Secure Comms [0.80, 0.35]
component Roaming / International Calling [0.78, 0.90]

// --- Access networks ---
component Mobile Access Network (4G/5G RAN) [0.72, 0.62]
component Fixed Access Network (FTTP / Copper) [0.70, 0.72]
component LEO Satellite Broadband [0.68, 0.55]
component GEO Satellite Services [0.66, 0.80]

// --- Spectrum (an input to access networks) ---
component Licensed Spectrum Holdings [0.63, 0.55]
component Spectrum Allocation & Auctions [0.60, 0.60]
component Spectrum Management & Monitoring [0.57, 0.65]

// --- Resilience / operational practices (sit above the core they protect) ---
component CNI Designation & Protection [0.65, 0.40]
component Network Redundancy & Route Diversity [0.62, 0.68]
component Subsea Cable Protection [0.58, 0.25]

// --- Security / interception capabilities (state-level, mid-chain) ---
component Lawful Interception Capability [0.55, 0.62]
component SIGINT / National Signals Capability [0.53, 0.30]
component Network Security Monitoring (Telco SOC) [0.51, 0.55]
component Supply Chain Assurance (TSR / NCSC) [0.49, 0.35]

// --- Regulation / policy framework ---
component National Telecoms Regulator (Ofcom) [0.54, 0.80]
component Telecoms Security Act / NIS Regime [0.48, 0.55]
component Lawful Interception Mandate [0.47, 0.70]
component High Risk Vendor Controls [0.46, 0.55]
component Competition / Market Regulation [0.44, 0.78]
component Cross-border Data Transfer Rules [0.42, 0.62]

// --- Core networks & transit ---
component 5G Standalone Core [0.45, 0.60]
component IP/MPLS Core Transit [0.42, 0.82]
component International Data Routing (BGP/peering) [0.39, 0.80]
component Optical Transport (DWDM) [0.36, 0.85]
component Internet Exchange Points (IXPs) [0.34, 0.80]
component Submarine Cable Landings [0.32, 0.70]

// --- Equipment & supply chain ---
component RAN Equipment (Ericsson/Nokia/Samsung) [0.30, 0.68]
component OpenRAN Equipment [0.28, 0.38]
component Core Network Equipment [0.26, 0.65]
component Optical / Transport Equipment [0.24, 0.82]
component Handsets / Devices [0.22, 0.92]
component Advanced Semiconductors (3nm–5nm) [0.14, 0.60]
component Trusted Fabrication (sovereign fabs) [0.08, 0.18]

// --- Foundational utilities & knowledge ---
component Encryption Standards [0.18, 0.90]
component Backup Power / Standby Generation [0.16, 0.92]
component Sovereign Telecoms Workforce [0.12, 0.45]
component Network Engineering Knowledge [0.10, 0.85]
component 3GPP / IETF Standards Bodies [0.08, 0.88]

// --- Dependencies (edges) ---
// Nation-State priorities
Nation-State (National Security)->Government Secure Comms
Nation-State (National Security)->Emergency Services Network (999/112)
Nation-State (National Security)->CNI Designation & Protection
Nation-State (National Security)->National Telecoms Regulator (Ofcom)
Nation-State (National Security)->SIGINT / National Signals Capability
Nation-State (National Security)->Lawful Interception Capability
Nation-State (National Security)->Supply Chain Assurance (TSR / NCSC)

// Citizen & business priorities
Citizen Connectivity->Mobile Voice & Data Service
Citizen Connectivity->Fixed Broadband Service
Citizen Connectivity->Emergency Services Network (999/112)
Citizen Connectivity->Roaming / International Calling
Business / Enterprise Connectivity->Mobile Voice & Data Service
Business / Enterprise Connectivity->Fixed Broadband Service
Business / Enterprise Connectivity->Wi-Fi / Enterprise LAN
Business / Enterprise Connectivity->LEO Satellite Broadband
Business / Enterprise Connectivity->GEO Satellite Services

// User-facing services -> access networks
Mobile Voice & Data Service->Mobile Access Network (4G/5G RAN)
Fixed Broadband Service->Fixed Access Network (FTTP / Copper)
Emergency Services Network (999/112)->Mobile Access Network (4G/5G RAN)
Emergency Services Network (999/112)->Network Redundancy & Route Diversity
Government Secure Comms->Encryption Standards
Government Secure Comms->Network Redundancy & Route Diversity
Roaming / International Calling->Mobile Access Network (4G/5G RAN)
Roaming / International Calling->International Data Routing (BGP/peering)
Wi-Fi / Enterprise LAN->Fixed Broadband Service

// Access -> core / equipment / spectrum
Mobile Access Network (4G/5G RAN)->5G Standalone Core
Mobile Access Network (4G/5G RAN)->RAN Equipment (Ericsson/Nokia/Samsung)
Mobile Access Network (4G/5G RAN)->OpenRAN Equipment
Mobile Access Network (4G/5G RAN)->Licensed Spectrum Holdings
Fixed Access Network (FTTP / Copper)->Optical Transport (DWDM)
Fixed Access Network (FTTP / Copper)->Optical / Transport Equipment
LEO Satellite Broadband->Licensed Spectrum Holdings
GEO Satellite Services->Licensed Spectrum Holdings

// Resilience practices -> the things they protect
Network Redundancy & Route Diversity->IP/MPLS Core Transit
Network Redundancy & Route Diversity->Submarine Cable Landings
CNI Designation & Protection->Subsea Cable Protection
CNI Designation & Protection->Network Redundancy & Route Diversity
CNI Designation & Protection->Backup Power / Standby Generation
Subsea Cable Protection->Submarine Cable Landings

// Core -> transit/transport
5G Standalone Core->IP/MPLS Core Transit
5G Standalone Core->Core Network Equipment
IP/MPLS Core Transit->International Data Routing (BGP/peering)
IP/MPLS Core Transit->Optical Transport (DWDM)
IP/MPLS Core Transit->Internet Exchange Points (IXPs)
International Data Routing (BGP/peering)->Internet Exchange Points (IXPs)
International Data Routing (BGP/peering)->Submarine Cable Landings
Optical Transport (DWDM)->Submarine Cable Landings
Optical Transport (DWDM)->Optical / Transport Equipment

// Equipment -> semiconductors
RAN Equipment (Ericsson/Nokia/Samsung)->Advanced Semiconductors (3nm–5nm)
OpenRAN Equipment->Advanced Semiconductors (3nm–5nm)
Core Network Equipment->Advanced Semiconductors (3nm–5nm)
Optical / Transport Equipment->Advanced Semiconductors (3nm–5nm)
Handsets / Devices->Advanced Semiconductors (3nm–5nm)
Advanced Semiconductors (3nm–5nm)->Trusted Fabrication (sovereign fabs)

// Spectrum pipeline (allocation is the process delivered by the regulator)
Licensed Spectrum Holdings->Spectrum Allocation & Auctions
Spectrum Allocation & Auctions->Spectrum Management & Monitoring
Spectrum Allocation & Auctions->National Telecoms Regulator (Ofcom)
Spectrum Management & Monitoring->National Telecoms Regulator (Ofcom)

// Regulation framework (deeper than the capabilities it mandates)
National Telecoms Regulator (Ofcom)->Telecoms Security Act / NIS Regime
National Telecoms Regulator (Ofcom)->Competition / Market Regulation
Telecoms Security Act / NIS Regime->High Risk Vendor Controls
Telecoms Security Act / NIS Regime->Cross-border Data Transfer Rules
Lawful Interception Capability->Lawful Interception Mandate

// Security/interception -> foundations
Lawful Interception Capability->Network Security Monitoring (Telco SOC)
Lawful Interception Capability->IP/MPLS Core Transit
SIGINT / National Signals Capability->Submarine Cable Landings
SIGINT / National Signals Capability->International Data Routing (BGP/peering)
Network Security Monitoring (Telco SOC)->Encryption Standards
Supply Chain Assurance (TSR / NCSC)->High Risk Vendor Controls
Supply Chain Assurance (TSR / NCSC)->Sovereign Telecoms Workforce

// Equipment -> knowledge / workforce / standards
RAN Equipment (Ericsson/Nokia/Samsung)->3GPP / IETF Standards Bodies
5G Standalone Core->3GPP / IETF Standards Bodies
OpenRAN Equipment->3GPP / IETF Standards Bodies
Core Network Equipment->3GPP / IETF Standards Bodies
Mobile Access Network (4G/5G RAN)->Sovereign Telecoms Workforce
Sovereign Telecoms Workforce->Network Engineering Knowledge
Network Engineering Knowledge->3GPP / IETF Standards Bodies

// Evolve signals (scenarios, not forecasts)
evolve OpenRAN Equipment 0.62
evolve LEO Satellite Broadband 0.75
evolve 5G Standalone Core 0.80
evolve High Risk Vendor Controls 0.72
evolve Trusted Fabrication (sovereign fabs) 0.35
evolve Subsea Cable Protection 0.45

note Sovereign moat zone [0.55, 0.18]
note Commodity utilities [0.20, 0.90]
note Regulatory industrialisation [0.45, 0.60]
```

**Validator:** `OK: 47 components/anchors, 77 edges — no violations.`

---

## What is differentiating vs commoditising? (the scenario's core question)

The clearest reading of this map is that **most of the stack is commoditising while most of the sovereign-control levers are not**. That is the strategic tension of telecoms sovereignty in 2022:

| Differentiating (left-of-map, state-controlled) | Commoditising (right-of-map, market-controlled) |
|---|---|
| SIGINT / National Signals Capability (Custom Built) | Mobile Voice & Data Service (Commodity +utility) |
| Subsea Cable Protection (Genesis → Custom Built) | Fixed Broadband Service (Commodity +utility) |
| Government Secure Comms (Custom Built) | International Data Routing via BGP (Commodity +utility) |
| Supply Chain Assurance (Custom Built) | RAN Equipment — Ericsson/Nokia/Samsung (Product +rental) |
| CNI Designation & Protection (Custom Built) | 5G Standalone Core (Product +rental, consolidating) |
| Trusted Fabrication (Genesis) | LEO Satellite Broadband (early Product +rental) |
| OpenRAN Equipment (Custom Built → Product transition) | Handsets / Devices (Commodity +utility) |
| High Risk Vendor Controls (transitioning into Product +rental) | Advanced Semiconductors (3nm–5nm) (Product +rental) |

The *connectivity* a citizen experiences is deeply commoditised. The *control* a state wants over that connectivity — who makes the kit, where the cables land, who can listen in, who gets cut off in a crisis — is still largely Custom Built or even Genesis, and is exactly where the 2022 sovereignty agenda is being fought.

---

## a. Differentiation opportunities (top 3)

1. **Government Secure Comms** (Custom Built) — the highest-D component in the map by a wide margin. User-facing for the state, deliberately held left of the evolution axis. This is *Custom Built on purpose*: commoditising it would destroy the property the state wants (exclusive control). Invest in indigenous PQC-ready crypto stacks and a sovereign Secure Comms platform.
2. **Subsea Cable Protection** (Genesis → Custom Built) — post-Nord Stream, this is a state-level differentiator with no mature doctrine. First-movers (UK, Norway, Japan) who build monitoring-and-response capability will define the category. Highest dependency-risk score in the map (see section c).
3. **CNI Designation & Protection** (Custom Built) — the institutional practice of which infra counts as critical and what the state is obliged to do about it. Still jurisdictionally bespoke (NIS2 in EU, TSR/TSA in UK, CISA in US). A state that articulates the sharpest doctrine here gains influence over allied regimes.

Honourable mentions: **Emergency Services Network** (D high because user-visible and still Custom Built for next-gen 4G/5G handover); **SIGINT** (the ultimate sovereign capability, deeply Custom Built).

## b. Commodity-leverage candidates (top 3)

Where to *stop* trying to build sovereign versions and just accept the utility:

1. **3GPP / IETF Standards Bodies** (Commodity +utility) — knowledge-layer; participate, don't fork. The worst sovereignty move is a state-specific protocol stack.
2. **Backup Power / Standby Generation** (Commodity +utility) — utility. Don't confuse "sovereign fuel" with "sovereign generator kit" — the latter is a commodity.
3. **Encryption Standards** (Commodity +utility — for the public algorithms, AES/TLS/post-quantum candidates) — accept the NIST/IETF public stack. Sovereign additions layer *on top*, not replace.

Close runners: **Handsets / Devices**, **Optical / Transport Equipment**. These are commodity markets with many vendors; state intervention there is usually a policy mistake (re-running 1970s telecoms national-champion playbooks on markets that don't reward them).

## c. Dependency risks (top 3)

Edges where a visible-to-state component rides on an immature foundation:

1. **Nation-State → Subsea Cable Protection** — the most visible sovereign dependency in the map rides on a Genesis-stage capability. Nord Stream (Sep 2022) and the Svalbard cable cut (early 2022) showed the foundation is not ready; the state's dependency is enormous.
2. **Nation-State → SIGINT / National Signals Capability** — SIGINT is deeply Custom Built and nation-specific. It works, but any shift in the underlying transit (end-to-end encrypted traffic, LEO routing that bypasses landings) erodes it fast. Climatic pattern #3 (everything evolves) is pressing on it.
3. **Nation-State → Supply Chain Assurance (TSR / NCSC)** — the UK created a formal regime only in 2021–22 and it is still Custom Built. As HRV designations multiply (Huawei → potentially others), the assurance capability itself needs to industrialise, or it becomes the choke point.

Secondary: **Mobile Access Network → OpenRAN Equipment** — a major sovereignty bet (diversify away from Huawei/ZTE/Ericsson/Nokia duopoly-plus) rests on tech that is only just Custom Built transitioning to Product (+rental); real-world performance in dense urban 5G is still being proven. **Equipment makers → Trusted Fabrication (sovereign fabs)** — every piece of telecoms kit on the map depends on a 3-firm bottleneck (TSMC/Samsung/Intel) at leading nodes, and sovereign fabs are Genesis.

## d. Suggested gameplays

Named from Wardley's 61-play catalogue:

- **#36 Directed investment** on **OpenRAN Equipment** and **Trusted Fabrication (sovereign fabs)** — two Custom/Genesis components the state can accelerate with capital (UK's Open RAN adoption strategy, US/EU CHIPS Acts). Directed investment is explicit sovereignty capex.
- **#15 Open Approaches** on **OpenRAN Equipment** — the defining 2022 play. Open interfaces (O-RAN Alliance specs) accelerate the transition out of the Huawei/Ericsson/Nokia triopoly and lower the barrier for sovereign vendors. Pair with #36.
- **#41 Alliances** on **Submarine Cable Protection** and **Supply Chain Assurance** — no single nation can police its own cables or audit every vendor in isolation. Five Eyes + AUKUS + EU structured alliances turn a Custom-Built capability into a shared Product (+rental). (NATO's Undersea Infrastructure Coordination Cell followed shortly after this map's date.)
- **#30 Standards game** on **High Risk Vendor Controls** — 2022 is the inflection where Huawei bans moved from unilateral (US, AU) to coordinated (UK TSA, EU toolbox, Germany lagging). A state that shapes the coordinated vocabulary — what counts as "high-risk", what counts as "remediation" — writes the rules for the next decade.
- **#35 Defensive regulation** on **Cross-border Data Transfer Rules** — GDPR-Schrems era; a state can use data-transfer law as a sovereignty lever over providers. Use with care; can backfire into isolation.
- **#29 Harvesting** on **LEO Satellite Broadband** — Starlink and OneWeb have done the heavy lifting. For most states, harvest (contract capacity) rather than build; only the largest (US, China, EU via IRIS²) can realistically build.
- **#20 Patents & IPR** — noted for completeness: the RAN equipment IPR stack (Ericsson, Nokia, Qualcomm) is a de-facto sovereignty constraint. A state cannot ignore it but also cannot easily attack it.
- **#43 Sensing Engines (ILC)** on **LEO Satellite Broadband** — by late 2022 the shape of LEO constellations (Starlink, OneWeb, Kuiper, IRIS²) is still forming; sense which geometry wins before betting regulation.

## e. Doctrine notes

- ✓ **#1 Focus on user needs** — map correctly distinguishes three user types. A single "citizen" anchor would collapse the nation-state's interest into the consumer's, which is the single most common error in telecoms-sovereignty discussions.
- ✓ **#10 Know your users** — three anchors represent the three real constituencies.
- ⚠ **#13 Manage inertia** — several structural inertias apply (see section f). The state's own inertia on HRV removal (BT asked for an extension in Oct 2022) is a classic example — #2 sunk capital (Huawei kit already paid for), #9 re-architecture cost.
- ⚠ **#22 Use standards where appropriate** — partial violation risk on the **Encryption Standards** and **3GPP / IETF Standards Bodies** edges. Sovereign encryption stacks (e.g., BSI VS-NfD, GCHQ's own suite) are legitimate at the top but should NOT replace the commodity underpinning.
- ⚠ **#38 There is no core** — any claim that "the RAN is the core" or "the fabs are the core" is wrong. Every sovereignty component here has an evolutionary trajectory.
- ⚠ **#28 Seek the best** — the regulatory capability layer (Ofcom, TSA, Lawful Interception Mandate) is competing with the pace of private-sector evolution; it needs to run on best-available practice, not legacy procedures.

## f. Climatic context

Which of Wardley's 27 climatic patterns are actively shaping this map in Oct 2022:

- **#3 Everything evolves through supply and demand competition** — applies to the whole right-hand block. Mobile voice, fixed broadband, RAN, handsets are all commoditising regardless of sovereignty preferences.
- **#5 No choice over evolution** — a state cannot "opt out" of 5G or of LEO; the only choice is how to respond (buy, build, regulate, prohibit).
- **#15–17 Inertia** — the Huawei removal timeline is a textbook case of inertia: operators have sunk capital (#15), re-architecture cost (inertia form #9), and strategic-control loss fears (form #14). October 2022 is precisely the month the UK government exercised legal notices to override that inertia. Left unmanaged, inertia can kill (#17); here it is being actively managed.
- **#18 You cannot measure evolution over time or adoption** — every `evolve` arrow is a scenario. The Huawei-to-2027 timeline is a political target, not a forecast.
- **#21 Peace/War/Wonder cycles** — telecoms in 2022 sits in **War** phase on several components simultaneously: RAN (industrialisation via OpenRAN), Satellite broadband (LEO industrialisation), Supply-chain vetting (regulation industrialising). This is why it feels turbulent.
- **#22 Two forms of disruption** — LEO broadband is Genesis-driven disruption (Starlink); OpenRAN is product-to-utility disruption of the RAN market. Different plays fit each.
- **#23 A "war" causes organisations to evolve** — expect M&A in RAN (confirmed later: Nokia/Mavenir/Viavi moves), consolidation in 5G core vendors, and state-level Org changes (NCSC/CISA growth).
- **#27 Product-to-utility punctuated equilibrium** — LEO broadband and 5G Core are in this phase. Expect rapid destruction of GEO-only models and of Non-Standalone 5G Core. Act fast or lose the window.

## g. Deep-placement notes

Four components were researched beyond the cheat sheet because they are strategically critical and the markets were moving quickly in 2022. (Sources in final section.)

- **OpenRAN Equipment** — cheat-sheet initial score 0.30 (mid-Custom). Research showed: Rakuten Mobile 4G/5G commercial in Japan (Sep 2022); Vodafone Germany first-deployment announcement (Oct 2022); Dish Networks contracted Samsung for 20% US population coverage by Jun 2022. Multiple vendors (Mavenir, Fujitsu, NEC, Samsung) competing but no single dominant. Moved ε to **0.38** — end of Custom Built, very early Product (+rental). Confirms the "transition" flag.
- **LEO Satellite Broadband** — cheat-sheet initial 0.45. Research showed: Starlink in 40 countries by Sep 2022 with reported $1.4B revenue; OneWeb launches resumed post-Soyuz cancellation, $800M order backlog. Ubiquity is rapidly increasing; vendor count is low (Starlink, OneWeb, Kuiper in prep) which is the tell for early Stage III. Moved ε to **0.55** — mid-Product (+rental). Evolve target 0.75 reflects the expected trajectory but remains a scenario.
- **5G Standalone Core** — cheat-sheet initial 0.55. Research showed: ~29 CSPs with live deployments by end 2022; Ericsson in 34 of 60 commercial SA deployments; Nokia at 33% share; Samsung dominant in Japan (KDDI); Oracle, Cisco, HPE active. A handful of dominant vendors with widespread uptake = mid Product (+rental). Moved ε to **0.60**.
- **High Risk Vendor Controls** — cheat-sheet initial 0.40 (mid-Custom). Research showed: UK Telecommunications (Security) Act 2021 in force; Oct 2022 legal notices issued; formal designation notice for Huawei; interim deadlines Jan 2023 and Oct 2023. Moved ε to **0.55** — formal, codified, industrialising into Product (+rental). The regulatory category exists globally now (US CHIPS-sanctions nexus, EU 5G toolbox, Japan, Australia); that's a Stage III signal.

One further component (**Subsea Cable Protection**) was researched because the Nord Stream sabotage happened only three weeks before the map date. Finding: no cross-state doctrine in place in Oct 2022 (NATO's Undersea Infrastructure Coordination Cell forms Feb 2023). Confirms Genesis/early-Custom. Kept ε at **0.25**.

Other components were scored from the cheat sheet without research (obvious commodities like handsets, backup power, encryption standards; obvious sovereign-bespoke components like SIGINT and Government Secure Comms).

## h. Caveat

Evolution trajectories on this map (the six `evolve` arrows) are scenarios, not forecasts. Wardley's climatic pattern #18: *"you cannot measure evolution over time or adoption."* OpenRAN may stall if operator performance data stays mixed. LEO economics may squeeze out all but Starlink. Subsea Cable Protection may remain Custom indefinitely if alliance politics prevent a shared doctrine. Use the map to identify *where to pay attention*, not to predict *when* each component will move.

---

## Sources (for deep-placement research)

- [Huawei to be removed from UK 5G networks by 2027 — GOV.UK](https://www.gov.uk/government/news/huawei-to-be-removed-from-uk-5g-networks-by-2027)
- [UK extends deadline to remove Huawei from 5G networks — CNBC, Oct 2022](https://www.cnbc.com/2022/10/13/uk-gives-telco-firms-more-time-to-remove-huawei-5g-equipment.html)
- [UK telcos legally required to remove Huawei equipment — The Register, Oct 2022](https://www.theregister.com/2022/10/13/uk_telcos_huawei_ban)
- [Open RAN Market Size, Share, Growth, Industry Trend — MarketsandMarkets](https://www.marketsandmarkets.com/Market-Reports/open-ran-market-153445936.html)
- [Open RAN Market Update — First Point Group](https://www.firstpointgroup.com/resources/blog/open-ran-market-update/)
- [5G standalone deployment — Ericsson Mobility Report](https://www.ericsson.com/en/reports-and-papers/mobility-report/dataforecasts/5g-standalone-deployment)
- [5G Standalone deployment globally — STL Partners](https://stlpartners.com/articles/network-innovation/5g-standalone-deployment/)
- [Omdia Market Landscape for 5G Core Vendors 2022 — Oracle summary](https://www.oracle.com/communications/5g-core/omdia-market-landscape-core-vendors-2022/)
- [Eutelsat OneWeb — Wikipedia](https://en.wikipedia.org/wiki/Eutelsat_OneWeb)
- [Starlink — Wikipedia](https://en.wikipedia.org/wiki/Starlink)
- [Security Implications of Nord Stream Sabotage — CSIS](https://www.csis.org/analysis/security-implications-nord-stream-sabotage)
- [NATO: More Effort Needed to Shield Subsea Links — CEPA](https://cepa.org/article/nato-more-effort-needed-to-shield-subsea-links/)
