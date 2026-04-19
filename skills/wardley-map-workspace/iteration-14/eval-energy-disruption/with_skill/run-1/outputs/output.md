# Wardley Map — Energy Sector Disruption (July 2022)

**Scenario:** Transition of the electricity sector from centralised fossil generation toward distributed renewables + storage + demand-side flexibility (DSF). Map spans generation, storage, grid, distribution, retail, consumer, policy, and market mechanisms. Three user types — consumer, grid operator, and policymaker / regulator — so the map is multi-anchored.

**Scope note:** This is a landscape-scale map of a contested multi-stakeholder system (48 components). Figures reflect positioning in **July 2022** — i.e., the immediate post-Ukraine-invasion gas-price shock, before Inflation Reduction Act effects, with European gas storage only partway to pre-winter targets, and with lithium-ion cell prices at their local peak before the late-2022 softening.

---

## Map (OWM)

```owm
title Energy Sector Disruption — Centralised Fossil to Distributed Renewables + Storage + DSF (July 2022)
style wardley

// Anchors — multi-stakeholder system
anchor Consumer (Household / Business) [0.98, 0.55]
anchor Grid Operator [0.95, 0.60]
anchor Policymaker / Regulator [0.93, 0.45]

// User-facing
component Energy Bill [0.88, 0.82]
component Reliable Supply [0.90, 0.85]
component Decarbonisation Target [0.86, 0.50]
component Energy Security Mandate [0.84, 0.55]

// Retail & consumer-visible products
component Retail Supply Contract [0.78, 0.80]
component Dynamic Time-of-Use Tariff [0.72, 0.40]
component Energy-Use Visibility App [0.70, 0.55]
component Peer-to-Peer Energy Trading [0.68, 0.15]
component Virtual Power Plant (VPP) [0.66, 0.30]
component Demand Response Program [0.64, 0.50]
component Aggregator Service [0.60, 0.45]

// Consumer-facing demand-side devices & DER
component Vehicle-to-Grid (V2G) [0.58, 0.15]
component EV Smart Charging [0.56, 0.45]
component Heat Pump [0.54, 0.55]
component Rooftop Solar PV [0.52, 0.70]
component Home Battery [0.50, 0.55]
component Home Energy Management System [0.46, 0.35]

// Market mechanisms (visible to Grid Operator & Policymaker)
component Wholesale Electricity Market [0.72, 0.80]
component Capacity Market [0.70, 0.65]
component Flexibility Market [0.68, 0.30]
component Ancillary Services Market [0.66, 0.60]
component Carbon Market / Pricing [0.65, 0.55]

// Generation
component Offshore Wind [0.40, 0.60]
component Onshore Wind [0.38, 0.75]
component Utility Solar PV [0.36, 0.75]
component Gas CCGT Generation [0.34, 0.88]
component Coal Generation [0.32, 0.88]
component Nuclear Generation [0.30, 0.80]

// Storage
component Grid-Scale Li-ion Battery [0.38, 0.50]
component Pumped Hydro Storage [0.28, 0.85]
component Long-Duration Storage (flow / iron-air) [0.26, 0.15]
component Green Hydrogen (Electrolyser) [0.24, 0.20]

// Grid infrastructure
component Distribution Network [0.26, 0.82]
component Transmission Network [0.22, 0.85]
component Synthetic Inertia [0.22, 0.20]
component Grid-Forming Inverter [0.18, 0.30]
component Smart Meter [0.32, 0.60]
component Grid SCADA / Control [0.16, 0.75]
component Forecasting (wind / solar / load) [0.28, 0.55]

// Policy & regulatory instruments
component Grid Code / Connection Rules [0.24, 0.70]
component CfD / Subsidy Scheme [0.34, 0.65]
component Planning / Permitting [0.30, 0.55]

// Foundational utilities & data
component Weather Data Feeds [0.14, 0.75]
component Cloud & Telemetry [0.10, 0.90]
component Electricity (commodity) [0.08, 0.95]

// Dependencies
Consumer (Household / Business)->Energy Bill
Consumer (Household / Business)->Reliable Supply
Consumer (Household / Business)->Retail Supply Contract
Consumer (Household / Business)->Energy-Use Visibility App
Consumer (Household / Business)->Dynamic Time-of-Use Tariff
Consumer (Household / Business)->Heat Pump
Consumer (Household / Business)->EV Smart Charging
Consumer (Household / Business)->Rooftop Solar PV
Consumer (Household / Business)->Home Battery
Consumer (Household / Business)->Peer-to-Peer Energy Trading

Grid Operator->Reliable Supply
Grid Operator->Wholesale Electricity Market
Grid Operator->Capacity Market
Grid Operator->Flexibility Market
Grid Operator->Ancillary Services Market
Grid Operator->Transmission Network
Grid Operator->Grid SCADA / Control
Grid Operator->Forecasting (wind / solar / load)
Grid Operator->Grid Code / Connection Rules

Policymaker / Regulator->Decarbonisation Target
Policymaker / Regulator->Energy Security Mandate
Policymaker / Regulator->Carbon Market / Pricing
Policymaker / Regulator->CfD / Subsidy Scheme
Policymaker / Regulator->Planning / Permitting
Policymaker / Regulator->Grid Code / Connection Rules

Energy Bill->Retail Supply Contract
Energy Bill->Dynamic Time-of-Use Tariff
Retail Supply Contract->Wholesale Electricity Market
Retail Supply Contract->Smart Meter
Dynamic Time-of-Use Tariff->Smart Meter
Energy-Use Visibility App->Smart Meter
Reliable Supply->Distribution Network
Reliable Supply->Transmission Network
Reliable Supply->Capacity Market

Peer-to-Peer Energy Trading->Aggregator Service
Peer-to-Peer Energy Trading->Smart Meter
Virtual Power Plant (VPP)->Aggregator Service
Aggregator Service->Home Energy Management System
Aggregator Service->Smart Meter
Aggregator Service->Cloud & Telemetry

Demand Response Program->Aggregator Service
Demand Response Program->Smart Meter

Heat Pump->Home Energy Management System
EV Smart Charging->Home Energy Management System
EV Smart Charging->Distribution Network
Vehicle-to-Grid (V2G)->EV Smart Charging
Vehicle-to-Grid (V2G)->Distribution Network
Home Battery->Home Energy Management System
Rooftop Solar PV->Home Energy Management System
Rooftop Solar PV->Distribution Network
Home Energy Management System->Cloud & Telemetry
Home Energy Management System->Smart Meter

Wholesale Electricity Market->Offshore Wind
Wholesale Electricity Market->Onshore Wind
Wholesale Electricity Market->Utility Solar PV
Wholesale Electricity Market->Gas CCGT Generation
Wholesale Electricity Market->Coal Generation
Wholesale Electricity Market->Nuclear Generation
Capacity Market->Gas CCGT Generation
Capacity Market->Grid-Scale Li-ion Battery
Capacity Market->Pumped Hydro Storage
Flexibility Market->Grid-Scale Li-ion Battery
Flexibility Market->Demand Response Program
Flexibility Market->Vehicle-to-Grid (V2G)
Ancillary Services Market->Grid-Forming Inverter
Ancillary Services Market->Synthetic Inertia
Ancillary Services Market->Grid-Scale Li-ion Battery
Ancillary Services Market->Pumped Hydro Storage
Carbon Market / Pricing->Gas CCGT Generation
Carbon Market / Pricing->Coal Generation

Offshore Wind->Transmission Network
Offshore Wind->CfD / Subsidy Scheme
Offshore Wind->Planning / Permitting
Offshore Wind->Forecasting (wind / solar / load)
Onshore Wind->Transmission Network
Onshore Wind->Planning / Permitting
Onshore Wind->Forecasting (wind / solar / load)
Utility Solar PV->Transmission Network
Utility Solar PV->Planning / Permitting
Utility Solar PV->Forecasting (wind / solar / load)
Gas CCGT Generation->Transmission Network
Coal Generation->Transmission Network
Nuclear Generation->Transmission Network

Grid-Scale Li-ion Battery->Distribution Network
Grid-Scale Li-ion Battery->Transmission Network
Grid-Scale Li-ion Battery->Grid-Forming Inverter
Pumped Hydro Storage->Transmission Network
Long-Duration Storage (flow / iron-air)->Transmission Network
Green Hydrogen (Electrolyser)->Transmission Network

Transmission Network->Electricity (commodity)
Distribution Network->Transmission Network
Distribution Network->Electricity (commodity)
Grid SCADA / Control->Cloud & Telemetry
Forecasting (wind / solar / load)->Weather Data Feeds
Forecasting (wind / solar / load)->Cloud & Telemetry
Smart Meter->Distribution Network
Smart Meter->Cloud & Telemetry
Synthetic Inertia->Grid-Forming Inverter

Decarbonisation Target->CfD / Subsidy Scheme
Decarbonisation Target->Carbon Market / Pricing
Energy Security Mandate->Capacity Market
Grid Code / Connection Rules->Grid-Forming Inverter

// Evolution trajectories (scenarios, not forecasts)
evolve Grid-Scale Li-ion Battery 0.78
evolve Home Battery 0.72
evolve Heat Pump 0.75
evolve EV Smart Charging 0.70
evolve Vehicle-to-Grid (V2G) 0.45
evolve Green Hydrogen (Electrolyser) 0.45
evolve Long-Duration Storage (flow / iron-air) 0.40
evolve Grid-Forming Inverter 0.60
evolve Flexibility Market 0.60
evolve Virtual Power Plant (VPP) 0.55
evolve Peer-to-Peer Energy Trading 0.40
evolve Dynamic Time-of-Use Tariff 0.65
evolve Offshore Wind 0.80
evolve Coal Generation 0.95

// Inertia markers — fossil incumbents will resist
component Coal Generation [0.32, 0.88] inertia
component Gas CCGT Generation [0.34, 0.88] inertia

note BUILD / differentiation zone [0.55, 0.20]
note Legacy utility foundations [0.15, 0.92]
note War zone — product-to-utility (pattern #27) [0.40, 0.60]
```

**Validator:** OK — 48 components/anchors, 102 edges, no visibility violations.

---

## What's differentiating vs. commoditising

The map has a clear split across the X-axis:

**Commoditising (right side, Stage III / IV — Product (+rental) / Commodity (+utility)):**
- **Coal**, **Gas CCGT**, **Pumped Hydro**, **Nuclear** — Stage IV legacy generation. The old centralised stack.
- **Utility Solar PV**, **Onshore Wind** — now genuinely Stage III (+rental), headed to IV. 2022 auction clearing prices make these the cheapest new MWh in almost every market.
- **Transmission / Distribution Network**, **Electricity-the-commodity** — Stage IV utility foundations; regulated natural monopolies.
- **Cloud & Telemetry**, **Weather Data Feeds** — Stage IV digital utilities underpinning the digitalisation of the grid.
- **Retail Supply Contract**, **Wholesale Market**, **Energy Bill** — Stage IV transactional layer; the "kWh bill" is a commodity product.

**Differentiating (left-centre, Stage I / II — Genesis / Custom Built):**
- **Peer-to-Peer Energy Trading**, **V2G**, **Long-Duration Storage (flow / iron-air)**, **Green Hydrogen (electrolyser)**, **Synthetic Inertia** — Genesis. Real bets, high uncertainty.
- **Virtual Power Plant**, **Grid-Forming Inverter**, **Home Energy Management System**, **Flexibility Market**, **Aggregator Service** — Custom Built. These are the build zone.

**The transition pivot:** the middle band (ε ≈ 0.4–0.6) is where the strategic war sits — the **Flexibility Market**, **VPP / Aggregator stack**, **Grid-Forming Inverters**, and **Dynamic Time-of-Use Tariffs**. This is where the business-model war over DSF is being fought in 2022. Whoever industrialises these first captures the "operating system" of a distributed grid.

---

## a. Differentiation opportunities (top 3)

1. **Virtual Power Plant / Aggregator stack** (Custom Built → Product (+rental)) — high visibility (ν ≈ 0.60–0.66) on an emerging capability. The aggregator that industrialises multi-asset VPPs across DR + V2G + battery + heat pump wins the consumer-facing operating layer for the distributed grid. No dominant vendor in July 2022 (Octopus Kraken, Tesla Autobidder, Next Kraftwerke, AutoGrid, Enel X — all fragmented). **Highest D in the map.**
2. **Grid-Forming Inverter** (Custom Built) — low visibility (ν ≈ 0.18) but strategically critical: as synchronous generation retires, someone has to replace the system services (inertia, voltage, frequency) that came free with big spinning machines. Whoever delivers grid-forming inverter IP wins a mandatory component in every battery project. **Deep but valuable — the "Intel Inside" of the renewable grid.**
3. **Dynamic Time-of-Use Tariff and the Energy-Use Visibility App** (Custom Built → Product (+rental)) — consumer-visible (ν ≈ 0.70–0.72); the loyalty wedge for a retailer. 2022 gas-price shock materially increased consumer appetite for any product that lets them shift load off peak.

(Honourable mentions: **Long-Duration Storage**, **Green Hydrogen Electrolyser** — both Genesis and strategically critical for deep-decarbonisation, but their uncertainty makes them option-plays rather than single-product differentiators.)

## b. Commodity-leverage candidates (top 3)

1. **Utility Solar PV and Onshore Wind** (Product (+rental) → Commodity (+utility)) — rent capacity via PPA or CfD; do not try to build proprietary solar farms. Module and turbine markets are near-utility.
2. **Cloud & Telemetry** (Commodity (+utility)) — treat AWS / Azure / GCP as utility; never build your own. All aggregator, VPP and SCADA-cloud vendors should standardise on hyperscaler primitives.
3. **Smart Meter and Retail Supply Contract** (Product (+rental) → Commodity (+utility)) — rollout is regulator-mandated and vendor-commoditised. Don't fight on the meter; fight on the app and tariff on top of it.

(Also: **Weather Data Feeds**, **Pumped Hydro**, **Gas CCGT** — all Stage IV utilities to consume, not build.)

## c. Dependency risks (top 3)

1. **Reliable Supply → Capacity Market → Gas CCGT Generation.** The whole reliability chain still hinges on a fleet the carbon market and retirement pressure are actively pushing out. In July 2022 the EU gas shock shows how badly this dependency can bite: decarbonisation targets are driving coal/gas capacity payments *down*, but nothing industrialised has yet replaced them for winter-peak reliability. Classic "visible user need depends on an asset class in managed decline."
2. **Flexibility Market → Demand Response Program / V2G.** The grid operator's flexibility toolbox is a Custom Built market (ν ≈ 0.68, ε ≈ 0.30) depending on **V2G (ε = 0.15, Genesis)** and **DR (ε = 0.50, edge of Custom / Product (+rental))**. If V2G doesn't industrialise on schedule (chicken-and-egg: OEMs, interop, network code), the flexibility market is under-supplied and winter-peak balancing suffers.
3. **Aggregator Service → Home Energy Management System.** The VPP/aggregator business case depends on device-level control that, in July 2022, is still fragmented (Matter 1.0 had barely shipped, EEBus is German-led, openADR is DR-specific). This is the sort of Custom → Product (+rental) transition gated on a standards war.

## d. Suggested gameplays (Wardley's 61)

- **#36 Directed investment** on the **VPP / Aggregator / HEMS / Dynamic ToU** stack. These are Custom Built components on a punctuated-equilibrium trajectory into Stage III Product (+rental). Put engineering there.
- **#15 Open Approaches** on **Grid-Forming Inverter control algorithms**, **HEMS device APIs**, and **Flexibility Market data schemas**. You win the mass market for distributed flex by opening the interfaces — not by hoarding them (Google/Android pattern).
- **#43 Sensing Engines (ILC)** on **Long-Duration Storage and Green Hydrogen.** Too early to pick winners; run an Innovate-Leverage-Commoditise loop — pilot several chemistries and electrolyser types, read consumption and price signals, commoditise the winner.
- **#45 Two factor** for any aggregator — prosumers on one side, grid services buyers on the other. This IS a two-sided-market play.
- **#16 Exploiting Network Effects** on VPP — each additional prosumer lowers marginal forecasting cost and raises aggregate bid reliability.
- **#41 Alliances** with OEMs (car, heat pump, HVAC) for smart-control hooks; and with DSOs for distribution-level flexibility contracts. V2G needs multi-party alignment.
- **#56 First mover** on **flexibility-market product design** in any jurisdiction where the regulator is drafting rules — first movers anchor the schema.
- **#29 Harvesting** on **heat pump installers, solar EPCs, battery installers** — let the installer market grow, then acquire the winning integrator.
- **#34 Procrastination** is the *anti-play* for fossil incumbents considering transition. It is Kodak's strategy. Watch for it among utilities defending CCGT fleets.
- **#50 Reinforcing inertia** is being actively played against renewables by fossil incumbents via planning / permitting delays and capacity-market rule-setting. Countermove: **#39 Undermining barriers to entry** — push for streamlined planning, standardised connection rules, and capacity-market reform.

## e. Doctrine notes (Wardley's 40 principles)

- ✓ **#1 Focus on user needs** — three anchors (Consumer, Grid Operator, Policymaker) reflect that this is a genuinely multi-stakeholder landscape; none of them is a proxy for the others.
- ✓ **#10 Know your users** — explicitly multi-anchor. In particular, the Policymaker anchor is important: **Decarbonisation Target** and **Energy Security Mandate** are legitimate user needs in their own right, not externalities.
- ⚠ **#13 Manage inertia** — flagged on **Coal** and **Gas CCGT**. Fossil incumbents carry inertia forms #2 (sunk capital in generation assets), #3 (political capital tied to stranded-asset debates), #4 (human capital — the workforce and skills), and #7 (supplier-trust: gas procurement networks). This is the largest inertia load on any single map in the reference catalogue.
- ⚠ **#7 Use appropriate methods** — the map spans the whole cheat sheet; applying one methodology (say, "agile everywhere") will fail. Six Sigma for transmission; Lean / SRE for aggregator platforms; agile and experimentation for Genesis components (LDES, hydrogen, V2G).
- ⚠ **#33 Don't neglect the levels** — Knowledge layer is thin in the current map (Grid Code, Decarbonisation Target are the only explicit knowledge-ish nodes). A richer map would add market-design theory, power-systems engineering practice, climate policy models as Knowledge components.
- ⚠ **#19 Distribute power and decision making** — arguably the decarbonisation transition itself is a doctrine-#19 moment for the whole sector: the old model concentrated decisions at the grid operator and a few gencos; the new one distributes them to millions of prosumer endpoints.

## f. Climatic context (27 patterns)

- **#3 Everything evolves** — fossil generation *will* be displaced; the only question is speed.
- **#4 Multiple waves of diffusion with chasms** — storage is a textbook case: pumped hydro (saturated) → Li-ion (scaling into Stage III) → LDES (Genesis). Three waves visible on this map.
- **#5 No choice over evolution** — incumbents who try to defend CCGT or coal indefinitely are fighting the climate.
- **#15–17 Past success breeds inertia / can kill** — the whole incumbent utility industry is under this pattern. Ørsted's transformation is the counter-example; many others are still in denial.
- **#22 Two forms of disruption** — both are visible here: (i) Genesis disruption from V2G, hydrogen, LDES; (ii) Product → Commodity (+utility) disruption from solar and wind displacing fossil fuel in the merit order. The **Product → Commodity (+utility) disruption is the more predictable and more immediate one.**
- **#27 Product-to-utility punctuated equilibrium** — this is literally happening now across solar (Stage III → IV) and wind (Stage III → IV). The **War** phase of the Peace-War-Wonder cycle.
- **#21 Economic cycles (Peace-War-Wonder)** — Generation is in **War** (fossil → renewable utility). VPP / flex markets are in **Wonder** (new Stage I–II business models emerging). Nuclear is in **Peace** (settled, slow).
- **#24 Efficiency enables innovation** — cheap renewable electricity (commodity foundation) enables new higher-order businesses (electrolysis-based hydrogen, green steel, data-centre siting near cheap renewable MWh).
- **#12 Jevons effect** — electrification of transport and heat is the Jevons paradox writ large: cheaper cleaner electricity grows aggregate demand, which is why transmission and distribution are simultaneously under retirement pressure (for old assets) and massive build pressure (for new capacity).
- **#18 You cannot measure evolution over time or adoption** — applies directly. All evolve arrows on this map are **scenarios, not forecasts**.

## g. Deep-placement notes

A handful of components warranted targeted thought beyond the initial cheat-sheet pass. In July 2022 these are defensible on the following evidence:

- **Utility Solar PV (ε = 0.75, Stage III edge of Commodity (+utility)).** Initial cheat-sheet reflex would say Stage III comfortably. In 2022 however, unsubsidised LCOEs in sunny geographies had undercut every fossil competitor; multiple Middle East / India auctions cleared at < $20/MWh; module manufacturing is a commodity game dominated by a few Chinese vendors. Publication type has shifted from "case studies / feature comparisons" to "operations / installation / best practice". This is Stage III transitioning to IV — kept at 0.75 to reflect the point-of-transition rather than overstate the move.
- **Grid-Scale Li-ion Battery (ε = 0.50, Custom → Product (+rental)).** Initial placement might sit higher (ε ≈ 0.60) given how much deployment happened 2020–22. But in July 2022, cell pricing is at a local peak (nickel/cobalt spike post-Ukraine), Tesla-vs-Fluence-vs-Wärtsilä competition is intense, and the battery-as-integrator play (services stacking) is still Custom. Auctions like UK's Dynamic Containment reward bespoke configurations. Keeping this at ε = 0.50 with an `evolve` target of 0.78 captures the near-term industrialisation trajectory.
- **V2G (ε = 0.15, Genesis).** Every public pilot in July 2022 (e.g., Nissan Leaf, UK trials) still counts in hundreds or low thousands of vehicles. ISO 15118-20 only finalised in 2022. OEM uptake is partial. No major OEM had mass-market bidirectional as a standard feature. Firmly Genesis.
- **Dynamic Time-of-Use Tariff (ε = 0.40).** Octopus Agile-style tariffs exist in the UK; European markets have less penetration; US is a patchwork. Not yet a standard Stage III product — Custom Built, with rapid learning. Hence ε = 0.40 and an `evolve` target to 0.65.
- **Heat Pump (ε = 0.55).** Feature-competitive Stage III in Europe (Nordic markets mature; UK/DE growing fast), Stage II in many others. Call Product (+rental) for a European market-relative scoring.
- **Offshore Wind (ε = 0.60).** Mature sector (Ørsted, Iberdrola, RWE). Fixed-bottom is clearly Product (+rental); floating is still Custom. Aggregate at 0.60.

(Full-list note: only 5–6 components received deep placement. Obvious commodities — Cloud, Weather Data, Electricity-the-commodity, Transmission Network — were not researched further; obvious Genesis bets — Green Hydrogen, LDES, P2P trading — were scored directly from cheat-sheet rows without chasing nuance.)

## h. Where is the transition fragile?

Three fragility zones stand out:

1. **Firm capacity during the shoulder years.** The capacity market currently props up Gas CCGT (Stage IV, declining). Renewables are not firm; batteries cover minutes-to-hours; **LDES (ε = 0.15) is still Genesis**. The period 2024–2028 when fossil retires faster than LDES can industrialise is genuinely risky for reliability. The Carbon Market / Pricing pressure on Gas CCGT plus capacity-market rule changes can accelerate retirement *faster than replacements arrive* — a classic climate-pattern-#27 fragility.
2. **Grid-forming capability.** As synchronous machines retire, the grid loses inertia and voltage-source behaviour "for free". The replacement — grid-forming inverters and synthetic inertia — is Custom Built. If deployment lags, the grid becomes less stable (UK's 9 August 2019 event was an early warning; Australia's 2016 SA blackout another). Grid-code reform is essential but slow.
3. **Standards fragmentation in the DSF stack.** Aggregator service, HEMS, V2G, smart appliances. If OEMs, DSOs, and software vendors don't converge on a small set of interoperable protocols (OpenADR, Matter, ISO 15118-20, IEEE 2030.5, EEBus), the aggregator market stays Custom Built far longer than needed — a standards-war chasm (#4 multi-wave with chasm). The punctuated-equilibrium exit requires **#30 Standards game + #15 Open Approaches**.

Secondary fragilities: planning/permitting bottleneck on transmission build-out; rare-earth and lithium supply chains concentrated in China; political / populist backlash on bills in a gas-shock year.

## Caveat

Evolution trajectories are **scenarios, not forecasts**. Wardley's climatic pattern #18: *"you cannot measure evolution over time or adoption."* The `evolve` arrows on this map are the author's read of market pressure and gameplay on July 2022 priors; re-map when signals change. The gas-price shock of 2022 is itself an example of why 12-month-old maps of this sector become obsolete quickly.

Stage labels (Genesis, Custom Built, Product (+rental), Commodity (+utility)) used throughout with their suffixes — Stage III covers both products and rental/licensing business models; Stage IV covers both commodities and utility services.
