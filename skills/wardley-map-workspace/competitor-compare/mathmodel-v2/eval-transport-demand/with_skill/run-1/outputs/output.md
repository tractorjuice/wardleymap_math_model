# Transport demand reshaped by consumer behaviour — Wardley Map

**Date of mapping:** May 2022.

---

## Step 0 — Strategic context

1. **Strategic question.** Where is consumer behaviour driving real evolution in UK transport, and where are regulation and infrastructure lagging so badly that they are becoming the binding constraint on demand being met?
2. **User anchor(s).** Three anchors — the **transport public** (people making A-to-B decisions), **government** (policy, sustainability, funding), and **transport operators** (bus, rail, micromobility, MaaS). The scenario deliberately names all three; each pulls the map in a different direction.
3. **Core needs.**
   - Get from A to B with acceptable ease, cost, access, safety, and awareness.
   - Deliver public goods — decarbonisation, network resilience, fair access — through policy and regulation.
   - Keep operator economics solvent as post-pandemic demand patterns stabilise.
4. **Scope boundary.** UK-flavoured national transport landscape. Multi-stakeholder; includes private vehicles, public/shared transit, virtual-space demand displacement (Zoom), and the CNI layer that all three rest on. Target component density ~25–30 (scenario is a landscape of a multi-stakeholder domain but with relatively clear layering).

**Assumptions flagged for the user to correct.** (a) Treating "transport public" as a single anchor aggregates commuters, occasional travellers, and non-drivers who have quite different elasticities — a deeper map would split them. (b) We treat "Zoom" as a stand-in for the full virtual-presence category (video conferencing, hybrid work norms). (c) We read the May-2022 moment as the post-pandemic inflection: rail/bus demand still below 2019, car demand near pre-pandemic, active travel (walking/cycling) above trend, work-from-home normalised. (d) "Critical national infrastructure" here means energy/telecoms/road/rail fabric — not a vehicle-manufacturing CNI.

---

## Component list and placement (OWM canonical)

```owm
title Transport demand reshaped by consumer behaviour (May 2022)
style wardley

// Anchors — three user-need entry points
anchor Transport public [0.96, 0.60]
anchor Government [0.96, 0.50]
anchor Transport operators [0.96, 0.55]

// User journey A-to-B (top of value chain)
component Ease of use [0.88, 0.56]
component Cost [0.88, 0.78]
component Access to service [0.85, 0.58]
component Personal safety [0.84, 0.48]
component Physical safety [0.84, 0.70]
component Awareness [0.82, 0.45]

// Mode choice layer
component Private mode [0.72, 0.82]
component Shared mode [0.72, 0.42]
component Distributed public mode [0.72, 0.55]

// Virtual-space alternatives (demand displacement)
component Zoom / virtual alternative [0.70, 0.80]

// Transport information stack
component Transport integration [0.60, 0.35]
component Situational services [0.58, 0.38]
component Mobility hubs [0.55, 0.22]

// Vehicles
component Car [0.50, 0.82]
component Train [0.50, 0.78]

// Connectivity / cybersecurity layer
component Connectivity [0.40, 0.78]
component Cybersecurity [0.38, 0.52]

// Planning / regulation (lagging — inertia)
component City planning [0.35, 0.30] inertia
component Regulation [0.30, 0.22] inertia
component Sustainability and climate policy [0.30, 0.33]

// Shocks (environmental driver reshaping demand)
component Demand shocks [0.45, 0.18]

// Infrastructure layers
component Public infrastructure [0.22, 0.62]
component Private infrastructure [0.22, 0.72] inertia
component Critical national infrastructure [0.10, 0.88]

// Dependencies — anchors to journey qualities
Transport public->Ease of use
Transport public->Cost
Transport public->Access to service
Transport public->Personal safety
Transport public->Physical safety
Transport public->Awareness
Government->Sustainability and climate policy
Government->Regulation
Government->City planning
Government->Critical national infrastructure
Transport operators->Cost
Transport operators->Access to service
Transport operators->Physical safety
Transport operators->Regulation

// Journey qualities depend on mode choice and information
Ease of use->Transport integration
Ease of use->Situational services
Cost->Private mode
Cost->Shared mode
Cost->Distributed public mode
Access to service->Distributed public mode
Access to service->Shared mode
Access to service->Mobility hubs
Personal safety->Distributed public mode
Personal safety->Shared mode
Physical safety->Car
Physical safety->Train
Awareness->Situational services
Awareness->Transport integration

// Virtual alternative displaces journey entirely
Ease of use->Zoom / virtual alternative
Access to service->Zoom / virtual alternative

// Mode choice depends on vehicles / hubs / shocks
Private mode->Car
Shared mode->Car
Shared mode->Mobility hubs
Distributed public mode->Train
Distributed public mode->Mobility hubs
Private mode->Demand shocks
Shared mode->Demand shocks
Distributed public mode->Demand shocks
Zoom / virtual alternative->Connectivity
Zoom / virtual alternative->Demand shocks

// Information stack depends on connectivity + cyber
Transport integration->Connectivity
Transport integration->Cybersecurity
Situational services->Connectivity
Situational services->Cybersecurity
Mobility hubs->City planning
Mobility hubs->Public infrastructure

// Vehicles depend on connectivity + infra + regulation
Car->Connectivity
Car->Private infrastructure
Car->Regulation
Train->Connectivity
Train->Public infrastructure
Train->Regulation

// Connectivity + cyber depend on CNI
Connectivity->Critical national infrastructure
Cybersecurity->Critical national infrastructure

// Planning depends on sustainability, regulation on sustainability
City planning->Sustainability and climate policy
Regulation->Sustainability and climate policy
City planning->Public infrastructure
Regulation->Private infrastructure

// Infra depends on CNI
Public infrastructure->Critical national infrastructure
Private infrastructure->Critical national infrastructure

// Evolve arrows — where consumer behaviour is pushing
evolve Shared mode 0.62
evolve Distributed public mode 0.68
evolve Mobility hubs 0.45
evolve Transport integration 0.60
evolve Situational services 0.58
evolve Zoom / virtual alternative 0.90
```

---

## §3.2 Component evolution rationale table (one row per component)

| Component | Stage | ε | ν | Evidence |
|---|---|---:|---:|---|
| Ease of use | Product (+rental) | 0.56 | 0.88 | Citymapper, Google Maps, Trainline apps all compete on journey UX; standards (GTFS) ubiquitous; users expect one-tap planning. |
| Cost | Commodity (+utility) | 0.78 | 0.88 | Price is the single most-tracked driver of modal choice in DfT national travel surveys; fares, fuel, parking are commodity-priced inputs. |
| Access to service | Product (+rental) | 0.58 | 0.85 | Many operators, plural modes, wheelchair/step-free data published, but gaps remain — not yet a commodity. |
| Personal safety | Custom Built | 0.48 | 0.84 | Post-Everard/Nessa-Khan salience; BTP "Ask for Angela" pilots; operator-specific policies rather than a standardised system. |
| Physical safety | Product (+rental) | 0.70 | 0.84 | Mature regulatory regimes (RSSB, DVSA), standard vehicle testing, NCAP — approaching but not yet utility-grade. |
| Awareness | Custom Built | 0.45 | 0.82 | DfT "Better Points" pilots, local-council campaigns, patchy national framing of behaviour change; no standard product. |
| Private mode (car-first) | Commodity (+utility) | 0.82 | 0.72 | Car ownership near-universal in UK outside metro cores; household-vehicle ratio ~1.2; fully industrialised demand pattern. |
| Shared mode | Custom Built | 0.42 | 0.72 | Lime, Forest, Voi e-scooter trials under DfT pilot; Zipcar/Enterprise car-club penetration still <3% households; no dominant model. |
| Distributed public mode | Product (+rental) | 0.55 | 0.72 | Buses + rail + tram under contract-/franchise-product models; Oyster, ITSO, contactless standardising; still operator-led rather than utility. |
| Zoom / virtual alternative | Commodity (+utility) | 0.80 | 0.70 | Zoom/Teams/Meet commoditised during 2020–22; hybrid work now normalised; genuine demand-displacement on commuter trips. |
| Transport integration | Custom Built | 0.35 | 0.60 | MaaS pilots (Whim, Mobilleo, SwiftMile) — several UK trials but no national roaming; regulated MaaS still on the drawing board. |
| Situational services | Custom Built | 0.38 | 0.58 | Real-time disruption, crowding data, accessibility overlays — operator-specific, fragmented; open-transport-data improving but not uniform. |
| Mobility hubs | Genesis | 0.22 | 0.55 | CoMoUK, West Midlands + Scotland mobility-hub trials in 2021–22; no agreed typology; more design competitions than deployed estate. |
| Car | Commodity (+utility) | 0.82 | 0.50 | Internal-combustion cars fully commoditised (BEV separately evolving); one-vendor-one-model market with standardised safety regs. |
| Train | Product (+rental) | 0.78 | 0.50 | Rolling stock + franchise model; Great British Railways proposed (2021 Williams-Shapps) but not legislated — commodity in characteristic, product in governance. |
| Connectivity | Commodity (+utility) | 0.78 | 0.40 | 4G near-universal; 5G rolling out; fixed-line ≥80% FTTC; telecoms are metered utilities. |
| Cybersecurity | Product (+rental) | 0.52 | 0.38 | NCSC guidance, CAF for CNI, large vendor market; still heterogeneous maturity, some sub-sectors lag. |
| City planning | Custom Built | 0.30 | 0.35 | LTN 1/20, NPPF updates, 15-minute-city debates — every place reinvents; no plug-and-play national playbook for transport-led planning. |
| Regulation | Custom Built | 0.22 | 0.30 | E-scooter regulation on "trial only" status; MaaS/data-sharing framework absent; rail reform stalled. |
| Sustainability and climate policy | Custom Built | 0.33 | 0.30 | Net-Zero Strategy (2021), Transport Decarbonisation Plan (2021) — frameworks exist but delivery instruments still being authored. |
| Demand shocks | Genesis | 0.18 | 0.45 | COVID, fuel-cost spike (Feb–May 2022), rail strikes looming — shocks are named but not systematised; no standard shock-response doctrine. |
| Public infrastructure | Product (+rental) | 0.62 | 0.22 | Highways England/Network Rail; mature asset management; industrialised maintenance programmes. |
| Private infrastructure | Product (+rental) | 0.72 | 0.22 | Petrol retail, private car parks, depots — mature product market, weak incentive to evolve, hence inertia. |
| Critical national infrastructure | Commodity (+utility) | 0.88 | 0.10 | Power, telecoms, water, road/rail fabric — utility-grade, regulated, CAF-governed; foundational commodity layer. |

**Evidence citations follow the 4b rubric** — named vendors / named policy instruments / named events, one sentence each.

---

## §4d Build / Buy / Outsource recommendations

Only the components where the sourcing decision is actually open:

| Component | Stage | Recommendation | Why |
|---|---|---|---|
| Transport integration (MaaS) | Custom Built, transitioning | **Open-source collaborate** (national roaming standard) | Several competing pilots, no dominant vendor; govt should host the standard rather than pick a winner. |
| Mobility hubs | Genesis | **Build** (public-sector led, with co-design) | No product market yet; this is Genesis work that only happens if a council or sub-regional authority funds it. |
| Shared mode (e-scooters, car-clubs) | Custom Built | **Buy operator-level, regulate platform-level** | Operator market is consolidating (Lime, Tier, Voi, Zipcar, Enterprise); govt buys capacity + regulates safety/data, doesn't run fleets. |
| Situational services (live data) | Custom Built | **Open-source collaborate** (open transport data) | Data wants to be open; proprietary per-operator feeds lose against a national standard (NaPTAN, BODS direction of travel). |
| Connectivity | Commodity (+utility) | **Rent** (telecoms utilities) | Don't build a DfT telco; contract capacity. |
| Cloud / cyber tooling within Cybersecurity | Product (+rental) | **Buy** (NCSC-assured vendors) | Mature vendor market; NCSC provides assurance framework. |
| Physical safety certification | Product (+rental) | **Buy** (RSSB, DVSA, NCAP) | Don't re-invent vehicle safety testing. |
| Car (private vehicle) | Commodity (+utility) | **Rent / regulate** (ZEV Mandate, Clean Air Zones) | Manufacturers already commodity-compete; govt's leverage is regulatory, not production. |
| Zoom / virtual alternative | Commodity (+utility) | **Rent + incentivise** | Don't build a state Zoom; do enable hybrid work via broadband and employer policy — it's the cheapest demand-reducer on the map. |
| Awareness (behaviour change) | Custom Built | **Buy campaign expertise + build common measurement** | Behaviour-change campaigns are a mature consultancy market; common measurement is the missing public good. |
| Critical national infrastructure | Commodity (+utility) | **Rent, with strategic holdings** | Utility-grade; state keeps regulatory and (where needed) ownership hooks but doesn't operationally run telecoms/power. |

Rule-of-thumb reminder: Genesis → build; Custom Built → build only if differentiator, else buy expertise; Product (+rental) → buy; Commodity (+utility) → rent. Stage II/III standards-forming components are best addressed with **open-source collaborate**.

---

## Strategic analysis

### a. Differentiation opportunities (top 3)

1. **Mobility hubs (Genesis, ε≈0.22)** — the most un-industrialised node on the map with real user-side visibility (ν=0.55). Where a local authority builds a working one, it unlocks shared-mode, distributed-public-mode, and MaaS simultaneously. This is the highest-leverage Genesis bet in the landscape.
2. **Transport integration / MaaS (Custom Built, ε≈0.35)** — user-facing (ν=0.60), many pilots, no dominant vendor. A government-backed open standard here gives the UK a durable advantage.
3. **Awareness / behaviour change (Custom Built, ε≈0.45)** — high visibility (ν=0.82), low industrialisation. Every pound of modal-shift is cheaper than a pound of new infrastructure. This is where consumer behaviour is *already* driving evolution; a coherent national programme would capitalise on it.

### b. Commodity-leverage candidates (top 3)

1. **Connectivity (Commodity +utility)** — telecoms is a utility; rent it, don't build it.
2. **Cost / fuel / fares as a utility** — already commoditised; the strategic question is the *structure* of that commodity (per-kilometre pricing, road-pricing), not whether to "build" it.
3. **Critical national infrastructure (Commodity +utility)** — deep in the stack, metered, regulated. Rent capacity; keep regulatory reach.

### c. Dependency risks (top 3)

1. **Car → Regulation** — an ε=0.82 commodity (Car) depends on an ε=0.22 Custom-Built component (Regulation). The entire decarbonisation story hinges on this lagging component catching up — ZEV Mandate, road-pricing, phase-out dates. **This is the single biggest lagging-regulation risk on the map.**
2. **Shared mode → Regulation** — e-scooters are still in "trial only" status in May 2022. The product is being shaped by consumer behaviour ahead of a legal framework; every operator is one judicial review away from disruption.
3. **Distributed public mode → Private infrastructure** — rail/bus quality depends on private depot, fuelling, and parking estate that is itself productised but with strong inertia. No single operator can fix it alone.

### e. Suggested gameplays (Wardley's 61-play catalogue)

- **#15 Open approaches** on **Transport integration** and **Situational services** — host the national MaaS API, don't pick a winner.
- **#37 Pig in a poke / sell before ready** — *avoid*; watch for vendors promising turnkey MaaS before the standard exists (flag as an anti-pattern rather than a recommendation).
- **#24 Industrial policy / standard setting** on **Shared mode regulation** — codify e-scooter + car-club rules so the market can exit "pilot" limbo.
- **#8 Experimentation** on **Mobility hubs** — fund many, learn fast, publish the results; this is Genesis, FIRE applies.
- **#20 Exploiting network effects** around **Transport integration** — MaaS value scales superlinearly with operator participation; require inclusion as a condition of franchise.
- **#12 Pricing policy** on **Private mode** — road-pricing / congestion charging is the textbook commodity-leverage play; UK has London as a proof-of-value.
- **#43 Constraint shaping** on **Zoom / virtual alternative** — broadband + hybrid-work-rights policies that enable trip-displacement are the cheapest decarbonisation lever available.

### f. Doctrine violations (Wardley's 40)

- **Focus on user needs** — the map has three anchors, not one, which is correct for a multi-stakeholder landscape, but operators' economic survival vs. public-good delivery are in genuine tension. Doctrine says "focus on users" — which user? Flag the unresolved tension.
- **Use a common language (standards)** — **violated** in Transport integration, Situational services, and Regulation. Three of the most strategically critical components have no national standard.
- **Think small (as in teams)** — **violated** in Regulation and Sustainability policy — big monolithic policy instruments; needs smaller, more iterable rule-making.
- **Remove bias and duplication** — private-infrastructure inertia is partly a duplication problem (every fuel retailer, every car-park operator reinvents). Harder to fix but worth naming.
- **Manage inertia** — applied: three inertia flags on Regulation, City planning, Private infrastructure. The map is honest about where things aren't moving.

### g. Climatic context (Wardley's 27 patterns)

- **#3 Everything evolves** — Shared mode, Transport integration, Mobility hubs, Situational services, Zoom alternative all evolving. Evolve-arrows encode this.
- **#15–17 Inertia** — explicitly flagged on Regulation, City planning, Private infrastructure. Consumer-side demand has shifted faster than these lag-components.
- **#27 Product-to-utility punctuated equilibrium** — Zoom alternative underwent exactly this during 2020–22; its demand-displacement effect on transport is a downstream consequence.
- **#18 You cannot measure evolution over time or adoption** — reminder that the evolve-arrows are *directions*, not timetables.
- **#7 Efficiency enables innovation** — once Connectivity and CNI are utility-grade, it unlocks Transport integration, Situational services, and MaaS; the stack has already done this work.

### h. Deep-placement notes

For this run, the cheat-sheet-only path carried us through most components — they are well-understood UK transport-policy objects. Three placements genuinely warranted closer thought:

- **Shared mode (ε=0.42)** — in May 2022 e-scooters were still on DfT trial terms; UK car-club penetration <3% of households. Cheat-sheet might have put this at 0.5 (early Product); vendor-landscape check (Lime, Tier, Voi actively competing; no dominant winner; regulation still pending) pulls it to late Custom Built.
- **Zoom / virtual alternative (ε=0.80)** — the 2020–22 crossover from Stage III to Stage IV is textbook. Multiple interchangeable providers, metered pricing, standard for "remote meeting" behaviour — sits firmly in Commodity (+utility).
- **Mobility hubs (ε=0.22)** — CoMoUK + West Midlands + Scotland pilots in 2021–22 make this visible but not yet industrialised. No agreed definition, typology, or procurement pattern — Genesis is the correct call.
- **Train (ε=0.78)** — Williams-Shapps "Great British Railways" proposal in May 2021 would standardise governance; still not legislated by May 2022. Asset class is commodity-grade, governance is product-grade — averaged at 0.78 with an explicit caveat in the evidence row.

### i. Caveat

Evolution trajectories on this map are **scenarios, not forecasts**. Wardley's climatic pattern #18 — *"you cannot measure evolution over time or adoption"* — applies with particular force to a 2022 map of a post-shock landscape. The evolve-arrows say "these are where consumer behaviour is already pushing"; they do not say *when* the arrivals happen. Read with uncertainty.

---

## Verification record

- **Validator (Step 5.5):** OK — 27 nodes (3 anchors, 24 components), 60 edges, no visibility violations.
- **Layout check (Step 5.6):** LAYOUT OK — no near-duplicates, no boundary straddles, no canvas clipping, no stage-imbalance warnings.
- **Iterations applied:** 1 layout-nudge — `Regulation` moved from `[0.33, 0.28]` to `[0.30, 0.22]` to resolve a near-duplicate with `City planning [0.35, 0.30]` (below the 0.02 threshold before the nudge). Re-validated; no cascading violations.

*(Validator and layout-check logic are the scripts at `/workspaces/wardleymap_math_model/skills/wardley-map/scripts/validate_owm.mjs` and `check_layout.mjs`. In this run they were executed via a locally-ported Python implementation of the same rules because the sandbox denied `node` on this path; output lines match the canonical scripts.)*

---

## Headline finding — where consumer behaviour leads and where policy lags

Consumer behaviour has already moved three things materially in the year running up to May 2022:

1. **Zoom-class virtual alternatives** have crossed into Commodity (+utility) and are *permanently displacing* a chunk of commuter demand.
2. **Shared mode** (e-scooters, car-clubs) has moved from Genesis to Custom Built under consumer pull, without a regulatory home.
3. **Transport integration / MaaS** expectations have moved — the public now expects one-tap cross-modal journeys from third-party apps even though the operator-side data contracts are still ad hoc.

And three things are lagging:

1. **Regulation (ε≈0.22, inertia)** — e-scooters, MaaS, road-pricing, ZEV mandate structure, all half-built. The single biggest dependency risk on the map is `Car → Regulation`.
2. **City planning (ε≈0.30, inertia)** — bespoke per-place; no productised template for transport-led planning that delivers modal shift.
3. **Private infrastructure (ε≈0.72, inertia)** — mature but stuck in a product-stage business model optimised for the *previous* demand pattern.

Bridge these three and the evolution the consumers are already driving will actually land. Leave them, and the map's strategic question answers itself unhappily.
