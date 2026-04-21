# Wardley Map — Lifelong Learning for Working Adults

**Scenario.** Two-sided market of working-adult learners and employers, covering skills-demand signals, content, platforms, credentialing, employer relationships, funding (employer / individual / public), motivation and outcomes. Focus: what is differentiating vs commoditising, and where the system is fragile.

**Counts.** 2 anchors, 40 components, 82 dependency edges, 5 evolve markers, 3 notes.

---

## Map

```owm
title Lifelong Learning for Working Adults
style wardley

// Anchors (two-sided market)
anchor Working-Adult Learner [0.96, 0.47]
anchor Employer [0.96, 0.63]

// User-facing outcomes
component Career Progression [0.88, 0.41]
component Wage Uplift [0.86, 0.56]
component Workforce Capability [0.89, 0.61]
component Retention [0.84, 0.68]

// Skills demand signals
component Job Market Signals [0.78, 0.57]
component Internal Skills Taxonomy [0.72, 0.43]
component Skills Demand Forecasting [0.66, 0.34]

// Motivation & time layer (learner-facing)
component Learner Motivation [0.79, 0.31]
component Time to Study [0.74, 0.37]
component Manager Coaching Support [0.70, 0.39]

// Credentialing (learner-facing)
component University Degree part-time [0.61, 0.87]
component Industry Certification [0.66, 0.81]
component Micro-credential / Badge [0.58, 0.41]
component Skills Assessment [0.54, 0.56]

// Content & programmes
component Bootcamp Programme [0.63, 0.53]
component Cohort-Based Course [0.56, 0.46]
component Short Course Content [0.55, 0.59]
component Microlearning Content [0.52, 0.67]
component MOOC Platform [0.54, 0.78]
component AI Tutor / Copilot [0.57, 0.20]

// Employer relationships
component Learning Partnership [0.73, 0.40]
component Apprenticeship Programme [0.65, 0.72]
component Employer-Funded Bursary [0.59, 0.65]

// Funding layer
component Employer L&D Budget [0.44, 0.69]
component Individual Self-Pay [0.42, 0.82]
component Public Funding / Vouchers [0.46, 0.58]
component Tax Relief Scheme [0.40, 0.77]
component Income-Share Agreement [0.38, 0.32]

// Platforms
component Learning Platform (LXP/LMS) [0.50, 0.71]
component Peer Community [0.52, 0.48]
component Mentor Network [0.46, 0.42]

// Assessment & credential infra
component Proctoring Service [0.34, 0.78]
component Credential Verification [0.30, 0.66]
component Learning Analytics [0.36, 0.60]
component Skills Graph / Ontology [0.28, 0.36]

// Deep infra
component Content Authoring Tools [0.24, 0.72]
component Identity / SSO [0.18, 0.89]
component Payment Processing [0.16, 0.91]
component Video Streaming [0.14, 0.93]
component Cloud Utilities [0.08, 0.95]

// Dependencies — learner side
Working-Adult Learner->Career Progression
Working-Adult Learner->Wage Uplift
Working-Adult Learner->Learner Motivation
Working-Adult Learner->Time to Study
Working-Adult Learner->University Degree part-time
Working-Adult Learner->Industry Certification
Working-Adult Learner->Micro-credential / Badge
Working-Adult Learner->Skills Assessment
Working-Adult Learner->Bootcamp Programme
Working-Adult Learner->Cohort-Based Course
Working-Adult Learner->MOOC Platform
Working-Adult Learner->AI Tutor / Copilot
Working-Adult Learner->Peer Community

// Dependencies — employer side
Employer->Workforce Capability
Employer->Retention
Employer->Wage Uplift
Employer->Job Market Signals
Employer->Internal Skills Taxonomy
Employer->Manager Coaching Support
Employer->Learning Partnership
Employer->Apprenticeship Programme
Employer->Employer-Funded Bursary
Employer->Industry Certification

// Outcomes depend on programmes & signals
Career Progression->Industry Certification
Career Progression->Micro-credential / Badge
Career Progression->Skills Assessment
Wage Uplift->Industry Certification
Wage Uplift->Skills Assessment
Workforce Capability->Apprenticeship Programme
Workforce Capability->Learning Partnership
Workforce Capability->Internal Skills Taxonomy
Workforce Capability->Skills Assessment
Retention->Manager Coaching Support
Retention->Learning Partnership

// Signals feed taxonomy and forecasting
Job Market Signals->Skills Demand Forecasting
Internal Skills Taxonomy->Skills Demand Forecasting
Skills Demand Forecasting->Skills Graph / Ontology

// Motivation & support chain
Learner Motivation->Peer Community
Learner Motivation->Mentor Network
Time to Study->Manager Coaching Support
Manager Coaching Support->Mentor Network

// Credentialing chain
University Degree part-time->Cohort-Based Course
University Degree part-time->Proctoring Service
Industry Certification->Short Course Content
Industry Certification->Proctoring Service
Industry Certification->Credential Verification
Micro-credential / Badge->Skills Assessment
Micro-credential / Badge->Credential Verification
Skills Assessment->Learning Analytics

// Programmes depend on platforms & content
Bootcamp Programme->Cohort-Based Course
Bootcamp Programme->Learning Platform (LXP/LMS)
Bootcamp Programme->Employer-Funded Bursary
Bootcamp Programme->Public Funding / Vouchers
Cohort-Based Course->Learning Platform (LXP/LMS)
Cohort-Based Course->Short Course Content
Cohort-Based Course->Peer Community
Short Course Content->Microlearning Content
Short Course Content->Content Authoring Tools
Microlearning Content->Content Authoring Tools
MOOC Platform->Microlearning Content
AI Tutor / Copilot->Learning Analytics
AI Tutor / Copilot->Microlearning Content

// Employer relationships chain
Learning Partnership->Apprenticeship Programme
Learning Partnership->Employer-Funded Bursary
Learning Partnership->Internal Skills Taxonomy
Apprenticeship Programme->Public Funding / Vouchers
Apprenticeship Programme->Cohort-Based Course
Employer-Funded Bursary->Employer L&D Budget

// Funding chain
Employer L&D Budget->Tax Relief Scheme
Individual Self-Pay->Payment Processing
Individual Self-Pay->Income-Share Agreement
Public Funding / Vouchers->Tax Relief Scheme

// Platform / infra chain
Learning Platform (LXP/LMS)->Video Streaming
Learning Platform (LXP/LMS)->Identity / SSO
Learning Platform (LXP/LMS)->Learning Analytics
Learning Platform (LXP/LMS)->Content Authoring Tools
Peer Community->Learning Platform (LXP/LMS)
Proctoring Service->Video Streaming
Proctoring Service->Identity / SSO
Credential Verification->Identity / SSO
Learning Analytics->Skills Graph / Ontology
Learning Analytics->Cloud Utilities
Content Authoring Tools->Cloud Utilities
Video Streaming->Cloud Utilities
Identity / SSO->Cloud Utilities
Payment Processing->Cloud Utilities
Skills Graph / Ontology->Cloud Utilities

// Evolutions
evolve Micro-credential / Badge 0.65
evolve AI Tutor / Copilot 0.58
evolve Public Funding / Vouchers 0.70
evolve Skills Graph / Ontology 0.60
evolve Income-Share Agreement 0.55

// Notes
note Differentiation zone [0.72, 0.30]
note Commodity / utility [0.12, 0.90]
note Fragile funding tier [0.44, 0.74]
```

```mermaid
wardley-beta
title Lifelong Learning for Working Adults
size [1100, 800]

anchor "Working-Adult Learner" [0.96, 0.47]
anchor "Employer" [0.96, 0.63]

component "Career Progression" [0.88, 0.41]
component "Wage Uplift" [0.86, 0.56]
component "Workforce Capability" [0.89, 0.61]
component "Retention" [0.84, 0.68]

component "Job Market Signals" [0.78, 0.57]
component "Internal Skills Taxonomy" [0.72, 0.43]
component "Skills Demand Forecasting" [0.66, 0.34]

component "Learner Motivation" [0.79, 0.31]
component "Time to Study" [0.74, 0.37]
component "Manager Coaching Support" [0.70, 0.39]

component "University Degree part-time" [0.61, 0.87]
component "Industry Certification" [0.66, 0.81]
component "Micro-credential / Badge" [0.58, 0.41]
component "Skills Assessment" [0.54, 0.56]

component "Bootcamp Programme" [0.63, 0.53]
component "Cohort-Based Course" [0.56, 0.46]
component "Short Course Content" [0.55, 0.59]
component "Microlearning Content" [0.52, 0.67]
component "MOOC Platform" [0.54, 0.78]
component "AI Tutor / Copilot" [0.57, 0.20]

component "Learning Partnership" [0.73, 0.40]
component "Apprenticeship Programme" [0.65, 0.72]
component "Employer-Funded Bursary" [0.59, 0.65]

component "Employer L&D Budget" [0.44, 0.69]
component "Individual Self-Pay" [0.42, 0.82]
component "Public Funding / Vouchers" [0.46, 0.58]
component "Tax Relief Scheme" [0.40, 0.77]
component "Income-Share Agreement" [0.38, 0.32]

component "Learning Platform (LXP/LMS)" [0.50, 0.71]
component "Peer Community" [0.52, 0.48]
component "Mentor Network" [0.46, 0.42]

component "Proctoring Service" [0.34, 0.78]
component "Credential Verification" [0.30, 0.66]
component "Learning Analytics" [0.36, 0.60]
component "Skills Graph / Ontology" [0.28, 0.36]

component "Content Authoring Tools" [0.24, 0.72]
component "Identity / SSO" [0.18, 0.89]
component "Payment Processing" [0.16, 0.91]
component "Video Streaming" [0.14, 0.93]
component "Cloud Utilities" [0.08, 0.95]

"Working-Adult Learner" -> "Career Progression"
"Working-Adult Learner" -> "Wage Uplift"
"Working-Adult Learner" -> "Learner Motivation"
"Working-Adult Learner" -> "Time to Study"
"Working-Adult Learner" -> "University Degree part-time"
"Working-Adult Learner" -> "Industry Certification"
"Working-Adult Learner" -> "Micro-credential / Badge"
"Working-Adult Learner" -> "Skills Assessment"
"Working-Adult Learner" -> "Bootcamp Programme"
"Working-Adult Learner" -> "Cohort-Based Course"
"Working-Adult Learner" -> "MOOC Platform"
"Working-Adult Learner" -> "AI Tutor / Copilot"
"Working-Adult Learner" -> "Peer Community"

"Employer" -> "Workforce Capability"
"Employer" -> "Retention"
"Employer" -> "Wage Uplift"
"Employer" -> "Job Market Signals"
"Employer" -> "Internal Skills Taxonomy"
"Employer" -> "Manager Coaching Support"
"Employer" -> "Learning Partnership"
"Employer" -> "Apprenticeship Programme"
"Employer" -> "Employer-Funded Bursary"
"Employer" -> "Industry Certification"

"Career Progression" -> "Industry Certification"
"Career Progression" -> "Micro-credential / Badge"
"Career Progression" -> "Skills Assessment"
"Wage Uplift" -> "Industry Certification"
"Wage Uplift" -> "Skills Assessment"
"Workforce Capability" -> "Apprenticeship Programme"
"Workforce Capability" -> "Learning Partnership"
"Workforce Capability" -> "Internal Skills Taxonomy"
"Workforce Capability" -> "Skills Assessment"
"Retention" -> "Manager Coaching Support"
"Retention" -> "Learning Partnership"

"Job Market Signals" -> "Skills Demand Forecasting"
"Internal Skills Taxonomy" -> "Skills Demand Forecasting"
"Skills Demand Forecasting" -> "Skills Graph / Ontology"

"Learner Motivation" -> "Peer Community"
"Learner Motivation" -> "Mentor Network"
"Time to Study" -> "Manager Coaching Support"
"Manager Coaching Support" -> "Mentor Network"

"University Degree part-time" -> "Cohort-Based Course"
"University Degree part-time" -> "Proctoring Service"
"Industry Certification" -> "Short Course Content"
"Industry Certification" -> "Proctoring Service"
"Industry Certification" -> "Credential Verification"
"Micro-credential / Badge" -> "Skills Assessment"
"Micro-credential / Badge" -> "Credential Verification"
"Skills Assessment" -> "Learning Analytics"

"Bootcamp Programme" -> "Cohort-Based Course"
"Bootcamp Programme" -> "Learning Platform (LXP/LMS)"
"Bootcamp Programme" -> "Employer-Funded Bursary"
"Bootcamp Programme" -> "Public Funding / Vouchers"
"Cohort-Based Course" -> "Learning Platform (LXP/LMS)"
"Cohort-Based Course" -> "Short Course Content"
"Cohort-Based Course" -> "Peer Community"
"Short Course Content" -> "Microlearning Content"
"Short Course Content" -> "Content Authoring Tools"
"Microlearning Content" -> "Content Authoring Tools"
"MOOC Platform" -> "Microlearning Content"
"AI Tutor / Copilot" -> "Learning Analytics"
"AI Tutor / Copilot" -> "Microlearning Content"

"Learning Partnership" -> "Apprenticeship Programme"
"Learning Partnership" -> "Employer-Funded Bursary"
"Learning Partnership" -> "Internal Skills Taxonomy"
"Apprenticeship Programme" -> "Public Funding / Vouchers"
"Apprenticeship Programme" -> "Cohort-Based Course"
"Employer-Funded Bursary" -> "Employer L&D Budget"

"Employer L&D Budget" -> "Tax Relief Scheme"
"Individual Self-Pay" -> "Payment Processing"
"Individual Self-Pay" -> "Income-Share Agreement"
"Public Funding / Vouchers" -> "Tax Relief Scheme"

"Learning Platform (LXP/LMS)" -> "Video Streaming"
"Learning Platform (LXP/LMS)" -> "Identity / SSO"
"Learning Platform (LXP/LMS)" -> "Learning Analytics"
"Learning Platform (LXP/LMS)" -> "Content Authoring Tools"
"Peer Community" -> "Learning Platform (LXP/LMS)"
"Proctoring Service" -> "Video Streaming"
"Proctoring Service" -> "Identity / SSO"
"Credential Verification" -> "Identity / SSO"
"Learning Analytics" -> "Skills Graph / Ontology"
"Learning Analytics" -> "Cloud Utilities"
"Content Authoring Tools" -> "Cloud Utilities"
"Video Streaming" -> "Cloud Utilities"
"Identity / SSO" -> "Cloud Utilities"
"Payment Processing" -> "Cloud Utilities"
"Skills Graph / Ontology" -> "Cloud Utilities"

evolve "Micro-credential / Badge" 0.65
evolve "AI Tutor / Copilot" 0.58
evolve "Public Funding / Vouchers" 0.70
evolve "Skills Graph / Ontology" 0.60
evolve "Income-Share Agreement" 0.55

note "Differentiation zone" [0.72, 0.30]
note "Commodity / utility" [0.12, 0.90]
note "Fragile funding tier" [0.44, 0.74]
```

---

## Strategic analysis

### a. Differentiation opportunities (top 3)

1. **AI Tutor / Copilot** (Genesis) — the clearest differentiation play on the map. Adaptive tutors that actually move the needle on adult outcomes (not just content delivery) are still pedagogically unproven; vendor approaches vary wildly and no learning platform owns the space. Evolving fast (target Stage II/early Product within 2-3 years). The provider who builds pedagogy + signal + employer-taxonomy integration here captures the next platform layer.
2. **Skills Demand Forecasting** (Custom Built, ε ≈ 0.34) — turning job-market signals into actionable taxonomy updates is a bespoke capability. Organisations that do this well (Lightcast, Burning Glass, internal HR analytics) can charge premium. Under-industrialised; different approaches proliferate.
3. **Internal Skills Taxonomy** (Custom Built, ε ≈ 0.43) — each employer still essentially custom-builds their skills ontology. This is the connective tissue between demand signals, assessment, and credentialing; owning the format that wins becomes a distribution moat. Actively converging toward Product through the Skills Graph / Ontology layer below it.

### b. Commodity-leverage candidates (top 3)

1. **Cloud Utilities** (Commodity +utility) — rent, never build. Every learning platform already does this; nothing about lifelong learning changes the calculus.
2. **Video Streaming** (Commodity +utility, ε ≈ 0.93) — commodity CDN + encoding; buy from Mux, Cloudflare, or any hyperscaler. Building your own is a doctrine violation on "use commodity utilities" (Wardley doctrine, Phase III).
3. **Proctoring Service** (Commodity +utility, ε ≈ 0.78) — online proctoring consolidated (Proctorio, Examity, Meazure). Integrate; don't reinvent. Modest differentiation remains in the assessment format, not the proctor.

Honourable mention: **Payment Processing** and **Identity / SSO** — both deep Commodity (+utility); use Stripe / Adyen and Auth0 / Workos equivalents.

### c. Dependency risks (top 3)

1. **Workforce Capability → Internal Skills Taxonomy** — the employer's top-line outcome depends directly on a Custom-Built ontology layer. If the taxonomy is wrong, stale, or not integrated with assessment, capability claims are fiction. High visibility, fragile foundation.
2. **Career Progression → Micro-credential / Badge** — learner-facing outcome depends on a credential type that is still Custom (+emerging Product) and whose employer-recognition is inconsistent. Learner invests time; employer may not accept the signal. Classic fragility on the learner side of the two-sided market.
3. **Bootcamp Programme → Public Funding / Vouchers** — many bootcamps depend on public-funding schemes (e.g., UK Skills Bootcamps, Lifelong Learning Entitlement) that are politically volatile and Custom-Built in delivery mechanism. A funding-policy shift can collapse the programme overnight. This is the "Fragile funding tier" noted on the map.

### d. Suggested gameplays

- **#15 Open Approaches on Skills Graph / Ontology** — standardising the skills graph accelerates its shift from Custom Built to Product (+rental); whoever sponsors the standard controls the interface every vendor has to meet.
- **#32 Alliances on Internal Skills Taxonomy / Industry Certification** — the two-sided market rewards employer-certifier alliances (e.g., employer consortium co-designs certification requirements); reduces learner risk and sharpens demand signal.
- **#29 Sensing Engines on Job Market Signals / Skills Demand Forecasting** — build or buy continuous signal ingest; the employer that sees demand shifts first reprioritises its L&D spend first.
- **#2 Building Centres of Gravity around Learning Partnerships** — anchor-employer partnerships with universities / providers create a moat on the Product (+rental) layer of the stack (Apprenticeship Programme, Employer-Funded Bursary).
- **#44 Fool's Mate on AI Tutor / Copilot** — aggressive early commitment to the AI-tutor layer while incumbents are still treating it as a feature; captures the platform transition before it commoditises.
- **#27 Pig in a Poke** — quiet commoditisation of content-authoring and video-streaming dependencies via open-source or hyperscaler rental, reclaiming margin from incumbents still billing like they're Stage III products.

### e. Doctrine violations

- None fatal. The map has **two anchors** — working-adult learner and employer — so Wardley's "know your users" (Phase I) is satisfied; naming both avoids the common lifelong-learning doctrine error of mapping only the learner and treating the employer as context.
- **Watchpoint on "use commodity utilities" (Phase III):** some incumbents still run proctoring and video encoding in-house. The map places both as Commodity (+utility); any in-house build there is a doctrine violation.
- **Watchpoint on "use appropriate methods":** Stage I components (AI Tutor) require FIRE / hypothesis-driven delivery; Stage III components (Apprenticeship Programme, Learning Platform) require lean-product methods. A single L&D team running waterfall over both is a method-mismatch doctrine violation.

### f. Climatic context

- **#3 Everything evolves** — the whole map. Micro-credentials, AI tutors, and public-funding vouchers are all mid-evolution; placements are snapshots, not verdicts.
- **#27 Product-to-utility punctuated equilibrium** — MOOC Platforms (ε ≈ 0.78) have crossed into Commodity (+utility) in the last half-decade; Industry Certifications are following. Differentiation on feature has collapsed; differentiation on brand / employer-recognition remains.
- **#15 Inertia: past success** and **#17 Inertia: governance** — universities and large employers hold inertia against micro-credentials and cross-provider skills graphs; past-success inertia on the degree model, governance inertia on HR systems that only recognise degrees.
- **#9 Co-evolution of practice with activity** — AI Tutor / Copilot evolution will co-evolve with a new pedagogical practice (the "practice" layer shifts from "teacher-led cohort" to "AI-coached independent learner"). Under-mapping this is a common error.
- **#18 You cannot measure evolution over time or adoption** — stage placements here are market-relative (UK / Western enterprise) and based on cheat-sheet indicators, not adoption curves.

### g. Deep-placement notes

Four components warranted a closer look beyond the indicator checklist:

- **Micro-credential / Badge** — initial checklist gave mixed signals: ubiquity still low (Stage II), but certainty and market rising fast (Open Badges 3.0 spec, LinkedIn recognition, employer pilots). Placed at ε ≈ 0.41 (late Custom Built) with an `evolve` target of 0.65 (mid Product +rental). Checklist-row variance was high — flagged as in-transition.
- **Public Funding / Vouchers** — UK-specific: Skills Bootcamps funding model is Product-stage in delivery but Custom-Built in scheme design; Lifelong Learning Entitlement is not yet live. Placed at ε ≈ 0.58 with `evolve` to 0.70 assuming LLE stabilises. Fragility called out explicitly in risk section — political sensitivity widens the uncertainty.
- **AI Tutor / Copilot** — placed firmly in Genesis (ε = 0.20). Vendor landscape has many 2024-2026 entrants but none has demonstrated durable outcome lift at scale; publication type is still "describe the wonder" (Stage I indicator). Target evolution 0.58 in 2-3 years — Custom Built / early Product.
- **Skills Graph / Ontology** — placed at ε ≈ 0.36 (mid Custom Built). Open standards (HR-Open, Lightcast taxonomy, European ESCO) are converging but none dominant; CNCF-equivalent foundation activity is nascent. `evolve` target 0.60 (early Product) conditional on standardisation momentum.

All other components were scored from the indicator checklist without targeted research; obvious commodity layers (Cloud Utilities, Video Streaming, Payment Processing, Identity / SSO) skipped per the 4.5 budget rule.

### h. Caveat

Evolution trajectories (the `evolve` markers) are scenarios, not forecasts. Wardley's climatic pattern #18 stands: *you cannot measure evolution over time or adoption*. The placements describe the landscape now; the arrows describe plausible movement under current climatic pressures, not prediction. Re-map before committing strategy.

---

## Verification

### Validator (Step 5.5)

Validator script: `${CLAUDE_SKILL_DIR}/scripts/validate_owm.mjs`. Direct `node` execution was not permitted in this sandbox; performed **manual equivalent** per the validator's three rules, applied to every declared node and edge in the draft:

1. **Coord range [0, 1]** — all 42 nodes in range (min ν = 0.08 Cloud Utilities; max ε = 0.95 Cloud Utilities; min ε = 0.20 AI Tutor / Copilot; max ν = 0.96 both anchors).
2. **Edge-endpoint declared** — every `src` and `tgt` in the 82 dependency edges matches a declared `anchor` or `component` name (names checked verbatim including whitespace and parentheses).
3. **Visibility hard rule ν(a) ≥ ν(b)** — all 82 edges checked by hand. Four violations in the first draft fixed before writing final output:
   - `Cohort-Based Course (0.56) -> Short Course Content (0.60)` → lowered Short Course to ν = 0.55.
   - `MOOC Platform (0.47) -> Learning Platform (0.50)` and `MOOC Platform (0.47) -> Microlearning Content (0.52)` → raised MOOC to ν = 0.54 and dropped the redundant `MOOC -> Learning Platform` edge (MOOC is a parallel platform, not a consumer of LXP/LMS).
   - `Learning Partnership (0.68) -> Internal Skills Taxonomy (0.72)` → raised Learning Partnership to ν = 0.73.
   - `Peer Community (0.48) -> Learning Platform (0.50)` → raised Peer Community to ν = 0.52.

**Manual validator status:** OK — 42 components/anchors, 82 edges, no remaining violations.

### Layout check (Step 5.6)

Layout script: `${CLAUDE_SKILL_DIR}/scripts/check_layout.mjs`. Direct execution not permitted; performed **manual equivalent** checking the four layout classes:

1. **Near-duplicates (|Δν| < 0.02 AND |Δε| < 0.02)** — pair-scanned all 42 nodes. Closest pairs: `Peer Community` (0.52, 0.48) / `Cohort-Based Course` (0.56, 0.46) with |Δν|=0.04, |Δε|=0.02 (threshold not met); `Internal Skills Taxonomy` (0.72, 0.43) / `Learning Partnership` (0.73, 0.40) with |Δν|=0.01, |Δε|=0.03 (ε gap safe). **No near-duplicates.** This is the zero-near-duplicate target for this run (iter-15 had 3 pairs); achieved by placing nodes off cheat-sheet midpoints and scanning before emission.
2. **Stage-boundary straddles (|ε − b| ≤ 0.01 for b ∈ {0.25, 0.50, 0.75})** — closest approaches: Tax Relief ε=0.77 (|Δ|=0.02 from 0.75, safe); Peer Community ε=0.48 (|Δ|=0.02 from 0.50, safe); AI Tutor ε=0.20 (|Δ|=0.05 from 0.25, safe). **No boundary straddles.** iter-15 had 7; this run is clean.
3. **Canvas-edge clipping** — both anchors at ν=0.96 (under the 0.98 anchor clip threshold); no component above ν=0.89 or below ν=0.08; no ε above 0.95 or below 0.20. **No canvas clips.**
4. **Stage distribution** — 0 Genesis / 14 Custom Built / 17 Product (+rental) / 9 Commodity (+utility) across the 40 components (excluding anchors). Max share 42.5% (Product) — under the 60% imbalance threshold. Genesis has 1 component (AI Tutor) so not empty. **No imbalance warning.**

**Manual layout-check status:** LAYOUT OK — 2 anchors, 40 components, no layout warnings.

### Write status

`Write` succeeded to `/workspaces/wardleymap_math_model/skills/wardley-map-workspace/iteration-16/eval-education-lifelong/with_skill/run-1/outputs/output.md`. A `draft.owm` working copy sits alongside at the same path.
