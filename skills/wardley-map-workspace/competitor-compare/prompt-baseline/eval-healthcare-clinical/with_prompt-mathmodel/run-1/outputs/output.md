```owm
title Clinical Decision Making in Healthcare (Aug 2022)
style wardley

// Anchors — the users whose needs this landscape exists to satisfy
anchor Patient (seeking treatment) [0.99, 0.55]
anchor Medical Practitioner [0.97, 0.50]
anchor Medical Institution [0.95, 0.60]
anchor Payer [0.93, 0.70]

// ---- Layer 1: directly visible clinical workflow ----
component Presenting Ailment [0.90, 0.45]
component Care Setting Selection [0.88, 0.55]
component Clinical Consultation [0.86, 0.55]
component Treatment Decision [0.84, 0.45]
component Treatment Delivery [0.82, 0.55]
component Measurable Clinical Outcome [0.80, 0.50]
component Reimbursement Claim [0.82, 0.75]

// ---- Layer 2: settings of care the patient flows through ----
component Primary Care Visit [0.74, 0.70]
component Emergency Department [0.72, 0.60]
component Specialist Clinic [0.70, 0.55]
component Hospital Inpatient Care [0.68, 0.55]
component Telehealth Encounter [0.70, 0.55]
component Community / Home Care [0.66, 0.45]

// ---- Layer 3: diagnostic reasoning & decision support ----
component Clinical History Taking [0.64, 0.50]
component Physical Examination [0.62, 0.55]
component Differential Diagnosis [0.60, 0.35]
component Diagnostic Reasoning (judgement) [0.58, 0.30]
component Clinical Decision Support System [0.56, 0.45]
component Risk Scoring / Calculators [0.54, 0.60]
component AI Diagnostic Aids [0.52, 0.25]
component Second Opinion / MDT Review [0.50, 0.35]
component Shared Decision Making [0.48, 0.35]
component Exception / Escalation Rules [0.46, 0.40]

// ---- Layer 4: permissible treatments & the rules around them ----
component Pharmacy Formulary [0.44, 0.70]
component Prescribed Medication [0.42, 0.80]
component Surgical Procedure [0.40, 0.55]
component Non-pharmacological Therapy [0.38, 0.50]
component Off-label / Compassionate Use [0.36, 0.30]
component Prior Authorisation [0.38, 0.65]

// ---- Layer 5: standards, guidelines, evidence, trials ----
component Clinical Practice Guideline [0.52, 0.55]
component Care Pathway / Protocol [0.50, 0.60]
component Coding Standard (ICD / SNOMED) [0.34, 0.85]
component Evidence Review (systematic) [0.32, 0.45]
component Randomised Controlled Trial [0.30, 0.55]
component Real-World Evidence [0.28, 0.35]
component Regulatory Approval (FDA / EMA / MHRA) [0.36, 0.75]
component Fairness / Bias Audit [0.26, 0.20]
component Health Equity Adjustment [0.24, 0.25]
component Medico-legal / Informed Consent [0.40, 0.65]

// ---- Layer 6: data sources & observation ----
component Patient-Reported Symptoms [0.60, 0.45]
component Vital Signs Monitoring [0.42, 0.75]
component Laboratory Testing [0.40, 0.80]
component Medical Imaging [0.38, 0.70]
component Pathology [0.36, 0.65]
component Genomic Testing [0.32, 0.35]
component Wearable / Continuous Monitoring [0.30, 0.30]
component Electronic Health Record [0.26, 0.70]
component Health Information Exchange [0.22, 0.55]

// ---- Layer 7: industrialised infrastructure ----
component Medical Device Supply [0.18, 0.80]
component Drug Manufacturing [0.16, 0.85]
component Cloud / Hosting [0.12, 0.92]
component Network / Connectivity [0.10, 0.95]
component Identity / Authentication [0.14, 0.88]

// ---- Dependencies ----
// Anchor → workflow entry points
Patient (seeking treatment)->Presenting Ailment
Patient (seeking treatment)->Care Setting Selection
Patient (seeking treatment)->Shared Decision Making
Patient (seeking treatment)->Measurable Clinical Outcome
Medical Practitioner->Clinical Consultation
Medical Practitioner->Treatment Decision
Medical Practitioner->Diagnostic Reasoning (judgement)
Medical Institution->Care Setting Selection
Medical Institution->Clinical Practice Guideline
Medical Institution->Care Pathway / Protocol
Payer->Reimbursement Claim
Payer->Prior Authorisation
Payer->Coding Standard (ICD / SNOMED)

// Clinical workflow chain
Presenting Ailment->Clinical Consultation
Care Setting Selection->Primary Care Visit
Care Setting Selection->Emergency Department
Care Setting Selection->Specialist Clinic
Care Setting Selection->Telehealth Encounter
Care Setting Selection->Community / Home Care
Clinical Consultation->Clinical History Taking
Clinical Consultation->Physical Examination
Clinical Consultation->Differential Diagnosis
Differential Diagnosis->Diagnostic Reasoning (judgement)
Differential Diagnosis->Clinical Decision Support System
Differential Diagnosis->Risk Scoring / Calculators
Differential Diagnosis->AI Diagnostic Aids
Differential Diagnosis->Second Opinion / MDT Review
Treatment Decision->Differential Diagnosis
Treatment Decision->Shared Decision Making
Treatment Decision->Exception / Escalation Rules
Treatment Decision->Clinical Practice Guideline
Treatment Decision->Care Pathway / Protocol
Treatment Decision->Medico-legal / Informed Consent
Treatment Delivery->Treatment Decision
Treatment Delivery->Prescribed Medication
Treatment Delivery->Surgical Procedure
Treatment Delivery->Non-pharmacological Therapy
Treatment Delivery->Off-label / Compassionate Use
Measurable Clinical Outcome->Treatment Delivery
Measurable Clinical Outcome->Electronic Health Record
Reimbursement Claim->Coding Standard (ICD / SNOMED)
Reimbursement Claim->Prior Authorisation
Reimbursement Claim->Electronic Health Record

// Settings → data & decision support feeds
Primary Care Visit->Clinical History Taking
Emergency Department->Vital Signs Monitoring
Emergency Department->Risk Scoring / Calculators
Specialist Clinic->Differential Diagnosis
Hospital Inpatient Care->Vital Signs Monitoring
Hospital Inpatient Care->Electronic Health Record
Telehealth Encounter->Patient-Reported Symptoms
Community / Home Care->Wearable / Continuous Monitoring

// Diagnostic reasoning data dependencies
Clinical History Taking->Patient-Reported Symptoms
Physical Examination->Vital Signs Monitoring
Differential Diagnosis->Laboratory Testing
Differential Diagnosis->Medical Imaging
Differential Diagnosis->Pathology
Differential Diagnosis->Genomic Testing
Clinical Decision Support System->Electronic Health Record
Clinical Decision Support System->Clinical Practice Guideline
Risk Scoring / Calculators->Evidence Review (systematic)
AI Diagnostic Aids->Real-World Evidence
AI Diagnostic Aids->Medical Imaging
AI Diagnostic Aids->Fairness / Bias Audit
Second Opinion / MDT Review->Clinical Practice Guideline
Shared Decision Making->Evidence Review (systematic)
Shared Decision Making->Patient-Reported Symptoms
Exception / Escalation Rules->Clinical Practice Guideline
Exception / Escalation Rules->Medico-legal / Informed Consent

// Treatment permissibility
Prescribed Medication->Pharmacy Formulary
Prescribed Medication->Regulatory Approval (FDA / EMA / MHRA)
Surgical Procedure->Regulatory Approval (FDA / EMA / MHRA)
Surgical Procedure->Medical Device Supply
Non-pharmacological Therapy->Care Pathway / Protocol
Off-label / Compassionate Use->Exception / Escalation Rules
Off-label / Compassionate Use->Medico-legal / Informed Consent
Pharmacy Formulary->Drug Manufacturing
Pharmacy Formulary->Regulatory Approval (FDA / EMA / MHRA)
Prior Authorisation->Coding Standard (ICD / SNOMED)
Prior Authorisation->Clinical Practice Guideline

// Guidelines / evidence chain
Clinical Practice Guideline->Evidence Review (systematic)
Care Pathway / Protocol->Clinical Practice Guideline
Evidence Review (systematic)->Randomised Controlled Trial
Evidence Review (systematic)->Real-World Evidence
Real-World Evidence->Electronic Health Record
Randomised Controlled Trial->Regulatory Approval (FDA / EMA / MHRA)
Health Equity Adjustment->Fairness / Bias Audit
Clinical Practice Guideline->Health Equity Adjustment

// Data sources → infrastructure
Laboratory Testing->Electronic Health Record
Medical Imaging->Electronic Health Record
Pathology->Electronic Health Record
Genomic Testing->Electronic Health Record
Wearable / Continuous Monitoring->Health Information Exchange
Electronic Health Record->Health Information Exchange
Electronic Health Record->Cloud / Hosting
Electronic Health Record->Identity / Authentication
Health Information Exchange->Network / Connectivity
Health Information Exchange->Identity / Authentication
Medical Device Supply->Drug Manufacturing

// Evolution projections (scenario, not forecast)
evolve AI Diagnostic Aids 0.50
evolve Wearable / Continuous Monitoring 0.55
evolve Real-World Evidence 0.55
evolve Genomic Testing 0.55
evolve Clinical Decision Support System 0.65
evolve Fairness / Bias Audit 0.40
evolve Telehealth Encounter 0.70

// Inertia — components resisting evolution (see Inertia doc: re-architecture cost, sunk capital, political capital)
component Legacy Paper Pathways [0.44, 0.50] inertia
Care Pathway / Protocol->Legacy Paper Pathways

// Notes
note Bespoke judgement zone [0.62, 0.15]
note Industrialised process zone [0.25, 0.90]
note Fairness / exceptions sit here [0.30, 0.22]
```

## Strategic Analysis

This map reflects clinical decision making as it looked in August 2022 — post-pandemic telehealth normalisation, pre-GPT-4, with AI diagnostic aids still mostly in radiology/pathology point solutions, and real-world evidence beginning to be accepted by regulators but far from dominant. Four anchors are used because the scenario is genuinely multi-sided: patients, practitioners, institutions, and payers each have distinct needs that pull the landscape in different directions.

### a. Top 3 components by D (differentiation pressure, D = ν · (1 − ε))

1. **Diagnostic Reasoning (judgement)** — D = 0.58 · 0.70 ≈ **0.41**. The core bespoke act: synthesising history, examination, tests and priors into a differential. Still a craft, irreducibly. This is where practitioners add the value machines do not yet replicate.
2. **Differential Diagnosis** — D = 0.60 · 0.65 ≈ **0.39**. One step up in the chain, highly visible to the practitioner and still immature as an automated output. The battleground where AI diagnostic aids, CDSS and human cognition collide.
3. **Shared Decision Making** — D = 0.48 · 0.65 ≈ **0.31**. Closer to the patient anchor and still a practice being formalised. Institutions that operationalise it well (decision aids, patient-reported outcome capture) gain a genuine patient-experience differentiator that also reduces medico-legal exposure.

### b. Top 3 components by K (commodity leverage, K = (1 − ν) · ε)

1. **Network / Connectivity** — K = 0.90 · 0.95 ≈ **0.86**. Pure utility. Should be consumed, not built.
2. **Cloud / Hosting** — K = 0.88 · 0.92 ≈ **0.81**. Same story — utility-grade, with healthcare-specific compliance wrappers (HIPAA, ISO 27001) available from the hyperscalers.
3. **Drug Manufacturing** — K = 0.84 · 0.85 ≈ **0.71**. Highly industrialised supply. Institutions should not attempt vertical integration here except for narrow strategic reasons (e.g. shortage resilience for a specific critical drug).

Honourable mention: **Laboratory Testing** (0.60 · 0.80 = 0.48) and **Coding Standard (ICD/SNOMED)** (0.66 · 0.85 = 0.56) — both close to utility status for everyone except the standards bodies themselves.

### c. Top 3 dependency risks by R (R = ν(a) · (1 − ε(b)))

1. **(Treatment Decision, Diagnostic Reasoning (judgement))** — R = 0.84 · 0.70 ≈ **0.59**. The entire downstream treatment chain hangs off an opaque, unaudited, hard-to-improve cognitive process. This is the single biggest fragility in clinical care: no metrics on the reasoning itself, only on the outputs.
2. **(Treatment Decision, Exception / Escalation Rules)** — R = 0.84 · 0.60 ≈ **0.50**. Exceptions and escalation are typically tacit, unevenly applied and legally consequential. A highly visible decision depending on an underspecified rule set.
3. **(Differential Diagnosis, AI Diagnostic Aids)** — R = 0.60 · 0.75 ≈ **0.45**. Where AI is used, it is often deployed upstream of differential diagnosis without robust fairness/bias audit coverage — an unstable foundation under a high-visibility decision.

### d. Suggested gameplays (from Wardley's 61-play catalogue)

- **Open Approaches** on *Clinical Decision Support System* and *Clinical Practice Guideline*. Open guideline libraries (NICE, AHRQ, MAGICapp) already exist; institutions should contribute rather than maintain proprietary forks. Accelerates the CDSS component toward Product/Commodity.
- **Industrialisation of components / Commoditise a component** on *Risk Scoring / Calculators* and *Coding Standard (ICD / SNOMED)*. These should be shared services behind APIs, not re-implemented per-hospital.
- **Use of ecosystems / Two-factor markets** on *Real-World Evidence* combined with the *Electronic Health Record*. Institutions that curate de-identified RWE datasets and share access under governance create a network effect that compounds on itself and feeds back into guideline development.
- **Standards game** on *Electronic Health Record* and *Health Information Exchange* (FHIR/SMART-on-FHIR). A payer or institution that drives the standard shifts where value accrues.
- **Harvesting** (#29 in the catalogue) on mature AI Diagnostic Aid vendors — pick off the companies whose radiology/pathology models are reaching Product stage.
- **Directed Investment** in *AI Diagnostic Aids* coupled with *Fairness / Bias Audit*. Investing in the audit function alongside the model is the only way to de-risk the (Differential Diagnosis → AI Diagnostic Aids) edge above.
- **Pig in a poke / Exploiting constraint** should be *avoided* by institutions vis-à-vis payers on *Prior Authorisation* — don't get locked into payer-specific authorisation software when an open submission standard would serve.
- **Fool's mate / Sweat & dump** would be the wrong play on *Diagnostic Reasoning (judgement)*; this is a Genesis-stage competency to invest in, not dispose of.

### e. Doctrine observations (from the 40-principle catalogue)

- **Focus on user needs** — the map has four anchors because the real landscape has four. A common failure mode in healthcare strategy decks is to anchor only on the patient and then silently bake in payer or institutional preferences. Making the anchors explicit surfaces the conflicts.
- **Know your users** (Phase II) — the fact that Patient and Payer sit on opposite sides of the *Prior Authorisation* and *Pharmacy Formulary* chain is visible in the dependency graph. That asymmetry is real strategy data, not a bug.
- **Use appropriate methods** — the split between *Diagnostic Reasoning (judgement)* (Genesis, needs agile / exploratory) and *Laboratory Testing* (Stage IV, needs Six-Sigma / lean) is textbook Pioneer-Settler-Town-Planner. Institutions that run clinical judgement with KPIs lifted from lab operations get predictable but bad outcomes on the judgement side.
- **Remove bias and duplication** — *Fairness / Bias Audit* and *Health Equity Adjustment* are deliberately placed deep and to the left (low ν, low ε). They are currently underspecified and politically costly. The doctrine implication: they should be moved up in visibility (institution-level dashboards) and accelerated in evolution (standardised audit protocols). This is where the scenario's "fairness and exceptions" question lives.
- **Manage inertia** — the *Legacy Paper Pathways* node with the `inertia` marker is the most visible illustrative form (re-architecture cost + human capital, from the 17-form inertia taxonomy). Many institutions still run parallel paper and electronic pathway copies; the sunk cost resists replacement even when the electronic version is technically superior.
- **A bias towards action, but evidence-based** — the tension between *Care Pathway / Protocol* (industrialised, Stage III) and *Exception / Escalation Rules* (Custom Built, Stage II) is the practical expression of this doctrine. Pathways run the 80%; exceptions handle the 20%. A mature institution instruments both.

### Dynamics note

Evolution arrows are shown for AI Diagnostic Aids, Wearables, RWE, Genomic Testing, CDSS, Fairness audit, and Telehealth. These are *scenarios*, not forecasts — following Wardley's climatic pattern that evolution cannot be measured over time. The logistic form $d\varepsilon/dt = r \varepsilon (1-\varepsilon)$ can be used to simulate trajectories, but the positions shown are judgements of where each component could plausibly sit within a 2–5 year horizon if the surrounding ecosystem (regulation, reimbursement, workforce) does not actively block them — which in healthcare it often does.

### Where bespoke ends and industrialised begins

- **Bespoke (Genesis / Custom Built) zone:** Diagnostic Reasoning, AI Diagnostic Aids, Off-label/Compassionate Use, Fairness / Bias Audit, Health Equity Adjustment, Real-World Evidence, Genomic Testing, Wearables, Shared Decision Making, Second Opinion / MDT Review.
- **Industrialised (Product / Commodity) zone:** Coding Standard (ICD/SNOMED), Laboratory Testing, Drug Manufacturing, Medical Device Supply, Vital Signs Monitoring, Reimbursement Claim, Prescribed Medication, Pharmacy Formulary, Regulatory Approval, Cloud / Hosting, Network, Identity.
- **Fairness and exception rules** sit in the bespoke-to-custom-built band at low visibility. The strategic move is to lift their visibility (make them dashboarded at institutional level) without prematurely industrialising them — a fairness audit that becomes a box-tick loses its meaning.
