# Wardley Map — State Sovereignty in a Digital, Globalised Economy (April 2023)

## Scenario

Map the landscape of state sovereignty in a digital, globalised economy. Include territorial, economic, technological, data, political, and cultural dimensions; instruments of sovereignty (regulation, standards, trade, defence, diplomacy); and erosion risks (platforms, capital flight, cyber, supply chain dependency). Call out what is differentiating and what is commoditising.

This is a multi-stakeholder landscape, so three anchors are used: the **State** as the sovereign actor, **Citizens** as the beneficiaries whose needs legitimise sovereignty, and **External Actors** (other states, multinationals, international organisations) who interact with the sovereignty frontier from outside.

---

## Map (OWM)

```owm
title State Sovereignty in a Digital, Globalised Economy (April 2023)
style wardley

// Anchors: the sovereign state (as actor), citizens (as beneficiaries), and external actors who interact with sovereignty
anchor State (Government) [0.99, 0.60]
anchor Citizens [0.96, 0.55]
anchor External Actors (States, MNCs) [0.92, 0.65]

// --- Sovereignty dimensions (the things the state claims to have sovereignty over) ---
component Territorial Sovereignty [0.85, 0.82]
component Economic Sovereignty [0.83, 0.60]
component Technological Sovereignty [0.80, 0.30]
component Data Sovereignty [0.78, 0.35]
component Political Sovereignty [0.82, 0.78]
component Cultural Sovereignty [0.74, 0.55]
component Monetary Sovereignty [0.76, 0.65]

// --- Instruments of sovereignty ---
component Regulation (Rule-making) [0.70, 0.65]
component Standards Setting [0.65, 0.50]
component Trade Policy (Tariffs, Export Controls) [0.68, 0.70]
component Industrial Policy & Subsidy [0.62, 0.45]
component Defence & Deterrence [0.64, 0.60]
component Diplomacy & Alliances [0.66, 0.80]
component Intelligence Services [0.58, 0.60]
component Sanctions Regime [0.60, 0.55]
component Tax Authority [0.62, 0.85]
component Law Enforcement [0.60, 0.80]
component Border & Customs Control [0.58, 0.85]

// --- Legal / doctrinal stack underneath instruments ---
component Legal System & Courts [0.48, 0.85]
component Constitution & Treaty Law [0.46, 0.75]
component International Law (WTO, UN) [0.42, 0.62]

// --- Technological / infrastructure layer the state depends on ---
component Digital ID & Civic Platforms [0.52, 0.40]
component Government Cloud [0.38, 0.45]
component Critical National Infrastructure [0.42, 0.78]
component Payment Rails (Domestic) [0.40, 0.82]
component SWIFT / Cross-border Payments [0.36, 0.80]
component Central Bank Digital Currency [0.44, 0.15]
component Reserve Currency Access (USD) [0.38, 0.75]

// --- Supply chain and physical dependencies ---
component Semiconductor Supply Chain [0.30, 0.50]
component Rare Earths & Critical Minerals [0.26, 0.55]
component Energy Supply [0.28, 0.75]
component Food Supply [0.24, 0.80]
component Pharmaceutical Supply [0.22, 0.70]

// --- Cyber / data foundations ---
component Cyber Defence Capability [0.50, 0.40]
component Encryption Standards [0.34, 0.65]
component Undersea Cable Infrastructure [0.20, 0.80]
component DNS & Internet Routing [0.16, 0.85]
component Public Key Infrastructure [0.18, 0.75]

// --- Erosion vectors (platforms, capital, cyber, supply chain) ---
component Foreign Platforms (GAFAM, TikTok) [0.60, 0.72]
component Cross-border Data Flows [0.56, 0.68]
component Capital Markets / Capital Flight [0.54, 0.78]
component Offshore Tax Havens [0.48, 0.82]
component Cyber Threats (State & Non-state) [0.56, 0.55]
component Foreign Influence Operations [0.68, 0.45]
component Supply Chain Dependency [0.54, 0.60]
component Climate / Transboundary Externalities [0.50, 0.35]

// --- Knowledge layer ---
component Technical Expertise (in-state) [0.32, 0.50]
component Strategic Doctrine [0.44, 0.55]
component Industrial Base / Skills [0.30, 0.60]

// --- Cultural layer ---
component National Media & Public Discourse [0.64, 0.65]
component Language & Education System [0.56, 0.75]
component National Identity & Narrative [0.70, 0.55]

// --- Dependencies ---

// Anchor -> dimensions
State (Government)->Territorial Sovereignty
State (Government)->Economic Sovereignty
State (Government)->Technological Sovereignty
State (Government)->Data Sovereignty
State (Government)->Political Sovereignty
State (Government)->Monetary Sovereignty
State (Government)->Cultural Sovereignty
Citizens->Political Sovereignty
Citizens->Cultural Sovereignty
Citizens->Economic Sovereignty
Citizens->Territorial Sovereignty
External Actors (States, MNCs)->Diplomacy & Alliances
External Actors (States, MNCs)->Trade Policy (Tariffs, Export Controls)
External Actors (States, MNCs)->International Law (WTO, UN)

// Dimensions -> instruments
Territorial Sovereignty->Defence & Deterrence
Territorial Sovereignty->Border & Customs Control
Territorial Sovereignty->Law Enforcement
Economic Sovereignty->Trade Policy (Tariffs, Export Controls)
Economic Sovereignty->Industrial Policy & Subsidy
Economic Sovereignty->Tax Authority
Economic Sovereignty->Regulation (Rule-making)
Economic Sovereignty->Sanctions Regime
Technological Sovereignty->Industrial Policy & Subsidy
Technological Sovereignty->Standards Setting
Technological Sovereignty->Regulation (Rule-making)
Data Sovereignty->Regulation (Rule-making)
Data Sovereignty->Standards Setting
Political Sovereignty->Diplomacy & Alliances
Political Sovereignty->Intelligence Services
Political Sovereignty->Law Enforcement
Cultural Sovereignty->National Media & Public Discourse
Cultural Sovereignty->Language & Education System
Cultural Sovereignty->National Identity & Narrative
Monetary Sovereignty->Payment Rails (Domestic)
Monetary Sovereignty->Central Bank Digital Currency
Monetary Sovereignty->Reserve Currency Access (USD)

// Instruments -> underlying legal / infra stack
Regulation (Rule-making)->Legal System & Courts
Regulation (Rule-making)->Constitution & Treaty Law
Standards Setting->International Law (WTO, UN)
Trade Policy (Tariffs, Export Controls)->International Law (WTO, UN)
Diplomacy & Alliances->International Law (WTO, UN)
Sanctions Regime->SWIFT / Cross-border Payments
Defence & Deterrence->Cyber Defence Capability
Defence & Deterrence->Critical National Infrastructure
Defence & Deterrence->Intelligence Services
Defence & Deterrence->Strategic Doctrine
Intelligence Services->Cyber Defence Capability
Law Enforcement->Legal System & Courts
Border & Customs Control->Critical National Infrastructure
Industrial Policy & Subsidy->Industrial Base / Skills
Industrial Policy & Subsidy->Technical Expertise (in-state)
Tax Authority->Legal System & Courts

// Digital / civic layer
Digital ID & Civic Platforms->Government Cloud
Digital ID & Civic Platforms->Public Key Infrastructure
Government Cloud->Semiconductor Supply Chain
Government Cloud->Energy Supply
Central Bank Digital Currency->Payment Rails (Domestic)
Central Bank Digital Currency->Public Key Infrastructure
Payment Rails (Domestic)->Public Key Infrastructure
SWIFT / Cross-border Payments->Public Key Infrastructure

// Cyber / infra dependencies
Cyber Defence Capability->Encryption Standards
Cyber Defence Capability->Technical Expertise (in-state)
Critical National Infrastructure->Energy Supply
Critical National Infrastructure->Semiconductor Supply Chain
Critical National Infrastructure->Undersea Cable Infrastructure
Critical National Infrastructure->DNS & Internet Routing
Encryption Standards->Public Key Infrastructure

// Supply chain
Semiconductor Supply Chain->Rare Earths & Critical Minerals
Semiconductor Supply Chain->Energy Supply

// Erosion vectors (what puts pressure on the dimensions)
Foreign Platforms (GAFAM, TikTok)->Cross-border Data Flows
Cross-border Data Flows->DNS & Internet Routing
Cross-border Data Flows->Undersea Cable Infrastructure
Capital Markets / Capital Flight->SWIFT / Cross-border Payments
Capital Markets / Capital Flight->Offshore Tax Havens
Cyber Threats (State & Non-state)->Undersea Cable Infrastructure
Cyber Threats (State & Non-state)->DNS & Internet Routing
Foreign Influence Operations->National Media & Public Discourse
Supply Chain Dependency->Semiconductor Supply Chain
Supply Chain Dependency->Rare Earths & Critical Minerals
Supply Chain Dependency->Pharmaceutical Supply
Supply Chain Dependency->Food Supply

// Cultural layer
National Media & Public Discourse->Foreign Platforms (GAFAM, TikTok)
National Identity & Narrative->Language & Education System
National Identity & Narrative->National Media & Public Discourse

// Erosion vectors depending on what the state depends on (for risk propagation)
Economic Sovereignty->Capital Markets / Capital Flight
Data Sovereignty->Cross-border Data Flows
Data Sovereignty->Foreign Platforms (GAFAM, TikTok)
Technological Sovereignty->Supply Chain Dependency
Technological Sovereignty->Foreign Platforms (GAFAM, TikTok)
Territorial Sovereignty->Cyber Threats (State & Non-state)
Cultural Sovereignty->Foreign Influence Operations
Political Sovereignty->Foreign Influence Operations

// Evolution targets (scenarios, not forecasts)
evolve Central Bank Digital Currency 0.50
evolve Technological Sovereignty 0.45
evolve Data Sovereignty 0.55
evolve Cyber Defence Capability 0.60
evolve Digital ID & Civic Platforms 0.65
evolve Semiconductor Supply Chain 0.35

// Zones
note BUILD — differentiation / sovereignty moat [0.70, 0.22]
note BUY / ALLY — rent, partner, coordinate [0.40, 0.88]
note EROSION ZONE — pressure from outside the state [0.55, 0.75]
```

Validator: `OK: 55 components/anchors, 92 edges — no violations.`

---

## Strategic Analysis

### Reading the map at a glance

The sovereignty dimensions fall into two clearly different regimes:

- **Classical (Westphalian) sovereignty** — Territorial, Political, Monetary — sits firmly in **Product (+rental)** territory. The instruments (defence, law enforcement, border control, tax authority, diplomacy) are **Commodity (+utility)** in the sense that every state of any size has them and they behave similarly across states. These are **commoditising** — mature, well-understood, hard to differentiate.

- **Digital-era sovereignty** — Technological, Data, and parts of Cultural — sits in **Custom Built**, with instruments still in transition. These are **differentiating**. In 2023 this is where state strategy is actually being contested (CHIPS Act, EU Chips Act, October 2022 US semiconductor export controls, GDPR/AI Act, Schrems II, TikTok debates).

The **erosion zone** — foreign platforms, cross-border data, capital flight, cyber threats, supply chain dependency — sits in the mid-right: these forces are **already mature** as phenomena, and they apply pressure whether the state engages or not (climatic pattern #5: no choice over evolution).

### a. Differentiation opportunities (top 3) — BUILD

Leading on D = ν·(1−ε). These are the components where a state can still build a durable sovereignty moat in 2023.

1. **Technological Sovereignty** (Custom Built) — the core of the digital-sovereignty contest. Chips, AI compute, 5G/6G stack, quantum. This is where industrial policy, subsidy, and strategic export controls are concentrating (CHIPS Act, EU Chips Act, NATO DIANA). Highest differentiation leverage on the map.
2. **Data Sovereignty** (Custom Built) — rule-making regimes (GDPR, DSA/DMA, India's DPDP, China's PIPL) are actively differentiating states from each other and from a global default. Who defines the regime shapes the market for everyone else.
3. **Cultural Sovereignty** (Product (+rental), but fronting onto an immature Foreign Influence Operations threat) — national identity, language, and discourse are increasingly contested through platform distribution. The *response* to platform-era cultural erosion is genuinely Custom Built right now (DSA risk assessments, online safety regimes, media codes).

Close behind: **Digital ID & Civic Platforms** (Custom → Product (+rental)) and **Cyber Defence Capability** (Custom Built). Both are places a state can still build a moat; both are scheduled to industrialise within 3–5 years.

### b. Commodity-leverage candidates (top 3) — BUY / RENT / ALLY

Leading on K = (1−ν)·ε. These are deep, mature components where "build" is waste.

1. **DNS & Internet Routing** (Commodity (+utility)) — do not try to build national DNS as differentiation. Use standard infrastructure; participate in ICANN/IETF; contribute to protocol evolution rather than fork.
2. **Public Key Infrastructure** (Commodity (+utility)) — use international standards (X.509, Web PKI, IETF protocols). Contribute to standards bodies; do not re-invent.
3. **Undersea Cable Infrastructure** (Commodity (+utility), but physically scarce) — treat as utility where possible; where strategic (landing stations, cable routes), invest via alliance, not solo build. *Note:* though commoditised as a class, specific cable routes are oligopoly assets — coalition-build, don't solo.

Also clearly commodity-leverage: **SWIFT / Cross-border Payments**, **Reserve Currency Access (USD)**, **Payment Rails (Domestic)**. These are strategically important but the state rents participation; it does not build them (unless it is the US, in which case it runs the utility).

### c. Dependency risks (top 3)

Edges where a visible component depends on an immature or fragile foundation. R = ν(a) · (1 − ε(b)).

1. **Monetary Sovereignty → Central Bank Digital Currency** — the state is being pushed (by capital-market innovation, by stablecoins, by China's e-CNY) to lean on a capability that is still **Genesis**. Most CBDCs are in research or pilot phase as of April 2023; only a handful are live (Sand Dollar, e-CNY pilot, eNaira). Shipping monetary policy on Genesis tech is fragile. Manage inertia carefully; do not over-commit architecture.
2. **Defence & Deterrence → Cyber Defence Capability** — a Product (+rental)-era instrument (physical deterrence) leaning on a **Custom Built** cyber stack. Capability quality varies wildly between states and inside states across departments. Private sector (CrowdStrike, Mandiant, Palo Alto) is further along than most state defences.
3. **Technological Sovereignty → Supply Chain Dependency** — the whole *project* of technological sovereignty depends on a Product (+rental)-stage external supply chain (TSMC, ASML, Samsung, Chinese rare earth refining) that the state neither owns nor fully controls. Industrialising supply chain resilience is a decade-long effort and there is no way to bypass this dependency in the short term.

Honourable mentions: **Government Cloud → Semiconductor Supply Chain** (all sovereign clouds are one fab bottleneck from distress); **Data Sovereignty → Cross-border Data Flows** (Schrems II adequacy regime is unstable infrastructure for a strategic pillar).

### d. Suggested gameplays

Cited by number from Wardley's 61-play catalogue.

- **#18 Industrial Policy** on Technological Sovereignty, Semiconductor Supply Chain, Digital ID — this is the canonical sovereign play for accelerating evolution of strategic components. CHIPS Act and EU Chips Act are the live examples.
- **#36 Directed investment** on Cyber Defence Capability, CBDC, Technical Expertise (in-state). Concentrated funding into the Custom Built components that will shape the next decade.
- **#41 Alliances** on Semiconductor Supply Chain, Rare Earths & Critical Minerals, Undersea Cable Infrastructure — solo sovereignty in these layers is economically irrational for all but the largest states. Build minilateral coalitions (Chip 4, G7 Critical Raw Materials, Five Eyes).
- **#30 Standards game** on Data Sovereignty, Encryption Standards, AI regulation — whoever writes the regulatory regime first (GDPR effect, AI Act effect) shapes the global market and imposes switching costs on others.
- **#15 Open Approaches** on Digital ID (cf. Estonia's X-Road, India's DPI / ONDC / Aadhaar) — commoditise the platform to enable higher-order civic innovation on top (climatic pattern #10: higher-order systems create new sources of worth).
- **#20 Patents & IPR** and **#22 Limitation of competition** on strategic export controls — already in use (US October 2022 export controls on advanced chips to China; the Entity List).
- **#43 Sensing Engines (ILC)** — the state's intelligence services and industrial policy apparatus should systematically read ecosystem signals to detect where to direct investment. Most state industrial policy is the opposite — centrally planned without ecosystem signal.
- **#44 Tower & Moat** on AI model regulation — position early (Bletchley Park summit was Nov 2023; the AI Safety Institute model) and dig in.
- **#45 Two factor** for Digital ID — citizens AND service providers must both be on it for the network effect to compound. India's Aadhaar-UPI stack is the canonical example.
- **#17 Co-operation** on Climate / Transboundary Externalities — sovereignty is structurally inadequate for transboundary problems; this is a category that requires pooled sovereignty (EU ETS, Paris Agreement) rather than national assertion.

### e. Doctrine violations and observations

- ✓ **#10 Know your users** — three anchors (State, Citizens, External Actors) reflect the real structure. Sovereignty is defined *relationally* against external actors, so including them is not optional.
- ✓ **#9 Think small (know details)** — the map decomposes sovereignty into 55 components across seven dimensions rather than treating "sovereignty" as one node.
- ⚠ **#13 Manage inertia** — the map implies significant inertia at the State anchor. Most state apparatus is the literal embodiment of inertia forms #2 (sunk capital in existing arrangements), #3 (political capital of past decisions), #4 (human capital of civil service), and #16 (rewards and culture). Any evolution target on the map has to explicitly budget inertia management.
- ⚠ **#7 Use appropriate methods** — states tend to apply bureaucratic (Commodity (+utility)) management to their Custom Built digital-sovereignty work. Technological Sovereignty needs pioneer-style teams (government digital services, GDS, 18F, USDS) rather than the default procurement-and-programme-office method.
- ⚠ **#22 Use standards where appropriate** — legitimate risk of premature standardisation on AI Act and DSA: the regulated components are still Custom Built, so the rule set is writing norms ahead of evidence. Defensible as a **#30 Standards game** play, but doctrine says don't standardise at Stage I/II — note the tension.
- ⚠ **#38 There is no core** — classical (Westphalian) sovereignty is already being eroded at its commodity foundations (payment rails, data flows, platform distribution) while the state asserts sovereignty at newer layers. Treat the map as a *generation transition* (territorial → digital sovereignty), not a static set.

### f. Climatic context

Which of Wardley's 27 climatic patterns are actively shaping this map.

- **#3 Everything evolves** — Territorial and Political sovereignty, once clearly differentiating, are now commodity state functions; Technological and Data sovereignty are the new differentiators. Tomorrow's commodities are today's Custom Built.
- **#5 No choice over evolution** — states cannot opt out of digital-sovereignty questions. "We will stay out of AI regulation" is not a strategy; it's a deferral. The erosion vectors act whether the state engages or not.
- **#11 Future value is inversely proportional to certainty** — the highest-value sovereignty moves are in the most uncertain zones (AI, CBDC, quantum, cyber norms). Do not over-invest in already-certain areas.
- **#15–17 Inertia** — states are the archetypal inertia-loaded actors. Large states have the most inertia at exactly the moment punctuated-equilibrium change is crossing their map.
- **#21 Peace / War / Wonder** — the classical sovereignty stack is in Peace (stable paradigm); the digital-sovereignty stack is in War (industrialisation boundary crossing). Both need different strategies.
- **#22 Two forms of disruption** — this landscape has both: Genesis-driven (quantum, AGI, CBDC) AND Product-to-utility (cloud, payment rails, identity). The state needs distinct playbooks for each.
- **#23 A war causes organisations to evolve** — the US-China tech decoupling IS the war, driving rapid M&A, subsidy, and structural change in the chip industry and adjacent layers. Expect consolidation and vertical integration of formerly open supply chains.
- **#27 Product-to-utility punctuated equilibrium** — cloud, payment rails, and identity are all crossing the Product-to-utility boundary. States that do not have a strategy here will discover they have no sovereignty over their own digital plumbing.

### g. Deep-placement notes

1. **Technological Sovereignty** — initial cheat-sheet placed this at ε≈0.30 (Custom Built). Checked against 2023 signals: CHIPS and Science Act passed August 2022; EU Chips Act provisional agreement April 2023; Biden's October 2022 BIS export controls; AUKUS pillar 2; Chip 4 alliance discussions. Publication types are heavily "build / construct / awareness" with case studies starting to accumulate. Confirmed Custom Built, near the Stage II/III boundary. The *concept* is industrialising even as implementations remain bespoke per state.
2. **Data Sovereignty** — initial ε≈0.35 (Custom Built). Signals: GDPR mature but its *sovereign* framing (vs. simply privacy) is recent; Schrems II (July 2020) opened a structural instability in transatlantic data; India's DPDP was in draft through 2023; China's PIPL (2021) live; data localisation proliferating. Many vendors of data-residency tooling (Cloudflare Data Localisation Suite, AWS Sovereign Cloud) appearing. Holding at early Custom Built — the *tooling* is productising even as the *doctrine* is Custom Built.
3. **Central Bank Digital Currency** — initial ε=0.15 (late Genesis). Signals: Bahamas Sand Dollar live (2020); Nigeria eNaira live (2021); China e-CNY in extended pilot; ECB digital euro investigation phase (2021–2023); Fed still researching. BIS paper counts and mCBDC experiments (Project mBridge, Project Icebreaker) are "describing the wonder" and "construct / learning" publication types. Confirmed late Genesis edge of Custom Built. Evolution target 0.50 within ~5 years is aggressive but plausible given Chinese lead.
4. **Cyber Defence Capability** — initial ε≈0.40 (mid Custom Built). Signals: private sector (CrowdStrike, Mandiant, SentinelOne) clearly Stage III, but *state* cyber defence capability varies enormously — US and Israel and UK near Stage III; many states near Stage II. Since the map is about state sovereignty, using the state capability placement rather than private sector. Confirmed Custom Built, widely variable — flag as "in transition" with uncertainty range ε ∈ [0.35, 0.55].
5. **Semiconductor Supply Chain** — initial ε≈0.50 (Product (+rental) boundary). Signals: TSMC and Samsung foundries are productised utility-like services; ASML is a product monopoly at EUV; but supply-chain *resilience* as a capability states buy or build is Custom Built. Held at 0.50 (Stage II/III boundary) reflecting the fact that the thing the state cares about — the *secure supply* — is distinct from the Commodity (+utility) substrate. Relevant export-control enforcement and CHIPS Act subsidies are actively moving this.

### h. What is differentiating vs. commoditising

Direct answer to the user's final question.

**Commoditising (treat as utility; rent or coalition-build):**
- Classical Westphalian instruments: Law Enforcement, Tax Authority, Border & Customs Control, Legal System & Courts, Diplomacy
- Most internet plumbing: DNS, PKI, Undersea Cables, SWIFT, Reserve Currency access
- Payment Rails (Domestic) and Payment Processing
- Language & Education System (stable, mature, essential utility — not a differentiator at the *system* level even though curriculum content matters)
- Food, Energy, Pharmaceutical, Critical National Infrastructure (physical commodities, though supply-chain resilience on top is still Custom)

**Differentiating (build, invest, set standards):**
- Technological Sovereignty (chips, AI, quantum stack)
- Data Sovereignty (regulatory regimes, residency, transfer rules)
- Central Bank Digital Currency (Genesis — options thinking, not roadmap)
- Digital ID & Civic Platforms (India stack, Estonia stack — differentiators that become commodities if opened; cf. gameplay #15)
- Cyber Defence Capability (state-level; private-sector equivalents are Product (+rental))
- Response regimes to Foreign Platforms and Foreign Influence Operations (DSA, AI Act, online safety laws) — the *rules*, not the platforms themselves
- Industrial Policy & Subsidy as a re-emergent instrument (was a Custom / Product (+rental) tool until 2020; now re-industrialising into a Product (+rental)-stage doctrine complete with playbooks and case studies)

**Crossing over right now:**
- Supply Chain Dependency (from a background constraint to a front-of-mind strategic component — climatic #27 punctuated equilibrium)
- Cross-border Data Flows (from Commodity (+utility) infrastructure to a contested strategic category with residency rules stacked on top)
- Foreign Platforms (Product (+rental), but subject to sovereignty reassertion — the rules around them are Custom Built even though the platforms are Product (+rental))

### h(bis). Inertia watch

From the 17 forms, the ones that bite hardest in this map:

- **#2 Sunk capital** — legacy arms budgets, legacy data centres, legacy platform dependencies. Heavy in Territorial and Political Sovereignty dimensions.
- **#4 Human capital** — civil service skillsets for an analogue era; deep shortage of engineering talent inside government.
- **#3 Political capital** — every sovereign decision was taken by someone who is still around. Reversing course has political cost.
- **#13 Price-competition loss / #14 Strategic-control loss** — the classic objections to cloud dependency, foreign platform dependency, reserve-currency dependency.
- **#16 Rewards and culture** — civil-service incentives do not reward the pioneer-style work required for Custom Built digital sovereignty (cf. doctrine #7 and #33).

### i. Caveat

Evolution trajectories in this map — the `evolve` arrows — are **scenarios, not forecasts**. Wardley's climatic pattern #18 is unambiguous: *"you cannot measure evolution over time or adoption."* Treat target positions as directional commitments to test, re-map, and revise.

Sovereignty is uniquely subject to adversarial reshaping: the map is *contested* between players with asymmetric stakes (states, platforms, citizens, other states). Expect the map of April 2024 to look meaningfully different from April 2023's — especially in the Technological, Data, and Cyber layers. Re-map annually at minimum; quarterly for the digital-sovereignty dimensions.
