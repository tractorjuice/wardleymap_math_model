# Electrical Energy Storage Landscape (April 2023)

Generated from the prompt-only baseline (`prompts/wardley_map_generator.md`).

## Components V and Anchors U

**Anchor (user need):** Consumers — end users of electricity.

**Activities / capabilities:** Activity, Control, Electricity Generation, Grid.

**Grid architecture split:** Traditional Grid (single-machine view) vs Distributed Grid (fault-tolerant, TCP/IP-style).

**Control plane:** Auto Generation Control (AGC), SCADA, Spinning Reserve, Fast-Response Systems.

**Platform / integration:** Energy Platform, Integration Layer (Pre-approval/Discovery), Adaptive Integration, Plug-and-Play Integration.

**Storage types:** Electrical Storage (Batteries), Hydro Storage (Pumped), Hydrogen Storage.

**Supply chain:** Sources, Stockpile, Material Supply Chain, Supply Chain Awareness.

## Dependencies E (highlights)

- Consumers → Activity, Control
- Activity → Electricity Generation, Grid
- Control → Grid, AGC
- Grid → {Traditional, Distributed}
- Traditional → AGC → {SCADA, Spinning Reserve}; Traditional → SCADA
- Distributed → {Fast-Response Systems, Energy Platform}
- Energy Platform → Integration Layer → {Adaptive, Plug-and-Play}
- Energy Platform → {Electrical, Hydro, Hydrogen} Storage
- Storage → {Sources, Material Supply Chain}
- Sources → {Stockpile, Material Supply Chain}
- Material Supply Chain → Supply Chain Awareness

## Visibility ν (Y-axis)

Seeded by distance from the anchor, then adjusted so that every edge satisfies ν(a) ≥ ν(b). Top layer (Activity/Control) is near the anchor; storage and supply-chain components sit at the bottom. SCADA and Spinning Reserve are deliberately placed below AGC to reflect that both are architecturally invisible support for the control plane.

## Evolution ε (X-axis) — cheat-sheet placements

Using the quick 4-row method (Ubiquity / Certainty / User Perception / Publication Types) averaging stage midpoints {0.125, 0.375, 0.625, 0.875}. April-2023 reading:

| Component | Stage | ε |
|---|---|---|
| Traditional Grid (Single-Machine View) | III, transitioning to IV in developed markets; but stagnant architecture | 0.62 |
| Distributed Grid (TCP/IP-style) | II (Custom Built) — active build-out, rapid learning | 0.32 |
| AGC | IV — commonly understood, focused on use | 0.70 |
| SCADA | IV — commoditised industrial standard | 0.78 |
| Spinning Reserve | IV — standard utility practice | 0.72 |
| Fast-Response Systems | II — rapid learning, battery-led | 0.38 |
| Energy Platform | II — build/construct/awareness stage | 0.30 |
| Integration Layer (Pre-approval/Discovery) | II, edging toward I on pre-approval | 0.22 |
| Adaptive Integration | I–II — still "describe the wonder" | 0.18 |
| Plug-and-Play Integration | II — leading edge | 0.28 |
| Electrical Storage (Batteries) | III (Product) — Li-ion rapidly increasing ubiquity | 0.58 |
| Hydro Storage (Pumped) | IV — widespread, stabilising; century-old | 0.82 |
| Hydrogen Storage | I — poorly understood at grid scale | 0.18 |
| Sources | III–IV | 0.70 |
| Stockpile | III | 0.55 |
| Material Supply Chain | II — rapid learning under stress (lithium, cobalt, nickel) | 0.35 |
| Supply Chain Awareness | I–II — still being built | 0.22 |

## OWM Map

See `draft.owm`. Rendered-in-source summary:

```owm
title Electrical Energy Storage Landscape (April 2023)
style wardley

anchor Consumers [0.98, 0.70]
component Activity [0.90, 0.55]
component Control [0.85, 0.40]
component Electricity Generation [0.78, 0.72]
component Grid [0.74, 0.68]
component Traditional Grid (Single-Machine View) [0.66, 0.62] inertia
component Distributed Grid (Fault-Tolerant, TCP/IP-style) [0.64, 0.32]
component Auto Generation Control (AGC) [0.58, 0.70]
component SCADA [0.56, 0.78] inertia
component Spinning Reserve [0.54, 0.72] inertia
component Fast-Response Systems [0.52, 0.38]
component Energy Platform [0.48, 0.30]
component Integration Layer (Pre-approval / Discovery) [0.44, 0.22]
component Adaptive Integration [0.42, 0.18]
component Plug-and-Play Integration [0.40, 0.28]
component Electrical Storage (Batteries) [0.36, 0.58]
component Hydro Storage (Pumped) [0.34, 0.82]
component Hydrogen Storage [0.32, 0.18]
component Sources [0.24, 0.70]
component Stockpile [0.20, 0.55]
component Material Supply Chain [0.14, 0.35]
component Supply Chain Awareness [0.12, 0.22]
```

## 9. Strategic Analysis

### a. Top 3 by Differentiation pressure D(v) = ν(v) · (1 − ε(v))

1. **Control** — D = 0.85 × 0.60 = 0.51. Visible user-facing capability that is still being redefined (especially as distributed grids reshape what "control" means). Worth building in-house.
2. **Distributed Grid (Fault-Tolerant, TCP/IP-style)** — D = 0.64 × 0.68 = 0.44. Immature architecture just below the Grid abstraction — high differentiation if an operator gets there first.
3. **Activity** — D = 0.90 × 0.45 = 0.41. User-defined demand shape (time-of-use, EV charging patterns, industrial load) is visible and still evolving.

### b. Top 3 by Commodity leverage K(v) = (1 − ν(v)) · ε(v)

1. **Hydro Storage (Pumped)** — K = 0.66 × 0.82 = 0.54. Mature, deep, fully understood — treat as utility infrastructure / procure at commodity terms.
2. **SCADA** — K = 0.44 × 0.78 = 0.34. Deeply commoditised industrial control stack — buy, don't build.
3. **Spinning Reserve** — K = 0.46 × 0.72 = 0.33. Standard utility capability, procurable from the wholesale market.

### c. Top 3 Dependency Risks R(a, b) = ν(a) · (1 − ε(b))

1. **(Fast-Response Systems, Electrical Storage Batteries)** — R = 0.52 × 0.42 = 0.22. The whole distributed-grid value proposition leans on a storage tier that is Stage III but moving, with material-supply-chain fragility underneath.
2. **(Electrical Storage Batteries, Material Supply Chain)** — R = 0.36 × 0.65 = 0.23. **This is where material supply chain risk is biting**: Li-ion has been Product-stage for years, but the cells depend on a Stage II supply chain (lithium, cobalt, nickel, graphite) that became acutely fragile post-2022.
3. **(Energy Platform, Integration Layer Pre-approval/Discovery)** — R = 0.48 × 0.78 = 0.37. Platform promise depends on pre-approval/discovery mechanisms still being invented — major execution risk for anyone betting on the platform.

### d. Suggested Gameplays (from the 61-play catalogue)

- **Open Approaches** applied to the **Energy Platform + Integration Layer** — open-source or open-standard the plug-and-play/pre-approval interfaces to push them from Custom Built → Product, commoditising the integration layer beneath a proprietary platform.
- **Pig in a Poke / Embrace and Extend** applied to **SCADA** — wrap legacy SCADA with modern APIs so Distributed Grid tenants see a uniform control surface, then harvest the commoditised base.
- **Tower and Moat** applied to **Distributed Grid + Fast-Response Systems** — the combination is where the strategic moat is being built. Fast-response + batteries + distributed grid is the "tower"; SCADA/AGC vendors are the moat being dug around the legacy model.
- **Co-option** applied to **Hydro Storage (Pumped)** — co-opt existing pumped-hydro capacity as the balance-of-plant for a distributed grid fleet; cheaper than new capacity.
- **Sweat and Dump** applied to **Traditional Grid (Single-Machine View)** — operators should sweat remaining value out of traditional-model assets while redirecting capex to the distributed/platform stack.
- **Two-factor market / Ecosystem** on **Energy Platform** — classic platform play: consumer-side + storage-provider-side + integration SDK.
- **Standards Game** on **Plug-and-Play Integration** — whoever defines the pre-approval/plug-and-play standard gets the integration tax.

### e. Doctrine Observations

- **Focus on user needs (Phase I):** The scenario names "consumers" as the anchor — good. A stronger version would split into *residential consumer*, *industrial consumer*, and *grid operator* (three distinct user-need profiles with very different visibility stacks). The current single anchor is defensible but loses some texture.
- **Think small (as in know the details):** The two storage types with very different maturity (Hydro Stage IV vs Hydrogen Stage I) need different gameplays — treating "storage" as one component would be a doctrine violation. We've split them, which is correct.
- **Challenge assumptions:** The climatic pattern "efficiency enables innovation" applies — commoditising the Integration Layer is what *lets* differentiation emerge at the Fast-Response layer.
- **Manage inertia:** Three inertia markers (Traditional Grid, SCADA, Spinning Reserve) reflect real sources of resistance — sunk capital, regulatory-approval inertia, and human capital of utility operators trained on the single-machine view. These map to Wardley's inertia forms: *sunk capital* (Traditional Grid), *existing practice / human capital* (SCADA/AGC operators), and *political capital* (regulators comfortable with the legacy model).
- **Apply appropriate methods:** The left side of this map (Genesis/Custom Built — Distributed Grid, Energy Platform, Hydrogen) needs Agile / in-house / venture methods. The right side (SCADA, Hydro, AGC) needs Lean / Six Sigma / procured methods. An operator applying one method universally would violate doctrine.

## Where the scenario-specific questions land on the map

**"Where are distributed fault-tolerant grids evolving faster than the traditional control model?"**

The answer is at the interface between **Grid** (ν 0.74) and its two alternatives:

- Traditional Grid: ε = 0.62, inertia-marked, stuck in late Stage III.
- Distributed Grid: ε = 0.32 and moving rapidly — projected to 0.55 (scenario, not forecast).

The delta is biggest at the **Fast-Response Systems → Electrical Storage (Batteries)** slice: batteries have moved Genesis → Product in ~15 years while AGC/SCADA has essentially not moved. The `evolve` arrows on Distributed Grid, Fast-Response, Electrical Storage, and Plug-and-Play Integration collectively visualise this.

**"Where is material supply chain risk biting?"**

At the bottom of the map, on the `Electrical Storage (Batteries) → Material Supply Chain` and `Hydrogen Storage → Material Supply Chain` edges. The Material Supply Chain sits at ε = 0.35 (Stage II — rapid learning under stress) with a dependency-risk score R = 0.23 feeding a Stage III component that is pulling the whole Distributed Grid play. The `Material supply chain risk biting here` note is positioned on that edge.

## Disclaimer

The evolution arrows (`evolve ...`) are **scenarios, not forecasts** — Wardley's climatic pattern is that evolution cannot be measured over time. The logistic form dε/dt = r·ε·(1−ε) was not used here; the arrows are qualitative "if pressure continues" targets.
