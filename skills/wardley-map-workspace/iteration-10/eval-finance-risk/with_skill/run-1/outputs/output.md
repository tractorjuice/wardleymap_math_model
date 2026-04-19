# Wardley Map — Risk Management in Financial Services

**Scenario:** The landscape of risk management in financial services (~2023 context). Four actor-classes (Public, Society, Corporations, Government) consume risk-aware services; six risk types (sovereign, territorial, economic, political, cybersecurity, perceived) flow up the value chain; and a regulated layer of signalling services (rating agencies, credit scoring, actuarial pricing) sits between everyday financial services and the mathematical / legal foundations.

---

## Map (OWM)

```owm
title Risk Management in Financial Services
style wardley

// Anchors — the scenario names four actor classes as users of risk management
anchor Public [0.99, 0.55]
anchor Society [0.97, 0.45]
anchor Corporations [0.96, 0.55]
anchor Government [0.95, 0.40]

// User-facing financial services (what users actually consume)
component Retail Banking [0.88, 0.82]
component Lending [0.85, 0.78]
component Insurance [0.83, 0.72]
component Public Services Continuity [0.80, 0.55]
component Corporate Treasury [0.78, 0.60]

// Perceived and reputational risk — close to users by definition
component Perceived Risk [0.86, 0.30]
component Trust in Institutions [0.82, 0.40]

// Risk categories users care about (second layer)
component Economic Risk [0.72, 0.65]
component Political Risk [0.68, 0.35]
component Sovereign Risk [0.66, 0.55]
component Territorial Risk [0.62, 0.30]
component Cybersecurity Risk [0.70, 0.48]

// Risk-assessment and signalling services
component Rating Agencies [0.60, 0.70]
component Credit Scoring [0.58, 0.82]
component Actuarial Pricing [0.55, 0.78]
component Stress Testing [0.46, 0.55]
component Scenario Analysis [0.50, 0.45]

// Regulatory layer
component Regulation [0.58, 0.65]
component Capital Requirements (Basel) [0.48, 0.72]
component AML / KYC [0.45, 0.78]
component Consumer Protection Rules [0.43, 0.60]
component Cyber Disclosure Rules [0.40, 0.30]

// Risk-management practices (mid-chain)
component Risk Modelling [0.42, 0.55]
component GenAI Risk Analytics [0.38, 0.15]
component Climate / ESG Risk Models [0.35, 0.25]
component Fraud Detection [0.40, 0.65]
component Geopolitical Intelligence [0.35, 0.30]

// Foundations — data and knowledge
component Market Data Feeds [0.30, 0.80]
component Credit Bureaux [0.28, 0.82]
component Historical Loss Data [0.25, 0.55]
component Statistical Methods [0.18, 0.88]
component Payments Rails [0.25, 0.92]
component Cloud Compute [0.15, 0.92]
component Identity / Auth [0.20, 0.88]
component Encryption / PKI [0.18, 0.90]

// Knowledge
component Finance Theory [0.08, 0.90]
component Legal Framework [0.06, 0.70]

// Dependencies — user-facing consumption
Public->Retail Banking
Public->Lending
Public->Insurance
Public->Perceived Risk
Public->Trust in Institutions
Society->Public Services Continuity
Society->Trust in Institutions
Society->Perceived Risk
Corporations->Lending
Corporations->Insurance
Corporations->Corporate Treasury
Corporations->Cybersecurity Risk
Government->Public Services Continuity
Government->Sovereign Risk
Government->Regulation
Government->Political Risk

// User-facing services -> risk categories and signalling
Retail Banking->Credit Scoring
Retail Banking->AML / KYC
Retail Banking->Fraud Detection
Lending->Credit Scoring
Lending->Rating Agencies
Lending->Economic Risk
Insurance->Actuarial Pricing
Insurance->Climate / ESG Risk Models
Insurance->Rating Agencies
Corporate Treasury->Rating Agencies
Corporate Treasury->Economic Risk
Corporate Treasury->Sovereign Risk
Corporate Treasury->Cybersecurity Risk
Public Services Continuity->Cybersecurity Risk
Public Services Continuity->Territorial Risk

// Perception edges
Perceived Risk->Trust in Institutions
Trust in Institutions->Regulation
Trust in Institutions->Rating Agencies

// Risk categories -> analytic services / regulation
Economic Risk->Scenario Analysis
Economic Risk->Stress Testing
Political Risk->Geopolitical Intelligence
Political Risk->Scenario Analysis
Sovereign Risk->Rating Agencies
Sovereign Risk->Scenario Analysis
Territorial Risk->Geopolitical Intelligence
Cybersecurity Risk->Cyber Disclosure Rules
Cybersecurity Risk->Fraud Detection

// Regulation
Regulation->Capital Requirements (Basel)
Regulation->AML / KYC
Regulation->Consumer Protection Rules
Regulation->Cyber Disclosure Rules
Capital Requirements (Basel)->Stress Testing

// Signalling services -> models & data
Rating Agencies->Risk Modelling
Rating Agencies->Historical Loss Data
Credit Scoring->Credit Bureaux
Credit Scoring->Statistical Methods
Actuarial Pricing->Historical Loss Data
Actuarial Pricing->Statistical Methods
Stress Testing->Risk Modelling
Scenario Analysis->Risk Modelling
Scenario Analysis->GenAI Risk Analytics

// Risk modelling decomposes
Risk Modelling->Statistical Methods
Risk Modelling->Market Data Feeds
Risk Modelling->Historical Loss Data
GenAI Risk Analytics->Cloud Compute
GenAI Risk Analytics->Statistical Methods
Climate / ESG Risk Models->Statistical Methods
Climate / ESG Risk Models->Market Data Feeds
Fraud Detection->Statistical Methods
Fraud Detection->Identity / Auth
Geopolitical Intelligence->Market Data Feeds

// Infrastructure
AML / KYC->Identity / Auth
Cyber Disclosure Rules->Encryption / PKI
Payments Rails->Encryption / PKI
Retail Banking->Payments Rails
Retail Banking->Cloud Compute
Insurance->Cloud Compute
Lending->Cloud Compute
Corporate Treasury->Payments Rails

// Knowledge grounding
Risk Modelling->Finance Theory
Actuarial Pricing->Finance Theory
Regulation->Legal Framework
Consumer Protection Rules->Legal Framework
Capital Requirements (Basel)->Legal Framework

// Evolve arrows — scenarios, not forecasts
evolve GenAI Risk Analytics 0.50
evolve Climate / ESG Risk Models 0.55
evolve Cyber Disclosure Rules 0.60
evolve Geopolitical Intelligence 0.55

note Differentiation zone [0.45, 0.22]
note Utility / commodity [0.18, 0.90]
note Perception frontier [0.85, 0.30]
```

---

## Strategic Analysis

### a. Differentiation opportunities (top 3)

Prose-first, stage-first, numbers only if they clarify.

1. **GenAI Risk Analytics** (Genesis) — the freshest uncharted territory on this map. LLM- and agent-based analytics for risk narratives, emerging-risk horizon-scanning, and scenario generation are still in the "describe the wonder" phase in 2023. This is the single highest differentiation leverage point: a visible-enough output (feeding Scenario Analysis and, through it, boardroom-level risk reports) depending on a component that very few institutions have industrialised. Build here.

2. **Climate / ESG Risk Models** (Genesis → Custom Built) — regulators (ECB, PRA, SEC) began mandating climate stress tests in 2022–23, but the underlying physical-risk and transition-risk models are idiosyncratic, vendor-led, and academically contested. Insurance and Corporate Treasury both depend on them. Highest differentiation for any insurer that can build a defensible internal capability before the model templates crystallise into Stage III products.

3. **Geopolitical Intelligence** (Genesis → Custom Built) — post-2022 (Russia/Ukraine, sanctions regimes, chip-export controls), territorial and political risk jumped from back-office afterthought to board-level concern. The signalling here is still bespoke analyst work. Firms that industrialise geopolitical-feed-to-portfolio linkages earlier capture differentiation before rating-agency and data-vendor products mature the space.

Honourable mention: **Perceived Risk** sits visibly close to users but scores low on evolution — it's an unusual shape (high `ν`, low `ε`). That's because *perception* is genuinely uncharted as a managed asset: the practices for managing it (crisis communications, social-sentiment analytics) exist but are pre-Product (+rental). For banks, insurers, and governments, this is a high-leverage Custom Built differentiator, not a Commodity (+utility).

### b. Commodity-leverage candidates (top 3)

Rent, don't build. Stage IV components treated as utility.

1. **Cloud Compute** (Commodity +utility) — the substrate for all risk modelling and GenAI workloads. Use AWS / Azure / GCP; do not run your own. The only reason a tier-1 bank still maintains its own data centres for risk workloads is #13 Manage inertia (sunk capital), and that's a losing fight.

2. **Payments Rails** (Commodity +utility) and **Encryption / PKI** (Commodity +utility) — both deeply industrialised utilities. Banks may operate them but they are not where differentiation lives. Treat as commodity with strong SLA.

3. **Statistical Methods** (Commodity +utility) — regression, GLMs, copulas, GARCH, extreme-value theory. All of this is in textbooks and open-source libraries. This does not mean *applying* them is a commodity — the modelling craft is still Custom Built — but the methods themselves are utility knowledge. Also **Credit Bureaux** (Commodity +utility) — Experian, Equifax, TransUnion, Dun & Bradstreet: buy the feed, don't try to out-collect the bureaux on consumer credit data.

### c. Dependency risks (top 3)

Edges where a highly visible component depends on an immature foundation — the places where the map is most exposed.

1. **Scenario Analysis → GenAI Risk Analytics** — Scenario Analysis is mid-chain and feeds Economic, Political, and Sovereign risk narratives that reach the boardroom. It is starting to lean on Genesis-stage GenAI analytics. The chain is only as mature as its weakest link; a hallucinated scenario in a climate or geopolitical stress test that is then rolled up into capital planning is a real-money error. This is the single most exposed foundation in 2023.

2. **Insurance → Climate / ESG Risk Models** — a user-visible product (home insurance, flood, wildfire, transition-risk-linked corporate cover) depending on Genesis-stage physical-risk models. Mispricing is not theoretical: it has already caused Florida / California insurer withdrawals. The map shape is a high-`ν` component standing on a low-`ε` foundation that disagrees across vendors.

3. **Corporate Treasury → Cybersecurity Risk → Cyber Disclosure Rules** — the chain that leads from board-level treasury risk through cyber exposure down to still-forming (2023 SEC cyber disclosure, DORA in the EU) regulatory rules. All three links are relatively immature. Boards are being asked to attest to cyber posture under rules whose form is still being drafted, against a threat whose surface is still expanding.

Honourable mention: **Rating Agencies → Risk Modelling → Historical Loss Data** — the whole sovereign / corporate rating chain rests on backward-looking loss data that has limited signal for the kinds of shocks (pandemic, war, climate) that are driving 2020s risk. The chain validates on decades of "peace-time" data.

### d. Suggested gameplays

Named plays from the 61-play catalogue, applied to this map.

- **#36 Directed investment** on **GenAI Risk Analytics** and **Climate / ESG Risk Models** — the two components with the highest differentiation leverage. Concentrate engineering/quant resource here.
- **#37 Experimentation** paired with **#36** on GenAI — Genesis stage wants FIRE-style experimentation (doctrine #15), not a three-year programme plan.
- **#58 Weak Signal** on **Geopolitical Intelligence** and **Cyber Disclosure Rules** — both are where climatic patterns are actively shifting the map. Read publication types and regulator drafts as signals.
- **#43 Sensing Engines (ILC)** on the vendor ecosystem for climate-risk models — many startups (Jupiter, Climate X, XDI) compete; watch which win, then commoditise via acquisition or standard.
- **#29 Harvesting** on the climate-risk vendor space once it consolidates.
- **#15 Open Approaches** on **Statistical Methods** and **Risk Modelling libraries** — the industry benefits from open quant libraries; nobody differentiates on Black-Scholes anymore. Accelerate commoditisation of the plumbing so capacity is freed for the Genesis layer above.
- **#41 Alliances** on **Credit Bureaux** feeds and **Market Data Feeds** — second-sourcing to reduce dependency on any single vendor (especially in jurisdictions where one bureau dominates).
- **#22 Limitation of competition** is the actor-level play that incumbent banks run against fintech challengers via Regulation and AML / KYC — important to *recognise* even if not a recommended play.
- **#56 First mover** on **DORA / SEC cyber disclosure compliance** — regulatory deadlines (DORA: January 2025) create a narrow window where early-mover advantage compounds.
- **#33 Raising barriers to entry** is the climatic gameplay that incumbent **Rating Agencies** run: the regulatory endorsement (ECAI status, NRSRO) is itself a barrier. Recognise this; don't try to out-rating-agency the rating agencies.

### e. Doctrine violations / notes

Checking against Wardley's 40 principles:

- **#10 Know your users** — four anchors is appropriate for this scenario (Public, Society, Corporations, Government). The scenario explicitly names these four, and mapping to a single "customer" anchor would hide the fact that Society's need for stability and Government's need for sovereign solvency are genuinely different needs driving different parts of the chain. Satisfied.
- **#1 Focus on user needs** — anchors are user-facing (people and institutions with needs), not internal artefacts. Satisfied.
- **#9 Think small (decompose)** — some composite components remain: *Retail Banking* in particular could be decomposed into accounts / cards / mortgages, and *Regulation* into specific regime families. For this map's scope (landscape view, not a single-institution strategy map), the current granularity is appropriate; but flag for a follow-up map if the user needs it.
- **#22 Use standards where appropriate** — standards live at Stage IV. The map correctly puts Payments Rails, Encryption / PKI, and Statistical Methods in Commodity (+utility) territory. Premature standardisation of GenAI Risk Analytics or Climate Models would violate #22; the evolve arrows on those components are scenarios, not instructions to standardise now.
- **#13 Manage inertia** — the map is rich in inertia (discussed in the inertia watch below). Explicitly flagged rather than glossed as "change management."
- **#31 Strategy is complex** — GenAI, climate and geopolitical placements carry wide uncertainty; treated as ranges in the deep-placement notes below, not point estimates.
- **#7 Use appropriate methods** — the prose recommendation applies different management styles across the evolution bands: agile / FIRE for the Genesis column, Product (+rental)-stage product management for rating agencies and actuarial products, Six Sigma / ops excellence for the Commodity (+utility) layer.

No flagrant violations, but a **two-anchor-vs-four-anchor** trade-off is worth noting: in a tighter-scope map (e.g., mapping one retail bank's risk function), you would consolidate Public + Society into a single "Customer" anchor. The four-anchor choice here is deliberate because the scenario asks about the *landscape*, where the four actor-classes genuinely have distinct needs and can create mutually-reinforcing or mutually-conflicting pressures on the same components.

### f. Climatic context

Which of the 27 climatic patterns are actively shaping this map?

- **#3 Everything evolves** — the defining pattern. Perceived Risk and Trust were Custom Built forever; GenAI and Climate now force the whole lower half of the map rightward.
- **#4 Multi-wave evolution** — risk analytics has gone through waves (analyst spreadsheets → Monte Carlo engines → ML / XGBoost → LLM-assisted scenario synthesis). Each wave leaves a chasm.
- **#11 Future value is inversely proportional to certainty** — GenAI, Climate, Geopolitical and Perceived Risk are all low-certainty and therefore the highest-option-value components on the map. This is why they sit in the differentiation zone.
- **#15 Past success breeds inertia / #16 Inertia increases with past success / #17 Inertia can kill** — Rating Agencies are the textbook case. Their past-success weight (the three-agency oligopoly that survived the 2008 accusation of structural failure) creates supplier-side inertia against reinventing a model whose training data predates most of the risks the 2020s actually face.
- **#18 You cannot measure evolution over time or adoption** — the evolve arrows are scenarios, not schedules.
- **#22 Two forms of disruption** — the map contains both: Genesis disruption (GenAI from outside the industry) and Product-to-utility disruption (stress testing maturing into regulator-prescribed utility).
- **#23 Industrialisation causes organisations to evolve** — Capital Requirements (Basel) + Stress Testing maturing to Stage III forces bank risk functions themselves to restructure.
- **#24 Efficiency enables innovation** — commoditising statistical methods and cloud compute frees quant capacity to work on GenAI and Climate models. Banks that haven't yet made that shift are paying the innovation-capacity tax twice.
- **#27 Shifts from product to utility demonstrate a punctuated equilibrium** — Stress Testing and, over the next few years, Cyber Disclosure Rules, look like product-to-utility transitions. When they cross, they cross fast.

### g. Deep-placement notes

Deep placement was done on four components where the cheat-sheet rows disagreed or the component is strategically pivotal and in a specialised / recent domain.

1. **GenAI Risk Analytics** — initial cheat-sheet pass placed this around 0.25 (just into Custom Built) because of 2023's rapid experimentation pace. Deeper look: research publications still dominated by "describe the wonder" papers (row 7); market perception is chaotic (row 10: domain of experts, not widespread); failure tolerance is high (row 16). These are Stage I signals. Moved to **0.15 (mid-Genesis)**. Uncertainty is wide — a credible case exists for 0.25 by late 2024 as early vendors productise. Flagged as in-transition.

2. **Climate / ESG Risk Models** — cheat-sheet rows disagreed. Ubiquity (row 5) is rising fast (regulatory mandates), so row says Stage III; but Certainty (row 6) is low, Publication types (row 7) are still "build / construct / awareness", Market (row 8) is forming, and Perception (row 10) is chaotic and contested. Var(ε) across these rows exceeds the 0.03 threshold. Settled at **0.25 (boundary Genesis / Custom Built)** with a range [0.15, 0.40]. Specialised-domain concession: this is a regulated, geographically fragmented market; placements differ by jurisdiction.

3. **Rating Agencies** — surprisingly hard to place. Ubiquity is high (row 5: widespread use) and Market (row 8) is mature, pointing at Stage IV. But Focus of Value (row 13) is still high-profit (Stage III); vendor count is concentrated to three firms (Moody's, S&P, Fitch) rather than the many-supplier shape of a true Stage IV utility. Public data on the sector shows high margins (>40%) maintained despite decades of regulatory scrutiny — that's Stage III pricing power, not Stage IV commodity economics. Placed at **0.70 (late Stage III, early Product-to-Commodity transition)**. The map notes this as a position under active inertia (forms #15, #17 supplier-side).

4. **Geopolitical Intelligence** — the scenario is explicitly ~2023, post-2022 Russia / Ukraine shock. Historically, geopolitical-risk teams were bespoke analyst functions (Stage II). 2022–23 saw explosive commercial activity: Control Risks, Verisk Maplecroft, Kharon, and incumbent data vendors (Bloomberg, Refinitiv) all shipping geopolitical-risk products. Publication types (row 7) are mixed — still "build / construct / awareness" dominating, but "maintenance / features" increasing. Placed at **0.30 (late Genesis / early Custom Built)**, trending to Custom Built. This is where the evolve arrow to ~0.55 reflects a 2–3 year scenario. Range [0.20, 0.45] acknowledges disagreement.

Components deliberately *not* deep-placed (obvious commodities): Cloud Compute, Payments Rails, Encryption / PKI, Statistical Methods, Credit Bureaux, Identity / Auth. All solidly Commodity (+utility) — the cheat-sheet rows agree and extra research would not change the placement.

### Inertia watch — where the landscape resists change

From the 17 structured forms, these dominate the map:

- **#2 Sunk capital** and **#9 Re-architecture cost** — tier-1 banks' risk engines are often decades of accreted C++, spreadsheets, and vendor contracts. Moving to cloud-native GenAI stacks is expensive and slow.
- **#4 Human capital** — quant talent is trained on traditional risk modelling; retraining or cultural change toward ML/LLM risk work is real effort.
- **#7 Supplier-trust concerns** / **#11 Suitability doubt** — boards and regulators legitimately question whether GenAI outputs are suitable for capital decisions. This is healthy scepticism, but it also slows adoption.
- **#14 Strategic-control loss** — regulators are wary of banks' whole risk function depending on one or two cloud providers or one or two AI model vendors.
- **#15 Past-success data / cannibalisation fear** — Rating Agencies specifically. Their business model depends on an oligopoly that regulators have repeatedly criticised but not dismantled.
- **#17 Financial-market expectations** — publicly-listed incumbents cannot easily switch to utility-margin businesses without shareholder revolt.
- **#3 Political capital** — the executive who authorised the last risk system cannot easily champion replacing it.

### Where risk management is most exposed (the explicit question)

Pulling the thread the user asked about: the places where this map is **most exposed** are where a user-visible component depends on a foundation that has not matured enough to bear the weight being put on it. In rank order:

1. **Board-level scenario and stress-test conclusions that rely on GenAI Risk Analytics or Climate / ESG Risk Models.** Both are Genesis-stage foundations being asked to inform decisions with capital-adequacy consequences. A hallucinated scenario or a model that miscalibrates tail risk propagates to Capital Requirements and ultimately to whether the bank has enough capital to survive the shock it modelled. This is the dependency-risk that matters most.

2. **Rating-agency-dependent sovereign and corporate decisions exposed to tail events their training data never saw.** A 2020s shock (pandemic, war, climate, sovereign debt spiral) stresses the historical-loss-data foundation of the ratings process. The shape of the dependency is visible-to-the-point-of-public-debate (sovereign downgrades move markets) resting on methods industrialised for a quieter era.

3. **Perceived Risk and Trust in Institutions — the perception layer on top of the whole stack.** This is actually the map's most politically volatile exposure. Perceived Risk sits close to Public and Society but is still Custom Built as a managed asset. A bank run (SVB, March 2023) is a perception cascade, not a mechanical consequence of the balance sheet; the map shape explains why traditional risk management misses it. Institutions under-invest in perception management because it doesn't fit neatly into any Stage III product bucket.

4. **Cybersecurity Risk → Cyber Disclosure Rules → Encryption / PKI** — the chain where visible corporate and government operations depend on a mid-chain regulatory regime still being drafted, with an industrialised cryptographic foundation that faces a non-trivial post-quantum transition over the next decade.

5. **Geopolitical Intelligence for territorial and political risk.** A Custom Built analytic service supporting decisions (sanctions compliance, supply-chain re-shoring, sovereign exposure limits) that now matter enormously. Since 2022 this has been in rapid evolution — the uncertainty is the exposure.

The single-line summary: **risk management is most exposed at the points where 2020s-era risks (climate, geopolitics, cyber, AI-driven scenarios, perception cascades) meet 2000s-era foundations.**

### h. Caveat

Evolution trajectories (the `evolve` arrows to GenAI Risk Analytics 0.50, Climate / ESG 0.55, Cyber Disclosure 0.60, Geopolitical Intelligence 0.55) are **scenarios, not forecasts**. Wardley's climatic pattern #18 applies in full force: *"you cannot measure evolution over time or adoption."* Treat trajectories as plausible stories that inform options, not as predictions that inform budgets.

All placements are judgement on a cheat sheet, not ground truth. Re-map every 6–12 months as the regulatory, vendor, and technology signals shift — especially in climate, GenAI, and geopolitics where 2023–2025 signals are still actively contested.

---

## Validator output

```
OK: 41 components/anchors, 80 edges — no violations.
```

(Validator: `python3 ${CLAUDE_SKILL_DIR}/scripts/validate_owm.py draft.owm` against the OWM block above. The visibility constraint ν(a) ≥ ν(b) is satisfied for every edge; every edge endpoint exists; all coordinates lie in [0, 1].)
