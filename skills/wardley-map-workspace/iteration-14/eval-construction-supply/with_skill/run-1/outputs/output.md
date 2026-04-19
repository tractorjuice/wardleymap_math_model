# Wardley Map — Modern Construction Supply Chain (Commercial Building, March 2023)

## Scenario

Map the modern construction supply chain for commercial building projects: material sourcing, specification, procurement, logistics, on-site coordination, subcontractors, compliance (building codes, safety), digital tools (BIM, procurement platforms), and stakeholder relationships (client, architect, contractor, suppliers). Diagnose what is differentiating vs. commoditising and where the chain is fragile.

The map is drawn as of **March 2023** — post-pandemic supply-chain stress, steel/concrete price shocks still fresh, Procore at scale, BIM Level 2 mandated in UK public-sector projects and normalised in US commercial practice, low-carbon concrete/mass-timber still emerging, OSHA/HSE rules settled, and ESG disclosure standards in industrialising flux.

---

## 1. Anchors and scope

Three user anchors are required — this is a genuinely multi-stakeholder chain and a single anchor would hide the real tensions.

| Anchor | Need |
|---|---|
| **Client (Developer/Owner)** | A building delivered on time, on budget, to spec, with defects covered. |
| **Architect** | Design intent executed faithfully; specs honoured; fees protected. |
| **General Contractor** | Build the project profitably, on the schedule, within the contract envelope. |

Subcontractors, suppliers, inspectors, and regulators are *actors* in the chain, not user anchors — their activities appear as components the three anchors depend on.

---

## 2. OWM map

```owm
title Modern Construction Supply Chain (Commercial, March 2023)
style wardley

// Anchors — three user types this chain must serve
anchor Client (Developer/Owner) [0.99, 0.55]
anchor Architect [0.95, 0.48]
anchor General Contractor [0.93, 0.60]

// Client-facing outcomes
component Completed Building Handover [0.88, 0.50]
component Project Schedule & Milestones [0.84, 0.55]
component Cost & Budget Certainty [0.82, 0.58]
component Quality & Defects Liability [0.80, 0.45]

// Design & specification layer
component Design Intent / Drawings [0.76, 0.45]
component Specifications (CSI/NBS) [0.68, 0.62]
component Value Engineering [0.70, 0.38]
component BIM Model (Federated) [0.44, 0.50]

// Procurement & commercial
component Tendering / Bid Management [0.64, 0.55]
component Subcontractor Packages [0.62, 0.52]
component Procurement Platform (e.g. Procore, Autodesk Build) [0.58, 0.55]
component Purchase Orders & Contracts [0.50, 0.70]
component Change Orders / Variations [0.54, 0.40]

// On-site coordination
component Site Management / Superintendent [0.66, 0.35]
component Daily Coordination Meetings [0.60, 0.50]
component Trade Sequencing (Look-ahead) [0.58, 0.42]
component Site Safety Management [0.55, 0.55]
component Quality Inspections [0.60, 0.50]

// Subcontractor trades
component MEP Subcontractors [0.50, 0.55]
component Structural/Concrete Subcontractors [0.48, 0.70]
component Envelope/Facade Subcontractors [0.46, 0.50]
component Finishing Trades [0.45, 0.65]

// Logistics & materials flow
component Just-in-Time Site Delivery [0.44, 0.42]
component Material Laydown / Staging [0.42, 0.60]
component Freight & Haulage [0.38, 0.78]
component Customs & Cross-border Logistics [0.30, 0.68]

// Material sourcing (upstream)
component Long-lead Item Management [0.40, 0.38]
component Material Sourcing (Steel, Concrete, Glass) [0.34, 0.75]
component Specialty Materials (Low-carbon, Engineered) [0.32, 0.30]
component Supplier/Fabricator Relationships [0.28, 0.45]
component Commodity Materials (Aggregates, Rebar, Timber) [0.22, 0.88]

// Compliance layer
component Building Code Compliance [0.56, 0.70]
component Planning/Permit Approvals [0.44, 0.65]
component Fire & Life-Safety Certification [0.42, 0.60]
component Health & Safety Regulation (OSHA/HSE) [0.40, 0.80]
component ESG & Embodied-Carbon Reporting [0.70, 0.25]
component Insurance & Bonding [0.32, 0.75]

// Digital stack & data
component Common Data Environment (CDE) [0.35, 0.50]
component Clash Detection (Navisworks/Solibri) [0.40, 0.62]
component Scheduling Software (P6/MSP) [0.55, 0.78]
component Project Reporting Dashboards [0.60, 0.55]
component Digital Twin / Sensor Feeds [0.42, 0.22]
component Cloud SaaS & Identity [0.14, 0.90]
component Connectivity (Site Networking) [0.10, 0.88]

// Knowledge base
component Construction Law & Standard Contracts (JCT/AIA/FIDIC) [0.18, 0.82]
component Trade Labour Pool [0.20, 0.55]

// Dependencies
Client (Developer/Owner)->Completed Building Handover
Client (Developer/Owner)->Cost & Budget Certainty
Client (Developer/Owner)->Project Schedule & Milestones
Client (Developer/Owner)->Quality & Defects Liability
Architect->Design Intent / Drawings
Architect->Specifications (CSI/NBS)
Architect->BIM Model (Federated)
General Contractor->Project Schedule & Milestones
General Contractor->Site Management / Superintendent
General Contractor->Tendering / Bid Management
General Contractor->Subcontractor Packages

Completed Building Handover->Quality & Defects Liability
Completed Building Handover->Fire & Life-Safety Certification
Completed Building Handover->Building Code Compliance
Project Schedule & Milestones->Trade Sequencing (Look-ahead)
Project Schedule & Milestones->Scheduling Software (P6/MSP)
Cost & Budget Certainty->Value Engineering
Cost & Budget Certainty->Change Orders / Variations
Cost & Budget Certainty->Purchase Orders & Contracts
Quality & Defects Liability->Quality Inspections

Design Intent / Drawings->BIM Model (Federated)
Design Intent / Drawings->Specifications (CSI/NBS)
Specifications (CSI/NBS)->Material Sourcing (Steel, Concrete, Glass)
Specifications (CSI/NBS)->Specialty Materials (Low-carbon, Engineered)
Value Engineering->Specifications (CSI/NBS)
Value Engineering->BIM Model (Federated)
BIM Model (Federated)->Common Data Environment (CDE)
BIM Model (Federated)->Clash Detection (Navisworks/Solibri)

Tendering / Bid Management->Subcontractor Packages
Tendering / Bid Management->Procurement Platform (e.g. Procore, Autodesk Build)
Subcontractor Packages->MEP Subcontractors
Subcontractor Packages->Structural/Concrete Subcontractors
Subcontractor Packages->Envelope/Facade Subcontractors
Subcontractor Packages->Finishing Trades
Procurement Platform (e.g. Procore, Autodesk Build)->Purchase Orders & Contracts
Procurement Platform (e.g. Procore, Autodesk Build)->Cloud SaaS & Identity
Purchase Orders & Contracts->Construction Law & Standard Contracts (JCT/AIA/FIDIC)
Change Orders / Variations->Purchase Orders & Contracts

Site Management / Superintendent->Daily Coordination Meetings
Site Management / Superintendent->Site Safety Management
Site Management / Superintendent->Trade Sequencing (Look-ahead)
Daily Coordination Meetings->Trade Sequencing (Look-ahead)
Trade Sequencing (Look-ahead)->Just-in-Time Site Delivery
Trade Sequencing (Look-ahead)->MEP Subcontractors
Trade Sequencing (Look-ahead)->Structural/Concrete Subcontractors
Site Safety Management->Health & Safety Regulation (OSHA/HSE)
Quality Inspections->Building Code Compliance

MEP Subcontractors->Trade Labour Pool
Structural/Concrete Subcontractors->Trade Labour Pool
Envelope/Facade Subcontractors->Trade Labour Pool
Finishing Trades->Trade Labour Pool
MEP Subcontractors->Material Sourcing (Steel, Concrete, Glass)
Structural/Concrete Subcontractors->Material Sourcing (Steel, Concrete, Glass)
Envelope/Facade Subcontractors->Specialty Materials (Low-carbon, Engineered)
Finishing Trades->Commodity Materials (Aggregates, Rebar, Timber)

Just-in-Time Site Delivery->Material Laydown / Staging
Just-in-Time Site Delivery->Freight & Haulage
Material Laydown / Staging->Long-lead Item Management
Freight & Haulage->Customs & Cross-border Logistics
Long-lead Item Management->Supplier/Fabricator Relationships
Material Sourcing (Steel, Concrete, Glass)->Supplier/Fabricator Relationships
Material Sourcing (Steel, Concrete, Glass)->Commodity Materials (Aggregates, Rebar, Timber)
Specialty Materials (Low-carbon, Engineered)->Supplier/Fabricator Relationships

Building Code Compliance->Planning/Permit Approvals
Building Code Compliance->Fire & Life-Safety Certification
Planning/Permit Approvals->Construction Law & Standard Contracts (JCT/AIA/FIDIC)
Insurance & Bonding->Construction Law & Standard Contracts (JCT/AIA/FIDIC)
ESG & Embodied-Carbon Reporting->BIM Model (Federated)
ESG & Embodied-Carbon Reporting->Specialty Materials (Low-carbon, Engineered)

Common Data Environment (CDE)->Cloud SaaS & Identity
Common Data Environment (CDE)->Connectivity (Site Networking)
BIM Model (Federated)->Clash Detection (Navisworks/Solibri)
Scheduling Software (P6/MSP)->Cloud SaaS & Identity
Project Reporting Dashboards->Common Data Environment (CDE)
Project Reporting Dashboards->Scheduling Software (P6/MSP)
Digital Twin / Sensor Feeds->Connectivity (Site Networking)
Digital Twin / Sensor Feeds->Common Data Environment (CDE)

// Strategic markers
evolve Digital Twin / Sensor Feeds 0.55
evolve Specialty Materials (Low-carbon, Engineered) 0.50
evolve Procurement Platform (e.g. Procore, Autodesk Build) 0.78
evolve ESG & Embodied-Carbon Reporting 0.55

note Differentiation zone [0.70, 0.28]
note Commodity / utility [0.20, 0.90]
pipeline Procurement Platform (e.g. Procore, Autodesk Build) [0.45, 0.80]
```

---

## 3. Strategic analysis

### a. Differentiation opportunities (top 3 — BUILD)

1. **Value Engineering** (Custom Built) — the craft of re-working design and specification to hit budget without losing intent is visibly at the top of the map and still highly Custom Built. Real differentiators (a consultant or GC with a strong VE capability) win jobs on this. No product category covers it.
2. **Site Management / Superintendent** (Custom Built) — the whole chain converges on the superintendent's judgement. Highly visible to the client, and still a craft role that refuses to industrialise. A GC with a strong superintendent bench outperforms.
3. **Digital Twin / Sensor Feeds** (Genesis → Custom Built) — deeper in the chain but strategically pivotal: the first GCs to wire the physical-build feedback loop back into the CDE and schedule gain a durable edge. Today this is still Genesis; the `evolve` arrow targets mid-Custom.

Runner-up worth calling out: **ESG & Embodied-Carbon Reporting** (Genesis, ε ≈ 0.25, but unusually visible at ν = 0.70 because clients are now asking for it). Placed in the "differentiation zone" note for this reason. Being the GC/architect who can credibly deliver carbon reporting wins RFPs in 2023.

### b. Commodity-leverage candidates (top 3 — BUY / RENT)

1. **Commodity Materials (Aggregates, Rebar, Timber)** (Commodity +utility) — price-driven, interchangeable, many suppliers. Source on lowest landed cost; don't try to lock in bespoke.
2. **Scheduling Software (P6/MSP)** (Commodity +utility) — Primavera P6 and MS Project are standard; no differentiation in owning or specialising the tool itself. Rent or standard-licence.
3. **Cloud SaaS & Identity / Connectivity** (Commodity +utility) — AWS/Azure/GCP plus on-site mesh/cellular. Pure utility; never engineer.

Also worth listing: **Health & Safety Regulation (OSHA/HSE)** and **Construction Law (JCT/AIA/FIDIC)** — Commodity (+utility) in the sense of "standardised accepted knowledge." You hire lawyers and safety officers; you don't invent the standards.

### c. Dependency risks (top 3)

1. **Structural/Concrete Subcontractors → Material Sourcing (Steel, Concrete, Glass)** — a mid-visible, user-close trade depends on a post-2021 materials market still recovering from price shocks and long lead times. A 6-week steel slip cascades into schedule slip and change-order pain. Classic "visible thing on fragile foundation" risk.
2. **Just-in-Time Site Delivery → Freight & Haulage → Customs & Cross-border Logistics** — visible site logistics depends on a logistics chain that was visibly fragile through 2022 (port congestion, driver shortages, container rates). JIT on a commercial build amplifies the risk because there's no laydown yard buffer.
3. **All four subcontractor trades → Trade Labour Pool** — every trade is ultimately a labour problem. The US/UK construction labour pool has structural skill shortages (ageing workforce, immigration headwinds, post-COVID exits). Visibility is lower in the chart but the *dependency* is total — no labour means no build.

Secondary concern: **Specifications (CSI/NBS) → Specialty Materials (Low-carbon, Engineered)** — an architect specifying cross-laminated timber or low-carbon cement today is committing to a supply chain that is still Genesis. Substitution risk if suppliers fail to deliver.

### d. Suggested gameplays

From Wardley's 61-play catalogue:

- **#1 Focus on user needs** — re-affirm that the map's three anchors (Client, Architect, GC) each get distinct paths through the chain. Design-build vs. design-bid-build deliver different edges; the map should be re-drawn for each procurement route.
- **#36 Directed investment** on **Digital Twin / Sensor Feeds** and **ESG Reporting** — these are the two Genesis-stage components where a GC with capital can build a moat that will still be differentiating in 3–5 years.
- **#56 First mover** on **ESG & Embodied-Carbon Reporting** — EU CSRD and the UK Part Z debate mean reporting is about to industrialise under regulation. Being early captures reputational and compliance premium before it becomes table-stakes.
- **#43 Sensing Engines (ILC)** on the **Procurement Platform** layer — Procore, Autodesk Build, RIB, Oracle Aconex are the race. Watch which wins each geography; plug in ecosystem APIs; avoid betting the farm on one vendor during the Stage III → Stage IV transition (see `pipeline` marker).
- **#15 Open Approaches** on **BIM Model (Federated)** — IFC and openBIM standards exist precisely to prevent Autodesk Revit from owning the schema. Architects and clients should push for open data portability before lock-in ossifies.
- **#41 Alliances** on **Supplier/Fabricator Relationships** — for specialty items (facade, long-lead MEP, engineered timber) alliance-based procurement beats spot-market given 2023's volatility.
- **#29 Harvesting** on commodity materials and on the cloud/identity stack — let the market do the pricing; buy on landed cost and SLA, not relationships.
- **#4 Structure & Culture** (PST) — design team as pioneers (BIM, digital twin, ESG), project delivery as settlers (procurement, VE, superintendent), materials/logistics as town planners (repeatable, flow-optimised). A single culture across all three is a common failure mode in GCs.
- **#34 Procrastination** on **Clash Detection tooling** — Navisworks and Solibri are mature, converging; don't burn engineering on building your own. Let the vendors converge.

### e. Doctrine notes

Checked against Wardley's 40 principles:

- **#1 Focus on user needs** — satisfied by the three-anchor structure.
- **#10 Know your users** — satisfied; Client / Architect / GC are distinct users with distinct paths.
- **#13 Manage inertia** — live concern. From the 17 forms of inertia:
  - **#4 Human capital** — the Superintendent and Trade Labour Pool are deeply craft-based; industry-wide skill shortages make any process change painful.
  - **#1 Supplier relationship change** — subcontractor relationships are decades old in many markets; switching costs are real.
  - **#9 Re-architecture cost** — moving a firm from document-centric procurement to CDE-centric takes years of re-tooling; many mid-market GCs are stuck.
  - **#16 Rewards & culture** — subcontractor margin models reward claims/variations, not schedule certainty. This actively resists process digitisation.
- **#7 Use appropriate methods** — partially violated in practice. Most GCs run one methodology (waterfall-ish critical-path) across the whole map. Genesis components (digital twin, ESG) need agile experimentation; commodity layers (payroll, cloud) need six-sigma operational excellence; these should not share a PM style.
- **#9 Think small (know the details)** — risk of coarse mapping. "Subcontractor" as one node would hide MEP vs. structural vs. envelope vs. finishing; each has a different evolution stage and different sourcing economics. The map above splits them — don't re-collapse them.
- **#2 Use a systematic mechanism of learning** — the construction industry's post-project learning loop is famously weak (lessons-learned binders gather dust). A CDE that survives handover and feeds the next project is still aspirational for most firms.
- **#15 Use FIRE (fast, inexpensive, restrained, elegant)** — flagged. Many firms launch "innovation programmes" that are none of the four. Digital twin pilots in particular burn budget before the data loop is proven.

### f. Climatic context

Active patterns from the 27 climatic patterns (see `references/climatic-patterns.md`):

- **#3 Everything evolves through supply and demand competition** — the procurement-platform category (Procore went public in 2021, Autodesk Build launched 2021) is mid-migration from Stage III → Stage IV. Incumbents (Procore's on-prem legacy competitors) are losing to SaaS. The `pipeline` marker on the procurement platform captures this in-transit state.
- **#9 Components can co-evolve** — BIM (activity) and integrated-project-delivery (practice) are co-evolving. Firms adopting BIM with document-era practices get worse outcomes than firms that update both.
- **#15–17 Inertia patterns** — the construction industry is possibly the most inertia-rich sector outside defence. Sunk capital in document workflows, human-capital dependence on superintendents, risk-averse client culture, and regulatory lag all compound. Expect most components to evolve slower than the underlying technology permits.
- **#4 Multi-wave evolution** — materials are visibly multi-wave: steel/concrete (Stage IV commodity) coexist with an emerging wave of low-carbon alternatives (Stage I–II Genesis/Custom). The two generations will share the map for ~10 years before substitution accelerates.
- **#27 Product-to-utility punctuated equilibrium** — procurement-platform space is showing classic Stage III → IV war signals: open-source alternatives (OpenProject etc.), cloud-native consolidation, API-first platforms, subscription pricing compressing margins. Expect a shake-out.

### g. Deep-placement notes

Four components flagged for targeted reflection against domain priors:

1. **Procurement Platform (Procore, Autodesk Build)** — initial cheat-sheet placement mid-Product (ε ≈ 0.55). Vendor landscape: Procore IPO'd 2021 at scale (~$10B market cap), Autodesk Construction Cloud unified in 2021, Oracle Aconex/Primavera consolidated, RIB/Nemetschek active in EU, open-source options exist. This is classic Stage III late/early Stage IV dynamics — multiple mature vendors, subscription pricing, feature parity flattening. Kept at 0.55 as a point estimate but explicitly marked with `pipeline` from 0.45 to 0.80 to capture the rapid industrialisation; `evolve` target 0.78 reflects a 2–3 year projection. *Confirms Stage III with heavy Stage IV drift.*

2. **BIM Model (Federated)** — initial placement mid-Product. BIM Level 2 is mandated in UK public-sector since 2016 and widely required in US commercial; Revit dominates but openBIM/IFC is standardising; many mid-market firms still run document-heavy. Kept at ε = 0.50 (early Product) because adoption is wide in top quartile of firms, patchy elsewhere. *Confirms Stage III; variance across geography and firm size means "range not point" is honest.*

3. **Specialty Materials (Low-carbon concrete, mass timber, engineered composites)** — initial cheat-sheet score would cluster around late Custom (ε ≈ 0.4). In 2023 reality: mass timber still bespoke (Stage I–II), low-carbon cement emerging from demonstration projects, engineered glass/facade systems more established. Pulled to ε = 0.30 (Genesis / early Custom) because the cheat-sheet rows on Ubiquity (rare) and User Perception (exciting, experimental) pushed left. *Shifted from 0.40 → 0.30 after reflection.*

4. **ESG & Embodied-Carbon Reporting** — initial cheat-sheet placement Custom Built. Regulatory landscape as of March 2023: EU CSRD adopted 2022 (phased from 2024), SEC climate-disclosure rule proposed, UK Part Z lobbied but not adopted, RICS Whole-Life Carbon Assessment (2nd ed) in force. Vendors (One Click LCA, EC3, Building Transparency) are Stage II–III tools. Methodology still varies. Kept at ε = 0.25 (Genesis/Custom boundary) because *industry practice* lags the regulatory framework. Visibility raised to ν = 0.70 because clients now ask for it explicitly on RFPs — it's visible even though it's Genesis. `evolve` target 0.55 reflects that CSRD will force Stage III within 2 years. *Confirmed Genesis (today) with near-term industrialisation pressure.*

### h. Derived heuristics (attention prompts, not canonical Wardley)

These are the skill's math-model heuristics — ranked qualitatively. D = ν·(1−ε), K = (1−ν)·ε, R = ν_source · (1−ε_target).

**Highest D (differentiation pressure — where to invest):**
1. Value Engineering (Custom Built, user-visible to client via cost)
2. Site Management / Superintendent (Custom Built, user-visible to client via delivery)
3. ESG & Embodied-Carbon Reporting (Genesis, unusually user-visible)

**Highest K (commodity leverage — where to consume as utility):**
1. Cloud SaaS & Identity (deep, Commodity +utility)
2. Connectivity / Site Networking (deepest, Commodity +utility)
3. Commodity Materials (Aggregates, Rebar, Timber) (deep, Commodity +utility)
4. Construction Law & Standard Contracts — deep, accepted-knowledge

**Highest R (dependency risk — visible edges on fragile foundations):**
1. Structural/Concrete Subcontractors → Specialty Materials (if low-carbon specified)
2. Site Management → Trade Sequencing → (long-lead items) → Supplier relationships
3. Completed Building Handover → Building Code Compliance → Fire & Life-Safety Certification (particularly acute post-Grenfell in UK, post-Champlain Towers in US)

### i. OWM validation

`python3 ${CLAUDE_SKILL_DIR}/scripts/validate_owm.py ./draft.owm`
→ **OK: 49 components/anchors, 77 edges — no violations.**

### j. Caveat

Every `evolve` arrow on this map is a **scenario**, not a forecast. Wardley's climatic pattern #18 stands: *"you cannot measure evolution over time or adoption."* The `pipeline` on the procurement platform and the four `evolve` targets (digital twin → 0.55, specialty materials → 0.50, procurement platform → 0.78, ESG → 0.55) are directional reads of 2023 signals, not predictions. Regulation, capital markets, and climatic events (recession, carbon pricing, new codes) can shift any of them. Re-map annually.

---

## 4. Summary — what's differentiating vs. commoditising, and where the chain is fragile

**Differentiating (BUILD, moat territory):**
- **Value Engineering** and **Superintendent craft** — where a GC wins jobs and delivers margin. Still Custom Built.
- **ESG / Embodied-Carbon Reporting** and **Digital Twin / Sensor Feeds** — still Genesis/early-Custom. Investing here in 2023 positions for 2025–2028 as regulation and client demand catch up.
- **Specialty low-carbon materials** — a supply-chain alliance with early fabricators is a Genesis-stage bet with large upside.

**Commoditising (BUY / RENT / HARVEST):**
- **Procurement platforms** (Procore, Autodesk Build) — mid Stage III, migrating to Stage IV. Pick a platform carefully but don't build one.
- **Cloud, identity, connectivity, scheduling software** — pure Commodity (+utility). Rent.
- **Commodity materials** (aggregates, rebar, bulk timber) — classic Commodity (+utility) sourcing.
- **Code compliance, health & safety regulation, standard contracts** — accepted standards; staff these with expertise, don't invent.

**Fragility (where the chain breaks in 2023):**
1. **Materials and freight layer** — steel/concrete/glass still in post-shock volatility; JIT delivery has little buffer; customs/cross-border adds lead-time risk. Every visible trade depends on this.
2. **Trade Labour Pool** — structural skills shortage; no amount of digitisation offsets the absence of crews.
3. **Subcontractor incentives** — claims/variation-driven margin models actively fight schedule certainty and digital adoption. A doctrine violation (#16 Rewards & culture) at the industry level.
4. **Specialty material commitments** — an architect specifying low-carbon concrete or mass timber is betting on a Genesis-stage supply chain with sparse second-sourcing. High R.
5. **Fire & Life-Safety / Code-compliance pathway** — visibility is high (client cannot hand over without it) but the regulatory regime is in post-incident flux (Grenfell, Champlain Towers, UK Building Safety Act 2022). Interpretation risk sits on a visible path.
