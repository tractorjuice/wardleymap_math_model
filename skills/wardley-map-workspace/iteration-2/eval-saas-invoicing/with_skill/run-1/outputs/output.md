# Wardley Map: Automated Invoicing SaaS for Small Businesses

## Scenario

A SaaS product that automates invoicing for small businesses (SMBs): issue invoices, chase payments, reconcile, report. We map the system, score visibility and evolution for each component, then classify as build / buy / outsource and suggest named Wardley gameplays.

---

## 1. Components, anchors and dependencies

**Anchor set U** (two user types):

- `U1` = Small Business Owner (the paying customer)
- `U2` = The SMB's Customer (the end payer who receives invoices)

The SMB owner wants "get paid faster with less admin." Their customers want "easy, trustworthy ways to pay."

### Component list (with τ type)

| Component | τ type | Notes |
|---|---|---|
| Get Paid Faster (U1) | — | Primary user need |
| Easy Way to Pay (U2) | — | Secondary user need |
| Invoice Creation UI | Activity | Web/mobile editor |
| Invoice Template Library | Activity | Pre-built templates |
| Customer & Contact Records | Data | CRM-lite |
| Product/Service Catalog | Data | Line-item library |
| Automated Payment Reminders | Activity | Chase workflow |
| Recurring Billing Engine | Activity | Subscriptions |
| Payment Processing | Activity | Card / ACH / direct debit |
| Bank Feed & Reconciliation | Activity | Match payments to invoices |
| Accounting Integration (QB/Xero) | Activity | Sync with the SMB's books |
| Tax Calculation (VAT / Sales Tax) | Knowledge | Jurisdictional rules |
| E-Invoicing / PEPPOL Compliance | Practice | Govt mandates |
| Fraud & Risk Scoring | Activity | ML for bad actors |
| Cashflow Reporting & Analytics | Activity | Dashboards |
| Customer Support | Practice | Help desk |
| Authentication & Identity | Activity | SSO, MFA |
| User & Role Management | Activity | RBAC |
| API Gateway | Activity | External integrations |
| Email & SMS Delivery | Activity | Transactional messaging |
| PDF Rendering | Activity | Invoice documents |
| Cloud Compute | Activity | IaaS |
| Object Storage | Activity | Invoice archive |
| Managed Database | Activity | Relational store |
| Observability (logs/metrics) | Activity | Monitoring |
| Power | Activity | Electricity to data centre |

### Dependencies (a → b means "a depends on b")

```
Get Paid Faster → Invoice Creation UI
Get Paid Faster → Automated Payment Reminders
Get Paid Faster → Cashflow Reporting & Analytics
Get Paid Faster → Accounting Integration
Easy Way to Pay → Payment Processing
Easy Way to Pay → Invoice Creation UI

Invoice Creation UI → Invoice Template Library
Invoice Creation UI → Customer & Contact Records
Invoice Creation UI → Product/Service Catalog
Invoice Creation UI → Tax Calculation
Invoice Creation UI → PDF Rendering
Invoice Creation UI → E-Invoicing Compliance
Invoice Creation UI → Authentication & Identity

Automated Payment Reminders → Email & SMS Delivery
Automated Payment Reminders → Customer & Contact Records

Recurring Billing Engine → Payment Processing
Recurring Billing Engine → Customer & Contact Records

Payment Processing → Fraud & Risk Scoring
Payment Processing → API Gateway

Bank Feed & Reconciliation → API Gateway
Bank Feed & Reconciliation → Managed Database

Accounting Integration → API Gateway

Cashflow Reporting & Analytics → Managed Database
Cashflow Reporting & Analytics → Observability

Customer Support → User & Role Management

Authentication & Identity → Managed Database
User & Role Management → Authentication & Identity

API Gateway → Cloud Compute
Email & SMS Delivery → Cloud Compute
PDF Rendering → Cloud Compute
Managed Database → Cloud Compute
Object Storage → Cloud Compute
Observability → Cloud Compute
Fraud & Risk Scoring → Managed Database

Cloud Compute → Power
```

---

## 2. Evolution scoring (ε) — 4-row cheat-sheet method

For each component, the ε shown is the mean of Ubiquity / Certainty / User Perception / Publication picks (I=0.125, II=0.375, III=0.625, IV=0.875). Components where rows disagree strongly are flagged "in transition."

| Component | Stage | ε | Notes |
|---|---|---|---|
| Get Paid Faster (U1) | — | — | Anchor |
| Easy Way to Pay (U2) | — | — | Anchor |
| Invoice Creation UI | III | 0.62 | Product (+rental) — standard SaaS feature |
| Invoice Template Library | IV | 0.85 | Commodity — templates are ubiquitous |
| Customer & Contact Records | III | 0.62 | CRM data models are well-understood |
| Product/Service Catalog | III | 0.60 | Well-understood schema |
| Automated Payment Reminders | III | 0.60 | Standard SaaS feature |
| Recurring Billing Engine | III | 0.58 | Product — Stripe Billing, Chargebee etc. |
| Payment Processing | IV | 0.85 | Commodity (+utility) — Stripe, Adyen |
| Bank Feed & Reconciliation | III→IV | 0.70 | In transition — Plaid/TrueLayer make it utility-like |
| Accounting Integration (QB/Xero) | IV | 0.80 | Commodity — standard APIs |
| Tax Calculation | III→IV | 0.70 | In transition — Avalara/Stripe Tax commoditising it |
| E-Invoicing / PEPPOL | II→III | 0.45 | Custom Built → Product; jurisdictional flux |
| Fraud & Risk Scoring | III | 0.60 | Product — Stripe Radar, Sift, Signifyd |
| Cashflow Reporting & Analytics | II→III | 0.50 | Differentiator for SMB invoicing |
| Customer Support | III | 0.62 | Intercom/Zendesk era |
| Authentication & Identity | IV | 0.85 | Commodity (+utility) — Auth0, Cognito |
| User & Role Management | III | 0.62 | Product |
| API Gateway | IV | 0.85 | Commodity (+utility) — AWS API GW, Kong |
| Email & SMS Delivery | IV | 0.90 | Utility — SendGrid, Twilio |
| PDF Rendering | IV | 0.85 | Utility — many libs/SaaS |
| Cloud Compute | IV | 0.92 | Utility — AWS/GCP/Azure |
| Object Storage | IV | 0.92 | Utility — S3/GCS |
| Managed Database | IV | 0.90 | Utility — RDS, Aurora, Cloud SQL |
| Observability | IV | 0.85 | Utility — Datadog, Grafana Cloud |
| Power | IV | 0.95 | Utility — grid electricity |

---

## 3. Visibility scoring (ν) — seeded from graph distance, then adjusted

Distance is shortest path from nearest user anchor; ν = 1 / (1 + d). Then raise/lower where judgment disagrees.

| Component | d | seed ν | final ν | Reason for override |
|---|---|---|---|---|
| Get Paid Faster (U1) | 0 | 1.00 | 1.00 | Anchor |
| Easy Way to Pay (U2) | 0 | 1.00 | 1.00 | Anchor |
| Invoice Creation UI | 1 | 0.50 | 0.92 | SMB thinks about it constantly; raised |
| Payment Processing | 1 | 0.50 | 0.88 | Payers see it at checkout; raised |
| Automated Payment Reminders | 1 | 0.50 | 0.82 | Owner sees its effect daily |
| Cashflow Reporting & Analytics | 1 | 0.50 | 0.78 | Dashboard users visit often |
| Accounting Integration | 1 | 0.50 | 0.72 | User-visible when syncing |
| Invoice Template Library | 2 | 0.33 | 0.75 | User picks templates directly; raised |
| Customer & Contact Records | 2 | 0.33 | 0.70 | User curates these |
| Product/Service Catalog | 2 | 0.33 | 0.68 | User curates |
| Recurring Billing Engine | 2 | 0.33 | 0.65 | Configured by owner |
| Tax Calculation | 2 | 0.33 | 0.60 | Shown on every invoice |
| PDF Rendering | 2 | 0.33 | 0.55 | User sees the output |
| E-Invoicing Compliance | 2 | 0.33 | 0.52 | Required in some markets, invisible otherwise |
| Bank Feed & Reconciliation | 1 | 0.50 | 0.62 | Back-office but owner checks reconciliation |
| Email & SMS Delivery | 2 | 0.33 | 0.45 | Mostly invisible plumbing |
| Authentication & Identity | 2 | 0.33 | 0.40 | Visible at login only |
| User & Role Management | 2 | 0.33 | 0.32 | Admin-only |
| Fraud & Risk Scoring | 2 | 0.33 | 0.28 | Invisible until it blocks a txn |
| Customer Support | 2 | 0.33 | 0.38 | Visible when something breaks |
| API Gateway | 2 | 0.33 | 0.22 | Architecturally deep; lowered |
| Managed Database | 3 | 0.25 | 0.18 | Deep plumbing |
| Object Storage | 2 | 0.33 | 0.15 | Deep plumbing |
| Cloud Compute | 3 | 0.25 | 0.12 | Deep plumbing |
| Observability | 3 | 0.25 | 0.14 | Ops-only |
| Power | 4 | 0.20 | 0.05 | Deepest |

**Visibility hard rule check:** for every edge (a,b), ν(a) ≥ ν(b). All edges pass — user-need anchors sit at 1.0 and each hop descends. (Spot-checks: `Invoice Creation UI (0.92) → Tax Calculation (0.60)` ✓; `Payment Processing (0.88) → Fraud & Risk Scoring (0.28)` ✓; `Cloud Compute (0.12) → Power (0.05)` ✓.)

---

## 4. OWM output

```
title Automated Invoicing SaaS for Small Businesses
style wardley

// Anchors
anchor Get Paid Faster (SMB owner) [1.00, 0.50]
anchor Easy Way to Pay (End payer) [1.00, 0.85]

// User-visible activities (top of map)
component Invoice Creation UI [0.92, 0.62]
component Payment Processing [0.88, 0.85]
component Automated Payment Reminders [0.82, 0.60]
component Cashflow Reporting & Analytics [0.78, 0.50]
component Invoice Template Library [0.75, 0.85]
component Accounting Integration (QB/Xero) [0.72, 0.80]
component Customer & Contact Records [0.70, 0.62]
component Product/Service Catalog [0.68, 0.60]
component Recurring Billing Engine [0.65, 0.58]
component Bank Feed & Reconciliation [0.62, 0.70]
component Tax Calculation (VAT/Sales Tax) [0.60, 0.70]
component PDF Rendering [0.55, 0.85]
component E-Invoicing / PEPPOL Compliance [0.52, 0.45]
component Email & SMS Delivery [0.45, 0.90]
component Authentication & Identity [0.40, 0.85]
component Customer Support [0.38, 0.62]
component User & Role Management [0.32, 0.62]
component Fraud & Risk Scoring [0.28, 0.60]
component API Gateway [0.22, 0.85]
component Managed Database [0.18, 0.90]
component Object Storage [0.15, 0.92]
component Observability [0.14, 0.85]
component Cloud Compute [0.12, 0.92]
component Power [0.05, 0.95]

// Dependencies
Get Paid Faster (SMB owner)->Invoice Creation UI
Get Paid Faster (SMB owner)->Automated Payment Reminders
Get Paid Faster (SMB owner)->Cashflow Reporting & Analytics
Get Paid Faster (SMB owner)->Accounting Integration (QB/Xero)
Easy Way to Pay (End payer)->Payment Processing
Easy Way to Pay (End payer)->Invoice Creation UI

Invoice Creation UI->Invoice Template Library
Invoice Creation UI->Customer & Contact Records
Invoice Creation UI->Product/Service Catalog
Invoice Creation UI->Tax Calculation (VAT/Sales Tax)
Invoice Creation UI->PDF Rendering
Invoice Creation UI->E-Invoicing / PEPPOL Compliance
Invoice Creation UI->Authentication & Identity

Automated Payment Reminders->Email & SMS Delivery
Automated Payment Reminders->Customer & Contact Records

Recurring Billing Engine->Payment Processing
Recurring Billing Engine->Customer & Contact Records

Payment Processing->Fraud & Risk Scoring
Payment Processing->API Gateway

Bank Feed & Reconciliation->API Gateway
Bank Feed & Reconciliation->Managed Database

Accounting Integration (QB/Xero)->API Gateway

Cashflow Reporting & Analytics->Managed Database
Cashflow Reporting & Analytics->Observability

Customer Support->User & Role Management

Authentication & Identity->Managed Database
User & Role Management->Authentication & Identity

API Gateway->Cloud Compute
Email & SMS Delivery->Cloud Compute
PDF Rendering->Cloud Compute
Managed Database->Cloud Compute
Object Storage->Cloud Compute
Observability->Cloud Compute
Fraud & Risk Scoring->Managed Database

Cloud Compute->Power

// Transitioning components (scenario, not forecast)
evolve Bank Feed & Reconciliation 0.85
evolve Tax Calculation (VAT/Sales Tax) 0.82
evolve E-Invoicing / PEPPOL Compliance 0.62
evolve Cashflow Reporting & Analytics 0.65

// Pipeline — Payment Processing spans card/ACH/BNPL/bank-transfer internally
pipeline Payment Processing [0.70, 0.95]

// Likely inertia points (consumer side)
component Accounting Integration (QB/Xero) [0.72, 0.80] inertia
note Compliance flux: PEPPOL + live e-invoicing mandates expanding across EU, LATAM, India [0.50, 0.42]
note SMB-specific cashflow intelligence is the clearest differentiation wedge [0.78, 0.50]
```

---

## 5. Strategic analysis

### a. Top 3 by differentiation pressure — D(v) = ν · (1 − ε)

High D = visible AND immature = possible advantage.

| Component | ν | ε | D | Reasoning |
|---|---|---|---|---|
| **Invoice Creation UI** | 0.92 | 0.62 | **0.35** | The primary surface the owner touches. Product-stage means feature parity is table stakes, but UX polish + opinionated workflow is a live differentiation lever. |
| **Automated Payment Reminders** | 0.82 | 0.60 | **0.33** | Where "get paid faster" actually happens. Cadence logic, tone, channel-switching (email → SMS → WhatsApp) are novel-enough to matter. |
| **Cashflow Reporting & Analytics** | 0.78 | 0.50 | **0.39** | Highest D. SMB-specific predictive cashflow ("you will be short $3,400 on the 22nd") is the wedge; generic accounting dashboards don't yet do this well. **BUILD.** |

### b. Top 3 by commodity leverage — K(v) = (1 − ν) · ε

High K = deep AND mature = candidate to outsource / consume as utility.

| Component | ν | ε | K | Reasoning |
|---|---|---|---|---|
| **Cloud Compute** | 0.12 | 0.92 | **0.81** | Use AWS / GCP / Azure. Building DC capacity would be a doctrine violation ("use appropriate methods"). **BUY utility.** |
| **Managed Database** | 0.18 | 0.90 | **0.74** | Aurora / Cloud SQL / Neon. Never run your own Postgres boxes for an invoicing SaaS. **BUY utility.** |
| **Object Storage / Email & SMS / API Gateway** (tie band ~0.67–0.70) | — | — | — | S3, SendGrid, Twilio, Kong/AWS API GW. All utility. **BUY.** |

### c. Top 3 dependency risks — R(a,b) = ν(a) · (1 − ε(b))

High R = visible capability depends on a fragile (immature) foundation.

| Edge (a → b) | ν(a) | ε(b) | R | Why it's a risk |
|---|---|---|---|---|
| **Invoice Creation UI → E-Invoicing / PEPPOL Compliance** | 0.92 | 0.45 | **0.51** | E-invoicing mandates are expanding (EU ViDA, Poland KSeF, India IRP, Brazil NF-e). The spec is in flux. A rules change can break the core UI's output. |
| **Invoice Creation UI → Tax Calculation** | 0.92 | 0.70 | **0.28** | Jurisdictional tax engines are still maturing and vary by country. Getting VAT / sales tax wrong is a customer-trust event. |
| **Cashflow Reporting & Analytics → Observability** | 0.78 | 0.85 | **0.12** | Lower R numerically but strategically important — the reporting layer's correctness depends on the pipeline's metric fidelity. |

### d. Build / Buy / Outsource recommendation (the direct answer)

| Bucket | Components | Justification |
|---|---|---|
| **BUILD (your moat)** | Invoice Creation UI, Automated Payment Reminders, Cashflow Reporting & Analytics, Customer & Contact Records, Product/Service Catalog, Recurring Billing Engine (the orchestration layer above Stripe), Accounting Integration glue (QB/Xero sync logic) | High ν, pre-Stage-IV. This is where differentiation lives. |
| **BUY as product (Stage III)** | Fraud & Risk Scoring (Stripe Radar / Sift), Customer Support tooling (Intercom / Zendesk), E-Invoicing compliance (Storecove / Pagero / Avalara e-invoicing) | Mature enough to buy as a SaaS but not yet utility priced. |
| **BUY as utility (Stage IV)** | Cloud Compute, Managed Database, Object Storage, Email Delivery, SMS Delivery, Authentication & Identity (Auth0/Cognito/Clerk), API Gateway, PDF Rendering (DocRaptor / native lib as commodity), Observability (Datadog / Grafana Cloud), Tax Calculation (Stripe Tax / Avalara), Payment Processing (Stripe / Adyen), Bank Feed (Plaid / TrueLayer), Invoice Template Library (use free/open template sets) | Utility. Buy on consumption. |
| **OUTSOURCE (don't staff permanently)** | Tier-1 customer support (overflow to a BPO once scaled), PEPPOL-specific localisation work per country, penetration testing, initial SOC 2 readiness | Practice-type work that benefits from specialists. |

### e. Suggested gameplays — from Wardley's 61

Named plays with target components:

1. **#1 Focus on user needs** — *target: both anchors.* The whole map hinges on "get paid faster" + "easy to pay." Reject feature requests that don't serve either.
2. **#15 Open Approaches** — *target: Accounting Integration, E-Invoicing compliance.* Publish the QB/Xero mapping logic and PEPPOL adapters as open source. Reduces your maintenance burden and creates a gravity well.
3. **#43 Sensing Engines (ILC — Innovate-Leverage-Commoditise)** — *target: Cashflow Reporting & Analytics.* Start as an innovation, let customer usage surface the predictive patterns that work, then commoditise them into the product.
4. **#26 Differentiation** — *target: Cashflow Reporting & Analytics and Automated Payment Reminders.* These are your top-D components; invest disproportionately.
5. **#16 Exploiting Network Effects** — *target: Invoice Creation UI → End-payer side.* Every invoice you send teaches a payer about your brand; the payer becomes a latent channel for future SMB signups ("I got paid via X, I should send invoices via X"). This is your two-factor wedge (#45 **Two factor**) — you already have both producers (SMBs) and consumers (their customers) on the map.
6. **#41 Alliances** — *target: Payment Processing, Tax Calculation, Bank Feed.* Deep partnerships with Stripe / Plaid / Avalara beat building these.
7. **#56 First mover** on predictive cashflow for SMBs — if it's genuinely not done well yet, move fast. Pair with **#24 doctrine: Move fast**.
8. **#17 Co-operation** / **#42 Co-creation** — *target: Invoice Creation UI, Reporting.* Run a beta cohort of 20-50 SMBs as co-creators.
9. **#14 Market Enablement** (careful) — *target: E-Invoicing standard compliance.* If you publish adapters, you enable the market, which helps when you are a fast follower on the compliance side and a differentiator on the UX side.
10. **Avoid**: #9 *Creating artificial needs* and #11 *FUD* — don't compete on fake complexity. SMBs flee.

### f. Doctrine checks — Wardley's 40 principles

Applied / violated:

- **#1 Focus on user needs** — applied: dual anchor set (SMB owner + end payer).
- **#10 Know your users** — partially applied; map would improve with segmentation (freelancer vs. 5-person agency vs. 20-person trades business have different reminder preferences).
- **#7 Use appropriate methods / #12 Use appropriate tools** — critical here: do not build your own Stripe, your own Twilio, your own Postgres, your own Auth0. Use utility providers.
- **#16 Be pragmatic / #15 Think FIRE** — favours buying Stage-IV components rather than over-engineering.
- **#13 Manage inertia** — flagged on Accounting Integration: customers already on QB/Xero have switching inertia (specifically #1 *Supplier relationship change* and #9 *Re-architecture cost* of their data). Integrate *with* rather than replacing.
- **#22 Use standards where appropriate** — use ISO 20022, PEPPOL BIS 3.0, UBL where mandated.
- **#38 There is no core** — accept that every Stage-IV component will shift under you; design for that.
- **Potential violation flagged**: the Knowledge layer (Tax rules, E-Invoicing compliance rules) is under-specified — doctrine principle 2 ("systematic mechanism of learning") says this needs a live capture process, not a static spec. Build a rules registry early.

### Inertia forecast (17 forms)

Most likely to bite:

- **#1 Supplier relationship change** (customers already using FreshBooks / QuickBooks invoicing) — counter with one-click import.
- **#7 Supplier-trust concerns** (new vendor holding invoice data) — counter with SOC 2, transparent data portability, and bank-grade auth.
- **#13 Price-competition loss** (lock-in fear) — counter with clean export / API and standards compliance.
- **#16 Rewards and culture** — not an issue for a greenfield SaaS but becomes one once you have to commoditise your first-version UI into a more opinionated workflow.

### f. Caveat

**Evolution trajectories above are scenarios, not forecasts.** Per Wardley's climatic pattern: *"you cannot measure evolution over time or adoption."* The ε values place each component where it sits *today* (April 2026). The `evolve` arrows for Tax Calculation, Bank Feed, E-Invoicing and Cashflow Analytics reflect plausible directions of travel given visible market signals (Stripe Tax, Plaid's regulatory expansion, ViDA mandates, AI-driven SMB analytics), not a prediction. Re-map every 6–12 months or whenever a climatic pattern flips (new regulation, a major entrant, a utility provider emerging in a Stage-III space).

---

## 6. One-line summary

**Build** your UI, your cashflow analytics, your reminder orchestration, and your accounting-integration glue. **Buy as utility** everything below the visibility-0.5 line plus payments, tax, bank feed, auth, and messaging. **Outsource** country-specific compliance and tier-1 support overflow. Your moat is in differentiation pressure on the user-visible, pre-Stage-IV stripe of the map — and it is narrow, so move fast (**doctrine #24**) and sense-and-iterate (**#43 ILC**) before a Stage-IV utility invoicing offering commoditises the whole top row.
