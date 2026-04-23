# Wardley Value Chain: Lifelong Education and Learning

## Executive Summary

**Anchor**: "Learner gains the skills and recognised credentials to thrive in work and life."

This value chain decomposes the lifelong learning landscape into 20 components spanning four levels from user-facing experience down to commodity infrastructure. Four first-order capabilities hang directly off the anchor: the **curriculum and learning experience**, **credentialing and recognition**, **employability and status signalling**, and **inclusive access**. The chain exposes two concentration points of power — **Regulation and Accreditation** (which gates who can issue recognised credentials and what counts as a degree) and **Skills Frameworks and Standards** (which decide what a skill is before it is taught or assessed). A third structural feature is that **Digital Identity** and **Data and Learning Records** increasingly sit beneath both credentialing and labour-market signals, making them shared-infrastructure concerns rather than niceties.

Per the partial-map convention, all components are placed at evolution ε = 0.50 (placeholder) — evolution assessment is deferred to a subsequent full-map pass.

## Users and Personas

| Persona | Primary need |
|---|---|
| Learner (student, worker, returner, retiree) | Acquire skills and recognised credentials over a lifetime |
| Employer | Identify and hire capable people; fund upskilling of staff |
| Educator (teacher, tutor, mentor) | Help learners progress; have their teaching recognised |
| Institution (school, college, university, platform) | Offer curricula and credentials at scale and remain viable |
| Government / Regulator | Ensure quality, access, and alignment with labour-market needs |
| Wider community | Informal learning, apprenticeship, civic participation |

The **learner** is treated as the anchor user. Other actors appear in the chain as supporting roles inside capabilities (e.g., educators inside *Teaching and Tutoring*, regulators inside *Regulation and Accreditation*).

## Value Chain Diagram

### ASCII sketch

```
Visibility  Components
─────────  ─────────────────────────────────────────────────
0.95       Learner Thriving (anchor)
0.80       Curriculum & Learning Experience | Credentialing & Recognition
           Employability & Status Signalling | Inclusive Access
0.60       Teaching & Tutoring | Curriculum Design | Assessment & Verification
           Credential Issuance | Community Learning
0.40       Skills Frameworks & Standards | AI Tutors | Content Production
           Learning Delivery Platform | Digital Identity | Labour Market Signals
0.20       Regulation & Accreditation | Funding & Subsidy | Data & Learning Records
0.10       Connectivity | Cloud Compute & Storage
```

### OWM code

```text
title Lifelong Learning Value Chain

anchor Learner Thriving [0.95, 0.50]

component Curriculum and Learning Experience [0.82, 0.50]
component Credentialing and Recognition [0.80, 0.50]
component Employability and Status Signalling [0.78, 0.50]
component Inclusive Access [0.76, 0.50]

component Teaching and Tutoring [0.66, 0.50]
component Curriculum Design [0.64, 0.50]
component Assessment and Verification [0.62, 0.50]
component Credential Issuance [0.60, 0.50]
component Community Learning [0.58, 0.50]

component Skills Frameworks and Standards [0.46, 0.50]
component AI Tutors [0.44, 0.50]
component Content Production [0.42, 0.50]
component Learning Delivery Platform [0.40, 0.50]
component Digital Identity [0.38, 0.50]
component Labour Market Signals [0.36, 0.50]

component Regulation and Accreditation [0.24, 0.50]
component Funding and Subsidy [0.22, 0.50]
component Data and Learning Records [0.18, 0.50]
component Connectivity [0.12, 0.50]
component Cloud Compute and Storage [0.08, 0.50]

Learner Thriving -> Curriculum and Learning Experience
Learner Thriving -> Credentialing and Recognition
Learner Thriving -> Employability and Status Signalling
Learner Thriving -> Inclusive Access

Curriculum and Learning Experience -> Teaching and Tutoring
Curriculum and Learning Experience -> Curriculum Design
Curriculum and Learning Experience -> Community Learning
Credentialing and Recognition -> Assessment and Verification
Credentialing and Recognition -> Credential Issuance
Employability and Status Signalling -> Credential Issuance
Employability and Status Signalling -> Labour Market Signals
Inclusive Access -> Learning Delivery Platform
Inclusive Access -> Funding and Subsidy

Teaching and Tutoring -> AI Tutors
Teaching and Tutoring -> Content Production
Teaching and Tutoring -> Learning Delivery Platform
Curriculum Design -> Skills Frameworks and Standards
Curriculum Design -> Content Production
Assessment and Verification -> Skills Frameworks and Standards
Assessment and Verification -> Digital Identity
Credential Issuance -> Digital Identity
Credential Issuance -> Regulation and Accreditation
Community Learning -> Learning Delivery Platform

Skills Frameworks and Standards -> Regulation and Accreditation
AI Tutors -> Cloud Compute and Storage
AI Tutors -> Data and Learning Records
Content Production -> Cloud Compute and Storage
Learning Delivery Platform -> Cloud Compute and Storage
Learning Delivery Platform -> Connectivity
Digital Identity -> Data and Learning Records
Labour Market Signals -> Data and Learning Records

Regulation and Accreditation -> Funding and Subsidy
Data and Learning Records -> Cloud Compute and Storage
Connectivity -> Cloud Compute and Storage

style wardley
```

### Mermaid wardley-beta equivalent

<details>
<summary>Mermaid rendering</summary>

```mermaid
wardley-beta
    title Lifelong Learning Value Chain
    size [1100, 800]

    anchor Learner Thriving [0.95, 0.50]

    component Curriculum and Learning Experience [0.82, 0.50]
    component Credentialing and Recognition [0.80, 0.50]
    component Employability and Status Signalling [0.78, 0.50]
    component Inclusive Access [0.76, 0.50]

    component Teaching and Tutoring [0.66, 0.50]
    component Curriculum Design [0.64, 0.50]
    component Assessment and Verification [0.62, 0.50]
    component Credential Issuance [0.60, 0.50]
    component Community Learning [0.58, 0.50]

    component Skills Frameworks and Standards [0.46, 0.50]
    component AI Tutors [0.44, 0.50]
    component Content Production [0.42, 0.50]
    component Learning Delivery Platform [0.40, 0.50]
    component Digital Identity [0.38, 0.50]
    component Labour Market Signals [0.36, 0.50]

    component Regulation and Accreditation [0.24, 0.50]
    component Funding and Subsidy [0.22, 0.50]
    component Data and Learning Records [0.18, 0.50]
    component Connectivity [0.12, 0.50]
    component Cloud Compute and Storage [0.08, 0.50]

    Learner Thriving -> Curriculum and Learning Experience
    Learner Thriving -> Credentialing and Recognition
    Learner Thriving -> Employability and Status Signalling
    Learner Thriving -> Inclusive Access

    Curriculum and Learning Experience -> Teaching and Tutoring
    Curriculum and Learning Experience -> Curriculum Design
    Curriculum and Learning Experience -> Community Learning
    Credentialing and Recognition -> Assessment and Verification
    Credentialing and Recognition -> Credential Issuance
    Employability and Status Signalling -> Credential Issuance
    Employability and Status Signalling -> Labour Market Signals
    Inclusive Access -> Learning Delivery Platform
    Inclusive Access -> Funding and Subsidy

    Teaching and Tutoring -> AI Tutors
    Teaching and Tutoring -> Content Production
    Teaching and Tutoring -> Learning Delivery Platform
    Curriculum Design -> Skills Frameworks and Standards
    Curriculum Design -> Content Production
    Assessment and Verification -> Skills Frameworks and Standards
    Assessment and Verification -> Digital Identity
    Credential Issuance -> Digital Identity
    Credential Issuance -> Regulation and Accreditation
    Community Learning -> Learning Delivery Platform

    Skills Frameworks and Standards -> Regulation and Accreditation
    AI Tutors -> Cloud Compute and Storage
    AI Tutors -> Data and Learning Records
    Content Production -> Cloud Compute and Storage
    Learning Delivery Platform -> Cloud Compute and Storage
    Learning Delivery Platform -> Connectivity
    Digital Identity -> Data and Learning Records
    Labour Market Signals -> Data and Learning Records

    Regulation and Accreditation -> Funding and Subsidy
    Data and Learning Records -> Cloud Compute and Storage
    Connectivity -> Cloud Compute and Storage
```

</details>

## Component Inventory

| # | Component | Visibility | Description | Depends on |
|---|---|---|---|---|
| 1 | Learner Thriving | 0.95 | Anchor: learner gains skills and recognised credentials to thrive in work and life | 2, 3, 4, 5 |
| 2 | Curriculum and Learning Experience | 0.82 | The experienced curriculum — formal and informal — as learners encounter it | 6, 7, 10 |
| 3 | Credentialing and Recognition | 0.80 | The outcome of being formally recognised: degrees, micro-credentials, badges | 8, 9 |
| 4 | Employability and Status Signalling | 0.78 | How credentials translate into jobs, pay, status, institutional brand | 9, 15 |
| 5 | Inclusive Access | 0.76 | Access on equal terms — online/physical split, affordability, accommodations | 13, 17 |
| 6 | Teaching and Tutoring | 0.66 | The act of teaching, whether by human, AI, peer, or mentor | 11, 12, 13 |
| 7 | Curriculum Design | 0.64 | Designing what is taught and sequencing it | 10, 12 |
| 8 | Assessment and Verification | 0.62 | Measuring whether the learner has learned and authenticating the attempt | 10, 14 |
| 9 | Credential Issuance | 0.60 | Producing and signing the degree, certificate, or badge | 14, 16 |
| 10 | Community Learning | 0.58 | Clubs, libraries, peer networks, apprenticeship-style informal learning | 13 |
| 11 | Skills Frameworks and Standards | 0.46 | Taxonomies of what counts as a skill (e.g., ESCO, O*NET, sector standards) | 16 |
| 12 | AI Tutors | 0.44 | Generative AI tutors, adaptive learning engines | 19, 20 |
| 13 | Content Production | 0.42 | Authoring learning materials (courses, videos, practice items) | 19, 20 |
| 14 | Learning Delivery Platform | 0.40 | LMS / MOOC / classroom-management platform through which learning is delivered | 19, 20 |
| 15 | Digital Identity | 0.38 | A learner's verifiable digital identity used to bind credentials to a person | 18 |
| 16 | Labour Market Signals | 0.36 | Job-posting signals, employer preferences, wage premia by credential | 18 |
| 17 | Regulation and Accreditation | 0.24 | Government and sector bodies deciding what counts as a recognised qualification | 19 |
| 18 | Funding and Subsidy | 0.22 | Public funding, student loans, employer sponsorship, grants | — |
| 19 | Data and Learning Records | 0.18 | Longitudinal record of a learner's activity, results, and credentials | 20 |
| 20 | Connectivity | 0.12 | Broadband, mobile data that reaches the learner | 20 |
| 21 | Cloud Compute and Storage | 0.08 | Commodity cloud hosting | — |

Note: Funding and Subsidy is depended on by Regulation and Accreditation (the state funds the regulator and the institutions it oversees) and by Inclusive Access. Connectivity sits above Cloud Compute and Storage as its commodity parent.

## Dependency Matrix

Rows depend on columns. X = direct, I = indirect. Abbreviated to capture the load-bearing relationships.

|  | Teach | Curr-Des | Assess | Cred-Iss | Commun | Skills-Std | AITut | Content | Platform | DigID | LabSig | RegAcc | Fund | Data | Conn | Cloud |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Curriculum Experience | X | X | I | I | X | I | I | I | I | I | — | I | I | I | I | I |
| Credentialing | I | I | X | X | — | I | — | — | — | I | — | I | I | I | I | I |
| Employability | — | — | I | X | — | — | — | — | — | I | X | I | I | X | — | I |
| Inclusive Access | — | — | — | — | I | — | — | — | X | — | — | — | X | — | I | I |
| Teaching | — | — | — | — | — | — | X | X | X | — | — | — | — | I | I | I |
| Curriculum Design | — | — | — | — | — | X | — | X | — | — | — | I | — | — | — | I |
| Assessment | — | — | — | — | — | X | — | — | — | X | — | I | — | I | — | I |
| Credential Issuance | — | — | — | — | — | — | — | — | — | X | — | X | I | I | — | I |
| AI Tutors | — | — | — | — | — | — | — | — | — | — | — | — | — | X | — | X |
| Delivery Platform | — | — | — | — | — | — | — | — | — | — | — | — | — | — | X | X |

## Critical Path Analysis

**Deepest path:**
Learner Thriving → Credentialing and Recognition → Credential Issuance → Digital Identity → Data and Learning Records → Cloud Compute and Storage.

This path covers six levels and is the backbone of what society actually needs from formal education — that someone be able to reliably say "this person holds this qualification."

**Bottlenecks and single points of failure:**

- **Regulation and Accreditation** is the upstream constraint on what credentials exist and who may issue them. It is the largest concentration of power in the chain and sits directly above Funding.
- **Skills Frameworks and Standards** acts as the semantic bottleneck — if a skill is not in the framework, it tends not to be taught, not assessed, and not priced by the labour market. Curriculum Design and Assessment both go through it.
- **Digital Identity** is a shared dependency of both Credential Issuance and Assessment, and increasingly of Labour Market Signals via verified records. It is beginning to behave like a utility but is unevenly available across jurisdictions.
- **Data and Learning Records** becomes a single point of failure as portable learning records become the substrate for credentialing, AI tutoring, and labour-market matching.

**Resilience gaps:**

- Community Learning is attached to the chain but is brittle — its funding routes and standards recognition are weak, which tends to exclude informal/artisanal learning from recognised credentials.
- Inclusive Access depends on Funding and Delivery Platform; failure of either pushes the chain back toward in-person, fee-paying institutions and widens the inclusion gap.
- AI Tutors and Content Production both rely on Data and Learning Records without that link being well governed.

## Validation Checklist

**Completeness**

- [x] Chain starts with a genuine user need — "Learner gains skills and recognised credentials to thrive in work and life" — not a solution
- [x] All significant dependencies between components are captured
- [x] Chain reaches commodity level (Cloud Compute and Storage, Connectivity)
- [x] No orphan components — every component connects
- [x] All components are capabilities, activities, or practices — not people or teams

**Accuracy**

- [x] Dependencies reflect real-world technical and operational relationships
- [x] Visibility ordering is consistent with dependency direction (ν(a) ≥ ν(b) for every edge a → b)
- [x] No component is both high-level user-facing and low-level infrastructure

**Usefulness**

- [x] Granularity appropriate for strategic decision-making (20 components, 4 levels)
- [x] Each component can be placed on the evolution axis in a subsequent full-map pass
- [x] Chain surfaces strategic insights about power concentration (regulation, standards, digital identity)

## Visibility Assessment

| Component | Visibility | Rationale |
|---|---|---|
| Learner Thriving | 0.95 | Anchor; outcome the learner experiences directly |
| Curriculum and Learning Experience | 0.82 | Directly experienced by the learner day-to-day |
| Credentialing and Recognition | 0.80 | Directly felt at graduation / hiring moments |
| Employability and Status Signalling | 0.78 | Experienced through job market outcomes |
| Inclusive Access | 0.76 | Experienced when a learner can or cannot participate |
| Teaching and Tutoring | 0.66 | One step behind the experience — mediates curriculum |
| Curriculum Design | 0.64 | Learners rarely see design; they see its output |
| Assessment and Verification | 0.62 | Felt at exam points; hidden between them |
| Credential Issuance | 0.60 | Felt once per credential; invisible otherwise |
| Community Learning | 0.58 | Informal; felt by some, invisible to others |
| Skills Frameworks and Standards | 0.46 | Shapes what is taught but rarely seen by learners |
| AI Tutors | 0.44 | Can be user-facing but typically sits inside a platform |
| Content Production | 0.42 | Felt as "materials" not as a production process |
| Learning Delivery Platform | 0.40 | User-facing when failing; invisible when smooth |
| Digital Identity | 0.38 | Experienced at login/verification; otherwise hidden |
| Labour Market Signals | 0.36 | Felt indirectly through hiring and wages |
| Regulation and Accreditation | 0.24 | Invisible to learners, central for institutions |
| Funding and Subsidy | 0.22 | Invisible except at fees / loan moments |
| Data and Learning Records | 0.18 | Infrastructural substrate, invisible to learners |
| Connectivity | 0.12 | Infrastructure; felt only when absent |
| Cloud Compute and Storage | 0.08 | Deep commodity infrastructure |

## Assumptions and Open Questions

**Assumptions made**

- The learner is the primary user. Employers, educators, and regulators appear as actors inside capabilities rather than as separate anchors. A parallel chain could be drawn with the employer as anchor ("Employer acquires capable workers") and would share much of the lower half.
- "Lifelong" is taken to span school-age to post-retirement; the anchor does not privilege any life stage.
- Formal and informal curricula are both encompassed in Curriculum and Learning Experience; the formal/informal split is handled at evolution-axis time rather than at value-chain time.
- AI Tutors is modelled as a component within Teaching and Tutoring rather than as a separate anchor capability, on the basis that it is a means of delivering teaching rather than a user need of its own.
- Degrees and micro-credentials/badges are both produced by Credential Issuance; their difference is a matter of evolution and issuer, not of distinct components.

**Open questions for the next pass**

- Should **Power and Curriculum Shaping** be modelled as a capability in its own right, or is it sufficiently captured by the combination of Regulation and Accreditation and Skills Frameworks and Standards?
- Is **Inclusion/Exclusion** a separate capability or an emergent property of Inclusive Access plus Funding and Digital Identity? This chain treats it as emergent.
- Should the **online/physical delivery split** be two components (Online Learning Delivery, Physical Learning Delivery) or one generalised Learning Delivery Platform? This chain uses the generalised form and defers the split to the evolution axis.
- How should **Institutional Brand and Status** be separated from Employability and Status Signalling? They are currently fused.

**Evolution placeholder**

All components are placed at ε = 0.50 in accordance with the partial-map convention. The subsequent full-map pass will reposition, with early expectations:

- Cloud Compute and Storage, Connectivity — commodity (ε ≥ 0.85)
- Digital Identity, Data and Learning Records — product trending to commodity (ε ≈ 0.65–0.75)
- Learning Delivery Platform, Content Production, Skills Frameworks — product (ε ≈ 0.55–0.70)
- Credential Issuance, Assessment, Regulation — product with heavy inertia (ε ≈ 0.55–0.65)
- Teaching and Tutoring, Curriculum Design — custom-built / artisanal for most of the field (ε ≈ 0.30–0.45)
- AI Tutors — genesis / custom-built, moving quickly (ε ≈ 0.20–0.35)
- Community Learning — artisanal (ε ≈ 0.25)

**What's industrialised vs artisanal (preview)**: Cloud, connectivity, delivery platforms, and large-scale content production are industrialised. Standards and credentialing are stable products with strong inertia. Teaching, curriculum design for specific contexts, and community learning remain artisanal. AI Tutors are in genesis and cannibalising the custom-built teaching activity. Power concentrates at Regulation and Accreditation and at Skills Frameworks — together they gate who gets recognised and what counts as a skill, which is the mechanism by which curriculum shapes inclusion.
