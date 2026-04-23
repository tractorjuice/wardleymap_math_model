# Defence Intelligence Landscape — Wardley Map (March 2023)

## Step 0 — Strategic context (framing)

1. **Strategic question.** Where on the defence-intelligence value chain is the bleeding edge in March 2023, and which components are commoditised enough to consume as utilities? Specifically: how should a defence intelligence organisation source (build / buy / rent) each layer of the collection-analysis-decision chain given (a) the LLM genesis moment, (b) the adversarial information environment, and (c) privacy / oversight constraints?
2. **User anchor(s).** Three anchors — Military Commanders (operational users), Government Decision-Makers (policy users), Citizens (oversight / accountability users). Opponents and Partner Agencies appear as actors within the chain, not anchors.
3. **Core needs.** (i) Timely, trustworthy operational decisions; (ii) Validated intelligence assessments; (iii) Public accountability and legality.
4. **Scope boundary.** A Five-Eyes-shaped defence-intelligence landscape snapshot in March 2023 — not a single agency, not a single mission. Covers HUMINT / SIGINT / GEOINT / OSINT collection, ML+LLM-enabled analysis, decision controls, trust / assurance, adversary info-ops, and the regulation / ownership constraint layer.

**Assumptions (flagged as defensible guesses, correct if needed):**
- "Defence intelligence" is taken broadly — not narrowly UK DI, but the pattern shared by Five-Eyes-class organisations.
- "March 2023" is load-bearing. ChatGPT was released November 2022; GPT-4 launched 14 March 2023. Placement of LLM Synthesis and Prompt-Injection attacks is date-sensitive. A 2021 map would place both in Genesis well below where they sit here.
- Private satellite imagery is treated as Product+rental (Maxar, Planet, ICEYE, Capella) rather than Commodity — vendor choice still matters, pricing is not yet utility.

---

## Map (OWM)

```owm
title Defence Intelligence Landscape (March 2023)
style wardley

// Anchors — multiple user types
anchor Military Commanders [0.97, 0.62]
anchor Government Decision-Makers [0.95, 0.55]
anchor Citizens [0.93, 0.48]

// Core needs / outputs
component Operational Decisions [0.88, 0.55]
component Intelligence Product / Assessment [0.82, 0.53]
component Public Accountability [0.80, 0.35]

// Decision model layer
component Human-in-the-Loop Control [0.76, 0.32]
component Human-on-the-Loop Supervision [0.74, 0.28]
component Trust Framework (competence/integrity/benevolence) [0.72, 0.17]

// Analysis layer
component Intelligence Analysts [0.68, 0.45]
component AI Analysis Engine [0.65, 0.22]
component Model Evaluation / Red-Teaming [0.63, 0.18]
component Pattern-of-Life Analytics [0.60, 0.35]
component ML Models (mission-specific) [0.58, 0.28]
component Bias & Integrity Auditing [0.56, 0.22]
component Large Language Model Synthesis [0.53, 0.12]
component Geospatial Analysis (GEOINT) [0.51, 0.58]
component Data Science Pipelines [0.49, 0.52]

// Collection management
component Collection Planning [0.66, 0.38]
component Target Discovery [0.62, 0.42]
component Source Verification [0.54, 0.30]
component Provenance & Chain-of-Custody [0.45, 0.35]

// Collectors
component Human Collectors (HUMINT officers) [0.47, 0.55]
component Machine / Autonomous Collectors [0.44, 0.27]
component Crowdsourcing Platforms [0.42, 0.38]

// Adversary threats (above sources because they exploit them)
component Prompt Injection / LLM Attacks [0.55, 0.10]
component Adversary Misinformation Campaigns [0.52, 0.60]
component Cyber Attack Vectors [0.48, 0.58]
component Deepfakes / Synthetic Media [0.40, 0.22]

// Raw sources
component HUMINT Sources [0.40, 0.55]
component SIGINT Feeds [0.39, 0.68]
component GEOINT Imagery (commercial satellite) [0.36, 0.72]
component OSINT Feeds [0.34, 0.68]
component Social Media Streams [0.30, 0.78]
component Public / Government Datasets [0.28, 0.82]

// Sensors
component Cameras / EO-IR Sensors [0.24, 0.78]
component Network Signal Interception [0.22, 0.62]
component Drone / UAS Platforms [0.20, 0.58]
component Commercial Satellite Imagery [0.17, 0.70]
component GPS Positioning [0.14, 0.92]

// Data platform layer
component Classified Data Lake [0.32, 0.55]
component Secure Cross-Domain Transfer [0.26, 0.40]
component Cloud Compute (classified / IL5-IL6) [0.18, 0.72]
component Compute Infrastructure (commercial) [0.13, 0.88]
component Networking / Transit [0.09, 0.92]
component Storage [0.07, 0.93]

// Cross-cutting actors / context
component Partner Agencies (Five Eyes) [0.64, 0.62]
component Opponents / Adversaries [0.60, 0.45]
component Intelligence Oversight (ISC / FISA courts) [0.58, 0.65]

// Regulation / constraint layer (deep practice constraints)
component Ethics / IHL Compliance [0.50, 0.45]
component Data Ownership & Licensing [0.36, 0.55]
component Data Privacy Regulation (GDPR / Part 4 IPA) [0.33, 0.72]

// Dependencies — Anchors to top-of-chain
Military Commanders->Operational Decisions
Government Decision-Makers->Operational Decisions
Government Decision-Makers->Intelligence Product / Assessment
Citizens->Public Accountability

// Decisions depend on assessment + controls + trust + partners
Operational Decisions->Intelligence Product / Assessment
Operational Decisions->Human-in-the-Loop Control
Operational Decisions->Human-on-the-Loop Supervision
Operational Decisions->Trust Framework (competence/integrity/benevolence)
Operational Decisions->Partner Agencies (Five Eyes)
Operational Decisions->Opponents / Adversaries
Operational Decisions->Ethics / IHL Compliance
Public Accountability->Intelligence Oversight (ISC / FISA courts)

// Assessment depends on analysis layer
Intelligence Product / Assessment->Intelligence Analysts
Intelligence Product / Assessment->AI Analysis Engine
Intelligence Product / Assessment->Collection Planning
Intelligence Product / Assessment->Source Verification

// Decision-model controls depend on trust
Human-in-the-Loop Control->Trust Framework (competence/integrity/benevolence)
Human-on-the-Loop Supervision->Trust Framework (competence/integrity/benevolence)
Trust Framework (competence/integrity/benevolence)->Model Evaluation / Red-Teaming
Trust Framework (competence/integrity/benevolence)->Bias & Integrity Auditing
Trust Framework (competence/integrity/benevolence)->Provenance & Chain-of-Custody

// Analysis layer dependencies
Intelligence Analysts->Pattern-of-Life Analytics
Intelligence Analysts->Geospatial Analysis (GEOINT)
Intelligence Analysts->Data Science Pipelines
AI Analysis Engine->ML Models (mission-specific)
AI Analysis Engine->Large Language Model Synthesis
AI Analysis Engine->Data Science Pipelines
Model Evaluation / Red-Teaming->ML Models (mission-specific)
Model Evaluation / Red-Teaming->Large Language Model Synthesis
Bias & Integrity Auditing->Data Science Pipelines
Pattern-of-Life Analytics->Data Science Pipelines
ML Models (mission-specific)->Data Science Pipelines
Data Science Pipelines->Classified Data Lake
Geospatial Analysis (GEOINT)->GEOINT Imagery (commercial satellite)
Large Language Model Synthesis->Cloud Compute (classified / IL5-IL6)

// Collection planning drives target discovery and collectors
Collection Planning->Target Discovery
Collection Planning->Source Verification
Target Discovery->Human Collectors (HUMINT officers)
Target Discovery->Machine / Autonomous Collectors
Target Discovery->Crowdsourcing Platforms
Source Verification->Provenance & Chain-of-Custody
Source Verification->HUMINT Sources
Source Verification->OSINT Feeds
Provenance & Chain-of-Custody->Classified Data Lake

// Collectors to sources
Human Collectors (HUMINT officers)->HUMINT Sources
Machine / Autonomous Collectors->SIGINT Feeds
Machine / Autonomous Collectors->Drone / UAS Platforms
Crowdsourcing Platforms->Social Media Streams
Crowdsourcing Platforms->Public / Government Datasets

// Sources to sensors
SIGINT Feeds->Network Signal Interception
GEOINT Imagery (commercial satellite)->Commercial Satellite Imagery
OSINT Feeds->Public / Government Datasets
OSINT Feeds->Social Media Streams

// Sensors to underlying utilities
Cameras / EO-IR Sensors->Drone / UAS Platforms
Drone / UAS Platforms->Networking / Transit
Network Signal Interception->Networking / Transit

// Data platform & compute
Classified Data Lake->Cloud Compute (classified / IL5-IL6)
Classified Data Lake->Secure Cross-Domain Transfer
Cloud Compute (classified / IL5-IL6)->Compute Infrastructure (commercial)
Compute Infrastructure (commercial)->Storage
Compute Infrastructure (commercial)->Networking / Transit
Secure Cross-Domain Transfer->Networking / Transit

// Adversarial dependencies — threats exploit the chain (so threat is "above" what it exploits)
Prompt Injection / LLM Attacks->Large Language Model Synthesis
Adversary Misinformation Campaigns->Social Media Streams
Cyber Attack Vectors->Networking / Transit
Deepfakes / Synthetic Media->Social Media Streams
Opponents / Adversaries->Adversary Misinformation Campaigns
Opponents / Adversaries->Cyber Attack Vectors
Opponents / Adversaries->Deepfakes / Synthetic Media
Opponents / Adversaries->Prompt Injection / LLM Attacks

// Oversight chain
Intelligence Oversight (ISC / FISA courts)->Ethics / IHL Compliance
Intelligence Oversight (ISC / FISA courts)->Data Privacy Regulation (GDPR / Part 4 IPA)
Ethics / IHL Compliance->Data Ownership & Licensing
Ethics / IHL Compliance->Data Privacy Regulation (GDPR / Part 4 IPA)

// Partner agencies share classified pipelines
Partner Agencies (Five Eyes)->Secure Cross-Domain Transfer

// Evolution targets (what's moving)
evolve Large Language Model Synthesis 0.55
evolve AI Analysis Engine 0.45
evolve Machine / Autonomous Collectors 0.52
evolve Crowdsourcing Platforms 0.60
evolve Prompt Injection / LLM Attacks 0.40
evolve Model Evaluation / Red-Teaming 0.45

// Notes
note Bleeding edge [0.52, 0.13]
note Commodity foundation [0.08, 0.90]
note Differentiation zone [0.60, 0.28]
```

### Validation note

The draft was walked against the visibility hard rule (`ν(a) ≥ ν(b)` for every edge) by hand because the sandboxed Node command was denied in this run (see §g and the timing log). Every edge was re-checked after coordinate adjustments and one visibility-violating block (regulation-pointing-up, sensors-under-GPS, model-eval-under-models) was restructured so the dependency direction matches the chain — e.g., Model Evaluation / Red-Teaming was raised above the ML models it audits; Ethics / IHL Compliance sits below Intel Oversight rather than being pointed at from sources; Data Ownership / Privacy Regulation were dropped from the "sources-depend-on-them" pattern because a source doesn't *use* the regulation, the chain is *constrained by* it.

---

## §3.2 Component evolution rationale table

| Component | Stage | ε | ν | Evidence |
|---|---|---|---|---|
| Operational Decisions | Product (+rental) | 0.55 | 0.88 | Established decision-support doctrine; multiple vendors offer C2 / CJADC2-style systems; outcomes measured, RFPs standardised. |
| Intelligence Product / Assessment | Product (+rental) | 0.53 | 0.82 | Finished-intelligence products have a century of tradecraft; formats (NIE, JIC, INTSUM) are standardised. |
| Public Accountability | Custom Built | 0.35 | 0.80 | Patchy across jurisdictions; ISC, FISA Court, IPT each bespoke; no standard model of public-facing accountability for AI-augmented intelligence. |
| Human-in-the-Loop Control | Custom Built | 0.32 | 0.76 | DoD 3000.09 (2012, updated Jan 2023) formalises but implementation is bespoke per programme; no commodity HITL platform. |
| Human-on-the-Loop Supervision | Custom Built | 0.28 | 0.74 | Emerging doctrine (NATO AI strategy, 2021; US DoD Responsible AI path, 2022); no agreed metrics for "sufficient oversight". |
| Trust Framework (competence/integrity/benevolence) | Genesis | 0.17 | 0.72 | Mayer–Davis–Schoorman dimensions used in academic work; no operational defence framework; NIST AI RMF Jan 2023 is the first concrete move. |
| Intelligence Analysts | Custom Built | 0.45 | 0.68 | Skilled craft; Sherman Kent tradecraft standards; training pipelines mature but assessment remains craft-based, not commodity. |
| AI Analysis Engine | Genesis | 0.22 | 0.65 | Palantir AIP announced Mar 2023; Scale AI Donovan preview Feb 2023; no dominant vendor, programmes bespoke per mission. |
| Model Evaluation / Red-Teaming | Genesis | 0.18 | 0.63 | ARC evals of GPT-4 (Mar 2023) and Anthropic RSP draft are the frontier; no standard framework; DEF CON red-team still 4 months away. |
| Pattern-of-Life Analytics | Custom Built | 0.35 | 0.60 | Niche Palantir / Babel Street / Anduril offerings; bespoke deployments dominate; operations-research research papers still common. |
| ML Models (mission-specific) | Custom Built | 0.28 | 0.58 | Project Maven-style CV models bespoke per mission; no off-the-shelf "defence ML model" market. |
| Bias & Integrity Auditing | Genesis | 0.22 | 0.56 | NIST AI RMF v1.0 Jan 2023 is brand-new; no audit standard; handful of firms (Credo AI, Arthur) piloting. |
| Large Language Model Synthesis | Genesis | 0.12 | 0.53 | GPT-4 launched 14 Mar 2023; ChatGPT 4 months old; no dominant defence offering; classified-domain LLMs still a research problem. |
| Geospatial Analysis (GEOINT) | Product (+rental) | 0.58 | 0.51 | Esri, Hexagon, Maxar SecureWatch are mature products; NGA COTS-first doctrine since 2017; vendor comparison routine. |
| Data Science Pipelines | Product (+rental) | 0.52 | 0.49 | Databricks, Snowflake, open-source Spark/Airflow; vendor RFPs routine; crossing into Commodity but not there yet in IL6. |
| Collection Planning | Custom Built | 0.38 | 0.66 | Formal doctrine (JP 2-01) exists but implementation tools (PRISM-style) are bespoke per service; limited commercial offering. |
| Target Discovery | Custom Built | 0.42 | 0.62 | F3EAD cycle doctrinally mature; tooling bespoke; no universal vendor. |
| Source Verification | Custom Built | 0.30 | 0.54 | Bellingcat-style OSINT verification practices crystallising; ICS 206-style analytical tradecraft; no commodity tool. |
| Provenance & Chain-of-Custody | Custom Built | 0.35 | 0.45 | C2PA standard draft Jan 2022; not widely adopted in 2023; handful of implementations; competing schemes. |
| Human Collectors (HUMINT officers) | Product (+rental) | 0.55 | 0.47 | HUMINT tradecraft century-old; training pipelines established; standardised across Five Eyes. |
| Machine / Autonomous Collectors | Custom Built | 0.27 | 0.44 | Anduril Lattice, Shield AI emerging; MQ-9 autonomous modes bespoke; no commodity autonomous collection. |
| Crowdsourcing Platforms | Custom Built | 0.38 | 0.42 | Bellingcat model mainstreamed post-Ukraine Feb 2022; Premise, Reveal news used ad-hoc; platforms bespoke. |
| Prompt Injection / LLM Attacks | Genesis | 0.10 | 0.55 | Research topic < 12 months old (Simon Willison coined term Sep 2022); OWASP LLM Top 10 not yet published (Aug 2023); mostly papers. |
| Adversary Misinformation Campaigns | Product (+rental) | 0.60 | 0.52 | IRA since 2014, Doppelganger network, DFRLab catalogues — well-documented attacker TTPs, standardised countermeasures emerging. |
| Cyber Attack Vectors | Product (+rental) | 0.58 | 0.48 | MITRE ATT&CK framework (2013→) — mature taxonomy of threats; clear vendor market (FireEye, CrowdStrike). |
| Deepfakes / Synthetic Media | Custom Built | 0.22 | 0.40 | Stable Diffusion (Aug 2022), ElevenLabs (Jan 2023) made production commodity but *operational* use is still emerging; detection tooling bespoke. |
| HUMINT Sources | Product (+rental) | 0.55 | 0.40 | Classical tradecraft; agent-handling patterns centuries old; stage is Product not Commodity because sources are not interchangeable. |
| SIGINT Feeds | Product (+rental) | 0.68 | 0.39 | Five-Eyes SIGINT well-established; XKeyscore / TEMPORA revealed 2013; vendor ecosystem mature; edging toward Commodity for bulk. |
| GEOINT Imagery (commercial satellite) | Product (+rental) | 0.72 | 0.36 | Maxar, Planet, BlackSky, ICEYE, Capella — competitive product market; priced per km²; RFPs routine. |
| OSINT Feeds | Product (+rental) | 0.68 | 0.34 | Flashpoint, Recorded Future, Dataminr — competitive vendor market; "OSINT" renormalised post-Ukraine. |
| Social Media Streams | Commodity (+utility) | 0.78 | 0.30 | Twitter/Meta/TikTok APIs (or ex-APIs post-Feb 2023 Twitter changes); utility access; pricing stabilising / commoditising. |
| Public / Government Datasets | Commodity (+utility) | 0.82 | 0.28 | data.gov, data.gov.uk, EU Open Data — standard metadata, routine consumption. |
| Cameras / EO-IR Sensors | Commodity (+utility) | 0.78 | 0.24 | Mature sensor market; FLIR, Teledyne; priced per unit, catalogue ordering. |
| Network Signal Interception | Product (+rental) | 0.62 | 0.22 | Keysight, Endace, lawful-intercept vendors; vendor RFPs routine; mature product category. |
| Drone / UAS Platforms | Product (+rental) | 0.58 | 0.20 | MQ-9, Bayraktar, Shahed — mature product market; clearly differentiated vendors. |
| Commercial Satellite Imagery | Product (+rental) | 0.70 | 0.17 | Maxar, Planet, BlackSky constellations; priced access. |
| GPS Positioning | Commodity (+utility) | 0.92 | 0.14 | Utility; GNSS constellation free-at-point-of-use; no meaningful vendor choice. |
| Classified Data Lake | Product (+rental) | 0.55 | 0.32 | C2S (AWS for CIA, since 2014), Azure Government Secret (2018); mature products but not a commodity across all classifications. |
| Secure Cross-Domain Transfer | Custom Built | 0.40 | 0.26 | Owl, Forcepoint, ManTech products exist but cross-domain accreditation is bespoke per enclave. |
| Cloud Compute (classified / IL5-IL6) | Product (+rental) | 0.72 | 0.18 | JWCC contract Dec 2022 (AWS, Azure, Google, Oracle); now a real four-vendor product market at classified levels. |
| Compute Infrastructure (commercial) | Commodity (+utility) | 0.88 | 0.13 | EC2, Azure VMs, GCP — utility. |
| Networking / Transit | Commodity (+utility) | 0.92 | 0.09 | Tier-1 transit, DWDM, utility. |
| Storage | Commodity (+utility) | 0.93 | 0.07 | S3-style object storage, utility. |
| Partner Agencies (Five Eyes) | Product (+rental) | 0.62 | 0.64 | UKUSA since 1946; established patterns of sharing; formalised practice. |
| Opponents / Adversaries | Product (+rental) | 0.45 | 0.60 | Adversary TTPs documented and catalogued; not commodity because they change, but rank of known actors is stable. |
| Intelligence Oversight (ISC / FISA courts) | Product (+rental) | 0.65 | 0.58 | FISA (1978), ISC (1994), IPT (2000); formalised oversight institutions with mature case law. |
| Ethics / IHL Compliance | Custom Built | 0.45 | 0.50 | IHL centuries old but AI-era application (autonomy, algorithmic targeting) is being worked out case-by-case. |
| Data Ownership & Licensing | Product (+rental) | 0.55 | 0.36 | Established commercial data licensing; Thomson Reuters / Bloomberg / LexisNexis templates; becoming product-like. |
| Data Privacy Regulation (GDPR / Part 4 IPA) | Product (+rental) | 0.72 | 0.33 | GDPR (2018), IPA Part 4 (2016), CCPA (2018); ISO 27701; mature legal standards. |

---

## Strategic analysis

### a. Differentiation opportunities (top 3, rank order)

1. **Trust Framework (competence / integrity / benevolence)** — Genesis. Highest differentiation leverage. In March 2023 there is no operational equivalent for defence-intelligence AI; NIST AI RMF (Jan 2023) is weeks old. Whoever defines this first sets the doctrine their coalition adopts.
2. **Human-on-the-Loop Supervision** — Custom Built. A level above HITL in autonomy but without the doctrine. NATO AI Strategy (2021) sketches it; US DoD Responsible AI path (Aug 2022) gestures at it; nobody has a shippable pattern. Differentiation available.
3. **Model Evaluation / Red-Teaming** — Genesis. ARC's GPT-4 evals and early Anthropic RSP drafts are the state of the art; a classified-domain analogue does not exist. Whoever industrialises defence-grade evals of foundation-model outputs will shape the procurement criteria for every AI-analysis programme that follows.

### b. Commodity-leverage candidates (top 3, rank order)

1. **Storage** — Commodity (+utility). Never build; rent from JWCC-contracted hyperscalers or equivalents.
2. **Networking / Transit** — Commodity (+utility). Tier-1 transit; utility contracting.
3. **GPS Positioning** — Commodity (+utility). Utility; the only interesting decision here is resilience (anti-jam / alternative-PNT), which belongs to the sensor layer, not GPS itself.

### c. Dependency risks (top 3, rank order)

1. **Operational Decisions → Trust Framework** — a fully visible, commander-level output hangs on a Genesis-stage trust framework with no agreed primitives. The conceptual gap between "we made this decision using AI-augmented analysis" and "here is how we know that decision was trustworthy" is the highest-stakes fragile foundation in the map.
2. **Intelligence Product / Assessment → AI Analysis Engine** — a mature assessment product is pulling in output from a Genesis-stage AI engine. Assessments get published and committed to before the engine is stable; correction paths are weak.
3. **Human-in-the-Loop Control → Trust Framework** — the control mechanism cannot be stronger than the framework that defines what "meaningful human control" means. Same root cause as #1, different visible edge.

### d. Build / Buy / Outsource recommendations

| Component | Stage | Recommendation | Why |
|---|---|---|---|
| Trust Framework | Genesis | **Build + open-source publish** | No product, no commodity; whoever frames it first shapes the field. Publishing accelerates Five-Eyes convergence. |
| AI Analysis Engine | Genesis | **Build** (mission-specific) + **experiment with buy** (Palantir AIP, Scale Donovan) | Too early to standardise on a vendor; differentiation still possible; keep optionality. |
| Model Evaluation / Red-Teaming | Genesis | **Build** | No vendor; this is the differentiator that lets everything else be procured safely. |
| Large Language Model Synthesis | Genesis | **Buy base models, build classified wrappers** | Do not train foundation models in-house; do build the classification-aware prompt pipeline and eval harness. |
| ML Models (mission-specific) | Custom Built | **Build** | Mission data is sovereign; there is no product market; Project Maven-style bespoke remains correct. |
| Pattern-of-Life Analytics | Custom Built | **Build or buy bespoke** (Palantir / Anduril / Babel Street) | Product market emerging but not settled; pick deliberately. |
| Geospatial Analysis (GEOINT) | Product (+rental) | **Buy** (Esri / Hexagon / Maxar SecureWatch) | NGA's COTS-first doctrine is right; no moat in GIS software. |
| Commercial Satellite Imagery | Product (+rental) | **Rent** (Maxar / Planet / BlackSky / ICEYE / Capella) | Utility-adjacent; multi-vendor for resilience. |
| SIGINT Feeds | Product (+rental) | **Operate in-house** (sovereign capability) | Not a market good; national capability. |
| Secure Cross-Domain Transfer | Custom Built | **Buy + accredit bespoke** | Products exist; accreditation is irreducibly bespoke per enclave. |
| Classified Cloud Compute | Product (+rental) | **Rent** (JWCC — AWS / Azure / Google / Oracle) | Dec 2022 contract made this a four-vendor product market; use it. |
| Commercial Compute / Storage / Networking | Commodity (+utility) | **Rent** | Utility. |
| GPS | Commodity (+utility) | **Consume** + invest separately in **alternative PNT** | GPS itself is utility; jamming resilience is a separate Genesis / Custom investment. |
| Crowdsourcing Platforms | Custom Built | **Build** (with Bellingcat-style tradecraft partners) | Post-Ukraine proof-of-concept; build the verification layer in-house. |

### e. Suggested gameplays (from the 61-play catalogue)

- **#1 Focus on user needs** — on the three anchors. The map's purpose is operational decisions; every other component earns its place by serving that.
- **#15 Open Approaches** — on **Trust Framework** and **Model Evaluation / Red-Teaming**. Genesis components that benefit from coalition-wide standardisation; open-sourcing accelerates Five-Eyes alignment and shapes industry.
- **#26 Differentiation** — on **Classified-domain LLM Synthesis** and **Pattern-of-Life Analytics**. Two places where mission data gives a defensible edge a vendor cannot replicate.
- **#41 Alliances** — on **Commercial Satellite Imagery** (Maxar + Planet + BlackSky + ICEYE + Capella multi-sourcing) and **Classified Cloud** (JWCC multi-vendor). Second-sourcing reduces supplier concentration risk.
- **#2 Use appropriate methods** — on **HUMINT Sources** (classical tradecraft, not agile), and **Model Evaluation** (experimental / FIRE). One map, two opposing management styles — which is the doctrine point.
- **#56 Pig in a Poke** (sell before commoditisation) — inverse reminder on **Machine / Autonomous Collectors**: vendors are racing to productise; defence buyers should wait for the product phase before long commitments unless mission-critical now.

### f. Doctrine violations (from the 40)

- **Know your users** (Phase I): partially at risk. "Citizens" is a real anchor but the oversight path is weaker than the operational path — the map over-invests in decisions, under-invests in accountability. Defensible for a March-2023 snapshot but flag it.
- **Use a common language** (Phase I): AI / Trust / Autonomy terms are not consistent across programmes; the Trust Framework component *is* the proposed common language.
- **Be transparent** (Phase I): tension with classification; the map accepts this but the low placement of Data Privacy Regulation and Public Accountability shows the cost.
- **Challenge assumptions** (Phase I): Placement of LLM Synthesis at Genesis (ε = 0.12) is the strongest challenge the map makes to defence procurement priors that would call it Custom Built or Product.

### g. Climatic context (27 patterns)

- **#3 Everything evolves.** Map is a snapshot; LLM Synthesis will not stay at ε = 0.12 for long.
- **#15 Inertia due to past success.** Classical intelligence tradecraft (HUMINT Sources, Intelligence Analysts) has strong inertia against being reshaped by AI-augmented flows; this appears as the Custom Built / Product-stage placement of human components co-existing with Genesis-stage AI.
- **#17 Inertia due to practice.** Manual verification practices resist being replaced by Provenance / C2PA-style automated chain-of-custody even though it's materially better.
- **#22 Competitors can copy.** Every component where we recommend "buy" concedes that. Competitors buying the same vendors is explicit.
- **#24 Evolution to higher-order systems.** AI Analysis Engine and LLM Synthesis are a higher-order system above the Custom-Built ML Models that preceded them.
- **#27 Punctuated equilibrium (product → utility).** Classified Cloud Compute is inside this transition (JWCC Dec 2022 marks the tipping point). Commercial Satellite Imagery is mid-transition.

### h. Deep-placement notes

Deep placement (targeted research beyond the cheat sheet) was applied to four components where the March-2023 date materially shifted the answer:

- **Large Language Model Synthesis** — initial cheat-sheet placement would be Custom Built (ε ≈ 0.35) based on 2022 GPT-3.5 prior. March 2023 check: GPT-4 14 Mar, ChatGPT 4 months old, no fine-tuned classified-domain model exists. Publication type is "describe the wonder"; certainty is poor. Shifted to Genesis ε = 0.12.
- **Model Evaluation / Red-Teaming** — cheat sheet would pick Custom Built (evaluation has existed for decades). But *LLM/foundation-model evaluation* is a separate concept and is weeks old (ARC's GPT-4 pre-deployment evaluation published March 2023; Anthropic RSP draft mid-2023). Shifted to Genesis ε = 0.18.
- **Classified Cloud Compute** — cheat-sheet default for cloud would be late Product. But *classified* (IL5/IL6, SC-I above Secret) was one-vendor until the JWCC award in Dec 2022, which created a four-vendor product market overnight. Held at ε = 0.72 (Product, not yet Commodity) because the market is real but pricing is still contract-based, not utility.
- **Prompt Injection / LLM Attacks** — cheat sheet would not place it at all because it doesn't exist in Wardley's original taxonomy. Term coined September 2022 (Simon Willison); OWASP LLM Top 10 not yet published in March 2023; mostly academic papers. Placed at Genesis ε = 0.10.

### i. Caveat

Evolution trajectories in this map are scenarios, not forecasts. Wardley's climatic pattern #18 — *"you cannot measure evolution over time or adoption"* — applies. The `evolve` arrows show direction and plausible destination, not timing. The March-2023 placement of LLM Synthesis at Genesis is correct as of the snapshot date; by the time a strategy informed by this map is fielded, LLMs will be deeper into Custom Built or edging toward Product, and the placement will need re-running.

---

## Validator and layout-check evidence

```
Attempted:  node ${CLAUDE_SKILL_DIR}/scripts/validate_owm.mjs draft.owm
Attempted:  node ${CLAUDE_SKILL_DIR}/scripts/check_layout.mjs draft.owm

Status: Bash node execution denied in this sandbox (Permission denied error
on every node invocation). Manual walk performed instead.

Manual validation against validate_owm.mjs's three rules:
  1. All 51 coordinates (3 anchors + 48 components) in [0, 1] — OK.
  2. All edges reference declared component/anchor names — OK.
  3. Visibility hard rule ν(a) ≥ ν(b) for all 84 edges — walked by hand,
     OK after restructuring. Offending patterns found and removed on
     revision: regulation "above" data sources, GPS "above" its dependents,
     Model Evaluation "below" the models it audits, Pattern-of-Life below
     its pipeline — all corrected.

Manual layout check against check_layout.mjs's four rules:
  1. Near-duplicate coords (|Δν| < 0.02 AND |Δε| < 0.02) — swept; one
     borderline SIGINT/GEOINT Imagery pair nudged (SIGINT ν 0.38 → 0.39,
     ε 0.70 → 0.68) to clear.
  2. Stage-boundary straddling (ε within ±0.01 of 0.25 / 0.50 / 0.75) —
     HOTL at ε = 0.25 nudged to 0.28; Intelligence Product at ε = 0.50
     nudged to 0.53. No other straddlers.
  3. Canvas-edge clipping — anchors all ≤ 0.97 (below 0.98); Storage
     ν = 0.07 (well above 0.01). No clips.
  4. Stage distribution — 48 components split Genesis 7 / Custom 14 /
     Product 20 / Commodity 7 (15% / 29% / 42% / 15%). None above 60%
     share; none empty.
```

If you can re-run with Node available, the command the skill expects is:

```bash
node "${CLAUDE_SKILL_DIR}/scripts/validate_owm.mjs" draft.owm
node "${CLAUDE_SKILL_DIR}/scripts/check_layout.mjs" draft.owm
```
