# Wardley Map: Freelance Marketplace Platform

## Scenario

A two-sided freelance marketplace where clients post jobs, freelancers bid, and the platform takes a cut of each transaction. Two user types (clients and freelancers) must be modelled as separate anchors.

## OWM Map

```owm
title Freelance Marketplace (Two-Sided Platform)
style wardley

// Anchors — two user types (doctrine #10: know your users)
anchor Client (Job Poster) [0.98, 0.55]
anchor Freelancer (Bidder) [0.98, 0.55]

// Stage IV — Commodity / utility
component Payments Processing [0.30, 0.88]
component KYC / Identity Verification [0.28, 0.82]
component Cloud Compute & Storage [0.12, 0.92]
component Email / SMS Notifications [0.40, 0.88]
component CDN & Media Hosting [0.14, 0.90]
component Tax / 1099 Reporting [0.22, 0.78]

// Stage III — Product (+rental)
component Search & Filtering [0.65, 0.62]
component Messaging / Chat [0.70, 0.68]
component Video Calls [0.55, 0.72]
component Mobile Apps [0.82, 0.60]
component Web Platform UI [0.88, 0.62]
component Escrow Service [0.50, 0.58]
component Freelancer Profiles [0.78, 0.64]
component Job Posting Flow [0.85, 0.65]
component Bidding / Proposals Engine [0.75, 0.55]
component Dispute Resolution Workflow [0.45, 0.52]
component Contract Templates [0.48, 0.72]

// Stage II — Custom Built
component Reputation & Review System [0.68, 0.42]
component Matching Algorithm (bid-to-job) [0.60, 0.35]
component Fraud Detection [0.35, 0.40]
component Dynamic Commission Pricing [0.42, 0.32]
component Talent Skill Taxonomy [0.55, 0.38]
component Trust & Safety Policies [0.50, 0.45]

// Stage I — Genesis
component AI Job-Scoping Assistant [0.72, 0.18]
component Predictive Bid Success Scoring [0.58, 0.15]
component Weak-Signal Demand Forecasting [0.38, 0.10]

// Dependencies — client side
Client (Job Poster)->Job Posting Flow
Client (Job Poster)->Search & Filtering
Client (Job Poster)->Freelancer Profiles
Client (Job Poster)->Messaging / Chat
Client (Job Poster)->Reputation & Review System
Client (Job Poster)->Web Platform UI
Client (Job Poster)->Mobile Apps
Client (Job Poster)->AI Job-Scoping Assistant

// Dependencies — freelancer side
Freelancer (Bidder)->Bidding / Proposals Engine
Freelancer (Bidder)->Freelancer Profiles
Freelancer (Bidder)->Messaging / Chat
Freelancer (Bidder)->Mobile Apps
Freelancer (Bidder)->Web Platform UI
Freelancer (Bidder)->Predictive Bid Success Scoring
Freelancer (Bidder)->Reputation & Review System

// Platform internals
Job Posting Flow->Talent Skill Taxonomy
Job Posting Flow->AI Job-Scoping Assistant
Bidding / Proposals Engine->Matching Algorithm (bid-to-job)
Bidding / Proposals Engine->Escrow Service
Matching Algorithm (bid-to-job)->Talent Skill Taxonomy
Matching Algorithm (bid-to-job)->Reputation & Review System
Search & Filtering->Talent Skill Taxonomy
Search & Filtering->Reputation & Review System
Freelancer Profiles->KYC / Identity Verification
Freelancer Profiles->CDN & Media Hosting
Escrow Service->Payments Processing
Escrow Service->Dispute Resolution Workflow
Dispute Resolution Workflow->Trust & Safety Policies
Dispute Resolution Workflow->Contract Templates
Messaging / Chat->Notifications
Messaging / Chat->Video Calls
Reputation & Review System->Fraud Detection
Fraud Detection->KYC / Identity Verification
Dynamic Commission Pricing->Weak-Signal Demand Forecasting
Dynamic Commission Pricing->Matching Algorithm (bid-to-job)
Web Platform UI->Cloud Compute & Storage
Mobile Apps->Cloud Compute & Storage
Video Calls->Cloud Compute & Storage
Payments Processing->Tax / 1099 Reporting
Email / SMS Notifications->Cloud Compute & Storage

// Evolution arrows — where things are headed
evolve AI Job-Scoping Assistant 0.55
evolve Matching Algorithm (bid-to-job) 0.60
evolve Reputation & Review System 0.65
evolve Escrow Service 0.80
evolve Video Calls 0.88

// Notes
note Two-sided network: liquidity is the moat [0.92, 0.30]
note Commoditise below; differentiate at matching [0.55, 0.50]
note Stage-I AI is the weak-signal bet [0.70, 0.12]

// Inertia marker — existing manual dispute ops likely resist automation
component Manual Dispute Ops [0.42, 0.35] inertia

// Pipeline: the Escrow Service spans from custom to utility across providers
pipeline Escrow Service [0.58, 0.85]
```

---

## Strategic Analysis

*Heuristics D, K, R below are proposed by this skill's math model — treat as attention prompts, not canonical Wardley metrics.*

### a. Top 3 by Differentiation Pressure — D(v) = ν · (1 − ε)

| Rank | Component | ν | ε | D | Reasoning |
|---|---|---|---|---|---|
| 1 | **Reputation & Review System** | 0.68 | 0.42 | 0.394 | High visibility to both sides; still custom-built across the industry. Trust is the marketplace's core asset. |
| 2 | **AI Job-Scoping Assistant** | 0.72 | 0.18 | 0.590 | Near-user, Genesis-stage. Scoping poorly written jobs into biddable briefs is a genuine pain. |
| 3 | **Matching Algorithm** | 0.60 | 0.35 | 0.390 | Custom-built; directly drives liquidity and fill rate — the two-sided network's flywheel. |

These are where the platform should **build in-house** with specialist teams (Pioneers in PST terms — doctrine #4).

### b. Top 3 by Commodity Leverage — K(v) = (1 − ν) · ε

| Rank | Component | ν | ε | K | Reasoning |
|---|---|---|---|---|---|
| 1 | **Cloud Compute & Storage** | 0.12 | 0.92 | 0.810 | Pure utility — rent from hyperscalers, never build. |
| 2 | **CDN & Media Hosting** | 0.14 | 0.90 | 0.774 | Commodity; use Cloudflare / Fastly / S3. |
| 3 | **Payments Processing** | 0.30 | 0.88 | 0.616 | Stripe Connect / Adyen / PayPal mass-market APIs. Building your own acquiring stack is negative-ROI unless you reach vast scale. |

Also-ran: **Email/SMS Notifications** (K=0.528) — Twilio / SendGrid. **KYC/Identity** (K=0.590) — Persona / Onfido / Stripe Identity.

**Outsource / rent / consume-as-utility** every one of these. Town-Planner team owns the integrations.

### c. Top 3 Dependency Risks — R(a, b) = ν(a) · (1 − ε(b))

| Rank | Edge (a → b) | R | Why |
|---|---|---|---|
| 1 | Client → **AI Job-Scoping Assistant** | 0.98 · 0.82 = 0.80 | Anchor depends on a Genesis-stage component. High user-visible risk: if the AI mis-scopes, job posting fails. Mitigate: keep a manual flow behind a feature flag. |
| 2 | Freelancer → **Predictive Bid Success Scoring** | 0.98 · 0.85 = 0.83 | Anchor on Genesis scoring. Poor calibration erodes freelancer trust fast. Run shadow-mode before user-visible. |
| 3 | Bidding Engine → **Matching Algorithm** | 0.75 · 0.65 = 0.49 | Core bidding depends on a still-custom matcher. A regression here breaks the marketplace's primary value proposition. |

### d. Suggested Gameplays (from Wardley's 61)

Targeting the map above:

1. **#45 Two factor** — *the* defining play for this business. Bring clients and freelockers together; prioritise liquidity balance over either side's growth alone. Targets: both anchors.
2. **#16 Exploiting Network Effects** — Reputation, Reviews, and the Matching Algorithm all gain value with users. Harvest this into pricing power. Targets: Reputation & Review System, Matching Algorithm.
3. **#43 Sensing Engines (ILC)** — Innovate (in-house) the AI Job-Scoping Assistant & Bid Scoring; Leverage their usage data; Commoditise matching sub-components as they mature. Targets: Stage-I components and the evolution pipeline.
4. **#26 Differentiation** — User-visible difference through the review/trust layer, not through payments or hosting. Targets: Reputation & Review System.
5. **#30 Standards game** — Publish an open skill taxonomy & review-portability schema; push it to become the industry default. Locks ecosystem to your vocabulary. Targets: Talent Skill Taxonomy.
6. **#15 Open Approaches** — Open API for job posting and profile import; lets agencies and ATS tools integrate. Targets: Job Posting Flow, Freelancer Profiles.
7. **#27 Pricing policy** — Dynamic Commission Pricing exploits supply/demand imbalances per skill/region. Targets: Dynamic Commission Pricing.
8. **#55 Land grab** — Move first on an AI-scoped-brief feature before rivals productise it. Targets: AI Job-Scoping Assistant.
9. **#17 Co-operation / #41 Alliances** — With Stripe (payments), Persona (KYC), Twilio (comms). Don't compete with utilities; embed them. Targets: Stage-IV commodity row.
10. **#24 Sweat & Dump** — Offload manual dispute ops to a BPO while building the automated workflow. Targets: Manual Dispute Ops (tagged `inertia`).

### e. Doctrine Notes

**Adhered:**
- **#1 Focus on user needs / #10 Know your users** — both client and freelancer modelled as anchors.
- **#3 Common language** — skill taxonomy explicitly on-map.
- **#22 Use standards** — Payments, KYC, Cloud explicitly commoditised.
- **#12 Use appropriate tools** — Stage III/IV components consume utilities rather than rebuild.

**Likely violations to watch:**
- **#4 Knowledge layer under-specified.** The map has Data (reviews, reputation, bids) but thin on Knowledge (τ = K). Concepts like "what makes a good job brief" and "what predicts freelancer retention" are largely tacit. **Action:** extend the map with explicit Knowledge components before investing in the AI Scoping Assistant — doctrine #2 (systematic learning).
- **#13 Manage inertia.** Manual Dispute Ops is tagged but the inertia list wasn't unpacked. Forms likely present: *#16 Rewards and culture* (ops team's review metrics), *#8 Skill acquisition cost* (building ML ops for dispute triage), and *#11 Suitability doubt* ("can AI really adjudicate?"). Name them explicitly to counter them.
- **#14 Manage failure.** Dispute Resolution, Fraud Detection, and Trust & Safety are user-invisible until they fail catastrophically. Add SLOs & visible status before scaling.
- **#23 Strategy is iterative.** The `evolve` arrows are multi-year bets; revisit each quarter.

### f. Caveat

Evolution positions above reflect the component's state **now**, not a forecast. The `evolve` arrows are **scenarios, not predictions** — per Wardley's climatic pattern, *"you cannot measure evolution over time or adoption."* What this map shows is where each component currently sits on the cheat-sheet and where market pressure is plausibly pushing it; external shocks (regulation of AI, a dominant platform opening its APIs, a new payments monopoly) could redraw the landscape. Re-map every 3–6 months and whenever a major competitor moves.
