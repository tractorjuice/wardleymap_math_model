# Clinical Decision Making in Healthcare — August 2022

## Map metadata

```yaml
wardley_map:
  metadata:
    title: "Clinical Decision Making in Healthcare"
    author: "arc-kit wardley-mapping skill"
    date: "2022-08-01"
    version: "1.0"
    scope: "How a patient's ailment becomes a treatment and a measurable outcome, covering people (patient, practitioner, institution, payer), the supporting apparatus (data/observation, diagnostic reasoning, decision support, permissible treatments, standards/guidelines, trials/reviews), and the settings of care."
  anchor:
    user: "Patient"
    need: "My ailment is understood, I receive a permissible treatment, and the clinical outcome is measured."
```

## Step 1 — Anchor and scope

- **User**: Patient (the person whose ailment is being diagnosed and treated).
- **User need**: "My ailment becomes a treatment and a measurable clinical outcome" — the full journey from presentation through diagnosis to outcome.
- **Scope**: The clinical decision-making landscape in a modern (UK/US-style) healthcare system at August 2022. Single map; moderate depth (~30 components, with gameplay/climatic commentary).
- **Primary goal**: Expose where clinical work is *bespoke judgement* vs *industrialised process*, and where fairness / the rules around exceptions sit relative to the guideline machinery.

## Step 2 — Value chain

Working down from the patient:

```
Patient
 ├── Treatment outcome
 │     └── Treatment plan
 │           ├── Diagnosis
 │           │     ├── Diagnostic reasoning ── Clinical judgement
 │           │     ├── Patient history / symptoms        \
 │           │     ├── Clinical observation               ├── EHR ── SNOMED/ICD ── Storage ── Cloud
 │           │     └── Diagnostic tests (lab/imaging)    /
 │           ├── Permissible treatments
 │           │     ├── Clinical guidelines ── Evidence base ── Clinical trials
 │           │     ├── Formulary / approved drug list
 │           │     └── Regulatory approval (MHRA/FDA)
 │           └── Clinical guidelines ── Standards and protocols
 ├── Medical practitioner
 │     ├── Clinical judgement
 │     ├── Diagnostic reasoning
 │     ├── Decision support (CDSS) ── AI-assisted diagnosis
 │     └── Clinical guidelines
 ├── Medical institution
 │     ├── Setting of care { Primary care, Specialist clinic, Hospital, Emergency, Community/home }
 │     ├── Standards and protocols
 │     └── EHR
 └── Payer
       ├── Formulary
       ├── Permissible treatments (approval envelope)
       └── Exception / appeals process ── Fairness & equity review ── Evidence base
```

## Step 3 — Evolution positioning (Ubiquity + Certainty scoring)

Scores use the skill's E(c) = (U + C) / 2 rubric. Bold rows are the load-bearing positions; the rest are support.

| Component | U | C | E(c) | Stage | Notes |
|---|---|---|---|---|---|
| **Patient** (anchor) | 1.00 | 1.00 | 1.00 | Anchor | Universal user. |
| Treatment outcome | 0.50 | 0.60 | 0.55 | Product | Outcome measurement standardised for common conditions, bespoke for rare. |
| Treatment plan | 0.45 | 0.55 | 0.50 | Custom→Product | Boundary case. |
| **Diagnosis** | 0.40 | 0.45 | 0.42 | Custom-Built | Guideline-assisted but still judgement-heavy. |
| Medical practitioner (role) | 0.75 | 0.60 | 0.68 | Product | Mature profession, defined training pathway. |
| Medical institution | 0.80 | 0.70 | 0.74 | Product | Widely understood operating model. |
| Payer | 0.65 | 0.55 | 0.60 | Product | Mature in US; mature-but-consolidated in NHS. |
| Setting of care | 0.75 | 0.65 | 0.70 | Product | Tiering is standard. |
| Primary care | 0.80 | 0.75 | 0.78 | Commodity-ish Product | Ubiquitous, well-defined. |
| Hospital / inpatient | 0.75 | 0.70 | 0.72 | Product | Standardised. |
| Emergency care | 0.75 | 0.72 | 0.74 | Product | Triage is well-codified. |
| Specialist clinic | 0.55 | 0.55 | 0.55 | Custom→Product | Variability by specialty. |
| Community / home care | 0.60 | 0.65 | 0.62 | Product | Maturing; tele-health lifting ubiquity. |
| **Diagnostic reasoning** | 0.45 | 0.50 | 0.48 | Custom-Built | Part craft, part protocol. |
| **Clinical judgement** | 0.30 | 0.30 | 0.30 | Custom-Built (towards Genesis of the bespoke) | The residual "art of medicine". |
| **Decision support (CDSS)** | 0.35 | 0.40 | 0.38 | Custom-Built | Rule-based systems live, ML-based CDSS still Custom in 2022. |
| **AI-assisted diagnosis** | 0.10 | 0.20 | 0.15 | Genesis | FDA 510(k) algorithms exist (Aidoc, IDx-DR), but adoption rare in routine practice Aug 2022, ChatGPT/GPT-4 not yet released. |
| **Exception / appeals process** | 0.20 | 0.25 | 0.22 | Genesis / Custom | Exists, but highly institution-specific; payer-driven exception paths vary. |
| **Fairness and equity review** | 0.10 | 0.15 | 0.12 | Genesis | Formal algorithmic-fairness audits of CDSS only just emerging. |
| **Permissible treatments** | 0.55 | 0.60 | 0.58 | Product | The envelope is mature, the contents shift constantly. |
| **Clinical guidelines** | 0.70 | 0.70 | 0.70 | Product | NICE / USPSTF / specialty-society guidelines — dominant. |
| **Standards and protocols** | 0.80 | 0.80 | 0.80 | Commodity | Checklists, WHO safety protocols. |
| **Formulary / approved drug list** | 0.80 | 0.85 | 0.82 | Commodity | Auditable, routine operation. |
| Evidence base (RCT, meta-analysis) | 0.55 | 0.55 | 0.55 | Product | Cochrane / PubMed — structurally mature. |
| Clinical trials and reviews | 0.35 | 0.35 | 0.35 | Custom-Built | Trial design still bespoke. |
| Regulatory approval (MHRA/FDA) | 0.75 | 0.80 | 0.78 | Commodity | Routine, auditable process. |
| Patient history / symptoms | 0.55 | 0.60 | 0.58 | Product | Intake forms + templates. |
| Clinical observation | 0.50 | 0.60 | 0.55 | Product | Vitals, examination — codified. |
| Diagnostic tests (lab/imaging) | 0.70 | 0.75 | 0.72 | Product (imaging/path labs are utility-like) | |
| **Electronic health record (EHR)** | 0.70 | 0.65 | 0.68 | Product (→ Commodity) | Epic/Cerner dominate; moving to commodity in large systems. |
| Medical terminologies (SNOMED/ICD) | 0.90 | 0.85 | 0.88 | Commodity | ISO-grade standards. |
| Health data storage | 0.90 | 0.90 | 0.90 | Commodity | HIPAA/GDPR-ready cloud storage. |
| Cloud compute / networking | 0.95 | 0.95 | 0.95 | Commodity | AWS/Azure/GCP. |

## Step 4 — Movement (August 2022 view)

- `evolve AI-assisted diagnosis 0.45` — radiology AI (Aidoc, Annalise, Viz.ai) and diabetic-retinopathy screening (IDx-DR) are productising. Large-language-model CDSS still genesis (GPT-4 lands Mar 2023, outside the map horizon).
- `evolve Decision support (CDSS) 0.60` — EHR-embedded rule engines (Epic BPA, Cerner) are well on the way to product; but next-gen ML-driven CDSS remain custom.
- `evolve Electronic health record (EHR) 0.80` — consolidation around Epic/Cerner; API access via FHIR is commoditising.
- `evolve Clinical trials and reviews 0.55` — decentralised trials, real-world-evidence pipelines, and adaptive designs post-COVID are productising trial infrastructure.
- `evolve Exception / appeals process 0.45` — ongoing pressure from both payer automation and patient-advocacy driving this from bespoke to process.
- `evolve Fairness and equity review 0.35` — WHO/FDA guidance on algorithmic bias is pushing this from genesis toward custom-built practice.

Inertia markers:
- **Clinical judgement** has strong inertia — professional identity, medico-legal exposure, and training reward individual judgement over protocolised decision-making.
- **Specialist clinics** carry inertia via consultant autonomy and referral patterns.
- **EHR** has path-dependency inertia (switching cost for hospitals is immense).

## Step 5 — Analysis and recommendations

### Completeness check

- Anchor (Patient) defined. Yes.
- All major actors present (patient, practitioner, institution, payer). Yes.
- All supporting apparatus the brief asked for (data/observation, diagnostic reasoning, decision support, permissible treatments, standards/guidelines, trials/reviews, settings of care). Yes.
- Bespoke vs industrial axis clearly exposed: the left-hand cluster (Clinical judgement, Diagnostic reasoning, AI-assisted diagnosis, Exception / appeals, Fairness review, Clinical trials) vs the right-hand cluster (Standards & protocols, Formulary, Regulatory approval, SNOMED/ICD, Health data storage, Cloud).
- Fairness and exceptions placed together at bottom-left (genesis / custom) deliberately — this is the honest picture for Aug 2022.
- Movement arrows present. Yes.

### Positioning check

- Each component positioned on market-wide maturity, not any single institution's capability.
- Commodity cluster (Formulary, Standards & protocols, SNOMED/ICD, Health data storage, Cloud, Regulatory approval) is on the right.
- Genuinely novel components (AI-assisted diagnosis, Fairness & equity review) are on the left.

### Opportunities

- **Productise decision support on top of the commodity data stack.** Standards, SNOMED, EHR, and cloud storage are all effectively commodity — the differentiating opportunity is Custom-Built CDSS and AI-assisted diagnosis that ride on that plumbing. This is a textbook *higher-order systems create new value* climatic pattern: commoditising infrastructure (EHR/cloud) unlocks the genesis layer above.
- **Industrialise the exception / appeals process.** It sits at Custom with high patient-visibility (0.62 vis). This is a *differentiation pressure* hotspot — D(v) = 0.62 × (1 − 0.22) ≈ **0.48**. Payers and providers who codify fair, auditable exception handling will earn trust and reduce legal risk.
- **Treat fairness and equity review as a genesis investment, not a compliance afterthought.** It depends on the evidence base (which is Product) but needs its own pioneering methods (audit tooling, bias metrics, stratified outcome reporting). Don't hand this to planners yet.
- **Watch the EHR commodity transition.** As FHIR APIs mature, institutions that keep building custom interfaces are accruing technical debt; institutions that consume FHIR-as-utility free up capacity for the CDSS layer above.

### Threats

- **AI-assisted diagnosis trails hype.** In Aug 2022 it is genesis-with-commercial-claims. Organisations that build heavy dependencies on it early risk a *betting on the wrong approach* failure mode.
- **Guideline calcification.** Clinical guidelines at Product maturity can ossify — evidence cycles (trials → evidence base → guideline update) run on multi-year timescales. Rapid-evolution areas (genomic medicine, AI diagnosis) may outrun guideline machinery.
- **Dependency risk: visible Diagnosis (vis 0.82) depends on immature Diagnostic reasoning (evol 0.48).** R = 0.82 × (1 − 0.48) = **0.43** — moderate. Misdiagnosis risk persists because the reasoning layer is still craft.
- **Dependency risk: Treatment plan (vis 0.86) depends on Permissible treatments (evol 0.58).** R = 0.86 × 0.42 = **0.36** — moderate. Formulary and regulatory shifts can move the envelope under a treating clinician.
- **Fairness inversion risk.** Fairness & equity review (genesis, vis 0.48) sits below the patient-visible Exception / appeals process (custom, vis 0.62). The audit tools are immature while the user-visible promise of "fair exceptions" is being made — classic under-specified dependency.

### Inertia points

| Component | Reason for inertia |
|---|---|
| Clinical judgement | Professional identity, medico-legal framing, training curricula all reward bespoke judgement over protocolisation. |
| Specialist clinics | Consultant autonomy and referral economics. |
| EHR | Switching cost + data-migration drag; staff retraining. |
| Clinical guidelines (update cycle) | Multi-year evidence-to-guideline lag — inertia in the methodology itself, not just the institutions. |

### Recommendations

**Immediate (this cycle)**
- Publish an honest audit of where your own CDSS sits on the Custom→Product spectrum; don't claim product maturity you haven't reached.
- Commission a fairness and equity review capability as a pioneer-staffed pilot — small team, accept high failure rate.
- Codify exception / appeals handling against the clinical guidelines layer; make it auditable.

**Short-term (6–18 months)**
- Consume EHR via FHIR as a utility wherever possible. Stop rebuilding integrations.
- Settle CDSS on top of the commodity data stack; move rule-based alerts toward product-grade observability.
- Build a real-world-evidence pipeline that feeds the evidence base layer (shortening the trials → guideline loop).

**Long-term (18 months+)**
- Industrialise AI-assisted diagnosis *once* it crosses into Custom-Built → Product (watch: multi-vendor competition, regulator-approved reimbursement codes, training certifications).
- Shift from per-institution guideline adaptation to federated, versioned guidelines with automatic formulary binding.
- Move fairness & equity review from genesis to custom-built with a dedicated methodology — this is a multi-year pioneer→settler handoff.

### Relevant gameplay and climatic patterns

- **Climatic — Higher-order systems create new value**: EHR/SNOMED/Cloud commoditising is what lets CDSS and AI diagnosis exist at all.
- **Climatic — Evolution cannot be measured over time**: AI-assisted diagnosis has been "imminent" for a decade; position by market maturity, not by how long it's been discussed.
- **Climatic — Past success breeds inertia**: Clinical judgement's defensive posture is the predictable pattern.
- **Gameplay — Industrialisation of the right-hand cluster**: Treat formulary, standards, regulatory approval, SNOMED as utilities. Build nothing here.
- **Gameplay — Pioneer/Settler/Planner split**: Pioneers own AI-assisted diagnosis and fairness review; settlers own CDSS and guideline-tooling; planners own EHR and formulary operations. Do not mix.
- **Doctrine — Use appropriate methods**: Don't treat CDSS as a product purchase yet; don't treat SNOMED/Cloud as bespoke build.

## Visual map (ASCII)

```
Title: Clinical Decision Making in Healthcare
Anchor: Patient
Date: 2022-08-01

                     Genesis    Custom     Product    Commodity
                        |          |          |          |
Visible             +---+----------+----------+----------+---+
                    |                                        |
                    |                                Patient | <- anchor
                    |                                 (0.96) |
                    |                               /  |   \ |
                    |                              /   |    \|
                    |                    Treatment outcome   |
                    |                    Treatment plan      |
                    |                    Medical practitioner|
                    |                    Medical institution |
                    |                    Payer               |
                    |                                        |
                    |                    Diagnosis           |
                    |   Exception/      Diagnostic reasoning |
                    |   appeals         Clinical judgement   |
                    |                                        |
                    |   Fairness &      Decision support     |
                    |   equity rev      (CDSS)               |
                    |                                        |
                    |   AI-assisted                          |
                    |   diagnosis       Permissible treat.   |
                    |                   Clinical guidelines  |
                    |                   Standards & prot.    |
                    |                   Formulary            |
                    |                   Regulatory approval  |
                    |                                        |
                    |   Clinical        Evidence base        |
                    |   trials          EHR ───────────→     |
Hidden              |                                        |
                    |                   SNOMED/ICD           |
                    |                   Health storage       |
                    |                   Cloud                |
                    +----------------------------------------+
Legend: Current position at left edge of each cluster; → indicates evolution movement.
```

## OnlineWardleyMaps source

See `draft.owm` in this directory. Paste into https://create.wardleymaps.ai to render.

```
title Clinical Decision Making in Healthcare (Aug 2022)

anchor Patient [0.96, 0.80]
component Treatment outcome [0.90, 0.55]
component Treatment plan [0.86, 0.50]
component Diagnosis [0.82, 0.42]
component Medical practitioner [0.88, 0.68]
component Medical institution [0.78, 0.74]
component Payer [0.70, 0.60]
component Setting of care [0.70, 0.70]
component Primary care [0.62, 0.78]
component Specialist clinic [0.60, 0.55]
component Hospital / inpatient [0.58, 0.72]
component Emergency care [0.58, 0.74]
component Community / home care [0.56, 0.62]
component Diagnostic reasoning [0.72, 0.48]
component Clinical judgement [0.68, 0.30]
component Decision support (CDSS) [0.50, 0.38]
component AI-assisted diagnosis [0.40, 0.15]
component Exception / appeals process [0.62, 0.22]
component Fairness and equity review [0.48, 0.12]
component Permissible treatments [0.66, 0.58]
component Clinical guidelines [0.50, 0.70]
component Standards and protocols [0.46, 0.80]
component Formulary / approved drug list [0.44, 0.82]
component Evidence base (RCT, meta-analysis) [0.40, 0.55]
component Clinical trials and reviews [0.30, 0.35]
component Regulatory approval (MHRA/FDA) [0.36, 0.78]
component Patient history / symptoms [0.74, 0.58]
component Clinical observation [0.68, 0.55]
component Diagnostic tests (lab/imaging) [0.50, 0.72]
component Electronic health record (EHR) [0.32, 0.68]
component Medical terminologies (SNOMED/ICD) [0.18, 0.88]
component Health data storage [0.12, 0.90]
component Cloud compute / networking [0.06, 0.95]

evolve AI-assisted diagnosis 0.45
evolve Decision support (CDSS) 0.60
evolve Electronic health record (EHR) 0.80
evolve Fairness and equity review 0.35
evolve Exception / appeals process 0.45
evolve Clinical trials and reviews 0.55
```
