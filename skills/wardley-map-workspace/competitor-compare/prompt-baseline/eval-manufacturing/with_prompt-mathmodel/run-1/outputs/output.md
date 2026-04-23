# Manufacturing Supply Chain — Wardley Map (February 2023)

## Scenario

Mapping a manufacturer's end-to-end supply chain: raw and refined materials through equipment, labour and R&D into a finished product reaching distributors, with the government/regulation side (compliance, certification, lobbying, safety), the financial lens (ROCE, cost, capital, sales forecasting), inventory/logistics decisions (JIT vs JIC, warehousing), and an awareness/visibility layer that tells the operator whether the chain is resilient. Timeframe: February 2023 — post-COVID disruption, mid-Ukraine-war energy shock, JIT orthodoxy under active re-evaluation.

## 1. Mathematical Model Applied

$\mathcal{M} = (V, E, U, \nu, \varepsilon, t)$ with three anchors ($|U|=3$) — **Distributor**, **Regulator**, **Investor / Board**. This is a multi-sided map: a manufacturer simultaneously satisfies commercial, regulatory and financial needs, and the same internal components rank differently against each.

Component-type annotation (τ) is used lightly: **Materials Science** and **Process Engineering** are labelled Knowledge (K); **Inventory Policy** and **Second-Source Strategy** are Practices (P); the rest are Activities (A) or Data (D) by default.

## 2. Components V and Anchors U

| Layer | Components |
|---|---|
| Anchors (U) | Distributor, Regulator, Investor / Board |
| User-facing | Finished Product, Compliance Certification, ROCE Reporting, Sales Forecast |
| Awareness | Supply Chain Visibility, Resilience Dashboard, Risk Register, Demand Signal |
| Manufacturing | Product Assembly, Quality Assurance, Packaging, Safety Testing |
| Supply-chain practices | Inventory Policy (JIT vs JIC), Warehousing, Logistics & Freight, Supplier Selection, Second-Source Strategy |
| Inputs / enablers | Equipment, Skilled Labour, R&D, Capital / Financing, Cost Accounting |
| Regulatory | Safety Standards Mgmt, Lobbying, Audit Trail |
| Raw inputs | Refined Materials, Raw Materials, Energy |
| Deep / knowledge | ERP / MRP, Materials Science (K), Process Engineering (K) |

## 3. Dependencies E

See the OWM file. Highlights:

- The three anchors fan out to three distinct user-facing components (Finished Product / Compliance Cert / ROCE Reporting) which then share the middle layers.
- The awareness layer is deliberately placed *below* Sales Forecast and *above* Supplier Selection — it's a cross-cutting sense-making layer that consumes Demand Signal and feeds decision-making.
- Raw Materials and Energy sit at the bottom as the deepest commodity dependencies; all physical production flows through them.

## 4. Visibility (Y-axis) — judgment notes

Seed values came from $\nu(v) = 1/(1 + d(v))$ from the nearest anchor, then adjusted:

- **Raised** for Supply Chain Visibility and Resilience Dashboard — technically mid-graph, but after 2021–22 the board *thinks about them directly*, so they sit close to user-facing.
- **Lowered** for ERP / MRP — structurally close to finance/audit but architecturally invisible to the user, placed at ν≈0.22.
- **Lowered** for Materials Science and Process Engineering — these are deep knowledge, treated as foundational (ν≈0.08, 0.14).

Hard constraint $\nu(a) \ge \nu(b)$ for every edge is satisfied (checked by hand on each declared dependency).

## 5. Evolution (X-axis) — cheat-sheet scoring

Quick 4-row method (Ubiquity, Certainty, User Perception, Publication). Representative scorings:

| Component | Ubiquity | Certainty | UserPerc | Pub | Avg ε | Stage |
|---|---|---|---|---|---|---|
| Raw Materials | IV (0.875) | IV (0.875) | IV (0.875) | IV (0.875) | 0.88 | Commodity |
| Energy | IV (0.875) | IV (0.875) | IV (0.875) | IV (0.875) | 0.88 | Commodity |
| Refined Materials | IV | IV | III | IV | 0.81 | Commodity |
| Logistics & Freight | IV | IV | IV | III | 0.81 | Commodity |
| Cost Accounting | IV | IV | IV | III | 0.81 | Commodity |
| Capital / Financing | IV | IV | IV | III | 0.81 | Commodity |
| ERP / MRP | IV | III | III | III | 0.69 | Product |
| Packaging | IV | IV | III | III | 0.75 | Commodity |
| Warehousing | III | IV | III | III | 0.69 | Product |
| ROCE Reporting | IV | IV | III | III | 0.75 | Commodity |
| Finished Product | III | III | III | IV | 0.69 | Product |
| Audit Trail | III | III | III | III | 0.63 | Product |
| Quality Assurance | III | III | III | III | 0.63 | Product |
| Equipment | III | III | III | III | 0.63 | Product |
| Compliance Certification | III | III | III | II | 0.56 | Product |
| Product Assembly | III | III | II | III | 0.56 | Product |
| Safety Standards | III | II | II | III | 0.50 | Product/CB edge |
| Safety Testing | II | III | II | III | 0.50 | transition |
| Sales Forecast | II | II | II | III | 0.44 | Custom Built |
| Demand Signal | II | II | II | III | 0.44 | Custom Built |
| Skilled Labour | III | II | II | II | 0.44 | Custom Built |
| Supplier Selection | II | II | II | II | 0.38 | Custom Built |
| Lobbying | II | II | II | II | 0.38 | Custom Built |
| Inventory Policy (JIT vs JIC) | II | II | I | II | 0.31 | Custom Built |
| R&D | II | II | II | I | 0.31 | Custom Built |
| Supply Chain Visibility | II | I | I | II | 0.25 | CB/Genesis |
| Second-Source Strategy | I | I | II | II | 0.25 | Genesis/CB edge |
| Risk Register | II | II | III | III | 0.56 | Product (mature) |
| Resilience Dashboard | I | I | I | II | 0.19 | Genesis |
| Process Engineering (K) | II | III | II | III | 0.50 | transition |
| Materials Science (K) | II | III | II | I | 0.38 | CB |

**In-transition flags:** Safety Testing, Process Engineering, Inventory Policy, Supply Chain Visibility — rows disagree by one stage. Notably, **Inventory Policy** is scored Genesis on User Perception (JIT was "common/expected" pre-2020; post-2020 the revalidation of JIC is a *surprise* again) but Custom Built on Ubiquity. This is real in-transition territory and justified the `inertia` marker.

## 6. OWM Map

See `draft.owm`.

## 7. Derived Heuristics

Computed $D = \nu(1-\varepsilon)$, $K = (1-\nu)\varepsilon$, $R = \nu(a)(1-\varepsilon(b))$ across all components / edges.

### Top 3 by D (differentiation pressure)

| Rank | Component | ν | ε | D | Reasoning |
|---|---|---|---|---|---|
| 1 | **Supply Chain Visibility** | 0.76 | 0.28 | **0.547** | Board-visible, still bespoke — post-COVID this is *the* scarce capability. |
| 2 | **Risk Register** | 0.72 | 0.55 | 0.324 | Visible to the C-suite, partly tooled but mostly spreadsheet-and-judgment. |
| 3 | **Demand Signal** | 0.70 | 0.50 | 0.350 | Sales/ops interface; predictive models exist but calibration is bespoke. |

*(Note: Resilience Dashboard has D = 0.74 × 0.78 = 0.58 numerically, beating #1 — it is the highest true D score but is essentially a view onto Supply Chain Visibility, so it's reported as joint #1 rather than separately. Listing both would double-count the same differentiation source.)*

### Top 3 by K (commodity leverage)

| Rank | Component | ν | ε | K | Reasoning |
|---|---|---|---|---|---|
| 1 | **Energy** | 0.10 | 0.90 | **0.810** | Textbook utility. Any manufacturer-specific handling of it is overhead. |
| 2 | **Raw Materials** | 0.12 | 0.88 | 0.774 | Commodity markets; only handling / hedging is manufacturer-specific. |
| 3 | **Refined Materials** | 0.18 | 0.82 | 0.672 | Commodity-ish; supplier concentration risk is the caveat (see R below). |

All three are buy, never build.

### Top 3 Dependency Risks R(a,b)

| Rank | Edge (a → b) | ν(a) | ε(b) | R | Why it's risky |
|---|---|---|---|---|---|
| 1 | **Product Assembly → R&D** | 0.64 | 0.28 | 0.461 | Production depends on an immature R&D function — any shock (staffing, IP) flows straight into the finished product. |
| 2 | **Resilience Dashboard → Second-Source Strategy** | 0.74 | 0.25 | 0.555 | Board-visible resilience dashboard is reading from a genesis-stage practice — the data is only as good as an underdeveloped second-sourcing discipline. |
| 3 | **Supply Chain Visibility → Demand Signal** | 0.76 | 0.50 | 0.380 | Entire visibility layer depends on a half-mature forecasting signal. |

(Ranking by raw $R$: #2 > #1 > #3. All three share a single root cause — the awareness layer is reading from immature upstream practices.)

## 8. Suggested Gameplays (Wardley's 61-play catalogue)

| Play | Target | Rationale |
|---|---|---|
| **Open approaches** (ecosystem) | Supply Chain Visibility, Resilience Dashboard | Push the visibility/resilience stack toward a shared industry standard — nobody wins by making this proprietary. |
| **Harvesting** | Demand Signal / Sales Forecast | Industry ML vendors (forecasting SaaS) are maturing; buy don't build. |
| **Directed investment / Differentiation** | Second-Source Strategy, R&D | These are the scarce-advantage components; fund them deliberately. |
| **Last-man-standing / Sweat-and-dump** | Legacy JIT warehousing contracts | For the JIT-only footprint being replaced, squeeze value out before sunsetting. |
| **Lobbying / Standards manipulation** | Safety Standards Mgmt, Compliance Certification | Already on the map as an explicit component — accept that it *is* a play, not overhead. |
| **Two-factor markets** | Distributor + Regulator | Treat regulator as a user, not a cost centre; shape compliance UX. |
| **Pig-in-a-poke** (avoid) | Supplier Selection | Don't dump second-source risk on the next-in-line supplier without visibility. |

## 9. Doctrine Observations

- **Phase II "Know your users"** — three anchors declared explicitly. Good: avoids the classic manufacturer doctrine violation of treating the regulator as a cost centre rather than a user.
- **Phase II "Focus on high situational awareness"** — the fact that the awareness layer (Supply Chain Visibility, Resilience Dashboard, Risk Register) is *itself* at Custom-Built / Genesis is itself a doctrine flag. A manufacturer without an industrialised visibility capability is flying on instinct.
- **Phase IV "Think small / think FIRE"** — Second-Source Strategy at ε ≈ 0.25 is a prime small-bet candidate; don't mega-project it.
- **Phase III "Use appropriate methods"** — Inventory Policy carries an inertia marker. The 17-forms reading: **sunk capital** (existing warehouses), **political capital** (procurement director's decade-long JIT gospel), and **second-sourcing risk** (the risk of the change itself). JIT isn't "wrong"; it's under-contested because the reversal carries its own switching cost.
- **Potential violation — "Use standards where appropriate"**: ERP/MRP is at ε ≈ 0.75 (Product) rather than Commodity; many manufacturers keep it heavily customised. Re-evaluate whether the customisation is genuinely strategic or legacy cruft.

## 10. Evolution Scenario (labelled as scenario, not forecast)

Using $d\varepsilon/dt = r\varepsilon(1-\varepsilon)$ with a notional $r=0.2/\text{yr}$, over a 3-year horizon (to ~2026):

- **Supply Chain Visibility**: 0.28 → ~0.45 (still Custom Built but pushing the boundary of Product). This is consistent with the post-COVID vendor land-grab.
- **Second-Source Strategy**: 0.25 → ~0.40. Genesis to Custom Built.
- **Inventory Policy**: 0.32 → ~0.50. The JIT/JIC rebalance becomes codified practice.
- **R&D**: 0.28 → ~0.40.

These are not predictions. They are illustrations of what a 3-year logistic step would imply, conditional on no disruption, with the explicit climatic-pattern caveat that evolution is not measurable over time.

## 11. Answer to the scenario's direct question

> "I want to understand where the supply chain itself sits on the evolution axis and what's industrialised versus still a bespoke judgment call."

**The physical supply chain** — raw materials, energy, freight, warehousing, cost accounting, ERP, capital — sits firmly in **Product / Commodity** territory (ε > 0.65). These are industrialised and should be bought or outsourced.

**The awareness and decision-making layer** — visibility, resilience, risk register, second-source strategy, inventory policy, R&D — sits in **Custom Built / Genesis** (ε < 0.40). These are bespoke judgment calls and the legitimate home of competitive advantage for a 2023 manufacturer.

The mismatch between a fully-industrialised *execution* stack and a largely-bespoke *sense-making* stack is the single most important feature of the map, and it's why pandemic-era disruption hurt manufacturers far more than their ERP systems suggested it should have.
</content>
