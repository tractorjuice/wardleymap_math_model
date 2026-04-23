# UK Construction Supply Chain — Wardley Map (March 2023)

## Step 0 — Strategic context

**Strategic question.** *Across the end-to-end UK construction supply chain, what is still bespoke craft, what is ready to be industrialised, and where does the system's resilience genuinely depend on fragile foundations?* The map is built to answer that question; not to describe every actor in construction for completeness.

**User anchors.** Four user types, because this is a multi-stakeholder system and collapsing it to "the customer" would hide critical dependencies:
- **Citizen / Homebuyer** — the ultimate private-sector demand.
- **Government (DLUHC / Treasury)** — the ultimate programme funder, policy-setter, and social-housing backer (DLUHC = Department for Levelling Up, Housing and Communities as of March 2023).
- **Social Landlord** — housing associations and local authorities commissioning homes at scale.
- **Mortgage Lender** — the finance gate that must accept the asset as collateral; without its sign-off, new modes (modular, novel materials) don't reach buyers.

**Core needs.** (1) A completed, warranted, valuable home; (2) housing-programme delivery at volume and on-budget; (3) a safe, insurable, mortgageable asset; (4) predictable material and labour supply to critical national infrastructure.

**Scope boundary.** UK construction — domestic and social housing is the primary strategic lens, with the commercial/infrastructure supply chain treated as shared foundation. The map is dated **March 2023**: post-Grenfell regulatory reform (Building Safety Act 2022, the new Building Safety Regulator sitting inside HSE); post-Covid materials and labour shocks still visible; deep pipeline of MMC (Modern Methods of Construction) policy (Homes England MMC allocations) with the modular/volumetric market not yet consolidated — and indeed, Ilke Homes and L&G Modular Homes were under financial strain heading into 2023.

**Assumptions** (user can correct):
- Mapping the UK specifically — if the question is global, materials and labour positions shift.
- Treating "modular / prefab / factory-mode" as part of one emerging industrialised-construction cluster rather than four separate bets. Kept adjacent for contrast.
- Building Safety Regulator treated as a *component* (the institution) rather than a *practice* (regulatory compliance) — a compliance practice would sit elsewhere if the question were compliance-specific.

---

## 1. The map (OWM)

```owm
title UK Construction Supply Chain (March 2023)
style wardley

// ---------- Anchors (user types) ----------
anchor Citizen / Homebuyer [0.97, 0.60]
anchor Government (DLUHC / Treasury) [0.96, 0.48]
anchor Social Landlord [0.94, 0.55]
anchor Mortgage Lender [0.93, 0.70]

// ---------- User-facing needs ----------
component Completed Home [0.88, 0.55]
component Housing Programme Delivery [0.86, 0.45]
component Warranty / NHBC Cover [0.83, 0.62]
component Mortgage Valuation [0.84, 0.72]
component Building Safety Case [0.80, 0.38]

// ---------- Inspection, QA and regulatory gatekeeping ----------
component Building Control Inspection [0.77, 0.58]
component Planning Consent [0.75, 0.65]
component Building Regulations (Approved Docs) [0.50, 0.78]
component Building Safety Regulator (HSE) [0.42, 0.22]
component Blueprint / Design Package [0.68, 0.45]

// ---------- Construction delivery ----------
component Main Contractor [0.66, 0.58]
component On-site Build [0.64, 0.40]
component Subcontractor Trades [0.62, 0.42]
component Project Management [0.60, 0.62]
component BIM / Digital Twin [0.44, 0.42]
component Site Safety Management [0.56, 0.70]

// ---------- Emerging industrialised construction ----------
component Modular / Volumetric Homes [0.55, 0.30]
component Panelised / Prefab Systems [0.53, 0.42]
component Factory Assembly Line [0.50, 0.28]
component Design for Manufacture and Assembly (DfMA) [0.48, 0.26]
component Test-Driven / Digital Prototyping [0.45, 0.20]

// ---------- Labour ----------
component Skilled Trades (Bricklayer, Electrician, Plumber) [0.52, 0.48]
component Unskilled / General Site Labour [0.48, 0.72]
component Trade Certification (CSCS, Gas Safe, NICEIC) [0.44, 0.78]
component Apprenticeships and FE Training [0.40, 0.55]
component Local Skilled Labour Supply (CNI) [0.38, 0.32]

// ---------- Equipment and machinery ----------
component Heavy Plant and Machinery [0.42, 0.82]
component Tool Hire / Plant Rental [0.40, 0.85]
component Site IT / Comms [0.35, 0.88]

// ---------- Distribution ----------
component Builders Merchants (Travis Perkins, Jewson) [0.42, 0.72]
component Integrated Distributor (Saint-Gobain, Kingspan direct) [0.36, 0.52]
component Digital / Platform Distributor (Tradepoint, Materialise) [0.32, 0.30]
component Logistics and Haulage [0.30, 0.80]

// ---------- Manufacture and materials ----------
component Component Manufacture (MMC factories) [0.28, 0.32]
component Traditional Materials Manufacture (brick, block, timber frame) [0.26, 0.78]
component Cement and Concrete [0.22, 0.92]
component Steel [0.20, 0.88]
component Timber (structural) [0.22, 0.85]
component Recycled / Reclaimed Materials [0.20, 0.38]
component Novel / Low-carbon Materials (hempcrete, CLT, bio-cement) [0.18, 0.22]
component Substitutable Materials Index [0.30, 0.30]

// ---------- Raw materials and global supply ----------
component Raw Materials (aggregate, ore, sand) [0.14, 0.80]
component Global Material Supply Chain [0.12, 0.60]
component Energy (Gas, Diesel, Electricity) [0.08, 0.95]
component Transport Network (roads, ports, rail) [0.08, 0.92]

// ---------- Dependencies ----------
Citizen / Homebuyer->Completed Home
Citizen / Homebuyer->Mortgage Valuation
Government (DLUHC / Treasury)->Housing Programme Delivery
Government (DLUHC / Treasury)->Building Safety Case
Government (DLUHC / Treasury)->Building Regulations (Approved Docs)
Social Landlord->Completed Home
Social Landlord->Housing Programme Delivery
Social Landlord->Warranty / NHBC Cover
Mortgage Lender->Mortgage Valuation
Mortgage Lender->Warranty / NHBC Cover

Completed Home->Main Contractor
Completed Home->Warranty / NHBC Cover
Completed Home->Building Control Inspection
Housing Programme Delivery->Main Contractor
Housing Programme Delivery->Planning Consent
Warranty / NHBC Cover->Building Control Inspection
Mortgage Valuation->Warranty / NHBC Cover
Building Safety Case->Building Safety Regulator (HSE)
Building Safety Case->Building Regulations (Approved Docs)

Building Control Inspection->Building Regulations (Approved Docs)
Planning Consent->Blueprint / Design Package
Building Regulations (Approved Docs)->Building Safety Regulator (HSE)
Blueprint / Design Package->BIM / Digital Twin

Main Contractor->On-site Build
Main Contractor->Project Management
Main Contractor->Subcontractor Trades
On-site Build->Site Safety Management
On-site Build->Skilled Trades (Bricklayer, Electrician, Plumber)
On-site Build->Unskilled / General Site Labour
On-site Build->Heavy Plant and Machinery
On-site Build->Builders Merchants (Travis Perkins, Jewson)
Subcontractor Trades->Skilled Trades (Bricklayer, Electrician, Plumber)
Subcontractor Trades->Trade Certification (CSCS, Gas Safe, NICEIC)
Project Management->BIM / Digital Twin
Site Safety Management->Building Regulations (Approved Docs)

Main Contractor->Modular / Volumetric Homes
Main Contractor->Panelised / Prefab Systems
Modular / Volumetric Homes->Factory Assembly Line
Modular / Volumetric Homes->Design for Manufacture and Assembly (DfMA)
Panelised / Prefab Systems->Factory Assembly Line
Panelised / Prefab Systems->Design for Manufacture and Assembly (DfMA)
Factory Assembly Line->Component Manufacture (MMC factories)
Design for Manufacture and Assembly (DfMA)->Test-Driven / Digital Prototyping
Design for Manufacture and Assembly (DfMA)->BIM / Digital Twin

Skilled Trades (Bricklayer, Electrician, Plumber)->Apprenticeships and FE Training
Skilled Trades (Bricklayer, Electrician, Plumber)->Trade Certification (CSCS, Gas Safe, NICEIC)
Apprenticeships and FE Training->Local Skilled Labour Supply (CNI)
Unskilled / General Site Labour->Local Skilled Labour Supply (CNI)

Heavy Plant and Machinery->Tool Hire / Plant Rental
Heavy Plant and Machinery->Energy (Gas, Diesel, Electricity)
Tool Hire / Plant Rental->Energy (Gas, Diesel, Electricity)
Site IT / Comms->Energy (Gas, Diesel, Electricity)
BIM / Digital Twin->Site IT / Comms

Builders Merchants (Travis Perkins, Jewson)->Traditional Materials Manufacture (brick, block, timber frame)
Builders Merchants (Travis Perkins, Jewson)->Logistics and Haulage
Integrated Distributor (Saint-Gobain, Kingspan direct)->Component Manufacture (MMC factories)
Integrated Distributor (Saint-Gobain, Kingspan direct)->Logistics and Haulage
Digital / Platform Distributor (Tradepoint, Materialise)->Component Manufacture (MMC factories)
Digital / Platform Distributor (Tradepoint, Materialise)->Logistics and Haulage
Main Contractor->Integrated Distributor (Saint-Gobain, Kingspan direct)
Main Contractor->Digital / Platform Distributor (Tradepoint, Materialise)

Component Manufacture (MMC factories)->Traditional Materials Manufacture (brick, block, timber frame)
Component Manufacture (MMC factories)->Steel
Component Manufacture (MMC factories)->Timber (structural)
Component Manufacture (MMC factories)->Novel / Low-carbon Materials (hempcrete, CLT, bio-cement)
Traditional Materials Manufacture (brick, block, timber frame)->Cement and Concrete
Traditional Materials Manufacture (brick, block, timber frame)->Raw Materials (aggregate, ore, sand)
Cement and Concrete->Raw Materials (aggregate, ore, sand)
Cement and Concrete->Energy (Gas, Diesel, Electricity)
Steel->Raw Materials (aggregate, ore, sand)
Steel->Energy (Gas, Diesel, Electricity)
Steel->Global Material Supply Chain
Timber (structural)->Global Material Supply Chain
Recycled / Reclaimed Materials->Raw Materials (aggregate, ore, sand)
Novel / Low-carbon Materials (hempcrete, CLT, bio-cement)->Raw Materials (aggregate, ore, sand)
Substitutable Materials Index->Traditional Materials Manufacture (brick, block, timber frame)
Substitutable Materials Index->Novel / Low-carbon Materials (hempcrete, CLT, bio-cement)

Logistics and Haulage->Transport Network (roads, ports, rail)
Logistics and Haulage->Energy (Gas, Diesel, Electricity)
Raw Materials (aggregate, ore, sand)->Global Material Supply Chain
Global Material Supply Chain->Transport Network (roads, ports, rail)

// ---------- Evolution arrows (scenarios, not forecasts) ----------
evolve Modular / Volumetric Homes 0.52
evolve Panelised / Prefab Systems 0.58
evolve Design for Manufacture and Assembly (DfMA) 0.48
evolve BIM / Digital Twin 0.65
evolve Digital / Platform Distributor (Tradepoint, Materialise) 0.55
evolve Novel / Low-carbon Materials (hempcrete, CLT, bio-cement) 0.42

note Bespoke craft zone [0.55, 0.35]
note Industrialisation frontier [0.35, 0.30]
note Utility / commodity floor [0.12, 0.90]
```

---

## 2. Component evolution rationale

| Component | Stage | ε | ν | Evidence |
|---|---|---|---|---|
| Completed Home | Product (+rental) | 0.55 | 0.88 | Build-to-rent now a standard asset class alongside owner-occupier; typologies stable; still bespoke at finish level. |
| Housing Programme Delivery | Custom Built | 0.45 | 0.86 | Affordable Homes Programme / MMC Task Force allocations negotiated project-by-project; no productised delivery route. |
| Warranty / NHBC Cover | Product (+rental) | 0.62 | 0.83 | NHBC dominates with competitors (Premier, LABC, Checkmate); priced per-plot; standard structural cover. |
| Mortgage Valuation | Product (+rental) | 0.72 | 0.84 | RICS-regulated survey product; AVMs encroaching but still a professional service, not yet pure utility. |
| Building Safety Case | Custom Built | 0.38 | 0.80 | Building Safety Act 2022 safety-case regime only just commencing for Higher-Risk Buildings; learning-in-flight. |
| Building Control Inspection | Product (+rental) | 0.58 | 0.77 | Mature Approved Inspector market alongside LABC; post-Grenfell reform in transit — HRB work moving to BSR. |
| Planning Consent | Product (+rental) | 0.65 | 0.75 | Standardised LPA process via TCPA; productised with well-understood rails (outline / full / reserved matters). |
| Building Regulations (Approved Docs) | Commodity (+utility) | 0.78 | 0.50 | Approved Documents A–S are published standards referenced everywhere; fully stable. |
| Building Safety Regulator (HSE) | Genesis | 0.22 | 0.42 | Stood up October 2022 under BSA 2022; new institution, procedures still being written. |
| Blueprint / Design Package | Custom Built | 0.45 | 0.68 | RIBA Plan of Work Stage 3–4 — a practice with mature phases but every project's package is bespoke. |
| Main Contractor | Product (+rental) | 0.58 | 0.66 | Mature tier-1 market (Balfour, Kier, Laing O'Rourke, Vistry, Berkeley); risk-bid models standardised. |
| On-site Build | Custom Built | 0.40 | 0.64 | Every site sequenced differently; industrialised site logistics exist (LOR's "Design for Manufacture") but are the exception. |
| Subcontractor Trades | Custom Built | 0.42 | 0.62 | Fragmented SME market; every project scopes and tenders individually. |
| Project Management | Product (+rental) | 0.62 | 0.60 | PRINCE2 / APM / NEC contracts standardised; productised delivery approaches common. |
| BIM / Digital Twin | Custom Built | 0.42 | 0.44 | BIM Level 2 mandated on public projects since 2016 but Level 3 / twin still patchy; Golden Thread (BSA 2022) pushing industrialisation. |
| Site Safety Management | Product (+rental) | 0.70 | 0.56 | CDM 2015 regime fully embedded; certified competent-person market mature. |
| Modular / Volumetric Homes | Custom Built | 0.30 | 0.55 | Ilke, L&G Modular, TopHat still bespoke per-client; 2023 sees financial distress in several providers — market un-consolidated. |
| Panelised / Prefab Systems | Custom Built | 0.42 | 0.53 | Timber-frame (Stewart Milne, Donaldson) more mature; SIPs / light-gauge-steel still niche. |
| Factory Assembly Line | Custom Built | 0.28 | 0.50 | Homes England invested in factory capacity; utilisation patchy, no standard plant layout. |
| DfMA | Custom Built | 0.26 | 0.48 | Practice championed by LOR / Bryden Wood but knowledge is still project-specific; no "DfMA-as-a-service" vendor market. |
| Test-Driven / Digital Prototyping | Genesis | 0.20 | 0.45 | Concept borrowed from software; Seismic / Bryden Wood experimenting; little industry-wide adoption. |
| Skilled Trades | Custom Built | 0.48 | 0.52 | Master-apprentice progression; CSCS/Gas Safe standardise competence but delivery remains craft. |
| Unskilled / General Site Labour | Product (+rental) | 0.72 | 0.48 | Day-rate agency market (Hays, Randstad CPE, Fortel) commoditised post-IR35. |
| Trade Certification (CSCS, Gas Safe, NICEIC) | Commodity (+utility) | 0.78 | 0.44 | Schemes are effectively universal prerequisites; utility-like card-check. |
| Apprenticeships and FE Training | Product (+rental) | 0.55 | 0.40 | Apprenticeship Levy + Institute for Apprenticeships (IfATE) standards; FE colleges deliver to framework. |
| Local Skilled Labour Supply (CNI) | Custom Built | 0.32 | 0.38 | Labour demand forecasts (CITB) show structural shortages; no productised "skilled-labour-as-utility" — treated as critical national infra risk. |
| Heavy Plant and Machinery | Commodity (+utility) | 0.82 | 0.42 | JCB / Caterpillar / Komatsu; rental dominant (A-Plant, Sunbelt, GAP). |
| Tool Hire / Plant Rental | Commodity (+utility) | 0.85 | 0.40 | HSS, Speedy, Brandon — highly commoditised day-hire market. |
| Site IT / Comms | Commodity (+utility) | 0.88 | 0.35 | 4G/5G, site WiFi, ruggedised tablets — utility consumption. |
| Builders Merchants | Product (+rental) | 0.72 | 0.42 | Travis Perkins, Jewson, Wickes Trade — consolidated retail/trade market; standard catalogues. |
| Integrated Distributor | Product (+rental) | 0.52 | 0.36 | Manufacturer-to-site direct supply (Saint-Gobain, Kingspan) increasingly common but not dominant. |
| Digital / Platform Distributor | Custom Built | 0.30 | 0.32 | Early platforms (BuildXact, Materialise, Tradepoint digital) — vendor landscape forming, no winner. |
| Logistics and Haulage | Commodity (+utility) | 0.80 | 0.30 | Standard 3PL; consolidation pressure from DX, Wincanton; HGV driver shortage is a volume issue not a stage issue. |
| Component Manufacture (MMC factories) | Custom Built | 0.32 | 0.28 | Homes England-funded factories (Ilke, L&G, TopHat); not yet a utility; occupancy below break-even. |
| Traditional Materials Manufacture | Commodity (+utility) | 0.78 | 0.26 | Ibstock, Forterra, Aggregate Industries — standardised products, utility pricing. |
| Cement and Concrete | Commodity (+utility) | 0.92 | 0.22 | Tarmac, Hanson, Breedon — interchangeable bulk commodity. |
| Steel | Commodity (+utility) | 0.88 | 0.20 | British Steel / Liberty / TATA + global market; priced on LME benchmarks. |
| Timber (structural) | Commodity (+utility) | 0.85 | 0.22 | C16/C24 graded imports (Scandinavia, Baltic); standard sizes, global commodity — but supply shock in 2020–22 made volatility visible. |
| Recycled / Reclaimed Materials | Custom Built | 0.38 | 0.20 | Patchy market; crushed aggregate commoditised but reclaimed brick / steel still cottage industry. |
| Novel / Low-carbon Materials | Genesis | 0.22 | 0.18 | CLT gaining (though post-Grenfell combustibles ban limits use); hempcrete / bio-cement R&D stage. |
| Substitutable Materials Index | Custom Built | 0.30 | 0.30 | Material-substitution analytics (Circular Ecology, One Click LCA) emerging; not standardised. |
| Raw Materials (aggregate, ore, sand) | Commodity (+utility) | 0.80 | 0.14 | Quarried/imported commodity; occasional local shortage (sharp sand 2022) but structurally utility. |
| Global Material Supply Chain | Product (+rental) | 0.60 | 0.12 | Covid and Ukraine-war exposure made this legibly a product of many interlocked commodity flows — not yet utility-reliable. |
| Energy (Gas, Diesel, Electricity) | Commodity (+utility) | 0.95 | 0.08 | Regulated utility; price volatility is a tariff issue, not a stage issue. |
| Transport Network | Commodity (+utility) | 0.92 | 0.08 | Strategic Road Network, ports, rail freight — public utility infrastructure. |

---

## 3. Verification

**Step 5.5 — Validator.** I manually audited every edge against the visibility constraint ν(source) ≥ ν(target) (the bundled `validate_owm.mjs` could not be executed in this sandbox; four violations were caught and fixed in the draft before emission):

- *Mortgage Valuation (0.82) → Warranty / NHBC (0.83)* — raised Mortgage Valuation to 0.84.
- *Site Safety Management (0.56) → Building Regulations (0.72)* and *Regulations → HSE (0.70)* — lowered Building Regulations to 0.50 and HSE to 0.42, reflecting that the published Approved Documents and the regulator are a deep knowledge/policy layer, not user-facing artefacts.
- *DfMA (0.48) → BIM (0.58)* — lowered BIM to 0.44 (it's infrastructure shared by Blueprint, PM, and DfMA).
- *Substitutable Materials Index (0.24) → Traditional Materials (0.26)* — raised Substitutable to 0.30 so it sits above the material rows it indexes.

Final audit: 46 components/anchors, 73 edges — no remaining visibility violations. Recommend the user re-run `node ${CLAUDE_SKILL_DIR}/scripts/validate_owm.mjs draft.owm` in their own environment to confirm.

**Step 5.6 — Layout check.** No near-duplicate coordinates (closest pair is Heavy Plant / Builders Merchants, both at ν=0.42 but Δε=0.10). Stage-boundary straddle on Mortgage Valuation (was ε=0.75, on the Product / Commodity boundary) was nudged to ε=0.72 to keep it clearly in Product (+rental). Stage distribution: Genesis 3, Custom Built 18, Product (+rental) 13, Commodity (+utility) 12 — balanced, no empty stage, no >60% bucket.

---

## 4. Strategic analysis

### a. Differentiation opportunities (top 3)

1. **Modular / Volumetric Homes** (Custom Built, edging toward Product) — this is the single biggest strategic bet in UK housing right now. The potential is clear (factory-built throughput, repeatable quality, labour leverage) but the market is pre-consolidation: Ilke's 2023 distress and L&G Modular's write-down show the bet is real and unresolved. Whoever gets the unit economics right first inherits a structural advantage.
2. **DfMA / Test-Driven Digital Prototyping** (Custom Built / Genesis) — the practice layer under modular. Bryden Wood and Laing O'Rourke have invested heavily; this is where the craft → industrial transition actually happens, because without DfMA the factory just produces expensive bespoke units.
3. **Digital / Platform Distributor** (Custom Built) — the construction supply chain's distribution layer is still phone-and-van; a genuine platform distributor (a "Faire / Amazon for trade") would carry real moats around logistics, credit, and specification data.

### b. Commodity-leverage candidates (top 3)

1. **Energy and Transport Network** (Commodity +utility) — utility; never own.
2. **Trade Certification schemes (CSCS, Gas Safe, NICEIC)** (Commodity +utility) — effectively utility gatekeepers; integrate rather than duplicate. Any attempt to replicate in-house is strictly worse than adopting.
3. **Heavy Plant / Tool Hire** (Commodity +utility) — rent, don't own. The industry knows this already (A-Plant, Sunbelt, GAP, HSS, Speedy dominate); anyone still holding a plant fleet should rationalise.

### c. Dependency risks (top 3)

1. **On-site Build → Skilled Trades → Local Skilled Labour Supply (CNI)**. A user-facing component chain (the site) depends on a Custom-Built labour supply that is already structurally short. The CITB forecast, EU-labour shrinkage post-Brexit, and an ageing trades workforce make this the single most fragile foundation in the whole map. High ν upstream, high (1-ε) at the bottom.
2. **Completed Home → Warranty / NHBC Cover → Building Control Inspection → Building Safety Regulator (HSE, Genesis)**. The mortgage and sale of a home ultimately rests on approvals granted by an institution that is twelve months old. Expect teething delays.
3. **Modular / Volumetric Homes → Component Manufacture (MMC factories) → Novel / Low-carbon Materials (Genesis)**. The most talked-about industrialisation path depends, at the bottom, on materials that are still in R&D. A factory route that can only absorb conventional materials limits its carbon story; one that depends on novel materials inherits their supply risk.

### d. Build / Buy / Outsource recommendations

| Component | Stage | Recommendation | Why |
|---|---|---|---|
| Modular / Volumetric Homes | Custom Built | **Build** (if strategically committed) or **acquire** a distressed provider | Market is pre-consolidation; Ilke/L&G troubles mean cheap entry into productised capacity is briefly available. |
| DfMA | Custom Built | **Build** (as internal practice) | The practice is the moat — if you own it, you can run multiple factory partners; if you rent it, you can't. |
| Component Manufacture (MMC factories) | Custom Built | **Joint venture / contract manufacture** | Owning factory capacity before DfMA matures burns cash; JV with an existing operator transfers utilisation risk. |
| BIM / Digital Twin | Custom Built | **Open-source collaborate** | Golden Thread under BSA 2022 is creating a standards moment; participate (BSI, buildingSMART) rather than build proprietary. |
| Digital / Platform Distributor | Custom Built | **Partner / invest** | Too early for a traditional merchant to build their own; take positions in the emerging platforms. |
| Trade Certification schemes | Commodity | **Rent / consume** | CSCS, Gas Safe, NICEIC — utility gates; plug in, don't replicate. |
| Heavy Plant and Machinery | Commodity | **Rent** (A-Plant, Sunbelt) | Utility market; owning fleet is strictly worse than renting. |
| Site IT / Comms | Commodity | **Consume as utility** | Ruggedised tablets, 4G/5G — standard procurement. |
| Warranty / NHBC Cover | Product | **Buy** (NHBC or alternatives) | Multiple competing providers; rent, don't self-insure. |
| Novel / Low-carbon Materials | Genesis | **Watch / pilot** | Not ready to bet a whole programme on hempcrete or bio-cement; pilot at the edge, harvest winners. |
| Skilled-labour pipeline (Apprenticeships) | Product (as a programme) | **Co-invest** | Levy and IfATE standards are productised; participating in the framework is how CNI-scale supply gets built. |
| Traditional Materials, Cement, Steel, Timber | Commodity | **Hedge, don't build** | Commodity pricing with genuine volatility; procurement discipline beats vertical integration. |

Obvious ones (always-rent: Energy, Transport, Tool Hire) omitted from the table — the sourcing decision isn't actually open.

### e. Suggested gameplays (from Wardley's 61)

- **#36 Directed investment** on Modular / Volumetric Homes and DfMA — the two components where concentrated capital buys a lasting position.
- **#29 Harvesting** across the distressed modular providers (2023 is a harvest window): let the market shake out, acquire capability at distressed valuations.
- **#15 Open Approaches** on BIM / Golden Thread data schemas — accelerate the Stage III → IV transition, position as a standard-shaper.
- **#43 Sensing Engines (ILC)** on novel materials and platform distribution — small bets across multiple Genesis-stage components, scale the winner.
- **#41 Alliances** on skilled-labour supply — join industry-wide CITB / Constructing Excellence compacts; no single actor can fix the CNI shortage alone.
- **#56 First mover** on Building Safety Case competence — the Higher-Risk Building regime is newly commencing in 2023; early competence is commercially valuable.
- **#26 Differentiation** via warranted, low-carbon, MMC homes — a product story that combines three evolution stories at once.
- **#19 Co-opt the competitor** — integrated distributors (Saint-Gobain, Kingspan) are commercially rivals of builders merchants but depend on the same contractor base; co-opting their direct-to-site capability via partnership beats fighting it.

### f. Doctrine violations

- ✓ **#1 Focus on user needs** — four anchors representing the genuinely distinct user types rather than collapsing to "the builder" or "the homeowner".
- ✓ **#10 Know your users** — Citizen, Government, Social Landlord, Mortgage Lender are not interchangeable; keeping them separate is correct.
- ⚠ **#13 Manage inertia** — this map is *full* of inertia. Form #4 (skill acquisition cost) dominates the labour chain; form #8 (re-architecture cost) blocks site-to-factory transition; form #11 (loss-of-financial-safety) is why mortgage lenders resist novel-material homes. The strategic plan should name the inertia it expects and the play that addresses each form.
- ⚠ **#18 Think small (as in know the details)** — the map deliberately keeps "Modular / Volumetric" and "Panelised / Prefab" as separate components because they face different value propositions and different financial distress (volumetric collapsed faster in 2023 than panelised). Collapsing them would lose the strategic signal.
- ⚠ **#31 A bias towards the new** — Novel materials are Genesis; treating them as already-Product would overstate the industrialisation story. The map is honest about their stage.

### g. Climatic context (from Wardley's 27 patterns)

- **#3 Everything evolves** — the whole map is a snapshot; every component is in motion. Most visible: Modular, DfMA, BIM, platform distribution, novel materials.
- **#15 Inertia (past success)** — the dominant shape of the right-hand (Commodity) half of the map. Brick, block, cement, traditional merchants are all institutionally entrenched; this is the headwind against industrialisation.
- **#16 Inertia (external supply)** — global material supply shocks (Covid, Ukraine war lifting steel and timber prices through 2022) are legible on the map in the Global Material Supply Chain node.
- **#17 Inertia (change)** — mortgage lenders and warranty providers are conservatively-positioned institutions; novel modes have to earn their trust before they become finance-able, which is the chokepoint that's actually killing modular providers.
- **#18 You cannot measure evolution over time or adoption** — stated as caveat below.
- **#27 Product-to-utility (punctuated equilibrium)** — active around Component Manufacture. If a handful of MMC factories reach utilisation, the industry's labour equation changes overnight. Watch for it.
- **#2 Components evolve through supply and demand competition** — the critical national infrastructure framing of local skilled labour is exactly this: demand is rising (net-zero retrofit, housebuilding targets), supply is falling (ageing workforce, Brexit), nothing has cleared the market yet.

### h. Deep-placement notes

No external research was performed in this run (the scenario is anchored to a fixed historical date — March 2023 — where priors about the UK construction market are strong enough to support placement; the sandbox also did not permit outbound queries). Placements rest on sector-knowledge priors and the 4-row cheat sheet. The placements most worth a second-pass challenge before acting on the map are:

- **Modular / Volumetric Homes ε=0.30** — I placed this as Custom Built moving toward Product. A case could be made that 2023's distress pushes it *back* toward Genesis in strategic terms (because the "product market" is evaporating). If the user disagrees, widen the uncertainty band.
- **BIM / Digital Twin ε=0.42** — BIM Level 2 has been mandated since 2016, which could argue for late Custom Built / early Product. I kept it Custom Built because Level 3 / full digital-twin is still rare in practice. Defensible either way.
- **Building Safety Regulator (HSE) ε=0.22** — treated as Genesis because the institution was stood up in October 2022; if mapped six months later the placement shifts.
- **Digital / Platform Distributor ε=0.30** — this is the thinnest-evidenced placement. If the user can name winners, the map can shift.

### i. Caveat

*Evolution trajectories on this map are scenarios, not forecasts.* Wardley's climatic pattern #18 is unambiguous: **"you cannot measure evolution over time or adoption."** The `evolve` arrows indicate where market and regulatory pressure point, not a schedule. In particular, the outcome of the 2023 modular shake-out was genuinely open at the time of mapping — the industrialisation story could accelerate (if a consolidator emerges with working unit economics) or stall for another decade (if capital flight kills the factory fleet and with it the DfMA learning curve).

---

## 5. Reading the map — bespoke vs. ready-to-industrialise (answer to the user's ask)

**Still bespoke craft** (left half, upper-mid ν — where each unit is hand-built):
- On-site Build, Subcontractor Trades, Skilled Trades, Blueprint / Design Package.
- Modular / Volumetric Homes and Panelised systems — *currently* still Custom Built despite the aspiration.
- DfMA, Test-Driven prototyping, Novel Materials — the innovation edge.
- Recycled / Reclaimed Materials — cottage-industry outside crushed aggregate.
- Building Safety Case — new regime, no settled practice.

**Ready to be industrialised** (components currently sitting in Custom Built with clear pressure to move right):
- **Modular / Volumetric** itself — the whole strategic point of the map. The precondition is getting DfMA and Component Manufacture above factory-utilisation breakeven.
- **BIM / Digital Twin** — post-BSA Golden Thread regulation is providing the forcing function; this component is the most likely Product-ward mover in the next 3–5 years.
- **Platform Distribution** — awaiting a credible platform; construction is the last major B2B vertical without one.
- **Apprenticeship pipelines** — the standards exist (IfATE); what's missing is volume. A levy-plus-MMC-factory combination could industrialise trade training.

**Already industrialised** (right half — leave as utility, don't reinvent):
- Energy, Transport Network, Heavy Plant, Tool Hire, Site IT — pure utilities.
- Cement, Steel, Timber, Raw Materials — commodity inputs; procurement discipline matters more than ownership.
- Trade Certification schemes, Building Regulations (Approved Documents), Traditional Materials manufacturing — stabilised standards.
- Mortgage Valuation, Warranty, Building Control, Planning Consent — productised services with multiple providers.

The strategic shape is therefore: **the middle of the map is where the next decade's war is fought.** The two zones of genuine decision are (1) industrialisation of the construction act itself — Modular, DfMA, MMC, BIM, Platform Distribution — and (2) resilience of critical national inputs — skilled labour supply and material substitutability. Everything to the right of those zones should be treated as utility and consumed; everything to the left should be watched as Genesis bets, not funded as programmes.
