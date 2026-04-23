# Wardley Value Chain — Cybersecurity Risk Management (Executive View)

**Command**: `arckit-wardley.value-chain`
**Date**: 2023-05 (scenario as-of)
**Skill**: `arckit-wardley.value-chain` (partial-map — value-chain only; evolution positions are placeholders at ε = 0.50 and should be set in a subsequent `$arckit-wardley` pass)

## 1. Executive Summary

**Anchor**: *Executive can make defensible decisions about cyber risk.*
A 30-component value chain decomposes the executive need into three top-of-chain drivers (P&L protection, compliance obligation, risk appetite) and a board-reporting duty, cascading down through the risk-management apparatus (identification, registers, assessment, quantification, frameworks), the treatment mix (mitigate / transfer / accept + cyber insurance), the operational defence layer (monitoring, incident response, testing, pen-test, bug bounty), the tooling stack (SOC tooling, SIEM, EDR, vulnerability scanning), the emerging LLM angle (both defence and attack surface), and commodity infrastructure (identity, logging, cloud). Key structural insight: every treatment branch re-converges on a narrow commodity base (logging + cloud), while the top of the chain is dominated by human-judgement capabilities that regulators are shaping from outside the map.

## 2. Users and Personas

| Persona | Primary need | Role in chain |
|---|---|---|
| Executive (CEO / CFO / Board sponsor) | Make defensible cyber-risk decisions that protect P&L and meet regulators | Anchor |
| CISO | Translate executive appetite into a controls and reporting programme | Consumes Risk identification practice & Risk treatment mix |
| Risk & Compliance function | Evidence conformance with Risk and Compliance frameworks | Consumes Compliance framework, Risk framework |
| SOC / IR lead | Run the operational defence | Consumes Security monitoring, Incident response |
| Security testing team | Prove controls hold | Consumes Security testing |
| Insurance broker / underwriter | Price transferred risk | Consumes Cyber insurance |

## 3. Value Chain Diagram

### ASCII placeholder

```text
ν ≈ 0.97  Executive (anchor)
ν ≈ 0.86–0.90  P&L protection | Compliance obligation | Risk appetite | Board-level reporting
ν ≈ 0.76–0.78  Risk identification practice | Risk treatment mix
ν ≈ 0.58–0.70  Risk assessment methodology | Risk register | Compliance framework |
                Risk framework | Asset inventory | Risk quantification
ν ≈ 0.50–0.56  Mitigation controls | Risk transfer | Risk acceptance | Cyber insurance
ν ≈ 0.44–0.48  Incident response | Security monitoring | Security testing
ν ≈ 0.34–0.40  Penetration testing | Bug bounty | LLM attack surface |
                LLM-assisted defence | Vulnerability scanning
ν ≈ 0.26–0.30  SOC tooling | SIEM | EDR
ν ≈ 0.10–0.22  Identity and access | Logging and telemetry | Cloud compute
```

### OWM code block

> Evolution is a placeholder (ε = 0.50) at the value-chain stage. Assign real evolution positions with `$arckit-wardley` using the 19-row cheat sheet.

```owm
title Cybersecurity Risk Management - Executive View (May 2023)

anchor Executive [0.97, 0.50]

component P&L protection [0.90, 0.50]
component Compliance obligation [0.90, 0.50]
component Risk appetite [0.88, 0.50]
component Board-level reporting [0.86, 0.50]

component Risk identification practice [0.78, 0.50]
component Risk treatment mix [0.76, 0.50]

component Risk assessment methodology [0.70, 0.50]
component Risk register [0.68, 0.50]
component Compliance framework [0.66, 0.50]
component Risk framework [0.64, 0.50]
component Asset inventory [0.62, 0.50]
component Risk quantification [0.58, 0.50]

component Mitigation controls [0.56, 0.50]
component Risk transfer [0.54, 0.50]
component Risk acceptance [0.52, 0.50]
component Cyber insurance [0.50, 0.50]

component Incident response [0.48, 0.50]
component Security monitoring [0.46, 0.50]
component Security testing [0.44, 0.50]

component Penetration testing [0.40, 0.50]
component Bug bounty [0.38, 0.50]
component LLM attack surface [0.38, 0.50]
component LLM-assisted defence [0.36, 0.50]
component Vulnerability scanning [0.34, 0.50]

component SOC tooling [0.30, 0.50]
component SIEM [0.26, 0.50]
component EDR [0.26, 0.50]

component Identity and access [0.22, 0.50]
component Logging and telemetry [0.18, 0.50]
component Cloud compute [0.10, 0.50]

Executive -> P&L protection
Executive -> Compliance obligation
Executive -> Risk appetite
Executive -> Board-level reporting

P&L protection -> Risk identification practice
P&L protection -> Risk treatment mix
Compliance obligation -> Compliance framework
Compliance obligation -> Risk framework
Risk appetite -> Risk treatment mix
Risk appetite -> Risk quantification
Board-level reporting -> Risk register
Board-level reporting -> Risk quantification

Risk identification practice -> Asset inventory
Risk identification practice -> Risk assessment methodology
Risk identification practice -> Risk register
Risk identification practice -> LLM attack surface

Risk assessment methodology -> Risk quantification
Risk assessment methodology -> Risk framework
Compliance framework -> Risk framework
Risk register -> Asset inventory

Risk treatment mix -> Mitigation controls
Risk treatment mix -> Risk transfer
Risk treatment mix -> Risk acceptance
Risk transfer -> Cyber insurance

Mitigation controls -> Security monitoring
Mitigation controls -> Incident response
Mitigation controls -> Security testing
Mitigation controls -> Identity and access

Security testing -> Penetration testing
Security testing -> Bug bounty
Security testing -> Vulnerability scanning

Security monitoring -> SOC tooling
Security monitoring -> LLM-assisted defence
Incident response -> SOC tooling

SOC tooling -> SIEM
SOC tooling -> EDR
SIEM -> Logging and telemetry
EDR -> Logging and telemetry

LLM-assisted defence -> Logging and telemetry

Identity and access -> Cloud compute
Logging and telemetry -> Cloud compute
SIEM -> Cloud compute
EDR -> Cloud compute

style wardley
```

### Mermaid equivalent

<details>
<summary>Mermaid <code>wardley-beta</code> block</summary>

```mermaid
wardley-beta
title Cybersecurity Risk Management - Executive View (May 2023)
size [1100, 800]

anchor Executive [0.97, 0.50]

component "P&L protection" [0.90, 0.50]
component Compliance obligation [0.90, 0.50]
component Risk appetite [0.88, 0.50]
component "Board-level reporting" [0.86, 0.50]

component Risk identification practice [0.78, 0.50]
component Risk treatment mix [0.76, 0.50]

component Risk assessment methodology [0.70, 0.50]
component Risk register [0.68, 0.50]
component Compliance framework [0.66, 0.50]
component Risk framework [0.64, 0.50]
component Asset inventory [0.62, 0.50]
component Risk quantification [0.58, 0.50]

component Mitigation controls [0.56, 0.50]
component Risk transfer [0.54, 0.50]
component Risk acceptance [0.52, 0.50]
component Cyber insurance [0.50, 0.50]

component Incident response [0.48, 0.50]
component Security monitoring [0.46, 0.50]
component Security testing [0.44, 0.50]

component Penetration testing [0.40, 0.50]
component Bug bounty [0.38, 0.50]
component "LLM attack surface" [0.38, 0.50]
component "LLM-assisted defence" [0.36, 0.50]
component Vulnerability scanning [0.34, 0.50]

component SOC tooling [0.30, 0.50]
component SIEM [0.26, 0.50]
component EDR [0.26, 0.50]

component Identity and access [0.22, 0.50]
component Logging and telemetry [0.18, 0.50]
component Cloud compute [0.10, 0.50]

Executive -> "P&L protection"
Executive -> Compliance obligation
Executive -> Risk appetite
Executive -> "Board-level reporting"

"P&L protection" -> Risk identification practice
"P&L protection" -> Risk treatment mix
Compliance obligation -> Compliance framework
Compliance obligation -> Risk framework
Risk appetite -> Risk treatment mix
Risk appetite -> Risk quantification
"Board-level reporting" -> Risk register
"Board-level reporting" -> Risk quantification

Risk identification practice -> Asset inventory
Risk identification practice -> Risk assessment methodology
Risk identification practice -> Risk register
Risk identification practice -> "LLM attack surface"

Risk assessment methodology -> Risk quantification
Risk assessment methodology -> Risk framework
Compliance framework -> Risk framework
Risk register -> Asset inventory

Risk treatment mix -> Mitigation controls
Risk treatment mix -> Risk transfer
Risk treatment mix -> Risk acceptance
Risk transfer -> Cyber insurance

Mitigation controls -> Security monitoring
Mitigation controls -> Incident response
Mitigation controls -> Security testing
Mitigation controls -> Identity and access

Security testing -> Penetration testing
Security testing -> Bug bounty
Security testing -> Vulnerability scanning

Security monitoring -> SOC tooling
Security monitoring -> "LLM-assisted defence"
Incident response -> SOC tooling

SOC tooling -> SIEM
SOC tooling -> EDR
SIEM -> Logging and telemetry
EDR -> Logging and telemetry

"LLM-assisted defence" -> Logging and telemetry

Identity and access -> Cloud compute
Logging and telemetry -> Cloud compute
SIEM -> Cloud compute
EDR -> Cloud compute
```

</details>

## 4. Component Inventory

| # | Component | ν | Description | Depends on |
|---|---|---|---|---|
| 1 | Executive | 0.97 | Anchor — board-level decision-maker accountable for cyber posture | P&L, Compliance obligation, Risk appetite, Board-level reporting |
| 2 | P&L protection | 0.90 | Need to keep financial impact within tolerance | RIP, RTM |
| 3 | Compliance obligation | 0.90 | External duty (GDPR, DORA-precursors, NIS, sector rules) | Compliance framework, Risk framework |
| 4 | Risk appetite | 0.88 | Declared tolerance for residual risk | RTM, Risk quantification |
| 5 | Board-level reporting | 0.86 | Regular board/audit-committee reporting | Risk register, Risk quantification |
| 6 | Risk identification practice | 0.78 | The discipline of spotting new / changed risks | Asset inventory, RAM, Register, LLM attack surface |
| 7 | Risk treatment mix | 0.76 | Decision on mitigate / transfer / accept portfolio | Mitigation, Transfer, Acceptance |
| 8 | Risk assessment methodology | 0.70 | The *how* of scoring a risk | Quantification, Risk framework |
| 9 | Risk register | 0.68 | The live list of risks + owners + status | Asset inventory |
| 10 | Compliance framework | 0.66 | ISO 27001, SOC 2, PCI-DSS, HIPAA, sector regs | Risk framework |
| 11 | Risk framework | 0.64 | NIST RMF, ISO 31000 taxonomy backbone | — |
| 12 | Asset inventory | 0.62 | What you own that can be attacked | — |
| 13 | Risk quantification | 0.58 | FAIR, Monte-Carlo loss distribution, or heat-map likelihood × impact | — |
| 14 | Mitigation controls | 0.56 | The preventive + detective + responsive controls portfolio | Monitoring, IR, Testing, Identity |
| 15 | Risk transfer | 0.54 | Moving residual loss to a third party | Cyber insurance |
| 16 | Risk acceptance | 0.52 | Formally signed-off decision to tolerate residual | — |
| 17 | Cyber insurance | 0.50 | Insurable portion of the risk, increasingly demanded by carriers | — |
| 18 | Incident response | 0.48 | Detect → contain → eradicate → recover workflow | SOC tooling |
| 19 | Security monitoring | 0.46 | Continuous observation of telemetry | SOC tooling, LLM-assisted defence |
| 20 | Security testing | 0.44 | Proof the controls actually hold | Pen-test, Bug bounty, Vuln scanning |
| 21 | Penetration testing | 0.40 | Scoped adversary simulation | — |
| 22 | Bug bounty | 0.38 | Crowd-sourced vulnerability discovery | — |
| 23 | LLM attack surface | 0.38 | Prompt injection, data-leak, model supply chain — a new risk class | — |
| 24 | LLM-assisted defence | 0.36 | Triage + summarisation + detection-writing with LLMs | Logging |
| 25 | Vulnerability scanning | 0.34 | Automated CVE / config scanning | — |
| 26 | SOC tooling | 0.30 | The platform layer that runs the SOC | SIEM, EDR |
| 27 | SIEM | 0.26 | Log aggregation + correlation + alerting | Logging, Cloud |
| 28 | EDR | 0.26 | Endpoint detection + response agent | Logging, Cloud |
| 29 | Identity and access | 0.22 | Authentication + authorisation + privileged access | Cloud |
| 30 | Logging and telemetry | 0.18 | Raw event / trace / metric capture | Cloud |
| 31 | Cloud compute | 0.10 | Commodity compute / storage / network | — |

## 5. Dependency Matrix (abridged, X = direct, I = indirect, — = none)

| From ↓ / To → | RIP | RTM | RegisterReg | AI | Mit | SOC | Logging | Cloud |
|---|---|---|---|---|---|---|---|---|
| Executive | X | X | I | I | I | I | I | I |
| P&L protection | X | X | I | I | I | I | I | I |
| Risk appetite | I | X | I | I | I | I | I | I |
| RIP | — | — | X | X | — | — | — | I |
| RTM | — | — | — | — | X | I | I | I |
| Mitigation | — | — | — | — | — | X | I | I |
| SOC tooling | — | — | — | — | — | — | I | I |
| SIEM | — | — | — | — | — | — | X | X |

*(Full 31×31 matrix omitted — reconstructable from the edge list above.)*

## 6. Critical Path Analysis

### Longest path (anchor → deepest infrastructure)

`Executive → P&L protection → Risk treatment mix → Mitigation controls → Security monitoring → SOC tooling → SIEM → Logging and telemetry → Cloud compute` (9 hops).

### Single points of failure

- **Logging and telemetry** — three SOC-stack components (SIEM, EDR, LLM-assisted defence) plus cloud depend on it. Its failure blinds the SOC.
- **Asset inventory** — RIP, Risk register all rely on it. A poor inventory silently corrupts the whole top of the chain.
- **Risk framework** — Risk assessment methodology, Compliance framework and (implicitly) risk quantification taxonomy inherit from here. A shift (e.g. NIST CSF 2.0 in draft at time-of-map) ripples upward.
- **Cyber insurance market** — Risk transfer reduces to insurance; a hardening market (post-2022) narrows the viable treatment mix and forces more mitigation.

### Resilience gaps

- **LLM attack surface** is a new risk identified at the top of the chain but has **no corresponding mitigation control** explicitly in the chain — mitigation is implicit in "Mitigation controls" but not broken out. Flag for follow-up: is there an AI-policy / AI-specific control family?
- **Security testing** has three children (pen-test, bug bounty, vuln scan) but pen-test and bug bounty do not yet feed back into the Risk register automatically — a known scaling bottleneck.

## 7. Validation Checklist

**Completeness**
- [x] Chain starts with a genuine user need (not a solution or capability) — "Executive can make defensible cyber-risk decisions"
- [x] All significant dependencies captured (scenario items all mapped)
- [x] Chain reaches commodity level (Cloud compute, Logging)
- [x] No orphan components (every node has at least one edge)
- [x] Components are activities / capabilities / practices — not people or teams

**Accuracy**
- [x] Dependencies reflect real-world relationships
- [x] Visibility ordering consistent with dependency direction (manually verified: for every edge A→B, ν(A) ≥ ν(B))
- [x] No component is both user-facing and infrastructure
- [x] DAG acyclicity — verified by the strict-decreasing ν invariant: every edge drops ν, so no cycle is reachable

**Usefulness**
- [x] 31 components — within the 8–25 strategic band (slightly over, justified by scenario breadth across executive / compliance / treatment / ops / LLM axes)
- [x] Each component can carry a meaningful evolution score in the follow-up `$arckit-wardley` pass
- [x] Strategic insight surfaced: LLM is simultaneously a new risk class (at ν 0.38) and a new defence tool (at ν 0.36) — rare symmetry worth board discussion

## 8. Visibility Assessment

| Component | ν | Rationale |
|---|---|---|
| Executive | 0.97 | Anchor |
| P&L protection / Compliance obligation | 0.90 | Named drivers the exec is accountable for |
| Risk appetite | 0.88 | Exec articulates, slightly more internal-facing |
| Board-level reporting | 0.86 | Exec-visible output |
| Risk identification practice | 0.78 | CISO-visible, exec is briefed on it |
| Risk treatment mix | 0.76 | CISO-visible decision record |
| Risk assessment methodology | 0.70 | Risk team's working practice |
| Risk register | 0.68 | Exec sees summary; register itself is a risk-team artefact |
| Compliance framework / Risk framework | 0.64–0.66 | Named in audit but invisible to day-to-day ops |
| Asset inventory | 0.62 | Critical but rarely top-of-mind for exec |
| Risk quantification | 0.58 | Visible in board packs as numbers |
| Mitigation / Transfer / Acceptance | 0.52–0.56 | Treatment-layer plumbing |
| Cyber insurance | 0.50 | Visible in legal / finance, not daily ops |
| Incident response / Monitoring / Testing | 0.44–0.48 | Operational — visible only when things break |
| Pen-test / Bug bounty / LLM surfaces / Vuln scan | 0.34–0.40 | Technical practices, exec sees only summaries |
| SOC tooling | 0.30 | Platform layer |
| SIEM / EDR | 0.26 | Tooling products |
| Identity / Logging | 0.18–0.22 | Deep plumbing |
| Cloud compute | 0.10 | Commodity substrate |

## 9. Assumptions and Open Questions

**Assumptions**
1. The executive perspective is a commercial / regulated-sector exec, not a public-sector one — May 2023 context implies DORA-precursor and SEC-incident-disclosure pressure, not a specific UK-GOV frame.
2. "Compliance framework" is separated from "Risk framework" because, in practice, ISO 27001 / SOC 2 are compliance-scoped while NIST RMF / ISO 31000 are risk-scoped. They share a dependency from Compliance framework → Risk framework.
3. LLM is treated as *both* a new risk class and a new defence capability — reflecting the May 2023 inflection point (GPT-4 public ~2 months earlier).
4. Cyber insurance is modelled as a component of Risk transfer rather than a peer of Mitigation — reflecting carrier-market reality post-2022 hardening.
5. Mitigate / Transfer / Accept are modelled as three siblings under Risk treatment mix, not a single component, so evolution can score them differently in the follow-up.

**Open questions for `$arckit-wardley` pass**
- Is AI-policy a separate control family that should sit under Mitigation controls?
- Should SOAR be split out from SOC tooling? Left folded for 2023-era unification narrative.
- Are risk quantification methods (FAIR vs heat-map) evolving at the same pace, or should they be decomposed?
- What is the current state of NIST CSF 2.0 draft adoption vs 1.1 — does it materially move Risk framework on the evolution axis?

## 10. Skill-Scope Disclosure

This skill (`arckit-wardley.value-chain`) produces a **partial map**: components, dependencies, and visibility are set; the evolution axis is a placeholder (ε = 0.50 for every component). To obtain full Wardley Map placements — Genesis / Custom Built / Product / Commodity — run `$arckit-wardley` against this chain using the 19-row cheat sheet from `docs/core/part-6-cheat-sheet-scoring.md`.

---

**Generated by**: `arckit-wardley.value-chain`
**Generated on**: 2026-04-23 (for a scenario as-of May 2023)
**Notes**: Blind benchmark run — no reference map read. Evolution placeholders (ε = 0.50) intentional per skill scope.
