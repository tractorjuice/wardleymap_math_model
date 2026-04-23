# Transportation Logistics Landscape — Wardley Map

**Anchor:** Goods delivered to the public, on time and on spec, across city and rural topology.
**Scope:** End-to-end goods flow — producers through commerce channels, fulfilment plumbing, vehicles and power, information, skills, regulation, and the sovereignty frame.
**Author:** arc-kit wardley-mapping skill
**Date:** 2026-04-22
**Version:** 1.0

---

## 1. Context gathered (Step 1)

Arc-kit Step 1 asks for anchor + scope + strategic context. The scenario is rich enough that I inferred answers rather than pausing for AskUserQuestion:

| Question | Working answer |
|---|---|
| Primary user | The public / consumers receiving goods; with producers, society, and government as cross-cutting actors the scenario explicitly names. |
| User need | Reliable delivery of goods from producers to the public across city and rural topology. |
| Scope | Whole transport-logistics landscape — commerce, fulfilment, vehicles, power, information, skills, regulation, sovereignty. |
| Primary goal | Identify where the chain is commoditised utility vs where automated delivery and sovereignty will force evolution. |
| Industry | Transport & logistics, 2026 — post-HGV crisis, mid electric / autonomous transition, active CNI/sovereignty debate. |
| Depth | Standard-to-deep map (~35 components with movement + inertia + climatic/gameplay cross-reference). |

---

## 2. Value chain (Step 2)

Working backwards from the anchor through the layers the scenario called out:

- **Actors / anchors:** The Public, Consumers, Producers, Society, Government.
- **Needs / outcomes:** Goods Delivered to the Public, Awareness of Supply Chain, Territorial / CNI Sovereignty, Logistics Regulation.
- **Commerce front-end:** Shops, E-commerce, Real-time Stock Visibility.
- **Fulfilment plumbing:** Last Mile Delivery, Long Haul Transport, Logistics Hubs, Warehouses, Storage, Delivery Operations.
- **Topology:** Cities, Rural Areas.
- **Vehicle & power layer:** Trucks (HGV), Autotrucks, Delivery Drones, Scouts, Automated Delivery (robots / lockers), Fossil-fuel Powertrain, Electric Powertrain.
- **Information layer:** Logistics Data, Traffic Data, Telematics.
- **Skills:** HGV Driver Skills, Logistics Workforce.
- **Commodity underlays:** Roads, Electricity Grid, Fuel Supply, Mobile Networks, Cloud / Data Storage.

---

## 3. Visual map (Steps 3 + 4)

```text
Title: Transportation Logistics Landscape
Anchor: Goods Delivered to the Public
Date: 2026-04-22

                 Genesis        Custom        Product        Commodity
                    │              │              │              │
Visible         ┌───┼──────────────┼──────────────┼──────────────┼───┐
                │   │              │              │              │   │
 Anchors        │   │ Gov  Soc     │              │    Producers ●   │
                │   │  ●    ●      │              │    Consumers ●   │
                │   │              │              │    The Public ●  │
                │   │              │              │        │         │
                │   │ Sovereignty ×│              │ Regulation ●→    │
                │   │ Awareness ×→ │              │              │   │
                │   │              │              │ Goods Delivered ●│
                │   │              │              │                  │
                │   │              │              │ Shops ●× E-com ● │
                │   │              │ Real-time    │                  │
                │   │              │ Stock ●→     │                  │
                │   │              │              │ Long Haul ●      │
                │   │              │ Last Mile ●  │                  │
                │   │              │ Delivery Ops●│ Warehouses ●     │
                │   │              │              │ Logistics Hubs ● │
                │   │              │              │ Storage ●        │
                │   │              │              │ Cities ●         │
                │   │              │              │ Rural Areas ●    │
                │   │              │ Electric     │ Trucks (HGV) ●   │
                │   │              │ Powertrain ●→│ Fossil Power ●×  │
                │   │ Autotrucks ●→│              │                  │
                │   │ Drones ●→    │              │                  │
                │   │ Scouts ●→    │              │                  │
                │   │ Auto-deliv ●→│              │                  │
                │   │              │ Logistics    │ Traffic Data ●   │
                │   │              │ Data ●       │ Telematics ●→    │
                │   │              │ HGV Skills ×│ Workforce ●       │
                │   │              │              │ Roads ●          │
Hidden          │   │              │              │ Elec Grid ●      │
                │   │              │              │ Fuel Supply ●×   │
                │   │              │              │ Mobile Nets ●    │
                │   │              │              │ Cloud/Storage ●  │
                └───┴──────────────────────────────────────────────┘

Legend: ● current position, → evolving, × inertia
```

---

## 4. Structured output

```yaml
wardley_map:
  metadata:
    title: "Transportation Logistics Landscape"
    author: "arc-kit wardley-mapping skill"
    date: "2026-04-22"
    version: "1.0"
    scope: "Producers to public: commerce, fulfilment, vehicles/power, information, skills, regulation, sovereignty."

  anchor:
    user: "The public / consumers"
    need: "Goods delivered on time and on spec, city and rural"

  components:
    - name: "The Public"
      evolution: "Commodity"
      position: 0.60
      visibility: 0.96
      depends_on: ["Goods Delivered to the Public"]
      notes: "Top-level actor; the demand-side end of the chain."
      movement: "none"

    - name: "Consumers"
      evolution: "Product"
      position: 0.58
      visibility: 0.94
      depends_on: ["Goods Delivered to the Public", "Shops", "E-commerce"]
      notes: "Active purchasing actor."
      movement: "none"

    - name: "Producers"
      evolution: "Custom"
      position: 0.30
      visibility: 0.93
      depends_on: ["Long Haul Transport", "Logistics Hubs"]
      notes: "Anchor on the supply side; they originate goods flow."
      movement: "none"

    - name: "Society"
      evolution: "Custom"
      position: 0.35
      visibility: 0.92
      depends_on: ["Awareness of Supply Chain", "Territorial / CNI Sovereignty"]
      notes: "Passive but increasingly active actor post-2021 shocks."
      movement: "none"

    - name: "Government"
      evolution: "Custom"
      position: 0.25
      visibility: 0.91
      depends_on: ["Logistics Regulation", "Territorial / CNI Sovereignty"]
      notes: "Regulator and CNI custodian; actively intervening."
      movement: "none"

    - name: "Goods Delivered to the Public"
      evolution: "Product"
      position: 0.72
      visibility: 0.88
      depends_on: ["Shops", "E-commerce", "Last Mile Delivery", "Real-time Stock Visibility"]
      notes: "The measurable user need; the outcome being mapped."
      movement: "none"

    - name: "Awareness of Supply Chain"
      evolution: "Genesis → Custom"
      position: 0.18
      visibility: 0.86
      depends_on: ["Logistics Data", "Telematics", "Real-time Stock Visibility"]
      notes: "Post-COVID / Suez / Brexit. n-tier visibility for the public and government is genesis-stage; tooling exists for enterprises but not for society-at-large."
      movement: "accelerating"

    - name: "Territorial / CNI Sovereignty"
      evolution: "Genesis → Custom"
      position: 0.15
      visibility: 0.84
      depends_on: ["Long Haul Transport", "Logistics Hubs", "Fuel Supply", "Mobile Networks"]
      notes: "Sovereignty over logistics as CNI is a live 2024-2026 policy debate; no settled playbook."
      movement: "accelerating"

    - name: "Logistics Regulation"
      evolution: "Product"
      position: 0.50
      visibility: 0.83
      depends_on: ["HGV Driver Skills", "Autotrucks (autonomous HGV)", "Delivery Drones", "Automated Delivery (robots/lockers)"]
      notes: "HGV/driver-hours regulation is mature product; autonomy and drone regulation still forming. Will evolve rightward but will also itself be reshaped by automation."
      movement: "evolving"

    - name: "Shops"
      evolution: "Commodity"
      position: 0.82
      visibility: 0.78
      depends_on: ["Warehouses", "Last Mile Delivery", "Real-time Stock Visibility"]
      notes: "Physical retail as a channel is commoditised. Inertia from leases and estate footprint."
      movement: "inertia"

    - name: "E-commerce"
      evolution: "Commodity"
      position: 0.78
      visibility: 0.76
      depends_on: ["Warehouses", "Last Mile Delivery", "Delivery Operations", "Real-time Stock Visibility"]
      notes: "Shopify/Amazon-style platforms are commodity; the channel itself is utility."
      movement: "none"

    - name: "Real-time Stock Visibility"
      evolution: "Product"
      position: 0.45
      visibility: 0.74
      depends_on: ["Logistics Data", "Telematics"]
      notes: "Vendor products exist (Manhattan, Blue Yonder, Shopify-native) but seamless cross-actor real-time visibility is still product-stage; consumer-facing ETAs are pushing it rightward."
      movement: "evolving"

    - name: "Last Mile Delivery"
      evolution: "Product"
      position: 0.70
      visibility: 0.66
      depends_on: ["Delivery Operations", "Automated Delivery (robots/lockers)", "Delivery Drones", "Cities", "Rural Areas"]
      notes: "Known pattern with competing solutions; still the most costly and most automatable portion of the chain."
      movement: "none"

    - name: "Long Haul Transport"
      evolution: "Commodity"
      position: 0.84
      visibility: 0.64
      depends_on: ["Trucks (HGV)", "Autotrucks (autonomous HGV)", "Logistics Hubs", "Roads"]
      notes: "Utility-priced per pallet-km; multi-provider 3PL market."
      movement: "none"

    - name: "Logistics Hubs"
      evolution: "Commodity"
      position: 0.75
      visibility: 0.60
      depends_on: ["Warehouses", "Storage", "Cities"]
      notes: "DC/cross-dock real estate is utility-grade; some sovereignty-sensitive hubs (ports, airports) carry inertia."
      movement: "none"

    - name: "Warehouses"
      evolution: "Commodity"
      position: 0.82
      visibility: 0.58
      depends_on: ["Storage"]
      notes: "3PL market is mature; WMS is Product stage, buildings themselves commodity."
      movement: "none"

    - name: "Storage"
      evolution: "Commodity"
      position: 0.88
      visibility: 0.56
      depends_on: []
      notes: "Utility — pallet-days are a traded commodity."
      movement: "none"

    - name: "Delivery Operations"
      evolution: "Product"
      position: 0.68
      visibility: 0.62
      depends_on: ["Trucks (HGV)", "HGV Driver Skills", "Logistics Workforce", "Telematics"]
      notes: "Run-the-depot operations are productised (TMS, routing suites); labour-bound."
      movement: "none"

    - name: "Cities"
      evolution: "Commodity"
      position: 0.92
      visibility: 0.50
      depends_on: ["Roads"]
      notes: "Topology — established urban networks. Utility in mapping terms; the substrate delivery runs over."
      movement: "none"

    - name: "Rural Areas"
      evolution: "Commodity"
      position: 0.85
      visibility: 0.48
      depends_on: ["Roads"]
      notes: "Topology — sparse networks, rural last-mile is a persistent cost/service gap."
      movement: "none"

    - name: "Trucks (HGV)"
      evolution: "Commodity"
      position: 0.86
      visibility: 0.42
      depends_on: ["Fossil-fuel Powertrain", "Electric Powertrain"]
      notes: "Diesel HGV is utility-priced; electric HGV is at product-stage on the horizon."
      movement: "none"

    - name: "Fossil-fuel Powertrain"
      evolution: "Commodity"
      position: 0.92
      visibility: 0.40
      depends_on: ["Fuel Supply"]
      notes: "Commoditised. Carries inertia from OEM/fleet lifecycles (15-20 years) blocking rapid transition."
      movement: "inertia"

    - name: "Electric Powertrain"
      evolution: "Product"
      position: 0.50
      visibility: 0.38
      depends_on: ["Electricity Grid"]
      notes: "Multiple vendors (Volvo, Mercedes, Tesla Semi, Scania), still productised, not yet commodity for heavy truck/drone sector. Moving right fast."
      movement: "evolving"

    - name: "Autotrucks (autonomous HGV)"
      evolution: "Genesis → Custom"
      position: 0.18
      visibility: 0.36
      depends_on: ["Electric Powertrain", "Telematics", "Logistics Data"]
      notes: "Scenario-specified pressure point. Level-4 HGV autonomy operates in narrow corridors (Embark, Aurora, Waymo Via) — no commodity solution yet."
      movement: "accelerating"

    - name: "Delivery Drones"
      evolution: "Genesis"
      position: 0.14
      visibility: 0.34
      depends_on: ["Electric Powertrain", "Telematics"]
      notes: "Zipline (medical) shows production; general parcel drone is still genesis at scale — regulatory and urban-airspace constraints bind."
      movement: "accelerating"

    - name: "Scouts (route/advance vehicles)"
      evolution: "Genesis → Custom"
      position: 0.22
      visibility: 0.32
      depends_on: ["Telematics", "Electric Powertrain"]
      notes: "Scout UGVs that clear or advance routes (military-adjacent, also yard/warehouse). Still in pilots."
      movement: "accelerating"

    - name: "Automated Delivery (robots/lockers)"
      evolution: "Genesis → Custom"
      position: 0.28
      visibility: 0.30
      depends_on: ["Electric Powertrain", "Cities"]
      notes: "Sidewalk robots (Starship) and lockers (Amazon Hub, InPost) exist. Still early commodity for lockers, genesis-to-custom for autonomous sidewalk bots."
      movement: "accelerating"

    - name: "Logistics Data"
      evolution: "Product"
      position: 0.60
      visibility: 0.28
      depends_on: ["Cloud / Data Storage"]
      notes: "EDI, API feeds, TMS data are productised."
      movement: "none"

    - name: "Traffic Data"
      evolution: "Product → Commodity"
      position: 0.72
      visibility: 0.26
      depends_on: ["Mobile Networks", "Cloud / Data Storage"]
      notes: "Google/HERE/TomTom-style feeds — almost utility."
      movement: "none"

    - name: "Telematics"
      evolution: "Product"
      position: 0.68
      visibility: 0.24
      depends_on: ["Mobile Networks", "Cloud / Data Storage", "Traffic Data"]
      notes: "Geotab / Samsara / MiX productised market; consolidating toward commodity."
      movement: "evolving"

    - name: "HGV Driver Skills"
      evolution: "Product"
      position: 0.45
      visibility: 0.22
      depends_on: ["Logistics Workforce"]
      notes: "Licensed, trained skill — productised as a labour market. Carries strong inertia because shortage is structural (UK 2021-2024), demographic and training-constrained."
      movement: "inertia"

    - name: "Logistics Workforce"
      evolution: "Product"
      position: 0.55
      visibility: 0.20
      depends_on: []
      notes: "Labour market exists but tight. Mid-transition as automation threatens/replaces parts."
      movement: "evolving"

    - name: "Roads"
      evolution: "Commodity"
      position: 0.95
      visibility: 0.14
      depends_on: []
      notes: "Public utility. The substrate of the chain."
      movement: "none"

    - name: "Electricity Grid"
      evolution: "Commodity"
      position: 0.94
      visibility: 0.12
      depends_on: []
      notes: "Utility; constrained by generation mix but commoditised as a delivered service."
      movement: "none"

    - name: "Fuel Supply"
      evolution: "Commodity"
      position: 0.93
      visibility: 0.10
      depends_on: []
      notes: "Utility. Inertia from global tax, pipeline, and refining infrastructure that anchors fossil power."
      movement: "inertia"

    - name: "Mobile Networks"
      evolution: "Commodity"
      position: 0.92
      visibility: 0.08
      depends_on: []
      notes: "Utility — 4G/5G/LEO sat backhaul for telematics."
      movement: "none"

    - name: "Cloud / Data Storage"
      evolution: "Commodity"
      position: 0.96
      visibility: 0.06
      depends_on: []
      notes: "Utility."
      movement: "none"

  analysis:
    opportunities:
      - "Industrialise Long Haul, Warehousing, Storage, Logistics Hubs, Traffic Data — treat as utility and stop over-investing. Buy, don't build."
      - "Invest pioneers into Autotrucks, Drones, Automated Delivery, Scouts — these are genesis/custom and will reshape last-mile economics when they cross the chasm."
      - "Build the public-facing Awareness of Supply Chain layer as a differentiator — there's no commodity solution for society-level n-tier visibility yet; government and large retailers can define the data schema."
      - "Shift fleet CapEx from fossil to electric on a schedule tuned to residual values — electric powertrain is mid-product and will commoditise within 5-7 years."
      - "Treat Real-time Stock Visibility as a near-product — productise an internal view and expose APIs to consumers; this sits just below E-commerce and moves customer trust."

    threats:
      - "HGV driver shortage is structural inertia — automation is a long bet, so short-term doctrine must be workforce + conditions + training. Wage compression will not fix it."
      - "Sovereignty/CNI regulation will arrive unevenly and fragment route planning (e.g. bans on foreign autotruck OEMs on national strategic corridors); builders of long-haul autonomy face multi-jurisdiction regulatory complexity."
      - "Fossil-fuel powertrain inertia and fleet refresh cycles mean the transition is slow in HGV — don't over-promise electric first-mile timelines."
      - "Regulation for drones and autonomous delivery lags the technology — pilots stall at demonstration scale because liability, airspace, and insurance frameworks are genesis-stage."
      - "Rural last-mile remains a cost sink and a political pressure point; any 'full automation' roadmap that ignores rural topology is fragile."

    inertia_points:
      - component: "HGV Driver Skills"
        reason: "Licensing regime, demographics, pay/conditions — not quickly reshapable. 18-36 month training cycle."
      - component: "Fossil-fuel Powertrain"
        reason: "15-20 year HGV lifecycle; sunk capex in fleets, fuelling infrastructure, OEM tooling."
      - component: "Shops"
        reason: "Physical retail estate (leases, staff contracts) resists channel shift even as consumers migrate online."
      - component: "Fuel Supply"
        reason: "Entrenched distribution (pipelines, forecourts), tax regimes, and geopolitical dependency. Very slow to commoditise away."

  recommendations:
    immediate:
      - "Stand up a 'supply-chain awareness' capability: n-tier supplier mapping + public-facing visibility pilot. Treat as genesis/custom — put pioneers on it, not planners."
      - "Consolidate Telematics / Traffic Data / Logistics Data procurement onto utility-priced platforms; redirect saved headcount to autonomy/drone pilots."
      - "Map fleet CapEx to residual-value curves for fossil vs electric vs autonomous-ready; freeze new diesel orders past 2027."
    short_term:
      - "Run a last-mile automation portfolio: 2-3 drone pilots (rural, medical-adjacent), 1-2 sidewalk-robot pilots (metro), locker rollout at scale. Treat lockers as the commoditisable backbone."
      - "Influence Logistics Regulation early — write the operating frameworks for autotrucks and drones before competitors do. Offensive regulatory play."
      - "Build an HGV-driver retention doctrine (training pipelines, apprenticeships, wage + conditions) to bridge to 2030-era partial autonomy."
    long_term:
      - "Productise the internal Supply Chain Awareness platform and expose it to government/society; this layer will commoditise in 5-10 years and early movers set the schema."
      - "Exit non-differentiating physical warehousing where DC lease cycles allow; partner with 3PL utilities."
      - "Treat CNI sovereignty as a first-class design constraint for long-haul: dual-source critical corridors, national-jurisdiction data residency for telematics, and sovereign cloud for logistics data."
```

---

## 5. Answer to the user's two headline questions

> **Where is logistics commoditised utility?**

Right-hand / high-position components (evolution ≥ 0.80) and the underlay: **Long Haul Transport (0.84), Warehouses (0.82), Logistics Hubs (0.75), Storage (0.88), Shops as a channel (0.82), E-commerce (0.78), Trucks/HGV (0.86), Fossil-fuel Powertrain (0.92), Traffic Data (0.72), Roads (0.95), Electricity Grid (0.94), Fuel Supply (0.93), Mobile Networks (0.92), Cloud/Data Storage (0.96).** Moving atoms at pallet-scale is a commodity market. The vehicles are commodity. The substrate (roads, fuel, grid, networks) is commodity. The visible commerce channels are commoditised. If you're running these in-house, you're paying a capability premium for utility-grade work.

> **Where will automated delivery or sovereignty concerns force it to evolve?**

Left-hand / low-position components with accelerating movement are where the next 5-10 years will be won or lost:

| Component | Current stage | Why it moves |
|---|---|---|
| Autotrucks (autonomous HGV) | Genesis → Custom | L4 corridor autonomy solves the HGV shortage; accelerated by labour scarcity. |
| Delivery Drones | Genesis | Rural / medical cases viable; general parcel awaits regulation + urban airspace. |
| Automated Delivery (robots/lockers) | Genesis → Custom | Lockers are already commoditising; sidewalk robots still early. |
| Scouts (route/advance vehicles) | Genesis → Custom | Yard/warehouse autonomy then route-advance in sovereignty-sensitive corridors. |
| Awareness of Supply Chain | Genesis → Custom | Society and government are becoming users; post-2020s shocks drive the pull. |
| Territorial / CNI Sovereignty | Genesis → Custom | No settled doctrine; nations are drafting frameworks live. |
| Electric Powertrain | Product | Vendor market exists; will commoditise within 5-7 years for medium/heavy haul. |
| Logistics Regulation | Product | Will restructure around autonomy + sovereignty constraints. |
| HGV Driver Skills | Product (with inertia) | Shrinking workforce forces automation at the top and training at the bottom. |

Strategic read: the industrial core of logistics is already utility; the **vehicle/power layer is mid-transition** (electric winning the race in the 5-7y window, autonomy the 10-15y window); and the **information + awareness + sovereignty layer is where the next durable moats sit** — they're genesis/custom now, and the players who productise them first set the standards.

---

## 6. Gameplay & climate cross-reference

**Climatic patterns in play (2026 UK/EU reading):**

- *Everything evolves* — Electric Powertrain, Telematics, Real-time Stock Visibility moving right; Autotrucks / Drones / Automated Delivery chasm-crossing.
- *Past success breeds inertia* — Fossil-fuel Powertrain, Shops, HGV Driver Skills, Fuel Supply.
- *Shocks happen* — COVID, Brexit (UK), Suez, Ukraine drive the Awareness and Sovereignty components upward on the agenda.
- *Efficiency enables innovation* — commoditised logistics underlay frees capital for automation pilots.
- *Peace / War / Wonder cycles* — logistics is entering a *war* phase on automation (autotrucks, drones, lockers competing for the last-mile).

**Applicable gameplays (from arc-kit references):**

- *Exploiting constraint* on HGV Driver Skills (training, automation investment).
- *Harvesting* in Long Haul / Warehousing / Storage / Traffic Data.
- *Pig in a poke / First Mover* on internal and public-facing Supply Chain Awareness platforms.
- *Raising barriers to entry* via regulation for autonomy (offensive lobbying before competitors define the frame).
- *Disruption (shifts to the right)* at the Electric Powertrain layer — early switchers win residuals.
- *Sensible accelerator* on drone regulation — government-backed pilots to unlock the commodity path.

**Doctrine weaknesses most logistics firms will exhibit here:**

- Weak *Know your users* — the public and government are users of the awareness layer too, not just buyers.
- Weak *Use appropriate methods* — applying lean-logistics doctrine to genesis-stage autonomy builds the wrong artefacts.
- Weak *Think small* — over-centralising telematics / stock visibility when federated / edge would match reality.
- Weak *Plan for constant evolution* — HGV-led operating model anchored to a labour pool that is shrinking fast.

---

## 7. Notes on limitations / method

- Generic UK/EU 2026 map; any real map should be per-firm (fleet mix specific, jurisdiction-specific, channel-mix specific).
- Positions are qualitative reads following the arc-kit `evolution-stages.md` rubric (Ubiquity × Certainty). A quantitative Ubiquity × Certainty scoring pass would tighten each within ±0.05.
- Movement arrows reflect 3-7 year expected drift, except for CNI/Sovereignty and Drones where regulation-led movement is much less predictable (could be 2y or 10y).
- Arc-kit Step 1 recommends AskUserQuestion; for this blind evaluation I inferred answers from the scenario text rather than pausing.
- OWM doesn't have a first-class inertia keyword, so inertia is recorded in the YAML `inertia_points` and as comments in `draft.owm`.
