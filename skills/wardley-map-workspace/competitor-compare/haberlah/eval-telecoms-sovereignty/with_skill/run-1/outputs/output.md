# Wardley Map Analysis: Telecoms Sovereignty (Nation-State Perspective, October 2022)

## Purpose

Given the nation-state as the mapping unit in October 2022, this map answers: **where is the telecoms stack truly sovereign-controllable, and where does the chain depend on foreign actors?** The map is built to inform sovereignty policy — doctrine for spectrum, cables, devices, control plane, compute and launch — rather than a single build/buy decision.

## Strategic Context (Step 1)

- **Strategic question:** Where does a nation state retain real levers over its telecoms chain, and where does foreign control make sovereignty aspirational rather than real?
- **User anchors (four):** Government, The Collective (civil society / the national public as an interest group), Corporations, People. All four depend on the same stack, but with different weightings.
- **Core needs:** the six sovereignty pillars — Territorial, Political, Cultural, Economic, Digital, and Critical National Infrastructure (CNI) sovereignty.
- **Scope boundary:** a single nation-state's telecoms value chain in October 2022, end-to-end: user anchors -> sovereignty pillars -> theatre and supply-chain awareness -> access devices -> control layer -> fixed/mobile topology -> access networks -> network equipment -> foundations (geography, supply chains, compute, power, space, spectrum) -> expertise and peering.

The map is deliberately larger than the 8-15 sweet spot in SKILL.md (29 non-anchor components, 4 anchors). The scenario brief explicitly lists the components to include across six pillars and multiple layers; splitting into submaps was considered, but the whole point of the request is to show the cross-layer dependency structure on a single canvas. This trade-off is flagged in the doctrine check below.

## Component Evolution Assessment (Step 3)

| Component | Stage | Position [vis, mat] | Rationale |
|---|---|---|---|
| Government (anchor) | User | [0.97, 0.60] | Sovereign anchor — sets policy and legitimises force. |
| The Collective (anchor) | User | [0.97, 0.54] | National public / civil society as an interest holder in sovereignty. |
| Corporations (anchor) | User | [0.97, 0.48] | Domestic corporates need sovereign telecoms for operations and IP protection. |
| People (anchor) | User | [0.97, 0.42] | Individual users — connectivity, speech, privacy, safety. |
| Territorial Sovereignty | Need | [0.90, 0.55] | Control of land, sea, air, space within borders. |
| Political Sovereignty | Need | [0.90, 0.50] | Domestic political process free from foreign interference. |
| Cultural Sovereignty | Need | [0.90, 0.45] | Language, media and narrative. |
| Economic Sovereignty | Need | [0.90, 0.40] | Ability to trade, tax, and protect domestic value creation. |
| Digital Sovereignty | Need | [0.90, 0.48] | Control over domestic digital traffic, identity and platforms. |
| CNI Sovereignty | Need | [0.90, 0.58] | Keeping critical telecoms functioning under duress. |
| Land-Sea-Air-Space Awareness | Product, inertia | [0.82, 0.55] | Mature C4ISR capability — multiple vendors (Thales, Lockheed, Leonardo, Saab) but incumbents create legacy inertia; not yet commodity. |
| Supply-Chain Awareness | Custom-Built | [0.82, 0.32] | SBOM, 5G supply-chain review, Huawei exclusion decisions were nascent in 2022 — practice still bespoke per nation. |
| Smartphones | Commodity | [0.73, 0.88] | iOS/Android duopoly, billions of devices, universally standardised — invisible until broken. |
| Computers | Commodity | [0.73, 0.85] | PC/laptop market fully commoditised; x86/ARM standards. |
| Radio and TV | Commodity | [0.73, 0.93] | Utility broadcast infrastructure; decades old, fully standardised. |
| Sat Phones | Product | [0.73, 0.58] | Multiple vendors (Iridium, Inmarsat, Thuraya, Globalstar); competitive market with feature differentiation, not universal. |
| IoT Devices | Product | [0.73, 0.62] | Highly fragmented but widely deployed (cellular, LoRa, Zigbee) — recognisable product market with dozens of vendors. |
| DNS-over-HTTPS | Product | [0.64, 0.65] | Standardised (RFC 8484, 2018), deployed by Cloudflare/Google/Mozilla by default in 2022 — actively evolving and politically contested. |
| Nation-State Firewall | Product | [0.64, 0.55] | Productised capability — vendors include Sandvine, Huawei, Thales; operated by China, Russia, Iran, Turkey; not universal, so not commodity. |
| SIMs / eSIM | Commodity | [0.64, 0.82] | GSMA-standardised; eSIM standard (GSMA RSP) widely deployed by 2022. Utility behaviour. |
| Geofencing | Product | [0.64, 0.60] | Mature capability across mobile networks and apps; multiple vendors; feature-competitive. |
| Fixed Network | Commodity | [0.55, 0.82] | Core IP/MPLS operations are utility; multiple kit vendors; standardised protocols. |
| Mobile Network | Commodity | [0.55, 0.82] | 4G mature, 5G well into rollout; 3GPP standards; operator-as-utility model globally. |
| Network Equipment | Product | [0.50, 0.78] | Oligopoly (Ericsson, Nokia, Huawei, Samsung, Cisco, Juniper) with feature and security competition — productised not commoditised. |
| Towers (RAN) | Commodity | [0.46, 0.80] | Tower infrastructure is utility; tower companies (Cellnex, American Tower) operate as commodity landlords. |
| Cable (Fibre / Subsea) | Commodity | [0.46, 0.84] | Subsea cable consortia, terrestrial fibre utility; standardised OTN/DWDM; dark fibre tradable. |
| Satellite Broadband | Product | [0.46, 0.55] | Starlink crossed 500k subs and LEO commercial broadband reached product stage in 2022 — evolving fast toward commodity, multiple entrants (OneWeb, Kuiper planned). |
| Launch Vehicles | Product | [0.38, 0.52] | SpaceX reusable-rocket dominant, but Arianespace, ULA, Rocket Lab, ISRO, Roscosmos, CNSA compete — competitive market with featured comparison, not commodity. |
| Expertise | Custom-Built, inertia | [0.40, 0.30] | Telecom RF engineers, spectrum lawyers, packet-core architects — decade-long training, scarce, tacit knowledge; sovereign pipelines where they exist. |
| Peering / IXPs | Commodity | [0.40, 0.90] | LINX, DE-CIX, AMS-IX and hundreds more; BGP fully standardised; peering is utility. |
| Physical Supply Chain | Product, inertia | [0.22, 0.70] | Concentrated (TSMC, ASML, container shipping, rare-earth refining in PRC) — mature structure but with heavy foreign concentration that creates inertia when re-shoring is attempted. |
| Information Supply Chain | Custom-Built, inertia | [0.22, 0.32] | Software/firmware supply chain discipline still emerging in 2022 (SBOM, SLSA, attestations) — each nation building bespoke practice. |
| Compute | Commodity | [0.18, 0.88] | Cloud compute is the canonical Wardley utility. AWS/Azure/GCP dominate; national clouds exist but usually ride hyperscaler kit. |
| Fab / Semiconductor Capability | Custom-Built, inertia | [0.18, 0.30] | Leading-edge fab = ASML EUV + TSMC/Samsung/Intel; US CHIPS Act and EU Chips Act were announced 2022 — nations explicitly treating this as custom-build-again. |
| Power | Commodity | [0.10, 0.92] | Grid electricity is the textbook utility. |
| Geography | Commodity | [0.06, 0.98] | The physical landmass, EEZ and airspace — the one truly sovereign asset, and therefore placed at maximum maturity: it does not evolve. |
| Orbital Slots & Spectrum | Product | [0.28, 0.50] | ITU-allocated; increasingly contested in 2022 (LEO congestion, 5G mid-band); treated as a product resource with clear buyers and sellers (auctions). |

## Key Strategic Observations (Step 7)

1. **Only Geography is genuinely sovereign.** Everything else in this map — even power and peering — is tradable, outsourced, or dependent on at least one foreign choke-point. The map's shape clusters commodity components (`Compute`, `Power`, `Peering`, `Cable`, `Smartphones`, `Computers`, `Radio and TV`, `SIMs`, `Towers`) across the right-hand column with no domestic producers for most of them — this is the telecoms sovereignty illusion in graphical form.

2. **The real sovereign levers sit in the control layer, not the physical layer.** `Nation-State Firewall`, `Geofencing`, `DNS-over-HTTPS` policy, and `SIMs/eSIM` (issuance, identification, lawful intercept) are where a nation can act unilaterally in months, without replacing the physical stack. These are Product-stage components that can be turned on with policy and vendor relationships, not factories.

3. **Three foreign-dependency chokepoints dominate the foundation layer:** (i) `Fab / Semiconductor Capability` (ASML + TSMC/Samsung), (ii) `Cable (Fibre / Subsea)` (consortium-owned, foreign-flagged ships, geographically vulnerable), and (iii) `Launch Vehicles` (SpaceX concentration). In October 2022 these were the focal points of CHIPS Act / EU Chips Act / undersea cable resilience reviews and launch diversification — the map predicts and explains that simultaneity.

4. **LEO satellite broadband is actively eroding national control of access.** Starlink is a Product-stage component in 2022 evolving rapidly (evolve arrow to ~0.72). Every device that can bypass `Towers (RAN)` and `Cable` via direct LEO link escapes `Nation-State Firewall`, `Geofencing`, and domestic `Peering / IXPs`. This is a structural threat to Digital and Political Sovereignty that ground-based inertia cannot defend against.

5. **Awareness and Expertise are the load-bearing inertia items.** `Land-Sea-Air-Space Awareness`, `Supply-Chain Awareness` and `Expertise` are where most nations are either under-invested or locked into legacy primes. The map shows that weakness here silently nullifies every downstream control-layer capability — you cannot enforce sovereignty you cannot see, with people you do not have.

## Doctrine Check

Assessed against the 40-principle doctrine catalogue; the most impactful observations for this map:

- **Know your users (#1) and focus on user needs (#2).** The four anchors and six pillars explicitly satisfy this — the map is anchored in needs (sovereignty dimensions), not in technology.
- **Challenge assumptions (#6).** The map challenges the popular assumption that "national 5G" or "owning the telco" equals sovereignty. The real sovereignty surface is at the control layer and in awareness/expertise, not in the RAN.
- **Remove bias and duplication (#7).** Two forms visible: (a) multiple nations independently rebuilding `Nation-State Firewall` and `Supply-Chain Awareness` — candidate for alliance-level co-opting; (b) `Fixed Network` and `Mobile Network` are drawn as separate components but share `Network Equipment`, `Peering`, and `Expertise` — that's legitimate, not duplication.
- **Use appropriate methods (#9).** Nations treating `Fab` and `Expertise` as if they were Commodity (just buy them) are making a method mismatch. These are Custom-Built — they require patient Settler/Pioneer investment, not procurement.
- **Manage inertia (#19).** The inertia markers on `Land-Sea-Air-Space Awareness`, `Expertise`, `Physical Supply Chain`, `Information Supply Chain`, and `Fab` are the map's primary doctrine warning: these are exactly where sovereignty fails silently.
- **Map readability (pragmatism, #12).** At 29 non-anchor components the map is above the 18-component warning threshold — this is a deliberate trade-off to keep the cross-layer dependency structure visible on one canvas, as requested. A follow-up pass would split `Supply-Chain Awareness` and `Control Layer` into submaps.

## Recommended Actions

Prioritised, with reference to map positions:

1. **Invest in sovereign control-layer capability before sovereign fab.** `Nation-State Firewall` (0.64, 0.55), `DNS-over-HTTPS policy` (0.64, 0.65), and `Geofencing` (0.64, 0.60) are Product-stage — achievable in 12-24 months via procurement + policy. `Fab` is a 10-year bet. Sequence matters.

2. **Treat `Expertise` (0.40, 0.30) as the single most underpriced asset.** Stand up multi-decade RF, spectrum-law, packet-core, cryptography and supply-chain assurance training pipelines. Without domestic Settlers and Town Planners, every downstream investment is captured by foreign consultants.

3. **Plan for Starlink-class LEO bypass, not against it.** The `Satellite Broadband` evolution arrow to 0.72 means sovereignty via ground-based chokepoints is a wasting asset. Invest in lawful-intercept at the ground-station and user-terminal level, and in domestic/alliance LEO.

4. **Diversify subsea cable and launch.** `Cable (Fibre / Subsea)` at Commodity (0.46, 0.84) hides extreme geographic concentration; and `Launch Vehicles` (0.38, 0.52) sit on a SpaceX-shaped asymmetry. Cable landings protection, alternate routes via allied states, and alliance-level launch capacity are sovereignty, not optional.

5. **Invest in Supply-Chain Awareness as a discipline, not a tool purchase.** SBOM + hardware BOM + vendor attestation + origin verification is Custom-Built in 2022 and should be built (not bought) with the evolution arrow to ~0.48 over two years.

## Build vs. Buy Assessment

| Component | Recommendation | Rationale |
|---|---|---|
| Nation-State Firewall | Build (or controlled-vendor) | Sovereign lever that cannot be outsourced; Product-stage means kit exists but policy and operation must be domestic. |
| Supply-Chain Awareness | Build | Custom-Built; each nation's threat model and vendor set is unique. Buying a generic tool fails the sovereignty test. |
| Land-Sea-Air-Space Awareness | Build (with allied co-development) | Product-stage but inertia-heavy. Pure buy locks in foreign primes. |
| Expertise | Build | There is no buy option — scarce global talent pool, decade-long pipelines. |
| Smartphones, Computers, SIMs/eSIM | Buy | True commodity. No sovereignty gain from attempting to rebuild. |
| Peering / IXPs, Power, Geography | Buy / already sovereign | Utilities or geographic given. |
| Launch Vehicles | Outsource carefully | Product; maintain multiple supplier relationships; do not become single-vendor dependent. |
| Compute | Outsource with caveats | Commodity hyperscaler cloud is efficient; sovereign cloud residency and key control must be contracted explicitly. |
| Fab / Semiconductor Capability | Build (multi-decade) | Custom-Built; alliance-level investment required (CHIPS/EU Chips Act pattern in 2022). |
| Satellite Broadband | Build + Buy | Product evolving to Commodity; access commercial LEO while investing in sovereign/allied constellations to avoid single-vendor capture. |

## Evolution Predictions (12-24 months, from October 2022)

- `Satellite Broadband` → 0.72 (crossing into Commodity as Starlink scales and OneWeb completes initial constellation).
- `Launch Vehicles` → 0.68 (SpaceX cadence + Rocket Lab + Chinese commercial launchers push toward commodity).
- `DNS-over-HTTPS` → 0.78 (browser-default rollout continues; becomes invisible to users — a Commodity control-layer primitive, making sovereign control harder).
- `Supply-Chain Awareness` → 0.48 (SBOM and secure-by-design frameworks mature from bespoke to product stage).
- `IoT Devices` → 0.78 (cellular IoT, Matter/Thread and eSIM adoption push the fragmentation downward).
- `Nation-State Firewall` → 0.68 (productisation accelerates as more nations adopt them; vendor market consolidates).

Inertia that will slow evolution: `Fab`, `Physical Supply Chain`, `Information Supply Chain`, `Expertise`, `Land-Sea-Air-Space Awareness` — explicitly flagged.

## Open Questions

1. **Where does alliance-level co-opting beat national self-sufficiency?** `Fab`, `Launch`, `Cable` and `Supply-Chain Awareness` may all be better addressed at alliance scale (Five Eyes, EU, Quad) than solo.
2. **Is `Digital Sovereignty` defensible against LEO bypass without either domestic constellations or enforcement at user-terminal level?** The map implies not, but the policy implications deserve dedicated treatment.
3. **How should `Information Supply Chain` sovereignty interact with open-source dependency?** Most nation-state telecom software now depends on foreign-hosted open-source — this is invisible on the map as currently drawn, and is a candidate submap.

---

## OWM (OnlineWardleyMaps) Text Block

```
title Telecoms Sovereignty — Nation-State Perspective (October 2022)
style wardley

// Anchors: four user groups that depend on sovereign telecoms
anchor Government [0.97, 0.60]
anchor The Collective [0.97, 0.54]
anchor Corporations [0.97, 0.48]
anchor People [0.97, 0.42]

// Sovereignty pillars — the needs the anchors have
component Territorial Sovereignty [0.90, 0.55]
component Political Sovereignty [0.90, 0.50]
component Cultural Sovereignty [0.90, 0.45]
component Economic Sovereignty [0.90, 0.40]
component Digital Sovereignty [0.90, 0.48]
component CNI Sovereignty [0.90, 0.58]

// Theatre / awareness layer
component Land-Sea-Air-Space Awareness [0.82, 0.55] inertia
component Supply-Chain Awareness [0.82, 0.32]

// Access devices
component Smartphones [0.73, 0.88]
component Computers [0.73, 0.85]
component Radio and TV [0.73, 0.93]
component Sat Phones [0.73, 0.58]
component IoT Devices [0.73, 0.62]

// Control layer
component DNS-over-HTTPS [0.64, 0.65]
component Nation-State Firewall [0.64, 0.55]
component SIMs / eSIM [0.64, 0.82]
component Geofencing [0.64, 0.60]

// Network topology
component Fixed Network [0.55, 0.82]
component Mobile Network [0.55, 0.82]

// Access networks (transport)
component Towers (RAN) [0.46, 0.80]
component Cable (Fibre / Subsea) [0.46, 0.84]
component Satellite Broadband [0.46, 0.55]
component Launch Vehicles [0.38, 0.52]

// Network equipment
component Network Equipment [0.50, 0.78]

// Expertise and peering
component Expertise [0.40, 0.30] inertia
component Peering / IXPs [0.40, 0.90]

// Reality / foundations
component Physical Supply Chain [0.22, 0.70] inertia
component Information Supply Chain [0.22, 0.32] inertia
component Compute [0.18, 0.88]
component Fab / Semiconductor Capability [0.18, 0.30] inertia
component Power [0.10, 0.92]
component Geography [0.06, 0.98]
component Orbital Slots & Spectrum [0.28, 0.50]

// Anchor -> pillar dependencies
Government->Territorial Sovereignty
Government->Political Sovereignty
Government->CNI Sovereignty
Government->Digital Sovereignty
The Collective->Cultural Sovereignty
The Collective->Political Sovereignty
Corporations->Economic Sovereignty
Corporations->Digital Sovereignty
People->Cultural Sovereignty
People->Digital Sovereignty

// Pillar -> awareness / control
Territorial Sovereignty->Land-Sea-Air-Space Awareness
CNI Sovereignty->Land-Sea-Air-Space Awareness
CNI Sovereignty->Supply-Chain Awareness
Economic Sovereignty->Supply-Chain Awareness
Digital Sovereignty->DNS-over-HTTPS
Digital Sovereignty->Nation-State Firewall
Political Sovereignty->Nation-State Firewall
Political Sovereignty->Geofencing
Cultural Sovereignty->Geofencing

// Awareness -> devices / networks
Land-Sea-Air-Space Awareness->Satellite Broadband
Land-Sea-Air-Space Awareness->Sat Phones
Land-Sea-Air-Space Awareness->IoT Devices
Supply-Chain Awareness->Information Supply Chain
Supply-Chain Awareness->Physical Supply Chain

// Pillars -> devices (user-facing)
Cultural Sovereignty->Radio and TV
Cultural Sovereignty->Smartphones
Economic Sovereignty->Computers
Economic Sovereignty->Smartphones

// Control layer -> networks
DNS-over-HTTPS->Fixed Network
DNS-over-HTTPS->Mobile Network
Nation-State Firewall->Fixed Network
Nation-State Firewall->Mobile Network
Geofencing->Mobile Network
SIMs / eSIM->Mobile Network

// Devices -> networks
Smartphones->Mobile Network
Smartphones->SIMs / eSIM
Computers->Fixed Network
Radio and TV->Cable (Fibre / Subsea)
Sat Phones->Satellite Broadband
IoT Devices->Mobile Network
IoT Devices->Fixed Network

// Networks -> transport
Fixed Network->Cable (Fibre / Subsea)
Fixed Network->Network Equipment
Fixed Network->Peering / IXPs
Mobile Network->Towers (RAN)
Mobile Network->Network Equipment
Mobile Network->Peering / IXPs
Satellite Broadband->Launch Vehicles

// Transport -> foundations
Towers (RAN)->Power
Towers (RAN)->Geography
Cable (Fibre / Subsea)->Geography
Cable (Fibre / Subsea)->Power
Satellite Broadband->Orbital Slots & Spectrum
Launch Vehicles->Orbital Slots & Spectrum
Network Equipment->Physical Supply Chain
Network Equipment->Information Supply Chain
Peering / IXPs->Fixed Network

// Everything needs compute, power, geography, expertise
Network Equipment->Compute
Compute->Fab / Semiconductor Capability
Compute->Power
Fab / Semiconductor Capability->Physical Supply Chain
Physical Supply Chain->Geography
Information Supply Chain->Expertise
Land-Sea-Air-Space Awareness->Expertise
Supply-Chain Awareness->Expertise
Nation-State Firewall->Expertise
DNS-over-HTTPS->Expertise

// Evolution arrows (predicted 12-24 months)
evolve Satellite Broadband 0.72
evolve Launch Vehicles 0.68
evolve DNS-over-HTTPS 0.78
evolve Supply-Chain Awareness 0.48
evolve IoT Devices 0.78
evolve Nation-State Firewall 0.68

// Build/Buy indicators
build Nation-State Firewall
build Supply-Chain Awareness
build Land-Sea-Air-Space Awareness
build Expertise
buy Smartphones
buy Computers
buy SIMs / eSIM
buy Peering / IXPs
buy Power
outsource Launch Vehicles
outsource Compute

// Annotations
annotation 1 [[0.64, 0.55]] Sovereign levers: firewalls, geofencing, DoH policy
annotation 2 [[0.22, 0.70]] Foreign-dependent: fabs, subsea cable, launch
annotation 3 [[0.06, 0.98]] Geography — the only truly sovereign asset
annotation 4 [[0.46, 0.55]] LEO constellations erode sovereign control of access
```

Paste this into [onlinewardleymaps.com](https://onlinewardleymaps.com), the VS Code OnlineWardleyMaps extension, or the Obsidian plugin to render.

---

## Interactive React Artifact (.jsx)

Renderable React component with inline SVG, hover tooltips (component name + stage + rationale), click-to-highlight dependency chain, evolution-stage shading, inertia markers, evolution arrows, and figure legend. Drop this into a React artifact surface or any CRA/Vite shell.

```jsx
import { useState, useCallback, useMemo } from "react";

// ============================================================
// 1. CONSTANTS (from style-constants.json, inlined)
// ============================================================
const WIDTH = 1200;
const HEIGHT = 860;
const PADDING = { top: 55, right: 30, bottom: 110, left: 80 };

const COLORS = {
  background: "#ffffff",
  stageFills: ["#fef9f0", "#fefcf7", "#f7faf7", "#f0f6fe"],
  gridLine: "#e2e2e2",
  axisLine: "#555555",
  axisLabel: "#666666",
  stageLabel: "#888888",
  componentFill: "#ffffff",
  componentStroke: "#333333",
  componentStrokeSelected: "#1a73e8",
  anchorFill: "#1a1a2e",
  anchorStroke: "#1a1a2e",
  anchorLabel: "#ffffff",
  dependencyLine: "#aaaaaa",
  dependencyLineSelected: "#1a73e8",
  evolutionArrow: "#d94040",
  inertiaBar: "#333333",
  pipelineFill: "rgba(180,180,180,0.12)",
  pipelineStroke: "#bbbbbb",
  tooltipBg: "#1a1a2e",
  tooltipText: "#f0f0f0",
  legendBorder: "#dddddd",
  title: "#1a1a1a",
  labelText: "#222222",
  dimmedOpacity: 0.15
};

const FONTS = {
  title: "16px 'Segoe UI', system-ui, -apple-system, sans-serif",
  axisLabel: "12px 'Segoe UI', system-ui, sans-serif",
  stageLabel: "11px 'Segoe UI', system-ui, sans-serif",
  componentLabel: "11px 'Segoe UI', system-ui, sans-serif",
  tooltip: "12px 'Segoe UI', system-ui, sans-serif",
  legend: "10px 'Segoe UI', system-ui, sans-serif"
};

const STAGE_BOUNDARIES = [0.25, 0.50, 0.75];
const STAGE_LABELS = ["Genesis", "Custom-Built", "Product (+Rental)", "Commodity (+Utility)"];

function toSvgX(m) { return PADDING.left + m * (WIDTH - PADDING.left - PADDING.right); }
function toSvgY(v) { return PADDING.top + (1 - v) * (HEIGHT - PADDING.top - PADDING.bottom); }

// ============================================================
// 2. MAP DATA
// ============================================================
const MAP = {
  title: "Telecoms Sovereignty — Nation-State Perspective (October 2022)",
  purpose: "Where telecoms is truly sovereign-controllable, and where the chain depends on foreign actors.",
  components: [
    // Anchors
    { id: "government", name: "Government", visibility: 0.97, maturity: 0.60, stage: "User", rationale: "Sovereign anchor — sets policy and legitimises force.", isAnchor: true },
    { id: "collective", name: "The Collective", visibility: 0.97, maturity: 0.54, stage: "User", rationale: "National public / civil society as a sovereignty stakeholder.", isAnchor: true },
    { id: "corporations", name: "Corporations", visibility: 0.97, maturity: 0.48, stage: "User", rationale: "Domestic corporates need sovereign telecoms for operations and IP.", isAnchor: true },
    { id: "people", name: "People", visibility: 0.97, maturity: 0.42, stage: "User", rationale: "Individual users — connectivity, speech, privacy, safety.", isAnchor: true },

    // Pillars
    { id: "cni-sov", name: "CNI Sovereignty", visibility: 0.90, maturity: 0.58, stage: "Need", rationale: "Critical telecoms functioning under duress." },
    { id: "terr-sov", name: "Territorial Sovereignty", visibility: 0.90, maturity: 0.55, stage: "Need", rationale: "Control of land, sea, air, space within borders." },
    { id: "pol-sov", name: "Political Sovereignty", visibility: 0.90, maturity: 0.50, stage: "Need", rationale: "Domestic political process free from foreign interference." },
    { id: "dig-sov", name: "Digital Sovereignty", visibility: 0.90, maturity: 0.48, stage: "Need", rationale: "Control over domestic digital traffic, identity, platforms." },
    { id: "cul-sov", name: "Cultural Sovereignty", visibility: 0.90, maturity: 0.45, stage: "Need", rationale: "Language, media, narrative sovereignty." },
    { id: "econ-sov", name: "Economic Sovereignty", visibility: 0.90, maturity: 0.40, stage: "Need", rationale: "Ability to trade, tax, and protect value creation." },

    // Awareness
    { id: "lsas-aware", name: "Land-Sea-Air-Space Awareness", visibility: 0.82, maturity: 0.55, stage: "Product", rationale: "Mature C4ISR — Thales/Lockheed/Leonardo/Saab — but with legacy inertia.", inertia: true },
    { id: "sc-aware", name: "Supply-Chain Awareness", visibility: 0.82, maturity: 0.32, stage: "Custom-Built", rationale: "SBOM, 5G supply-chain reviews still bespoke per nation in 2022." },

    // Devices
    { id: "smartphones", name: "Smartphones", visibility: 0.73, maturity: 0.88, stage: "Commodity", rationale: "iOS/Android duopoly, universally standardised." },
    { id: "computers", name: "Computers", visibility: 0.73, maturity: 0.85, stage: "Commodity", rationale: "Fully commoditised PC/laptop market; x86/ARM standards." },
    { id: "radio-tv", name: "Radio and TV", visibility: 0.73, maturity: 0.93, stage: "Commodity", rationale: "Utility broadcast, decades old, fully standardised." },
    { id: "sat-phones", name: "Sat Phones", visibility: 0.73, maturity: 0.58, stage: "Product", rationale: "Iridium, Inmarsat, Thuraya, Globalstar — competitive, not universal." },
    { id: "iot", name: "IoT Devices", visibility: 0.73, maturity: 0.62, stage: "Product", rationale: "Widely deployed, fragmented (cellular/LoRa/Zigbee) — product market." },

    // Control layer
    { id: "doh", name: "DNS-over-HTTPS", visibility: 0.64, maturity: 0.65, stage: "Product", rationale: "RFC 8484, deployed by Cloudflare/Google/Mozilla; actively contested." },
    { id: "ns-firewall", name: "Nation-State Firewall", visibility: 0.64, maturity: 0.55, stage: "Product", rationale: "Productised: Sandvine/Huawei/Thales; operated by China/Russia/Iran/Turkey." },
    { id: "geofence", name: "Geofencing", visibility: 0.64, maturity: 0.60, stage: "Product", rationale: "Mature capability across mobile networks and apps; multiple vendors." },
    { id: "sims", name: "SIMs / eSIM", visibility: 0.64, maturity: 0.82, stage: "Commodity", rationale: "GSMA-standardised; eSIM (RSP) widely deployed by 2022." },

    // Topology
    { id: "fixed-net", name: "Fixed Network", visibility: 0.55, maturity: 0.82, stage: "Commodity", rationale: "Core IP/MPLS is utility; standardised protocols." },
    { id: "mobile-net", name: "Mobile Network", visibility: 0.55, maturity: 0.82, stage: "Commodity", rationale: "4G mature, 5G well into rollout; 3GPP standards." },

    // Network equipment
    { id: "net-eq", name: "Network Equipment", visibility: 0.50, maturity: 0.78, stage: "Product", rationale: "Ericsson/Nokia/Huawei/Samsung/Cisco oligopoly — feature and security competition." },

    // Transport
    { id: "towers", name: "Towers (RAN)", visibility: 0.46, maturity: 0.80, stage: "Commodity", rationale: "Tower companies (Cellnex, American Tower) operate as commodity landlords." },
    { id: "cable", name: "Cable (Fibre / Subsea)", visibility: 0.46, maturity: 0.84, stage: "Commodity", rationale: "Subsea consortia, fibre utility, standardised OTN/DWDM." },
    { id: "satbb", name: "Satellite Broadband", visibility: 0.46, maturity: 0.55, stage: "Product", rationale: "Starlink at product stage Oct 2022, OneWeb/Kuiper entering — evolving fast.", evolveTo: 0.72 },
    { id: "launch", name: "Launch Vehicles", visibility: 0.38, maturity: 0.52, stage: "Product", rationale: "SpaceX dominant; Arianespace, ULA, Rocket Lab, ISRO, Roscosmos compete.", evolveTo: 0.68 },

    // Expertise/peering
    { id: "expertise", name: "Expertise", visibility: 0.40, maturity: 0.30, stage: "Custom-Built", rationale: "RF/spectrum/packet-core experts — scarce, tacit, decade-long training.", inertia: true },
    { id: "peering", name: "Peering / IXPs", visibility: 0.40, maturity: 0.90, stage: "Commodity", rationale: "LINX, DE-CIX, AMS-IX; BGP is utility." },

    // Foundations
    { id: "orbital", name: "Orbital Slots & Spectrum", visibility: 0.28, maturity: 0.50, stage: "Product", rationale: "ITU-allocated, auctioned; contested by LEO congestion and 5G mid-band." },
    { id: "phys-sc", name: "Physical Supply Chain", visibility: 0.22, maturity: 0.70, stage: "Product", rationale: "TSMC/ASML/container shipping/PRC rare-earths — concentrated, inertia-heavy.", inertia: true },
    { id: "info-sc", name: "Information Supply Chain", visibility: 0.22, maturity: 0.32, stage: "Custom-Built", rationale: "SBOM/SLSA attestations emerging in 2022 — bespoke per nation.", inertia: true },
    { id: "compute", name: "Compute", visibility: 0.18, maturity: 0.88, stage: "Commodity", rationale: "AWS/Azure/GCP; national clouds usually ride hyperscaler kit." },
    { id: "fab", name: "Fab / Semiconductor Capability", visibility: 0.18, maturity: 0.30, stage: "Custom-Built", rationale: "ASML EUV + TSMC/Samsung/Intel; CHIPS Act + EU Chips Act both 2022.", inertia: true },
    { id: "power", name: "Power", visibility: 0.10, maturity: 0.92, stage: "Commodity", rationale: "Grid electricity — textbook utility." },
    { id: "geography", name: "Geography", visibility: 0.06, maturity: 0.98, stage: "Commodity", rationale: "Landmass, EEZ, airspace — the only truly sovereign asset, does not evolve." }
  ],
  links: [
    { from: "government", to: "terr-sov" },
    { from: "government", to: "pol-sov" },
    { from: "government", to: "cni-sov" },
    { from: "government", to: "dig-sov" },
    { from: "collective", to: "cul-sov" },
    { from: "collective", to: "pol-sov" },
    { from: "corporations", to: "econ-sov" },
    { from: "corporations", to: "dig-sov" },
    { from: "people", to: "cul-sov" },
    { from: "people", to: "dig-sov" },

    { from: "terr-sov", to: "lsas-aware" },
    { from: "cni-sov", to: "lsas-aware" },
    { from: "cni-sov", to: "sc-aware" },
    { from: "econ-sov", to: "sc-aware" },
    { from: "dig-sov", to: "doh" },
    { from: "dig-sov", to: "ns-firewall" },
    { from: "pol-sov", to: "ns-firewall" },
    { from: "pol-sov", to: "geofence" },
    { from: "cul-sov", to: "geofence" },

    { from: "lsas-aware", to: "satbb" },
    { from: "lsas-aware", to: "sat-phones" },
    { from: "lsas-aware", to: "iot" },
    { from: "sc-aware", to: "info-sc" },
    { from: "sc-aware", to: "phys-sc" },

    { from: "cul-sov", to: "radio-tv" },
    { from: "cul-sov", to: "smartphones" },
    { from: "econ-sov", to: "computers" },
    { from: "econ-sov", to: "smartphones" },

    { from: "doh", to: "fixed-net" },
    { from: "doh", to: "mobile-net" },
    { from: "ns-firewall", to: "fixed-net" },
    { from: "ns-firewall", to: "mobile-net" },
    { from: "geofence", to: "mobile-net" },
    { from: "sims", to: "mobile-net" },

    { from: "smartphones", to: "mobile-net" },
    { from: "smartphones", to: "sims" },
    { from: "computers", to: "fixed-net" },
    { from: "radio-tv", to: "cable" },
    { from: "sat-phones", to: "satbb" },
    { from: "iot", to: "mobile-net" },
    { from: "iot", to: "fixed-net" },

    { from: "fixed-net", to: "cable" },
    { from: "fixed-net", to: "net-eq" },
    { from: "fixed-net", to: "peering" },
    { from: "mobile-net", to: "towers" },
    { from: "mobile-net", to: "net-eq" },
    { from: "mobile-net", to: "peering" },
    { from: "satbb", to: "launch" },

    { from: "towers", to: "power" },
    { from: "towers", to: "geography" },
    { from: "cable", to: "geography" },
    { from: "cable", to: "power" },
    { from: "satbb", to: "orbital" },
    { from: "launch", to: "orbital" },
    { from: "net-eq", to: "phys-sc" },
    { from: "net-eq", to: "info-sc" },
    { from: "peering", to: "fixed-net" },

    { from: "net-eq", to: "compute" },
    { from: "compute", to: "fab" },
    { from: "compute", to: "power" },
    { from: "fab", to: "phys-sc" },
    { from: "phys-sc", to: "geography" },
    { from: "info-sc", to: "expertise" },
    { from: "lsas-aware", to: "expertise" },
    { from: "sc-aware", to: "expertise" },
    { from: "ns-firewall", to: "expertise" },
    { from: "doh", to: "expertise" }
  ],
  evolutions: [
    { componentId: "satbb", toMaturity: 0.72 },
    { componentId: "launch", toMaturity: 0.68 },
    { componentId: "doh", toMaturity: 0.78 },
    { componentId: "sc-aware", toMaturity: 0.48 },
    { componentId: "iot", toMaturity: 0.78 },
    { componentId: "ns-firewall", toMaturity: 0.68 }
  ]
};

// ============================================================
// 3. COMPONENT
// ============================================================
export default function WardleyMapArtifact() {
  const [hovered, setHovered] = useState(null);
  const [selected, setSelected] = useState(null);

  const byId = useMemo(() => {
    const m = {};
    MAP.components.forEach(c => { m[c.id] = c; });
    return m;
  }, []);

  // Compute full dependency chain (upstream + downstream) for a selected id
  const chain = useMemo(() => {
    if (!selected) return null;
    const up = new Set([selected]);
    const down = new Set([selected]);
    const stepUp = id => MAP.links.filter(l => l.to === id).forEach(l => { if (!up.has(l.from)) { up.add(l.from); stepUp(l.from); } });
    const stepDown = id => MAP.links.filter(l => l.from === id).forEach(l => { if (!down.has(l.to)) { down.add(l.to); stepDown(l.to); } });
    stepUp(selected);
    stepDown(selected);
    const all = new Set([...up, ...down]);
    return all;
  }, [selected]);

  const isInChain = (id) => !chain || chain.has(id);
  const isLinkInChain = (l) => !chain || (chain.has(l.from) && chain.has(l.to));

  const handleComponentClick = useCallback((id, e) => {
    e.stopPropagation();
    setSelected(prev => prev === id ? null : id);
  }, []);

  const plotW = WIDTH - PADDING.left - PADDING.right;
  const plotH = HEIGHT - PADDING.top - PADDING.bottom;

  return (
    <div style={{ width: "100%", background: COLORS.background, fontFamily: "Segoe UI, system-ui, sans-serif" }}>
      <svg viewBox={`0 0 ${WIDTH} ${HEIGHT}`} width="100%" height="auto" onClick={() => setSelected(null)}>
        <defs>
          <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
            <path d="M 0 0 L 10 5 L 0 10 z" fill={COLORS.evolutionArrow} />
          </marker>
        </defs>

        {/* 1. Background */}
        <rect x="0" y="0" width={WIDTH} height={HEIGHT} fill={COLORS.background} />

        {/* 2. Stage fills */}
        {STAGE_LABELS.map((_, i) => {
          const x0 = i === 0 ? 0 : STAGE_BOUNDARIES[i - 1];
          const x1 = i === 3 ? 1 : STAGE_BOUNDARIES[i];
          return (
            <rect key={i}
              x={toSvgX(x0)} y={PADDING.top}
              width={toSvgX(x1) - toSvgX(x0)} height={plotH}
              fill={COLORS.stageFills[i]} />
          );
        })}

        {/* 3. Grid lines */}
        {STAGE_BOUNDARIES.map(b => (
          <line key={b} x1={toSvgX(b)} y1={PADDING.top} x2={toSvgX(b)} y2={HEIGHT - PADDING.bottom}
            stroke={COLORS.gridLine} strokeDasharray="4,4" />
        ))}

        {/* 4. Axes */}
        <line x1={PADDING.left} y1={PADDING.top} x2={PADDING.left} y2={HEIGHT - PADDING.bottom} stroke={COLORS.axisLine} />
        <line x1={PADDING.left} y1={HEIGHT - PADDING.bottom} x2={WIDTH - PADDING.right} y2={HEIGHT - PADDING.bottom} stroke={COLORS.axisLine} />
        <text x={15} y={PADDING.top + 10} fill={COLORS.axisLabel} style={{ font: FONTS.axisLabel }}>Visible</text>
        <text x={15} y={HEIGHT - PADDING.bottom - 2} fill={COLORS.axisLabel} style={{ font: FONTS.axisLabel }}>Invisible</text>
        {STAGE_LABELS.map((s, i) => {
          const x0 = i === 0 ? 0 : STAGE_BOUNDARIES[i - 1];
          const x1 = i === 3 ? 1 : STAGE_BOUNDARIES[i];
          const cx = toSvgX((x0 + x1) / 2);
          return (
            <text key={s} x={cx} y={HEIGHT - PADDING.bottom + 18} textAnchor="middle"
              fill={COLORS.stageLabel} style={{ font: FONTS.stageLabel }}>{s}</text>
          );
        })}

        {/* 5. Dependency lines */}
        {MAP.links.map((l, i) => {
          const a = byId[l.from]; const b = byId[l.to];
          if (!a || !b) return null;
          const ax = toSvgX(a.maturity), ay = toSvgY(a.visibility);
          const bx = toSvgX(b.maturity), by = toSvgY(b.visibility);
          const mx = (ax + bx) / 2, my = (ay + by) / 2 + 8;
          const inChain = isLinkInChain(l);
          return (
            <path key={i} d={`M ${ax} ${ay} Q ${mx} ${my} ${bx} ${by}`}
              fill="none"
              stroke={selected && inChain ? COLORS.dependencyLineSelected : COLORS.dependencyLine}
              strokeWidth={selected && inChain ? 1.6 : 1}
              opacity={selected && !inChain ? COLORS.dimmedOpacity : 0.9} />
          );
        })}

        {/* 6. Evolution arrows */}
        {MAP.evolutions.map((e, i) => {
          const c = byId[e.componentId];
          if (!c) return null;
          const x1 = toSvgX(c.maturity), x2 = toSvgX(e.toMaturity);
          const y = toSvgY(c.visibility);
          return (
            <line key={i} x1={x1 + 8} y1={y} x2={x2 - 2} y2={y}
              stroke={COLORS.evolutionArrow} strokeWidth={1.5} strokeDasharray="5,3"
              markerEnd="url(#arrow)"
              opacity={selected && !isInChain(c.id) ? COLORS.dimmedOpacity : 1} />
          );
        })}

        {/* 7. Inertia bars */}
        {MAP.components.filter(c => c.inertia).map(c => {
          const x = toSvgX(c.maturity), y = toSvgY(c.visibility);
          return (
            <line key={c.id} x1={x + 9} y1={y - 10} x2={x + 9} y2={y + 10}
              stroke={COLORS.inertiaBar} strokeWidth={3}
              opacity={selected && !isInChain(c.id) ? COLORS.dimmedOpacity : 1} />
          );
        })}

        {/* 8. Component circles */}
        {MAP.components.map(c => {
          const cx = toSvgX(c.maturity), cy = toSvgY(c.visibility);
          const dim = selected && !isInChain(c.id);
          const r = c.isAnchor ? 7 : 6;
          return (
            <g key={c.id}
              onMouseEnter={() => setHovered(c.id)}
              onMouseLeave={() => setHovered(null)}
              onClick={(e) => handleComponentClick(c.id, e)}
              style={{ cursor: "pointer" }}
              opacity={dim ? COLORS.dimmedOpacity : 1}>
              <circle cx={cx} cy={cy} r={r}
                fill={c.isAnchor ? COLORS.anchorFill : COLORS.componentFill}
                stroke={selected === c.id ? COLORS.componentStrokeSelected : (c.isAnchor ? COLORS.anchorStroke : COLORS.componentStroke)}
                strokeWidth={selected === c.id ? 2.5 : 1.5} />
            </g>
          );
        })}

        {/* 9. Labels */}
        {MAP.components.map(c => {
          const cx = toSvgX(c.maturity), cy = toSvgY(c.visibility);
          const dim = selected && !isInChain(c.id);
          // Simple label placement: right of circle, with y offset for dense clusters
          const dx = 10;
          const dy = 4;
          return (
            <text key={"l-" + c.id} x={cx + dx} y={cy + dy}
              fill={COLORS.labelText}
              style={{ font: FONTS.componentLabel }}
              opacity={dim ? COLORS.dimmedOpacity : 1}>
              {c.name}
            </text>
          );
        })}

        {/* 10. Title */}
        <text x={PADDING.left} y={30} fill={COLORS.title} style={{ font: FONTS.title, fontWeight: 600 }}>
          {MAP.title}
        </text>

        {/* 11. Legend */}
        <g transform={`translate(${WIDTH - 330}, ${HEIGHT - 95})`}>
          <rect x="0" y="0" width="320" height="85" fill="#ffffff" stroke={COLORS.legendBorder} />
          <text x="10" y="15" style={{ font: FONTS.legend, fontWeight: 600 }}>Legend</text>
          <circle cx="20" cy="32" r="5" fill="#fff" stroke={COLORS.componentStroke} strokeWidth="1.5" />
          <text x="32" y="35" style={{ font: FONTS.legend }}>Component</text>
          <circle cx="120" cy="32" r="6" fill={COLORS.anchorFill} />
          <text x="132" y="35" style={{ font: FONTS.legend }}>Anchor (user)</text>
          <line x1="220" y1="32" x2="250" y2="32" stroke={COLORS.dependencyLine} />
          <text x="256" y="35" style={{ font: FONTS.legend }}>Dependency</text>
          <line x1="20" y1="52" x2="50" y2="52" stroke={COLORS.evolutionArrow} strokeDasharray="5,3" markerEnd="url(#arrow)" />
          <text x="56" y="55" style={{ font: FONTS.legend }}>Evolution (12-24m)</text>
          <line x1="160" y1="47" x2="160" y2="57" stroke={COLORS.inertiaBar} strokeWidth="3" />
          <text x="168" y="55" style={{ font: FONTS.legend }}>Inertia</text>
          <text x="10" y="75" style={{ font: FONTS.legend, fontStyle: "italic", fill: "#666" }}>
            Click component to highlight its dependency chain
          </text>
        </g>

        {/* 12. Tooltip */}
        {hovered && (() => {
          const c = byId[hovered];
          if (!c) return null;
          const cx = toSvgX(c.maturity), cy = toSvgY(c.visibility);
          const boxW = 320, boxH = 70;
          const bx = Math.min(cx + 12, WIDTH - boxW - 4);
          const by = Math.max(cy - boxH - 8, PADDING.top + 4);
          return (
            <g>
              <rect x={bx} y={by} width={boxW} height={boxH} rx="4" fill={COLORS.tooltipBg} />
              <text x={bx + 10} y={by + 18} fill={COLORS.tooltipText} style={{ font: FONTS.tooltip, fontWeight: 600 }}>
                {c.name} {c.isAnchor ? "(anchor)" : ""} — {c.stage}
              </text>
              <foreignObject x={bx + 10} y={by + 24} width={boxW - 20} height={boxH - 30}>
                <div xmlns="http://www.w3.org/1999/xhtml"
                  style={{ color: COLORS.tooltipText, font: FONTS.tooltip, lineHeight: "1.25" }}>
                  {c.rationale}
                </div>
              </foreignObject>
            </g>
          );
        })()}
      </svg>
    </div>
  );
}
```

---

## Summary

The map answers the brief directly:

- **Truly sovereign:** Geography alone. Everything else is procured, outsourced, or built on a foreign dependency.
- **Sovereign-controllable without rebuilding the stack (12-24 months):** Nation-State Firewall, DNS-over-HTTPS policy, Geofencing, SIMs/eSIM issuance, Supply-Chain Awareness, and Peering / IXP policy. These are Product-stage levers.
- **Structurally foreign-dependent:** Fab/Semiconductor Capability, Compute (hyperscalers), Subsea Cable consortia, Launch Vehicles, Network Equipment kit vendors.
- **The quiet strategic lever:** Expertise — the map's most under-valued Custom-Built component, and the one that silently makes every control-layer capability real.
- **The Oct 2022 evolution threat:** LEO satellite broadband is moving toward Commodity fast enough to bypass ground-based sovereignty controls. Sovereignty policy built around RAN and fibre ignores this at its peril.
