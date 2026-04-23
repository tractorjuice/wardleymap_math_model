# Wardley Map Analysis: UK Labour Party — Preparing for Government (May 2024)

## Purpose

What parts of Labour's political machinery are **industrialised** (Product / Commodity stages — Labour plugs in and executes) versus **still being invented** (Genesis / Custom-Built — bespoke delivery vehicles that do not yet exist at scale)? The map is a diagnostic of government-readiness in the final weeks before the 2024 general election.

---

## Deliverable 1 — Interactive React Artifact

See `wardley-map-labour.jsx`. The artifact is a self-contained React component (inline SVG) that renders the map with:

- Hover tooltips showing each component's name, stage, `[visibility, maturity]` coordinates, and a 1-2 sentence evolution rationale.
- Click-to-highlight dependency chains (both upstream and downstream), dimming unselected components to `opacity=0.15`.
- A figure legend below the map explaining the component / anchor / dependency / evolution arrow / inertia markers plus the four evolution stage columns.
- Four numbered on-map annotations (see table at bottom of this file).
- Professional muted palette (`#ffffff` background, `#333` component stroke, `#d94040` evolution arrows, stage-shaded columns) — no generic AI aesthetics.

Structure follows the skill's `templates/artifact-template.jsx` exactly. Claude.ai artifact imports only: `react` (`useState`, `useCallback`, `useMemo`) and Tailwind classes — no charting libraries.

---

## Deliverable 2 — OWM (OnlineWardleyMaps) Text Block

Also written to `draft.owm`. Paste into VS Code (Wardley Maps extension), Obsidian (wardley-maps plugin), or onlinewardleymaps.com.

```
title UK Labour Party - Preparing for Government (May 2024)
style wardley

// --- Anchors ---
anchor UK Voters [0.97, 0.50]
anchor Keir Starmer [0.95, 0.58]
anchor Labour Members [0.93, 0.42]

// --- Visible value proposition ---
component Electoral Victory [0.88, 0.45]
component Public Trust [0.86, 0.36]
component Policy Platform [0.84, 0.40]

// --- Campaign / engagement machinery ---
component Campaign Strategy [0.78, 0.58]
component Media Relations [0.76, 0.72]
component Public Engagement [0.74, 0.55]
component Volunteer Mobilisation [0.72, 0.65]
component Stakeholder Engagement [0.70, 0.52]
component Fundraising [0.68, 0.68]
component Private Sector Collaboration [0.66, 0.36]

// --- Policy apparatus ---
component Party Policy Framework [0.64, 0.55]
component Research and Policy Dev [0.60, 0.42]
component Internal Party Democracy [0.58, 0.48]

// --- Substantive policy areas ---
component Anti-Discrimination Policy [0.55, 0.56]
component Healthcare Access (NHS) [0.52, 0.64]
component Education Access [0.49, 0.60]
component National Security [0.50, 0.72]
component International Relations [0.46, 0.68]
component Community Programs [0.44, 0.46]
component Workers Rights (New Deal) [0.42, 0.30]
component Economic Equality [0.40, 0.22]
component Social Justice [0.38, 0.38]
component Infrastructure Development [0.36, 0.50]
component Public Sector Investment [0.34, 0.34]
component Housing Policy [0.32, 0.26] inertia
component Climate Action (GB Energy) [0.29, 0.14]
component Digital Transformation [0.26, 0.42]

// --- Infrastructure / utilities ---
component Voter Data and Analytics [0.18, 0.72]
component Civil Service Apparatus [0.15, 0.86]
component Funding Infrastructure [0.12, 0.78]
component Electoral Regulation [0.10, 0.88]

// --- Dependencies: voters / leader / members -> visible layer ---
UK Voters->Electoral Victory
UK Voters->Public Trust
UK Voters->Policy Platform
Keir Starmer->Electoral Victory
Keir Starmer->Public Trust
Keir Starmer->Policy Platform
Labour Members->Policy Platform
Labour Members->Internal Party Democracy
Labour Members->Volunteer Mobilisation

// --- Visible layer -> campaign machinery ---
Electoral Victory->Campaign Strategy
Electoral Victory->Public Engagement
Public Trust->Media Relations
Public Trust->Stakeholder Engagement
Policy Platform->Party Policy Framework
Policy Platform->Research and Policy Dev

// --- Campaign machinery internal wiring ---
Campaign Strategy->Media Relations
Campaign Strategy->Public Engagement
Campaign Strategy->Volunteer Mobilisation
Campaign Strategy->Fundraising
Campaign Strategy->Voter Data and Analytics
Public Engagement->Volunteer Mobilisation
Public Engagement->Voter Data and Analytics
Stakeholder Engagement->Private Sector Collaboration
Fundraising->Funding Infrastructure

// --- Policy apparatus wiring ---
Party Policy Framework->Internal Party Democracy
Party Policy Framework->Research and Policy Dev
Research and Policy Dev->Economic Equality
Research and Policy Dev->Workers Rights (New Deal)
Research and Policy Dev->Anti-Discrimination Policy
Research and Policy Dev->Social Justice
Research and Policy Dev->Healthcare Access (NHS)
Research and Policy Dev->Education Access
Research and Policy Dev->Housing Policy
Research and Policy Dev->Infrastructure Development
Research and Policy Dev->Public Sector Investment
Research and Policy Dev->Climate Action (GB Energy)
Research and Policy Dev->National Security
Research and Policy Dev->International Relations
Research and Policy Dev->Digital Transformation
Research and Policy Dev->Community Programs

// --- Policy areas -> state / infra ---
Healthcare Access (NHS)->Civil Service Apparatus
Education Access->Civil Service Apparatus
Infrastructure Development->Civil Service Apparatus
Public Sector Investment->Civil Service Apparatus
National Security->Civil Service Apparatus
International Relations->Civil Service Apparatus
Digital Transformation->Civil Service Apparatus
Housing Policy->Civil Service Apparatus
Climate Action (GB Energy)->Civil Service Apparatus
Community Programs->Civil Service Apparatus
Workers Rights (New Deal)->Civil Service Apparatus
Economic Equality->Civil Service Apparatus

// --- Regulatory / data / funding utilities ---
Campaign Strategy->Electoral Regulation
Fundraising->Electoral Regulation
Media Relations->Electoral Regulation
Voter Data and Analytics->Electoral Regulation
Volunteer Mobilisation->Funding Infrastructure

// --- Evolution arrows: where the next 12-24 months move components ---
evolve Campaign Strategy 0.70
evolve Private Sector Collaboration 0.55
evolve Climate Action (GB Energy) 0.42
evolve Digital Transformation 0.55
evolve Housing Policy 0.42
evolve Research and Policy Dev 0.55
evolve Infrastructure Development 0.58

// --- Annotations ---
annotation 1 [[0.78, 0.42]] Campaign op industrialising under McSweeney
annotation 2 [[0.66, 0.24]] Business engagement being actively invented
annotation 3 [[0.32, 0.22]] Climate / Housing delivery vehicles still Custom-Built
annotation 4 [[0.15, 0.92]] Governing utilities Labour inherits day one
```

---

## Deliverable 3 — Strategic Commentary

### Component Evolution Assessment

| Component | Stage | Position [vis, mat] | Rationale |
|---|---|---|---|
| UK Voters | Product (anchor) | [0.97, 0.50] | Electorate whose verdict in the 2024 general election is the ultimate user need driving every other component. |
| Keir Starmer | Product (anchor) | [0.95, 0.58] | Leader as political product: well known, professionally managed, still actively positioned as government-ready alternative. |
| Labour Members | Custom-Built (anchor) | [0.93, 0.42] | Specific, contested constituency whose policy and selection rights are bespoke to this party. |
| Electoral Victory | Custom-Built | [0.88, 0.45] | Winning a working majority after 14 years of opposition is a one-off campaign-specific outcome, not a repeatable Product. |
| Public Trust | Custom-Built | [0.86, 0.36] | Post-Corbyn, Labour is rebuilding credibility on economy and security; actively constructed voter-by-voter. |
| Policy Platform | Custom-Built | [0.84, 0.40] | Five Missions / pre-manifesto platform still being finalised in May 2024; bespoke to this leadership. |
| Campaign Strategy | Product | [0.78, 0.58] | Professionalised operation under McSweeney using modern GE playbook (target seats, messaging discipline, digital, GOTV); multiple vendors and precedents. |
| Media Relations | Product | [0.76, 0.72] | Mature practice across UK parties: press office, briefing cycles, broadcast bid management; approaching utility. |
| Public Engagement | Product | [0.74, 0.55] | Canvassing, hustings, town-halls are century-old practice; digital layer on top still evolving but core well-understood. |
| Volunteer Mobilisation | Product | [0.72, 0.65] | Long-established activist model with standard tools (Contact Creator, Ecanvasser-style apps); commodity skill-set inside the party. |
| Stakeholder Engagement | Product | [0.70, 0.52] | Structured engagement with unions, civil society and devolved administrations via well-trodden channels; balance being re-set. |
| Fundraising | Product | [0.68, 0.68] | Regulated donor funnel (affiliated unions, high-value donors, membership) is codified, multi-vendor, with clear compliance infrastructure. |
| Private Sector Collaboration | Custom-Built | [0.66, 0.36] | Starmer/Reeves business charm-offensive, CEO round-tables and the 'partnership with business' framing are an actively invented capability. |
| Party Policy Framework | Product | [0.64, 0.55] | Codified machinery (NPF, Clause V, Conference) with defined rules and long institutional history. |
| Research & Policy Dev | Custom-Built | [0.60, 0.42] | In-house policy units plus bespoke think-tank ecosystem (Labour Together, IPPR, Resolution Foundation); every leadership rebuilds it. |
| Internal Party Democracy | Product | [0.58, 0.48] | Long-established selection/NEC/Conference mechanisms; well-defined Product but actively contested. |
| Anti-Discrimination Policy | Product | [0.55, 0.56] | Mature statutory framework (Equality Act 2010, PSED); Labour inherits well-defined delivery mechanics. |
| Healthcare Access (NHS) | Product | [0.52, 0.64] | Vast NHS machinery with standard commissioning, workforce and regulatory apparatus; Labour inherits a Product it must reform. |
| Education Access | Product | [0.49, 0.60] | Schools, FE, HE funding and regulation run on well-understood levers (DfE, Ofsted, OfS, SFA). |
| National Security | Commodity | [0.50, 0.72] | Intelligence and defence apparatus is utility-like state infrastructure; policy levers commoditised across successive governments. |
| International Relations | Product | [0.46, 0.68] | FCDO, embassy network and multilateral memberships are mature Product/utility; Labour varies positioning not machinery. |
| Community Programs | Custom-Built | [0.44, 0.46] | Mix of mature third-sector infrastructure and new Labour-specific programs (Sure Start revival, youth hubs); model being re-specified. |
| Workers' Rights (New Deal) | Custom-Built | [0.42, 0.30] | Flagship bespoke policy package (day-one rights, zero-hours reform, Fair Work Agency) still being drafted. |
| Economic Equality | Custom-Built | [0.40, 0.22] | Reeves's fiscal/tax framing (tight rules + targeted reform) is bespoke; no off-the-shelf delivery pattern applies. |
| Social Justice | Custom-Built | [0.38, 0.38] | Umbrella stitching child poverty, criminal justice, welfare reform; delivery vehicles still forming. |
| Infrastructure Development | Product | [0.36, 0.50] | NSIP regime, planning law, HS2-era delivery models are recognisable Product; Labour layers on National Wealth Fund. |
| Public Sector Investment | Custom-Built | [0.34, 0.34] | Post-austerity capital envelope under new fiscal rules being freshly designed. |
| Housing Policy | Custom-Built (inertia) | [0.32, 0.26] | 1.5m-homes pledge requires inventing a planning and delivery vehicle that does not yet exist; decades of failed industrialisation. |
| Climate Action (GB Energy) | Genesis | [0.29, 0.14] | GB Energy is a novel publicly-owned investment vehicle with no UK precedent; £28bn plan scaled back, delivery shape still forming. |
| Digital Transformation | Custom-Built | [0.26, 0.42] | GDS and departmental digital teams are Product, but Labour's cross-government digital/AI/data ambition is a bespoke programme. |
| Voter Data & Analytics | Product | [0.18, 0.72] | Electoral roll + Experian/YouGov/Datapraxis-style services + standard MI tooling behave as Product with utility elements. |
| Civil Service Apparatus | Commodity | [0.15, 0.86] | Permanent neutral Whitehall machinery is the commodity substrate of any UK government. |
| Funding Infrastructure | Commodity | [0.12, 0.78] | Donor law, PPERA caps, membership dues collection, union affiliation — commoditised regulatory rails. |
| Electoral Regulation | Commodity | [0.10, 0.88] | Electoral Commission, returning officers, ballot logistics, spending limits — utility-grade state infrastructure. |

### Key Strategic Observations

1. **Two-speed value chain.** The upper half of the map (campaign, media, stakeholder, fundraising, voter data) is almost entirely Product or Commodity — Labour is running an industrialised election-winning machine. The lower half (climate delivery, housing, digital transformation, workers' rights, public sector investment) is Custom-Built or Genesis — Labour will take power carrying delivery vehicles it has not yet built.

2. **The headline answer to the scenario question.** *Industrialised political machinery*: Campaign Strategy, Media Relations, Public Engagement, Volunteer Mobilisation, Fundraising, Stakeholder Engagement, Party Policy Framework, Internal Party Democracy, NHS / Education / International Relations / Anti-Discrimination policy delivery, National Security, Voter Data, Civil Service, Funding Infrastructure, Electoral Regulation. *Still being invented*: Public Trust, Policy Platform, Private Sector Collaboration, Research & Policy Dev, Workers' Rights (New Deal), Economic Equality framing, Social Justice, Community Programs, Public Sector Investment, Housing, Climate Action / GB Energy, Digital Transformation.

3. **Genesis-stage component on a flagship policy is a strategic risk.** GB Energy (Climate Action) is the only Genesis-stage component (maturity 0.14). It is a novel publicly-owned investment vehicle with no UK precedent. Critical path on a headline pledge with no operating blueprint is the single biggest policy-delivery risk on the map.

4. **Housing carries inertia — and it is structural.** The inertia marker on Housing Policy is not Labour-specific; UK housing supply has failed to industrialise for 40 years across multiple governments. Labour's pledge operates against deep doctrinal resistance in the planning system — the evolution arrow (0.26 → 0.42) is achievable only if Labour attacks the supply-side planning Product itself.

5. **Research & Policy Dev is a bottleneck node.** The map has a star topology around Research & Policy Dev: it feeds every substantive policy area. That single Custom-Built node has to industrialise fast once in government, or it becomes a throughput bottleneck for Labour's whole legislative programme.

### Doctrine Check

Against Wardley's doctrine principles (see `references/doctrine-and-gameplay.md`):

- **Focus on user needs** — satisfied. Three anchors (voters, leader, members) differentiate the distinct user groups and their distinct needs.
- **Use appropriate methods per evolution stage** — partially violated. Labour is (correctly) running Lean/Six-Sigma style campaign ops for its Product components, but the same disciplined-delivery culture is being asked to design Genesis-stage GB Energy and Custom-Built housing and digital transformation, which need Agile experimentation and tolerance of failure. Mismatch risk.
- **Remove duplication / reduce bias** — a large cluster of Custom-Built policy areas (Workers' Rights, Economic Equality, Social Justice, Community Programs, Public Sector Investment) suggests possible unmodelled overlap. Government will likely consolidate them into fewer programme vehicles.
- **Think small (as in small teams)** — Research & Policy Dev has too many outbound edges; once in government this should decompose into departmental teams, not remain a central node.
- **A bias toward action** — the strong campaign-stage Product stack means Labour can execute its electoral phase effectively; the risk is that the same bias gets misapplied to Genesis-stage policy delivery.

### Recommended Actions

1. **Harden GB Energy / Climate Action now, before the election.** The Genesis-stage delivery vehicle is a headline pledge. Publish an operating-model white paper pre-manifesto so government day-one can stand up a team, not start one. This is the highest-risk component on the map.
2. **Pre-industrialise the housing delivery vehicle.** Treat Housing's inertia marker as a signal to invest now in shadow-teams / New Towns Commission architecture, so evolution to 0.42 happens inside Year 1 of government. Do not leave it to the Civil Service to design the vehicle.
3. **Stabilise Private Sector Collaboration as a governing capability, not a campaign tactic.** Move it from bespoke CEO round-tables to a named institutional vehicle (business council with statutory basis) — that is the path from 0.36 to 0.55.
4. **Decompose Research & Policy Dev upon entering government.** Break the star topology by devolving policy development into departmental teams under a shared doctrine. Otherwise it becomes a throughput bottleneck for every legislative priority.
5. **Name the methods mismatch explicitly.** Industrialised campaign culture does not transfer to Genesis-stage policy delivery. Tag Climate Action, Housing, Digital Transformation, and Workers' Rights delivery as requiring distinct operating cultures (exploration, prototyping, failure tolerance) with separate governance from the Product-stage Whitehall stack.

### Build vs. Buy Assessment

| Component | Recommendation | Rationale |
|---|---|---|
| Public Trust | Build | Bespoke to this leadership's ethical reset; cannot be outsourced. |
| Policy Platform | Build | Unique to Labour; differentiation from incumbent and from previous Labour iterations. |
| Private Sector Collaboration | Build | Genuine governing capability Labour must own; do not delegate to CBI-style intermediaries. |
| Workers' Rights (New Deal) | Build | Policy identity; cannot be outsourced to statutory bodies without losing political signal. |
| Economic Equality / Fiscal Framework | Build | Bespoke to Reeves; fundamental to Labour's economic credibility. |
| Climate Action (GB Energy) | Build (Genesis) | No off-the-shelf publicly-owned energy vehicle to buy; must be invented. |
| Housing delivery vehicle | Build | Market has failed for 40 years; purchasing existing delivery capacity is not possible at scale. |
| Campaign Strategy | Buy / rent | Mature Product; use agencies, vendors, modern GE tooling. Labour already does this. |
| Media Relations | Buy / rent | Standard PR/press-office Product. |
| Voter Data & Analytics | Buy | Commodity-adjacent Product with specialised vendors. |
| Healthcare, Education, International Relations, National Security policy delivery | Buy / inherit | Existing Product/Commodity machinery; reform, do not rebuild. |
| Funding Infrastructure, Electoral Regulation | Utility (inherited) | Not a choice — shared national rails. |

### Evolution Predictions (12-24 months)

- **Campaign Strategy 0.58 → 0.70.** Post-election the full operation will professionalise further into a semi-permanent Labour campaign capability, approaching utility once in government.
- **Private Sector Collaboration 0.36 → 0.55.** Business Council, Industrial Strategy Council and sectoral partnerships will institutionalise the ad-hoc engagement.
- **Research & Policy Dev 0.42 → 0.55.** Moves into government, decomposes into departmental teams with shared doctrine.
- **Infrastructure Development 0.50 → 0.58.** National Wealth Fund operating, Planning and Infrastructure Bill passed, NSIP streamlined.
- **Digital Transformation 0.42 → 0.55.** GDS 2.0 / AI Opportunities Unit-style programmes move from aspiration to delivery vehicles.
- **Housing Policy 0.26 → 0.42.** Only if planning reform succeeds. Inertia is real; the arrow is contingent not predicted.
- **Climate Action (GB Energy) 0.14 → 0.42.** GB Energy incorporates, appoints leadership, takes first investment decisions. Still Custom-Built at best in 24 months — will not reach Product.
- **Counter-forces.** A hostile Office for Budget Responsibility fiscal event, a cost-of-living shock, or trade-union disputes could arrest the campaign-stage machinery and force Labour back to bespoke crisis-management methods on issues currently treated as Product.

### Open Questions

1. **Does GB Energy actually get stood up before the next Spending Review window?** The map's single Genesis component is also a headline pledge. If it cannot move rightward in 12 months, the climate agenda stalls.
2. **Can Labour's campaign-stage cultural norms (discipline, delivery, centralised comms) survive contact with Genesis-stage policy delivery?** Or will the methods mismatch surface as public delivery failures in Year 2?
3. **Where does the Research & Policy Dev function actually live in government?** Inside No. 10? Inside a strengthened Cabinet Office? Inside departments? The answer determines whether the bottleneck observed on this map persists.

---

## Annotations on the Map

| # | Note | Position [y, x] |
|---|---|---|
| 1 | Campaign op industrialising under McSweeney — nearing Product maturity. | [0.78, 0.42] |
| 2 | Business engagement being actively invented as a governing capability. | [0.66, 0.24] |
| 3 | Climate / Housing delivery vehicles are still Custom-Built / Genesis. | [0.32, 0.22] |
| 4 | Governing utilities (civil service, electoral regulation) Labour inherits day one. | [0.15, 0.92] |

---

## Scope Note

The scenario enumerates 30+ components (3 anchors, 3 visible value items, 7 campaign/engagement systems, 3 policy apparatus elements, 14 substantive policy areas, 4 infrastructure utilities). The skill recommends 8-15 components with submaps for larger scopes. This map covers the full enumeration in one view because the user asked for coverage of all listed items; in production the 14 substantive policy areas would each become submaps off the Research & Policy Dev component, so the main map would decompose to ~16 nodes. The `draft.owm` file is designed to be split that way: `submap Healthcare Access (NHS) [0.52, 0.64]` in the main map, with a sibling `nhs.owm` holding its own full value chain.
