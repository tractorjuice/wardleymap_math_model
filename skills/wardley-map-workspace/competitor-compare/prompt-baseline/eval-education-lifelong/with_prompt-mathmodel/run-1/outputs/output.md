# Wardley Map: Lifelong Education and Learning Landscape

## 1. Scenario restatement

Map the lifelong education and learning ecosystem end-to-end — students, employees, employers, educators, institutions, government and regulators, and the wider community — covering curricula (formal and informal), skills, certification and standards, assessment and verification, degrees versus micro-credentials and badges, digital identity, status and brand, inclusion and exclusion, the online/physical delivery split, and emerging pieces such as AI tutors and community learning. Separate the industrialised parts from the still-artisanal parts, and name where power and curriculum decide who gets included.

## 2. Components V and anchors U

Six anchors are warranted — this is not a single-user domain:

- Student / Learner (primary)
- Employee (learner-in-role)
- Employer (demand side for skills)
- Educator (producer of teaching)
- Government / Regulator (policy, funding, frameworks)
- Wider Community (informal and community learning)

Components are grouped in the OWM file into six layers: user-facing propositions, delivery surfaces, assessment/verification/certification, institutions and educators, enabling platforms, and foundations (policy, data, infrastructure). Total: 6 anchors + 36 components.

## 3. Dependencies E

Directed. Read "A -> B" as "A depends on B". The graph is a DAG. Key chains:

- Student -> Degree Qualification -> Formal Curriculum -> Assessment -> Proctoring -> Video Conferencing -> Broadband / Cloud.
- Employer -> Employment Outcome -> Verification of Learning -> Digital Identity -> Credential Wallet.
- Student -> Skills Development -> AI Tutor -> Foundation Models (LLMs).
- Wider Community -> Community Learning -> Informal Curriculum -> Content Library / OER.

The visibility constraint $\nu(a) \ge \nu(b)$ holds on every edge in the file.

## 4. Visibility ν (Y-axis)

Seeded via shortest-path distance from the anchor set, then adjusted:

- Raised visibility for Status / Brand Signalling — learners and employers think about it directly even though it's technically derived from Certification + Institution.
- Raised visibility for Inclusion / Access — policy-makers treat it as a first-class outcome, not a derivative.
- Lowered visibility for Video Conferencing and Proctoring — architecturally present but invisible to the learner.
- Lowered visibility for Foundation Models — an upstream substrate, not something the learner sees.

## 5. Evolution ε (X-axis) — quick 4-row cheat-sheet rationale

Scored per component using the Ubiquity / Certainty / User Perception / Publication Types rows. Averages placed each component in one of the four stage bands. Representative placements:

| Component | Stage | ε | Rationale |
|---|---|---|---|
| Degree Qualification | IV | 0.82 | Ubiquitous, understood, standard expectation. Inertia flag (see §8). |
| Formal Curriculum | III→IV | 0.70 | Widely adopted, maintenance-phase publications, but national variance keeps it pre-utility. |
| Physical Classroom Delivery | IV | 0.80 | The baseline delivery mode for centuries. |
| Online Course Delivery | III | 0.72 | Post-2020 mainstream, product-stage, consolidating. |
| Micro-credential / Badge | II | 0.45 | Rapid learning, leading-edge framing, explosive growth but not yet standard. |
| AI Tutor | I→II | 0.18 | Different / exciting / surprising; publications describe the wonder. |
| Credential Wallet | I→II | 0.30 | W3C VC standards emerging but not widespread. |
| Digital Identity | II→III | 0.50 | Common in adjacent sectors (gov, banking); still fragmented in education. |
| Assessment | III | 0.68 | Product/rental stage — standardised frameworks with variance. |
| Accreditation Standards | III | 0.60 | National bodies, well-understood processes. |
| Learning Management System | IV | 0.78 | Canvas/Moodle/Blackboard are commodity. |
| Video Conferencing | IV | 0.88 | Utility. |
| Cloud Compute / Broadband | IV | 0.90–0.92 | Utility. |
| Foundation Models (LLMs) | II | 0.40 | Rapid learning, product-like access but far from standardised. |
| Informal Curriculum | II | 0.35 | Widely practised but never standardised; power resides in who defines it. |
| Community Learning | II | 0.30 | Long history, still artisanal; libraries, U3A, meetups, peer-circles. |
| Mentoring / Coaching | II | 0.35 | Professionalised in pockets, still artisanal at scale. |
| Pedagogy | II→III | 0.50 | Known craft, multiple competing schools — not a utility. |

## 6. What's industrialised vs what's artisanal

- Industrialised (Stage III–IV): Degree Qualification, Formal Curriculum, Physical Classroom Delivery, Online Course Delivery, Assessment, Certification Issuance, LMS, Video Conferencing, Payment / Student Finance, Cloud, Broadband.
- In transition (Stage II–III): Accreditation Standards, Qualification Frameworks, Digital Identity, Pedagogy, Verification of Learning.
- Still artisanal (Stage I–II): AI Tutor, Micro-credential / Badge, Credential Wallet, Informal Curriculum, Community Learning, Mentoring, Peer study groups, Foundation Models as a learning substrate.

## 7. Where power and curriculum shape inclusion

Two nodes determine who gets in and who is kept out:

- Formal Curriculum (ν 0.74, ε 0.70) sits upstream of Assessment, Certification, and Institution. Whoever writes it decides what counts as knowledge.
- Accreditation Standards + Qualification Frameworks (ν ≈ 0.50, ε ≈ 0.60–0.70) gate which credentials are recognised — and therefore which learners' effort is visible to employers.

Inclusion / Access is therefore not primarily a delivery problem — it is a curriculum-and-standards problem. Broadband and Funding are necessary but not sufficient; the learner also needs their learning to be recognised by the accreditation apparatus, which is controlled by the state and incumbent institutions.

## 8. Strategic analysis

### a. Top 3 by D (differentiation pressure, $D = \nu \cdot (1 - \varepsilon)$)

1. Community Learning — $0.82 \times 0.70 = 0.574$. High visibility (anchor-adjacent to Wider Community, Learner) and still Stage II. Differentiation space for civic / municipal / peer-led models.
2. Inclusion / Access — $0.80 \times 0.60 = 0.480$. Visible political outcome, still artisanal in execution. Room for a winning approach.
3. Informal Curriculum — $0.72 \times 0.65 = 0.468$. Highly visible to the Wider Community anchor, early-stage, no dominant standard.

Honorable mention: Micro-credential / Badge ($0.86 \times 0.55 = 0.473$) — high D and high-velocity evolution. A prime target for a platform play.

### b. Top 3 by K (commodity leverage, $K = (1 - \nu) \cdot \varepsilon$)

1. Broadband / Connectivity — $0.88 \times 0.90 = 0.792$. Utility — do not build.
2. Cloud Compute — $0.86 \times 0.92 = 0.791$. Utility.
3. Video Conferencing — $0.74 \times 0.88 = 0.651$. Commodity.

Treat all three as consumption, not construction. Payment / Student Finance ($0.82 \times 0.80 = 0.656$) is also highly commoditised and should be outsourced to payment/student-loan utilities.

### c. Top 3 dependency risks ($R(a, b) = \nu(a) \cdot (1 - \varepsilon(b))$)

1. (Skills Development, AI Tutor) = $0.85 \times 0.82 = 0.697$. A highly visible learner proposition leaning on a Stage I–II technology. High value if it works; unstable if over-relied on.
2. (Verification of Learning, Credential Wallet) = $0.54 \times 0.70 = 0.378$. Employer-facing function depending on an immature standards stack (W3C Verifiable Credentials, OpenBadges 3.0).
3. (Skills Development, Peer / Community Study Groups) = $0.85 \times 0.60 = 0.510$. Visible proposition depending on an unstandardised social practice.

### d. Suggested gameplays (from Wardley's 61-play catalogue)

- Open Approaches (Acceleration play) on Credential Wallet and Micro-credential / Badge — open standards (W3C VC, OpenBadges) will speed commoditisation in the employer's favour.
- Standards Game (Ecosystem play) on Qualification Frameworks and Accreditation Standards — whoever defines the frame defines inclusion.
- Pig in a Poke (Disposal / De-accelerator play) for incumbent institutions facing commoditisation of the degree — recognise the commoditising wrapper and sell it to a utility provider before the margin collapses.
- Sensing Engines (Gameplay #24 / data play) on Labour Market Data — tie curriculum to live signals from employers.
- Designed to Fail (Acceleration play) on AI Tutor — run many small experiments; expect most to fail; harvest the successes.
- Co-operation (Ecosystem play) on Community Learning — municipal + civic partnerships to scale what is still artisanal.
- Harvesting (Acceleration play) on Foundation Models — observe which specialist LLM-for-education providers reach product-stage and acquire.
- Defensive regulation (Defensive play) for incumbent universities — expect it; plan around it; it is a known form of inertia.

### e. Doctrine observations (from the 40 principles)

- Phase I "Focus on user needs" — this map uses six anchors, which is unusual but right: treating only Students as users would hide the Employer–Employee–Regulator dynamics that actually determine power.
- Phase II "Know your users" — the Wider Community anchor is frequently missing from education maps; keeping it prevents "institution-centric" drift.
- "Remove bias and duplication" — Formal and Informal Curriculum overlap substantially in what learners actually experience; treating them as separate nodes is a choice to surface the power difference, not a mistake.
- Risk: Knowledge layer is thin. Pedagogy is the sole K-type node. For a deeper pass, add Learning Science, Credential Theory, and Epistemic Standards as K-nodes under Pedagogy and Accreditation Standards.

### f. Inertia call-outs (from the 17 forms)

- Degree Qualification — sunk capital (institutional brand) + political capital (state recognition) + human capital (teaching workforce trained against it).
- Physical Classroom Delivery — sunk capital (estate) + existing practice (pedagogy built around rooms).
- Teaching Workforce — human capital + second-sourcing risk (professional bodies gate entry).

These are the three inertia flags in the OWM draft. They are reasons the industrialised pieces move slowly even when their ε rating suggests they should be utility-like.

## 9. Reading guide

- Left half of the map (ε < 0.5): the politics of curriculum and who gets included. Differentiation zone. Civic / community-led plays live here.
- Right half (ε ≥ 0.5): industrialised delivery and credentialling. Commodity-leverage zone. Utility consumption, not construction.
- Middle band (ν ≈ 0.5): the standards/verification gate. The most politically contested zone on the map — this is where accreditation, qualification frameworks, and digital identity fight out which credentials count.
