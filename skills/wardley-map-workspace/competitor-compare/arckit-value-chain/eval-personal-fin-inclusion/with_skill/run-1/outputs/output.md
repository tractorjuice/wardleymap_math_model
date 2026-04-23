# Value Chain: Personal Financial Inclusion

**Command:** `arckit-wardley.value-chain`
**Anchor:** Individual in an underbanked region
**Components:** 29 (1 anchor + 28 components)
**Stage:** Value chain only — evolution placeholder ε=0.50 (build/buy not assessed)

## Executive Summary

The anchor is **an individual in an underbanked region** pursuing five genuine needs (inclusion, trade, options, equality, sustainability). Below those needs sits a socio-institutional layer (identity and trust, risk, behaviour, markets, authority, redistribution), then banking provision and currency forms, then the technology/network/energy stack. The chain reveals three strategic observations:

1. Identity and Trust is a shared dependency of Banking Services, Authority and Governance, and (via Authority) most of the currency layer — it is a critical chokepoint.
2. Internet Access and Mobile Device are pan-stack dependencies: every path from user need to energy flows through them.
3. The currency triad (Fiat / CBDC / Cryptocurrency) partitions on authority (centralised vs decentralised) but converges on shared computing and network infrastructure — the bottom of the stack commoditises globally while identity, authority, energy and last-mile network remain locally constrained.

## Users and Personas

| User type | Primary need |
|---|---|
| Individual in underbanked region (anchor) | Access to inclusive, low-friction financial services |
| Informal worker / smallholder | Trade, savings, remittance without a branch |
| Recipient of state transfers | Reliable redistribution channel |
| Local merchant | Exchange protocol compatible with peers and buyers |

## Value Chain Diagram (ASCII)

```
ν=0.96  Individual (anchor)
ν=0.85–0.90  Inclusion · Trade · Options · Equality · Sustainability
ν=0.68–0.78  Identity and Trust · Risk · Behaviour · Markets · Authority · Redistribution
ν=0.53–0.60  Banking Services · Bank Branches · Online Payments · Fiat · CBDC · Crypto
ν=0.42–0.45  Financial Infrastructure · Consensus Algorithms
ν=0.28–0.35  Mobile Device · Internet Access · Computing Infrastructure
ν=0.16–0.22  5G · Satellite · Mesh · Copper
ν=0.06–0.10  Minigrids · Renewable · Fossil
```

## OWM Code

```owm
title Personal Financial Inclusion (value chain, evolution placeholder)

anchor Individual [0.96, 0.50]

component Inclusion [0.90, 0.50]
component Trade [0.88, 0.50]
component Options [0.87, 0.50]
component Equality [0.86, 0.50]
component Sustainability [0.85, 0.50]

component Identity and Trust [0.78, 0.50]
component Risk Management [0.76, 0.50]
component Behaviour and Literacy [0.74, 0.50]
component Markets and Exchange [0.72, 0.50]
component Authority and Governance [0.70, 0.50]
component Redistribution [0.68, 0.50]

component Banking Services [0.60, 0.50]
component Online Payments [0.58, 0.50]
component Bank Branches [0.56, 0.50]
component Fiat Currency [0.55, 0.50]
component CBDC [0.54, 0.50]
component Cryptocurrency [0.53, 0.50]

component Financial Infrastructure [0.45, 0.50]
component Consensus Algorithms [0.42, 0.50]

component Mobile Device [0.35, 0.50]
component Internet Access [0.32, 0.50]
component Computing Infrastructure [0.28, 0.50]

component 5G Network [0.22, 0.50]
component Satellite Network [0.20, 0.50]
component Mesh Network [0.18, 0.50]
component Copper Network [0.16, 0.50]

component Minigrids [0.10, 0.50]
component Renewable Energy [0.08, 0.50]
component Fossil Energy [0.06, 0.50]

Individual -> Inclusion
Individual -> Trade
Individual -> Options
Individual -> Equality
Individual -> Sustainability

Inclusion -> Identity and Trust
Inclusion -> Redistribution
Trade -> Markets and Exchange
Trade -> Banking Services
Options -> Banking Services
Options -> Authority and Governance
Equality -> Redistribution
Equality -> Authority and Governance
Sustainability -> Authority and Governance

Identity and Trust -> Banking Services
Identity and Trust -> Authority and Governance
Risk Management -> Banking Services
Risk Management -> Markets and Exchange
Behaviour and Literacy -> Banking Services
Behaviour and Literacy -> Mobile Device
Markets and Exchange -> Fiat Currency
Markets and Exchange -> Cryptocurrency
Markets and Exchange -> CBDC
Authority and Governance -> Fiat Currency
Authority and Governance -> CBDC
Redistribution -> Banking Services
Redistribution -> Online Payments

Banking Services -> Bank Branches
Banking Services -> Online Payments
Banking Services -> Financial Infrastructure
Online Payments -> Financial Infrastructure
Online Payments -> Mobile Device
Bank Branches -> Financial Infrastructure
Fiat Currency -> Financial Infrastructure
CBDC -> Financial Infrastructure
CBDC -> Consensus Algorithms
Cryptocurrency -> Consensus Algorithms

Financial Infrastructure -> Computing Infrastructure
Financial Infrastructure -> Internet Access
Consensus Algorithms -> Computing Infrastructure
Consensus Algorithms -> Internet Access

Mobile Device -> Internet Access
Internet Access -> 5G Network
Internet Access -> Satellite Network
Internet Access -> Mesh Network
Internet Access -> Copper Network

5G Network -> Fossil Energy
5G Network -> Renewable Energy
Satellite Network -> Renewable Energy
Mesh Network -> Minigrids
Copper Network -> Fossil Energy
Computing Infrastructure -> Fossil Energy
Computing Infrastructure -> Renewable Energy

Minigrids -> Renewable Energy
Minigrids -> Fossil Energy

style wardley
```

<details>
<summary>Mermaid wardley-beta equivalent</summary>

```mermaid
wardley-beta
title Personal Financial Inclusion (value chain, evolution placeholder)
size [1100, 800]

anchor Individual [0.96, 0.50]

component Inclusion [0.90, 0.50]
component Trade [0.88, 0.50]
component Options [0.87, 0.50]
component Equality [0.86, 0.50]
component Sustainability [0.85, 0.50]

component "Identity and Trust" [0.78, 0.50]
component "Risk Management" [0.76, 0.50]
component "Behaviour and Literacy" [0.74, 0.50]
component "Markets and Exchange" [0.72, 0.50]
component "Authority and Governance" [0.70, 0.50]
component Redistribution [0.68, 0.50]

component "Banking Services" [0.60, 0.50]
component "Online Payments" [0.58, 0.50]
component "Bank Branches" [0.56, 0.50]
component "Fiat Currency" [0.55, 0.50]
component CBDC [0.54, 0.50]
component Cryptocurrency [0.53, 0.50]

component "Financial Infrastructure" [0.45, 0.50]
component "Consensus Algorithms" [0.42, 0.50]

component "Mobile Device" [0.35, 0.50]
component "Internet Access" [0.32, 0.50]
component "Computing Infrastructure" [0.28, 0.50]

component "5G Network" [0.22, 0.50]
component "Satellite Network" [0.20, 0.50]
component "Mesh Network" [0.18, 0.50]
component "Copper Network" [0.16, 0.50]

component Minigrids [0.10, 0.50]
component "Renewable Energy" [0.08, 0.50]
component "Fossil Energy" [0.06, 0.50]

Individual -> Inclusion
Individual -> Trade
Individual -> Options
Individual -> Equality
Individual -> Sustainability
Inclusion -> "Identity and Trust"
Inclusion -> Redistribution
Trade -> "Markets and Exchange"
Trade -> "Banking Services"
Options -> "Banking Services"
Options -> "Authority and Governance"
Equality -> Redistribution
Equality -> "Authority and Governance"
Sustainability -> "Authority and Governance"
"Identity and Trust" -> "Banking Services"
"Identity and Trust" -> "Authority and Governance"
"Risk Management" -> "Banking Services"
"Risk Management" -> "Markets and Exchange"
"Behaviour and Literacy" -> "Banking Services"
"Behaviour and Literacy" -> "Mobile Device"
"Markets and Exchange" -> "Fiat Currency"
"Markets and Exchange" -> Cryptocurrency
"Markets and Exchange" -> CBDC
"Authority and Governance" -> "Fiat Currency"
"Authority and Governance" -> CBDC
Redistribution -> "Banking Services"
Redistribution -> "Online Payments"
"Banking Services" -> "Bank Branches"
"Banking Services" -> "Online Payments"
"Banking Services" -> "Financial Infrastructure"
"Online Payments" -> "Financial Infrastructure"
"Online Payments" -> "Mobile Device"
"Bank Branches" -> "Financial Infrastructure"
"Fiat Currency" -> "Financial Infrastructure"
CBDC -> "Financial Infrastructure"
CBDC -> "Consensus Algorithms"
Cryptocurrency -> "Consensus Algorithms"
"Financial Infrastructure" -> "Computing Infrastructure"
"Financial Infrastructure" -> "Internet Access"
"Consensus Algorithms" -> "Computing Infrastructure"
"Consensus Algorithms" -> "Internet Access"
"Mobile Device" -> "Internet Access"
"Internet Access" -> "5G Network"
"Internet Access" -> "Satellite Network"
"Internet Access" -> "Mesh Network"
"Internet Access" -> "Copper Network"
"5G Network" -> "Fossil Energy"
"5G Network" -> "Renewable Energy"
"Satellite Network" -> "Renewable Energy"
"Mesh Network" -> Minigrids
"Copper Network" -> "Fossil Energy"
"Computing Infrastructure" -> "Fossil Energy"
"Computing Infrastructure" -> "Renewable Energy"
Minigrids -> "Renewable Energy"
Minigrids -> "Fossil Energy"
```

</details>

## Component Inventory

| # | Component | ν | Level | Description |
|---|---|---|---|---|
| 1 | Individual | 0.96 | Anchor | Person in an underbanked region seeking financial inclusion |
| 2 | Inclusion | 0.90 | User-facing | Being able to participate in the financial system |
| 3 | Trade | 0.88 | User-facing | Exchanging value for goods and services |
| 4 | Options | 0.87 | User-facing | Access to multiple providers and instruments |
| 5 | Equality | 0.86 | User-facing | Fair terms relative to other participants |
| 6 | Sustainability | 0.85 | User-facing | Durable, environmentally viable participation |
| 7 | Identity and Trust | 0.78 | High | Verified identity and counterparty trust |
| 8 | Risk Management | 0.76 | High | Credit, fraud, and operational risk handling |
| 9 | Behaviour and Literacy | 0.74 | High | Financial literacy and usage habits |
| 10 | Markets and Exchange | 0.72 | High | Protocols for matching buyers and sellers |
| 11 | Authority and Governance | 0.70 | High | Central / decentralised rule-setting |
| 12 | Redistribution | 0.68 | Medium-High | State transfers, welfare, aid channels |
| 13 | Banking Services | 0.60 | Medium-High | Accounts, savings, credit, transfers |
| 14 | Online Payments | 0.58 | Medium-High | Digital payment rails |
| 15 | Bank Branches | 0.56 | Medium-High | Physical service points |
| 16 | Fiat Currency | 0.55 | Medium-High | State-issued unit of account |
| 17 | CBDC | 0.54 | Medium-High | Central bank digital currency |
| 18 | Cryptocurrency | 0.53 | Medium-High | Decentralised digital assets |
| 19 | Financial Infrastructure | 0.45 | Medium | Clearing, settlement, ledgers, rails |
| 20 | Consensus Algorithms | 0.42 | Medium | Distributed agreement (PoW, PoS, BFT) |
| 21 | Mobile Device | 0.35 | Medium | Handset used by the individual |
| 22 | Internet Access | 0.32 | Medium | Connectivity layer |
| 23 | Computing Infrastructure | 0.28 | Low | Compute, storage, hosting |
| 24 | 5G Network | 0.22 | Low | Modern mobile radio |
| 25 | Satellite Network | 0.20 | Low | LEO/GEO links |
| 26 | Mesh Network | 0.18 | Low | Peer-relayed local connectivity |
| 27 | Copper Network | 0.16 | Low | Legacy wireline |
| 28 | Minigrids | 0.10 | Infrastructure | Local community power |
| 29 | Renewable Energy | 0.08 | Infrastructure | Solar / wind primary generation |
| 30 | Fossil Energy | 0.06 | Infrastructure | Legacy primary generation |

## Dependency Matrix (abridged)

Direct deps (X) — sample rows for chokepoints:

| From \ To | Banking Services | Authority | Fin. Infra. | Internet | Energy* |
|---|---|---|---|---|---|
| Identity and Trust | X | X | I | I | I |
| Markets and Exchange | I | I | I | I | I |
| Banking Services | — | I | X | I | I |
| CBDC | I | I | X | I | I |
| Online Payments | I | I | X | I | I |
| Financial Infrastructure | I | I | — | X | I |

*Energy = any of {Minigrids, Renewable, Fossil}. Full edge list in the OWM block.

## Critical Path Analysis

**Primary path (anchor to deepest infrastructure):**
Individual → Inclusion → Identity and Trust → Banking Services → Online Payments → Financial Infrastructure → Internet Access → 5G / Satellite / Mesh / Copper → Renewable / Fossil Energy

**Bottlenecks and single points of failure:**

- **Identity and Trust** — every banking path and most authority paths pass through it. In underbanked regions this is frequently the binding constraint (no formal ID, no bank).
- **Internet Access** — pan-stack. Its last-mile form (5G / satellite / mesh / copper) varies sharply by locality; this is where "global commodity" meets "local constraint."
- **Authority and Governance** — gates both Fiat and CBDC; if local authority is weak or contested, the centralised currency path is fragile and Cryptocurrency's decentralised path gains relative weight.
- **Energy layer** — Mesh depends on Minigrids; 5G and Copper still lean on Fossil in many regions. Sustainability is a user need that depends on a still-non-renewable base.

**Resilience gaps:** Satellite + Renewable is the only energy-resilient path not dependent on Fossil. Mesh + Minigrids + Renewable is the locally-resilient fallback. Cryptocurrency + Consensus + Satellite provides a currency path independent of local Authority and local Banking Services.

## Validation Checklist

- [x] Chain starts with a genuine user need (individual seeking inclusion), not a solution
- [x] All 29 components are activities, capabilities, or forms — no people or teams
- [x] Chain reaches commodity level (energy, consensus, internet)
- [x] No orphan components — every node has at least one edge
- [x] DAG — no cycles (verified by inspection; all edges flow downward in visibility)
- [x] Visibility ordering — every edge A→B has ν(A) ≥ ν(B) (verified against validator rules)
- [x] Anchor visibility ≥ 0.90 (0.96)
- [x] 8–20 strategic components target exceeded intentionally to honour the scenario's explicit enumeration — still within strategic tolerance at 29

## Visibility Assessment Summary

| Band | Count | Components |
|---|---|---|
| 0.90–1.00 | 2 | Individual, Inclusion |
| 0.70–0.89 | 9 | Trade, Options, Equality, Sustainability, Identity, Risk, Behaviour, Markets, Authority |
| 0.50–0.69 | 7 | Redistribution, Banking Services, Online Payments, Bank Branches, Fiat, CBDC, Crypto |
| 0.30–0.49 | 5 | Financial Infrastructure, Consensus, Mobile Device, Internet Access |
| 0.10–0.29 | 5 | Computing Infra, 5G, Satellite, Mesh, Copper |
| 0.00–0.09 | 3 | Minigrids, Renewable, Fossil |

## Assumptions and Open Questions

- **Evolution axis deferred.** All components placed at ε=0.50 per the skill's partial-map contract. Build/buy positioning is a subsequent step (`$arckit-wardley`).
- **Region not specified.** "Underbanked region" is broad; sub-Saharan Africa, rural South Asia, and remote LATAM would tilt the network and energy sublayer differently (e.g., mobile money via feature phones replaces Mobile Device + Internet Access path in Kenya's M-Pesa model).
- **Redistribution placement.** Treated as a user-need-adjacent capability (state-to-individual). Could alternatively sit under Authority.
- **Consensus Algorithms** covers PoW/PoS/BFT families collectively — in a deeper map these would split, since their energy profiles differ sharply and affect Sustainability.
- **Behaviour and Literacy** is non-technical but modelled as a component because it is a capability that evolves and is depended on by adoption of Banking Services.

## Suggested Next Steps

- Run `$arckit-wardley` to position each component on the evolution axis and produce the full map.
- Split Consensus Algorithms by family (PoW vs PoS vs BFT) if sustainability analysis matters.
- Add a second value chain anchored on a regional operator or aid agency to surface redistribution dynamics.
