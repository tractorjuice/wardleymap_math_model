# Energy Disruption Landscape — Wardley Map (July 2022)

**Anchor:** Consumers and industrial off-takers need reliable, affordable, low-carbon energy — where today's demand meets tomorrow's survivability.
**Scope:** End-to-end electricity + gas value chain (generation → transmission → distribution → market → consumer), overlaid with control, regulation, CO2 apparatus, supply-chain awareness, and the storage / externality questions.
**Author:** wardley-mapping skill (arc-kit)
**Date:** 2022-07-15
**Version:** 1.0

---

## 1. Context gathered (Step 1)

| Question | Answer |
|---|---|
| Primary user | Consumers (household / business) and industrial off-takers; secondary: regulators and system operators — the demand side facing a disrupted supply side. |
| User need | "Energy that works today, keeps the lights on tomorrow, and doesn't cook the planet." Reliability, affordability, low-carbon. |
| Scope | Whole electricity + gas value chain from primary fuels to the meter, including the market layer, the regulatory / CO2 apparatus, and supply-chain + externality picture. |
| Primary goal | Identify (a) where disruption is most likely, (b) where infrastructure is locked-in (inertia), and (c) what supply-chain awareness and externality visibility look like. |
| Industry | Global / UK–EU energy system, July 2022: four months into the Russia–Ukraine war, European gas prices at historical highs, net-zero commitments hardening, IRA about to pass in the US. |
| Depth | Deep analysis — ~55 components across generation, T&D, market, control, storage, consumer, supply-chain / externality layers, with gameplay + climate overlay. |

---

## 2. Value chain (Step 2)

Working backwards from the anchor (consumer / industrial off-taker needing energy):

- **Anchor layer:** Consumer (household / business), Industrial off-taker, National Government / Regulator, System Operator (TSO / ISO).
- **Consumer-facing:** today's "flick-the-switch" behaviour vs tomorrow's "flex + self-gen" behaviour, energy security expectation, sustainability expectation, energy literacy / education, the bill, the smart meter / HEM, time-of-use / DR, self-generation.
- **Market layer:** spot (day-ahead / intraday), OTC, PPAs, wholesale price, retail supply, capacity market, balancing / ancillary services market, carbon price, full-cost (externality) accounting, energy as a public good.
- **Control / regulation / CO2:** market regulator (Ofgem / FERC / ACER), grid code, net-zero commitments, CO2 MRV, CBAM, price-cap / tariff regulation, subsidies (CfD / ITC / FIT).
- **Distribution:** DSO network, local reinforcement, EV charging infrastructure.
- **Transmission:** AC grid, HVDC interconnectors, transmission capex lock-in.
- **Production / balancing:** central dispatch, inverter-based resource control, frequency / voltage stability, flexibility / firming services, capacity-intensive capex.
- **Generation mix:** fossil (coal / gas peaker), gas CCGT, nuclear (existing + SMR), utility-scale wind, utility-scale solar PV, solar microgen, community / microgrid, biomass / W2E, geothermal / tidal / wave.
- **Storage:** aggregate storage need; subtypes — Li-ion grid battery, flow battery, hydrogen / electrolyser, pumped hydro, compressed air / thermal, strategic gas/oil reserve.
- **Fuel / primary energy:** natural gas (pipeline + LNG), Russian gas exposure, LNG import terminals, coal, uranium, critical minerals (Li / Co / Ni / REE).
- **Supply-chain awareness + externality:** energy-system supply-chain awareness, Scope 1–3 disclosure, externality pricing (health / climate), just-transition / fuel poverty, geopolitical risk.

---

## 3. Visual map (Step 3 + 4)

```text
Title: Energy Disruption Landscape
Anchor: Consumer + Industrial off-taker need reliable, affordable, low-C energy
Date: 2022-07-15

                    Genesis     Custom      Product     Commodity
                       │          │          │          │
Visible            ┌───┼──────────┼──────────┼──────────┼───┐
                   │   │          │          │          │   │
 Anchors           │   │ Gov/Reg ●       TSO ●     Ind  ●  Consumer ●
                   │   │          │          │          │          │
 Consumer layer    │   │ Tomorrow●→ Time-of-Use●→  Smart Meter ●→   │
                   │   │ Self-gen ●→ Tariff ●     Today's Behav. ● ×
                   │   │ Sustain. ●→               Energy Security ●
                   │   │ Education ●→                               │
 Market            │   │ Public-Good ●→ Carbon Price ●→ PPA ●  Retail ●
                   │   │ Full-cost ●→  Balancing ●      Capacity ●  │
                   │   │                           Wholesale ●  Spot●
                   │   │                           OTC ●            │
 Regulation/CO2    │   │ CBAM ●→ CO2 MRV ●→  Subsidies ● Net-Zero ●→│
                   │   │        Externality ●  Market Reg ● Price Cap●
                   │   │                       Grid Code ●           │
 Distribution      │   │         EV Charging ●→ Local Reinforce ●  DSO ●×
 Transmission      │   │          HVDC Interc. ●    Transmission AC ●×
                   │   │                                    Tx Capex ●×
 Prod / Balance    │   │ Grid IBR Ctl ●→ Flex/Firm ●→  Dispatch ●×
                   │   │                                Freq/V ●  Capex×●
 Generation        │   │ SMR/new nuc ●→ Solar microgen●→  Nuclear exist ●
                   │   │ Microgrid ●→  Solar PV ●→       CCGT ●× Fossil●×
                   │   │ Geo/Tidal ●→ Wind ●→                       │
                   │   │               Biomass ●                    │
 Storage           │   │ Flow-batt ●→ Li-ion ●→→   Pumped hydro ●   │
                   │   │ H2/Electro ●→       Strategic Reserve ●×   │
                   │   │ CAES/Thermal ●→ Storage-need ●→            │
 Fuel / primary    │   │ Crit.Min. ●→ LNG terminal ●→  Uranium ●    │
                   │   │              Coal ●     Gas Supply ●×      │
                   │   │              Russian Gas ●×                │
                   │   │              Geo-Risk ●                    │
 Supply-ch / Ext.  │   │ Externality ●→ Scope 1-3 ●→ Just-Trans ●→  │
Hidden             │   │ Supply-Ch Aware ●→                         │
                   │   │                                            │
                   └───┴────────────────────────────────────────────┘

Legend: ● Current position, → Evolution direction, × Inertia / lock-in
```

---

## 4. Structured output

```yaml
wardley_map:
  metadata:
    title: "Energy Disruption Landscape"
    author: "arc-kit wardley-mapping skill"
    date: "2022-07-15"
    version: "1.0"
    scope: "Full electricity + gas value chain, market, regulation, CO2, storage, supply-chain, externalities"

  anchor:
    user: "Consumer (household / business) and industrial off-taker"
    need: "Reliable, affordable, low-carbon energy — today's demand meeting tomorrow's survivability"

  components:
    - name: "Today's Consumer Behaviour (flick-the-switch)"
      evolution: "Commodity"
      position: 0.95
      visibility: 0.88
      depends_on: ["Consumer Bill / Tariff"]
      notes: "Deeply ingrained — energy is assumed invisible until the bill arrives."
      movement: "inertia"

    - name: "Tomorrow's Consumer Behaviour (flex / self-gen)"
      evolution: "Genesis → Custom"
      position: 0.18
      visibility: 0.88
      depends_on: ["Smart Meter / HEM", "Time-of-Use / Demand Response", "Consumer Self-generation"]
      notes: "Consumer-as-participant is still genesis in Jul 2022 — few households flex load or run a home battery."
      movement: "evolving"

    - name: "Consumer Self-generation (rooftop solar / battery)"
      evolution: "Product"
      position: 0.48
      visibility: 0.74
      depends_on: ["Solar Microgeneration", "Electrical Storage (Li-ion)", "Distribution Network (DSO)"]
      notes: "Rooftop PV is productised (installers, finance); home battery is mid-product; integration with DSO is the open edge."
      movement: "evolving"

    - name: "Smart Meter / HEM"
      evolution: "Product"
      position: 0.70
      visibility: 0.78
      depends_on: ["Distribution Network (DSO)"]
      notes: "Rollout largely complete in UK / some EU; HEM apps maturing."
      movement: "evolving"

    - name: "Time-of-Use / Demand Response"
      evolution: "Custom → Product"
      position: 0.38
      visibility: 0.76
      depends_on: ["Smart Meter / HEM", "Spot Market", "Flexibility / Firming Services"]
      notes: "Octopus Agile-style dynamic tariffs exist but are niche; most retailers still flat-rate."
      movement: "evolving"

    - name: "Energy Security (reliability of supply)"
      evolution: "Product → Commodity"
      position: 0.78
      visibility: 0.86
      depends_on: ["Strategic Reserve", "Capacity Market"]
      notes: "Assumed default in the Global North; Jul-2022 is the first serious doubt since 1970s oil shocks."
      movement: "none"

    - name: "Sustainability Expectation"
      evolution: "Custom"
      position: 0.30
      visibility: 0.84
      depends_on: ["Net-Zero Policy Commitment", "Carbon Price"]
      notes: "Rising fast but still bespoke per household / corporate buyer."
      movement: "evolving"

    - name: "Consumer Bill / Tariff"
      evolution: "Commodity"
      position: 0.85
      visibility: 0.80
      depends_on: ["Retail Supply", "Price Cap / Tariff Regulation", "Wholesale Price"]
      notes: "Mature; but Jul-2022 price shock is stressing the retail-supplier model (UK supplier failures)."
      movement: "none"

    - name: "Retail Supply (energy retailer)"
      evolution: "Product → Commodity"
      position: 0.82
      visibility: 0.74
      depends_on: ["Wholesale Price", "OTC / Bilateral Contracts", "Spot Market", "Balancing / Ancillary Services Market"]
      notes: "Productised market; thin margins, high hedging risk."
      movement: "none"

    - name: "Spot Market (day-ahead / intraday)"
      evolution: "Commodity"
      position: 0.90
      visibility: 0.80
      depends_on: ["Wholesale Price"]
      notes: "Mature utility-style exchange (EPEX, Nordpool, ERCOT)."
      movement: "none"

    - name: "OTC / Bilateral Contracts"
      evolution: "Commodity"
      position: 0.82
      visibility: 0.78
      depends_on: ["Wholesale Price"]
      notes: "Standard ISDA-style practice."
      movement: "none"

    - name: "PPA (Power Purchase Agreement)"
      evolution: "Product"
      position: 0.68
      visibility: 0.68
      depends_on: ["Utility-Scale Renewable", "Utility-Scale Solar PV", "Wholesale Price"]
      notes: "Mature product; corporate PPA pricing still opaque but legal templates standardised."
      movement: "none"

    - name: "Wholesale Price (merchant signal)"
      evolution: "Commodity"
      position: 0.88
      visibility: 0.76
      depends_on: ["Central Production / Dispatch", "Capacity Market"]
      notes: "Standard merit-order clearing — but gas-setting-price is Jul-2022's political problem."
      movement: "none"

    - name: "Capacity Market"
      evolution: "Product"
      position: 0.60
      visibility: 0.70
      depends_on: ["Central Production / Dispatch", "Flexibility / Firming Services"]
      notes: "Productised in UK / PJM; politically contested in EU."
      movement: "none"

    - name: "Balancing / Ancillary Services Market"
      evolution: "Product"
      position: 0.65
      visibility: 0.68
      depends_on: ["Flexibility / Firming Services", "Grid-Scale Inverter-Based Resource Control"]
      notes: "Opening up to battery / DSR aggregators but still mostly CCGT-served."
      movement: "evolving"

    - name: "Carbon Price (ETS / floor)"
      evolution: "Product"
      position: 0.55
      visibility: 0.66
      depends_on: ["CO2 MRV (emissions measurement)"]
      notes: "EU ETS matured to product; UK ETS just launched; US lacks federal price."
      movement: "evolving"

    - name: "Full-Cost (incl. externalities) Accounting"
      evolution: "Custom"
      position: 0.22
      visibility: 0.70
      depends_on: ["CO2 MRV (emissions measurement)", "Externality Pricing"]
      notes: "Still bespoke — no standard for health / biodiversity / climate externalities to hit the price."
      movement: "evolving"

    - name: "Energy as Public Good"
      evolution: "Genesis → Custom"
      position: 0.15
      visibility: 0.72
      depends_on: ["Net-Zero Policy Commitment", "Price Cap / Tariff Regulation", "Just-Transition / Fuel Poverty"]
      notes: "The Jul-2022 price-shock is re-opening the question of whether energy should be a market or a utility — genesis politically."
      movement: "evolving"

    - name: "Market Regulation (Ofgem / FERC / ACER)"
      evolution: "Product"
      position: 0.62
      visibility: 0.64
      depends_on: []
      notes: "Mature institutions — but Jul-2022 gas crisis is straining their doctrine."
      movement: "none"

    - name: "Grid Code / Network Rules"
      evolution: "Product → Commodity"
      position: 0.78
      visibility: 0.60
      depends_on: []
      notes: "Codified (e.g., GB Grid Code, ENTSO-E Network Codes)."
      movement: "none"

    - name: "Net-Zero Policy Commitment"
      evolution: "Custom → Product"
      position: 0.38
      visibility: 0.62
      depends_on: []
      notes: "Widely committed but bespoke per jurisdiction; implementation pathways still custom."
      movement: "evolving"

    - name: "CO2 MRV (emissions measurement)"
      evolution: "Custom → Product"
      position: 0.45
      visibility: 0.58
      depends_on: []
      notes: "ISO 14064 + GHG Protocol mature for Scope 1/2; Scope 3 and real-time MRV still bespoke."
      movement: "evolving"

    - name: "Carbon Border Adjustment (CBAM)"
      evolution: "Genesis"
      position: 0.18
      visibility: 0.56
      depends_on: ["CO2 MRV (emissions measurement)"]
      notes: "EU CBAM transitional phase starting Oct 2023 — Jul 2022 it is genesis policy."
      movement: "evolving"

    - name: "Price Cap / Tariff Regulation"
      evolution: "Product"
      position: 0.72
      visibility: 0.60
      depends_on: []
      notes: "UK default-tariff cap mechanism is the high-profile example; about to reset upwards sharply in Oct 2022."
      movement: "none"

    - name: "Subsidies (CfD / ITC / FIT)"
      evolution: "Product"
      position: 0.58
      visibility: 0.58
      depends_on: []
      notes: "Mature auction-based products (UK CfD, US ITC/PTC); IRA about to step-change the US."
      movement: "evolving"

    - name: "Distribution Network (DSO)"
      evolution: "Commodity"
      position: 0.88
      visibility: 0.56
      depends_on: ["Transmission Network (AC grid)", "Local Network Reinforcement"]
      notes: "Utility — but reinforcement debt is the choke on EV + rooftop PV uptake."
      movement: "inertia"

    - name: "Local Network Reinforcement"
      evolution: "Product"
      position: 0.62
      visibility: 0.54
      depends_on: ["Transmission Capex (locked-in assets)"]
      notes: "Standard engineering — speed is the problem, not novelty."
      movement: "none"

    - name: "EV Charging Infrastructure"
      evolution: "Custom → Product"
      position: 0.50
      visibility: 0.52
      depends_on: ["Distribution Network (DSO)", "Local Network Reinforcement"]
      notes: "Rapidly productising; interoperability / billing / siting still contested."
      movement: "evolving"

    - name: "Transmission Network (AC grid)"
      evolution: "Commodity"
      position: 0.92
      visibility: 0.50
      depends_on: ["Transmission Capex (locked-in assets)", "HVDC Interconnector"]
      notes: "Century-old utility — but decarbonisation demands massive reinforcement."
      movement: "inertia"

    - name: "HVDC Interconnector"
      evolution: "Product"
      position: 0.65
      visibility: 0.48
      depends_on: ["Transmission Capex (locked-in assets)"]
      notes: "Mature product (IFA2, NSL); project pipeline long."
      movement: "none"

    - name: "Transmission Capex (locked-in assets)"
      evolution: "Commodity"
      position: 0.85
      visibility: 0.46
      depends_on: []
      notes: "Decades-duration regulated asset base; hard to rewind."
      movement: "inertia"

    - name: "Central Production / Dispatch"
      evolution: "Commodity"
      position: 0.82
      visibility: 0.44
      depends_on: ["Fossil Generation", "Gas CCGT", "Nuclear", "Utility-Scale Renewable", "Utility-Scale Solar PV", "Biomass / W2E", "Pumped Hydro", "Grid-Scale IBR Control"]
      notes: "Merit-order dispatch is standard; inertia from fossil assumption embedded in software."
      movement: "inertia"

    - name: "Grid-Scale Inverter-Based Resource Control"
      evolution: "Custom"
      position: 0.38
      visibility: 0.42
      depends_on: ["Utility-Scale Solar PV", "Utility-Scale Renewable", "Electrical Storage (Li-ion)"]
      notes: "Grid-forming inverters and synthetic inertia are still bespoke / vendor-specific — Jul-2022 it is the frontier."
      movement: "evolving"

    - name: "Frequency / Voltage Stability"
      evolution: "Product → Commodity"
      position: 0.78
      visibility: 0.40
      depends_on: ["Transmission Network (AC grid)"]
      notes: "Classical power-system engineering — but increasingly strained by IBR share."
      movement: "none"

    - name: "Flexibility / Firming Services"
      evolution: "Custom"
      position: 0.30
      visibility: 0.38
      depends_on: ["Storage (aggregate need)", "Gas CCGT", "Grid-Scale IBR Control"]
      notes: "Flex markets (DSR, aggregators, distributed flex) still custom-stage."
      movement: "evolving"

    - name: "Capacity-Intensive Capex (asset lock-in)"
      evolution: "Commodity"
      position: 0.88
      visibility: 0.36
      depends_on: []
      notes: "Long-lived asset problem — 30-60 year payback locks today's decisions in for decades."
      movement: "inertia"

    - name: "Fossil Generation (coal / gas peaker)"
      evolution: "Commodity"
      position: 0.96
      visibility: 0.32
      depends_on: ["Coal Supply", "Natural Gas Supply", "Capacity-Intensive Capex"]
      notes: "Utility at Jul 2022 — and politically the thing that keeps the lights on while gas is scarce."
      movement: "inertia"

    - name: "Gas CCGT (combined cycle)"
      evolution: "Commodity"
      position: 0.92
      visibility: 0.30
      depends_on: ["Natural Gas Supply", "Capacity-Intensive Capex"]
      notes: "Standard flexible thermal — but Jul-2022 gas price makes it the setter of marginal wholesale price."
      movement: "inertia"

    - name: "Nuclear (existing fleet)"
      evolution: "Product → Commodity"
      position: 0.78
      visibility: 0.28
      depends_on: ["Uranium Supply", "Capacity-Intensive Capex"]
      notes: "Operating fleet is mature but ageing; life-extension is the live question."
      movement: "none"

    - name: "Nuclear (SMR / new build)"
      evolution: "Custom"
      position: 0.22
      visibility: 0.26
      depends_on: ["Uranium Supply", "Capacity-Intensive Capex"]
      notes: "SMR designs pre-FOAK in Jul-2022; new GW-scale (HPC) still under construction."
      movement: "evolving"

    - name: "Utility-Scale Renewable (wind onshore / offshore)"
      evolution: "Product → Commodity"
      position: 0.72
      visibility: 0.30
      depends_on: ["Critical Minerals", "Capacity-Intensive Capex"]
      notes: "Onshore wind effectively commodity; offshore wind productised with active vendor competition."
      movement: "evolving"

    - name: "Utility-Scale Solar PV"
      evolution: "Product → Commodity"
      position: 0.72
      visibility: 0.28
      depends_on: ["Critical Minerals", "Capacity-Intensive Capex"]
      notes: "Module price at historical lows; land + grid access is the binding constraint, not tech."
      movement: "evolving"

    - name: "Solar Microgeneration (distributed rooftop)"
      evolution: "Product"
      position: 0.55
      visibility: 0.30
      depends_on: ["Critical Minerals"]
      notes: "Product with strong retail channels; network-integration lag."
      movement: "evolving"

    - name: "Community / Microgrid Generation"
      evolution: "Custom"
      position: 0.32
      visibility: 0.26
      depends_on: ["Solar Microgeneration", "Electrical Storage (Li-ion)", "Distribution Network (DSO)"]
      notes: "Pilot-heavy — regulation and DSO integration are the blockers."
      movement: "evolving"

    - name: "Biomass / Waste-to-Energy"
      evolution: "Product"
      position: 0.60
      visibility: 0.24
      depends_on: ["Capacity-Intensive Capex"]
      notes: "Mature but contested on LCA grounds."
      movement: "none"

    - name: "Geothermal / Tidal / Wave"
      evolution: "Custom"
      position: 0.25
      visibility: 0.20
      depends_on: []
      notes: "Niche / bespoke; wave + tidal stuck in demo phase."
      movement: "evolving"

    - name: "Storage (aggregate need)"
      evolution: "Custom"
      position: 0.35
      visibility: 0.52
      depends_on: ["Electrical Storage (Li-ion)", "Electrical Storage (flow)", "Hydrogen Storage", "Pumped Hydro", "Compressed Air / Thermal", "Strategic Reserve"]
      notes: "The pivot question of the whole map — Jul 2022 the system has nowhere near enough firming for >60% VRE."
      movement: "evolving"

    - name: "Electrical Storage (Li-ion grid battery)"
      evolution: "Product"
      position: 0.58
      visibility: 0.50
      depends_on: ["Critical Minerals"]
      notes: "Costs collapsing; grid-battery is productised and building fast."
      movement: "evolving"

    - name: "Electrical Storage (flow battery)"
      evolution: "Custom"
      position: 0.28
      visibility: 0.48
      depends_on: ["Critical Minerals"]
      notes: "Vanadium redox etc. — niche, long-duration edge."
      movement: "evolving"

    - name: "Hydrogen Storage / H2 Production (electrolyser)"
      evolution: "Custom"
      position: 0.28
      visibility: 0.46
      depends_on: ["Utility-Scale Renewable", "Utility-Scale Solar PV"]
      notes: "Green H2 is custom in Jul 2022 — costly electrolysers, uncertain offtake, huge political bet."
      movement: "evolving"

    - name: "Pumped Hydro (potential energy)"
      evolution: "Commodity"
      position: 0.80
      visibility: 0.44
      depends_on: []
      notes: "Century-old utility; new sites geo-constrained."
      movement: "none"

    - name: "Compressed Air / Thermal Storage"
      evolution: "Custom"
      position: 0.25
      visibility: 0.42
      depends_on: []
      notes: "CAES + high-temp thermal (e.g., Malta, Highview) at demo / early-product stage."
      movement: "evolving"

    - name: "Strategic Reserve (gas / oil inventory)"
      evolution: "Commodity"
      position: 0.82
      visibility: 0.40
      depends_on: ["Natural Gas Supply", "Coal Supply"]
      notes: "Re-politicised in Jul 2022 — EU gas-storage targets just legislated."
      movement: "inertia"

    - name: "Natural Gas Supply (pipeline / LNG)"
      evolution: "Commodity"
      position: 0.88
      visibility: 0.24
      depends_on: ["Russian Gas Exposure", "LNG Import Terminal", "Geopolitical Risk"]
      notes: "Commodity market in shock — Jul 2022 TTF ~€170/MWh."
      movement: "inertia"

    - name: "Russian Gas Exposure"
      evolution: "Commodity"
      position: 0.90
      visibility: 0.22
      depends_on: ["Geopolitical Risk"]
      notes: "Jul 2022 — Nord Stream 1 already down to 40%, Europe scrambling to substitute."
      movement: "inertia"

    - name: "LNG Import Terminal (capex-heavy)"
      evolution: "Product"
      position: 0.55
      visibility: 0.20
      depends_on: ["Capacity-Intensive Capex"]
      notes: "FSRUs accelerating (German Wilhelmshaven contract just signed); fixed terminals take 3-5 years."
      movement: "evolving"

    - name: "Coal Supply"
      evolution: "Commodity"
      position: 0.85
      visibility: 0.18
      depends_on: []
      notes: "Utility; counter-intuitively seeing a Jul-2022 revival in EU as gas substitutes."
      movement: "none"

    - name: "Uranium Supply"
      evolution: "Commodity"
      position: 0.70
      visibility: 0.16
      depends_on: []
      notes: "Small, concentrated market (Kazakhstan, Russia, Canada) — geopolitical tail."
      movement: "none"

    - name: "Critical Minerals (Li / Co / Ni / REE)"
      evolution: "Custom → Product"
      position: 0.40
      visibility: 0.16
      depends_on: []
      notes: "Refining is concentrated (China); Jul-2022 Li prices at peak. Supply-chain aware but not yet transparent."
      movement: "evolving"

    - name: "Supply-Chain Awareness (energy system)"
      evolution: "Custom"
      position: 0.25
      visibility: 0.64
      depends_on: ["Scope 1-3 Emissions Disclosure", "Critical Minerals", "Natural Gas Supply", "Russian Gas Exposure"]
      notes: "Jul 2022 — most utilities do NOT have n-tier visibility of their fuel / mineral supply."
      movement: "evolving"

    - name: "Scope 1-3 Emissions Disclosure"
      evolution: "Custom"
      position: 0.32
      visibility: 0.62
      depends_on: ["CO2 MRV (emissions measurement)"]
      notes: "TCFD + ISSB emerging but Scope 3 is still bespoke."
      movement: "evolving"

    - name: "Externality Pricing (health / climate)"
      evolution: "Genesis"
      position: 0.20
      visibility: 0.58
      depends_on: ["CO2 MRV (emissions measurement)", "Carbon Price"]
      notes: "Health co-benefits of decarbonisation not yet priced into wholesale signal."
      movement: "evolving"

    - name: "Just-Transition / Fuel Poverty"
      evolution: "Custom"
      position: 0.28
      visibility: 0.60
      depends_on: ["Price Cap / Tariff Regulation", "Subsidies"]
      notes: "Acute in Jul 2022 — UK price-cap uplift forthcoming Oct; EU state-aid derogations active."
      movement: "evolving"

    - name: "Geopolitical Risk (Russia / Ukraine)"
      evolution: "Commodity"
      position: 0.80
      visibility: 0.42
      depends_on: []
      notes: "The exogenous shock that defines the Jul-2022 map."
      movement: "none"

  analysis:
    opportunities:
      - "Commoditise flexibility: storage-as-a-service + aggregator DSR. The market layer for flex is still Custom; first movers shape the protocol."
      - "Industrialise EV charging + local reinforcement on shared standards — the DSO choke point."
      - "Scale grid-scale Li-ion storage (Product-stage) aggressively to displace gas peakers."
      - "Stand up a proper supply-chain awareness capability for fuels + critical minerals — Jul 2022 shows the cost of not knowing."
      - "Productise real-time CO2 MRV + Scope 3 disclosure; lock in the schema before big-4 accountants do."
      - "Make CfD / IRA-style subsidy the new commodity — auction-based procurement is now mature enough to be default."
      - "Accelerate grid-forming inverter / IBR control — the custom-stage layer that will matter at 80% VRE penetration."

    threats:
      - "Russian-gas cliff + LNG dependence: Jul 2022's acute risk — substituting one commodity dependence for another."
      - "Transmission + DSO reinforcement debt: decarbonisation speed bottleneck is network queue, not generation."
      - "Locked-in fossil capex: new CCGT / peaker decisions in Jul 2022 will still be running in 2050."
      - "Critical-minerals concentration risk — Chinese refining dominance is the new OPEC."
      - "Retail supplier collapse (UK pattern): wholesale-retail hedge model breaking under volatility."
      - "Inverter-based resource control not yet solved: system stability risk rises non-linearly with VRE share."
      - "Externality pricing still genesis: merit-order still dispatches on fuel cost, not social cost — wrong signal at the top of the stack."
      - "Just-transition / fuel-poverty politics could derail net-zero commitment if affordability not solved this winter."

    inertia_points:
      - component: "Gas CCGT (combined cycle)"
        reason: "Existing fleet has decades of remaining economic life; Jul-2022 high gas price paradoxically makes them the marginal price-setter."
      - component: "Natural Gas Supply (pipeline / LNG)"
        reason: "Pipeline infrastructure is multi-decade sunk; LNG terminals add years, not months, of alternative supply."
      - component: "Transmission Network (AC grid)"
        reason: "Regulated asset base with 40-year depreciation; reinforcement queue is 5-10 years long."
      - component: "Central Production / Dispatch"
        reason: "Dispatch software, operator training, and market codes were all written around synchronous-thermal assumptions."
      - component: "Today's Consumer Behaviour (flick-the-switch)"
        reason: "Generations of habit that energy is invisible; hard to retrain at scale without price pain."
      - component: "Distribution Network (DSO)"
        reason: "Century-old radial network design; active-network management still custom / pilot."
      - component: "Capacity-Intensive Capex (asset lock-in)"
        reason: "30-60 year payback cycles guarantee that Jul-2022 capex decisions define the 2050s energy mix."
      - component: "Russian Gas Exposure"
        reason: "Not a technical lock-in but a political/commercial one that unwound in 2022 is still working through the system."

  recommendations:
    immediate:
      - action: "Re-price wholesale risk. Treat Jul-2022 gas price as the new regime; mark-to-market all CCGT-dispatch assumptions in operator / retailer models."
        rationale: "The old hedge-book cost manager is broken; acting on stale assumptions destroys retailers."
      - action: "Stand up cross-ministry gas-storage + LNG-capacity war-room; mandate winter storage targets."
        rationale: "The commodity chain is broken; immediate reserve policy is the only short-cycle lever."
      - action: "Accelerate DSR + demand-side flexibility for this winter; make it a national capability, not a retailer afterthought."
        rationale: "Fastest MW of firming available is behind the meter."
      - action: "Protect fuel-poor households with a lump-sum mechanism — not by suppressing the wholesale price signal."
        rationale: "Price signal is the disruption tool; suppressing it slows the transition."
    short_term:
      - action: "Deploy 20-30 GWh of utility Li-ion over 18 months to displace gas peakers in balancing + ancillary markets."
        rationale: "Li-ion is Product-stage, capex is falling, and the flex market is still Custom — first movers win."
      - action: "Industrialise EV charging + local reinforcement with shared standards (OCPP, smart-charging mandates)."
        rationale: "DSO queue is the 2025 bottleneck; acting in 2022 unblocks EVs and rooftop PV in parallel."
      - action: "Launch a real-time Scope 1-3 MRV programme for utilities + large off-takers; mandate from 2024."
        rationale: "CO2 is about to become the second price signal — the system needs real data, not annual estimates."
      - action: "Build supply-chain awareness (n-tier visibility) for fuels + critical minerals, starting with grid-battery cathode supply."
        rationale: "Jul-2022 shock taught us not knowing is expensive; critical-minerals is the next shock."
      - action: "Reform capacity market rules to pay for storage + DSR on symmetric terms with thermal."
        rationale: "Current capacity markets were designed around CCGT economics; need re-drafting for clean firm power."
    long_term:
      - action: "Invest pioneers into Genesis / Custom layers: Hydrogen, grid-forming IBR, long-duration storage, externality pricing."
        rationale: "These are where 2035-2050 strategic differentiation lives; cannot be bought in off-the-shelf."
      - action: "Build policy + market mechanism for externality pricing — beyond carbon, include health and biodiversity."
        rationale: "Until full-cost accounting is product-stage, the merit order dispatches on the wrong signal."
      - action: "Commit to 3-5x transmission build-out; reform planning consent + connection queue reform as national mission."
        rationale: "Grid is the single biggest decarbonisation constraint; capex-heavy and slow."
      - action: "Treat grid-forming IBR + synthetic inertia as a national-champion programme — the 'operating system' of the decarbonised grid."
        rationale: "At >70% VRE, synchronous-thermal assumptions fail; whoever owns the IBR control schema owns the stability layer."
      - action: "Pilot community + microgrid as serious consumer proposition (not PR exercise); regulatory sandbox at scale."
        rationale: "Tomorrow's consumer behaviour needs a place to land — without it, self-generation stays product-niche."
```

---

## 5. Answer to the user's three specific questions

### 5.1 Where is disruption most likely?

The **upper-left-to-middle band** of the map — where high-visibility, low-evolution components live — is where Jul-2022 disruption concentrates. Specifically:

| Zone | Components | Why disruption |
|---|---|---|
| **Consumer-behaviour pivot** | Tomorrow's consumer behaviour, self-generation, ToU / DSR, sustainability expectation, literacy | Very visible, low-evolution — every % gained is a % off the fossil backbone. |
| **Storage + flex** | Storage-aggregate, Li-ion grid battery, H2 electrolyser, flow battery, flexibility / firming services, grid-forming IBR control | Missing capability for a 70%+ VRE grid; Custom-stage frontier; large addressable market. |
| **CO2 + externality apparatus** | Full-cost accounting, externality pricing, CBAM, Scope 1-3 disclosure, CO2 MRV | Signal layer is wrong — fixing it reshapes every downstream decision. |
| **Supply-chain awareness** | Energy-system supply-chain awareness, critical minerals | Jul-2022 shock revealed blindness; standardisation about to arrive. |
| **Market reform** | Capacity market, balancing/ancillary services, carbon price, PPA variants | Being rewritten under pressure; first movers shape the next 20 years. |

### 5.2 Where is infrastructure locked-in?

The **lower-right** of the map (commodity, low-visibility) — this is the multi-decade asset base:

- **Fossil stack:** fossil generation, gas CCGT, natural gas supply (pipeline + LNG), coal, strategic reserves — all capex-amortised over 30+ years.
- **Network:** transmission AC grid, DSO, transmission capex, local reinforcement — regulated asset base, century of sunk cost.
- **Dispatch / market software:** central production/dispatch, grid code, frequency/voltage stability — built around synchronous-thermal assumptions.
- **Consumer habit:** today's flick-the-switch behaviour — a behavioural, not physical, lock-in.
- **Capacity-intensive capex generally:** any asset ordered in Jul 2022 locks the 2050 mix.

The paradox: **much of this lock-in is commodity-stage (right side) — i.e., mature and working**. That's why it's so hard to displace: these components aren't failing; they are doing their job. They are just doing the **wrong** job for a net-zero target.

### 5.3 What does the supply-chain awareness + externality picture look like?

Mostly **missing**. Both layers are in the **Custom / Genesis range**:

- **Supply-Chain Awareness (energy system)** at evolution ~0.25 — most utilities in Jul 2022 had no n-tier visibility of their fuel sources, LNG shipping, critical-mineral refining.
- **Scope 1-3 disclosure** at ~0.32 — Scope 1/2 is converging, Scope 3 still bespoke.
- **Externality pricing** at ~0.20 — health + biodiversity costs not in the wholesale merit order.
- **Full-cost accounting** at ~0.22 — no standard for loading externalities onto dispatch.
- **CBAM** at ~0.18 — Jul 2022 is still pre-transitional phase.
- **CO2 MRV** at ~0.45 — product-ish for Scope 1 but real-time / Scope 3 still custom.

Strategic read: **the signal layer is the weakest part of the stack**. The physical infrastructure works; the markets clear; the regulator acts; but the *information* that should be steering all of this — what is in the chain, what harm it causes, how to price both — is still custom-built. This is where a disciplined actor gains asymmetric advantage through Jul 2022 onwards.

---

## 6. Quantitative cross-check (Step 6)

Applying evolution scoring (Ubiquity × Certainty), differentiation pressure D(v) = visibility × (1 − evolution), and commodity leverage K(v) = (1 − visibility) × evolution:

| Component | Vis. | Evol. | D(v) | K(v) | Verdict |
|---|---|---|---|---|---|
| Gas CCGT | 0.30 | 0.92 | 0.02 | **0.64** | Utility — consume, do not build. |
| Utility Solar PV | 0.28 | 0.72 | 0.08 | **0.52** | Commoditising — auction-based procurement. |
| Li-ion Grid Battery | 0.50 | 0.58 | 0.21 | 0.29 | Product — buy with scale; competitive edge fading fast. |
| Hydrogen / Electrolyser | 0.46 | 0.28 | **0.33** | 0.39 | Custom — bet on if strategic; niche else. |
| Tomorrow's Consumer Behaviour | 0.88 | 0.18 | **0.72** | 0.02 | Differentiator — highly visible, not commoditised — **build capability**. |
| Supply-Chain Awareness | 0.64 | 0.25 | **0.48** | 0.27 | Invest — visibility gap is the 2022 lesson. |
| Full-Cost Accounting | 0.70 | 0.22 | **0.55** | 0.21 | Invest — shape the schema. |
| Carbon Price | 0.66 | 0.55 | 0.30 | 0.15 | Product — track, integrate, don't build. |
| Storage (aggregate need) | 0.52 | 0.35 | 0.34 | 0.31 | Custom/moderate — pick your chemistry. |
| EV Charging Infra | 0.52 | 0.50 | 0.26 | 0.24 | Product — standards/land-acquisition play. |
| Transmission AC grid | 0.50 | 0.92 | 0.04 | **0.46** | Commodity — but with inertia — run better, extend. |

### High dependency risks

| Dependency (a → b) | vis(a) | 1−evol(b) | R(a,b) | Level |
|---|---|---|---|---|
| Consumer → Retail Supply → Wholesale Price | 0.80 | (mature) | 0.10 | Low technical, high political. |
| Flexibility / Firming → Storage | 0.38 | 0.65 | **0.25** | Moderate — storage immaturity constrains flex. |
| Wholesale Price → Gas CCGT → Russian Gas | 0.76 | 0.10 | 0.08 technical, **political 0.76 × 0.80** = 0.61 | **High geopolitical** — the key Jul-2022 dependency risk. |
| Net-Zero Policy → CO2 MRV | 0.62 | 0.55 | 0.34 | Moderate — measurement gap undermines policy. |
| Utility-Scale Renewable → Critical Minerals | 0.30 | 0.60 | 0.18 | Low visibility → moderate exposure — watch. |
| Tomorrow's Consumer Behaviour → Smart Meter → DSO | 0.88 | 0.12 | 0.11 | Low technical, **high adoption** risk. |

The numbers confirm the qualitative read: **the hardest bets are the most-visible, least-mature components (tomorrow's behaviour, flex / firm, externality pricing, supply-chain awareness)** — and the greatest dependency risk in Jul-2022 is the single commodity dependence on Russian-origin gas at the bottom of the stack.

---

## 7. Gameplay & climate cross-reference (Step 5)

### Climatic patterns active in Jul 2022

- **Everything evolves** — storage, IBR control, MRV, CBAM, public-good framing all in motion.
- **Past success breeds inertia** — the fossil-CCGT merit-order, the synchronous-grid dispatch software, the "energy is invisible" consumer habit.
- **Shocks happen** — Russian gas cut-off is *the* shock; it has pulled forward decisions by 5-10 years.
- **Efficiency enables innovation** — falling solar + battery costs created the affordability window that policy (IRA) is now closing on.
- **Commoditisation enables new sources of worth** — cheap solar + storage enables the next layer (microgrids, V2G, green H2) that couldn't exist before.
- **Higher-order systems create new worth** — integrated DER + DSO + home-flex is the higher-order layer being built on commoditised panels + batteries.
- **Component evolves through inertia barrier** — Li-ion, offshore wind, solar PV all pushed over the chasm; fuel-cell and H2 still on the left.
- **Co-evolution** — EV uptake ↔ charging infra ↔ DSO reinforcement ↔ time-of-use tariffs.
- **Competitors change the game** — Tesla's storage-plus-energy-retail play; Octopus Agile; Enel X aggregator — all reshaping market mechanics.

### Applicable gameplays

- **Commoditisation play** on storage + EV charging — shared protocols, utility pricing.
- **Open source / open data** play on CO2 MRV + Scope 3 — shape the schema, lock competitors to it.
- **Raising barriers to entry** via CBAM + certification — legitimate protection for mature low-C producers.
- **Pig in a poke** on internal flexibility / DSR platforms — build ahead of market.
- **Harvesting** in mature stacks — run gas CCGT as cash cow while exiting.
- **First Mover** on grid-forming IBR control — the next control-layer monopoly.
- **Exploiting constraint** on skilled labour for electrification + network reinforcement (the 2025 bottleneck).

### Doctrine weaknesses most firms will show

- Weak **Know your users** — especially household fuel-poor and industrial off-takers in hard-to-abate sectors.
- Weak **Use appropriate methods** — applying product-stage procurement to genesis-stage H2 or IBR control.
- Weak **Think small** — over-centralising flexibility, not enough at the DSO + behind-the-meter edge.
- Weak **Be transparent** — Scope 3 + supply-chain data held as competitive info when it should be shared infrastructure.

---

## 8. Notes on limitations

- Positions are qualitative Jul-2022 reads. A quantitative U × C scoring pass would tighten each by ±0.05 and is a natural next step.
- The map is generic (UK-EU-centric); US positioning shifts markedly once IRA takes effect (Aug 2022 onwards) — especially subsidies, H2, CBAM.
- Movement arrows are 3-5 year expectations; the Jul-2022 shock can accelerate or reverse individual components dramatically.
- The gas-CCGT wholesale-price-setter dynamic is treated here as inertia; it is also the proximate disruption signal — the map could equally mark it "disrupting" in 2022.
- The "energy-as-public-good" component is partly political, not technical — its evolution depends on election outcomes, not just tech maturity.
