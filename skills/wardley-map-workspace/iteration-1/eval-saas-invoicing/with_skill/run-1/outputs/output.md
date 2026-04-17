# Wardley Map: Automated Invoicing SaaS for Small Businesses

## OWM Map

```owm
title Automated Invoicing SaaS for Small Businesses
style wardley

// Anchors — two user types
anchor Small Business Owner [0.98, 0.55]
anchor Small Business Accountant [0.95, 0.60]

// Visible value proposition
component Automated Invoice Generation [0.88, 0.40]
component Recurring / Subscription Billing [0.85, 0.45]
component Payment Reminders & Dunning [0.83, 0.38]
component Tax & VAT Calculation [0.82, 0.70]
component Client / Customer Portal [0.80, 0.55]
component Mobile App [0.78, 0.65]
component Multi-Currency Support [0.76, 0.68]

// Core product capabilities
component Invoice Template Engine [0.70, 0.55]
component Onboarding & Setup Wizard [0.72, 0.45]
component Reporting & Dashboards [0.68, 0.60]
component Bookkeeping / GL Sync [0.66, 0.65]
component AI Line-Item Extraction (OCR) [0.64, 0.30]
component Cashflow Forecast AI [0.62, 0.20]
component Fraud / Duplicate Detection [0.60, 0.40]

// Data
component Customer Data [0.58, 0.55]
component Invoice Ledger Data [0.56, 0.65]
component Tax Rate Data [0.54, 0.80]
component Chart of Accounts Data [0.52, 0.70]

// Integration / partner layer
component Accounting Software Integrations [0.50, 0.70]
component Bank Feed Integration [0.48, 0.75]
component CRM Integration [0.46, 0.60]
component E-Invoicing Network (Peppol) [0.44, 0.55]

// Payments layer
component Payment Processing [0.42, 0.85]
component ACH / Direct Debit Rails [0.40, 0.82]
component Card Network Rails [0.38, 0.92]
component KYC / AML [0.36, 0.80]

// Communications
component Transactional Email [0.34, 0.88]
component SMS Gateway [0.32, 0.88]
component Push Notifications [0.30, 0.85]

// Platform / engineering
component Identity & SSO [0.28, 0.82]
component Auth (OAuth2 / OIDC) [0.26, 0.90]
component API Gateway [0.24, 0.85]
component Application Runtime / Containers [0.22, 0.88]
component Relational Database (Postgres) [0.20, 0.90]
component Object Storage [0.18, 0.93]
component Message Queue [0.16, 0.88]
component CDN [0.14, 0.95]
component Observability (Logs/Metrics/Traces) [0.12, 0.85]
component Cloud Compute [0.10, 0.95]
component Networking [0.08, 0.95]
component Electricity [0.05, 0.98]

// Knowledge / practice
component Tax Regulation Knowledge [0.50, 0.55]
component GAAP / IFRS Accounting Practice [0.48, 0.82]
component PCI-DSS Compliance Practice [0.32, 0.85]
component SOC2 / ISO27001 Practice [0.30, 0.80]
component GDPR / Data Protection Practice [0.34, 0.82]

// Dependencies — user-facing
Small Business Owner->Automated Invoice Generation
Small Business Owner->Recurring / Subscription Billing
Small Business Owner->Payment Reminders & Dunning
Small Business Owner->Client / Customer Portal
Small Business Owner->Mobile App
Small Business Owner->Reporting & Dashboards
Small Business Owner->Tax & VAT Calculation
Small Business Owner->Multi-Currency Support
Small Business Accountant->Bookkeeping / GL Sync
Small Business Accountant->Reporting & Dashboards
Small Business Accountant->Tax & VAT Calculation
Small Business Accountant->Invoice Ledger Data

// Product → core capabilities
Automated Invoice Generation->Invoice Template Engine
Automated Invoice Generation->AI Line-Item Extraction (OCR)
Automated Invoice Generation->Customer Data
Automated Invoice Generation->Invoice Ledger Data
Recurring / Subscription Billing->Invoice Ledger Data
Recurring / Subscription Billing->Payment Processing
Payment Reminders & Dunning->Transactional Email
Payment Reminders & Dunning->SMS Gateway
Payment Reminders & Dunning->Invoice Ledger Data
Tax & VAT Calculation->Tax Rate Data
Tax & VAT Calculation->Tax Regulation Knowledge
Client / Customer Portal->Identity & SSO
Client / Customer Portal->Payment Processing
Mobile App->Push Notifications
Mobile App->API Gateway
Multi-Currency Support->Tax Rate Data
Multi-Currency Support->Payment Processing

Invoice Template Engine->Object Storage
Onboarding & Setup Wizard->Identity & SSO
Onboarding & Setup Wizard->Chart of Accounts Data
Reporting & Dashboards->Invoice Ledger Data
Reporting & Dashboards->Observability (Logs/Metrics/Traces)
Bookkeeping / GL Sync->Accounting Software Integrations
Bookkeeping / GL Sync->Chart of Accounts Data
AI Line-Item Extraction (OCR)->Object Storage
AI Line-Item Extraction (OCR)->Cloud Compute
Cashflow Forecast AI->Invoice Ledger Data
Cashflow Forecast AI->Bank Feed Integration
Fraud / Duplicate Detection->Invoice Ledger Data

// Data dependencies
Customer Data->Relational Database (Postgres)
Invoice Ledger Data->Relational Database (Postgres)
Tax Rate Data->Relational Database (Postgres)
Chart of Accounts Data->Relational Database (Postgres)

// Integrations
Accounting Software Integrations->API Gateway
Bank Feed Integration->API Gateway
CRM Integration->API Gateway
E-Invoicing Network (Peppol)->API Gateway

// Payments
Payment Processing->Card Network Rails
Payment Processing->ACH / Direct Debit Rails
Payment Processing->KYC / AML
Payment Processing->PCI-DSS Compliance Practice

// Platform
Identity & SSO->Auth (OAuth2 / OIDC)
Auth (OAuth2 / OIDC)->API Gateway
API Gateway->Application Runtime / Containers
Application Runtime / Containers->Cloud Compute
Relational Database (Postgres)->Cloud Compute
Object Storage->Cloud Compute
Message Queue->Cloud Compute
CDN->Networking
Observability (Logs/Metrics/Traces)->Cloud Compute
Cloud Compute->Electricity
Networking->Electricity

// Communications
Transactional Email->API Gateway
SMS Gateway->API Gateway
Push Notifications->API Gateway

// Knowledge / practice wiring
Tax & VAT Calculation->Tax Regulation Knowledge
Bookkeeping / GL Sync->GAAP / IFRS Accounting Practice
Customer Data->GDPR / Data Protection Practice
Invoice Ledger Data->GDPR / Data Protection Practice
Payment Processing->PCI-DSS Compliance Practice
Identity & SSO->SOC2 / ISO27001 Practice

// Transition candidates — forecast direction (scenario, not forecast)
evolve AI Line-Item Extraction (OCR) 0.70
evolve Cashflow Forecast AI 0.55
evolve E-Invoicing Network (Peppol) 0.82
evolve Tax & VAT Calculation 0.85
evolve Bookkeeping / GL Sync 0.82

// Pipeline — Payment Processing spans rental products to true utility
pipeline Payment Processing [0.70, 0.95]

// Notes
note Regulated E-Invoicing (EU Peppol, LATAM CFDI) is industrialising fast [0.42, 0.56]
note Build differentiation in the visible, immature AI layer [0.65, 0.22]
note Buy / rent the platform layer — do not self-host [0.14, 0.90]
```

---

## Strategic Analysis

Scoring note: D(v) = ν(v)·(1-ε(v)), K(v) = (1-ν(v))·ε(v), R(a,b) = ν(a)·(1-ε(b)). All values rounded.

### a. Top 3 by Differentiation Pressure D — BUILD

| Component | ν | ε | D | Reasoning |
|---|---|---|---|---|
| Cashflow Forecast AI | 0.62 | 0.20 | 0.50 | Highly visible to owners (cash is the #1 SMB pain), still in Custom Built / early Product. Few SMB-grade solutions that combine invoice data, bank feeds, and AR aging. Genuine moat possible if the model improves with use. |
| AI Line-Item Extraction (OCR) | 0.64 | 0.30 | 0.45 | Visible in "snap a supplier invoice" flows. Commercial OCR exists but small-business accuracy on messy receipts is still a differentiator; improves the onboarding & dunning loops. |
| Automated Invoice Generation | 0.88 | 0.40 | 0.53 | The headline user need. Product-stage but your template engine, auto-send rules, and AI-assisted drafting are where perception of "it just works" is earned. |

**Verdict: BUILD** these three. They are the reason a small business chooses you over FreshBooks / Wave / Xero.

### b. Top 3 by Commodity Leverage K — BUY / RENT

| Component | ν | ε | K | Reasoning |
|---|---|---|---|---|
| Cloud Compute | 0.10 | 0.95 | 0.86 | True utility. Rent from AWS/GCP/Azure/Fly. Do not operate hardware. |
| Card Network Rails | 0.38 | 0.92 | 0.57 | Commodity + utility, but regulated. Use Stripe / Adyen / Checkout.com. Never build a card acquirer. |
| Transactional Email | 0.34 | 0.88 | 0.58 | Postmark / SendGrid / Resend / SES. Deliverability is a black art — outsource. |

**Also clearly buy/rent:** Object Storage (K=0.76), CDN (K=0.82), SMS Gateway (K=0.60), Auth/OIDC (K=0.67), Observability (K=0.75), Relational DB managed (K=0.72), KYC/AML (K=0.51).

**Verdict: BUY/RENT.** Every hour spent on these is an hour not spent on D-list differentiators.

### c. Top 3 Dependency Risks R — the fragile edges

| Edge (a depends on b) | ν(a) | ε(b) | R | Why it matters |
|---|---|---|---|---|
| Cashflow Forecast AI -> Bank Feed Integration | 0.62 | 0.75 | 0.16 | Headline feature depends on aggregators (Plaid, TrueLayer, Tink). Pricing and coverage volatility, regional gaps. Mitigate with second-sourcing. |
| Automated Invoice Generation -> AI Line-Item Extraction (OCR) | 0.88 | 0.30 | 0.62 | The most visible component depends on a Genesis/Custom-Built capability. If OCR misreads, users see it. High visibility · low maturity = exposure. |
| Tax & VAT Calculation -> Tax Regulation Knowledge | 0.82 | 0.55 | 0.37 | Tax law changes (e-invoicing mandates in EU/LATAM/India). A missed rule update becomes a compliance incident for every customer. |

**Honourable mention — outsource risk:** Payment Processing is low-ν but a Stripe outage is user-visible. Treat as a strategic-control-loss inertia risk (inertia #14).

### d. Suggested Gameplays (named from Wardley's 61)

| # | Gameplay | Target component(s) | How |
|---|---|---|---|
| 1 | **Focus on user needs** | Anchors | Keep "get paid faster" and "close the books in under an hour" as the only North-Star metrics. |
| 56 | **First mover** | Cashflow Forecast AI, AI Line-Item Extraction | The AI layer is still Genesis/Custom. Grab it before accounting incumbents bolt it on. |
| 15 | **Open Approaches** | E-Invoicing Network (Peppol), Accounting Software Integrations | Publish open APIs / webhook SDKs; Peppol is standards-driven anyway. |
| 30 | **Standards game** | E-Invoicing Network, Tax & VAT Calculation | Align early with EU Peppol, Brazil NF-e, India GSTN. Compliance as moat. |
| 41 | **Alliances** | Bank Feed Integration, Accounting Software Integrations | Formal partnerships with Plaid/TrueLayer and Xero/QuickBooks App Store. |
| 43 | **Sensing Engines (ILC)** | Entire product | Instrument feature usage; commoditise winners back into the core plan, innovate above. |
| 16 | **Exploiting Network Effects** | Client / Customer Portal, E-Invoicing Network | Every invoice sent exposes a recipient — two-sided pull. |
| 45 | **Two factor** | Client / Customer Portal | Bring the payer (your user's customer) onto the platform; become the rails between them. |
| 26 | **Differentiation** | Automated Invoice Generation, Cashflow Forecast AI | Visible, user-perceived differences (AI drafting, cash-forecast widget on home). |
| 17 | **Co-operation** | KYC/AML, Payment Processing | Piggy-back on Stripe's regulatory perimeter; don't build your own. |
| 23 | **Disposal of liability** | Card Network Rails, Payment Processing, Hosting | Keep these off your balance sheet and off your SOC2 scope where possible. |
| 29 | **Harvesting** | OSS template libraries, OCR models | Let the ecosystem develop; productise the winners (open-weights OCR etc.). |
| 33 | **Raising barriers to entry** | SOC2/ISO27001, PCI-DSS, Tax Regulation Knowledge | Compliance hurts you less than a late entrant — lean into it. |
| 7 | **Education** | Bookkeeping / GL Sync, Onboarding | SMB owners aren't accountants; teach the workflow, reduce skill-acquisition inertia (inertia #8). |

### Build / Buy / Outsource summary

- **BUILD (custom, your IP):** Automated Invoice Generation, Recurring Billing logic, Payment Reminders / Dunning engine, Client Portal, Reporting & Dashboards, AI Line-Item OCR model + wrappers, Cashflow Forecast AI, Fraud / Duplicate Detection, Onboarding Wizard, Invoice Template Engine.
- **BUY / LICENSE (product, renewable):** Tax & VAT Calculation (Avalara / Stripe Tax / Fonoa), Accounting Software connectors (Codat / Rutter), Bank Feeds (Plaid / TrueLayer / Tink — second-sourced), CRM connectors (native APIs), E-invoicing network connector (Storecove / Tickstar / Pagero).
- **OUTSOURCE / UTILITY:** Payment Processing (Stripe / Adyen), Card rails, ACH, KYC/AML (Stripe Identity / Persona / Onfido), Transactional Email (Postmark / Resend), SMS (Twilio / MessageBird), Push (FCM / APNs), Auth (Auth0 / WorkOS / Clerk), Cloud compute + DB + storage + CDN + observability (AWS/GCP + Datadog or equivalent).
- **PARTNER:** Xero / QuickBooks / Sage app stores, Peppol access points, banks for embedded invoicing.

### e. Doctrine Violations / Risks to Flag

Mapped against Wardley's 40 doctrine principles:

- **#1 Focus on user needs** — Two anchors are modelled (owner + accountant). Consider a third (the *payer* — your user's customer) since a portal that makes paying frictionless drives the whole flywheel. Currently underspecified.
- **#10 Know your users** — "Small business" is broad (solo freelancer vs 20-person agency vs micro-retailer). Segment before building; the D-list changes.
- **#13 Manage inertia** — Migrating from spreadsheets / Xero incurs inertia #6 (confusion over method), #8 (skill acquisition), #9 (re-architecture of chart of accounts). Plan migration tools, not just imports.
- **#22 Use standards where appropriate** — Non-negotiable: Peppol, ISO 20022, OFX, OAuth2/OIDC, OpenAPI. Do not invent proprietary invoice formats.
- **#7 Use appropriate methods** — Pioneer-Settler-Town-Planner split: Pioneers on Cashflow AI/OCR, Settlers on core billing, Town Planners on the platform-rental glue.
- **#14 Manage failure** — Payment-processor outages and bank-feed breakages *will* happen. Design degraded modes (queue invoices, manual reconcile).
- **Underspecified Knowledge layer** — Tax Regulation and GAAP/IFRS are modelled but thin. For a global play you need a living knowledge base per jurisdiction; this is where Avalara/Fonoa earn their fee (buy, don't build).

### f. Caveat

Evolution positions here are scenarios, not forecasts. Wardley's climatic pattern: *"you cannot measure evolution over time or adoption."* In particular:

- The AI components (OCR, Cashflow Forecast) could jump one whole stage in 12–18 months if foundation-model pricing continues to fall — re-map quarterly.
- E-invoicing's industrialisation pace is legislation-driven and uneven by country (EU Peppol, Brazil NF-e, India GSTN, Malaysia, Poland KSeF). Your ε estimate for it depends on which market you enter first.
- "Build" recommendations assume you have a small high-quality team; if not, the D-list collapses and you should narrow to one differentiator (most likely Cashflow Forecast AI) and buy everything else.

Re-map when: you pick a launch geography, close a seed round (strategy shifts from land-grab to defensible moat), or a major incumbent (Stripe, Intuit, Xero) announces an adjacent AI feature.
