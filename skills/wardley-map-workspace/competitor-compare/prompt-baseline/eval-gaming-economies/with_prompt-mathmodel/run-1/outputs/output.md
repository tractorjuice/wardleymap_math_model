# Game Economies Landscape (November 2023)

Mapped against the Wardley tuple $\mathcal{M} = (V, E, U, \nu, \varepsilon, t)$ using the generator prompt's 4-row cheat-sheet method. Two anchors — **Publishers** and **Players** — reflect the two-sided nature of the market. The map covers the four requested chain stages (fund, build, distribute, monetise), the marketing/buzz apparatus, and the trust-collapse vector.

## Map (OWM)

```owm
title Game Economies Landscape (November 2023)
style wardley

// Anchors — two user types: publishers (commissioning/producing) and players (consuming)
anchor Publishers [0.98, 0.55]
anchor Players [0.96, 0.70]

// Layer 1 — directly user-facing experiences
component Game Title [0.88, 0.45]
component Player Community [0.86, 0.55]
component Brand / Franchise [0.84, 0.35]

// Layer 2 — distribution and storefronts
component Game Stores [0.78, 0.80]
component Game Catalogues / Subscription Services [0.76, 0.55]
component Game-Specific Marketplaces [0.72, 0.45]
component Alternative Distribution [0.70, 0.30]

// Layer 3 — monetisation surfaces
component Virtual Items / Skins [0.68, 0.55]
component In-Game Economy [0.66, 0.45]
component Licensing / Subscriptions [0.64, 0.70]
component In-Game Advertising [0.60, 0.60]

// Layer 4 — marketing & buzz apparatus
component Marketing Campaigns [0.74, 0.75]
component Esports Tournaments [0.68, 0.50]
component Influencer Communities [0.66, 0.55]
component Streaming Content (Twitch / YouTube Gaming) [0.70, 0.70]
component Social Platforms [0.62, 0.85]
component Player Profiling / Analytics [0.50, 0.55]

// Layer 5 — production: developers and creative work
component Developers / Studios [0.58, 0.35]
component Live-Ops Team [0.52, 0.45]
component Game Design / IP [0.54, 0.25]
component QA / Playtesting [0.46, 0.55]
component Localisation [0.42, 0.70]

// Layer 6 — build tooling and engines
component Game Engines [0.44, 0.70]
component Dev Tools (Asset pipelines, VCS, CI) [0.40, 0.72]
component Middleware (Physics / Audio / Networking SDKs) [0.36, 0.65]
component Anti-Cheat Services [0.38, 0.55]

// Layer 7 — funding and business models
component VC / Private Investors [0.60, 0.60]
component Funding Models (Publisher advance / Crowdfunding / Grants) [0.56, 0.50]
component Business Models (F2P / Premium / Live-service / Subscription) [0.58, 0.55]

// Layer 8 — trust & safety (the collapse vector)
component Player Trust [0.80, 0.30]
component Content Moderation / Toxicity Management [0.48, 0.35]
component Account Security / Fraud Prevention [0.44, 0.60]

// Layer 9 — hardware and platforms
component Game Platforms (Consoles / PC / Mobile) [0.54, 0.78]
component Client Hardware (GPUs, Consoles, Phones) [0.30, 0.88]
component Controllers / Peripherals [0.26, 0.85]

// Layer 10 — deep infrastructure
component Payment Processing [0.28, 0.90]
component CDN / Game Delivery [0.22, 0.92]
component Cloud Compute [0.18, 0.92]
component Matchmaking / Multiplayer Backend [0.32, 0.70]
component Telemetry / Data Pipeline [0.24, 0.75]
component Identity / Auth [0.20, 0.88]

// (dependencies and evolve/note lines — see draft.owm for the complete edge list)
```

*(Full edge list and evolve/pipeline/note lines are in `draft.owm` alongside this file.)*

## Stage-band summary

- **Genesis / Custom-Built (left of map — publisher/developer differentiation zone):** Brand / Franchise, Game Design / IP, Alternative Distribution, Content Moderation / Toxicity Management, Player Trust, Developers / Studios, Game Title.
- **Product + rental (centre):** Virtual Items / Skins, In-Game Economy, Esports Tournaments, Influencer Communities, Streaming Content, Game Engines (Unreal/Unity are Product but edging right), Dev Tools, Anti-Cheat Services, Funding Models, Business Models, VC / Private Investors, Matchmaking / Multiplayer Backend, Player Profiling / Analytics, Localisation, Licensing / Subscriptions.
- **Commodity + utility (right edge — buy, don't build):** Game Stores (Steam/Apple/Google rentier layer), Social Platforms, Client Hardware, Controllers / Peripherals, Game Platforms (as a rental substrate), Payment Processing, CDN, Cloud Compute, Identity / Auth, Telemetry pipeline.

## Strategic analysis

### a. Top 3 by D (differentiation pressure) — $D(v) = \nu(v) \cdot (1 - \varepsilon(v))$

1. **Brand / Franchise** — $0.84 \cdot (1 - 0.35) = 0.55$. A publisher's single most defensible asset. Visible, distinctive, still pre-commodity. This is why GTA, Call of Duty, Pokémon, Mario are the true moats.
2. **Game Title** — $0.88 \cdot (1 - 0.45) = 0.48$. Each title is a bespoke creative artefact; hits are unrepeatable. High D sits right at the anchor surface.
3. **Player Trust** — $0.80 \cdot (1 - 0.30) = 0.56$. Visible to players, genesis-to-custom in how it is managed. *This is the component that can collapse the whole economy — see risks.*

Honourable mentions: Game Design / IP ($0.54 \cdot 0.75 = 0.41$) — the upstream differentiator most directly under the studio's control.

### b. Top 3 by K (commodity leverage) — $K(v) = (1 - \nu(v)) \cdot \varepsilon(v)$

1. **Cloud Compute** — $(1 - 0.18) \cdot 0.92 = 0.75$. AWS/GCP/Azure; there is no reason to run your own data centres for anything but edge-latency multiplayer.
2. **CDN / Game Delivery** — $(1 - 0.22) \cdot 0.92 = 0.72$. Akamai/Cloudflare/Steampipe; game patch delivery is a commoditised pipe.
3. **Identity / Auth** — $(1 - 0.20) \cdot 0.88 = 0.70$. Platform SDKs, OAuth, Firebase Auth. Only build your own if you have a specific anti-fraud angle.

Also notable: Payment Processing ($0.72 \cdot 0.90 = 0.65$), Client Hardware (for publishers this is simply bought-in).

### c. Top 3 dependency risks $R(a, b) = \nu(a) \cdot (1 - \varepsilon(b))$

1. **(Game Title → Alternative Distribution)** $= 0.88 \cdot (1 - 0.30) = 0.62$. Epic Games v Apple/Google is still live in late 2023; publishers betting on side-loaded distribution on mobile have a visible product depending on an immature, legally-contested channel.
2. **(Player Trust → Content Moderation / Toxicity Management)** $= 0.80 \cdot (1 - 0.35) = 0.52$. A high-visibility trust asset depending on an under-commoditised, labour-intensive practice. Incidents (toxicity, hate, harassment in live-service MP titles) directly erode the anchor.
3. **(Brand / Franchise → Game Design / IP)** $= 0.84 \cdot (1 - 0.25) = 0.63$. A top-line differentiator rests on a genesis-stage craft activity — one misstep from the designers and the franchise equity is damaged. This is a *healthy* risk (you want this dependency) but a fragile one; it justifies investment in the design practice.

### d. Suggested gameplays (from the 61-play catalogue)

- **Open Approaches (#15)** on **Game Engines** — Unity's pricing crisis in September 2023 has made open/alternative engines (Godot, O3DE) credible. Publishers that funded or switched early acquire bargaining power. *Targets: Game Engines, Dev Tools.*
- **Two-Factor Markets (#26)** / **Platform Play** on **Game-Specific Marketplaces** — building a storefront for your franchise's UGC (items, mods, cosmetics) converts players into sellers and captures the monetisation surface. *Targets: Game-Specific Marketplaces, In-Game Economy.*
- **Harvesting (#29)** on **Middleware / Anti-Cheat** — the anti-cheat market is consolidating (Easy Anti-Cheat/BattlEye/Denuvo); acquire or lock in a supplier before incumbent players commoditise it.
- **Pig in a Poke / Exploiting Constraint (#47)** on **Game Catalogues / Subscription Services** — Game Pass and PS Plus Extra have not stabilised. Publishers can negotiate day-one deals while platforms are still buying market share, locking in guaranteed revenue before the commoditisation of "gaming subscriptions" is complete.
- **Fool's Mate (#4)** against **Console Exclusivity Deals** (inertia) — refusing exclusivity and going multi-platform neutralises a platform-holder's favourite lever.
- **Co-creation (#12)** on **Influencer Communities and Player Community** — structured creator programmes rather than one-shot sponsorships. Converts rented buzz (streaming + socials) into owned relationships.
- **Undermining Barriers / Threat Acquisition (#33)** on **Streaming Content** — publishers acquiring or partnering with streaming studios before the buzz layer gets squeezed by Twitch/YouTube algorithm changes.
- **Weak Signal Play (#54)** — act on the September 2023 Unity pricing change and the ongoing Epic-Apple ruling as early signals that the engine and distribution layers are entering political-capital-backed re-evolution.

### e. Doctrine observations (from the 40-principle catalogue)

- **Phase II "Know your users"** — this map **has two anchors**. That's correct doctrine — publishers and players are genuinely different users with different needs. Do not collapse them.
- **"Focus on user needs"** (Phase I) — flagged: the map distinguishes *Players* (experience, trust, community) from *Publishers* (revenue, retention, portfolio). Do not optimise the Player Profiling/Analytics component in ways that erode Player Trust; that is a within-map doctrine tension.
- **"Challenge assumptions"** — the common assumption that *Game Engines are a commodity* is wrong at Nov-2023. Unity's behaviour has revealed that the engine layer has live political-capital-backed inertia; rated here as high Stage-III ($\varepsilon = 0.70$), not Stage-IV.
- **"Manage inertia"** — the map flags one inertia component (**Console Exclusivity Deals**, sunk-capital + political-capital) and implicitly another (legacy in-house engines — re-architecture cost). A longer pass should enumerate the 17 forms against each stuck component.
- **Knowledge layer underspecified** — I did not explicitly tag components with $\tau \in \{A, P, D, K\}$. *Player Profiling / Analytics* is a D (data), *Game Design / IP* has K (knowledge) elements, *Live-Ops* is P (practice). A doctrine-compliant v2 would colour these explicitly.

### Collapse vector — where toxicity or trust can bring it down

The hard answer the scenario asks for: **the collapse vector runs Player → Player Trust → Content Moderation → Player Community/Social Platforms**. If toxicity or fraud persists to the point of player departure, anchor-level demand erodes and the whole chain — from VC funding through engines through stores — loses its justification. Two observable mechanisms:

1. **Economic** — Roblox/Fortnite-style scandals (scam items, predatory loot-box design, minor-targeting) trigger regulatory action (EU loot-box rulings, DE/BE bans), which invalidates monetisation-surface assumptions and re-prices the In-Game Economy overnight.
2. **Social** — persistent toxicity in a flagship live-service title drives the community to rivals or non-gaming social spaces; the buzz apparatus (streamers, influencers) follows, and marketing spend returns diminish.

Both flow through the map from high-visibility anchors downward; an incumbent's best defence is *Content Moderation as a Practice* (co-evolve it with Live-Ops) and *Account Security as a Utility* (buy it in), and **not** to let Player Trust erode below the brand-equity stage where reacquisition cost spirals.

## Notes on method

- Visibility seeded from $\nu(v) = 1/(1+d(v))$ then adjusted per value-chain judgment. Key adjustments: *Player Trust* raised from its graph distance because players directly consume it; *Matchmaking* lowered because architecturally invisible to most players.
- Evolution scored on the 4-row cheat-sheet (Ubiquity / Certainty / User Perception / Publication). Strong disagreements: **Game Engines** (Ubiquity IV, Certainty III, User Perception III, Publication III → 0.70, flagged in transition post-Unity 2023); **Virtual Items** (IV/III/III/III → ~0.55, transitional); **Game Stores** (IV on ubiquity, III on certainty → 0.80).
- Evolution *movements* (`evolve ...`) are labelled as scenario, not forecast, per §9 of the prompt.
- Inertia marked once (`Console Exclusivity Deals`) — more could be marked in a follow-up pass.
- I have NOT simulated the logistic ODE; no timeline claims made.
