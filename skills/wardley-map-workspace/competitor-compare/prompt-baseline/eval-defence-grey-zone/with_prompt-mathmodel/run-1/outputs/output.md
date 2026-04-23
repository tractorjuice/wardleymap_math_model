# Grey Zone of Defence — Wardley Map

## 1. Model Instantiation

Tuple $\mathcal{M} = (V, E, U, \nu, \varepsilon, t)$ where:

- $|V| \approx 39$ components
- $|U| = 4$ anchors: Supranationals, Governments, Private-Proxy Operators, People
- Dependency edges $E$ are declared in the OWM (below)
- $\nu$ seeded from anchor distance, then adjusted against value-chain judgment
- $\varepsilon$ scored against the quick 4-row cheat sheet (Ubiquity / Certainty / User Perception / Publication Types)
- No time dynamics simulated — climatic pattern: evolution cannot be measured over time

Four anchors were used because the scenario explicitly names four actor classes and each has distinct, partially-opposed needs. A single-anchor map would collapse the central grey-zone tension (states vs. proxies, supranationals vs. governments) that the scenario asks us to show.

## 2. OWM Map

```owm
title Grey Zone of Defence — Below-Threshold Competition
style wardley

// Anchor set U — four classes of actor who have needs in the grey zone
anchor Supranationals [0.99, 0.45]
anchor Governments [0.98, 0.55]
anchor Private-Proxy Operators [0.96, 0.72]
anchor People [0.97, 0.40]

// Sovereignty pillars under contest
component Cyber Sovereignty [0.90, 0.50]
component Territorial Sovereignty [0.92, 0.30]
component Economic Sovereignty [0.91, 0.55]
component Cultural Sovereignty [0.89, 0.35]

// Statecraft frame
component Legitimacy [0.86, 0.40]
component Statecraft [0.85, 0.55]
component Treaties [0.83, 0.30]
component Ethics [0.82, 0.25]

// Theatres of competition
component Land Theatre [0.78, 0.80]
component Finance Theatre [0.76, 0.75]
component Electronic Theatre [0.74, 0.60]
component Space Theatre [0.72, 0.35]
component Social Media Theatre [0.73, 0.82]

// Effect types
component Kinetic Effect [0.66, 0.78]
component Coerce Effect [0.64, 0.55]
component Deter Effect [0.63, 0.50]
component Hearts and Minds Effect [0.62, 0.45]
component Propaganda Effect [0.65, 0.70]

// Consequences
component Friendly Fire [0.55, 0.25]
component Unintended Outcomes [0.54, 0.20]
component Accountability [0.52, 0.30]
component Attribution [0.50, 0.45]
component Deniability [0.51, 0.60]

// Landscape layer
component Physical Landscape [0.42, 0.80]
component Virtual Landscape [0.40, 0.65]
component Supply Chain Landscape [0.38, 0.70]

// Awareness of each landscape layer
component Physical Awareness (ISR) [0.33, 0.55]
component Virtual Awareness (SIGINT-OSINT) [0.31, 0.50]
component Supply Chain Awareness [0.29, 0.35]

// Foundational enablers
component Crypto (Payments, Anonymity) [0.22, 0.70]
component Cyber Toolkits (exploits, C2) [0.20, 0.60]
component PMCs-Proxy Forces [0.24, 0.78]
component Disinformation Infrastructure [0.18, 0.82]
component Commercial Satellites [0.15, 0.72]
component Public Cloud [0.12, 0.92]
component Global Payment Rails [0.10, 0.88]

// Dependencies — (A,B) means A depends on B
Supranationals->Legitimacy
Supranationals->Treaties
Supranationals->Cyber Sovereignty
Supranationals->Territorial Sovereignty
Governments->Statecraft
Governments->Cyber Sovereignty
Governments->Territorial Sovereignty
Governments->Economic Sovereignty
Governments->Cultural Sovereignty
Governments->Legitimacy
Private-Proxy Operators->Statecraft
Private-Proxy Operators->Deniability
Private-Proxy Operators->Economic Sovereignty
People->Cultural Sovereignty
People->Territorial Sovereignty
People->Legitimacy
Statecraft->Treaties
Statecraft->Ethics
Statecraft->Legitimacy
Legitimacy->Ethics
Cyber Sovereignty->Electronic Theatre
Cyber Sovereignty->Social Media Theatre
Territorial Sovereignty->Land Theatre
Territorial Sovereignty->Space Theatre
Economic Sovereignty->Finance Theatre
Cultural Sovereignty->Social Media Theatre
Land Theatre->Kinetic Effect
Land Theatre->Coerce Effect
Electronic Theatre->Coerce Effect
Electronic Theatre->Deter Effect
Space Theatre->Deter Effect
Social Media Theatre->Propaganda Effect
Social Media Theatre->Hearts and Minds Effect
Finance Theatre->Coerce Effect
Finance Theatre->Deter Effect
Kinetic Effect->Friendly Fire
Kinetic Effect->Unintended Outcomes
Propaganda Effect->Unintended Outcomes
Coerce Effect->Attribution
Deter Effect->Attribution
Hearts and Minds Effect->Unintended Outcomes
Attribution->Accountability
Friendly Fire->Accountability
Unintended Outcomes->Accountability
Deniability->Attribution
Accountability->Legitimacy
Land Theatre->Physical Landscape
Electronic Theatre->Virtual Landscape
Space Theatre->Physical Landscape
Social Media Theatre->Virtual Landscape
Finance Theatre->Virtual Landscape
Finance Theatre->Supply Chain Landscape
Physical Landscape->Physical Awareness (ISR)
Virtual Landscape->Virtual Awareness (SIGINT-OSINT)
Supply Chain Landscape->Supply Chain Awareness
Attribution->Virtual Awareness (SIGINT-OSINT)
Attribution->Physical Awareness (ISR)
Attribution->Supply Chain Awareness
Virtual Landscape->Public Cloud
Virtual Awareness (SIGINT-OSINT)->Commercial Satellites
Physical Awareness (ISR)->Commercial Satellites
Supply Chain Landscape->Global Payment Rails
Finance Theatre->Global Payment Rails
Electronic Theatre->Cyber Toolkits (exploits, C2)
Social Media Theatre->Disinformation Infrastructure
Land Theatre->PMCs-Proxy Forces
Private-Proxy Operators->PMCs-Proxy Forces
Economic Sovereignty->Global Payment Rails
Deniability->Crypto (Payments, Anonymity)
Deniability->PMCs-Proxy Forces
Finance Theatre->Crypto (Payments, Anonymity)
Cyber Toolkits (exploits, C2)->Public Cloud
Disinformation Infrastructure->Public Cloud

// Evolution movements (scenario, NOT forecast)
evolve Attribution 0.60
evolve Deniability 0.75
evolve Crypto (Payments, Anonymity) 0.85
evolve Disinformation Infrastructure 0.90
evolve Supply Chain Awareness 0.55
evolve Space Theatre 0.55

// Inertia — existing capital resisting evolution
component Treaties [0.83, 0.30] inertia
component Ethics [0.82, 0.25] inertia

// Strategic notes
note Weaponised-commodity zone: exploits, disinfo, crypto, proxies [0.20, 0.78]
note Genuinely novel: attribution, accountability, friendly-fire, treaty gap [0.55, 0.25]
note Differentiation pressure: sovereignty pillars + statecraft frame [0.88, 0.35]
note Utility-grade enablers (cloud, payment rails, sat imagery) [0.13, 0.88]
```

## 3. Evolution Rationale (quick 4-row cheat sheet)

| Component | Ubiquity | Certainty | User Perception | Pub Types | ε (avg) |
|---|---|---|---|---|---|
| Public Cloud | IV | IV | IV | IV | 0.875 |
| Global Payment Rails | IV | IV | IV | IV | 0.875 |
| Commercial Satellites | IV | III | III | IV | 0.72 |
| Disinformation Infrastructure | IV | III | IV | III | 0.75 (mapped 0.82 for saturation) |
| Cyber Toolkits | III | III | III | II | 0.55 |
| PMCs / Proxy Forces | III | III | III | IV | 0.69 (mapped 0.78) |
| Crypto (payments/anonymity) | III | III | III | III | 0.625 (mapped 0.70 — operationally normalised) |
| Social Media Theatre | IV | IV | IV | III | 0.78 |
| Land Theatre | IV | IV | IV | IV | 0.875 (mapped 0.80 — state asymmetry mod) |
| Finance Theatre | IV | III | IV | III | 0.69 |
| Electronic Theatre | III | III | III | II | 0.55 |
| Space Theatre | II | II | II | II | 0.375 |
| Attribution | II | I | I | II | 0.25 (mapped 0.45 — some forensic maturity) |
| Accountability | I | I | I | I | 0.125 (mapped 0.30 — legal scaffolding exists) |
| Friendly Fire | II | I | I | II | 0.25 |
| Unintended Outcomes | I | I | I | I | 0.125 (mapped 0.20) |
| Treaties | II | II | III | IV | 0.56 (mapped 0.30 — treaties for grey zone don't yet exist) |
| Ethics | I | II | II | II | 0.28 |
| Legitimacy | II | II | III | III | 0.47 (mapped 0.40) |

Components mapped lower than their row-average are flagged "in transition" — treaties, ethics, attribution and accountability all have strong row disagreement because frameworks exist (IV-ish publications) but the substantive concepts are still being worked out (I-II on certainty). The map's ε uses the lower value as the operative position.

## 4. Strategic Analysis

### a) Top 3 by differentiation pressure $D(v) = \nu \cdot (1 - \varepsilon)$

1. **Territorial Sovereignty** ($0.92 \cdot 0.70 = 0.644$) — visible to all four anchor classes and still contested by first principles (what counts as a territorial incursion in cyber/space?). Genuine differentiation zone for any state that codifies a doctrine first.
2. **Cultural Sovereignty** ($0.89 \cdot 0.65 = 0.579$) — high visibility to People anchor, immature as a defensible concept. Legitimacy battleground.
3. **Cyber Sovereignty** ($0.90 \cdot 0.50 = 0.450$) — midway maturing; the "norms of responsible state behaviour in cyberspace" process is still Stage II–III.

(Legitimacy at $0.86 \cdot 0.60 = 0.516$ would rank 2 if it were a component rather than a cross-cutting frame — treat it as a honorable mention.)

### b) Top 3 by commodity leverage $K(v) = (1 - \nu) \cdot \varepsilon$

1. **Public Cloud** ($0.88 \cdot 0.92 = 0.810$) — already utility. Disinfo infra, cyber toolkits, SIGINT back-ends all run on it.
2. **Global Payment Rails** ($0.90 \cdot 0.88 = 0.792$) — utility for legitimate finance, instrumentalised for sanctions and coercion.
3. **Commercial Satellites** ($0.85 \cdot 0.72 = 0.612$) — commoditised ISR; Maxar / Planet / ICEYE turned strategic reconnaissance into a subscription service.

These three are the weaponised-commodity backbone. Treat any effort to build sovereign equivalents as a *Defensive regulation* or *Sovereign capability* play, not a greenfield build.

### c) Top 3 dependency risks $R(a, b) = \nu(a) \cdot (1 - \varepsilon(b))$

1. **(Accountability → Legitimacy)**: $0.52 \cdot 0.60 = 0.312$ — visible consequence layer depending on a still-immature frame; when accountability fails, legitimacy erodes fast.
2. **(Attribution → Supply Chain Awareness)**: $0.50 \cdot 0.65 = 0.325$ — attribution increasingly needs supply-chain provenance (SolarWinds-style) but the awareness layer is Stage II.
3. **(Territorial Sovereignty → Space Theatre)**: $0.92 \cdot 0.65 = 0.598$ — highest raw R; space-based territorial concepts (orbital sovereignty, cis-lunar) are Genesis-stage.

### d) Suggested gameplays (from the 61-play catalogue)

Targeting the contested zone:

- **Open approaches / Open source** on **Attribution** — publish indicators, forensics standards, and shared threat intelligence to accelerate Attribution from Genesis/Custom-Built into Product. Analogous to what the CTI community did for malware families.
- **Experimentation** on **Supply Chain Awareness** — small, fast pilots (SBOM mandates, provenance graphs) rather than a grand architecture.
- **Co-creation with ecosystem** on **Treaties** — the Tallinn Manual process as template; states and academics co-draft before trying to ratify.

Targeting the weaponised commodities:

- **Pig in a poke** (#44) / **Fragmentation play** (#21) for defenders against **Disinformation Infrastructure**: force platform-level changes (content provenance, C2PA) that raise attacker cost.
- **Restriction of movement** / **Regulatory capture** on **Crypto (Payments, Anonymity)** — FATF travel rule, mixer sanctions — to re-commoditise back toward the legitimate payment rail.
- **Harvesting** on **PMCs / Proxy Forces** in legitimate markets (licensed private security) while **Procrastination** is applied to the grey-market segment via sanctions and banking de-risking.

Targeting the novel zone:

- **Sensing engine / Weak signal detection** on **Unintended Outcomes** and **Friendly Fire** — incident databases, lessons-learned feedback loops.
- **Pioneer-Settler-Town Planner** as an organisational play inside the defence ministry: Pioneers work on attribution/accountability, Settlers on the theatres, Town Planners on the utility enablers.

### e) Doctrine observations (from the 40 principles)

- **Phase I "Know your users"** — Four anchors is defensible for this scenario; collapsing to one would hide the central dynamic. Risk: "People" is a very generic anchor — break it into citizens-of-ally vs citizens-of-adversary vs global-public if the map is used operationally.
- **Phase I "Focus on high situational awareness"** — The three paired awareness components are deliberately separated from their landscape layers because *the awareness is always lagging the landscape*. This is consistent with doctrine.
- **Phase II "Use appropriate methods"** — Inertia markers on Treaties and Ethics reflect that legal/normative capital is slow-moving; the 17-form inertia doc would label these as *political capital* and *ethical/cultural capital*.
- **Phase III "A bias towards action"** — The evolve movements (Attribution → 0.60, Deniability → 0.75) are labelled as scenarios, not forecasts, per the canonical climatic pattern.
- **Potential violation** — the "Knowledge layer" (K in the τ extension) is underspecified here: concepts like "below-threshold", "hybrid warfare", "lawfare" are Knowledge but they're folded into Ethics/Legitimacy rather than surfaced separately. A follow-on map would unpack Knowledge components.

## 5. Where is the grey zone weaponised-commodity vs. genuinely novel?

**Weaponised-commodity (right-and-low — $\varepsilon > 0.70$, $\nu < 0.30$):**

- Public Cloud, Global Payment Rails, Commercial Satellites (utility enablers)
- Disinformation Infrastructure, Cyber Toolkits, PMCs/Proxy Forces, Crypto
- Social Media Theatre and Finance Theatre (as *arenas* — the mechanics are understood; only the legitimacy is contested)

The skill/cost barrier has collapsed. An adversary renting $N$ bot farms, hiring a PMC, acquiring exploit packs, and moving crypto is executing a repeatable play, not innovating.

**Genuinely novel (left-and-middle — $\varepsilon < 0.45$, $\nu$ in mid range):**

- Attribution, Accountability, Friendly Fire, Unintended Outcomes
- Treaties, Ethics (for this domain — slow-moving inertia)
- Space Theatre (as a sovereign domain, not as a capability)
- Cultural Sovereignty (as a doctrine, not as rhetoric)

The consequences layer and the governance frame have not caught up with the theatres. This is the "doctrinal wild west" — whoever codifies a working attribution-to-consequence chain in this region captures significant differentiation.

**Implication for strategy:** don't try to out-commoditise the adversary on Disinformation Infrastructure or Crypto — those races are lost or losing. Invest differentiation budget in the novel zone: Attribution, Accountability, and the paired Awareness capabilities, and use *Open approaches* and *Co-creation* plays to pull these toward Product stage faster than adversaries can re-establish deniability.
