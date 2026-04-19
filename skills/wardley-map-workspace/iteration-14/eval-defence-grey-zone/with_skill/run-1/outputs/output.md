# Grey Zone Conflict — Wardley Map and Strategic Analysis

Scenario: map the landscape of grey-zone conflict — hostile activity below the threshold of conventional war — spanning disinformation, cyber operations, economic coercion, proxy forces, lawfare, influence operations, critical infrastructure attack, and the defender's counter-measures. The map uses three anchors because grey-zone effects are felt by three distinct user types: the nation-state itself, critical-infrastructure operators (mostly private), and civil society (whose cohesion is the ultimate attack surface for influence operations).

---

## Map (OWM)

```owm
title Grey Zone Conflict Landscape
style wardley

// Anchors — three user types: the state, CI operators, civil society
anchor Nation State [0.99, 0.45]
anchor Critical Infrastructure Operator [0.96, 0.55]
anchor Civil Society [0.93, 0.50]

// ---- Top-line outcomes sought ----
component Sovereign Decision Space [0.88, 0.40]
component Operational Continuity [0.86, 0.55]
component Public Trust & Cohesion [0.84, 0.35]
component Deterrence Posture [0.82, 0.30]

// ---- Attacker-side capability categories (what the defender "sees") ----
component Election Interference [0.80, 0.40]
component Influence Operations [0.78, 0.45]
component Disinformation Campaign [0.76, 0.55]
component Critical Infrastructure Attack [0.74, 0.30]
component Ransomware Operations [0.72, 0.78]
component Supply Chain Compromise [0.70, 0.45]
component Undersea Cable Sabotage [0.68, 0.25]
component Economic Coercion [0.66, 0.45]
component Lawfare [0.64, 0.30]
component Cyber Intrusion (APT) [0.62, 0.70]
component Proxy Forces / PMCs [0.60, 0.40]
component GNSS Jamming & Spoofing [0.58, 0.55]
component Sanctions Evasion [0.54, 0.60]

// ---- Defender-side counter-measures ----
component Counter-Disinformation [0.72, 0.30]
component Strategic Communications [0.70, 0.45]
component Platform Content Moderation [0.66, 0.55]
component Incident Response [0.64, 0.65]
component Diplomatic Demarche [0.62, 0.65]
component Indictments & Legal Action [0.60, 0.45]
component Cyber Defence Operations (SOC) [0.58, 0.65]
component Endpoint Detection & Response [0.54, 0.75]
component Sanctions Regime [0.52, 0.60]
component Export Controls [0.50, 0.55]
component Alliance Coordination (NATO/Five Eyes) [0.48, 0.50]
component Resilience & Redundancy [0.46, 0.45]
component Attribution [0.44, 0.30]
component Threat Intelligence [0.40, 0.55]

// ---- Enabling substrate (shared infra + knowledge) ----
component Social Media Platforms [0.32, 0.80]
component Generative AI Models [0.30, 0.55]
component OSINT Tooling [0.26, 0.55]
component SIGINT / HUMINT Collection [0.24, 0.35]
component Cryptocurrency Rails [0.22, 0.60]
component Cloud Infrastructure [0.18, 0.90]
component Telecoms & Internet Backbone [0.14, 0.92]
component Satellite / GNSS [0.12, 0.80]
component International Law Framework [0.10, 0.40]
component Academic / Think-tank Research [0.08, 0.55]

// ---- Dependencies ----
// Anchors depend on their top-line outcomes
Nation State->Sovereign Decision Space
Nation State->Deterrence Posture
Nation State->Public Trust & Cohesion
Critical Infrastructure Operator->Operational Continuity
Critical Infrastructure Operator->Deterrence Posture
Civil Society->Public Trust & Cohesion
Civil Society->Sovereign Decision Space

// Sovereign decision space pressured by influence/info attacks and defended by comms
Sovereign Decision Space->Election Interference
Sovereign Decision Space->Influence Operations
Sovereign Decision Space->Lawfare
Sovereign Decision Space->Strategic Communications
Sovereign Decision Space->Counter-Disinformation

// Operational continuity threatened by infra attacks and cyber ops
Operational Continuity->Critical Infrastructure Attack
Operational Continuity->Ransomware Operations
Operational Continuity->Supply Chain Compromise
Operational Continuity->Undersea Cable Sabotage
Operational Continuity->GNSS Jamming & Spoofing
Operational Continuity->Resilience & Redundancy
Operational Continuity->Incident Response

// Public trust shaped by info environment
Public Trust & Cohesion->Disinformation Campaign
Public Trust & Cohesion->Influence Operations
Public Trust & Cohesion->Counter-Disinformation
Public Trust & Cohesion->Strategic Communications

// Deterrence rests on attribution, sanctions, alliances, legal action
Deterrence Posture->Sanctions Regime
Deterrence Posture->Export Controls
Deterrence Posture->Alliance Coordination (NATO/Five Eyes)
Deterrence Posture->Indictments & Legal Action
Deterrence Posture->Diplomatic Demarche
Deterrence Posture->Economic Coercion

// Broader attacker categories subsume the technical tools
Election Interference->Disinformation Campaign
Election Interference->Cyber Intrusion (APT)
Influence Operations->Disinformation Campaign
Influence Operations->Proxy Forces / PMCs
Disinformation Campaign->Social Media Platforms
Disinformation Campaign->Generative AI Models
Critical Infrastructure Attack->Cyber Intrusion (APT)
Critical Infrastructure Attack->Proxy Forces / PMCs
Ransomware Operations->Cyber Intrusion (APT)
Ransomware Operations->Cryptocurrency Rails
Supply Chain Compromise->Cyber Intrusion (APT)
Undersea Cable Sabotage->Proxy Forces / PMCs
Undersea Cable Sabotage->Telecoms & Internet Backbone
Economic Coercion->Sanctions Evasion
Economic Coercion->Cryptocurrency Rails
Lawfare->International Law Framework
Cyber Intrusion (APT)->Cloud Infrastructure
Cyber Intrusion (APT)->Telecoms & Internet Backbone
Proxy Forces / PMCs->Cryptocurrency Rails
GNSS Jamming & Spoofing->Satellite / GNSS
Sanctions Evasion->Cryptocurrency Rails

// Defender dependencies
Counter-Disinformation->Platform Content Moderation
Counter-Disinformation->Threat Intelligence
Counter-Disinformation->OSINT Tooling
Strategic Communications->Social Media Platforms
Strategic Communications->Threat Intelligence
Platform Content Moderation->Social Media Platforms
Incident Response->Cyber Defence Operations (SOC)
Incident Response->Endpoint Detection & Response
Diplomatic Demarche->Attribution
Diplomatic Demarche->Alliance Coordination (NATO/Five Eyes)
Indictments & Legal Action->Attribution
Indictments & Legal Action->International Law Framework
Cyber Defence Operations (SOC)->Endpoint Detection & Response
Cyber Defence Operations (SOC)->Threat Intelligence
Endpoint Detection & Response->Cloud Infrastructure
Sanctions Regime->International Law Framework
Sanctions Regime->Alliance Coordination (NATO/Five Eyes)
Export Controls->International Law Framework
Alliance Coordination (NATO/Five Eyes)->International Law Framework
Resilience & Redundancy->Cloud Infrastructure
Resilience & Redundancy->Telecoms & Internet Backbone
Attribution->Threat Intelligence
Attribution->SIGINT / HUMINT Collection
Attribution->OSINT Tooling
Threat Intelligence->OSINT Tooling
Threat Intelligence->SIGINT / HUMINT Collection
Threat Intelligence->Academic / Think-tank Research

// Evolution targets (scenarios, not forecasts)
evolve Generative AI Models 0.78
evolve Attribution 0.55
evolve Counter-Disinformation 0.55
evolve Platform Content Moderation 0.75
evolve Resilience & Redundancy 0.65

note Attacker differentiation zone [0.72, 0.32]
note Commoditised attack substrate [0.20, 0.90]
note Defender industrialisation gap [0.48, 0.35]
```

**Validator:** `OK: 44 components/anchors, 77 edges — no violations.`

---

## Strategic analysis

Read this map as a *contest between two players writing on the same substrate*. Attackers and defenders share the lower-half infrastructure — social platforms, cloud, telecoms, GNSS, cryptocurrency — which is solidly Commodity (+utility). Above that substrate, the attacker's novel moves sit in Genesis / Custom Built and look asymmetric; defender responses lag by roughly one evolution band. The question the map answers: *which grey-zone effects are industrialising (so defenders should buy/rent/standardise against them) and which are genuinely novel (so the exposure is highest and bespoke response is required)?*

### a. Differentiation opportunities (top 3)

Visible components that are still Genesis or Custom Built — where bespoke investment is justified because a product-class answer does not yet exist. These are the places where a defender (or an attacker) can build advantage rather than buy it.

1. **Counter-Disinformation** (Custom Built, ε=0.30) — the most user-visible defender capability that is still bespoke. EU DSA, Taiwan's civil-society fact-check networks, and a handful of government strat-comm units have shown that *something* works, but there is no productised off-the-shelf answer. Highest usable differentiation leverage on the defender side.
2. **Deterrence Posture** (Custom Built, ε=0.30) — as a publishable doctrine, cross-domain deterrence ("integrated deterrence", "persistent engagement") is still being invented. Where the theory lives determines whether the state's threats are credible.
3. **Attribution** (Custom Built, ε=0.30) — the linchpin of every subsequent deterrence move (sanctions, indictments, demarche, alliance action). Still analyst-driven and politically mediated; no commodity product will give you this. Highest *structural* leverage of any defender capability, which is why attackers invest heavily in #11 FUD and plausible deniability around it.

For attacker-side differentiation (interpret as "where adversaries have the highest asymmetric upside"), the mirror trio is **Undersea Cable Sabotage** (Genesis, ε=0.25), **Critical Infrastructure Attack** (Custom Built, ε=0.30), and **Lawfare** (Custom Built, ε=0.30) — all visible pressure points against the defender where the tactic is still novel enough that defender playbooks are thin.

### b. Commodity-leverage candidates (top 3)

Deep, mature components — rent, standardise, or treat as utility. Defenders should not build these.

1. **Telecoms & Internet Backbone** (Commodity +utility, ε=0.92) — utility rails. Resilience investments go into redundancy *on top of* these rails, not into building new ones.
2. **Cloud Infrastructure** (Commodity +utility, ε=0.90) — utility. For Endpoint Detection & Response, for Resilience & Redundancy, and for Strategic Communications, cloud is consumption-priced utility; never self-host the substrate.
3. **Satellite / GNSS** (Commodity +utility, ε=0.80) — utility, but with a sharp caveat: commoditisation has made jamming/spoofing cheap too (GNSS Jamming sits at ε=0.55 precisely because the attack has industrialised alongside the rail). Leverage the commodity, but architect for degraded-mode operations.

Honourable mention: **Ransomware Operations** (Commodity +utility, ε=0.78) is commoditised *on the attacker side* — Ransomware-as-a-Service is a metered utility with affiliate business models. That isn't a defender leverage point, but it is strategically load-bearing: defenders face an industrialised attacker economy, not a craft one.

### c. Dependency risks (top 3)

Edges where a highly visible component depends on something still immature.

1. **Sovereign Decision Space → Counter-Disinformation** — the most politically consequential outcome in the map rests on a Custom Built capability. One cycle of a credible AI-powered influence operation against an electoral decision is the canonical worst case. R ≈ 0.62.
2. **Public Trust & Cohesion → Counter-Disinformation** — same fragility from the civic side. Civil Society is an anchor; its trust rests on a capability that doesn't yet have a product-class answer. R ≈ 0.59.
3. **Deterrence Posture → Attribution** (via Indictments and Diplomatic Demarche) — every sanctions, indictment, and demarche move transitively needs Attribution at ε=0.30. If attribution fails or is contested, the whole deterrence stack silently degrades. R ≈ 0.43–0.57 depending on path.

Two further risks worth naming even though they don't top the list:
- **Operational Continuity → Critical Infrastructure Attack** — the outcome the CI operator cares about most sits directly against a Custom Built (bespoke, low-warning) attack category. Resilience & Redundancy partially covers this but itself is only early Custom Built (ε=0.45).
- **Operational Continuity → Undersea Cable Sabotage** — Genesis-stage attack against a Commodity (+utility) rail. The low ε on the attack side and the concentration on the substrate side compound; this is where exposure is *highest in absolute terms*, even though the map-level R number is more modest.

### d. Suggested gameplays

Named from Wardley's 61-play catalogue:

- **#1 Focus on user needs** — the map deliberately uses three anchors because a state-only map would miss the Civil Society axis, which is where influence operations actually land. Strat-comm that doesn't speak to Civil Society as a user is strat-comm aimed at the wrong audience.
- **#36 Directed investment** on **Attribution**, **Counter-Disinformation**, **Resilience & Redundancy** — the three highest-leverage immature defender capabilities. These are also where every `evolve` arrow in the map points.
- **#15 Open Approaches** on **Platform Content Moderation** and **Counter-Disinformation tooling** — standardise labels, taxonomies, and provenance signatures (C2PA-style watermarking, shared indicators). The defender has an incentive to commoditise content-moderation primitives so that every platform is carrying them; the attacker doesn't. Open-sourcing accelerates the defender-favoured equilibrium.
- **#41 Alliances** — NATO CCDCOE, Five Eyes, EU Hybrid CoE. The map already shows Alliance Coordination at ε=0.50 (early Product); pushing it toward ε=0.65 via standardised threat-intel sharing protocols (MISP, STIX/TAXII) is the industrialisation move.
- **#43 Sensing Engines (ILC)** on **Threat Intelligence** and **OSINT Tooling** — the Bellingcat-era pattern. Read the ecosystem; let open-source investigators front-run state capabilities; harvest the techniques that scale.
- **#33 Raising barriers to entry** on **Cryptocurrency Rails** and **Social Media Platforms** — the two most commoditised attacker substrates. KYC on crypto (MiCA, Travel Rule), DSA-style platform duties on social media. This is defender-side #33, forcing attackers to pay industrial-scale compliance costs.
- **#20 Patents & IPR** — largely irrelevant here and explicitly *not* recommended. Grey-zone attack tools live in national-security R&D, not commercial IP. Export Controls (#22 Limitation of competition) are the analogue that does apply — semiconductor and advanced-GNSS export control is the right lever.
- **#56 First mover** on **GenAI watermarking / provenance standards** — narrow window before generative AI becomes fully commoditised for influence operations. First-moving a provenance standard (C2PA adoption, cryptographic content signing) raises the cost of disinformation content creation.
- **#29 Harvesting** of commercial **Endpoint Detection & Response**, **SOC tooling**, and **Cyber Defence Operations** — the commercial cybersecurity market has already done this industrialisation; governments should consume the product, not re-build it. Harvest the winners (Microsoft Defender, CrowdStrike, SentinelOne, Mandiant).
- **#50 Reinforcing inertia** (adversary-facing) — attackers have sunk capital in specific supply-chain compromise toolchains (SolarWinds, ShadowPad families). Technical counter-measures that force re-tooling (attestation, SBOM) raise the adversary's re-architecture cost (inertia form #9).

### e. Doctrine notes

From Wardley's 40 doctrine principles:

- ✓ **#1 Focus on user needs** — three anchors are used deliberately; grey-zone policy that treats only the state as user systematically under-invests in civil-society resilience.
- ✓ **#10 Know your users** — the three-anchor choice follows this. State, CI operator, and civil society each have different value chains.
- ⚠ **#13 Manage inertia** — the single largest doctrine risk in this domain. Defender inertia is huge: classified-only information-sharing (#6 Confusion over method), sunk capital in legacy air-gapped SCADA (#2, #9), career-incentive misalignment (#4 Human capital). A map this full of Custom Built defender components is a map where inertia will block evolution unless actively managed.
- ⚠ **#2 Use a systematic mechanism of learning** — Attribution and Counter-Disinformation especially need feedback loops from deployed outcomes back into the model. Absent these loops, defenders re-invent techniques per incident.
- ⚠ **#19 There is no single method for managing a map** — grey zone spans Pioneer (novel attack typologies), Settler (productising defender tools like EDR/SIEM), and Town-Planner (utility provisioning of cloud/telecoms). A single agency running all three at once with one culture will fail.
- ⚠ **#28 Remove duplication and bias** — in allied coalitions, the same threat intelligence is produced by multiple national services at sovereign expense; harmonisation is a doctrine obligation, not just a gameplay.

### f. Climatic context

From Wardley's 27 climatic patterns, the shapers of this map:

- **#3 Everything evolves** — every component on the map is moving rightward; the attacker-side commodities (Ransomware-as-a-Service, crypto rails, social platforms) have industrialised faster than the defender-side counter-measures. The gap is the grey-zone exposure.
- **#15–17 Inertia** — especially the *defender* inertia built into classification regimes, legal authorities, and alliance decision-making. Every doctrine violation above manifests as an inertia form.
- **#27 Product-to-utility punctuated equilibrium** — Platform Content Moderation and Generative AI are mid-transition. When a utility model emerges (regulated provenance APIs, safety-tested model marketplaces), the defender landscape changes sharply.
- **#18 You cannot measure evolution over time or adoption** — applies here explicitly. The `evolve` arrows are *scenarios* conditioned on action being taken; they are not forecasts.
- **#13 Competitors' actions will change the game** — uniquely acute for this map because adversaries are *themselves* Wardley mappers. Any defender commoditisation move shifts attacker attention to the next frontier (e.g., harden cyber, attackers shift to cable cutting; harden platforms, attackers shift to encrypted-messenger amplification).
- **#21 Efficiency enables innovation** — attacker commoditisation of the substrate (cheap infrastructure, generative-AI-as-a-service, crypto payments) frees attackers to innovate at the Genesis frontier of Critical Infrastructure Attack and Undersea Cable Sabotage. The same efficiency dynamic defenders celebrate in their cloud bills is arming the adversary.

### g. Deep-placement notes

Four components received targeted second-pass review because they sit on `evolve` arrows or drive the D/R heuristics.

- **Generative AI Models** — initial cheat-sheet placement was ε=0.30 (Custom Built) reflecting adversarial-use bespoke tuning. Re-assessment: the *substrate* (API-priced foundation models, many vendors, published benchmarks, open-weight releases, publication types shifted from "wonder" to "how-to" and operations) is Stage III rapidly industrialising. Moved to ε=0.55 (early Product). `evolve` target 0.78 reflects expected utility-model emergence (metered safety-tested inference marketplaces) over the 2026–2028 horizon. Attacker-use *applications* remain Stage II — not reflected in the substrate node.
- **Attribution** — retained at ε=0.30. Rows disagree: Publication Types (abundant academic literature on attribution methodology) would score Stage III, but Ubiquity (only a handful of credible attributers worldwide), Certainty (contested, politically mediated), and Market (no commodity product exists) anchor it firmly in Custom Built. Flag as "in transition" with uncertainty band 0.25–0.45. The `evolve` arrow to 0.55 is a *scenario* conditioned on standardised tradecraft emerging, not a forecast.
- **Ransomware Operations** — initial ε=0.75. Deep placement via vendor-landscape reasoning (LockBit, Conti, Cl0p affiliate ecosystems; Ransomware-as-a-Service with industrialised support, negotiation services, leak-site operations; cryptocurrency payment rails; industry analyst reporting) moved it to ε=0.78. Solidly Commodity (+utility) on the attacker side. Strategically important because it reframes the defender's counter-measures as fighting an industrialised supplier base, not craft attackers.
- **Platform Content Moderation** — retained at ε=0.55. Commercial products (Hive, Spectrum Labs, Meta/TikTok internal tools) exist and are productised; EU DSA is creating regulatory standardisation pressure. But contested political environments around moderation (post-2022 X, varied national policies) keep it from the Commodity band. `evolve` target 0.75 conditioned on DSA-style regulatory standardisation globalising.
- **Counter-Disinformation** (briefly) — kept at ε=0.30. No productised off-the-shelf answer exists beyond narrow tools (pre-bunking, fact-check networks). Publication is still describing the problem more than operating solutions.

Obvious-commodity components (Cloud, Telecoms, Satellite, Social Media Platforms, Cryptocurrency Rails) were *not* deep-placed — their stage is settled and further research would not shift the strategy.

### h. Caveat

Evolution positions here are a *snapshot plus a scenario*. The `evolve` arrows are conditional hypotheses about where focused investment could move the respective components over the next 2–4 years; they are not forecasts. Wardley's climatic pattern #18 stands: *"you cannot measure evolution over time or adoption."* Attribution in particular has resisted industrialisation for a decade and may continue to. The map's recommendations are stage-robust — they don't require the `evolve` arrows to play out to make sense — but the prioritisation would shift if, for example, a regulated GenAI-provenance utility emerged faster than expected (compressing the window for play #56 First mover) or slower than expected (widening the defender exposure on Disinformation Campaigns).

---

## Where grey-zone exposure is highest

The direct answer to the user's question, distilled from the D/K/R analysis above:

1. **Information environment pressure on sovereign decisions and elections.** Attacker capability is visible (ν≈0.76–0.80) and the defender counter (Counter-Disinformation) is Custom Built. Substrate (Social Media Platforms, Generative AI) is already Commodity or near-Commodity, meaning attacker marginal cost is low. This is the single biggest strategic exposure in the map.

2. **Critical infrastructure under Genesis-stage physical/cyber hybrid attacks.** Undersea Cable Sabotage (ε=0.25) and Critical Infrastructure Attack (ε=0.30) against Commodity (+utility) Telecoms / GNSS / Cloud rails. Exposure is compounded by the substrate being highly concentrated (few cable operators, a handful of cloud hyperscalers, two GNSS constellations the West relies on).

3. **Deterrence dependence on Attribution.** Every consequential retaliatory move (indictments, demarche, sanctions, alliance action) transitively requires Attribution, which remains Custom Built. This is the structural weak point that explains why attackers deliberately operate in the grey zone rather than above the threshold of conflict — the attribution tax is the whole reason the grey zone works as a concept.

## What's differentiating vs. commoditising

**Commoditising (on the attacker side, raising exposure):** Ransomware-as-a-Service, generative AI models, cryptocurrency rails, social media reach. These are all utility-priced; the attacker's marginal cost of a campaign is falling.

**Commoditising (on the defender side, lowering cost of defence):** Endpoint Detection & Response, SOC operations, cloud-backed Resilience & Redundancy, Platform Content Moderation. Defenders should consume these as products / utilities, not build them.

**Differentiating (on the defender side, where investment pays off):** Attribution, Counter-Disinformation, Strategic Communications, Alliance Coordination, Deterrence Posture doctrine. These are Custom Built and are where national-level advantage is actually built.

**Differentiating (on the attacker side, where exposure is highest):** Undersea Cable Sabotage, Critical Infrastructure Attack, Lawfare, Election Interference campaign design. These are the Genesis / Custom Built frontiers that attackers are actively exploiting because defender playbooks are thin.

The structural asymmetry of grey-zone conflict is readable directly off this map: the attacker has industrialised the substrate and is innovating at the top; the defender is fighting yesterday's war at the product-commodity layer while the decisive contests happen in the Custom Built band above it.
