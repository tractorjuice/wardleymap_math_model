# Changing Consumer Behaviour and Transport Demand (May 2022)

Prompt-only baseline run. Scenario: mapping how changing consumer behaviour is reshaping transport demand in May 2022, with three user anchors (government, the transport public, transport operators).

## 1. Mathematical Model Recap

Map tuple $\mathcal{M} = (V, E, U, \nu, \varepsilon, t)$ with:

- $U = \{\text{Government}, \text{Transport Public}, \text{Transport Operators}\}$ — three anchors reflecting the scenario's instruction.
- $|V| \approx 27$ components covering user journey, information stack, mode choice, vehicles, connectivity/cyber, planning/regulation, infrastructure.
- Visibility $\nu$ seeded by $1/(1+d(v))$ from the anchor set, then adjusted by value-chain judgment.
- Evolution $\varepsilon$ scored via the quick 4-row cheat-sheet method (Ubiquity, Certainty, User Perception, Publication Types), averaged to a midpoint.

## 2. OWM Output

See `draft.owm` for the canonical file. Reproduced inline for review:

```owm
title Changing Consumer Behaviour and Transport Demand (May 2022)
style wardley

anchor Government [0.98, 0.55]
anchor Transport Public [0.98, 0.70]
anchor Transport Operators [0.97, 0.60]

// Layer 1 — user journey
component Ease of Use [0.90, 0.55]
component Cost [0.89, 0.75]
component Access to Service [0.88, 0.65]
component Personal Safety [0.87, 0.55]
component Physical Safety [0.86, 0.70]
component Awareness [0.85, 0.50]

// Layer 2 — transport information stack
component Transport Integration [0.75, 0.40]
component Situational Services [0.72, 0.35]
component Mobility Hubs [0.70, 0.30]

// Layer 3 — mode choice
component Private Mode [0.62, 0.75]
component Shared Mode [0.60, 0.45]
component Distributed Public Mode [0.58, 0.35]

// Virtual alternative
component Virtual Space (Zoom) [0.68, 0.80]

// Shocks
component Demand Shocks (Pandemic, Fuel) [0.78, 0.20]

// Vehicles
component Car [0.48, 0.80]
component Train [0.46, 0.65]

// Connectivity layer
component Connectivity [0.38, 0.82]
component Cybersecurity [0.36, 0.55]

// Planning and regulation
component City Planning [0.42, 0.35] inertia
component Regulation [0.40, 0.30] inertia
component Sustainability and Climate Policy [0.44, 0.30]

// Infrastructure and CNI
component Public Infrastructure [0.25, 0.55] inertia
component Private Infrastructure [0.24, 0.70]
component Critical National Infrastructure [0.12, 0.60]
```

(Full edge list, evolution arrows, and notes are in `draft.owm`.)

## 3. Evolution Scoring Rationale (quick-4 cheat sheet)

Representative scoring for the non-obvious components:

| Component | Ubiquity | Certainty | User Perception | Publication | Avg ε | Band |
|---|---|---|---|---|---|---|
| Transport Integration | II | II | II | II | 0.375 | Custom Built |
| Mobility Hubs | I | II | I | II | 0.250 | Genesis/Custom boundary |
| Situational Services | II | II | II | II | 0.375 | Custom Built |
| Shared Mode (ride-share, e-bike) | III | II | II | II | 0.44 | Custom/Product boundary |
| Distributed Public Mode (on-demand) | II | I | II | II | 0.31 | Custom Built |
| Private Mode (car ownership) | IV | IV | IV | III | 0.81 | Commodity |
| Car | IV | IV | IV | III | 0.81 | Commodity |
| Train | III | IV | III | III | 0.69 | Product (late) |
| Virtual Space (Zoom) | IV | IV | III | IV | 0.84 | Commodity — accelerated by pandemic |
| Connectivity (4G/5G) | IV | IV | IV | IV | 0.88 | Utility |
| Cybersecurity | II | II | III | III | 0.50 | Custom/Product boundary |
| Regulation | II | II | II | II | 0.375 | Custom Built (lagging) |
| City Planning | II | II | II | II | 0.375 | Custom Built (process-bound) |
| Public Infrastructure | III | III | III | III | 0.625 | Product (mature but slow to change) |
| Private Infrastructure | IV | III | III | III | 0.69 | Product (late) |
| Critical National Infrastructure | III | III | III | III | 0.625 | Product |
| Demand Shocks | I | I | I | I | 0.125 | Genesis — novel forcing events |
| Sustainability and Climate Policy | II | II | II | II | 0.375 | Custom Built |

In transition (rows disagree): **Shared Mode** and **Private Mode** — consumer behaviour is shifting the former rightward (ubiquity rising fast) while the latter is being partially displaced but remains commoditised.

## 4. Strategic Analysis

### a. Top 3 differentiation pressure D(v) = ν · (1 − ε)

1. **Mobility Hubs** — D = 0.70 × (1 − 0.30) = **0.49**. Visible intermediary, still in custom-build territory. High differentiation zone.
2. **Situational Services** — D = 0.72 × (1 − 0.35) = **0.47**. Real-time micro-guidance during the journey; still bespoke.
3. **Transport Integration** — D = 0.75 × (1 − 0.40) = **0.45**. The MaaS integration layer. Whoever captures this owns the user relationship.

### b. Top 3 commodity leverage K(v) = (1 − ν) · ε

1. **Connectivity** — K = (1 − 0.38) × 0.82 = **0.51**. Utility-grade 4G/5G; buy it, don't build it.
2. **Private Infrastructure** — K = (1 − 0.24) × 0.70 = **0.53**. Outsource / consortium plays.
3. **Critical National Infrastructure** — K = (1 − 0.12) × 0.60 = **0.53**. State-adjacent utility; lean on regulated providers.

### c. Top 3 dependency risks R(a, b) = ν(a) · (1 − ε(b))

1. **(Transport Integration, Connectivity)** at face value is low risk (Connectivity mature), but **(Transport Integration, City Planning)**: R = 0.75 × (1 − 0.35) = **0.49** — a user-visible layer depending on an immature, slow-moving planning process.
2. **(Ease of Use, Transport Integration)**: R = 0.90 × (1 − 0.40) = **0.54**. High-visibility need resting on a Custom-Built layer.
3. **(Access to Service, Mobility Hubs)**: R = 0.88 × (1 − 0.30) = **0.62**. Biggest dependency risk in the map — the public's access need depends on a nascent, under-funded hub concept.

### d. Suggested gameplays (Wardley's 61-play catalogue)

- **Open Approaches (#15)** on **Transport Integration** — open standards for ticketing / APIs to push it rightward into the Product band fast. Stops a proprietary aggregator locking the market.
- **Centre of Gravity / Ecosystem (#28)** on **Mobility Hubs** — operator consortium around physical interchange points, amplifying network effect.
- **Co-opt / Fighting with Sensible Allies (#22)** between **Government** and **Transport Operators** on **Distributed Public Mode** — on-demand rural / suburban transit as a public-private experiment.
- **Pig in a Poke (#41)** risk on **Private Infrastructure** — legacy car-park and petrol-station estates look valuable but are being stranded as Private Mode demand softens; plan for rotation into charging / hub use.
- **Sweat and Dump (#39)** on legacy **Private Mode** assets where operators hold sunk ICE-vehicle capital — extract value while redirecting investment.
- **Pre-emptive Strike (#34)** for the **Zoom / Virtual Space** displacement — operators need a differentiated journey experience (comfort, productivity, integration) that beats "just staying home."
- **Standards Game (#14)** on **Cybersecurity** for connected vehicles — government-driven minimum bar to prevent a race-to-the-bottom.

### e. Doctrine violations / observations

- **Phase II "Know your users"**: The scenario explicitly names three user types and the map carries three anchors — compliant, but the map should watch that *Transport Operators* don't become the de facto primary user (a common failure mode where the industry maps itself, not the public).
- **Phase II "Focus on user needs"**: Good — the top layer is needs (ease of use, cost, safety, awareness), not solutions.
- **Phase III "Use appropriate methods"**: Custom-Built components (Transport Integration, Mobility Hubs, Situational Services) should be built in-house / agile; Commodity components (Connectivity, Car) should be bought. The map flags this.
- **Phase IV "Think small (as in teams)"**: Connectivity + Cybersecurity layers sit at the edge — a single national team is a doctrine violation; distribute.
- **Phase V "Be pragmatic"**: Regulation and Public Infrastructure are flagged with inertia markers per the scenario brief (consumer behaviour is driving real evolution, regulation / infrastructure are lagging). The inertia forms implicated are primarily **sunk capital** (highway/rail estate), **political capital** (regulation), and **re-architecture cost** (CNI).

## 5. Where consumer behaviour drives evolution vs where regulation/infrastructure lag

**Driving evolution (consumer behaviour):**

- **Virtual Space (Zoom)** — moved from Custom-Built pre-2020 to Commodity in ~24 months; now a durable substitute for ~15–30% of business travel.
- **Shared Mode** — ride-share, e-scooter, e-bike share is rapidly increasing in ubiquity (Stage III).
- **Cost** sensitivity — post-fuel-spike, consumers are actively re-choosing mode in ways the system hadn't modelled.
- **Ease of Use** — one-tap multi-modal booking is now the expected norm.

**Lagging (regulation and infrastructure):**

- **Regulation** (ε ≈ 0.30) — still Custom-Built per jurisdiction. e-Scooter trials, autonomous, ride-hail all ahead of rules.
- **City Planning** (ε ≈ 0.35) — road hierarchy, kerb-space allocation, hub siting: decade-scale cycles versus month-scale behaviour change.
- **Public Infrastructure** (ε ≈ 0.55, marked inertia) — rail network, road network: sunk-capital inertia dominates.
- **Critical National Infrastructure** (ε ≈ 0.60) — moves glacially; rearchitecture cost is prohibitive.

The gap between the right-hand column (consumer behaviour at commodity / high product) and the regulation/infrastructure cluster (stuck in Custom-Built) is the strategic tension this map surfaces.

## 6. Notes on scope

- Evolution trajectories shown via `evolve` arrows are **scenarios**, not forecasts — Wardley's climatic pattern: evolution cannot be measured over time.
- The `Demand Shocks` component is placed high on visibility (a forcing input the public and operators cannot ignore) but low on evolution (Genesis-level novelty each time a shock arrives — pandemic, fuel crisis, extreme weather).
- Inertia markers follow the scenario brief; in Wardley's taxonomy these are primarily the *supplier* forms (sunk capital, re-architecture cost) for infrastructure and the *consumer* forms (past political capital, incumbent constituency) for regulation.
