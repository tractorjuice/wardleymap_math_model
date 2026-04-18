# SaaS Invoicing for Small Businesses — Wardley Map & Strategic Analysis

Scenario: a SaaS for automated invoicing aimed at small businesses. Two user types are treated as anchors — the SMB owner (who creates invoices, chases money, watches cashflow) and the Accountant / bookkeeper (who reconciles, files, and closes books on behalf of multiple SMBs). The map places components, then derives build / buy / outsource calls from their evolution stage and visibility.

---

## 1. Map (OWM format)

```owm
title SaaS Invoicing for Small Businesses
style wardley

// Anchors — two user types
anchor SMB Owner [0.98, 0.55]
anchor Accountant / Bookkeeper [0.93, 0.62]

// User-facing surfaces
component Invoice Creation UI [0.86, 0.55]
component Client Portal (Pay-this-invoice page) [0.80, 0.65]
component Reporting Dashboard [0.76, 0.50]
component Cashflow Forecast [0.70, 0.28]
component Mobile App [0.72, 0.70]

// Core domain logic
component Invoice Generation (templates + numbering) [0.62, 0.60]
component Recurring / Subscription Billing [0.58, 0.55]
component Payment Reminders (dunning) [0.55, 0.50]
component Late-Payer Scoring (ML) [0.50, 0.22]
component Receipt / Line-Item OCR [0.48, 0.30]
component Tax Rules Engine (VAT / GST / sales tax) [0.45, 0.55]
component Multi-currency & FX [0.42, 0.70]

// Integrations (data in/out)
component Accounting Integration (Xero / QBO / Sage) [0.40, 0.70]
component Bank Feeds (open banking) [0.38, 0.65]
component PEPPOL / E-invoicing Network [0.35, 0.45]
component CRM Integration (HubSpot / Pipedrive) [0.32, 0.70]

// Payment rails
component Payment Processing (card + ACH + SEPA) [0.30, 0.90]
component Card Networks / Interchange [0.22, 0.95]
component Direct Debit / Bank Transfer rails [0.25, 0.88]

// Comms + platform utilities
component Transactional Email [0.26, 0.92]
component SMS / WhatsApp delivery [0.24, 0.88]
component Identity / Auth [0.22, 0.92]
component Cloud Compute [0.18, 0.92]
component Object Storage (invoice PDFs) [0.15, 0.93]
component Relational Database [0.14, 0.88]
component Observability / Logging [0.12, 0.88]
component CDN [0.10, 0.93]

// Knowledge layer (Stage IV — accepted; use experts, don't re-derive)
component Double-entry Bookkeeping [0.08, 0.95]
component Tax Law per Jurisdiction [0.06, 0.58]
component E-invoicing Regulation (PEPPOL / ViDA / CTC) [0.05, 0.40]

// Dependencies
SMB Owner->Invoice Creation UI
SMB Owner->Reporting Dashboard
SMB Owner->Cashflow Forecast
SMB Owner->Mobile App
Accountant / Bookkeeper->Reporting Dashboard
Accountant / Bookkeeper->Client Portal (Pay-this-invoice page)
Accountant / Bookkeeper->Accounting Integration (Xero / QBO / Sage)

Invoice Creation UI->Invoice Generation (templates + numbering)
Invoice Creation UI->Receipt / Line-Item OCR
Invoice Creation UI->Identity / Auth
Invoice Creation UI->Cloud Compute
Invoice Creation UI->CDN
Mobile App->Invoice Generation (templates + numbering)
Mobile App->Identity / Auth

Invoice Generation (templates + numbering)->Tax Rules Engine (VAT / GST / sales tax)
Invoice Generation (templates + numbering)->Multi-currency & FX
Invoice Generation (templates + numbering)->PEPPOL / E-invoicing Network
Invoice Generation (templates + numbering)->Object Storage (invoice PDFs)

Recurring / Subscription Billing->Invoice Generation (templates + numbering)
Recurring / Subscription Billing->Payment Processing (card + ACH + SEPA)

Client Portal (Pay-this-invoice page)->Payment Processing (card + ACH + SEPA)
Client Portal (Pay-this-invoice page)->Object Storage (invoice PDFs)

Payment Reminders (dunning)->Transactional Email
Payment Reminders (dunning)->SMS / WhatsApp delivery
Payment Reminders (dunning)->Late-Payer Scoring (ML)

Cashflow Forecast->Late-Payer Scoring (ML)
Cashflow Forecast->Bank Feeds (open banking)
Cashflow Forecast->Relational Database

Late-Payer Scoring (ML)->Relational Database
Late-Payer Scoring (ML)->Bank Feeds (open banking)

Receipt / Line-Item OCR->Object Storage (invoice PDFs)

Tax Rules Engine (VAT / GST / sales tax)->Tax Law per Jurisdiction
Tax Rules Engine (VAT / GST / sales tax)->Double-entry Bookkeeping

PEPPOL / E-invoicing Network->E-invoicing Regulation (PEPPOL / ViDA / CTC)

Accounting Integration (Xero / QBO / Sage)->Relational Database
Bank Feeds (open banking)->Relational Database
CRM Integration (HubSpot / Pipedrive)->Relational Database

Payment Processing (card + ACH + SEPA)->Card Networks / Interchange
Payment Processing (card + ACH + SEPA)->Direct Debit / Bank Transfer rails

Reporting Dashboard->Relational Database
Reporting Dashboard->Cloud Compute

Cloud Compute->Observability / Logging

evolve PEPPOL / E-invoicing Network 0.75
evolve Late-Payer Scoring (ML) 0.50
evolve Receipt / Line-Item OCR 0.55
evolve Bank Feeds (open banking) 0.85

note BUILD (differentiation) [0.65, 0.25]
note BUY / RENT (product) [0.40, 0.65]
note OUTSOURCE / UTILITY [0.18, 0.90]
```

---

## 2. Strategic analysis

### a. Top 3 by differentiation pressure D = ν · (1 − ε)

These are visible to the user AND still immature — the zone where a new entrant can legitimately build a moat.

1. **Cashflow Forecast** — D = 0.70 · (1 − 0.28) = **0.504**. Visible on the SMB owner's home screen; Genesis / Custom Built territory. "Will I make payroll?" is the question an SMB owner actually wakes up at 3am for. Nobody has nailed this; incumbents show static reports.
2. **Late-Payer Scoring (ML)** — D = 0.50 · (1 − 0.22) = **0.390**. The engine that makes the Cashflow Forecast non-trivial. Predicting which invoices slip, by how many days, per customer, from behavioural + payment history. Genesis — models will compound with your data.
3. **Invoice Creation UI** — D = 0.86 · (1 − 0.55) = **0.387**. UX is the most visible surface and is only mid-Product. "Ten seconds from job-done to invoice-sent" still isn't a solved problem on mobile. This is where SMBs pick their tool.

Honourable mentions at the D boundary: **Reporting Dashboard** (0.38), **Receipt / Line-Item OCR** (0.34).

### b. Top 3 by commodity leverage K = (1 − ν) · ε

Deep in the stack AND mature — rent, don't build.

1. **CDN** — K = 0.90 · 0.93 = **0.837**. Cloudflare / Fastly.
2. **Object Storage** — K = 0.85 · 0.93 = **0.791**. S3 / R2 / GCS.
3. **Transactional Email** — K = 0.74 · 0.92 = **0.681**. Postmark, SendGrid, SES.

Also very high: **Cloud Compute** K = 0.75, **Identity / Auth** K = 0.72, **Relational Database** K = 0.76, **Payment Processing** K = 0.63, **SMS / WhatsApp delivery** K = 0.67. All Stage IV (+utility) — treat as metered utilities.

### c. Top 3 dependency risks R = ν(a) · (1 − ε(b))

The visible-thing-sitting-on-fragile-foundation risk.

1. **(Cashflow Forecast → Late-Payer Scoring (ML))** — R = 0.70 · (1 − 0.22) = **0.546**. The headline feature rests entirely on an ML component that is barely past Genesis. Early models will be wrong in public-facing ways. Mitigation: confidence bands on the forecast, label the feature as "beta / improving with your data", gate how much of the UX depends on it.
2. **(Payment Reminders → Late-Payer Scoring (ML))** — R = 0.55 · 0.78 = **0.429**. Automated chasing of the wrong customers destroys relationships. Mitigation: keep a hand-editable override; never auto-escalate without an SMB-owner confirm until the model is production-reliable.
3. **(Invoice Creation UI → Receipt / Line-Item OCR)** — R = 0.86 · (1 − 0.30) = **0.602**. OCR failures happen in the highest-visibility screen. Technically this is the largest R number; the mitigation is design — always let the user fall back to manual entry and never block invoice send on OCR.

Secondary: **(Invoice Generation → PEPPOL / E-invoicing Network)** — R ≈ 0.62 · 0.55 = 0.341. PEPPOL / ViDA is evolving fast with jurisdictional variation; rent an adapter, don't build the network code yourself.

### d. Suggested gameplays (Wardley's 61)

- **#1 Focus on user needs** — two anchors make this concrete: the SMB-owner job ("get paid, don't run out of cash") is distinct from the accountant job ("close the books, file taxes, reconcile"). Every component should map back to one of those.
- **#36 Directed investment** on **Cashflow Forecast + Late-Payer Scoring (ML)**. These are your Top 2 D components; concentrate engineering here, not on re-implementing Stage IV utilities.
- **#37 Experimentation** on the forecast UX. Genesis components need FIRE (fast, inexpensive, restrained, elegant) experiments — small releases, talk to 20 SMBs a month, throw the losers away.
- **#43 Sensing Engines (ILC)** on **Receipt / Line-Item OCR**. The OCR market has several maturing vendors (AWS Textract, Google Document AI, Mindee, Rossum). Instrument usage; harvest the winner, don't marry one early.
- **#29 Harvesting** on **Bank Feeds (open banking)** and **Accounting Integration**. Let Codat / Rutter / Plaid aggregate the long tail; consume their APIs instead of maintaining hundreds of brittle bank and accounting-platform integrations yourself.
- **#15 Open Approaches** on the **PEPPOL / E-invoicing** adapter layer. Publish your connector as open-source — you don't make money owning PEPPOL glue code, you make money on the forecast above it. Open-sourcing accelerates commoditisation of the thing below you and lowers your own maintenance cost.
- **#56 First mover** on **PEPPOL / ViDA / e-invoicing compliance** in jurisdictions with hard deadlines (EU ViDA 2028, various CTC regimes in Italy, Poland, France, LatAm). Regulatory deadlines create a narrow migration window — be the obvious choice during it.
- **#45 Two factor** — recognise this is not purely two-sided, but the accountant is a strong second user type who brings many SMBs per acquisition. Build accountant-specific surface (multi-client dashboard, bulk actions, partner programme) — accountants function like a distribution channel.
- **#33 Raising barriers to entry** on your own moat: once the forecast is good, accumulated per-customer payment history becomes a durable data moat that a new entrant starts from zero on. That data flywheel is the real long-term asset.
- **#30 Standards game** — decide whether to push for open export standards (aligns with doctrine #4 Be transparent and #13 Know the details of switching) or to set a de-facto integration format. For SMB SaaS, erring on open is usually right — SMBs and accountants are trust-sensitive.

### e. Doctrine notes

- ✓ **#1 Focus on user needs** — map anchored on SMB Owner + Accountant, both of whom have genuine, distinct needs.
- ✓ **#10 Know your users** (Phase II) — two anchors with a clear dependency split (SMBs own creation; accountants own reconciliation) reflects the real workflow.
- ✓ **#9 Think small** (Phase I) — components are decomposed to a level where each can be cheat-sheet scored. "Payments" has been split into Processing / Card Networks / Direct Debit; "Cloud" into Compute / Storage / DB / CDN.
- ⚠ **#2 Use a systematic mechanism of learning** — the ML components (Late-Payer Scoring, OCR) must include a feedback loop from observed outcomes (did this customer actually pay late?) back into training data. Bake this in from day one; retrofitting a feedback loop is expensive.
- ⚠ **#13 Manage inertia** (Phase II) — be deliberate about switching costs. Your own forecast history will eventually lock customers in (good for you, bad for them); portability / export (doctrine #4 Be transparent) is the honest counter. Short-term, recognise that SMBs on Xero / QBO / Sage have significant inertia (see the "Inertia watch" below).
- ⚠ **#15 Do better with less** (Phase III) — don't build what you can rent. Every utility you reimplement is engineering capacity not spent on the forecast moat.
- ⚠ **#7 Use appropriate methods** — agile for Cashflow Forecast (Genesis), six-sigma-ish for Payment Processing integration (Stage IV, stability matters). Don't let one methodology rule the whole map.

### f. Climatic context

Patterns actively shaping this map:

- **#3 Everything evolves** — every component on the map will move right. Plan the Genesis components (forecast, OCR) as Product (+rental) by Year 3.
- **#13 Components evolve through supply and demand competition** — the e-invoicing network effect (PEPPOL, ViDA, CTC regimes) is propagating jurisdiction by jurisdiction; each regulatory deadline injects demand-side pressure.
- **#15–17 Inertia patterns** — SMBs on desktop accounting (legacy Sage, older QB Desktop) and accountants with entrenched practice-management software create consumer-side inertia the map must plan around. See the inertia forms called out below.
- **#24 Componentisation accelerates the pace of evolution** — utility-grade Payments, Email, Auth, Cloud have dropped the cost of standing up an invoicing SaaS by an order of magnitude. The entry barrier is lower than ever; differentiation has to live further up-stack.
- **#27 Product-to-utility punctuated equilibrium** — Payment Processing has already crossed; Bank Feeds are crossing now via open banking; e-invoicing networks are crossing via regulation. Each of those is a "war" that reshuffles the competitive landscape.
- **#25 Efficiency enables innovation** — harvesting the utility layer (Stripe, Postmark, AWS) is what frees the capital to do any novel work at the forecast layer.

**Inertia watch** (specific forms from the 17):
- **#8 Skill acquisition cost** — SMB owners resist learning new invoicing workflows even when the new one is better. Keep onboarding under 5 minutes; import from Xero / QBO in one click.
- **#9 Re-architecture cost** — accountants with 200 clients on one incumbent platform face huge switching cost. Migrate-in tooling matters more than feature parity.
- **#14 Strategic-control loss** — accountants are professionally sensitive to lock-in. Offer full export, open formats, data portability (this is also doctrine #4 Be transparent).
- **#7 Supplier-trust concerns** — financial SaaS lives or dies on trust. SOC 2, ISO 27001, clear data-handling posture, named regulatory compliance (ViDA, PEPPOL, local e-invoicing) are a cost of entry, not a nice-to-have.

### g. Caveat

Evolution trajectories on this map — and the specific evolve arrows (PEPPOL to 0.75, Late-Payer Scoring to 0.50, OCR to 0.55, Bank Feeds to 0.85) — are **scenarios, not forecasts**. Wardley's climatic pattern: *"you cannot measure evolution over time or adoption."* Re-score against the cheat sheet every 6–12 months and when a major signal fires (a utility-grade OCR launch from a hyperscaler; a new CTC mandate in a target jurisdiction; a bank-feed aggregator being acquired). The D / K / R numbers are heuristics proposed by this skill's math model, not canonical Wardley metrics — treat them as attention prompts, not verdicts.

---

## 3. Build / Buy / Outsource summary

| Bucket | Components | Why |
|---|---|---|
| **BUILD** — your moat, concentrate engineering here | Cashflow Forecast; Late-Payer Scoring (ML); Invoice Creation UI & Mobile App UX; Reporting Dashboard; the accountant multi-client surface on the Client Portal | Genesis / Custom Built; highest D; the data flywheel compounds with usage |
| **BUY / RENT** — Stage III products, rent an adapter, don't reinvent | Accounting Integration (Codat / Rutter); Bank Feeds (open-banking aggregators); PEPPOL / e-invoicing network adapter (Pagero / Storecove / Tradeshift); Tax Rules (Avalara / Stripe Tax / TaxJar); CRM integration SaaS; OCR API (harvest the winner of AWS Textract / Google Document AI / Mindee / Rossum via #43 Sensing Engines) | Stage III; multiple competing vendors; renting preserves optionality |
| **OUTSOURCE / UTILITY** — Stage IV commodities, treat as metered tap | Payment Processing (Stripe / Adyen); Transactional Email (Postmark / SES); SMS & WhatsApp (Twilio / MessageBird); Identity / Auth (Clerk / Auth0 / WorkOS); Cloud Compute (AWS / GCP); Object Storage (S3 / R2); Relational Database (RDS / Cloud SQL / Neon); CDN (Cloudflare / Fastly); Observability (Datadog / Honeycomb) | Stage IV (+utility); reimplementing any of these is capital destruction |
| **LEVERAGE** — Knowledge layer, hire experts, don't re-derive | Double-entry Bookkeeping; Tax Law per Jurisdiction; E-invoicing Regulation (PEPPOL / ViDA / CTC) | Stage IV accepted knowledge (bookkeeping) or externally-governed regulatory knowledge — retain specialist advisers, don't re-derive |

If you take nothing else from the map: **build the forecast, rent the integrations, outsource the rails**. The forecast is where small-business SaaS can still win; the rest is already commoditised and you waste your runway if you build it yourself.
