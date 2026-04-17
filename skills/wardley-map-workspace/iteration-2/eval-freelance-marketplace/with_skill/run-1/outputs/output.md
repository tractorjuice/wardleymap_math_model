# Wardley Map — Freelance Marketplace

**Scenario.** A two-sided freelance marketplace. Clients post jobs, freelancers bid on them, the platform facilitates matching, communication, contracting, escrow, payment, and dispute resolution, and takes a cut (commission) on each completed engagement.

Because the scenario has two distinct user types with different needs, the map uses two anchors.

---

## 1. OWM Output

```
title Freelance Marketplace
style wardley

// Anchors (two-sided marketplace)
anchor Client - Get Work Done [0.98, 0.70]
anchor Freelancer - Earn Income [0.98, 0.70]

// Visible activities (top of the map)
component Job Posting [0.86, 0.70]
component Bid / Proposal Submission [0.86, 0.65]
component Messaging / Chat [0.78, 0.78]
component Search [0.80, 0.80]
component Freelancer Profiles [0.82, 0.62]
component Ratings & Reviews [0.80, 0.60]
component Dispute Resolution [0.74, 0.35]
component Contract / SOW Templates [0.72, 0.55]

// Middle layer - the differentiating platform logic
component Matching / Recommendation [0.68, 0.40]
component Trust & Safety / Fraud Detection [0.58, 0.38]
component Skills Taxonomy [0.55, 0.45]
component Market Rate Data [0.52, 0.42]
component Analytics Dashboard [0.60, 0.58]
component File Sharing / Deliverables [0.62, 0.72]
component Notifications (Email / SMS) [0.64, 0.85]

// Regulated / financial plumbing
component Escrow / Payment Holding [0.55, 0.68]
component Commission Billing [0.50, 0.78]
component Identity / KYC Verification [0.45, 0.72]
component Payment Processing [0.40, 0.88]

// Deep commodity foundations
component CDN / Network [0.22, 0.92]
component Compute / Hosting [0.18, 0.90]

// Notes
note Differentiator band [0.65, 0.38]
note Outsource / buy-as-utility band [0.25, 0.88]

// Dependencies — Client side
Client - Get Work Done->Job Posting
Client - Get Work Done->Search
Client - Get Work Done->Freelancer Profiles
Client - Get Work Done->Messaging / Chat
Client - Get Work Done->Ratings & Reviews
Client - Get Work Done->Contract / SOW Templates
Client - Get Work Done->Escrow / Payment Holding
Client - Get Work Done->Dispute Resolution

// Dependencies — Freelancer side
Freelancer - Earn Income->Bid / Proposal Submission
Freelancer - Earn Income->Freelancer Profiles
Freelancer - Earn Income->Messaging / Chat
Freelancer - Earn Income->Ratings & Reviews
Freelancer - Earn Income->Payment Processing
Freelancer - Earn Income->Dispute Resolution

// Cross dependencies
Job Posting->Skills Taxonomy
Bid / Proposal Submission->Job Posting
Search->Matching / Recommendation
Search->Skills Taxonomy
Matching / Recommendation->Skills Taxonomy
Matching / Recommendation->Market Rate Data
Matching / Recommendation->Ratings & Reviews
Ratings & Reviews->Trust & Safety / Fraud Detection
Freelancer Profiles->Identity / KYC Verification
Contract / SOW Templates->Escrow / Payment Holding
Escrow / Payment Holding->Payment Processing
Escrow / Payment Holding->Identity / KYC Verification
Commission Billing->Payment Processing
Dispute Resolution->Messaging / Chat
Dispute Resolution->Ratings & Reviews
Messaging / Chat->Notifications (Email / SMS)
File Sharing / Deliverables->Compute / Hosting
Analytics Dashboard->Market Rate Data
Analytics Dashboard->Ratings & Reviews

// Platform foundations
Matching / Recommendation->Compute / Hosting
Search->Compute / Hosting
Job Posting->Compute / Hosting
Messaging / Chat->Compute / Hosting
Freelancer Profiles->Compute / Hosting
Notifications (Email / SMS)->Compute / Hosting
Compute / Hosting->CDN / Network

// Movement hints (scenario, not forecast)
evolve Matching / Recommendation 0.65
evolve Skills Taxonomy 0.70
evolve Identity / KYC Verification 0.85
evolve Trust & Safety / Fraud Detection 0.60

// Pipelines (range of offerings within one component)
pipeline Payment Processing [0.80, 0.95]
pipeline Dispute Resolution [0.25, 0.55]

// Inertia flags
component Contract / SOW Templates [0.72, 0.55] inertia
```

---

## 2. Evolution scoring (ε) — worked table

Using the 4-row cheat sheet from SKILL.md (Ubiquity, Certainty, User Perception, Publication Types) with band midpoints I→0.125, II→0.375, III→0.625, IV→0.875. ε is the mean of the four picks. Variance flags "in transition".

| Component | Ubiq. | Cert. | User Perc. | Pub. | ε | Stage |
|---|---|---|---|---|---|---|
| Job Posting | IV | IV | III | III | 0.70 | Product (+rental) upper |
| Bid / Proposal Submission | III | III | III | IV | 0.69 | Product (+rental) |
| Messaging / Chat | IV | IV | IV | IV | 0.875 | Commodity (+utility) |
| Search | IV | IV | IV | IV | 0.875 | Commodity (+utility) |
| Freelancer Profiles | III | III | III | III | 0.625 | Product (+rental) |
| Ratings & Reviews | III | III | III | III | 0.625 | Product (+rental) |
| Matching / Recommendation | II | II | II | III | 0.44 | Custom / Product cusp (transition) |
| Trust & Safety / Fraud Detection | II | II | II | III | 0.44 | Custom / transition |
| Skills Taxonomy | II | II | II | III | 0.44 | Custom (in transition) |
| Market Rate Data | II | II | II | III | 0.44 | Custom / transition |
| Dispute Resolution | II | II | II | II | 0.375 | Custom Built |
| Contract / SOW Templates | III | III | II | III | 0.56 | Product (+rental) — inertia |
| Escrow / Payment Holding | III | IV | III | III | 0.69 | Product (+rental) |
| Commission Billing | IV | IV | IV | III | 0.81 | Commodity |
| Identity / KYC Verification | III | IV | III | IV | 0.75 | Commodity cusp |
| Payment Processing | IV | IV | IV | IV | 0.875 | Commodity (+utility) |
| Notifications (Email / SMS) | IV | IV | IV | IV | 0.875 | Commodity (+utility) |
| File Sharing / Deliverables | IV | IV | III | IV | 0.81 | Commodity |
| Analytics Dashboard | III | III | III | III | 0.625 | Product (+rental) |
| CDN / Network | IV | IV | IV | IV | 0.875 | Commodity (+utility) |
| Compute / Hosting | IV | IV | IV | IV | 0.875 | Commodity (+utility) |

**Components flagged as in transition** (rows disagree, high variance): Matching / Recommendation, Trust & Safety / Fraud Detection, Skills Taxonomy, Market Rate Data. Range ≈ 0.375–0.625. Plot as error bars, not points.

---

## 3. Strategic analysis

### a. Top 3 by differentiation pressure D(v) = ν · (1 − ε)

Components high on the value chain and still immature — where advantage is available.

| Rank | Component | ν | ε | D |
|---|---|---|---|---|
| 1 | **Dispute Resolution** | 0.74 | 0.35 | **0.481** |
| 2 | **Matching / Recommendation** | 0.68 | 0.40 | **0.408** |
| 3 | **Trust & Safety / Fraud Detection** | 0.58 | 0.38 | **0.360** |

Reasoning. A freelance marketplace lives or dies on trust. Disputes are the single most emotional moment in the buyer/seller relationship, and no one has an "accepted" (Stage IV) solution — fast, fair, cheap dispute resolution is a durable differentiator. Matching directly determines whether the right freelancer surfaces for the right job; small ranking gains compound into take-rate and retention. Fraud detection sits just below: visible to neither side when it works, catastrophic when it fails. These three are the **invest** list.

### b. Top 3 by commodity leverage K(v) = (1 − ν) · ε

Components deep in the stack and mature — where the platform should **buy / rent / outsource** rather than build.

| Rank | Component | ν | ε | K |
|---|---|---|---|---|
| 1 | **Compute / Hosting** | 0.18 | 0.875 | **0.718** |
| 2 | **CDN / Network** | 0.22 | 0.92 | **0.718** |
| 3 | **Payment Processing** | 0.40 | 0.88 | **0.528** |

Reasoning. Compute, CDN, and payment rails are utilities. Building your own cloud, edge network, or card-acquiring stack is self-harm for a marketplace. Rent them (AWS/GCP/Azure, Cloudflare/Fastly, Stripe/Adyen). **Identity/KYC Verification** (K = 0.414) and **Commission Billing** (K = 0.390) narrowly miss the podium but belong in the same category: use specialised utility providers (Persona/Onfido/Sumsub for KYC, Stripe Tax / Avalara for invoicing).

### c. Top 3 dependency risks R(a, b) = ν(a) · (1 − ε(b))

Edges where something users see directly depends on something still fragile.

| Rank | Edge (a → b) | ν(a) | ε(b) | R |
|---|---|---|---|---|
| 1 | Client anchor → Dispute Resolution | 0.98 | 0.35 | **0.637** |
| 2 | Client anchor → Contract / SOW Templates (inertia) | 0.98 | 0.55 | **0.441** |
| 3 | Search → Matching / Recommendation | 0.80 | 0.40 | **0.480** |

(Freelancer anchor → Dispute Resolution is identical to rank 1.)

Interpretation. The most load-bearing user-facing promise of the platform — *"we'll keep you safe if something goes wrong"* — rests on a Custom-Built, under-evolved capability. That is exactly where risk *and* differentiation co-locate, so this is simultaneously the biggest threat and the biggest prize. Search quality also depends on matching quality; a weak matcher creates a visible product defect.

### d. Suggested Wardley gameplays (from the 61-play catalogue)

Invest side — differentiators:
- **#36 Directed investment** — fund Matching / Recommendation, Trust & Safety, and Dispute Resolution as specific future-change bets. These are not line-of-business costs; treat them VC-style.
- **#37 Experimentation** — hackdays / spike teams around matching algorithms and fraud signals; Stage II components reward exploration.
- **#38 Creating centres of gravity** — build a visible trust-and-safety / marketplace-integrity hub that attracts the scarce talent for this work.
- **#26 Differentiation** — position Dispute Resolution as the *visible* user promise ("we resolve disputes in 48 hours") to create a user-perceptible difference.

Two-sided / network side:
- **#16 Exploiting Network Effects** — core to the model; every freelancer attracts more clients and vice versa. Target: Ratings & Reviews and Freelancer Profiles (the data assets that create the cross-side effect).
- **#45 Two factor** — consciously manage the chicken-and-egg: subsidise whichever side is short (usually freelancers early, clients later in category expansion).
- **#43 Sensing Engines (ILC)** — innovate new services (escrow types, contract templates, skill verifications), leverage the ones adopted, commoditise them into the core offering.

Outsource / utility side:
- **#17 Co-operation** — partner with payment, KYC, CDN, and compute providers rather than build.
- **#15 Open Approaches** — publish the Skills Taxonomy as open data / open API. A shared taxonomy reduces friction, accelerates ecosystem, and positions the platform as the **standard** (see below).
- **#30 Standards game** — drive the Skills Taxonomy and ratings-portability format toward being *the* industry standard. The player who owns the taxonomy owns search.

Defensive / ecosystem:
- **#44 Tower and Moat** — once matching + trust + dispute are strong, the moat is data (past engagements, ratings, taxonomy). Protect the data graph; open the APIs around it.
- **#41 Alliances** — with corporate procurement platforms / staffing agencies to expand the client side.
- **#14 Market Enablement** — encourage a freelancer-tooling ecosystem (invoicing, tax, training) around the core platform.

Channel / acquisition:
- **#6 Channel Conflict** — watch for LinkedIn, Upwork, Fiverr, vertical specialists (Toptal) competing on the same two-sided pattern.

### e. Doctrine violations to watch for

Reviewing against the 40 doctrine principles (`doctrine.md`):

- **#1 Focus on user needs / #10 Know your users** — satisfied by having two explicit anchors; do *not* collapse into a single "user". A common failure mode is designing only for the paying side (the client) and treating freelancers as supply. That violates #1 for half the marketplace.
- **#8 Focus on high situational awareness** — ensure Matching, Trust & Safety, and Market Rate Data are continuously re-scored; they are in transition (high variance) and can shift quarter on quarter.
- **#13 Manage inertia** — Contract / SOW Templates carries an inertia flag. Expect legal, governance-change, and political-capital resistance when moving from bespoke templates to algorithmic contracts; see `inertia.md` #3 (political capital), #10 (governance change), #16 (rewards and culture).
- **#22 Use standards where appropriate** — for payment (ISO 20022), KYC (eIDAS, GLEIF), identity (OIDC), messaging (SMTP / webhook). Don't reinvent.
- **Knowledge layer underspecification risk** — the map's one Knowledge component (Skills Taxonomy) is under-specified. A richer Knowledge layer (job-outcome ontology, trust model, rate model) would strengthen the map; flag this for the next iteration.
- **#25 Set exceptional standards / #26 Optimise flow** — trust-and-safety SLAs (response-time, resolution-time) must be visible operational metrics, not hidden.

### f. Caveat

The evolution positions above place each component **now**, based on the market for marketplace-style freelance platforms. The `evolve` hints (Matching → 0.65, Skills Taxonomy → 0.70, Identity/KYC → 0.85, Trust & Safety → 0.60) are **scenarios, not forecasts**. Per Wardley's climatic pattern: *"you cannot measure evolution over time or adoption."* Treat differentiation pressure D, commodity leverage K, and dependency risk R as attention prompts — heuristics proposed by the skill's math model, not canonical Wardley metrics. Re-map on a regular cadence; strategy is iterative, not linear (doctrine #23).

---

## 4. Summary — invest vs outsource

**Invest (build, own, differentiate):**
1. **Matching / Recommendation** — the core product moment for both sides.
2. **Trust & Safety / Fraud Detection** — invisible when working, fatal when not.
3. **Dispute Resolution** — the user-facing trust promise; currently Custom Built industry-wide.
4. **Ratings & Reviews + Freelancer Profiles** — the data assets that drive network effects and lock-in.
5. **Skills Taxonomy + Market Rate Data** — the proprietary knowledge layer that feeds matching and analytics; pursue the **Standards game** here.

**Outsource (rent from utility providers):**
1. **Compute / Hosting** — cloud (AWS/GCP/Azure).
2. **CDN / Network** — Cloudflare / Fastly / Akamai.
3. **Payment Processing** — Stripe / Adyen / Braintree.
4. **Identity / KYC Verification** — Persona / Onfido / Sumsub / Jumio.
5. **Notifications (Email / SMS)** — SendGrid / Twilio / AWS SES-SNS.
6. **File Sharing / Deliverables storage** — S3 / GCS + a thin product layer.
7. **Commission Billing plumbing** — Stripe Billing / Chargebee / Avalara for tax.

**Keep on a short leash (Product +rental, monitor closely):** Job Posting, Bid / Proposal Submission, Messaging / Chat, Search, Contract / SOW Templates, Analytics Dashboard, Escrow / Payment Holding. These are table-stakes product surfaces — build thin, use commodities underneath, and do not let engineering spend drift from the true differentiators.
