# Risk Management in Financial Services — Value Chain

## Executive Summary

**Anchor:** Public, Corporations, and Governments need trusted financial services where risk is managed, visible, and accountable. Three anchor user groups consume financial services (retail banking, insurance, lending) that depend on a trust-and-assets layer, are shaped by regulation and rating agencies, and are exposed to five risk types (credit, systemic, cybersecurity, cascade failure, third-party). The chain terminates in an accountability-to-society loop and a cost/value/supply-chain-awareness foundation. Strategic insights: regulation sits notably lower than the risk it governs — indicating regulatory lag; trust sits high in visibility but depends on deeply-hidden supply-chain awareness; and third-party and cascade failure risks are the least-visible risk types despite being the fastest-evolving.

## Users and Personas

| User | Primary Need |
|------|--------------|
| Public (individuals/households) | Safe deposits, affordable credit, insurable lives and property |
| Corporations | Working capital, risk transfer, payments infrastructure |
| Governments | Financial stability, tax base protection, sovereignty of financial system |

## Value Chain Diagram

```text
VIS   COMPONENTS
0.95  [Public] [Corporations] [Governments]
0.80  [Retail Banking] [Insurance] [Lending]
0.70  [Customer Relationships] [Trust] [Assets]
0.55  [Regulation] [Rating Agencies] [Sovereignty]
0.45  [Credit Risk] [Systemic Risk] [Cybersecurity Risk] [Third-Party Risk] [Cascade Failure Risk]
0.35  [Accountability] [Society]
0.25  [Value] [Cost] [Supply-Chain Awareness]
```

### OWM Syntax

```owm
title Risk Management in Financial Services

anchor Public [0.95, 0.50]
anchor Corporations [0.95, 0.50]
anchor Governments [0.95, 0.50]

component Retail Banking [0.82, 0.50]
component Insurance [0.80, 0.50]
component Lending [0.80, 0.50]

component Trust [0.70, 0.50]
component Assets [0.68, 0.50]
component Customer Relationships [0.72, 0.50]

component Regulation [0.58, 0.50]
component Rating Agencies [0.55, 0.50]
component Sovereignty [0.50, 0.50]

component Credit Risk [0.48, 0.50]
component Systemic Risk [0.45, 0.50]
component Cybersecurity Risk [0.46, 0.50]
component Cascade Failure Risk [0.42, 0.50]
component Third Party Risk [0.44, 0.50]

component Accountability [0.38, 0.50]
component Society [0.32, 0.50]

component Cost [0.25, 0.50]
component Value [0.28, 0.50]
component Supply Chain Awareness [0.22, 0.50]

Public -> Retail Banking
Public -> Insurance
Public -> Lending
Corporations -> Retail Banking
Corporations -> Insurance
Corporations -> Lending
Governments -> Regulation
Governments -> Sovereignty

Retail Banking -> Trust
Retail Banking -> Customer Relationships
Retail Banking -> Assets
Insurance -> Trust
Insurance -> Customer Relationships
Insurance -> Assets
Lending -> Trust
Lending -> Customer Relationships
Lending -> Assets

Retail Banking -> Regulation
Insurance -> Regulation
Lending -> Regulation
Retail Banking -> Rating Agencies
Insurance -> Rating Agencies
Lending -> Rating Agencies

Trust -> Credit Risk
Trust -> Systemic Risk
Trust -> Cybersecurity Risk
Assets -> Credit Risk
Customer Relationships -> Cybersecurity Risk
Regulation -> Systemic Risk
Regulation -> Cascade Failure Risk
Regulation -> Third Party Risk
Rating Agencies -> Credit Risk

Credit Risk -> Accountability
Systemic Risk -> Accountability
Cybersecurity Risk -> Accountability
Cascade Failure Risk -> Accountability
Third Party Risk -> Accountability

Accountability -> Society
Sovereignty -> Society

Cost -> Supply Chain Awareness
Value -> Cost
Trust -> Value
Assets -> Cost

style wardley
```

<details>
<summary>Mermaid wardley-beta equivalent</summary>

```mermaid
wardley-beta
title Risk Management in Financial Services
size [1100, 800]

anchor Public [0.95, 0.50]
anchor Corporations [0.95, 0.50]
anchor Governments [0.95, 0.50]

component "Retail Banking" [0.82, 0.50]
component Insurance [0.80, 0.50]
component Lending [0.80, 0.50]

component Trust [0.70, 0.50]
component Assets [0.68, 0.50]
component "Customer Relationships" [0.72, 0.50]

component Regulation [0.58, 0.50]
component "Rating Agencies" [0.55, 0.50]
component Sovereignty [0.50, 0.50]

component "Credit Risk" [0.48, 0.50]
component "Systemic Risk" [0.45, 0.50]
component "Cybersecurity Risk" [0.46, 0.50]
component "Cascade Failure Risk" [0.42, 0.50]
component "Third Party Risk" [0.44, 0.50]

component Accountability [0.38, 0.50]
component Society [0.32, 0.50]

component Cost [0.25, 0.50]
component Value [0.28, 0.50]
component "Supply Chain Awareness" [0.22, 0.50]

Public -> "Retail Banking"
Public -> Insurance
Public -> Lending
Corporations -> "Retail Banking"
Corporations -> Insurance
Corporations -> Lending
Governments -> Regulation
Governments -> Sovereignty

"Retail Banking" -> Trust
"Retail Banking" -> "Customer Relationships"
"Retail Banking" -> Assets
Insurance -> Trust
Insurance -> "Customer Relationships"
Insurance -> Assets
Lending -> Trust
Lending -> "Customer Relationships"
Lending -> Assets

"Retail Banking" -> Regulation
Insurance -> Regulation
Lending -> Regulation
"Retail Banking" -> "Rating Agencies"
Insurance -> "Rating Agencies"
Lending -> "Rating Agencies"

Trust -> "Credit Risk"
Trust -> "Systemic Risk"
Trust -> "Cybersecurity Risk"
Assets -> "Credit Risk"
"Customer Relationships" -> "Cybersecurity Risk"
Regulation -> "Systemic Risk"
Regulation -> "Cascade Failure Risk"
Regulation -> "Third Party Risk"
"Rating Agencies" -> "Credit Risk"

"Credit Risk" -> Accountability
"Systemic Risk" -> Accountability
"Cybersecurity Risk" -> Accountability
"Cascade Failure Risk" -> Accountability
"Third Party Risk" -> Accountability

Accountability -> Society
Sovereignty -> Society

Cost -> "Supply Chain Awareness"
Value -> Cost
Trust -> Value
Assets -> Cost
```

</details>

## Component Inventory

| Component | Visibility | Description |
|-----------|------------|-------------|
| Public | 0.95 | Individuals and households — anchor user group |
| Corporations | 0.95 | Business customers — anchor user group |
| Governments | 0.95 | Sovereign actors demanding stability — anchor user group |
| Retail Banking | 0.82 | Deposit-taking and payments provider |
| Insurance | 0.80 | Risk-transfer provider |
| Lending | 0.80 | Credit provision |
| Customer Relationships | 0.72 | Direct channel trust and servicing |
| Trust | 0.70 | Perceived reliability and solvency |
| Assets | 0.68 | Balance-sheet instruments backing obligations |
| Regulation | 0.58 | Rules constraining providers |
| Rating Agencies | 0.55 | Third-party creditworthiness assessment |
| Sovereignty | 0.50 | National control over monetary/financial system |
| Credit Risk | 0.48 | Risk of borrower default |
| Cybersecurity Risk | 0.46 | Risk of data/system compromise |
| Systemic Risk | 0.45 | Risk of sector-wide contagion |
| Third-Party Risk | 0.44 | Risk from vendors and counterparties |
| Cascade Failure Risk | 0.42 | Risk of chain-reaction collapse across providers |
| Accountability | 0.38 | Mechanisms linking failures to consequences |
| Society | 0.32 | Broader social receiver of externalities |
| Value | 0.28 | Outcome worth delivered to users |
| Cost | 0.25 | Price of operating the chain |
| Supply Chain Awareness | 0.22 | Visibility into upstream provider dependencies |

## Dependency Matrix (summary)

Direct dependencies (X):

- Public, Corporations -> Retail Banking, Insurance, Lending
- Governments -> Regulation, Sovereignty
- Providers (Retail Banking, Insurance, Lending) -> Trust, Assets, Customer Relationships, Regulation, Rating Agencies
- Trust -> Credit Risk, Systemic Risk, Cybersecurity Risk, Value
- Assets -> Credit Risk, Cost
- Customer Relationships -> Cybersecurity Risk
- Regulation -> Systemic Risk, Cascade Failure Risk, Third-Party Risk
- Rating Agencies -> Credit Risk
- All risk types -> Accountability -> Society
- Sovereignty -> Society
- Value -> Cost -> Supply-Chain Awareness

## Critical Path Analysis

**Primary critical path:** Public -> Retail Banking -> Trust -> Systemic Risk -> Accountability -> Society

**Bottlenecks / single points of failure:**

- **Trust**: three provider types all depend on it; degradation cascades widely.
- **Regulation**: the only dependency path for three of the five risk types (systemic, cascade, third-party).
- **Accountability**: narrow funnel — all five risk types collapse into it before reaching Society.

**Resilience gaps:**

- Supply-Chain Awareness sits at the bottom, implying it is the most evolved/commodity-like foundation — but in reality financial firms often lack visibility into their third-party chain. The low position reflects *structural* dependency, not *actual* maturity.
- Cascade Failure Risk has only Regulation as a parent; if regulation lags, cascade risk is effectively unmanaged.

## Validation Checklist

- [x] Chain starts with genuine user needs (Public, Corporations, Governments) — not solutions.
- [x] All three anchors present, each with >= 0.90 visibility.
- [x] Dependencies captured across provider, trust/assets, oversight, risk, accountability, and cost layers.
- [x] Chain reaches commodity-like foundations (Supply-Chain Awareness).
- [x] No orphan components — every node has >=1 edge.
- [x] All components are capabilities/activities/practices, not actors. (Exception: anchor user groups, which are user-need bearers by design.)
- [x] Visibility ordering consistent with dependency direction (parents >= children along every edge).
- [x] DAG: no cycles — verified by hand-tracing the 7 visibility tiers.
- [x] Granularity 22 components — within the 8-25 strategic-clarity band.

## Visibility Assessment

| Tier | Range | Components |
|------|-------|-----------|
| Anchor (user-facing) | 0.90-1.00 | Public, Corporations, Governments |
| High | 0.70-0.89 | Retail Banking, Insurance, Lending, Customer Relationships, Trust |
| Medium-High | 0.50-0.69 | Assets, Regulation, Rating Agencies, Sovereignty |
| Medium | 0.30-0.49 | Credit/Systemic/Cybersecurity/Cascade/Third-Party Risk, Accountability, Society |
| Low | 0.10-0.29 | Value, Cost, Supply-Chain Awareness |

## Assumptions and Open Questions

**Assumptions:**

1. "Accountability chain back to society" is modelled as a single Accountability node fed by all risk types, terminating at Society. An alternative model would split political, legal, and reputational accountability.
2. Regulation is placed *below* the providers it shapes (because providers depend on regulation) but *above* the risks it is meant to cover (which matches the scenario's framing of regulatory lag).
3. Rating Agencies are modelled as a peer of Regulation rather than a child — they are an external oversight mechanism, not a regulated output.
4. Cost, Value, Supply-Chain Awareness form a separate economic-foundation strand that the scenario asked to locate on the evolution axis; at the value-chain stage we only place them on visibility. Evolution is set to 0.50 placeholder per skill contract.

**Open questions:**

1. Should "Trust" be split into retail trust vs. institutional (interbank) trust? They evolve at different rates.
2. Is Sovereignty truly a child of Governments, or a peer constraint that cross-cuts regulation and rating agencies?
3. Does Cybersecurity Risk warrant its own dedicated sub-chain (identity, data, network) or is a single node sufficient at strategic granularity?

## Generation Metadata

- **Skill**: arckit-wardley.value-chain (partial-map skill; components + visibility only; evolution=0.50 placeholder)
- **Scenario**: finance-risk — Risk management across financial services
- **Components**: 22 (3 anchors + 19 supporting components)
- **Dependency edges**: 43
- **Visibility tiers**: 7 levels from 0.22 to 0.95
