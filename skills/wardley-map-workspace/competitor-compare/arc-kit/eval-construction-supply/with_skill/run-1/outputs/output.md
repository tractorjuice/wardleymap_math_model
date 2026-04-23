# UK Construction Supply Chain - Wardley Map (March 2023)

## Metadata

```yaml
wardley_map:
  metadata:
    title: "UK Construction Supply Chain (End-to-End)"
    author: "arc-kit wardley-mapping skill (blind benchmark run-1)"
    date: "2023-03-15"
    version: "1.0"
    scope: "Construction supply chain from citizen/government demand through build delivery, materials, manufacture, logistics, and the critical-national-infrastructure concerns of skilled-labour supply. Focus: what is still bespoke craft vs. what is ready to industrialise."
```

## Anchor (User Need)

- **Users:** Citizens, Government (housing policy), Mortgage Companies (project finance / valuation gatekeepers).
- **Need:** A reliable pipeline of habitable, regulation-compliant buildings — private homes, social housing, and commercial stock — delivered on time, on budget, and to a standard that mortgage finance and building control will accept.

## Visual Map

```text
Title: UK Construction Supply Chain (End-to-End)
Anchor: Habitable, regulation-compliant buildings
Date: 2023-03-15

                     Genesis         Custom          Product        Commodity
                       │               │               │               │
  Visible          ┌───┼───────────────┼───────────────┼───────────────┼───┐
  (user-facing)    │   │               │               │               │   │
                   │   │               │              Citizens ● Gov ● │   │
                   │   │               │                        │Mortg●│   │
                   │   │               │           CompletedHomes●   ● │   │
                   │   │               │   PlanningPermission ●   BldgRegs●│
                   │   │               │         BuildingInspection ●   │   │
                   │   │               │   MainContractor ●              │   │
                   │   │               │        SiteWorks ●  (bespoke)   │   │
                   │   │            ModularMMC ●→→  ArchDesign ●  BIM ●   │   │
                   │   │            FactoryMode ●→→          Blueprints ●│   │
                   │   │   DigitalTwin●→              SkilledTrades ×    │   │
                   │   │               │       PrefabPanels ●→           │   │
                   │   │               │    Training ●        Certific●  │   │
                   │   │               │              Unskilled Labour ● │   │
                   │   │               │    Platform ● Integrated●  Merchants●
                   │   │               │    Mkts →→→                     │   │
                   │   │               │       ComponentMfg ●  Cement ●  │   │
                   │   │               │                       Steel ●   │   │
                   │   │     Novel●→      RecycledMat ●       HeavyPlant●│   │
                   │   │  Substitut●→                          HandTools●│   │
                   │   │     MaterialVis●    Warehouse ●   Road/Haulage ●│   │
                   │   │     CNI Labour ●   Port/Import ● RawMaterials ● │   │
  Hidden           │   │               │               │               │   │
                   └───┴───────────────┴───────────────┴───────────────┴───┘

Legend:  ●  current position
         →  natural evolution (rightward drift)
         →→ accelerated evolution
         ×  inertia (resistance to movement)
```

## Components (structured)

```yaml
components:

  # === Anchors (demand side, top of map) ===
  - name: "Citizens"
    evolution: "Commodity"
    position: 0.97
    visibility: 0.95
    depends_on: ["Completed Homes (Private)", "Social Housing Stock"]
    notes: "Ultimate end user. Need is habitable home."
    movement: "none"

  - name: "Government Housing Policy"
    evolution: "Commodity"
    position: 0.95
    visibility: 0.92
    depends_on:
      - "Social Housing Stock"
      - "Completed Homes (Private)"
      - "Building Regulations"
      - "Critical National Infrastructure (Skilled Labour Supply)"
    notes: "Sets targets (300k/yr), planning policy, HRRA (Building Safety Act 2022)."
    movement: "none"

  - name: "Mortgage Companies"
    evolution: "Commodity"
    position: 0.93
    visibility: 0.30
    depends_on:
      - "Completed Homes (Private)"
      - "Building Inspection / QA"
    notes: "Gate for private demand. Will not lend on non-compliant or non-certified stock."
    movement: "none"

  # === Demand-side outputs ===
  - name: "Completed Homes (Private)"
    evolution: "Product"
    position: 0.65
    visibility: 0.40
    depends_on: ["Planning Permission", "Building Inspection / QA", "Main Contractor Delivery"]
    notes: "Volume-housebuilder output (Barratt, Persimmon, Taylor Wimpey). Increasingly productised but still largely site-built."
    movement: "evolving"

  - name: "Social Housing Stock"
    evolution: "Product"
    position: 0.60
    visibility: 0.45
    depends_on: ["Planning Permission", "Main Contractor Delivery", "Building Inspection / QA"]
    notes: "HA and council-commissioned. Increasingly using MMC (Homes England Affordable Homes Programme 25% MMC target)."
    movement: "evolving"

  - name: "Commercial Buildings"
    evolution: "Product"
    position: 0.65
    visibility: 0.35
    depends_on: ["Planning Permission", "Main Contractor Delivery", "Building Inspection / QA"]
    notes: "Office, retail, industrial. Commercial fit-out is further right than housing."
    movement: "evolving"

  # === Regulation / QA layer ===
  - name: "Planning Permission"
    evolution: "Product"
    position: 0.60
    visibility: 0.50
    depends_on: ["Building Regulations"]
    notes: "LPA-driven, slow, paper+portal. NPPF defines rules; Planning Inspectorate on appeal."
    movement: "evolving"

  - name: "Building Regulations"
    evolution: "Commodity"
    position: 0.82
    visibility: 0.18
    depends_on: []
    notes: "Approved Documents A-R. Commodity in the regulatory sense: fully codified, audited, predictable."
    movement: "none"

  - name: "Building Inspection / QA"
    evolution: "Product"
    position: 0.70
    visibility: 0.45
    depends_on: ["Building Regulations", "Certification (CSCS, Gas Safe, NICEIC)"]
    notes: "LABC + Approved Inspectors (AIs). Post-Grenfell, Building Safety Regulator covers HRRB. Process is maturing toward commodity."
    movement: "accelerating"

  # === Delivery / site layer ===
  - name: "Main Contractor Delivery"
    evolution: "Product"
    position: 0.55
    visibility: 0.55
    depends_on:
      - "Project Management"
      - "Site Works (Bespoke Build)"
      - "Modular / Volumetric Construction"
      - "Architectural Design"
      - "Integrated Distributors"
      - "Platform / Online Marketplaces"
    notes: "Tier-1 contractors (Balfour Beatty, Kier, Morgan Sindall). Project-based delivery, product-like but each project is a one-off."
    movement: "evolving"

  - name: "Project Management"
    evolution: "Product"
    position: 0.60
    visibility: 0.45
    depends_on: ["Blueprints / Drawings"]
    notes: "NEC4, PRINCE2, PMI. Well-productised. Tools (Procore, Asta) mature."
    movement: "evolving"

  - name: "Site Works (Bespoke Build)"
    evolution: "Custom-Built"
    position: 0.35
    visibility: 0.70
    depends_on:
      - "Skilled Trades (Bricklayers, Electricians, Plumbers)"
      - "Unskilled Site Labour"
      - "Heavy Plant & Machinery"
      - "Hand Tools / Small Plant"
      - "Traditional Builders' Merchants"
    notes: "THIS IS STILL BESPOKE CRAFT. Each site is a unique wet-trade project. Low productivity growth for 40+ years (ONS)."
    movement: "inertia"

  # === Labour ===
  - name: "Skilled Trades (Bricklayers, Electricians, Plumbers)"
    evolution: "Custom-Built"
    position: 0.40
    visibility: 0.65
    depends_on: ["Certification (CSCS, Gas Safe, NICEIC)", "Training / Apprenticeships"]
    notes: "Acute shortage post-Brexit + ageing workforce. Master-craft skill, slow to reproduce."
    movement: "inertia"

  - name: "Unskilled Site Labour"
    evolution: "Product"
    position: 0.60
    visibility: 0.25
    depends_on: []
    notes: "Gang-labour, self-employed (CIS). Heavily EU/migrant pre-2020; tighter post-Brexit."
    movement: "evolving"

  - name: "Certification (CSCS, Gas Safe, NICEIC)"
    evolution: "Commodity"
    position: 0.80
    visibility: 0.18
    depends_on: []
    notes: "Scheme-based certification is standardised and audited. Commodity."
    movement: "none"

  - name: "Training / Apprenticeships"
    evolution: "Custom-Built"
    position: 0.45
    visibility: 0.55
    depends_on: ["Critical National Infrastructure (Skilled Labour Supply)"]
    notes: "T-Levels, Construction Industry Training Board levy. Capacity limited; long lead time."
    movement: "evolving"

  # === Emerging modes ===
  - name: "Modular / Volumetric Construction"
    evolution: "Custom-Built"
    position: 0.45
    visibility: 0.60
    depends_on:
      - "Prefabricated Panels"
      - "Factory-Mode Housing (MMC)"
      - "Test-Driven / Digital-Twin Methods"
    notes: "Ilke, TopHat, Vistry's Modern Methods. Still fragile (L&G Modular closed in 2023). Cat 1 MMC."
    movement: "accelerating"

  - name: "Prefabricated Panels"
    evolution: "Custom-Built"
    position: 0.45
    visibility: 0.45
    depends_on: ["Component Manufacture (Windows, Doors, Fittings)"]
    notes: "Timber-frame, SIPs. Cat 2 MMC. More mature than volumetric."
    movement: "accelerating"

  - name: "Factory-Mode Housing (MMC)"
    evolution: "Custom-Built"
    position: 0.35
    visibility: 0.70
    depends_on:
      - "Component Manufacture (Windows, Doors, Fittings)"
      - "Prefabricated Panels"
    notes: "Whole-house factory assembly. High capex, utilisation-sensitive. Evolving but fragile."
    movement: "accelerating"

  - name: "Test-Driven / Digital-Twin Methods"
    evolution: "Genesis"
    position: 0.20
    visibility: 0.82
    depends_on: ["Building Information Modelling (BIM)"]
    notes: "Sensor-instrumented, validated digital twin of the building for predictive QA. Rare in housing; early in commercial."
    movement: "evolving"

  # === Design / blueprint layer ===
  - name: "Architectural Design"
    evolution: "Product"
    position: 0.55
    visibility: 0.45
    depends_on:
      - "Structural Engineering"
      - "Blueprints / Drawings"
      - "Building Information Modelling (BIM)"
      - "Novel Materials (Cross-Laminated Timber, Low-Carbon Cement)"
      - "Substitutable Materials (Hempcrete, Bio-Based)"
    notes: "RIBA stages. Productised (practice + CAD tools)."
    movement: "evolving"

  - name: "Structural Engineering"
    evolution: "Product"
    position: 0.60
    visibility: 0.42
    depends_on: ["Blueprints / Drawings"]
    notes: "Chartered engineers (IStructE). Tooling is productised."
    movement: "evolving"

  - name: "Blueprints / Drawings"
    evolution: "Product"
    position: 0.65
    visibility: 0.35
    depends_on: []
    notes: "AutoCAD / Revit outputs. Commoditising as BIM replaces 2D paper."
    movement: "evolving"

  - name: "Building Information Modelling (BIM)"
    evolution: "Product"
    position: 0.60
    visibility: 0.40
    depends_on: []
    notes: "BIM Level 2 mandated on UK public projects since 2016. Product-stage, standardising to commodity."
    movement: "evolving"

  # === Distribution ===
  - name: "Traditional Builders' Merchants"
    evolution: "Commodity"
    position: 0.78
    visibility: 0.28
    depends_on:
      - "Component Manufacture (Windows, Doors, Fittings)"
      - "Cement / Concrete Production"
      - "Road Logistics / Haulage"
    notes: "Travis Perkins, Jewson, Selco. High-street utility of construction. Commodity."
    movement: "none"

  - name: "Integrated Distributors"
    evolution: "Product"
    position: 0.55
    visibility: 0.45
    depends_on:
      - "Component Manufacture (Windows, Doors, Fittings)"
      - "Steel Production"
      - "Road Logistics / Haulage"
    notes: "One-stop-shop + logistics + installation. Building Materials Nation, Grafton. Product stage."
    movement: "evolving"

  - name: "Platform / Online Marketplaces"
    evolution: "Custom-Built"
    position: 0.42
    visibility: 0.58
    depends_on:
      - "Component Manufacture (Windows, Doors, Fittings)"
      - "Warehousing"
      - "Road Logistics / Haulage"
    notes: "IronmongeryDirect, Materials Market, Kubix. Still emerging, fragmentation-limited network effects."
    movement: "accelerating"

  # === Manufacture ===
  - name: "Component Manufacture (Windows, Doors, Fittings)"
    evolution: "Commodity"
    position: 0.72
    visibility: 0.30
    depends_on:
      - "Raw Materials (Aggregate, Timber, Steel Feedstock)"
      - "Recycled Materials"
      - "Novel Materials (Cross-Laminated Timber, Low-Carbon Cement)"
    notes: "Fenestration, ironmongery, fittings. Standardised product output."
    movement: "evolving"

  - name: "Cement / Concrete Production"
    evolution: "Commodity"
    position: 0.85
    visibility: 0.15
    depends_on: ["Raw Materials (Aggregate, Timber, Steel Feedstock)"]
    notes: "Cemex, Tarmac, Hanson. Pure commodity; under carbon-price pressure."
    movement: "none"

  - name: "Steel Production"
    evolution: "Commodity"
    position: 0.82
    visibility: 0.18
    depends_on:
      - "Raw Materials (Aggregate, Timber, Steel Feedstock)"
      - "Recycled Materials"
    notes: "British Steel, Tata. Commodity with carbon / energy-price exposure."
    movement: "none"

  # === Materials ===
  - name: "Raw Materials (Aggregate, Timber, Steel Feedstock)"
    evolution: "Commodity"
    position: 0.88
    visibility: 0.12
    depends_on: ["Port / Import Logistics", "Material Supply Chain Visibility"]
    notes: "UK ~60% timber import dependency. Global commodity."
    movement: "none"

  - name: "Recycled Materials"
    evolution: "Product"
    position: 0.55
    visibility: 0.45
    depends_on: []
    notes: "Steel recycling mature; aggregate/plasterboard growing; timber emerging. Product-stage."
    movement: "evolving"

  - name: "Novel Materials (Cross-Laminated Timber, Low-Carbon Cement)"
    evolution: "Custom-Built"
    position: 0.30
    visibility: 0.78
    depends_on: []
    notes: "CLT in mid-rise, geopolymer cement, hempcrete. Emerging; regulatory headwinds post-Grenfell."
    movement: "accelerating"

  - name: "Substitutable Materials (Hempcrete, Bio-Based)"
    evolution: "Genesis"
    position: 0.20
    visibility: 0.85
    depends_on: []
    notes: "Bio-based, carbon-negative. R&D + first-commercial-projects stage."
    movement: "evolving"

  # === Equipment / machinery ===
  - name: "Heavy Plant & Machinery"
    evolution: "Commodity"
    position: 0.78
    visibility: 0.30
    depends_on: []
    notes: "Excavators, cranes, telehandlers. Hire-first model (Sunbelt, A-Plant). Commodity."
    movement: "none"

  - name: "Hand Tools / Small Plant"
    evolution: "Commodity"
    position: 0.88
    visibility: 0.15
    depends_on: []
    notes: "Pure commodity. Screwfix / Toolstation."
    movement: "none"

  # === Logistics ===
  - name: "Road Logistics / Haulage"
    evolution: "Commodity"
    position: 0.88
    visibility: 0.12
    depends_on: []
    notes: "HGV haulage for materials delivery. Post-Brexit driver shortages."
    movement: "none"

  - name: "Port / Import Logistics"
    evolution: "Commodity"
    position: 0.82
    visibility: 0.20
    depends_on: ["Road Logistics / Haulage"]
    notes: "Felixstowe, London Gateway. Commodity."
    movement: "none"

  - name: "Warehousing"
    evolution: "Commodity"
    position: 0.78
    visibility: 0.22
    depends_on: ["Road Logistics / Haulage"]
    notes: "3PL / builders'-merchant regional DCs."
    movement: "none"

  # === Supply-chain resilience / CNI ===
  - name: "Material Supply Chain Visibility"
    evolution: "Custom-Built"
    position: 0.30
    visibility: 0.70
    depends_on: ["Critical National Infrastructure (Skilled Labour Supply)"]
    notes: "Post-Brexit, post-COVID, post-Ukraine: material-traceability is a growing concern. Custom tools, no standard."
    movement: "accelerating"

  - name: "Critical National Infrastructure (Skilled Labour Supply)"
    evolution: "Custom-Built"
    position: 0.25
    visibility: 0.75
    depends_on: []
    notes: "Skilled-trade shortage is a CNI-grade risk: housing targets unachievable without it. Local supply of skilled labour = explicit scenario call-out."
    movement: "inertia"
```

## Analysis

### What is still bespoke craft (left of centre)

| Component | Stage | Why bespoke |
|---|---|---|
| Site Works (wet trades) | Custom-Built (0.35) | Each site is a one-off. Bricklaying productivity is essentially unchanged since 1970. |
| Skilled Trades | Custom-Built (0.40) | Master-craft, slow to reproduce. Post-Brexit shortage. |
| Training / Apprenticeships | Custom-Built (0.45) | Slow throughput via CITB levy + T-Levels. |
| Modular / Factory-Mode / Prefab | Custom-Built (0.35-0.45) | Technically feasible but commercially fragile; L&G Modular closed 2023. |
| Novel / Substitutable Materials | Genesis-Custom (0.20-0.30) | CLT, hempcrete, low-carbon cement still early. |
| Test-Driven / Digital-Twin | Genesis (0.20) | Rare in housing; early in commercial/infrastructure. |
| Material Supply Chain Visibility | Custom-Built (0.30) | Post-COVID / post-Brexit concern; no standard tooling. |
| Critical National Infrastructure - Skilled Labour | Custom-Built (0.25) | Strategic shortage; policy-level problem. |

### What is ready to industrialise (crossing to product/commodity)

| Component | Current Stage | Direction |
|---|---|---|
| Main Contractor Delivery | Product (0.55) | Productising via digital-PM + MMC. |
| Architectural Design / BIM | Product (0.55-0.60) | BIM Level 2 mandated; standardising. |
| Building Inspection / QA | Product (0.70) | Accelerating post-Building Safety Act 2022. |
| Platform / Online Marketplaces | Custom (0.42) -> Product | Disrupting traditional merchants. |
| Integrated Distributors | Product (0.55) | Network effects emerging. |
| Recycled Materials | Product (0.55) | Driven by carbon targets and regulation. |

### Already commodity (right of map)

Building Regulations (rules), Certification schemes, Traditional Builders' Merchants, Component Manufacture, Cement/Concrete, Steel, Raw Materials, Heavy Plant, Hand Tools, Road Logistics, Ports, Warehousing.

```yaml
opportunities:
  - "Industrialise site works: MMC / factory-mode / modular is the productivity lever — move Site Works from Custom-Built to Product by shifting work upstream into the factory."
  - "Platform-distribution: Platform / Online Marketplaces can leapfrog traditional merchants if they solve credit + trade-relationship dynamics."
  - "Digital-twin + test-driven QA: pre-commodity Genesis — early mover advantage on HRRB compliance post-Building Safety Act."
  - "Novel materials (CLT, low-carbon cement): Genesis-to-Custom bet aligned with carbon policy."
  - "Training / apprenticeship capacity: CITB levy reform + factory-mode relaxes the skilled-trade bottleneck."

threats:
  - "Skilled-labour shortage (CNI-grade): will cap housing output regardless of other moves — strategic national risk."
  - "Material cost shocks: 2022 inflation already showed raw-materials + haulage are fragile in global disruption."
  - "Post-Grenfell regulation uncertainty for novel materials (cladding + timber in mid-rise face inertia)."
  - "Factory-mode fragility: L&G Modular, Urban Splash House closed 2022-23 — capex + utilisation model is unforgiving."
  - "Planning system inertia: slow LPA throughput constrains everything downstream."

inertia_points:
  - component: "Site Works (Bespoke Build)"
    reason: "40-year productivity flatline; skilled-trade culture + site-based contracting."
  - component: "Skilled Trades"
    reason: "Master-craft model + Brexit-induced supply shock; ageing workforce."
  - component: "Traditional Builders' Merchants"
    reason: "Incumbent relationships + trade-credit model resist platform disruption."
  - component: "Building Regulations (for novel materials)"
    reason: "Post-Grenfell, regulators are defensive around combustible materials in mid-rise."

recommendations:
  immediate:
    - "For a government actor: fund CITB expansion + T-Levels capacity — skilled-labour CNI is the binding constraint."
    - "For a Tier-1 contractor: invest in MMC Cat-2 (panels) before Cat-1 (volumetric); lower capex risk, same productivity gain."
    - "For a materials business: RMC/cement to invest in low-carbon alternatives before carbon price forces it."
  short_term:
    - "Mandate BIM Level 2/3 on all publicly-funded housing — standardisation drives rightward evolution."
    - "Digital-twin QA pilots on HRRB — Building Safety Regulator will reward evidence-based assurance."
    - "Platform-marketplace entrants should partner with haulage + small-merchant credit, not bypass them."
  long_term:
    - "Industrialise housing output — treat a home as a product (factory-built, site-assembled), not a project."
    - "Shift skilled-trade training to factory-technician pathways — re-skills the CNI-grade labour bottleneck."
    - "Standardise material-supply traceability (post-Brexit resilience + carbon-reporting driver)."

climatic_patterns:
  - "Everything evolves (rightward): all MMC components are mid-transition."
  - "Efficiency enables innovation: commodity merchants + commodity plant/haulage enable novel-material plays."
  - "Characteristics change across evolution: factory-mode needs Town Planners (volume ops), not Pioneers — this is why L&G Modular failed."
  - "Peace / War / Wonder: housing is in 'War' (product-stage competition between MMC and traditional) — expect shakeout."
  - "Co-evolution of practice: factory-mode demands new QA practice (test-driven / digital-twin)."

gameplay_patterns:
  - play: "Industrialise (Commoditise)"
    where: "Main Contractor Delivery + Site Works"
    rationale: "Classic commoditisation play — drive the industrialisation of housebuilding via MMC."
  - play: "Tower and Moat"
    where: "Integrated Distributors over Traditional Merchants"
    rationale: "Build the tower (merchant network) + moat (logistics + trade credit)."
  - play: "Open Source / Open Standard"
    where: "BIM / Digital-Twin"
    rationale: "Standardise the digital fabric to commoditise it; UK public-sector BIM mandate is example."
  - play: "Sensing / Weak Signal"
    where: "Novel Materials / Test-Driven QA"
    rationale: "Early-stage bets with high optionality under carbon + Building Safety Act pressure."

doctrine_weaknesses:
  - "Think small (no): UK construction is fragmented into 100k+ SMEs — hard to industrialise."
  - "Use a common language (partial): BIM mandate helps but site-practice is still tribal."
  - "Know your users (weak): mortgage companies + building-control + citizens have divergent user-journeys."
  - "Pioneers/Settlers/Town-Planners (mismatch): factory-mode failures (L&G) reflect Pioneer/Settler talent running a Planner business."
```

## Summary: bespoke vs. industrialisable

**Still bespoke craft (left of map):** on-site wet trades, skilled-trade labour, bespoke site-works, training pipeline, novel materials, digital-twin QA, material-supply visibility, and the CNI-grade skilled-labour supply itself.

**Ready to industrialise (mid-map, moving right):** MMC (modular / prefab / factory-mode), BIM-driven design, integrated distributors, platform marketplaces, recycled materials, and QA / building-inspection processes.

**Already commodity (right of map):** building regulations, certification schemes, traditional merchants, component manufacture, cement/concrete, steel, raw materials, heavy plant, hand tools, and logistics.

The most strategically important observation is that the binding constraint on UK housing output in March 2023 is not materials, not regulations, not capital — it is the **skilled-labour CNI problem** on the far left of the map. Every rightward-industrialisation move (MMC, platform distribution, digital-twin QA) is ultimately a play to reduce the system's dependence on this scarce, slow-to-reproduce resource.
