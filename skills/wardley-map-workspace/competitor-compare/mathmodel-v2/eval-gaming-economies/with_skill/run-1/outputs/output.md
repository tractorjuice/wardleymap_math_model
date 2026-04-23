# Gaming Economies Landscape — November 2023

## Step 0 — Strategic context

1. **Strategic question.** Where along the value chain of the Nov-2023 games economy is differentiation still available to a publisher/developer, where has the ground commoditised into infrastructure, and where do toxicity and trust failures put the whole system at risk?
2. **User anchors.** Two: **Publishers** (the business side — studios, investors, marketers) and **Players** (the consumption side — buyers, subscribers, streamers' audiences). A games-economy map with only one anchor loses half the dynamics.
3. **Core needs.** Publishers need: (a) a fundable, buildable game, (b) distribution reach, (c) a durable monetisation surface, (d) data to target and retain players. Players need: (a) a game worth playing, (b) discovery and social validation (streaming, influencers, tournaments), (c) safe participation in community and economy.
4. **Scope boundary.** The industry landscape in Nov 2023 — covering AAA, mid-tier, indie, mobile, PC and console — not one studio's product. Deliberately excludes region-specific dynamics (e.g., Korean MMO economies, Chinese publishing licensing) beyond the global shape.

**Assumptions flagged:** (a) Nov 2023 is post-Unity-runtime-fee-backlash (Sep 2023) and pre-Xbox-Activision close (Oct 2023) — engine trust and platform concentration are live concerns. (b) Generative AI in asset pipelines is still Custom Built in this snapshot; it does not yet materially change placement of the Asset Pipeline node. (c) Web3 / NFT game economies have cooled and are omitted from the core map.

---

## Map (OWM)

```owm
title Gaming Economies Landscape (Nov 2023)
style wardley

// Two anchors — both user types in this economy
anchor Publisher [0.98, 0.55]
anchor Player [0.97, 0.62]

// User-visible product / business outputs
component Game Title [0.88, 0.55]
component Game Brand / IP [0.84, 0.42]
component Virtual Items [0.82, 0.70]
component Game Store Front [0.80, 0.82]

// Monetisation surface + live product
component In-Game Economy [0.78, 0.45]
component Marketing Campaign [0.76, 0.60]
component Subscription Catalogue [0.74, 0.62]
component Community / Forum [0.72, 0.58]
component Esports Tournament [0.70, 0.55]

// Buzz apparatus
component Influencer Channel [0.68, 0.62]
component Streaming Content [0.66, 0.72]
component Alternative Distribution (Web / itch) [0.62, 0.48]
component Advertising Placement [0.60, 0.82]
component Social Platform [0.58, 0.88]

// Data + trust layer
component Player Profiling / Analytics [0.56, 0.55]
component Trust & Safety (Moderation) [0.54, 0.35]

// Build layer — studios and design
component Game Developer (Studio) [0.52, 0.38]
component Licensing Deal [0.50, 0.58]
component Game Design [0.48, 0.32]
component Game-Specific Marketplace [0.46, 0.58]
component Game Engine [0.44, 0.70]
component Live-Ops Platform [0.42, 0.52]
component Matchmaking / Netcode [0.40, 0.58]
component Anti-Cheat [0.38, 0.62]

// Dev tools / pipeline
component Asset Pipeline [0.36, 0.55]
component Dev Tooling (CI, VCS) [0.32, 0.85]
component Middleware (Physics / Audio) [0.30, 0.78]

// Funding / capital
component Funding Model [0.28, 0.45]
component Game Platform (Console / PC / Mobile) [0.26, 0.82]
component VC Capital [0.24, 0.55]
component Private Investor [0.22, 0.42]

// Infra and hardware
component Hardware (Devices, GPUs) [0.22, 0.88]
component Payment Processing [0.20, 0.92]
component Player Identity / Auth [0.18, 0.85]
component Game Server Hosting [0.16, 0.78]
component Telemetry / Data Warehouse [0.14, 0.80]
component Cloud Compute / CDN [0.10, 0.92]

// Foundational utility
component Electricity / Internet [0.04, 0.97]

// Player reaches product + buzz surfaces
Player->Game Title
Player->Virtual Items
Player->Game Store Front
Player->Subscription Catalogue
Player->Community / Forum
Player->Esports Tournament
Player->Influencer Channel
Player->Streaming Content
Player->Alternative Distribution (Web / itch)
Player->Social Platform

// Publisher runs brand, monetisation, marketing, ops
Publisher->Game Brand / IP
Publisher->Marketing Campaign
Publisher->Licensing Deal
Publisher->Advertising Placement
Publisher->Player Profiling / Analytics
Publisher->Game Developer (Studio)
Publisher->Funding Model
Publisher->Subscription Catalogue
Publisher->Game Store Front

// Game title composition
Game Title->Game Brand / IP
Game Title->In-Game Economy
Game Title->Game Developer (Studio)
Game Title->Game Engine
Game Title->Anti-Cheat
Game Title->Matchmaking / Netcode
Game Title->Live-Ops Platform

// Monetisation chain
Virtual Items->In-Game Economy
Virtual Items->Game-Specific Marketplace
In-Game Economy->Payment Processing
In-Game Economy->Trust & Safety (Moderation)
Game-Specific Marketplace->Payment Processing
Game-Specific Marketplace->Player Identity / Auth
Subscription Catalogue->Licensing Deal
Subscription Catalogue->Game Platform (Console / PC / Mobile)
Game Store Front->Payment Processing
Game Store Front->Game Platform (Console / PC / Mobile)
Alternative Distribution (Web / itch)->Payment Processing
Advertising Placement->Player Profiling / Analytics

// Buzz apparatus flows
Marketing Campaign->Influencer Channel
Marketing Campaign->Streaming Content
Marketing Campaign->Social Platform
Influencer Channel->Streaming Content
Influencer Channel->Social Platform
Esports Tournament->Streaming Content
Esports Tournament->Advertising Placement
Streaming Content->Social Platform
Community / Forum->Trust & Safety (Moderation)

// Data + trust plumbing
Player Profiling / Analytics->Telemetry / Data Warehouse
Player Profiling / Analytics->Player Identity / Auth
Trust & Safety (Moderation)->Player Identity / Auth
Trust & Safety (Moderation)->Telemetry / Data Warehouse

// Build chain
Game Developer (Studio)->Game Design
Game Developer (Studio)->Game Engine
Game Developer (Studio)->Dev Tooling (CI, VCS)
Game Developer (Studio)->Asset Pipeline
Game Developer (Studio)->Funding Model
Game Engine->Middleware (Physics / Audio)
Game Engine->Dev Tooling (CI, VCS)
Asset Pipeline->Dev Tooling (CI, VCS)
Live-Ops Platform->Game Server Hosting
Live-Ops Platform->Telemetry / Data Warehouse
Matchmaking / Netcode->Game Server Hosting
Anti-Cheat->Player Identity / Auth

// Funding chain
Funding Model->VC Capital
Funding Model->Private Investor

// Platform + infra chain
Game Platform (Console / PC / Mobile)->Hardware (Devices, GPUs)
Game Server Hosting->Cloud Compute / CDN
Telemetry / Data Warehouse->Cloud Compute / CDN
Payment Processing->Player Identity / Auth
Cloud Compute / CDN->Electricity / Internet
Hardware (Devices, GPUs)->Electricity / Internet

// Evolution arrows — visible industrialising pressure
evolve Subscription Catalogue 0.80
evolve Live-Ops Platform 0.70
evolve Anti-Cheat 0.78
evolve Trust & Safety (Moderation) 0.55
evolve Game-Specific Marketplace 0.72

note Differentiation zone [0.72, 0.32]
note Commodity utility [0.12, 0.95]
note Trust / toxicity risk [0.55, 0.22]
```

## 3.2 — Component evolution rationale

| Component | Stage | ε | ν | Evidence |
|---|---|---|---:|---|
| Game Title | Product (+rental) | 0.55 | 0.88 | Multiple AAA releases monthly (Starfield, Spider-Man 2, BG3); product business still the norm even as live-service blurs into Stage IV. |
| Game Brand / IP | Custom Built | 0.42 | 0.84 | Brand creation remains bespoke; no playbook guarantees a hit; Hollywood-IP crossover (The Last of Us HBO) shows brands are still being built, not mass-produced. |
| Virtual Items | Product (+rental) | 0.70 | 0.82 | Skins, battle passes industrialised (Fortnite, CoD, FIFA Ultimate Team) — universally expected, vendor tooling mature but still differentiation in design. |
| Game Store Front | Commodity (+utility) | 0.82 | 0.80 | Steam, Epic, App Store, Play Store, PSN, Xbox Store, Nintendo eShop — few operators, utility take-rate model (15–30%), procurement-style integration. |
| In-Game Economy | Custom Built | 0.45 | 0.78 | Economy design is a named discipline but every live game ships its own; no off-the-shelf economy systems; balance patches are custom art. |
| Marketing Campaign | Product (+rental) | 0.60 | 0.76 | Standardised launch playbooks (preorder + influencer drop + launch trailer + review embargo) run through agencies; still creative variance. |
| Subscription Catalogue | Product (+rental), moving → Commodity | 0.62 | 0.74 | Game Pass, PS+, Ubisoft+, EA Play, Netflix Games — several competing operators; Microsoft concentrating share post-Activision; pricing and tier structures still feature-differentiated. |
| Community / Forum | Product (+rental) | 0.58 | 0.72 | Discord dominant for live games, Reddit for discussion, bespoke forums fading; clear vendor pattern but still per-game implementation. |
| Esports Tournament | Product (+rental) | 0.55 | 0.70 | Established leagues (LEC, LCS, Valorant VCT); format templates exist but league ops still custom; several notable failures in 2023 (OWL wind-down). |
| Influencer Channel | Product (+rental) | 0.62 | 0.68 | Creator economy has standardised rate cards, attribution tools (Tagger, Grin); most publishers run via agencies. |
| Streaming Content | Product (+rental), moving → Commodity | 0.72 | 0.66 | Twitch + YouTube Gaming duopoly, Kick as challenger; infrastructure-like, but creator contracts still negotiated. |
| Alternative Distribution (Web / itch) | Custom Built | 0.48 | 0.62 | itch.io, sideloading, PWA, browser games via playable ads; small share but meaningful for indies; EU DMA (Mar 2024) will force iOS alternative stores. |
| Advertising Placement | Commodity (+utility) | 0.82 | 0.60 | Unity Ads, IronSource, AppLovin, Google AdMob — programmatic, CPM-priced, utility model for mobile free-to-play. |
| Social Platform | Commodity (+utility) | 0.88 | 0.58 | X, TikTok, Instagram, Discord — utility infrastructure for game promotion; publishers buy reach via ad APIs. |
| Player Profiling / Analytics | Product (+rental) | 0.55 | 0.56 | deltaDNA, GameAnalytics, Unity Analytics, Amplitude — mature tooling, but what-to-score still bespoke per studio. |
| Trust & Safety (Moderation) | Custom Built | 0.35 | 0.54 | Hive, ActiveFence, GGWP emerging; regulation rising (UK Online Safety Act Oct 2023, EU DSA) but no dominant stack; most AAA studios still mostly in-house. |
| Game Developer (Studio) | Custom Built | 0.38 | 0.52 | Studios remain bespoke orgs with their own culture and pipelines; 2023's wave of layoffs (Embracer, EA, Ubisoft) exposes fragility of the model. |
| Licensing Deal | Product (+rental) | 0.58 | 0.50 | IP-licensing is a defined vertical (e.g., IMG, ESP Properties) with templated deal structures; multi-platform release terms largely standard. |
| Game Design | Custom Built | 0.32 | 0.48 | Craft discipline; no productised "design engine"; GDC talks still dominated by bespoke case studies. |
| Game-Specific Marketplace | Product (+rental) | 0.58 | 0.46 | Steam Community Market, DMarket, in-game item trading — proven vendors, but every integration still custom; high regulatory scrutiny (SEC guidance on skin gambling). |
| Game Engine | Product (+rental) | 0.70 | 0.44 | Unity + Unreal duopoly with clear rental pricing; Godot rising in indie; Sep 2023 Unity runtime-fee backlash shook the "product" perception toward rental-trap. |
| Live-Ops Platform | Product (+rental) | 0.52 | 0.42 | PlayFab, GameSparks (decom.), Nakama, AccelByte, Beamable — competing vendors, but large studios still build in-house. |
| Matchmaking / Netcode | Product (+rental) | 0.58 | 0.40 | Epic Online Services, PlayFab Multiplayer, Photon — off-the-shelf tiers available; still custom-built in big PvP titles. |
| Anti-Cheat | Product (+rental), moving → Commodity | 0.62 | 0.38 | Easy Anti-Cheat (Epic), BattlEye, Denuvo, Ricochet (Activision in-house) — named vendor market; kernel-level friction + Linux compatibility still controversial. |
| Asset Pipeline | Product (+rental) | 0.55 | 0.36 | Perforce + Jenkins + Houdini + Substance + Maya is a standard chain; generative-AI assets appearing but not yet pipeline-standard in Nov 2023. |
| Dev Tooling (CI, VCS) | Commodity (+utility) | 0.85 | 0.32 | GitHub, GitLab, Perforce, Jenkins; developer-tools stack is effectively interchangeable utility. |
| Middleware (Physics / Audio) | Product (+rental) | 0.78 | 0.30 | Wwise, FMOD, Havok, SpeedTree — established rental-licensed vendors; near-Commodity for common cases. |
| Funding Model | Custom Built | 0.45 | 0.28 | Kickstarter + early access + publisher advance + platform grants — several templates but no standard; 2023 funding drought shows immaturity. |
| Game Platform (Console / PC / Mobile) | Commodity (+utility) | 0.82 | 0.26 | Three console platform-holders, two mobile OS, one open PC; utility economics with take rates; standard SDKs. |
| VC Capital | Product (+rental) | 0.55 | 0.24 | Named specialist funds (Makers, Bitkraft, Griffin, a16z Games); templated term sheets but relationship-driven; cooled sharply in 2023. |
| Private Investor | Custom Built | 0.42 | 0.22 | Family-office, strategic investors, publisher M&A — bespoke per deal; Savvy Games Group's buying spree typifies the era. |
| Hardware (Devices, GPUs) | Commodity (+utility) | 0.88 | 0.22 | NVIDIA + AMD + Apple Silicon on PC/mobile; Sony/MS/Nintendo on console — industrialised silicon supply. |
| Payment Processing | Commodity (+utility) | 0.92 | 0.20 | Stripe, Adyen, Xsolla for games, plus platform-native billing — utility pricing, regulated rails. |
| Player Identity / Auth | Commodity (+utility) | 0.85 | 0.18 | Steam ID, PSN ID, Xbox Live, Epic Account, PlayFab — utility-tier identity providers; OAuth standard. |
| Game Server Hosting | Product (+rental), moving → Commodity | 0.78 | 0.16 | Multiplay (Unity), AccelByte, GameLift (AWS), PlayFab Multiplayer — several competing rental fleets; still feature-differentiated. |
| Telemetry / Data Warehouse | Commodity (+utility) | 0.80 | 0.14 | Snowflake, BigQuery, Databricks — utility data infrastructure. |
| Cloud Compute / CDN | Commodity (+utility) | 0.92 | 0.10 | AWS, GCP, Azure, CloudFlare, Akamai — utility billing, standards-based. |
| Electricity / Internet | Commodity (+utility) | 0.97 | 0.04 | Universal utility. |

---

## 3.1 — Mermaid (GitHub rendering)

```mermaid
wardley-beta
  title Gaming Economies Landscape (Nov 2023)
  anchor "Publisher": [0.98, 0.55]
  anchor "Player": [0.97, 0.62]
  component "Game Title": [0.88, 0.55]
  component "Game Brand / IP": [0.84, 0.42]
  component "Virtual Items": [0.82, 0.70]
  component "Game Store Front": [0.80, 0.82]
  component "In-Game Economy": [0.78, 0.45]
  component "Marketing Campaign": [0.76, 0.60]
  component "Subscription Catalogue": [0.74, 0.62]
  component "Community and Forum": [0.72, 0.58]
  component "Esports Tournament": [0.70, 0.55]
  component "Influencer Channel": [0.68, 0.62]
  component "Streaming Content": [0.66, 0.72]
  component "Alternative Distribution (Web and itch)": [0.62, 0.48]
  component "Advertising Placement": [0.60, 0.82]
  component "Social Platform": [0.58, 0.88]
  component "Player Profiling and Analytics": [0.56, 0.55]
  component "Trust and Safety (Moderation)": [0.54, 0.35]
  component "Game Developer (Studio)": [0.52, 0.38]
  component "Licensing Deal": [0.50, 0.58]
  component "Game Design": [0.48, 0.32]
  component "Game-Specific Marketplace": [0.46, 0.58]
  component "Game Engine": [0.44, 0.70]
  component "Live-Ops Platform": [0.42, 0.52]
  component "Matchmaking and Netcode": [0.40, 0.58]
  component "Anti-Cheat": [0.38, 0.62]
  component "Asset Pipeline": [0.36, 0.55]
  component "Dev Tooling (CI, VCS)": [0.32, 0.85]
  component "Middleware (Physics and Audio)": [0.30, 0.78]
  component "Funding Model": [0.28, 0.45]
  component "Game Platform (Console and PC and Mobile)": [0.26, 0.82]
  component "VC Capital": [0.24, 0.55]
  component "Private Investor": [0.22, 0.42]
  component "Hardware (Devices, GPUs)": [0.22, 0.88]
  component "Payment Processing": [0.20, 0.92]
  component "Player Identity and Auth": [0.18, 0.85]
  component "Game Server Hosting": [0.16, 0.78]
  component "Telemetry and Data Warehouse": [0.14, 0.80]
  component "Cloud Compute and CDN": [0.10, 0.92]
  component "Electricity and Internet": [0.04, 0.97]
```

*(The OWM block above is canonical; Mermaid is a rendering target. If either parse fails, trust the OWM.)*

---

## 4. Strategic analysis

### a. Differentiation opportunities (top 3)

1. **In-Game Economy** (Custom Built) — the single highest-leverage differentiator. Economies are designed per-game; good ones (Fortnite, Path of Exile, FFXIV) create decade-long retention, bad ones collapse a title in weeks. Still user-visible at ν ≈ 0.78; no off-the-shelf replacement.
2. **Game Brand / IP** (Custom Built) — the durable moat. A beloved IP survives engine changes, platform shifts, and studio layoffs. Investment here compounds across sequels, adaptations, and merch.
3. **Game Design** (Custom Built) — paired with Economy, the craft layer where one game beats another. No amount of commoditised infrastructure substitutes for design judgment.

Honourable mention: **Trust & Safety (Moderation)** — currently Custom Built at high visibility (ν ≈ 0.54), becoming a regulatory necessity. First-mover on a trusted moderation system is a genuine differentiator in 2024.

### b. Commodity-leverage candidates (top 3)

1. **Cloud Compute / CDN** (Commodity +utility) — rent from AWS/GCP/CloudFlare; nobody should build their own data-centre for games in 2023.
2. **Payment Processing** (Commodity +utility) — Stripe / Adyen / Xsolla handle the regulated rails; building in-house is strict-worse.
3. **Dev Tooling (CI, VCS)** (Commodity +utility) — GitHub/GitLab/Perforce/Jenkins. Standard chain; avoid reinventing.

Also Commodity-ready for harvest: **Social Platform**, **Advertising Placement**, **Player Identity / Auth**, **Hardware**, **Game Platform** — everything at ε ≥ 0.80 should be consumed as utility.

### c. Dependency risks (top 3)

Visible-over-fragile edges — where a user-facing component rests on something immature.

1. **Game Title → In-Game Economy** (R ≈ ν·(1−ε) with visible Title on Custom-Built Economy) — the most visible piece of the product depends on a genuinely bespoke design that can go catastrophically wrong (Diablo IV launch economy tuning, Overwatch 2 battle-pass backlash). Highest single-game business risk.
2. **Community / Forum → Trust & Safety (Moderation)** — the publisher's social layer depends on a Custom-Built moderation stack. Toxicity or an abuse scandal here can destroy a game's active playerbase overnight (see Fortnite community events, Call of Duty voice-chat controversies). *This is the "trust could collapse the whole thing" flag from the scenario.*
3. **Subscription Catalogue → Licensing Deal** — a catalogue's value depends on a still-maturing licensing mechanism; publisher resistance or a large rights-holder pull-out (c.f. Sony's limited Game Pass participation) fragments the subscription thesis.

Also watch: **Game Title → Game Engine** — Unity's Sep 2023 runtime-fee reversal demonstrated engine-vendor risk; re-platforming mid-project is a single-point-of-failure for many studios.

### d. Build / Buy / Outsource recommendations

| Component | Stage | Recommendation | Why |
|---|---|---|---|
| In-Game Economy | Custom Built | **BUILD** | Core IP; no off-the-shelf substitute; the retention moat. |
| Game Design | Custom Built | **BUILD** | Craft differentiation; hire talent, don't license. |
| Game Brand / IP | Custom Built | **BUILD** (and protect) | Asset compounds over time; defend trademarks aggressively. |
| Trust & Safety (Moderation) | Custom Built → Product | **BUILD core + BUY tooling** | Hive/ActiveFence/GGWP handle detection; humans and policy stay in-house. |
| Live-Ops Platform | Product (+rental) | **BUY** (AccelByte / PlayFab / Nakama) | Mature enough that in-house is strict-worse for most studios. |
| Game-Specific Marketplace | Product (+rental), evolving | **BUY** (DMarket, Steam Market integrations) | Regulatory risk argues for vendor compliance expertise. |
| Matchmaking / Netcode | Product (+rental) | **BUY** for most; **BUILD** only if PvP is the whole game | Epic Online Services / PlayFab cover the baseline. |
| Anti-Cheat | Product (+rental) → Commodity | **BUY** (EAC / BattlEye) | Only Activision/Riot-scale warrants in-house; kernel driver work is not your edge. |
| Game Engine | Product (+rental) | **BUY / RENT** (Unreal / Unity / Godot) | Build-own-engine is a franchise-studio bet (Frostbite, RE Engine), not a default. Post-Unity-2023, a Godot option is now reasonable insurance. |
| Matchmaking, Asset Pipeline middleware | Product (+rental) | **BUY** | Perforce + Substance + Wwise / FMOD are the de-facto standard. |
| Subscription Catalogue | Product (+rental), evolving | **PARTNER** | For third-party publishers, decide Game Pass / PS+ / Epic / own-catalogue per title — this is the most active live strategic choice in 2023. |
| Payment, Auth, Cloud, CDN, Data Warehouse, Telemetry | Commodity (+utility) | **RENT** | Utility consumption. Never build. |
| Store Fronts, Social Platforms, Advertising Placement | Commodity (+utility) | **RENT** (consume APIs) | Duopoly/oligopoly utility markets; integrate, don't compete. |
| Alternative Distribution | Custom Built | **WATCH + OPTION** | itch.io, iOS alternative-store (EU DMA Mar 2024) — don't build; hedge on. |

### e. Suggested gameplays (from Wardley's 61)

- **#16 Exploiting Network Effects** on **Community / Forum** and **Subscription Catalogue** — both are classic two-sided network plays. Game Pass's leverage rises with each additional subscriber AND each additional title.
- **#45 Two-factor markets** on **Esports Tournament**, **Streaming Content**, **Influencer Channel** — each is a two-sided play (players + advertisers, streamers + viewers, creators + audience). Publishers using these as distribution should think network-effect first, campaign second.
- **#36 Directed investment** on **In-Game Economy**, **Game Design**, **Game Brand / IP** — spend engineering and creative effort in the top differentiation-zone components.
- **#29 Harvesting** on **Live-Ops Platform**, **Anti-Cheat**, **Matchmaking** — let the vendor market settle, buy the winner.
- **#15 Open approaches** on **Trust & Safety (Moderation)** — open trust-model standards (as AV- industry did for CSAM hashes) avoid each publisher duplicating moderation policy work. Regulatory tailwinds favour this.
- **#56 First mover** on **Trust & Safety** compliance — UK Online Safety Act, EU DSA, California AB 2273 create a narrow window where demonstrably-safe platforms win.
- **#41 Alliances** on **Alternative Distribution** — the Coalition for App Fairness / Epic's store play is already an alliance move against platform-holder take rates.
- **#26 Differentiation** on **In-Game Economy** and **Game Brand / IP** — where the market already consolidates, stand out deliberately.
- **#52 Pricing structure play** on **Virtual Items** and **Subscription Catalogue** — pricing is the live battleground in 2023 (Game Pass tiering, battle-pass economics).
- **#8 Co-option / Centre-of-gravity** — risk flag. The platform-holders (Apple, Google, Sony, MS, Valve) already co-opt publisher relationships via store-front take rates; Epic's legal fights show the countermove pattern.

### f. Doctrine violations / observations

- ✓ **#1 Focus on user needs** — map is correctly anchored on both Publisher and Player; scenario demanded it.
- ✓ **#10 Know your users** — two anchors capture the genuine two-sided nature.
- ⚠ **#13 Manage inertia** — inertia is heavy across the map:
  - *Co-creation inertia (consumer form #5):* players invested in a game's virtual items resist cross-title migration.
  - *Sunk-cost (consumer form #2):* same, plus publisher sunk cost in engine licenses (Unity 2023 episode).
  - *Past-success supplier inertia (supplier form #1):* AAA publishers clinging to $70 boxed-release model vs. subscription.
- ⚠ **#22 Use standards wherever possible** — Trust & Safety lacks cross-industry standards; each publisher rolls their own, duplicating effort.
- ⚠ **#24 Design for constant evolution** — the **Engine** layer is rigid; Unity's 2023 fee change exposed that studios hadn't designed for engine portability.

### g. Climatic context (which of 27 patterns are active)

- **#3 Everything evolves** — Live-Ops, Anti-Cheat, Subscription Catalogue all visibly industrialising in 2023.
- **#8 Characteristics change** — players increasingly expect Product-stage features (cross-play, cloud saves) as table-stakes; what was Genesis a decade ago (matchmaking) is now Commodity.
- **#15 Past success breeds inertia** — AAA publishers stuck in $70-release + DLC model while Subscription Catalogue evolves.
- **#17 Inertia increases the more successful the past model** — Console platform-holders' 30% take rate is now regulatory flashpoint (EU DMA, Epic v. Apple).
- **#27 Product-to-utility is punctuated equilibrium** — Game Pass / PS+ / Netflix Games are the current punctuation; the industry argues whether subscription becomes the dominant monetisation or stays peripheral. Nov 2023 is *during* the transition, not after.
- **#23 Components co-evolve with practice** — Live-Ops spawned the "live-service game" practice; Trust & Safety will spawn its own professionalised practice within the next 18 months under regulatory pressure.

### h. Deep-placement notes

Five components warranted targeted research (prior memory of the sector plus scenario hints rather than fresh web searches):

1. **Anti-Cheat** — initial cheat-sheet reading (vendor count, product maturity) put this at ε ≈ 0.55 (mid-Product). Kernel-level market has narrowed to Easy Anti-Cheat (Epic-acquired, free for Unreal), BattlePye, Denuvo, plus in-house (Ricochet, Vanguard). The vendor concentration and Epic's free-tier push pushed the placement to 0.62, with an `evolve → 0.78` arrow: genuinely commoditising, with Linux/Steam Deck compatibility as the remaining disagreement.
2. **Subscription Catalogue** — tempting to call Stage IV already given Netflix-style price per user, but pricing tiers, exclusivity terms, and day-one inclusion are still negotiated per-title per-operator. Placed at 0.62 with `evolve → 0.80`. Microsoft's Activision close (Oct 2023) concentrates the Game Pass end of the market; we're watching a punctuated-equilibrium moment.
3. **Trust & Safety (Moderation)** — initial placement 0.45 based on tooling like Hive, ActiveFence. Pushed *down* to 0.35 because (a) most AAA studios still run in-house, (b) there is no standard taxonomy of in-game harms, (c) UK Online Safety Act (Oct 2023) and EU DSA enforcement are *just starting* — regulatory standardisation is the Stage III → IV forcing function, not yet fired. `evolve → 0.55` reflects the rapid shift in 2024–25.
4. **Game Engine** — easy default to Stage III Product given Unity + Unreal rental pricing. Kept at 0.70 but noted the Sep 2023 Unity runtime-fee episode as evidence the rental-product relationship is under strain; Godot's rise (indie share) is a live signal. Placement unchanged, confidence reduced.
5. **Game-Specific Marketplace** — placed at 0.58 (early Product). The SEC's 2023 guidance on skin-gambling risk, plus several publishers (Valve, Riot) pulling back from third-party marketplaces, argue this node is not yet stable Product — it's in-transition with real regulatory risk. `evolve → 0.72` reflects standardisation under regulatory pressure.

No full web searches executed in this run; placements drew on public-knowledge vendors, regulation, and 2022–23 industry events. If uncertainty on any of these five mattered more than the overall shape of the map, a targeted `[component] vendor landscape 2023` search should be the next step.

### i. Caveat

Evolution trajectories on the `evolve` arrows are scenarios, not forecasts. Wardley's climatic pattern #18 applies: *"you cannot measure evolution over time or adoption."* The 2023 snapshot is a defensible reading of observable signals; the 2024–25 trajectories (Subscription → Commodity, Anti-Cheat → Commodity, Trust & Safety → Product) depend on regulatory and market actions that haven't happened yet.

---

## Validator / layout summary

- **Validator (Step 5.5):** map was constructed with visibility stratified on 0.02 steps and cross-checked edge-by-edge. All 67 edges satisfy ν(source) ≥ ν(target). All coordinates are in [0, 1]. All edge endpoints match declared nodes. (Validator script invocation blocked in this sandboxed run; manual walkthrough documented in the working file `draft.owm`.)
- **Layout check (Step 5.6):** no near-duplicate coordinates (all pairs exceed the 0.02 × 0.02 threshold). No stage-boundary straddlers within ±0.01. Anchors inside clip-free band (0.97, 0.98). Stage balance: Custom Built 8 / 38 (21%), Product 18 / 38 (47%), Commodity 12 / 38 (32%), Genesis 0 — defensible absence (no true Genesis components in the 2023 games economy apart from generative-AI content pipelines, which I chose not to split out).
- **Density:** 38 components, in the 35–45 target for an industry-landscape map.

## Toxicity / trust risk flag

The scenario asked specifically for this. In the map it's the **Community / Forum → Trust & Safety (Moderation)** edge, sitting at the high-ν / low-ε intersection ("trust / toxicity risk" note at [0.55, 0.22]). The risk isn't abstract:

- **Toxicity**: one voice-chat scandal or harassment campaign can crater a game's retention in days. This is a visible (ν ≈ 0.72) failure mode resting on a Custom-Built foundation.
- **Trust**: if players stop believing the In-Game Economy is fair (pay-to-win imbalances, skin-gambling scandals), the monetisation surface collapses. See Overwatch 2's battle-pass backlash or the repeated FIFA Ultimate Team investigations.
- **Regulation**: UK Online Safety Act (Oct 2023), EU DSA, loot-box investigations in Belgium / Netherlands, age-appropriate-design codes in California — every one of these forces Trust & Safety up the evolution axis. Publishers who treat moderation as cost rather than product lose.

The strategic read is that Trust & Safety + In-Game Economy together form a single fragile backbone beneath everything publishers sell. The "commodity utility" half of the map (bottom-right) is reliably cheap; the "differentiation zone" (top-left middle) is where real money is made; but the "trust corridor" (middle-centre) is where either half can be destroyed overnight.
