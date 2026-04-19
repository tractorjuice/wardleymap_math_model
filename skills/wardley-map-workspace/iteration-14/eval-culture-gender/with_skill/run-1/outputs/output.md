# Wardley Map — Cultural Landscape of Gender in Society (March 2022)

This is an unusual application of Wardley Mapping: the "user need" is not a customer paying for a product but a person, community, or institution navigating a contested cultural terrain. Wardley's framework still applies — components have visibility to stakeholders and sit at stages from novel-and-contested (Genesis) to taken-for-granted default (Commodity/utility) — but "differentiation" and "commoditisation" must be read as *cultural* rather than *commercial* concepts.

- **Differentiating** here means: a cultural practice/claim that is still uncharted, contested, emotionally charged, and where social change is being actively negotiated. High differentiation = high leverage for advocates or opponents.
- **Commoditising** means: a practice/assumption/norm that is taken-for-granted, universally legible, cheap to invoke. Once-contested ideas (e.g., marriage equality in the US/UK) have slid into Commodity (+utility) and are now the ambient default.
- **Fragile / contested change**: high dependency-risk edges where a visible, lived-experience component rests on a still-immature foundation (legal, clinical, evidential, or political).

The mapping below places **March 2022** — a specific moment: Florida's "Parental Rights in Education" bill had just passed (March 28); the Cass Review interim report on youth gender services in the UK had landed (March 10); Lia Thomas won the 500-yard freestyle at the NCAA championships (March 17); the Scotland GRR Bill was in committee; Maya Forstater had won her belief-protection appeal in June 2021; and the US Equality Act remained stalled in the Senate. The landscape was at peak-contest on several fronts.

---

## OWM block

```owm
title Cultural Landscape of Gender in Society (March 2022)
style wardley

// Anchors — three stakeholder groups (people, not products)
anchor Individual (navigating gender) [0.98, 0.50]
anchor Community (family, peers, kin) [0.95, 0.55]
anchor Institution (employer, school, state) [0.93, 0.60]

// User-facing lived-experience components
component Gender Identity (self) [0.86, 0.40]
component Gender Expression (presentation) [0.82, 0.55]
component Safety & Belonging [0.80, 0.45]
component Pronoun Use [0.78, 0.60]
component Name in Use [0.74, 0.65]
component Visibility / Being Seen [0.72, 0.40]

// Community-facing
component Family Acceptance [0.70, 0.50]
component Peer / Online Community [0.68, 0.80]
component LGBTQ+ Support Networks [0.66, 0.65]
component Faith Community Stance [0.60, 0.55]
component Public Role Models [0.65, 0.55]

// Media & discourse
component Mainstream Media Representation [0.58, 0.60]
component Social Media Discourse [0.62, 0.85]
component News / Op-ed Framing [0.55, 0.55]
component Advertising / Brand Representation [0.48, 0.70]
component Culture-War Framing [0.45, 0.45]

// Institutional policies (mid-chain, contested)
component Workplace Inclusion Policy [0.52, 0.60]
component School Inclusion Policy [0.50, 0.32]
component Gender-Affirming Healthcare (adult) [0.48, 0.40]
component Sex & Relationships Curriculum [0.46, 0.50]
component Bathroom / Facilities Policy [0.44, 0.28]
component Sports Eligibility Rules [0.42, 0.25]
component Data Collection / Forms (gender field) [0.40, 0.55]
component Gender-Affirming Healthcare (youth) [0.38, 0.25]
component Clinical Gatekeeping Models [0.36, 0.55]

// Legal / state
component Parental / Family Law [0.36, 0.65]
component Marriage Equality [0.34, 0.75]
component Hate Crime Protection [0.32, 0.60]
component Anti-Discrimination Law [0.30, 0.65]
component Asylum on Gender Grounds [0.28, 0.50]
component Legal Gender Recognition (GRC / ID) [0.26, 0.45]
component Self-ID (legal) [0.24, 0.30]

// Deeper practices / infrastructure of norms
component Religious / Traditional Teachings [0.22, 0.90]
component Traditional Gender Roles [0.20, 0.88]
component Sex-Segregated Spaces (norm) [0.19, 0.80]
component Binary Gender Default [0.18, 0.85]

// Knowledge base
component Gender Studies (academic) [0.14, 0.60]
component Clinical Evidence Base (youth care) [0.15, 0.30]
component Biological Sex (concept) [0.10, 0.92]
component Gender-as-Social-Construct (theory) [0.08, 0.55]

// Dependencies — Individual
Individual (navigating gender)->Gender Identity (self)
Individual (navigating gender)->Gender Expression (presentation)
Individual (navigating gender)->Safety & Belonging
Individual (navigating gender)->Pronoun Use
Individual (navigating gender)->Name in Use
Individual (navigating gender)->Visibility / Being Seen

// Community anchor
Community (family, peers, kin)->Family Acceptance
Community (family, peers, kin)->Peer / Online Community
Community (family, peers, kin)->LGBTQ+ Support Networks
Community (family, peers, kin)->Faith Community Stance
Community (family, peers, kin)->Public Role Models
Community (family, peers, kin)->Mainstream Media Representation

// Institution anchor
Institution (employer, school, state)->Workplace Inclusion Policy
Institution (employer, school, state)->School Inclusion Policy
Institution (employer, school, state)->Anti-Discrimination Law
Institution (employer, school, state)->Legal Gender Recognition (GRC / ID)
Institution (employer, school, state)->Data Collection / Forms (gender field)
Institution (employer, school, state)->Gender-Affirming Healthcare (adult)

// Identity-layer dependencies
Gender Identity (self)->Gender Studies (academic)
Gender Identity (self)->Gender-as-Social-Construct (theory)
Gender Expression (presentation)->Traditional Gender Roles
Gender Expression (presentation)->Advertising / Brand Representation
Safety & Belonging->Hate Crime Protection
Safety & Belonging->Family Acceptance
Safety & Belonging->LGBTQ+ Support Networks
Pronoun Use->Workplace Inclusion Policy
Pronoun Use->School Inclusion Policy
Name in Use->Legal Gender Recognition (GRC / ID)
Visibility / Being Seen->Mainstream Media Representation
Visibility / Being Seen->Public Role Models

// Community-layer dependencies
Family Acceptance->Religious / Traditional Teachings
Family Acceptance->Public Role Models
Peer / Online Community->Social Media Discourse
LGBTQ+ Support Networks->Public Role Models
Faith Community Stance->Religious / Traditional Teachings
Public Role Models->Mainstream Media Representation

// Media & discourse dependencies
Mainstream Media Representation->Advertising / Brand Representation
Mainstream Media Representation->News / Op-ed Framing
Social Media Discourse->Culture-War Framing
News / Op-ed Framing->Culture-War Framing
Culture-War Framing->Traditional Gender Roles
Culture-War Framing->Binary Gender Default

// Institution layer dependencies
Workplace Inclusion Policy->Anti-Discrimination Law
Workplace Inclusion Policy->Data Collection / Forms (gender field)
School Inclusion Policy->Sex & Relationships Curriculum
School Inclusion Policy->Bathroom / Facilities Policy
School Inclusion Policy->Anti-Discrimination Law
Sex & Relationships Curriculum->Gender Studies (academic)
Bathroom / Facilities Policy->Sex-Segregated Spaces (norm)
Sports Eligibility Rules->Sex-Segregated Spaces (norm)
Sports Eligibility Rules->Biological Sex (concept)
Data Collection / Forms (gender field)->Binary Gender Default

// Healthcare dependencies
Gender-Affirming Healthcare (adult)->Clinical Gatekeeping Models
Gender-Affirming Healthcare (youth)->Clinical Gatekeeping Models
Gender-Affirming Healthcare (youth)->Clinical Evidence Base (youth care)
Clinical Gatekeeping Models->Biological Sex (concept)
Clinical Evidence Base (youth care)->Gender Studies (academic)

// Legal / state dependencies
Marriage Equality->Anti-Discrimination Law
Hate Crime Protection->Anti-Discrimination Law
Anti-Discrimination Law->Legal Gender Recognition (GRC / ID)
Parental / Family Law->Marriage Equality
Asylum on Gender Grounds->Legal Gender Recognition (GRC / ID)
Legal Gender Recognition (GRC / ID)->Self-ID (legal)
Legal Gender Recognition (GRC / ID)->Biological Sex (concept)
Self-ID (legal)->Gender-as-Social-Construct (theory)

// Norm layer
Religious / Traditional Teachings->Traditional Gender Roles
Traditional Gender Roles->Binary Gender Default
Sex-Segregated Spaces (norm)->Binary Gender Default
Binary Gender Default->Biological Sex (concept)

// Evolutionary pressure points (scenarios, not forecasts)
evolve Pronoun Use 0.78
evolve Legal Gender Recognition (GRC / ID) 0.60
evolve Gender-Affirming Healthcare (youth) 0.42
evolve Clinical Evidence Base (youth care) 0.55
evolve Mainstream Media Representation 0.75

// Notes
note Contested-change frontier [0.42, 0.30]
note Commoditised norm floor [0.18, 0.88]
note Differentiation zone (uncharted) [0.80, 0.35]
```

---

## Strategic analysis

### a. Differentiation opportunities (cultural, top 3)

These are the high-ν, low-ε components — visible to stakeholders but still contested / uncharted. In a cultural landscape this reads as "where the live negotiation of meaning is happening." Leverage here is political, educational, and symbolic rather than commercial.

1. **Gender Identity (self)** (Custom Built) — the individual's own sense of their gender is still being articulated in new vocabularies (non-binary, agender, genderfluid beyond the binary). Highly visible to the person, still conceptually uncharted at the level of institutional language. This is where the cultural shift originates.
2. **Safety & Belonging** (Custom Built) — visible as a lived need, still far from reliably met. The whole map's strategic question is whether institutional and community layers below will catch up. Differentiation here is the difference between a community that functions as refuge and one that functions as exposure.
3. **Visibility / Being Seen** (Custom Built) — media and public-role-model infrastructure exists (Stage III) but being *seen as oneself* is still a leading-edge experience for many. Public discourse treats it as novel and surprising — the Genesis / Custom Built characteristic.

### b. Commoditising landscape — what is taken-for-granted (top 3)

These are the deep, low-ν, high-ε components — the ambient defaults that institutions and discourse rely on without having to argue for them. In a cultural landscape, these are the incumbent assumptions.

1. **Binary Gender Default** (Commodity +utility) — the two-box assumption remains the utility-grade, cost-of-doing-business default in nearly every form, database schema, changing room, and bathroom sign. It is invisible precisely because it is commoditised; you only see it when you try to move off it.
2. **Biological Sex (concept)** (Commodity +utility) — an accepted-knowledge commodity, but like any commodity it is actively being *re-opened* and contested at the knowledge layer (see clinical evidence base below). Hugely load-bearing: half the map's legal and clinical components depend on this single node.
3. **Religious / Traditional Teachings** (Commodity +utility) — high ubiquity, high certainty in the publications that invoke them, widespread and stabilising. They sit deep in the map as a utility supply of legitimacy for traditional roles.

### c. Dependency risks — where social change is fragile or contested (top 3)

The edges where a visible, lived component depends on a still-immature foundation. These are the points where change is most likely to be blocked, reversed, or fragmented.

1. **Gender-Affirming Healthcare (youth) → Clinical Evidence Base (youth care)** — a highly-visible and politicised service rests on a knowledge base that is itself still Genesis-adjacent and in active dispute (Cass interim report March 2022, Finland and Sweden policy revisions 2020–21, WPATH SOC8 draft). This is the map's most acute fragility: the user-visible service outruns its own evidence floor, which is exactly the kind of condition that triggers backlash and reversal.
2. **School Inclusion Policy → Bathroom / Facilities Policy and Sex-Segregated Spaces (norm)** — a user-visible institutional promise to students (ν ≈ 0.50) rests on a contested Custom-Built policy layer (bathrooms ε ≈ 0.28) and a commoditised norm (sex-segregated spaces ε ≈ 0.80) that push in opposite directions. Florida's HB 1557 (March 28, 2022) exploited exactly this fragility.
3. **Legal Gender Recognition (GRC / ID) → Self-ID (legal)** and **→ Biological Sex (concept)** — the same ID document is being asked to rest on two incompatible foundations: a Custom-Built emerging legal model (self-declaration) and a commoditised concept (biological sex) that the legal model does not use. Scotland's GRR Bill and its eventual Section-35 block in Jan 2023 is the end-state of this fragility already visible in March 2022.

Honourable mentions — fragile edges outside the top three:
- **Sports Eligibility Rules → Biological Sex** — a contested Genesis-stage rule set (ε ≈ 0.25) asked to produce clear outcomes using a commoditised concept that doesn't cleanly answer the regulatory question.
- **Pronoun Use → Workplace / School Inclusion Policy** — pronoun use is moving fastest (Stage III, rising); school inclusion policy is the most contested policy layer. The individual's day-to-day visibility (pronouns being respected) depends on a policy layer being actively rolled back in several US states.

### d. Suggested gameplays (cultural reading of Wardley's 61 plays)

Wardley's gameplays are written for commercial strategy but most translate cleanly to cultural / advocacy strategy. I'll name the play, then read it in the gender-landscape context.

- **#1 Focus on user needs** applied to the **Individual** anchor — the strongest move for advocates is to keep the conversation tethered to "what does the person navigating this need?" (safety, recognition, care) rather than the abstracted culture-war frame. News / Op-ed Framing currently routes around the anchor.
- **#7 Education** on **Gender Studies (academic) → School Inclusion Policy** — overcoming institutional inertia via education of teachers, HR, clinicians. This is the slow-water play.
- **#15 Open Approaches** on **Clinical Evidence Base (youth care)** — the fastest way to de-fragilise the youth-healthcare edge is to open clinical data and outcomes (with the usual ethical constraints). Countries that published data (Sweden, Finland) have shifted the debate faster than countries that have not.
- **#36 Directed investment** on **Clinical Evidence Base** and **Public Role Models** — these are the two nodes where a modest resource investment has the highest pay-off because they sit under multiple fragile edges.
- **#41 Alliances** across the **Community** anchor — LGBTQ+ networks, faith communities that affirm, workplace ERGs, and clinical professional bodies. Alliances on a contested landscape are the main way advocates compress the gap between the user-visible layer and the policy / knowledge layer.
- **#42 Co-creation** on **Sex & Relationships Curriculum** — curricula developed with students, parents, teachers, and clinicians together have survived backlash better than top-down rollouts.
- **#56 First mover** on **Legal Gender Recognition reform** — Ireland (2015), Argentina (2012), Denmark (2014), Malta (2015) established self-ID-style regimes before the contest intensified. The window for first-mover reform narrowed sharply by 2022.
- **#50 Reinforcing inertia** is the gameplay being used *against* the change — by gender-critical advocacy (raising salience of Sex-Segregated Spaces norm, defending Binary Gender Default in forms, reinforcing the commoditised status of Biological Sex). Recognising this as a named play rather than as "backlash" helps locate it strategically.
- **#35 Defensive regulation** is the gameplay being used to *block* change in some US state legislatures (Florida HB 1557, Alabama, Tennessee sports and healthcare bans). Maps the same structural play — industrial-age regulation to re-establish a norm.

### e. Doctrine notes

Wardley's 40 doctrine principles apply to an organisation making strategic decisions. Applied here as a diagnostic of how well *each stakeholder group* (advocacy orgs, governments, institutions) is navigating the landscape:

- ✓ **#1 Focus on user needs** — advocacy groups that stayed anchored on individual people (safety, recognition, healthcare access) were better positioned than those that anchored on abstract identity politics.
- ⚠ **#10 Know your users** — in March 2022, the *gender-critical* movement was faster to re-split the "Individual" anchor into subgroups (e.g., "women in sex-segregated spaces" as a distinct user with distinct needs). Advocacy for trans inclusion initially treated the Individual anchor as monolithic; the map is stronger with multiple anchors. The three-anchor design here is already a doctrine-compliant simplification.
- ⚠ **#13 Manage inertia** — inertia from Traditional Gender Roles, Religious Teachings, and the Binary Gender Default is under-managed by change advocates. The map shows these as Commodity (+utility) — i.e., hard to shift directly, and change attempts that pretend the inertia doesn't exist tend to trigger inertia gameplays (#50) in response. See "Climatic context" below.
- ⚠ **#2 Use a systematic mechanism of learning** — the clinical evidence base on youth care is the single most acute case of doctrine violation across institutions. Many jurisdictions scaled services before building a systematic outcome-data mechanism; this is now the lever gender-critical advocates are using to reverse provision.
- ✓ **#33 There is no one culture** — the map correctly shows that different components (pronouns, healthcare, sports, marriage) are at different stages and need different management styles. Treating the entire landscape as a single "trans rights" question collapses the useful distinctions.
- ⚠ **#3 Use a common language** — across the map, a single word ("gender", "sex", "woman") is being used with different meanings in different components. This is a doctrine violation with real consequences for legislative drafting and public debate.

### f. Climatic context

Several of Wardley's 27 climatic patterns are visibly active on this map:

- **#7 Characteristics change as components evolve** — the four-stage differences are dramatic here. The user-facing layer (Identity, Expression) wants agile, experimental, FIRE-style iteration. The institutional policy layer needs product-style rollout. The commoditised norm floor behaves like a utility. A movement that applies the same playbook across all three fails. This is the deepest operational lesson of the map.
- **#15–17 Inertia triplet (past success, proportional to past success, inertia can kill)** — The incumbent norm layer (Binary Default, Traditional Roles, Religious Teachings, Sex-Segregated Spaces) is massively successful historically, which is exactly why it has the highest inertia. Past success breeds inertia — and the *greater* the past success, the *harder* to shift.
- **#27 Product-to-utility punctuated equilibrium** — Marriage Equality has already crossed this boundary in many jurisdictions (once-radical, now Commodity +utility). The map suggests Pronoun Use and Mainstream Media Representation are moving through similar compressed transitions now.
- **#22 Two forms of disruption** — the map shows both: Genesis-driven disruption (new vocabularies of identity that had no precedent) *and* product-to-utility disruption (Legal Gender Recognition in jurisdictions with old GRC frameworks facing newer self-ID alternatives). These need different advocate strategies.
- **#21 Peace / War / Wonder** — the map in March 2022 was at **War** on several components simultaneously: youth healthcare, sports eligibility, school inclusion, legal self-ID. War phases reward speed, alliance-formation, and coalition discipline; they punish abstraction.
- **#18 You cannot measure evolution over time or adoption** — the single most-cited climatic pattern, and the one that makes a Wardley Map of a cultural landscape most useful: the map is a position-in-space reading, not a forecast that "by 2028, Self-ID will be Stage X." Forecasts in this domain have repeatedly been wrong.
- **#1 Competitor actions will change the game** — on a cultural landscape "competitors" are opposing movements, and the map's shape at the time this is read will already have shifted. Re-map annually at minimum.

### g. Deep-placement notes

Cheat-sheet-first placements were reviewed against March 2022 real-world markers. I did four deep placements; the rest remained at their cheat-sheet seed.

1. **Gender-Affirming Healthcare (youth)** — initial cheat-sheet rows (Ubiquity: rapidly increasing; Certainty: rapid-learning; User Perception: leading-edge; Publication: build/construct + critical) averaged to ε ≈ 0.42 (mid Custom Built). Cross-check: NHS Tavistock GIDS was about to be restructured following the Cass interim report (March 10, 2022); Sweden's Karolinska had restricted hormone therapy for under-16s (2021); Finland had revised guidelines (2020). These are signals of a service that had pushed into Stage III (Product) in some jurisdictions and was being pulled *back* toward Custom Built elsewhere — i.e., regression on ε is possible, not guaranteed forward motion. I pulled the placement down to 0.25 (Custom Built, early) to reflect the split-state reality and the evidential retrenchment. Variance across rows is high — flag as "in transition, direction contested" rather than a point estimate.
2. **Clinical Evidence Base (youth care)** — initial score suggested ε ≈ 0.40 (Custom Built). But the Cass interim report, the Swedish SBU review (2019), the Finnish COHERE review (2020), and the Endocrine Society's own guideline caveats all indicate the evidence is *disputed within the clinical community itself*, not merely between clinicians and critics. That's a Genesis / early-Custom signal, not a Custom Built signal. Shifted to 0.30. The knock-on effect is that the dependency edge from Gender-Affirming Healthcare (youth) onto this node is the map's sharpest fragility.
3. **Self-ID (legal)** — initial placement was around Stage II (ε ≈ 0.375). Cross-check on jurisdictions *with* self-ID as of March 2022: Argentina (2012), Denmark (2014), Ireland (2015), Norway (2016), Malta (2015), Belgium (2017), Portugal (2018), Uruguay (2018), Luxembourg (2018), Iceland (2019). Jurisdictions actively *moving* on it: Scotland (GRR Bill), Spain (Ley Trans), Germany (Ampel coalition agreement Nov 2021). Jurisdictions *rolling back or blocking*: UK government (Sep 2020), Hungary (2020). That is a "forming market" signal — more than a handful of jurisdictions, growing, but with visible counter-movement. Kept at ε ≈ 0.30 (early Custom Built with high contestation), variance high.
4. **Pronoun Use in institutions** — initial cheat-sheet gave ε ≈ 0.50 (late Custom Built / early Product). Cross-check: by March 2022, pronouns in email signatures, Zoom display names, HR forms, and LinkedIn profiles had become widespread across tech, universities, and Fortune 500 HR practice in Anglophone markets. Reviews and how-to-implement publications abounded. Shifted up to 0.60 (Product, early). I added an `evolve` target of 0.78 — Commodity +utility within 3–5 years in the target markets. The `evolve` is a scenario, not a forecast (see caveat).

Other components where I considered but did not run a targeted check because the cheat-sheet was internally consistent: Marriage Equality (solidly Commodity +utility in the markets where it exists), Binary Gender Default (unambiguously Commodity +utility globally), Social Media Discourse (Commodity +utility as infrastructure), Biological Sex as a concept (accepted-knowledge Commodity at the knowledge layer, even while contested in application).

### h. Caveat

This map is a **position reading for March 2022**, not a forecast of trajectories. Wardley's climatic pattern #18 applies with particular force in a cultural landscape: *you cannot measure evolution over time or adoption.* The `evolve` targets drawn on the map are scenarios illustrating a direction of contest, not predictions. Several components on this map are capable of *regressing* on ε (moving leftward) under legal, political, and clinical counter-pressure; Wardley's framework does not require evolution to be monotonic in a cultural domain where reversals are normal.

Two further caveats specific to cultural mapping:

1. **Stage labels carry commercial framing.** "Commoditisation" does not mean good or bad — it means taken-for-granted, legible, cheap to invoke. "Commoditised" marriage equality is a *success* for advocates; "commoditised" binary gender default is the *incumbent assumption* for advocates to move. Read stages as positions, not verdicts.
2. **Multiple anchors, multiple maps.** The three anchors here (Individual, Community, Institution) are a useful simplification, but advocacy organisations, state actors, and gender-critical movements would each draw partially different maps. The shape of the map above reflects one reading — a reading anchored on the people navigating the landscape. A map drawn from the perspective of "preserving existing norms" would re-score several components differently, especially around Binary Gender Default, Sex-Segregated Spaces, and the Clinical Evidence Base. The framework works; the specific placements reflect the reading.

---

## Verification (step 5.5)

- Draft OWM: `./draft.owm` co-located with this output.
- Validator: `python3 ${CLAUDE_SKILL_DIR}/scripts/validate_owm.py ./draft.owm`
- **Result: OK — 43 components/anchors, 69 edges — no violations.** Two rounds of validate → fix → validate were needed. The fix-ups moved Public Role Models above Mainstream Media Representation, tightened the legal-layer ordering so Anti-Discrimination Law supports the other laws rather than the other way around, and swapped Binary Gender Default with Sex-Segregated Spaces in the norm layer (Sex-Segregated Spaces *depends on* the binary default, not vice versa).
- Stage naming in prose: reviewed for "Product (+rental)" and "Commodity (+utility)" forms. Bare stage references corrected.
