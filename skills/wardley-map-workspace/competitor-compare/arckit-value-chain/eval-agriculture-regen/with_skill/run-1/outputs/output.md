# Wardley Value Chain — Regenerative Agriculture Landscape (August 2022)

**Document ID**: ARC-000-WVCH-001-v1.0
**Date**: 2026-04-23
**Document Type**: Wardley Value Chain
**Command**: arckit.wardley.value-chain
**Classification**: PUBLIC
**Owner**: [PENDING]
**Reviewer**: [PENDING]
**Approver**: [PENDING]
**Distribution**: Project Team, Architecture Team

| Version | Date | Author | Summary | Reviewer | Approver |
|---------|------|--------|---------|----------|----------|
| 1.0 | 2026-04-23 | ArcKit AI | Initial creation from `$arckit-wardley.value-chain` command | [PENDING] | [PENDING] |

---

## Prerequisite Warnings

- **REQ (Requirements) — MISSING.** No structured requirements document was supplied. Per the skill, this is a MANDATORY input; its absence means the value chain is anchored directly on the free-form scenario rather than on validated user needs. Recommend running `$arckit-requirements` before the chain is used for a decision.
- **STKE (Stakeholder Analysis) — MISSING.** User personas were inferred from the scenario text (consumers, farmers, retailers, certification bodies, governments, supranational institutions). Recommend running `$arckit-stakeholders` to validate personas and success metrics.
- **PRIN (Architecture Principles) — MISSING.** No enterprise standards or build/buy preferences available.
- **External documents — NONE.** No prior WVCH artifacts, policy catalogues, soil-science references, or supply-chain maps were provided.

## Executive Summary

**Anchor**: Consumer can access food produced in ways that regenerate rather than deplete the land.

Twenty components were identified across seven visibility tiers, spanning consumer-facing demand signals (purchasing, retail, labelling), measurement and certification plumbing, the two rival practice families (regenerative and extractive at industrial scale), national and supranational governance, and the deep biological substrate (soil health, microbial activity, photosynthesis). Three strategic insights emerge. (1) The **measurement-and-grading layer is the structural bottleneck** — consumer purchasing, retail stocking, and policy implementation all ultimately read from the same thin, immature evidence pipeline. (2) **Extractive practice at scale is far more locked in than its surface visibility suggests**: it shares petrochemical inputs and a near-uniform monoculture substrate with the global grain system, so its effective commoditisation is structural rather than merely preferential. (3) The **biological substrate (soil → microbes → photosynthesis) is the commodity floor** shared by both rival practice families — yet it is simultaneously the least-instrumented layer, which is why the scenario's "what's still knowledge-based" question resolves largely to this tier.

## Users and Personas

| Persona | Primary Need | Trust / Purchase Gate |
|---------|--------------|-----------------------|
| Consumer | Buy food that matches stated values without being misled | Product label, retailer reputation |
| Farmer | Make land-use decisions that are economically viable and ecologically improving | Price premium, subsidy, peer knowledge |
| Retailer | Stock shelves with credible claims that match category demand | Certification, supply-chain audit |
| Certification Body | Issue claims that withstand audit and public scrutiny | Measurement evidence, standards |
| National Government | Meet food-security and climate obligations via agricultural policy | Policy instruments, treaty obligations |
| Supranational Body (UN / FAO) | Coordinate cross-border targets on food, climate, biodiversity | Treaties, voluntary frameworks |

## Value Chain — Anchor Statement

```text
Anchor: Consumer can access food produced in ways that regenerate rather than deplete the land
User:   Food consumers (with retail, certification, policy, and farm actors mediating the chain)
Outcome: A purchase decision reliably reflects the regenerative / extractive character of the food
```

## Value Chain Diagram — ASCII

```text
vis
1.0 |  Consumer Access to Regenerative Food                           (anchor)
    |         |              |              |
0.90|   Purchasing Decision  |              |
0.85|         |         Retail Distribution  Food Production
0.78|     Product Labelling   \                    |
0.72|              \      Supply Chain Transparency|
0.70|               \            /            Farm Management
    |                \          /                 /    \
0.65|            Measurement and Grading         /      \
0.60|            Certification and Standards    /        \
0.58|                           Regenerative Practice    Extractive Practice
0.52|                                         National Agricultural Policy
0.48|                       Crop Rotation    Crop Diversity
0.46|                                               Monoculture
0.42|                          Conservation Practice
0.38|                       International Policy Framework
0.32|                                               Petrochemical Inputs
0.28|                           Soil Health
    |                                |
0.18|                          Soil Microbial Activity
    |                                |
0.10|                          Photosynthesis                  (commodity floor)
```

## OWM Syntax (for https://create.wardleymaps.ai)

```owm
title Regenerative Agriculture Landscape (August 2022)

anchor Consumer Access to Regenerative Food [0.95, 0.50]

component Consumer Purchasing Decision [0.90, 0.50]
component Retail Distribution [0.85, 0.50]
component Food Production [0.85, 0.50]
component Product Labelling [0.78, 0.50]
component Supply Chain Transparency [0.72, 0.50]
component Farm Management [0.70, 0.50]
component Measurement and Grading [0.65, 0.50]
component Certification and Standards [0.60, 0.50]
component Regenerative Practice [0.58, 0.50]
component Extractive Practice [0.58, 0.50]
component National Agricultural Policy [0.52, 0.50]
component Crop Rotation [0.48, 0.50]
component Crop Diversity [0.48, 0.50]
component Monoculture [0.46, 0.50]
component Conservation Practice [0.42, 0.50]
component International Policy Framework [0.38, 0.50]
component Petrochemical Inputs [0.32, 0.50]
component Soil Health [0.28, 0.50]
component Soil Microbial Activity [0.18, 0.50]
component Photosynthesis [0.10, 0.50]

Consumer Access to Regenerative Food -> Consumer Purchasing Decision
Consumer Access to Regenerative Food -> Retail Distribution
Consumer Access to Regenerative Food -> Food Production
Consumer Purchasing Decision -> Product Labelling
Consumer Purchasing Decision -> Retail Distribution
Retail Distribution -> Supply Chain Transparency
Retail Distribution -> Food Production
Food Production -> Farm Management
Product Labelling -> Measurement and Grading
Product Labelling -> Certification and Standards
Supply Chain Transparency -> Measurement and Grading
Supply Chain Transparency -> Certification and Standards
Farm Management -> Regenerative Practice
Farm Management -> Extractive Practice
Farm Management -> National Agricultural Policy
Measurement and Grading -> Certification and Standards
Certification and Standards -> National Agricultural Policy
Certification and Standards -> Regenerative Practice
Regenerative Practice -> Crop Rotation
Regenerative Practice -> Crop Diversity
Regenerative Practice -> Conservation Practice
Regenerative Practice -> Soil Health
Extractive Practice -> Monoculture
Extractive Practice -> Petrochemical Inputs
National Agricultural Policy -> International Policy Framework
Crop Rotation -> Soil Health
Crop Diversity -> Soil Health
Conservation Practice -> Soil Health
Monoculture -> Soil Health
Monoculture -> Petrochemical Inputs
Soil Health -> Soil Microbial Activity
Soil Microbial Activity -> Photosynthesis

style wardley
```

> **Evolution placeholder note**: this is a value-chain-only skill. ε values above are NOT assessed — they are all set to a neutral placeholder of `0.50` solely to satisfy the `[visibility, evolution]` OWM coordinate shape. Run `$arckit-wardley` to assign real evolution positions.

<details>
<summary>Mermaid wardley-beta equivalent</summary>

```mermaid
wardley-beta
title Regenerative Agriculture Landscape (August 2022)
size [1100, 800]

anchor Consumer Access to Regenerative Food [0.95, 0.50]

component Consumer Purchasing Decision [0.90, 0.50]
component Retail Distribution [0.85, 0.50]
component Food Production [0.85, 0.50]
component Product Labelling [0.78, 0.50]
component Supply Chain Transparency [0.72, 0.50]
component Farm Management [0.70, 0.50]
component Measurement and Grading [0.65, 0.50]
component Certification and Standards [0.60, 0.50]
component Regenerative Practice [0.58, 0.50]
component Extractive Practice [0.58, 0.50]
component National Agricultural Policy [0.52, 0.50]
component Crop Rotation [0.48, 0.50]
component Crop Diversity [0.48, 0.50]
component Monoculture [0.46, 0.50]
component Conservation Practice [0.42, 0.50]
component International Policy Framework [0.38, 0.50]
component Petrochemical Inputs [0.32, 0.50]
component Soil Health [0.28, 0.50]
component Soil Microbial Activity [0.18, 0.50]
component Photosynthesis [0.10, 0.50]

Consumer Access to Regenerative Food -> Consumer Purchasing Decision
Consumer Access to Regenerative Food -> Retail Distribution
Consumer Access to Regenerative Food -> Food Production
Consumer Purchasing Decision -> Product Labelling
Consumer Purchasing Decision -> Retail Distribution
Retail Distribution -> Supply Chain Transparency
Retail Distribution -> Food Production
Food Production -> Farm Management
Product Labelling -> Measurement and Grading
Product Labelling -> Certification and Standards
Supply Chain Transparency -> Measurement and Grading
Supply Chain Transparency -> Certification and Standards
Farm Management -> Regenerative Practice
Farm Management -> Extractive Practice
Farm Management -> National Agricultural Policy
Measurement and Grading -> Certification and Standards
Certification and Standards -> National Agricultural Policy
Certification and Standards -> Regenerative Practice
Regenerative Practice -> Crop Rotation
Regenerative Practice -> Crop Diversity
Regenerative Practice -> Conservation Practice
Regenerative Practice -> Soil Health
Extractive Practice -> Monoculture
Extractive Practice -> Petrochemical Inputs
National Agricultural Policy -> International Policy Framework
Crop Rotation -> Soil Health
Crop Diversity -> Soil Health
Conservation Practice -> Soil Health
Monoculture -> Soil Health
Monoculture -> Petrochemical Inputs
Soil Health -> Soil Microbial Activity
Soil Microbial Activity -> Photosynthesis
```

</details>

## Component Inventory

| # | Component | Visibility | Tier | Description | Dependencies (down) |
|---|-----------|-----------:|------|-------------|---------------------|
| 0 | Consumer Access to Regenerative Food | 0.95 | Anchor | The user-side outcome: a purchase that reliably reflects regenerative provenance | Purchasing Decision, Retail Distribution, Food Production |
| 1 | Consumer Purchasing Decision | 0.90 | Demand | The act of choosing one product over another at shelf or checkout | Product Labelling, Retail Distribution |
| 2 | Retail Distribution | 0.85 | Demand | The channel that stocks, prices, and merchandises food | Supply Chain Transparency, Food Production |
| 3 | Food Production | 0.85 | Demand | The aggregate of farm outputs reaching market | Farm Management |
| 4 | Product Labelling | 0.78 | Experience | Claims visible at point of sale (organic, regen-verified, carbon-labelled) | Measurement and Grading, Certification and Standards |
| 5 | Supply Chain Transparency | 0.72 | Experience | Traceability of a product back to farm, field, and practice | Measurement and Grading, Certification and Standards |
| 6 | Farm Management | 0.70 | Experience | The farmer's decisions about what to grow and how | Regenerative Practice, Extractive Practice, National Agricultural Policy |
| 7 | Measurement and Grading | 0.65 | Evidence | Instruments and protocols that quantify farm-level outcomes (soil carbon, biodiversity, input volumes) | Certification and Standards |
| 8 | Certification and Standards | 0.60 | Evidence | Schemes that translate measurement into claims (organic, Regenerative Organic, Demeter, carbon standards) | National Agricultural Policy, Regenerative Practice |
| 9 | Regenerative Practice | 0.58 | Practice | The practice family: cover crops, low-till, diversified rotations, managed grazing, agroforestry | Crop Rotation, Crop Diversity, Conservation Practice, Soil Health |
| 10 | Extractive Practice | 0.58 | Practice | Industrial monoculture + chemical inputs + heavy tillage as the incumbent default | Monoculture, Petrochemical Inputs |
| 11 | National Agricultural Policy | 0.52 | Governance | Subsidies, cross-compliance, conservation payments, procurement rules | International Policy Framework |
| 12 | Crop Rotation | 0.48 | Practice detail | Ordered sequencing of crops to interrupt disease and restore nutrients | Soil Health |
| 13 | Crop Diversity | 0.48 | Practice detail | Mixed species, intercropping, polyculture, heritage varieties | Soil Health |
| 14 | Monoculture | 0.46 | Practice detail | Single-species, single-genotype, single-rotation cropping at scale | Soil Health, Petrochemical Inputs |
| 15 | Conservation Practice | 0.42 | Practice detail | Habitat margins, buffer strips, water management, tillage reduction | Soil Health |
| 16 | International Policy Framework | 0.38 | Governance | Treaties and frameworks (UNFCCC, CBD, Paris, FAO Koronivia, EU Farm-to-Fork) | (terminal governance) |
| 17 | Petrochemical Inputs | 0.32 | Substrate | Synthetic N fertiliser, pesticides, herbicides, fuel | (terminal industrial input) |
| 18 | Soil Health | 0.28 | Substrate | Aggregate structure, organic matter, water-holding capacity, nutrient cycling | Soil Microbial Activity |
| 19 | Soil Microbial Activity | 0.18 | Substrate | The bacterial, fungal, and faunal biomass that mediates the rhizosphere | Photosynthesis |
| 20 | Photosynthesis | 0.10 | Commodity floor | Primary productivity — the energy and carbon source underwriting the whole chain | (terminal commodity) |

## Dependency Matrix (direct `X`, indirect `I`)

Rows are parents; columns are children. Only the condensed view is shown; the OWM edge list is authoritative.

| Parent \ Child | Label | SupChain | FarmMgmt | M&G | Cert | Regen | Extract | NatPol | Rot | Div | Mono | Cons | IntlPol | Petro | Soil | Micro | Photo |
|----------------|:-----:|:--------:|:--------:|:---:|:----:|:-----:|:-------:|:------:|:---:|:---:|:----:|:----:|:-------:|:-----:|:----:|:-----:|:-----:|
| Anchor         | I     | I        | I        | I   | I    | I     | I       | I      | I   | I   | I    | I    | I       | I     | I    | I     | I     |
| Purchasing     | X     | I        | I        | I   | I    | I     | I       | I      | I   | I   | I    | I    | I       | I     | I    | I     | I     |
| Retail         | I     | X        | I        | I   | I    | I     | I       | I      | I   | I   | I    | I    | I       | I     | I    | I     | I     |
| FoodProd       |       |          | X        | I   | I    | I     | I       | I      | I   | I   | I    | I    | I       | I     | I    | I     | I     |
| Label          |       |          |          | X   | X    | I     | I       | I      | I   | I   | I    | I    | I       | I     | I    | I     | I     |
| SupChain       |       |          |          | X   | X    | I     | I       | I      | I   | I   | I    | I    | I       | I     | I    | I     | I     |
| FarmMgmt       |       |          |          | I   | I    | X     | X       | X      | I   | I   | I    | I    | I       | I     | I    | I     | I     |
| M&G            |       |          |          |     | X    | I     |         | I      |     |     |      |      | I       |       |      |       |       |
| Cert           |       |          |          |     |      | X     |         | X      | I   | I   |      | I    | I       |       | I    | I     | I     |
| Regen          |       |          |          |     |      |       |         |        | X   | X   |      | X    |         |       | X    | I     | I     |
| Extract        |       |          |          |     |      |       |         |        |     |     | X    |      |         | X     | I    | I     | I     |
| NatPol         |       |          |          |     |      |       |         |        |     |     |      |      | X       |       |      |       |       |
| Rot / Div / Cons |     |          |          |     |      |       |         |        |     |     |      |      |         |       | X    | I     | I     |
| Mono           |       |          |          |     |      |       |         |        |     |     |      |      |         | X     | X    | I     | I     |
| Soil           |       |          |          |     |      |       |         |        |     |     |      |      |         |       |      | X     | I     |
| Micro          |       |          |          |     |      |       |         |        |     |     |      |      |         |       |      |       | X     |

## Critical Path Analysis

**Longest chain (anchor → commodity floor)**:

```text
Consumer Access to Regenerative Food
  → Consumer Purchasing Decision
    → Product Labelling
      → Certification and Standards
        → Regenerative Practice
          → Conservation Practice  (or Crop Rotation / Diversity)
            → Soil Health
              → Soil Microbial Activity
                → Photosynthesis
```

Nine levels deep. This is the chain that determines whether a shelf label can be trusted back to biology.

**Bottlenecks and single points of failure**:

- **Measurement and Grading (0.65)** — labelling, supply-chain transparency, and certification all read from the same measurement layer. In August 2022 soil-carbon measurement is still largely model-based rather than directly measured, so the whole assurance stack rests on contested numerics. This is the structural bottleneck of the chain.
- **Certification and Standards (0.60)** — sits between measurement and both the consumer-facing claim and the policy instrument. A single scheme (e.g., Regenerative Organic Certified, launched 2020) carries disproportionate load because its competitors (organic, LEAF, Demeter, voluntary carbon schemes) each define "regenerative" differently.
- **Soil Health (0.28)** — terminal-tier ecological component that both practice families depend on, but which extractive practice structurally erodes while regenerative practice structurally builds. The chain's directionality problem lives here.
- **Petrochemical Inputs (0.32)** — terminal industrial input; a concentrated upstream (synthetic N is dominated by Haber-Bosch capacity tied to natural gas, which in August 2022 is in acute European crisis). Classical commodity fragility.

**Resilience gaps**:

- No redundancy between Certification and Measurement: a compromised or contested measurement method propagates through every certification scheme that leans on it, and therefore into every label on shelf.
- Supply Chain Transparency and Product Labelling are both consumer-facing assurance channels, but they share the same Measurement + Certification substrate, so they fail together rather than providing independent redundancy.
- International Policy Framework is a weak lever: it anchors National Policy but has no direct enforcement on Farm Management, so treaty commitments discount heavily on their way down the chain.

## Validation Checklist

**Completeness**

- [x] Chain starts with a genuine user need (consumer access to regeneratively-produced food), not a product or a specific certification scheme
- [x] All significant dependencies captured (31 edges)
- [x] Chain reaches commodity level (Photosynthesis as the biological commodity floor; Petrochemical Inputs as the industrial terminal)
- [x] No orphan components — every node has at least one edge
- [x] All components are activities, practices, or capabilities — not people or organisations. Actors named in the scenario (farmers, retailers, certification bodies, governments, UN) are represented by their activities (Farm Management, Retail Distribution, Certification and Standards, National Agricultural Policy, International Policy Framework)

**Accuracy**

- [x] Dependencies reflect real August-2022 relationships (Regenerative Organic Certified launched 2020; EU Farm-to-Fork active; UNFCCC Koronivia active; Ukraine-war nitrogen spike in force)
- [x] Visibility ordering consistent with dependency direction — parents ≥ children in every edge (checked manually)
- [x] No component is simultaneously user-facing and infrastructure

**Usefulness**

- [x] Granularity appropriate for strategic decisions (20 components + anchor; within the 8-20 guidance, at the upper end because the scenario spans consumer, supply chain, practice, policy, and substrate)
- [x] Each component can be meaningfully positioned on the evolution axis in a follow-up mapping pass
- [x] Chain reveals strategic insight — measurement as structural bottleneck; extractive practice locked in via petrochemical + monoculture substrate; biological substrate as unmetered commodity floor

## Visibility Assessment

| Component | ν | Reasoning |
|-----------|---:|-----------|
| Consumer Access to Regenerative Food | 0.95 | Anchor — by construction highest |
| Consumer Purchasing Decision | 0.90 | Directly performed by the anchor user |
| Retail Distribution | 0.85 | Immediate channel the consumer interacts with |
| Food Production | 0.85 | Visible in aggregate via availability and price |
| Product Labelling | 0.78 | Visible at point of sale; failure (misleading claim) is immediately consequential |
| Supply Chain Transparency | 0.72 | Visible via QR codes, brand websites, retailer disclosure; one step off shelf |
| Farm Management | 0.70 | Visible via farm-to-fork stories but mostly abstracted from the consumer |
| Measurement and Grading | 0.65 | Hidden from consumers but directly observed by retailers, auditors, policy |
| Certification and Standards | 0.60 | Visible as a logo on-shelf (0.78 channel) but the standard itself is operational (0.60) |
| Regenerative Practice | 0.58 | Named in marketing and policy debate; the practice itself is operational |
| Extractive Practice | 0.58 | The incumbent default; rarely named but structurally visible via price and yield |
| National Agricultural Policy | 0.52 | Affects farmers directly; consumers only experience it indirectly |
| Crop Rotation | 0.48 | Farm-level decision, invisible to consumers |
| Crop Diversity | 0.48 | Farm-level decision, invisible to consumers |
| Monoculture | 0.46 | Farm-level pattern, invisible to consumers but structurally dominant |
| Conservation Practice | 0.42 | Field-margin / off-crop activity, invisible to consumers |
| International Policy Framework | 0.38 | Treaty layer; visible to specialists, invisible to consumers and most farmers |
| Petrochemical Inputs | 0.32 | Upstream industrial supply; invisible to consumers, visible to farmers via price |
| Soil Health | 0.28 | Ecological substrate; measurable but rarely measured |
| Soil Microbial Activity | 0.18 | Deep biology; invisible to nearly all actors |
| Photosynthesis | 0.10 | Terminal commodity — the underwriter of the whole chain |

## Assumptions and Open Questions

**Assumptions made**

- The anchor was set at the **consumer**, not the farmer or the policymaker. The scenario explicitly asks for the picture "that connects farming to consumer behaviour" and the "supply-chain awareness picture", so consumer access is the cleanest anchor. A farmer-anchored chain would have Farm Management at the top and would re-tier nearly everything.
- **Regenerative Practice** and **Extractive Practice** are represented as two sibling components at the same visibility (0.58). In reality they are rival practice families rather than a single spectrum, and placing them as siblings exposes the competition between them. A more granular map would split each into its doctrinal forms.
- **Monoculture** is treated as a dependency of Extractive Practice, but it also historically leaks into nominally "sustainable" chains (e.g., organic monoculture). The edge captures the dominant, not the universal, case.
- **Soil Health, Soil Microbial Activity, Photosynthesis** are included as substrate components even though they are biological rather than built. The mapping rationale is that they are the terminal commons that every upstream practice either invests in or depletes — they function as the commodity floor of agriculture.
- August-2022 framing: the EU Farm-to-Fork strategy is active (May 2020 Communication); Regenerative Organic Certified has been shipping labels since 2020; the UNFCCC Koronivia Joint Work on Agriculture is in its final decision-making year; Russia's invasion of Ukraine has spiked nitrogen-fertiliser prices, which sharpens the Petrochemical Inputs dependency.

**Open questions**

1. Should **Carbon Market / Credits** appear as a distinct component alongside Certification and Standards? In August 2022 voluntary soil-carbon markets are emerging but immature, and the governance is split between ISO, Verra, Gold Standard, and a dozen scheme-specific protocols. The current map folds this into Certification and Standards.
2. Should **Farmer Knowledge Transfer** (extension services, farmer-to-farmer networks, agronomists) appear as a distinct component? The scenario asks "what's still knowledge-based" — knowledge infrastructure is arguably a peer to Measurement and Grading, but is currently folded into Farm Management.
3. Should **Water** appear as a distinct substrate component alongside Soil Health? Conservation Practice touches water implicitly, but in many regenerative frameings water (and watershed stewardship) is elevated to a first-class component.
4. Should **Seed and Genetics** appear between Crop Diversity and Soil Health? Seed sovereignty and heritage varieties are a significant differentiator in regenerative practice and a classical consolidation story in extractive practice.

---

**Differentiating vs. commoditising — summary for the scenario prompt**

- **Still knowledge-based (differentiating)** in August 2022: Regenerative Practice, Crop Rotation / Diversity, Conservation Practice, Measurement and Grading, Certification and Standards. These are where the chain is genuinely undefined and where strategic moves have leverage.
- **Industrial practice locked in (commoditised)**: Extractive Practice, Monoculture, Petrochemical Inputs. These sit on deeply concentrated upstream supply (synthetic N, global grain genetics, global logistics) and are commoditised in the negative sense — difficult to dislodge because they are cheap and universal.
- **Supply-chain awareness picture**: weak. Supply Chain Transparency (0.72) is consumer-facing, but its evidence layer (Measurement 0.65, Certification 0.60) is still custom-built and contested. That gap is the reason consumer-side claims outpace on-farm verification.
- **Fragile points**: Measurement and Grading as a shared dependency of Labelling, Transparency, and Certification; Petrochemical Inputs in a year of acute European gas-price crisis; Soil Microbial Activity as a largely unmetered but foundational layer.

---

**Generated by**: ArcKit `$arckit-wardley.value-chain` command
**Generated on**: 2026-04-23 11:33 GMT
**ArcKit Version**: (external skill; benchmark harness)
**Project**: Regenerative Agriculture Landscape benchmark (competitor-compare/arckit-value-chain/eval-agriculture-regen)
**AI Model**: claude-opus-4-7 (1M context)
**Generation Context**: Free-form scenario input (August 2022 regenerative farming landscape); no REQ/STKE/PRIN artifacts supplied — warnings above. No external documents available. Value-chain-only skill — evolution positions NOT assessed.
