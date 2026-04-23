# Wardley Map: Digital Financial Inclusion (Individual in an Underbanked Region)

**Date:** 2026-04-22
**Author:** arc-kit wardley-mapping skill (benchmark run-1)
**Scope:** The landscape of digital financial inclusion as experienced by an individual living in an underbanked region, from user needs down to the energy layer.
**Anchor:** The Individual — needing options, trade, equality, sustainability, and inclusion.

---

## 1. Anchor and Scope

- **Primary user:** An individual (person) in an underbanked region — typically rural or peri-urban communities in sub-Saharan Africa, parts of South / Southeast Asia, Latin America, or informal economies globally.
- **User needs:** Options (choice), Trade (ability to exchange value), Equality (access parity with the banked world), Sustainability (reliable long-term access), Inclusion (participation in the financial system).
- **Scope:** A cross-cutting landscape map spanning user needs, institutional/behavioural layer, banking provision and currency, technology stack, network topology, and energy.
- **Primary goal:** Show where the stack is commoditised globally (and therefore cheap, utility-grade, available anywhere) versus where **local landscape constraints still dominate** (and therefore require bespoke or still-emerging solutions).

---

## 2. The Map (visual)

```text
                     Genesis      Custom      Product      Commodity
                       0.00         0.25         0.50         0.75        1.00
                         │            │            │            │           │
Visible  ┌───────────────┼────────────┼────────────┼────────────┼───────────┐
 1.00    │                                                                  │
         │      Individual (anchor) ●                                       │
  0.94   │               Inclusion ●   Options ●                            │
  0.92   │                                           Equality ●             │
  0.90   │                    Sustainability ●           Trade ●            │
         │                        │  │                                      │
  0.82   │                Identity & Trust ●→                               │
  0.80   │                    Behaviour ●                                   │
  0.78   │                                                   Risk ●         │
  0.74   │                   Redistribution ●                               │
  0.72   │                                       Markets/Exchange ●         │
  0.70   │     Authority(Decentralised) ●                   Authority(Central) ×
         │                                                                  │
  0.62   │                                   Bank Branches × ●              │
  0.60   │                                     Banking Services ●           │
  0.58   │                                                  Online Pay ●→→  │
  0.56   │                                                        Fiat ●    │
  0.54   │                                 Cryptocurrency ●→                │
  0.52   │                                               Fin Infrastructure ●
  0.50   │            CBDC ●→                                               │
         │                                                                  │
  0.44   │                                  Mobile Device ●                 │
  0.42   │                              Internet Access ●                   │
  0.38   │                          Consensus Algos ●→                      │
  0.36   │                                             Compute Infra ●      │
         │                                                                  │
  0.30   │              Satellite ●→                                        │
  0.28   │       Mesh Networks ●→                                           │
  0.26   │                     5G ●→                                        │
  0.24   │                                              Copper × ●          │
         │                                                                  │
  0.14   │         Minigrids ●→                                             │
  0.12   │                       Renewable Energy ●→                        │
Hidden   │                                              Fossil Generation × ●
  0.00   └──────────────────────────────────────────────────────────────────┘

Legend: ● Current position, → Evolution direction, × Inertia (resistance to movement)
```

(A structural OWM-style representation is in `draft.owm`.)

---

## 3. Value Chain (what depends on what)

### Top — user and their needs

- **Individual** (anchor) depends on: Options, Trade, Equality, Sustainability, Inclusion.

### Behavioural / institutional layer

- **Identity & Trust** — required for any account opening, KYC, remittance, or credit. In this context it sits in **Custom-Built → Product** (score ~0.38): national ID programmes (Aadhaar, Ghana Card, ID4D) are productising, but for many individuals the lived experience is still bespoke and fragmented across biometric, SIM-registration, and self-sovereign-ID approaches.
- **Risk** — credit and counterparty risk modelling. **Product (~0.55)**: for the banked, this is productised (FICO, Experian); in underbanked contexts, alternative-data credit scoring is still settling.
- **Behaviour** — financial literacy, usage patterns. **Custom (~0.30)**: varies strongly by locality and culture.
- **Markets & Exchange Protocols** — card rails, SWIFT, Open Banking, ISO 20022. **Product (~0.60)**.
- **Authority (Centralised)** — central banks, regulators. **Commodity (~0.80)** with heavy institutional **inertia**.
- **Authority (Decentralised)** — DAOs, token-voting, community governance. **Custom (~0.28)**.
- **Redistribution** — welfare, aid, remittance flows, zakat, mutual societies. **Custom (~0.30)**: locally specific.

### Banking provision and currency

- **Bank Branches** — **Product (~0.65)**, but with **inertia** (declining asset class; expensive in low-density regions).
- **Banking Services** — **Product (~0.70)**.
- **Online Payments** — **Commodity (~0.84)** globally (Stripe, Adyen, M-Pesa, bKash, Pix, UPI).
- **Financial Infrastructure** (clearing, settlement, messaging) — **Commodity (~0.78)**.
- **Fiat Currency** — **Commodity (~0.92)**.
- **Cryptocurrency** — **Product (~0.55)** — moved out of custom/genesis, now has productised wallets, exchanges, stablecoins, but regulation is still forming.
- **CBDC** — **Genesis (~0.15)** — a handful of live deployments (eNaira, Sand Dollar, e-CNY pilot); most jurisdictions are experimenting.

### Technology stack

- **Internet Access** — globally **Commodity (~0.85)**; locally for the individual in an underbanked region, **Product (~0.60)** (intermittent, expensive per GB, uneven coverage). *Mapped here at 0.60 to reflect the individual's experience.*
- **Mobile Device** — **Commodity (~0.90)** (smartphones and feature phones are ubiquitous).
- **Consensus Algorithms** — **Product (~0.60)** for PoW/PoS; newer BFT variants still settling.
- **Computing Infrastructure** — **Commodity (~0.92)**.

### Network topology

- **Mesh Networks** — **Custom (~0.30)** (Guifi, goTenna, community mesh).
- **Satellite** — **Product (~0.55)** and productising fast (Starlink, OneWeb, Kuiper).
- **5G** — **Product (~0.60)**.
- **Copper** — **Commodity (~0.85)**, but declining/legacy with **inertia** (stranded asset class).

### Energy layer

- **Minigrids** — **Custom (~0.40)** (solar home systems, community grids).
- **Renewable Energy** — **Product (~0.60)**, productising rapidly.
- **Fossil Generation** — **Commodity (~0.85)**, high institutional **inertia** (sunk capex, subsidies).

---

## 4. Evolution Positioning — Summary Table

| Component | Stage | Position | Movement | Notes |
|---|---|---|---|---|
| Individual (anchor) | — | — | — | Anchor |
| Options | Genesis | 0.18 | evolving | For the underbanked these are still aspirational |
| Trade | Genesis | 0.28 | evolving | |
| Equality | Genesis | 0.12 | evolving | Social outcome, hard to commoditise |
| Sustainability | Genesis | 0.22 | evolving | |
| Inclusion | Genesis | 0.15 | evolving | Goal, not a product |
| Identity & Trust | Custom | 0.38 | accelerating (→ 0.60) | National ID programmes productising |
| Risk | Product | 0.55 | evolving | Alt-data credit moving right |
| Behaviour | Custom | 0.30 | — | Locally specific |
| Markets & Exchange Protocols | Product | 0.60 | evolving | ISO 20022 migration |
| Authority (Centralised) | Commodity | 0.80 | inertia × | Regulatory inertia |
| Authority (Decentralised) | Custom | 0.28 | evolving | DAOs settling |
| Redistribution | Custom | 0.30 | — | |
| Bank Branches | Product | 0.65 | inertia × | Declining asset |
| Banking Services | Product | 0.70 | evolving | |
| Online Payments | Commodity | 0.84 | accelerating (→ 0.90) | M-Pesa, UPI, Pix |
| Financial Infrastructure | Commodity | 0.78 | evolving | |
| Fiat Currency | Commodity | 0.92 | — | |
| Cryptocurrency | Product | 0.55 | evolving (→ 0.70) | |
| CBDC | Genesis | 0.15 | accelerating (→ 0.45) | eNaira, Sand Dollar, e-CNY |
| Internet Access | Product | 0.60 | evolving | Local gap vs global commodity |
| Mobile Device | Commodity | 0.90 | — | |
| Consensus Algorithms | Product | 0.60 | evolving (→ 0.75) | |
| Computing Infrastructure | Commodity | 0.92 | — | |
| Mesh Networks | Custom | 0.30 | evolving (→ 0.50) | |
| Satellite | Product | 0.55 | accelerating (→ 0.75) | Starlink |
| 5G | Product | 0.60 | evolving (→ 0.80) | |
| Copper | Commodity | 0.85 | inertia × | Legacy |
| Minigrids | Custom | 0.40 | evolving (→ 0.60) | |
| Renewable Energy | Product | 0.60 | accelerating (→ 0.82) | |
| Fossil Generation | Commodity | 0.85 | inertia × | Subsidies, sunk capex |

---

## 5. Movement — what's evolving, with inertia, and accelerating

**Naturally evolving (→)**

- CBDC, Cryptocurrency, Identity & Trust, Renewable Energy, Mesh Networks, Satellite, 5G, Consensus Algorithms, Online Payments, Minigrids are all drifting right.

**Accelerating (>>)**

- **Online Payments** — mobile money and instant-payment rails (M-Pesa, UPI, Pix, PIX-PSEs) compressing the stack toward utility.
- **Satellite** (Starlink and peers) — bypassing terrestrial network buildouts entirely, collapsing the "local internet" gap in months, not decades.
- **Renewable Energy** — cost curves are forcing acceleration; solar + storage is the cheapest new generation in most of the underbanked world.
- **Identity & Trust** — pushed by both national-ID programmes and interoperable digital-credential standards (mDL, W3C VC).

**Inertia (×)**

- **Bank Branches** — sunk physical capex, regulatory capital requirements, incumbent employment.
- **Authority (Centralised)** — central banks and regulators move slowly; treaty-level standards (Basel, FATF) add lag.
- **Copper** — stranded telecoms assets, unwilling to write down.
- **Fossil Generation** — sunk generation capex, subsidies, political economy.

---

## 6. Where the Stack Is Commoditised Globally vs Where Local Landscape Dominates

The central question. Read the map right-to-left and bottom-to-top:

### Globally commoditised (right side, position ≥ 0.75)

- **Fiat Currency, Financial Infrastructure, Online Payments** — ubiquitous utility rails. A dollar, euro or rupee transfers with standardised cost profiles; Stripe, Adyen, PayPal, M-Pesa, UPI, Pix are all utility-grade.
- **Mobile Device, Computing Infrastructure** — effectively universal; smartphones reach almost everywhere, cloud compute is a fungible utility.
- **Copper, Fossil Generation** — commodity but legacy; they look commoditised but they are mostly *terminal* commodities, no longer evolving.
- **Authority (Centralised) / Fiat** — the governance stack itself is highly institutionalised.

### Where local landscape constraints still dominate (left-of-centre, position ≤ 0.50)

This is where the individual in an underbanked region actually lives:

- **Internet Access** — globally commodity; locally still Product-stage for the individual (coverage gaps, affordability, throttling).
- **Minigrids, Renewable Energy, Fossil Generation mix** — the energy layer underneath is highly locality-specific. Minigrids are still Custom-stage.
- **Mesh Networks, Satellite, 5G** — network topology at the last mile is locally constrained. Satellite is accelerating but not yet utility-grade in this context.
- **Identity & Trust, Behaviour, Redistribution** — the social/institutional layer is irreducibly local.
- **CBDC** — Genesis-stage: each jurisdiction has a different experiment.
- **Authority (Decentralised)** — still forming, varies by community.

### The strategic reading

The individual sits at the top of a stack that is **commoditised from the middle down to computing infrastructure and fiat**, but has **two locally bound gaps**:

1. **The last-mile physical stack** (Internet Access + Network topology + Energy) — globally commoditising, but the individual's experience is Product-at-best and often Custom.
2. **The institutional/social stack** (Identity & Trust, Behaviour, Redistribution, Authority-Decentralised) — irreducibly local.

These two gaps are where strategic investment lives. The middle tier (payments, fiat, banking services) is already mostly a utility.

---

## 7. Analysis Checklist

### Completeness
- Anchor clearly defined (Individual + five named needs). ✓
- All components in the scenario prompt are present (banking, currency, tech stack, network topology, energy). ✓
- Dependencies flow downward from anchor through institutions, services, tech, network, energy. ✓
- Movement arrows and inertia markers present. ✓

### Positioning
- Positioned on market evolution, not internal capability. ✓
- Commodities (fiat, mobile, compute, online payments, financial infrastructure) on the right. ✓
- Genesis components (CBDC, user-need goals) on the left. ✓

### Insights (from the map)

**Inertia points**
- Bank Branches — sunk physical capex, staffing, regulatory capital → slow to exit.
- Authority (Centralised) — treaty-level and central-bank conservatism.
- Copper telecoms — accounting/stranded-asset reluctance.
- Fossil Generation — sunk capex and subsidy politics.

**Opportunities to commoditise**
- Identity & Trust — a pan-regional interoperable digital identity layer would collapse a major barrier.
- Cryptocurrency rails and stablecoins as remittance commodity (already happening: USDC/USDT rails in LATAM, West Africa).
- Satellite internet as "last-mile" commodity — Starlink pricing is the weak signal.
- Minigrids as a productised service (SolShare, M-KOPA, Sun King).

**Where Genesis activities could become differentiators**
- CBDC-plus-digital-ID combinations, where jurisdictions pair a retail CBDC with a national ID — the first movers set the reference architecture (China, Nigeria, Bahamas).
- Decentralised authority + consensus algorithm combinations for remittance settlement in jurisdictions where the central bank is absent or distrusted.
- Minigrid + mesh + mobile bundling as a single utility for the underserved.

**Technical debt**
- Continuing to operate bank *branches* in low-density underbanked regions is classic technical debt (building custom where a product — agent banking, mobile money — already exists).
- National-ID programmes that build bespoke biometric stacks rather than using open standards (ICAO, W3C VC) accrue integration debt.

### Strategic

**Gameplay patterns applicable**

- **Open sourcing the commodity** — push online-payment interfaces, identity credentials, and consensus protocols into open standards to prevent regulatory capture by incumbents.
- **Sensing engagement** (open the door to ecosystems) — satellite providers partnering with local payment rails; mesh/minigrid operators partnering with mobile-money issuers.
- **Constraint removal** — every commoditised layer below should reduce the delivery cost upward; the strategic question is which gateway (Identity, Risk, Authority) is throttling that flow.
- **Cross-subsidy (Tower and Moat)** — pair a commodity layer (fiat/online payments) with a differentiator (local-context identity or risk) to defend margin.

**Climatic patterns at play**

- *Everything evolves* — the whole middle tier is drifting right.
- *No choice over evolution* — Fossil Generation and Copper are being displaced regardless of incumbent preferences.
- *Inertia is caused by past success* — central bank authority and bank-branch networks are the classic examples.
- *Commoditisation enables genesis above it* — commoditised Mobile + Online Payments enables Genesis-stage experiments in CBDC, tokenised redistribution, decentralised authority.
- *Local vs global* — the core tension of this map: the stack commoditises globally but the lived experience is local.

**Doctrine weaknesses**

- *Know your users* — the "underbanked individual" is not one user; it's many (rural agrarian, urban informal, refugee, woman denied banking access). Segmenting the anchor clarifies priorities.
- *Focus on high situational awareness* — most financial-inclusion programmes don't map their stack; they reason about a single layer (often banking services or identity) in isolation.
- *Think small (as in teams)* — local-context layers (identity, behaviour, minigrids) benefit from small situated teams, not global programmes.
- *Use appropriate methods (for each stage)* — Genesis-stage CBDC and decentralised authority need agile/in-house experimentation; Commodity-stage payments should be outsourced to utility providers.

---

## 8. Recommendations

### Immediate (next 6-12 months)

- **Treat payments as a utility.** For any organisation serving underbanked individuals, stop building payment rails; integrate with the local dominant utility (M-Pesa, UPI, Pix, bKash, GCash) and a stablecoin rail for cross-border.
  *Rationale:* Online Payments is already Commodity-stage; competing here burns capital.

- **Pilot Identity & Trust on open standards.** Adopt W3C Verifiable Credentials and ICAO mDL, rather than custom biometric stacks.
  *Rationale:* Identity is accelerating toward Product-stage; standardisation wins.

- **Bundle Minigrid + Mesh + Mobile Money as a single utility offering** in regions where all three are sub-Product.
  *Rationale:* the three locally-constrained layers reinforce each other; a bundled offer moves the whole stack right faster than any single component.

### Short-term (1-2 years)

- **Adopt Satellite as last-mile default.** Starlink and peers are moving faster than national telecoms rollouts; design for satellite-first, cellular-second, copper-never.
  *Rationale:* the weak signal — price-per-GB parity with fixed broadband — has already fired in several markets.

- **Exit Bank Branches where agent banking is viable.** Redirect capex from branches into agent networks and mobile money interoperability.
  *Rationale:* branches carry inertia; agent banking is the productised successor.

- **Participate in CBDC pilots without betting the stack on any one.** Treat CBDC as Genesis; keep optionality; avoid building CBDC-specific irreversible integrations.
  *Rationale:* the failure mode of Genesis is "bet on the wrong approach." Multiple jurisdictional designs will coexist.

### Long-term (2-5 years)

- **Build for a commodity payments + utility energy + decentralised-or-centralised authority stack.** Assume that Online Payments, Financial Infrastructure, Fiat, Mobile Device, Compute, Renewable Energy and Satellite Internet will all be utility-grade globally.
  *Rationale:* the weight of commoditisation is on that side of the map.

- **Invest in local-context differentiators.** Identity & Trust, Risk (for thin-file users), Behaviour (literacy, language, norms), Redistribution — these are where local landscape constraints persist and where competitive advantage is durable.
  *Rationale:* the two strategic gaps identified above — last-mile physical and institutional/social — are the long-term investment thesis for financial inclusion.

- **Design for energy-constrained operation.** Minigrid and renewable-first architectures at every layer (device battery life, consensus-algorithm energy profile, network-access duty cycle) reduce lock-in to fossil inertia.
  *Rationale:* the energy layer's inertia is the deepest; design around it rather than wait for it to resolve.

---

## 9. Quantitative (Optional) Cross-Check

Selected components scored on Ubiquity × Certainty (per `mathematical-models.md`):

| Component | Ubiquity (0-1) | Certainty (0-1) | Mean | Stage (expected) | Stage (observed) |
|---|---|---|---|---|---|
| Fiat Currency | 0.98 | 0.95 | 0.97 | Commodity | Commodity (0.92) ✓ |
| Online Payments | 0.85 | 0.85 | 0.85 | Commodity | Commodity (0.84) ✓ |
| CBDC | 0.12 | 0.25 | 0.18 | Genesis | Genesis (0.15) ✓ |
| Cryptocurrency | 0.45 | 0.55 | 0.50 | Product (low) | Product (0.55) ✓ |
| Identity & Trust | 0.35 | 0.40 | 0.38 | Custom | Custom (0.38) ✓ |
| Satellite | 0.45 | 0.60 | 0.53 | Product (low) | Product (0.55) ✓ |
| Minigrids | 0.35 | 0.40 | 0.38 | Custom | Custom (0.40) ✓ |
| Renewable Energy | 0.55 | 0.65 | 0.60 | Product | Product (0.60) ✓ |

Positioning is consistent between qualitative reasoning and quantitative scoring.

---

## 10. Closing Observation

The individual in an underbanked region sits at the top of a value chain that is **predominantly commoditised in the middle (payments, fiat, infrastructure, mobile, compute)** but still **locally bound at the top (identity, behaviour, redistribution) and at the bottom (network topology, minigrid energy)**.

The strategic opportunity for inclusion is **not to reinvent the commodity middle** — it's to **close the two locally-constrained gaps** while leaning on the commodity middle as hard as possible, and to keep optionality around the Genesis-stage assets (CBDC, decentralised authority) whose outcomes are still uncertain.
