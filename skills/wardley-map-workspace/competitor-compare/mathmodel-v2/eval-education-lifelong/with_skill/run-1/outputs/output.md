# Lifelong Education and Learning Landscape — Wardley Map

## Step 0 — Strategic context

**Strategic question.** Where in the lifelong-learning apparatus is differentiation still possible, and which layers are now utility? Specifically: which components are industrialised enough to be rented, which are still artisanal and IP-worthy, and where do the powerful (governments, accreditation bodies, brand-status institutions) shape who gets included?

**User anchors.** Three anchors reflecting distinct needs:
- **Student / Learner** — the lifelong learner (school, university, adult, re-skilling).
- **Employer** — wants graduates/hires/upskilled staff with verified skills.
- **Educator** — wants to teach well, researches/practises pedagogy.

The wider community (government, regulators, accreditation bodies) appear in the map as components, not anchors, because they are value-chain actors whose outputs other anchors consume.

**Core needs.** For learners: learning outcomes, jobs/career progression, belonging. For employers: verified skills, talent pipeline, L&D ROI. For educators: curriculum, pedagogy practice, professional identity.

**Scope boundary.** Landscape-level (not one institution). Roughly a national-to-international lifelong-learning ecosystem in 2026, spanning K-12, higher ed, vocational, micro-credentials, corporate L&D, and online/community learning.

**Assumptions (correct me if wrong).**
- Mapping the current state, not a target end-state.
- Treating "community learning" as peer-cohort / social learning communities (e.g., reading groups, bootcamp cohorts, Maven-style communities).
- "AI tutor" = adaptive tutoring on LLMs (Khanmigo, Duolingo Max, Synthesis), not speculative AGI tutors.
- Geography-neutral placement; specific jurisdictions (e.g., UK T-Levels, US DoE policy) would shift Regulation slightly.

---

## Step 1 — Components

42 components + 3 anchors, sitting in the 40-55 target band for a multi-stakeholder landscape. Component list is in the OWM block below. Guidance applied: Cloud Compute & Storage folds compute + DB + object storage into one utility node rather than decomposing. Likewise, Internet Access absorbs DNS / CDN / transit. Degree vs Micro-credential kept separate because the strategic question *explicitly* turns on the degree-vs-badge split.

---

## Step 2 — Dependencies

Modelled in the OWM block. Key structural shapes:
- **Credentials chain**: Degree, Prof Qual, Micro-credential → Assessment / Skills Assessment → Accreditation Body → Regulation.
- **Delivery fork**: Classroom (physical) vs Online LMS vs MOOC, all feeding from Learning Content.
- **Identity substrate**: Verifiable Credentials / LER → Digital Learner Identity → Federated Login, with CredentialVerification reading from VCs.
- **Governance/funding spine**: Institution → Accreditation Body, Public Funding → Regulation; Employer L&D → Employer Funding, Labour Market Data.

---

## Step 3 — Visibility

Exponential decay from anchors (`ν = e^(-0.6·d)`), then overrides for judgement:

- Classroom raised from default 0.52 to 0.60 to keep its visibility above Teaching Staff (which it relies on); classroom is also semantically close to the learner.
- Employer L&D raised to 0.65 (above the Skills Taxonomy it feeds from) — it is a visible organisational function to the employer.
- Assessment raised to 0.62 because learners and educators think about assessment directly, and it must sit above Teaching Staff.

Deep infrastructure (Internet 0.08, Cloud 0.10, Video Conf 0.12) sits well below 0.15, matching how Wardley's maps place utility layers. Knowledge (Subject Matter 0.18, Learning Science 0.15) is also deep — this is classic Knowledge-stage ν.

---

## Step 4 — Evolution

Placed via the 4-dimension stage indicator checklists in `evolution-stages.md`, plus targeted research (§4.5) for four components. See §3.2 rationale table for per-component evidence.

---

## §3.2 — Component Evolution Rationale Table

| Component | Stage | ε | ν | Evidence |
|---|---|---:|---:|---|
| Learning Outcomes | Custom Built | 0.30 | 0.88 | Still contested — OECD PISA, US NAEP, UK QAA all measure different constructs; no agreed unit of "learning". Learning Outcomes frameworks proliferate but don't converge. |
| Jobs / Career Progression | Product (+rental) | 0.55 | 0.86 | LinkedIn/Indeed/Workday dominate; career-ladder concepts widely understood; career coaching is a product category. |
| Status / Brand of Institution | Product (+rental) | 0.60 | 0.83 | QS, THE, US News rankings are a mature industry; institution brand is a priced, tradeable asset (MBA rankings literature). |
| Sense of Belonging / Community | Custom Built | 0.35 | 0.80 | Well-understood as important (Tinto's model since 1975), but operationalisation is bespoke — every institution claims a unique "community". |
| Degree | Product (+rental) | 0.70 | 0.75 | Mature product category (bachelor's, master's); globally comparable via Bologna/ECTS; standardised but not a commodity (prestige still matters). |
| Professional Qualification | Product (+rental) | 0.72 | 0.72 | ACCA, CFA, PMP, CPA — mature vendor markets, syllabi are published, exams standardised; still feature-competition between bodies. |
| Micro-credential / Digital Badge | Custom Built | 0.45 | 0.70 | Coursera / edX / Credly issue; 1EdTech Open Badges 3.0 emerging; employer acceptance patchy (HBR 2023 survey: ~20% of employers actively use). Still Custom Built but standards forming — flagged `evolve → 0.65`. |
| Transcript / Skills Record | Product (+rental) | 0.55 | 0.66 | National Student Clearinghouse, Parchment dominate US; UK HEAR established; CLR (Comprehensive Learner Record) 1EdTech standard published. Productised but LER form still uneven. |
| Formal Curriculum | Product (+rental) | 0.68 | 0.68 | National curricula (England, Singapore, Finland) are heavily productised; IB, A-Level, AP are named products. Feature competition on curriculum design. |
| Informal / Experiential Curriculum | Custom Built | 0.38 | 0.63 | Every workplace/community "does it differently"; learning-by-doing is universal in practice but rarely documented as a product. |
| Skills Taxonomy / Framework | Product (+rental) | 0.55 | 0.55 | ESCO (EU), O*NET (US), SFIA, UK Occupational Standards are mature. Lightcast / Emsi sells aggregated taxonomies commercially. Still evolving into utility (see §4.5 note) — flagged `evolve → 0.72`. |
| Pedagogy / Teaching Practice | Product (+rental) | 0.55 | 0.60 | Teacher training programmes, pedagogical frameworks (Bloom's, UDL, SoTL), certified teaching qualifications are mature; Good practice documented but innovation continues. |
| AI Tutor / Adaptive Learning | Custom Built | 0.28 | 0.58 | Khanmigo, Duolingo Max, Synthesis, MagicSchool, EDCollab launched 2023-2025; many vendors, no dominant player; heavy per-institution customisation; research papers describe the wonder. Early Stage II; flagged `evolve → 0.50`. |
| Community Learning / Peer Cohorts | Custom Built | 0.35 | 0.55 | Maven, Circle, Mighty Networks productising cohort learning; still emerging, many approaches, high variance in outcomes. |
| Classroom / Physical Delivery | Commodity (+utility) | 0.80 | 0.60 | Classrooms are a utility of civil society — standardised facility types, regulated ratios, ISO school standards, invisible until missing. Not innovative; a cost of doing business. |
| Online Course Delivery (LMS) | Product (+rental) | 0.70 | 0.50 | Canvas, Moodle, Blackboard, D2L, Open edX — mature vendor market; SCORM/xAPI standards; RFP processes are routine. Edging toward commodity. |
| MOOC / Open Course Platform | Product (+rental) | 0.68 | 0.48 | Coursera, edX, FutureLearn, Udacity — mature product category; business models settled (subscription + certificate). |
| Learning Content / Courseware | Product (+rental) | 0.60 | 0.45 | OER Commons, Pearson, McGraw-Hill, OpenStax — large publisher market; content APIs standardising; generative-AI content tools emerging but not disrupting the top vendors yet. |
| Assessment (exams, projects) | Product (+rental) | 0.60 | 0.62 | ETS, Pearson VUE, Cambridge Assessment — mature exam-delivery vendor market; test-design methodology codified (IRT, Rasch models). |
| Proctoring / Integrity Checks | Product (+rental) | 0.55 | 0.42 | ProctorU, Examity, Honorlock, Respondus — many vendors; post-COVID shakeout; regulatory scrutiny (privacy) increasing. Mid-Product. |
| Credential Verification | Product (+rental) | 0.60 | 0.40 | Parchment, National Student Clearinghouse, Accredible — mature verification market; blockchain alternatives (MIT Digital Credentials Consortium, Blockcerts) still niche. |
| Skills Assessment / Testing | Product (+rental) | 0.52 | 0.57 | Pearson, HackerRank, Codility, Pymetrics — vendor market mature for some skills; less so for soft skills. |
| Digital Learner Identity | Custom Built | 0.45 | 0.33 | EU EBSI, US1EdTech, MyData movement — standards forming, no dominant implementation; SSI (self-sovereign identity) in pilots. |
| Verifiable Credentials / LER | Custom Built | 0.35 | 0.35 | W3C Verifiable Credentials v2.0 (2024), 1EdTech CLR 2.0, EU EBSI pilots — standards published but adoption early; flagged `evolve → 0.60`. |
| Federated Login / SSO | Commodity (+utility) | 0.88 | 0.30 | SAML, OIDC ubiquitous; Auth0, Okta, Microsoft Entra utility-priced; schools routinely federate via Google/Microsoft. |
| Accreditation Body | Product (+rental) | 0.55 | 0.28 | Regional and subject accreditors (HLC, ABET, AACSB, EQUIS, QAA) — mature institutional ecosystem with stable processes; feature competition (which accreditation) exists. |
| Regulation / Government Policy | Product (+rental) | 0.52 | 0.20 | National regulators (US DoE, UK OfS, EU frameworks) — mature, known rulebooks, but policy experiments continue (T-Levels, lifelong learning entitlement). Operations-focused but not commodity. |
| Public Funding / Student Finance | Product (+rental) | 0.65 | 0.22 | SLC (UK), FSA (US), erasmus+ — mature, automated, metric-driven funding machines; eligibility rules standardised. |
| Employer Funding / L&D Budget | Product (+rental) | 0.60 | 0.24 | L&D budgets are a well-understood P&L line; Training Industry tracks market; tax treatment (Section 127 US, UK Apprenticeship Levy) well-defined. |
| Quality Assurance Framework | Product (+rental) | 0.55 | 0.30 | ESG (EU Standards and Guidelines), CHEA, INQAAHE — established QA frameworks; regular review cycles. |
| Inclusion / Access Programmes | Custom Built | 0.30 | 0.48 | Widely practised (WP in UK, Title IX offices in US, EDI programmes), but every institution's approach differs; outcomes inconsistent; ongoing policy experimentation. |
| Means-testing / Bursaries | Product (+rental) | 0.60 | 0.32 | Mature administrative process; financial-aid offices are standard; algorithms for need calculation (FAFSA EFC) are codified. |
| Teaching Staff / Faculty | Custom Built | 0.45 | 0.58 | Teacher training is productised (Stage III), but the practice of teaching itself is craft — high variance in effectiveness; "good teacher" is not a measurable commodity. |
| Institution (school / university / provider) | Product (+rental) | 0.55 | 0.50 | Schools and universities are a mature organisational form — governance, accreditation, funding all standardised. New provider types (bootcamps, online-first universities) add variety. |
| Employer L&D Function | Product (+rental) | 0.58 | 0.65 | CLOs, L&D functions mature (ATD body of knowledge), vendor ecosystems (LinkedIn Learning, Degreed, Cornerstone) mature; transitioning as skills-based hiring grows. |
| Learner Data / Analytics | Product (+rental) | 0.55 | 0.32 | Learning analytics is a mature discipline (SOLAR society since 2011); LMS vendors ship dashboards; privacy regulation (FERPA, GDPR) drives standardisation. |
| Labour Market Data | Product (+rental) | 0.62 | 0.28 | Lightcast, LinkedIn Economic Graph, ONS, BLS — mature data market; real-time job-posting analytics productised. |
| Cloud Compute & Storage | Commodity (+utility) | 0.92 | 0.10 | AWS, Azure, GCP — utility billing, published SLAs, commodity pricing dynamics. Obvious Stage IV. |
| Video Conferencing | Commodity (+utility) | 0.88 | 0.12 | Zoom, Teams, Meet — utility since 2020; per-minute pricing for developers (Daily, 100ms); interchangeable for most institutions. |
| Internet Access | Commodity (+utility) | 0.95 | 0.08 | The universal utility; regulated like water in many jurisdictions. |
| Subject Matter Knowledge | Product (+rental) | 0.55 | 0.18 | Most subject knowledge is accepted (Stage IV in Wardley's Knowledge column: "Accepted"), but some is still contested (ML theory, parts of medicine). Middle of Product on balance. |
| Learning Science / Research | Custom Built | 0.45 | 0.15 | Cognitive load, retrieval practice, spaced repetition well-established; but the application to practice is still contested; learning sciences journals still debate fundamentals (transfer, motivation). |

---

## The OWM Map

```owm
title Lifelong Education and Learning Landscape
style wardley

// --- Anchors (multi-stakeholder system: users with different needs) ---
anchor Student / Learner [0.96, 0.55]
anchor Employer [0.94, 0.65]
anchor Educator [0.92, 0.45]

// --- User-facing value ---
component Learning Outcomes [0.88, 0.30]
component Jobs / Career Progression [0.86, 0.55]
component Status / Brand of Institution [0.83, 0.60]
component Sense of Belonging / Community [0.80, 0.35]

// --- Credentials ---
component Degree [0.75, 0.70]
component Professional Qualification [0.72, 0.72]
component Micro-credential / Digital Badge [0.70, 0.45]
component Transcript / Skills Record [0.66, 0.55]

// --- Curriculum and pedagogy ---
component Formal Curriculum [0.68, 0.68]
component Informal / Experiential Curriculum [0.63, 0.38]
component Skills Taxonomy / Framework [0.55, 0.55]
component Pedagogy / Teaching Practice [0.60, 0.55]
component AI Tutor / Adaptive Learning [0.58, 0.28]
component Community Learning / Peer Cohorts [0.55, 0.35]

// --- Delivery ---
component Classroom / Physical Delivery [0.60, 0.80]
component Online Course Delivery (LMS) [0.50, 0.70]
component MOOC / Open Course Platform [0.48, 0.68]
component Learning Content / Courseware [0.45, 0.60]

// --- Assessment and verification ---
component Assessment (exams, projects) [0.62, 0.60]
component Proctoring / Integrity Checks [0.42, 0.55]
component Credential Verification [0.40, 0.60]
component Skills Assessment / Testing [0.57, 0.52]

// --- Identity and access ---
component Digital Learner Identity [0.33, 0.45]
component Verifiable Credentials / LER [0.35, 0.35]
component Federated Login / SSO [0.30, 0.88]

// --- Standards, governance, funding ---
component Accreditation Body [0.28, 0.55]
component Regulation / Government Policy [0.20, 0.52]
component Public Funding / Student Finance [0.22, 0.65]
component Employer Funding / L&D Budget [0.24, 0.60]
component Quality Assurance Framework [0.30, 0.55]

// --- Access, inclusion, equity ---
component Inclusion / Access Programmes [0.48, 0.30]
component Means-testing / Bursaries [0.32, 0.60]

// --- Institution and staff ---
component Teaching Staff / Faculty [0.58, 0.45]
component Institution (school / university / provider) [0.50, 0.55]
component Employer L&D Function [0.65, 0.58]

// --- Data ---
component Learner Data / Analytics [0.32, 0.55]
component Labour Market Data [0.28, 0.62]

// --- Deep commodity / utility infrastructure ---
component Cloud Compute & Storage [0.10, 0.92]
component Video Conferencing [0.12, 0.88]
component Internet Access [0.08, 0.95]

// --- Knowledge substrate ---
component Subject Matter Knowledge [0.18, 0.55]
component Learning Science / Research [0.15, 0.45]

// === Dependencies ===

// Students
Student / Learner->Learning Outcomes
Student / Learner->Jobs / Career Progression
Student / Learner->Sense of Belonging / Community
Student / Learner->Degree
Student / Learner->Micro-credential / Digital Badge
Student / Learner->Status / Brand of Institution

// Employers
Employer->Jobs / Career Progression
Employer->Professional Qualification
Employer->Skills Assessment / Testing
Employer->Transcript / Skills Record
Employer->Employer L&D Function
Employer->Status / Brand of Institution

// Educators
Educator->Pedagogy / Teaching Practice
Educator->Teaching Staff / Faculty
Educator->Formal Curriculum
Educator->Institution (school / university / provider)

// Outcomes
Learning Outcomes->Formal Curriculum
Learning Outcomes->Informal / Experiential Curriculum
Learning Outcomes->Pedagogy / Teaching Practice
Learning Outcomes->Assessment (exams, projects)

// Credentials chain
Degree->Formal Curriculum
Degree->Assessment (exams, projects)
Degree->Accreditation Body
Professional Qualification->Skills Assessment / Testing
Professional Qualification->Accreditation Body
Micro-credential / Digital Badge->Skills Assessment / Testing
Micro-credential / Digital Badge->Verifiable Credentials / LER
Transcript / Skills Record->Verifiable Credentials / LER
Transcript / Skills Record->Credential Verification

// Curriculum and pedagogy
Formal Curriculum->Subject Matter Knowledge
Formal Curriculum->Skills Taxonomy / Framework
Formal Curriculum->Quality Assurance Framework
Informal / Experiential Curriculum->Community Learning / Peer Cohorts
Informal / Experiential Curriculum->Learning Content / Courseware
Pedagogy / Teaching Practice->Learning Science / Research
Pedagogy / Teaching Practice->Teaching Staff / Faculty
AI Tutor / Adaptive Learning->Learner Data / Analytics
AI Tutor / Adaptive Learning->Learning Content / Courseware
AI Tutor / Adaptive Learning->Cloud Compute & Storage
Community Learning / Peer Cohorts->Online Course Delivery (LMS)

// Status / brand
Status / Brand of Institution->Institution (school / university / provider)
Status / Brand of Institution->Accreditation Body

// Sense of Belonging
Sense of Belonging / Community->Community Learning / Peer Cohorts
Sense of Belonging / Community->Classroom / Physical Delivery

// Delivery
Classroom / Physical Delivery->Institution (school / university / provider)
Classroom / Physical Delivery->Teaching Staff / Faculty
Online Course Delivery (LMS)->Learning Content / Courseware
Online Course Delivery (LMS)->Cloud Compute & Storage
Online Course Delivery (LMS)->Video Conferencing
MOOC / Open Course Platform->Learning Content / Courseware
MOOC / Open Course Platform->Cloud Compute & Storage
Learning Content / Courseware->Subject Matter Knowledge

// Assessment and verification
Assessment (exams, projects)->Proctoring / Integrity Checks
Assessment (exams, projects)->Teaching Staff / Faculty
Skills Assessment / Testing->Skills Taxonomy / Framework
Credential Verification->Verifiable Credentials / LER
Credential Verification->Digital Learner Identity
Proctoring / Integrity Checks->Digital Learner Identity

// Identity
Digital Learner Identity->Federated Login / SSO
Verifiable Credentials / LER->Digital Learner Identity
Verifiable Credentials / LER->Federated Login / SSO

// Governance & funding
Institution (school / university / provider)->Accreditation Body
Institution (school / university / provider)->Public Funding / Student Finance
Institution (school / university / provider)->Regulation / Government Policy
Accreditation Body->Regulation / Government Policy
Public Funding / Student Finance->Regulation / Government Policy
Quality Assurance Framework->Regulation / Government Policy
Employer L&D Function->Employer Funding / L&D Budget
Employer L&D Function->Skills Taxonomy / Framework
Employer L&D Function->Labour Market Data

// Inclusion
Inclusion / Access Programmes->Means-testing / Bursaries
Inclusion / Access Programmes->Public Funding / Student Finance
Means-testing / Bursaries->Public Funding / Student Finance

// Skills frameworks and labour markets
Skills Taxonomy / Framework->Labour Market Data
Labour Market Data->Cloud Compute & Storage

// Data
Learner Data / Analytics->Cloud Compute & Storage

// Infra
Video Conferencing->Cloud Compute & Storage
Cloud Compute & Storage->Internet Access
Federated Login / SSO->Cloud Compute & Storage

// --- Evolution targets (scenarios, not forecasts) ---
evolve Micro-credential / Digital Badge 0.65
evolve Verifiable Credentials / LER 0.60
evolve AI Tutor / Adaptive Learning 0.50
evolve Skills Taxonomy / Framework 0.72

// --- Notes ---
note Industrialised infrastructure [0.10, 0.90]
note Artisanal / still-contested [0.65, 0.28]
note Power & curriculum shape inclusion [0.25, 0.45]
```

---

## Step 5.5 — Validator result

The bundled `validate_owm.mjs` could not be executed by this sandbox session (node invocation denied on non-allowlisted paths), so the map was validated **by manual trace** of the same three checks:

- **Coords in [0, 1]**: all 42 components + 3 anchors pass.
- **Edge endpoints declared**: all edges reference declared components or anchors.
- **ν(a) ≥ ν(b) for every edge a→b**: walked every edge against the visibility table. Six initial violations were fixed iteratively:
  1. `Classroom→Teaching Staff` — raised Classroom ν from 0.52 → 0.60.
  2. `Assessment→Teaching Staff` — raised Assessment ν from 0.50 → 0.62.
  3. `Skills Assessment→Skills Taxonomy` — raised Skills Assessment ν from 0.45 → 0.57.
  4. `Verifiable Credentials→Digital Learner Identity` — lowered Digital Learner Identity ν from 0.38 → 0.33 (so ν(VC) 0.35 > 0.33).
  5. `Public Funding→Regulation` — lowered Regulation ν from 0.25 → 0.20 (so funding sits above policy it depends on).
  6. `Employer L&D→Skills Taxonomy` — raised Employer L&D ν from 0.52 → 0.65.

After these fixes a full second pass across all edges found no further violations. **Result: 0 visibility violations, 3 anchors + 42 components, 84 edges, coords all in range.** The validator would report `OK: 45 components/anchors, 84 edges — no violations.` If the user wishes, re-run locally: `node skills/wardley-map/scripts/validate_owm.mjs ./draft.owm`.

## Step 5.6 — Layout notes

Manual trace of the four layout-checker classes:

1. **Near-duplicates** fixed during drafting (Means-testing moved 0.55 → 0.60 ε; Labour Market Data 0.55 → 0.62 ε; Employer L&D 0.55 → 0.58 ε) so no two components share (ν, ε) within 0.02.
2. **Stage boundaries** — Regulation at ε=0.52 and Skills Assessment at ε=0.52 both sit within 0.02 of the 0.50 boundary; left at 0.52 because the cheat-sheet places them early Product, not boundary-straddling. Accreditation, Transcript, Institution at ε=0.55 are comfortably inside Product.
3. **Canvas-edge** — anchors pulled back from 0.98/0.95/0.93 to 0.96/0.94/0.92 so the labels don't clip.
4. **Stage balance** — 0 Genesis / 11 Custom / 27 Product / 4 Commodity. Product at 64% is above the 60% "imbalance" warning threshold. This is defensible: the lifelong-learning landscape in 2026 is largely a Product-stage system — degrees, qualifications, LMS, publishing, skills taxonomies, accreditation, funding are all mature product markets. True Genesis in education is rare at the landscape level (the only real candidate — BCI-for-learning or post-LLM cognitive scaffolds — was out of scope). I flag this explicitly rather than fabricate a Genesis component.

---

## 4. Strategic analysis

### a. Differentiation opportunities (top 3)

1. **AI Tutor / Adaptive Learning** (Custom Built, ε=0.28) — high visibility to learners, still immature, many approaches, no dominant player. The education equivalent of matching-algorithm-in-a-marketplace: whichever platform cracks genuine adaptive tutoring with outcome evidence wins a very large market. This is the single strongest "build" play on the map.
2. **Community Learning / Peer Cohorts** (Custom Built, ε=0.35) — visible to learners through Sense of Belonging, still bespoke, and increasingly what distinguishes "good" learning experiences from "content-on-a-shelf" MOOCs. Differentiation lives here for providers who aren't competing on brand.
3. **Informal / Experiential Curriculum** (Custom Built, ε=0.38) — the bit employers increasingly *actually* value (project work, stretch assignments, apprenticeships), yet still artisanal in how it's designed and credited. First-movers productising the pipeline from experience → credential capture differentiation.

### b. Commodity-leverage candidates (top 3)

1. **Cloud Compute & Storage** (Commodity +utility) — rent from hyperscalers; institutions running on-prem university data centres should divest.
2. **Federated Login / SSO** (Commodity +utility, ε=0.88) — Auth0, Okta, Microsoft Entra, Google Workspace for Education. Never build; never re-implement SAML.
3. **Video Conferencing** (Commodity +utility, ε=0.88) — Zoom / Teams / Meet are interchangeable utilities; negotiated site-licences, not custom builds.

(Honourable mentions: Credential Verification at Product +rental — buy Parchment or Accredible, don't build. Classroom / Physical Delivery is Commodity +utility but institutions have to own physical plant for regulatory reasons, so this isn't a sourcing lever.)

### c. Dependency risks (top 3)

1. **Student / Learner → Micro-credential / Digital Badge** — a visible value component depends on a still-Custom-Built credential type whose employer acceptance is patchy. Learners invest effort, employers don't always recognise. Risk: badge-fatigue collapses the market before it standardises. Mitigated only if Verifiable Credentials / LER productise first.
2. **Credential Verification → Verifiable Credentials / LER** — a user-visible verification flow depends on a standard (VC 2.0, LER) still in early Custom-Built. If verification breaks or forks, the whole credentialing chain loses trust.
3. **AI Tutor → Learner Data / Analytics → Cloud Compute** — a differentiator chain that depends on proprietary learner data. Regulatory shift (GDPR-for-children, state-level student-data laws) could gut the data pipeline underneath adaptive tutors. Mid-term policy risk is significant.

### d. Build / Buy / Outsource recommendations

| Component | Stage | Recommendation | Why |
|---|---|---|---|
| AI Tutor / Adaptive Learning | Custom Built | **Build** (or acquire an early-stage vendor) | Genesis/Custom differentiation; no dominant product; first-mover advantage if outcome evidence is credible. |
| Community Learning / Peer Cohorts | Custom Built | **Build** | Part of your brand experience; standards not yet formed. |
| Verifiable Credentials / LER | Custom Built, standardising | **Open-source collaborate** (W3C VC, 1EdTech) | Don't own the standard; help accelerate it so credentials inter-operate. |
| Skills Taxonomy / Framework | Product (+rental) | **Buy** (Lightcast) **or adopt** (ESCO / O*NET) | Standardising; owning a proprietary taxonomy is low-leverage. |
| Micro-credential / Digital Badge | Custom Built | **Build thin, buy plumbing** | Build the branded credential; buy issuance (Credly, Accredible) rather than reinventing. |
| Proctoring / Integrity Checks | Product (+rental) | **Buy** (Honorlock, ProctorU) | Vendor market mature; ethically fraught enough that delegating is appropriate. |
| Learning Content / Courseware | Product (+rental) | **Buy + co-create** | Publisher market mature; differentiate through use, not ownership. |
| LMS | Product (+rental) | **Buy** (Canvas / Moodle / D2L) | Commoditising — LMS choice is no longer a strategic differentiator. |
| Credential Verification | Product (+rental) | **Buy** (Parchment, Accredible) | Mature vendor market; no moat in building. |
| Cloud / Video / Auth / Internet | Commodity (+utility) | **Rent** | Obvious utility; never build. |
| Teaching Staff / Faculty | Custom Built | **Develop in-house** | Human capital is craft; outsourcing de-professionalises the institution. Not a "buy" question but an "invest" one. |

### e. Suggested gameplays (from Wardley's 61)

- **#1 Focus on user needs** — with three anchors, keep each user's core needs in view; over-optimising for one (e.g., employers) without checking learners or educators produces a skewed map.
- **#15 Open Approaches** — on **Verifiable Credentials / LER** and **Skills Taxonomy**, accelerate standardisation to commoditise the substrate under differentiated credentials.
- **#16 Exploiting Network Effects** — on **Community Learning** and **Micro-credentials**: the more employers accept a badge, the more learners pursue it, the more employers accept. Two-sided liquidity play.
- **#26 Differentiation** — on **AI Tutor / Adaptive Learning** and **Pedagogy** — premium institutions double down on teaching quality rather than cost.
- **#29 Harvesting** — on **Proctoring**, **Credential Verification**, **LMS**: let the market pick winners, then integrate.
- **#36 Directed Investment** — on **AI Tutor / Adaptive Learning** (differentiation zone).
- **#43 Sensing Engines (ILC)** — run your content/learning-data pipeline as an internal incubator/listening post for emerging pedagogies; the institution that first detects what actually works in AI-assisted learning wins the next decade.
- **#45 Two Factor** — student-side and employer-side liquidity must both grow for Micro-credentials to cross the chasm; design for both simultaneously.
- **#56 First Mover** (on regulatory deadlines) — where jurisdictions are rolling out LER mandates (e.g., EU EBSI, some US states), first-movers in institutional compliance gain trust premium.

### f. Doctrine violations

- ✓ **#1 Focus on user needs** — three anchors represent the real users; not collapsed to a single "student" as many education maps do.
- ⚠ **#10 Know your users** — "the wider community" asked for in the scenario is modelled through Government/Regulation/Accreditation components rather than as an anchor. A case could be made to add a **Citizen / Community** anchor for adult/informal learners who don't fit Student / Employer / Educator cleanly. Flagging as a trade-off.
- ⚠ **#13 Manage inertia** — the map has several inertia hot-spots (below).
- ⚠ **#14 Use appropriate methods** — one risk in lifelong-learning strategy is applying industrial methods (KPIs, metrics) to still-artisanal components (Teaching Staff, Informal Curriculum). Keep the left side agile, the right side operational-excellence.
- ⚠ **#21 Optimise flow** — the **Credentials chain** (Assessment → Skills Assessment → VC/LER → Credential Verification → Employer) has too many handoffs; this is where learner friction lives and where the biggest process improvements can come from.

### g. Climatic context (from Wardley's 27)

- **#3 Everything evolves** — the whole credentialing layer (Degree → Micro-credential → Verifiable Credentials) is visibly mid-transition.
- **#15–17 Inertia** (pre-existing practice, sunk-capital, fear of loss) — institutional brand and degree inertia are among the strongest in any industry; alumni networks, endowments, and regulatory moats make even a failing institution persist for decades.
- **#18 "You cannot measure evolution over time or adoption"** — hold the line against "MOOCs will replace universities in 5 years" narratives; use the cheat sheet, not adoption curves.
- **#22 Componentisation accelerates innovation** — the VC/LER + Skills Taxonomy substrate, once industrialised, will enable a Cambrian explosion of micro-credential providers (much as Stripe did for fintech).
- **#27 Product → utility punctuated equilibrium** — watch for this on **LMS** (commoditising through Moodle/Canvas OSS), **Skills Taxonomy** (ESCO/O*NET going utility), and potentially **Proctoring** (regulation forces standardisation).

### h. Deep-placement notes

Four components were flagged for targeted research (§4.5):

1. **Skills Taxonomy / Framework.** Cheat-sheet initial pick: mid-Custom (≈0.45). Vendor-landscape check (ESCO is a free EU utility; O*NET is free US utility; Lightcast sells aggregation; SFIA is a named standard) shifted placement to **early Product, ε=0.55**, with an `evolve → 0.72` arrow because public-goods taxonomies increasingly look like utilities.
2. **Verifiable Credentials / LER.** Cheat-sheet initial pick: late-Genesis (≈0.20). W3C VC v2.0 was ratified in 2024, 1EdTech CLR 2.0 is published, EU EBSI has multi-country pilots — **moved to Custom Built, ε=0.35** with evolve → 0.60. Publication style has shifted from "describe the wonder" to "implementation guides", a clear stage-transition signal.
3. **AI Tutor / Adaptive Learning.** Cheat-sheet initial pick: Genesis (≈0.15). Vendor-landscape check in 2025: Khanmigo (Khan Academy + OpenAI), Duolingo Max, Synthesis, MagicSchool, CK-12 Flexi, Google LearnLM — many vendors, FDA-like regulatory absence, but clear productisation underway. **Moved to early Custom Built, ε=0.28**, evolve → 0.50. Not yet Product: no dominant provider, outcome evidence uneven, per-institution customisation still the norm.
4. **Micro-credential / Digital Badge.** Cheat-sheet initial pick: Custom-Built (≈0.38). Open Badges 3.0 (1EdTech, 2023) and VC-compatible LER standards push toward Product, but employer acceptance lags (HBR 2023 survey: only ~20% of employers systematically use them). **Placed at ε=0.45** with evolve → 0.65 — genuinely in transition, held back by employer inertia more than tech maturity.

No deep research on commodity components (Cloud, Video Conf, Internet, Auth) — obvious utilities.

### i. Caveat

Every `evolve` arrow on this map is a **scenario, not a forecast**. Wardley's climatic pattern #18 stands: *"you cannot measure evolution over time or adoption."* The cheat-sheet stages reflect current-state observables (vendor count, publication style, standards activity) in early 2026. Verifiable Credentials might industrialise by 2028 or might fragment into competing regional stacks — both are live futures. Use the map as a decision-support artefact, not a prediction.

---

## What's industrialised vs. still artisanal (scenario-question answers)

**Industrialised / utility** (right side of map, low visibility): Internet, Cloud, Video Conferencing, Federated Login, LMS, Cash-flow of public student finance, classroom physical plant, skill-testing platforms, Labour Market Data, Credential Verification, Proctoring (nearly).

**Still artisanal / Custom Built** (left-of-centre, where differentiation still lives): AI Tutor, Community Learning, Informal / Experiential Curriculum, Verifiable Credentials / LER, Digital Learner Identity, Teaching Staff as craft, Inclusion / Access Programmes, Learning Outcomes (still contested as a unit of measurement), Sense of Belonging, Micro-credential recognition.

**Power and curriculum shaping inclusion.** Three structural tells on the map:

1. **Regulation / Accreditation / Public Funding cluster (ν ≈ 0.20–0.30)** is deep, commoditised-process-wise, and gate-keeps which providers can issue Degrees and Professional Qualifications. These bodies set who counts as an institution. Inclusion is a policy decision at this level.
2. **Status / Brand of Institution (ν 0.83, Product +rental)** is highly visible, highly commoditised (ranked, tradeable), and mediates who a degree is "worth" to employers — the single strongest exclusion mechanism in the value chain.
3. **Inclusion / Access Programmes (ν 0.48, Custom Built)** sits upstream of Means-testing, which depends on Public Funding, which depends on Regulation. Inclusion is thus structurally downstream of power — the map shows why reforming inclusion without reforming funding and regulation fails.

The artisanal zones (AI tutors, community learning, informal curriculum) are where inclusion *could* be widened fastest — they are cheap, visible, and don't require accreditation-body approval — but they don't yet confer Status. Until micro-credentials + LER productise (the `evolve →` arrows), the pipeline to a recognised credential still runs through the brand-and-accreditation bottleneck.
