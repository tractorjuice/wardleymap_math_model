# Wardley Map: Game Economies Landscape (November 2023)

**Anchor:** Publishers and Players
**Date:** 2023-11 (landscape snapshot)
**Scope:** End-to-end game economy — funding, build, distribution, monetisation, marketing/buzz, player profiling, trust/toxicity

## 1. Context

The request is to map the global game-economies landscape as of November 2023, anchored on the two user groups whose needs drive the value chain: **publishers** (need: profitable, sustainable franchises) and **players** (need: entertaining, fair experiences). The map must span the full chain from capital formation through to the marketing/buzz apparatus and flag the components whose collapse (toxicity, trust) could take the whole economy with them.

I worked through the arc-kit skill's six steps — context, value chain, evolution positioning, movement, analysis, and the optional quantitative layer — and produced the OWM map in `draft.owm`.

## 2. Value Chain

Working backwards from the two anchors:

- **Publishers** need: a funded business model, a development capability, a distribution route, a monetisation scheme, a marketing engine, and insight into their players.
- **Players** need: hardware to play on, a place to discover and buy games, items and economies inside those games, communities to share the experience, and tournaments/streamers to follow.

These two need-trees overlap heavily in the middle (the game platform, the stores, the in-game economy) and diverge at the ends — publishers sit on top of funding and campaigns; players sit on top of social platforms, streaming content, and hardware.

Two cross-cutting components — **Trust** and **Toxicity Moderation** — sit underneath the visible chain. They are hidden infrastructure, but every visible element depends on them implicitly; their failure collapses the value chain regardless of how well everything above is executed.

## 3. Evolution Positioning

Using the arc-kit evolution rubric (Ubiquity + Certainty, weighted equally), the components fall into four groups.

### Commodity (evolution 0.75 - 1.00)

| Component | U | C | E | Rationale |
|---|---|---|---|---|
| Hardware (consoles, PCs, mobile) | 0.90 | 0.85 | 0.88 | Ubiquitous, standardised form factors, utility pricing at the chip level |
| Social Platforms (Discord, X, Reddit, TikTok) | 0.85 | 0.80 | 0.82 | Mature utilities, near-universal adoption by gaming communities |
| Dev Tools (VCS, CI, asset pipelines) | 0.85 | 0.75 | 0.80 | Fully standardised, commodity cloud offerings dominate |
| Game Stores (Steam, Epic, PSN, Xbox, eShop) | 0.80 | 0.80 | 0.80 | A handful of dominant storefronts; rev-share terms are now "weather" |
| Campaigns (paid media buying) | 0.80 | 0.75 | 0.78 | Agencies, programmatic, measurement — fully industrialised |
| VCs | 0.80 | 0.75 | 0.78 | Gaming-specialist VCs are a mature sub-asset class |
| Game Engines (Unreal, Unity, Godot, in-house) | 0.80 | 0.75 | 0.78 | Two dominant products + open-source + custom; selection is routine |
| Business Models (F2P, premium, subscription, hybrid) | 0.75 | 0.75 | 0.75 | Well-catalogued; choice is product selection, not invention |

### Product (evolution 0.50 - 0.75)

| Component | U | C | E | Rationale |
|---|---|---|---|---|
| Streaming Content (Twitch, YouTube Gaming) | 0.75 | 0.70 | 0.73 | Two-platform product market; monetisation is configured, not invented |
| Licensing and Subscriptions (Game Pass, PS+) | 0.75 | 0.70 | 0.72 | Multiple maturing services; pricing and catalogue strategy converging |
| Virtual Items | 0.70 | 0.70 | 0.70 | Established pattern; legal frameworks still evolving (see loot-box regulation) |
| Private Investors | 0.70 | 0.65 | 0.68 | Mature investment class, product-level diligence |
| Advertising (in-game, rewarded, sponsored) | 0.70 | 0.65 | 0.66 | Measurement mature, but in-game ad standards still diverging |
| Catalogues (Game Pass, PS+ Extra, EA Play) | 0.65 | 0.60 | 0.62 | Multi-vendor product competition; day-one differentiation still active |
| Game Marketplaces (skin markets, in-game stores) | 0.60 | 0.55 | 0.58 | Technology standardised; policy/legality still variable |
| Game Platform (PC, console, mobile, cloud gaming) | 0.70 | 0.60 | 0.68 | Cloud gaming dragging the mean leftward; mostly product stage |
| Influencer Communities (creators, streamers) | 0.60 | 0.55 | 0.58 | Product-ified via agencies and platforms, but still partly bespoke |
| Player Profiling (analytics, segmentation, matchmaking data) | 0.55 | 0.55 | 0.55 | Tooling exists (GameAnalytics, Unity Analytics) but publishers still build bespoke pipelines |
| Funding Models (publisher advances, grants, crowdfunding, Web3) | 0.60 | 0.50 | 0.55 | Heterogeneous — some commodity (publisher deals), some custom (Web3, platform grants) |
| Developers (the people and studios) | 0.60 | 0.50 | 0.55 | Practice-oriented; mature labour market but individual studios differentiate |
| In-game Economy design | 0.55 | 0.50 | 0.52 | Patterns are emerging (sinks, faucets, dual-currency) but implementation still bespoke per title |
| Tournaments (esports leagues and events) | 0.55 | 0.50 | 0.52 | Industrialising, but governance, franchising, and format still evolving |

### Custom-Built (evolution 0.25 - 0.50)

| Component | U | C | E | Rationale |
|---|---|---|---|---|
| Alternative Distribution (itch.io, direct, Web3 marketplaces) | 0.35 | 0.30 | 0.32 | Non-standard; Web3 distribution in particular is mid-custom |
| Toxicity Moderation (policy, tooling, human review) | 0.40 | 0.30 | 0.36 | Every publisher still builds their own — tooling exists but policy is bespoke |
| Trust (the social contract between players/devs/publishers) | 0.30 | 0.25 | 0.28 | No shared standard; each publisher accrues (or burns) it independently |

### Genesis

None of the components in the requested scope are truly novel as of November 2023. The closest candidates — blockchain-based in-game economies and generative-AI content pipelines — are better modelled as genesis-stage **variants** of existing components (Alternative Distribution, Dev Tools) rather than separate anchor-visible entities.

## 4. Movement

Evolution arrows are included in the OWM (`evolve` directives). The six components with the clearest rightward pressure:

| Component | Now | Target (12-18 mo) | Driver |
|---|---|---|---|
| Catalogues | 0.62 | 0.76 | Game Pass / PS+ Extra compressing the market; day-one strategy now table-stakes |
| Player Profiling | 0.55 | 0.72 | Privacy-respecting analytics standardising; Unity Gaming Services, GameAnalytics maturing |
| Tournaments | 0.52 | 0.68 | Riot franchise model + Saudi PIF consolidation pushing toward product norms |
| In-game Economy | 0.52 | 0.70 | Industry playbook (Hooked/Reforge/GDC talks) hardening into product patterns |
| Toxicity Moderation | 0.36 | 0.55 | EU DSA + regulatory pressure + third-party vendors (Modulate, GGWP) forcing standardisation |
| Alternative Distribution | 0.32 | 0.55 | Epic vs. Apple, steam alternatives, Web3 storefronts — all pulling the mean rightward |

**Inertia** (marked `x` in the arc-kit convention — represented in the analysis below rather than in OWM syntax):
- Publisher reluctance on **Alternative Distribution** — the 30% storefront tax is painful but switching cost is customer-acquisition, not technology.
- **Game Engines** — Unity's runtime-fee episode in 2023 showed how much inertia is embedded in engine choice; studios absorb costs rather than re-port.

**Accelerators** (`>>`):
- **Player Profiling** is being dragged right by platform providers bundling analytics; a publisher that hasn't industrialised profiling by end-2024 is behind.
- **Toxicity Moderation** is being accelerated by regulation more than by market pull.

## 5. Analysis

### Where the economy is commoditised infrastructure

The right-hand band of the map — Hardware, Dev Tools, Social Platforms, Game Stores, Campaigns, VCs, Game Engines, Business Models — is **utility territory**. A publisher or developer trying to differentiate here will lose: it is cheaper and faster to consume these as services. The correct posture is operational excellence — pay the platform tax, integrate the SDKs, run the campaign playbook — and invest the savings further left.

### Where differentiation is still available

Three zones are live for differentiation, each with a distinct play:

1. **In-game Economy + Player Profiling** (evolution ~0.55). The pattern library is hardening but the implementation is still bespoke. Studios that treat economy design as a first-class engineering discipline (dedicated economy designers, telemetry-driven balancing, segmented monetisation) outperform. This is the **ILC / custom-built differentiator** zone for the next 12-24 months.
2. **Catalogues and Licensing/Subscriptions** (evolution ~0.62-0.72). Still active product-stage feature competition — day-one titles, exclusivity, family plans. A publisher large enough to run its own catalogue (Microsoft, Sony, EA) still has room. For mid-size publishers, the game is negotiating the right terms to ride another's catalogue without cannibalising direct sales.
3. **Alternative Distribution + Influencer Communities** (evolution ~0.32-0.58). The custom-built end, where creativity still wins. Strong publisher IP + a tight influencer program can out-run a pure storefront dependency — Hoyoverse, Supercell, and Innersloth have demonstrated this.

### Where toxicity or trust could collapse the whole thing

**Trust (0.28) and Toxicity Moderation (0.36)** are the load-bearing but hidden components. Every visible revenue stream — virtual items, subscriptions, in-game economy, tournaments, streaming content — is a **Dependency Risk** hanging off these two custom-built components. Applying the arc-kit Dependency Risk formula R(a,b) = vis(a) × (1 − evol(b)):

| Dependent (a) | Depends on | vis(a) | evol(b) | R |
|---|---|---|---|---|
| Virtual Items | In-game Economy / Trust | 0.58 | 0.28 | **0.42** |
| In-game Economy | Trust | 0.52 | 0.28 | **0.37** |
| Social Platforms | Toxicity Moderation | 0.64 | 0.36 | **0.41** |
| Tournaments | Toxicity Moderation | 0.70 | 0.36 | **0.45** |
| Influencer Communities | Trust | 0.72 | 0.28 | **0.52** |

Every one of these exceeds the 0.30 threshold where the arc-kit playbook prescribes explicit contingency planning. Influencer Communities (0.52) and Tournaments (0.45) are the highest-risk dependencies. **If trust or moderation fails — a loot-box scandal, a major streamer-league collapse, a cheating epidemic, a child-safety incident — the effect does not stay local; it propagates up through the visible revenue chain.**

The 2023 evidence is already there: Fortnite's FTC settlement, Roblox's child-safety scrutiny, the Destiny-2 / Twitch raid harassment cycles, CS:GO skin gambling regulation. These are all instances of a 0.28-evolution component threatening 0.70-evolution revenue streams.

### Gameplay recommendations (arc-kit gameplay patterns)

- **Industrialise** (commodity play) everything to the right of evolution 0.70: consume engines, stores, social platforms, campaigns, dev tools as utility.
- **ILC (Innovate-Leverage-Commoditise)** on In-game Economy and Player Profiling: build the next generation of telemetry-led economy design in-house, then commoditise the *infrastructure* as a publisher-wide platform.
- **Co-opetition / Sensing Engine** around Alternative Distribution: publishers should participate in (rather than ignore) the Epic/itch/Web3/direct-to-player channels to sense where the 30% tax becomes negotiable.
- **Defensive regulation** on Toxicity and Trust: get ahead of the EU DSA / UK OSA by investing in moderation as a differentiator, not a compliance line item — a trusted brand is a durable moat when the category is otherwise commoditising.

### Climatic patterns at work (arc-kit climatic reference)

- **Everything Evolves** — the whole right-hand block is a cautionary tale: what looks like sustainable rent (storefront 30%) is already under evolutionary pressure.
- **Co-evolution** — Streaming Content and Tournaments co-evolve with Influencer Communities; moves in one pull the others.
- **Higher-order systems create new sources of worth** — the category of "creator economy inside games" (UEFN, Roblox creators, Fortnite creative) is a higher-order system that will destabilise traditional dev-tools and publishing arrangements.
- **Inertia is a killer** — Unity's 2023 runtime-fee misstep is the canonical gaming example of inertia-blindness by an incumbent.
- **Red Queen** — running to stay still in the F2P / live-service space; absolute improvement in monetisation does not guarantee relative improvement as competitors iterate in parallel.

## 6. Quantitative Summary

Applying arc-kit's decision metrics (Differentiation Pressure, Commodity Leverage) to the headline components:

| Component | Vis. | Evol. | D = v·(1−e) | K = (1−v)·e | Verdict |
|---|---|---|---|---|---|
| Player Profiling | 0.48 | 0.55 | 0.22 | 0.29 | Borderline — invest only if it is a differentiator |
| In-game Economy | 0.52 | 0.52 | 0.25 | 0.25 | Custom-build — the differentiating layer |
| Influencer Communities | 0.72 | 0.58 | 0.30 | 0.16 | Invest (visible, not yet commoditised) |
| Catalogues | 0.66 | 0.62 | 0.25 | 0.21 | Product-buy, but terms are negotiable |
| Hardware | 0.38 | 0.88 | 0.05 | 0.54 | Consume as utility |
| Game Engines | 0.54 | 0.78 | 0.12 | 0.36 | Buy / configure; inertia risk is real |
| Social Platforms | 0.64 | 0.82 | 0.12 | 0.13 | Already utility — optimise spend |
| Toxicity Moderation | 0.30 | 0.36 | 0.19 | 0.45 | Outsource to specialist vendors + in-house policy layer |
| Trust | 0.26 | 0.28 | 0.19 | 0.53 | Cannot outsource — must build, protect, measure |

**Reading the matrix:** the highest D(v) is Influencer Communities (0.30) — confirming the intuition that this is where publisher marketing dollars still earn outsized returns. The highest K(v) is Trust (0.53), but the K score is misleading here: trust cannot be consumed as a utility even though the numbers suggest it. This is a case where the qualitative analysis overrides the formula — Trust is the one component on the map that is both low-visibility AND must be built, not bought.

## 7. Recommendations

**Immediate (next quarter):**
- Run a toxicity-moderation audit against the incoming EU DSA / UK OSA requirements; treat this as a board-level risk.
- Stand up first-class telemetry on the in-game economy for any live-service title — economy design without telemetry is guessing.

**Short-term (6-12 months):**
- Industrialise campaigns, dev tools, game-engine selection, and platform consumption — stop treating these as strategic decisions.
- Launch an influencer program that owns the relationships, not the agency middleman.

**Long-term (12-24 months):**
- Build a publisher-wide player-profiling platform (commoditising it internally across titles).
- Participate in at least one alternative distribution channel (Epic, direct, EU-mandated iOS alternatives) to sense commoditisation of storefronts.
- Invest in Trust as a brand moat: transparent economy disclosure, child-safety leadership, anti-cheat investment.

## 8. Files

- `draft.owm` — OnlineWardleyMaps source (paste into https://onlinewardleymaps.com to render)
- `../timing.json` — run timing metadata
