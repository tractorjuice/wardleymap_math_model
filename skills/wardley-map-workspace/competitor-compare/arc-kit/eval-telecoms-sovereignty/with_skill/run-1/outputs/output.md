# Telecoms Sovereignty — Nation-State Perspective (October 2022)

**Anchor users:** Government, the Collective (civil society), Corporations (telcos / OEMs / platforms), People (citizens / subscribers)
**User need:** Maintain sovereign control of telecoms across six pillars — territorial, political, cultural, economic, digital, CNI.
**Date:** October 2022 (as per scenario); document generated 2026-04-22
**Scope:** The full communication stack (access devices, access networks, network equipment & topology, control layer, theatre/awareness, expertise, peering, and the underlying physical and informational reality) assessed from a single nation-state's point of view.

This is a **multi-anchor map**. The nation-state does not control the stack as a single owner — it has four constituencies whose claims on sovereignty overlap and conflict. The map is designed to show two things the scenario asks for: (1) where a nation can genuinely exercise sovereign control, and (2) where the chain depends on foreign actors it cannot compel.

---

## Visual Map

```text
Title: Telecoms Sovereignty — Nation-State Perspective (Oct 2022)
Anchor: Government / Collective / Corporations / People
Date: 2022-10

                    Genesis    Custom     Product    Commodity
                       │          │          │          │
Visible            ┌───┼──────────┼──────────┼──────────┼───┐
                   │   │          │          │          │   │
                   │   │  Collective ●        Gov ●   Corp ● People ●    (anchors)
                   │   │                                    │
                   │   │     Digital         Polit.  Econ.  │
                   │   │     Sov ●    Cult.  Sov ●   Sov ● Territ.
                   │   │              Sov ●                 │
                   │   │                   CNI ●            │
                   │   │                                    │
                   │   │                         Radio/TV ● │
                   │   │                         Smartphone ●
                   │   │                         PC ●       │
                   │   │                         SIM ●      │
                   │   │                   IoT ●            │
                   │   │              Sat Phone ●           │
                   │   │                                    │
                   │   │                         Towers ●   │
                   │   │                         Fibre ●    │
                   │   │                      Sub.Cable ●   │
                   │   │                      GEO Sat ●     │
                   │   │   LEO Constellation ●─────→        │
                   │   │       Launch (sov) ●──→            │
                   │   │           Launch (com) ●──→        │
                   │   │                                    │
                   │   │                   NEV ●            │
                   │   │                     Fixed Core ●   │
                   │   │                     Mobile Core ●  │
                   │   │   Open RAN ●──────→                │
                   │   │                        IXP ●       │
                   │   │                Peering ●           │
                   │   │                       Tier-1 ●     │
                   │   │                                    │
                   │   │   Control layer:                   │
                   │   │   NSF (firewall) ●──→              │
                   │   │                    L.I. ●          │
                   │   │              DoH ●────────→        │
                   │   │             Nat.DNS ●────→         │
                   │   │           Geofence ●───→           │
                   │   │                  SIM Reg ●──→      │
                   │   │              BGP Filter ●──→       │
                   │   │         Kill-switch ●──→           │
                   │   │             Takedown ●             │
                   │   │                                    │
                   │   │   Awareness:                       │
                   │   │   LSAS SA ●──→                     │
                   │   │   Sub.cable aware ●──→             │
                   │   │   SDA ●──→                         │
                   │   │ Supply intel ●──→                  │
                   │   │      Threat intel ●                │
                   │   │                                    │
                   │   │   Expertise:                       │
                   │   │       Tel.Eng.WF ●                 │
                   │   │         RF expertise ●             │
                   │   │   Semi design ●                    │
                   │   │           Crypto ●                 │
                   │   │   Space/launch expertise ● (×)     │
                   │   │                                    │
                   │   │   Reality (the leaks):             │
                   │   │      Phys.SC ● (×)                 │
                   │   │      Info.SC ●──→                  │
                   │   │    Fab ● (×)                       │
                   │   │                Rare Earths ● (×)   │
                   │   │                         Compute ●  │
                   │   │                         Power ●    │
                   │   │                   Spectrum ●       │
                   │   │            Orbital slots ●         │
Hidden             │   │                         Geography ●│
                   └───┴────────────────────────────────────┘

Legend: ● Current position, → Evolution direction, × Inertia / foreign-dependency bottleneck
Full numeric positions in `draft.owm`.
```

Positions follow the OWM convention: X-axis is evolution in [0,1] (Genesis → Commodity); Y-axis is visibility in [0,1] (anchors near the top, substrate at the bottom).

---

## Value-Chain Walkthrough

Working down from the anchors:

1. **Four anchors, six pillars.** The Government, the Collective, Corporations, and People each pull on a different subset of the six sovereignty pillars. The Government pulls on all six; the Collective mostly on cultural and political sovereignty; Corporations on economic and CNI (they operate it); People on cultural/political (what they see and say).
2. **Pillars are outcomes, not components.** Territorial, political, cultural, economic, digital, and CNI sovereignty are what the nation wants. They depend on very different things: territorial sovereignty needs awareness; political and cultural sovereignty lean on the control layer; economic and CNI sovereignty lean on hardware and vendor relationships; digital sovereignty spans almost the whole stack.
3. **Access devices are commodities.** Smartphones, PCs, radio/TV, SIM/eSIM, and IoT endpoints are mature commodity products with global supply chains. Sat phones are still a specialised product, not a commodity.
4. **Access networks split three ways.** Terrestrial — towers, fibre, submarine cable — is commodity infrastructure. GEO satellite is mature product. **LEO constellations** (Starlink / OneWeb) and their **launch cadence** are the disruptors: in October 2022 they are transitioning from custom-built into product, and this is where the map moves fastest.
5. **Network equipment and topology is a quasi-monopoly layer.** Four vendors (Ericsson, Nokia, Huawei, ZTE) dominate mobile cores; IXPs and Tier-1 transit are commodity but concentrated. **Open RAN** sits in custom-built, evolving toward product — it is the main play for vendor-dependency relief.
6. **Control layer is where the nation actually exercises technical sovereignty.** Nation-state firewalls (GFW-style DPI), DoH, national DNS resolvers, SIM registration, BGP filtering, geofencing, kill-switches, and legal takedown: these are the levers the state *can* pull, and they are all evolving toward product/commodity maturity.
7. **Theatre / awareness is the deepest visibility gap.** Space-domain awareness, submarine-cable route awareness, and supply-chain intelligence are all in the custom-built band — most nations see their own orbital, seabed, and supplier environment poorly.
8. **Expertise and peering are the human layer.** Telecoms engineering, RF, semiconductor design, cryptography, and space/launch expertise are the bottleneck that no amount of capital unlocks quickly.
9. **The underlying reality is where sovereignty most often leaks.** Silicon, rare earths, the information supply chain (firmware, patches, CVE feeds), and compute are globally sourced. Only spectrum, orbital slots, and geography are truly sovereign — and even orbital is contested.

---

## Where Telecoms is Truly Sovereign-Controllable

These are the cells where a determined nation-state can exercise real, direct, enforceable sovereignty:

| Layer | Controllable Component | Why sovereign |
|-------|------------------------|---------------|
| Spectrum / orbit | **Spectrum (radio)** | Allocated by national regulator + ITU; enforceable on territory |
| Spectrum / orbit | **Orbital slots** | ITU filings + national licensing; partially controllable |
| Territory | **Geography / airspace / sea** | Intrinsically sovereign |
| Control layer | **Nation-State Firewall (DPI)** | Law + mandate on domestic ISPs + IXPs |
| Control layer | **National DNS Resolver** | ISP licensing mandate |
| Control layer | **SIM Registration Regime** | Domestic law on operators |
| Control layer | **Kill-Switch / Network Shutdown** | Emergency powers over domestic carriers |
| Control layer | **Lawful Intercept Apparatus** | Legislated + built into vendor equipment |
| Control layer | **BGP Route Filtering** | Applied at domestic carriers / IXPs |
| Control layer | **Geofencing / Content Takedown** | Legal orders to platforms / carriers |
| CNI | **Fibre / Copper last mile** | Physical plant on national territory |
| CNI | **Mobile Tower / Cell Site** | Sited on national land + spectrum |

All of these sit in the **right-centre band** of the map (evolution ~0.5 - 0.9) with high-to-mid visibility — they are the levers the state actually pulls.

---

## Where the Chain Depends on Foreign Actors

These are the cells where sovereign control is illusory — the nation-state can regulate but cannot supply:

| Layer | Component | Where the dependency lands |
|-------|-----------|----------------------------|
| Network equipment | **Ericsson / Nokia / Huawei / ZTE** | Four foreign vendors; no domestic alternative at scale |
| Silicon | **Semiconductor Fab** (TSMC / Samsung / SMIC / Intel) | Concentrated in a handful of non-sovereign jurisdictions |
| Materials | **Rare Earths & Metals** | China-dominated refining, Taiwan-dominated fab, limited diversification |
| Subsea | **Submarine Cable** | Private consortia (Google, Meta, SubCom, ASN, NEC) lay + maintain |
| Transit | **Tier-1 Transit** | Foreign-held IP transit; peering can be throttled/priced |
| Space | **Launch Vehicle (commercial)** | SpaceX dominance; most nations have no sovereign equivalent |
| Space | **LEO Constellation (Starlink / OneWeb)** | Commercial, licensed foreign operators; nation can grant/deny local access but not compel service |
| Information | **Information supply chain (firmware / patches / CVE feeds)** | Vendor-controlled update channels |
| Expertise | **Space / launch + Semiconductor design** | Human-capital bottleneck; decade-plus to build |
| Awareness | **Space Domain Awareness, Supply-Chain Intelligence** | Mostly bought in from allies (Five Eyes, EU partners) |

All of these sit on the **left side** of the map (evolution < 0.6) and in the **low-visibility band**. They are the parts the nation-state cannot directly compel. The deepest leak is **silicon + rare earths + launch** — the three chokepoints where a single foreign actor (or cartel of two or three) can withhold supply.

---

## Structured YAML

```yaml
wardley_map:
  metadata:
    title: "Telecoms Sovereignty — Nation-State Perspective"
    author: "arc-kit wardley-mapping skill (competitor-compare/arc-kit/skill)"
    date: "2022-10"
    version: "1.0"
    scope: "End-to-end telecoms stack from access devices to orbital/physical reality, assessed for sovereign controllability"

  anchor:
    users: ["Government", "Collective (civil society)", "Corporations (telcos / OEMs / platforms)", "People (citizens / subscribers)"]
    need: "Maintain sovereign control of telecoms across six pillars (territorial, political, cultural, economic, digital, CNI)"

  components:
    - name: "Smartphone"
      evolution: "Commodity"
      position: 0.92
      visibility: 0.76
      depends_on: ["SIM / eSIM", "Mobile Tower / Cell Site", "Physical Supply Chain (hardware)", "Silicon / Semiconductor Fab"]
      notes: "Globally sourced hardware; sovereign control is regulatory (import, security cert), not productive"
      movement: "none"
    - name: "Mobile Tower / Cell Site"
      evolution: "Commodity"
      position: 0.90
      visibility: 0.60
      depends_on: ["Spectrum (radio)", "Power Grid", "Mobile Network Core (4G/5G RAN + EPC/5GC)", "Geography"]
      notes: "Sited on national territory; sovereign control is real (licensing + spectrum)"
      movement: "none"
    - name: "Submarine Cable"
      evolution: "Product"
      position: 0.82
      visibility: 0.56
      depends_on: ["Geography", "Physical Supply Chain (hardware)"]
      notes: "Private consortia lay and maintain; sovereignty leak at landing stations only"
      movement: "inertia"
    - name: "LEO Satellite Constellation (Starlink / OneWeb)"
      evolution: "Custom/Product transition"
      position: 0.45
      visibility: 0.52
      depends_on: ["Launch Vehicle (commercial)", "Space (orbital slots)", "Spectrum (radio)"]
      notes: "Oct 2022: scaling fast; sovereignty leak — nation can block local service but not compel it"
      movement: "accelerating"
    - name: "Network Equipment Vendor (Ericsson / Nokia / Huawei / ZTE)"
      evolution: "Product"
      position: 0.75
      visibility: 0.40
      depends_on: ["Physical Supply Chain (hardware)", "Silicon / Semiconductor Fab"]
      notes: "Four foreign vendors dominate. Primary sovereignty leak at network-core layer. Open RAN is the strategic relief valve."
      movement: "inertia"
    - name: "Open RAN"
      evolution: "Custom"
      position: 0.32
      visibility: 0.40
      depends_on: ["Semiconductor Design Expertise", "Information Supply Chain"]
      notes: "Primary lever for vendor-dependency relief; still custom-built in Oct 2022"
      movement: "evolving"
    - name: "Nation-State Firewall (GFW-style / DPI)"
      evolution: "Product"
      position: 0.55
      visibility: 0.54
      depends_on: ["Fixed Network Core", "Mobile Network Core", "BGP Route Filtering", "Cryptographic Expertise"]
      notes: "The paradigm case: real, directly exercisable sovereign control. Evolving to commodity-like maturity."
      movement: "evolving"
    - name: "DNS-over-HTTPS (DoH)"
      evolution: "Product"
      position: 0.70
      visibility: 0.50
      depends_on: ["Cryptographic Expertise"]
      notes: "Commoditising fast. Nation-state response is to mandate national DoH resolvers."
      movement: "evolving"
    - name: "Silicon / Semiconductor Fab"
      evolution: "Product"
      position: 0.55
      visibility: 0.18
      depends_on: ["Rare Earths & Metals", "Power Grid"]
      notes: "The deepest sovereignty leak. Concentration risk: TSMC, Samsung, SMIC, Intel. Decade-plus to replicate."
      movement: "inertia"
    - name: "Rare Earths & Metals"
      evolution: "Commodity"
      position: 0.72
      visibility: 0.16
      depends_on: []
      notes: "Commodity market, but refining is geographically concentrated. Sovereignty leak."
      movement: "inertia"
    - name: "Space Domain Awareness (SDA)"
      evolution: "Custom"
      position: 0.28
      visibility: 0.28
      depends_on: ["Space (orbital slots)", "Space / Launch Expertise"]
      notes: "Most nations buy SDA from allies. Primary growth area for sovereign investment."
      movement: "evolving"
    - name: "Supply-Chain Intelligence (components / vendors)"
      evolution: "Custom"
      position: 0.22
      visibility: 0.26
      depends_on: ["Physical Supply Chain (hardware)", "Information Supply Chain"]
      notes: "Awareness gap — most nations cannot enumerate their own hardware dependency tree"
      movement: "evolving"
    - name: "Launch Vehicle (commercial)"
      evolution: "Product"
      position: 0.58
      visibility: 0.50
      depends_on: ["Space (orbital slots)", "Space / Launch Expertise"]
      notes: "SpaceX dominance; legacy providers (Arianespace, ULA, Roscosmos, JAXA, ISRO) stratified"
      movement: "accelerating"
    - name: "Launch Vehicle (sovereign)"
      evolution: "Custom"
      position: 0.30
      visibility: 0.48
      depends_on: ["Space / Launch Expertise", "Physical Supply Chain", "Rare Earths & Metals"]
      notes: "Only a handful of nations have sovereign launch. Post-Ukraine this is a growth bet."
      movement: "evolving"
    # (full component set is listed in draft.owm)

  analysis:
    opportunities:
      - "Mandate Open RAN in domestic operators — shift 5G core out of the four-vendor lock"
      - "Build sovereign LEO constellation or strike reciprocal access deals before Starlink becomes the global utility"
      - "Invest in Space Domain Awareness + Submarine Cable Route Awareness — the two biggest awareness gaps"
      - "Regulate DNS-over-HTTPS: national resolver + upstream policy"
      - "Build Supply-Chain Intelligence capability — SBOMs, firmware attestation, vendor origin tracking"
      - "Develop indigenous semiconductor capacity (or guaranteed ally-country supply) — the deepest leak"

    threats:
      - "Foreign-vendor kill-switch or tampering in mobile/fixed network equipment"
      - "Submarine-cable cut (deliberate or accidental) at landing stations or mid-ocean"
      - "Loss of launch access (sanctioned, or commercial provider withdraws)"
      - "Rare-earth refining withheld by single supplier country"
      - "Chipset export controls (CHIPS Act era) cascading into telecoms equipment"
      - "DNS-over-HTTPS + encrypted SNI defeating national-firewall policy"
      - "Starlink / foreign LEO bypassing national access controls directly to citizens"
      - "Information supply chain poisoning (firmware backdoor, malicious CVE)"

    inertia_points:
      - component: "Network Equipment Vendor (Ericsson / Nokia / Huawei / ZTE)"
        reason: "No domestic alternative at scale; multi-billion replacement cost; operator skill base locked to existing stack"
      - component: "Silicon / Semiconductor Fab"
        reason: "Decade-plus build time; capex on the order of tens of billions per fab; skill base concentrated in a handful of countries"
      - component: "Rare Earths & Metals"
        reason: "Refining capacity geographically concentrated; years to stand up alternative supply"
      - component: "Submarine Cable"
        reason: "Private consortium-owned; replacement cycles 20-25 years; nation cannot compel build"
      - component: "Tier-1 Transit"
        reason: "Foreign-held transit monopolies; peering economics favour incumbents"
      - component: "Physical Supply Chain (hardware)"
        reason: "Global JIT logistics; inventory-efficiency incentives push against sovereign redundancy"
      - component: "Space / Launch Expertise"
        reason: "Human capital — decade-plus to train a cadre; shrinking in most countries since the 1970s"
      - component: "Launch Vehicle (sovereign)"
        reason: "Program cost, skill base, and industrial ecosystem all need to be rebuilt"

  recommendations:
    immediate:
      - "Stand up a national Supply-Chain Intelligence capability (SBOM + origin tracking for all CNI-tier telecoms equipment)"
      - "Mandate a National DNS Resolver + DoH policy alignment"
      - "Audit vendor exposure at mobile and fixed core; publish Open-RAN migration roadmap"
    short_term:
      - "Negotiate reciprocal-access agreements with LEO constellation operators (Starlink, OneWeb, Kuiper, future domestic)"
      - "Fund Open-RAN trial deployments in regional operators"
      - "Invest in SDA + submarine-cable-route awareness (sensor fusion + ally data-sharing)"
      - "Stockpile / diversify rare-earth and chipset supply"
    long_term:
      - "Domestic or ally-country semiconductor fab capacity for telecoms-grade silicon"
      - "Sovereign launch capability or long-term allied-launch contracts"
      - "Rebuild national space, RF, and semiconductor-design workforce pipeline"
      - "Treat telecoms as CNI end-to-end, including the awareness + supply-chain layer, not just the physical plant"
```

---

## Analysis Checklist

**Completeness**
- Anchor — four stakeholders with distinct claims: government, collective, corporations, people — all present
- Components — 50+ components spanning devices → access networks → core → control layer → awareness → expertise → underlying reality
- Dependencies — explicit, anchors flow down to substrate; the six sovereignty pillars fan out into the stack
- Movement arrows — 16 evolve arrows covering LEO, Open RAN, control-layer items, and awareness

**Positioning**
- Commodity items on the right (devices, towers, fibre, radio/TV spectrum consumption)
- Custom-built / novel on the left (Open RAN, LEO constellations in Oct 2022, sovereign launch, SDA, supply-chain intelligence, digital sovereignty as an organising concept)
- Anchors high on visibility; substrate (geography, power, spectrum, orbital slots, fabs, rare earths) at the bottom

**Insights**
- **Inertia** sits on the hardware + silicon + launch axis
- **Commoditisation opportunity** — Open RAN, DoH, SIM registration regimes, BGP filtering all commoditise over the next 3-5 years
- **Genesis → differentiator** — supply-chain intelligence, space-domain awareness, and a sovereign information-supply-chain attestation regime are the differentiators a nation can still build
- **Technical debt** — running foreign-vendor network cores is the paradigm "building custom where a geopolitical alternative is required"

**Strategic**
- Gameplay patterns: **Constraint of adversary** (DPI + BGP filtering), **Dependency reduction** (Open RAN, sovereign launch), **Sensing** (SDA + supply-chain intel), **Standards game** (ITU allocations, national DoH mandate)
- Climatic patterns at play: **commoditisation of communications access** (Starlink); **peace/war/wonder** cycle — telecoms equipment is in a "war" phase (Huawei ban era); **efficiency moves to the edge** (LEO vs. tower)
- Doctrine weaknesses: most nations fail the "know your supply chain" principle and "think big, act small" — the full-stack sovereignty view is rarely articulated end-to-end

---

## Gameplay + Climatic Notes

**Climatic patterns (from references/climatic-patterns.md):**
1. **Everything evolves** — even the sovereignty-conferring bits. DPI moves from custom to commodity, which means a nation's "sovereign firewall" becomes a buyable product (good) but the same commoditisation helps adversaries too.
2. **Efficiency vs. Effectiveness** — LEO constellations are massively more efficient than terrestrial coverage in sparse territories, but they move effectiveness of national control *out* of national hands.
3. **Peace-war-wonder cycle** — network equipment (Huawei ban, Open RAN emergence) is in a "war" phase; launch is in a "wonder" phase (Starlink / SpaceX disruption); silicon is in a "peace/war transition" (CHIPS Act era).

**Gameplay patterns (from references/gameplay-patterns.md):**
1. **Constraint (on adversary)** — DPI, BGP filtering, SIM registration, content takedown are constraint plays, applied to domestic carriers and foreign platforms alike.
2. **Dependency reduction** — Open RAN, sovereign launch, indigenous silicon. Long-horizon, high-cost.
3. **Building a sensor network** — SDA + submarine-cable route awareness + supply-chain intelligence are sensing plays. Cheapest high-leverage move in the near term.
4. **Standards game** — national DoH resolver mandate, ITU orbital-slot filings, spectrum auctions. The nation-state's "home field."
5. **Pig-in-the-middle** — risk of becoming the pig — if a nation is neither sovereign nor aligned with a bloc, it sits between the US, China, and EU telecoms orders and is squeezed from all sides.

---

## Summary

**Where telecoms is truly sovereign-controllable:** the control layer (DPI, national DNS, SIM registration, BGP filtering, kill-switch, geofencing, lawful intercept), spectrum allocation, orbital-slot filings, and physically sited infrastructure (towers, fibre, landing stations). These occupy the right-centre band of the map and are what the state actually directly commands.

**Where the chain depends on foreign actors:** network-equipment vendors (the four-vendor lock), silicon fabs, rare-earth refining, submarine cables and tier-1 transit, launch vehicles, foreign LEO constellations, and the information supply chain (firmware/patches). These occupy the left and bottom of the map, most of them with inertia markers. Together they represent the genuine sovereignty leak — a nation cannot compel their supply; it can only regulate access and pursue multi-year substitution plays (Open RAN, sovereign fab, sovereign launch, SDA, supply-chain intelligence).

The strategic message of the map: sovereignty at the *control layer* is real; sovereignty at the *hardware, silicon, launch, and supply-chain* layer is mostly aspirational in October 2022, and the gap is widening as LEO commoditises connectivity and pulls it further out of national hands.
