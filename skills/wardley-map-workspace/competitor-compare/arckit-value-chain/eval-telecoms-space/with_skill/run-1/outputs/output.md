# Space-Based Telecoms Landscape — Value Chain

## Executive Summary

**Anchor:** Consumers, Corporations, and Government need reliable network access and broadcast delivered over a physical network whose topology now includes Non-Terrestrial Networks (NTN) alongside mobile and fibre. The value chain descends from user-facing access through NTN into user terminals (with phased-array antennas), ground stations, spectrum (Ku/Ka/V bands), and the satellite itself (LEO microsats vs GEO). Beneath the satellite sit the subsystems — antennas, beamforming/beam-steering, optical inter-satellite links, propulsion (Krypton/Xenon), power, cooling (thermal-electric, radiative, cryogens), launchers, and control systems (orbit, debris, fleet management) — all underpinned by automation and supply-chain awareness. Space Regulation is modelled as a low-visibility cross-cutting constraint that Government directly touches and that Launchers, Satellite, Spectrum and Debris Tracking all depend on. Strategic insights: (1) NTN is the only new **topology option** alongside mobile/fibre and is the point where space telecoms connects to mainstream networks; (2) LEO microsats with optical sat-to-sat comms are the novel spine, while GEO, Ku/Ka spectrum, and chemical launch are comparatively mature; (3) Supply-Chain Awareness sits at the floor — the whole satellite subsystem stack funnels into it, and it is the weakest-visibility node in the chain despite being strategically critical given geopolitical fragmentation of propellant, optics, and space-grade electronics.

## Users and Personas

| User | Primary Need |
|------|--------------|
| Consumers (individuals, rural households, mobile subscribers) | Reliable broadband and broadcast anywhere, including where terrestrial networks don't reach |
| Corporations (maritime, aviation, oil & gas, enterprise WAN, IoT) | Resilient connectivity outside terrestrial coverage; low-latency global backhaul |
| Government (defence, civil, regulators) | Sovereign communications, broadcast continuity, space regulation and debris management |

## Value Chain Diagram

```text
VIS   COMPONENTS
0.95  [Consumers] [Corporations] [Government]
0.86  [Network Access] [Broadcast]
0.78  [Physical Network] [Topology]
0.70  [Mobile] [Fibre] [Non-Terrestrial Networks]
0.60  [User Terminals] [Ground Stations] [Satellite]
0.52  [Phased-Array Antennas] [Spectrum] [LEO Microsats] [GEO Satellites]
0.44  [Ku Band] [Ka Band] [V Band] [Antennas] [Control Systems] [Launchers]
0.36  [Beamforming] [Beam-Steering] [Optical Sat-to-Sat Comms] [Propulsion] [Power] [Cooling] [Fleet Mgmt] [Orbit Tracking] [Debris Tracking]
0.26  [Krypton] [Xenon] [Thermal Electric Cooling] [Radiative Cooling] [Cryogens]
0.20  [Automation] [Space Regulation]
0.14  [Supply-Chain Awareness]
```

### OWM Syntax

```owm
title Space-Based Telecoms Landscape

anchor Consumers [0.95, 0.50]
anchor Corporations [0.95, 0.50]
anchor Government [0.95, 0.50]

component Network Access [0.86, 0.50]
component Broadcast [0.84, 0.50]

component Physical Network [0.78, 0.50]
component Topology [0.76, 0.50]

component Mobile [0.70, 0.50]
component Fibre [0.68, 0.50]
component Non-Terrestrial Networks [0.70, 0.50]

component User Terminals [0.62, 0.50]
component Ground Stations [0.60, 0.50]
component Satellite [0.58, 0.50]

component Phased-Array Antennas [0.54, 0.50]
component Spectrum [0.52, 0.50]
component LEO Microsats [0.50, 0.50]
component GEO Satellites [0.50, 0.50]

component Ku Band [0.44, 0.50]
component Ka Band [0.44, 0.50]
component V Band [0.42, 0.50]

component Antennas [0.46, 0.50]
component Control Systems [0.44, 0.50]
component Launchers [0.42, 0.50]

component Beamforming [0.38, 0.50]
component Beam-Steering [0.38, 0.50]
component Optical Sat-to-Sat Comms [0.36, 0.50]

component Propulsion [0.38, 0.50]
component Power Subsystem [0.38, 0.50]
component Cooling Subsystem [0.36, 0.50]

component Fleet Management [0.36, 0.50]
component Orbit Tracking [0.34, 0.50]
component Debris Tracking [0.34, 0.50]

component Krypton Propellant [0.28, 0.50]
component Xenon Propellant [0.28, 0.50]
component Thermal Electric Cooling [0.26, 0.50]
component Radiative Cooling [0.26, 0.50]
component Cryogens [0.24, 0.50]

component Automation [0.22, 0.50]
component Space Regulation [0.20, 0.50]
component Supply-Chain Awareness [0.14, 0.50]

Consumers -> Network Access
Consumers -> Broadcast
Corporations -> Network Access
Corporations -> Broadcast
Government -> Network Access
Government -> Broadcast
Government -> Space Regulation

Network Access -> Physical Network
Network Access -> Topology
Broadcast -> Physical Network
Broadcast -> Topology

Physical Network -> User Terminals
Physical Network -> Ground Stations
Topology -> Mobile
Topology -> Fibre
Topology -> Non-Terrestrial Networks

Non-Terrestrial Networks -> Satellite
Non-Terrestrial Networks -> Ground Stations
Non-Terrestrial Networks -> User Terminals
Non-Terrestrial Networks -> Spectrum

User Terminals -> Phased-Array Antennas
Ground Stations -> Spectrum
Ground Stations -> Antennas

Spectrum -> Ku Band
Spectrum -> Ka Band
Spectrum -> V Band

Satellite -> LEO Microsats
Satellite -> GEO Satellites
Satellite -> Antennas
Satellite -> Propulsion
Satellite -> Power Subsystem
Satellite -> Cooling Subsystem
Satellite -> Control Systems
Satellite -> Launchers

LEO Microsats -> Optical Sat-to-Sat Comms
LEO Microsats -> Propulsion
GEO Satellites -> Propulsion

Antennas -> Beamforming
Antennas -> Beam-Steering
Phased-Array Antennas -> Beamforming
Phased-Array Antennas -> Beam-Steering

Propulsion -> Krypton Propellant
Propulsion -> Xenon Propellant

Cooling Subsystem -> Thermal Electric Cooling
Cooling Subsystem -> Radiative Cooling
Cooling Subsystem -> Cryogens

Control Systems -> Orbit Tracking
Control Systems -> Debris Tracking
Control Systems -> Fleet Management

Fleet Management -> Automation
Orbit Tracking -> Automation
Debris Tracking -> Automation

Launchers -> Space Regulation
Satellite -> Space Regulation
Spectrum -> Space Regulation
Debris Tracking -> Space Regulation

Launchers -> Supply-Chain Awareness
Propulsion -> Supply-Chain Awareness
Power Subsystem -> Supply-Chain Awareness
Cooling Subsystem -> Supply-Chain Awareness
Antennas -> Supply-Chain Awareness
Automation -> Supply-Chain Awareness

style wardley
```

<details>
<summary>Mermaid wardley-beta equivalent</summary>

```mermaid
wardley-beta
title Space-Based Telecoms Landscape
size [1100, 800]

anchor Consumers [0.95, 0.50]
anchor Corporations [0.95, 0.50]
anchor Government [0.95, 0.50]

component "Network Access" [0.86, 0.50]
component Broadcast [0.84, 0.50]

component "Physical Network" [0.78, 0.50]
component Topology [0.76, 0.50]

component Mobile [0.70, 0.50]
component Fibre [0.68, 0.50]
component "Non-Terrestrial Networks" [0.70, 0.50]

component "User Terminals" [0.62, 0.50]
component "Ground Stations" [0.60, 0.50]
component Satellite [0.58, 0.50]

component "Phased-Array Antennas" [0.54, 0.50]
component Spectrum [0.52, 0.50]
component "LEO Microsats" [0.50, 0.50]
component "GEO Satellites" [0.50, 0.50]

component "Ku Band" [0.44, 0.50]
component "Ka Band" [0.44, 0.50]
component "V Band" [0.42, 0.50]

component Antennas [0.46, 0.50]
component "Control Systems" [0.44, 0.50]
component Launchers [0.42, 0.50]

component Beamforming [0.38, 0.50]
component "Beam-Steering" [0.38, 0.50]
component "Optical Sat-to-Sat Comms" [0.36, 0.50]

component Propulsion [0.38, 0.50]
component "Power Subsystem" [0.38, 0.50]
component "Cooling Subsystem" [0.36, 0.50]

component "Fleet Management" [0.36, 0.50]
component "Orbit Tracking" [0.34, 0.50]
component "Debris Tracking" [0.34, 0.50]

component "Krypton Propellant" [0.28, 0.50]
component "Xenon Propellant" [0.28, 0.50]
component "Thermal Electric Cooling" [0.26, 0.50]
component "Radiative Cooling" [0.26, 0.50]
component Cryogens [0.24, 0.50]

component Automation [0.22, 0.50]
component "Space Regulation" [0.20, 0.50]
component "Supply-Chain Awareness" [0.14, 0.50]

Consumers -> "Network Access"
Consumers -> Broadcast
Corporations -> "Network Access"
Corporations -> Broadcast
Government -> "Network Access"
Government -> Broadcast
Government -> "Space Regulation"

"Network Access" -> "Physical Network"
"Network Access" -> Topology
Broadcast -> "Physical Network"
Broadcast -> Topology

"Physical Network" -> "User Terminals"
"Physical Network" -> "Ground Stations"
Topology -> Mobile
Topology -> Fibre
Topology -> "Non-Terrestrial Networks"

"Non-Terrestrial Networks" -> Satellite
"Non-Terrestrial Networks" -> "Ground Stations"
"Non-Terrestrial Networks" -> "User Terminals"
"Non-Terrestrial Networks" -> Spectrum

"User Terminals" -> "Phased-Array Antennas"
"Ground Stations" -> Spectrum
"Ground Stations" -> Antennas

Spectrum -> "Ku Band"
Spectrum -> "Ka Band"
Spectrum -> "V Band"

Satellite -> "LEO Microsats"
Satellite -> "GEO Satellites"
Satellite -> Antennas
Satellite -> Propulsion
Satellite -> "Power Subsystem"
Satellite -> "Cooling Subsystem"
Satellite -> "Control Systems"
Satellite -> Launchers

"LEO Microsats" -> "Optical Sat-to-Sat Comms"
"LEO Microsats" -> Propulsion
"GEO Satellites" -> Propulsion

Antennas -> Beamforming
Antennas -> "Beam-Steering"
"Phased-Array Antennas" -> Beamforming
"Phased-Array Antennas" -> "Beam-Steering"

Propulsion -> "Krypton Propellant"
Propulsion -> "Xenon Propellant"

"Cooling Subsystem" -> "Thermal Electric Cooling"
"Cooling Subsystem" -> "Radiative Cooling"
"Cooling Subsystem" -> Cryogens

"Control Systems" -> "Orbit Tracking"
"Control Systems" -> "Debris Tracking"
"Control Systems" -> "Fleet Management"

"Fleet Management" -> Automation
"Orbit Tracking" -> Automation
"Debris Tracking" -> Automation

Launchers -> "Space Regulation"
Satellite -> "Space Regulation"
Spectrum -> "Space Regulation"
"Debris Tracking" -> "Space Regulation"

Launchers -> "Supply-Chain Awareness"
Propulsion -> "Supply-Chain Awareness"
"Power Subsystem" -> "Supply-Chain Awareness"
"Cooling Subsystem" -> "Supply-Chain Awareness"
Antennas -> "Supply-Chain Awareness"
Automation -> "Supply-Chain Awareness"
```

</details>

## Component Inventory

| Component | Visibility | Description |
|-----------|------------|-------------|
| Consumers | 0.95 | Individuals, rural households, mobile subscribers — anchor user group |
| Corporations | 0.95 | Enterprise customers (maritime, aviation, energy, IoT, WAN) — anchor user group |
| Government | 0.95 | Defence, civil, and regulators — anchor user group and regulation consumer |
| Network Access | 0.86 | Data connectivity service experienced by users |
| Broadcast | 0.84 | One-to-many delivery (TV, radio, emergency) |
| Physical Network | 0.78 | The concrete infrastructure that carries access/broadcast |
| Topology | 0.76 | The set of delivery topologies available (mobile/fibre/NTN) |
| Mobile | 0.70 | Terrestrial cellular delivery |
| Non-Terrestrial Networks | 0.70 | Satellite-delivered access, the scenario's focus |
| Fibre | 0.68 | Wired terrestrial delivery |
| User Terminals | 0.62 | Customer-premises satellite equipment (e.g., Starlink dish class) |
| Ground Stations | 0.60 | Teleports and gateways that land signals |
| Satellite | 0.58 | The orbiting platform itself |
| Phased-Array Antennas | 0.54 | Electronically-steerable flat-panel antennas at the user terminal |
| Spectrum | 0.52 | Allocated radio-frequency bands used by the link |
| LEO Microsats | 0.50 | Low-Earth-orbit small satellites (Starlink, OneWeb class) |
| GEO Satellites | 0.50 | Geostationary-orbit satellites (classical SATCOM) |
| Antennas | 0.46 | Satellite and ground-station RF/optical antenna systems |
| Ku Band | 0.44 | 12–18 GHz satellite band — broad, mature |
| Ka Band | 0.44 | 26.5–40 GHz — higher throughput, newer |
| Control Systems | 0.44 | On-orbit and ground-based constellation control |
| Launchers | 0.42 | Launch vehicles that place satellites in orbit |
| V Band | 0.42 | 40–75 GHz — frontier, high-throughput, weather-sensitive |
| Beamforming | 0.38 | Shaping radio beams in software/hardware |
| Beam-Steering | 0.38 | Pointing beams at users/satellites dynamically |
| Propulsion | 0.38 | On-orbit station-keeping and manoeuvre |
| Power Subsystem | 0.38 | Solar arrays, batteries, power management |
| Optical Sat-to-Sat Comms | 0.36 | Laser inter-satellite links within LEO constellations |
| Cooling Subsystem | 0.36 | Thermal management of satellite electronics and optics |
| Fleet Management | 0.36 | Operating many satellites as a constellation |
| Orbit Tracking | 0.34 | Position and ephemeris of owned assets |
| Debris Tracking | 0.34 | Space situational awareness / conjunction avoidance |
| Krypton Propellant | 0.28 | Ion-thruster propellant, lower-cost Xenon alternative |
| Xenon Propellant | 0.28 | Traditional ion-thruster propellant |
| Thermal Electric Cooling | 0.26 | Peltier-based active cooling |
| Radiative Cooling | 0.26 | Passive radiator-based cooling |
| Cryogens | 0.24 | Deep cooling for sensitive payloads |
| Automation | 0.22 | Autonomous ops, collision avoidance, fleet control software |
| Space Regulation | 0.20 | ITU spectrum, licensing, debris and orbital-slot rules — cross-cutting constraint |
| Supply-Chain Awareness | 0.14 | Visibility into upstream hardware, propellants, optics, space-grade electronics |

## Dependency Matrix (summary)

Direct dependencies (X):

- Consumers, Corporations, Government -> Network Access, Broadcast
- Government -> Space Regulation (direct — regulator role)
- Network Access, Broadcast -> Physical Network, Topology
- Physical Network -> User Terminals, Ground Stations
- Topology -> Mobile, Fibre, Non-Terrestrial Networks
- NTN -> Satellite, Ground Stations, User Terminals, Spectrum
- User Terminals -> Phased-Array Antennas
- Ground Stations -> Spectrum, Antennas
- Spectrum -> Ku Band, Ka Band, V Band
- Satellite -> LEO Microsats, GEO Satellites, Antennas, Propulsion, Power, Cooling, Control Systems, Launchers
- LEO Microsats -> Optical Sat-to-Sat Comms, Propulsion
- GEO Satellites -> Propulsion
- Antennas, Phased-Array Antennas -> Beamforming, Beam-Steering
- Propulsion -> Krypton, Xenon
- Cooling -> Thermal Electric, Radiative, Cryogens
- Control Systems -> Orbit Tracking, Debris Tracking, Fleet Management
- Fleet Mgmt, Orbit Tracking, Debris Tracking -> Automation
- Launchers, Satellite, Spectrum, Debris Tracking -> Space Regulation
- Launchers, Propulsion, Power, Cooling, Antennas, Automation -> Supply-Chain Awareness

## Critical Path Analysis

**Primary critical path (NTN spine):**

Consumers -> Network Access -> Topology -> Non-Terrestrial Networks -> Satellite -> LEO Microsats -> Optical Sat-to-Sat Comms -> (... underlying silicon & supply chain)

**Bottlenecks / single points of failure:**

- **Non-Terrestrial Networks** — the only junction by which space telecoms enters the mainstream Topology layer; if NTN integration with mobile/fibre stalls, the whole chain remains a premium niche.
- **Satellite** — eight subsystem strands all hang off a single Satellite node; any subsystem shortage (e.g., Xenon supply, space-grade optics) propagates up.
- **Spectrum** — a shared dependency of Ground Stations, NTN, and Satellite; spectrum allocation decisions by ITU/regulators gate multiple branches.
- **Launchers** — single choke point for placing the entire Satellite layer into orbit.
- **Automation** — terminal node before the supply-chain floor, absorbing Orbit Tracking, Debris Tracking, and Fleet Management; failure of autonomy invalidates constellation economics.

**Resilience gaps:**

- **Supply-Chain Awareness** is the lowest-visibility node (0.14) yet sits under six subsystems. In Feb-2023 context, Xenon availability, EU vs non-EU space-grade component sourcing, and optics supply were all material risks — this low position understates strategic urgency.
- **Space Regulation** sits at 0.20 but gates four high-value nodes (Launchers, Satellite, Spectrum, Debris Tracking). Regulatory lag on LEO mega-constellations and debris rules is a cross-constellation risk.
- **V Band** is the newest spectrum layer and sits below Ku/Ka — it is the chain's spectrum frontier and likely to evolve fastest.
- **Optical Sat-to-Sat Comms** is specific to LEO microsats only; GEO has no comparable dependency, highlighting that inter-satellite mesh is a LEO-constellation differentiator.

## Validation Checklist

- [x] Chain starts with genuine user needs (Consumers, Corporations, Government) — not solutions.
- [x] All three anchors present with visibility 0.95 (>=0.90).
- [x] Access-stack layers covered: Network Access, Broadcast, Physical Network, Topology (mobile/fibre/NTN), Ground Stations, User Terminals with Phased-Array Antennas, Spectrum (Ku/Ka/V).
- [x] Satellite and orbit classes covered: LEO Microsats, GEO Satellites.
- [x] Satellite subsystems covered: Propulsion (Krypton, Xenon), Power, Cooling (Thermal Electric, Radiative, Cryogens), Antennas, Optical Sat-to-Sat Comms, Launchers, Beamforming, Beam-Steering.
- [x] Control systems covered: Orbit Tracking, Debris Tracking, Fleet Management + Automation.
- [x] Cross-cutting Space Regulation placed as a low-visibility foundation consumed by Launchers/Satellite/Spectrum/Debris Tracking and directly consumed by Government.
- [x] Supply-Chain Awareness included as the terminal foundation.
- [x] No orphan components — every non-root has at least one parent.
- [x] All non-anchor components are capabilities/activities/subsystems, not actors.
- [x] Visibility ordering consistent with dependency direction on every edge (parent >= child) — verified programmatically: 0 violations across 62 edges.
- [x] DAG: verified acyclic — 0 cycles across 40 nodes.
- [x] Granularity 40 components total (3 anchors + 37) — above the 25-upper-band guidance; justified by the scenario's explicit request for deep subsystem coverage.

## Visibility Assessment

| Tier | Range | Components |
|------|-------|-----------|
| Anchor (user-facing) | 0.90-1.00 | Consumers, Corporations, Government |
| High | 0.70-0.89 | Network Access, Broadcast, Physical Network, Topology, Mobile, Fibre, Non-Terrestrial Networks |
| Medium-High | 0.50-0.69 | User Terminals, Ground Stations, Satellite, Phased-Array Antennas, Spectrum, LEO Microsats, GEO Satellites |
| Medium | 0.30-0.49 | Ku/Ka/V Bands, Antennas, Control Systems, Launchers, Beamforming, Beam-Steering, Optical Sat-to-Sat Comms, Propulsion, Power, Cooling, Fleet Mgmt, Orbit Tracking, Debris Tracking |
| Low | 0.20-0.29 | Krypton, Xenon, Thermal Electric Cooling, Radiative Cooling, Cryogens, Automation, Space Regulation |
| Infrastructure | 0.00-0.19 | Supply-Chain Awareness |

## Assumptions and Open Questions

**Assumptions:**

1. **Non-Terrestrial Networks** is modelled as a *peer* of Mobile and Fibre under Topology, per 3GPP Rel-17 framing, not as a standalone silo. This matches the Feb 2023 state of standards and positions NTN as the natural integration point with terrestrial mobile.
2. **Space Regulation** is placed as a low-visibility cross-cutting constraint (vis=0.20). Four operator-facing components depend on it (Launchers, Satellite, Spectrum, Debris Tracking), and Government consumes it directly as the regulator. An alternative model would split ITU spectrum vs orbital-debris vs export-control into separate regulation nodes.
3. **Satellite** is a single node with two explicit sub-variants (LEO Microsats, GEO Satellites) rather than two peer nodes. This preserves the shared-subsystem fan-out while still making the LEO-vs-GEO split visible.
4. **Krypton and Xenon** are modelled as peer propellants under Propulsion; Xenon is the incumbent, Krypton the newer cheaper alternative adopted by Starlink-class constellations.
5. **Optical Sat-to-Sat Comms** is attached only to LEO Microsats (not GEO Satellites), reflecting that inter-satellite laser links are a LEO-constellation differentiator as of Feb 2023.
6. **Beamforming and Beam-Steering** are peer sub-capabilities under both Antennas and Phased-Array Antennas (they serve both satellite payload and user-terminal antenna faces).
7. **Evolution is fixed at 0.50 placeholder per skill contract** — this is a value-chain (partial) skill, not a full Wardley Map. The subsequent full-map skill would place Ku band and GEO toward commodity, and NTN/LEO/V band/Optical Sat-to-Sat/Krypton toward genesis/custom.
8. **Automation** is modelled as a shared descendant of Fleet Management, Orbit Tracking, and Debris Tracking rather than a peer — reflecting that constellation economics require automation of all three.

**Open questions:**

1. Should **Broadcast** have its own Satellite TV sub-chain (DTH, DVB-S2) distinct from generic Satellite, given it has historically been a GEO-only use case?
2. Is **Ground Stations** over-collapsed? In reality there are teleport operators, hybrid Gateway-as-a-Service (AWS Ground Station, Azure Orbital), and owner-operator ground networks — these evolve at different rates.
3. Should **Space Situational Awareness** be modelled explicitly as a peer of Control Systems rather than rolled into Debris Tracking? SSA as a capability has a distinct commercial vs sovereign evolution profile.
4. **Export controls** (ITAR, EU dual-use) and **sovereignty** (EU Iris², Chinese GuoWang) aren't nodes in this chain — should they be added as peers of Space Regulation?
5. Should **Launchers** decompose further into reusable vs expendable, small-lift vs heavy-lift? As of Feb 2023 this split is strategically significant (SpaceX dominance).
6. **Cryogens** — included because the scenario asked for it, but few Feb-2023 commercial telecoms satellites actually require cryogenic cooling; it may be more relevant to optical payloads / scientific platforms than to mainstream telecoms.

## Generation Metadata

- **Skill**: arckit-wardley.value-chain (partial-map skill; components + visibility only; evolution=0.50 placeholder)
- **Scenario**: telecoms-space — Space-Based Telecoms Landscape (Feb 2023 snapshot)
- **Components**: 40 (3 anchors + 37 supporting components)
- **Dependency edges**: 62
- **Visibility range**: 0.14 (Supply-Chain Awareness) to 0.95 (anchors)
- **Visibility violations**: 0 (verified — parent >= child on every edge)
- **Cycles**: 0 (DAG verified)
