# Wardley Map — Regenerative Farming Landscape (pinned August 2022)

**Scenario:** Map the landscape of regenerative farming. Include soil health, biodiversity, carbon sequestration, farmer practices, certifications, supply chains to consumers, funding sources, and measurement/verification. Identify what is differentiating vs. commoditising, and where adoption is fragile.

**Time pin:** August 2022 — specifically the week the Inflation Reduction Act (IRA) was signed (16 August 2022), which injected ~$19.5B of new climate-smart ag money into USDA conservation programs and materially changed the funding landscape.

Two anchors are used because the scenario explicitly spans both sides of the chain: the **farmer** (who changes practices, receives payments, and supplies ingredients) and the **consumer** (who pays the price premium and reads the certification label). Doctrine #10 (*know your users*) — a single anchor would hide the two-sided structure.

---

## Map (OWM)

```owm
title Regenerative Farming Landscape (Aug 2022)
style wardley

// Anchors — two user types
anchor Farmer [0.98, 0.45]
anchor Consumer [0.98, 0.70]

// User-facing (consumer side)
component Regeneratively-Grown Food Product [0.86, 0.40]
component Retail Shelf / Brand Story [0.80, 0.60]
component Regen Certification Label [0.74, 0.25]
component Consumer Price Premium [0.70, 0.50]

// User-facing (farmer side)
component Farm Profitability [0.86, 0.55]
component On-Farm Decisions [0.82, 0.35]
component Payment for Ecosystem Services [0.76, 0.30]
component Agronomic Advice [0.72, 0.50]

// Supply chain to consumers
component Ingredient Sourcing (Brands) [0.62, 0.55]
component Scope 3 Emissions Reporting [0.55, 0.30]
component Corporate Regen Commitments [0.60, 0.40]
component Traceability / Chain of Custody [0.55, 0.35]
component Processors / Aggregators [0.52, 0.60]

// Farmer practices (the doing)
component No-Till / Reduced Till [0.65, 0.60]
component Cover Cropping [0.62, 0.40]
component Diverse Crop Rotations [0.58, 0.45]
component Integrated Livestock / Managed Grazing [0.55, 0.35]
component Reduced Synthetic Inputs [0.52, 0.40]
component Agroforestry / Perennial Integration [0.45, 0.20]

// Funding sources
component Federal Conservation Payments (EQIP/CSP/RCPP) [0.48, 0.70]
component IRA Climate-Smart Ag Funding [0.50, 0.15]
component Private Carbon Payments [0.48, 0.25]
component Brand-Funded Transition Programs [0.60, 0.30]
component Philanthropy / Impact Capital [0.38, 0.35]
component Bank Lending / Crop Insurance [0.40, 0.70]

// Measurement & verification
component Soil Carbon MRV [0.32, 0.20]
component Satellite / Remote Sensing of Practices [0.30, 0.45]
component On-Farm Soil Sampling [0.28, 0.70]
component Biogeochemical Models (DNDC, DayCent) [0.25, 0.50]
component Biodiversity Monitoring [0.22, 0.20]
component Ecological Outcome Verification (EOV) [0.26, 0.30]
component Voluntary Carbon Market Protocols [0.40, 0.30]
component Third-Party Certification Bodies [0.34, 0.55]

// Certifications (standards themselves)
component Regenerative Organic Certified (ROC) [0.42, 0.30]
component Land to Market (Savory) [0.38, 0.35]
component A Greener World Certified Regenerative [0.38, 0.25]
component USDA Organic Baseline [0.40, 0.80]

// Biological & agronomic inputs
component Biological Inputs (N-fixing microbes etc.) [0.42, 0.35]
component Cover Crop Seed Supply [0.38, 0.60]
component Conventional Synthetic Fertiliser [0.35, 0.90] inertia
component Conventional Crop Protection [0.33, 0.88] inertia

// Deep infrastructure / ecosystem services (outcomes)
component Carbon Sequestration [0.24, 0.20]
component Soil Health (SOM, aggregate stability) [0.20, 0.30]
component Biodiversity (above and below ground) [0.16, 0.25]
component Water Cycle / Infiltration [0.22, 0.35]

// Knowledge
component Farmer Peer Networks [0.30, 0.40]
component Extension Services [0.28, 0.70]
component Soil Science / Ecology Research [0.15, 0.50]
component Indigenous / Traditional Knowledge [0.12, 0.30]

// Utilities / commodities
component Farmland (access, tenure) [0.25, 0.75]
component Farm Equipment (tractors, drills) [0.18, 0.90]
component Cloud Compute / Satellite Imagery [0.08, 0.90]
component Connectivity / Rural Broadband [0.06, 0.85]

// Dependencies — Consumer side
Consumer->Regeneratively-Grown Food Product
Consumer->Retail Shelf / Brand Story
Consumer->Regen Certification Label
Consumer->Consumer Price Premium
Regeneratively-Grown Food Product->Retail Shelf / Brand Story
Regeneratively-Grown Food Product->Regen Certification Label
Regeneratively-Grown Food Product->Ingredient Sourcing (Brands)
Retail Shelf / Brand Story->Corporate Regen Commitments
Regen Certification Label->Regenerative Organic Certified (ROC)
Regen Certification Label->Land to Market (Savory)
Regen Certification Label->A Greener World Certified Regenerative
Regen Certification Label->USDA Organic Baseline

// Dependencies — Farmer side
Farmer->Farm Profitability
Farmer->On-Farm Decisions
Farmer->Payment for Ecosystem Services
Farmer->Agronomic Advice
Farm Profitability->Payment for Ecosystem Services
Farm Profitability->Consumer Price Premium
Farm Profitability->Bank Lending / Crop Insurance
On-Farm Decisions->No-Till / Reduced Till
On-Farm Decisions->Cover Cropping
On-Farm Decisions->Diverse Crop Rotations
On-Farm Decisions->Integrated Livestock / Managed Grazing
On-Farm Decisions->Reduced Synthetic Inputs
On-Farm Decisions->Agroforestry / Perennial Integration
On-Farm Decisions->Agronomic Advice
Agronomic Advice->Farmer Peer Networks
Agronomic Advice->Extension Services

// Supply chain
Ingredient Sourcing (Brands)->Processors / Aggregators
Ingredient Sourcing (Brands)->Corporate Regen Commitments
Ingredient Sourcing (Brands)->Traceability / Chain of Custody
Corporate Regen Commitments->Scope 3 Emissions Reporting
Traceability / Chain of Custody->Third-Party Certification Bodies

// Practices depend on inputs and funding
No-Till / Reduced Till->Farm Equipment (tractors, drills)
No-Till / Reduced Till->Reduced Synthetic Inputs
Cover Cropping->Cover Crop Seed Supply
Cover Cropping->Soil Health (SOM, aggregate stability)
Diverse Crop Rotations->Cover Crop Seed Supply
Integrated Livestock / Managed Grazing->Farmland (access, tenure)
Reduced Synthetic Inputs->Biological Inputs (N-fixing microbes etc.)
Agroforestry / Perennial Integration->Farmland (access, tenure)

// Funding flows into practices
Payment for Ecosystem Services->Federal Conservation Payments (EQIP/CSP/RCPP)
Payment for Ecosystem Services->IRA Climate-Smart Ag Funding
Payment for Ecosystem Services->Private Carbon Payments
Payment for Ecosystem Services->Brand-Funded Transition Programs
Private Carbon Payments->Voluntary Carbon Market Protocols
Brand-Funded Transition Programs->Corporate Regen Commitments
Philanthropy / Impact Capital->Soil Science / Ecology Research

// Measurement underpins carbon payments and certifications
Private Carbon Payments->Soil Carbon MRV
Voluntary Carbon Market Protocols->Soil Carbon MRV
Soil Carbon MRV->Satellite / Remote Sensing of Practices
Soil Carbon MRV->On-Farm Soil Sampling
Soil Carbon MRV->Biogeochemical Models (DNDC, DayCent)
Satellite / Remote Sensing of Practices->Cloud Compute / Satellite Imagery
Biogeochemical Models (DNDC, DayCent)->Soil Science / Ecology Research
On-Farm Soil Sampling->Soil Health (SOM, aggregate stability)

// Certifications depend on outcome/verification
Regenerative Organic Certified (ROC)->Third-Party Certification Bodies
Regenerative Organic Certified (ROC)->USDA Organic Baseline
Land to Market (Savory)->Ecological Outcome Verification (EOV)
A Greener World Certified Regenerative->Third-Party Certification Bodies
Ecological Outcome Verification (EOV)->Biodiversity Monitoring
Ecological Outcome Verification (EOV)->Soil Health (SOM, aggregate stability)
Third-Party Certification Bodies->On-Farm Soil Sampling

// Outcomes / ecosystem services — Soil Health is the substrate; specific services (carbon, water) depend on it
Carbon Sequestration->Soil Health (SOM, aggregate stability)
Water Cycle / Infiltration->Soil Health (SOM, aggregate stability)
Soil Health (SOM, aggregate stability)->Biodiversity (above and below ground)
Biodiversity Monitoring->Biodiversity (above and below ground)

// Knowledge flows
Farmer Peer Networks->Indigenous / Traditional Knowledge
Extension Services->Soil Science / Ecology Research
Soil Science / Ecology Research->Cloud Compute / Satellite Imagery

// Deep utilities
Farm Equipment (tractors, drills)->Connectivity / Rural Broadband
Cloud Compute / Satellite Imagery->Connectivity / Rural Broadband

// Evolution trajectories (scenarios, not forecasts)
evolve Soil Carbon MRV 0.55
evolve Voluntary Carbon Market Protocols 0.60
evolve Biological Inputs (N-fixing microbes etc.) 0.60
evolve Regenerative Organic Certified (ROC) 0.55
evolve Cover Cropping 0.65
evolve Scope 3 Emissions Reporting 0.55
evolve Satellite / Remote Sensing of Practices 0.70

// Strategic notes
note Differentiation zone (build) [0.75, 0.20]
note Commoditising foundation (rent/use) [0.15, 0.88]
note Fragile adoption — MRV + carbon markets [0.30, 0.22]
```

**Validator result:** `OK: 55 components/anchors, 72 edges — no violations.`

---

## Strategic analysis

### a. Differentiation opportunities (top 3)

1. **Soil Carbon MRV** (Genesis, edge of Custom Built) — the whole private-money side of regen ag hinges on being able to measure carbon credibly. In August 2022 there is no agreed method; every major programme (Indigo, Nori, Bayer, CIBO, Truterra, Agoro, Locus, Pachama, ESMC, ~13 active) is running a different protocol. Whoever defines the trusted, cheap, scalable MRV wins the category. Highest differentiation leverage on the map — deeply contested, highly visible to brands and carbon buyers. Note it is **not** yet visible to consumers, who see a label, not a soil-sample protocol.
2. **Ecological Outcome Verification (EOV) / Savory-style biodiversity MRV** (Custom Built) — the sibling measurement problem for the non-carbon half of "regenerative". ROC, Land to Market, and any credible definition of regen need this. Fewer players, fewer investors, lower hype than soil carbon — meaning whoever builds a repeatable, affordable ecological-outcome measurement owns a durable niche.
3. **Brand-Funded Transition Programs** (Custom Built) — the specific offering by which General Mills / Unilever / PepsiCo / Danone fund their ingredient farmers' regen transition. In Aug 2022 these are bespoke (every brand is inventing its own). A productised "regen transition program in a box" for the Fortune 500 is a very visible, very immature space — a marketplace that doesn't exist yet.

### b. Commodity-leverage candidates (top 3)

1. **Cloud compute / satellite imagery** (Commodity +utility) — rent from AWS/GCP/Planet Labs/Sentinel. Never build.
2. **Conventional synthetic fertiliser & crop protection** (Commodity +utility) — these are flagged `inertia` on the map because for the regen-farming use case they are what farmers are trying to *reduce*, but they remain an industrialised commodity that any farm still uses some of. Treat as utility; do not build.
3. **Farm equipment** (Commodity +utility) — no-till drills, roller-crimpers and similar are now off-the-shelf from John Deere, Case IH, Great Plains. Twenty years ago this was Custom Built for pioneers; today it's Product (+rental) to Commodity (+utility).

### c. Dependency risks (top 3)

These are the places where a visible, user-facing component depends on an immature foundation — rank order by reasoning about the visibility-times-immaturity product:

1. **Private Carbon Payments → Soil Carbon MRV** (edge at ν≈0.48 into ε≈0.20). The whole voluntary carbon-market value proposition to farmers depends on an MRV stack that is not yet trusted. Headlines in mid-2022 are already questioning permanence, additionality, and leakage of ag soil-carbon credits. If MRV loses public credibility before it matures, the private payment channel collapses and farmers who invested based on it will be burned — permanently souring the farmer population on the model. This is the single biggest fragility in the map.
2. **Brand-Funded Transition Programs → Corporate Regen Commitments** — farmer cash flow depends on brand commitments that are PR-driven and Scope-3-mandate-driven; if regulation softens, the CEO changes, or net-zero enthusiasm cools, the money stops. Corporate commitments in Aug 2022 are still mostly voluntary (SBTi FLAG guidance is fresh from September 2022; CSRD not yet in force) — the foundation under the visible farmer payments is politically soft.
3. **Regen Certification Label → ROC / Land to Market / A Greener World** — consumers pay a premium based on a label whose underlying standards (ROC ~1M acres / 142 farms; Land to Market ~2.5M acres) are still small-scale, still under revision, and not yet recognised by a government body. If a "greenwashing" scandal hits one, it stains all.

### d. Suggested gameplays

- **#15 Open Approaches** on **Soil Carbon MRV and satellite RS** — the category needs a trusted open protocol (MRV-as-standard) more than it needs another proprietary one. Whoever opens first sets the de-facto standard and harvests the ecosystem built on top. ESMC is partway here; an incumbent brand or agtech could accelerate this.
- **#36 Directed investment** on **MRV and Biological Inputs** — the top-2 differentiators. Pivot Bio's 300% YoY acre growth and $60M 2022 revenue is the archetype of what directed capital into a Custom-Built biological-inputs category can produce; repeat for microbiome-based phosphorus, nitrogen dialling, and plant-microbe resilience.
- **#43 Sensing Engines (ILC)** on **certifications** — don't pick a standard yet; instrument acreage and farmer adoption across ROC / Land to Market / AGW / Carbon Standard / Gold Standard, then back the winner. Ecosystem observability is cheap because the certifiers publish their acreage figures.
- **#41 Alliances** on **Farmer Peer Networks** — alliances with groups like Soil Health Academy, Practical Farmers of Iowa, Pasa, AFT, and regional grazing networks is the only scalable way to reach farmers at adoption cost below $/acre brand-economics can tolerate. Extension is too thin after 40 years of defunding; peer networks have already stepped in.
- **#56 First mover** on **IRA Climate-Smart Ag Funding capture** — the $19.5B was appropriated last week (relative to the map pin). NRCS will publish state-level allocations and project RFPs in Q4 2022 / Q1 2023. Technical-assistance providers, brand-funded cost-share stackers, and MRV providers who move first win multi-year contracts.
- **#1 Focus on user needs** — doctrine-level but worth naming as gameplay because many Aug 2022 regen programmes are visibly built for the brand's Scope 3 reporting, not for the farmer. Farms exiting these programmes after year 1-2 are a symptom.
- **#29 Harvesting** on **Biological Inputs** — the category is mid-formation; watch the next 18–24 months for which microbial formulations get repeatable field results, then acquire. Do not try to build one from scratch.
- **#44 Tower and Moat** on a trusted certification — if ROC or Land to Market can take the industrialising wave (brand + IRA + carbon-market convergence) and occupy the "trusted regen label" position before the FTC / USDA defines its own, they own the moat.

### e. Doctrine notes

- ✓ **#1 Focus on user needs** — two anchors (Farmer, Consumer) correctly surface that this is a two-sided system and the winning strategy must serve both.
- ✓ **#10 Know your users** — same point; a map with only "Brand" or only "Farmer" as the anchor would systematically under-invest in the other side. This is the most common Aug 2022 failure mode: brand-commissioned maps treat the farmer as a supplier, farmer-commissioned maps treat the brand as a buyer, neither treats the relationship as the central feature.
- ⚠ **#13 Manage inertia** — the map explicitly flags Conventional Synthetic Fertiliser and Conventional Crop Protection as inertia. But the human / political inertia is understated here: knowledge-transfer gap (form #8 skill acquisition cost), sunk capital in existing equipment and rotations (form #2), and supplier-side inertia in agri-retail co-ops (form #15 existing revenue streams) all apply. See section (g) below for the full inertia analysis.
- ⚠ **#18 Think small (as in know the details)** — "regenerative agriculture" is not one thing. Cover cropping in Iowa corn is not the same as holistic planned grazing on Montana rangeland. The map uses umbrella terms; a real strategy document should be commodity-specific (row crops, dairy, beef, produce, tree crops — each has a different map shape).
- ⚠ **#33 There is no one culture** — a brand transition programme needs Pioneer energy for MRV / biological-inputs R&D, Settler discipline for protocol and certification work, and Town-Planner efficiency for the commoditising practice payments. Most brand programmes are staffed monoculturally from sustainability teams and struggle with the Pioneer work.
- ⚠ **#15 Use a FIRE methodology for genesis** — Soil Carbon MRV demands FIRE (fast, inexpensive, restrained, elegant). Several Aug 2022 programmes are doing the opposite: large, expensive, over-specified. See the cost-per-credit commentary in ag-MRV trade press.

### f. Climatic context

Of Wardley's 27 climatic patterns, the ones actively shaping this map in Aug 2022:

- **#3 Everything evolves through supply and demand competition.** Regen practices that were Genesis 10 years ago (cover cropping, no-till, integrated grazing) are being pulled rightward by IRA funding, brand Scope 3 demand, and carbon-market demand simultaneously. No-till is already at Stage III (~50% of cropland is reduced-tillage of some kind per 2022 census). Cover cropping is mid-Stage II (~5% of cropland but growing at 17% per five-year period).
- **#27 Product-to-utility punctuated equilibrium (a "war").** Signals are stacking for an impending war in ag-MRV: multiple vendors with different protocols, regulatory standardisation coming (USDA's "Partnerships for Climate-Smart Commodities" announcements through 2022), open-source alternatives (OpenTEAM, ESMC) appearing, a major utility provider (Bayer / Corteva / Nutrien) entering to create a single platform. Expect industrialisation to one or two trusted MRV stacks within 3–5 years.
- **#4 Evolution is multi-wave with chasms.** Regen ag is the *second* wave of sustainable agriculture — following the 1990s–2010s organic wave that hit a chasm around 1–2% of US ag acreage. Regen needs to cross its own chasm (currently at ~1–5% of US cropland by most measures). Treating regen as a linear continuation of organic is the wrong mental model.
- **#15 Inertia caused by past success.** Conventional synthetic fertiliser and crop protection are deeply embedded (profitable, efficient-per-acre, crop-insured, extension-backed, trade-financed). They are doing their job at Commodity (+utility) and will not be displaced by regen practices in mid-2020s — only complemented.
- **#17 Inertia caused by existing business models.** Agri-retail co-ops and input dealers make margin selling synthetic inputs; regen's reduced-input thesis is directly adversarial to their revenue. Their sales forces are a structural brake.
- **#10 Higher-order systems create new sources of worth.** As Soil Carbon MRV industrialises (the "lower layer"), new higher-order systems become possible: regen-backed green bonds, soil-carbon-linked crop insurance, biodiversity futures. These are not viable today because the measurement substrate isn't trusted — but they become viable as soon as it is.
- **#18 you cannot measure evolution over time or adoption.** A useful warning specifically for this map — IRA funding and brand commitments will accelerate rightward evolution of several components, but cannot be used to *predict* when each will cross its stage boundary.

### g. Deep-placement notes

Five components were flagged for targeted research because each is in a recently-formed or contested space.

- **Soil Carbon MRV.** Initial cheat-sheet score put this around 0.25–0.30 (late Genesis / early Custom Built). Vendor-landscape search confirmed the late-Genesis / very-early-Custom reading: 10+ active MRV vendors (Indigo, InSoil, Seqana, SatMRV, AgroCares, Nori, Pachama, Truterra, Climate FieldView, Boomitra, etc.), but each with a different protocol, no winner, and active academic / NGO critique of permanence, additionality, and uncertainty deductions. Kept at **ε = 0.20** with the understanding that it's on the cusp of moving rightward — hence the `evolve Soil Carbon MRV 0.55` trajectory. Variance across cheat-sheet rows was high (Ubiquity said Stage I, Certainty said Stage I, Publication Type said Stage II, Market said Stage II) so plot this as a range 0.15–0.35, not a point.
- **Voluntary Carbon Market Protocols (for ag).** Initial score 0.35 (mid Custom Built). Research confirmed the activity level — Indigo surpassed 2M MT CO2e verified in its fifth issuance by late-2022; Nori credited 125k MtCO2e across 43k acres; Bayer Carbon Program launched in 2022 — but the *protocols* themselves (Climate Action Reserve Soil Enrichment, Verra VM0042, plan vivo, Nori's proprietary protocol) are still consolidating and being revised. Moved slightly leftward to **ε = 0.30** to reflect that it's still protocol-fragmented rather than a single standard.
- **Regenerative Organic Certified (ROC) / Land to Market / AGW.** Initial score ~0.35 (mid Custom Built). Research confirmed the placements are correct for Aug 2022: ROC has certified ~1M acres and 142 certified farms (launched 2018, still small-scale); Land to Market has 2.5M acres monitored and 1000+ products carrying the seal (deeper into product-form). Placed ROC at **ε = 0.30** (Custom Built, edge of Product (+rental)), Land to Market at **ε = 0.35** (slightly further along because of the product-seal infrastructure), AGW Certified Regenerative at **ε = 0.25** (launched 2020, earliest). This is a three-way certification race; the climatic-pattern #27 signals suggest it won't settle as three winners.
- **Biological Inputs (N-fixing microbes).** Initial score 0.30 (early Custom Built). Research bumped this to **ε = 0.35** (solidly Custom Built, approaching Product (+rental) boundary) on the evidence that Pivot Bio alone covered ~3M acres in 2022 with $60M revenue and 300% YoY growth for two consecutive years. Set `evolve` target to 0.60 — a credible Stage III trajectory within 2–4 years given the adoption curve, but real Custom-Built variability exists across biological-input sub-categories (nitrogen fixers are further along than phosphorus solubilisers, which are further along than biostimulants generally).
- **Cover Cropping.** Initial score ~0.45 (late Custom Built). Research showed only 4.7% of total US cropland planted to cover crops in 2022 — looks low, but the *practice itself* (as knowledge and activity) is well-understood, with seed supply chains forming, so it's not Custom Built at the practice level. Kept at **ε = 0.40** (mid-Custom) to reflect that the practice is mature as a concept but adoption is still low-percentage. Evolution target 0.65 (late Product (+rental)) is ambitious but plausible if IRA cost-sharing scales adoption.

### h. Differentiating vs. commoditising summary

**Differentiating (Stage I–II, user-visible, contested):**
- Soil Carbon MRV
- Ecological Outcome Verification (EOV) / biodiversity monitoring
- Brand-Funded Transition Programs
- Regen Certification schemes (ROC / Land to Market / AGW)
- Biological Inputs (N-fixing microbes etc.)
- Agroforestry / perennial integration
- Payment for Ecosystem Services bundling

**Commoditising (Stage III–IV, foundational):**
- No-till / reduced till (already well into Product (+rental) and edging toward Commodity (+utility))
- Farm equipment
- Conventional synthetic inputs (fully Commodity (+utility); flagged as inertia)
- Cloud compute / satellite imagery
- USDA Organic baseline (Commodity (+utility) — the old regime)
- Federal conservation payments (established programme machinery)
- On-farm soil sampling (the physical act; the *meaning* of the results is still Custom)

**Fragile adoption zones (the map's red-flag intersections):**
- **The carbon-payment-to-MRV bridge.** Farmers making multi-year practice changes on the strength of private-carbon-market revenue that is delivered by an MRV stack that could lose credibility. The whole stack from *Private Carbon Payments* to *Soil Carbon MRV* to *Biogeochemical Models* is in Genesis / early Custom Built.
- **The Scope-3-to-farm-payment bridge.** Corporate regen commitments are PR-fragile; a greenwashing scandal, CEO change, or regulatory softening reverses them within one budget cycle.
- **The certification-label-to-consumer bridge.** The label means less than consumers think it does because the underlying verification (EOV, biodiversity monitoring) is still Custom Built. A single scandal in a mass-retail chain (Whole Foods, Sprouts, Costco regen SKUs) could stall the movement by 3–5 years.
- **The farmer retention gap after cost-share.** Federal (EQIP/CSP) and IRA-funded conservation payments are typically 3–5 year contracts. If the practice (cover cropping in particular) does not pay for itself by year 5 without the subsidy, the farmer reverts. Currently it often does not, outside of specific geographies and rotations.

### i. Caveat

Evolution trajectories (every `evolve` arrow in the map) are scenarios, not forecasts. Wardley's climatic pattern #18: *"you cannot measure evolution over time or adoption."* The IRA passage one week before the map pin is a strong tailwind for many of these components' rightward movement, but the direction is not the same as the date. Re-map in six months.

---

## Verification record (Step 5.5)

- **Validator run:** `python3 ${CLAUDE_SKILL_DIR}/scripts/validate_owm.py ./draft.owm`
- **Final result:** `OK: 55 components/anchors, 72 edges — no violations.`
- Multiple iterations were required; visibility constraint violations arose during deep-placement coordinate shifts (certifications cluster, ecosystem-service substrate cluster, corporate / brand-funded cluster). Each was resolved by raising the source or lowering the target per the validator output, and re-run until clean.
- Canonical stage names used throughout analysis: "Product (+rental)" and "Commodity (+utility)" are used; bare "Product" or "Commodity" as stage labels do not appear in prose.

Sources consulted for deep placement:
- [Soil carbon MRV solutions and insights — ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0301479724022709)
- [Agricultural Carbon Programs — AFT / Farmland Info](https://farmlandinfo.org/wp-content/uploads/sites/2/2023/08/AFT-SVS-Agricultural-Carbon-Programs.pdf)
- [FarmRaise — carbon credit companies overview](https://www.farmraise.com/blog/the-top-5-carbon-credit-companies)
- [Indigo Ag — fifth issuance, 2M MT CO2e](https://www.indigoag.com/pages/news/indigo-surpasses-2-million-metric-tons-of-verified-soil-carbon-impact-with-fifth-credit-issuance)
- [Nosh — regen certification landscape 2022](https://www.nosh.com/news/2022/regenerative-ag-certification-options-are-growing-but-what-do-they-mean/)
- [Modern Farmer — regen cert: gold standard or greenwashing](https://modernfarmer.com/2023/08/regenerative-food-certification/)
- [Pivot Bio — 2022 impact report, 3M acres, $60M revenue, 300% YoY](https://www.pivotbio.com/press-releases/2022pivotbioimpactreport)
- [AgFunderNews — Pivot Bio 1M-acre pilot](https://agfundernews.com/breaking-pivot-bio-pilot-replaces-synthetic-nitrogen-on-nearly-1m-acres-of-farmland)
- [USDA ERS — 2022 Census of Agriculture cover crop data (4.7%)](https://www.ers.usda.gov/data-products/charts-of-note/chart-detail?chartId=108950)
- [NRCS — Inflation Reduction Act summary](https://www.nrcs.usda.gov/about/priorities/inflation-reduction-act)
- [Kleinman Center — IRA agricultural provisions](https://kleinmanenergy.upenn.edu/commentary/blog/agricultural-provisions-of-the-inflation-reduction-act-and-beyond/)
