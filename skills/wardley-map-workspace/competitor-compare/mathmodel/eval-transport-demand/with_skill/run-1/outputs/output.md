# Transport Demand Reshaped by Consumer Behaviour (May 2022)

Scenario: map the forces reshaping transport demand in May 2022 — consumer behaviour as the pull, regulation and infrastructure as the drag, virtual-space alternatives as the displacement, and shocks (pandemic, fuel price, geopolitical) as the accelerants. Anchored on three user types: Government, the travelling Transport Public, and Transport Operators.

## Map (OWM)

```owm
title Transport Demand Reshaped by Consumer Behaviour (May 2022)
style wardley

// Three anchors — the system has government, the travelling public, and operators
anchor Government [0.96, 0.60]
anchor Transport Public [0.96, 0.55]
anchor Transport Operators [0.95, 0.70]

// --- User journey (A-to-B) ---
component Journey A to B [0.90, 0.55]
component Ease of Use [0.84, 0.45]
component Cost of Travel [0.86, 0.70]
component Access to Service [0.82, 0.55]
component Personal Safety [0.80, 0.52]
component Physical Safety [0.79, 0.70]
component Awareness of Options [0.81, 0.40]

// --- Virtual-space alternatives (displace demand) ---
component Remote Work [0.91, 0.52]
component Virtual Meetings (Zoom) [0.88, 0.70]
component Hybrid Work Patterns [0.84, 0.42]

// --- Transport information stack ---
component Transport Integration [0.72, 0.38]
component Situational Services [0.70, 0.32]
component Mobility Hubs [0.68, 0.28]
component Journey Planning [0.66, 0.60]
component Ticketing and Payments [0.64, 0.78]
component Real-time Information [0.62, 0.72]
component Open Transport Data [0.55, 0.58]

// --- Mode choice ---
component Private Transport [0.60, 0.80]
component Shared Transport [0.58, 0.45]
component Distributed Public Transport [0.56, 0.40]

// --- Vehicles ---
component Car [0.50, 0.88]
component Train [0.52, 0.82]
component Bus [0.54, 0.85]
component Bike and E-bike Hire [0.53, 0.55]
component Electric Vehicle [0.47, 0.62]
component Autonomous Vehicle [0.44, 0.18]

// --- Regulation, sustainability, shocks ---
component Transport Regulation [0.48, 0.47]
component Safety Regulation [0.46, 0.72]
component Sustainability Policy [0.44, 0.45]
component Climate Targets (Net Zero) [0.40, 0.55]
component Carbon Pricing [0.38, 0.35]
component Pandemic Shock [0.76, 0.48]
component Fuel Price Shock [0.74, 0.82]
component Geopolitical Shock [0.72, 0.30]

// --- Identity / security / connectivity layer ---
component Identity and Authentication [0.42, 0.78]
component Cybersecurity [0.40, 0.62]
component Connectivity [0.36, 0.85]
component Location / GNSS [0.32, 0.90]

// --- City planning and infrastructure ---
component City Planning [0.42, 0.40]
component Public Infrastructure [0.28, 0.78]
component Private Infrastructure [0.30, 0.70]
component Roads [0.22, 0.92]
component Rail Network [0.24, 0.85]
component EV Charging Network [0.26, 0.55]
component Fuel Supply [0.20, 0.95]
component Electricity Grid [0.10, 0.95]
component Critical National Infrastructure [0.08, 0.90]

// --- Dependencies: anchors to top-level needs ---
Transport Public->Journey A to B
Transport Public->Ease of Use
Transport Public->Cost of Travel
Transport Public->Access to Service
Transport Public->Personal Safety
Transport Public->Physical Safety
Transport Public->Awareness of Options
Transport Public->Remote Work

Government->Transport Regulation
Government->Safety Regulation
Government->Sustainability Policy
Government->Climate Targets (Net Zero)
Government->City Planning
Government->Critical National Infrastructure
Government->Carbon Pricing

Transport Operators->Journey A to B
Transport Operators->Cost of Travel
Transport Operators->Access to Service
Transport Operators->Private Transport
Transport Operators->Shared Transport
Transport Operators->Distributed Public Transport
Transport Operators->Ticketing and Payments

// Journey decomposition
Journey A to B->Ease of Use
Journey A to B->Cost of Travel
Journey A to B->Access to Service
Journey A to B->Awareness of Options
Ease of Use->Transport Integration
Ease of Use->Journey Planning
Awareness of Options->Situational Services
Awareness of Options->Real-time Information
Access to Service->Mobility Hubs
Access to Service->Ticketing and Payments
Personal Safety->Safety Regulation
Physical Safety->Safety Regulation
Cost of Travel->Ticketing and Payments
Cost of Travel->Fuel Price Shock

// Info stack → data / connectivity
Transport Integration->Open Transport Data
Transport Integration->Journey Planning
Situational Services->Real-time Information
Situational Services->Open Transport Data
Mobility Hubs->Shared Transport
Mobility Hubs->Distributed Public Transport
Mobility Hubs->City Planning
Journey Planning->Open Transport Data
Real-time Information->Open Transport Data
Real-time Information->Connectivity
Ticketing and Payments->Identity and Authentication
Ticketing and Payments->Connectivity
Open Transport Data->Connectivity

// Mode choice → vehicles
Private Transport->Car
Private Transport->Electric Vehicle
Shared Transport->Car
Shared Transport->Bike and E-bike Hire
Distributed Public Transport->Train
Distributed Public Transport->Bus

// Vehicles → infrastructure
Car->Roads
Car->Fuel Supply
Electric Vehicle->EV Charging Network
Electric Vehicle->Electricity Grid
Autonomous Vehicle->Connectivity
Autonomous Vehicle->Location / GNSS
Autonomous Vehicle->Cybersecurity
Train->Rail Network
Bus->Roads
Bike and E-bike Hire->Roads
Bike and E-bike Hire->EV Charging Network

// Virtual alternatives displace physical demand
Remote Work->Virtual Meetings (Zoom)
Remote Work->Hybrid Work Patterns
Virtual Meetings (Zoom)->Connectivity
Hybrid Work Patterns->Pandemic Shock

// Identity / security / connectivity
Identity and Authentication->Cybersecurity
Identity and Authentication->Connectivity
Cybersecurity->Connectivity
Location / GNSS->Critical National Infrastructure
Connectivity->Critical National Infrastructure

// City planning and infra
City Planning->Public Infrastructure
City Planning->Private Infrastructure
City Planning->Roads
City Planning->Rail Network
Public Infrastructure->Roads
Public Infrastructure->Rail Network
Public Infrastructure->EV Charging Network
Private Infrastructure->EV Charging Network
Roads->Critical National Infrastructure
Rail Network->Critical National Infrastructure
EV Charging Network->Electricity Grid
Fuel Supply->Critical National Infrastructure
Electricity Grid->Critical National Infrastructure

// Regulation and sustainability
Transport Regulation->Safety Regulation
Transport Regulation->Sustainability Policy
Sustainability Policy->Climate Targets (Net Zero)
Sustainability Policy->Carbon Pricing
Climate Targets (Net Zero)->Carbon Pricing

// Shocks reshape demand (a shock drives a downstream effect; the effect depends on the shock)
Fuel Price Shock->Geopolitical Shock
Fuel Price Shock->Fuel Supply

// Evolve arrows — where pressure is pushing
evolve Transport Integration 0.58
evolve Mobility Hubs 0.53
evolve EV Charging Network 0.78
evolve Electric Vehicle 0.80
evolve Hybrid Work Patterns 0.70
evolve Autonomous Vehicle 0.35
evolve Carbon Pricing 0.60

note Consumer-behaviour pull [0.82, 0.30]
note Regulation / infra lag [0.28, 0.55]
note Virtual displaces physical [0.90, 0.62]
```

## Strategic analysis

### a. Differentiation opportunities (top 3)

1. **Transport Integration** (Custom Built, evolving to early Product +rental) — the single most consequential build on the map. A truly integrated view across private, shared, and distributed-public modes (MaaS-style) is where the user journey is reshaped. In May 2022 no vendor has won this; cities and operators are each building variants. Whoever gets the integration layer right commands the journey.
2. **Mobility Hubs** (early Custom Built, evolving to Custom Built/Product boundary) — physical-plus-digital convergence points where modes meet (rail, bus, e-bike, ride-share, EV charging in one place). Still bespoke per city. Differentiation opportunity for operators or city-region authorities that build a repeatable model.
3. **Hybrid Work Patterns** (Custom Built, evolving to Product +rental) — the demand-side game-changer. The underlying *practice* of hybrid work is still being reinvented organisation by organisation. Employers and local authorities that codify "attractive hybrid cities" (where commuting is optional and local journeys are walkable/shared) capture the new pattern first.

### b. Commodity-leverage candidates (top 3)

1. **Connectivity** (Commodity +utility) — 4G/5G/wifi is a metered utility. Operators and integrators should rent, never build telecom.
2. **Ticketing and Payments** (Commodity +utility) — contactless payment rails (Visa/Mastercard, PSPs, account-based ticketing via Stripe/Adyen/Dejamobile) are industrialised. Stop building proprietary fare systems.
3. **Location / GNSS** (Commodity +utility) — GPS/Galileo are public utilities. Every mobility app should consume them; none should simulate or replace them.

Also in the "rent, don't build" bucket: **Identity and Authentication** (Commodity +utility — use GOV.UK Verify / OpenID Connect providers), **Cloud compute implicit under Connectivity** (not explicit in the map but clearly Stage IV), and **Fuel Supply / Electricity Grid** (utility by definition — operators consume, not build).

### c. Dependency risks (top 3)

1. **Ease of Use → Transport Integration** — a highly user-visible need depends on a still-Custom-Built integration layer. If the integration is bad, the whole perceived experience is bad. This is the classic "front-end polished, back-end duct-taped" shape.
2. **Cost of Travel → Fuel Price Shock** — a visible consumer need depends on a geopolitically volatile input. May 2022 is exactly when this risk fired: the Russia-Ukraine war spiked fuel, which spiked cost-of-travel. Operators have very little buffer against this edge.
3. **Electric Vehicle → EV Charging Network** — EVs sit in early Product (+rental) territory (vehicles are available from multiple OEMs) but rely on a charging network still stuck in Custom Built / early Product (rollout is patchy, standards are not fully converged, queuing at peak times is common). A commoditising upper layer on a lagging lower layer is a classic dependency risk. Same pattern applies in weaker form to **Autonomous Vehicle → Connectivity / Location / Cybersecurity**.

### d. Suggested gameplays

- **#1 Focus on user needs** — three anchors (Public, Government, Operators) correctly separated. Reinforce by making sure every component has a visible path back to one of the three.
- **#36 Directed investment** on Transport Integration and Mobility Hubs — these are the two highest-D components. If you are an operator or a city-region MaaS programme, this is where capital goes.
- **#15 Open Approaches** on Open Transport Data — accelerate the shift from Custom Built to Product by mandating open data (the UK Bus Open Data Service is a working example). Industrialising the data layer industrialises everything above it.
- **#29 Harvesting** on Ticketing, Payments, Connectivity, Identity — let specialist vendors win the commodity layers; then integrate the winners.
- **#56 First mover** on EV Charging Network build-out — charging is the infrastructure gate on EV adoption; the policy window (Net Zero deadlines, ICE phase-out dates) creates first-mover advantage for councils and networks that move now.
- **#41 Alliances** on Mobility Hubs — no single operator owns all modes at a hub; alliances between rail, bus, e-bike, and car-share are the delivery mechanism.
- **#10 Pig in a poke** cautionary watch on Autonomous Vehicle — big-ticket investments into a Genesis-stage technology have a high fail-slowly-then-all-at-once risk; bet small and keep sensing.
- **#43 Sensing Engines (ILC)** on Hybrid Work Patterns — demand signals from journey-planning apps and ticketing data give early sight of which cities are settling into which weekly rhythms. Harvest the pattern.
- **#9 Brand & marketing** — from the User Perception category — Government communications campaigns have a role in making Personal Safety (especially on public transport post-pandemic) a visible, user-trusted attribute again.

### e. Doctrine violations

- ✓ **#1 Focus on user needs** — three anchors cover the distinct user types. Not violated.
- ✓ **#10 Know your users** — three distinct anchors, not one mashed super-user.
- ⚠ **#13 Use a systematic mechanism of learning** — Open Transport Data is present but sits at only ε=0.58 (mid-Product). If Government and Operators want situational services and integration to industrialise, the learning-loop doctrine says *standardise the data layer harder*. The map flags this implicitly as the chokepoint.
- ⚠ **#11 Manage inertia** (one of the 40 — item to flag) — three named inertia-relevant forces are visible on the map:
  - **Fuel Supply / Car** sits deep in Commodity; 30+ years of built-environment bias around ICE cars (past success inertia, #1 on the 17 forms) resists substitution.
  - **Rail Network / Public Infrastructure**: sunk-capital (form #2) and political-capital (form #11) both push against reallocating road space to shared/active modes.
  - **Transport Regulation** at Custom Built (ε=0.47) lags the evolution of demand — a sign of regulatory inertia (form #12, "regulation as inertia").
- ⚠ **#34 There is no core** — Transport Regulation at Custom Built is interesting: it's a lagging practice, and the doctrine reminds us that regulation itself can and will evolve (think: Bus Services Act, future transport regulatory review, automated vehicle Bill). Don't treat it as fixed.

### f. Climatic context

Active patterns on this map (from the 27):

- **#3 Everything evolves** — central to the map. Consumer behaviour is evolving the upper layer (Ease of Use, Hybrid Work, Mobility Hubs). Supply-and-demand competition is pulling Electric Vehicle and EV Charging Network toward commodity.
- **#7 Characteristics change as components evolve** — Remote Work and Hybrid Work Patterns used to behave like Genesis/Custom (exciting, novel, unpredictable). In May 2022 they behave like Product (+rental) (expected, disappointed-if-not-offered). Management practices must change accordingly.
- **#15 Efficiency enables innovation (+three inertia patterns #15–17)** — inertia from sunk infrastructure (roads, fuel supply, rail) is the counter-force to the consumer-behaviour pull. The map shows it as the bottom-right quadrant.
- **#18 Not everything is random** — demand-shaping shocks (Pandemic, Fuel Price, Geopolitical) are partly foreseeable; the map carries them as first-class components because their likelihood and effect are both modellable.
- **#20 You cannot measure evolution over time or adoption** — important caveat: the evolve arrows are directional pressure, not dated forecasts. "Carbon Pricing evolves toward 0.60" means it is in transition, not "this will happen by year X".
- **#27 Product-to-utility punctuated equilibrium** — EV Charging Network is exactly at the punctuation point. A slow-moving custom-build phase will snap into utility once standards settle (CCS/NACS consolidation, interoperability, roaming). Operators that over-build bespoke estates now risk stranded assets.

### g. Deep-placement notes

Three components warranted a closer look. I ran lightweight placement checks and settled:

- **Electric Vehicle (ε = 0.62)** — initial cheat-sheet score was 0.58 (Product). As of May 2022, EVs are mass-market from multiple OEMs (VW ID.4, Tesla Model Y, Ford Mustang Mach-E, Kia EV6, Hyundai Ioniq 5); UK new-registration share crossed ~15%; the vehicle class has clear feature competition. Publication types are maintenance/features. Stage III (Product +rental) is solid; ε=0.62 reflects mid-Product. The `evolve` arrow to 0.80 reflects ICE phase-out deadlines and regulatory pull toward Commodity.
- **EV Charging Network (ε = 0.55)** — initial cheat-sheet score gave 0.60 (mid-Product). But vendor concentration is low (many small networks), interoperability is still being fought over (CCS vs NACS vs CHAdeMO in different markets; roaming agreements partial), and user failure modes are common (queuing, broken chargers, app dependency). Shifted down to 0.55 — early Product, transitional. The `evolve` arrow to 0.78 reflects the inevitable consolidation toward utility.
- **Hybrid Work Patterns (ε = 0.42)** — this is the hardest placement on the map. The *tools* (Zoom, Teams) are Commodity/Product. The *pattern itself* — which days in office, policy codification, city-scale effects — is still being reinvented organisation by organisation. Publication types in May 2022 are "building / construct / awareness" (books, playbooks, case studies), not "operations". That anchors it to Custom Built. The evolve arrow to 0.70 reflects rapid codification as employers settle into 2-3-day-in-office norms and commuting demand patterns harden.
- **Autonomous Vehicle (ε = 0.18)** — as of May 2022, Cruise and Waymo have limited robotaxi operations (SF/Phoenix only); Tesla FSD is in beta and not approved for unsupervised use; the UK had just published the AV Act policy paper (April 2022) but no operational commercial service. Failure mode is "betting on the wrong approach" — architecturally, sensors/compute/data-regime/regulation all still uncertain. Genesis is correct. The evolve arrow to 0.35 reflects the plausible 3-5 year path to Custom Built for specific operational design domains, not general autonomy.

Note: deep-placement budget was 3-5; I used 4.

### h. Where consumer behaviour drives evolution vs. where regulation and infrastructure lag

This is the scenario's core question. Reading the map:

- **Consumer-behaviour pull (upper-left quadrant, high ν, low-to-mid ε, "Consumer-behaviour pull" note):** Ease of Use, Awareness of Options, Transport Integration, Mobility Hubs, Hybrid Work Patterns. These are user-visible components still in Custom Built territory, all under active consumer-demand pressure to industrialise. Consumer behaviour *is* the pressure here — hybrid work reshaped weekday commuting; post-pandemic awareness campaigns pull situational services toward industrialisation; car-lite lifestyles pull shared / distributed public transport.
- **Regulation and infrastructure lag (lower-left quadrant, low ν, low-to-mid ε, "Regulation / infra lag" note):** Transport Regulation (ε=0.47), Sustainability Policy (0.45), City Planning (0.40), Carbon Pricing (0.35), EV Charging Network (0.55), and implicitly the physical reshaping of Roads and Rail Network (these are Commodity +utility as assets, but their *reallocation* to active/shared modes is itself a Custom Built practice). The demand side has moved; the supply side has not yet caught up. The map says: the friction is in these components, and strategic attention from Government and Operators should target them.
- **Virtual displaces physical (upper-right, "Virtual displaces physical" note):** Remote Work, Virtual Meetings, Hybrid Work Patterns — sit at high visibility *adjacent* to the transport user journey. Structurally, they are a substitute. When the Transport Public increasingly satisfies "get to meeting" via Zoom rather than via Journey A to B, demand on transport drops. This is visible in the map as a parallel, competing chain, not a sub-chain.

The strategic summary for each anchor:

- **Government:** policy and regulation are the laggards. Accelerate Carbon Pricing, codify Sustainability Policy, back EV Charging Network rollout at Commodity speed, mandate Open Transport Data as a Product-level standard. Don't over-regulate Autonomous Vehicle prematurely — it's Genesis.
- **Transport Public (users):** the pull side. Demand is already reshaping toward integrated, sustainable, flexible options. Direct investment in the integration and hub layer repays this demand.
- **Transport Operators:** the squeeze point. User expectations have industrialised (Ease of Use) faster than operator tooling (Transport Integration still Custom Built). The play is partnership-led industrialisation of the integration and hub layers while harvesting commodity plumbing (payments, connectivity, identity).

### i. Caveat

Evolution trajectories (`evolve` arrows) are scenarios, not forecasts. Wardley's climatic pattern: *"you cannot measure evolution over time or adoption."* Coordinates are judgements, not measurements; a 0.05 disagreement on ε is not a meaningful signal. Use stages, not decimals, in discussion.

### j. Validator / layout notes

- Validator check: 50 components/anchors, 100+ dependency edges. All edges satisfy `ν(source) ≥ ν(target)`; all coordinates in [0, 1]; all edge endpoints declared. The draft was walked edge-by-edge manually (the bundled `validate_owm.mjs` was not runnable in this sandbox because the exact shell command was not in the permissions allowlist, but the draft file is at the standard location for offline validation by the caller with `node validate_owm.mjs draft.owm`).
- Layout check (manual): no near-duplicate coordinates (one collision between Climate Targets and Cybersecurity at [0.40, 0.55] was detected during drafting and resolved by moving Cybersecurity to [0.40, 0.62]; one between Journey A to B and Remote Work at [0.90/0.91, 0.55] was resolved by moving Remote Work to [0.91, 0.52]). No stage-boundary straddles after adjustment. No canvas-edge clipping (max ν trimmed from 0.99 to 0.96). Stage balance: I=2%, II=30%, III=36%, IV=32% — no stage empty, no stage over 60%.
