# Wardley Map: Electrical Energy Storage & the Grid (April 2023)

**Anchor:** Activity — the thing electricity exists to power. Consumers demand it; generation and the grid deliver it; storage, control, platform and supply chain sit underneath.

**Date:** 2023-04 (scenario context), generated 2026-04-22.

**Scope:** The electrical energy storage landscape connecting consumers, activity, control, electricity generation and the grid — with an explicit traditional-vs-distributed grid contrast, a storage portfolio (hydro / battery / hydrogen), the emerging energy platform + integration layer, and the chain underneath (sources, stockpile, material supply chain, awareness).

---

## Step 1 — Context

Blind benchmark: no interactive user is available, so the arc-kit `AskUserQuestion` step is resolved by inference from the scenario brief.

| Question | Answer |
|---|---|
| Primary user | Consumers of electricity (residential, industrial, commercial) |
| User need | *Activity* — the work electricity enables |
| Scope | Electrical energy storage landscape as it connects to generation, grid and control |
| Primary goal | Show where distributed fault-tolerant grids evolve faster than traditional control, and where material supply chain risk is biting |
| Industry | Energy — generation, storage, grid control |
| Depth | Standard (~20 components) |
| Date of landscape | April 2023 (before the 2023-2024 lithium price normalisation and before widespread grid-scale hydrogen storage) |

## Step 2 — Value Chain

Working downward from the user need:

1. **Anchor:** *Activity* — everything consumers do that requires electricity.
2. **Demand:** Consumers.
3. **Delivery layer:** Electricity Generation, Grid.
4. **Grid models (the contrast the user asked for):**
   - Traditional Grid (single-machine view) — one-big-synchronous-machine mental model, top-down control.
   - Distributed Grid (fault-tolerant, TCP/IP-style) — packet-style routing of power/signals, graceful degradation, many small sources.
5. **Control plane:** Control, SCADA, Auto Generation Control (AGC), Spinning Reserve, Fast-Response Systems.
6. **Storage portfolio:** Hydro Storage, Electrical Storage (battery), Hydrogen Storage.
7. **Energy platform & integration layer:** Energy Platform, Integration Layer (pre-approval/discovery), Adaptive Integration, Plug-and-Play Energy.
8. **Underlying supply chain:** Sources, Stockpile, Material Supply Chain, Awareness of Energy Supply Chain.

## Step 3 — Evolution Positioning

Stage lookups reference `references/evolution-stages.md` (arc-kit). Coordinates use `[visibility, maturity]` with visibility 0 at bottom of map.

| Component | Stage | Maturity (X) | Visibility (Y) | Rationale |
|---|---|---|---|---|
| Activity | Commodity | 0.92 | 0.97 | The root user need; ubiquitous. |
| Consumers | Commodity | 0.88 | 0.92 | Mature demand population. |
| Electricity Generation | Commodity | 0.86 | 0.84 | Century-old utility; many providers; utility pricing. |
| Grid | Commodity | 0.84 | 0.82 | National transmission + distribution networks; utility. |
| Traditional Grid (single-machine view) | Product / high-commodity with inertia | 0.72 | 0.74 | Well-understood model, standardised practice, but institutionally locked in. |
| Distributed Grid (fault-tolerant, TCP/IP-style) | Custom | 0.32 | 0.74 | Multiple pilots (microgrids, VPPs, TSO experiments) but no single winning pattern in 2023. |
| Control | Product | 0.62 | 0.66 | Multi-vendor control software market; standards and training courses exist. |
| SCADA | Product / Commodity-edge | 0.78 | 0.58 | Long-established product category with many vendors and standards. |
| Auto Generation Control | Product | 0.68 | 0.56 | Standardised in traditional grid; regional variants. |
| Spinning Reserve | Commodity | 0.82 | 0.52 | Utility-priced ancillary service in every mature power market. |
| Fast-Response Systems | Product | 0.55 | 0.54 | 2022-2023 markets for battery-based frequency response (EFR, FFR, DFR) are a recognisable product category with competing vendors. |
| Hydro Storage | Commodity | 0.85 | 0.46 | Pumped-hydro is a century old; utility-run; low innovation rate. |
| Electrical Storage (battery) | Product | 0.62 | 0.48 | By April 2023 grid-scale battery is a vendor-competitive product category (Tesla Megapack, Fluence, BYD, CATL) with ranked analyst coverage. |
| Hydrogen Storage | Custom | 0.30 | 0.44 | Bespoke pilot projects; little standardisation; no utility price signal yet. |
| Energy Platform | Custom | 0.35 | 0.40 | Emerging DERMS / aggregator platform concept; no dominant player. |
| Integration Layer (pre-approval/discovery) | Genesis / early Custom | 0.18 | 0.36 | Pre-approval and discovery workflows are bespoke; each pilot invents its own. |
| Adaptive Integration | Genesis | 0.14 | 0.34 | Self-configuring interoperability is aspirational in 2023. |
| Plug-and-Play Energy | Genesis | 0.10 | 0.32 | Analogue of IP-style plug-and-play for energy assets is a research concept. |
| Sources | Commodity | 0.82 | 0.26 | Primary energy sources (gas, coal, wind, solar, uranium) are mature. |
| Stockpile | Product | 0.70 | 0.24 | Strategic fuel reserves are an established, policy-managed product. |
| Material Supply Chain | Custom | 0.30 | 0.18 | In 2023 lithium, cobalt, rare-earth, graphite supply-chain resilience is actively bespoke; companies are only just building visibility tooling. |
| Awareness of Energy Supply Chain | Genesis | 0.12 | 0.14 | Post-Ukraine invasion; the discipline of systematic supply-chain awareness in energy is only just forming. |

## Step 4 — Movement

The two headline movements the user asked to see are marked first.

| Component | Direction | Target maturity | Note |
|---|---|---|---|
| Distributed Grid (fault-tolerant, TCP/IP-style) | `>>` accelerating | 0.58 | Moving from Custom toward Product — grid operators, battery firms, and ISO grid codes are standardising around distributed / IP-style patterns faster than traditional control can reorganise. |
| Traditional Grid (single-machine view) | `×` inertia | 0.75 | Still the default mental model of TSOs; institutional inertia is the hallmark of regulated utilities and long-lived synchronous-generator assets. |
| Fast-Response Systems | `→` evolving | 0.68 | Productising rapidly as more grid codes require sub-second response. |
| Electrical Storage (battery) | `→` evolving | 0.75 | Cell chemistry and integration are commoditising. |
| Hydrogen Storage | `→` evolving | 0.45 | Custom today, moving to Product as green-hydrogen projects come online. |
| Energy Platform | `→` evolving | 0.55 | Aggregation software (DERMS, VPP) is productising. |
| Integration Layer (pre-approval/discovery) | `→` evolving | 0.35 | Still Genesis/early-Custom in 2023; regulatory discovery is slow. |
| Material Supply Chain | `>>` accelerating | 0.48 | Moving right fast but from a low base — this is where the user said "material supply chain risk is biting": visibility and resilience tooling is being operationalised at speed. |
| Awareness of Energy Supply Chain | `>>` accelerating | 0.30 | Post-2022 geopolitical shock is forcing rapid standardisation of this discipline. |

## Step 5 — Visual Map

```text
Title: Electrical Energy Storage & the Grid (April 2023)
Anchor: Activity
Date: 2023-04

                    Genesis    Custom     Product    Commodity
                       |          |          |          |
Visible            ----+----------+----------+----------+----
                                                        Activity        <- anchor
                                                        Consumers
                                                        Electricity Gen
                                                        Grid
                                     Distributed Grid >>                 Traditional Grid x  (Commodity-leaning but inertia)
                                                  Control
                                                        SCADA
                                                  AGC
                                                        Spinning Reserve
                                             Fast-Response Systems ->
                                             Electrical Storage ->
                                                        Hydro Storage
                                 Hydrogen Storage ->
                                  Energy Platform ->
                         Integration Layer ->
                        Adaptive Integration
                      Plug-and-Play Energy
                                                        Sources
                                                  Stockpile
                                 Material Supply Chain >>
                      Awareness of Energy Supply Chain >>
Hidden             ----+----------+----------+----------+----

Legend: -> evolving, >> accelerating, x inertia
```

## Step 6 — Analysis

### Completeness
- Anchor (Activity) defined, with consumers immediately beneath.
- Both grid models present with explicit maturity offset (Traditional at 0.72, Distributed at 0.32) — the *same visibility band* (0.74) to show they are functionally equivalent peers competing on maturity.
- All storage types present (hydro, battery, hydrogen).
- Full platform and integration layer present (platform → pre-approval/discovery → adaptive → plug-and-play).
- Full underlying chain present (sources, stockpile, material supply chain, awareness).
- Dependencies shown as directed edges; all obey the visibility constraint.
- Movement arrows present on the nine components with meaningful change.

### Positioning
- Commodity cluster (right): Activity, Consumers, Electricity Generation, Grid, Spinning Reserve, SCADA, Hydro Storage, Sources.
- Product cluster: Traditional Grid, Control, AGC, Electrical Storage (battery), Fast-Response Systems, Stockpile.
- Custom cluster: Distributed Grid, Hydrogen Storage, Energy Platform, Material Supply Chain.
- Genesis cluster: Integration Layer (pre-approval/discovery), Adaptive Integration, Plug-and-Play Energy, Awareness of Energy Supply Chain.
- The dependency constraint `visibility(a) >= visibility(b)` is respected on every edge.

### Key insights (what the user explicitly asked for)

**1. Where distributed fault-tolerant grids are evolving faster than traditional control.**

Place Traditional Grid at maturity 0.72 with `inertia` (×) and Distributed Grid at maturity 0.32 with `accelerating` (`>>`). At the same visibility band (0.74), two components competing for the same job:

- Traditional Grid's maturity is already near-Commodity but its *evolutionary velocity is near zero* — regulated utility, sunk-cost synchronous assets, century-old operator culture. This is textbook arc-kit "Commodity with inertia" — dangerous because the world moves and the component does not.
- Distributed Grid is moving fast (`>>` target 0.58). Pilots and standards that were research in 2019 are now Custom-Built in 2023 and heading into Product. Operators who only think in single-machine terms will be blindsided by fault-tolerant microgrids, VPPs, and IP-style routing.
- Consequence: the control plane splits. SCADA, AGC, Spinning Reserve stay anchored to Traditional Grid. Fast-Response Systems and newer DERMS aggregators anchor to Distributed Grid. That divergence is the strategic discontinuity.

**2. Where material supply chain risk is biting.**

Material Supply Chain sits at maturity 0.30 (Custom) but is flagged accelerating (`>>`) to 0.48. Two things to read from that:

- It is *still* Custom. In 2023 every battery integrator, every hydrogen project, every utility's procurement function is building bespoke visibility tooling — there is no commodity answer.
- It is moving fast because it *has to*. Lithium price spikes, cobalt sourcing scrutiny, Chinese rare-earth leverage, and Ukraine-war-driven fuel stockpiling are forcing discovery and pre-approval disciplines that did not exist two years earlier.
- Underneath it, Awareness of Energy Supply Chain is still Genesis (0.12). That is the real bite: the *discipline* of being aware is not yet a thing. Material Supply Chain is moving; *knowing about it* is not.

### Inertia points
- **Traditional Grid (single-machine view)** — institutional, regulatory, and asset-base inertia.
- **Spinning Reserve** — entrenched as an ancillary service; difficult to replace even when Fast-Response Systems are measurably better.
- **Hydro Storage** — geographically locked; no amount of competition moves it.

### Opportunities
- Productise the distributed-grid control plane (DERMS, VPP platforms, peer-to-peer trading) before traditional TSO vendors pivot.
- Build commodity material-supply-chain visibility tooling (analogous to software SBOM but for battery BOMs) — the market is obviously forming.
- Push the integration layer (pre-approval/discovery, adaptive, plug-and-play) toward standardisation; early movers define the protocol.

### Threats
- Traditional-grid operators' inertia risks a control-plane split where two mental models must be operated in parallel for a decade.
- Material supply-chain concentration (lithium, cobalt, rare earth, graphite) creates a tail-risk dependency for all battery-backed storage.
- Hydrogen Storage remains Custom; over-betting on it today before the platform standardises is the "built it wrong" failure mode from the arc-kit Custom-Built stage.

### Climatic patterns in play
- *Evolution is inevitable* — Traditional Grid's inertia cannot stop the move.
- *Past success breeds inertia* — century-old operator mental model.
- *Capital flows to the novel* — battery + distributed-grid investment is outpacing traditional-grid reinvestment.
- *Components co-evolve* — material-supply-chain awareness co-evolves with battery deployment; one drags the other right.

### Gameplay suggestions
- **Open Source / Open Data** on integration-layer interfaces (pre-approval/discovery) to accelerate commoditisation.
- **Standards game** around distributed-grid fault tolerance and Fast-Response Systems interfaces.
- **Pioneer / Settler / Town Planner** split: pioneer teams on Adaptive Integration and Plug-and-Play Energy; settlers on DERMS platforms; town planners on battery fleet operations and spinning-reserve contracts.

## Output Format

```yaml
wardley_map:
  metadata:
    title: "Electrical Energy Storage & the Grid (April 2023)"
    author: "arc-kit wardley-mapping skill (blind benchmark run)"
    date: "2023-04"
    version: "1.0"
    scope: "Electrical energy storage landscape connecting consumers, activity, control, generation, grid, grid models, storage types, energy platform, integration layer, and the underlying supply chain."

  anchor:
    user: "Consumers of electricity"
    need: "Activity (the work electricity powers)"

  components:
    - name: "Activity"
      evolution: "Commodity"
      position: 0.92
      visibility: 0.97
      depends_on: ["Consumers", "Electricity Generation"]
      notes: "Anchor user need"
      movement: "none"
    - name: "Consumers"
      evolution: "Commodity"
      position: 0.88
      visibility: 0.92
      depends_on: ["Grid", "Electricity Generation"]
      notes: "Demand population"
      movement: "none"
    - name: "Electricity Generation"
      evolution: "Commodity"
      position: 0.86
      visibility: 0.84
      depends_on: ["Hydro Storage", "Electrical Storage (battery)", "Hydrogen Storage", "Sources", "Stockpile"]
      notes: "Utility-scale generation"
      movement: "none"
    - name: "Grid"
      evolution: "Commodity"
      position: 0.84
      visibility: 0.82
      depends_on: ["Traditional Grid (single-machine view)", "Distributed Grid (fault-tolerant, TCP/IP-style)", "Hydro Storage", "Electrical Storage (battery)"]
      notes: "Transmission + distribution networks"
      movement: "none"
    - name: "Traditional Grid (single-machine view)"
      evolution: "Product"
      position: 0.72
      visibility: 0.74
      depends_on: ["Control", "SCADA", "Auto Generation Control", "Spinning Reserve"]
      notes: "One-big-synchronous-machine mental model; near-commodity but institutionally locked"
      movement: "inertia"
    - name: "Distributed Grid (fault-tolerant, TCP/IP-style)"
      evolution: "Custom"
      position: 0.32
      visibility: 0.74
      depends_on: ["Control", "Fast-Response Systems", "SCADA"]
      notes: "Packet-style routing; microgrids; VPPs"
      movement: "accelerating"
    - name: "Control"
      evolution: "Product"
      position: 0.62
      visibility: 0.66
      depends_on: []
      notes: "Control software; multi-vendor market"
      movement: "evolving"
    - name: "SCADA"
      evolution: "Product"
      position: 0.78
      visibility: 0.58
      depends_on: []
      notes: "Long-established product category"
      movement: "evolving"
    - name: "Auto Generation Control"
      evolution: "Product"
      position: 0.68
      visibility: 0.56
      depends_on: []
      notes: "Standardised in traditional grid"
      movement: "none"
    - name: "Spinning Reserve"
      evolution: "Commodity"
      position: 0.82
      visibility: 0.52
      depends_on: ["Hydro Storage"]
      notes: "Mature ancillary service"
      movement: "inertia"
    - name: "Fast-Response Systems"
      evolution: "Product"
      position: 0.55
      visibility: 0.54
      depends_on: ["Electrical Storage (battery)"]
      notes: "Battery-based frequency response products"
      movement: "evolving"
    - name: "Hydro Storage"
      evolution: "Commodity"
      position: 0.85
      visibility: 0.46
      depends_on: ["Sources"]
      notes: "Pumped hydro; geographically locked"
      movement: "none"
    - name: "Electrical Storage (battery)"
      evolution: "Product"
      position: 0.62
      visibility: 0.48
      depends_on: ["Energy Platform", "Material Supply Chain"]
      notes: "Grid-scale battery is a productised vendor market by 2023"
      movement: "evolving"
    - name: "Hydrogen Storage"
      evolution: "Custom"
      position: 0.30
      visibility: 0.44
      depends_on: ["Energy Platform", "Material Supply Chain"]
      notes: "Bespoke pilots; pre-productisation"
      movement: "evolving"
    - name: "Energy Platform"
      evolution: "Custom"
      position: 0.35
      visibility: 0.40
      depends_on: ["Integration Layer (pre-approval/discovery)", "Awareness of Energy Supply Chain"]
      notes: "DERMS / aggregator platform concept"
      movement: "evolving"
    - name: "Integration Layer (pre-approval/discovery)"
      evolution: "Custom"
      position: 0.18
      visibility: 0.36
      depends_on: ["Adaptive Integration"]
      notes: "Bespoke per pilot"
      movement: "evolving"
    - name: "Adaptive Integration"
      evolution: "Genesis"
      position: 0.14
      visibility: 0.34
      depends_on: ["Plug-and-Play Energy"]
      notes: "Self-configuring interop; aspirational"
      movement: "none"
    - name: "Plug-and-Play Energy"
      evolution: "Genesis"
      position: 0.10
      visibility: 0.32
      depends_on: []
      notes: "Research concept"
      movement: "none"
    - name: "Sources"
      evolution: "Commodity"
      position: 0.82
      visibility: 0.26
      depends_on: ["Material Supply Chain"]
      notes: "Primary energy feedstocks"
      movement: "none"
    - name: "Stockpile"
      evolution: "Product"
      position: 0.70
      visibility: 0.24
      depends_on: ["Material Supply Chain"]
      notes: "Policy-managed strategic reserves"
      movement: "none"
    - name: "Material Supply Chain"
      evolution: "Custom"
      position: 0.30
      visibility: 0.18
      depends_on: ["Awareness of Energy Supply Chain"]
      notes: "Lithium / cobalt / rare earth / graphite — visibility tooling is bespoke but accelerating"
      movement: "accelerating"
    - name: "Awareness of Energy Supply Chain"
      evolution: "Genesis"
      position: 0.12
      visibility: 0.14
      depends_on: []
      notes: "Discipline of systematic energy supply-chain awareness is only just forming post-2022"
      movement: "accelerating"

  analysis:
    opportunities:
      - "Productise the distributed-grid control plane (DERMS / VPP / peer-to-peer) before incumbent TSO vendors pivot."
      - "Build commodity material-supply-chain visibility tooling — the battery-BOM analogue of software SBOM."
      - "Push the integration layer (pre-approval/discovery, adaptive, plug-and-play) toward a standard protocol."
    threats:
      - "Traditional-grid operator inertia risks a decade-long split control plane."
      - "Material supply-chain concentration (Li, Co, rare earth, graphite) is a single-point-of-failure for battery-backed storage."
      - "Hydrogen Storage is still Custom — over-investing before the platform standardises risks the Custom-Built 'built it wrong' failure mode."

    inertia_points:
      - component: "Traditional Grid (single-machine view)"
        reason: "Regulated-utility culture, sunk-cost synchronous assets, century-old operator mental model"
      - component: "Spinning Reserve"
        reason: "Entrenched ancillary-service contracts"
      - component: "Hydro Storage"
        reason: "Geographic lock-in"

  recommendations:
    immediate:
      - "Inventory material-supply-chain exposure for every battery and hydrogen project (bill of materials, country-of-origin, substitutability)."
      - "Name an owner for the distributed-grid / traditional-grid split and decide which model owns which control primitives."
    short_term:
      - "Pilot a DERMS/VPP platform that is explicit about pre-approval/discovery interfaces — treat Integration Layer as a standards play, not a product play."
      - "Set up a supply-chain awareness discipline (analyst function, signals feed) — pull Awareness of Energy Supply Chain out of Genesis."
    long_term:
      - "Drive interoperability standards for Plug-and-Play Energy so adaptive integration becomes a commodity."
      - "Rebalance spinning-reserve and fast-response-systems procurement — move from contract-only to mixed spinning + battery."
```

## Analysis Checklist (arc-kit)

- **Completeness:** anchor set (Activity, Consumers), all user-requested components present (both grid models, all three storage types, full platform + integration stack, full supply chain), dependencies shown, movement arrows present.
- **Positioning:** each component positioned on market evolution — Commodity on the right (Grid, Generation, Hydro, SCADA, Spinning Reserve, Sources), Custom on the left (Distributed Grid, Hydrogen, Energy Platform, Material Supply Chain), Genesis at the far left (Adaptive Integration, Plug-and-Play Energy, Awareness of Energy Supply Chain).
- **Insights:** regulatory/institutional inertia on Traditional Grid, accelerating shift to Distributed Grid, Custom-stage material supply chain still biting, Genesis-stage awareness discipline.
- **Strategic:** gameplay suggestions (Open Source, Standards game, Pioneers/Settlers/Town Planners talent split), climatic patterns (evolution inevitability, past-success inertia, capital flows to novel), explicit opportunities / threats / inertia / recommendations.
