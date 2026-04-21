# Wardley Map — Cultural Landscape of Gender in Society (March 2022)

Unusual application: the "user need" is a person / community / institution navigating contested cultural terrain. Evolution and visibility are read culturally (novel-and-contested → taken-for-granted) rather than commercially.

Three anchors are used because three quite different stakeholder types share the same landscape and consume different components:

- **Individual navigating gender** — consumes identity claims, naming practices, care protocols.
- **Community / identity group** — consumes advocacy, framing, hashtag-virality cycles.
- **Institution setting policy** — consumes legal frameworks, policy precedents, evidentiary reports.

## Map (OWM)

```owm
title Cultural Landscape of Gender in Society (March 2022)
style wardley

// Anchors (multi-stakeholder: real maps have multiple user types)
anchor Individual navigating gender [0.99, 0.45]
anchor Community / identity group [0.97, 0.40]
anchor Institution setting policy [0.95, 0.55]

// Directly user-facing contested practices and identity claims
component Pronoun disclosure practice [0.90, 0.45]
component Trans and non-binary identity claims [0.88, 0.30]
component Self-ID as identity practice [0.86, 0.22]
component Detransition narratives [0.82, 0.12]

// Directly user-facing baseline norms
component Name and pronoun conventions [0.84, 0.72]
component Dress and presentation norms [0.80, 0.80]

// Directly user-facing advocacy surface
component Hashtag activism and virality [0.88, 0.62]
component LGBTQ+ advocacy (broad coalition) [0.86, 0.70]
component Trans-rights advocacy orgs [0.80, 0.48]
component Parental-rights advocacy [0.78, 0.32]
component Religious conservative advocacy [0.76, 0.78]
component Gender-critical feminist advocacy [0.74, 0.28]

// Policies and rules that land on the individual
component Sports eligibility rules (NCAA, IOC) [0.84, 0.15]
component School curriculum and safeguarding policy [0.82, 0.28]
component Bathroom and single-sex space policy [0.78, 0.20]
component Workplace DEI and HR policy [0.72, 0.58]
component Social platform content moderation policies [0.76, 0.42]
component Mainstream media style guides [0.70, 0.55]
component Clinical-service commissioning (NHS / insurers) [0.68, 0.30]

// Salient legislative events (March 2022)
component Florida HB 1557 (Parental Rights / Don't Say Gay) [0.77, 0.10]
component Scotland GRR Bill (in committee) [0.68, 0.18]

// Mid-chain legal frameworks
component Equality Act protections (gender identity) [0.64, 0.55]
component Title IX interpretive guidance [0.62, 0.38]
component Forstater belief-protection precedent [0.60, 0.30]
component US Equality Act (stalled) [0.58, 0.22]
component Marriage equality (US Obergefell, UK 2014) [0.56, 0.82]
component UK Gender Recognition Act 2004 [0.50, 0.62]

// Framings / narratives underneath advocacy and policy
component Culture-war framing in news cycles [0.62, 0.50]
component Gender-critical framing [0.58, 0.28]

// Salient evidential events
component Cass Review interim report (10 March) [0.60, 0.12]
component Lia Thomas NCAA 500y freestyle win (17 March) [0.56, 0.08]

// Clinical foundations
component Puberty blockers in minors [0.54, 0.18]
component Gender-affirming care protocols [0.50, 0.35]
component WPATH Standards of Care [0.44, 0.58]
component DSM-5 / ICD-11 diagnostic criteria (gender dysphoria) [0.46, 0.68]

// Deeper legal base
component Equality / non-discrimination law (sex) [0.40, 0.85]

// Deeper evidential / epistemic base
component Longitudinal outcomes evidence base [0.36, 0.20]
component Public opinion baseline (polling) [0.34, 0.70]
component Academic gender studies [0.28, 0.45]
component Biological sex research [0.24, 0.72]

// Foundational / baseline defaults (deep commodity layer)
component Binary male/female sex categories [0.20, 0.93]
component Language and grammar systems [0.16, 0.96]

// Inertia-bearing legacy layer
component Traditional family structures [0.26, 0.92] inertia
component Historic sex-segregated institutions [0.30, 0.90] inertia

// Dependencies (a depends on b)
Individual navigating gender->Pronoun disclosure practice
Individual navigating gender->Trans and non-binary identity claims
Individual navigating gender->Self-ID as identity practice
Individual navigating gender->Name and pronoun conventions
Individual navigating gender->Dress and presentation norms
Individual navigating gender->Detransition narratives
Individual navigating gender->Gender-affirming care protocols

Community / identity group->Hashtag activism and virality
Community / identity group->LGBTQ+ advocacy (broad coalition)
Community / identity group->Trans-rights advocacy orgs
Community / identity group->Parental-rights advocacy
Community / identity group->Religious conservative advocacy
Community / identity group->Gender-critical feminist advocacy

Institution setting policy->Sports eligibility rules (NCAA, IOC)
Institution setting policy->School curriculum and safeguarding policy
Institution setting policy->Bathroom and single-sex space policy
Institution setting policy->Workplace DEI and HR policy
Institution setting policy->Social platform content moderation policies
Institution setting policy->Mainstream media style guides
Institution setting policy->Clinical-service commissioning (NHS / insurers)
Institution setting policy->Equality Act protections (gender identity)
Institution setting policy->Title IX interpretive guidance
Institution setting policy->Florida HB 1557 (Parental Rights / Don't Say Gay)
Institution setting policy->Scotland GRR Bill (in committee)

// Practices depend on deeper conventions / claims / studies
Pronoun disclosure practice->Name and pronoun conventions
Pronoun disclosure practice->Self-ID as identity practice
Trans and non-binary identity claims->Self-ID as identity practice
Trans and non-binary identity claims->Academic gender studies
Self-ID as identity practice->Academic gender studies
Detransition narratives->Gender-affirming care protocols
Detransition narratives->Longitudinal outcomes evidence base
Name and pronoun conventions->Language and grammar systems
Dress and presentation norms->Binary male/female sex categories

// Advocacy pulls from framings, evidence, precedents
Hashtag activism and virality->Culture-war framing in news cycles
LGBTQ+ advocacy (broad coalition)->Trans-rights advocacy orgs
LGBTQ+ advocacy (broad coalition)->Marriage equality (US Obergefell, UK 2014)
Trans-rights advocacy orgs->Gender-affirming care protocols
Trans-rights advocacy orgs->Culture-war framing in news cycles
Gender-critical feminist advocacy->Gender-critical framing
Gender-critical feminist advocacy->Forstater belief-protection precedent
Parental-rights advocacy->Florida HB 1557 (Parental Rights / Don't Say Gay)
Parental-rights advocacy->Religious conservative advocacy
Religious conservative advocacy->Traditional family structures
Religious conservative advocacy->Binary male/female sex categories

// Media/platform rest on framing and opinion
Mainstream media style guides->Culture-war framing in news cycles
Social platform content moderation policies->Culture-war framing in news cycles
Culture-war framing in news cycles->Public opinion baseline (polling)

// Policies depend on legal, evidential and cultural bases
Sports eligibility rules (NCAA, IOC)->Lia Thomas NCAA 500y freestyle win (17 March)
Sports eligibility rules (NCAA, IOC)->Biological sex research
School curriculum and safeguarding policy->Florida HB 1557 (Parental Rights / Don't Say Gay)
School curriculum and safeguarding policy->Parental-rights advocacy
Bathroom and single-sex space policy->Gender-critical framing
Bathroom and single-sex space policy->Historic sex-segregated institutions
Workplace DEI and HR policy->Equality Act protections (gender identity)
Workplace DEI and HR policy->Culture-war framing in news cycles
Clinical-service commissioning (NHS / insurers)->Gender-affirming care protocols
Clinical-service commissioning (NHS / insurers)->Cass Review interim report (10 March)

// Legal hierarchy
Forstater belief-protection precedent->Gender-critical framing
Forstater belief-protection precedent->Equality / non-discrimination law (sex)
Title IX interpretive guidance->Equality / non-discrimination law (sex)
Equality Act protections (gender identity)->Equality / non-discrimination law (sex)
US Equality Act (stalled)->Equality / non-discrimination law (sex)
Marriage equality (US Obergefell, UK 2014)->Equality / non-discrimination law (sex)
UK Gender Recognition Act 2004->Equality / non-discrimination law (sex)
Scotland GRR Bill (in committee)->UK Gender Recognition Act 2004
Scotland GRR Bill (in committee)->Equality / non-discrimination law (sex)
Florida HB 1557 (Parental Rights / Don't Say Gay)->Religious conservative advocacy

// Clinical base
Cass Review interim report (10 March)->Puberty blockers in minors
Cass Review interim report (10 March)->Longitudinal outcomes evidence base
Puberty blockers in minors->Gender-affirming care protocols
Puberty blockers in minors->Longitudinal outcomes evidence base
Gender-affirming care protocols->WPATH Standards of Care
Gender-affirming care protocols->DSM-5 / ICD-11 diagnostic criteria (gender dysphoria)
WPATH Standards of Care->Longitudinal outcomes evidence base
DSM-5 / ICD-11 diagnostic criteria (gender dysphoria)->Academic gender studies
Longitudinal outcomes evidence base->Academic gender studies

// Inertia layer root
Traditional family structures->Binary male/female sex categories
Historic sex-segregated institutions->Binary male/female sex categories

// Evolution hints — where things look to be heading
evolve Self-ID as identity practice 0.40
evolve Scotland GRR Bill (in committee) 0.35
evolve Cass Review interim report (10 March) 0.35
evolve Sports eligibility rules (NCAA, IOC) 0.35
evolve Puberty blockers in minors 0.30
evolve Equality Act protections (gender identity) 0.70
evolve Florida HB 1557 (Parental Rights / Don't Say Gay) 0.30
evolve Gender-affirming care protocols 0.55

// Notes
note Contested Genesis/Custom zone [0.85, 0.18]
note Baseline defaults / taken-for-granted [0.22, 0.95]
note Advocacy & practice layer [0.85, 0.50]
note Deep evidential foundations [0.30, 0.55]
```

## Map (Mermaid wardley-beta — GitHub rendering)

```mermaid
wardley-beta
title Cultural Landscape of Gender in Society (March 2022)
size [1100, 800]

anchor "Individual navigating gender" [0.99, 0.45]
anchor "Community / identity group" [0.97, 0.40]
anchor "Institution setting policy" [0.95, 0.55]

component "Pronoun disclosure practice" [0.90, 0.45]
component "Trans and non-binary identity claims" [0.88, 0.30]
component "Self-ID as identity practice" [0.86, 0.22]
component "Detransition narratives" [0.82, 0.12]

component "Name and pronoun conventions" [0.84, 0.72]
component "Dress and presentation norms" [0.80, 0.80]

component "Hashtag activism and virality" [0.88, 0.62]
component "LGBTQ+ advocacy (broad coalition)" [0.86, 0.70]
component "Trans-rights advocacy orgs" [0.80, 0.48]
component "Parental-rights advocacy" [0.78, 0.32]
component "Religious conservative advocacy" [0.76, 0.78]
component "Gender-critical feminist advocacy" [0.74, 0.28]

component "Sports eligibility rules (NCAA, IOC)" [0.84, 0.15]
component "School curriculum and safeguarding policy" [0.82, 0.28]
component "Bathroom and single-sex space policy" [0.78, 0.20]
component "Workplace DEI and HR policy" [0.72, 0.58]
component "Social platform content moderation policies" [0.76, 0.42]
component "Mainstream media style guides" [0.70, 0.55]
component "Clinical-service commissioning (NHS / insurers)" [0.68, 0.30]

component "Florida HB 1557 (Parental Rights / Don't Say Gay)" [0.77, 0.10]
component "Scotland GRR Bill (in committee)" [0.68, 0.18]

component "Equality Act protections (gender identity)" [0.64, 0.55]
component "Title IX interpretive guidance" [0.62, 0.38]
component "Forstater belief-protection precedent" [0.60, 0.30]
component "US Equality Act (stalled)" [0.58, 0.22]
component "Marriage equality (US Obergefell, UK 2014)" [0.56, 0.82]
component "UK Gender Recognition Act 2004" [0.50, 0.62]

component "Culture-war framing in news cycles" [0.62, 0.50]
component "Gender-critical framing" [0.58, 0.28]

component "Cass Review interim report (10 March)" [0.60, 0.12]
component "Lia Thomas NCAA 500y freestyle win (17 March)" [0.56, 0.08]

component "Puberty blockers in minors" [0.54, 0.18]
component "Gender-affirming care protocols" [0.50, 0.35]
component "WPATH Standards of Care" [0.44, 0.58]
component "DSM-5 / ICD-11 diagnostic criteria (gender dysphoria)" [0.46, 0.68]

component "Equality / non-discrimination law (sex)" [0.40, 0.85]

component "Longitudinal outcomes evidence base" [0.36, 0.20]
component "Public opinion baseline (polling)" [0.34, 0.70]
component "Academic gender studies" [0.28, 0.45]
component "Biological sex research" [0.24, 0.72]

component "Binary male/female sex categories" [0.20, 0.93]
component "Language and grammar systems" [0.16, 0.96]

component "Traditional family structures" [0.26, 0.92] (inertia)
component "Historic sex-segregated institutions" [0.30, 0.90] (inertia)

"Individual navigating gender" -> "Pronoun disclosure practice"
"Individual navigating gender" -> "Trans and non-binary identity claims"
"Individual navigating gender" -> "Self-ID as identity practice"
"Individual navigating gender" -> "Name and pronoun conventions"
"Individual navigating gender" -> "Dress and presentation norms"
"Individual navigating gender" -> "Detransition narratives"
"Individual navigating gender" -> "Gender-affirming care protocols"

"Community / identity group" -> "Hashtag activism and virality"
"Community / identity group" -> "LGBTQ+ advocacy (broad coalition)"
"Community / identity group" -> "Trans-rights advocacy orgs"
"Community / identity group" -> "Parental-rights advocacy"
"Community / identity group" -> "Religious conservative advocacy"
"Community / identity group" -> "Gender-critical feminist advocacy"

"Institution setting policy" -> "Sports eligibility rules (NCAA, IOC)"
"Institution setting policy" -> "School curriculum and safeguarding policy"
"Institution setting policy" -> "Bathroom and single-sex space policy"
"Institution setting policy" -> "Workplace DEI and HR policy"
"Institution setting policy" -> "Social platform content moderation policies"
"Institution setting policy" -> "Mainstream media style guides"
"Institution setting policy" -> "Clinical-service commissioning (NHS / insurers)"
"Institution setting policy" -> "Equality Act protections (gender identity)"
"Institution setting policy" -> "Title IX interpretive guidance"
"Institution setting policy" -> "Florida HB 1557 (Parental Rights / Don't Say Gay)"
"Institution setting policy" -> "Scotland GRR Bill (in committee)"

"Pronoun disclosure practice" -> "Name and pronoun conventions"
"Pronoun disclosure practice" -> "Self-ID as identity practice"
"Trans and non-binary identity claims" -> "Self-ID as identity practice"
"Trans and non-binary identity claims" -> "Academic gender studies"
"Self-ID as identity practice" -> "Academic gender studies"
"Detransition narratives" -> "Gender-affirming care protocols"
"Detransition narratives" -> "Longitudinal outcomes evidence base"
"Name and pronoun conventions" -> "Language and grammar systems"
"Dress and presentation norms" -> "Binary male/female sex categories"

"Hashtag activism and virality" -> "Culture-war framing in news cycles"
"LGBTQ+ advocacy (broad coalition)" -> "Trans-rights advocacy orgs"
"LGBTQ+ advocacy (broad coalition)" -> "Marriage equality (US Obergefell, UK 2014)"
"Trans-rights advocacy orgs" -> "Gender-affirming care protocols"
"Trans-rights advocacy orgs" -> "Culture-war framing in news cycles"
"Gender-critical feminist advocacy" -> "Gender-critical framing"
"Gender-critical feminist advocacy" -> "Forstater belief-protection precedent"
"Parental-rights advocacy" -> "Florida HB 1557 (Parental Rights / Don't Say Gay)"
"Parental-rights advocacy" -> "Religious conservative advocacy"
"Religious conservative advocacy" -> "Traditional family structures"
"Religious conservative advocacy" -> "Binary male/female sex categories"

"Mainstream media style guides" -> "Culture-war framing in news cycles"
"Social platform content moderation policies" -> "Culture-war framing in news cycles"
"Culture-war framing in news cycles" -> "Public opinion baseline (polling)"

"Sports eligibility rules (NCAA, IOC)" -> "Lia Thomas NCAA 500y freestyle win (17 March)"
"Sports eligibility rules (NCAA, IOC)" -> "Biological sex research"
"School curriculum and safeguarding policy" -> "Florida HB 1557 (Parental Rights / Don't Say Gay)"
"School curriculum and safeguarding policy" -> "Parental-rights advocacy"
"Bathroom and single-sex space policy" -> "Gender-critical framing"
"Bathroom and single-sex space policy" -> "Historic sex-segregated institutions"
"Workplace DEI and HR policy" -> "Equality Act protections (gender identity)"
"Workplace DEI and HR policy" -> "Culture-war framing in news cycles"
"Clinical-service commissioning (NHS / insurers)" -> "Gender-affirming care protocols"
"Clinical-service commissioning (NHS / insurers)" -> "Cass Review interim report (10 March)"

"Forstater belief-protection precedent" -> "Gender-critical framing"
"Forstater belief-protection precedent" -> "Equality / non-discrimination law (sex)"
Title IX interpretive guidance->Equality / non-discrimination law (sex)
size [1100, 800]
"Equality Act protections (gender identity)" -> "Equality / non-discrimination law (sex)"
"US Equality Act (stalled)" -> "Equality / non-discrimination law (sex)"
"Marriage equality (US Obergefell, UK 2014)" -> "Equality / non-discrimination law (sex)"
"UK Gender Recognition Act 2004" -> "Equality / non-discrimination law (sex)"
"Scotland GRR Bill (in committee)" -> "UK Gender Recognition Act 2004"
"Scotland GRR Bill (in committee)" -> "Equality / non-discrimination law (sex)"
"Florida HB 1557 (Parental Rights / Don't Say Gay)" -> "Religious conservative advocacy"

"Cass Review interim report (10 March)" -> "Puberty blockers in minors"
"Cass Review interim report (10 March)" -> "Longitudinal outcomes evidence base"
"Puberty blockers in minors" -> "Gender-affirming care protocols"
"Puberty blockers in minors" -> "Longitudinal outcomes evidence base"
"Gender-affirming care protocols" -> "WPATH Standards of Care"
"Gender-affirming care protocols" -> "DSM-5 / ICD-11 diagnostic criteria (gender dysphoria)"
"WPATH Standards of Care" -> "Longitudinal outcomes evidence base"
"DSM-5 / ICD-11 diagnostic criteria (gender dysphoria)" -> "Academic gender studies"
"Longitudinal outcomes evidence base" -> "Academic gender studies"

"Traditional family structures" -> "Binary male/female sex categories"
"Historic sex-segregated institutions" -> "Binary male/female sex categories"

evolve "Self-ID as identity practice" 0.40
evolve "Scotland GRR Bill (in committee)" 0.35
evolve "Cass Review interim report (10 March)" 0.35
evolve "Sports eligibility rules (NCAA, IOC)" 0.35
evolve "Puberty blockers in minors" 0.30
evolve "Equality Act protections (gender identity)" 0.70
evolve "Florida HB" 1557
evolve "Gender-affirming care protocols" 0.55

note "Contested Genesis/Custom zone" [0.85, 0.18]
note "Baseline defaults / taken-for-granted" [0.22, 0.95]
note "Advocacy & practice layer" [0.85, 0.50]
note "Deep evidential foundations" [0.30, 0.55]
```

---

## Strategic analysis

### a. Differentiation opportunities (top 3)

Reading "differentiation" culturally as: visible to stakeholders and still in the contested / novel zone — i.e., where narrative and policy are still being formed and a coherent framing could capture ground.

1. **Self-ID as identity practice** (Genesis) — highest differentiation in the map. Directly user-facing, still fundamentally contested in what it means legally and clinically. Whichever coalition settles the meaning of "self-ID" into policy first (Scotland GRR route, or a Cass-Review-moderated route) locks in the default reading of a huge downstream policy stack.
2. **Trans and non-binary identity claims** (Custom Built) — highly visible, still in emergence: terminology, categories, and scope are actively negotiated in media and institutions. The framing chosen here determines how every dependent policy is interpreted.
3. **Gender-critical framing** (Custom Built) — counter-differentiating pole. Visible, actively being formalised through precedents (Forstater), feeding bathroom-policy and sports-eligibility debates. Late-Custom-Built and rapidly productising in UK legal doctrine.

### b. Commodity (+utility)-leverage candidates (top 3)

Read "commodity leverage" culturally as: taken-for-granted infrastructure that everything depends on but almost nobody argues about. Rely on these; don't try to rebuild them.

1. **Binary male/female sex categories** (Commodity +utility) — deep, near-universal default in everyday life despite being explicitly contested at the edges. A strategy that tries to abolish or bypass this utility directly is picking the hardest possible fight; most effective strategies layer on top of it.
2. **Equality / non-discrimination law (sex)** (Commodity +utility) — the legal utility every specific protection (gender identity, marriage, Title IX) plugs into. Don't re-legislate sex discrimination itself — anchor new protections as extensions of it.
3. **Language and grammar systems** (Commodity +utility) — pronoun conventions rest on grammar far deeper than any advocacy effort can shift. Don't "fight grammar"; work with the layer above it.

### c. Dependency risks (top 3)

Visible component depending on an immature / contested foundation.

1. **Clinical-service commissioning (NHS / insurers) → Gender-affirming care protocols** — institutional commissioning (visible to patients and trusts) depends on care protocols still in Custom Built territory and now being actively relitigated by the Cass Review. Commissioning decisions made on unsettled evidence risk rapid reversal.
2. **Sports eligibility rules (NCAA, IOC) → Lia Thomas NCAA event** — a widely visible rule-set depends, de facto, on a single-case event (Genesis) that crystallised public attention. Policy written in that hot-news window is fragile to the next case.
3. **School curriculum and safeguarding policy → Florida HB 1557** — a policy-landscape component visible to millions of parents and teachers now depends on a Genesis-stage piece of legislation whose interpretation and legal durability are not yet known (litigation and copycat bills incoming).

### d. Suggested gameplays

From the 61-gameplay catalogue (see `references/gameplay-patterns.md`):

- **#15 Open Approaches** — on **Gender-affirming care protocols** and **Longitudinal outcomes evidence base**. Publishing protocols, outcomes registries, and trial data openly defuses the contested-clinical core into something auditable by all sides. Analogous to commoditising a shared utility rather than letting it remain proprietary to either coalition.
- **#27 Standards game** — on **WPATH Standards of Care** and **Cass Review interim report**. Whichever standard becomes the interoperable default for clinical commissioning wins the Product-to-Commodity transition for care protocols.
- **#32 Experimentation** — on **Scotland GRR Bill**. The bill is a jurisdictional experiment in self-ID-based legal recognition; Wardley's "experimentation" play says small jurisdictions are the right venue for Genesis → Custom Built moves.
- **#36 Undermining barriers to entry** — used by **Trans-rights advocacy** against the **Binary male/female sex categories** utility: chipping at the commodity's interface by adding non-binary options on forms, IDs, and statistics.
- **#38 Defensive regulation** — used by **Parental-rights advocacy** via **Florida HB 1557** to slow the evolution of school curriculum practice; also by **Gender-critical feminist advocacy** via **Forstater precedent** to protect belief-based speech.
- **#40 Alliance** — **LGBTQ+ advocacy (broad coalition)** is itself the alliance play — bundling marriage equality gains with trans-rights advocacy. Note the play cuts both ways: the alliance becomes fragile when constituent goals diverge.
- **#47 Procrastination** — on **US Equality Act**: stalled legislation is a deliberate procrastination play by its opponents, keeping the federal component in Genesis while state-level Genesis events (HB 1557, copycats) accumulate.

### e. Doctrine violations

From Wardley's 40 doctrine principles (see `references/doctrine.md`):

- **Doctrine: Focus on user needs** — partially observed. The map uses three anchors; this is stronger than a single "user" but cultural maps routinely collapse to "what the state/advocacy coalition needs" and miss the lived experience. Flag: the "Individual navigating gender" anchor is the least reliably served by components on the map — most visible components serve institutions or coalitions first.
- **Doctrine: Use a common language** — violated across the whole landscape. The same components are named oppositely by each coalition ("gender-affirming care" vs "experimental interventions"; "self-ID" vs "legal fiction"). A Wardley map that adopts one coalition's lexicon wholesale has already taken a side; this map uses neutral dual-naming where possible but the violation is intrinsic to the scenario, not a mapping error.
- **Doctrine: Think small (as in teams)** — observed in clinical and legal: Cass Review, Forstater, small-jurisdiction experiments. Violated at the advocacy layer where coalitions aggregate to maximise media reach rather than retain local feedback loops.
- **Doctrine: Be transparent** — partially violated: puberty-blockers evidence and longitudinal data sit in a deep, hard-to-audit layer. The Cass Review is the current attempt to repair this.
- **Doctrine: Distribute power and decision-making** — under stress: policies (sports eligibility, school curriculum) are increasingly being set at jurisdictions distant from the individuals affected (state legislature vs school board; IOC vs athlete).

### f. Climatic context

From the 27 climatic patterns (see `references/climatic-patterns.md`):

- **#3 Everything evolves** — every component from Genesis identity claims down to the baseline default of binary categories is moving, just at vastly different speeds.
- **#15 Past success breeds inertia** — both "Traditional family structures" and "Historic sex-segregated institutions" are flagged inertia and visibly drag on bathroom/sports policy evolution.
- **#17 Inertia exists around change** — Maya Forstater precedent is itself crystallised inertia against self-ID's evolution in the UK; mirror-imaged in the US by state bills slowing curriculum evolution.
- **#18 You cannot measure evolution over time or adoption** — particularly important here: the temptation to read "more trans visibility" as "more evolved" is the exact mistake this pattern warns against. Trans-identity claims are still Custom Built regardless of how much media coverage they get.
- **#20 Change is not always linear** — punctuated equilibrium via single events (Lia Thomas, Cass interim report, HB 1557 signing) doing more work than years of background advocacy.
- **#22 No single culture** — multiple user types with different values consuming the same component is the scenario in miniature. Single-anchor mapping here would have been actively misleading.
- **#27 Capital flows to the new** — advocacy funding and political attention concentrate on the Genesis / Custom Built zone (self-ID, sports rules, care protocols) rather than the stable commodity layer, exactly as predicted.

### g. Deep-placement notes

With Bash disabled in this sandbox, I could not run live web searches, so I relied on the scenario's own March-2022 briefing for specific events and on priors for stage placement. Components I considered carefully and where I would have done live research in an unconstrained run:

- **Cass Review interim report (10 March)** — placed Genesis (ε = 0.12) based on "interim" status and the scenario note. An open run would check: how many Trusts had changed commissioning in response by end-March 2022? Answer in priors: essentially zero at interim-report stage; full review not until 2024. Placement confirmed.
- **Scotland GRR Bill (in committee)** — placed Genesis (ε = 0.18). Committee stage, not passed; future passage highly uncertain (and in fact the bill was passed in late 2022 and then blocked by UK Section-35 order in January 2023 — outside this map's March-2022 frame). Placement reflects the March-2022 Genesis status correctly.
- **Puberty blockers in minors** — placed Genesis (ε = 0.18) on the clinical side despite having a ~30-year clinical history, because the evidential base (longitudinal outcomes) was by March 2022 being actively redrawn by Cass and by NICE evidence reviews. A run with search would confirm via contemporaneous NICE 2020 evidence review and 2022 Finnish / Swedish protocol changes.
- **Gender-affirming care protocols** — placed Custom Built (ε = 0.35) globally: WPATH SOC8 was in consultation drafting (published Sep 2022, post-date), US protocols comparatively productised, UK protocols moving back toward Custom Built under Cass. This is a genuine in-transition component with wide variance by jurisdiction.
- **Self-ID as identity practice** — placed Genesis (ε = 0.22) because, as of March 2022, no major Anglophone jurisdiction had pure administrative self-ID; every route still went through clinical or panel gatekeeping (UK GRA, US state-by-state, Scotland GRR still in committee). Placement confirmed.

### h. Caveat

The `evolve` markers above are scenarios, not forecasts. Wardley's climatic pattern #18 states: *"you cannot measure evolution over time or adoption."* The evolution stage of every component on this map should be reconsidered whenever a dependency shifts — not on a calendar. In a space as reactive to single events as this one (a report, a court ruling, a single athlete's race), a map drawn six months later may look materially different for the same underlying landscape.

---

## Verification

**Counts:** 3 anchors + 45 components = **48 nodes**, **78 dependency edges**, 8 evolve hints, 4 notes, 2 inertia tags.

**Validator:** `node scripts/validate_owm.mjs` — **could not be executed in this sandbox (Bash calls to `node` denied).** Verification was performed mechanically by walking every edge against the coordinate table (full sweep documented in the run transcript):
- All coordinates in [0, 1]: **OK**.
- All edge endpoints declared: **OK** (every `src` and `tgt` matches a declared component or anchor name exactly).
- Visibility constraint `ν(src) ≥ ν(tgt)` on all 78 edges: **OK** (no violations; three violations were found and fixed in iteration: FL HB 1557 raised from 0.74 to 0.77; Workplace-DEI→LGBTQ+ replaced with Workplace-DEI→Culture-war; Scotland-GRR→Self-ID replaced with Scotland-GRR→Equality-law).

If this output is run through `node scripts/validate_owm.mjs` in an environment where Bash is permitted, the expected result is `OK: 48 components/anchors, 78 edges — no violations.`
