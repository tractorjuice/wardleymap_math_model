# Wardley Map Analysis: Defence Intelligence Landscape (March 2023)

## Purpose

How do operational decisions get made in defence intelligence in March 2023, and where on the evolution axis does each component sit? The map is intended to expose what is already commoditised utility (so no competitive advantage remains there), where the bleeding edge actually is (Genesis/Custom-Built components worth investing in), and how adversarial capability and regulation constrain the chain.

## Strategic Context

- **Strategic question:** Given the post-ChatGPT inflection (GPT-4 released March 14, 2023), where should a defence-intelligence organisation place investment today — which layers are commodity utility and which are still emerging enough to yield competitive advantage or strategic risk?
- **Anchors (users):** Military Command (the operational decision-maker), Government (oversight and policy), and Citizens (subjects of surveillance and privacy regulation).
- **Scope:** The collection-to-decision intelligence chain, its adversarial threat surface, and the regulatory constraints on data.

## Component Evolution Assessment

| Component | Stage | Position [vis, mat] | Rationale |
|---|---|---|---|
| Military Command | Product | [0.97, 0.75] | Institutional anchor with well-defined command structures; the operational decision-maker. Included as anchor, not a traded component. |
| Government | Product | [0.95, 0.65] | Policy and oversight anchor; stable institutional role across democracies. |
| Citizens | Product | [0.93, 0.55] | Stakeholder in the privacy/regulation sub-chain; not a traded component. |
| Operational Decisions | Product | [0.87, 0.58] | The activity of making operational decisions is ancient and well-understood; doctrine exists across services. Differentiation is in speed and quality, not in the activity itself. |
| Intelligence Agencies | Product | [0.82, 0.68] | Institutional form is mature (NSA/GCHQ/DIA analogues exist globally); roles, functions, and inter-agency protocols are codified. |
| Decision Model (HITL/HOTL) | Custom-Built | [0.78, 0.28] | As of March 2023 there is no agreed doctrine for human-in-the-loop vs human-on-the-loop autonomy thresholds in lethal or semi-lethal AI-assisted decision support. DoD Directive 3000.09 exists but is under active revision; EU AI Act still in trilogue. Multiple bespoke frameworks per organisation. |
| Trust (Competence/Integrity/Benevolence) | Genesis/early Custom | [0.70, 0.18] | The three-factor trust construct (Mayer et al.) applied to AI decision partners in defence is an active research topic with no agreed measurement. Trust calibration for mixed human-machine teams is being invented, not bought. |
| Intelligence Analysis | Product (inertia) | [0.68, 0.45] | Tradecraft is well-developed (structured analytic techniques, IC Directive 203) but carries significant inertia from legacy workflows and classification constraints that resist integration of AI-native tooling. Marked with inertia. |
| Target Discovery | Product | [0.60, 0.55] | Mature mission-planning process with defined methodologies (F3EAD, find-fix-finish cycles). |
| AI/ML Analytics Engine | Custom-Built (edging toward Product) | [0.52, 0.32] | March 2023 is the post-GPT-4 inflection point. Classical ML analytics (computer vision, anomaly detection) is Product-stage, but LLM-enabled analysis, retrieval-augmented tradecraft and foundation-model fine-tuning in classified environments are still bespoke. Palantir Foundry, Scale AI, and primes are building custom stacks; no commodity defence-AI platform exists yet. |
| Intelligence Collection | Product | [0.50, 0.58] | Well-codified activity across SIGINT/IMINT/HUMINT/GEOINT/OSINT disciplines. |
| Verified Diverse Sources | Product | [0.42, 0.50] | Multi-source verification doctrine is well-established (admiralty code, SATs) though the explosion of synthetic media is straining the practice. |
| Regulation, Privacy & Ownership | Custom-Built | [0.40, 0.35] | Patchwork: GDPR and national surveillance acts are mature, but rules for AI training on public/scraped data, ownership of model outputs, and cross-border intelligence sharing post-Schrems II are actively evolving. No global consensus. |
| OSINT | Product | [0.35, 0.68] | Well-developed discipline with mature tooling (Maltego, Shodan, Recorded Future, Bellingcat methodology), published training curricula, and agency-standard workflows. Moving toward commodity as LLM-assisted OSINT becomes packaged. |
| Social Media & Crowdsourcing | Product/Commodity edge | [0.28, 0.62] | Public-data pipelines are largely commodity (web scraping, firehose APIs) though pre-empt by the 2023 Twitter API shutdown. Ukrainian-war crowdsourcing (e.g. geolocation of Russian positions via Bellingcat/OSINT Twitter) demonstrated commodity-scale crowdsourced intel. |
| Adversarial Capability | Custom-Built (edge of Genesis) | [0.28, 0.22] | Mixed: traditional misinformation/PSYOPS are Product-stage, but prompt-injection attacks on LLM-enabled intel tooling are Genesis (first serious exploits disclosed late 2022 / early 2023). Weighted-average placement is Custom-Built at the boundary of Genesis. |
| Sensors (GPS/Cameras/Signals) | Commodity | [0.22, 0.82] | GPS is a utility (GNSS constellations are state-run commodity infrastructure), consumer/commercial cameras and network signal capture are commodity pipelines. Defence-grade variants exist but the underlying sensing is commoditised. |

## Key Strategic Observations

1. **Bleeding-edge cluster sits around the decision/trust/AI triangle.** Three of the strategically most consequential components — Decision Model (HITL/HOTL), Trust, and AI/ML Analytics Engine — are clustered in the Genesis-to-Custom region (maturity 0.18–0.32) with high visibility from the decision layer. This is where doctrine, not technology, is the bottleneck.
2. **The input layer is already commodity.** Sensors are near pure utility (0.82), public-data pipelines are close behind (0.62). No competitive advantage is available from owning more sensors or scraping more Twitter; the differentiator has moved up-stack to analysis and trust.
3. **Verified Diverse Sources is a load-bearing component under strain.** All three collection sub-chains (OSINT, social media, sensors) feed verification. Adversarial capability (deepfakes, astroturfing, prompt-injected reports) attacks this node directly. Its Product-stage position is not stable; verification methodology faces a Genesis-stage threat.
4. **Regulation sits lower than analysis and constrains three collection nodes.** The regulation component (0.35 maturity) is Custom-Built and applies sideways pressure on OSINT, social-media ingestion, and sensor use. A map drawn without regulation as a first-class component under-weights a real constraint.
5. **Intelligence Analysis carries inertia.** Despite being a Product-stage activity, tradecraft culture, classification barriers, and accreditation processes resist absorption of AI-native workflows. The inertia marker flags this as the component most likely to block evolution of the AI/ML layer above it.

## Doctrine Check

Assessed against Wardley doctrine principles:

- **Focus on user needs:** Three anchors declared (Military Command, Government, Citizens) rather than a single military anchor. This is intentional — excluding Citizens makes the regulation/privacy chain feel like an afterthought rather than a genuine constraint, and the map would miss a real stakeholder.
- **Know the details:** Per-component rationale references specific evidence (DoD Directive 3000.09, GPT-4 March 2023 release, Bellingcat/Ukraine OSINT patterns, Twitter API 2023 shutdown, Schrems II).
- **Use appropriate methods:** The cluster analysis flags the mismatch — Product-stage Intelligence Analysis is being asked to consume Custom-Built AI/ML outputs using Genesis-stage trust protocols. This is a methods mismatch and is flagged as inertia.
- **Challenge assumptions:** The scenario explicitly asks for the bleeding edge; the map does not default to placing AI at Genesis reflexively. Classical ML is Product-stage; LLM-enabled intel specifically is Custom-Built. Granularity matters.
- **A bias toward action:** Recommendations below are phrased as specific build/buy/hold moves, not abstract themes.

## Recommended Actions

1. **Build: HITL/HOTL doctrine and trust-calibration instrumentation.** These are Genesis/Custom components with high strategic leverage. No vendor will sell you defensible doctrine here; it has to be grown in-house or via trusted research partnerships. Investment here compounds because the analytics layer above it cannot mature without it.
2. **Build (selectively) / partner: defence-specific LLM analytics stack.** The commercial LLM market is rapidly commoditising but classified-environment deployment, evaluation against adversarial prompts, and tradecraft-aware fine-tuning remain Custom-Built. Partnerships with Palantir/Scale/Anthropic-equivalents are more appropriate than greenfield builds, but the integration layer itself is defensible.
3. **Buy / utility: sensors, OSINT tooling, public-data pipelines.** Do not spend scarce engineering on GPS, camera arrays, or generic web scraping. Buy commodity capacity; differentiate in verification and analysis, not in acquisition.
4. **Defend: verified-sources pipeline.** Given the Genesis-stage threat from prompt-injection and synthetic media, invest in provenance (C2PA-style content credentials), source-scoring, and red-team probing of the analysis pipeline before adversarial capability matures further.
5. **Break inertia: classification-aware AI tooling integration.** The inertia marker on Intelligence Analysis signals a doctrine/culture bottleneck, not a technology one. A pilot programme to co-develop AI-native tradecraft with analysts (not imposed on them) is the move.

## Build vs. Buy Assessment

| Component | Recommendation | Rationale |
|---|---|---|
| Trust / HITL-HOTL doctrine | Build | Genesis-to-Custom; no market to buy from; strategic advantage is all in the doctrine. |
| AI/ML Analytics Engine (defence-context) | Partner / selectively build | Custom-Built and moving; leverage commercial foundation models, build the integration and eval layer. |
| Verified Diverse Sources | Build (methodology) | The practice is Product but the threat is Genesis; invest in provenance and verification as a distinctive capability. |
| Intelligence Analysis tradecraft | Invest in transformation | Product-stage with inertia; value lies in unlocking it, not replacing it. |
| OSINT tooling | Buy | Product stage with clear vendor market. |
| Social Media & Crowdsourcing ingestion | Buy | Commodity data pipes. |
| Sensors (GPS/cameras/signals) | Buy (utility) | Commoditised. |
| Regulation navigation | Partner / legal counsel | Custom-Built patchwork; requires specialist expertise, not bespoke build. |

## Evolution Predictions (12–24 Months)

- **AI/ML Analytics Engine → Product (0.32 → 0.55).** The defence-AI vendor market will consolidate; classified deployment patterns will emerge. Expect a Gartner Magic Quadrant analogue by 2024–2025.
- **Decision Model (HITL/HOTL) → late Custom-Built (0.28 → 0.45).** Driven by EU AI Act coming into force, updated DoD 3000.09, and NATO AI strategy. Not yet Product — too contested.
- **Trust construct → Custom-Built (0.18 → 0.32).** Measurement frameworks published, some standardisation begins; still mostly bespoke.
- **Adversarial Capability → Custom-Built (0.22 → 0.42).** Prompt-injection tooling matures rapidly as commercial LLM deployment proliferates; defensive tooling lags.
- **Regulation, Privacy & Ownership → Product (0.35 → 0.50).** EU AI Act finalised, US executive orders crystallise, legal templates for AI-training data emerge.
- **OSINT → Commodity edge (0.68 → 0.78).** LLM-assisted OSINT tooling will commoditise rapidly; the discipline itself becomes utility.

Inertia to watch: Intelligence Analysis tradecraft, classification processes, and inter-agency information-sharing protocols will resist the upstream evolution of AI/ML analytics.

## Open Questions

1. Is Citizens the right third anchor, or should the map use a narrower legitimacy-holder (e.g. legislative oversight committee)? Broader anchor captures privacy-constrained collection; narrower anchor tightens the decision focus.
2. Should Adversarial Capability be a first-class map component (as drawn) or an overlay/climatic-pattern annotation? The draw here shows it consuming social-media signal and targeting the AI layer — a simplification that may understate state-level cyber adversary capability.
3. For March 2023 specifically, is the AI/ML placement at 0.32 too optimistic? Arguments for lower (closer to Genesis) include the immaturity of classified LLM deployment; arguments for the current placement include the maturity of classical ML analytics that sits inside the same node.
