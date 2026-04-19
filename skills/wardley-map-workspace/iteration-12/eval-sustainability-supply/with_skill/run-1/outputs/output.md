# Wardley Map — Sustainable Supply Chain Management

**Scenario.** How organisations reduce environmental and social impact across their supply chains — traceability, emissions measurement, supplier assessment, circular-economy models, regulation (CSRD, CBAM, EUDR, SFDR, Modern Slavery, ISSB), stakeholder reporting, and governance. What is differentiating, what is commoditising, and where is sustainability fragile?

Three anchors are used because sustainable supply-chain management has genuinely distinct user types with different needs:

- **Sustainability Officer** — the internal user who owns the programme and consumes dashboards, scorecards, strategy.
- **Regulator / Auditor** — an external user who consumes statutory filings (CSRD/ESRS report, CBAM, EUDR, SFDR, Modern Slavery Statement) and assurance opinions.
- **Investor / Customer** — the external stakeholder who reads ESG disclosures, product sustainability claims, and ratings.

---

## OWM

```owm
title Sustainable Supply Chain Management
style wardley

// Anchors — three user types
anchor Sustainability Officer [0.99, 0.55]
anchor Regulator / Auditor [0.96, 0.60]
anchor Investor / Customer [0.97, 0.50]

// User-facing reporting & disclosure
component CSRD / ESRS Report [0.90, 0.55]
component CDP / TCFD Disclosure [0.88, 0.70]
component Investor ESG Dashboard [0.86, 0.55]
component Product Sustainability Claim [0.84, 0.40]
component Supplier Scorecard [0.82, 0.45]
component Sustainability Strategy [0.80, 0.30]

// Regulatory filings (read by Regulator anchor)
component CBAM Reporting [0.90, 0.45]
component EUDR Deforestation Compliance [0.88, 0.30]
component SFDR Classification [0.86, 0.50]
component Modern Slavery Statement [0.88, 0.70]
component ISSB / IFRS S1 S2 Alignment [0.82, 0.40]

// Governance & assurance
component Board ESG Oversight [0.78, 0.30]
component External Assurance (Limited / Reasonable) [0.76, 0.45]
component Double Materiality Assessment [0.74, 0.40]
component Internal Controls over Sustainability [0.72, 0.35]

// Core activities — assessment, due diligence
component Supplier ESG Assessment [0.68, 0.45]
component Supplier Code of Conduct [0.66, 0.70]
component Supply Chain Due Diligence [0.70, 0.35]
component Human Rights / Modern Slavery Audit [0.62, 0.50]
component Environmental & Social Audit [0.60, 0.55]
component Corrective Action Tracking [0.56, 0.40]

// Emissions measurement
component Scope 1 Emissions Accounting [0.58, 0.75]
component Scope 2 Emissions Accounting [0.57, 0.75]
component Scope 3 Emissions Accounting [0.55, 0.35]
component Carbon Accounting Platform [0.52, 0.55]
component Product Carbon Footprint (PCF) [0.50, 0.35]
component Lifecycle Assessment (LCA) [0.48, 0.45]

// Traceability & chain-of-custody
component Chain-of-Custody Certification [0.46, 0.60]
component Digital Product Passport (DPP) [0.44, 0.20]
component Traceability Platform [0.40, 0.40]
component Tier-N Supplier Mapping [0.42, 0.30]
component Origin / Provenance Data [0.36, 0.35]

// Circular economy programmes
component Product Take-Back Scheme [0.48, 0.30]
component Reverse Logistics [0.34, 0.50]
component Recycled Content Sourcing [0.50, 0.55]
component Design for Disassembly [0.52, 0.25]

// Data plumbing
component Supplier Data Collection [0.32, 0.50]
component ESG Data Lake / Warehouse [0.26, 0.70]
component Emission Factor Database [0.22, 0.75]
component Primary Activity Data (Utilities, Fuel) [0.24, 0.65]
component IoT / Sensor Telemetry [0.18, 0.55]
component Third-Party ESG Ratings Feed [0.30, 0.70]

// Knowledge / standards
component GHG Protocol [0.20, 0.88]
component Science-Based Targets (SBTi) [0.30, 0.70]
component ESRS Standards [0.24, 0.60]
component ISO 14001 / 14064 / 14067 [0.18, 0.88]
component Emission Factor Science [0.08, 0.85]
component Climate Science / IPCC [0.06, 0.90]

// Infrastructure
component Cloud Compute [0.14, 0.92]
component Database [0.12, 0.90]
component Identity / Auth [0.12, 0.90]
component Document Storage [0.14, 0.92]
component Blockchain / Distributed Ledger [0.16, 0.35]

// Dependencies — reporting up to users
Sustainability Officer->Sustainability Strategy
Sustainability Officer->CSRD / ESRS Report
Sustainability Officer->Supplier Scorecard
Sustainability Officer->Investor ESG Dashboard
Regulator / Auditor->CSRD / ESRS Report
Regulator / Auditor->CBAM Reporting
Regulator / Auditor->EUDR Deforestation Compliance
Regulator / Auditor->Modern Slavery Statement
Regulator / Auditor->SFDR Classification
Regulator / Auditor->External Assurance (Limited / Reasonable)
Investor / Customer->Investor ESG Dashboard
Investor / Customer->CDP / TCFD Disclosure
Investor / Customer->Product Sustainability Claim

// Reports depend on core data + assurance
CSRD / ESRS Report->Double Materiality Assessment
CSRD / ESRS Report->External Assurance (Limited / Reasonable)
CSRD / ESRS Report->ESRS Standards
CSRD / ESRS Report->Scope 1 Emissions Accounting
CSRD / ESRS Report->Scope 2 Emissions Accounting
CSRD / ESRS Report->Scope 3 Emissions Accounting
CSRD / ESRS Report->Supply Chain Due Diligence
CDP / TCFD Disclosure->Scope 1 Emissions Accounting
CDP / TCFD Disclosure->Scope 2 Emissions Accounting
CDP / TCFD Disclosure->Scope 3 Emissions Accounting
CDP / TCFD Disclosure->Science-Based Targets (SBTi)
Investor ESG Dashboard->Carbon Accounting Platform
Investor ESG Dashboard->Supplier Scorecard
Investor ESG Dashboard->ESG Data Lake / Warehouse
Product Sustainability Claim->Product Carbon Footprint (PCF)
Product Sustainability Claim->Chain-of-Custody Certification
Product Sustainability Claim->Digital Product Passport (DPP)
Supplier Scorecard->Supplier ESG Assessment
Supplier Scorecard->Supplier Data Collection
Sustainability Strategy->Board ESG Oversight
Sustainability Strategy->Double Materiality Assessment
Sustainability Strategy->Science-Based Targets (SBTi)

// Regulatory filings
CBAM Reporting->Scope 1 Emissions Accounting
CBAM Reporting->Origin / Provenance Data
EUDR Deforestation Compliance->Origin / Provenance Data
EUDR Deforestation Compliance->Tier-N Supplier Mapping
Modern Slavery Statement->Human Rights / Modern Slavery Audit
SFDR Classification->ISSB / IFRS S1 S2 Alignment
ISSB / IFRS S1 S2 Alignment->ESRS Standards

// Governance
Board ESG Oversight->Internal Controls over Sustainability
External Assurance (Limited / Reasonable)->Internal Controls over Sustainability
External Assurance (Limited / Reasonable)->ESG Data Lake / Warehouse
Double Materiality Assessment->ESRS Standards
Internal Controls over Sustainability->ESG Data Lake / Warehouse

// Assessment and due diligence
Supplier ESG Assessment->Supplier Code of Conduct
Supplier ESG Assessment->Third-Party ESG Ratings Feed
Supply Chain Due Diligence->Tier-N Supplier Mapping
Supply Chain Due Diligence->Human Rights / Modern Slavery Audit
Supply Chain Due Diligence->Environmental & Social Audit
Human Rights / Modern Slavery Audit->Corrective Action Tracking
Environmental & Social Audit->Corrective Action Tracking

// Emissions
Scope 1 Emissions Accounting->Carbon Accounting Platform
Scope 2 Emissions Accounting->Carbon Accounting Platform
Scope 3 Emissions Accounting->Carbon Accounting Platform
Scope 3 Emissions Accounting->Supplier Data Collection
Scope 3 Emissions Accounting->Emission Factor Database
Carbon Accounting Platform->ESG Data Lake / Warehouse
Carbon Accounting Platform->GHG Protocol
Scope 1 Emissions Accounting->Primary Activity Data (Utilities, Fuel)
Scope 2 Emissions Accounting->Primary Activity Data (Utilities, Fuel)
Scope 1 Emissions Accounting->GHG Protocol
Scope 2 Emissions Accounting->GHG Protocol
Scope 3 Emissions Accounting->GHG Protocol
Product Carbon Footprint (PCF)->Lifecycle Assessment (LCA)
Product Carbon Footprint (PCF)->ISO 14001 / 14064 / 14067
Lifecycle Assessment (LCA)->Emission Factor Database
Lifecycle Assessment (LCA)->ISO 14001 / 14064 / 14067

// Traceability
Chain-of-Custody Certification->Traceability Platform
Digital Product Passport (DPP)->Traceability Platform
Traceability Platform->Origin / Provenance Data
Traceability Platform->Blockchain / Distributed Ledger
Tier-N Supplier Mapping->Supplier Data Collection
Origin / Provenance Data->IoT / Sensor Telemetry
Origin / Provenance Data->Supplier Data Collection

// Circular
Product Take-Back Scheme->Reverse Logistics
Recycled Content Sourcing->Chain-of-Custody Certification
Design for Disassembly->Lifecycle Assessment (LCA)

// Data plumbing
Supplier Data Collection->ESG Data Lake / Warehouse
Emission Factor Database->Emission Factor Science
ESG Data Lake / Warehouse->Database
ESG Data Lake / Warehouse->Cloud Compute
Primary Activity Data (Utilities, Fuel)->IoT / Sensor Telemetry
Third-Party ESG Ratings Feed->Database
IoT / Sensor Telemetry->Cloud Compute

// Infrastructure
Cloud Compute->Database
Cloud Compute->Identity / Auth
Document Storage->Cloud Compute
Blockchain / Distributed Ledger->Database

// Knowledge
Science-Based Targets (SBTi)->Climate Science / IPCC
GHG Protocol->Climate Science / IPCC
ESRS Standards->Climate Science / IPCC
Emission Factor Science->Climate Science / IPCC

// Evolution targets (scenario)
evolve Scope 3 Emissions Accounting 0.60
evolve Digital Product Passport (DPP) 0.55
evolve Tier-N Supplier Mapping 0.55
evolve Carbon Accounting Platform 0.80
evolve CBAM Reporting 0.75
evolve Supply Chain Due Diligence 0.55

// Inertia markers
component Legacy ERP ESG Module [0.36, 0.65] inertia
component Spreadsheet-based Carbon Tracking [0.40, 0.70] inertia

// Notes
note Build moat — claims, materiality, strategy [0.85, 0.25]
note Industrialising — carbon accounting rails [0.55, 0.70]
note Utility layer — cloud, DB, identity [0.12, 0.92]
note Fragile — Scope 3, Tier-N visibility [0.55, 0.30]
```

**Validator result.** `OK: 58 components/anchors, 95 edges — no violations.`

---

## Strategic analysis

### a. Differentiation opportunities (top 3)

1. **Sustainability Strategy** (Custom Built, stage II) — the organisation's point of view on where it will reduce impact and why. Not a product you can buy; it expresses the material issues, ambition, and theory-of-change. This is where boards and CEOs differentiate from peers, and what investors increasingly reward or punish. Highest differentiation leverage because it is user-facing *and* genuinely uncommoditised.
2. **Double Materiality Assessment** (Custom Built) — the uniquely-CSRD requirement to score impacts on both financial performance and people/planet. The methodology is still forming; early CSRD filers are inventing the craft. Doing this well (or badly) shapes every subsequent disclosure.
3. **Tier-N Supplier Mapping** (Custom Built, ε≈0.30) — mapping beyond Tier-1 into Tier-N where most environmental and social risk actually sits. Critically visible under EUDR, CSDDD, CBAM and Modern Slavery regimes. Still bespoke per commodity and geography. Organisations that solve this once extract reuse across multiple disclosures.

Honourable mention: **Product Sustainability Claim** (Custom Built) — regulated (EU Green Claims Directive) and a growing competitive front in B2C. Differentiates only if defensible; otherwise it's greenwashing exposure.

### b. Commodity-leverage candidates (top 3) — rent, do not build

1. **Cloud Compute / Database / Document Storage / Identity** (Commodity +utility) — the base plumbing. Rent from hyperscalers.
2. **GHG Protocol / ISO 14064 / Emission Factor Science / Emission Factor Database** (Commodity +utility / edge-of-Commodity) — accepted knowledge and public utility data. Use the standards; buy or subscribe to factor libraries (ecoinvent, DEFRA, IEA). Do not invent your own emission factors.
3. **Scope 1 & Scope 2 Emissions Accounting** (Product +rental, ε≈0.75) — a crowded vendor market (Watershed, Persefoni, Sweep, Sustain.life, Salesforce Net Zero Cloud, Workiva, Microsoft Sustainability Manager, IBM Envizi, SAP Sustainability Footprint Management). Buy, do not build. The differentiation is in Scope 3 and supply-chain data, not in summing utility bills.

### c. Dependency risks (top 3)

1. **CSRD / ESRS Report → Scope 3 Emissions Accounting** — a high-visibility statutory filing depends on emissions category where 70–90 % of many companies' footprint sits and where methodology is still Custom Built. This is the single largest source of assurance and restatement risk.
2. **CBAM Reporting → Origin / Provenance Data** — from 2026 the definitive CBAM regime requires verified embedded emissions for iron, steel, cement, aluminium, fertilisers, hydrogen and electricity imports. The upstream data is immature and often held by third-country suppliers with no incentive or capability to share it. The filing is legally required; the foundation is not legally obtainable.
3. **EUDR Deforestation Compliance → Tier-N Supplier Mapping** — EUDR requires geolocated plots for seven commodities (cattle, cocoa, coffee, palm oil, rubber, soya, wood). Tier-N visibility in these agricultural supply chains is early Custom Built at best. Non-compliance is a forfeiture-of-goods risk at EU borders.

Honourable mention: **Investor ESG Dashboard → Third-Party ESG Ratings Feed** — investors act on ratings from MSCI, S&P Global, Sustainalytics, ISS. Methodologies disagree; the same company gets divergent scores. Visible decisions depend on a fragile and contested proxy.

### d. Suggested gameplays

- **#1 Focus on user needs** — three anchors keep all three user types in view. If the programme is organised around "Regulator" alone, investor claims and internal strategy starve.
- **#15 Open Approaches** on **Carbon Accounting Platform**, **Emission Factor Database**, **GHG Protocol extensions**. The PACT (Partnership for Carbon Transparency) Pathfinder framework and WBCSD's open methodologies are already doing this. Support and contribute; do not build proprietary carbon accounting.
- **#36 Directed investment** on **Double Materiality Assessment**, **Sustainability Strategy**, **Tier-N Supplier Mapping** — the three highest-differentiation components. Put the sustainability team's scarce senior capacity here, not in manual data wrangling.
- **#29 Harvesting** on the carbon-accounting platform vendor space — let Watershed, Persefoni, Sweep and Microsoft Sustainability Manager compete; adopt the winner once consolidation happens. Avoid long-term lock-in by insisting on open data export (ESRS XBRL, PACT).
- **#41 Alliances** on **Scope 3** and **Tier-N Supplier Mapping** — sector coalitions (Responsible Business Alliance, Together for Sustainability, Sustainable Apparel Coalition, Responsible Minerals Initiative, Catena-X) let you share supplier audit data and cut duplicate assessment burden. The alliance is the only way deep-tier visibility becomes economical.
- **#43 Sensing Engines (ILC)** on the **Digital Product Passport** space — watch the EU ESPR regulated categories (batteries first, then textiles, electronics, construction products) for the winners that emerge. Do not commit to a single DPP stack yet.
- **#56 First mover** on **CBAM Reporting** and **EUDR** — the 2026 definitive CBAM and the EUDR enforcement dates create a narrow window where early compliance is a differentiator. After that, it is cost of doing business.
- **#30 Standards game** — participate in ESRS/ISSB interoperability working groups. Whoever shapes the ISSB–ESRS bridge and the GHG Protocol Land Sector / Scope 3 revisions (both due in 2026–2027) shapes the cost of compliance for the whole sector.
- **#13 Lobbying** — candid acknowledgement that much of this regime is politically contested (the EU Omnibus simplification package and deferrals are already in flight). Organisations lobby both to tighten (first movers wanting to lock in advantage) and to loosen (laggards).

### e. Doctrine notes

- **#1 Focus on user needs** — satisfied; three anchors represent the real user types. A single-anchor "Stakeholders" version of this map would mask the conflicts between what the Regulator, the Investor, and the Sustainability Officer each want.
- **#10 Know your users** — satisfied; the three anchors separate needs that materially diverge. Regulator cares about conformity; Investor cares about comparability and risk; internal cares about reducibility and action. The same disclosure serves all three poorly.
- **#2 Use a systematic mechanism of learning** — at risk. Most programmes consume Corrective Action Tracking as a filing chore rather than as a learning loop into Sustainability Strategy. Close the loop or this whole map is performative.
- **#13 Manage inertia** — the two inertia-marked components (Legacy ERP ESG Module, Spreadsheet-based Carbon Tracking) are where most organisations live today. Named explicitly so they are not ignored.
- **#11 A bias toward action** — the map has many "reporting" components and fewer "reducing" components. That is an honest reflection of current practice but also a flag: sustainability programmes tilt toward disclosure theatre unless governance explicitly rewards reductions.
- **#26 Optimise flow** — Scope 3 and Tier-N data flow through email and spreadsheets in most organisations. The bottleneck is Supplier Data Collection; optimise it first.

### f. Climatic context

From the 27 climatic patterns, four are actively shaping this map:

- **#3 Everything evolves** — sustainability reporting is visibly moving left-to-right. Carbon accounting software is an obvious Custom Built → Product transition over the past five years. Double materiality is at the start of the same curve.
- **#15–17 Inertia (three forms)** — the legacy-ERP inertia, the spreadsheet inertia, and the supplier-side political inertia (suppliers resisting data requests) together explain why the map is visibly "top-heavy": reporting has moved faster than underlying data collection.
- **#18 You cannot measure evolution over time or adoption** — the usual caveat, doubly important here because the sector has strong incentives to narrate progress that the cheat-sheet placements do not support.
- **#27 Product-to-utility punctuated equilibrium** — carbon accounting is already visibly entering this transition. Hyperscalers (Microsoft, Salesforce, SAP, Oracle, Google) have all launched sustainability clouds; it is plausible that within a 3–5 year horizon the core carbon accounting platform becomes a utility embedded in enterprise data stacks. That is what the `evolve Carbon Accounting Platform 0.80` arrow captures.
- **#11 Past success breeds inertia** — incumbent ERP vendors' existing dominance in enterprise finance is exactly what drags their ESG modules right despite weak functionality; customers buy the ESG module because they already own the ERP.

### g. Deep-placement notes

Five components warranted closer inspection beyond the cheat-sheet pass.

- **Carbon Accounting Platform** — initial cheat-sheet placement was Stage II–III mid-Product. Deep placement: 40+ identifiable vendors (Watershed, Persefoni, Sweep, Sustain.life, Plan A, Greenly, Normative, Emitwise, Workiva, Salesforce Net Zero Cloud, Microsoft Sustainability Manager, SAP Sustainability Footprint Management, IBM Envizi, Oracle Fusion Sustainability, Google Cloud, ServiceNow ESG, etc.). Hyperscalers entering is the Stage III→IV signal (#40 Fool's mate). Publication type shifted from "build your own carbon ledger" posts (Stage II) to vendor-comparison and Gartner/Forrester market guides (Stage III). Held at ε≈0.55 (early Product +rental); `evolve → 0.80` is a plausible 3–5 year scenario, not a forecast.
- **Scope 3 Emissions Accounting** — initial cheat-sheet score was high-variance across rows: Ubiquity rising fast (Stage III signals), Certainty still low (spend-based factors vs activity-based, primary vs secondary data debates, ongoing GHG Protocol Scope 3 revision due 2027). Kept at ε≈0.35 (Custom Built) with the high variance flagged, and an `evolve → 0.60` scenario arrow noting the direction. This is the single highest-variance placement in the map.
- **Digital Product Passport (DPP)** — regulatory driver (ESPR 2024/1781, Battery Passport 2027, textiles later) creates a hard deadline. Vendor market is nascent (Circularise, Kezzler, ChainPoint, Makersite, TrusTrace, EON, early blockchain consortia including Catena-X). No dominant platform; publications still describe the wonder. Placed at ε≈0.20 (late Genesis). `evolve → 0.55` reflects the regulatory timetable as a scenario.
- **CBAM Reporting** — transitional phase (default values permitted) runs to end-2025; definitive phase from 2026 requires verified embedded emissions. This is genuinely a Stage II component being industrialised by regulation ahead of readiness. Placed at ε≈0.45 now; `evolve → 0.75` once verified-data vendor markets emerge.
- **Tier-N Supplier Mapping** — platforms exist (Sourcemap, IntegrityNext, EcoVadis, Achilles, TrusTrace, Sayari) but most enterprises still rely on manual surveys. Mixed publication types (wonder + build + case studies) — the rows disagreed, variance elevated. Placed at ε≈0.30 (mid Custom Built). Left at this seed because the real constraint is suppliers' willingness and capability to respond, not mapping software — and that is the inertia being modelled.

Knowledge layer (GHG Protocol, ISO 14064, Emission Factor Science, Climate Science / IPCC) was not researched further — these are accepted knowledge by anybody's definition and are correctly placed at the Commodity-plus-utility end.

### h. Caveat

Every `evolve` arrow in this map is a scenario, not a forecast. Wardley's climatic pattern #18 holds: *you cannot measure evolution over time or adoption*. The direction of travel (rightward) is the reliable signal; the dated endpoints are not. The sustainability-reporting regime is unusually exposed to political reversal (e.g., the EU Omnibus simplification package currently in negotiation, US state-level anti-ESG legislation). A disruption to the regulatory drivers would reshape several evolutions — particularly CBAM, EUDR, and SFDR.

---

## Where sustainability is fragile

Four zones of fragility, in rough order of severity:

1. **The Scope 3 / Tier-N chasm.** User-visible filings (CSRD report, CBAM, CDP disclosure, product claims) are Stage III reporting rails standing on Stage II (Custom Built) supplier data. Assurance providers know it; so do regulators. Expect restatement and enforcement action in 2026–2028.
2. **Ratings divergence.** Investor decisions depend on third-party ratings that disagree by ~0.3 correlation. Whichever rating wins, the underlying data pipeline is the same map — so a move from one rating to another does not shift the fragility, only who gets blamed.
3. **Claim defensibility.** Product-level sustainability claims are regulated (EU Green Claims Directive, US FTC Green Guides) and sit on Lifecycle Assessment, Emission Factor Database, and Chain-of-Custody components that are still mixed Stage II–III. A wave of regulatory challenges and class actions is plausible.
4. **Political reversal.** Much of the right-hand industrialisation pressure comes from regulation. A political retreat (Omnibus, CSRD thresholds raised, CBAM narrowed) would leave many organisations with sunk investment in Stage II components that nobody legally requires. Doctrine #13 (manage inertia) matters symmetrically — both the inertia toward and the inertia away from sustainability work.
