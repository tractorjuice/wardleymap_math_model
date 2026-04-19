# Wardley Map — Game Economies in Modern Live-Service Games (Nov 2023)

## Scenario

Map the landscape of game economies in modern live-service games. Include player motivation, engagement systems, in-game currency, items and loot, trading, monetisation, live-ops, analytics, anti-cheat, and regulation. Identify what is differentiating vs. commoditising, and flag where game economies are fragile or under regulatory pressure.

Two anchors: the **Player** (who pays attention, time, and money) and the **Publisher / Studio** (who extracts sustainable revenue from a live service). Mapping the economy as a two-sided chain is essential because most regulatory and moral-hazard tension sits at the interface between them.

---

## Map (OWM)

```owm
title Game Economies in Modern Live-Service Games (Nov 2023)
style wardley

// Anchors — two user types
anchor Player [0.98, 0.55]
anchor Publisher / Studio [0.95, 0.60]

// ===== Player-facing experience =====
component Progression & Status [0.90, 0.45]
component In-Game Store [0.88, 0.70]
component Battle Pass [0.87, 0.65]
component Cosmetic Items & Skins [0.83, 0.70]
component Seasonal Events / LTMs [0.82, 0.55]
component Daily Quests & Challenges [0.80, 0.70]
component Social / Clan Features [0.78, 0.60]

// ===== Currency & loot systems =====
component Loot Boxes / Gacha [0.76, 0.60]
component Premium (Hard) Currency [0.74, 0.72]
component Soft (Earned) Currency [0.72, 0.78]
component Crafting / Upgrade Materials [0.68, 0.58]
component Drop-Rate / Reward Tables [0.55, 0.55]
component Player Inventory [0.50, 0.80]

// ===== Trading & secondary markets =====
component RMT / Grey Market [0.65, 0.30]
component Player-to-Player Marketplace [0.60, 0.35]
component In-Game Player Trading [0.56, 0.40]

// ===== Monetisation =====
component Microtransaction IAP [0.70, 0.80]
component Subscriptions / Game Pass [0.68, 0.65]
component Rewarded Ads (mobile) [0.62, 0.82]

// ===== Live-ops & content cadence =====
component Live-Ops Content Pipeline [0.55, 0.55]
component Balance Patching [0.50, 0.60]
component Seasonal Roadmap [0.52, 0.50]
component Event Scheduling / LiveOps Tooling [0.42, 0.55]

// ===== Analytics, ML & experimentation =====
component A/B Testing Platform [0.48, 0.70]
component LTV / Whale Modelling [0.46, 0.45]
component Churn Prediction (ML) [0.44, 0.40]
component Player Telemetry [0.40, 0.72]
component Segmentation & Cohorting [0.35, 0.60]
component Data Warehouse [0.22, 0.82]

// ===== Anti-cheat, security & integrity =====
component Anti-Cheat (client kernel) [0.48, 0.55]
component Fraud / Chargeback Detection [0.46, 0.65]
component Server-Side Validation [0.40, 0.50]
component KYC / Age Verification [0.38, 0.55]
component Account Security / 2FA [0.30, 0.80]

// ===== Regulation & compliance =====
component Gambling-Law Compliance [0.50, 0.35]
component Loot Box Regulation [0.45, 0.25]
component Consumer-Protection / UK CMA [0.44, 0.28]
component Content Rating (ESRB/PEGI) [0.42, 0.80]
component Regional Age-Gating (China/KR) [0.34, 0.45]
component Privacy (GDPR/COPPA) [0.30, 0.70]

// ===== Infrastructure =====
component Game Servers / Netcode [0.32, 0.70]
component Platform Payment Rails [0.26, 0.90]
component Storefront Commission (30%) [0.24, 0.88]
component CDN / Patch Distribution [0.20, 0.90]
component Identity / Auth [0.18, 0.90]
component Cloud Compute [0.12, 0.92]
component Object Storage [0.10, 0.92]

// ===== Dependencies — player side =====
Player->Progression & Status
Player->Cosmetic Items & Skins
Player->Battle Pass
Player->Seasonal Events / LTMs
Player->Daily Quests & Challenges
Player->Social / Clan Features
Player->In-Game Store

Progression & Status->Soft (Earned) Currency
Progression & Status->Daily Quests & Challenges
Progression & Status->Crafting / Upgrade Materials
Battle Pass->Seasonal Events / LTMs
Battle Pass->Soft (Earned) Currency
Battle Pass->Cosmetic Items & Skins
Daily Quests & Challenges->Soft (Earned) Currency
Seasonal Events / LTMs->Live-Ops Content Pipeline

In-Game Store->Premium (Hard) Currency
In-Game Store->Cosmetic Items & Skins
In-Game Store->Microtransaction IAP
Cosmetic Items & Skins->Player Inventory
Cosmetic Items & Skins->Loot Boxes / Gacha
Loot Boxes / Gacha->Drop-Rate / Reward Tables
Loot Boxes / Gacha->Premium (Hard) Currency
Loot Boxes / Gacha->Loot Box Regulation
Loot Boxes / Gacha->Gambling-Law Compliance

Crafting / Upgrade Materials->Player Inventory
Player Inventory->Data Warehouse

// Trading
In-Game Player Trading->Player Inventory
In-Game Player Trading->Server-Side Validation
Player-to-Player Marketplace->In-Game Player Trading
Player-to-Player Marketplace->Fraud / Chargeback Detection
RMT / Grey Market->Player-to-Player Marketplace

// ===== Dependencies — publisher side =====
Publisher / Studio->In-Game Store
Publisher / Studio->Live-Ops Content Pipeline
Publisher / Studio->Player Telemetry
Publisher / Studio->Microtransaction IAP
Publisher / Studio->Subscriptions / Game Pass
Publisher / Studio->Rewarded Ads (mobile)

// Monetisation
Microtransaction IAP->Platform Payment Rails
Microtransaction IAP->Storefront Commission (30%)
Subscriptions / Game Pass->Platform Payment Rails
Rewarded Ads (mobile)->Platform Payment Rails

// Live-ops
Live-Ops Content Pipeline->Balance Patching
Live-Ops Content Pipeline->Seasonal Roadmap
Live-Ops Content Pipeline->Event Scheduling / LiveOps Tooling
Live-Ops Content Pipeline->Game Servers / Netcode
Balance Patching->Player Telemetry
Seasonal Roadmap->Segmentation & Cohorting

// Analytics
Player Telemetry->Data Warehouse
A/B Testing Platform->Player Telemetry
A/B Testing Platform->Segmentation & Cohorting
LTV / Whale Modelling->Segmentation & Cohorting
LTV / Whale Modelling->Data Warehouse
Segmentation & Cohorting->Data Warehouse
Churn Prediction (ML)->Data Warehouse
Churn Prediction (ML)->Player Telemetry

// Integrity
Anti-Cheat (client kernel)->Server-Side Validation
Server-Side Validation->Game Servers / Netcode
Fraud / Chargeback Detection->Platform Payment Rails
Fraud / Chargeback Detection->Account Security / 2FA
Account Security / 2FA->Identity / Auth
KYC / Age Verification->Identity / Auth
KYC / Age Verification->Regional Age-Gating (China/KR)

// Regulation wiring
Loot Boxes / Gacha->Consumer-Protection / UK CMA
Microtransaction IAP->Privacy (GDPR/COPPA)
Player Telemetry->Privacy (GDPR/COPPA)
In-Game Store->Content Rating (ESRB/PEGI)
Gambling-Law Compliance->Loot Box Regulation

// Infra
Game Servers / Netcode->Cloud Compute
Game Servers / Netcode->CDN / Patch Distribution
Data Warehouse->Cloud Compute
Data Warehouse->Object Storage
CDN / Patch Distribution->Cloud Compute
Platform Payment Rails->Identity / Auth

// Evolve targets
evolve Loot Boxes / Gacha 0.45
evolve Loot Box Regulation 0.55
evolve Churn Prediction (ML) 0.60
evolve LTV / Whale Modelling 0.60
evolve Subscriptions / Game Pass 0.78
evolve Event Scheduling / LiveOps Tooling 0.72

note Differentiation zone [0.72, 0.30]
note Commoditising infra [0.20, 0.88]
note Regulatory pressure rising [0.45, 0.30]
```

---

## Strategic analysis

### a. Differentiation opportunities (top 3 — BUILD)

1. **Progression & Status** (Custom Built) — the deepest human-behavioural moat. Every dominant live-service (Fortnite, Destiny, Genshin, Warzone, Apex) differentiates on the *shape* of its progression loop (seasonal resets, mastery trees, prestige systems). Generic engagement systems are increasingly Product (+rental), but the *specific* progression fantasy remains Stage II. Highest differentiation leverage.
2. **Live-Ops Content Pipeline** (Product (+rental), still industrialising) — cadence and theme coherence are what keep Fortnite ahead of imitators. Stage II–III hybrid: tooling is maturing (hence the `evolve` arrow on Event Scheduling) but the *creative product* sitting on top is bespoke.
3. **LTV / Whale Modelling + Churn Prediction** (Custom Built) — the ML behind dynamic offers, targeted pricing, and win-back flows is where the money really is. Publishers who own first-party behavioural models out-monetise those who rent generic segmentation. Note the ethical ambiguity: this is differentiation *and* the locus of regulatory interest.

### b. Commodity-leverage candidates (top 3 — RENT / BUY)

1. **Platform Payment Rails** (Commodity (+utility), ε≈0.90) — Apple IAP, Google Play Billing, Xbox Live, PSN, Steam. You rent these, and rental cost (the 30% storefront commission) is itself Stage IV.
2. **Cloud Compute + Object Storage + CDN** (all Commodity (+utility)) — hyperscaler utilities. Epic, Activision, and EA run on AWS/Azure/GCP at this point; even Nintendo does for cloud-save and matchmaking. Rent, don't build.
3. **A/B Testing Platform + Data Warehouse** (Product (+rental) → Commodity (+utility)) — Optimizely / LaunchDarkly / Unleash for experimentation; Snowflake / BigQuery for warehouse. These became commodity in 2021–2023; building in-house is a doctrine violation in 2023.

### c. Dependency risks (top 3)

1. **In-Game Store -> Content Rating (ESRB/PEGI) and Loot Boxes / Gacha -> Loot Box Regulation / UK CMA** — highly visible monetisation surfaces depend on regulatory regimes that are themselves still Stage I–II (Loot Box Regulation ε=0.25, Consumer-Protection ε=0.28). A single ruling in the UK, Germany, or the Netherlands can force a store redesign overnight. The Belgian 2018 ruling and the 2022 Dutch Supreme Court reversal already reshaped Overwatch, FIFA Ultimate Team, and Diablo Immortal. **This is the single most fragile edge in the whole map.**
2. **Microtransaction IAP -> Storefront Commission (30%)** — the entire upstream monetisation chain hangs on a commission rate that is itself under pressure (Epic v. Apple, EU DMA, Fortnite's direct-pay experiment). A visible, high-margin component (Stage IV IAP) depends on a utility whose *pricing* is being renegotiated. If the 30% takes a haircut, it reshapes the unit economics of every game in this map.
3. **Battle Pass -> Seasonal Events / LTMs -> Live-Ops Content Pipeline** — user-facing Battle Pass (now Product (+rental) and commonly expected) depends on a content pipeline that is still Custom Built and deeply studio-specific. A content-factory stumble (delayed season, burnt-out team) is an existential brand risk, as shown by Halo Infinite's Season 2 fiasco.

### d. Suggested gameplays (from Wardley's 61)

- **#1 Focus on user needs** on Progression & Status and Social / Clan Features — most engagement failures are misreadings of *why* a player shows up. Anchor the map and the roadmap on player needs, not D7 retention.
- **#36 Directed investment** on Live-Ops Content Pipeline and LTV / Whale Modelling — the two highest-D components deserve disproportionate engineering headcount.
- **#29 Harvesting** on A/B Testing, Data Warehouse, Cloud Compute, Payment Rails — let the market build it; consume the winner.
- **#43 Sensing Engines (ILC)** on Churn Prediction and Segmentation — treat the ML stack as an Innovate-Leverage-Commoditise pipeline: innovate on in-house signals, leverage the cluster, commoditise the rest to vendors.
- **#45 Two-factor markets** — trading / marketplace / UGC economies are two-sided; reinforce both sides (creators + buyers). Roblox and Fortnite Creator are the reference plays.
- **#15 Open Approaches** on Drop-Rate Transparency — Apple's 2017 loot-box-disclosure requirement and China's drop-rate disclosure law effectively forced the industry to open-source this. Publishers who embrace it ahead of regulation build trust AND reduce regulatory exposure.
- **#56 First mover** on Loot-Box Regulation compliance — jurisdictions that have not yet ruled (UK, US state-level) will rule; a publisher that standardises disclosure and spend caps *ahead* of regulation reduces their own inertia when the law lands.
- **#37 Exploiting constraint** on Storefront Commission — Epic Games Store's 12% and direct-web-payment schemes are a constraint-exploitation play against Apple/Google 30%.
- **#42 Co-creation** via UGC / creator economies — Roblox, Fortnite Creator, Minecraft marketplace. Deepens the two-sided moat and generates content that the publisher cannot pay for internally.
- **#11 FUD** (defensive, ethically grey) — incumbents often deploy FUD around new monetisation models ("subscription fatigue", "loot-box panic"). Flagged only to identify it in the landscape, not recommended.

### e. Doctrine notes / violations

- OK **#1 Focus on user needs** — two anchors correctly distinguish Player and Publisher. Most industry maps conflate them, leading to engagement-metric gaming that destroys player trust.
- OK **#10 Know your users** — multiple anchors modelled.
- WARN **#13 Manage inertia** — `Anti-Cheat (client kernel)` has deep supplier inertia: ring-0 drivers (Vanguard, EAC, BattlEye) are hard to swap, and kernel access creates user trust backlash (form #14 Strategic-control loss over users' own machines).
- WARN **#2 Use a systematic mechanism of learning** — Balance Patching depends on Player Telemetry; many studios still ship balance changes on designer intuition rather than closed-loop telemetry. A doctrine miss.
- WARN **#11 Be transparent** — RMT / Grey Market and loot-box odds remain murky in many titles. Non-transparency is both doctrinally wrong and increasingly a regulatory liability.
- WARN **#9 Use appropriate methods** — applying Stage IV management (metric-driven, efficiency) to Stage II content design is a common failure mode in big publishers (Activision's mid-2010s sequelisation strategy).

### f. Climatic context

Actively shaping this map:

- **#3 Everything evolves** — Loot Boxes, once Stage III and the dominant monetisation, are being forced *back* down evolution by regulation AND by user backlash; Battle Pass (Stage III) is the natural successor. This is a rare "regression under social pressure" case.
- **#4 Multi-wave evolution** — monetisation itself: retail → expansion packs → DLC → microtransactions → battle pass → subscriptions / game-pass. Each wave has its own chasm. Sub/game-pass is the current left-edge wave.
- **#15 Inertia from past success** — publishers who built on loot-box revenue (EA's FIFA Ultimate Team) face enormous inertia adapting to a post-loot-box world. Consumer-side inertia also: players *like* the dopamine loop.
- **#16 Inertia from co-evolution of practices** — the *practice* of whale-targeted monetisation co-evolves with LTV modelling; changing either requires changing both.
- **#27 Product-to-utility punctuated equilibrium** — A/B testing, warehouse, payment rails, ID / auth all crossed the Product → Commodity (+utility) chasm in 2019–2023. Studios still running self-hosted equivalents are burning money.
- **#20 Commoditisation enables new genesis** — the utility infra below ν=0.30 is what made the *current* wave of live-service games economically viable; expect the next wave (on-chain economies, AI-generated content, social sims) to genesis *on top of* this utility base.

### g. Deep-placement notes

Four components got a closer look (Nov 2023 context); the rest use cheat-sheet priors.

- **Loot Boxes / Gacha** — initial cheat-sheet placed this around ε≈0.65 (solid Product +rental), because it's a widely-implemented feature. Closer look: regulatory contraction (Belgium 2018, NL Supreme Court 2022, UK CMA 2022 principles, Austria ruling 2023, China 2017 disclosure, Japan Kompu Gacha ban) has *reversed* diffusion in major markets. EA removed FUT packs from Belgium, Diablo Immortal is banned in NL. I placed at ε=0.60 with an `evolve` arrow back to 0.45 — an unusual *leftward* evolution under social/legal pressure. This is the "reverse-direction" component in the map.
- **Loot Box Regulation** — initial cheat-sheet would put at ε≈0.35 (Custom Built, emerging legal theory). Closer look: UK CMA guidance, NL/BE case law, China disclosure, EU DSA all indicate standardising Stage II–III. Placed at ε=0.25 with `evolve` to 0.55 — regulation is actively industrialising and will become Stage III within 2–4 years.
- **Battle Pass** — initial cheat-sheet ε≈0.55 (feels Product). Closer look: the *format* is now universal (Fortnite, Apex, Warzone, Destiny, Rocket League, Overwatch 2, Diablo IV, Genshin, FIFA, CS2, Marvel Snap) with well-understood implementation patterns and vendor platforms (LiveOps Group / Brainblocks-style tools) — ε=0.65 (Product +rental, late). It is *the* replacement play for loot boxes and is itself now being scrutinised (UK CMA "time-limited pressure").
- **Anti-Cheat (client kernel)** — initial cheat-sheet ε≈0.65 (Product). Closer look: Riot Vanguard's controversy, kernel-level integrations only now standardising, EAC/BattlEye/Denuvo fragmentation. Placed at ε=0.55 (early Product +rental, still emerging). Expect consolidation and a move to ε~0.70 over 2–3 years as Windows/console OSes expose standard attestation APIs.

Components that stayed at cheat-sheet defaults: cloud/CDN/storage/auth/payments (obvious Commodity (+utility)), daily quests/cosmetics (obvious Product (+rental)), progression systems (obvious Custom Built to Product (+rental) depending on studio).

### h. Caveat

Evolution trajectories (`evolve` arrows) are **scenarios, not forecasts**. Wardley's climatic pattern #18 applies: *"you cannot measure evolution over time or adoption."* The leftward evolution on Loot Boxes in particular is a scenario driven by continuing regulatory pressure and consumer backlash — a single US federal preemption or industry self-regulation compromise could flip the direction.

---

## What's differentiating vs. commoditising (summary view)

| Differentiating (BUILD) | Commoditising (BUY / RENT) |
|---|---|
| Progression & Status | Platform Payment Rails |
| Live-Ops Content Pipeline | Cloud Compute / Storage / CDN |
| LTV / Whale Modelling | A/B Testing Platform |
| Churn Prediction (ML) | Data Warehouse |
| Seasonal Roadmap | Identity / Auth |
| Social / Clan Features (UGC / creator layer) | Rewarded Ads SDKs (mobile) |
| Anti-Cheat integrations (for now) | Content Rating submission workflows |

## Where game economies are fragile / under regulatory pressure

- **Loot boxes / gacha** — the biggest fragility. Legal in Japan, China, US; restricted or banned in Belgium, NL, ongoing UK CMA review, Austrian courts ruling against. Edge `Loot Boxes / Gacha -> Loot Box Regulation / UK CMA` is the single most-exposed edge.
- **Targeted monetisation of minors** — UK Age-Appropriate Design Code, California AADC (struck down Sept 2023 but being reworked), EU DSA Article 28. Any LTV model that segments on age is regulatory thin-ice.
- **Storefront commission (30%)** — Epic v. Apple, EU DMA, Korean law (2021 law requiring alternative billing). The monetisation base rate is in flux.
- **Dark patterns** — UK CMA 2022 principles on online choice architecture explicitly call out in-game purchase flows. Visual scarcity timers, currency obfuscation (buy 500 gems, item costs 450, next item costs 100) are being scrutinised.
- **RMT / grey market** — intrinsically fragile because it depends on tolerance from platform holders, creates chargeback / fraud liability, and invites money-laundering scrutiny.
- **Kernel-level anti-cheat** — user-trust and privacy fragility, especially in EU (GDPR + principle of minimum processing). A ruling that kernel drivers collect excessive personal data could nuke the current anti-cheat architecture.
- **Addictive-design lawsuits** — Fortnite $520M FTC settlement (Dec 2022) was a shot across the bow. Expect similar around dopamine-loop engagement systems.

## Validator output

```
OK: 49 components/anchors, 73 edges — no violations.
```
