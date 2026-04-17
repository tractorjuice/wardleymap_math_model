# Wardley Map — Freelance Marketplace

Scenario: A two-sided marketplace where clients post jobs, freelancers bid, and the platform takes a commission. The strategic question is where the platform should invest vs outsource.

Market frame for evolution scoring: **global digital labour / professional-services marketplaces** (Upwork, Fiverr, Toptal, Freelancer.com are the reference set). This matters because ubiquity is market-relative (see `cheat-sheet.md`, caveat 1).

---

## 1. OWM output

```owm
title Freelance Marketplace
style wardley

// --- Anchors (two user types) ---
anchor Client gets work done           [0.96, 0.78]
anchor Freelancer wins paid work       [0.96, 0.70]

// --- User-facing activities (visible value chain) ---
component Job posting & intake         [0.86, 0.80]
component Search & matching            [0.82, 0.62]
component Bidding & proposals          [0.82, 0.58]
component Messaging / chat             [0.78, 0.80]
component Contract & SOW               [0.74, 0.55]
component Escrow & milestone payments  [0.74, 0.72]
component Reviews & reputation         [0.70, 0.55]
component Dispute resolution           [0.66, 0.45]
component Identity verification (KYC)  [0.62, 0.82]

// --- Practices ---
component Commission / take-rate model [0.60, 0.45] inertia
component Trust & safety policy        [0.58, 0.50]
component Pricing guidance             [0.56, 0.40]

// --- Data ---
component Freelancer profile data      [0.54, 0.55]
component Job / project history        [0.50, 0.60]
component Skill taxonomy               [0.48, 0.45]
component Reputation graph             [0.46, 0.35]
component Bid / price signal data      [0.44, 0.30]

// --- Knowledge / models ---
component Matching / ranking model     [0.40, 0.40]
component Fraud & abuse detection      [0.38, 0.55]
component Pricing intelligence         [0.34, 0.25]
component LLM-assisted job scoping     [0.32, 0.20]

// --- Supporting / infrastructure ---
component Payment rails                [0.30, 0.90]
component KYC / AML service            [0.28, 0.88]
component Notification / email / SMS   [0.26, 0.92]
component Cloud compute & storage      [0.18, 0.93]
component CDN                          [0.16, 0.95]
component Authentication / identity    [0.22, 0.88]

// --- Dependencies (a -> b means a depends on b) ---
Client gets work done->Job posting & intake
Client gets work done->Search & matching
Client gets work done->Messaging / chat
Client gets work done->Contract & SOW
Client gets work done->Escrow & milestone payments
Client gets work done->Reviews & reputation
Client gets work done->Dispute resolution

Freelancer wins paid work->Search & matching
Freelancer wins paid work->Bidding & proposals
Freelancer wins paid work->Messaging / chat
Freelancer wins paid work->Escrow & milestone payments
Freelancer wins paid work->Reviews & reputation
Freelancer wins paid work->Identity verification (KYC)

Job posting & intake->LLM-assisted job scoping
Job posting & intake->Skill taxonomy
Job posting & intake->Cloud compute & storage

Search & matching->Matching / ranking model
Search & matching->Freelancer profile data
Search & matching->Skill taxonomy
Search & matching->Reputation graph
Search & matching->Cloud compute & storage

Bidding & proposals->Bid / price signal data
Bidding & proposals->Pricing guidance
Bidding & proposals->Cloud compute & storage

Messaging / chat->Notification / email / SMS
Messaging / chat->Cloud compute & storage
Messaging / chat->Fraud & abuse detection

Contract & SOW->Trust & safety policy
Contract & SOW->Commission / take-rate model

Escrow & milestone payments->Payment rails
Escrow & milestone payments->KYC / AML service
Escrow & milestone payments->Commission / take-rate model
Escrow & milestone payments->Fraud & abuse detection

Reviews & reputation->Reputation graph
Reviews & reputation->Job / project history

Dispute resolution->Trust & safety policy
Dispute resolution->Job / project history
Dispute resolution->Reputation graph

Identity verification (KYC)->KYC / AML service
Identity verification (KYC)->Authentication / identity

Matching / ranking model->Freelancer profile data
Matching / ranking model->Job / project history
Matching / ranking model->Bid / price signal data
Matching / ranking model->Cloud compute & storage

Fraud & abuse detection->Job / project history
Fraud & abuse detection->Reputation graph
Fraud & abuse detection->Cloud compute & storage

Pricing intelligence->Bid / price signal data
Pricing intelligence->Job / project history

Pricing guidance->Pricing intelligence

LLM-assisted job scoping->Cloud compute & storage

Freelancer profile data->Cloud compute & storage
Job / project history->Cloud compute & storage
Reputation graph->Cloud compute & storage
Bid / price signal data->Cloud compute & storage
Skill taxonomy->Cloud compute & storage

// --- Evolution arrows (scenario, not forecast) ---
evolve Matching / ranking model       0.70
evolve LLM-assisted job scoping       0.55
evolve Reputation graph               0.55
evolve Identity verification (KYC)    0.92
evolve Dispute resolution             0.60

// --- Pipeline: matching spans from custom built to product ---
pipeline Matching / ranking model     [0.30, 0.70]

// --- Notes ---
note Two-sided network: retention depends on both anchors                       [0.92, 0.50]
note Commission model carries inertia from incumbents' 10-20% norm              [0.60, 0.35]
note Reputation graph is the most defensible proprietary asset                  [0.48, 0.28]
```

---

## 2. How the coordinates were derived

### Visibility ν (graph seed then judgment override)

Shortest-path distances from the two anchors gave the seed `ν(v) = 1/(1 + d(v))`:

- d=0: anchors → ν=1.0, placed at 0.96 for drawing
- d=1: intake, matching, bidding, messaging, escrow, reviews, disputes, KYC → ν in 0.6–0.9 band
- d=2: commission model, trust & safety, skill taxonomy, reputation graph → ν in 0.4–0.6 band
- d=3+: matching model, fraud detection, pricing intelligence → ν in 0.3–0.45 band
- d=4+: cloud, CDN, payment rails, KYC service, auth → ν below 0.3

Judgment overrides applied:
- **Commission / take-rate model** raised above graph distance — clients and freelancers *think about* the cut even though it is mechanically a back-office policy.
- **Reputation graph** kept low in ν (architectural asset) even though reviews are user-visible; users see the *output*, not the *graph*.
- **Payment rails / KYC service** pushed to the very bottom (ν ≈ 0.28–0.30) — they are commodity utilities invisible to the user.

All directed edges `(a, b)` satisfy the hard rule `ν(a) ≥ ν(b)`.

### Evolution ε — scoring table (4-row quick method per `SKILL.md` §4)

Each component scored on rows 5 (Ubiquity), 6 (Certainty), 11 (User Perception), 7 (Publication Types). Stage → midpoint: I=0.125, II=0.375, III=0.625, IV=0.875. Mean ε listed.

| Component | Ubiquity | Certainty | User Perception | Publications | Mean ε | Band |
|---|---|---|---|---|---|---|
| Job posting & intake | IV | IV | IV | III | 0.80 | Commodity |
| Search & matching | III | III | III | III | 0.625 | Product |
| Bidding & proposals | III | III | III | II | 0.56 | Product |
| Messaging / chat | IV | IV | IV | IV | 0.875 | Commodity |
| Contract & SOW | III | III | II | III | 0.56 | Product |
| Escrow & milestone | III | IV | III | III | 0.69 | Product |
| Reviews & reputation | III | III | III | II | 0.56 | Product |
| Dispute resolution | II | II | III | III | 0.44 | Custom Built |
| Identity verification | IV | IV | III | IV | 0.81 | Commodity |
| Commission / take-rate | III | II | III | II | 0.50 | Custom/Product boundary |
| Trust & safety policy | II | II | III | III | 0.44 | Custom Built |
| Pricing guidance | II | II | II | II | 0.375 | Custom Built |
| Freelancer profile data | III | III | III | II | 0.56 | Product |
| Job / project history | III | III | III | III | 0.625 | Product |
| Skill taxonomy | II | II | III | II | 0.44 | Custom Built |
| Reputation graph | II | II | II | II | 0.375 | Custom Built |
| Bid / price signal data | I | II | I | II | 0.25 | Genesis/Custom boundary |
| Matching / ranking model | II | II | II | II | 0.375 | Custom Built — **in transition** (range II–III) |
| Fraud & abuse detection | III | II | II | III | 0.50 | Custom/Product boundary |
| Pricing intelligence | I | II | I | II | 0.25 | Genesis/Custom boundary |
| LLM-assisted job scoping | I | I | I | II | 0.19 | Genesis |
| Payment rails | IV | IV | IV | IV | 0.875 | Commodity (utility) |
| KYC / AML service | IV | IV | III | IV | 0.81 | Commodity (utility) |
| Notification / email / SMS | IV | IV | IV | IV | 0.875 | Commodity (utility) |
| Cloud compute & storage | IV | IV | IV | IV | 0.875 | Commodity (utility) |
| CDN | IV | IV | IV | IV | 0.875 | Commodity (utility) |
| Authentication / identity | IV | IV | III | IV | 0.81 | Commodity (utility) |

**In-transition flags** (rows disagree, track as error bar):

- *Matching / ranking model*: emerging LLM-era re-architecture. Public benchmark models (Stage II practice) but productised embeddings + ranking stacks (Stage III infrastructure). Range 0.30–0.70 — shown as a `pipeline`.
- *LLM-assisted job scoping*: genesis (Stage I ubiquity) but built on already-commodity LLM APIs — conceptually hybrid. Watch row 5 (ubiquity) rapidly climbing over 2024–2026.
- *Reputation graph*: graph-form reputation is still Stage II (divergent data, no standard). Star-rating UI is Stage IV. Tracked as the underlying data structure, not the UI.

---

## 3. Strategic analysis

### (a) Top 3 by differentiation pressure D(v) = ν(v) · (1 − ε(v))

| Rank | Component | ν | ε | D | Reasoning |
|---|---|---|---|---|---|
| 1 | **Bidding & proposals** | 0.82 | 0.58 | **0.34** | Visible to both sides, still Stage III — proposal UX, AI-assisted proposals, and match-to-propose flow are differentiators. Incumbents' experience here is crude. |
| 2 | **Search & matching (user-facing)** | 0.82 | 0.62 | **0.31** | Visible, and the matching model underneath is in transition (pipeline 0.30→0.70). Whoever industrialises quality matching first captures share. |
| 3 | **Contract & SOW** | 0.74 | 0.55 | **0.33** | Clients feel contract friction acutely; Stage III product-with-AI-drafting is an open lane. LLM-assisted contracts are barely rolled out across the category. |

### (b) Top 3 by commodity leverage K(v) = (1 − ν(v)) · ε(v)

| Rank | Component | ν | ε | K | Reasoning |
|---|---|---|---|---|---|
| 1 | **Cloud compute & storage** | 0.18 | 0.875 | **0.72** | Deep in the stack, full utility. Outsource to AWS/GCP/Azure — do not run your own. |
| 2 | **CDN** | 0.16 | 0.95 | **0.80** | Pure utility. Cloudflare / Fastly / CloudFront. |
| 3 | **Payment rails** | 0.30 | 0.90 | **0.63** | Stripe Connect / Adyen / Airwallex. Building a PSP is a classic Stage IV trap. |

Runners-up worth outsourcing: **KYC / AML service** (K=0.63) via Onfido / Persona / Jumio; **Notification / email / SMS** (K=0.68) via Twilio / SendGrid; **Authentication / identity** (K=0.69) via Auth0 / Clerk / Cognito.

### (c) Top 3 dependency risks R(a, b) = ν(a) · (1 − ε(b))

| Rank | Edge (a → b) | ν(a) | ε(b) | R | Why |
|---|---|---|---|---|---|
| 1 | Search & matching → **Matching / ranking model** | 0.82 | 0.40 | **0.49** | A highly-visible activity depends on an in-transition custom-built component. Model drift or a better entrant cripples the whole map. |
| 2 | Bidding & proposals → **Bid / price signal data** | 0.82 | 0.30 | **0.57** | Core bidding UX depends on Stage I/II data. If a competitor aggregates better price signals (e.g., via harvesting), this collapses. |
| 3 | Contract & SOW → **Commission / take-rate model** | 0.74 | 0.45 | **0.41** | Revenue mechanism is Stage II/III with inertia. A rival's lower-fee model is a direct attack vector (Fiverr vs Upwork fee structures). |

Other elevated risks: Dispute resolution → Trust & safety policy (R=0.36); Reviews & reputation → Reputation graph (R=0.45).

### (d) Suggested gameplays (from the 61-play catalogue in `gameplays.md`)

Invest (custody) side — where to build and keep in-house:

- **#43 Sensing Engines (ILC)** — on the *Matching / ranking model* and *Reputation graph*. The platform sits on consumption data from both sides; use it to detect which novel matching features graduate from Genesis to Product. This is the canonical two-sided-marketplace play.
- **#45 Two factor** — on the *anchors*. This is literally a two-factor market; doctrine #1 (focus on user needs) means the platform must serve both simultaneously. Under-serving either side collapses liquidity.
- **#16 Exploiting Network Effects** — on the *Reputation graph* and *Freelancer profile data*. Reputation compounds per user; make it the stickiest asset.
- **#26 Differentiation** — on *Bidding & proposals*, *Search & matching*, and *Contract & SOW* (the top-D components).
- **#44 Tower and Moat** — on the *Reputation graph* specifically. Dominate the data asset, let the utilities around it (payments, KYC, cloud) be commodities you rent.
- **#36 Directed investment** — on *LLM-assisted job scoping* and *Pricing intelligence* (both Genesis). Treat as VC-style bets.
- **#56 First mover** / **#55 Land grab** — on *LLM-assisted job scoping*. The space is pre-competitive; moving first on AI-native scoping creates a durable capability.

Outsource (rent from utility) side — gameplays for the commodity tail:

- **#24 Sweat & Dump** and **#23 Disposal of liability** — for *Payment rails*, *CDN*, *Cloud compute*, *KYC / AML*, *Notification*. If any of these are currently built in-house, push them out to utility providers.
- **#30 Standards game** — on *Skill taxonomy*. Drive the market to your taxonomy (cf. LinkedIn Skills). Turns a Custom-Built data asset into a moat.
- **#17 Co-operation** and **#15 Open Approaches** — open-source the *Matching / ranking model*'s feature-extraction layer or the *Skill taxonomy* to accelerate commoditisation downwards and free engineering to focus on the proprietary reputation graph. Classic Wardley "commoditise below to differentiate above."
- **#29 Harvesting** — monitor niche AI-matching startups and acquire winners once ILC signals confirm.

Attacker-side awareness:

- **#49 Fragmentation** and **#27 Pricing policy** — rivals will attack the *Commission / take-rate model*. Defend by re-segmenting (per-vertical fees, outcome-based fees) rather than a blanket cut.
- **#33 There is no one culture** (doctrine) drives **#4 Structure & Culture (PST)** — Pioneers on *LLM-assisted job scoping*, Settlers on *Matching / ranking model*, Town Planners on *Payments / KYC / Cloud*.

### (e) Doctrine violations / risks (against the 40 principles in `doctrine.md`)

The map itself does not violate doctrine, but three pressure points deserve flags:

- **#1 Focus on user needs / #10 Know your users** — two anchors are declared, which is correct for a two-sided marketplace. A common failure mode is collapsing to one anchor (usually the paying client). Guard against it in the roadmap.
- **#13 Manage inertia** — the *Commission / take-rate model* carries at least three of the 17 inertia forms (see `inertia.md`): #15 *past-success data / cannibalisation fear*, #16 *rewards and culture* (sales comp tied to GMV × take-rate), #17 *financial-market expectations* (investors modelling take-rate). Any pivot to outcome- or subscription-based pricing will hit these.
- **#22 Use standards where appropriate** — *Skill taxonomy* is currently Custom Built. Adopting an external standard (ESCO, O*NET, or LinkedIn's) is a doctrine call; building a proprietary taxonomy is defensible only if paired with **#30 Standards game**.
- **#38 There is no core** (Phase IV) — if the platform claims "matching is our core", it is already frozen. Today's core (matching) is tomorrow's commodity. The map reflects this: the matching model is a pipeline, not a point.
- Under-specified **Knowledge layer** — the map includes knowledge components (matching model, fraud detection, pricing intelligence, LLM scoping) but deeper knowledge such as *labour-market dynamics* and *category-specific expertise* are implicit. In a v2 of this map, promote them to τ=K nodes.

### (f) Caveat

The evolution positions and the `evolve` arrows above are a **scenario, not a forecast**. Per Wardley's climatic pattern, *"you cannot measure evolution over time or adoption"* — the X-axis is a judgment about *characteristics* (ubiquity, certainty, user perception, publication types), not a timeline. The derived metrics D, K, R are heuristics proposed by this skill's math model and are attention prompts, not scores. Re-run the map annually, with the 19-row cheat sheet rather than the 4-row quick method, when making irreversible outsourcing decisions.

---

## 4. Bottom-line answer to the strategic question

**Invest in (build / keep in-house):**

1. **Reputation graph** and **Freelancer profile data** — the only components where network effects + D and K both argue for ownership. This is the Tower (#44).
2. **Matching / ranking model** — pipeline Stage II→III. Industrialise it yourself via **ILC (#43)**; this is where data advantages compound.
3. **Bidding & proposals** and **Contract & SOW** UX — top-D components; where user-visible differentiation is still unclaimed.
4. **LLM-assisted job scoping** and **Pricing intelligence** — Genesis bets via **Directed investment (#36)**. Small teams, FIRE doctrine (#15).
5. **Commission / take-rate model** and **Trust & safety policy** — defensive ownership; these define the business model.

**Outsource to utilities (rent, do not build):**

1. **Cloud compute & storage, CDN** — hyperscalers.
2. **Payment rails** — Stripe Connect / Adyen (escrow as a service where available).
3. **KYC / AML** — Onfido / Persona / Jumio.
4. **Authentication / identity** — Auth0 / Clerk.
5. **Notification (email / SMS / push)** — Twilio / SendGrid / OneSignal.

**Open-source or standardise (commoditise below to differentiate above):**

- *Skill taxonomy* — adopt ESCO/O*NET or open-source your own and run **#30 Standards game**.
- *Feature-extraction pipeline* for matching — open-source the boring layer, keep the ranking-on-reputation layer proprietary.

The strategic shape is Wardley's canonical *"commoditise the stack below, differentiate the experience above, own the data in between."* For a freelance marketplace, the data-in-between is the **reputation graph** — that is the one asset worth fighting for.
