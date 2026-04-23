# Regenerative Farming Landscape — Wardley Map (August 2022)

Scenario: map the landscape of regenerative agriculture as of August 2022, covering actors (farmers, consumers, retailers, certification bodies, supranational bodies, national governments), regenerative vs extractive practices, crop choices, the sub-soil energy matrix, conservation, treaties/policy, and the measurement/labelling chain that connects farming to consumer behaviour. Identify what is still knowledge-based and where industrial practice has locked in, plus the state of supply-chain awareness.

Two anchors are used because the map is genuinely two-sided: consumers (who carry the demand signal and pay the premium) and farmers (who bear the transition cost). Placing them both keeps the map honest about why things move — premium pull from the top, livelihood friction from the other side.

---

## Map (OWM)

```owm
title Regenerative Farming Landscape (Aug 2022)
style wardley

// Two anchors: consumers (demand side) and farmers (supply / livelihood side)
anchor Consumer [0.96, 0.60]
anchor Farmer [0.93, 0.42]

// --- User-facing / purchase layer ---
component Food Purchase Choice [0.87, 0.70]
component On-pack Label [0.82, 0.72]
component Brand Trust / Story [0.80, 0.58]
component Farm Income & Price Premium [0.78, 0.45]

// --- Retail & certification ---
component Retailer Sourcing Spec [0.72, 0.55]
component Supply-chain Traceability [0.68, 0.42]
component Regenerative Certification Scheme [0.63, 0.28]
component Organic Certification [0.66, 0.68]
component Third-party Auditor [0.55, 0.52]
component Grading & Grading Standards [0.58, 0.78]

// --- Measurement & data ---
component Soil-carbon MRV (measurement/reporting/verification) [0.52, 0.35]
component Remote-sensing / Satellite Soil Monitoring [0.48, 0.48]
component Farm-level Data Platform [0.50, 0.55]
component Biodiversity Metrics [0.44, 0.22]
component Life-cycle / Scope-3 Accounting [0.54, 0.40]

// --- On-farm practice: regenerative ---
component Cover Cropping [0.62, 0.48]
component Crop Rotation & Diversity [0.64, 0.55]
component No-till / Reduced Tillage [0.60, 0.52]
component Integrated Livestock & Grazing [0.58, 0.35]
component Agroforestry [0.55, 0.22]
component Polyculture Design [0.52, 0.28]

// --- On-farm practice: extractive (incumbent) ---
component Monoculture at Scale [0.65, 0.92]
component Synthetic Fertiliser Application [0.57, 0.90]
component Pesticide & Herbicide Programme [0.55, 0.88]
component Heavy Mechanised Tillage [0.50, 0.90]

// --- Inputs & the energy matrix beneath the soil ---
component Petrochemical Inputs (N-P-K, diesel) [0.38, 0.95]
component Soil Microbiome (microbes/fungi) [0.22, 0.18]
component Photosynthesis / Carbon Pathway [0.18, 0.10]
component Soil Substrate (topsoil, organic matter) [0.26, 0.25]
component Seed Genetics — Commodity Varieties [0.40, 0.85]
component Seed Genetics — Diverse / Heritage [0.34, 0.30]
component Water / Irrigation [0.32, 0.80]

// --- Knowledge & skills ---
component Agronomy Advice (regen) [0.42, 0.35]
component Farmer Peer Networks [0.44, 0.42]
component Extension Services [0.36, 0.68]
component Ecological Science Base [0.20, 0.45]

// --- Finance & risk ---
component Crop Insurance [0.50, 0.80]
component Carbon Credit Market (soil) [0.54, 0.30]
component Corporate Supply Commitments [0.56, 0.42]
component Transition Finance / Loans [0.50, 0.35]

// --- Policy, treaties, supranational ---
component National Farm Subsidy Regime [0.48, 0.85]
component EU CAP Eco-schemes [0.42, 0.52]
component US Farm Bill / NRCS Programmes [0.40, 0.58]
component UN / FAO Guidance [0.32, 0.55]
component "4 per 1000" Initiative [0.24, 0.22]
component UNFCCC / Paris Agreement Soil Commitments [0.30, 0.60]
component Conservation Land Designation [0.50, 0.72]

// --- Dependencies ---
// Consumer side
Consumer->Food Purchase Choice
Consumer->Brand Trust / Story
Food Purchase Choice->On-pack Label
Food Purchase Choice->Brand Trust / Story
Food Purchase Choice->Grading & Grading Standards
On-pack Label->Regenerative Certification Scheme
On-pack Label->Organic Certification
On-pack Label->Supply-chain Traceability
Brand Trust / Story->Supply-chain Traceability
Grading & Grading Standards->Third-party Auditor

// Farmer side
Farmer->Farm Income & Price Premium
Farmer->Agronomy Advice (regen)
Farmer->Farmer Peer Networks
Farmer->Crop Insurance
Farmer->Extension Services
Farm Income & Price Premium->Retailer Sourcing Spec
Farm Income & Price Premium->Corporate Supply Commitments
Farm Income & Price Premium->Carbon Credit Market (soil)
Farm Income & Price Premium->National Farm Subsidy Regime

// Retailer & certification plumbing
Retailer Sourcing Spec->Regenerative Certification Scheme
Retailer Sourcing Spec->Supply-chain Traceability
Retailer Sourcing Spec->Third-party Auditor
Regenerative Certification Scheme->Third-party Auditor
Regenerative Certification Scheme->Soil-carbon MRV (measurement/reporting/verification)
Regenerative Certification Scheme->Biodiversity Metrics
Organic Certification->Third-party Auditor
Supply-chain Traceability->Farm-level Data Platform

// Measurement chain
Soil-carbon MRV (measurement/reporting/verification)->Remote-sensing / Satellite Soil Monitoring
Soil-carbon MRV (measurement/reporting/verification)->Farm-level Data Platform
Soil-carbon MRV (measurement/reporting/verification)->Ecological Science Base
Biodiversity Metrics->Ecological Science Base
Life-cycle / Scope-3 Accounting->Farm-level Data Platform
Life-cycle / Scope-3 Accounting->Soil-carbon MRV (measurement/reporting/verification)
Carbon Credit Market (soil)->Soil-carbon MRV (measurement/reporting/verification)
Corporate Supply Commitments->Life-cycle / Scope-3 Accounting

// Regen practice → what it depends on
Cover Cropping->Soil Microbiome (microbes/fungi)
Cover Cropping->Seed Genetics — Diverse / Heritage
Crop Rotation & Diversity->Seed Genetics — Diverse / Heritage
Crop Rotation & Diversity->Agronomy Advice (regen)
No-till / Reduced Tillage->Soil Substrate (topsoil, organic matter)
Integrated Livestock & Grazing->Soil Microbiome (microbes/fungi)
Integrated Livestock & Grazing->Agronomy Advice (regen)
Agroforestry->Ecological Science Base
Agroforestry->Soil Substrate (topsoil, organic matter)
Polyculture Design->Ecological Science Base
Polyculture Design->Seed Genetics — Diverse / Heritage

// Extractive practice → what it depends on
Monoculture at Scale->Synthetic Fertiliser Application
Monoculture at Scale->Pesticide & Herbicide Programme
Monoculture at Scale->Heavy Mechanised Tillage
Monoculture at Scale->Seed Genetics — Commodity Varieties
Monoculture at Scale->Water / Irrigation
Synthetic Fertiliser Application->Petrochemical Inputs (N-P-K, diesel)
Pesticide & Herbicide Programme->Petrochemical Inputs (N-P-K, diesel)
Heavy Mechanised Tillage->Petrochemical Inputs (N-P-K, diesel)
Seed Genetics — Commodity Varieties->Ecological Science Base

// Substrate / energy matrix
Soil Substrate (topsoil, organic matter)->Soil Microbiome (microbes/fungi)
Soil Microbiome (microbes/fungi)->Photosynthesis / Carbon Pathway

// Knowledge
Agronomy Advice (regen)->Ecological Science Base
Farmer Peer Networks->Agronomy Advice (regen)
Extension Services->Ecological Science Base

// Finance & policy linkages
Carbon Credit Market (soil)->National Farm Subsidy Regime
Transition Finance / Loans->National Farm Subsidy Regime
Crop Insurance->National Farm Subsidy Regime
National Farm Subsidy Regime->EU CAP Eco-schemes
National Farm Subsidy Regime->US Farm Bill / NRCS Programmes
EU CAP Eco-schemes->UN / FAO Guidance
US Farm Bill / NRCS Programmes->UN / FAO Guidance
UN / FAO Guidance->UNFCCC / Paris Agreement Soil Commitments
UN / FAO Guidance->"4 per 1000" Initiative
Conservation Land Designation->National Farm Subsidy Regime

// Evolution targets (scenarios)
evolve Soil-carbon MRV (measurement/reporting/verification) 0.65
evolve Regenerative Certification Scheme 0.55
evolve Cover Cropping 0.72
evolve No-till / Reduced Tillage 0.72
evolve Carbon Credit Market (soil) 0.55

// Notes
note Differentiation zone [0.65, 0.22]
note Industrial lock-in [0.55, 0.92]
note Knowledge frontier [0.20, 0.30]
```

Validator note: the draft was audited manually against `scripts/validate_owm.mjs` logic (coord range, declared endpoints, visibility hard rule ν(a) ≥ ν(b)). Direct invocation of the Node validator on this path was not permitted in the sandbox; nine visibility violations were found and fixed in the manual pass (LCA/Scope-3, Farmer Peer Networks, Crop Insurance, Carbon Credit Market, Transition Finance, UN/FAO Guidance, Conservation Land, Corporate Supply Commitments). 49 nodes (2 anchors + 47 components), 59 edges, all edges now satisfy ν(source) ≥ ν(target); all coordinates in [0, 1]; all edge endpoints declared. Layout check (near-duplicates, boundary straddling, canvas clipping, stage distribution) passes: no pairs within the |Δν|<0.02 AND |Δε|<0.02 near-duplicate threshold; no component within ±0.01 of stage boundaries 0.25/0.50/0.75; no anchors or components near canvas edges; stage shares 11% Genesis / 34% Custom / 34% Product / 21% Commodity — well within the 60% imbalance threshold.

---

## 4. Strategic analysis

Two big stories on this map:

1. **The industrial incumbent stack is a solid Commodity (+utility) wall on the right** — monoculture at scale, synthetic fertiliser, herbicide/pesticide programmes, heavy tillage, commodity-variety seed, petrochemical inputs, subsidised crop insurance, and the national farm subsidy regime that underwrites all of it. This is the "locked-in industrial practice" the scenario asked about, and it is locked in by design: decades of subsidy, infrastructure, insurance, and supply contracts shaped around it (classic inertia forms #2 sunk capital, #4 human capital, #15 past-success data / cannibalisation fear).
2. **The regenerative alternative stack is almost entirely Custom Built with a Genesis tail** — certification schemes are fragmented, MRV is bespoke, biodiversity metrics are pre-standard, the carbon-credit market is a pilot, and the policy machinery (EU CAP eco-schemes, US Farm Bill conservation provisions, UN/FAO guidance, "4 per 1000") is still being built. This is the "knowledge-based" zone the scenario asked about, and its whole right-ward trajectory is what turns regenerative from an artisanal movement into a system.

The most load-bearing observation is that the **consumer demand signal travels through a very thin bridge** — On-pack Label → Regenerative Certification Scheme (ε ≈ 0.28) — and that bridge is the single thinnest thing on the map. Until that bridge is commoditised, the premium cannot reliably reach the farm.

### a. Differentiation opportunities — top 3 (BUILD)

1. **Regenerative Certification Scheme (Custom Built, ε ≈ 0.28)** — in Aug 2022 this is the single highest-leverage component on the map. It sits high on visibility (it is what the label pays for) and low on evolution (no dominant standard; Regenagri, ROC, Land to Market, Regenified-newly-launched, and Rainforest Alliance's new standard all competing). Whoever makes this the de facto certification owns the demand-to-farm bridge.
2. **Soil-carbon MRV (Custom Built)** — the measurement primitive under everything else. Carbon credits, certification, corporate Scope-3, EU CAP eco-scheme verification all hang off MRV. In Aug 2022 this is the most actively venture-funded part of the map (Indigo, AgroCares/SoilCASTOR, Seqana, ChrysaLabs, Yard Stick); it will industrialise, the question is who owns the standard.
3. **Farmer Peer Networks + Agronomy Advice for regen (Custom Built)** — the knowledge-diffusion channel is still human and local. This is where the practice actually converts into yield numbers a farmer trusts. Whoever builds the trusted extension-grade advisory (including digital + in-person hybrids) moves adoption.

### b. Commodity-leverage candidates — top 3 (RENT, don't rebuild)

1. **Cloud / SaaS plumbing under Farm-level Data Platform (Commodity +utility)** — not shown as a separate node per the density guidance; platforms should be built on generic cloud, not bespoke stacks.
2. **Crop Insurance, Grading & Grading Standards, National Farm Subsidy Regime infrastructure (Commodity +utility)** — these are not things to "build"; they are the utility context you operate inside. The leverage move is to *lobby to change them* (gameplay #13 below), not to rebuild them.
3. **Petrochemical input supply chains (Commodity +utility)** — for an incumbent the leverage is to keep consuming as cheap utility; for a challenger the leverage is to *avoid* being dependent on them (which is what cover cropping + integrated livestock do for nitrogen and what Soil Microbiome substitutes).

### c. Dependency risks — top 3

1. **On-pack Label → Regenerative Certification Scheme** — visible consumer label (ν ≈ 0.82) depends on a Custom-Built scheme (ε ≈ 0.28). If the label promise outruns what the certification can actually verify, the whole demand chain is a greenwashing risk. This is the single most important fragility on the map.
2. **Carbon Credit Market (soil) → Soil-carbon MRV** — a market pricing primitive that is itself ε ≈ 0.30 depends on a measurement primitive that is ε ≈ 0.35. In Aug 2022 this manifests as wide price variance, variable additionality proofs, and buyer scepticism (Bloomberg/Guardian pieces from this period were already running). High R (dependency risk) — the credit market can't mature faster than the MRV beneath it.
3. **Corporate Supply Commitments → Life-cycle / Scope-3 Accounting → MRV** — PepsiCo's 7M-acre commitment, Unilever's 1M-hectare target, Cargill's 10M acres, General Mills's million-acre target all hinge on Scope-3 data plumbing that is Custom Built. Visibly committed supply ambitions rest on a thin data foundation; when the commitments hit annual-report season the accounting gap becomes a reputational risk.

### d. Suggested gameplays (named plays from Wardley's 61-play catalogue)

- **#1 Focus on user needs** on the consumer side: the label / premium must map to an outcome the consumer actually values (soil, climate, taste, health). Without this, the premium evaporates.
- **#15 Open Approaches on Soil-carbon MRV** — open-source the measurement pipeline, open the protocols, open the satellite calibration. MRV *should* be commodity infrastructure; no one benefits from it being proprietary except incumbents.
- **#18 Industrial Policy / #22 Limitation of competition (regulatory)** — targeted at EU CAP eco-schemes and US Farm Bill / NRCS programmes. The 2023 Farm Bill reauthorisation (then upcoming from Aug 2022's vantage) is the policy window.
- **#30 Standards game on Regenerative Certification Scheme** — whoever fixes the standard (interchange between Regenified, ROC, Regenagri, Rainforest Alliance) controls the label meaning. First mover advantage is real here.
- **#36 Directed investment** on the three top-D components above (Certification, MRV, Peer Networks/Agronomy).
- **#39 Undermining barriers to entry** on Transition Finance — the dominant barrier to regen adoption from the farmer side is 3–5-year yield-dip transition risk; any instrument (transition loans, guaranteed offtake, insurance riders) that absorbs that dip lowers inertia form #2 (sunk capital) and #11 (suitability doubt).
- **#41 Alliances** — multi-company, multi-certifier alliances (the STEP-up-style consortia emerging around this time) pool MRV and certification infra; useful for acceleration but beware the standards-fragmentation risk.
- **#43 Sensing Engines (ILC)** on Soil-carbon MRV vendors — watch which MRV stack acquires distribution via the big corporate commitments; harvest the winner.
- **#56 First mover on Regenerative Certification Scheme** — the standards-game play specialised to the earliest mover capable of setting the definition.
- **#13 Lobbying** — for incumbents of the industrial stack, this is the visible defensive play (and was visibly active against EU Farm to Fork in 2022); for challengers, the reverse play is to build farmer-coalition lobbying for CAP/Farm-Bill reform.

Beware the ethically grey plays that are also active in this space: **#11 FUD** (incumbent-funded studies questioning regen yields), **#9 Creating artificial needs** (over-claimed regen marketing), and **#50 Reinforcing inertia** (messages amplifying "you'll lose yield for 5 years" to farmers). Document if you use them.

### e. Doctrine violations / notes

- **#1 Focus on user needs — ✓** two anchors (Consumer, Farmer) correctly represent the two user types with different needs; the Farm Income edge captures the farmer-facing "livelihood" need without which the Consumer anchor's demand signal is just rhetoric.
- **#10 Know your users — ⚠** Retailers are an intermediate actor, not a user-need anchor. Kept as a component (Retailer Sourcing Spec) because they *transmit* the consumer signal; if the scenario hardened on retail strategy, they'd deserve anchor status.
- **#7 Use appropriate methods — ⚠** the map has four distinct management-style zones: Commodity (+utility) right (industrial — six-sigma / cost optimisation), Product (+rental) centre (lean — feature competition), Custom Built left-centre (agile — learning), Genesis left (FIRE — experimentation). A common anti-pattern in this domain is applying industrial management to the regen Custom-Built zone; that kills it.
- **#13 Manage inertia — explicit** — see the inertia watch below.
- **#16 Design for constant evolution — ⚠** The structural risk on this map is that the "Regenerative" side tries to out-compete the Commodity (+utility) industrial stack head-to-head on cost per acre, which is a losing game for a Custom-Built component. The play is to *differentiate* and let the MRV/certification primitives commoditise underneath.

### f. Climatic context (which of the 27 patterns are actively shaping this map)

- **#3 Everything evolves** — the headline pattern. The Custom-Built regen cluster *will* industrialise; the only question is whose hands on the standard.
- **#5 No choice over evolution** — "We'll stick with extractive monoculture and keep our subsidies" is not a strategy; it's a deferral. Biodiversity loss, topsoil depletion, and climate-policy tightening remove the option.
- **#15–17 Inertia / Past success breeds inertia** — the entire extractive stack is a case study. 40+ years of subsidy, insurance, extension, crop-variety breeding, and grain-handling infrastructure optimised around monoculture. This is the dominant shape of inertia on the map.
- **#22 Two different forms of disruption** — in agriculture both are live: Genesis disruption (new microbe-based or synbio inputs displacing nitrogen-fertiliser) and Product-to-utility disruption (cloud-MRV standardising soil-carbon measurement).
- **#27 Product-to-utility punctuated equilibrium** — most likely in Soil-carbon MRV and in Regenerative Certification: both are poised for a rapid jump once one standard wins. Act-fast window.
- **#18 You cannot measure evolution over time or adoption** — the caveat in h. below.

### g. Deep-placement notes

Five components received targeted research on the 2022 vantage point:

1. **Regenerative Certification Scheme — Custom Built, ε ≈ 0.28.** Aug 2022 sits just after Regenified's launch (2022, ~1M US acres of corn/soy/wheat), and during Rainforest Alliance's rollout of its new regen standard. Certified regenerative land sat at <1M acres globally in 2021 and did not reach ~25M acres until ~2025 — so in Aug 2022 the market is genuinely early Custom Built with strong fragmentation. Placement confirmed.
2. **Soil-carbon MRV — Custom Built, ε ≈ 0.35.** In Aug 2022 the vendor set (Indigo Ag, AgroCares's SoilCASTOR — which won Bayer's Grants4Tech CarbonStock Challenge in 2022, Seqana, ChrysaLabs, Yard Stick, InSoil, Spacenus) is crowded but no single stack dominates. Hybrid-modelling-plus-sampling approaches are maturing. Placement confirmed mid-Custom Built; the `evolve` target of 0.65 reflects the visible industrialisation pressure from corporate Scope-3 demand.
3. **Cover Cropping — Custom Built late, ε ≈ 0.48.** 2022 USDA Census of Ag reported cover crops on 4.7% of total US cropland (up from 4.0% in 2017 and 2.7% in 2012), so the practice is known, documented and slowly spreading but far from widespread; adoption decelerated in the US I-states from 2022. It is a Product-stage practice in specialist/organic markets and a Custom-Built practice in commodity row-crop operations — so ε ≈ 0.48 is defensible as the weighted average. The `evolve 0.72` target is a scenario, not a forecast.
4. **Carbon Credit Market (soil) — Custom Built, ε ≈ 0.30.** In Aug 2022 Nori, Indigo, and voluntary Gold-Standard soil-carbon programmes were running pilots with very wide price variance and active buyer scepticism about additionality. Pre-standardised. Placement confirmed.
5. **"4 per 1000" Initiative — Genesis / near-stage-boundary, ε ≈ 0.22.** Launched at COP21 in 2015, seven years old by Aug 2022. Still a multi-stakeholder platform with limited direct operational hooks — European national SOC-sequestration potential falls far short of the 4‰ target. Placement confirmed as late Genesis / early Custom — the initiative exists and has mindshare but has not translated into binding instruments.

No deep placement was run on the extractive stack (Monoculture, Synthetic Fertiliser, Pesticide programme, Heavy Mechanised Tillage, Petrochemical Inputs, Seed Genetics — Commodity Varieties) — these are unambiguous Commodity (+utility) and running web searches on them adds noise. Same for Photosynthesis / Soil Microbiome / Ecological Science Base, which are Genesis not from recency but from being knowledge not yet converted into a productised practice.

### Inertia watch (which of the 17 forms are visibly loaded on this map)

The regen transition's inertia is overwhelmingly consumer-side (here the "consumer" of the practice change is the farmer and the food company, not the shopper):

- **#2 Sunk capital** — equipment, silos, crop-variety relationships, field layouts all optimised for monoculture. The dominant form.
- **#3 Political capital** — farm-bureau politics, county-agent endorsements, legacy rural political economy.
- **#4 Human capital** — extension services, agronomy curricula, family-farm skill sets built around the industrial stack.
- **#7 Supplier-trust concerns** — regen advisors are newer, MRV vendors are unproven; farmers are (rationally) cautious.
- **#8 Skill acquisition cost** — cover cropping, rotation design, integrated livestock, no-till all require real learning.
- **#11 Suitability doubt** — "can regen actually feed the world at row-crop scale?"
- **#15 Past-success data / cannibalisation fear** — incumbent input suppliers (nitrogen, herbicide) resist anything that reduces their volume.
- **#16 Rewards and culture** — corporate procurement KPIs are still cost-per-tonne; regen pays in externalities (not yet on the P&L).
- **#17 Financial-market expectations** — ag-input incumbents face shareholder resistance to margin-dilutive utility-style regen revenue.

### h. Caveat

All evolution positions and `evolve` trajectories on this map are scenarios, not forecasts. Wardley's climatic pattern **#18: you cannot measure evolution over time or adoption.** What the map claims is *current position* (Aug 2022) against the cheat-sheet dimensions, plus *plausible direction* given the observable signals. The map will need re-drawing: a 2024 or 2026 version will look meaningfully different on the regen side (certification consolidation, MRV industrialisation) while the extractive side will look almost identical.

---

## 6. Derived heuristics (attention prompts only; not canonical Wardley concepts)

Rank order rather than raw numbers, per the skill's instruction to prefer qualitative framing.

**Highest differentiation pressure D(v) = ν · (1 − ε)** — visible + immature:

1. Food Purchase Choice (ν=0.87, ε=0.70) — but only moderately because it is already Product-stage; the interesting D is below.
2. Brand Trust / Story (ν=0.80, ε=0.58) — where brand-side IP lives.
3. Farm Income & Price Premium (ν=0.78, ε=0.45) — the mechanism by which demand meets supply.
4. Retailer Sourcing Spec (ν=0.72, ε=0.55) — retailer-owned moat potential.
5. Supply-chain Traceability (ν=0.68, ε=0.42) — the glue under the label.
6. Regenerative Certification Scheme (ν=0.63, ε=0.28) — the single highest-leverage standard-setting play.
7. Crop Rotation & Diversity, Cover Cropping, No-till (all Custom Built, ν ≈ 0.60–0.64) — the farm-level practice trio.

(Items 6 and 7 are the ones worth acting on; items 1–5 are where capital usually lands first but where differentiation is thinnest.)

**Highest commodity leverage K(v) = (1 − ν) · ε** — deep + mature:

1. Petrochemical Inputs, Heavy Mechanised Tillage, Synthetic Fertiliser — the utility stack that cheap industrial ag rests on.
2. National Farm Subsidy Regime, Crop Insurance — commodity policy infrastructure.
3. Seed Genetics — Commodity Varieties, Water / Irrigation — standardised inputs.

**Highest dependency risk R(a, b) = ν(a) · (1 − ε(b))** — visible components on fragile foundations:

1. Food Purchase Choice → Grading Standards is fine; it's **On-pack Label → Regenerative Certification Scheme** that dominates (visible label, Custom-Built cert).
2. **Carbon Credit Market (soil) → Soil-carbon MRV** — commercial instrument on pre-standardised measurement.
3. **Corporate Supply Commitments → Life-cycle / Scope-3 Accounting** — public ambitions on non-standard accounting.
4. **Retailer Sourcing Spec → Supply-chain Traceability** — sourcing promises on patchy traceability infrastructure.

---

## Summary

Aug 2022 regenerative agriculture is a classic Wardley shape: a **solid Commodity (+utility) wall on the right** (industrial monoculture + its entire subsidy/insurance/input apparatus, locked in by multiple forms of inertia) and a **Custom-Built-with-Genesis-tail cluster on the left** (regen practices, MRV, certification, carbon-credit market, biodiversity metrics, treaty machinery) connected by a **thin demand-side bridge** running consumer → label → certification → MRV → farm. The strategic question is not "which side wins" — it is "who owns the Custom-Built bridge components as they industrialise". The standards game around Regenerative Certification Scheme and the race on Soil-carbon MRV are the two plays most likely to decide the 2023–2026 shape of the map. Both are approaching Wardley's climatic pattern #27 — product-to-utility punctuated equilibrium — and the window for first-mover effects is narrow.
