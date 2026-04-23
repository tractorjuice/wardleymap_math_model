# Clinical Decision Making in Healthcare (August 2022)

## Executive Summary

**Anchor**: A patient can have their ailment translated into an effective treatment with a measurable clinical outcome.

The value chain decomposes this need into 20 components spanning clinical actors (practitioners, institutions), the reasoning apparatus (diagnostic reasoning, decision support, clinical judgement), governance (standards/guidelines, permissible treatments, exceptions/appeals, fairness review), evidence (trials, evidence base), data (observations, tests, EHR, data sources, standards), and commodity compute. Strategic contrasts surface immediately: clinical judgement and diagnostic reasoning sit on the bespoke side of the chain, while standards, EHR, health data standards, and compute infrastructure sit on the industrialised side. Fairness/equity review and exceptions/appeals are pulled out as distinct nodes so that the rules-vs-exceptions tension can be inspected separately rather than hidden inside "guidelines." Payer reimbursement is modelled as a sibling to practitioner/institution rather than a subordinate of clinical reasoning — it gates which permissible treatments are actually reachable for a given patient.

## Users and Personas

| User                    | Primary need                                                              |
|-------------------------|---------------------------------------------------------------------------|
| Patient                 | Have ailment translated into an effective treatment and measurable outcome |
| Medical practitioner    | Reach a defensible, evidence-based decision under time pressure            |
| Medical institution     | Deliver safe, guideline-consistent care across settings and caseload       |
| Payer                   | Reimburse only treatments that are permissible, evidenced, and fair        |
| Regulator / guideline body | Keep standards and exception mechanisms current and equitable           |

The Patient is the anchor; the other users are modelled as institutional/ operational lenses that shape how the patient's need is satisfied.

## Value Chain Diagram (ASCII)

```
Visibility
  1.00  Patient  (anchor)
  0.90  Effective Treatment and Outcome
  0.85  Medical Practitioner
  0.80  Medical Institution
  0.76  Setting of Care
  0.72  Clinical Judgement
  0.68  Diagnostic Reasoning
  0.60  Decision Support
  0.58  Permissible Treatments
  0.55  Payer Reimbursement
  0.54  Exceptions and Appeals
  0.52  Standards and Guidelines
  0.48  Fairness and Equity Review
  0.46  Patient Observation and History
  0.42  Diagnostic Tests and Imaging
  0.38  Evidence Base
  0.34  Clinical Trials and Reviews
  0.28  Patient Data Sources
  0.22  Electronic Health Record
  0.15  Health Data Standards
  0.08  Compute and Storage Infrastructure
```

## OWM Code (partial map: visibility only, evolution placeholder ε=0.50)

```
title Clinical Decision Making in Healthcare (August 2022)

anchor Patient [0.97, 0.50]

component Effective Treatment and Outcome [0.90, 0.50]
component Medical Practitioner [0.85, 0.50]
component Medical Institution [0.80, 0.50]
component Setting of Care [0.76, 0.50]
component Clinical Judgement [0.72, 0.50]
component Diagnostic Reasoning [0.68, 0.50]
component Decision Support [0.60, 0.50]
component Permissible Treatments [0.58, 0.50]
component Payer Reimbursement [0.55, 0.50]
component Exceptions and Appeals [0.54, 0.50]
component Standards and Guidelines [0.52, 0.50]
component Fairness and Equity Review [0.48, 0.50]
component Patient Observation and History [0.46, 0.50]
component Diagnostic Tests and Imaging [0.42, 0.50]
component Evidence Base [0.38, 0.50]
component Clinical Trials and Reviews [0.34, 0.50]
component Patient Data Sources [0.28, 0.50]
component Electronic Health Record [0.22, 0.50]
component Health Data Standards [0.15, 0.50]
component Compute and Storage Infrastructure [0.08, 0.50]

Patient->Effective Treatment and Outcome
Effective Treatment and Outcome->Medical Practitioner
Effective Treatment and Outcome->Medical Institution
Effective Treatment and Outcome->Setting of Care
Effective Treatment and Outcome->Payer Reimbursement
Medical Practitioner->Clinical Judgement
Medical Practitioner->Diagnostic Reasoning
Medical Institution->Setting of Care
Medical Institution->Standards and Guidelines
Setting of Care->Permissible Treatments
Clinical Judgement->Diagnostic Reasoning
Clinical Judgement->Decision Support
Diagnostic Reasoning->Patient Observation and History
Diagnostic Reasoning->Diagnostic Tests and Imaging
Diagnostic Reasoning->Decision Support
Decision Support->Standards and Guidelines
Decision Support->Evidence Base
Decision Support->Electronic Health Record
Permissible Treatments->Standards and Guidelines
Permissible Treatments->Payer Reimbursement
Permissible Treatments->Exceptions and Appeals
Standards and Guidelines->Evidence Base
Standards and Guidelines->Fairness and Equity Review
Exceptions and Appeals->Fairness and Equity Review
Exceptions and Appeals->Standards and Guidelines
Payer Reimbursement->Standards and Guidelines
Payer Reimbursement->Electronic Health Record
Patient Observation and History->Patient Data Sources
Patient Observation and History->Electronic Health Record
Diagnostic Tests and Imaging->Patient Data Sources
Diagnostic Tests and Imaging->Health Data Standards
Evidence Base->Clinical Trials and Reviews
Evidence Base->Health Data Standards
Clinical Trials and Reviews->Patient Data Sources
Patient Data Sources->Electronic Health Record
Patient Data Sources->Health Data Standards
Electronic Health Record->Health Data Standards
Electronic Health Record->Compute and Storage Infrastructure
Health Data Standards->Compute and Storage Infrastructure

style wardley
```

<details>
<summary>Mermaid wardley-beta equivalent</summary>

```mermaid
wardley-beta
title Clinical Decision Making in Healthcare (August 2022)
size [1100, 800]

anchor Patient [0.97, 0.50]

component Effective Treatment and Outcome [0.90, 0.50]
component Medical Practitioner [0.85, 0.50]
component Medical Institution [0.80, 0.50]
component Setting of Care [0.76, 0.50]
component Clinical Judgement [0.72, 0.50]
component Diagnostic Reasoning [0.68, 0.50]
component Decision Support [0.60, 0.50]
component Permissible Treatments [0.58, 0.50]
component Payer Reimbursement [0.55, 0.50]
component Exceptions and Appeals [0.54, 0.50]
component Standards and Guidelines [0.52, 0.50]
component Fairness and Equity Review [0.48, 0.50]
component Patient Observation and History [0.46, 0.50]
component Diagnostic Tests and Imaging [0.42, 0.50]
component Evidence Base [0.38, 0.50]
component Clinical Trials and Reviews [0.34, 0.50]
component Patient Data Sources [0.28, 0.50]
component Electronic Health Record [0.22, 0.50]
component Health Data Standards [0.15, 0.50]
component Compute and Storage Infrastructure [0.08, 0.50]

Patient -> Effective Treatment and Outcome
Effective Treatment and Outcome -> Medical Practitioner
Effective Treatment and Outcome -> Medical Institution
Effective Treatment and Outcome -> Setting of Care
Effective Treatment and Outcome -> Payer Reimbursement
Medical Practitioner -> Clinical Judgement
Medical Practitioner -> Diagnostic Reasoning
Medical Institution -> Setting of Care
Medical Institution -> Standards and Guidelines
Setting of Care -> Permissible Treatments
Clinical Judgement -> Diagnostic Reasoning
Clinical Judgement -> Decision Support
Diagnostic Reasoning -> Patient Observation and History
Diagnostic Reasoning -> Diagnostic Tests and Imaging
Diagnostic Reasoning -> Decision Support
Decision Support -> Standards and Guidelines
Decision Support -> Evidence Base
Decision Support -> Electronic Health Record
Permissible Treatments -> Standards and Guidelines
Permissible Treatments -> Payer Reimbursement
Permissible Treatments -> Exceptions and Appeals
Standards and Guidelines -> Evidence Base
Standards and Guidelines -> Fairness and Equity Review
Exceptions and Appeals -> Fairness and Equity Review
Exceptions and Appeals -> Standards and Guidelines
Payer Reimbursement -> Standards and Guidelines
Payer Reimbursement -> Electronic Health Record
Patient Observation and History -> Patient Data Sources
Patient Observation and History -> Electronic Health Record
Diagnostic Tests and Imaging -> Patient Data Sources
Diagnostic Tests and Imaging -> Health Data Standards
Evidence Base -> Clinical Trials and Reviews
Evidence Base -> Health Data Standards
Clinical Trials and Reviews -> Patient Data Sources
Patient Data Sources -> Electronic Health Record
Patient Data Sources -> Health Data Standards
Electronic Health Record -> Health Data Standards
Electronic Health Record -> Compute and Storage Infrastructure
Health Data Standards -> Compute and Storage Infrastructure
```

</details>

## Component Inventory

| # | Component | Visibility | Description | Depends on |
|---|-----------|-----------:|-------------|------------|
| 1  | Patient (anchor) | 0.97 | The user whose ailment enters the system and whose outcome is measured | Effective Treatment and Outcome |
| 2  | Effective Treatment and Outcome | 0.90 | The end-state satisfying the patient's need: a treatment selected, delivered, and measurable | Practitioner, Institution, Setting of Care, Payer Reimbursement |
| 3  | Medical Practitioner | 0.85 | The activity of practising medicine on this patient (not the individual) | Clinical Judgement, Diagnostic Reasoning |
| 4  | Medical Institution | 0.80 | Organised care-provision (hospital, surgery, network) within which practice occurs | Setting of Care, Standards and Guidelines |
| 5  | Setting of Care | 0.76 | Primary / secondary / tertiary / community / home — shapes what can actually be done | Permissible Treatments |
| 6  | Clinical Judgement | 0.72 | Bespoke expert reasoning about this specific patient | Diagnostic Reasoning, Decision Support |
| 7  | Diagnostic Reasoning | 0.68 | Hypothesis → test → refine cycle that maps observations to a diagnosis | Observation, Tests, Decision Support |
| 8  | Decision Support | 0.60 | Tools, alerts, and pathways that assist (but do not replace) the clinician | Standards, Evidence Base, EHR |
| 9  | Permissible Treatments | 0.58 | The formulary / procedure set actually allowed in this setting for this condition | Standards, Payer, Exceptions |
| 10 | Payer Reimbursement | 0.55 | The rules and funding flow that determine which treatments the patient can actually receive | Standards, EHR |
| 11 | Exceptions and Appeals | 0.54 | The named-patient / prior-authorisation / appeal route for deviating from the guideline | Fairness, Standards |
| 12 | Standards and Guidelines | 0.52 | Codified clinical protocols (NICE, royal colleges, specialty societies) | Evidence Base, Fairness |
| 13 | Fairness and Equity Review | 0.48 | The equity lens applied when standards or exceptions are set or invoked | — (terminal practice) |
| 14 | Patient Observation and History | 0.46 | Symptoms, vitals, lived experience, history taking | Patient Data Sources, EHR |
| 15 | Diagnostic Tests and Imaging | 0.42 | Labs, pathology, radiology — the industrialised observation layer | Patient Data Sources, Health Data Standards |
| 16 | Evidence Base | 0.38 | The body of evidence standards rest on (systematic reviews, meta-analyses) | Clinical Trials and Reviews, Health Data Standards |
| 17 | Clinical Trials and Reviews | 0.34 | The process that generates and refreshes the evidence base | Patient Data Sources |
| 18 | Patient Data Sources | 0.28 | Raw feeds: devices, lab systems, registries, claims | EHR, Health Data Standards |
| 19 | Electronic Health Record | 0.22 | The institutional record where data is written, read, and audited | Health Data Standards, Compute |
| 20 | Health Data Standards | 0.15 | HL7/FHIR, SNOMED, ICD, LOINC — the interoperability substrate | Compute |
| 21 | Compute and Storage Infrastructure | 0.08 | Commodity cloud/on-prem compute and storage | — (commodity terminal) |

## Dependency Matrix (direct = X, indirect = I)

Abbreviated for readability — rows are dependents, columns are dependencies. Only direct edges shown.

| Dependent \ Dep | Treatment | Pract | Inst | Setting | Judge | Diag Reason | Dec Sup | Permiss | Payer | Except | Stand | Fair | Obs | Tests | Evid | Trials | Sources | EHR | HDS | Compute |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Patient | X | | | | | | | | | | | | | | | | | | | |
| Treatment | | X | X | X | | | | | X | | | | | | | | | | | |
| Practitioner | | | | | X | X | | | | | | | | | | | | | | |
| Institution | | | | X | | | | | | | X | | | | | | | | | |
| Setting | | | | | | | | X | | | | | | | | | | | | |
| Judgement | | | | | | X | X | | | | | | | | | | | | | |
| Diag Reason | | | | | | | X | | | | | | X | X | | | | | | |
| Dec Support | | | | | | | | | | | X | | | | X | | | X | | |
| Permissible | | | | | | | | | X | X | X | | | | | | | | | |
| Payer | | | | | | | | | | | X | | | | | | | X | | |
| Exceptions | | | | | | | | | | | X | X | | | | | | | | |
| Standards | | | | | | | | | | | | X | | | X | | | | | |
| Observation | | | | | | | | | | | | | | | | | X | X | | |
| Tests | | | | | | | | | | | | | | | | | X | | X | |
| Evid Base | | | | | | | | | | | | | | | | X | | | X | |
| Trials | | | | | | | | | | | | | | | | | X | | | |
| Sources | | | | | | | | | | | | | | | | | | X | X | |
| EHR | | | | | | | | | | | | | | | | | | | X | X |
| HDS | | | | | | | | | | | | | | | | | | | | X |

## Critical Path Analysis

Primary critical path from anchor to deepest commodity:

Patient → Effective Treatment and Outcome → Medical Practitioner → Clinical Judgement → Decision Support → Evidence Base → Clinical Trials and Reviews → Patient Data Sources → Electronic Health Record → Health Data Standards → Compute and Storage Infrastructure

- **Bottleneck**: Standards and Guidelines is depended on by Decision Support, Permissible Treatments, Payer Reimbursement, Exceptions and Appeals, and Medical Institution. A stale or absent guideline bottlenecks five downstream activities.
- **Single point of failure**: Electronic Health Record is the hub where Observation, Tests, Decision Support, Payer, and Data Sources converge. EHR outage degrades most of the chain.
- **Resilience gap**: Fairness and Equity Review is a terminal practice (no dependencies below it), which makes it easy to under-resource. It is a leaf where strategic neglect is invisible in the topology.

## Validation Checklist

- [x] Chain starts with a genuine user need (patient outcome), not a solution
- [x] All significant dependencies captured (20 components, 39 edges)
- [x] Chain reaches commodity level (Compute and Storage Infrastructure)
- [x] No orphan components
- [x] Components are activities/capabilities/practices (practitioner = practising medicine, not a named person)
- [x] Dependencies reflect real-world clinical and operational relationships
- [x] Visibility ordering consistent: every edge A→B has ν(A) ≥ ν(B)
- [x] No cycles (verified by topological ordering of visibility values)
- [x] Granularity appropriate for strategic analysis (20 components within the 8–20 target)
- [x] Chain reveals strategic insight (bespoke judgement vs industrialised process line falls naturally around ν≈0.45)

## Visibility Assessment

| Component | ν | Rationale |
|-----------|--:|-----------|
| Patient | 0.97 | Anchor |
| Effective Treatment and Outcome | 0.90 | The user-experienced outcome itself |
| Medical Practitioner | 0.85 | Directly interacts with patient; failure immediately visible |
| Medical Institution | 0.80 | Setting the patient enters — visible as a brand and as a building |
| Setting of Care | 0.76 | The context (GP, A&E, ward, home) the patient perceives |
| Clinical Judgement | 0.72 | Patient experiences the clinician's reasoning via conversation |
| Diagnostic Reasoning | 0.68 | Visible as explanation and question-asking |
| Decision Support | 0.60 | Patient rarely sees it, but clinician-visible and outcome-shaping |
| Permissible Treatments | 0.58 | Patient feels it only when a treatment is refused |
| Payer Reimbursement | 0.55 | Patient sees it at bills, prior auth, coverage letters |
| Exceptions and Appeals | 0.54 | Visible only when invoked, but patient-facing when it is |
| Standards and Guidelines | 0.52 | Cited to the patient rather than directly experienced |
| Fairness and Equity Review | 0.48 | Mostly invisible at point of care |
| Patient Observation and History | 0.46 | The clinician sees this; patient lives it but does not "see" it as a component |
| Diagnostic Tests and Imaging | 0.42 | Patient sees the event (blood draw) but not the component |
| Evidence Base | 0.38 | Invisible background to the guideline |
| Clinical Trials and Reviews | 0.34 | Invisible to individual patient unless enrolled |
| Patient Data Sources | 0.28 | Pure infrastructure from patient view |
| Electronic Health Record | 0.22 | Institutional infrastructure |
| Health Data Standards | 0.15 | Deep infrastructure |
| Compute and Storage Infrastructure | 0.08 | Commodity terminal |

## Assumptions and Open Questions

- **Jurisdiction**: Treated as a mixed UK/US 2022 landscape so that both NICE-style guideline bodies and payer-gated formularies are meaningful. A single-jurisdiction map would move Payer Reimbursement up or down.
- **Patient as anchor, not "population health"**: Single-patient decision-making is the stated scenario. A population-health anchor would add epidemiology and public-health surveillance as parallel sub-chains.
- **Fairness review modelled as a distinct node**: The scenario asks where fairness sits; rather than bundle it into Standards, it is pulled out so its relationship to exceptions is explicit.
- **Exceptions as a distinct node alongside Standards**: Rules-and-exceptions is called out by the user; the two are siblings so the map can show how appeals travel differently from the main guideline path.
- **Decision Support treated as a capability, not a product**: No specific CDS vendor assumed.
- **Evolution stage not assessed**: Per the partial-map convention, all ε are placeholders (0.50) and the chain is not yet positioned on the evolution axis.

## Footer

Generated by: arckit-wardley.value-chain skill (partial-map variant; visibility only, ε=0.50 placeholder)
Generated on: 2026-04-23
Scenario: Clinical decision making in healthcare, August 2022
Components: 20 + 1 anchor. Edges: 39.
