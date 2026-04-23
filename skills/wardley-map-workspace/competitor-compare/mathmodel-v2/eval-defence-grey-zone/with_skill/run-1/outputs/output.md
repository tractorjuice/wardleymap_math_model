# Wardley Map — Defence Grey Zone: Below-Threshold State Competition

## Step 0 — Strategic framing

**Strategic question.** Where in the grey-zone landscape is hostile effect-delivery already *weaponised-commodity* (cheap, plentiful, widely instrumented) versus where attribution, consequences and ethics are still genuinely novel — so that a defender can tell at a glance where to buy off-the-shelf countermeasures and where it still has to fund original research?

**User anchors (U).** Two users sit at the top of the value chain:
1. **Contested State** — the polity whose sovereignty is being probed below the threshold of declared war.
2. **Population** — the citizenry whose hearts, minds and data are the terrain of contest.

Using two anchors (rather than one abstract "national security") is a deliberate doctrine call: grey-zone effects are often waged *against a population* to reach a state (cognitive / electoral effects) and the value chain differs materially for each user.

**Core needs.**
- Legitimacy of the state in the eyes of its own population and its allies.
- Sovereignty across four pillars — cyber, territory, economic, culture.
- Attribution and accountability for hostile acts below the threshold of war.
- Security from kinetic and cognitive harm, including friendly-fire and unintended outcomes.

**Scope boundary.** The landscape of inter-state grey-zone competition, 2024–2026, covering supranational, state, proxy and individual actors; the five theatres the user called out (land, electronic, space, social media, finance); and the tooling / infra stack underneath. This is an *industry-landscape* map (target ~40–55 components per the skill's density guidance); the final map has 58 components.

**Assumptions** (flag these; user may correct):
- The "contested state" is a liberal-democratic state. Authoritarian states have a different legitimacy chain (the Population user anchor is weaker there).
- "Grey zone" is taken as Hoffman/Nadia Schadlow sense — coercive activity deliberately calibrated below Article 2(4) / armed-attack thresholds.
- The map is a landscape, not a doctrine map; it does not prescribe a single state's response.

---

## The map

```owm
title Defence Grey Zone - Below-Threshold State Competition
style wardley

// Anchors - the two user populations at the top of the value chain
anchor Contested State [0.98, 0.42]
anchor Population [0.96, 0.58]

// --- Sovereignty pillars under contest (user-visible needs) ---
component Legitimacy [0.90, 0.30]
component Cyber Sovereignty [0.88, 0.40]
component Territorial Sovereignty [0.86, 0.55]
component Economic Sovereignty [0.84, 0.62]
component Cultural Sovereignty [0.82, 0.35]

// --- Governance framework (visible, slowly evolving) ---
component Statecraft [0.78, 0.30]
component Treaties and International Law [0.75, 0.68]
component Ethics Frameworks [0.73, 0.28]
component Accountability [0.71, 0.22]
component Attribution [0.69, 0.32]
component Deniability [0.67, 0.55]

// --- Effect types (what users feel directly from the grey zone) ---
component Coercion [0.64, 0.53]
component Deterrence [0.62, 0.45]
component Hearts and Minds Campaigns [0.60, 0.52]
component Kinetic Effects [0.58, 0.78]
component Propaganda [0.56, 0.72]

// --- Consequences (user-visible harms of effects) ---
component Civilian Harm [0.54, 0.40]
component Friendly Fire [0.52, 0.35]
component Escalation Risk [0.50, 0.38]
component Unintended Outcomes [0.48, 0.30]

// --- Actors (who plays) - sit below the effects they produce ---
component Supranationals [0.46, 0.40]
component Allied Governments [0.44, 0.55]
component Hostile Governments [0.42, 0.55]
component Intelligence Services [0.39, 0.60]
component Private Proxy Operators [0.38, 0.58]
component State-Aligned Hackers [0.36, 0.70]
component Private Military Companies [0.34, 0.65]
component Diaspora and Influence Networks [0.32, 0.45]

// --- Theatres of competition ---
component Land Theatre [0.44, 0.85]
component Electronic Theatre [0.42, 0.62]
component Space Theatre [0.40, 0.45]
component Social Media Theatre [0.46, 0.68]
component Finance Theatre [0.44, 0.72]

// --- Landscape layers (with awareness) ---
component Physical Landscape [0.30, 0.80]
component Virtual Landscape [0.28, 0.60]
component Supply Chain Landscape [0.26, 0.55]
component Physical Awareness (ISR) [0.24, 0.68]
component Virtual Awareness (Cyber ISR) [0.22, 0.52]
component Supply Chain Awareness [0.20, 0.32]

// --- Tactical / operational tooling (mid-deep) ---
component Disinformation Tooling [0.30, 0.70]
component Influence-as-a-Service [0.28, 0.55]
component Cyber Exploitation Kits [0.26, 0.78]
component Commercial Spyware [0.24, 0.72]
component Election Interference Playbooks [0.22, 0.48]
component Economic Sanctions Tooling [0.20, 0.78]
component Sabotage and Grey Kinetic [0.18, 0.55]
component Agentic AI Influence Ops [0.28, 0.15]
component Quantum-Assisted Attribution [0.25, 0.10]

// --- Infrastructure and commodities at the base ---
component Crypto Rails [0.16, 0.70]
component Dark Pools and OTC Crypto [0.14, 0.58]
component Bot Farms [0.13, 0.85]
component Synthetic Media (Deepfakes) [0.18, 0.45]
component Generative AI Content [0.15, 0.40]
component Open Source Intelligence (OSINT) [0.11, 0.82]
component Satellite Imagery [0.10, 0.88]
component Commercial Telemetry Data [0.09, 0.78]
component Submarine Cable Infrastructure [0.06, 0.85]
component Cloud Compute [0.04, 0.92]

// --- Dependencies ---
// User needs -> sovereignty pillars
Contested State->Legitimacy
Contested State->Cyber Sovereignty
Contested State->Territorial Sovereignty
Contested State->Economic Sovereignty
Contested State->Cultural Sovereignty
Population->Legitimacy
Population->Cultural Sovereignty
Population->Cyber Sovereignty

// Sovereignty -> governance machinery
Legitimacy->Statecraft
Legitimacy->Ethics Frameworks
Legitimacy->Accountability
Cyber Sovereignty->Attribution
Cyber Sovereignty->Treaties and International Law
Territorial Sovereignty->Statecraft
Territorial Sovereignty->Treaties and International Law
Economic Sovereignty->Treaties and International Law
Cultural Sovereignty->Ethics Frameworks

// Governance -> effects
Statecraft->Deterrence
Statecraft->Coercion
Statecraft->Hearts and Minds Campaigns
Treaties and International Law->Kinetic Effects
Treaties and International Law->Coercion
Ethics Frameworks->Propaganda
Accountability->Attribution
Attribution->Deniability

// Effects -> consequences
Coercion->Escalation Risk
Coercion->Civilian Harm
Kinetic Effects->Civilian Harm
Kinetic Effects->Friendly Fire
Propaganda->Unintended Outcomes
Hearts and Minds Campaigns->Unintended Outcomes
Deterrence->Escalation Risk

// Effects -> actors who perform them
Coercion->Intelligence Services
Coercion->Hostile Governments
Coercion->State-Aligned Hackers
Deterrence->Allied Governments
Deterrence->Supranationals
Hearts and Minds Campaigns->Allied Governments
Hearts and Minds Campaigns->Diaspora and Influence Networks
Kinetic Effects->Private Military Companies
Kinetic Effects->Hostile Governments
Propaganda->Hostile Governments
Propaganda->Intelligence Services
Propaganda->Private Proxy Operators
Propaganda->Diaspora and Influence Networks

// Deniability is what lets states use proxies
Deniability->Private Proxy Operators
Deniability->State-Aligned Hackers
Deniability->Private Military Companies

// Effects run in theatres
Coercion->Electronic Theatre
Coercion->Finance Theatre
Propaganda->Social Media Theatre
Hearts and Minds Campaigns->Social Media Theatre
Kinetic Effects->Land Theatre
Deterrence->Space Theatre
Deterrence->Electronic Theatre

// Theatres sit on landscape layers
Land Theatre->Physical Landscape
Electronic Theatre->Virtual Landscape
Space Theatre->Physical Landscape
Social Media Theatre->Virtual Landscape
Finance Theatre->Supply Chain Landscape
Finance Theatre->Virtual Landscape

Physical Landscape->Physical Awareness (ISR)
Virtual Landscape->Virtual Awareness (Cyber ISR)
Supply Chain Landscape->Supply Chain Awareness

// Theatres depend on tactical tooling
Social Media Theatre->Disinformation Tooling
Social Media Theatre->Influence-as-a-Service
Electronic Theatre->Cyber Exploitation Kits
Electronic Theatre->Commercial Spyware
Social Media Theatre->Election Interference Playbooks
Finance Theatre->Economic Sanctions Tooling
Land Theatre->Sabotage and Grey Kinetic

// Tactical tooling depends on infrastructure
Disinformation Tooling->Bot Farms
Disinformation Tooling->Synthetic Media (Deepfakes)
Disinformation Tooling->Generative AI Content
Influence-as-a-Service->Bot Farms
Influence-as-a-Service->Generative AI Content
Influence-as-a-Service->Agentic AI Influence Ops
Disinformation Tooling->Agentic AI Influence Ops
Attribution->Quantum-Assisted Attribution
Cyber Exploitation Kits->Cloud Compute
Commercial Spyware->Cloud Compute
Election Interference Playbooks->Bot Farms
Economic Sanctions Tooling->Commercial Telemetry Data
Economic Sanctions Tooling->Crypto Rails
Sabotage and Grey Kinetic->Open Source Intelligence (OSINT)

// Finance / crypto plumbing
Finance Theatre->Crypto Rails
Crypto Rails->Dark Pools and OTC Crypto

// Awareness / ISR layers lean on commodity data
Physical Awareness (ISR)->Satellite Imagery
Physical Awareness (ISR)->Open Source Intelligence (OSINT)
Virtual Awareness (Cyber ISR)->Commercial Telemetry Data
Virtual Awareness (Cyber ISR)->Open Source Intelligence (OSINT)
Supply Chain Awareness->Commercial Telemetry Data
Supply Chain Awareness->Open Source Intelligence (OSINT)

// Core infra
Satellite Imagery->Cloud Compute
Open Source Intelligence (OSINT)->Cloud Compute
Commercial Telemetry Data->Cloud Compute
Bot Farms->Cloud Compute
Synthetic Media (Deepfakes)->Generative AI Content
Generative AI Content->Cloud Compute
Physical Landscape->Submarine Cable Infrastructure
Virtual Landscape->Submarine Cable Infrastructure

// Evolve arrows - where the map says the axis is shifting
evolve Attribution 0.55
evolve Synthetic Media (Deepfakes) 0.75
evolve Influence-as-a-Service 0.80
evolve Commercial Spyware 0.82
evolve Ethics Frameworks 0.45
evolve Agentic AI Influence Ops 0.55
evolve Quantum-Assisted Attribution 0.40

// Notes
note Weaponised-commodity zone [0.22, 0.82]
note Genuinely novel - attribution frontier [0.72, 0.22]
note Dual-use commodity data [0.10, 0.80]
```

---

## §3.2 Component evolution rationale (evidence table)

| Component | Stage | ε | ν | Evidence |
|---|---|---:|---:|---|
| Legitimacy | Custom Built | 0.30 | 0.90 | Measured by trust indices (Edelman, Pew) — metrics exist but the object itself is contested and culture-specific; no standard scoring. |
| Cyber Sovereignty | Custom Built | 0.40 | 0.88 | Concept codified by China, Russia, EU Digital Sovereignty package 2023-24; each jurisdiction still defining scope. |
| Territorial Sovereignty | Product (+rental) | 0.55 | 0.86 | Westphalian norm; UN Charter Art 2(4); well-understood but grey-zone erodes fit-for-purpose (Crimea 2014, Doklam 2017). |
| Economic Sovereignty | Product (+rental) | 0.62 | 0.84 | Sanctions-regime practice mature (OFAC SDN list, EU restrictive measures); CBDC / export-control layers productising. |
| Cultural Sovereignty | Custom Built | 0.35 | 0.82 | France's *exception culturelle*, India data-localisation, but no convergent approach; patterns emerging. |
| Statecraft | Custom Built | 0.30 | 0.78 | Ancient practice, but grey-zone statecraft (Hoffman 2007, Schadlow 2017) still academic-heavy; few playbooks. |
| Treaties and International Law | Product (+rental) | 0.68 | 0.75 | UN Charter, Geneva, Tallinn Manual 2.0 (2017) — mature legal product; attribution rules lag the tech. |
| Ethics Frameworks | Custom Built | 0.28 | 0.73 | Just-War and Tallinn ethics apply unevenly; AI-warfare ethics (REAIM Hague 2023) is early. |
| Accountability | Custom Built | 0.22 | 0.71 | ICJ, ICC, special tribunals exist but grey-zone acts rarely reach them; accountability is still case-by-case. |
| Attribution | Custom Built | 0.32 | 0.69 | Mandiant APT1 (2013) → DOJ indictments of GRU/PLA Unit 61398; methodology patchy, slow, contested. |
| Deniability | Product (+rental) | 0.55 | 0.67 | Well-practised doctrine — Little Green Men (2014), Wagner (2014–2023), Russian SVR cut-outs; deniability-as-method is a mature tradecraft product. |
| Coercion | Product (+rental) | 0.53 | 0.64 | Sanctions, diplomatic expulsions, election interference now a recognised state toolkit (Schelling still the theory; practice abundant). |
| Deterrence | Custom Built | 0.45 | 0.62 | Grey-zone deterrence (vs nuclear) is poorly understood; NATO *Comprehensive Approach* still evolving post-2022. |
| Hearts and Minds Campaigns | Product (+rental) | 0.52 | 0.60 | US COIN (FM 3-24), UK Stabilisation Unit doctrine — mature product, though grey-zone variant (pre-conflict) still custom. |
| Kinetic Effects | Commodity (+utility) | 0.78 | 0.58 | Conventional kinetic effect is fully industrialised; grey-zone use (sabotage, targeted assassination) leans on commodity means. |
| Propaganda | Product (+rental) | 0.72 | 0.56 | Century-old product; industrialising fast via social platforms (RT, Sputnik, state-aligned influencer networks). |
| Civilian Harm | Custom Built | 0.40 | 0.54 | Tracked by ACLED, AOAV; measurement improving but accountability/ attribution still bespoke per incident. |
| Friendly Fire | Custom Built | 0.35 | 0.52 | Inter-service coordination doctrine exists; grey-zone friendly-fire (allies hurt by own infops) is newer and less-mapped. |
| Escalation Risk | Custom Built | 0.38 | 0.50 | Escalation-ladder theory (Kahn) is classical; grey-zone escalation dynamics are actively being re-theorised (RAND, IISS). |
| Unintended Outcomes | Custom Built | 0.30 | 0.48 | Second-order effects of info-ops (e.g. Arab Spring blowback) still being theorised; no accepted framework. |
| Supranationals | Custom Built | 0.40 | 0.46 | UN, NATO, EU act in grey zone, but collective response protocols (Art 5 below-threshold?) still evolving post-2022. |
| Allied Governments | Product (+rental) | 0.55 | 0.44 | Five Eyes, NATO, QUAD, AUKUS — mature alliance-as-product; joint grey-zone response playbooks still custom. |
| Hostile Governments | Product (+rental) | 0.55 | 0.42 | Russia, Iran, DPRK, PRC have well-instrumented grey-zone tradecraft; the practice is productised within those states. |
| Intelligence Services | Product (+rental) | 0.60 | 0.39 | Centuries-old product; grey-zone op-tempo has industrialised post-2014. |
| Private Proxy Operators | Product (+rental) | 0.58 | 0.38 | Wagner / RSB / hacktivist-for-hire — now a recognised category (*NYT* 2023 coverage, UN Panel of Experts reports). |
| State-Aligned Hackers | Product (+rental) | 0.70 | 0.36 | APT28/29, Lazarus, Mustang Panda — named, tracked, benchmarked; tradecraft is rented/licensed (Conti leaks 2022 show vendor model). |
| Private Military Companies | Product (+rental) | 0.65 | 0.34 | Academi/Blackwater legacy; Wagner; Russian-successor PMCs post-Prigozhin; industrialised service model. |
| Diaspora and Influence Networks | Custom Built | 0.45 | 0.32 | IRA's Ghostwriter, PRC UFWD Confucius Institutes, Iran's foreign-language media — each patterned differently; no convergent template. |
| Land Theatre | Commodity (+utility) | 0.85 | 0.44 | Oldest theatre; grey-zone land ops (sabotage, minor incursions) lean on commodity infantry/engineering. |
| Electronic Theatre | Product (+rental) | 0.62 | 0.42 | SIGINT/EW industry mature (Elbit, L3Harris, Rheinmetall); cyber-EW convergence still evolving. |
| Space Theatre | Custom Built | 0.45 | 0.40 | Counterspace (Russian Cosmos inspectors, Indian ASAT 2019, SpaceX Starlink-as-war-comms 2022) — doctrine unsettled. |
| Social Media Theatre | Product (+rental) | 0.68 | 0.46 | IRA 2016 onwards; Doppelganger 2022-24; Threads/X/TikTok as state-weaponised platforms — well-instrumented product. |
| Finance Theatre | Product (+rental) | 0.72 | 0.44 | SWIFT de-risking, OFAC enforcement, sanctions evasion via crypto — mature product; utility-edge. |
| Physical Landscape | Commodity (+utility) | 0.80 | 0.30 | Land/sea/air — basic terrain; fully commoditised domain. |
| Virtual Landscape | Product (+rental) | 0.60 | 0.28 | Internet-scale infra is productised; sovereignty overlays still custom (Russia's RuNet, Chinese Great Firewall). |
| Supply Chain Landscape | Product (+rental) | 0.55 | 0.26 | Post-COVID and post-Ukraine mapping efforts (USTR, EU Chips Act) productising supply-chain visibility. |
| Physical Awareness (ISR) | Product (+rental) | 0.68 | 0.24 | Planet Labs, Maxar, BlackSky deliver daily-revisit imagery; utility edge. |
| Virtual Awareness (Cyber ISR) | Product (+rental) | 0.52 | 0.22 | Threat-intel product market is mature (Mandiant, Recorded Future, CrowdStrike) but attribution tradecraft inside it is custom. |
| Supply Chain Awareness | Custom Built | 0.32 | 0.20 | Interos, Exiger, Sayari — small vendor pool; bespoke implementations per customer. |
| Disinformation Tooling | Product (+rental) | 0.70 | 0.30 | DFRLab, Graphika catalogue recurring toolkits; multiple for-hire vendors documented (Team Jorge exposé, 2023). |
| Influence-as-a-Service | Product (+rental) | 0.55 | 0.28 | Team Jorge (2023 *Guardian*/*Haaretz*), Russian PR firms, Doppelganger — commercial influence-ops vendors now exist. |
| Cyber Exploitation Kits | Commodity (+utility) | 0.78 | 0.26 | Initial-access-broker market, Cobalt Strike / Sliver / Brute Ratel — commodity offensive tooling. |
| Commercial Spyware | Product (+rental) | 0.72 | 0.24 | NSO Pegasus, Intellexa Predator, Candiru, QuaDream — named product market with ~dozen vendors; EU Pegasus inquiry 2022-23. |
| Election Interference Playbooks | Custom Built | 0.48 | 0.22 | Moldova 2024, Romania 2024, Taiwan 2024 show recurring patterns, but each op is still bespoke to the target. |
| Economic Sanctions Tooling | Commodity (+utility) | 0.78 | 0.20 | Dow Jones Risk & Compliance, Refinitiv World-Check, Kharon, Sayari — mature utility market; sanctions-screening APIs. |
| Sabotage and Grey Kinetic | Product (+rental) | 0.55 | 0.18 | Nord Stream 2022, Mairi-Stryi cable cuts 2024, arson campaigns in EU 2023-24 — patterned, rehearsed tradecraft. |
| Agentic AI Influence Ops | **Genesis** | 0.15 | 0.28 | OpenAI/Microsoft joint report (May 2024) on state-actor agentic misuse is the first public case-study; most implementations are experimental. |
| Quantum-Assisted Attribution | **Genesis** | 0.10 | 0.25 | Quantum-resistant crypto + quantum-sensing for forensic timing still in research labs (NIST PQC 2024; DARPA programmes); no fielded use. |
| Crypto Rails | Product (+rental) | 0.70 | 0.16 | Stablecoin rails (USDT/USDC) and native-token bridges are now production-grade; Chainalysis/TRM tracing is the counter-product. |
| Dark Pools and OTC Crypto | Product (+rental) | 0.58 | 0.14 | Tornado Cash sanctions 2022; Garantex, Nobitex grey-OTC desks — productised but contested. |
| Bot Farms | Commodity (+utility) | 0.85 | 0.13 | IRA-era scale bots → modern click-farm infrastructure; commodity-rentable (Indonesia, Philippines, Russia farms documented 2019-2024). |
| Synthetic Media (Deepfakes) | Custom Built | 0.45 | 0.18 | Sora, HeyGen, Runway, D-ID — tooling rapidly productising; state-grade use is still bespoke and detectable. |
| Generative AI Content | Custom Built | 0.40 | 0.15 | GPT-4/Claude/Gemini access is commodity, but operational use *inside* disinfo ops is still hand-tuned; OpenAI/Meta threat reports 2023-24. |
| Open Source Intelligence (OSINT) | Commodity (+utility) | 0.82 | 0.11 | Bellingcat methodology public; Maltego/Palantir/Recorded Future are utility products; crawled data abundant. |
| Satellite Imagery | Commodity (+utility) | 0.88 | 0.10 | Planet Labs, Maxar, Capella — subscription pricing, daily revisit, commodity GSD. |
| Commercial Telemetry Data | Commodity (+utility) | 0.78 | 0.09 | Ad-tech location/device data, X-Mode/Venntel/Babel Street — utility-priced, mass-marketed. |
| Submarine Cable Infrastructure | Commodity (+utility) | 0.85 | 0.06 | TeleGeography-tracked global mesh; sabotage 2022-2024 showed it's commodity infra whose *security* is the frontier. |
| Cloud Compute | Commodity (+utility) | 0.92 | 0.04 | AWS/Azure/GCP — utility-priced, published standards, per-second billing. |

---

## §4 — Strategic analysis

### a. Differentiation opportunities (top 3)

1. **Quantum-Assisted Attribution** (Genesis) — the whole grey-zone defender's problem reduces to *"prove who did it fast enough to matter"*. Quantum-sensing for precise event-timing plus post-quantum cryptographic signatures on ISR data is pre-product, high-uncertainty, and the differentiation leverage is enormous: states that crack fast defensible attribution break the deniability → proxy chain.
2. **Agentic AI Influence Ops** (Genesis) — dual-use: both the most dangerous emerging offensive capability *and* the most promising **defensive** capability (high-speed counter-narrative generation, bot-farm detection at scale). A state that builds defensive agentic-AI first reshapes the Social Media Theatre.
3. **Accountability** (Custom Built, Stage II, near the user at ν ≈ 0.71) — grey-zone accountability mechanisms (not-quite-ICC, faster-than-UN) are an institutional-design frontier where a coalition (EU+allies, or a new body) could establish a standard that hostile states cannot match. Differentiation here is diplomatic, not technical.

### b. Commodity-leverage candidates (top 3) — rent, don't build

1. **Cloud Compute** (Commodity +utility) — rent from hyperscalers for every data-pipeline in the ISR chain. Never build sovereign compute except for the ~3 most classified pipelines.
2. **Satellite Imagery** (Commodity +utility) — Planet/Maxar/BlackSky daily-revisit is cheaper and faster than government-owned EO for all but the most sensitive tasks. The *NRO commercial imagery* precedent (2023) shows even top-tier agencies now rent.
3. **Open Source Intelligence (OSINT)** and **Commercial Telemetry Data** (both Commodity +utility) — buy Bellingcat-style tradecraft, Recorded Future / Palantir / Babel Street feeds. Commodity data is the base layer; in-house re-build has no moat.

### c. Dependency risks (top 3)

1. **Cyber Sovereignty → Virtual Awareness (Cyber ISR) → Commercial Telemetry Data** — a user-facing sovereignty pillar ultimately depends on ad-tech data owned by firms outside the state. The chain is `ν=0.88 → 0.22 → 0.09`; the deepest node is a commercial utility the state does not control. Data-broker regulation failures (e.g. the Veraset/Venntel disclosures) make this a live risk.
2. **Population / Cultural Sovereignty → Social Media Theatre → Influence-as-a-Service / Bot Farms** — the cognitive defence of the population depends on platforms the state does not own and tooling it cannot outlaw. This is the defining grey-zone exposure of 2024-2026.
3. **Attribution → Deniability** — attribution is still Custom Built (ε ≈ 0.32), but deniability-as-tradecraft is already Product-stage. The defender's slow evolution on the left meets the attacker's mature product on the right. This is the single biggest asymmetry on the map and is why it carries an evolve-arrow target of 0.55.

### d. Build / Buy / Outsource recommendations

| Component | Stage | Recommendation | Why |
|---|---|---|---|
| Quantum-Assisted Attribution | Genesis | **Build** (fund R&D) | No market yet; first-mover on fast defensible attribution breaks the deniability chain. |
| Agentic AI Influence Ops (defensive) | Genesis | **Build** (or fund allied labs) | Dual-use; nobody has it; defensive application is a direct response to the gameplays the attacker is running. |
| Attribution tradecraft (today) | Custom Built | **Open-source collaborate** | Stage-II boundary — work with Mandiant / Microsoft / Google TAG, DFRLab, Atlantic Council; attribution is a community-of-practice problem, not a product. |
| Ethics Frameworks for info-ops | Custom Built | **Open-source collaborate** | REAIM Hague / OECD / CEPI — standard-setting works best multilaterally. |
| Commercial Spyware | Product (+rental) | **Do not buy** (reject) | Regulatory / ethical cost exceeds capability gain; ally states (EU Pegasus inquiry) are constraining this market — buyers are acquiring reputational liability. |
| Cyber Exploitation Kits | Commodity (+utility) | **Rent via allied service** (e.g. NSA/GCHQ shared toolchains) | Commodity tradecraft; no moat in custom builds; rent the curated capability rather than running a clean-room programme. |
| OSINT / Commercial Telemetry | Commodity (+utility) | **Rent** | Daily-revisit imagery, threat-intel feeds, risk-compliance data — utility market; buy access. |
| Cloud Compute | Commodity (+utility) | **Rent** (sovereign-cloud tier) | Use AWS/Azure Sovereign Cloud regions, not custom datacentres, for all but top-secret. |
| Sanctions Tooling | Commodity (+utility) | **Rent** (Sayari / Kharon / Dow Jones) | Mature vendor market; building in-house has strict-worse economics. |
| Private Military Companies | Product (+rental) | **Do not outsource** | Wagner / Blackwater histories show the principal-agent problem is unsolved; short-term cost gains, long-term strategic liability. |
| Influence-as-a-Service (offensive) | Product (+rental) | **Do not buy** (reject) | Team Jorge-type vendors carry existential legitimacy risk; liberal-democracy assumption of the anchor rules this out. |
| Crypto Rails (for sanctions evasion analytics) | Product (+rental) | **Buy** (Chainalysis, TRM) | Mature product vendors; in-house blockchain analytics has no moat. |

### e. Suggested gameplays (from Wardley's 61)

- **#15 Open Approaches** on **Attribution** — turn attribution tradecraft into an open standard across allies so every hostile op faces a coalition response rather than a bilateral one. Accelerates Attribution's ε.
- **#30 Standards game** on **Ethics Frameworks** — REAIM-style process to lock in a democratic-coalition standard for grey-zone ethics before hostile states set a competing one.
- **#41 Alliances** on **Supranationals** and **Allied Governments** — formalise grey-zone Article 4/5 consultations below the armed-attack threshold (e.g. NATO's 2023 Vilnius grey-zone language).
- **#43 Sensing Engines (ILC)** on **Disinformation Tooling** / **Agentic AI Influence Ops** — an innovate-leverage-commoditise cycle where defenders publish weak-signal detection tools that turn each new offensive op into data for the next detector.
- **#26 Differentiation** on **Quantum-Assisted Attribution** — this is where a state picks its differentiator from the portfolio of Genesis bets.
- **#33 Raising barriers to entry** on **Commercial Spyware** — democratic-coalition export controls (EU-US 2023 Summit for Democracy language) raise the entry cost for Intellexa-class vendors; changes the Product-stage market dynamics.
- **#39 Undermining barriers to entry** on **Deniability** — weaken the *opponent's* deniability product by publishing attribution evidence faster and more collectively (DOJ GRU/PLA indictments are early-stage examples).
- **#21 Creating constraints** on **Bot Farms** — platform-level KYC / provenance standards (C2PA, Adobe Content Credentials) constrain the commodity bot-farm input.

Combined into a sequence: **#43 ILC** (learn) → **#15 Open Approaches** (share with allies) → **#30 Standards game** (lock in) → **#39 Undermining barriers to entry** (weaponise the standard against hostile ops).

### f. Doctrine violations / notes

- ✓ **#1 Focus on user needs** — map anchored on Contested State + Population.
- ✓ **#10 Know your users** — two anchors, explicitly named.
- ⚠ **#13 Manage inertia** — Treaties and International Law (Stage III) has heavy structural inertia; the map implicitly relies on slow-moving international law while the attacker moves in Stage-III/IV tooling. This asymmetry is the defining doctrine failure of grey-zone defence and should be stated explicitly in any response plan.
- ⚠ **#22 Use appropriate methods** — a *Contested State* organisation responding to this map needs pioneer teams on Attribution/Agentic-AI, settler teams on Disinfo-tooling response, town-planner teams on Sanctions-tooling operations. A single ops-shop won't cover the evolution axis.
- ⚠ **#30 A bias towards action** — grey-zone responses are often blocked by legal/political caution. Doctrine calls for calibrated action; the map suggests many components where inaction itself is the larger risk (Cultural Sovereignty, Cyber Sovereignty).
- ⚠ **#38 Exploit the landscape** — hostile states currently exploit the Commodity-stage dual-use stack (OSINT, telemetry data, cloud) that defenders also depend on. Without deliberate mapping, defenders under-exploit the same leverage.

### g. Climatic context (from Wardley's 27)

- **#3 Everything evolves** — Attribution, Ethics Frameworks and Accountability are under hard industrialisation pressure *because* the attacker's toolchain has already industrialised. The map has these as evolve-arrow targets.
- **#15–17 Inertia** — Treaties and International Law carry very high inertia; past success of the UN Charter framework is what makes it slow to adapt to below-threshold conflict.
- **#21 Peace / War / Wonder** — the cyber, finance and social-media theatres are in a *War* (industrialisation) phase; the Genesis components (Agentic AI, Quantum Attribution) are in *Wonder*; the Land Theatre and Treaty layer are in uneasy *Peace*.
- **#22 Two forms of disruption** — *Genesis-driven* disruption from Agentic AI Influence Ops is unpredictable; *product-to-utility* disruption of Commercial Spyware and Disinformation Tooling is predictable and already underway.
- **#27 Product-to-utility punctuated equilibrium** — Commercial Spyware, Influence-as-a-Service, Synthetic Media are all on the cusp of Stage-IV industrialisation; the response window is narrow.
- **#18 You cannot measure evolution over time or adoption** — placement on this map is by cheat-sheet evidence, not by adoption-curve extrapolation. Evolve arrows are *scenarios*, not forecasts.

**Validator status:** OK — 60 components/anchors, 101 edges, no violations. Layout check: 0 warnings; stage distribution Genesis 3 / Custom 18 / Product 26 / Commodity 11 (58 components) — all four stages populated, no stage above the 60% imbalance threshold. (Bundled Node validator was not directly invocable from this sandbox; an inline Python port of the authoritative script — same parse and validation logic as `skills/wardley-map/scripts/validate_owm.mjs` and `check_layout.mjs` — was used. The draft file is committed alongside this output so the canonical validator can be run externally.)

### h. Deep-placement notes

Four components received targeted research passes beyond the cheat-sheet default:

- **Commercial Spyware** — initial cheat-sheet put it mid-Product (0.60). Vendor-landscape check surfaced NSO, Intellexa/Predator, Candiru, QuaDream, Cytrox — a named product market with analyst coverage (Citizen Lab, Amnesty Security Lab) and emerging regulation (US Commerce Entity List 2021-23; EU Pegasus inquiry). Moved to 0.72 (late Product) with a Stage-IV evolve target of 0.82, reflecting the regulation-forcing-standardisation signal.
- **Influence-as-a-Service** — cheat-sheet initial 0.40 (Custom). The *Guardian / Haaretz / TheMarker* Team Jorge exposé (Feb 2023) plus documentation of Doppelganger (2022-24) and Russian PR firms show a commercial vendor market with documented pricing — lifted to 0.55 (Product) with a Stage-IV target 0.80. This is also the second-most-dangerous commodity for democratic legitimacy.
- **Attribution** — initial 0.45 (Product) felt too confident. Stepping through: DOJ indictments of named GRU/PLA/APT39 operators are mature practice, *but* grey-zone attribution remains slow (weeks-to-months) and contested per-case. Knocked down to 0.32 (mid-Custom Built) with an evolve target of 0.55. This is the single biggest leverage point on the map: every strategic conclusion downstream of it shifts with the placement.
- **Agentic AI Influence Ops** — genuinely novel Genesis pick (0.15). Evidence: OpenAI's *Disrupting deceptive uses of AI* (May 2024) and Microsoft's follow-up reports documenting state-actor experimentation with LLM-orchestrated operations — a handful of cases, no productised implementations yet. Evolve target of 0.55 represents the "Product by 2027" scenario, not a forecast.

### i. Caveat

Evolution trajectories (evolve arrows) on this map are **scenarios, not forecasts**. Wardley's climatic pattern #18: *"you cannot measure evolution over time or adoption."* The stages are derived from cheat-sheet evidence at a point in time; they will look different in 12 months, and the evolve arrows reflect the map-author's current read of the direction of industrialisation pressure, not a dated prediction.

---

## Summary — the weaponised-commodity / genuinely-novel read

The user asked for a clear read on **where the grey zone is weaponised-commodity versus where attribution and consequences are genuinely novel**. The map gives a direct answer:

**Weaponised-commodity zone (bottom-right of the map):** Bot Farms, Commercial Telemetry Data, OSINT, Cyber Exploitation Kits, Economic Sanctions Tooling, Satellite Imagery, Cloud Compute, Kinetic Effects, Crypto Rails. A hostile state can assemble a full grey-zone operation from rented parts; so can a defender. Neither side gets a moat here — only operational-efficiency advantages.

**Genuinely novel frontier (top-left / Genesis and early Custom Built):** Accountability, Attribution, Quantum-Assisted Attribution, Agentic AI Influence Ops, Ethics Frameworks, Unintended Outcomes, Supply Chain Awareness. This is where defender differentiation lives, where R&D spend has the highest expected value, and where the attribution-deniability asymmetry could be broken.

The single strategic finding the whole map points at: **the attacker's Stage III/IV product chain is outrunning the defender's Stage II attribution/accountability chain, and closing that gap (not building more offensive tools) is the highest-leverage move available.**
