# Wardley Map: Automated Invoicing SaaS for Small Businesses

## 1. Scope & Anchor (The User)

- **User**: Small business owner / bookkeeper
- **Primary needs**:
  1. Get paid faster (reduce days-sales-outstanding)
  2. Stay compliant (tax, e-invoicing mandates)
  3. Spend less time on admin

The anchor is the *small business*. Everything else on the map exists to serve that user need.

---

## 2. Component Inventory & Evolution Position

Evolution axis: Genesis [0.00–0.25) → Custom [0.25–0.50) → Product [0.50–0.75) → Commodity [0.75–1.00]
Visibility axis: 1.0 (most visible to user) → 0.0 (deep infrastructure)

| # | Component | Visibility | Evolution | Stage | Rationale |
|---|-----------|-----------:|----------:|-------|-----------|
| U | Small business (user) | 1.00 | 0.95 | Commodity | The anchor |
| 1 | Get paid faster (need) | 0.95 | 0.90 | Commodity | Universal need |
| 2 | Invoice creation UX | 0.90 | 0.70 | Product | Well-understood, differentiator in polish |
| 3 | Invoice templates | 0.88 | 0.85 | Commodity | Widely available |
| 4 | Client / customer management | 0.85 | 0.75 | Product | Standard CRM-lite |
| 5 | Payment collection (card / ACH / SEPA) | 0.85 | 0.90 | Commodity | Stripe/Adyen/GoCardless own this |
| 6 | Recurring billing / subscriptions | 0.80 | 0.70 | Product | Mature, many providers |
| 7 | Dunning & reminders | 0.78 | 0.60 | Product | Common but quality varies |
| 8 | Accounting integration (Xero, QuickBooks) | 0.75 | 0.80 | Commodity | APIs are stable and commoditised |
| 9 | E-invoicing compliance (Peppol, ViDA, CTCs) | 0.70 | 0.40 | Custom-built → shifting | Regulatory, evolving fast (2024–2030 mandates) |
| 10 | Tax calculation (VAT/GST/Sales tax) | 0.68 | 0.75 | Product/Commodity | Avalara, TaxJar, Stripe Tax |
| 11 | AI-assisted line-item extraction / categorisation | 0.65 | 0.30 | Custom → Product | LLM-driven, differentiator today |
| 12 | Cash-flow forecasting | 0.60 | 0.35 | Custom | Emerging value-add |
| 13 | Multi-currency / FX | 0.55 | 0.85 | Commodity | Wise, Stripe, banks |
| 14 | Identity & auth (SSO, MFA) | 0.45 | 0.90 | Commodity | Auth0, Clerk, Cognito |
| 15 | Notifications (email / SMS / WhatsApp) | 0.45 | 0.85 | Commodity | SendGrid, Twilio, Postmark |
| 16 | PDF generation & e-signature | 0.42 | 0.80 | Commodity | DocuSign, open-source libs |
| 17 | Data storage (relational + object) | 0.25 | 0.95 | Commodity | RDS/Aurora, S3 |
| 18 | Compute / hosting | 0.20 | 0.95 | Commodity | AWS/GCP/Azure |
| 19 | Observability (logs, metrics, traces) | 0.20 | 0.85 | Commodity | Datadog, Grafana Cloud |
| 20 | Fraud & sanctions screening | 0.30 | 0.70 | Product | ComplyAdvantage, Sift |
| 21 | Power / network | 0.05 | 1.00 | Commodity | Utility |

---

## 3. The Map (ASCII)

```
Visibility
  1.0 |  [U User: Small Business]
      |          |
  0.9 |   [1 Get paid faster]
      |          |
  0.8 |   [2 Invoice UX]---[3 Templates]   [4 Clients]   [5 Payments]
      |     |        \         |               |            |
  0.7 |   [6 Recurring]-[7 Dunning]------[8 Accounting int.]
      |       |            |                |
  0.6 |  [9 E-invoicing compliance]    [10 Tax calc]
      |       |                              |
  0.5 | [11 AI extraction]  [12 Cashflow]  [13 FX]
      |       |                 |            |
  0.4 |  [20 Fraud]      [16 PDF/eSign]  [15 Notif]  [14 Auth]
      |       |                 |            |         |
  0.2 |              [17 Storage]   [18 Compute]   [19 Observability]
      |                       |          |             |
  0.0 |                         [21 Power / network]
      +----------------------------------------------------------
        Genesis        Custom         Product        Commodity
         0.00           0.25           0.50           0.75     1.00
                              Evolution ->
```

Arrows represent dependencies $(a,b) \in E$ meaning *a depends on b*, with the constraint $\nu(a) \ge \nu(b)$.

---

## 4. Build / Buy / Outsource Decisions

Rule of thumb (Wardley doctrine):
- **Genesis / Custom (ε < 0.5)**: BUILD — this is where differentiation lives.
- **Product (0.5 ≤ ε < 0.75)**: BUY / rent — use off-the-shelf SaaS or libraries.
- **Commodity (ε ≥ 0.75)**: OUTSOURCE / use utility — pay-as-you-go cloud/API.

### BUILD (your IP, your moat)

| Component | Why build |
|-----------|-----------|
| **2 Invoice creation UX** | The one thing the user touches every day. Polish and speed are your wedge against incumbents. |
| **9 E-invoicing compliance** (orchestration layer) | Peppol, France (2026), Germany (2025–28), ViDA by 2030 — regulations shift yearly. Own the orchestration; plug in certified access points underneath. This is genuine differentiation for small-biz users who can't track mandates themselves. |
| **11 AI line-item extraction & categorisation** | Currently custom/genesis. LLM-powered "snap-a-receipt / forward-an-email → draft invoice" is where you can leapfrog QuickBooks/Xero today. |
| **12 Cash-flow forecasting** | Turns invoicing data into a second product. Small-biz owners will pay for "when will I run out of cash?" |
| **7 Dunning logic** (behavioural, not the sending) | Smart reminder cadence tuned to payer behaviour is a measurable ROI story (DSO reduction). |

### BUY (rent productised SaaS / libraries)

| Component | Recommended vendors |
|-----------|---------------------|
| **5 Payments** | Stripe (primary), GoCardless (ACH/SEPA direct debit), Adyen at scale |
| **8 Accounting integration** | Codat or Rutter (unified API across Xero/QuickBooks/Sage) — avoids 1:1 integration work |
| **10 Tax calculation** | Stripe Tax for simple cases; Avalara / Anrok for complex multi-jurisdiction |
| **6 Recurring billing primitives** | Stripe Billing or build thin layer on Stripe |
| **16 PDF / e-signature** | wkhtmltopdf / Puppeteer + DocuSign or Dropbox Sign |
| **20 Fraud / sanctions** | Stripe Radar (bundled) or ComplyAdvantage for AML |
| **E-invoicing access points** (under component 9) | Pagero, Storecove, Tungsten — do NOT become a certified Peppol AP yourself |

### OUTSOURCE / UTILITY (commodity, pay-as-you-go)

| Component | Provider |
|-----------|----------|
| **14 Auth** | Clerk or Auth0 (don't roll your own) |
| **15 Notifications** | Postmark (transactional email), Twilio (SMS/WhatsApp) |
| **17 Storage** | AWS RDS/Aurora + S3 |
| **18 Compute** | AWS (ECS/Fargate or Lambda); avoid Kubernetes until scale demands it |
| **19 Observability** | Grafana Cloud or Datadog |
| **13 FX** | Wise Platform or Stripe FX |

---

## 5. Climatic Patterns to Watch

1. **E-invoicing mandates are industrialising** — component 9 is moving left-to-right fast. Build the orchestration now while it's custom; in 3 years it'll be a commodity checkbox and differentiation vanishes.
2. **AI copilots are entering accounting** — component 11 is currently Genesis/Custom. Incumbents (Intuit, Xero) are adding AI features; your window to lead on this is ~18 months.
3. **Embedded finance** — payments + lending embedded inside invoicing (invoice financing, instant payout) is a future adjacency. Don't build now, but design data model to enable it.
4. **Open Banking** — A2A payments (PIS) will erode card-rail economics in EU/UK. Pick payment providers that already support it (GoCardless, TrueLayer).

---

## 6. Strategic Gameplays to Apply

- **Accelerate commoditisation of e-invoicing APIs**: contribute to open Peppol tooling to reduce your own integration cost.
- **Exploit constraint (component 11)**: AI extraction is the scarce, high-value capability. Invest disproportionately here.
- **Industrialise components (17–19)**: IaC from day one, no snowflake infra. These should be boring.
- **Avoid**: do not build your own payment processor, your own tax engine, or your own Peppol AP. Each is a multi-year distraction with no user-visible win.

---

## 7. Formal Model Summary

$\mathcal{M} = (V, E, \nu, \varepsilon, t)$ where:

- $|V| = 21$ components plus user anchor
- $E$ = dependency edges shown in section 3 (directed, $\nu(a) \ge \nu(b)$)
- $\nu: V \to [0,1]$ as tabulated in section 2
- $\varepsilon: V \to [0,1]$ as tabulated in section 2
- $t$ = snapshot at 2026-Q2

Evolution dynamics: $\tfrac{d\varepsilon}{dt} = r(1-\varepsilon)$. Components 9 and 11 have the highest $r$ (regulatory pressure and AI capability diffusion respectively) and should be re-mapped every 6 months.

---

## 8. One-Line Answer

**Build** the invoicing UX, the e-invoicing compliance orchestration, the AI line-item extraction, and the cash-flow forecast. **Buy** payments, tax, accounting-integration, and recurring-billing primitives. **Outsource** auth, notifications, storage, compute, and observability to commodity cloud/SaaS.
