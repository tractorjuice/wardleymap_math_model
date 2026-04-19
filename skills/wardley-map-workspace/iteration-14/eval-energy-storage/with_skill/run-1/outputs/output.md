# Wardley Map — Electrical Energy Storage Landscape (April 2023)

## Scenario

Map the landscape of electrical energy storage — grid-scale and distributed battery storage, pumped hydro, thermal, hydrogen. Include storage technologies, deployment models, markets (frequency response, arbitrage, capacity), regulation, supply chains (battery minerals, manufacturing), and grid integration. What's differentiating vs. commoditising?

## Map (OWM)

```owm
title Electrical Energy Storage Landscape (April 2023)
style wardley

// Anchors — the users whose needs drive the map
anchor Grid Operator [0.99, 0.60]
anchor Utility / Generator [0.96, 0.55]
anchor C&I / Prosumer [0.93, 0.50]

// User-facing services / value streams
component Frequency Response Service [0.86, 0.78]
component Capacity Market Service [0.83, 0.80]
component Energy Arbitrage Service [0.80, 0.60]
component Ancillary Services (reserve, black start) [0.77, 0.65]
component Behind-the-Meter Storage Service [0.74, 0.55]

// Deployment models
component Grid-Scale BESS Project [0.68, 0.62]
component Utility Pumped Hydro Project [0.66, 0.90]
component Distributed / Residential Storage [0.64, 0.58]
component Co-located Storage + Renewables [0.62, 0.45]
component Long-Duration Storage Pilot [0.60, 0.20]

// Storage technologies — batteries
component Li-ion NMC Battery System [0.55, 0.72]
component Li-ion LFP Battery System [0.53, 0.70]
component Sodium-ion Battery [0.50, 0.22]
component Flow Battery (Vanadium / Iron) [0.48, 0.30]
component Iron-air / Metal-air Battery [0.46, 0.12]

// Storage technologies — non-battery
component Pumped Hydro Storage [0.58, 0.92]
component Compressed Air (CAES) [0.44, 0.35]
component Thermal Storage (molten salt, bricks) [0.42, 0.30]
component Green Hydrogen Storage [0.40, 0.18]
component Gravity Storage [0.38, 0.15]

// Integration & control layer
component Battery Management System (BMS) [0.50, 0.68]
component Power Conversion / Inverter [0.48, 0.78]
component EMS / Storage Dispatch Software [0.52, 0.55]
component SCADA / Grid Telemetry [0.36, 0.82]
component Market Bidding Platform [0.58, 0.50]

// Markets & regulation
component Wholesale Electricity Market [0.56, 0.88]
component Capacity Market Rules [0.60, 0.72]
component FERC Order 841 / GB Dynamic Services [0.58, 0.62]
component Interconnection / Grid-Code Compliance [0.42, 0.70]
component Safety & Fire Codes (UL9540, NFPA855) [0.36, 0.55]
component IRA / EU Green Deal Subsidy [0.40, 0.35]

// Supply chain — minerals & cells
component Lithium Refining [0.30, 0.58]
component Lithium Mining [0.25, 0.75]
component Cobalt / Nickel Supply [0.24, 0.80]
component Cell Manufacturing (Gigafactory) [0.32, 0.55]
component Battery Module / Pack Assembly [0.34, 0.72]
component Cathode / Anode Active Materials [0.30, 0.45]
component Battery Recycling / Second-Life [0.32, 0.20]

// Platform / utility layer
component Cloud Analytics Platform [0.18, 0.88]
component AI Forecasting (price, load, weather) [0.20, 0.40]
component Cybersecurity for OT [0.16, 0.45]

// Foundational knowledge & utilities
component Electrochemistry R&D [0.10, 0.38]
component Grid Physics / Power Systems Knowledge [0.08, 0.92]
component Electricity (transmission) [0.06, 0.96]

// Dependencies
Grid Operator->Frequency Response Service
Grid Operator->Capacity Market Service
Grid Operator->Ancillary Services (reserve, black start)
Utility / Generator->Energy Arbitrage Service
Utility / Generator->Capacity Market Service
Utility / Generator->Ancillary Services (reserve, black start)
C&I / Prosumer->Behind-the-Meter Storage Service
C&I / Prosumer->Energy Arbitrage Service

Frequency Response Service->Grid-Scale BESS Project
Frequency Response Service->Market Bidding Platform
Capacity Market Service->Grid-Scale BESS Project
Capacity Market Service->Utility Pumped Hydro Project
Capacity Market Service->Capacity Market Rules
Energy Arbitrage Service->Grid-Scale BESS Project
Energy Arbitrage Service->Co-located Storage + Renewables
Energy Arbitrage Service->Market Bidding Platform
Ancillary Services (reserve, black start)->Utility Pumped Hydro Project
Ancillary Services (reserve, black start)->Grid-Scale BESS Project
Behind-the-Meter Storage Service->Distributed / Residential Storage

Grid-Scale BESS Project->Li-ion LFP Battery System
Grid-Scale BESS Project->Li-ion NMC Battery System
Grid-Scale BESS Project->EMS / Storage Dispatch Software
Grid-Scale BESS Project->Power Conversion / Inverter
Grid-Scale BESS Project->Interconnection / Grid-Code Compliance
Grid-Scale BESS Project->Safety & Fire Codes (UL9540, NFPA855)
Grid-Scale BESS Project->IRA / EU Green Deal Subsidy

Utility Pumped Hydro Project->Pumped Hydro Storage
Utility Pumped Hydro Project->Interconnection / Grid-Code Compliance
Utility Pumped Hydro Project->Grid Physics / Power Systems Knowledge

Distributed / Residential Storage->Li-ion LFP Battery System
Distributed / Residential Storage->Power Conversion / Inverter
Distributed / Residential Storage->Safety & Fire Codes (UL9540, NFPA855)

Co-located Storage + Renewables->Li-ion LFP Battery System
Co-located Storage + Renewables->EMS / Storage Dispatch Software
Co-located Storage + Renewables->Interconnection / Grid-Code Compliance

Long-Duration Storage Pilot->Flow Battery (Vanadium / Iron)
Long-Duration Storage Pilot->Iron-air / Metal-air Battery
Long-Duration Storage Pilot->Green Hydrogen Storage
Long-Duration Storage Pilot->Thermal Storage (molten salt, bricks)
Long-Duration Storage Pilot->Compressed Air (CAES)
Long-Duration Storage Pilot->Gravity Storage

Li-ion NMC Battery System->Battery Management System (BMS)
Li-ion NMC Battery System->Battery Module / Pack Assembly
Li-ion LFP Battery System->Battery Management System (BMS)
Li-ion LFP Battery System->Battery Module / Pack Assembly
Sodium-ion Battery->Electrochemistry R&D
Sodium-ion Battery->Cell Manufacturing (Gigafactory)
Flow Battery (Vanadium / Iron)->Electrochemistry R&D
Iron-air / Metal-air Battery->Electrochemistry R&D

Pumped Hydro Storage->Grid Physics / Power Systems Knowledge
Compressed Air (CAES)->Grid Physics / Power Systems Knowledge
Thermal Storage (molten salt, bricks)->Electrochemistry R&D
Green Hydrogen Storage->Electrochemistry R&D

Battery Module / Pack Assembly->Cell Manufacturing (Gigafactory)
Cell Manufacturing (Gigafactory)->Cathode / Anode Active Materials
Cell Manufacturing (Gigafactory)->Cobalt / Nickel Supply
Cathode / Anode Active Materials->Lithium Refining
Lithium Refining->Lithium Mining
Battery Recycling / Second-Life->Cell Manufacturing (Gigafactory)

EMS / Storage Dispatch Software->AI Forecasting (price, load, weather)
EMS / Storage Dispatch Software->SCADA / Grid Telemetry
EMS / Storage Dispatch Software->Cloud Analytics Platform
Market Bidding Platform->Wholesale Electricity Market
Market Bidding Platform->AI Forecasting (price, load, weather)
SCADA / Grid Telemetry->Cybersecurity for OT

Battery Management System (BMS)->Power Conversion / Inverter
Power Conversion / Inverter->Electricity (transmission)

Capacity Market Rules->Wholesale Electricity Market
FERC Order 841 / GB Dynamic Services->Wholesale Electricity Market
Interconnection / Grid-Code Compliance->Grid Physics / Power Systems Knowledge

AI Forecasting (price, load, weather)->Cloud Analytics Platform

// Strategic movement arrows
evolve Sodium-ion Battery 0.50
evolve Iron-air / Metal-air Battery 0.35
evolve Green Hydrogen Storage 0.35
evolve Li-ion LFP Battery System 0.85
evolve AI Forecasting (price, load, weather) 0.65
evolve Battery Recycling / Second-Life 0.45
evolve Long-Duration Storage Pilot 0.45

note Differentiation zone [0.55, 0.20]
note Industrialising fast [0.55, 0.72]
note Utility commodity [0.12, 0.92]
```

Validator output: `OK: 47 components/anchors, 71 edges — no violations.`

---

## Strategic analysis

### a. Differentiation opportunities (top 3)

Components are ranked qualitatively by `D = ν · (1 − ε)` — visible plus immature — but the call is made by stage and strategic role, not the decimal.

1. **Long-Duration Storage Pilot (Genesis)** — the most visible Genesis-band component on the map. 8–100 hour duration is the capability the grid will need as renewable penetration rises above ~60–70%, and no technology has clearly won yet. A utility or developer that can make one long-duration chemistry work at grid scale captures the incumbent position for decades. This is where capital flows for uncharted value (climatic pattern #14).
2. **EMS / Storage Dispatch Software (Product +rental, early)** — the control brain that turns generic cells into revenue. Stack-and-rack hardware is commoditising; the dispatch/optimisation layer is where revenue per MWh is actually captured. This is the classic "industrialisation below creates higher-order worth above" move (climatic pattern #10).
3. **Co-located Storage + Renewables (Custom Built)** — emerging deployment pattern where the storage is part of the solar/wind power purchase agreement rather than a separate asset. Developers who get the contractual, grid-code and dispatch-stack right here build a durable moat before the model standardises.

Honourable mention: **AI Forecasting (Custom Built)** — price/load/weather forecasting for dispatch and bidding is still bespoke at most operators and is a strong Stage II differentiator.

### b. Commodity-leverage candidates (top 3)

Components ranked qualitatively by `K = (1 − ν) · ε` — deep and mature — where the call is "rent, don't build".

1. **Electricity (transmission) (Commodity +utility)** — the ultimate utility; take it, don't re-invent it.
2. **Wholesale Electricity Market (Commodity +utility)** — the market clearing engines (PJM, ERCOT, ISO-NE, GB Balancing Mechanism) are mature utilities; integrate via existing APIs and brokers, don't re-platform.
3. **Pumped Hydro Storage (Commodity +utility)** — the technology itself is ~90 years mature. Where geography allows it, rent the existing asset or partner with the incumbent hydro operator. Don't try to innovate the physics.

Also in the "buy, don't build" bucket: **Cloud Analytics Platform**, **Power Conversion / Inverter** (hardware is dominated by SMA, Sungrow, Power Electronics, Sineng — multi-vendor Stage IV behaviour), **SCADA / Grid Telemetry**.

### c. Dependency risks (top 3)

Edges `(a, b)` where a visible user-facing component depends on a fragile foundation.

1. **Grid-Scale BESS Project → Lithium Mining / Cobalt / Nickel Supply (via cell manufacturing)** — the most important visible deployment model on the map depends on a concentrated, geopolitically exposed mineral supply (China ~70% refining; DRC cobalt). In 2022 Li carbonate prices spiked 5–10×; every BESS project's unit economics flexed by 20–40%. Single-technology, single-geography dependency is the map's biggest structural risk.
2. **EMS / Storage Dispatch Software → SCADA / Grid Telemetry → Cybersecurity for OT** — a revenue-critical software layer depends on OT-cyber practice that is still emerging (Custom Built). A single well-timed OT attack on a fleet could wipe a trading year; the dependency chain is visible in the map.
3. **Long-Duration Storage Pilot → Iron-air / Metal-air Battery (Genesis)** — pilot projects (and the utilities funding them) are betting on chemistry that has not passed the Genesis bar. There's no second source. The risk is not exotic failure — it's the chemistry never industrialising and leaving pilots as stranded assets. This is the prototype of climatic pattern #4 (multi-wave S-curves with chasms): Li-ion may be the S-curve we have, and the next curve may not arrive on schedule.

### d. Suggested gameplays

- **#15 Open Approaches** on **EMS / Storage Dispatch Software** interfaces and telemetry standards — a CNCF-style foundation for dispatch APIs accelerates Product (+rental) → Commodity (+utility), which benefits everyone who makes money in the layer above (optimisation, trading, forecasting). Don't open-source the optimiser itself (that's the moat — see #26).
- **#26 Differentiation** on **AI Forecasting** and **EMS / Storage Dispatch Software** — these are the features the grid operator and utility actually pay for and switch on.
- **#36 Directed investment** on **Sodium-ion Battery** and **Iron-air / Metal-air Battery** — both Genesis bets with plausible 3–5 year Stage II paths. Concentrate capital on 1–2 chemistries rather than spray-and-pray across all long-duration options.
- **#43 Sensing Engines (ILC)** across the **Long-Duration Storage Pilot** portfolio — run many small pilots, instrument them, harvest the emergent winner. This is the canonical climate-tech deployment pattern.
- **#29 Harvesting** on **Battery Recycling / Second-Life** — let the ecosystem of start-ups (Redwood, Li-Cycle, Ecobat) prove closed-loop chemistry and economics; acquire or tolling-partner with the winner.
- **#55 Land grab** on **Co-located Storage + Renewables** contracting patterns — developers who standardise their own co-located PPA template and grid-code compliance playbook before the market converges build a first-mover moat.
- **#56 First mover** on **IRA / EU Green Deal Subsidy** qualifying projects — regulatory windows close; the Inflation Reduction Act 45X and investment tax credits reward speed.
- **#41 Alliances** on **Lithium Refining / Cell Manufacturing (Gigafactory)** — vertical-integration alliances (automotive + storage + miner) are the standard move against the mineral-supply dependency risk.
- **#17 Co-operation** + **#18 Industrial Policy** on **Battery Recycling / Second-Life** — public-private funding pools are how this layer crosses the chasm from Genesis to Custom Built in a regulated-materials regime.
- **#30 Standards game** on **Safety & Fire Codes (UL9540, NFPA855)** — shaping the emerging standard creates a cost of transition for later entrants.

### e. Doctrine notes

- **#1 Focus on user needs** — satisfied. Three anchors cover the distinct users (grid operator, utility/generator, C&I prosumer) whose needs drive distinct services.
- **#10 Know your users** — satisfied. The three anchors represent materially different buying centres; collapsing them would hide the two-sided nature of behind-the-meter vs. grid-scale.
- **#7 Use appropriate methods** — the map spans four evolution stages; teams running Genesis long-duration pilots should not be on the same delivery cadence as teams running standardised LFP BESS projects. Structure and culture (gameplay #4) needs to mirror the axis.
- **#13 Manage inertia** — visible risks: (a) utilities' sunk-capital / political-capital inertia in thermal-fossil peakers that storage displaces (inertia form #2, #3); (b) grid operators' suitability-doubt inertia (form #11) on letting batteries provide inertia/black-start services historically done by synchronous machines. Both are exploitable wedges for an entrant.
- **#26 Optimise flow** — the interconnection queue is the map's bottleneck in both the US (MISO, CAISO, PJM queues at multi-year delays by 2023) and GB. The map implicitly routes every deployment model through Interconnection / Grid-Code Compliance; doctrine says attack the bottleneck before it becomes a strategic lock.
- Weak spot: the **Knowledge** layer — `Grid Physics / Power Systems Knowledge` and `Electrochemistry R&D` — is thin in staffing across the industry. Doctrine #21 ("There is no core — only retained talent") applies: the firms that attract and retain these specialists win the decade.

### f. Climatic context

- **#3 Everything evolves through supply and demand competition** — Li-ion has moved from the Product (+rental) stage into the Product/Commodity (+utility) boundary in under a decade. The whole map's right-hand side will thicken.
- **#4 Multi-wave evolution with chasms** — grid storage *is* a multi-wave story: pumped hydro (mature, saturated at good-geography sites), Li-ion (rapidly industrialising), and long-duration chemistries (pre-chasm). Planning on a single S-curve misses the transition dynamics.
- **#7 Characteristics change as components evolve** — the map has Genesis pilots and Commodity (+utility) electricity in the same tuple. Do not manage them the same way; do not measure them the same way.
- **#10 Higher-order systems create new worth** — commoditising the Li-ion cell (and the inverter) is what created space for the EMS / Dispatch / Forecasting / Trading layers where today's differentiation sits.
- **#13 Evolution to higher-order systems raises resource consumption** — as cells get cheaper, total deployed GWh grows faster than unit cost falls. Capacity-planning based on "storage will be a modest add" consistently under-forecasts mineral demand.
- **#14 Capital flows to new areas of value** — VC and growth capital flowed heavily into Iron-air (Form Energy), Zinc-air (Eos, e-Zinc), thermal (Malta, Antora), gravity (Energy Vault), hydrogen (ITM, Plug) through 2022. The map reflects that uncharted-zone capital attraction.
- **#15–17 Inertia** — the three inertia climatic patterns all bite: existing fossil peaker owners (sunk capital), permitting regimes that pre-date storage (regulatory inertia), and grid planners' suitability-doubt around battery-provided inertia/black start.
- **#18 (quoted by the skill) "You cannot measure evolution over time or adoption"** — keep the evolve arrows as scenarios, not forecasts.
- **#27 Product-to-utility punctuated equilibrium** — the war presently shaping the map is the Li-ion BESS war: the *cell* is over the Product/Commodity boundary, the *integrated BESS system* is still competing on features, and in 3–5 years the system layer is likely to industrialise the same way. When that happens, differentiation migrates upward to EMS, forecasting, and market-bidding — exactly where the differentiation arrows in part (a) point.

### g. Deep-placement notes

Four components were flagged for a closer look because they are strategically pivotal or had high within-component variance across the cheat-sheet rows. Notes reflect the state of public evidence through April 2023:

- **Li-ion LFP Battery System — initial cheat-sheet ε ≈ 0.68 (mid Product (+rental)). Deep placement held at 0.70.** By 2023 LFP had passed BYD, CATL, EVE, Gotion, REPT, Sungrow, Hithium, and others at scale; pack-level prices below ~$120/kWh; publication pattern was maintenance/operations/features; market ubiquity rising fast in stationary storage after the EV pivot. Rows #5 Ubiquity and #7 Publication pointed late-III / early-IV, so ε held close to the Product/Commodity boundary with an `evolve` arrow into Commodity (+utility) over 3–5 years. Not yet Stage IV because grid-scale system integration still differentiates on features (safety, density, thermal management).
- **Sodium-ion Battery — initial cheat-sheet ε ≈ 0.20 (Genesis). Held at 0.22.** By April 2023 CATL had announced, HiNa had shipped small volumes, and there was rapid publication activity — but ubiquity was still "rare" (row #5 → Stage I) and user perception was "different/exciting" (row #11 → Stage I). Rows disagreed on row #6 (certainty — rapid learning, Stage II). Held at Genesis with an `evolve` arrow to early Product over a 3-year horizon because the chemistry's emergence is unusually well-signalled.
- **Green Hydrogen Storage — initial cheat-sheet ε ≈ 0.22. Dropped to 0.18 after reflection.** High announcement volume (EU Hydrogen Bank, US IRA 45V) but near-zero industrial scale for grid storage specifically. Papers are still "describing the wonder"; costs 3–10× natural gas peaking on a delivered-energy basis; round-trip efficiency 35–45% suppresses the economic case versus batteries for anything under ~24h duration. Kept in Genesis.
- **EMS / Storage Dispatch Software — initial cheat-sheet ε ≈ 0.48 (late Custom). Lifted to 0.55 (early Product (+rental)).** Vendor landscape had matured: Fluence Mosaic, Wartsila GEMS, Habitat Energy, Modo Energy, Enoda, Stem Athena, Powin Energos — a multi-vendor field with visible feature competition. Publication pattern skewed toward comparison and case-study. Still pre-standardisation (every vendor's API is proprietary), so not yet Stage IV. Flagged as the most strategically important Stage-III component on the map.

One point on which the cheat sheet is deliberately *not* used: the **Frequency Response Service** was placed very high on visibility (ν = 0.86) not because it's graph-shallow (it isn't — it's 2 steps from Grid Operator), but because the grid-operator user thinks about it directly. That's a judgment override per SKILL.md Step 3.

### h. Caveat

Evolution placements and the `evolve` trajectories are **scenarios, not forecasts**. Wardley's climatic pattern #18 is explicit: *"you cannot measure evolution over time or adoption."* The map's purpose is to inform where to build, buy, harvest, and hedge *today* given the present landscape — not to predict 2026 market share. Re-map at least every 12 months; for the Genesis long-duration chemistries, re-map at every public data point (pilot announcements, price curves, regulatory changes). Competitor actions and climate-policy shocks can redraw the right half of this map within a single procurement cycle.

---

## Summary: what's differentiating vs. commoditising

**Commoditising (rent, don't build):**
- **Li-ion LFP cells and packs** — industrialising fast; moving from Product (+rental) to Commodity (+utility) over ~3–5 years.
- **Power conversion / inverters** — already multi-vendor Commodity (+utility).
- **Pumped hydro** — commoditised technology; only the geography is scarce.
- **Cloud analytics, SCADA, wholesale market access** — utility infrastructure.
- **Capacity / frequency / arbitrage market mechanisms themselves** — product-grade regulated structures.

**Differentiating (build, invest):**
- **EMS / dispatch software** and **AI forecasting** — where revenue-per-MWh actually gets captured.
- **Long-duration chemistries** (sodium-ion, iron-air, flow, thermal, H₂) — Genesis bets with the highest differentiation leverage; pick 1–2 and concentrate.
- **Co-located storage + renewables contracting and grid-code compliance** — Custom Built deployment patterns that will standardise soon; early movers define the template.
- **Battery recycling / second-life** — Genesis; valuable because it attacks the biggest dependency risk (mineral supply) and is regulatorily favoured.
- **Safety/fire code shaping** — standards-game play on UL9540 / NFPA855 is a durable moat where successful.

**Structural risks the map reveals:**
- Grid-scale BESS deployments depend, at three hops down, on a geographically concentrated and price-volatile mineral supply.
- Interconnection queues are the system-level bottleneck; every deployment model routes through them.
- OT cybersecurity is Custom Built under a revenue-critical software layer — a live tail risk.
