# Wardley Value Chain — Government Digital Identity (November 2022)

**Document ID**: ARC-GOVDID-WVCH-001-v1.0
**Date**: 2026-04-23
**Document Type**: Wardley Value Chain
**Command**: `arckit.wardley.value-chain`
**Classification**: PUBLIC
**Owner**: [PENDING]
**Reviewer**: [PENDING]
**Approver**: [PENDING]
**Distribution**: Project Team, Architecture Team

## Executive Summary

**Anchor**: A citizen can prove who they are to access public and private services.

This value chain decomposes the landscape of government digital identity as it stood in November 2022. The chain runs from the citizen's service-access need, through the regulatory and trust apparatus that governs assertion, down through the canonical identity stack (service → claims → credentials → identity → identification → identifiers → authority) and terminates in commodity transport. Sixteen components are identified across roughly six dependency levels. The chain surfaces three strategic tensions raised in the scenario: (1) centralised issuing authority competing with self-sovereign identifier management, (2) rules-and-exception machinery creating a lever that bad actors exploit, and (3) the uneven evolution of digital identification relative to still-physical identification.

Note: actors named in the scenario (government, society, citizens, corporations, entities, bad actors) are **users/stakeholders**, not value-chain components. They appear in the Users and Personas section.

## Users and Personas

| User / Stakeholder | Primary Need |
|---|---|
| Citizen (end user) | Prove identity once, access many services, retain privacy and recourse |
| Government (service provider) | Identify entitled recipients, prevent fraud, satisfy statutory duty |
| Society (collective) | Trustworthy attribution without surveillance overreach |
| Corporations (relying parties) | Verify claims at low cost, meet KYC/AML obligations |
| Entities (non-human: companies, devices) | Establish provenance and delegated authority |
| Bad actors (adversarial) | Exploit rule gaps, impersonation, and exception paths |

Primary anchor user: **Citizen**.

## Anchor Statement

```text
Anchor: Citizen can prove who they are to access public and private services.
User: Citizen
Outcome: Citizen gains authorised access to a service with proportionate disclosure.
```

## Value Chain Diagram (ASCII)

```
visibility
  1.0  Citizen Access to Services
       |
  0.9  Service Delivery
       |    \
  0.8  Regulation and Rules    Trust Assessment
       |     \                   |
       |      Exception Handling |
  0.7  Claims Exchange     Power Relations
       |
  0.6  Verifiable Credentials
       |
  0.5  Identity Assertion
       | \
  0.5  Physical Identification    Digital Identification
       |
  0.4  Authority and Issuance
       |
  0.3  Identifier Management -> Connectedness Graph
       |
  0.2  Cryptographic Key Material     Biometric Capture
       |
  0.0  Transport Layer
```

## OWM Syntax

```text
title Government Digital Identity — Value Chain (November 2022)

anchor Citizen Access to Services [0.97, 0.50]

component Service Delivery [0.90, 0.50]
component Regulation and Rules [0.86, 0.50]
component Exception Handling [0.82, 0.50]
component Trust Assessment [0.80, 0.50]
component Claims Exchange [0.74, 0.50]
component Power Relations [0.70, 0.50]
component Verifiable Credentials [0.66, 0.50]
component Identity Assertion [0.58, 0.50]
component Physical Identification [0.52, 0.50]
component Digital Identification [0.52, 0.50]
component Authority and Issuance [0.46, 0.50]
component Identifier Management [0.38, 0.50]
component Connectedness Graph [0.32, 0.50]
component Cryptographic Key Material [0.24, 0.50]
component Biometric Capture [0.22, 0.50]
component Transport Layer [0.08, 0.50]

Citizen Access to Services -> Service Delivery
Citizen Access to Services -> Regulation and Rules
Citizen Access to Services -> Trust Assessment
Service Delivery -> Claims Exchange
Service Delivery -> Power Relations
Service Delivery -> Transport Layer
Regulation and Rules -> Exception Handling
Regulation and Rules -> Authority and Issuance
Trust Assessment -> Claims Exchange
Trust Assessment -> Authority and Issuance
Claims Exchange -> Verifiable Credentials
Claims Exchange -> Transport Layer
Verifiable Credentials -> Identity Assertion
Verifiable Credentials -> Cryptographic Key Material
Identity Assertion -> Physical Identification
Identity Assertion -> Digital Identification
Physical Identification -> Identifier Management
Physical Identification -> Biometric Capture
Digital Identification -> Identifier Management
Digital Identification -> Cryptographic Key Material
Digital Identification -> Transport Layer
Authority and Issuance -> Identifier Management
Authority and Issuance -> Cryptographic Key Material
Identifier Management -> Connectedness Graph
Identifier Management -> Transport Layer
Connectedness Graph -> Transport Layer
Power Relations -> Authority and Issuance
Exception Handling -> Identity Assertion

style wardley
```

<details>
<summary>Mermaid wardley-beta equivalent</summary>

```mermaid
wardley-beta
title Government Digital Identity — Value Chain (November 2022)
size [1100, 800]
anchor "Citizen Access to Services" [0.97, 0.50]
component "Service Delivery" [0.90, 0.50]
component "Regulation and Rules" [0.86, 0.50]
component "Exception Handling" [0.82, 0.50]
component "Trust Assessment" [0.80, 0.50]
component "Claims Exchange" [0.74, 0.50]
component "Power Relations" [0.70, 0.50]
component "Verifiable Credentials" [0.66, 0.50]
component "Identity Assertion" [0.58, 0.50]
component "Physical Identification" [0.52, 0.50]
component "Digital Identification" [0.52, 0.50]
component "Authority and Issuance" [0.46, 0.50]
component "Identifier Management" [0.38, 0.50]
component "Connectedness Graph" [0.32, 0.50]
component "Cryptographic Key Material" [0.24, 0.50]
component "Biometric Capture" [0.22, 0.50]
component "Transport Layer" [0.08, 0.50]
"Citizen Access to Services" -> "Service Delivery"
"Citizen Access to Services" -> "Regulation and Rules"
"Citizen Access to Services" -> "Trust Assessment"
"Service Delivery" -> "Claims Exchange"
"Service Delivery" -> "Power Relations"
"Service Delivery" -> "Transport Layer"
"Regulation and Rules" -> "Exception Handling"
"Regulation and Rules" -> "Authority and Issuance"
"Trust Assessment" -> "Claims Exchange"
"Trust Assessment" -> "Authority and Issuance"
"Claims Exchange" -> "Verifiable Credentials"
"Claims Exchange" -> "Transport Layer"
"Verifiable Credentials" -> "Identity Assertion"
"Verifiable Credentials" -> "Cryptographic Key Material"
"Identity Assertion" -> "Physical Identification"
"Identity Assertion" -> "Digital Identification"
"Physical Identification" -> "Identifier Management"
"Physical Identification" -> "Biometric Capture"
"Digital Identification" -> "Identifier Management"
"Digital Identification" -> "Cryptographic Key Material"
"Digital Identification" -> "Transport Layer"
"Authority and Issuance" -> "Identifier Management"
"Authority and Issuance" -> "Cryptographic Key Material"
"Identifier Management" -> "Connectedness Graph"
"Identifier Management" -> "Transport Layer"
"Connectedness Graph" -> "Transport Layer"
"Power Relations" -> "Authority and Issuance"
"Exception Handling" -> "Identity Assertion"
```

</details>

## Component Inventory

| # | Component | Visibility | Description | Depends On |
|---|---|---|---|---|
| 1 | Citizen Access to Services | 0.97 | Anchor: user need for authorised service access | Service Delivery; Regulation and Rules; Trust Assessment |
| 2 | Service Delivery | 0.90 | The public/private service transaction itself | Claims Exchange; Power Relations; Transport Layer |
| 3 | Regulation and Rules | 0.86 | Statutory and regulatory frame (GDPR, eIDAS, etc.) | Exception Handling; Authority and Issuance |
| 4 | Exception Handling | 0.82 | Manual override, edge-case, and assisted digital paths | Identity Assertion |
| 5 | Trust Assessment | 0.80 | Evaluation of benevolence, capability, integrity of counterparty | Claims Exchange; Authority and Issuance |
| 6 | Claims Exchange | 0.74 | Conveyance of asserted attributes between parties | Verifiable Credentials; Transport Layer |
| 7 | Power Relations | 0.70 | Power-over, power-with, power-to shaping consent and coercion | Authority and Issuance |
| 8 | Verifiable Credentials | 0.66 | Cryptographically signed claim containers | Identity Assertion; Cryptographic Key Material |
| 9 | Identity Assertion | 0.58 | The act of asserting who one is in a transaction | Physical Identification; Digital Identification |
| 10 | Physical Identification | 0.52 | Document-based, in-person identification | Identifier Management; Biometric Capture |
| 11 | Digital Identification | 0.52 | Remote, digital-native identification flows | Identifier Management; Cryptographic Key Material; Transport Layer |
| 12 | Authority and Issuance | 0.46 | Centralised, decentralised, and issuing authority for identity | Identifier Management; Cryptographic Key Material |
| 13 | Identifier Management | 0.38 | Mutable and immutable identifier lifecycle (allocation, resolution, revocation) | Connectedness Graph; Transport Layer |
| 14 | Connectedness Graph | 0.32 | Relationships that make identifiers meaningful across services | Transport Layer |
| 15 | Cryptographic Key Material | 0.24 | Keys, signatures, HSMs, PKI primitives | — (terminal within chain) |
| 16 | Biometric Capture | 0.22 | Sensor-level capture of fingerprint, face, iris | — (terminal within chain) |
| 17 | Transport Layer | 0.08 | The internet and underlying networks | — (commodity) |

## Dependency Matrix (direct X, indirect I)

| From \ To | SD | RR | EH | TA | CE | PR | VC | IA | PI | DI | AI | IM | CG | CK | BC | TL |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Citizen Access | X | X | I | X | I | I | I | I | I | I | I | I | I | I | I | I |
| Service Delivery | — | I | I | I | X | X | I | I | I | I | I | I | I | I | I | X |
| Regulation and Rules | — | — | X | — | I | I | I | I | I | I | X | I | I | I | I | I |
| Exception Handling | — | — | — | — | I | I | I | X | I | I | I | I | I | I | I | I |
| Trust Assessment | — | — | — | — | X | — | I | I | I | I | X | I | I | I | I | I |
| Claims Exchange | — | — | — | — | — | — | X | I | I | I | I | I | I | I | I | X |
| Power Relations | — | — | — | — | — | — | — | I | I | I | X | I | I | I | I | I |
| Verifiable Credentials | — | — | — | — | — | — | — | X | I | I | I | I | I | X | I | I |
| Identity Assertion | — | — | — | — | — | — | — | — | X | X | I | I | I | I | I | I |
| Physical Identification | — | — | — | — | — | — | — | — | — | — | I | X | I | I | X | I |
| Digital Identification | — | — | — | — | — | — | — | — | — | — | I | X | I | X | I | X |
| Authority and Issuance | — | — | — | — | — | — | — | — | — | — | — | X | I | X | I | I |
| Identifier Management | — | — | — | — | — | — | — | — | — | — | — | — | X | I | I | X |
| Connectedness Graph | — | — | — | — | — | — | — | — | — | — | — | — | — | I | I | X |

## Critical Path Analysis

**Deepest chain (anchor to commodity)**:

`Citizen Access to Services → Service Delivery → Claims Exchange → Verifiable Credentials → Identity Assertion → Digital Identification → Identifier Management → Connectedness Graph → Transport Layer`

**Bottlenecks / single points of failure**:

- **Identifier Management** — the joint point where both physical and digital identification, and centralised and decentralised authority, must land. A break here is felt everywhere.
- **Authority and Issuance** — governs who gets to say who someone is. Concentration creates systemic risk; fragmentation creates trust-arbitrage opportunities for bad actors.
- **Cryptographic Key Material** — underpins Verifiable Credentials, Digital Identification, and Authority; compromised key material cascades through three branches.
- **Transport Layer** — the internet is a shared commodity and a single dependency for the digital half of the chain.

**Resilience gaps**:

- No independent assurance path below Trust Assessment other than Claims Exchange and Authority — there is no mapped "attestor of attestors."
- Exception Handling reaches back up into Identity Assertion; rules-with-exceptions is a known vector for bad-actor exploitation (social engineering, assisted-digital abuse).
- Biometric Capture is a terminal leaf — irrevocable, and its compromise cannot be undone like a key can be rotated.

## Strategic Tensions Surfaced by the Chain

1. **Centralised vs self-sovereign authority**: Authority and Issuance sits at the same level whether centralised or decentralised, but drives divergent Identifier Management approaches (mutable directory vs immutable DID-style identifiers). Choosing one shapes everything above it.
2. **Rules with exceptions as an attack surface**: Exception Handling's upward dependency into Identity Assertion means that every codified exception is a bypass path. Bad actors operate here, not on the cryptography.
3. **Physical vs digital identification co-equal in 2022**: These are shown at the same visibility because, as of November 2022, a large share of identity-establishing events still required a physical document; digital-native establishment was not yet the dominant path.
4. **Trust is an upper-chain component, not a lower one**: Trust Assessment sits near the anchor because it is a user-facing judgement about counterparties, decomposed into benevolence, capability, and integrity — these are not cryptographic primitives and should not be conflated with them.

## Validation Checklist

- [x] Chain starts with a genuine user need (citizen service access), not a solution
- [x] All significant dependencies captured; no orphans
- [x] Chain reaches commodity level (Transport Layer / internet)
- [x] All components are capabilities/activities/practices, not actors (actors moved to Users and Personas)
- [x] Dependencies reflect real technical and institutional relationships
- [x] Visibility ordering is consistent with dependency direction (parent >= child on every edge — manually verified)
- [x] Anchor visibility >= 0.90 (0.97)
- [x] DAG: no cycles (manually traced)
- [x] Granularity: 16 components + anchor, within the 8–20 target
- [x] Each component is individually positionable on evolution (deferred to `$arckit-wardley`)
- [x] Chain surfaces strategic insights (centralised vs SSI, exception-handling as attack surface, physical/digital parity)

## Visibility Assessment Rationale

| Component | Visibility | Rationale |
|---|---|---|
| Citizen Access to Services | 0.97 | Anchor; the felt user need |
| Service Delivery | 0.90 | The interaction the user is actually doing |
| Regulation and Rules | 0.86 | Visible to the user via consent notices, forms, and refusals |
| Exception Handling | 0.82 | Visible when the normal path fails; the "press 0 for an agent" moment |
| Trust Assessment | 0.80 | Conscious user judgement of counterparties |
| Claims Exchange | 0.74 | Partly visible — the user sees claims being moved but not the protocol |
| Power Relations | 0.70 | Felt rather than seen (consent pressure, coercion, agency) |
| Verifiable Credentials | 0.66 | Visible when the user holds a wallet; otherwise inferred |
| Identity Assertion | 0.58 | The user performs it but is not taught its mechanics |
| Physical Identification | 0.52 | Co-equal with digital in Nov 2022 |
| Digital Identification | 0.52 | Co-equal with physical in Nov 2022 |
| Authority and Issuance | 0.46 | Institutional; named on credentials but not user-operated |
| Identifier Management | 0.38 | Infrastructure with user-visible symptoms (change of address, replacement card) |
| Connectedness Graph | 0.32 | Operational; users rarely see it |
| Cryptographic Key Material | 0.24 | Infrastructure; silent when it works |
| Biometric Capture | 0.22 | Momentarily visible at enrolment, invisible after |
| Transport Layer | 0.08 | Deep commodity; users only notice when it fails |

## Assumptions and Open Questions

**Assumptions**:

- The anchor is the citizen, not the relying party (bank, employer). A relying-party anchor would re-rank Trust Assessment and Claims Exchange upward.
- "Identifiers (mutable, immutable, connectedness)" is captured as two components: Identifier Management (covering the mutable/immutable lifecycle) and Connectedness Graph (covering the relational dimension).
- "Authority (centralised, decentralised, issuing)" is collapsed into one component — Authority and Issuance — because in a value chain they occupy the same dependency slot; the *choice* between them is an evolution and gameplay question for the full map.
- Actors listed in the scenario (government, society, citizens, corporations, entities, bad actors) are kept out of the chain per the skill's explicit guidance that components must be capabilities, not actors.

**Open questions**:

- Should Biometric Capture and Physical Identification be merged? They decouple at the evolution axis but at the value-chain level they are tightly bound.
- Is there a missing "Audit and Recourse" component that should sit alongside Exception Handling? The scenario mentions bad-actor exploitation of rules — recourse is the user-side counterpart.
- Where does machine identity (for "entities" in the scenario) fit? It is plausibly a second anchor ("Entity can prove itself to a service"). This chain is human-centric by default.

## External References

None supplied for this run (no `external/` documents available at run time).

## Next Steps

- Run `$arckit-wardley` to add the evolution axis, turning this value chain into a full Wardley Map.
- Run `$arckit-wardley.doctrine` to assess the organisational capability to hold centralised-vs-SSI tension.
- Re-run with relying-party anchor (bank/employer) for contrastive mapping.

---

**Generated by**: ArcKit `$arckit-wardley.value-chain` command
**Generated on**: 2026-04-23 (blind benchmark run, arckit-value-chain skill)
**Project**: Government Digital Identity (November 2022)
**AI Model**: claude-opus-4-7 (1M context)
**Generation Context**: Blind benchmark; no external or reference documents read.
