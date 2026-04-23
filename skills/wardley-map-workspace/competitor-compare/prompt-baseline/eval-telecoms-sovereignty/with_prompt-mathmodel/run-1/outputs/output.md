# Telecoms Sovereignty — Wardley Map (Nation-State View, October 2022)

Prompt-only baseline run. Generated using only `/workspaces/wardleymap_math_model/prompts/wardley_map_generator.md`.

## 1. Mathematical model in use

`M = (V, E, U, ν, ε, t)` per the prompt's Part 1, with four anchors (government, collective, corporations, people). Visibility is seeded from chain distance and then adjusted for value-chain judgment; the hard rule `ν(a) ≥ ν(b)` for every edge is enforced. Evolution is scored against the 4-row cheat sheet (Ubiquity, Certainty, User Perception, Publication Types) and mapped to band midpoints.

## 2. Components V and anchor set U

Anchor set U = {Government, The Collective, Corporations, People}.

Sovereignty pillars (territorial, political, cultural, economic, digital, CNI) are treated as first-class needs attached to the appropriate anchor(s) — e.g., Cultural is a collective+people need, CNI is primarily a government need, Economic is primarily a corporate need, Digital cuts across all four.

The value chain then resolves into four broad tiers:

1. Theatre / awareness (land-sea-air-space, supply chain, peering)
2. Communication stack: devices → access networks → equipment & topology → control layer
3. Expertise and standards (Knowledge layer)
4. Underlying reality: geography, physical + information supply chains, compute, power, space

## 3. Evolution scoring (4-row cheat sheet, abbreviated)

Scores are the mean of four row-midpoints; values that disagreed strongly across rows are flagged.

| Component | Ubi | Cert | User | Pub | ε |
|---|---|---|---|---|---|
| Smartphones | IV | IV | IV | III-IV | ≈ 0.88 |
| Computers | IV | IV | IV | III-IV | ≈ 0.88 |
| Radio / TV | IV | IV | IV | IV | 0.90 |
| Satellite Phones | III | III | II-III | II | ≈ 0.55 (in transition) |
| IoT Devices | III | III | III | II-III | ≈ 0.60-0.65 |
| Mobile Towers | IV | IV | III | III | ≈ 0.78 |
| Fixed Cable | IV | IV | IV | III | ≈ 0.82 |
| Satellite Access (LEO) | III | II-III | II | II | ≈ 0.55 (in transition — Starlink-era) |
| Launch Vehicles | II-III | II-III | II | II | ≈ 0.40-0.50 |
| Network Eqpt (Fixed/Mobile) | IV | IV | III-IV | III | ≈ 0.78 |
| Network Topology | III-IV | III | III | III | ≈ 0.68 |
| DNS-over-HTTPS | IV | IV | III | III | ≈ 0.80 |
| Nation-State Firewall | II-III | II | II | II-III | ≈ 0.45 (in transition) |
| SIMs / eSIMs | IV | IV | IV | IV | 0.88 |
| Geofencing | III | II-III | II-III | II | ≈ 0.55 |
| Standards Bodies | III-IV | IV | III | III | ≈ 0.72 |
| Telecoms Expertise | II-III | III | II | II | ≈ 0.40 |
| Compute | IV | IV | IV | III-IV | ≈ 0.85 |
| Power | IV | IV | IV | IV | 0.90 |
| Physical Supply Chain | III | II-III | III | II | ≈ 0.55 (in transition) |
| Information Supply Chain | III | II-III | III | II | ≈ 0.55 (in transition) |
| Space (Orbits) | II-III | II | II | II | ≈ 0.45 |
| Geography | IV | IV | IV | IV | 0.95 (effectively fixed) |

"In transition" flags: Satellite Access, Nation-State Firewall, Supply Chains, IoT — the rows disagreed by one stage, consistent with the scenario date (Oct 2022, when LEO constellations, CBAM-style supply-chain controls, and "splinternet" legislation were all visibly moving).

## 4. Visibility ν

Seeds from `d(v)` were then adjusted upward for pillars (the user thinks about them directly) and slightly downward for control-layer and underlying-reality items that are architecturally invisible to end users even though graph distance is small. The HARD rule `ν(a) ≥ ν(b)` holds across every declared edge.

## 5. OWM output

See `draft.owm` in this directory. Summary layout:

- Top band (ν ≥ 0.85): anchors and sovereignty pillars.
- Upper-middle (0.60 ≤ ν < 0.85): theatre/awareness + access devices.
- Middle (0.40 ≤ ν < 0.60): access networks, network equipment, control layer.
- Lower-middle (0.25 ≤ ν < 0.40): expertise, compute.
- Bottom (ν < 0.25): power, supply chains, space, geography.

## 6. Strategic Analysis

### a. Top 3 by Differentiation pressure D(v) = ν · (1 − ε)

Excluding anchors and pillars (which dominate D trivially because they sit near the user and are not meaningfully scored on evolution):

1. **Land-Sea-Air-Space Awareness** — D ≈ 0.80 · 0.68 = 0.54. High visibility, genuinely custom-built per nation (space-domain awareness, OSINT fusion, integration with MoD sensors). Investment here directly advances territorial sovereignty.
2. **Supply-Chain Awareness** — D ≈ 0.78 · 0.80 = 0.62. Post-COVID + post-Ukraine-invasion, visibility of physical and information supply chains is both important and poorly understood. Classic custom-built problem.
3. **Nation-State Firewall** — D ≈ 0.56 · 0.55 = 0.31. Moderate visibility, genuinely custom-built per nation (policy and legal context is not transferable). Unlike the Chinese model, Western variants are only just emerging in Oct 2022 (UK Online Safety Bill, EU DSA).

### b. Top 3 by Commodity leverage K(v) = (1 − ν) · ε

1. **Power** — K ≈ 0.75 · 0.90 = 0.68. Utility par excellence; procured, not built. Sovereign concern is the *grid* (and its fuel supply), not power as a commodity.
2. **Compute** — K ≈ 0.70 · 0.85 = 0.60. The hyperscaler stack is a commodity but the *location* of compute is a sovereignty variable — see note on doctrine below.
3. **SIMs / eSIMs** — K ≈ 0.36 · 0.88 = 0.32. Fully commoditised; the sovereign leverage is over issuance policy, not over the silicon.

### c. Top 3 dependency risks R(a, b) = ν(a) · (1 − ε(b))

1. **(CNI Sovereignty → Mobile Network Equipment)** — R ≈ 0.85 · 0.22 = 0.19. Well-known risk: vendor concentration (Ericsson, Nokia, Huawei, Samsung) and the 2020 UK Huawei stripping decision still in execution in Oct 2022.
2. **(Digital Sovereignty → Nation-State Firewall)** — R ≈ 0.86 · 0.55 = 0.47. Highest raw R in the map. A high-visibility sovereignty pillar depending on a still-immature control instrument.
3. **(Territorial Sovereignty → Land-Sea-Air-Space Awareness)** — R ≈ 0.90 · 0.68 = 0.61. Again high raw R, but here the risk is *incompleteness* not *fragility* — much of the space-domain-awareness stack depends on foreign actors (US SDA, commercial SSA providers).

### d. Suggested gameplays

From the 61-play catalogue referenced in the prompt:

- **Sensing engines / situational awareness** (Doctrine-adjacent gameplay) on Supply-Chain Awareness — build a national telemetry and inventory capability before legislating on it.
- **Harvesting** on Launch Vehicles and Satellite Access — let SpaceX et al. mature the market, then buy capacity and selectively insource the sovereignty-critical layer (launch from sovereign soil, sovereign ground stations).
- **Open Approaches** on Network Equipment via Open RAN — the explicit 2022 UK / US / Japan policy direction, reducing dependence on the Ericsson/Nokia/Huawei oligopoly.
- **Standards engagement** (play type: "Setting Exceptional Standards") on 3GPP / ITU — sovereignty over telecoms is partly sovereignty over the standards that define it. Directly raises Digital Sovereignty without raising build cost.
- **Tower & Moat / "Restrict movement"** on DNS-over-HTTPS — nation-states either co-opt or block DoH, because it removes the traditional DNS-based choke point.
- **Directed investment** on Telecoms Expertise (Knowledge layer) — the scarcest resource; without it all other plays hollow out.

### e. Doctrine observations

- **Multiple anchors declared** — matches Phase II doctrine "know your users." Good.
- **Knowledge layer present** (Telecoms Expertise, Standards Bodies) — satisfies "understand what is being considered" and avoids the common failure mode of mapping only activities.
- **Component types τ** not explicitly annotated. If added: Awareness items are Practices (P), Standards Bodies is Knowledge (K), Supply Chains are Data/Activity hybrids, physical stack is all Activity (A). Practice–activity co-evolution is visible in the Nation-State-Firewall ↔ Digital Sovereignty pair.
- **Missing on this pass:** explicit climate pattern list (peace-war-wonder cycle, chasms, commoditisation pressure). The 2022 scenario has a very clear "Wonder" signal in LEO satellites and a "War" signal in supply-chain decoupling — a full pass would annotate those.

## 7. Where telecoms is truly sovereign-controllable vs foreign-dependent

**Sovereign-controllable (high ν, low-to-moderate ε, governable by policy):**
- Territorial / Political / Cultural sovereignty pillars themselves.
- Nation-State Firewall, Geofencing, SIM/eSIM issuance policy.
- Peering policy and national IXPs.
- Network topology decisions (landing points, route diversity, dark fibre).
- Spectrum allocation (not drawn separately but implicit under Mobile Towers).

**Foreign-dependent chokepoints (low ν, high ε — commoditised but foreign-owned):**
- Compute silicon (TSMC, Samsung, Intel) and EDA tooling.
- Launch vehicles and LEO constellations (US-dominated in Oct 2022).
- Network equipment vendor oligopoly (three vendors, none sovereign for most nations).
- Submarine cable manufacture and repair ships (ASN, SubCom, NEC).
- Physical supply chain for rare earths and specialty materials.

**In-transition zones where sovereignty is actively contested (ε in transition):**
- Satellite Access — Starlink changed the map materially in Feb–Oct 2022.
- Supply chains — decoupling is underway but incomplete.
- DNS-over-HTTPS — sovereignty is being asserted but without consensus mechanism.
- IoT Devices — security + origin-of-component debate active.

## 8. Caveats

- This is a prompt-only baseline: no tool use, no validator, no iterative refinement.
- Evolution scores are single-pass 4-row estimates; full 19-row scoring would shift some values by one band.
- Inertia form annotations are informal — only Copper Last-Mile is explicitly flagged.
- The map does not forecast evolution over time (per the prompt's instruction and Wardley's climatic pattern that evolution cannot be measured over time).
