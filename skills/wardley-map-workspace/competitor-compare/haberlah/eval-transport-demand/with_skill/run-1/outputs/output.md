# Wardley Map Analysis: Consumer Behaviour Reshaping Transport Demand (May 2022)

## Purpose

This map answers the question: **In May 2022, where is changing consumer behaviour driving real evolution in the transport value chain, and where are regulation and infrastructure lagging?** It is a landscape map for the UK/Western transport ecosystem as it emerges from the pandemic — commuter patterns are permanently changed (hybrid work, Zoom), fuel prices have just been shocked by the Ukraine invasion, and a still-forming MaaS (Mobility-as-a-Service) stack is being asked to do more than its maturity supports.

## Strategic Context (answered from the brief)

The skill's Step 1 asks for four inputs. Because this is an offline benchmark delivered as a single prompt, the answers below are inferred from the brief rather than solicited from a live user.

| Question | Answer used |
|---|---|
| Strategic question | "Where is consumer behaviour driving transport evolution, and where are regulation and infrastructure lagging?" |
| User anchors | Government, Transport Public, Transport Operators — the three constituencies named in the brief |
| Core needs | Ease of use, Cost, Access to service, Safety (personal + physical), Awareness |
| Scope boundary | UK/Western transport ecosystem, May 2022 — post-COVID, post-Ukraine-fuel-shock |

## Value Chain Overview

Working backward from the three anchors produces 22 nodes (3 anchors + 19 components). This is at the upper bound of the skill's 8-18 component guideline; it reflects the deliberate breadth the brief asks for ("user journey → information stack → mode choice → vehicles → connectivity → planning → infrastructure → regulation → sustainability → shocks → virtual alternatives"). The stack falls naturally into six bands:

- **User needs band (visible, 0.80-0.88)**: Ease of Use, Cost, Access to Service, Safety, Awareness
- **Substitute band (0.76)**: Virtual Alternatives — Zoom displaces a slice of commute demand
- **Mode choice band (0.64-0.68)**: Private, Shared, Distributed Public
- **Information stack band (0.44-0.56)**: Transport Integration (MaaS), Situational Services, Mobility Hubs
- **Vehicle + policy band (0.28-0.40)**: Car, Train, Regulation, City Planning, Connectivity & Cyber
- **Infrastructure band (invisible, 0.08-0.18)**: Transport Infrastructure, CNI

## OWM (OnlineWardleyMaps) Text Block

```
title Consumer Behaviour Reshaping Transport Demand (May 2022)
style wardley

anchor Government [0.96, 0.40]
anchor Transport Public [0.96, 0.52]
anchor Transport Operators [0.96, 0.62]

component Ease of Use [0.88, 0.48]
component Cost [0.86, 0.60]
component Access to Service [0.84, 0.52]
component Safety [0.85, 0.40]
component Awareness [0.82, 0.28]

component Virtual Alternatives [0.76, 0.70]

component Private Mode [0.68, 0.82]
component Shared Mode [0.66, 0.50]
component Distributed Public [0.64, 0.30]

component Transport Integration [0.56, 0.28]
component Situational Services [0.50, 0.42]
component Mobility Hubs [0.44, 0.20]

component Car [0.38, 0.78]
component Train [0.36, 0.68]

component Regulation [0.40, 0.42] inertia
component City Planning [0.30, 0.48]
component Connectivity & Cyber [0.28, 0.70]

component Transport Infrastructure [0.18, 0.65] inertia
component CNI [0.08, 0.86]

Government->Safety
Government->Regulation
Government->City Planning
Government->Access to Service

Transport Public->Ease of Use
Transport Public->Cost
Transport Public->Access to Service
Transport Public->Safety
Transport Public->Awareness

Transport Operators->Cost
Transport Operators->Access to Service
Transport Operators->Safety
Transport Operators->Awareness

Ease of Use->Transport Integration
Ease of Use->Situational Services
Cost->Shared Mode
Cost->Distributed Public
Cost->Private Mode
Access to Service->Mobility Hubs
Access to Service->Distributed Public
Access to Service->Shared Mode
Safety->Regulation
Safety->Connectivity & Cyber
Awareness->Situational Services
Awareness->Transport Integration

Virtual Alternatives->Connectivity & Cyber

Private Mode->Car
Shared Mode->Car
Shared Mode->Transport Integration
Distributed Public->Train
Distributed Public->Mobility Hubs
Distributed Public->Transport Integration

Transport Integration->Situational Services
Transport Integration->Connectivity & Cyber
Situational Services->Connectivity & Cyber
Situational Services->Mobility Hubs
Mobility Hubs->City Planning
Mobility Hubs->Transport Infrastructure

Car->Transport Infrastructure
Car->Connectivity & Cyber
Train->Transport Infrastructure

Regulation->City Planning
City Planning->Transport Infrastructure
Connectivity & Cyber->CNI
Transport Infrastructure->CNI

evolve Transport Integration 0.55
evolve Situational Services 0.62
evolve Mobility Hubs 0.45
evolve Distributed Public 0.52
evolve Shared Mode 0.70
evolve Awareness 0.48
evolve Virtual Alternatives 0.82

annotation 1 [[0.54, 0.22]] MaaS stack is where consumer behaviour is driving real evolution — left-to-right pressure from post-COVID demand.
annotation 2 [[0.38, 0.40]] Regulation carries inertia: it lags the consumer-driven modes above it.
annotation 3 [[0.76, 0.72]] Zoom is Product/Commodity — it permanently displaces a slice of commute demand.
annotation 4 [[0.18, 0.60]] Transport Infrastructure carries inertia: 30-50y asset lifecycles cannot track consumer-behaviour speed.
annotation 5 [[0.68, 0.82]] Private Mode (car) is Commodity but under cost pressure from fuel (Ukraine shock, May 2022) and climate policy.

note SHOCKS: COVID, fuel, climate [0.92, 0.10]
```

## Component Evolution Assessment

| Component | Stage | Position [vis, mat] | Rationale |
|---|---|---|---|
| Government | Anchor | [0.96, 0.40] | Top-of-chain constituency; placed at mode-choice maturity centroid. |
| Transport Public | Anchor | [0.96, 0.52] | Travelling public — the demand side whose behaviour is shifting. |
| Transport Operators | Anchor | [0.96, 0.62] | Private and public operators (rail franchises, bus groups, car-club operators). |
| Ease of Use | Product | [0.88, 0.48] | Well-understood need; Apple Maps/Citymapper/Google Maps have defined user expectations. |
| Cost | Product | [0.86, 0.60] | Price sensitivity is universal and well-measured — fare structures, fuel costs, subscription modes are all Product-grade. |
| Access to Service | Product | [0.84, 0.52] | Clear need with mature delivery patterns (timetables, on-demand, station catchments). |
| Safety | Product (+Commodity) | [0.85, 0.40] | Mature regulatory concept; personal safety (harassment, lighting) less commoditised than physical safety (rail signalling, vehicle standards) — aggregated here. |
| Awareness | Custom-Built | [0.82, 0.28] | Consumers' awareness of multimodal options is still forming in May 2022; no dominant product solves "which mode is best for this trip?" |
| Virtual Alternatives | Product | [0.76, 0.70] | Zoom, Teams, Meet are Product-grade commoditising fast; displaces commute demand — placed as a peer of Mode Choice because it substitutes for it. |
| Private Mode | Commodity | [0.68, 0.82] | Car ownership is universal, standardised, taken for granted. Evolve arrow would push it slightly further right but climate/fuel shock (below) is creating real inertia. |
| Shared Mode | Product, evolving | [0.66, 0.50] | Uber/Bolt/Lyft/car-club operators are a competitive Product market; e-scooter rental is behind. Evolves to 0.70 (Commodity) in 12-24m as integration with MaaS hardens. |
| Distributed Public | Custom-Built, evolving | [0.64, 0.30] | Demand-responsive transit, flexible bus, rural DRT — still bespoke in May 2022. Evolves to 0.52 as operators adopt common platforms. |
| Transport Integration (MaaS) | Custom-Built, evolving fast | [0.56, 0.28] | Whim (Helsinki), Jelbi (Berlin) are live; UK MaaS is pilot-scale. Evolves to 0.55 (Product) as 2020s progress. |
| Situational Services | Custom-Built → Product | [0.50, 0.42] | Real-time disruption, journey update, crowding data — uneven coverage in May 2022 (rail decent, bus patchy). Evolves to 0.62. |
| Mobility Hubs | Custom-Built | [0.44, 0.20] | Concept defined but only ~dozens of true multimodal hubs exist in the UK. Evolves to 0.45 as LTAs deliver. |
| Car | Commodity | [0.38, 0.78] | Manufacturing, ownership, fuelling all Commodity. EV sub-component is Product and evolving, but aggregate is Commodity. |
| Train | Product (+Commodity) | [0.36, 0.68] | Well-understood mode; rolling stock and signalling have multiple vendors; but reliability outcomes vary enough that it is not fully Commodity. |
| Regulation | Product (lagging) | [0.40, 0.42] inertia | DfT regulatory frameworks are Product-grade but **inertia marker** because regulation of new modes (e-scooters, MaaS data, autonomy) trails consumer adoption. |
| City Planning | Product | [0.30, 0.48] | Established discipline (local plans, LTPs); Good Practice methods are documented and trainable. |
| Connectivity & Cyber | Commodity (connectivity) / Product (cyber) | [0.28, 0.70] | 4G/5G coverage is Commodity; transport-specific cybersecurity (OT/rail signalling, connected-vehicle) is Product and still hardening. |
| Transport Infrastructure | Commodity, inertia-bound | [0.18, 0.65] inertia | Roads, rail, stations — Commodity in form but **inertia marker** because 30-50y asset lifecycles cannot move at consumer-behaviour speed. |
| CNI | Commodity | [0.08, 0.86] | Critical National Infrastructure (power, water, networks) underpins everything; fully Commodity/Utility. |

## Where Consumer Behaviour Is Driving Real Evolution

Four components are on active rightward arrows, all driven by post-COVID consumer behaviour change:

1. **Virtual Alternatives → 0.82.** This is the sharpest consumer-behaviour signal on the map. Zoom/Teams/Meet have gone from novelty to default in 24 months and are actively substituting for commute and business-travel demand. This is not a transport component that is evolving — it is a **demand-displacing substitute** that sits inside the transport question.
2. **Shared Mode → 0.70.** Rideshare and car-club demand rebounded quickly and are integrating with MaaS apps. Users who deferred car purchase during the pandemic are sustaining shared demand.
3. **Transport Integration (MaaS) → 0.55 and Situational Services → 0.62.** Consumers now expect app-mediated, multimodal, real-time journey planning. The supply side (MaaS platforms) is racing to catch up with the demand.
4. **Awareness → 0.48 and Mobility Hubs → 0.45 and Distributed Public → 0.52.** All three are in Custom-Built territory but under consumer pull.

## Where Regulation and Infrastructure Are Lagging

The map carries **two inertia markers**, both deliberate:

- **Regulation [0.40, 0.42] inertia.** Regulation *as a capability* is Product-grade, but the specific regulatory regimes for e-scooters (still a trial in May 2022), connected/autonomous vehicles, MaaS data-sharing, and gig-economy driver classification are all trailing consumer adoption. Inertia is *operator/policy* inertia: the activity is Product, the instance is lagging.
- **Transport Infrastructure [0.18, 0.65] inertia.** Physical assets with 30-50 year lifecycles cannot evolve at consumer-behaviour speed. This is Wardley's "change vs. lifecycle mismatch" in classic form — the lower we go in the stack, the more the asset base is locked in.

City Planning [0.30, 0.48] does not carry an inertia marker but is **lag-prone** in a related sense: the cycle time of a Local Transport Plan (~5 years) is short compared to infrastructure but slow compared to app-layer evolution.

## Key Strategic Observations

1. **The map has a "pinch point" between 0.40 and 0.60 visibility, at the 0.20-0.50 maturity band.** This is where the MaaS information stack lives (Transport Integration, Situational Services, Mobility Hubs) alongside Regulation. It is the most active zone on the map — everything here is moving rightward under demand pressure, except Regulation which carries inertia.
2. **Virtual Alternatives sits above Mode Choice, not beside it.** This is deliberate: Zoom does not compete with Private/Shared/Distributed — it competes with the *need to travel*. Its effect is to shrink the pool of demand that reaches mode choice at all.
3. **Private Mode is Commodity but destabilising.** Car ownership remains Commodity but is under a two-front pressure (fuel cost + climate policy). The evolve arrow is small because Commodity components do not easily regress; the pressure shows up instead in shifting *share* toward Shared and Distributed Public.
4. **The "consumer behaviour → evolution" story is an information-stack story.** The vehicles (Car, Train) and infrastructure below them are not the site of evolution. The information stack (MaaS + Situational Services + Mobility Hubs) is where Custom-Built components are being pulled rapidly toward Product under consumer demand.
5. **Safety is anchored to two kinds of inertia.** Personal safety (harassment, lighting, station staffing) depends on Regulation (inertia). Physical safety depends on Transport Infrastructure (inertia). Any major safety-driven behaviour shift is therefore gated by two of the map's slowest components.

## Doctrine Check

Against the Wardley doctrine principles (see `references/doctrine-and-gameplay.md`):

- **Focus on user needs — satisfied.** The five named needs sit immediately below the anchors with clear dependency chains.
- **Know your users — partially satisfied.** Three anchors is correct for the brief, but the Transport Public is heterogeneous (commuter, occasional, rural, disabled) — a sub-segmented anchor list would strengthen the map.
- **Remove bias and duplication — check.** Situational Services and Transport Integration both touch real-time data; Mobility Hubs and Transport Integration both touch inter-modal exchange. The map resolves this by placing them in dependency order (Integration depends on Situational Services depends on Mobility Hubs) rather than as peers.
- **Use appropriate methods per stage.** The inertia markers flag the doctrine violation: Regulation and Infrastructure are being asked to respond at Product/Product-Rental pace while they operate on Commodity/Utility lifecycles.
- **Be pragmatic about maps — not rooms with all the data.** This map omits multi-operator rail franchising, freight, aviation, and active-travel components. All are defensible omissions for a consumer-behaviour map.

## Recommended Actions

Ordered by leverage (map-topology-derived):

1. **Invest in the Transport Integration / Situational Services / Mobility Hubs cluster.** This is the largest concentration of Custom-Built components under consumer pull. Public investment (DfT, LTAs) and operator investment here creates disproportionate user-journey improvement.
2. **Close the regulation gap on e-scooters, MaaS data, and autonomy.** Regulation's inertia is a *policy* inertia, not an intrinsic capability inertia. It is removable. Match the Custom-Built → Product pace of the modes it regulates.
3. **Treat Virtual Alternatives as a transport scenario variable, not an external factor.** Modal forecasts through to 2030 must bake in permanent virtual substitution of ~20-40% of pre-2020 commute demand. This affects all investment cases below the Mode Choice band.
4. **Protect Cost as a user need in the cost-of-living shock.** With fuel prices elevated by the Ukraine invasion, Shared Mode and Distributed Public have a short window to win behavioural shifts that would otherwise be sticky for years.
5. **Sequence the infrastructure conversation honestly.** Because Transport Infrastructure and CNI cannot evolve at consumer-behaviour speed, strategy should focus on upper-stack change (MaaS + modes) and treat infrastructure as a long-horizon, gradient-of-change problem rather than a responsive lever.

## Build vs. Buy Assessment

| Component | Recommendation | Rationale |
|---|---|---|
| Transport Integration (MaaS) | **Build/invest** (public + large operators) | Custom-Built; still differentiating; integration decisions lock in network effects for a decade. |
| Situational Services | **Buy/partner** | Multiple Product-grade providers for rail and road data exist; no advantage in building. |
| Mobility Hubs | **Build** (public, LTA-led) | Place-based; cannot be outsourced; site selection is the strategy. |
| Awareness campaigns | **Build** | Tailored to local modal mix; not a commodity product. |
| Car / Train (vehicles) | **Buy** | Commodity/Product vehicle manufacturing; no advantage in building. |
| Connectivity | **Buy** | Commodity utility. |
| Cybersecurity (transport-specific) | **Partner** | Product-stage; use specialist suppliers (OT security). |
| Transport Infrastructure | **Maintain** (long-cycle capital) | Existing asset base dominates; new-build decisions lock in 30-50y. |
| Regulation (as capability) | **Build** (public) | Sovereign function. |

## Evolution Predictions (12-24 months)

- **Transport Integration** moves from 0.28 → 0.55. UK MaaS moves out of pilot into operational at three-to-five city scale; national account integrations harden.
- **Situational Services** moves 0.42 → 0.62. Rail real-time data standardises; bus CAV AVL coverage closes the last gaps.
- **Shared Mode** moves 0.50 → 0.70. Consolidation (Uber-style) and integration into MaaS brings it to Commodity.
- **Virtual Alternatives** moves 0.70 → 0.82. Continued Commodity compression as hybrid work becomes default and as VR/AR meeting tools begin to bite.
- **Regulation** should move 0.42 → ~0.55 but the inertia marker says it won't. This is the single biggest risk on the map.
- **Distributed Public** moves 0.30 → 0.52 if DRT platform standardisation accelerates; more uncertain than the MaaS moves.
- **Awareness** moves 0.28 → 0.48 as multimodal journey-planning apps become defaults for under-35s.

## Open Questions

1. **Does the Transport Public sub-segment matter for this map?** Disabled, rural, low-income, and under-35 users experience the evolution very differently. A multi-anchor map with sub-segmented anchors might expose inertia the current map hides.
2. **Where should active travel (walk, cycle, e-bike) sit?** Omitted here to keep component count within bounds, but it is the fastest-growing mode in some cities and arguably belongs as a fourth Mode Choice peer.
3. **Is Virtual Alternatives really Product at 0.70, or already Commodity (0.75+)?** A case can be made for either; the evolve arrow to 0.82 assumes rapid further commoditisation. If it is already Commodity, the displacement effect on transport demand is structural and permanent.
4. **What is the right representation of Shocks?** The map represents them as a note rather than a component because they are not on an evolution journey — they are exogenous. A fuller treatment would use Wardley's climatic-pattern overlay for shocks.
