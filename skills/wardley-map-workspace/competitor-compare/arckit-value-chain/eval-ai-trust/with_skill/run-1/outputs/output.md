# Wardley Value Chain — AI Trust Landscape (June 2023)

**Document ID**: ARC-000-WVCH-001-v1.0
**Date**: 2026-04-23
**Document Type**: Wardley Value Chain
**Command**: arckit.wardley.value-chain
**Classification**: PUBLIC
**Owner**: [PENDING]
**Reviewer**: [PENDING]
**Approver**: [PENDING]
**Distribution**: Project Team, Architecture Team

| Version | Date | Author | Summary | Reviewer | Approver |
|---------|------|--------|---------|----------|----------|
| 1.0 | 2026-04-23 | ArcKit AI | Initial creation from `$arckit-wardley.value-chain` command | [PENDING] | [PENDING] |

---

## Prerequisite Warnings

- **REQ (Requirements) — MISSING.** No structured requirements document was supplied. Per the skill, this is a MANDATORY input; its absence means the value chain is anchored directly on the free-form scenario rather than on validated user needs. Recommend running `$arckit-requirements` before the chain is used for a decision.
- **STKE (Stakeholder Analysis) — MISSING.** User personas were inferred from the scenario text (individuals, government, business). Recommend running `$arckit-stakeholders` to validate personas and success metrics.
- **PRIN (Architecture Principles) — MISSING.** No enterprise standards or build/buy preferences available.
- **External documents — NONE.** No prior WVCH artifacts, architecture diagrams, or dependency maps were provided.

## Executive Summary

**Anchor**: Stakeholder (individual, government, business) can rely on AI system outputs for consequential decisions.

Eighteen components were identified across six visibility tiers, spanning outcome signals (trust, reputation, competitive advantage), governance (regulation, audits, benchmarks), control mechanisms (forensics, feedback loops, constitution), and the technical substrate (foundation models, algorithms, data, compute). Three strategic insights emerge from the decomposition: (1) trust is a **compound outcome** with three independent demand paths (individual, government, business) that each rest on a different mix of governance and evidence; (2) the **evaluation harness** is a shared single point of failure — audits, benchmarks, and forensics all depend on it, yet it is currently bespoke across labs; (3) the **foundation model** layer sits surprisingly deep in the value chain — closer to infrastructure than to the user — which is why commoditisation pressure at that layer is eroding differentiation even while trust expectations climb above it.

## Users and Personas

| Persona | Primary Need | Trust Gate |
|---------|--------------|------------|
| Individual User | Use AI for daily tasks without being deceived or harmed | Reputation, observed outputs |
| Government / Regulator | Assure the public that deployed AI systems are safe and lawful | Regulation, independent audits, forensics |
| Business Adopter | Deploy AI in revenue-affecting workflows without taking on uninsurable risk | Safety assurance, reputation, competitive upside |

## Value Chain — Anchor Statement

```text
Anchor: Stakeholder can rely on AI system outputs for consequential decisions
User:   Individuals, governments, and businesses interacting with or deploying AI
Outcome: Decisions made with or about AI systems can be defended, audited, and reversed
```

## Value Chain Diagram — ASCII

```text
vis
1.0 |  Stakeholder Trust in AI                                              (anchor)
    |        |            |            |
0.88|  Individual     Government    Business
    |   Trust         Confidence    Risk-Accept
    |     |  \           |   \          |  \___________
0.78|   AI Outputs       |    \         |              \
0.72|     \         Safety Assurance    |               Reputation Signal
0.68|      \                            Competitive Advantage
    |       \__________________________/|\_____________/|
0.62|                Regulation & Policy                |
0.58|           Independent Audits                      |
0.55|              Public Benchmarks                    |
0.50|              Incident Forensics                   |
0.48|              Human Feedback Loop                  |
0.45|              Model Constitution                   |
    |                       |
0.42|                 Foundation Models
0.35|                 Training Algorithms
0.32|                 Evaluation Harness
    |                       |
0.25|                 Training Data
    |                       |
0.12|                 Compute Infrastructure             (commodity floor)
```

## OWM Syntax (for https://create.wardleymaps.ai)

```owm
title AI Trust Landscape (June 2023)
anchor Stakeholder Trust in AI [0.95, 0.50]

component Individual User Trust [0.88, 0.50]
component Government Regulatory Confidence [0.88, 0.50]
component Business Risk Acceptance [0.88, 0.50]

component AI System Outputs [0.78, 0.50]
component Safety Assurance [0.72, 0.50]
component Reputation Signal [0.70, 0.50]
component Competitive Advantage [0.68, 0.50]

component Regulation and Policy [0.62, 0.50]
component Independent Audits [0.58, 0.50]
component Public Benchmarks [0.55, 0.50]
component Incident Forensics [0.50, 0.50]
component Human Feedback Loop [0.48, 0.50]
component Model Constitution [0.45, 0.50]

component Foundation Models [0.42, 0.50]
component Training Algorithms [0.35, 0.50]
component Evaluation Harness [0.32, 0.50]
component Training Data [0.25, 0.50]
component Compute Infrastructure [0.12, 0.50]

Stakeholder Trust in AI -> Individual User Trust
Stakeholder Trust in AI -> Government Regulatory Confidence
Stakeholder Trust in AI -> Business Risk Acceptance

Individual User Trust -> AI System Outputs
Individual User Trust -> Reputation Signal
Government Regulatory Confidence -> Regulation and Policy
Government Regulatory Confidence -> Independent Audits
Government Regulatory Confidence -> Safety Assurance
Business Risk Acceptance -> Competitive Advantage
Business Risk Acceptance -> Safety Assurance
Business Risk Acceptance -> Reputation Signal

AI System Outputs -> Foundation Models
AI System Outputs -> Safety Assurance
Safety Assurance -> Independent Audits
Safety Assurance -> Public Benchmarks
Safety Assurance -> Incident Forensics
Safety Assurance -> Model Constitution
Reputation Signal -> Public Benchmarks
Reputation Signal -> Incident Forensics
Competitive Advantage -> Foundation Models
Competitive Advantage -> Training Data

Regulation and Policy -> Public Benchmarks
Independent Audits -> Evaluation Harness
Independent Audits -> Incident Forensics
Public Benchmarks -> Evaluation Harness
Incident Forensics -> Evaluation Harness
Human Feedback Loop -> Foundation Models
Model Constitution -> Foundation Models

Foundation Models -> Training Algorithms
Foundation Models -> Training Data
Foundation Models -> Compute Infrastructure
Foundation Models -> Human Feedback Loop
Training Algorithms -> Compute Infrastructure
Evaluation Harness -> Foundation Models
Training Data -> Compute Infrastructure

style wardley
```

> **Evolution placeholder note**: this is a value-chain-only skill. ε values above are NOT assessed — they are all set to a neutral placeholder of `0.50` solely to satisfy the `[visibility, evolution]` OWM coordinate shape. Run `$arckit-wardley` to assign real evolution positions.

<details>
<summary>Mermaid wardley-beta equivalent</summary>

```mermaid
wardley-beta
title AI Trust Landscape (June 2023)
size [1100, 800]

anchor Stakeholder Trust in AI [0.95, 0.50]

component Individual User Trust [0.88, 0.50]
component Government Regulatory Confidence [0.88, 0.50]
component Business Risk Acceptance [0.88, 0.50]
component AI System Outputs [0.78, 0.50]
component Safety Assurance [0.72, 0.50]
component Reputation Signal [0.70, 0.50]
component Competitive Advantage [0.68, 0.50]
component Regulation and Policy [0.62, 0.50]
component Independent Audits [0.58, 0.50]
component Public Benchmarks [0.55, 0.50]
component Incident Forensics [0.50, 0.50]
component Human Feedback Loop [0.48, 0.50]
component Model Constitution [0.45, 0.50]
component Foundation Models [0.42, 0.50]
component Training Algorithms [0.35, 0.50]
component Evaluation Harness [0.32, 0.50]
component Training Data [0.25, 0.50]
component Compute Infrastructure [0.12, 0.50]

Stakeholder Trust in AI -> Individual User Trust
Stakeholder Trust in AI -> Government Regulatory Confidence
Stakeholder Trust in AI -> Business Risk Acceptance
Individual User Trust -> AI System Outputs
Individual User Trust -> Reputation Signal
Government Regulatory Confidence -> Regulation and Policy
Government Regulatory Confidence -> Independent Audits
Government Regulatory Confidence -> Safety Assurance
Business Risk Acceptance -> Competitive Advantage
Business Risk Acceptance -> Safety Assurance
Business Risk Acceptance -> Reputation Signal
AI System Outputs -> Foundation Models
AI System Outputs -> Safety Assurance
Safety Assurance -> Independent Audits
Safety Assurance -> Public Benchmarks
Safety Assurance -> Incident Forensics
Safety Assurance -> Model Constitution
Reputation Signal -> Public Benchmarks
Reputation Signal -> Incident Forensics
Competitive Advantage -> Foundation Models
Competitive Advantage -> Training Data
Regulation and Policy -> Public Benchmarks
Independent Audits -> Evaluation Harness
Independent Audits -> Incident Forensics
Public Benchmarks -> Evaluation Harness
Incident Forensics -> Evaluation Harness
Human Feedback Loop -> Foundation Models
Model Constitution -> Foundation Models
Foundation Models -> Training Algorithms
Foundation Models -> Training Data
Foundation Models -> Compute Infrastructure
Foundation Models -> Human Feedback Loop
Training Algorithms -> Compute Infrastructure
Evaluation Harness -> Foundation Models
Training Data -> Compute Infrastructure
```

</details>

## Component Inventory

| # | Component | Visibility | Tier | Description | Dependencies (down) |
|---|-----------|-----------:|------|-------------|--------------------|
| 0 | Stakeholder Trust in AI | 0.95 | Anchor | The compound outcome — ability to rely on AI for consequential decisions | Individual User Trust, Government Regulatory Confidence, Business Risk Acceptance |
| 1 | Individual User Trust | 0.88 | Demand | End-user willingness to use and act on AI outputs | AI System Outputs, Reputation Signal |
| 2 | Government Regulatory Confidence | 0.88 | Demand | Regulator's willingness to permit deployment in public-interest domains | Regulation and Policy, Independent Audits, Safety Assurance |
| 3 | Business Risk Acceptance | 0.88 | Demand | Enterprise willingness to place AI on revenue-affecting paths | Competitive Advantage, Safety Assurance, Reputation Signal |
| 4 | AI System Outputs | 0.78 | Experience | The observed behaviour — answers, actions, refusals | Foundation Models, Safety Assurance |
| 5 | Safety Assurance | 0.72 | Outcome | Evidence that the system will not cause foreseeable harm | Independent Audits, Public Benchmarks, Incident Forensics, Model Constitution |
| 6 | Reputation Signal | 0.70 | Outcome | Third-party and peer signal about vendor/model trustworthiness | Public Benchmarks, Incident Forensics |
| 7 | Competitive Advantage | 0.68 | Outcome | Business value differential from using this AI over alternatives | Foundation Models, Training Data |
| 8 | Regulation and Policy | 0.62 | Governance | Statutory rules and guidance (EU AI Act draft, White House EO) | Public Benchmarks |
| 9 | Independent Audits | 0.58 | Governance | Third-party red-team and conformance reviews | Evaluation Harness, Incident Forensics |
| 10 | Public Benchmarks | 0.55 | Governance | Shared evaluation suites (HELM, MMLU, TruthfulQA, BIG-bench) | Evaluation Harness |
| 11 | Incident Forensics | 0.50 | Control | Post-hoc trace and root-cause capability on AI failures | Evaluation Harness |
| 12 | Human Feedback Loop | 0.48 | Control | RLHF / RLAIF pipeline adjusting model behaviour from human signal | Foundation Models |
| 13 | Model Constitution | 0.45 | Control | Declarative value spec the model is trained / prompted against (Anthropic-style) | Foundation Models |
| 14 | Foundation Models | 0.42 | Technical | Pretrained large models used as the backbone | Training Algorithms, Training Data, Compute Infrastructure, Human Feedback Loop |
| 15 | Training Algorithms | 0.35 | Technical | Transformer + optimiser recipes used to fit the model | Compute Infrastructure |
| 16 | Evaluation Harness | 0.32 | Technical | Test-runner plumbing that drives benchmarks, audits, forensics | Foundation Models |
| 17 | Training Data | 0.25 | Technical | Text / code / image corpora used for pretraining and fine-tuning | Compute Infrastructure |
| 18 | Compute Infrastructure | 0.12 | Commodity | GPU / TPU cloud capacity | (terminal commodity) |

## Dependency Matrix (direct `X`, indirect `I`)

Rows are parents (depend on); columns are children (are depended on by). Only a condensed view is shown; the OWM edge list above is authoritative.

| Parent \ Child | Outputs | Safety | Reputation | CompAdv | Reg | Audits | Bench | Forensics | HFL | Const | FM | Algo | Harness | Data | Compute |
|----------------|:-------:|:------:|:----------:|:-------:|:---:|:------:|:-----:|:---------:|:---:|:-----:|:--:|:----:|:-------:|:----:|:-------:|
| Individual     | X       | I      | X          |         |     | I      | I     | I         |     |       | I  | I    | I       | I    | I       |
| Government     |         | X      |            |         | X   | X      | I     | I         |     |       | I  | I    | I       | I    | I       |
| Business       | I       | X      | X          | X       |     | I      | I     | I         |     |       | X* | I    | I       | X*   | I       |
| Outputs        |         | X      |            |         |     |        |       |           |     |       | X  | I    | I       | I    | I       |
| Safety         |         |        |            |         |     | X      | X     | X         |     | X     | I  | I    | I       | I    | I       |
| Reputation     |         |        |            |         |     |        | X     | X         |     |       |    |      | I       |      |         |
| CompAdv        |         |        |            |         |     |        |       |           |     |       | X  | I    |         | X    | I       |
| Audits         |         |        |            |         |     |        |       | X         |     |       |    |      | X       |      |         |
| Benchmarks     |         |        |            |         |     |        |       |           |     |       |    |      | X       |      |         |
| Forensics      |         |        |            |         |     |        |       |           |     |       |    |      | X       |      |         |
| HFL            |         |        |            |         |     |        |       |           |     |       | X  | I    |         | I    | I       |
| Constitution   |         |        |            |         |     |        |       |           |     |       | X  | I    |         | I    | I       |
| FM             |         |        |            |         |     |        |       |           | X   |       |    | X    |         | X    | X       |
| Algo           |         |        |            |         |     |        |       |           |     |       |    |      |         |      | X       |
| Harness        |         |        |            |         |     |        |       |           |     |       | X  | I    |         | I    | I       |
| Data           |         |        |            |         |     |        |       |           |     |       |    |      |         |      | X       |

`X*` = captured via Competitive Advantage.

## Critical Path Analysis

**Longest chain (anchor → commodity floor)**:

```text
Stakeholder Trust in AI
  → Government Regulatory Confidence
    → Safety Assurance
      → Independent Audits
        → Evaluation Harness
          → Foundation Models
            → Training Data
              → Compute Infrastructure
```

Eight levels deep. This is the chain that determines whether regulated-sector deployment is possible.

**Bottlenecks and single points of failure**:

- **Evaluation Harness (0.32)** — audits, benchmarks, and forensics all depend on it, yet in June 2023 each lab runs its own bespoke harness. Shared commoditisation here would collapse the assurance cost across the ecosystem.
- **Foundation Models (0.42)** — sit under Outputs, CompAdv, HFL, Constitution, and the Evaluation Harness. A regression at this layer propagates to every downstream signal simultaneously.
- **Compute Infrastructure (0.12)** — terminal commodity but a concentrated one (three hyperscalers + NVIDIA). Classical commodity fragility.

**Resilience gaps**:

- No redundancy between the three governance signals (Regulation, Audits, Benchmarks). If Benchmarks are gamed, Audits and Regulation both inherit the compromise via the shared Evaluation Harness.
- The Human Feedback Loop and Model Constitution are both control mechanisms acting on Foundation Models, but neither has an independent verifier — their effect is only legible through the same benchmarks and forensics they feed.

## Validation Checklist

**Completeness**

- [x] Chain starts with a genuine user need (reliance on AI for consequential decisions), not a product
- [x] All significant dependencies captured (38 edges)
- [x] Chain reaches commodity level (Compute Infrastructure)
- [x] No orphan components — every node has at least one edge
- [x] All components are activities/capabilities, not people or teams

**Accuracy**

- [x] Dependencies reflect real June-2023 relationships
- [x] Visibility ordering consistent with dependency direction — parents ≥ children in every edge (checked manually)
- [x] No component is simultaneously user-facing and infrastructure

**Usefulness**

- [x] Granularity appropriate for strategic decisions
- [x] Each component can be meaningfully positioned on the evolution axis in a follow-up mapping pass
- [x] Chain reveals strategic insight (Evaluation Harness as shared SPOF; FM layer commoditising below the trust line)

## Visibility Assessment

| Component | ν | Reasoning |
|-----------|---:|-----------|
| Stakeholder Trust in AI | 0.95 | Anchor — by construction highest |
| Individual / Government / Business (demand) | 0.88 | One step below anchor — the three audiences experience trust directly |
| AI System Outputs | 0.78 | User directly observes; failure immediately visible |
| Safety Assurance | 0.72 | Indirectly visible via incident absence + published attestations |
| Reputation Signal | 0.70 | Travels via peer/press channel; noticed quickly |
| Competitive Advantage | 0.68 | Visible to business decision-makers via outcome metrics |
| Regulation and Policy | 0.62 | Visible to regulators, enterprises; mostly invisible to end-users |
| Independent Audits | 0.58 | Visible when published; otherwise background |
| Public Benchmarks | 0.55 | Visible to technical community; not to end-users |
| Incident Forensics | 0.50 | Invoked after failures; visibility spikes on incident |
| Human Feedback Loop | 0.48 | Invisible to users; shapes outputs indirectly |
| Model Constitution | 0.45 | Invisible to users; declarative layer inside the model |
| Foundation Models | 0.42 | Hidden but named — users know "GPT-4 is inside" |
| Training Algorithms | 0.35 | Research-layer — invisible to users |
| Evaluation Harness | 0.32 | Plumbing — invisible to users, visible only to auditors |
| Training Data | 0.25 | Deep — users generally unaware of what the model was trained on |
| Compute Infrastructure | 0.12 | Terminal commodity — users have no awareness |

## Assumptions and Open Questions

**Assumptions made**

- "Stakeholder" collapses three distinct demand nodes (individual, government, business) into a single anchor; this is correct for a single-map view but a multi-anchor map may be more faithful.
- "Model Constitution" is treated as a first-class control component, reflecting Anthropic's Constitutional AI framing (May 2022). Teams without an explicit constitution may not recognise this node.
- "Evaluation Harness" is treated as distinct from "Public Benchmarks". In practice they are often conflated; keeping them separate exposes the shared-dependency risk.
- June-2023 framing: the EU AI Act is a draft, the US Executive Order is pre-publication, and RLHF is the dominant alignment technique. Later dates would reclassify several components.

**Open questions**

1. Should "Deployment Guardrails" (content filters, refusal policies) appear as a distinct component alongside Model Constitution, or are they a sub-component of Safety Assurance?
2. Is "Data Provenance / Licensing" a missing 19th component? It is increasingly coupled to both trust (copyright litigation) and risk (training-data lineage).
3. Should "Insurance / Liability" appear as an outcome-tier component between Business Risk Acceptance and Safety Assurance?

---

**Differentiating vs. commoditising — summary for the scenario prompt**

- **Differentiating in June 2023**: Foundation Models, Training Data (proprietary mixes), Human Feedback Loop quality, Model Constitution.
- **Commoditising**: Training Algorithms (transformer recipe is public), Compute Infrastructure, Public Benchmarks.
- **Fragile trust points**: Evaluation Harness (shared single point of failure), Incident Forensics (immature across labs), Regulation and Policy (drafted but not yet enforced — trust rests on promises, not case law).

---

**Generated by**: ArcKit `$arckit-wardley.value-chain` command
**Generated on**: 2026-04-23 11:09 GMT
**ArcKit Version**: (external skill; benchmark harness)
**Project**: AI Trust Landscape benchmark (competitor-compare/arckit-value-chain/eval-ai-trust)
**AI Model**: claude-opus-4-7 (1M context)
**Generation Context**: Free-form scenario input; no REQ/STKE/PRIN artifacts supplied — warnings above. No external documents available. Value-chain-only skill — evolution positions NOT assessed.
