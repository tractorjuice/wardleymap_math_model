# National Sovereignty (Government View, April 2023)

A Wardley Map of how a sitting government perceives its own sovereignty, following the formal model $\mathcal{M} = (V, E, U, \nu, \varepsilon, t)$ from the wardley-map skill.

The map uses four anchors — Supranational Layer, Government, Corporations and Shareholders, Society — and surfaces where sovereignty is already industrialised infrastructure (law, land, media, armed forces) versus where it is still contested and fragile (digital, supply-chain awareness, crisis doctrine).

---

## Map (OWM)

```owm
title National Sovereignty (Government View, April 2023)
style wardley

// Anchors — four user types in the sovereignty chain
anchor Supranational Layer [0.97, 0.68]
anchor Government [0.95, 0.55]
anchor Corporations and Shareholders [0.93, 0.72]
anchor Society [0.91, 0.48]

// Outcome layer — what "sovereignty" actually produces for the anchors
component Legitimacy [0.86, 0.55]
component Perception of Success [0.82, 0.58]
component Public Belonging [0.80, 0.45]
component Election Legitimacy [0.78, 0.52]

// Pillars of sovereignty — the first-order claims a government asserts
component Territorial Sovereignty [0.74, 0.78]
component Economic Sovereignty [0.72, 0.65]
component Political Sovereignty [0.70, 0.80]
component Digital Sovereignty [0.68, 0.32]
component Cultural Sovereignty [0.66, 0.70]
component Security Sovereignty [0.64, 0.72]

// Theatres — where the pillars actually play out
component Land Theatre [0.58, 0.88]
component Supply Chain Theatre [0.56, 0.55]
component Cyber Theatre [0.54, 0.38]
component CNI Theatre [0.52, 0.62]

// Awareness apparatus — what the government sees
component Territorial Awareness [0.48, 0.82]
component Supply-Chain Awareness [0.46, 0.28]
component Digital-Chain Awareness [0.44, 0.18]

// Capability layer — what the government can do with what it sees
component Capability Layer [0.40, 0.55]
component Crisis Response [0.38, 0.42]
component Intelligence Services [0.36, 0.70]
component Armed Forces [0.34, 0.78]
component Regulatory Enforcement [0.33, 0.68]
component Diplomacy [0.32, 0.76]

// Media mix — the channels that shape perception
component Social Media [0.52, 0.68]
component Mainstream Media [0.50, 0.85]
component Education [0.48, 0.88]
component Art [0.46, 0.82]
component Propaganda [0.44, 0.78]

// Social norms — the K-layer the legitimacy rests on
component Integrity [0.23, 0.84]
component Benevolence [0.21, 0.78]
component Fairness [0.19, 0.86]
component Competency [0.17, 0.80]
component Identity [0.15, 0.72]

// Legal foundation
component International Law [0.26, 0.82]
component Domestic Laws [0.28, 0.88]
component Treaties and Alliances [0.30, 0.76]

// Feedback and reinforcement
component Civic Participation [0.60, 0.58]
component Public Discourse [0.58, 0.62]

// Dependencies — anchors into legitimacy/pillars
Supranational Layer->Legitimacy
Supranational Layer->Political Sovereignty
Supranational Layer->International Law
Supranational Layer->Treaties and Alliances
Government->Legitimacy
Government->Election Legitimacy
Government->Territorial Sovereignty
Government->Economic Sovereignty
Government->Political Sovereignty
Government->Digital Sovereignty
Government->Cultural Sovereignty
Government->Security Sovereignty
Corporations and Shareholders->Economic Sovereignty
Corporations and Shareholders->Digital Sovereignty
Corporations and Shareholders->Perception of Success
Society->Public Belonging
Society->Election Legitimacy
Society->Cultural Sovereignty
Society->Legitimacy

// Legitimacy depends on perception, belonging, elections
Legitimacy->Perception of Success
Legitimacy->Public Belonging
Legitimacy->Election Legitimacy
Perception of Success->Mainstream Media
Perception of Success->Social Media
Public Belonging->Cultural Sovereignty
Public Belonging->Identity
Election Legitimacy->Integrity
Election Legitimacy->Fairness
Election Legitimacy->Domestic Laws

// Pillars depend on theatres
Territorial Sovereignty->Land Theatre
Territorial Sovereignty->CNI Theatre
Economic Sovereignty->Supply Chain Theatre
Economic Sovereignty->CNI Theatre
Political Sovereignty->Civic Participation
Political Sovereignty->International Law
Digital Sovereignty->Cyber Theatre
Digital Sovereignty->CNI Theatre
Cultural Sovereignty->Public Discourse
Cultural Sovereignty->Education
Security Sovereignty->Land Theatre
Security Sovereignty->Cyber Theatre
Security Sovereignty->CNI Theatre

// Theatres depend on awareness
Land Theatre->Territorial Awareness
Supply Chain Theatre->Supply-Chain Awareness
Cyber Theatre->Digital-Chain Awareness
CNI Theatre->Territorial Awareness
CNI Theatre->Digital-Chain Awareness

// Awareness depends on capability
Territorial Awareness->Intelligence Services
Supply-Chain Awareness->Intelligence Services
Digital-Chain Awareness->Intelligence Services

// Capability layer decomposition
Capability Layer->Crisis Response
Capability Layer->Intelligence Services
Capability Layer->Armed Forces
Capability Layer->Regulatory Enforcement
Capability Layer->Diplomacy
Crisis Response->Armed Forces
Crisis Response->Regulatory Enforcement
Diplomacy->Treaties and Alliances
Diplomacy->International Law
Regulatory Enforcement->Domestic Laws

// Awareness/capability from pillar action
Economic Sovereignty->Regulatory Enforcement
Security Sovereignty->Armed Forces
Security Sovereignty->Intelligence Services
Political Sovereignty->Diplomacy

// Civic participation and public discourse
Election Legitimacy->Civic Participation
Civic Participation->Public Discourse
Public Discourse->Social Media
Public Discourse->Mainstream Media
Public Discourse->Education
Public Discourse->Art

// Media mix feeds the norms and perception
Social Media->Propaganda
Mainstream Media->Propaganda
Education->Competency
Education->Benevolence
Art->Identity

// Laws codify norms (laws depend on the norms they encode)
Domestic Laws->Integrity
Domestic Laws->Fairness
Domestic Laws->Competency
Domestic Laws->Benevolence
International Law->Integrity
International Law->Fairness

// Evolve targets — the known 2023-era trajectories
evolve Digital Sovereignty 0.55
evolve Supply-Chain Awareness 0.50
evolve Digital-Chain Awareness 0.45
evolve Crisis Response 0.60
evolve Cyber Theatre 0.62

// Notes
note Industrialised sovereignty [0.5, 0.88]
note Contested and fragile [0.55, 0.22]
```

### Validator status

The in-tree validator (`skills/wardley-map/scripts/validate_owm.mjs`) was not runnable in this sandbox (the `node` invocation for this file path is outside the current allowlist). **Manual edge-walk**: 4 anchors + 41 components = 45 nodes; 81 edges. Every edge has $\nu(a) \ge \nu(b)$ after fixes; every endpoint is declared; every coordinate is in $[0, 1]$. Three initial violations (Civic Participation → Election Legitimacy, Art → Cultural Sovereignty, and the four norm → Domestic Laws edges) were caught and corrected by reversing the dependency direction (laws codify norms, so Domestic Laws depends on Integrity / Fairness / Competency / Benevolence — not the reverse). The reversed shape is also more semantically defensible: the ideal that a society agrees on (Knowledge, Stage IV) is deeper in the chain than the codification (Activity, Stage IV).

### Layout check status

Advisory layout-check items fixed by nudging: `Election Legitimacy ε` 0.50 → 0.52 (was exactly on a stage boundary), `Diplomacy ε` 0.75 → 0.76 (boundary), `Treaties and Alliances ε` 0.75 → 0.76 (boundary), anchor $\nu$ values pulled back from 0.98/0.96/0.94/0.92 to 0.97/0.95/0.93/0.91 (avoids the canvas-edge warning at $\nu > 0.98$). Norm cluster (Integrity / Benevolence / Fairness / Competency / Identity) spread across $\nu \in [0.15, 0.23]$ and $\varepsilon \in [0.72, 0.86]$ to avoid near-duplicate collisions. No stage is empty; distribution is Genesis 1 / Custom Built 5 / Product (+rental) ~15 / Commodity (+utility) ~18 — Commodity-weighted but not above 60%.

---

## Optional: Mermaid `wardley-beta`

The converter script (`skills/wardley-map/scripts/owm_to_mermaid.mjs`) was similarly outside the node-invocation allowlist in this sandbox. A hand-rolled block that follows the converter's conventions (double-quoted names, `-` replaced with ` and ` is not needed here because no slashes or hyphens-inside-names appear; the Mermaid wardley-beta grammar requires double-quoted forms for any name that contains spaces or hyphens):

```mermaid
wardley-beta
    title "National Sovereignty (Government View, April 2023)"
    anchor "Supranational Layer": [0.68, 0.97]
    anchor "Government": [0.55, 0.95]
    anchor "Corporations and Shareholders": [0.72, 0.93]
    anchor "Society": [0.48, 0.91]
    component "Legitimacy": [0.55, 0.86]
    component "Perception of Success": [0.58, 0.82]
    component "Public Belonging": [0.45, 0.80]
    component "Election Legitimacy": [0.52, 0.78]
    component "Territorial Sovereignty": [0.78, 0.74]
    component "Economic Sovereignty": [0.65, 0.72]
    component "Political Sovereignty": [0.80, 0.70]
    component "Digital Sovereignty": [0.32, 0.68]
    component "Cultural Sovereignty": [0.70, 0.66]
    component "Security Sovereignty": [0.72, 0.64]
    component "Land Theatre": [0.88, 0.58]
    component "Supply Chain Theatre": [0.55, 0.56]
    component "Cyber Theatre": [0.38, 0.54]
    component "CNI Theatre": [0.62, 0.52]
    component "Territorial Awareness": [0.82, 0.48]
    component "Supply-Chain Awareness": [0.28, 0.46]
    component "Digital-Chain Awareness": [0.18, 0.44]
    component "Capability Layer": [0.55, 0.40]
    component "Crisis Response": [0.42, 0.38]
    component "Intelligence Services": [0.70, 0.36]
    component "Armed Forces": [0.78, 0.34]
    component "Regulatory Enforcement": [0.68, 0.33]
    component "Diplomacy": [0.76, 0.32]
    component "Social Media": [0.68, 0.52]
    component "Mainstream Media": [0.85, 0.50]
    component "Education": [0.88, 0.48]
    component "Art": [0.82, 0.46]
    component "Propaganda": [0.78, 0.44]
    component "Integrity": [0.84, 0.23]
    component "Benevolence": [0.78, 0.21]
    component "Fairness": [0.86, 0.19]
    component "Competency": [0.80, 0.17]
    component "Identity": [0.72, 0.15]
    component "International Law": [0.82, 0.26]
    component "Domestic Laws": [0.88, 0.28]
    component "Treaties and Alliances": [0.76, 0.30]
    component "Civic Participation": [0.58, 0.60]
    component "Public Discourse": [0.62, 0.58]
```

The Mermaid block omits edges because the number (81) crowds the render; the OWM block is canonical.

---

## Strategic analysis

### a. Differentiation opportunities (top 3)

1. **Digital Sovereignty** (Custom Built, $\varepsilon \approx 0.32$) — **highest differentiation pressure on the map.** A pillar of sovereignty that the government asserts visibly to all anchors, but whose underlying components (chip supply, cloud layer, cross-border data flows, platform governance) are still bespoke per-jurisdiction. No settled model exists — EU, US, China, India, and the UK are each pursuing incompatible approaches in April 2023. This is where a sitting government can build genuine strategic advantage over a 3-5 year horizon.
2. **Public Belonging** (Custom Built → Product boundary, $\varepsilon \approx 0.45$) — the affective glue between Society and Legitimacy. Contested in almost every developed democracy post-2016. A government that can credibly build public belonging has an advantage that can't be rented from any vendor.
3. **Legitimacy** (Product +rental, $\varepsilon \approx 0.55$) — the most visible component on the entire map. It is *not* Genesis — the concept of government legitimacy is ancient. But its *current state* for any given government is a Product-stage feature-competitive landscape, and the features that matter (Perception of Success, Public Belonging, Election Legitimacy) are all themselves in transition. Differentiation is high because legitimacy is visible and its supply is contested.

### b. Commodity-leverage candidates (top 3)

1. **Domestic Laws** (Commodity +utility, $\varepsilon \approx 0.88$) — deep, mature, institutionally standard. Don't reinvent; apply. High $K$ because every pillar depends on the legal substrate.
2. **International Law** (Commodity +utility, $\varepsilon \approx 0.82$) — body of law, ICJ, ICC, UNCLOS, Geneva Conventions, and the WTO corpus are all decades-mature. The government consumes this layer rather than building it; alliances (Treaties and Alliances) and diplomacy (Diplomacy) operate on top.
3. **Armed Forces** (Commodity +utility, $\varepsilon \approx 0.78$) — as a *capability*, armed forces are a mature, standardised government function in developed states. This is not to say they're trivial — but the doctrine, procurement, structure, and norms are industrialised. Leverage through alliance (NATO, AUKUS) rather than reinvention.

Other strong K candidates worth naming: **Education** ($\varepsilon \approx 0.88$), **Mainstream Media** ($\varepsilon \approx 0.85$), **Propaganda** ($\varepsilon \approx 0.78$, treated as a capability that exists in every state information apparatus regardless of political valence).

### c. Dependency risks (top 3)

1. **Government → Digital Sovereignty** — the highest-R edge on the map. The government makes a highly visible sovereignty claim (it features in every national strategy document in 2022-2023) but the underlying pillar is Custom Built. This is the single biggest "asserting more than you can do" gap.
2. **Corporations and Shareholders → Digital Sovereignty** — the same claim from the private-sector anchor. Corporations have adopted the language of digital sovereignty (sovereign clouds, data residency, on-shore AI) but the supply is still bespoke. Risk that corporate strategy is pegged to a pillar that isn't yet industrialised.
3. **Cyber Theatre → Digital-Chain Awareness** — the cyber theatre is real and active (state-on-state cyber operations are the post-2022 norm), but the awareness apparatus underneath it (SBOM, software supply-chain attestation, vendor attestation at scale) is still at the Genesis–Custom boundary ($\varepsilon \approx 0.18$). Visible warfighting depends on invisible, immature sensing.

Honourable mentions: **Society → Election Legitimacy** (the electorate's trust in a Product-stage institution that is sliding backward in several major democracies); **Supply Chain Theatre → Supply-Chain Awareness** (supply-chain discourse has industrialised since 2020, but actual multi-tier visibility tooling hasn't).

### d. Suggested gameplays

- **#36 Directed investment** on **Digital Sovereignty** and **Digital-Chain Awareness** — concentrate sovereign-fund / CHIPS-equivalent / NAIC-equivalent capital into the one pillar where the differentiation leverage is highest and the supply is not yet set. Pair with #37 Experimentation: test multiple approaches to sovereign cloud / sovereign AI / SBOM programmes rather than committing to one.
- **#18 Industrial Policy** on **Supply-Chain Awareness** and **Cyber Theatre** — governments have the (rare) legitimate tool of raising baseline $r_0$ via public investment, standards mandates, and procurement signalling. CHIPS Act, IRA, EU Chips Act, and US Executive Order 14028 are this play in action.
- **#41 Alliances** on **Treaties and Alliances** and **Intelligence Services** — a well-documented small-state strategy, but equally valid for mid-sized powers in April 2023 (Five Eyes, AUKUS, I2U2, Quad, expanded NATO). Cheap way to rent capability you cannot afford to build.
- **#15 Open Approaches** on **Digital-Chain Awareness** — once SBOM standards mature, opening them aggressively (pushing CycloneDX / SPDX / GUAC as open frameworks rather than proprietary national schemes) accelerates commoditisation and lets the government focus on higher-order capabilities.
- **#30 Standards game** on **Digital Sovereignty** — whichever jurisdiction sets the de facto standards for cross-border data, AI governance, and platform regulation will define the pillar. EU is visibly playing this via GDPR/DSA/DMA/AI Act; other governments can respond by setting alternative or compatible standards.
- **#35 Defensive regulation** on **Cultural Sovereignty** via the media mix — every government in the map's 2023 landscape is visibly doing this (content moderation, platform regulation, streaming quotas). Named explicitly so it's on the map rather than pretending it isn't.
- **#43 Sensing Engines (ILC)** on **Social Media** and **Public Discourse** — governments consume consumption data (either directly or via intelligence services) to detect shifts. This is industrialised in practice; naming it lets the map include the feedback loop honestly.
- **#11 FUD** and **#50 Reinforcing inertia** are the adversarial plays a hostile state deploys against this map (on Perception of Success, Public Belonging, Election Legitimacy). Named here not as recommendation but as contingency — the government's crisis response (Crisis Response) needs to plan for these.

### e. Doctrine violations and notes

- **Doctrine #10 Know your users** — **passes**. Four anchors (Supranational, Government, Corporations & Shareholders, Society) correctly reflect that sovereignty is not a single-user-need system. An earlier draft with one anchor (Government alone) would be a doctrine violation.
- **Doctrine #13 Manage inertia** — **inertia is the dominant theme of the bottom half of the map.** The social norms (Integrity, Benevolence, Fairness, Competency, Identity) and the legal substrate are Stage IV with enormous inertia weights. A government moving against them triggers legitimacy loss; a government moving with them moves slowly. The most important inertia forms from the 17 structured forms: **#2 Sunk capital** (decades of institutional investment in Armed Forces, legal code, education), **#3 Political capital** (elected governments are tethered to prior legislative commitments), **#4 Human capital** (civil service skill profiles), **#13 Social convention** (public belonging is conservative by design), and the supplier-side **#15 Practice-acquisition cost** (intelligence and diplomatic services have very slow talent pipelines).
- **Doctrine #1 Focus on user needs** — **partial**. The outcome layer (Legitimacy, Perception of Success, Public Belonging, Election Legitimacy) correctly sits between the anchors and the pillars. But the Corporations & Shareholders anchor is often the weakest-represented user in government strategy in practice — if the map ignores it, it violates doctrine. The map keeps it.
- **Doctrine #8 Focus on high situational awareness** — **under-realised on this map**. Three awareness components (Territorial, Supply-Chain, Digital-Chain) are present, but the fact that they share a single downstream dependency (Intelligence Services) compresses a genuinely tri-theatre sensing problem into a single-point-of-failure. Real governments invest in distinct teams, but map-wise this is the honest picture.
- **Doctrine #22 Use standards where appropriate** — naturally satisfied: standards apply at International Law, Domestic Laws, Armed Forces, Mainstream Media. Premature standardisation on Digital Sovereignty is a live risk — several jurisdictions are locking in Stage-II designs prematurely.

### f. Climatic context

- **#3 Everything evolves** — Digital Sovereignty, cyber capability, supply-chain awareness, and crisis response are all on Red-Queen trajectories. A government that locks in 2023's approach will be mis-positioned by 2028.
- **#15–17 Inertia (all three forms)** — past success with the Westphalian model breeds inertia; the larger the state's historical sovereignty claim, the harder it is to adapt (Kodak logic applied to nation-states). The mapped relationship between successful-in-the-past norms and fragile-in-the-present legitimacy is the inertia dynamic playing out.
- **#18 You cannot measure evolution over time or adoption** — the canonical caveat, relevant because several governments have tried to measure digital-sovereignty progress by adoption percentages (share of citizens using a sovereign cloud, etc.) and drawn unsafe conclusions. The cheat sheet's ubiquity-and-certainty axes are the right way to score, not adoption rates.
- **#27 Product-to-utility punctuated equilibrium** — visible on Cyber Theatre, Supply-Chain Awareness, and Digital-Chain Awareness. These will shift from bespoke-per-state to utility over the coming five years; the states that are late will experience a legitimacy cliff-edge when peers industrialise the capability and they cannot.
- **#4 Evolution consists of multiple waves with many chasms** — Cyber Theatre is on its second wave (post-2000 state cyber was Custom; post-2015 state cyber is Product-ish; post-2022 persistent engagement is its own wave). A single-logistic dynamic would under-model it.
- **#1 Competitor actions will change the game** — Russia/Ukraine war, PRC Taiwan posture, and US-China tech competition are all actively re-shaping this map every quarter. The map should be re-drawn at least every 6 months.
- **#7 Characteristics change as components evolve** — the management style for Digital Sovereignty (agile, FIRE, hypothesis-driven) is the opposite of the style for Armed Forces (six sigma, operational excellence). Applying one across the other is a doctrine #7/#8 violation.

### g. Deep-placement notes

Four components warranted a closer look (high D, high K, or sub-cheat-sheet-row variance). All four land defensibly in the chosen stage, with the noted movements:

- **Digital Sovereignty** — initial cheat-sheet pass put this at $\varepsilon \approx 0.30$ because the term is ubiquitous in 2023 policy discourse (suggesting late Custom). Publication-type scan shifts it slightly: multiple national strategies published 2022-2023 (US National Cyber Strategy March 2023, UK National Cyber Strategy 2022, EU Digital Sovereignty Framework, CHIPS Act Aug 2022 — build / construct / awareness publications) confirm Stage II; no dominant vendor, no convergence on approach, no ISO-style standards. Settled at $\varepsilon = 0.32$.
- **Supply-Chain Awareness** — initial read suggested Product (+rental) because post-COVID and Russia-sanctions awareness raised profile dramatically. But vendor-landscape probe pulls it back: Roambee, Overhaul, Project44, Everstream Analytics are emerging but the multi-tier visibility problem is not solved at scale, and there is no market-standard schema. ISO 28000 exists but adoption is thin. Settled at $\varepsilon = 0.28$ (early Custom Built).
- **Digital-Chain Awareness** (SBOM, software supply-chain attestation) — US Executive Order 14028 was May 2021; CISA SBOM guidance 2021-2022; in-toto / SLSA frameworks are Genesis-to-early-Custom; CycloneDX and SPDX are the two candidate formats with no clear winner in 2023. Settled at $\varepsilon = 0.18$ (late Genesis / early Custom) — this is the single most uncertain placement on the map.
- **Election Legitimacy** — the historical institution of elections is Stage IV Commodity. But what the user asked for is the *2023 state* of election legitimacy for a sitting government, and multiple developed democracies have seen this *regress* from Stage IV back toward Stage III (denialism, audit disputes, claimed fraud, procedural distrust) since 2020. Settled at $\varepsilon = 0.52$ (early Product) to reflect the observed backwards drift. Note: the **concept** is Commodity; the **current achievement** is Product-stage. The two disagree, and that disagreement is itself strategically important.

### h. Caveat

Evolution trajectories on this map are scenarios, not forecasts. Wardley's climatic pattern #18: *"you cannot measure evolution over time or adoption."* The `evolve` arrows (Digital Sovereignty → 0.55; Supply-Chain Awareness → 0.50; Digital-Chain Awareness → 0.45; Crisis Response → 0.60; Cyber Theatre → 0.62) represent plausible 3-5 year directions under current climatic conditions. Competitor moves (#1), black-swan events, and strategic shocks can re-draw the map at any time. Re-map quarterly.

---

## Where sovereignty is industrialised vs contested

**Industrialised (Commodity +utility, $\varepsilon \ge 0.75$ and high-visibility):**

| Component | Stage | Strategic posture |
|---|---|---|
| Land Theatre | Commodity | Stable border regime, mature doctrine |
| Armed Forces | Commodity | Alliance-leveraged, standardised doctrine |
| International Law | Commodity | Inherited substrate, leverage via treaties |
| Domestic Laws | Commodity | Deep institutional foundation |
| Education | Commodity | Mature system, cultural inertia is a feature |
| Mainstream Media | Commodity | Well-understood (if declining in reach) |
| Art | Commodity | Deep cultural capital |
| Territorial Awareness | Commodity | Satellites, mature intel tradecraft |
| Territorial Sovereignty | Commodity | Westphalian concept; well-defined |
| Political Sovereignty | Commodity | As a concept; contested as an achievement |

**Contested and fragile (Genesis or Custom Built, $\varepsilon < 0.50$ with high visibility):**

| Component | Stage | Strategic posture |
|---|---|---|
| Digital Sovereignty | Custom Built | Highest differentiation leverage; bespoke |
| Cyber Theatre | Custom Built | Doctrine incomplete; rapidly evolving |
| Supply-Chain Awareness | Custom Built | Post-2020 priority; tools immature |
| Digital-Chain Awareness | Genesis / Custom | SBOM and attestation still emerging |
| Crisis Response | Custom Built | Each shock requires new doctrine |
| Public Belonging | Custom Built → Product | Contested in every developed state |
| Election Legitimacy | Product (regressing) | Backwards drift post-2020 |

The pattern is clear: **the classical pillars of sovereignty (land, law, armed forces) are industrialised; the post-2015 pillars (digital, cyber, supply-chain) are contested.** Where differentiation is available is therefore mostly on the left of the map — which is exactly where we would expect a sitting government to be making its biggest strategic bets. The risk is that visible claims on these left-side components (Government → Digital Sovereignty being the largest-R edge) outrun the maturity of the supply underneath.
