# Supply-Chain Sustainability — Wardley Map

Scenario: Map supply-chain sustainability from producer to consumer, including actors (producer, retailer, consumer, regulator), the physical chain (sourcing → manufacturing → packaging → transport → distribution → end-of-life), the regulatory apparatus, and the compliance signals consumers see. Show where sustainability is open-market driven vs regulated, and where R&D and resource efficiency fit.

## 1. Mathematical model applied

$$\mathcal{M} = (V, E, U, \nu, \varepsilon, t)$$

- $|U| = 4$: **Consumer**, **Producer**, **Retailer**, **Regulator** — multi-anchor, because the scenario explicitly calls out four distinct actors with different needs.
- $|V| \approx 31$ components spanning physical chain, regulatory apparatus, compliance signals, and R&D/methodology layer.
- Visibility $\nu$ seeded from $\nu(v) = 1/(1 + d(v))$ and then adjusted (e.g., **Eco-Label** raised because consumers think about it directly even though it is technically a certification output; **Emissions Accounting Methodology** lowered because it is architecturally invisible to the shopper).
- Hard constraint checked: for every edge $(a, b) \in E$, $\nu(a) \ge \nu(b)$.

## 2. OWM map

See `draft.owm` in the same folder.

## 3. Stage-band rationale (Evolution $\varepsilon$)

Using the quick 4-row cheat sheet (Ubiquity, Certainty, User Perception, Publication Types), a representative selection:

| Component | Ubiquity | Certainty | UserPerception | Publication | Avg $\varepsilon$ | Band |
|---|---|---|---|---|---|---|
| Storefront Distribution | IV | IV | IV | III | 0.81 | Commodity (+utility) |
| Last-Mile Transportation | IV | III | III | IV | 0.75 | Commodity (+utility) |
| Packaging | III | IV | III | III | 0.72 | Product (+rental) |
| Eco-Label / Certification Mark | III | III | III | III | 0.625 | Product (+rental) |
| Manufacturing | III | III | III | III | 0.625 | Product (+rental) |
| Third-Party Audit | III | III | II | III | 0.56 | Product (+rental) |
| Sustainability Rating (Consumer-Facing) | III | II | II | II | 0.44 | Custom Built — **in transition** |
| Regulations | II | III | II | II | 0.41 | Custom Built |
| Continuous Monitoring | II | II | II | III | 0.44 | Custom Built |
| End-of-Life Reuse | II | II | II | II | 0.375 | Custom Built |
| Sustainability R&D | I | I | I | I | 0.125 | Genesis |
| Lifecycle Assessment Methodology | II | II | I | II | 0.31 | Custom Built |
| Emissions Accounting Methodology | II | II | II | II | 0.375 | Custom Built |

In-transition flags: **Sustainability Rating (Consumer-Facing)** (rows span II–III) — this is why an `evolve` arrow points it toward 0.80, under consumer-pull pressure. **Emissions Accounting Methodology** also flagged, evolving toward 0.70 as CSRD/ISSB-style regimes mature.

## 4. Open-market vs regulated split (scenario question)

| Zone | Components | Driver |
|---|---|---|
| **Open-market (consumer-pull)** | Sustainability Rating, Eco-Label, Storefront / Online / Coop Distribution, Packaging | Consumers and retailers compete on visible sustainability claims |
| **Regulated (policy-push)** | Laws, Regulations, Trade Agreements, Sanctions, Guidelines, Bureaucracy, Continuous Monitoring, Disclosure | State/multilateral apparatus sets the floor |
| **Hybrid (mandated-but-marketed)** | Certification Scheme, Third-Party Audit, Disclosure | Required for market access but used as brand differentiation |
| **R&D / resource-efficiency zone** | Sustainability R&D, Lifecycle Assessment, Emissions Accounting, Resource Efficiency Practice | Pre-commoditised; firms and academia differentiate here |

R&D and resource efficiency sit deep-left (low $\nu$, low $\varepsilon$) — they are the **differentiation engine** that feeds higher-visibility claims (ratings, labels) over time.

## 5. Strategic analysis

### (a) Top 3 differentiation pressure $D(v) = \nu(v) \cdot (1 - \varepsilon(v))$

| Rank | Component | $\nu$ | $\varepsilon$ | D | Why |
|---|---|---|---|---|---|
| 1 | Sustainability Rating (Consumer-Facing) | 0.86 | 0.55 | **0.387** | Visible to consumer but still immature/fragmented (several competing rating schemes). Whoever defines the dominant rating wins the narrative. |
| 2 | Coop / Community Distribution | 0.78 | 0.45 | **0.429** | High-visibility distribution channel that is still custom/bespoke — room for sustainability-native brands. |
| 3 | Sustainability Disclosure (ESG reports) | 0.62 | 0.50 | **0.310** | Visible to regulators and investors; content and format still in flux — differentiation possible via higher-quality disclosure. |

### (b) Top 3 commodity leverage $K(v) = (1 - \nu(v)) \cdot \varepsilon(v)$

| Rank | Component | $\nu$ | $\varepsilon$ | K | Why |
|---|---|---|---|---|---|
| 1 | Storefront Distribution | 0.82 | 0.80 | 0.144 | (not top K because visible) |
| 1 | Last-Mile Transportation | 0.52 | 0.75 | **0.36** | Widely available 3PL / parcel utilities — default outsource. |
| 2 | Backhaul Transportation | 0.44 | 0.70 | **0.392** | Highly commoditised freight; optimise for load factor, not ownership. |
| 3 | Waste Handling | 0.30 | 0.55 | **0.385** | Deep in chain, mature municipal / industrial services — outsource, but watch for regulated reclassification. |

### (c) Top 3 dependency risks $R(a, b) = \nu(a) \cdot (1 - \varepsilon(b))$

| Edge | $\nu(a)$ | $\varepsilon(b)$ | R | Why |
|---|---|---|---|---|
| Sustainability Rating → Sustainability Disclosure | 0.86 | 0.50 | **0.430** | Consumer-facing rating is only as credible as the underlying (immature) disclosure regime. Reputational risk if disclosure is challenged. |
| Eco-Label → Certification Scheme | 0.84 | 0.60 | **0.336** | Labels the consumer sees depend on certification schemes that vary widely in rigour. |
| Continuous Monitoring → Emissions Accounting Methodology | 0.58 | 0.45 | **0.319** | Monitoring that feeds disclosure sits on top of still-contested accounting rules (Scope 3, land-use, etc.). |

### (d) Suggested gameplays (from the 61-play catalogue)

- **Open Approaches (#15 / Open Source)** on **Emissions Accounting Methodology** and **Lifecycle Assessment Methodology** — commoditise the measurement layer so that disclosure becomes comparable. Blocks incumbents from using methodological opacity as a moat.
- **Industrial Policy / Exploiting Constraint** on **Regulations** and **Certification Scheme** — lobby for single, high-rigour schemes to displace weaker private labels (converts a fragmented market into a regulated one, favouring producers with already-strong practice).
- **Sensing (pre-commoditisation scanning) / Weak Signal Detection** on **End-of-Life Reuse** — extended-producer-responsibility and right-to-repair rules are at the chasm; early movers on reuse infrastructure gain regulatory goodwill and consumer trust.
- **Experimentation / Pioneer-Settler-Town Planner** on **Sustainability R&D** — keep R&D pioneering but industrialise **Resource Efficiency Practice** via settlers; hand commoditised emissions accounting to town planners.
- **Differentiation on Non-Price (Signalling)** for **Sustainability Rating** — own the rating channel (e.g., first-party rating backed by audited disclosure) before a dominant third-party rating emerges.
- **Harvesting** on **Last-Mile / Backhaul Transportation** — route via specialised low-carbon logistics vendors once commoditised enough; don't build in-house.
- **Fear-Uncertainty-Doubt** is a common *defensive* play on sustainability claims — **don't play it** (it violates the Open Approaches stance above and invites regulatory backlash). Noted to avoid.

### (e) Doctrine violations / cautions

- **"Know your users" (Phase II)** — the map has four anchors; watch that Producer and Regulator needs are not subordinated to Consumer optics (greenwashing risk).
- **"Use a common language"** — at risk when Emissions Accounting and Lifecycle Assessment methodologies remain fragmented. Doctrine says standardise.
- **"Be transparent"** — natural fit with real (audited) disclosure; violated by private-label-only certification.
- **"Optimise flow"** — end-of-life → manufacturing loop is under-built in most real chains; the circular edge (Waste Handling → Manufacturing) in this map is aspirational.
- **"Focus on high-value"** — differentiation should be on Rating, Disclosure, and R&D, not on re-building commodity logistics.
- **"Think big, but act iteratively"** — consumer-facing rating is the visible differentiator but must be earned by iterative improvement in the invisible methodology layer.

## 6. Inertia

Two inertia markers included:

- **Legacy Packaging Lines** (form: *sunk physical capital*) — blocks fast substitution toward compostable / refill packaging.
- **Established Audit Firms** (form: *political / relationship capital*) — incumbent audit firms resist methodology change that would expose the gap between form and substance in ESG assurance.

Both are from the 14 consumer-side inertia forms (as opposed to supplier-side).

## 7. Dynamics — illustrative scenario only

Using the logistic form $d\varepsilon/dt = r \cdot \varepsilon(1 - \varepsilon)$ with $r \approx 0.15$/yr for **Sustainability Rating (Consumer-Facing)** at $\varepsilon_0 = 0.55$: $\varepsilon$ approaches 0.80 on a 3–5 year horizon *if* methodology commoditises and one rating consolidates. **This is a scenario, not a forecast** — Wardley's climatic pattern is that evolution cannot be measured over time.

## 8. Summary

- The map separates the **physical chain** (producer → retailer → consumer) from the **regulatory apparatus** (regulator) and the **compliance signalling layer** (labels, ratings, disclosure, audit) that glues the two together.
- **Open-market zone** lives in the upper-right (distribution, packaging, last-mile, ratings); **regulated zone** sits mid-upper-left (laws, regs, trade agreements, sanctions, guidelines); **R&D / efficiency differentiation zone** is deep-left (LCA, emissions accounting, R&D).
- Top strategic move: **commoditise the measurement layer (LCA, emissions accounting) via open approaches**, then **differentiate at the visible rating / disclosure layer**. Avoid over-investing in commodity logistics; treat waste handling and last-mile as utilities.
