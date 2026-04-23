# Energy Disruption Landscape — July 2022

Scenario: Map the landscape of energy disruption — how today's user demand meets tomorrow's survivability. Generation mix, production/transmission/distribution chain, storage problem, market layer, consumer-facing pieces, control/regulation/CO2 apparatus. Show where disruption is most likely, where infrastructure is locked-in, and what the supply-chain awareness and externality picture looks like.

## 1. Mathematical model applied

- **Tuple** `M = (V, E, U, ν, ε, t)` with `t = 2022-07`.
- `|V| = 31` components, `|U| = 2` anchors (two user types: _Today Demand_ and _Tomorrow Survivability_).
- `|E| = 55` directed dependencies.
- Visibility `ν` seeded from `ν(v) = 1/(1+d(v))` then adjusted downward on infrastructure and generation (architecturally invisible to users) and upward on _Price_ and _Security of Supply_ (users think about them directly even though they sit below the behaviour layer).
- Evolution `ε` scored via the quick 4-row cheat-sheet method (ubiquity / certainty / user perception / publication types). See §3 below for representative scorings.
- Every edge `(a,b) ∈ E` satisfies the hard constraint `ν(a) ≥ ν(b)`.

## 2. Two anchors — why

The scenario explicitly contrasts "today's user demand" with "tomorrow's survivability." These are structurally different user needs:

- **Today Demand** is a mature, price-sensitive, availability-sensitive need. It sits at `ε ≈ 0.82` — effectively a Stage IV utility expectation (flip a switch, get power, pay a bill).
- **Tomorrow Survivability** is an emergent need driven by climate, energy-security shock (Russia/Ukraine war, July 2022 context), and intergenerational risk. It sits at `ε ≈ 0.28` — still Custom-Built in the sense that society is actively constructing what "survivable energy" even means.

Running both anchors on the same map is exactly the doctrine "Know your users" at the Phase II level.

## 3. Evolution scoring — representative rows

| Component | Ubiquity | Certainty | User perception | Pub types | Avg ε | Stage |
|---|---|---|---|---|---|---|
| Fossil Generation | IV | IV | IV | IV | 0.875 | Commodity +utility |
| Gas Generation | IV | IV | IV | IV | 0.875 | Commodity +utility — but politically destabilised |
| Legacy Grid Infrastructure | IV | IV | IV | IV | 0.875 | Commodity (with inertia) |
| Price | IV | IV | IV | IV | 0.875 | Commodity |
| Spot Market | IV | IV | IV | IV | 0.875 | Commodity |
| Renewable Generation | III | III | III | II | 0.56 | Product, pushing right |
| Nuclear Generation | III | III | III | II | 0.56 | Product, mixed (political inertia) |
| Solar Microgen | II | III | II | II | 0.40 | Custom Built → Product |
| Electrical Storage | II | II | II | II | 0.375 | Custom Built |
| Potential Energy Storage | III | IV | III | III | 0.625 | Product (pumped hydro is mature) |
| Hydrogen Storage | I | I | I | I | 0.15 | Genesis |
| CO2 Accounting | II | II | II | II | 0.375 | Custom Built |
| Supply Chain Awareness | I–II | II | II | II | 0.28 | Custom Built (early) |
| Tomorrow Behaviour | II | II | II | II | 0.28 | Custom Built (early) |
| Cost with Externalities | I–II | II | II | II | 0.22 | Genesis → Custom Built |
| Public Good Framing | II | II | II | II | 0.30 | Custom Built |

Rows that disagree strongly are flagged as "in transition" — notably _Nuclear Generation_ (mature technology but the build-programme row drags it left) and _Solar Microgen_ (residential adoption is rapid but integration practice is immature).

## 4. OWM output

See `draft.owm` in this directory. Coordinates are `[visibility, evolution]`.

## 5. Strategic analysis

### a. Top 3 by D = ν(1 − ε) — differentiation pressure (visible and immature)

1. **Tomorrow Behaviour** — D = 0.88 × 0.75 = **0.66**. A user-visible, still-unformed need. Whoever helps consumers _change_ behaviour (demand-shifting, prosumer participation, dynamic tariffs) has real advantage room.
2. **Sustainability** — D = 0.85 × 0.70 = **0.60**. Highly visible framing; still immature as an operational product. Huge product-design space.
3. **Education** — D = 0.82 × 0.72 = **0.59**. User-visible knowledge component, very immature. Energy literacy is Wardley's Knowledge layer — and it is underspecified (see doctrine note below).

### b. Top 3 by K = (1 − ν) · ε — commodity leverage (deep and mature)

1. **Legacy Grid Infrastructure** — K = 0.82 × 0.85 = **0.70**. This is the classic utility layer. But it also carries an inertia marker — see below.
2. **Fossil Capex Lock-in** — K = 0.85 × 0.70 = **0.60**. Already a utility-economic commodity; the question is whether it should be deprecated, not outsourced.
3. **Fossil Generation** — K = 0.74 × 0.88 = **0.65**. Fully commoditised; the externality question is moved elsewhere (to _Cost with Externalities_).

### c. Top 3 dependency risks by R(a,b) = ν(a) · (1 − ε(b))

1. **(Tomorrow Behaviour → Cost with Externalities)**: R = 0.88 × 0.78 = **0.69**. Consumer choice about "the right thing to do" depends on an externality cost signal that barely exists yet. This is the defining gap of the map.
2. **(Sustainability → CO2 Accounting)**: R = 0.85 × 0.65 = **0.55**. A highly visible public concept depending on a still-immature accounting practice (Scope 3, embedded carbon, border adjustment).
3. **(Cost with Externalities → Supply Chain Awareness)**: R = 0.72 × 0.78 = **0.56**. Internalising externalities requires upstream traceability that doesn't yet exist at scale.

### d. Suggested gameplays (from Wardley's 61-play catalogue)

- **Open Approaches (#15)** on _CO2 Accounting_ and _Supply Chain Awareness_ — commodity-grade carbon accounting is a public good; pushing open standards accelerates it toward Stage III/IV where its externality-pricing function actually works.
- **Sweat and dump (#57)** / **Pig in a poke (#54)** on _Fossil Capex Lock-in_ — at the asset-holder level, recognise the stranded-asset risk and extract value before the write-down. At the policy level, this is the climate-transition rationale for carbon pricing.
- **Directed investment (#36)** on _Electrical Storage_ and _Hydrogen Storage_ — these are the genuine Genesis → Custom Built → Product pipeline; storage is the choke point between intermittent renewables and reliable supply.
- **Centre of gravity (#3)** and **Cooperation with competitors (#42)** on _Control and Balancing_ — grid balancing in a high-renewables mix is pre-competitive infrastructure; it wants a shared-operator model.
- **Exploit network effects (#13)** on _Solar Microgen_ — each rooftop installed raises the political and economic viability of the next. This is a two-sided effect because prosumers also become balancing participants.
- **Constraint shaping (#35)** on _Legacy Grid Infrastructure_ — the inertia is structural; regulatory constraint-shaping (e.g. mandating interconnection, time-of-use pricing, bidirectional metering) is the direct lever.
- **Pig in a poke / Fear, Uncertainty and Doubt** caution — note that in energy, FUD is a _gameplay_ used against renewables by incumbents; name it, don't import it.

### e. Doctrine observations

- **"Know your users" (Phase II)** — explicitly honoured: two anchors (Today Demand vs. Tomorrow Survivability). Many real energy strategies conflate these, which is why they satisfy neither.
- **"Focus on high awareness"** and **"A bias towards action"** — both pushed toward _Tomorrow Behaviour_ and _Education_, which are the highest-D components.
- **Knowledge layer underspecified** — _Education_ is a placeholder for a much richer Knowledge component set (thermodynamics literacy, system-risk literacy, intergenerational accounting). Flag this as a doctrine violation to be fixed in the next iteration.
- **"Use appropriate methods" / "Think small"** — the inertia trio (Legacy Grid, Fossil Capex, Nuclear Build Programme) is genuinely large-scale, but the disruption-adjacent work (microgen, storage, demand response) is small-unit and should not be procured on utility-scale contracts.
- **"Manage inertia"** — three inertia markers are set deliberately; the 17-forms mapping: _Legacy Grid_ = sunk-capital + re-architecture-cost; _Fossil Capex Lock-in_ = sunk-capital + second-sourcing risk + political capital; _Nuclear Build Programme_ = political capital + regulatory capital + human capital.
- **"Optimise flow" / "Remove bias and duplication"** — the market layer (Spot, OTC, Price) is commoditised; the externality-accounting layer (CO2, Supply Chain) is not. The mismatch is the distortion.

## 6. Where the disruption is most likely

Reading the map as a landscape:

- **Horizontally near the middle, vertically near the top** is where disruption concentrates — the `D`-heavy region. _Tomorrow Behaviour_, _Sustainability_, _Education_, and _Cost with Externalities_ all sit there. Disruption here looks like: dynamic tariffs, demand-response products, prosumer platforms, embedded-carbon pricing, consumer carbon scores.
- **Lower-left (Genesis → Custom Built)** is where technical disruption incubates: _Hydrogen Storage_, _Electrical Storage_, _Solar Microgen_, _Supply Chain Awareness_, _CO2 Accounting_. Storage is the most load-bearing of these because it unlocks everything to its right.
- **Lower-right (inertia band)** is where disruption is _resisted_ rather than produced: _Legacy Grid_, _Fossil Capex Lock-in_, _Nuclear Build Programme_. These are where the fight is.

## 7. Externality picture

The externality structure of the map has a specific shape:

- _Price_ is a Stage IV commodity that **does not internalise externalities**.
- _Cost with Externalities_ is a Stage I→II component that is still being invented (carbon border adjustments, embedded carbon in supply chains, methane accounting).
- _CO2 Accounting_ and _Supply Chain Awareness_ are the mechanisms by which the externality could be priced; they are early-Custom-Built.
- The gap between `ε(Price) ≈ 0.88` and `ε(Cost with Externalities) ≈ 0.22` is **the** market failure that the rest of the map is responding to.

The disruption thesis, in one sentence: _the externality gap between Price and true cost is the attractor; every high-D component on the map exists because that gap exists._
