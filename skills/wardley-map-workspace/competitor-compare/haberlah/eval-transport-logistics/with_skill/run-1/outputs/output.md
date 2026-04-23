# Wardley Map Analysis: Transportation Logistics Landscape

## Purpose

This map answers the question: **where in the transportation logistics
landscape is the activity a commoditised utility, and where will automated
delivery or sovereignty/CNI concerns force it to evolve?**

The user anchor is **The Public** (consumers as citizens), with secondary
anchors for **Producers** (who ship goods) and **Government** (who regulates
and guards sovereignty). Scope is national-to-regional freight and parcel
logistics end-to-end, from producer to doorstep.

## Map

### OWM Source

```wardley
title Transportation Logistics Landscape
style wardley

// Anchors
anchor The Public [0.97, 0.60]
anchor Producers [0.94, 0.48]
anchor Government [0.95, 0.32]

// Retail / commerce surface
component Shops [0.88, 0.80]
component E-commerce [0.86, 0.68]

// User-facing supply chain capabilities
component Delivery [0.80, 0.58]
component Real-Time Stock [0.74, 0.30]
component Supply Chain Awareness [0.78, 0.18]

// Core physical flow
component Last Mile [0.66, 0.48]
component Long Haul [0.60, 0.80]
component Logistics Hubs [0.54, 0.62]
component Warehouses & Storage [0.48, 0.82]

// Vehicle / power layer
component Trucks (HGV) [0.38, 0.80]
component Automated Delivery [0.34, 0.18]
component Drones & Scouts [0.30, 0.12]
component Powertrain (Fossil/Electric) [0.26, 0.60]

// Information layer
component Traffic & Telematics Data [0.42, 0.70]

// Topology
component Cities [0.22, 0.86]
component Rural Areas [0.20, 0.72]

// Enablers
component Regulation [0.14, 0.66]
component HGV Skills [0.44, 0.40] inertia
component Sovereignty (CNI/Territorial) [0.10, 0.24] inertia

// Links
The Public->Shops
The Public->E-commerce
The Public->Supply Chain Awareness
Producers->Long Haul
Producers->Warehouses & Storage
Government->Regulation
Government->Sovereignty (CNI/Territorial)

Shops->Delivery
Shops->Real-Time Stock
E-commerce->Delivery
E-commerce->Real-Time Stock

Delivery->Last Mile
Delivery->Long Haul
Last Mile->Logistics Hubs
Long Haul->Logistics Hubs
Logistics Hubs->Warehouses & Storage
Real-Time Stock->Traffic & Telematics Data
Supply Chain Awareness->Traffic & Telematics Data

Last Mile->Trucks (HGV)
Last Mile->Automated Delivery
Last Mile->Drones & Scouts
Long Haul->Trucks (HGV)
Long Haul->Automated Delivery
Automated Delivery->Drones & Scouts

Trucks (HGV)->Powertrain (Fossil/Electric)
Automated Delivery->Powertrain (Fossil/Electric)
Drones & Scouts->Powertrain (Fossil/Electric)

Trucks (HGV)->Traffic & Telematics Data
Automated Delivery->Traffic & Telematics Data

Last Mile->Cities
Last Mile->Rural Areas
Logistics Hubs->Cities

Trucks (HGV)->HGV Skills
Long Haul->HGV Skills
Long Haul->Regulation
Warehouses & Storage->Regulation
Logistics Hubs->Sovereignty (CNI/Territorial)
Warehouses & Storage->Sovereignty (CNI/Territorial)

// Evolution arrows
evolve Last Mile 0.72
evolve Automated Delivery 0.55
evolve Drones & Scouts 0.42
evolve Real-Time Stock 0.72
evolve Powertrain (Fossil/Electric) 0.82
evolve Traffic & Telematics Data 0.85
evolve Supply Chain Awareness 0.50
evolve Shops 0.90

// Build/buy/outsource guidance
build Automated Delivery
build Supply Chain Awareness
buy Traffic & Telematics Data
buy Real-Time Stock
buy Powertrain (Fossil/Electric)
outsource Long Haul
outsource Warehouses & Storage

// Annotations
annotation 1 [[0.48, 0.88]] Long-haul, warehousing, and shops behave as commoditised utility
annotation 2 [[0.32, 0.15]] Automated delivery / drones: Genesis/Custom-Built, poised to evolve
annotation 3 [[0.10, 0.24]] Sovereignty + CNI concerns are the main source of inertia
annotation 4 [[0.44, 0.40]] HGV skills shortage: Product-stage activity stuck behind a scarce resource
```

Paste the block above into [onlinewardleymaps.com](https://onlinewardleymaps.com/),
the VS Code extension, or the Obsidian plugin to render an editable map.

## Component Evolution Assessment

| Component | Stage | Position [vis, mat] | Rationale |
|---|---|---|---|
| The Public | Anchor | [0.97, 0.60] | End-user of the logistics system as consumer and citizen. |
| Producers | Anchor | [0.94, 0.48] | Secondary user: manufacturers/growers whose goods must move. |
| Government | Anchor | [0.95, 0.32] | Regulatory and sovereign actor, separate from end-consumers. |
| Shops | Commodity | [0.88, 0.80] | Retail is ubiquitous and commoditised; pure-play shops differ mainly on format, not existence. |
| E-commerce | Product | [0.86, 0.68] | Mature category with several dominant platforms (Amazon, Shopify, Tmall) and a long tail; still evolving toward utility as integrations standardise. |
| Delivery | Product | [0.80, 0.58] | Many competing vendors (UPS, FedEx, DPD, Evri, Amazon Logistics) with comparable service envelopes. |
| Real-Time Stock | Custom-Built | [0.74, 0.30] | Across the economy real-time inventory visibility is still patchy and bespoke; only leading retailers have it end-to-end. |
| Supply Chain Awareness | Custom-Built | [0.78, 0.18] | Public/shipper ability to know what is in the supply chain is emerging — driven by post-2020 disruption — but not yet a product. |
| Last Mile | Product | [0.66, 0.48] | Multiple established providers; economics still painful and innovation-heavy, so not yet Commodity. |
| Long Haul | Commodity | [0.60, 0.80] | Trunk road/rail/sea freight is near-utility — price-driven, standardised loading units, interchangeable carriers. |
| Logistics Hubs | Product | [0.54, 0.62] | Operated by professional 3PLs (DHL, Kuehne+Nagel, XPO); differentiation by location and automation level. |
| Warehouses & Storage | Commodity | [0.48, 0.82] | Square-footage of pallet storage is sold on spot markets (e.g., Stord, Flexe, Flock Freight) at transparent pricing. |
| Trucks (HGV) | Commodity | [0.38, 0.80] | Heavy trucks from a handful of global OEMs (Daimler, Volvo, Scania, Paccar) with stable specifications. |
| Automated Delivery | Custom-Built | [0.34, 0.18] | Emerging: Nuro, Starship, Amazon Scout pilots, etc. Few deployments, no standardised model yet. |
| Drones & Scouts | Genesis | [0.30, 0.12] | Active experimentation (Zipline, Wing, Amazon Prime Air). Limited routes, constant regulatory change, no stable market. |
| Powertrain (Fossil/Electric) | Product | [0.26, 0.60] | Diesel is commoditised; electric truck/van powertrain is a fast-moving Product stage (Tesla Semi, Volvo FH Electric, Volta, BYD). |
| Traffic & Telematics Data | Commodity | [0.42, 0.70] | Road data, weather, and telematics are available as utility APIs (HERE, TomTom, Geotab); consumers and fleets alike rely on them. |
| Cities | Commodity | [0.22, 0.86] | Urban topology is a stable given — pricing in congestion, ULEZ etc. |
| Rural Areas | Commodity | [0.20, 0.72] | Equally stable; the last-mile cost problem is structural, not novel. |
| Regulation | Product | [0.14, 0.66] | Mature regulatory apparatus (driver hours, vehicle standards, customs) but steadily evolving with electrification and autonomy rules. |
| HGV Skills | Product (with inertia) | [0.44, 0.40] | Training and licensing are a well-understood Product-stage activity, but acute structural shortages (UK, EU, US) resist commoditisation — hence inertia marker. |
| Sovereignty (CNI/Territorial) | Custom-Built (with inertia) | [0.10, 0.24] | Each jurisdiction defines what counts as Critical National Infrastructure differently; sovereignty requirements actively resist commoditisation of foreign providers — hence inertia marker. |

## Key Strategic Observations

1. **A clear "commodity belt" runs from long-haul through warehousing to
   shops.** Long Haul (0.80), Warehouses & Storage (0.82), Trucks (0.80),
   and Shops (0.80) all sit in the Commodity column. This is the core
   insight: *moving and storing boxes* has already been solved as utility.
   The money is not in operating those assets — it is in the information
   and automation layers sitting on top.

2. **Automated delivery is a tight Genesis/Custom-Built cluster in the
   lower-left.** Automated Delivery (0.18), Drones & Scouts (0.12), and
   Supply Chain Awareness (0.18) are all pre-Product. They are poised to
   sweep rightward over the next 5–10 years. Anyone building logistics
   strategy today needs a thesis for how their asset base will look when
   these cross into Product.

3. **The information layer outruns the physical layer.** Traffic &
   Telematics Data sits at Commodity (0.70) while the trucks that consume
   it are still dispatched by humans on legacy systems. This is a classic
   doctrine mismatch — using novel practices around a commodity input, or
   vice versa, creates friction.

4. **HGV Skills is a Product-stage bottleneck with genuine inertia.**
   Drivers can be trained (the activity exists as Product) but the market
   is chronically under-supplied. This creates a leftward pull on every
   Long Haul and Last Mile component that depends on it — exactly the
   shape the inertia marker is meant to capture.

5. **Sovereignty/CNI is the biggest source of inertia in the map.**
   Logistics Hubs and Warehouses & Storage *could* be outsourced to the
   lowest global bidder, but governments increasingly insist on
   in-territory infrastructure, domestic carriers, and vetted personnel.
   This pulls otherwise-commodity components back toward Custom-Built.

## Doctrine Check

- **User needs clearly identified**: Yes — The Public (buy things, know
  what is arriving, trust the chain), Producers (ship reliably), and
  Government (regulate, protect CNI) are all explicit anchors.
- **Unnecessary duplication**: Delivery and Last Mile partially overlap;
  the map treats Delivery as the user-facing capability and Last Mile as
  the underlying physical operation. This is intentional but worth
  revisiting if the audience finds it confusing.
- **Appropriate methods to evolution stage**: The map suggests
  Genesis/Custom components (Automated Delivery, Supply Chain Awareness)
  should be built in-house (marked `build`), Product components bought
  off-the-shelf (`buy`), and Commodity components outsourced
  (`outsource`). This aligns with Pioneers/Settlers/Town Planners
  doctrine.
- **Bias toward a single stage**: The map leans heavily Commodity-side;
  that is the honest truth of the industry, not a mapping error.
  Nevertheless, any strategy that only optimises the commodity belt will
  miss the incoming automation wave.

## Recommended Actions

1. **Build an in-house automation programme around Last Mile and
   Automated Delivery.** These are the two components whose rightward
   movement over the next 3–5 years will reshape landed cost more than
   any other. Waiting for products to arrive means buying from whoever
   crosses the Custom-Built → Product boundary first — you lose first-
   mover advantage *and* optionality.

2. **Treat Traffic & Telematics Data and Real-Time Stock as utility
   purchases, not custom builds.** Vendors exist; buy APIs, do not
   build them. Refuse vendor-lock propositions that look like bespoke
   "platforms".

3. **Invest in HGV Skills as a strategic workforce programme.** The
   inertia on this node is the single biggest risk to Long Haul
   reliability. Treat driver training the way airlines treat pilot
   training — a long-cycle capital investment, not an op-ex line item.

4. **Design for sovereignty, not around it.** CNI rules are not going
   away; they are tightening. Co-locate warehouses in-territory, use
   domestically owned hub operators for sensitive categories, and build
   audit trails that satisfy the regulator by default.

5. **Split the map into a main map plus two submaps before it becomes
   unreadable.** At 22 components this map is one step beyond the
   suggested 15-component limit (the validator warns at >18). Proposed
   submaps: **(a)** Automated Delivery stack (Automated Delivery, Drones
   & Scouts, Powertrain, Traffic & Telematics Data); **(b)** Sovereignty
   stack (Sovereignty, Regulation, Cities, Rural Areas). Each would
   replace one node on the main map.

## Build vs Buy Assessment

| Component | Recommendation | Rationale |
|---|---|---|
| Automated Delivery | **Build** | Custom-Built / Genesis — no dominant vendor yet; first-mover advantage on offer. |
| Supply Chain Awareness | **Build** | Emerging capability; differentiating if done well. |
| Drones & Scouts | **Build / Partner** | Genesis — bet on 1-2 specialist partners, but keep integration in-house. |
| Real-Time Stock | **Buy** | Mature vendors (Manhattan, Blue Yonder, Oracle). Don't reinvent. |
| Traffic & Telematics Data | **Buy** | Commodity API market (HERE, TomTom, Geotab). |
| Powertrain (Fossil/Electric) | **Buy** | Truck OEMs are the product market; don't become a vehicle manufacturer. |
| Long Haul | **Outsource** | Commodity. Spot markets exist. |
| Warehouses & Storage | **Outsource** | Commodity — but in-territory for CNI sensitivity. |
| HGV Skills | **Build / Invest** | Structural scarcity makes the market unreliable; internal training programme reduces risk. |

## Evolution Predictions (3–10 years)

- **Last Mile** moves from Product (0.48) toward Commodity (0.72) as
  automated delivery and drone corridors mature. The economics of the
  last mile are the single biggest cost lever in the chain, so market
  pressure here is enormous.
- **Automated Delivery** moves from Custom-Built (0.18) to late
  Product (0.55). Expect 2–3 dominant platforms by the late 2020s.
- **Drones & Scouts** moves from Genesis (0.12) to Custom-Built (0.42).
  Regulatory overhead keeps this slower than the tech permits.
- **Powertrain (Fossil/Electric)** moves from mid-Product (0.60) to
  Commodity (0.82) as electric platforms hit price parity with diesel
  (~2028–2030). Fossil becomes the declining sub-segment of the same
  commoditised powertrain market.
- **Traffic & Telematics Data** moves from early Commodity (0.70) to
  deep Commodity (0.85) as ADAS, C-ITS and V2X standards force
  interoperability.
- **Real-Time Stock** moves from Custom-Built (0.30) to Product (0.72)
  as the post-pandemic wave of supply-chain SaaS reaches maturity.
- **Supply Chain Awareness** moves from Custom-Built (0.18) toward
  Product (0.50) as public-facing visibility tools (provenance,
  carbon, origin) become table stakes.
- **Shops** edges from Commodity (0.80) to deeper Commodity (0.90) —
  continued format consolidation, more dark stores and micro-fulfilment.
- **Sovereignty/CNI** and **HGV Skills** stay where they are, or move
  left. These are the inertia-heavy nodes that *do not* follow the
  normal rightward drift because non-market forces dominate.

## Open Questions

1. **Where does rail fit?** The current map collapses rail into
   Long Haul, which is defensible but hides the particular economics
   and electrification dynamics of freight rail. Consider a submap.
2. **Is there a meaningful distinction between Drones and Scouts?**
   They are grouped here because both are Genesis; if either matures
   faster they should be split.
3. **How much of "Supply Chain Awareness" is regulatory-driven
   (CSRD, EUDR, UFLPA) vs consumer-driven?** That split changes whether
   the component evolves through regulation (slow) or the market (fast).

---

## React Artifact

The interactive React component is in `artifact.jsx` alongside this
file. It renders the same map with hover tooltips (showing the
rationale column above), click-to-highlight dependency chains, a figure
legend, and evolution stage shading. Open in a React runtime with
Tailwind CSS available.

## Validator Output

The skill's own validator (`scripts/validate_map.py`) reports:

```
WARNINGS (1):
  ⚠ Map has 22 components. Maps with >18 components become hard to read.
    Consider splitting into a main map and submaps.
✓ Map is valid with 1 warning(s).
```

The warning is acknowledged: the scenario explicitly asks for six
distinct layers (actors, commerce, vehicles, information, topology,
enablers) which is difficult to fit under 18 components without losing
fidelity. Recommended split into main + automation submap + sovereignty
submap is captured in Action 5 above.
