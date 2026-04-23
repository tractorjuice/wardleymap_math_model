# Wardley Map Analysis: Space-Based Telecoms (February 2023)

## Purpose

Where has space telecoms commoditised, and where is the LEO / NTN stack still
novel? The map is built to support a build-vs-buy and
where-to-invest conversation across the consumer, corporate, and
government access stack — including the satellite itself, its subsystems,
the control plane, and the supply chain underneath. Space regulation is
treated as a cross-cutting climate factor.

Note on scope: the scenario explicitly asks for a broad inventory (access
stack, topology variants, full satellite subsystem list, control systems,
supply chain, regulation). The resulting map has 27 components — above the
"<= 18" readability guidance in SKILL.md Step 2. Splitting into submaps
(e.g. a Satellite subsystem submap and a Control / Operations submap) is
recommended for consulting use; here we keep a single map so the
commoditised Commodity cluster and the novel LEO/NTN cluster are visible
side-by-side, which is the question asked.

---

## Three Deliverables

1. Interactive React artifact — see `artifact.jsx` in this folder.
2. OWM text block — below (also in `draft.owm`).
3. Strategic commentary — this document.

---

## OWM Text Block

```owm
title Space-Based Telecoms (February 2023)
style wardley

// Anchors — users of the space-telecoms value chain
anchor Consumers [0.97, 0.45]
anchor Corporations [0.97, 0.55]
anchor Government [0.97, 0.65]

// User-visible services
component Network Access [0.90, 0.55]
component Broadcast [0.82, 0.85]
component Space Regulation [0.82, 0.50]

// Access-stack topology
component Mobile Topology (4G/5G) [0.74, 0.78]
component Fibre Topology [0.74, 0.86]
component NTN Topology [0.74, 0.30] inertia
component Physical Network [0.66, 0.80]

// Edge and terminal
component User Terminals (Phased Array) [0.58, 0.38]
component Ground Stations [0.60, 0.58]
component Spectrum (Ku/Ka/V) [0.56, 0.70]

// Satellite platform
component LEO Microsats [0.48, 0.35]
component GEO Satellites [0.48, 0.78]

// Satellite subsystems
component Beamforming / Beam-Steering [0.38, 0.32] inertia
component Satellite Antennas [0.38, 0.65]
component Optical Sat-to-Sat Comms [0.38, 0.18]
component Satellite Propulsion (Kr/Xe) [0.30, 0.55]
component Thermal Control (TE/Rad/Cryo) [0.30, 0.62]
component Satellite Power [0.30, 0.82]

// Launch and orbit services
component Launchers [0.22, 0.58]
component Orbit Tracking [0.22, 0.68]
component Debris Tracking [0.22, 0.42]

// Ops and supply chain underneath
component Fleet Management [0.14, 0.35]
component Automation [0.14, 0.22]
component Supply-Chain Awareness [0.06, 0.22]

// Anchor -> service
Consumers->Network Access
Corporations->Network Access
Government->Network Access
Consumers->Broadcast
Corporations->Broadcast
Government->Broadcast
Consumers->Space Regulation
Corporations->Space Regulation
Government->Space Regulation

// Service -> topology
Network Access->Mobile Topology (4G/5G)
Network Access->Fibre Topology
Network Access->NTN Topology
Broadcast->NTN Topology
Broadcast->GEO Satellites

// Topology -> transport
Mobile Topology (4G/5G)->Physical Network
Fibre Topology->Physical Network
NTN Topology->Physical Network
NTN Topology->User Terminals (Phased Array)
NTN Topology->Ground Stations
NTN Topology->Spectrum (Ku/Ka/V)

// Physical network shares ground segment
Physical Network->Ground Stations

// Edge -> satellite platform
User Terminals (Phased Array)->LEO Microsats
User Terminals (Phased Array)->GEO Satellites
Ground Stations->LEO Microsats
Ground Stations->GEO Satellites
Spectrum (Ku/Ka/V)->Space Regulation
Spectrum (Ku/Ka/V)->LEO Microsats
Spectrum (Ku/Ka/V)->GEO Satellites

// Satellite -> subsystems
LEO Microsats->Beamforming / Beam-Steering
LEO Microsats->Satellite Antennas
LEO Microsats->Optical Sat-to-Sat Comms
LEO Microsats->Satellite Propulsion (Kr/Xe)
LEO Microsats->Thermal Control (TE/Rad/Cryo)
LEO Microsats->Satellite Power
GEO Satellites->Satellite Antennas
GEO Satellites->Satellite Propulsion (Kr/Xe)
GEO Satellites->Thermal Control (TE/Rad/Cryo)
GEO Satellites->Satellite Power

// Satellite -> launch / ops
LEO Microsats->Launchers
GEO Satellites->Launchers
LEO Microsats->Orbit Tracking
GEO Satellites->Orbit Tracking
LEO Microsats->Fleet Management
GEO Satellites->Fleet Management

// Ops stack
Orbit Tracking->Debris Tracking
Fleet Management->Orbit Tracking
Fleet Management->Automation
Debris Tracking->Automation
Automation->Supply-Chain Awareness

// Regulation is a cross-cutting dependency for launch and orbit
Launchers->Space Regulation
Orbit Tracking->Space Regulation
Debris Tracking->Space Regulation

// Supply chain sits underneath hardware
Launchers->Supply-Chain Awareness
Satellite Propulsion (Kr/Xe)->Supply-Chain Awareness
Satellite Power->Supply-Chain Awareness
Satellite Antennas->Supply-Chain Awareness
Thermal Control (TE/Rad/Cryo)->Supply-Chain Awareness

// Evolution arrows — predicted 12-24 month movement
evolve NTN Topology 0.48
evolve User Terminals (Phased Array) 0.55
evolve LEO Microsats 0.52
evolve Optical Sat-to-Sat Comms 0.35
evolve Beamforming / Beam-Steering 0.50
evolve Fleet Management 0.48
evolve Debris Tracking 0.58

annotation 1 [[0.78, 0.20]] LEO / NTN frontier: still novel in Feb 2023
annotation 2 [[0.30, 0.82]] Commoditised subsystems — buy, do not build
annotation 3 [[0.50, 0.50]] Regulation as cross-cutting climate

build Optical Sat-to-Sat Comms
build Fleet Management
build NTN Topology
buy Satellite Power
buy Thermal Control (TE/Rad/Cryo)
buy Launchers
outsource Physical Network
outsource Ground Stations
```

---

## Component Evolution Assessment

| Component | Stage | Position [vis, mat] | Rationale |
|---|---|---|---|
| Consumers | Anchor (Product) | [0.97, 0.45] | End customers buying connectivity/broadcast. |
| Corporations | Anchor (Product) | [0.97, 0.55] | Enterprise buyers (maritime, aviation, backhaul). |
| Government | Anchor (Product) | [0.97, 0.65] | Defence, civil agencies, regulators. |
| Network Access | Product | [0.90, 0.55] | Well-understood user-facing service competing on feature/price. |
| Broadcast | Commodity | [0.82, 0.85] | DTH satellite has been utility-priced since the 1990s. |
| Space Regulation | Product | [0.82, 0.50] | ITU / national regulators are institutionalised, but mega-constellation / NTN rules still being written. |
| Mobile Topology (4G/5G) | Commodity | [0.74, 0.78] | 4G fully commoditised, 5G late Product / early Commodity. |
| Fibre Topology | Commodity | [0.74, 0.86] | Regulated, standardised, pay-per-bit transport. |
| NTN Topology | Custom-Built (inertia) | [0.74, 0.30] | 3GPP Rel-17 NTN frozen mid-2022; integration still bespoke per operator. Inertia flagged on the standards side. |
| Physical Network | Commodity | [0.66, 0.80] | IP/MPLS + submarine cable are utility infrastructure. |
| User Terminals (Phased Array) | Custom-Built | [0.58, 0.38] | Dishy / Kymeta / ThinKom expensive, subsidised, not interoperable. |
| Ground Stations | Product | [0.60, 0.58] | AWS Ground Station, Azure Orbital, KSAT — rentable Product market. |
| Spectrum (Ku/Ka/V) | Product | [0.56, 0.70] | Ku/Ka mature via ITU; V-band still early. |
| LEO Microsats | Custom-Built | [0.48, 0.35] | Starlink/OneWeb/Planet iterate hardware every generation — still a competitive differentiator. |
| GEO Satellites | Commodity | [0.48, 0.78] | Airbus/Boeing/Lockheed/Thales/Maxar standardised buses since 1970s. |
| Beamforming / Beam-Steering | Custom-Built (inertia) | [0.38, 0.32] | Digital multi-beam processors iterated in-house; operators protect payload IP. |
| Satellite Antennas | Product | [0.38, 0.65] | Multiple vendors (Airbus, Thales, L3Harris, Viasat). |
| Optical Sat-to-Sat Comms | Genesis | [0.38, 0.18] | Starlink v1.5/v2-mini lasercom just deploying through 2022-23; Mynaric / TESAT supply others. |
| Satellite Propulsion (Kr/Xe) | Product | [0.30, 0.55] | Hall-effect thrusters available from Busek / Aerojet / Safran; Xenon mature, Krypton newer. |
| Thermal Control (TE/Rad/Cryo) | Product | [0.30, 0.62] | Radiative radiators and heat pipes off-the-shelf; TE and cryo are Product for most classes. |
| Satellite Power | Commodity | [0.30, 0.82] | Space-grade solar cells + Li-ion are standardised and price-competitive. |
| Launchers | Product | [0.22, 0.58] | Falcon 9 / rideshare pushing toward Commodity on $/kg but ULA/Arianespace/Rocket Lab/ISRO still compete. |
| Orbit Tracking | Product | [0.22, 0.68] | 18 SPCS / Space-Track plus LeoLabs / COMSPOC / ExoAnalytic. |
| Debris Tracking | Custom-Built | [0.22, 0.42] | Commercial SSA for sub-10 cm emerging (LeoLabs, NorthStar). |
| Fleet Management | Custom-Built | [0.14, 0.35] | Each operator builds its own constellation OSS/BSS. |
| Automation | Custom-Built | [0.14, 0.22] | Autonomous conjunction / manoeuvre planning still bespoke. |
| Supply-Chain Awareness | Custom-Built | [0.06, 0.22] | Component traceability / ITAR / heritage databases remain a patchwork. |

---

## Key Strategic Observations

1. **Two clusters, one horizontal line.** The satellite platform row at
   visibility 0.48 splits cleanly: GEO sits at 0.78 (Commodity), LEO sits at
   0.35 (Custom-Built). Beneath each hangs a subsystem ecosystem that is
   mostly shared (antennas, power, thermal, propulsion are reused between
   both) but one frontier is LEO-specific — optical inter-satellite links —
   and sits at 0.18, visibly to the left of everything else. That is
   the answer to "where is LEO/NTN still novel": optical ISL, beamforming,
   NTN topology, fleet management, and automation.

2. **Commodity tail — buy, don't build.** The right-hand Commodity column
   contains Satellite Power (0.82), Fibre Topology (0.86), Broadcast (0.85),
   Physical Network (0.80), Mobile Topology (0.78), and GEO Satellites
   (0.78). These are purchased inputs or utility-priced services. Any
   operator investing engineering headcount in these is mis-allocated.

3. **Regulation is climate, not component.** Space Regulation sits at
   [0.82, 0.50] with four in-bound dependencies (all three anchors plus
   launchers, orbit tracking, debris tracking, and spectrum). It behaves
   like a climatic pattern — you don't build it, you react to it — but it
   moves under you as mega-constellation rules are written.

4. **Vertical inertia chain on the LEO side.** NTN Topology (Custom-Built,
   inertia) → User Terminals (Custom-Built) → LEO Microsats (Custom-Built)
   → Beamforming (Custom-Built, inertia) → Optical ISL (Genesis). This
   column is both the source of differentiation and the greatest
   execution risk.

5. **Single point of failure underneath.** Supply-Chain Awareness at
   [0.06, 0.22] is the sink for seven dependencies. Weakness here
   (ITAR blockages, rare-earth shortages, heritage silicon lead times) is
   invisible to the user but catastrophic in effect. This is where a
   resilience investment has the highest leverage.

---

## Doctrine Check

- **Focus on user needs**: The three anchors (Consumers, Corporations,
  Government) all route to the same Network Access / Broadcast services but
  with different implicit SLAs. The map would be sharper if split into three
  per-anchor submaps.
- **Use appropriate methods**: Applying waterfall to LEO Microsats (still
  Custom-Built with rapid iteration) would kill the programme. Applying
  agile to GEO Satellites (a Commodity market) wastes attention. There is
  a visible methods-mismatch risk on any operator that treats the whole
  value chain with the same governance.
- **Remove duplication**: GEO Satellites and LEO Microsats share five
  subsystems (power, thermal, propulsion, antennas, beamforming). Sharing
  infrastructure across programmes is a concrete doctrine win.
- **Bias check**: The map is Custom-Built-heavy on the left, which reflects
  the Feb 2023 reality (LEO buildout), not wishful thinking. No
  "everything-is-commodity" bias.

---

## Recommended Actions

1. **Invest in optical ISL and fleet-management automation.** Both are
   Genesis / early Custom-Built and both are where a multi-year lead
   materialises. A vertically integrated programme (Starlink model) wins
   here because there is no product market to buy from.
2. **Buy, do not build, the Commodity subsystems.** Satellite Power,
   Launchers, Physical Network, Mobile/Fibre Topology. Any in-house work
   on these is a methods mismatch and a capex burn.
3. **Outsource Ground Stations.** AWS Ground Station / Azure Orbital /
   KSAT are Product-stage offerings priced per pass. Build ground segment
   only where sovereign / jurisdictional constraints force it
   (government anchor only).
4. **Harden Supply-Chain Awareness.** Invest in traceability, dual-source
   components, ITAR-aware inventory. Low-visibility, high-blast-radius.
5. **Engage regulators actively.** NTN spectrum rules, V-band
   coordination, and mega-constellation orbit rules are being written
   now. Sitting out costs you a seat at the table when they harden.

---

## Build vs. Buy Assessment

| Component | Recommendation | Rationale |
|---|---|---|
| Optical Sat-to-Sat Comms | **Build / Invest** | Genesis; no mature product market; differentiator. |
| Beamforming / Beam-Steering | **Build / Invest** | Custom-Built with inertia; payload IP is competitive moat. |
| NTN Topology | **Build / Invest** | Custom-Built; integration with 5G core is where differentiation lives. |
| User Terminals (Phased Array) | **Build (co-invest)** | Custom-Built; subsidised today — co-invest with chipset partners. |
| LEO Microsats | **Build** | Custom-Built; bus iteration is differentiator. |
| Fleet Management | **Build** | Custom-Built; each operator's ops model is unique. |
| Debris Tracking | **Buy + supplement** | Emerging Product (LeoLabs, COMSPOC); supplement internally. |
| Ground Stations | **Outsource** | Product-stage; AWS / Azure / KSAT compete. |
| Launchers | **Buy** | Product; competitive vendors, clear $/kg pricing. |
| Satellite Antennas | **Buy** | Product; multiple vendors. |
| Satellite Propulsion (Kr/Xe) | **Buy** | Product; commercial Hall-effect available. |
| Thermal Control (TE/Rad/Cryo) | **Buy** | Product; standard parts catalogue. |
| Satellite Power | **Buy** | Commodity; utility economics. |
| Physical Network | **Outsource** | Commodity; IP transit is utility. |
| Mobile / Fibre Topology | **Buy** | Commodity; transit from tier-1 carriers. |
| Broadcast | **Outsource** | Commodity; DTH operators exist. |
| GEO Satellites | **Buy** | Commodity; buy from Airbus/Boeing/Lockheed/Thales/Maxar. |
| Orbit Tracking | **Buy** | Product; 18 SPCS plus commercial SSA. |
| Space Regulation | **Engage** | Not a "buy" — regulatory engagement as a discipline. |
| Supply-Chain Awareness | **Build** | Custom-Built; internal resilience capability. |

---

## Evolution Predictions (12-24 months, from Feb 2023)

- **NTN Topology**: Custom-Built → late Custom-Built / early Product
  (0.30 → 0.48). 3GPP Release 18 will tighten NTN integration and at
  least one interoperable vendor solution will emerge.
- **User Terminals**: Custom-Built → Product (0.38 → 0.55). Chipset
  generation shrinks and subsidy burn forces interoperability conversations.
- **LEO Microsats**: Custom-Built → late Custom-Built (0.35 → 0.52).
  Contract manufacturing (Lockheed/Terran Orbital, Airbus/OneWeb) will
  standardise bus options.
- **Optical ISL**: Genesis → late Genesis / Custom-Built (0.18 → 0.35).
  Starlink proves at-scale viability; Mynaric/TESAT / CACI scale
  production.
- **Beamforming**: Custom-Built → Product (0.32 → 0.50). Silicon vendors
  package more of the stack; operators stop reinventing the DSP layer.
- **Fleet Management**: Custom-Built → late Custom-Built (0.35 → 0.48).
  A shared OSS/BSS for small operators will emerge (likely SaaS).
- **Debris Tracking**: Custom-Built → Product (0.42 → 0.58). Commercial
  SSA matures as insurance / regulatory demand grows.

**Inertia to watch**: NTN Topology and Beamforming are both flagged
inertia. Expect terrestrial-mobile incumbents to resist NTN integration,
and chipset vendors to protect beamforming IP.

---

## Open Questions

1. **Where does inter-constellation roaming sit?** It isn't on the map
   yet because no commercial model exists in Feb 2023 — but it's where
   LEO/NTN might collapse into a commodity layer over 2025-2027.
2. **Sovereignty of ground stations**: does "outsource to AWS / Azure"
   hold for the Government anchor, or does it force a separate submap with
   a sovereign ground-segment constraint?
3. **What is the cannibalisation risk** from LEO to GEO for
   broadcast/VSAT? GEO is Commodity; LEO is Custom-Built. A classic
   climatic pattern ("past success breeds inertia") applies to GEO
   incumbents.

---

## Map Validation

Validated with `scripts/validate_map.py` (haberlah skill). Result:
- 0 errors.
- 1 warning (27 components > 18). Accepted: the scenario explicitly
  asks for the full subsystem inventory. Splitting into submaps (Satellite
  subsystem, Control / Ops) is recommended for consulting use.
