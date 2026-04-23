# Wardley Map Analysis: Game Economies (November 2023)

## Purpose

Where in the modern game economy is infrastructure now commoditised, where can
publishers and developers still differentiate, and where could toxicity or
trust failures collapse the whole value chain? The map is anchored on two
users — **Players** and **Publishers** — and traces the chain from capital and
creation through distribution, monetisation, buzz, and player profiling.

## Component Evolution Assessment

| Component | Stage | Position [vis, mat] | Rationale |
|---|---|---|---|
| Players | Anchor | [0.97, 0.55] | End user; drives demand for the title and for every monetisation surface. |
| Publishers | Anchor | [0.95, 0.62] | Commercial anchor; allocates capital, owns IP, runs the marketing apparatus. |
| Game Title | Product | [0.88, 0.45] | Branded, differentiated IP. Many competing titles, but each title is a unique product in its genre bracket — clearly Product, not Commodity. |
| Business Models | Custom-Built/Product | [0.84, 0.42] | F2P, premium, live-service, UGC (Roblox, Fortnite). Patterns are emerging but live-service and creator-monetisation models were still being invented in 2023 — sits on the Custom-Built / Product boundary. |
| Developers | Custom-Built | [0.82, 0.38] | Each studio is bespoke; talent, culture and pipeline are non-fungible. "Build-type" knowledge (post-mortems, GDC talks) but no off-the-shelf substitute. |
| Funding (VC / crowdfunding / publisher advance) | Product | [0.78, 0.70] | VC term sheets and publisher advances are standardised; Kickstarter, Indiegogo, publisher slates, grants — multiple competing sources with published norms. |
| Tournaments & Influencers | Product | [0.72, 0.52] | ESL, BLAST, FaceIt tournament operators; creator agencies; rate cards and sponsorship packages exist. Mature market but still a source of differentiation. |
| Streaming & Social | Commodity | [0.68, 0.86] | Twitch, YouTube, Discord, X, TikTok are ubiquitous utilities in 2023. Players expect them to work; outage = front-page news. |
| Player Profiling | Product | [0.62, 0.55] | DeltaDNA, GameAnalytics, Unity Gaming Services, Amplitude, plus proprietary stacks. Well-understood requirements, competitive vendor landscape. |
| In-Game Economy | Custom-Built | [0.58, 0.33] | Drop tables, sink/source balancing, currency design — each title's economy is hand-tuned. No standard "economy-as-a-service" has emerged. |
| Virtual Items & Marketplaces | Product | [0.55, 0.55] | Skins, battle passes, Steam Community Market, TF2 / CS hats; industry-wide playbook. Per-game marketplace tech is still bespoke but the pattern is a Product. |
| Licensing & Subscriptions | Product | [0.50, 0.62] | Game Pass (2017), PS Plus Extra/Premium (2022), Ubisoft+, EA Play. Multiple competing catalogues with transparent pricing. |
| Advertising | Product | [0.46, 0.66] | Unity Ads, ironSource, AppLovin, Google AdMob dominate mobile; rewarded-video and playables are standardised. Console/PC in-game ads less mature. |
| Game Stores & Catalogues | Commodity-approaching | [0.42, 0.72] | Steam, Epic, App Store, Play Store, first-party console stores. 30% platform tax is the de-facto utility price; stores feel invisible until they break. |
| Game Engines | Product | [0.35, 0.60] | Unity, Unreal, Godot, GameMaker; multiple competing vendors, certifications, published learning paths. Feature competition, not invention. |
| Game Platforms (PSN, Xbox Live, Steamworks) | Product/Commodity | [0.28, 0.68] | Backend SDKs — auth, achievements, matchmaking, leaderboards. Standardised APIs; developers integrate them, they don't reinvent them. |
| Hardware | Commodity | [0.15, 0.90] | Sony, Microsoft, Nintendo, Apple, Google, AMD, Nvidia. Utility-priced silicon and dev kits; failure is catastrophic. |
| Trust & Anti-Toxicity | Custom-Built (inertia) | [0.30, 0.22] | No standard answer. ToxMod, Two Hat, Community Sift, Modulate exist but adoption is patchy; most studios still roll their own moderation. Carries inertia because past success (organic growth) breeds resistance to intervention. |

## Key Strategic Observations

1. **The infrastructure floor is a commodity.** Hardware, Streaming & Social,
   Game Stores and Game Platforms form a dense band on the right of the map.
   A studio that still treats any of these as differentiators is mis-reading
   the landscape — they are the substrate on which the game economy runs.

2. **Differentiation is a thin middle band.** Game Title, Developers,
   Business Models, In-Game Economy and Player Profiling cluster in the
   upper-centre of the map. This is where publishers and developers still
   win: IP, live-service economy design, player-behaviour data, and the
   novel business models built on top of UGC and creator economies.

3. **The economy's load-bearing wall is Genesis-adjacent.** In-Game Economy
   (0.33 maturity) and Trust & Anti-Toxicity (0.22 maturity) sit below a
   tower of Product and Commodity components. A failure in either — a
   collapse of in-game currency (hyperinflation, unaddressed exploits) or
   a public toxicity/abuse scandal — propagates up through Virtual Items,
   Streaming & Social, and the Game Title itself.

4. **Storefront commoditisation is the strategic climate for 2024–2026.**
   With Steam at 30%, Epic pushing 12%, Apple under regulatory pressure
   (EU DMA, Epic v Apple aftermath), and Game Pass absorbing first-party
   titles, the channel layer is commoditising faster than the economics
   above it. Publishers who treated the store as invisible infrastructure
   will absorb the shock; those who built store-specific gameplays (Epic
   exclusives, Game Pass day-one deals) are exposed to contract renewal.

5. **Trust sits on the co-evolution fault line.** Streaming & Social are
   Commodity, but the trust mechanisms that police them (moderation,
   toxicity detection, identity verification) are still Custom-Built. This
   is the classic climatic mismatch — *components co-evolve*. The longer
   trust lags the platforms, the larger the inertia and the bigger the
   eventual disruption (regulatory, player exodus, or advertiser flight).

## Doctrine Check

- **Know your users (1)** — Two anchors, Players and Publishers, with
  distinct needs. Publishers are sometimes forgotten in "player-centric"
  mapping; including them is essential because they allocate capital and
  set the business model.
- **Remove bias and duplication (7)** — Most mid-size publishers still
  maintain bespoke analytics *and* a bespoke moderation stack *and* a
  bespoke storefront integration. Duplication is rampant; the map
  suggests buying Player Profiling and Game Platforms and concentrating
  investment on In-Game Economy and Business Models.
- **Use appropriate methods (9)** — Pioneers should own In-Game Economy
  and Trust & Anti-Toxicity (Genesis/Custom). Settlers should own
  Business Models and Player Profiling. Town Planners should run Game
  Stores integration, Platform SDK integration, and Hardware certification.
  A studio using Agile squads to certify a console build is mismatched.
- **Manage inertia (19)** — Trust & Anti-Toxicity carries an explicit
  inertia marker. Publishers have historically profited from permissive
  communities (engagement is higher); the map flags this as the most
  dangerous pattern.
- **Focus on user needs (2)** — Live-service design frequently drifts
  toward publisher needs (ARPU optimisation) rather than player needs
  (fair, fun progression). The map should be re-read every quarter to
  check whether In-Game Economy still serves the Player anchor.

## Recommended Actions

1. **Industrialise Player Profiling this year.** Buy, don't build. Unity
   Gaming Services, Amplitude, or a specialist (DeltaDNA) will be cheaper
   and better than a three-person in-house analytics team. Redirect that
   team to In-Game Economy design.

2. **Treat Trust & Anti-Toxicity as a Pioneer programme with board-level
   visibility.** It is the single highest-leverage Genesis component on
   the map. A credible moderation programme — voice moderation
   (ToxMod/Modulate), proactive text moderation, reporting and appeal
   flows, identity gates for competitive play — converts a systemic risk
   into a retention and regulatory moat.

3. **Exit or hedge exclusive storefront deals.** Game Stores & Catalogues
   are commoditising faster than contracts anticipated. Lock in revenue
   share reductions now while platform holders are still negotiating
   against regulatory pressure, and build multi-store release pipelines.

4. **Make Business Models a Settler competency.** Live-service and
   creator-economy models are moving Custom-Built → Product fast. Publishers
   that codify monetisation patterns (cohort-based balancing, creator rev
   share, sub-to-F2P on-ramps) in a shared internal playbook will
   out-iterate competitors that treat each title's business model as a
   blank sheet.

5. **Build the In-Game Economy as your moat.** Of everything on this map,
   In-Game Economy is the lowest-maturity component *and* the component
   most directly tied to revenue. Pioneer teams, published internal
   post-mortems, and a shared economy-simulation toolchain are high-ROI
   investments that competitors cannot buy off-the-shelf.

## Build vs. Buy Assessment

| Component | Recommendation | Rationale |
|---|---|---|
| Game Title | **Build** | The title IS the differentiation. Building is the business. |
| Business Models | **Build** | Custom-Built / Product boundary; codify in-house to compound learning. |
| In-Game Economy | **Build** | Genesis-adjacent; competitive moat; no off-the-shelf substitute. |
| Trust & Anti-Toxicity | **Build + partner** | Pioneer programme; combine internal policy with specialist vendors (ToxMod, Modulate) rather than rolling pure-custom. |
| Player Profiling | **Buy** | Product stage; multiple competing vendors; internal builds waste pioneer talent. |
| Game Engines | **Buy** | Unreal/Unity/Godot cover 95% of use cases; in-house engines only justified for AAA scale. |
| Game Platforms | **Buy** | SDKs are utilities; integrate, don't reinvent. |
| Hardware | **Buy** | Utility; certify against platform SKUs. |
| Game Stores & Catalogues | **Buy (with leverage)** | Commodity channel; push for improved revenue share and multi-store release. |
| Licensing & Subscriptions | **Buy** | Game Pass / PS Plus / Ubisoft+ are a channel; participate, don't build a rival. |
| Streaming & Social | **Buy** | Utility; integrate Discord/Twitch/YouTube rather than a bespoke community stack. |
| Advertising | **Outsource** | Unity Ads / ironSource / AppLovin absorb the complexity; don't run an ad network. |
| Funding | **Outsource** | Capital is a commodity; optimise cost of capital, don't build a finance function beyond need. |

## Evolution Predictions (12–24 months)

- **Game Stores & Catalogues → 0.82** (further commoditisation). Regulatory
  pressure (EU DMA, Epic v Google) plus Game Pass / PS Plus absorbing
  day-one releases will push the channel layer deeper into utility
  territory. Expect negotiated revenue share improvements and forced
  side-loading on mobile.
- **Licensing & Subscriptions → 0.75**. Game Pass, PS Plus and the
  emerging Netflix / Amazon / Apple Arcade cohort converge to a
  utility-priced catalogue tier.
- **Player Profiling → 0.72**. Privacy-preserving analytics (IDFA
  deprecation, EU-style regulations) plus Unity Gaming Services and
  Amplitude consolidation push this firmly into Product / Commodity.
- **In-Game Economy → 0.50**. Live-service economy playbooks codify.
  Expect the first credible "economy-as-a-service" offerings and shared
  simulation tooling to emerge during this window.
- **Business Models → 0.55**. UGC monetisation (Roblox, Fortnite creator
  economy) productises into reusable patterns.
- **Trust & Anti-Toxicity → 0.42**. Regulatory push (UK Online Safety
  Act, EU DSA) plus voice-moderation vendors reaching scale. Inertia will
  slow this but not stop it — publishers who hold out will be dragged by
  compliance.

## Open Questions

1. **Where does generative AI land on this map in 2024?** AI asset
   pipelines, NPC dialogue, and procedural content are compressing the
   Custom-Built → Product boundary for Developers and In-Game Economy.
   A 2024 refresh should place "AI-assisted content" and re-evaluate
   the maturity of Developers and Business Models.
2. **Is there a regulatory component that deserves its own node?**
   Loot-box regulation (Belgium, Netherlands), gambling classification,
   DMA, and age verification all constrain monetisation and distribution.
   In the next iteration, consider adding "Regulatory Compliance" as a
   cross-cutting component with inertia.
3. **Who is the real user anchor on UGC platforms?** For Roblox and
   Fortnite Creative, creators are a third anchor between Players and
   Publishers. A UGC-specific submap may be warranted.
