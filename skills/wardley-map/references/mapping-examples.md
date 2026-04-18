# Mapping Examples

Three worked Wardley Maps demonstrating the skill's output format and analysis depth. Use these as output templates.

---

## Example 1 — Tea Shop (classic single-anchor)

**Scenario:** A small tea shop that serves cups of tea to customers, handles payment, and sources tea leaves from suppliers.

### Map

```owm
title Tea Shop
style wardley

anchor Customer [0.98, 0.55]

// User-facing
component Cup of Tea [0.88, 0.65]
component Payment [0.85, 0.80]
component Service / Hospitality [0.80, 0.45]

// Mid-chain
component Barista [0.70, 0.40]
component Brewing [0.68, 0.60]
component Cup [0.65, 0.85]
component Milk & Sugar [0.55, 0.88]

// Ingredients and equipment
component Tea Leaves [0.50, 0.85]
component Hot Water [0.45, 0.90]
component Kettle [0.30, 0.90]
component Shop Premises [0.28, 0.55]

// Payment layer
component Till / POS [0.55, 0.70]
component Card Payment Processing [0.45, 0.90]

// Utilities
component Electricity [0.12, 0.95]
component Water [0.10, 0.95]

// Supply chain
component Tea Sourcing [0.25, 0.50]
component Tea Supplier Relationship [0.15, 0.45]

// Dependencies
Customer->Cup of Tea
Customer->Payment
Customer->Service / Hospitality
Cup of Tea->Brewing
Cup of Tea->Cup
Cup of Tea->Milk & Sugar
Service / Hospitality->Barista
Service / Hospitality->Shop Premises
Barista->Shop Premises
Brewing->Tea Leaves
Brewing->Hot Water
Brewing->Barista
Hot Water->Kettle
Hot Water->Water
Kettle->Electricity
Payment->Till / POS
Payment->Card Payment Processing
Till / POS->Electricity
Card Payment Processing->Electricity
Tea Leaves->Tea Sourcing
Tea Sourcing->Tea Supplier Relationship
Shop Premises->Electricity
Shop Premises->Water

evolve Tea Supplier Relationship 0.55
evolve Till / POS 0.85

note Differentiation zone [0.7, 0.35]
note Utility commodity [0.15, 0.92]
```

### Strategic analysis

**Top 3 by differentiation pressure D = ν·(1−ε):**
1. **Service / Hospitality** (0.80 × 0.55 = 0.44) — the core user-facing differentiator; a commodity tea shop competes on service.
2. **Barista** (0.70 × 0.60 = 0.42) — human capital is where craft emerges.
3. **Tea Supplier Relationship** (0.15 × 0.55 = 0.08 low D; but note the supply risk below).

**Top 3 by commodity leverage K = (1−ν)·ε:**
1. **Electricity** (0.88 × 0.95 = 0.84) — treat as utility, do not engineer.
2. **Water** (0.90 × 0.95 = 0.86) — same.
3. **Card Payment Processing** (0.55 × 0.90 = 0.50) — rent from Stripe/Square, do not build.

**Top 3 dependency risks R = ν(a)·(1−ε(b)):**
1. **(Brewing, Barista)** = 0.68 × 0.60 = 0.41 — the whole chain hangs on one barista.
2. **(Tea Leaves, Tea Sourcing)** = 0.50 × 0.50 = 0.25 — single-supplier risk.
3. **(Service / Hospitality, Barista)** = 0.80 × 0.60 = 0.48 — human capital fragility.

**Suggested gameplays:**
- **#1 Focus on user needs** — the service differentiation is the whole business; reinforce it.
- **#26 Differentiation** — lean into premium tea, ceremony, atmosphere.
- **#41 Alliances** — second-sourcing on tea suppliers to reduce dependency risk.
- **#29 Harvesting** — let the market develop kettles / water infra; buy cheapest commodities.

**Doctrine notes:**
- ✓ **#1 Focus on user needs** — map is correctly anchored on Customer.
- ⚠ **#10 Know your users** — single anchor is a simplification. Takeaway customers vs. sit-in customers may warrant two anchors.
- ⚠ **#13 Manage inertia** — Barista's human capital inertia (form #4) is a real strategic risk on a small team.

**Caveat:** Evolution trajectories (`evolve` arrows) are scenarios, not forecasts. Wardley's climatic pattern: *"you cannot measure evolution over time or adoption."*

---

## Example 2 — Freelance Marketplace (multi-anchor, two-sided)

**Scenario:** A marketplace where clients post jobs, freelancers bid on them, and the platform takes a cut.

### Map

```owm
title Freelance Marketplace
style wardley

// Two anchors for the two-sided market
anchor Client [0.98, 0.60]
anchor Freelancer [0.95, 0.50]

// User-facing
component Job Posting [0.82, 0.60]
component Bid Submission [0.80, 0.55]
component Portfolio / Profile [0.72, 0.65]
component Messaging [0.70, 0.82]

// Matching core
component Matching Algorithm [0.62, 0.35]
component Reputation & Reviews [0.58, 0.55]
component Skills Taxonomy [0.55, 0.40]

// Trust and transactions
component Escrow [0.48, 0.70]
component Dispute Resolution [0.45, 0.35]
component KYC / Identity [0.40, 0.85]
component Payment Processing [0.38, 0.90]
component FX / Multi-currency [0.35, 0.75]

// Infrastructure
component Auth [0.25, 0.90]
component Cloud Compute [0.18, 0.90]
component Database [0.15, 0.88]
component CDN [0.12, 0.92]
component Email / SMS [0.20, 0.90]

// Dependencies
Client->Job Posting
Client->Messaging
Freelancer->Bid Submission
Freelancer->Portfolio / Profile
Freelancer->Messaging
Job Posting->Matching Algorithm
Bid Submission->Matching Algorithm
Matching Algorithm->Skills Taxonomy
Matching Algorithm->Reputation & Reviews
Bid Submission->Escrow
Escrow->Payment Processing
Escrow->Dispute Resolution
Payment Processing->FX / Multi-currency
Portfolio / Profile->KYC / Identity
Reputation & Reviews->Database
Messaging->Email / SMS
Job Posting->Cloud Compute
Bid Submission->Cloud Compute
Portfolio / Profile->CDN
Matching Algorithm->Database
KYC / Identity->Auth

evolve Matching Algorithm 0.55
evolve Dispute Resolution 0.50

note Build moat [0.55, 0.25]
note Rent / buy [0.25, 0.88]
```

### Strategic analysis

**Top 3 by D (BUILD):**
1. **Matching Algorithm** (0.62 × 0.65 = 0.40) — platform's core IP.
2. **Dispute Resolution** (0.45 × 0.65 = 0.29) — differentiator that wins repeat custom.
3. **Reputation & Reviews** (0.58 × 0.45 = 0.26) — the moat deepens with history.

**Top 3 by K (BUY / RENT):**
1. **CDN** (0.88 × 0.92 = 0.81), **Cloud Compute** (0.82 × 0.90 = 0.74), **Database** (0.85 × 0.88 = 0.75) — utility infrastructure.

**Top 3 R:**
1. **(Bid Submission, Matching Algorithm)** = 0.80 × 0.65 = 0.52 — core UX depends on immature algorithm.
2. **(Job Posting, Matching Algorithm)** = 0.82 × 0.65 = 0.53 — same fragility.
3. **(Escrow, Dispute Resolution)** = 0.48 × 0.65 = 0.31 — payment trust depends on immature dispute process.

**Suggested gameplays:**
- **#45 Two factor** — the defining play for a two-sided marketplace; both sides reinforce value.
- **#16 Exploiting Network Effects** — matching quality rises with liquidity.
- **#36 Directed investment** — put engineering into Matching and Dispute Resolution (the two highest-D components).
- **#43 Sensing Engines (ILC)** — use platform data to detect adjacent markets to enter.
- **#15 Open Approaches** — consider opening KYC or Skills Taxonomy APIs to build ecosystem.
- **#29 Harvesting** — let Stripe do Payment Processing; let Auth0/Clerk do Auth; harvest the best.

**Doctrine notes:**
- ✓ **#10 Know your users** — two anchors correctly identified.
- ✓ **#45 Two factor** play is the dominant strategic shape.
- ⚠ **#13 Manage inertia** — once reputation history builds, switching cost locks both sides in (inertia forms #2 sunk capital, #14 strategic-control loss).

**Caveat:** Evolution is a scenario, not a forecast.

---

## Example 3 — SaaS Invoicing (build/buy/outsource focus)

**Scenario:** A SaaS for automated invoicing aimed at small businesses. Map components and give build/buy/outsource decisions.

### Map

```owm
title SaaS Invoicing
style wardley

anchor SMB Owner [0.98, 0.55]
anchor Accountant [0.92, 0.60]

// User-facing
component Invoice UI [0.85, 0.55]
component Client Portal [0.78, 0.60]
component Reporting Dashboard [0.75, 0.50]
component Cashflow Forecast [0.68, 0.30]

// Core logic
component Invoice Generation [0.60, 0.60]
component Payment Reminders [0.55, 0.45]
component Late-Payer Scoring (ML) [0.50, 0.25]
component Line-Item OCR [0.48, 0.35]
component Tax Rules Engine [0.45, 0.55]

// Integrations
component Accounting Integration [0.40, 0.70]
component Bank Feeds [0.38, 0.65]
component PEPPOL / E-invoicing [0.35, 0.40]

// Payments
component Payment Processing [0.30, 0.90]
component Card Networks [0.25, 0.92]

// Communications & infra
component Email / SMS [0.25, 0.90]
component Auth [0.22, 0.92]
component Cloud Compute [0.18, 0.90]
component Object Storage [0.15, 0.92]
component Database [0.15, 0.88]
component Observability [0.12, 0.85]

// Knowledge
component Double-entry Bookkeeping [0.08, 0.95]
component Tax Law per Jurisdiction [0.06, 0.60]

// Dependencies
SMB Owner->Invoice UI
SMB Owner->Reporting Dashboard
SMB Owner->Cashflow Forecast
Accountant->Client Portal
Accountant->Reporting Dashboard
Invoice UI->Invoice Generation
Invoice Generation->Tax Rules Engine
Invoice Generation->PEPPOL / E-invoicing
Client Portal->Accounting Integration
Reporting Dashboard->Database
Cashflow Forecast->Late-Payer Scoring (ML)
Cashflow Forecast->Bank Feeds
Payment Reminders->Email / SMS
Late-Payer Scoring (ML)->Database
Line-Item OCR->Object Storage
Tax Rules Engine->Tax Law per Jurisdiction
Tax Rules Engine->Double-entry Bookkeeping
Accounting Integration->Payment Processing
Payment Processing->Card Networks
Bank Feeds->Database
Invoice UI->Cloud Compute
Invoice UI->Auth
Cloud Compute->Observability

evolve PEPPOL / E-invoicing 0.70
evolve Late-Payer Scoring (ML) 0.55
```

### Build / Buy / Outsource table

| Bucket | Components | Rationale |
|---|---|---|
| **BUILD** (differentiation) | Cashflow Forecast, Late-Payer Scoring, Line-Item OCR, Reporting Dashboard, Invoice UI UX | Genesis/Custom — ML + UX is your moat |
| **BUY / RENT** (product) | PEPPOL adapter (Pagero/Storecove), Bank Feeds (Codat/Rutter), Tax Rules (Avalara/Stripe Tax) | Stage III — rent don't build |
| **OUTSOURCE / UTILITY** (commodity) | Payment Processing (Stripe), Email/SMS (Postmark/Twilio), Auth (Clerk/Auth0), Cloud (AWS/GCP), Database, Storage, Observability (Datadog) | Stage IV — treat as utility |
| **LEVERAGE** (knowledge) | Double-entry Bookkeeping, Tax Law | Accepted knowledge — hire experts, don't redevelop |

### Suggested gameplays

- **#36 Directed investment** on Late-Payer Scoring and Cashflow Forecast — the ML moat.
- **#15 Open Approaches** on PEPPOL adapter — accelerate the industry shift; avoid owning the standard.
- **#43 Sensing Engines (ILC)** on Line-Item OCR — watch which vendors emerge, harvest the winner.
- **#29 Harvesting** on Bank Feeds and Accounting Integration — let Codat/Rutter win, then acquire API.
- **#56 First mover** on PEPPOL/ViDA compliance — regulatory deadlines create a narrow window.

### Doctrine notes

- ✓ **#10 Know your users** — two anchors (SMB owner + accountant) correctly represent the real users.
- ⚠ **#2 Use a systematic mechanism of learning** — Late-Payer Scoring should feed training data back from observed outcomes.
- ⚠ **#13 Manage inertia** — as customers accrue history in your cashflow forecasts (sunk capital #2), switching costs build. Use this.

### Inertia watch

From the 17 forms, three dominate:
- **#8 Skill acquisition cost** — SMB owners resist learning new invoicing workflows.
- **#9 Re-architecture cost** — migrating from desktop accounting (Sage, Xero Desktop) to SaaS has high switching cost.
- **#14 Strategic-control loss** — accountants worry about lock-in; offer export/portability.

**Caveat:** All evolution positions are scenarios, not forecasts.
