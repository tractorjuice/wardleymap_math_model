# Clinical Decision-Making in Healthcare — Wardley Map (August 2022)

**Scenario.** How medical practitioners and institutions reach treatment decisions for patients, including the knowledge layer (trials, reviews, historical data), the decision components (diagnosis, treatment options, permissible treatment under funding rules), the settings of care (primary, ER, virtual, assisted living), and the outcomes (patient health, clinical metrics, fairness). All scoring is pinned to August 2022 — i.e., before the ChatGPT release and before the large-language-model wave reshaped clinical decision support.

## The Map

```owm
title Clinical Decision-Making in Healthcare (August 2022)
style wardley

// Anchors — the two user types whose needs drive the value chain
anchor Patient [0.98, 0.55]
anchor Clinician [0.96, 0.50]

// Outcomes (what the users actually care about)
component Patient Health Outcome [0.92, 0.45]
component Clinical Outcome Metrics [0.86, 0.62]
component Fairness / Equity in Care [0.84, 0.22]

// User-facing decision & consultation
component Patient-Clinician Consultation [0.88, 0.58]
component Treatment Decision [0.80, 0.40]
component Diagnosis [0.78, 0.55]
component Treatment Options [0.75, 0.55]
component Permissible Treatment [0.72, 0.62]

// Settings of care
component Primary Care Visit [0.78, 0.78]
component ER / Emergency Care [0.78, 0.80]
component Virtual Visit / Telehealth [0.76, 0.62]
component Assisted Living Care [0.74, 0.58]

// Decision support & knowledge
component Clinical Decision Support [0.62, 0.60]
component Diagnostic AI / ML [0.58, 0.38]
component Prior Authorization [0.60, 0.65]
component Formulary [0.58, 0.80]
component Coverage / Funding Rules [0.56, 0.78]
component Clinical Guidelines [0.55, 0.78]
component Patient History [0.55, 0.65]
component Historical EHR Data [0.50, 0.60]
component Systematic Reviews [0.48, 0.80]
component Lab Results [0.42, 0.85]
component Imaging / Radiology [0.42, 0.82]
component Clinical Trials / RCTs [0.42, 0.82]
component Medical Literature [0.38, 0.85]

// Platform / commodity layer
component EHR / EMR [0.32, 0.82]
component Clinical Coding (ICD/SNOMED/LOINC) [0.25, 0.82]
component Identity / Auth [0.18, 0.90]

// Dependencies — Patient
Patient->Patient Health Outcome
Patient->Patient-Clinician Consultation
Patient->Treatment Decision

// Dependencies — Clinician
Clinician->Treatment Decision
Clinician->Diagnosis
Clinician->Patient-Clinician Consultation
Clinician->Clinical Outcome Metrics
Clinician->Fairness / Equity in Care

// Outcomes
Patient Health Outcome->Treatment Decision
Patient Health Outcome->Clinical Outcome Metrics
Clinical Outcome Metrics->Historical EHR Data
Clinical Outcome Metrics->Clinical Coding (ICD/SNOMED/LOINC)
Fairness / Equity in Care->Historical EHR Data
Fairness / Equity in Care->Clinical Coding (ICD/SNOMED/LOINC)

// Consultation into settings
Patient-Clinician Consultation->Primary Care Visit
Patient-Clinician Consultation->ER / Emergency Care
Patient-Clinician Consultation->Virtual Visit / Telehealth
Patient-Clinician Consultation->Assisted Living Care

// Decision -> its three sub-decisions
Treatment Decision->Diagnosis
Treatment Decision->Treatment Options
Treatment Decision->Permissible Treatment

// Diagnosis
Diagnosis->Lab Results
Diagnosis->Imaging / Radiology
Diagnosis->Patient History
Diagnosis->Clinical Decision Support
Diagnosis->Diagnostic AI / ML
Diagnosis->Clinical Coding (ICD/SNOMED/LOINC)

// Treatment options — the knowledge funnel
Treatment Options->Clinical Guidelines
Treatment Options->Systematic Reviews
Treatment Options->Medical Literature
Treatment Options->Clinical Trials / RCTs

// Permissible treatment — the funding/rules filter
Permissible Treatment->Formulary
Permissible Treatment->Coverage / Funding Rules
Permissible Treatment->Prior Authorization

// Funding rules dependencies
Formulary->Coverage / Funding Rules
Prior Authorization->Formulary
Prior Authorization->EHR / EMR
Coverage / Funding Rules->Clinical Guidelines
Coverage / Funding Rules->Systematic Reviews

// Guidelines / reviews chain
Clinical Guidelines->Systematic Reviews
Clinical Guidelines->Clinical Trials / RCTs
Systematic Reviews->Clinical Trials / RCTs
Systematic Reviews->Medical Literature

// Decision support
Clinical Decision Support->Clinical Guidelines
Clinical Decision Support->EHR / EMR
Diagnostic AI / ML->Historical EHR Data
Diagnostic AI / ML->Imaging / Radiology
Diagnostic AI / ML->Lab Results

// Historical data
Historical EHR Data->EHR / EMR

// Settings of care on the platform
Primary Care Visit->EHR / EMR
Primary Care Visit->Patient History
ER / Emergency Care->EHR / EMR
ER / Emergency Care->Patient History
ER / Emergency Care->Imaging / Radiology
ER / Emergency Care->Lab Results
Virtual Visit / Telehealth->EHR / EMR
Virtual Visit / Telehealth->Identity / Auth
Assisted Living Care->EHR / EMR
Assisted Living Care->Patient History

// Records & codes
Patient History->EHR / EMR
Patient History->Clinical Coding (ICD/SNOMED/LOINC)
Lab Results->Clinical Coding (ICD/SNOMED/LOINC)
Imaging / Radiology->EHR / EMR

// Evolve arrows — directional scenarios, not forecasts
evolve Diagnostic AI / ML 0.60
evolve Virtual Visit / Telehealth 0.78
evolve Fairness / Equity in Care 0.45
evolve Historical EHR Data 0.75

note BUILD differentiation [0.75, 0.25]
note RENT / utility [0.25, 0.88]
```

Validator result: **OK — 30 components/anchors, 63 edges, no violations.**

---

## Strategic Analysis

Stage labels lead; numbers follow only to disambiguate. Everything below is scored against the August 2022 understanding of each component — not the post-ChatGPT 2024–26 picture.

### a. Differentiation opportunities (top 3)

1. **Fairness / Equity in Care** (Genesis, edging into Custom Built) — in August 2022 this is still a research frontier: Obermeyer et al.'s 2019 *Science* paper on risk-score bias is cited constantly, FDA's "Software as a Medical Device" action plan is still early, and no institution has a standardised, audited fairness pipeline running on live clinical decisions. Any health system or vendor that industrialises a credible fairness-monitoring layer over live decisions captures the highest-visibility uncharted component on the map.
2. **Diagnostic AI / ML** (Custom Built) — radiology AI has scattered 510(k) clearances (Viz.ai, IDx-DR, Aidoc) but adoption is uneven, workflows are bespoke, and there is no dominant vendor. A clinician-visible AI layer that actually changes diagnosis (not just alerts) is where the moat sits.
3. **Treatment Decision** (Custom Built) — the act of synthesising diagnosis + options + permissibility into a specific recommendation remains craft. Most of the "decision" is in clinicians' heads and is not instrumented. Operationalising it (e.g., decision-rationale capture, shared decision-making tools) converts tacit craft into an asset.

### b. Commodity-leverage candidates (top 3)

1. **EHR / EMR** (Commodity (+utility)) — Epic and Cerner/Oracle dominate in the US; dominant vendors exist in UK/EU. Don't build an EHR; integrate.
2. **Clinical Coding (ICD/SNOMED/LOINC)** (Commodity (+utility)) — standards bodies own these. Use them; never own them.
3. **Medical Literature** and **Clinical Trials / RCTs infrastructure** (Commodity (+utility)) — PubMed, ClinicalTrials.gov, Cochrane Library are industrialised public/private utilities. Rent access; contribute data; never try to replicate the index.

A second tier of commodity-leverage: **Lab Results** (LabCorp/Quest + LIS is utility infrastructure), **Imaging / Radiology** (DICOM + PACS is utility), **Identity / Auth** (standard OIDC/SAML).

### c. Dependency risks (top 3)

1. **Treatment Decision → Diagnostic AI / ML** — a user-visible decision leaning on an immature, multi-vendor, unvalidated-at-scale layer. Most Diagnostic AI in 2022 is bench-validated but workflow-fragile; clinician trust is uneven; failure modes are opaque. This is the single most fragile limb of the tree for any institution adopting AI aggressively.
2. **Clinical Outcome Metrics → Historical EHR Data** — visible outcome measurement depends on historical EHR data that is inconsistent across sites, sparsely coded, and often missing the social and environmental variables needed to make the metrics meaningful. FHIR R4 is out, the CMS Interoperability Rule is in effect, but the data on the ground is messy.
3. **Fairness / Equity in Care → Historical EHR Data** — the same substrate problem bites harder here. You cannot measure fairness in outcomes without demographic labelling, representative cohorts, and clean stratification — all of which are sparse in real EHR extracts in August 2022. The fairness function is fragile because the data under it is not yet modelled.

Also worth calling out: **Permissible Treatment → Prior Authorization** — a visible "can you have this drug/procedure?" decision depending on a stage-III process that is inconsistent, vendor-specific, manually operated, and widely regarded (by clinicians) as broken.

### d. Suggested gameplays

- **#1 Focus on user needs** — the two-anchor shape (Patient + Clinician) is correct; keep re-anchoring. Insurers and regulators are secondary users worth surfacing in a richer map.
- **#36 Directed investment** on **Diagnostic AI / ML** and on **Fairness / Equity in Care** — these are the two highest-differentiation components and both are still uncharted; a concentrated bet pays off more here than anywhere else on the map.
- **#43 Sensing Engines (ILC)** on **Diagnostic AI / ML** — run an innovate-leverage-commoditise cycle: stand up a platform that watches which AI models move the needle on outcomes, then harvest the winners.
- **#15 Open Approaches** on **Fairness / Equity in Care** — this is precisely the class of component where open standards, open benchmarks, and open audit tooling will accelerate the stage I→II→III shift and build trust. Do not try to privately own the definition of "fairness".
- **#41 Alliances** on **Historical EHR Data** — no single institution has enough; federated data alliances (OHDSI, TriNetX) are the unit that can give the fairness and AI layers enough substrate.
- **#29 Harvesting** on **Virtual Visit / Telehealth** — post-COVID the market is consolidating. Watch Teladoc/Amwell/Doximity and acquire the operational patterns that emerge; do not re-build.
- **#22 Limitation of competition** on **Prior Authorization** (reverse reading) — this is actually being applied *to* clinicians today; a useful map insight is that this gameplay is running against you. Countermove: **#39 Undermining barriers to entry** via PA-automation standards (CMS's proposed Prior Authorization rule is the regulatory tailwind).
- **#56 First mover** on **Fairness / Equity in Care auditing** — FDA action plan + emerging regulatory expectations mean there is a narrow window to establish the standard.
- **#30 Standards game** on **Diagnostic AI / ML** — push FDA's Good Machine Learning Practice (GMLP) and model-card-style disclosures to become the industry expectation.

### e. Doctrine notes

- **#1 Focus on user needs, #10 Know your users** — satisfied: both Patient and Clinician are explicit anchors. A richer version of this map would add Insurer/Payer and Regulator as third/fourth anchors, which would move **Coverage / Funding Rules** and **Prior Authorization** closer to the top.
- **#9 Think small (know the details)** — partially satisfied: "Treatment Options" is a coarse component that in a real workshop would decompose into drug therapy, surgical therapy, lifestyle intervention, watchful waiting, palliative care. Decomposing it is the next iteration.
- **#13 Manage inertia** — the map is heavy with consumer-side inertia forms: **#8 skill acquisition cost** (clinicians retraining on AI tools), **#6 confusion over method** (too many AI diagnostic vendors), **#9 re-architecture cost** (EHR migrations are generational), **#14 strategic-control loss** (fear of automation replacing clinical judgment). These should be enumerated alongside any `evolve` arrow.
- **#22 Use standards where appropriate** — satisfied on the right side of the map (FHIR, SNOMED, DICOM, LOINC, ICD). The risk is *premature* standardisation on the left: do not standardise Diagnostic AI or Fairness-auditing before patterns emerge — that is a Genesis/Custom region where FIRE (#15) applies.
- **#7 Use appropriate methods** — this is violated by any organisation running the whole map with a single methodology. ER and Primary Care (Commodity (+utility)) want operational excellence and six-sigma-like variation reduction. Diagnostic AI and Fairness (Custom Built / Genesis) want agile, hypothesis-driven, small-team work. Mixing these up is a classic organisational failure mode.

### f. Climatic context

- **#3 Everything evolves through supply and demand competition** — the whole knowledge funnel (trials → reviews → guidelines → CDS) has already evolved right; the AI layer is now being pulled in the same direction.
- **#11 Future value is inversely proportional to certainty** — Diagnostic AI and Fairness carry the highest potential value precisely because they are the most uncertain pieces of the map in 2022.
- **#15–17 Inertia and the punctuated equilibrium (#27)** — Virtual Visit / Telehealth is mid-way through a Product (+rental) → Commodity (+utility) transition driven by COVID-era demand; the organisations that still treat it as a Genesis experiment are behind the curve, and the organisations that have fully operationalised it are harvesting the demand.
- **#18 You cannot measure evolution over time or adoption** — the scoring in this map is for August 2022; the `evolve` arrows are scenarios, not forecasts.
- **#22 Two different forms of disruption** — Diagnostic AI is a Genesis-driven disruption (new uncharted component); Virtual Visit is a Product-to-utility disruption (existing component industrialising). They need different responses.
- **#24 Efficiency enables innovation** — commoditising the bottom of the stack (EHR, coding, labs) is what frees capacity for the AI and fairness work at the top.

### g. Deep-placement notes

Four components warranted closer attention because they are strategically critical and/or in rapid transition. All priors are pinned to August 2022.

- **Diagnostic AI / ML.** Initial cheat-sheet placement Stage II mid (ε ≈ 0.375). Targeted reasoning: by August 2022, the FDA had cleared a material but not large number of AI/ML-based medical devices (the FDA list grew from ~29 in 2020 to somewhere over 170 by late 2022, dominated by radiology). Multiple active vendors (Viz.ai, Aidoc, Rad AI, Paige, Caption Health) but no single dominant one; adoption concentrated in large academic centres; workflow integration bespoke per site. Publications are a mix of "describing the wonder" (Stage I) and "case studies / implementation" (Stage II) — not yet "operations/maintenance" (Stage III). Confirms Stage II, placed ε = 0.38. Flag: high uncertainty, treat as a range ε ∈ [0.30, 0.45].
- **Virtual Visit / Telehealth.** Initial cheat-sheet placement Stage III mid. Targeted reasoning: post-COVID, CMS temporarily relaxed telehealth rules in 2020, still extended in 2022; multiple large vendors (Teladoc, Amwell, Doxy.me, Doximity Dialer); adoption widespread but stabilising down from peak. Ubiquity is Stage III→IV; certainty is Stage III (models still shaking out); user perception is Stage III (expected when appropriate, still a leading-edge channel in some specialties). Placed ε = 0.62 (mid Product (+rental)). This is the component with the fastest arrow on the map — `evolve` target 0.78 reflects a likely Product (+rental) → Commodity (+utility) transition within a few years.
- **Fairness / Equity in Care.** Initial cheat-sheet placement Stage I (ε ≈ 0.125). Targeted reasoning: Obermeyer 2019 is the seminal paper; NIH All of Us is running; FDA's AI/ML SaMD action plan (2021) names bias as a priority; EU AI Act draft is in play but not law. Scholarly output is growing exponentially but operational implementations in live clinical decisions are rare. Two cheat-sheet rows (publication types, ubiquity) clearly point at Stage I; user perception is Stage I→II ("leading edge, cautiously excited"). Nudged to ε = 0.22 — still Genesis, but bleeding into early Custom Built as some US health systems stand up internal fairness dashboards.
- **Historical EHR Data.** Initial cheat-sheet placement Stage III mid. Targeted reasoning: FHIR R4 published 2018, CMS Interoperability and Patient Access Final Rule effective 2021 requiring FHIR APIs, ONC's Cures Act Final Rule enforcing information blocking prohibitions. Ubiquity is Stage III (growing, not yet universal); certainty is Stage III; market is Stage III (Epic/Cerner/Oracle/Allscripts + third parties like Health Catalyst, Datavant); convergence (FHIR) is happening but real-world data is still messy. Placed ε = 0.60 (mid Product (+rental)), with `evolve` arrow to 0.75 reflecting the expected industrialisation over the next 3–5 years.

Components not deep-placed (obvious commodities): EHR platform, clinical coding, medical literature indexing, lab results infra, imaging/PACS, auth. These are all solidly Commodity (+utility) and the scoring is uncontroversial.

### h. Where clinical decision-making is fragile (direct answer to the user's question)

Three fragility zones dominate:

1. **The AI-into-decision limb.** Diagnostic AI is Custom Built and plugged directly into a Product (+rental) stage diagnosis process that drives a Custom-Built treatment decision. It's a stack of uncharted components carrying a high-visibility payload. Failure modes are opaque, validation is thin outside the reference sites, and clinician trust is uneven. This is the most strategically important fragility on the map because the promised payoffs are highest here.
2. **The knowledge-into-permissibility chain.** Treatment Options pulls from Guidelines → Systematic Reviews → Trials (a chain of Commodity (+utility) knowledge), then Permissible Treatment filters through Coverage / Funding / Formulary / Prior Authorization. The knowledge side is mature; the filter side is Product (+rental) stage and inconsistent, with Prior Authorization widely regarded as broken. A "good" treatment can be blocked not for clinical reasons but because the permissibility layer is brittle.
3. **The outcomes-and-fairness measurement layer.** Clinical Outcome Metrics and Fairness both depend on Historical EHR Data — which in August 2022 is in the middle of a Product (+rental) → Commodity (+utility) transition via FHIR. Until that transition completes, outcome measurement is uneven and fairness measurement is effectively impossible at scale. This fragility is hidden because it shows up as missing data rather than wrong data — you do not see the metrics you cannot compute.

A secondary fragility to flag: **setting-of-care heterogeneity.** ER, Primary Care, Virtual Visit, and Assisted Living all plug into the same decision machinery but have very different data completeness, time pressure, and clinician training. The same map element ("Treatment Decision") runs fundamentally differently in a 10-minute ER encounter vs. a 20-minute virtual primary-care visit.

### i. Differentiating vs. commoditising — direct answer

- **Differentiating (BUILD) in August 2022:** Fairness / Equity in Care, Diagnostic AI / ML, Treatment Decision instrumentation. These are the components where meaningful moats can still be built. Add a distant fourth: Patient-Clinician Consultation *quality* (the craft of shared decision-making) — a human-capital component that resists commoditisation.
- **Commoditising (RENT / leverage):** EHR platform, Clinical Coding standards, Medical Literature indexing, Clinical Trials / RCT infrastructure, Lab Results, Imaging / Radiology, Identity / Auth. Treat as utilities. Any organisation still trying to build its own EHR or its own coding taxonomy in 2022 has lost the plot.
- **In active transition (watch):** Virtual Visit / Telehealth (Product (+rental) → Commodity (+utility)) and Historical EHR Data (Product (+rental) → Commodity (+utility) via FHIR). These are the components where climatic pattern #27 (punctuated equilibrium) applies most sharply; decisions about them should be made fast.

### j. Derived heuristics — attention prompts only

These three scores are the skill's math-model heuristics, not canonical Wardley concepts. Use for attention, not verdicts.

- **Top-3 differentiation pressure D = ν·(1−ε):** Fairness / Equity in Care (0.84·0.78 ≈ 0.66), Treatment Decision (0.80·0.60 = 0.48), Diagnostic AI / ML (0.58·0.62 ≈ 0.36). Patient Health Outcome also scores high but is a goal, not a buildable component.
- **Top-3 commodity leverage K = (1−ν)·ε:** Identity / Auth (0.82·0.90 ≈ 0.74), Clinical Coding (0.75·0.82 ≈ 0.62), EHR / EMR (0.68·0.82 ≈ 0.56). These are the obvious rents.
- **Top-3 dependency risks R = ν(a)·(1−ε(b)):** Treatment Decision(0.80) → Diagnostic AI(ε=0.38) ≈ 0.50; Clinician(0.96) → Fairness(ε=0.22) ≈ 0.75 (highest on the map); Patient Health Outcome(0.92) → Treatment Decision(ε=0.40) ≈ 0.55. The Clinician → Fairness risk is notable: the map says clinicians are institutionally responsible for equitable care but are being asked to deliver it on top of a Genesis-stage measurement apparatus.

### k. Caveat

Evolution is a position, not a trajectory, and certainly not a timeline. Wardley's climatic pattern #18 stands: *you cannot measure evolution over time or adoption.* The `evolve` arrows in this map (Diagnostic AI to 0.60, Virtual Visit to 0.78, Fairness to 0.45, Historical EHR Data to 0.75) are directional scenarios reflecting the pressures visible in August 2022, not predictions. The world in which ChatGPT is released in November 2022 is outside this map's scoring horizon — a future iteration scored for 2024 or 2026 would place Diagnostic AI materially differently and add LLM-based clinical reasoning as a new, high-visibility Genesis component of its own.
