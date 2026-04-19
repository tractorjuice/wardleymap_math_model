# Defence Intelligence Landscape — Wardley Map (March 2023)

**Scenario.** A national defence establishment's intelligence enterprise: collection (HUMINT, SIGINT, OSINT, GEOINT/satellite, MASINT, cyber), processing/exploitation/dissemination (PED), all-source fusion and analysis, tradecraft, tooling, and decision-support to commanders, planners and allied partners. Mapped as of March 2023 — before the post-Ukraine commercial-OSINT and generative-AI waves had fully reshaped the landscape but when both were clearly in motion.

**Scope note.** This is a *landscape* map (35–45 components is the target). It does not attempt to model a specific agency's org chart; it captures the capability layers every Five-Eyes-class intelligence establishment operates. Multi-anchor: the decision-maker, the operational planner, and the allied partner all consume the enterprise's output but for different reasons.

---

## 1. Map (OWM)

```owm
title Defence Intelligence Landscape (March 2023)
style wardley

// Anchors — three distinct user-need nodes
anchor Commander / Minister [0.99, 0.45]
anchor Operational Planner [0.96, 0.50]
anchor Allied Partner [0.93, 0.55]

// User-facing outputs (dissemination)
component Actionable Intelligence Product [0.88, 0.45]
component Daily Intelligence Briefing [0.84, 0.55]
component All-Source Assessment [0.82, 0.35]
component Targeting Support Pack [0.80, 0.40]
component Indications & Warnings [0.78, 0.35]

// Analysis layer
component All-Source Fusion [0.72, 0.30]
component Geopolitical Analysis [0.70, 0.25]
component Threat Modelling [0.68, 0.40]
component Analytic Tradecraft [0.66, 0.55]
component Red Teaming [0.64, 0.30]
component Structured Analytic Techniques [0.62, 0.55]
component AI-Assisted Analysis [0.58, 0.15]

// Processing & exploitation
component PED (Processing, Exploitation, Dissemination) [0.54, 0.45]
component Imagery Exploitation [0.52, 0.55]
component SIGINT Processing [0.50, 0.50]
component Language Translation [0.48, 0.60]
component Entity Resolution [0.46, 0.40]
component Data Fusion Platform [0.44, 0.35]
component Secure Collaboration Tooling [0.42, 0.55]

// Collection disciplines
component HUMINT Collection [0.38, 0.30]
component SIGINT Collection [0.36, 0.55]
component OSINT Collection [0.34, 0.65]
component GEOINT / Satellite Imagery [0.32, 0.60]
component Commercial Satellite Imagery [0.30, 0.70]
component Cyber Intelligence [0.28, 0.40]
component MASINT [0.26, 0.30]
component Social Media Monitoring [0.24, 0.70]

// Collection infrastructure
component Agent Handling Tradecraft [0.22, 0.30]
component Covert Platforms [0.20, 0.25]
component Signals Interception Infrastructure [0.18, 0.55]
component Own Satellite Constellations [0.16, 0.40]
component Covert Comms [0.14, 0.35]

// Knowledge & doctrine
component Target Language Expertise [0.20, 0.50]
component Regional / Cultural Expertise [0.18, 0.45]
component Intelligence Doctrine [0.16, 0.70]
component Classification & Handling Rules [0.14, 0.80]

// Foundational IT utilities
component Classified Networks (JWICS / STONEGHOST) [0.12, 0.60]
component Secure Cloud (IL6 / Top Secret) [0.10, 0.45]
component Cryptography [0.08, 0.85]
component Compute & Storage [0.06, 0.90]
component Power & Comms [0.04, 0.95]

// Dependencies
Commander / Minister->Actionable Intelligence Product
Commander / Minister->Daily Intelligence Briefing
Commander / Minister->Indications & Warnings
Operational Planner->Targeting Support Pack
Operational Planner->All-Source Assessment
Operational Planner->Actionable Intelligence Product
Allied Partner->All-Source Assessment
Allied Partner->Daily Intelligence Briefing

Actionable Intelligence Product->All-Source Fusion
Daily Intelligence Briefing->All-Source Assessment
All-Source Assessment->All-Source Fusion
All-Source Assessment->Geopolitical Analysis
Targeting Support Pack->All-Source Fusion
Targeting Support Pack->Threat Modelling
Indications & Warnings->All-Source Fusion
Indications & Warnings->Threat Modelling

All-Source Fusion->Analytic Tradecraft
All-Source Fusion->Data Fusion Platform
All-Source Fusion->Entity Resolution
All-Source Fusion->Red Teaming
Geopolitical Analysis->Regional / Cultural Expertise
Threat Modelling->Structured Analytic Techniques
Threat Modelling->AI-Assisted Analysis
Analytic Tradecraft->Structured Analytic Techniques
Red Teaming->Structured Analytic Techniques
AI-Assisted Analysis->Compute & Storage

PED (Processing, Exploitation, Dissemination)->Imagery Exploitation
PED (Processing, Exploitation, Dissemination)->SIGINT Processing
PED (Processing, Exploitation, Dissemination)->Language Translation
PED (Processing, Exploitation, Dissemination)->Data Fusion Platform
Imagery Exploitation->GEOINT / Satellite Imagery
Imagery Exploitation->Commercial Satellite Imagery
SIGINT Processing->SIGINT Collection
Language Translation->Target Language Expertise
Entity Resolution->Data Fusion Platform
Data Fusion Platform->Secure Cloud (IL6 / Top Secret)
Secure Collaboration Tooling->Classified Networks (JWICS / STONEGHOST)

All-Source Fusion->PED (Processing, Exploitation, Dissemination)
All-Source Fusion->Secure Collaboration Tooling
All-Source Fusion->HUMINT Collection
All-Source Fusion->SIGINT Collection
All-Source Fusion->OSINT Collection
All-Source Fusion->GEOINT / Satellite Imagery
All-Source Fusion->Cyber Intelligence
All-Source Fusion->MASINT

HUMINT Collection->Agent Handling Tradecraft
HUMINT Collection->Covert Platforms
HUMINT Collection->Covert Comms
SIGINT Collection->Signals Interception Infrastructure
SIGINT Collection->Cryptography
OSINT Collection->Social Media Monitoring
OSINT Collection->Compute & Storage
GEOINT / Satellite Imagery->Own Satellite Constellations
GEOINT / Satellite Imagery->Commercial Satellite Imagery
Cyber Intelligence->Signals Interception Infrastructure
MASINT->Covert Platforms
Social Media Monitoring->Compute & Storage

Agent Handling Tradecraft->Regional / Cultural Expertise
Agent Handling Tradecraft->Target Language Expertise
Covert Platforms->Power & Comms
Signals Interception Infrastructure->Power & Comms
Own Satellite Constellations->Power & Comms
Covert Comms->Cryptography

Classified Networks (JWICS / STONEGHOST)->Secure Cloud (IL6 / Top Secret)
Classified Networks (JWICS / STONEGHOST)->Cryptography
Secure Cloud (IL6 / Top Secret)->Compute & Storage
Secure Cloud (IL6 / Top Secret)->Cryptography
Compute & Storage->Power & Comms

All-Source Assessment->Intelligence Doctrine
All-Source Assessment->Classification & Handling Rules
Actionable Intelligence Product->Classification & Handling Rules

evolve Commercial Satellite Imagery 0.85
evolve OSINT Collection 0.80
evolve AI-Assisted Analysis 0.55
evolve Social Media Monitoring 0.80
evolve Own Satellite Constellations 0.65

note Human craft + secrets [0.30, 0.20]
note Commoditising open layer [0.30, 0.75]
note Utility infrastructure [0.08, 0.92]
```

---

## 2. Strategic analysis

### a. Differentiation opportunities (top 3)

1. **All-Source Fusion (Custom Built).** The ability to integrate HUMINT, SIGINT, OSINT, GEOINT, cyber and MASINT into a single coherent picture *faster and more accurately than an adversary* is the defining craft of a modern intelligence enterprise. Every user-facing product funnels through this node. Highest differentiation leverage — visible, immature, and uniquely yours.
2. **Agent Handling Tradecraft and HUMINT Collection (Custom Built).** Human networks, recruitment, and covert tradecraft are irreducibly bespoke. No vendor will ever sell this. It sits deep but its value is disproportionate to its visibility because the rest of the stack can be commoditised around it.
3. **AI-Assisted Analysis (Genesis).** In March 2023 this is a transformer-wave frontier play: LLM-assisted triage, imagery classification at scale, anomaly detection across heterogeneous feeds. Still Genesis in defence contexts (classified environments lag the commercial state of the art by 12–24 months). Whoever gets this right first inside TS/SCI boundaries captures a durable analytic-speed advantage.

Honourable mentions: **Regional / Cultural Expertise** (deep, late Custom) — cannot be bought, cannot be rushed, and is usually under-funded relative to its strategic weight.

### b. Commodity-leverage candidates (top 3)

1. **Compute & Storage (Commodity +utility)** — hyperscaler utility even inside classified environments (AWS Secret Region, Azure Government/IL6, Google Distributed Cloud). Rent, do not build.
2. **Cryptography (Commodity +utility)** — NSA Suite B / CNSA 2.0 are standards; agencies consume, they don't invent. The only variable is post-quantum migration timing.
3. **Commercial Satellite Imagery (Product +rental, trending toward Commodity +utility)** — Maxar, Planet, BlackSky, Capella Space, ICEYE now offer near-daily revisit at sub-metre resolution under subscription. Buy capacity; reserve organic constellations for the things commercials cannot do (persistent, covert, non-revealing).

Close contender: **Classified Networks (JWICS / STONEGHOST)** are operated as an inter-agency utility — treat as consumed infrastructure, not a capability to re-invent.

### c. Dependency risks (top 3)

Edges where a visible component depends on a fragile, immature, or single-source foundation.

1. **All-Source Fusion → Data Fusion Platform (Custom Built → Custom Built).** A Stage II → Stage II dependency right at the top of the analysis stack. Most defence enterprises rely on bespoke, contractor-integrated Palantir/IBM i2/homegrown stacks with heavy technical debt. If the fusion platform is slow or siloed, every downstream product is slow and siloed. High dependency risk because the node above is visible and the node below is immature.
2. **HUMINT Collection → Agent Handling Tradecraft (Custom Built → Custom Built).** Irreducibly human; the craft lives in a small population of experienced officers. Talent attrition, generational handover, and recruitment pool narrowing are all material. Cannot be commoditised, so the fragility must be managed by structure and pipeline — not eliminated.
3. **Targeting Support Pack → Threat Modelling → AI-Assisted Analysis (visible → Custom → Genesis).** A user-facing product increasingly pulling on Genesis-stage ML for tempo. Any outage, hallucination, or misclassification event lands on the commander's desk. This chain is the most common place where the ML stack will meet its first operationally-embarrassing failure — worth an explicit assurance regime before scale-out.

Also noted: **All-Source Assessment → Geopolitical Analysis → Regional / Cultural Expertise** — a Product-stage briefing depending on late-Custom tradecraft depending on thinning human-capital pool. Classic tail-risk shape.

### d. Suggested gameplays

Citing from Wardley's 61-play catalogue:

- **#1 Focus on user needs** — the three anchors (Commander, Planner, Ally) produce different products. Avoid a single "intelligence product" pipeline that flattens their distinct needs.
- **#36 Directed investment** on **All-Source Fusion** and **AI-Assisted Analysis** — these are the top-D components; concentrate engineering and data-science effort here rather than spreading it across every PED silo.
- **#29 Harvesting** on **Commercial Satellite Imagery**, **Social Media Monitoring**, and **OSINT Collection** — let Maxar, Planet, BlackSky, Bellingcat-style open platforms, and commercial social-listening vendors race; consume the winners on contract. Do not build what a three-year-old Seattle startup now ships as SaaS.
- **#43 Sensing Engines (ILC)** on the **OSINT → All-Source Fusion** edge — use ecosystem signals (commercial vendor roadmaps, open datasets appearing, academic publication patterns) to decide which OSINT capabilities are about to become utilities so you can re-allocate analyst time.
- **#15 Open Approaches** on **Intelligence Doctrine** between Five Eyes / NATO partners — standardising doctrine and metadata reduces allied-partner friction and lowers switching cost when two agencies must fuse data on short notice. Explicitly *not* open-sourcing tradecraft.
- **#41 Alliances** on **GEOINT / Satellite Imagery** and **Own Satellite Constellations** — partner with allies for constellation coverage (NATO AGS model) rather than unilaterally building everything.
- **#55 Land grab** on **AI-Assisted Analysis inside TS/SCI** — be the first sovereign establishment to run a credible classified LLM-in-the-SCIF capability. The window is 2023–2025.
- **#56 First mover** on **commercial OSINT integration at speed** — Ukraine 2022 proved the value; the first agency to fully industrialise the OSINT → All-Source pipeline pulls ahead on tempo.
- **#30 Standards game** on **metadata / sharing protocols** (STIX/TAXII-equivalents for all-source) — whoever sets the standard reduces their own integration cost and raises competitor transition cost.
- **#13 Lobbying** (ethics-noted) — commercial-imagery licence regimes, PQC timelines, and data-access law are actively shaped; agencies that leave this to others are ceding structural ground.
- **#7 Education** of commanders and ministers — user inertia (form #6, *confusion over method*) on probabilistic intelligence language is a real consumption blocker. The best fusion in the world fails on delivery if the customer can't act on "moderate confidence".

### e. Doctrine violations / risks

Using the 40 principles:

- **✓ #1 Focus on user needs** — three anchors correctly identified.
- **✓ #10 Know your users** — Commander, Planner and Allied Partner are genuinely distinct user classes. The map respects this; a single-anchor map would have hidden the allied-sharing constraints.
- **⚠ #9 Think small (know the details)** — "PED" and "All-Source Fusion" are still relatively coarse nodes. For an actual enterprise workshop they would each need decomposing (e.g., target-nomination flow, GEOINT PED pipeline, cyber-triage loop). Left coarse here deliberately to keep the landscape map at ~44 components.
- **⚠ #13 Manage inertia** — at least five live inertia forms are visible: **#2 sunk capital** in legacy Palantir/i2 instances; **#3 political capital** around discipline fiefdoms (the HUMINT vs SIGINT vs GEOINT turf problem is perennial); **#4 human-capital inertia** in linguists and area experts; **#6 confusion over method** with decision-makers on probabilistic language; **#14 strategic-control loss** fears around commercial-OSINT dependency. Each needs naming, not papering over.
- **⚠ #2 Use a systematic mechanism of learning** — post-mortems on intelligence failures exist (IC Inspector-General reviews, Butler/Chilcot in the UK) but feeding those findings back into tradecraft and tool design is structurally weak. The analytic-tradecraft and red-team nodes are the learning surface; they need protected time.
- **⚠ #4 Be transparent** — tension with classification is inherent in this domain. Doctrine doesn't ask for operational transparency, it asks for *strategy* transparency. Maps like this one should be legible across the enterprise at unclassified level.
- **⚠ #29 Distribute power and decision making** — high-tempo environments (cyber, I&W) collapse if every release needs flag-officer sign-off. The visibility constraint on Indications & Warnings (ν = 0.78, directly to Commander) implies a release authority designed for speed.

### f. Climatic context

Patterns actively shaping this map (of 27):

- **#3 Everything evolves through supply-and-demand competition.** Commercial satellite imagery, OSINT, and social-media monitoring have all marched rightward sharply since 2020. Defence establishments that treat them as 2015-era niche tools have a stale map.
- **#4 Evolution is multi-wave with chasms.** Satellite imagery is on its third generation (national → commercial hi-res → smallsat constellation + SAR + RF). GEOINT analysts trained on NGA-grade products hit a chasm moving to Planet-Labs-tempo workflows. Plan for the chasm, don't deny it.
- **#7 Characteristics change as components evolve.** The open/commercial OSINT layer is in Stage III (product) behaviour — price pressure, feature comparison, vendor churn — while HUMINT tradecraft is in Stage II (craft + bespoke). Applying Six-Sigma-style management to the latter, or Genesis-style experimentation to the former, both fail. Doctrine #7 (Use appropriate methods) is the operational response.
- **#11 Future value is inversely proportional to certainty.** AI-Assisted Analysis has the highest future optionality precisely because it is most uncertain. Under-investment here because "we don't know if it'll work" is precisely the error pattern Wardley warns against.
- **#15–17 Inertia.** Five Eyes establishments that dominated the Cold War satellite era carry the most inertia precisely *because* they won. Exploitable by adversaries running #50 (Reinforcing inertia) — forcing the incumbent to double down on the old collection paradigm.
- **#22 Two forms of disruption.** The landscape is seeing both types simultaneously: Genesis disruption (generative AI for analysis) and Product-to-Utility disruption (commercial OSINT replacing bespoke collection for a widening class of questions). They require different responses; conflating them is the classic strategic error.
- **#27 Product-to-utility punctuated equilibrium.** Commercial satellite imagery is mid-transition right now. Delays in restructuring organic collection around commercial-first will compound rapidly once the transition fully punctuates.
- **#18 You cannot measure evolution over time or adoption.** Every `evolve` arrow below is scenario, not forecast.

### g. Deep-placement notes

For the 2023 snapshot, four components warranted targeted reflection beyond cheat-sheet defaults. No live web searches were run in this pass (budget-conscious; the landscape is well-characterised in open sources up to March 2023), but the priors below are documented so a reader can challenge them:

- **Commercial Satellite Imagery — placed at ε = 0.70 (late Product (+rental)), evolving to 0.85 (Commodity (+utility)).** Initial cheat-sheet instinct was mid-Product (~0.60). The 2022–2023 Ukraine tempo — Maxar/Planet daily publication, BlackSky tip-and-cue, Capella SAR — showed *ubiquity* and *publication type* had both advanced into standardisation, while *user perception* was shifting from "leading edge" to "expected". This justifies the nudge from 0.60 to 0.70 and the evolve-target of 0.85.
- **OSINT Collection — placed at ε = 0.65 (mid Product (+rental)), evolving to 0.80.** Initial cheat-sheet would have put traditional agency-run OSINT at mid-Custom (~0.45). But by March 2023 the OSINT landscape includes commercial platforms (Janes, Recorded Future, Maltego, Bellingcat-style open workflows); the *market* and *ubiquity* rows clearly say Product. I placed the node at the market-aware score, not the internal-tool score. Worth flagging: there is a legitimate case for treating "internal OSINT cell tooling" as a separate lower-ε node; I folded them into one to keep the landscape readable.
- **AI-Assisted Analysis — placed at ε = 0.15 (Genesis), evolving to 0.55.** In March 2023 most agencies are *just* reacting to ChatGPT (Nov 2022) and the GPT-4 release (March 2023). Classified ML capabilities are 12–24 months behind the commercial frontier. Stage I is the honest placement; analysts disagree on what works; publication types describe the wonder; the market is undefined inside secure environments. Variance across cheat-sheet rows is high here — flagged as in-transition. Plot could reasonably be a range 0.10–0.25.
- **Social Media Monitoring — placed at ε = 0.70 (late Product (+rental)), evolving to 0.80.** Commercial vendors (Babel Street, Dataminr, ShadowDragon) are mature; the public-sector user perception has caught up post-2020. Placed alongside OSINT, deliberately.

If a live workshop were to run this map with search budget, priority deep-placement targets would be: (1) AI-Assisted Analysis (variance highest); (2) Own Satellite Constellations (smallsat-era economics may have shifted its ε); (3) Data Fusion Platform (vendor concentration post Palantir's FY22 growth is worth measuring).

### h. Validator

Ran `scripts/validate_owm.py` against the draft:

```
OK: 44 components/anchors, 71 edges — no violations.
```

### i. Caveat

All evolution positions, and especially the `evolve` arrows for Commercial Satellite Imagery, OSINT, AI-Assisted Analysis, Social Media Monitoring, and Own Satellite Constellations, are **scenarios, not forecasts**. Wardley's climatic pattern #18 stands: *"you cannot measure evolution over time or adoption."* The map is a situational-awareness artefact anchored to March 2023; it should be re-scored as commercial OSINT, classified LLMs, and smallsat economics continue to move. Anything with an `evolve` arrow should be revisited quarterly during the 2023–2025 transition window; the rest can be reviewed annually.
