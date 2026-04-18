# SaaS Invoicing for Small Businesses — Wardley Map & Build/Buy/Outsource Analysis

**Scenario:** A SaaS product for automated invoicing aimed at small businesses (SMBs). Users: the SMB owner/operator who raises invoices and chases payment, and the SMB's accountant who reviews books and handles compliance. Goal: produce a Wardley Map, decide what to build, buy, or outsource, and flag the strategic moves.

---

## 1. Components and anchors

Two anchors (this is a two-user-type business, per doctrine #10 Know your users):

- **SMB Owner** — wants to get paid fast with minimum effort.
- **Accountant** — wants clean books, compliant filings, auditable records.

Components grouped by layer:

- **User-facing:** Invoice UI, Client/Customer Portal, Reporting Dashboard, Cashflow Forecast, Mobile Capture
- **Core invoicing logic:** Invoice Generation, Recurring Billing, Payment Reminders, Late-Payer Scoring (ML), Line-Item OCR, Tax Rules Engine, Credit Notes & Refunds
- **Integrations:** Accounting Integration (Xero/QuickBooks), Bank Feeds, PEPPOL / E-invoicing Adapter, Webhooks
- **Payments:** Payment Processing, Card Networks, Direct Debit / SEPA, FX / Multi-currency
- **Comms & identity:** Email / SMS, Auth, KYC / AML
- **Infrastructure:** Cloud Compute, Object Storage, Database, Observability, CDN
- **Knowledge layer:** Double-entry Bookkeeping, Tax Law per Jurisdiction, e-invoicing standards (EN-16931)

---

## 2. OWM Map

```owm
title SaaS Invoicing for SMBs
style wardley

// Anchors (two user types per doctrine #10)
anchor SMB Owner [0.98, 0.55]
anchor Accountant [0.93, 0.60]

// User-facing
component Invoice UI [0.88, 0.55]
component Client Portal [0.82, 0.60]
component Mobile Capture [0.78, 0.45]
component Reporting Dashboard [0.76, 0.50]
component Cashflow Forecast [0.70, 0.28]

// Core logic
component Invoice Generation [0.62, 0.60]
component Recurring Billing [0.60, 0.65]
component Payment Reminders [0.55, 0.48]
component Credit Notes & Refunds [0.52, 0.62]
component Late-Payer Scoring (ML) [0.50, 0.30]
component Line-Item OCR [0.48, 0.55]
component Tax Rules Engine [0.45, 0.65]

// Integrations
component Accounting Integration [0.40, 0.70]
component Bank Feeds [0.38, 0.75]
component PEPPOL / E-invoicing Adapter [0.36, 0.62]
component Webhooks [0.34, 0.85]
component KYC / AML [0.32, 0.82]

// Payments
component Payment Processing [0.28, 0.92]
component Direct Debit / SEPA [0.26, 0.88]
component FX / Multi-currency [0.24, 0.80]
component Card Networks [0.22, 0.95]

// Comms & infra
component Email / SMS [0.22, 0.92]
component Auth [0.20, 0.92]
component Observability [0.15, 0.88]
component Object Storage [0.14, 0.92]
component Database [0.13, 0.90]
component Cloud Compute [0.12, 0.92]
component CDN [0.10, 0.94]

// Knowledge
component Double-entry Bookkeeping [0.08, 0.95]
component Tax Law per Jurisdiction [0.06, 0.60]
component EN-16931 Standard [0.05, 0.78]

// Dependencies (a->b means a depends on b)
SMB Owner->Invoice UI
SMB Owner->Reporting Dashboard
SMB Owner->Cashflow Forecast
SMB Owner->Mobile Capture
Accountant->Client Portal
Accountant->Reporting Dashboard

Invoice UI->Invoice Generation
Invoice UI->Auth
Mobile Capture->Line-Item OCR
Reporting Dashboard->Database
Cashflow Forecast->Late-Payer Scoring (ML)
Cashflow Forecast->Bank Feeds

Invoice Generation->Tax Rules Engine
Invoice Generation->PEPPOL / E-invoicing Adapter
Invoice Generation->Recurring Billing
Recurring Billing->Payment Processing
Credit Notes & Refunds->Invoice Generation
Payment Reminders->Email / SMS
Payment Reminders->Late-Payer Scoring (ML)
Late-Payer Scoring (ML)->Database
Line-Item OCR->Object Storage
Tax Rules Engine->Tax Law per Jurisdiction
Tax Rules Engine->Double-entry Bookkeeping

Client Portal->Accounting Integration
Client Portal->Payment Processing
Accounting Integration->Webhooks
Bank Feeds->Database
PEPPOL / E-invoicing Adapter->EN-16931 Standard

Payment Processing->Card Networks
Payment Processing->Direct Debit / SEPA
Payment Processing->FX / Multi-currency
KYC / AML->Database

Invoice UI->Cloud Compute
Cloud Compute->Observability
Database->Cloud Compute
Object Storage->Cloud Compute
Client Portal->CDN

// Evolution arrows (scenarios, not forecasts)
evolve PEPPOL / E-invoicing Adapter 0.78
evolve Line-Item OCR 0.72
evolve Late-Payer Scoring (ML) 0.55
evolve Bank Feeds 0.85

// Pipelines (multiple variants of the same component)
pipeline Payment Processing [0.85, 0.95]

// Inertia flags
component Accounting Integration [0.40, 0.70] inertia

note Build moat here [0.65, 0.22]
note Rent from product vendors [0.40, 0.70]
note Utility — do not build [0.18, 0.92]
```

---

## 3. Build / Buy / Outsource — the headline decision

| Bucket | Components | Evolution stage | Rationale |
|---|---|---|---|
| **BUILD** (differentiate) | Invoice UI UX, Cashflow Forecast, Late-Payer Scoring (ML), Reporting Dashboard, Payment Reminders logic | Stage I–II (Genesis / Custom Built) | This is your moat. SMB owners pick invoicing SaaS on "does it feel effortless?" and "does it help me get paid faster?" — both UX and predictive-ML bets. |
| **BUY / RENT** (product) | PEPPOL Adapter (Pagero, Storecove, Tradeshift), Line-Item OCR (ABBYY, Rossum, Koncile), Tax Rules Engine (Avalara, Stripe Tax, Sphere/Anrok), Accounting Integration (Codat, Rutter), Bank Feeds (Plaid, Codat, Rutter), KYC / AML (Onfido, Persona) | Stage III (Product +rental) | Mature vendor market. Building in-house loses 12–24 months and never catches up. Rent the API, own the integration logic on top. |
| **OUTSOURCE / UTILITY** (commodity) | Payment Processing (Stripe / Adyen), Direct Debit / SEPA (GoCardless), Email / SMS (Postmark / Twilio / SendGrid), Auth (Clerk / Auth0 / WorkOS), Cloud Compute (AWS / GCP), Database, Object Storage, CDN (Cloudflare / Fastly), Observability (Datadog / Honeycomb) | Stage IV (Commodity +utility) | Treat as metered utility. Price, reliability, SLA — nothing else. Any engineering effort beyond integration glue is waste. |
| **LEVERAGE** (accepted knowledge) | Double-entry Bookkeeping, Tax Law per Jurisdiction, EN-16931 Standard | Stage IV knowledge | Hire accountants and tax specialists; do not reinvent. Consult, don't develop. |

---

## 4. Strategic analysis

### a. Top 3 by differentiation pressure D = ν·(1 − ε)

1. **Cashflow Forecast** (D = 0.70 × 0.72 = **0.50**) — high visibility (the SMB owner stares at this), low evolution (Genesis ML problem for SMB-scale data). This is the single biggest "why switch to us" differentiator.
2. **Late-Payer Scoring (ML)** (D = 0.50 × 0.70 = **0.35**) — feeds Cashflow Forecast and Payment Reminders. Still Custom Built in the SMB segment; enterprise (Microsoft Dynamics, HighRadius) have it, SMB tools don't.
3. **Payment Reminders logic** (D = 0.55 × 0.52 = **0.29**) — the tone, timing, escalation ladder, and which customers get which treatment. Most competitors send dumb scheduled emails; smart reminders (driven by Late-Payer Scoring) convert materially better.

### b. Top 3 by commodity leverage K = (1 − ν)·ε

1. **Cloud Compute** (K = 0.88 × 0.92 = **0.81**) — rent from AWS/GCP, don't run.
2. **Card Networks** (K = 0.78 × 0.95 = **0.74**) — sit behind Stripe/Adyen, never touch rails directly.
3. **CDN** (K = 0.90 × 0.94 = **0.85**) — Cloudflare/Fastly. Tied with Database (K = 0.87 × 0.90 = 0.78) and Email/SMS (K = 0.78 × 0.92 = 0.72).

### c. Top 3 dependency risks R = ν(a)·(1 − ε(b))

1. **(Cashflow Forecast → Late-Payer Scoring)** = 0.70 × 0.70 = **0.49** — your headline feature depends on an immature model. Mis-predicting a late-payer embarrasses the user.
2. **(Invoice Generation → Tax Rules Engine)** = 0.62 × 0.35 = **0.22** — the whole chain breaks if tax rules are wrong. Rent from Avalara/Stripe Tax; don't roll your own.
3. **(Invoice Generation → PEPPOL Adapter)** = 0.62 × 0.38 = **0.24** — regulatory criticality. Wrong PEPPOL format means the invoice is rejected and the SMB doesn't get paid. Buy this from Storecove/Pagero.

### d. Suggested gameplays (from Wardley's 61)

- **#36 Directed investment** on Cashflow Forecast + Late-Payer Scoring. This is where engineering time should go. Top-D components = build budget.
- **#29 Harvesting** on Accounting Integration and Bank Feeds — Codat/Rutter are in a land-grab for this API layer. Let them win; you rent.
- **#43 Sensing Engines (ILC)** — instrument your own platform to observe which SMB workflows correlate with fast payment. That signal is proprietary and feeds #36.
- **#56 First mover** on PEPPOL / ViDA compliance in the EU. Belgium mandates B2B e-invoicing from Jan 2026; France from Sept 2026; EU-wide by 2030. SMBs need to be compliant and most don't realise it yet. Being the "compliant by default" SMB invoicing tool in 2026 is a narrow-window positional play.
- **#15 Open Approaches** on the PEPPOL adapter shape (once yours works, publish a reference integration) — accelerate the standard, don't try to own it.
- **#26 Differentiation** on the Invoice UI and Cashflow Forecast — the user-facing components are where SMBs choose on feel.
- **#7 Education** — many SMBs don't understand ViDA is coming. Education plays dual role: compliance awareness + inbound marketing.
- **#41 Alliances** with Xero and QuickBooks — be the predictive-cashflow layer on top of their data, not a competitor to them.

### e. Doctrine violations / notes

- **#1 Focus on user needs** — satisfied. Anchors are user-facing needs (getting paid / keeping books), not internal deliverables.
- **#10 Know your users** — satisfied. Two anchors (SMB Owner, Accountant) reflect the two-sided nature.
- **#13 Manage inertia** — *watch*. Accounting Integration is flagged as `inertia` — migrating SMBs off desktop Sage / QuickBooks Desktop (Wardley inertia form #9 Re-architecture cost and form #2 Sunk capital) is the dominant onboarding friction.
- **#2 Use a systematic mechanism of learning** — the Late-Payer Scoring model must feed observed payment outcomes back as training data. If you don't wire this feedback loop in from day one, you've violated #2 and destroyed your moat. A "scoring model" without outcome feedback is just a heuristic.
- **#22 Use standards where appropriate** — Stage IV components should be standard APIs (Stripe, Twilio). Stage I–II (Cashflow Forecast) should *not* be standardised — that's where you experiment.
- **#33 There is no one culture** — the team building Invoice UI (pioneer/settler) and the team running Payment Processing integration SRE (town planner) want different cultures. Don't force one methodology across the whole map (this is doctrine #7).

### f. Climatic patterns actively shaping this map

- **#3 Everything evolves** — Line-Item OCR, PEPPOL Adapter, Bank Feeds are all actively moving right during 2024–2027. A map drawn in 2024 is already wrong.
- **#15 Past success breeds inertia** — incumbents (Sage, Xero Desktop legacies) resist cloud-SaaS migration; this is your wedge.
- **#17 Co-evolution of practice with activity** — as e-invoicing commoditises, accountants' practice co-evolves (PEPPOL literacy becomes table stakes). You can accelerate this.
- **#22 Efficiency enables innovation** — industrialising payments/OCR/tax lets the small team focus on Cashflow Forecast as a differentiator.
- **#27 Punctuated equilibrium: product → utility** — PEPPOL is a regulatory-forced punctuated transition in e-invoicing. You're mapping inside the war.

### g. Deep-placement notes

Five components warranted targeted research beyond the cheat sheet. Summary of what shifted:

1. **PEPPOL / E-invoicing Adapter — initial cheat-sheet ε ≈ 0.40 (Custom Built); revised to 0.62 (mid-Product).** Vendor-landscape and regulation searches found: Belgium mandates B2B PEPPOL from Jan 2026, France from Sept 2026, and EU-wide ViDA by July 2030. Mature adapter vendors (Storecove, Pagero, Tradeshift) already productised. The standard (EN-16931) is converging. Publication type has shifted from "build/construct" (Stage II) to "compliance guides and vendor comparisons" (Stage III). Still short of Stage IV because the format is not yet universal — hence ε = 0.62 with an `evolve` arrow to 0.78 over 2026–2030. Sources: EU eInvoicing factsheets; Novutech; fiskaly; Tradeshift compliance guides.

2. **Line-Item OCR — initial cheat-sheet ε ≈ 0.35 (Custom Built); revised to 0.55 (early Product).** Vendor research found ABBYY at 99.5% accuracy on structured invoices, Rossum 95–98% with continuous learning, plus active market (Tofu, Koncile, ChatFin). LLM-driven approaches are the new baseline. Header-field extraction is effectively commoditised; line-item extraction is the hard bit but vendors handle it now. Publication types are case studies and comparison roundups (Stage III signal). Shifted placement to 0.55 with an `evolve` arrow to 0.72 as LLM-native extraction matures. Clear **buy, do not build** verdict.

3. **Bank Feeds — initial cheat-sheet ε ≈ 0.65; revised to 0.75 (Product/Commodity edge).** Plaid secured an $8B valuation in Feb 2026 and supports 9,699+ institutions; Codat integrates 11,000+; Rutter is actively competing on Bank Feeds into accounting platforms. 67+ aggregators exist. This is a near-utility API layer with a handful of dominant players — a classic Stage III → IV transition. Gameplay verdict: **#29 Harvesting** — let Plaid/Codat/Rutter fight, pick the winner to integrate against, re-pick every 18 months.

4. **Late-Payer Scoring (ML) — initial cheat-sheet ε ≈ 0.25 (Genesis/late); confirmed at 0.30.** Research found the technique itself is mature (gradient-boosted trees, 77% accuracy in literature; Microsoft Dynamics 365 Finance Insights ships it for enterprise; HighRadius has had it since 2018 for large AR teams) but **there is no dominant SMB-focused vendor**. In SMB invoicing, this is still Custom Built — your data, your feature engineering, your training loop. Confirms the **build** decision and the #36 Directed-investment recommendation. Note: the academic consensus gives you a floor of ~75% prediction accuracy out of the box; the moat is calibration on your customer cohort.

5. **Tax Rules Engine — initial cheat-sheet ε ≈ 0.55; revised to 0.65 (mid-Product).** Avalara, Vertex, Sovos dominate enterprise; Stripe Tax, Sphere, Anrok target SaaS/subscription. Avalara launched an enhanced Stripe Billing app in Sep 2025, explicitly partnering rather than competing. Mature API market with clear segmentation. Verdict: **rent**. For SMB invoicing, Stripe Tax is the default (it's already in the payment stack) with Avalara as a fallback if you need deeper jurisdictional coverage.

**Not researched (skipped as obvious commodities or obvious moats per Step 4.5 budget):**
- Cloud Compute, CDN, Object Storage, Database, Email/SMS, Auth, Card Networks — obvious Stage IV utilities; cheat-sheet rows all agree; no reason to spend search budget.
- Double-entry Bookkeeping, EN-16931 — accepted knowledge (Stage IV), no research needed.
- Invoice UI, Cashflow Forecast — these are the mapper's known differentiation bets; the question is not "where is this in the market?" but "how good is *our* version?" — research doesn't help place them.

### h. Caveat

Evolution trajectories on this map (`evolve` arrows and the ε scores that drive them) are **scenarios, not forecasts**. Per Wardley's climatic pattern #18: *"you cannot measure evolution over time or adoption."* Re-score quarterly; the PEPPOL and OCR positions in particular will shift materially between 2026 and 2028.

---

## 5. One-sentence summary

**Build the UX + predictive ML (Cashflow Forecast, Late-Payer Scoring, Invoice UI); rent the regulated/commoditising middle layer (PEPPOL, OCR, Tax, Accounting/Bank Feeds) from mature Stage III vendors; treat payments, email, auth, and cloud as Stage IV utilities; and use ViDA/PEPPOL mandates as a first-mover positional play (gameplay #56) into European SMBs during the 2026–2030 compliance window.**

---

### Sources (deep-placement research)

- [E-Invoicing in Europe 2026: Complete roadmap of mandates and deadlines (fiskaly)](https://www.fiskaly.com/blog/e-invoicing-mandates-in-europe-2026)
- [E-Invoicing Europe 2025-2027: Complete Mandate Guide (Novutech)](https://www.novutech.com/news/e-invoicing-in-europe-overview-of-mandates-2025-2027)
- [Belgium B2B E-Invoicing Mandate (Tradeshift)](https://tradeshift.com/resources/compliance/belgium-e-invoicing-mandate-2026-compliance-peppol/)
- [eInvoicing Country Factsheets (European Commission)](https://ec.europa.eu/digital-building-blocks/sites/spaces/DIGITAL/pages/467108874/eInvoicing+Country+Factsheets+for+each+Member+State+and+other+countries)
- [10 Best AI OCR Tools for Invoice Extraction in 2026 (Koncile)](https://www.koncile.ai/en/ressources/top-10-ocr-tools-for-invoices-2025)
- [8 Best Invoice Data Extraction Software 2026 (Tofu)](https://www.gotofu.com/blog/best-invoice-data-extraction-software)
- [Banking Data Aggregation APIs: Compare Plaid, Tink & 67+ (Open Banking Tracker)](https://www.openbankingtracker.com/banking-data-aggregation)
- [Codat Bank Feeds API](https://www.codat.io/bank-feeds-api/)
- [Rutter Bank Feeds](https://www.rutter.com/blog/bank-feeds-sync-banking-data-to-any-accounting-system-netsuite-sage)
- [Optimize Cash Collection: Machine Learning for Invoice Payment (arXiv)](https://arxiv.org/pdf/1912.10828)
- [Customer payment predictions - Microsoft Dynamics 365](https://learn.microsoft.com/en-us/dynamics365/finance/finance-insights/payment-insights-overview)
- [Avalara vs. Stripe Tax: In-Depth Comparison 2026 (Numeral)](https://www.numeral.com/blog/avalara-vs-stripe-tax)
- [Top 8 Leading Sales Tax Compliance Software US 2026 (Sphere)](https://www.getsphere.com/blog/leading-sales-tax-compliance-software-in-the-us)
- [Avalara launches enhanced tax app for Stripe Billing](https://www.avalara.com/blog/en/north-america/2025/09/enhanced-tax-app-for-stripe-billing-and-stripe-checkout.html)
