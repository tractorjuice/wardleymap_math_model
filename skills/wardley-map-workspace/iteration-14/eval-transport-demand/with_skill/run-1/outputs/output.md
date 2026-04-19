# Urban Transportation Demand and Consumer Behaviour (May 2022)

A Wardley Map of the urban mobility landscape — how city-dwellers, commuters, and municipalities choose and supply transport modes, what drives the choice (cost, time, sustainability, convenience, safety), and the supply-side operators, manufacturers, and platforms underneath.

Time anchor: **May 2022**. COVID-era habit shifts have partially settled, micromobility has scaled post-2018, ride-hail is post-IPO, EV adoption is accelerating, and most office workers have adopted some form of hybrid work.

---

## Map

```owm
title Urban Transportation Demand and Consumer Behaviour (May 2022)
style wardley

// Anchors — three user types
anchor Urban Resident [0.99, 0.55]
anchor Daily Commuter [0.97, 0.60]
anchor Municipality [0.95, 0.50]

// User-facing mode / experience components
component Get to Destination [0.90, 0.65]
component Avoid a Trip (Remote Work) [0.88, 0.55]
component Private Car Use [0.85, 0.80]
component Ride-hail Trip [0.84, 0.68]
component Public Transit Trip [0.83, 0.85]
component Shared E-scooter Trip [0.82, 0.58]
component Shared Bike Trip [0.81, 0.62]
component Walking Trip [0.80, 0.88]
component Personal Cycling Trip [0.79, 0.72]
component Taxi Trip [0.78, 0.82]
component Car Rental / Car-share Trip [0.76, 0.62]
component Delivery-to-me (avoided trip) [0.75, 0.70]

// Choice-driver layer (factors that shape mode selection)
component Trip Cost to User [0.70, 0.78]
component Trip Time / Reliability [0.69, 0.65]
component Convenience / Door-to-door Fit [0.68, 0.55]
component Perceived Safety [0.66, 0.55]
component Sustainability Preference [0.64, 0.40]
component Social / Status Signal [0.62, 0.60]

// Streets, vehicles, operators seen from the user
component Private Car (owned) [0.58, 0.80]
component Household EV [0.56, 0.52]
component Personal E-bike [0.55, 0.58]
component Personal Bicycle [0.54, 0.88]
component Ride-hail Driver Supply [0.38, 0.60]
component Transit Vehicle Fleet [0.34, 0.80]
component Shared Micromobility Fleet [0.36, 0.55]
component MaaS / Multimodal App [0.46, 0.35]
component In-car Navigation / Routing App [0.44, 0.85]
component Mobile Ticketing / Fare Payment [0.42, 0.80]

// Operator / platform layer
component Ride-hail Platform (Uber / Lyft / Bolt) [0.40, 0.68]
component Shared Micromobility Operator (Lime / Bird / Tier) [0.38, 0.55]
component Transit Authority Operations [0.36, 0.80]
component Vehicle OEM / EV Maker [0.34, 0.65]
component Remote Work Platforms (Zoom / Teams / Slack) [0.32, 0.78]
component E-commerce / Delivery Networks [0.30, 0.72]

// City, infra and deep supply
component Street & Curb Design [0.26, 0.55]
component Bike / Bus Lane Allocation [0.24, 0.50]
component Municipal Permits & Regulation [0.14, 0.55]
component Congestion / Low-Emission Zone Policy [0.20, 0.35]
component Parking Supply & Pricing [0.19, 0.72]
component Autonomous Driving Stack [0.17, 0.18]
component EV Charging Network [0.15, 0.45]
component Road Network & Maintenance [0.13, 0.88]
component Fuel / Energy Supply [0.11, 0.92]
component Telematics / IoT on Vehicles [0.10, 0.70]
component Mapping & Routing APIs [0.08, 0.90]
component Mobile Connectivity (4G / 5G) [0.07, 0.92]
component GNSS / GPS [0.06, 0.95]
component Payment Rails [0.05, 0.92]
component Cloud Utilities [0.04, 0.93]

// User dependencies
Urban Resident->Get to Destination
Urban Resident->Avoid a Trip (Remote Work)
Daily Commuter->Get to Destination
Daily Commuter->Avoid a Trip (Remote Work)
Municipality->Get to Destination
Municipality->Street & Curb Design
Municipality->Congestion / Low-Emission Zone Policy

// Mode choice
Get to Destination->Private Car Use
Get to Destination->Ride-hail Trip
Get to Destination->Public Transit Trip
Get to Destination->Shared E-scooter Trip
Get to Destination->Shared Bike Trip
Get to Destination->Walking Trip
Get to Destination->Personal Cycling Trip
Get to Destination->Taxi Trip
Get to Destination->Car Rental / Car-share Trip
Get to Destination->Delivery-to-me (avoided trip)
Avoid a Trip (Remote Work)->Remote Work Platforms (Zoom / Teams / Slack)
Avoid a Trip (Remote Work)->Delivery-to-me (avoided trip)
Delivery-to-me (avoided trip)->E-commerce / Delivery Networks

// Choice drivers influence every mode (representative edges)
Private Car Use->Trip Cost to User
Private Car Use->Trip Time / Reliability
Private Car Use->Convenience / Door-to-door Fit
Private Car Use->Social / Status Signal
Ride-hail Trip->Trip Cost to User
Ride-hail Trip->Trip Time / Reliability
Ride-hail Trip->Convenience / Door-to-door Fit
Public Transit Trip->Trip Cost to User
Public Transit Trip->Trip Time / Reliability
Public Transit Trip->Sustainability Preference
Shared E-scooter Trip->Trip Cost to User
Shared E-scooter Trip->Convenience / Door-to-door Fit
Shared E-scooter Trip->Perceived Safety
Shared Bike Trip->Convenience / Door-to-door Fit
Shared Bike Trip->Sustainability Preference
Walking Trip->Perceived Safety
Personal Cycling Trip->Perceived Safety
Personal Cycling Trip->Sustainability Preference
Taxi Trip->Trip Cost to User
Car Rental / Car-share Trip->Trip Cost to User

// Mode -> vehicles / operators
Private Car Use->Private Car (owned)
Private Car Use->Household EV
Ride-hail Trip->Ride-hail Platform (Uber / Lyft / Bolt)
Ride-hail Trip->Ride-hail Driver Supply
Ride-hail Trip->In-car Navigation / Routing App
Public Transit Trip->Transit Vehicle Fleet
Public Transit Trip->Transit Authority Operations
Public Transit Trip->Mobile Ticketing / Fare Payment
Shared E-scooter Trip->Shared Micromobility Fleet
Shared E-scooter Trip->Shared Micromobility Operator (Lime / Bird / Tier)
Shared Bike Trip->Shared Micromobility Fleet
Shared Bike Trip->Shared Micromobility Operator (Lime / Bird / Tier)
Personal Cycling Trip->Personal Bicycle
Personal Cycling Trip->Personal E-bike
Taxi Trip->Ride-hail Driver Supply
Car Rental / Car-share Trip->Vehicle OEM / EV Maker
Car Rental / Car-share Trip->MaaS / Multimodal App

// Multimodal / MaaS glues several modes
MaaS / Multimodal App->Ride-hail Platform (Uber / Lyft / Bolt)
MaaS / Multimodal App->Shared Micromobility Operator (Lime / Bird / Tier)
MaaS / Multimodal App->Transit Authority Operations
MaaS / Multimodal App->Mobile Ticketing / Fare Payment
MaaS / Multimodal App->Mapping & Routing APIs

// Private car dependencies
Private Car (owned)->Vehicle OEM / EV Maker
Private Car (owned)->Fuel / Energy Supply
Private Car (owned)->Road Network & Maintenance
Private Car (owned)->Parking Supply & Pricing
Household EV->Vehicle OEM / EV Maker
Household EV->EV Charging Network
Household EV->Road Network & Maintenance

// Ride-hail platform
Ride-hail Platform (Uber / Lyft / Bolt)->Ride-hail Driver Supply
Ride-hail Platform (Uber / Lyft / Bolt)->Mapping & Routing APIs
Ride-hail Platform (Uber / Lyft / Bolt)->Payment Rails
Ride-hail Platform (Uber / Lyft / Bolt)->Mobile Connectivity (4G / 5G)
Ride-hail Platform (Uber / Lyft / Bolt)->Cloud Utilities
Ride-hail Platform (Uber / Lyft / Bolt)->Municipal Permits & Regulation

// Micromobility
Shared Micromobility Operator (Lime / Bird / Tier)->Shared Micromobility Fleet
Shared Micromobility Operator (Lime / Bird / Tier)->Mapping & Routing APIs
Shared Micromobility Operator (Lime / Bird / Tier)->Payment Rails
Shared Micromobility Operator (Lime / Bird / Tier)->Mobile Connectivity (4G / 5G)
Shared Micromobility Operator (Lime / Bird / Tier)->Telematics / IoT on Vehicles
Shared Micromobility Operator (Lime / Bird / Tier)->Municipal Permits & Regulation
Shared Micromobility Fleet->Vehicle OEM / EV Maker
Shared Micromobility Fleet->EV Charging Network

// Transit
Transit Authority Operations->Transit Vehicle Fleet
Transit Authority Operations->Bike / Bus Lane Allocation
Transit Authority Operations->Road Network & Maintenance
Transit Vehicle Fleet->Vehicle OEM / EV Maker
Transit Vehicle Fleet->Fuel / Energy Supply

// Vehicle OEM
Vehicle OEM / EV Maker->Autonomous Driving Stack
Vehicle OEM / EV Maker->Telematics / IoT on Vehicles

// In-car nav and ticketing
In-car Navigation / Routing App->Mapping & Routing APIs
In-car Navigation / Routing App->GNSS / GPS
In-car Navigation / Routing App->Mobile Connectivity (4G / 5G)
Mobile Ticketing / Fare Payment->Payment Rails
Mobile Ticketing / Fare Payment->Mobile Connectivity (4G / 5G)

// Municipality infrastructure
Street & Curb Design->Bike / Bus Lane Allocation
Street & Curb Design->Road Network & Maintenance
Congestion / Low-Emission Zone Policy->Municipal Permits & Regulation
Parking Supply & Pricing->Municipal Permits & Regulation
Bike / Bus Lane Allocation->Road Network & Maintenance

// Remote work
Remote Work Platforms (Zoom / Teams / Slack)->Cloud Utilities
Remote Work Platforms (Zoom / Teams / Slack)->Mobile Connectivity (4G / 5G)
E-commerce / Delivery Networks->Cloud Utilities
E-commerce / Delivery Networks->Payment Rails

// EV charging
EV Charging Network->Fuel / Energy Supply
EV Charging Network->Municipal Permits & Regulation

// Autonomous stack
Autonomous Driving Stack->Mapping & Routing APIs
Autonomous Driving Stack->GNSS / GPS
Autonomous Driving Stack->Telematics / IoT on Vehicles

// Evolution arrows (scenario, not forecast)
evolve MaaS / Multimodal App 0.55
evolve EV Charging Network 0.70
evolve Autonomous Driving Stack 0.40
evolve Household EV 0.75
evolve Shared Micromobility Operator (Lime / Bird / Tier) 0.72
evolve Congestion / Low-Emission Zone Policy 0.55
evolve Remote Work Platforms (Zoom / Teams / Slack) 0.88

note Build moat — differentiation zone [0.55, 0.25]
note Rent / utility — commodity zone [0.15, 0.90]
note War zone on Micromobility and Ride-hail [0.45, 0.65]
```

---

## Strategic analysis

The map is a **multi-stakeholder landscape**: three anchors (Urban Resident, Daily Commuter, Municipality) share most infrastructure but weight the choice-drivers differently. The most interesting strategic feature in May 2022 is a layered commodity stack (roads, fuel, mapping, payments, connectivity) supporting a Product (+rental) layer in mid-war (ride-hail, micromobility) while Genesis-ish bets (Autonomous Driving, MaaS) sit off to the left waiting for their S-curves.

### a. Differentiation opportunities (top 3)

Where a component is user-visible AND still immature — these are where strategic moats are built.

1. **MaaS / Multimodal App** (Custom Built, ε ≈ 0.35) — the one component that glues every mode together for the user. Still fragmented across cities (Whim, Citymapper, Jelbi, Transit). Whoever wins becomes the default front-door for urban mobility; the operator below becomes substitutable. Highest differentiation leverage on the map.
2. **Sustainability Preference** (Custom Built, ε ≈ 0.40) — a choice-driver that is moving rapidly up in salience (especially for under-35 demographics in May 2022). Any operator that can credibly ladder cost + sustainability into their value proposition (transit, micromobility, EV car-share) is differentiated.
3. **Congestion / Low-Emission Zone Policy** (Custom Built, ε ≈ 0.35) — for municipalities this is the distinguishing policy lever. London ULEZ, Paris ZFE, etc. are custom-per-city in 2022; no standard playbook yet. First-mover cities capture reputational and behavioural change.

Honourable mention: **Autonomous Driving Stack** (Genesis, ε ≈ 0.18) is where big differentiation *could* sit — but the signal in May 2022 (Uber ATG wound down, Cruise and Waymo still geo-fenced, Tesla FSD in beta) is that this is a long-horizon Genesis bet rather than a near-term moat.

### b. Commodity-leverage candidates (top 3)

Deep, mature components — rent from utilities, never build.

1. **Mapping & Routing APIs** (Commodity +utility, ε ≈ 0.90) — Google Maps, Mapbox, HERE are commodity. Rebuilding routing is ~100% wasted engineering for any operator.
2. **Payment Rails** (Commodity +utility, ε ≈ 0.92) — Stripe, Adyen, Checkout. Every operator should rent.
3. **Cloud Utilities / Mobile Connectivity / GPS** (all Commodity +utility, ε ≈ 0.92–0.95) — baseline infrastructure; operators who still run their own datacentres are carrying dead weight.

Runners-up for commodity leverage: **Fuel / Energy Supply** and **Mobile Ticketing / Fare Payment** (both Commodity +utility) are also safely outsource-able.

### c. Dependency risks (top 3)

Edges where a visible component depends on an immature foundation.

1. **Ride-hail Trip → Ride-hail Driver Supply** (user-visible ν = 0.84 depends on Custom Built driver-supply at ε ≈ 0.60) — driver-availability shock in 2021-22 (post-pandemic driver shortages and gig-worker reclassification in UK/EU) exposed the fragility. A wonderful-looking app is useless without drivers.
2. **Car Rental / Car-share Trip → MaaS / Multimodal App** (car-share trip ν = 0.76 depends on Custom Built ε ≈ 0.35) — whenever a mode depends on a still-Custom aggregator, the user experience is brittle. Car-share cannot industrialise faster than its multimodal front-door.
3. **Household EV → EV Charging Network** (ν = 0.56 depends on Custom Built ε ≈ 0.45) — the single biggest consumer-adoption blocker for EVs in May 2022 is charging coverage, especially on-street for flat-dwellers and on motorway corridors. A clearly visible vehicle-purchase decision depends on an immature foundation.

Broader pattern: every **consumer-facing operator (ride-hail, micromobility) → Municipal Permits & Regulation** is a live dependency-risk edge. Municipalities can and do revoke permits overnight (Lime/Bird exit from Paris, etc.), and the regulator is still operating Custom Built rulebooks.

### d. Suggested gameplays (from Wardley's 61)

- **#1 Focus on user needs** — the three anchors are deliberate: solving for commuter + resident + municipality at once is the map's defining challenge. An operator tempted to optimise only for commuters will lose its permit.
- **#45 Two factor (marketplace)** on **Ride-hail Platform** and **Shared Micromobility Operator** — classic two-sided play. Rider liquidity pulls driver / fleet density; density pulls riders.
- **#16 Exploiting Network Effects** on **MaaS / Multimodal App** — the multimodal app gets better with every added operator, and every added rider improves inventory visibility.
- **#36 Directed Investment** on **MaaS / Multimodal App** and **EV Charging Network** — both are top-3-D components; the strategic answer is *concentrate engineering here*, not spread thin.
- **#15 Open Approaches** on **Mobile Ticketing / Fare Payment** and **Transit Authority Data** — open GTFS-RT, open account-based ticketing (contactless EMV). Accelerates the Product (+rental) → Commodity (+utility) transition, which benefits the multimodal-app operator over any single mode operator.
- **#29 Harvesting** on **Autonomous Driving Stack** — don't build in-house; let the AV market consolidate, then buy or licence the winner. May 2022's evidence (Uber sold ATG to Aurora; Lyft sold L5 to Toyota) is that harvesting beats first-party building.
- **#43 Sensing Engines (ILC)** for municipalities — use curb and micromobility data to sense where demand is shifting (late-night leisure, school-run, last-mile) and target bike-lane / bus-lane allocations accordingly.
- **#56 First Mover** on **Congestion / Low-Emission Zone Policy** — cities that acted first (London 2003, Stockholm 2006, Oslo 2019) have the data and political capital to ratchet policy; late movers face a political uphill.
- **#41 Alliances / #42 Co-creation** between **Transit Authorities** and **Shared Micromobility Operators** — last-mile integration is the obvious alliance. Helsinki / Berlin examples show the play.
- **#8 Bundling** on **Mobile Ticketing / Fare Payment** — bundle transit + bikeshare + scooter into one monthly cap. Reduces perceived cost, increases multimodal use.

### e. Doctrine check

- ✓ **#1 Focus on user needs** — three anchors present, reflecting real user heterogeneity.
- ✓ **#10 Know your users** — separating Urban Resident, Daily Commuter, and Municipality avoids the common mistake of collapsing them into a generic "traveller".
- ⚠ **#13 Manage inertia** — the map has several inertia hotspots. **Private Car (owned)** carries sunk-capital inertia (form #2) for households; **Transit Authority Operations** carries institutional inertia (political, bureaucratic — forms #7, #12); **Ride-hail Driver Supply** carries workforce-classification inertia (regulatory, form #13). Strategy that ignores these will over-estimate transition speed.
- ⚠ **#16 Use appropriate methods** — practices do not evolve uniformly with activities. Street & Curb Design is Custom Built as a practice even in cities whose road network is Commodity (+utility) as an activity. Policy-side actors must not be managed with operational-excellence playbooks.
- ⚠ **#2 Use a systematic mechanism of learning** — the municipality anchor typically lacks a real learning loop. Data from operators flows out, but integrated decision-support for curb-allocation and permit design is mostly absent. Gap.

### f. Climatic context (of Wardley's 27 patterns)

- **#3 Everything evolves** — operative on Ride-hail (Product → Commodity +utility likely within the decade), Household EV (Product → Commodity +utility as ICE share collapses), and Remote Work Platforms (already Product (+rental) moving toward Commodity (+utility)).
- **#15–17 Inertia** — strongest on Private Car (owned) (sunk capital, status signalling), Transit Authority Operations (political / union / procurement cycles), and Parking Supply & Pricing (rent-seeking coalitions in most cities).
- **#27 Punctuated equilibrium (Product → Commodity war)** — visibly active on **Shared Micromobility** (consolidation wave underway — Lime/Jump, Bird post-SPAC, Tier acquiring Spin and Dott in talks) and **Ride-hail** (price-discipline, path to profitability, regulatory standardisation).
- **#23 Co-evolution of practice with activity** — critical for **Bike / Bus Lane Allocation**: the practice "tactical urbanism" co-evolves with the physical activity of re-allocating street space. You cannot commoditise curb design faster than the practice of participatory street design matures.
- **#18 You cannot measure evolution over time or adoption** — directly relevant; all evolve arrows are scenarios.
- **#13 Capital flows to new** — capital in 2021-2022 was flowing strongly into micromobility, EV OEMs, and charging networks. That flow itself accelerates the right-ward drift of those components — a self-reinforcing dynamic.

### g. Deep-placement notes

Targeted research was done on components where cheat-sheet rows disagreed or where the placement carries disproportionate strategic weight. Rather than run every component through the 19-row table, these four were prioritised because the map's top-3 differentiation and top-3 risk conclusions depend on them.

- **MaaS / Multimodal App (final ε ≈ 0.35, Custom Built).** Cheat-sheet rows for Ubiquity and User Perception suggested late Custom Built; Market row suggested early Product (Whim, Citymapper, Moovit, Transit app, Jelbi all exist). Vendor-landscape reading: many active vendors but no dominant, most still regional, integration with transit is fragmented — stays in Custom Built. Variance was the second-highest on the map, so this is plotted with an implied range of 0.30 – 0.45.
- **Shared Micromobility Operator (final ε ≈ 0.55, mid Product +rental).** Operators have clearly productised (seasonal pricing, tiered access, safety training). Vendor-count in May 2022 shows ongoing consolidation (Tier + Spin, Helbiz + Wheels, Bird's struggles). Publication type has shifted from "describe the wonder" (2018-19) to "operations / safety / regulation" (2021-22) — a Stage III → Stage IV signal. Evolve arrow set to 0.72 to reflect the industrialisation trajectory.
- **Household EV (final ε ≈ 0.52, mid Product +rental).** Ubiquity is still well below ICE (Stage II-III by vehicle share), but product maturity, range anxiety decreasing, and OEM model-count are all Stage III signals. Ubiquity row pulls it down; Publications and Certainty rows push it up. Plotted at the boundary; evolve arrow to 0.75 to reflect 2025-30 scenario of rising share.
- **Autonomous Driving Stack (final ε ≈ 0.18, Genesis).** Cheat-sheet would normally score this in Custom Built based on engineering depth (demos, limited robotaxi ops in Phoenix / SF). But Ubiquity is near-zero for real consumer use, Certainty is low, User Perception is "exciting/scary", and Market is undefined. Kept at Genesis. Uber/Lyft divestitures in 2020-21 are a public signal against treating this as a near-term Custom Built platform play.

No deep placement was done for obvious commodities (Cloud, Payment Rails, GPS, Mapping APIs, Mobile Connectivity) or obvious mature activities (Private Car Use, Fuel Supply, Public Transit Trip). Those placements are not load-bearing for the strategic conclusions and the cheat-sheet gives them unambiguously.

### h. What's differentiating vs. what's commoditising?

**Differentiating (left side, user-visible):**
- The **multimodal aggregation layer** (MaaS / routing) — the orchestration is still Custom Built.
- **Sustainability framing** as a choice driver — still emerging as a standard promise; operators can still earn a premium on it.
- **City-level policy design** (CAZ / ULEZ / pricing) — each city is still Custom Built; standards haven't formed.
- **EV charging experience** (speed, reliability, payment interop) — Stage II/III heading right; operators who can industrialise UX first win.
- **Autonomous stack components** (perception, motion-planning, sim) — still Genesis for years more.

**Commoditising (right side, moving or already moved):**
- **Ride-hail** as an experience — platforms fungible; riders care about cost and ETA.
- **Shared micromobility** — consolidation wave plus city-mandated data/safety standards (MDS, ISO 4210-10) are right-ward pushers.
- **Mobile ticketing** — account-based contactless (EMV / Apple Pay) is killing bespoke transit cards in Product (+rental) timeframe.
- **Vehicle OEM manufacturing** as an activity — EV transition is a classic Product (+rental) → Commodity (+utility) war; see BYD and the Chinese entrants pressuring margins.
- **Remote-work tools** — already Product (+rental) heading strongly toward Commodity (+utility); the pandemic compressed five years of evolution into 18 months.

### i. Validator check

```
python3 ${CLAUDE_SKILL_DIR}/scripts/validate_owm.py ./draft.owm
OK: 52 components/anchors, 109 edges — no violations.
```

### j. Caveat

All evolve arrows and trajectories are **scenarios, not forecasts**. Wardley climatic pattern #18: *"you cannot measure evolution over time or adoption."* The map is a snapshot of May 2022 with plausible pressure vectors, not a prediction about exact timing. War-zone components (ride-hail, micromobility, EVs) can move faster than expected if open-source / standardisation accelerates (#27 punctuated equilibrium); Genesis components (autonomous) can stall for a decade.
