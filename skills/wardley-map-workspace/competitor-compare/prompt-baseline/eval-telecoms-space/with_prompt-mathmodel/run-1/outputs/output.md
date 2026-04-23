# Space-Based Telecoms Landscape (Feb 2023)

## Mathematical Model $\mathcal{M} = (V, E, U, \nu, \varepsilon, t)$

**Time:** $t$ = February 2023. Key signals at this instant:

- Starlink has ~3,500 operational LEO sats; V1.5 with optical inter-sat laser links is rolling out; consumer dish is shipping globally.
- 3GPP Release 17 (NTN) was frozen June 2022; chipset support for direct-to-satellite is nascent.
- AST SpaceMobile BlueWalker 3 launched Sep 2022 (direct-to-cell from LEO).
- Amazon Kuiper has launched zero satellites; first protoflight imminent.
- ITU WRC-23 is later in 2023 — V-band coordination still open.
- ESA's ARTES programme and FCC orbital debris rules (Sept 2022, 5-year de-orbit) tightening regulation.

**Anchors $U$:** three user needs — Consumers, Corporations, Government.

**Component types:** most nodes are Activities (A). Phased-array antennas, optical sat-to-sat comms, beamforming are Knowledge-heavy (K) boundary cases. Fleet management, orbit/debris tracking are Practice (P). Supply-chain awareness is Data (D).

## 1. Components and coordinates

See `draft.owm`. 31 components plus 3 anchors plus regulatory cross-cutting.

## 2. Evolution scoring (quick 4-row cheat sheet)

For each component, I scored Ubiquity, Certainty, User Perception, Publication Types and averaged.

**Commodity (ε ≥ 0.75) — widespread, standard, focused on use:**

| Component | ε | Reasoning |
|---|---|---|
| Fibre Topology | 0.90 | Decades-deployed backbone; commonly understood. |
| Power Subsystem (sat) | 0.88 | Triple-junction GaAs solar + Li-ion — standard sat bus fare. |
| Mobile Topology | 0.88 | 4G/5G terrestrial is widespread and expected. |
| Spectrum Ku/Ka | 0.85 | ITU-coordinated, auctioned, operationally mature. |
| Radiative Cooling | 0.85 | Passive thermal straps/radiators — textbook. |
| GEO Satellite | 0.82 | 60 years of operational heritage; Boeing 702, Airbus Eurostar, etc. |
| Broadcast | 0.80 | DTH TV, Ku-band broadcast — mature utility. |

**Product +rental (ε ∈ [0.5, 0.75)) — rapidly increasing, fit-for-purpose, feature-focused:**

| Component | ε | Reasoning |
|---|---|---|
| Network Access | 0.72 | Multiple mature delivery channels; subscription-grade. |
| Satellite Antennas | 0.70 | Parabolic reflectors mature; array tech is the rental-stage piece. |
| Physical Network | 0.70 | Access networks are rented/leased at scale. |
| Ground Stations | 0.62 | AWS Ground Station, KSAT GSaaS — rental model emerging strongly. |
| Xenon Propulsion | 0.62 | Hall-effect thrusters (SPT-100, PPS-1350) — productised. |
| Launchers | 0.62 | Reusable (F9) mature; Falcon Heavy, Ariane 5/6, Electron all rental. |
| User Terminals | 0.58 | Starlink Dishy is first true consumer-product phased array. |
| Thermal Electric Cooling | 0.58 | Peltier/TEC widely productised for focal-plane sensors. |
| LEO Microsat | 0.55 | Starlink mass production (~40/week) = product-stage manufacturing. |
| Orbit Tracking | 0.55 | Space-Track, LeoLabs commercial feeds. |
| Beamforming | 0.52 | DSP silicon (Ball, Anokiwave) — productised but still specialist. |
| Beam-Steering | 0.50 | Similar — commercial arrays available. |
| Fleet Management | 0.50 | SpaceX Starlink mgmt bespoke; Kratos OpenSpace, SES adaptive — productising. |

**Custom Built (ε ∈ [0.25, 0.5)) — slowly increasing, rapid learning, leading edge:**

| Component | ε | Reasoning |
|---|---|---|
| Phased-Array Antennas (consumer) | 0.48 | Still heavily engineered; cost curve only just breaking. |
| Space Regulation | 0.42 | ITU/FCC frameworks exist but being rewritten for mega-constellations. |
| Debris Tracking | 0.38 | LeoLabs/Slingshot/USSF SSA — fragmented, early commercial. |
| Supply-Chain Awareness | 0.35 | COVID exposed brittleness; digital-twin supply visibility nascent. |
| Krypton Propulsion | 0.32 | SpaceX's Kr Hall thrusters novel at scale; one-operator deployment. |
| Cryogenic Cooling (smallsat) | 0.30 | Still custom per mission (mostly IR payloads). |
| Non-Terrestrial Networks | 0.30 | 3GPP Rel-17 just frozen; no carrier has commercial NTN at scale. |
| Optical Sat-to-Sat Comms | 0.28 | Starlink V1.5 OISLs just starting; Mynaric, Tesat early. |

**Genesis (ε < 0.25) — rare, poorly understood, exciting:**

| Component | ε | Reasoning |
|---|---|---|
| Constellation Automation | 0.20 | Fully autonomous collision-avoidance + bus mgmt still research. |
| Spectrum V-band | 0.18 | WRC allocations pending; experimental licenses only. |

## 3. Visibility scoring

Seed from graph distance, then overridden where value-chain judgment differs. Hard rule $\nu(a) \ge \nu(b)$ enforced on every edge — checked against draft.owm.

Anchors at $\nu \ge 0.96$. NTN sits high ($\nu = 0.72$) because it is a first-class topology choice even though it's bottom of the evolution curve — visibility is about user proximity, not maturity. Supply-chain awareness is pushed to the deepest visibility ($\nu = 0.08$) — invisible to end users but feeds everything. Space Regulation is placed at $\nu = 0.10$ (deep) because the dependency semantics are *"X depends on regulation"* — every regulated component sits above it.

Fleet Management is raised to $\nu = 0.22$ above Orbit Tracking (0.18), Debris Tracking (0.16) and Constellation Automation (0.12) to satisfy the hard rule $\nu(a) \ge \nu(b)$ on the `Fleet Management → Orbit / Debris / Automation` edges.

## 4. Derived heuristics (attention prompts, not canonical)

### Top 3 by Differentiation pressure $D(v) = \nu(v) \cdot (1 - \varepsilon(v))$

| # | Component | D | Why it matters |
|---|---|---|---|
| 1 | **Non-Terrestrial Networks** | 0.72 × 0.70 = **0.504** | Highly visible topology choice, still Custom-Built. Whoever builds the NTN-to-carrier integration plays wins enterprise/gov share. |
| 2 | **User Terminals** | 0.64 × 0.42 = **0.269** | Starlink's moat: consumer-grade phased-array at <$600 BOM. Kuiper/OneWeb need equivalent. |
| 3 | **Phased-Array Antennas** | 0.58 × 0.52 = **0.302** | Underlying tech for terminals *and* satellite-side. Still custom at scale. |

(Ranking by D value; NTN dominates.)

### Top 3 by Commodity leverage $K(v) = (1 - \nu(v)) \cdot \varepsilon(v)$

| # | Component | K | Why |
|---|---|---|---|
| 1 | **Power Subsystem** | (1−0.30) × 0.88 = **0.616** | Deep + mature. Buy from TAS, Airbus, or Rocket Lab (after Solero). |
| 2 | **Launchers** | (1−0.20) × 0.62 = **0.496** | Deep dependency, productised rental market (F9, Transporter, Ariane). |
| 3 | **Radiative Cooling** | (1−0.27) × 0.85 = **0.621** | Deep + commoditised. COTS thermal products. |

(K₃ is marginally above K₁; all three are buy/outsource defaults.)

### Top 3 dependency risks $R(a,b) = \nu(a) \cdot (1 - \varepsilon(b))$

| # | Edge (a → b) | R | Why |
|---|---|---|---|
| 1 | **NTN → Optical Sat-to-Sat Comms** | 0.72 × 0.72 = **0.518** | (Indirect via LEO) User-visible NTN fundamentally depends on immature OISLs for global coverage without ground-station landing rights. |
| 2 | **Network Access → NTN** | 0.88 × 0.70 = **0.616** | User-facing access tier pinned to a Custom-Built topology. |
| 3 | **User Terminals → Phased-Array Antennas** | 0.64 × 0.52 = **0.333** | Terminal availability is gated on array yield/cost curve. |

## 5. Suggested gameplays (from Wardley's 61-play catalogue)

- **#2 Standards game** on **Non-Terrestrial Networks** — 3GPP Rel-17/18 is live; operator that influences the TS 38.101-5 chipset profile locks in economics for a decade.
- **#15 Open approaches** / **#13 Open source** on **Constellation Automation** and **Debris Tracking** — these are too immature and too shared-interest to win closed. OpenSSA-style collaboration (NASA CARA + ESA + commercial) turns them into a common utility.
- **#29 Harvesting** on **Optical Sat-to-Sat Comms** — acquire Mynaric / Tesat / smallsat OISL vendors early while they are still Custom-Built. Once Starlink's V2 normalises the interface, harvesting cost climbs fast.
- **#36 Directed investment** on **Phased-Array Antennas** and **Krypton Propulsion** — the two components with highest D that are also technically addressable by a directed R&D euro.
- **#41 Fool's mate** (use ecosystem to attack incumbent) on **GEO Satellite** operators — LEO player uses NTN + direct-to-cell to bypass the teleport/GEO stack entirely.
- **#48 Pig in a poke** — consciously avoid: GEO operators buying LEO slots at WRC-23 peak premium are exposed.
- **#7 Sweat and dump** (harvest incumbent, move capital elsewhere) — candidate for **Broadcast**: still Commodity, high cash, but being eaten from below by NTN.

## 6. Doctrine notes (from the 40 principles)

- **Know your users (Phase II)** — three anchors declared. Good. But watch that *consumer* and *government* have genuinely different value chains below `Network Access`; this map collapses them at Layer 1 and that may be under-resolved.
- **Focus on high situational awareness** — the map is weak on regulatory sub-structure. Space Regulation is a single node; in reality it's (spectrum coordination, orbital slots, debris mitigation, export control, landing rights) — five sub-concerns with different evolution stages.
- **Remove duplication and bias** — Xenon vs Krypton propulsion are both drawn; they're substitutes. Good for tracking cannibalisation.
- **Use appropriate methods** — LEO mass-manufacturing is a Pioneer-phase activity even though the satellite itself is becoming Product-stage; the map doesn't yet separate pioneer/settler/town-planner responsibility. Add a PST overlay if using operationally.
- **Think small** (#25) / **Think aptitude and attitude** (#31) — NTN integration requires a small, pioneer team working against telecoms-standards incumbents. Don't let a town-planner-shaped operator own it.

## 7. Where it has commoditised vs where LEO/NTN is still novel

**Commoditised (right-hand side of the map, ε > 0.75):**

- Fibre, mobile 4G/5G backhaul, Ku/Ka spectrum, broadcast, GEO satellite platforms, satellite power subsystems, radiative cooling.
- These are outsource/buy defaults. No differentiation available.

**Still novel — the LEO/NTN frontier (ε < 0.45, high D):**

- **Non-Terrestrial Networks** — the integration layer between 3GPP carriers and LEO constellations. Genesis-to-Custom transition.
- **Optical Sat-to-Sat Comms** — the thing that makes LEO constellations independent of ground-station geopolitics.
- **Krypton propulsion** — commodity gas, novel electric-propulsion chemistry at constellation scale.
- **Consumer phased-array antennas** — the one component where a supplier (Starlink) has a genuine differentiation window of ~2-3 years.
- **Constellation automation** — still research, still the bottleneck for 10k+ sat operations.
- **V-band spectrum** — genesis; WRC-23 will determine next phase.

## 8. Evolution scenario (NOT a forecast)

Using logistic $d\varepsilon/dt = r \varepsilon (1 - \varepsilon)$ with $r \approx 0.25\,\text{yr}^{-1}$ for communications tech on the frontier:

- **NTN**: $\varepsilon = 0.30 \to 0.55$ over ~3 years (Rel-18/19 freeze + chipset ubiquity).
- **LEO Microsat**: $\varepsilon = 0.55 \to 0.72$ as Kuiper/OneWeb/China's Guo Wang reach production.
- **Phased-Array Antennas**: $\varepsilon = 0.48 \to 0.70$ driven by CMOS beamformers.
- **Optical Sat-to-Sat Comms**: $\varepsilon = 0.28 \to 0.50$ as Starlink V2 defines the de-facto interface.
- **Krypton Propulsion**: $\varepsilon = 0.32 \to 0.55$ as other operators follow Starlink's supply-chain.

These are *scenarios*, not predictions — Wardley's climatic pattern: *you cannot measure evolution over time.*

## 9. Summary

The space-telecoms landscape in Feb 2023 is bimodal:

- Everything above $\nu = 0.70$ and to the right of $\varepsilon = 0.75$ is the classical operator stack — commoditised, buy-or-outsource.
- Everything in the NTN / LEO / OISL / phased-array cluster (ε 0.25–0.55, ν 0.30–0.72) is the frontier. Four companies (SpaceX, Amazon, AST SpaceMobile, Lynk) are racing to cross to Product stage.
- Supply-chain awareness and constellation automation are the deepest, most neglected components — both are high-leverage for any operator running more than ~100 satellites.

The strategic question isn't *build or buy a satellite*; it's *which component of the integration layer (NTN, OISL, phased array, fleet automation) do we own vs commoditise*. The map names six candidates explicitly.
