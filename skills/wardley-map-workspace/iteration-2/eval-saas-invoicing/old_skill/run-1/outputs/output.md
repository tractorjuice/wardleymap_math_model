# Wardley Map: SaaS for Automated Invoicing (Small Business)

Scenario: A SaaS product for automated invoicing aimed at small businesses — generate and send invoices, track payments, chase late payers, reconcile payments, and handle basic tax/VAT. Two clear user types: **Small Business Owner** (creates/sends invoices, wants to get paid) and **Customer / Payer** (receives invoice, pays).

---

## 1. Components (V) and anchors (U)

Anchors:
- **Small Business Owner** — wants "get paid quickly with minimal admin"
- **Customer / Payer** — wants "easy, trustworthy way to pay this bill"

Activities, Practices, Data, Knowledge:

- Invoice Creation UI
- Invoice Templates / Branding
- Recurring Invoices / Subscriptions
- Automated Payment Reminders (dunning)
- Payment Acceptance (card / bank / ACH / SEPA)
- Payment Reconciliation
- Tax / VAT Calculation
- Tax Filing Integrations (e.g. HMRC MTD, IRS, etc.)
- Accounting Software Integrations (Xero, QuickBooks, Sage)
- CRM / Customer Records
- Email Delivery (transactional)
- SMS / WhatsApp Notifications
- Customer Portal (to view + pay)
- Multi-currency FX
- Credit Risk / Late-Payer Scoring (ML)
- Fraud / AML Screening
- Authentication & Identity
- Billing Data Store
- Audit Log / Compliance Evidence
- Application Hosting / Compute
- Object Storage (PDFs, attachments)
- Relational Database
- Analytics / BI for SMB (cashflow dashboard)
- Practice: Double-entry bookkeeping
- Knowledge: Tax rules per jurisdiction

---

## 2. OWM Output

```owm
title SaaS for Automated Invoicing (Small Business)
style wardley

// Anchors — two user types
anchor Small Business Owner [0.98, 0.72]
anchor Customer / Payer [0.98, 0.80]

// Visible user-facing activities (high ν)
component Invoice Creation UI [0.90, 0.62]
component Customer Portal [0.88, 0.70]
component Cashflow Dashboard [0.86, 0.55]
component Automated Payment Reminders [0.84, 0.60]
component Recurring Invoices [0.82, 0.62]
component Late-Payer Scoring (ML) [0.80, 0.30]
component Invoice Templates & Branding [0.78, 0.78]

// Mid-layer: domain logic + integrations
component Tax / VAT Calculation [0.70, 0.55]
component Tax Filing Integrations [0.68, 0.45]
component Accounting Integrations [0.68, 0.72]
component Payment Reconciliation [0.66, 0.58]
component CRM / Customer Records [0.64, 0.70]
component Multi-currency FX [0.58, 0.75]
component Credit Risk & Fraud Screening [0.56, 0.65]

// Lower-mid: shared mechanics
component Billing Data Store [0.48, 0.55]
component Audit Log / Compliance Evidence [0.46, 0.60]
component Authentication & Identity [0.42, 0.85]

// Commodity utility layer (low ν, high ε)
component Payment Acceptance (Stripe/Adyen) [0.38, 0.88]
component Email Delivery [0.32, 0.90]
component SMS / WhatsApp Notifications [0.30, 0.88]
component Object Storage [0.22, 0.92]
component Relational Database [0.20, 0.90]
component Application Hosting / Compute [0.18, 0.92]

// Practices and knowledge
component Double-entry Bookkeeping (practice) [0.55, 0.90]
component Tax Rules per Jurisdiction (knowledge) [0.60, 0.55]

// Dependencies (A -> B means A depends on B)
Small Business Owner->Invoice Creation UI
Small Business Owner->Cashflow Dashboard
Small Business Owner->Recurring Invoices
Small Business Owner->Automated Payment Reminders
Small Business Owner->Accounting Integrations
Small Business Owner->Tax Filing Integrations

Customer / Payer->Customer Portal
Customer / Payer->Invoice Templates & Branding

Invoice Creation UI->Invoice Templates & Branding
Invoice Creation UI->Tax / VAT Calculation
Invoice Creation UI->Billing Data Store
Invoice Creation UI->CRM / Customer Records
Invoice Creation UI->Authentication & Identity

Customer Portal->Payment Acceptance (Stripe/Adyen)
Customer Portal->Billing Data Store
Customer Portal->Authentication & Identity

Cashflow Dashboard->Payment Reconciliation
Cashflow Dashboard->Billing Data Store
Cashflow Dashboard->Late-Payer Scoring (ML)

Automated Payment Reminders->Email Delivery
Automated Payment Reminders->SMS / WhatsApp Notifications
Automated Payment Reminders->CRM / Customer Records
Automated Payment Reminders->Late-Payer Scoring (ML)

Recurring Invoices->Billing Data Store
Recurring Invoices->Payment Acceptance (Stripe/Adyen)

Late-Payer Scoring (ML)->Billing Data Store
Late-Payer Scoring (ML)->CRM / Customer Records

Tax / VAT Calculation->Tax Rules per Jurisdiction (knowledge)
Tax / VAT Calculation->Billing Data Store
Tax Filing Integrations->Tax Rules per Jurisdiction (knowledge)
Tax Filing Integrations->Billing Data Store

Accounting Integrations->Billing Data Store
Accounting Integrations->Double-entry Bookkeeping (practice)

Payment Reconciliation->Payment Acceptance (Stripe/Adyen)
Payment Reconciliation->Billing Data Store
Payment Reconciliation->Double-entry Bookkeeping (practice)

CRM / Customer Records->Billing Data Store
Multi-currency FX->Payment Acceptance (Stripe/Adyen)
Credit Risk & Fraud Screening->CRM / Customer Records
Credit Risk & Fraud Screening->Billing Data Store

Billing Data Store->Relational Database
Billing Data Store->Object Storage
Audit Log / Compliance Evidence->Object Storage
Audit Log / Compliance Evidence->Relational Database
Authentication & Identity->Relational Database

Payment Acceptance (Stripe/Adyen)->Application Hosting / Compute
Email Delivery->Application Hosting / Compute
SMS / WhatsApp Notifications->Application Hosting / Compute
Relational Database->Application Hosting / Compute
Object Storage->Application Hosting / Compute

// Evolve hints (scenario, not forecast)
evolve Late-Payer Scoring (ML) 0.60
evolve Tax Filing Integrations 0.70
evolve Cashflow Dashboard 0.70

// Inertia to watch
component Double-entry Bookkeeping (practice) [0.55, 0.90] inertia

note Build differentiators here [0.90, 0.30]
note Buy / rent the middle [0.60, 0.60]
note Outsource the utility floor [0.20, 0.92]
```

---

## 3. Strategic Analysis

### a. Top 3 by differentiation pressure D(v) = ν · (1 − ε)

Visible + immature = where to **build** proprietary capability.

| Rank | Component | ν | ε | D | Why |
|---|---|---|---|---|---|
| 1 | **Late-Payer Scoring (ML)** | 0.80 | 0.30 | **0.56** | User-visible outcome ("will I get paid?"), still Custom-Built stage for SMB segment; a specialist ML edge here is defensible and directly tied to user need. |
| 2 | **Cashflow Dashboard** | 0.86 | 0.55 | **0.39** | Main thing the owner opens each morning; product-stage but with room to differentiate on predictive cashflow vs. basic reports. |
| 3 | **Automated Payment Reminders (dunning)** | 0.84 | 0.60 | **0.34** | Direct lever on DSO; tone, timing, channel mix (email/SMS/WhatsApp) are not yet standard — beats generic "send reminder" competitors. |

**Recommendation: BUILD these.** They are the product.

### b. Top 3 by commodity leverage K(v) = (1 − ν) · ε

Deep + mature = where to **buy / rent** utility services.

| Rank | Component | ν | ε | K | Why |
|---|---|---|---|---|---|
| 1 | **Application Hosting / Compute** | 0.18 | 0.92 | **0.75** | AWS / GCP / Azure; no rational reason to build this. |
| 2 | **Relational Database** | 0.20 | 0.90 | **0.72** | Managed Postgres (RDS / Cloud SQL / Neon). |
| 3 | **Object Storage** | 0.22 | 0.92 | **0.72** | S3 / GCS. Also: **Payment Acceptance** (K ≈ 0.55) — use Stripe / Adyen; **Email Delivery** (K ≈ 0.61) — use SES / Postmark. |

**Recommendation: BUY / RENT these as utility.** Burning engineering budget on them is doctrine #27 ("Do better with less") violation.

Near-miss but strong candidates for **OUTSOURCE** (third-party SaaS API, not utility cloud):
- **Tax / VAT Calculation** — use Avalara / Stripe Tax / Anrok; tax rules are Knowledge you do not want to maintain yourself.
- **Credit Risk & Fraud Screening** — Stripe Radar / Sift.
- **SMS / WhatsApp Notifications** — Twilio / MessageBird.

### c. Top 3 dependency risks R(a, b) = ν(a) · (1 − ε(b))

Visible components resting on an immature or fragile foundation.

| Rank | Edge (a → b) | ν(a) | ε(b) | R | Why it's risky |
|---|---|---|---|---|---|
| 1 | **Cashflow Dashboard → Late-Payer Scoring (ML)** | 0.86 | 0.30 | **0.60** | Your most-used user surface leans on a Custom-Built ML model. Accuracy regressions are directly visible to the owner. Mitigate: set confidence thresholds, fall back to heuristics, SLO the model. |
| 2 | **Automated Payment Reminders → Late-Payer Scoring (ML)** | 0.84 | 0.30 | **0.59** | Bad scoring = harassing good customers or missing late ones. Same mitigation plus human-in-the-loop overrides. |
| 3 | **Small Business Owner → Tax Filing Integrations** | 0.98 | 0.45 | **0.54** | Filing wrong = fines, licence loss. Custom-Built integrations per jurisdiction are a long tail of fragility. Mitigate: **outsource** to a specialist tax engine (Avalara / Stripe Tax) and treat filing as a service, not a feature. |

### d. Suggested Wardley gameplays (named from the 61-play catalogue)

- **#1 Focus on user needs** — anchor every roadmap choice on the two anchors (Owner: get paid; Payer: pay easily). Most SMB invoicing tools over-index on accountants.
- **#15 Open Approaches** — publish an **open API** for invoice/payment events to lock in accounting and banking integrators. Targets: *Accounting Integrations*, *Billing Data Store*.
- **#16 Exploiting Network Effects (Two-factor)** — every invoice sent surfaces the product to a Payer who may become an Owner. Targets: *Customer Portal*, *Invoice Templates & Branding*.
- **#41 Alliances** — partner with Stripe, Xero, QuickBooks rather than compete with them. Targets: *Payment Acceptance*, *Accounting Integrations*.
- **#43 Sensing Engines (ILC)** — Innovate-Leverage-Commoditise: watch consumption patterns in *Late-Payer Scoring* and *Cashflow Dashboard*; commoditise the winners into API endpoints.
- **#26 Differentiation** — make *Late-Payer Scoring* the visible brand promise ("we get you paid 8 days faster").
- **#56 First mover / #57 Fast follower** — be first mover on AI-native invoicing assistant features; fast follower on commodity tax filing.
- **#17 Co-operation** + **#30 Standards game** — adopt **e-invoicing standards** (Peppol, UBL) early so you ride regulatory tailwinds rather than fight them.
- **#7 Education** — SMB owners resist changing accounting habits (doctrine inertia); short in-app guidance reduces churn.

### e. Doctrine violations / risks to watch

Cross-referenced against Wardley's 40 principles:

- **Doctrine #1 Focus on user needs** — satisfied (two anchors named), but beware that the SMB *Owner* need ("get paid") is not the same as the *Accountant* need ("clean books"). A third anchor may emerge.
- **Doctrine #10 Know your users** — small-business segment is broad (freelancer vs. 20-person shop); sub-segmentation is needed before scaling.
- **Doctrine #12 Use appropriate tools** — violated if the team builds its own hosting, DB, email, payments. Those are utility — rent them.
- **Doctrine #22 Use standards where appropriate** — adopt Peppol / UBL / ISO 20022 rather than a bespoke invoice schema.
- **Doctrine #13 Manage inertia** — expected forms from `inertia.md`:
  - #6 Confusion over method ("isn't this just QuickBooks?") — counter with clear positioning.
  - #8 Skill acquisition cost — SMB owners don't want to learn a new tool; minimise onboarding friction.
  - #16 Rewards and culture (internal) — if the team grew up building everything, they'll resist outsourcing tax/payments/hosting.
- **Knowledge layer** is currently light. *Tax Rules per Jurisdiction* is the only explicit Knowledge node; add **SMB payment behaviour models** and **regulatory change-tracking** as the product matures. Doctrine #2 (systematic learning) applies.

### f. Build / Buy / Outsource summary

| Decision | Components |
|---|---|
| **BUILD** (differentiators) | Late-Payer Scoring (ML), Cashflow Dashboard, Automated Payment Reminders logic, Invoice Creation UX, Customer Portal UX |
| **BUY / rent as product** | Accounting Integrations (via partner SDKs), CRM (optional: embed HubSpot / build light), Analytics tooling internally |
| **OUTSOURCE to specialist API** | Payment Acceptance (Stripe / Adyen), Tax / VAT Calculation (Avalara / Stripe Tax / Anrok), Email (SES / Postmark), SMS / WhatsApp (Twilio), Fraud (Stripe Radar / Sift), Authentication (Auth0 / Clerk / WorkOS), Multi-currency FX (via payment provider) |
| **UTILITY (rent from cloud)** | Hosting / Compute, Relational DB, Object Storage |

### g. Caveat

Evolution positions on this map are **a snapshot judgment**, not a forecast. Per Wardley's climatic pattern, *"you cannot measure evolution over time or adoption."* The `evolve` arrows are **scenarios** of plausible movement, not predictions. Re-map when market conditions change — especially if a large player commoditises ML-based collections or if e-invoicing regulation (Peppol / ViDA) shifts tax filing further right.

The derived metrics D, K, R are **heuristics** proposed by this skill's math model, not canonical Wardley concepts — treat them as attention prompts, not scores.
