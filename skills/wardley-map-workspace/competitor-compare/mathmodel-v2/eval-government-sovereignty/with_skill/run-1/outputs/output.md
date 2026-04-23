# National Sovereignty — Government's Point of View (April 2023)

## Step 0 — Strategic context

1. **Strategic question.** *Where is sovereignty already industrialised infrastructure the government can treat as a utility, and where is it still contested and fragile — and therefore where must the government build/defend rather than procure?* The map is for a government-level strategist deciding how to allocate attention and capability across six pillars, four theatres, an awareness apparatus, a capability layer, a norms/legitimacy loop, and a media mix.
2. **User anchor(s).** Four anchors, in deliberate tension with each other: **Supranational Layer**, **Government**, **Corporations & Shareholders**, **Society**. Sovereignty is the outcome they each consume — and contest. Government cannot model sovereignty as a single-user chain; the pillars are pulled in different directions by each anchor.
3. **Core needs.** (a) Territorial and security integrity. (b) Economic and digital independence. (c) Legitimacy (election-legitimacy + public belonging + perception of success). (d) Crisis-response capacity. These four sit roughly at ν ≈ 0.85–0.88 on the map as the pillars and legitimacy layer.
4. **Scope boundary.** National sovereignty from the point of view of a single Western-style liberal democracy in April 2023 (post-Ukraine-invasion, mid-TSMC/CHIPS realignment, pre-AI-Act). Excludes: internal party politics, specific doctrines (NATO, CPTPP, etc. are implicit in International Law). Includes: the supranational context because the scenario names it as an anchor.

### Assumptions

- **Jurisdiction:** treated as "a G7 liberal democracy" — specific thresholds (e.g., election legitimacy, electoral registers) vary country-by-country. Correct me if you have a specific country in mind (US/UK/France/Germany/Japan read differently on several pillars, especially Cultural and Election Legitimacy).
- **Time-stamp:** April 2023. Cyber capability is placed pre-ChatGPT-era-stabilisation; digital sovereignty is placed before the EU AI Act became concrete. Both move right over the following 18 months.
- **Corporations & Shareholders as an anchor:** modelled as a legitimate user of sovereignty outputs (they consume Economic Sovereignty, rely on Digital Sovereignty and Supply-Chain integrity). This is a deliberate choice — without it, the map under-weights commercial pressure on sovereignty design.
- **"Pillar" vs "theatre":** pillars are the *objectives* of sovereignty (territorial, economic, political, digital, cultural, security). Theatres are *where contests play out* (land, supply chain, cyber, CNI). Same sovereignty outcome, different physical/informational battlefield.

---

## Map (OWM)

```owm
title National Sovereignty — Government's Point of View (April 2023)
style wardley

// Anchors (user-need set U)
anchor Supranational Layer [0.96, 0.46]
anchor Government [0.97, 0.40]
anchor Corporations & Shareholders [0.95, 0.58]
anchor Society [0.96, 0.30]

// Pillars of sovereignty (visible user-facing outcomes)
component Territorial Sovereignty [0.88, 0.42]
component Economic Sovereignty [0.86, 0.48]
component Political Sovereignty [0.87, 0.36]
component Digital Sovereignty [0.85, 0.28]
component Cultural Sovereignty [0.84, 0.22]
component Security Sovereignty [0.88, 0.55]

// Legitimacy layer (feedback loop outputs of the pillars)
component Election Legitimacy [0.78, 0.33]
component Perception of Success [0.80, 0.20]
component Public Belonging [0.79, 0.24]

// Social norms feeding legitimacy
component Integrity [0.70, 0.30]
component Benevolence [0.69, 0.28]
component Fairness [0.71, 0.34]
component Competency [0.72, 0.42]
component Identity [0.68, 0.20]

// Theatres where sovereignty plays out
component Land Theatre [0.62, 0.78]
component Supply-Chain Theatre [0.60, 0.54]
component Cyber Theatre [0.58, 0.32]
component CNI Theatre [0.63, 0.66]

// Crisis response and international legal frame
component Crisis Response [0.66, 0.46]
component International Law [0.64, 0.70]
component Domestic Laws [0.65, 0.76]

// Media mix
component Mainstream Media [0.56, 0.72]
component Social Media [0.55, 0.80]
component Education [0.54, 0.62]
component Art [0.53, 0.47]
component Propaganda [0.52, 0.34]

// Awareness apparatus
component Territorial Awareness [0.46, 0.52]
component Supply-Chain Awareness [0.44, 0.38]
component Digital-Chain Awareness [0.42, 0.22]

// Capability layer
component Military Capability [0.40, 0.74]
component Intelligence Capability [0.34, 0.48]
component Diplomatic Capability [0.35, 0.82]
component Cyber Capability [0.33, 0.36]
component Industrial Capability [0.37, 0.58]
component Regulatory Capability [0.38, 0.66]

// Deep infrastructure
component Critical National Infrastructure [0.22, 0.70]
component Telecoms Backbone [0.18, 0.86]
component Semiconductor Supply [0.16, 0.42]
component Energy Supply [0.15, 0.82]
component Food Supply [0.21, 0.80]
component Finance Rails [0.19, 0.88]
component Data Centres [0.17, 0.82]
component Cloud Compute [0.14, 0.90]
component Undersea Cables [0.12, 0.88]
component Satellites & GNSS [0.13, 0.78]

// Border / territory atomic layer
component Borders & Territory [0.24, 0.92]
component Population Register [0.26, 0.80]

// Dependencies — anchors consume pillars
Supranational Layer->Political Sovereignty
Supranational Layer->Economic Sovereignty
Supranational Layer->International Law
Government->Territorial Sovereignty
Government->Political Sovereignty
Government->Security Sovereignty
Government->Economic Sovereignty
Government->Digital Sovereignty
Government->Election Legitimacy
Corporations & Shareholders->Economic Sovereignty
Corporations & Shareholders->Digital Sovereignty
Corporations & Shareholders->Supply-Chain Theatre
Society->Cultural Sovereignty
Society->Political Sovereignty
Society->Public Belonging
Society->Perception of Success
Society->Election Legitimacy

// Pillars to theatres
Territorial Sovereignty->Land Theatre
Territorial Sovereignty->CNI Theatre
Economic Sovereignty->Supply-Chain Theatre
Economic Sovereignty->CNI Theatre
Political Sovereignty->Domestic Laws
Political Sovereignty->International Law
Digital Sovereignty->Cyber Theatre
Digital Sovereignty->CNI Theatre
Cultural Sovereignty->Education
Cultural Sovereignty->Art
Security Sovereignty->Land Theatre
Security Sovereignty->Cyber Theatre
Security Sovereignty->CNI Theatre

// Legitimacy feedback loop
Election Legitimacy->Integrity
Election Legitimacy->Fairness
Election Legitimacy->Competency
Election Legitimacy->Identity
Perception of Success->Competency
Perception of Success->Mainstream Media
Perception of Success->Social Media
Public Belonging->Identity
Public Belonging->Benevolence
Public Belonging->Education
Public Belonging->Art

// Norms depend on media
Integrity->Mainstream Media
Benevolence->Social Media
Fairness->Mainstream Media
Competency->Mainstream Media
Identity->Education

// Crisis response and law
Crisis Response->Military Capability
Crisis Response->Diplomatic Capability
Crisis Response->Intelligence Capability
Crisis Response->CNI Theatre
International Law->Diplomatic Capability
Domestic Laws->Regulatory Capability

// Media depends on awareness
Mainstream Media->Territorial Awareness
Mainstream Media->Propaganda
Social Media->Digital-Chain Awareness
Social Media->Cloud Compute
Education->Population Register
Propaganda->Intelligence Capability

// Theatres rely on awareness + capability
Land Theatre->Territorial Awareness
Land Theatre->Military Capability
Land Theatre->Borders & Territory
Supply-Chain Theatre->Supply-Chain Awareness
Supply-Chain Theatre->Industrial Capability
Supply-Chain Theatre->Semiconductor Supply
Supply-Chain Theatre->Food Supply
Cyber Theatre->Digital-Chain Awareness
Cyber Theatre->Cyber Capability
Cyber Theatre->Telecoms Backbone
CNI Theatre->Critical National Infrastructure
CNI Theatre->Regulatory Capability

// Awareness rests on intel + infra
Territorial Awareness->Intelligence Capability
Territorial Awareness->Satellites & GNSS
Supply-Chain Awareness->Intelligence Capability
Supply-Chain Awareness->Data Centres
Digital-Chain Awareness->Intelligence Capability
Digital-Chain Awareness->Cloud Compute
Digital-Chain Awareness->Telecoms Backbone

// Capability rests on infrastructure
Military Capability->Industrial Capability
Military Capability->Satellites & GNSS
Intelligence Capability->Data Centres
Intelligence Capability->Cloud Compute
Cyber Capability->Cloud Compute
Cyber Capability->Telecoms Backbone
Industrial Capability->Energy Supply
Industrial Capability->Semiconductor Supply
Regulatory Capability->Population Register

// CNI rests on deep commodities
Critical National Infrastructure->Energy Supply
Critical National Infrastructure->Telecoms Backbone
Critical National Infrastructure->Finance Rails
Critical National Infrastructure->Data Centres
Critical National Infrastructure->Undersea Cables
Critical National Infrastructure->Food Supply
Telecoms Backbone->Undersea Cables
Data Centres->Cloud Compute
Data Centres->Energy Supply
Semiconductor Supply->Energy Supply
Finance Rails->Cloud Compute

// Transitions to watch
evolve Digital Sovereignty 0.55
evolve Digital-Chain Awareness 0.50
evolve Cyber Capability 0.58
evolve Semiconductor Supply 0.60
evolve Election Legitimacy 0.52

// Inertia markers
component Mainstream Media [0.56, 0.72] inertia
component Domestic Laws [0.65, 0.76] inertia

note Industrialised sovereignty (utilities & rails) [0.12, 0.92]
note Contested & fragile sovereignty (norms, legitimacy, cyber) [0.78, 0.22]
note Pillars of sovereignty [0.86, 0.38]
note Capability layer [0.35, 0.62]
note Awareness apparatus [0.44, 0.38]
```

---

## §3.2 — Component evolution rationale (evidence table)

| Component | Stage | ε | ν | Evidence |
|---|---|---:|---:|---|
| Territorial Sovereignty | Custom Built | 0.42 | 0.88 | UN Charter Art.2(4) remains the frame, but Ukraine 2022 invasion showed every state now re-interprets territoriality bespoke; no "off-the-shelf" doctrine. |
| Economic Sovereignty | Custom Built | 0.48 | 0.86 | Post-Ukraine sanctions regimes, IRA (2022), EU Chips Act (Feb 2023) — each country re-inventing industrial policy; no stabilised pattern. |
| Political Sovereignty | Custom Built | 0.36 | 0.87 | Liberal-democratic norms still contested (Hungary, Turkey drift); no shared playbook for legitimate sovereignty assertion. |
| Digital Sovereignty | Genesis→Custom | 0.28 | 0.85 | EU GDPR stabilised (III) but digital sovereignty *as a concept* still emerging: GAIA-X prototypes, EU AI Act draft (April 2023), India Digital Personal Data Protection still pre-pass. |
| Cultural Sovereignty | Genesis | 0.22 | 0.84 | No consensus on what it means; policy tools ad-hoc (France's cultural exception vs. US First-Amendment globalism vs. China's content firewalls). |
| Security Sovereignty | Product (+rental) | 0.55 | 0.88 | NATO Art.5 + Five Eyes + FVEY-adjacent alliances are mature, standardised products; capability tiers well-defined. |
| Election Legitimacy | Custom Built | 0.33 | 0.78 | US 2020/2022, Brazil Jan-2023, Kenya 2022 — every cycle forces bespoke defence; no stable industrialised trust mechanism. Actively evolving. |
| Perception of Success | Genesis | 0.20 | 0.80 | Outcome measurement contested (GDP vs. wellbeing vs. climate). No accepted metric of government success in 2023. |
| Public Belonging | Genesis | 0.24 | 0.79 | Identity politics fractures; no reliable "social cohesion index"; academic field (Putnam, Haidt) still hypothesis-level. |
| Integrity | Custom Built | 0.30 | 0.70 | Transparency International CPI is a proxy, not a product; institutional integrity measured bespoke per country. |
| Benevolence | Custom Built | 0.28 | 0.69 | Welfare-state design is mature in form but contested in substance; no universal template. |
| Fairness | Custom Built | 0.34 | 0.71 | Procedural fairness reasonably stable; distributive fairness wildly contested (Piketty 2014→; post-COVID debates). |
| Competency | Custom Built | 0.42 | 0.72 | Civil-service reform playbooks exist (NPM, digital-government) but effectiveness highly variable. |
| Identity | Genesis | 0.20 | 0.68 | National identity construction is a bespoke, contested practice — no "identity-as-a-service". |
| Land Theatre | Commodity (+utility) | 0.78 | 0.62 | Territorial defence is an industrialised domain: treaties, force-structure doctrines, border-management tech all stabilised. |
| Supply-Chain Theatre | Product (+rental) | 0.54 | 0.60 | Post-Ukraine + post-COVID "friendshoring" / "de-risking" is a named, taught concept (Yellen 2022 speech); many consultancies selling it. |
| Cyber Theatre | Custom Built | 0.32 | 0.58 | Offensive cyber doctrine still opaque; defensive frameworks (NIST CSF, ISO 27001) exist but national-level cyber war posture is bespoke. |
| CNI Theatre | Product (+rental) | 0.66 | 0.63 | UK CPNI, US CISA, EU NIS2 (Jan 2023) — CNI protection is productised regulatory frameworks. |
| Crisis Response | Custom Built | 0.46 | 0.66 | COVID (2020–22) and Ukraine (2022) exposed every government's response as improvised; "crisis playbooks" are case-studies not standards. |
| International Law | Product (+rental) | 0.70 | 0.64 | UN Charter, Geneva Conventions, VCLT are mature; but enforcement remains contested — product exists, delivery is uneven. |
| Domestic Laws | Product (+rental) | 0.76 | 0.65 | Statute and case-law infrastructure is near-commodity in democracies; regulatory coverage of new domains (AI, crypto) lagging (inertia). |
| Mainstream Media | Product (+rental) | 0.72 | 0.56 | Newspapers, broadcast — mature product market, declining audiences; inertia against disruption by social platforms. |
| Social Media | Commodity (+utility) | 0.80 | 0.55 | Meta, X, TikTok, YouTube — utility-scale consumption (billions of users); algorithmic feeds are commodity infrastructure. |
| Education | Product (+rental) | 0.62 | 0.54 | State curricula, universities — productised; content mostly standardised, delivery mechanism (online/in-person) in transition. |
| Art | Custom Built | 0.47 | 0.53 | Cultural production remains bespoke; state funding (Arts Councils) productised but outputs per-artist custom. |
| Propaganda | Custom Built | 0.34 | 0.52 | IRA/RT playbook is studied (2016 DNC hack, Mueller report) but still bespoke per-campaign; no "propaganda-as-a-service" vendor market at this stage. |
| Territorial Awareness | Product (+rental) | 0.52 | 0.46 | Maxar, Planet Labs, NGA products — commercial GEOINT is a mature market; national systems layer on top. |
| Supply-Chain Awareness | Custom Built | 0.38 | 0.44 | Bloomberg / Kpler / Interos, etc. emerging; first-gen SCRM tools shipping; no dominant utility yet. |
| Digital-Chain Awareness | Genesis→Custom | 0.22 | 0.42 | Attribution of cyber ops, SBOM regimes (Exec Order 14028 May 2021), dependency-scanning — all early; no national "digital-chain GPS" in April 2023. |
| Military Capability | Commodity (+utility) | 0.74 | 0.40 | Established force structures, doctrine, logistics — near-commodity in G7 (albeit expensive commodity). |
| Intelligence Capability | Custom Built | 0.48 | 0.34 | Signals-intelligence methods mature but each service's tradecraft bespoke; all-source fusion still Custom. |
| Diplomatic Capability | Commodity (+utility) | 0.82 | 0.35 | Foreign service, treaties, UN/WTO/NATO representation — mature utility. |
| Cyber Capability | Custom Built | 0.36 | 0.33 | NSA/GCHQ/Unit 8200 capabilities are world-class but national-level posture varies wildly; no "cyber NATO" yet. Actively evolving. |
| Industrial Capability | Product (+rental) | 0.58 | 0.37 | Manufacturing base quantifiable (PMI, IP); post-Ukraine re-shoring making it policy-visible; productised policy tools (tax credits). |
| Regulatory Capability | Product (+rental) | 0.66 | 0.38 | FCA, FTC, ACM — mature regulator model; new-domain regulation (AI) still being built. |
| Critical National Infrastructure | Product (+rental) | 0.70 | 0.22 | NIS2 (Jan 2023), Presidential Policy Directive 21 (US) — productised regulatory taxonomies. |
| Telecoms Backbone | Commodity (+utility) | 0.86 | 0.18 | Tier-1 ISPs, IX fabric, submarine cable systems — utility. |
| Semiconductor Supply | Custom Built | 0.42 | 0.16 | Pre-CHIPS-Act-implementation (Oct 2022 → still ramping April 2023); TSMC concentration is a known Custom-Built fragility. Actively industrialising. |
| Energy Supply | Commodity (+utility) | 0.82 | 0.15 | Grid, LNG, pipelines — utility, but post-Ukraine has been *re-politicised* which lifts ν slightly above pure commodity. |
| Food Supply | Commodity (+utility) | 0.80 | 0.21 | Global grain/fertiliser markets are utility-priced; Ukraine disruption showed fragility but underlying structure is commodity. |
| Finance Rails | Commodity (+utility) | 0.88 | 0.19 | SWIFT, CHIPS, Fedwire, TARGET2 — utility; weaponisation of SWIFT in 2022 revealed it as a choke-point but structurally it's a commodity rail. |
| Data Centres | Commodity (+utility) | 0.82 | 0.17 | Hyperscaler + colo market — utility-priced. |
| Cloud Compute | Commodity (+utility) | 0.90 | 0.14 | AWS, Azure, GCP — textbook utility. |
| Undersea Cables | Commodity (+utility) | 0.88 | 0.12 | ~500 cables, a handful of cable-laying ships — utility, but with geopolitical choke-point concentration. |
| Satellites & GNSS | Commodity (+utility) | 0.78 | 0.13 | GPS/Galileo/BeiDou/GLONASS — utility at the service level; Starlink commoditising LEO comms. |
| Borders & Territory | Commodity (+utility) | 0.92 | 0.24 | Westphalian borders + IR-standard cadastral systems — utility-level stability. |
| Population Register | Commodity (+utility) | 0.80 | 0.26 | National IDs, census systems — mature utility in G7. |

---

## §3.1 — Mermaid wardley-beta (GitHub rendering)

```mermaid
wardley-beta
  title "National Sovereignty — Government's Point of View (April 2023)"
  anchor "Supranational Layer" [0.96, 0.46]
  anchor "Government" [0.97, 0.40]
  anchor "Corporations & Shareholders" [0.95, 0.58]
  anchor "Society" [0.96, 0.30]
  component "Territorial Sovereignty" [0.88, 0.42]
  component "Economic Sovereignty" [0.86, 0.48]
  component "Political Sovereignty" [0.87, 0.36]
  component "Digital Sovereignty" [0.85, 0.28]
  component "Cultural Sovereignty" [0.84, 0.22]
  component "Security Sovereignty" [0.88, 0.55]
  component "Election Legitimacy" [0.78, 0.33]
  component "Perception of Success" [0.80, 0.20]
  component "Public Belonging" [0.79, 0.24]
  component "Integrity" [0.70, 0.30]
  component "Benevolence" [0.69, 0.28]
  component "Fairness" [0.71, 0.34]
  component "Competency" [0.72, 0.42]
  component "Identity" [0.68, 0.20]
  component "Land Theatre" [0.62, 0.78]
  component "Supply-Chain Theatre" [0.60, 0.54]
  component "Cyber Theatre" [0.58, 0.32]
  component "CNI Theatre" [0.63, 0.66]
  component "Crisis Response" [0.66, 0.46]
  component "International Law" [0.64, 0.70]
  component "Domestic Laws" [0.65, 0.76]
  component "Mainstream Media" [0.56, 0.72]
  component "Social Media" [0.55, 0.80]
  component "Education" [0.54, 0.62]
  component "Art" [0.53, 0.47]
  component "Propaganda" [0.52, 0.34]
  component "Territorial Awareness" [0.46, 0.52]
  component "Supply-Chain Awareness" [0.44, 0.38]
  component "Digital-Chain Awareness" [0.42, 0.22]
  component "Military Capability" [0.40, 0.74]
  component "Intelligence Capability" [0.34, 0.48]
  component "Diplomatic Capability" [0.35, 0.82]
  component "Cyber Capability" [0.33, 0.36]
  component "Industrial Capability" [0.37, 0.58]
  component "Regulatory Capability" [0.38, 0.66]
  component "Critical National Infrastructure" [0.22, 0.70]
  component "Telecoms Backbone" [0.18, 0.86]
  component "Semiconductor Supply" [0.16, 0.42]
  component "Energy Supply" [0.15, 0.82]
  component "Food Supply" [0.21, 0.80]
  component "Finance Rails" [0.19, 0.88]
  component "Data Centres" [0.17, 0.82]
  component "Cloud Compute" [0.14, 0.90]
  component "Undersea Cables" [0.12, 0.88]
  component "Satellites & GNSS" [0.13, 0.78]
  component "Borders & Territory" [0.24, 0.92]
  component "Population Register" [0.26, 0.80]
  edge "Government" -> "Territorial Sovereignty"
  edge "Government" -> "Digital Sovereignty"
  edge "Government" -> "Election Legitimacy"
  edge "Society" -> "Cultural Sovereignty"
  edge "Society" -> "Election Legitimacy"
  edge "Digital Sovereignty" -> "Cyber Theatre"
  edge "Cyber Theatre" -> "Cyber Capability"
  edge "Cyber Theatre" -> "Telecoms Backbone"
  edge "Critical National Infrastructure" -> "Undersea Cables"
  edge "Critical National Infrastructure" -> "Finance Rails"
  edge "Election Legitimacy" -> "Integrity"
  edge "Election Legitimacy" -> "Identity"
  edge "Supply-Chain Theatre" -> "Semiconductor Supply"
  edge "Military Capability" -> "Satellites & GNSS"
  edge "Digital-Chain Awareness" -> "Cloud Compute"
```

*(Mermaid `wardley-beta` is still evolving; a stripped edge set keeps the render readable. Canonical wiring is in the OWM block above.)*

---

## 4. Strategic analysis

**Qualitative headline:** sovereignty in April 2023 is a **two-tier landscape**. Deep infrastructure is industrialised — cloud, undersea cables, finance rails, energy grid, telecoms, borders — the government can and should *consume* these as utilities. But the entire **legitimacy stack and digital/cyber pillar are in Custom-Built / Genesis territory** — contested, fragile, and where the government's real battle is. The irony: the most strategically decisive layer (legitimacy + digital sovereignty) is the least industrialised; the least strategically-contestable layer (utilities) is the most.

### a. Differentiation opportunities (top 3)

1. **Digital Sovereignty (Genesis → Custom Built)** — the pillar the scenario rightly highlights. Few states have a coherent posture; EU is ahead (GDPR, AI Act draft) but implementation is Custom. This is where sovereign "national platform" choices (identity, cloud, data residency) are made once a decade. Highest D — visible and immature.
2. **Election Legitimacy (Custom Built, transitioning)** — visibility is extreme; every incident (Jan 6, Brazil 2023) moves sovereignty legitimacy. The state that industrialises a trustworthy, audited, transparent election chain sets a pattern others follow.
3. **Digital-Chain Awareness (Genesis → Custom)** — knowing your software supply chain (SBOMs, attestation, provenance) is where the next "SolarWinds-class" sovereignty shock lands. The government that builds a national digital-chain sensor network has a generation-long lead.

### b. Commodity-leverage candidates (top 3)

1. **Cloud Compute (Commodity +utility)** — rent from AWS/Azure/GCP under sovereign-cloud contracts; don't build national equivalents except at the classified tier.
2. **Finance Rails (Commodity +utility)** — consume SWIFT/Fedwire/TARGET2 but retain a *contingency* rail (the Russia lesson). Weaponisation potential is high, so treat as a commodity you keep a backup for.
3. **Satellites & GNSS (Commodity +utility)** — use multi-constellation (GPS+Galileo+BeiDou) commercial GNSS for civilian needs; preserve sovereign PNT only for warfighting.

### c. Dependency risks (top 3)

1. **Election Legitimacy → Mainstream Media / Social Media** — a highly visible, norm-bearing component (ν=0.78) rests partly on a Commodity +utility (Social Media ε=0.80) that is *not under sovereign control*. Meta/X/TikTok make unilateral content decisions that move election legitimacy.
2. **Cyber Theatre → Cyber Capability** — visible cyber-theatre (ν=0.58) depends on a Custom-Built national cyber capability (ε=0.36). Operational gap between adversary speed and regulatory/capability speed is a chronic risk.
3. **Supply-Chain Theatre → Semiconductor Supply** — ν(supply-chain) 0.60 depends on Semiconductor Supply which is Custom Built (ε=0.42) and geographically concentrated (TSMC). Highest *physical* dependency risk on the map.

### d. Build / Buy / Outsource recommendations

| Component | Stage | Recommendation | Why |
|---|---|---|---|
| Digital-Chain Awareness | Genesis→Custom | **Build** (national capability) | No vendor market can deliver sovereign-grade attribution yet. Treat like the NSA of 1952 — build now or never. |
| Semiconductor Supply | Custom Built | **Build + ally** (CHIPS / Chips Act / friendshore) | Concentration risk unacceptable; but no one state can do it alone — ally-build via CHIPS4 / EU Chips Act. |
| Cyber Capability | Custom Built | **Build + open-source collaborate** | Elite tradecraft is custom, but defensive tooling is collaborative (CISA KEV, MITRE ATT&CK). Collaborate on defence, hoard offence. |
| Election Legitimacy (tech stack) | Custom Built | **Open-source collaborate** | Verifiability frameworks (end-to-end verifiable voting) only credible as open, auditable standards. |
| Territorial Awareness | Product (+rental) | **Buy** (Maxar, Planet, ICEYE) | Commercial GEOINT has leapfrogged many national services; buy the feed, layer national overlays. |
| Cloud Compute | Commodity (+utility) | **Rent** (sovereign-cloud tiers) | AWS GovCloud, Azure Gov, Bleu-SecNumCloud. Build only at TS/SCI tier. |
| Finance Rails | Commodity (+utility) | **Rent + hedge** | Consume SWIFT but retain CBDC/domestic-rail contingency after Russia 2022. |
| Telecoms Backbone | Commodity (+utility) | **Rent + regulate** | Commercial Tier-1s; the sovereign lever is regulation, not ownership. |
| Undersea Cables | Commodity (+utility) | **Rent + protect** | Consortium-owned commodity; the job is Royal-Navy/USN patrol and diversification, not building cables. |
| Military Capability | Commodity (+utility) | **Build (retain)** | Sovereign core — the one commodity the state must own outright. |
| Diplomatic Capability | Commodity (+utility) | **Build (retain)** | Foreign service is sovereign-only by treaty and tradition. |
| Propaganda / Strategic Communication | Custom Built | **Build (carefully)** | Custom per-campaign; democratic constraints limit how industrialised it can become. |
| Regulatory Capability (new-domain AI / crypto / biotech) | Product→emerging | **Build fast** | Regulatory-lag is the biggest doctrine violation on the map; see §f. |

### e. Suggested gameplays (from the 61-play catalogue)

- **#10 Embrace and Extend** — on *Digital Sovereignty*: adopt EU / allied digital-sovereignty primitives (data-space specs, GAIA-X patterns) and extend nationally rather than building from scratch.
- **#15 Open Approaches** — on *Election Legitimacy tech* and *Digital-Chain Awareness (SBOM / attestation)*: commoditise the trust layer by open-sourcing it; prevents adversary-controlled platforms from owning it.
- **#17 Cooperation** (with allies) — on *Semiconductor Supply*: CHIPS4 / EU Chips Act co-investment. No single state can unlock TSMC-scale concentration alone.
- **#22 Alliances** — on *Military Capability*, *Cyber Capability*, *Intelligence Capability*: Five Eyes / NATO / AUKUS as force-multipliers.
- **#34 Standards Game** — on *Digital Sovereignty* and *Digital-Chain Awareness*: shape ISO / IETF / NIST standards so national-security requirements become global defaults (the US has played this move on crypto for decades).
- **#38 Pig in a Poke** (defensive) — on *Social Media*: regulate platform accountability (DSA 2022, UK Online Safety Bill) before platforms lock in an unaccountable pattern.
- **#46 Fear, Uncertainty & Doubt (FUD)** as a *gameplay watch* — adversaries use FUD on *Perception of Success* (e.g., election-fraud narratives, COVID-origin confusion); defensive counter-play is rapid, high-credibility communication via *Mainstream Media*.
- **#48 Sensing Engines** — on *Territorial / Supply-Chain / Digital-Chain Awareness*: invest in sensor networks now; they compound over time.

### f. Doctrine violations (against Wardley's 40 doctrine)

- **#3 Focus on user needs** — partially met. The four anchors are named, but "what does Society actually need from sovereignty?" is under-specified. Governments often map without consulting Society's real needs, producing pillars optimised for *government's* view of sovereignty.
- **#11 Use a systematic mechanism of learning** — violated by **Regulatory Capability** in new domains. AI/crypto/bio regulation runs years behind the evolution of the thing being regulated. The government's learning loop is mis-tuned.
- **#17 Use appropriate methods** — risk of applying Commodity (+utility) management (six-sigma, metric-driven) to Genesis components like *Digital-Chain Awareness* or *Digital Sovereignty*. Will kill them. Agile/FIRE needed for the left-of-map components.
- **#21 Manage inertia** — explicitly flagged. *Mainstream Media* and *Domestic Laws* carry inertia against digital/social-media evolution. Regulating platforms requires breaking inertia in both.
- **#28 Think small (as in teams)** — mostly violated by governments: Genesis components like *Digital-Chain Awareness* are often handed to large prime contractors instead of small FIRE teams.

### g. Climatic context (of the 27 patterns)

- **#3 Everything evolves.** The six pillars are evolving right-to-left-or-right depending; the map captures a snapshot.
- **#9 Higher-order systems create new sources of worth.** Digital Sovereignty is a higher-order pillar that didn't exist as a distinct category pre-2015; it's carving out value from Political + Security Sovereignty.
- **#15 Inertia from past success.** Mainstream Media and Domestic Laws carry heavy inertia — they were peak-legitimacy in 1990 and haven't adapted to the Social Media utility layer.
- **#18 You cannot measure evolution over time or adoption.** Important framing for this map — Digital Sovereignty is "newer" than Territorial Sovereignty but not necessarily earlier in its evolution curve. Evolution is measured by the cheat sheet, not by calendar.
- **#19 No choice over evolution.** Components WILL industrialise (Cyber Capability, Digital-Chain Awareness). The question is whether the sovereign shapes the industrialisation or accepts a foreign one.
- **#27 Punctuated equilibrium.** Ukraine 2022 triggered a punctuated equilibrium in Energy Supply and Supply-Chain Awareness; both shifted right rapidly. Expect another shock (Taiwan / AI / climate) to punctuate Digital Sovereignty.

**Validator output:** the bundled `node validate_owm.mjs` script was not runnable in this sandbox (`Bash: permission denied`). Instead I hand-walked every edge against the visibility rule ν(a) ≥ ν(b) and recorded the full walk; the map has **47 components + 4 anchors, 97 edges, zero violations**. Initial drafting produced three violations — `Art → Cultural Sovereignty` (wrong direction; removed), `Diplomatic Capability → International Law` (duplicate of the correct reverse edge; removed), `Military Capability → Industrial Capability` (fixed by raising Military from ν=0.36 to ν=0.40) and `Data Centres → Energy Supply` (fixed by lowering Energy from ν=0.20 to ν=0.15). The layout checker was similarly unavailable; a manual layout review prompted four coordinate nudges (Art ε=0.50 → 0.47 off stage boundary; Digital-Chain Awareness ε=0.24 → 0.22; Benevolence ε=0.26 → 0.28; Military ν=0.36 → 0.40). No near-duplicate coordinates remain under the 0.02/0.02 rule; stage distribution is 5 Genesis / 17 Custom / 12 Product / 13 Commodity (all under the 60% single-stage cap).

### h. Deep-placement notes

I did focused placement work on four components that carry strategic weight and where the cheat-sheet rows pointed at different stages:

- **Digital Sovereignty.** Initial 7-row cheat sheet returned ε ≈ 0.35 (rows 5, 6, 11 pulled toward Genesis; row 7 toward Custom). Evidence: EU AI Act still in trilogue April 2023; GDPR (2018) is the first genuinely productised sovereignty-data regulation; GAIA-X prototypes alive but not adopted; India DPDP still pre-pass. Shifted to ε = 0.28 (early Custom / late Genesis) with an `evolve` target of 0.55 inside ~3 years as AI Act + DPDP + other frameworks land.
- **Semiconductor Supply.** Initial cheat-sheet said ε ≈ 0.55 (mature, globalised, commodity-priced). Evidence: pre-CHIPS-Act (Oct 2022 signed, implementation just starting April 2023); TSMC concentration risk = *not* commodity-replicable; ASML-EUV choke-point. This is a Custom-Built sovereignty-critical component dressed up as a commodity. Shifted to ε = 0.42 with `evolve 0.60` as CHIPS + EU Chips Act deliver over 3–5 years.
- **Digital-Chain Awareness.** Initial cheat-sheet suggested Genesis (ε ≈ 0.20). Evidence: EO 14028 (May 2021) mandates SBOMs across US federal; SLSA framework published 2021; CycloneDX / SPDX stabilising. The *regulatory* push is Custom-ifying the space fast. Held ε at 0.22 (Genesis→Custom transition) with `evolve 0.50`.
- **Social Media.** Initial cheat-sheet said ε ≈ 0.65 (Product). Evidence: daily-active-user counts in billions, utility-grade pricing (free-to-user, ad-funded), interchangeable feed-algorithms, low switching costs for ad buyers. This is Commodity (+utility) infrastructure now, despite brand-differentiated UIs. Shifted to ε = 0.80.

### i. Caveat

Evolution trajectories on this map (the `evolve` targets on Digital Sovereignty, Digital-Chain Awareness, Cyber Capability, Semiconductor Supply, Election Legitimacy) are **scenarios, not forecasts**. Wardley's climatic pattern #18: *you cannot measure evolution over time or adoption.* The `evolve` targets represent a plausible late-2020s state-of-play; a punctuated event (Taiwan crisis, Europe-wide cyber incident, major election-integrity breakdown) would redraw the picture.
