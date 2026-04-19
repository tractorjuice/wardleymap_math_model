# UK Labour Party — Core Values and Policy Positioning (May 2024)

## Scenario

Map the landscape of the UK Labour Party's core values and policy positioning on the eve of the July 2024 general election. Include core values (equality, fairness, opportunity, community, responsibility), constituencies, policy levers (NHS, education, housing, climate, workers' rights), media relations, and party machinery. Identify what is **differentiating** vs **commoditising** in political positioning.

This is a multi-stakeholder political landscape (leadership, members, affiliated unions, electorate as voter-consumer, media as channel) so we target 40–55 components. The final map has 45 components (including 2 anchors) and 78 dependency edges.

---

## Map

```owm
title UK Labour Party Core Values and Policy Positioning (May 2024)
style wardley

// Anchors: the party has two user types
// The electorate is the primary user (whose vote is sought)
// Members are a secondary user (whose activism and subs sustain the machine)
anchor UK Electorate [0.99, 0.70]
anchor Party Member [0.95, 0.55]

// User-facing brand and offer
component Party Brand / Leadership Image [0.88, 0.50]
component Five Missions Narrative [0.85, 0.25]
component Manifesto 2024 [0.83, 0.55]
component Change Slogan [0.82, 0.65]

// User-facing policy levers (what voters see)
component NHS Commitment [0.80, 0.88]
component Workers Rights Package (New Deal for Working People) [0.78, 0.35]
component Housing Pledge (1.5m homes) [0.76, 0.55]
component Education Policy (VAT on private schools, breakfast clubs) [0.75, 0.45]
component Climate / GB Energy [0.73, 0.30]
component Fiscal Rules / Tax Pledges [0.72, 0.70]

// Constituencies (segments of the electorate, user-proximate)
component Red Wall Voters [0.70, 0.40]
component Core Urban Working-Class Base [0.68, 0.75]
component Middle-Class Swing Voters [0.66, 0.55]
component Young / First-Time Voters [0.62, 0.45]
component Scottish Voters [0.60, 0.40]
component Trade Union Members [0.58, 0.80]
component Muslim / Minority Communities [0.56, 0.50]

// Media and communications (close to user because perception-forming)
component Broadcast Media Relations (BBC, ITV) [0.65, 0.75]
component Press Strategy (tabloids, broadsheets) [0.63, 0.70]
component Social / Digital Campaigning [0.60, 0.55]
component Grassroots Canvassing [0.55, 0.85]
component Leader Media Appearances [0.68, 0.55]

// Mid-chain: policy and governance structures
component Shadow Cabinet [0.52, 0.60]
component Policy Forum / National Policy Forum [0.45, 0.65]
component Candidate Selection [0.42, 0.55]
component Campaign Strategy (Morgan McSweeney) [0.48, 0.45]
component Polling / Focus Groups [0.43, 0.75]
component Constituency Targeting Model [0.40, 0.50]

// Party machinery (deeper)
component Constituency Labour Parties (CLPs) [0.35, 0.70]
component National Executive Committee (NEC) [0.30, 0.65]
component Affiliated Trade Unions [0.28, 0.75]
component Fundraising / Donor Relations [0.32, 0.60]
component Membership Database / CRM [0.22, 0.80]

// Core values (Knowledge layer — widely accepted, low-visibility)
component Equality (value) [0.18, 0.78]
component Fairness (value) [0.16, 0.80]
component Opportunity (value) [0.15, 0.75]
component Community (value) [0.14, 0.72]
component Responsibility (value) [0.13, 0.70]

// Deeper institutional knowledge and foundations
component Social Democratic Tradition [0.10, 0.85]
component Post-Ideological Pragmatism (Starmerism) [0.12, 0.35]
component Party Constitution / Clause IV (revised) [0.08, 0.90]
component UK Electoral System (FPTP) [0.06, 0.95]
component Parliamentary Convention [0.05, 0.95]

// Dependencies — flow from user need down to foundations
UK Electorate->Party Brand / Leadership Image
UK Electorate->Five Missions Narrative
UK Electorate->Change Slogan
UK Electorate->Manifesto 2024
UK Electorate->NHS Commitment
UK Electorate->Workers Rights Package (New Deal for Working People)
UK Electorate->Housing Pledge (1.5m homes)
UK Electorate->Education Policy (VAT on private schools, breakfast clubs)
UK Electorate->Climate / GB Energy
UK Electorate->Fiscal Rules / Tax Pledges
UK Electorate->Broadcast Media Relations (BBC, ITV)
UK Electorate->Press Strategy (tabloids, broadsheets)
UK Electorate->Leader Media Appearances

Party Member->Manifesto 2024
Party Member->Constituency Labour Parties (CLPs)
Party Member->Policy Forum / National Policy Forum
Party Member->Candidate Selection
Party Member->Grassroots Canvassing

// Brand and narrative rest on underlying policy + comms
Party Brand / Leadership Image->Leader Media Appearances
Party Brand / Leadership Image->Campaign Strategy (Morgan McSweeney)
Party Brand / Leadership Image->Polling / Focus Groups
Five Missions Narrative->Policy Forum / National Policy Forum
Five Missions Narrative->Shadow Cabinet
Change Slogan->Campaign Strategy (Morgan McSweeney)
Manifesto 2024->Shadow Cabinet
Manifesto 2024->Policy Forum / National Policy Forum

// Policy levers depend on shadow cabinet and deeper values
NHS Commitment->Fairness (value)
NHS Commitment->Shadow Cabinet
Workers Rights Package (New Deal for Working People)->Affiliated Trade Unions
Workers Rights Package (New Deal for Working People)->Fairness (value)
Workers Rights Package (New Deal for Working People)->Shadow Cabinet
Housing Pledge (1.5m homes)->Opportunity (value)
Housing Pledge (1.5m homes)->Shadow Cabinet
Education Policy (VAT on private schools, breakfast clubs)->Opportunity (value)
Education Policy (VAT on private schools, breakfast clubs)->Shadow Cabinet
Climate / GB Energy->Responsibility (value)
Climate / GB Energy->Shadow Cabinet
Fiscal Rules / Tax Pledges->Responsibility (value)
Fiscal Rules / Tax Pledges->Shadow Cabinet

// Constituencies are segments the electorate maps into, depend on targeting
Red Wall Voters->Constituency Targeting Model
Core Urban Working-Class Base->Trade Union Members
Middle-Class Swing Voters->Constituency Targeting Model
Young / First-Time Voters->Social / Digital Campaigning
Scottish Voters->Candidate Selection
Trade Union Members->Affiliated Trade Unions
Muslim / Minority Communities->Grassroots Canvassing

// Media channels depend on press and campaign ops
Broadcast Media Relations (BBC, ITV)->Campaign Strategy (Morgan McSweeney)
Press Strategy (tabloids, broadsheets)->Campaign Strategy (Morgan McSweeney)
Social / Digital Campaigning->Membership Database / CRM
Grassroots Canvassing->Constituency Labour Parties (CLPs)
Grassroots Canvassing->Membership Database / CRM
Leader Media Appearances->Campaign Strategy (Morgan McSweeney)

// Campaign depends on polling and targeting
Campaign Strategy (Morgan McSweeney)->Polling / Focus Groups
Campaign Strategy (Morgan McSweeney)->Constituency Targeting Model
Polling / Focus Groups->Membership Database / CRM
Constituency Targeting Model->Membership Database / CRM

// Shadow cabinet depends on selection, NEC
Shadow Cabinet->Candidate Selection
Shadow Cabinet->National Executive Committee (NEC)
Candidate Selection->National Executive Committee (NEC)
Candidate Selection->Constituency Labour Parties (CLPs)
Policy Forum / National Policy Forum->National Executive Committee (NEC)
Policy Forum / National Policy Forum->Affiliated Trade Unions

// Machinery rests on affiliates and constitution
Constituency Labour Parties (CLPs)->Party Constitution / Clause IV (revised)
National Executive Committee (NEC)->Party Constitution / Clause IV (revised)
National Executive Committee (NEC)->Affiliated Trade Unions
Affiliated Trade Unions->Party Constitution / Clause IV (revised)
Fundraising / Donor Relations->Affiliated Trade Unions
Fundraising / Donor Relations->Membership Database / CRM

// Values rest on traditions
Equality (value)->Social Democratic Tradition
Fairness (value)->Social Democratic Tradition
Opportunity (value)->Social Democratic Tradition
Opportunity (value)->Post-Ideological Pragmatism (Starmerism)
Community (value)->Social Democratic Tradition
Responsibility (value)->Post-Ideological Pragmatism (Starmerism)

// Traditions and constitution rest on electoral system
Social Democratic Tradition->Party Constitution / Clause IV (revised)
Campaign Strategy (Morgan McSweeney)->Post-Ideological Pragmatism (Starmerism)
Party Constitution / Clause IV (revised)->Parliamentary Convention
UK Electoral System (FPTP)->Parliamentary Convention

// Strategic evolution arrows (May 2024 scenario)
evolve Five Missions Narrative 0.55
evolve Workers Rights Package (New Deal for Working People) 0.60
evolve Climate / GB Energy 0.55
evolve Post-Ideological Pragmatism (Starmerism) 0.60

note Differentiation zone [0.75, 0.25]
note Commoditising pledges [0.78, 0.82]
note Knowledge layer (values) [0.15, 0.80]
```

---

## Strategic analysis

### a. Differentiation opportunities (top 3)

The differentiating zone is user-facing **and** still-immature — where Labour can claim ownership of an idea the public cannot get elsewhere:

1. **Five Missions Narrative** (Genesis, ε ≈ 0.25) — the "national missions" framing (growth, NHS, opportunity, clean energy, safe streets) is *novel branding* for UK politics in 2024. No other UK party is using mission-driven government as an organising frame. This is the single highest differentiation lever: highly visible, low-commodity. If the party owns the narrative before it is copied or diluted by office, it becomes durable identity.
2. **Climate / GB Energy** (Custom Built, ε ≈ 0.30) — GB Energy as a publicly-owned clean-power company is a concrete, branded policy product that neither the Conservatives, LibDems, nor Reform offer. High-visibility, still novel. Clear ownership of the industrial-strategy lane.
3. **Workers Rights Package (New Deal for Working People)** (Custom Built, ε ≈ 0.35) — the single most substantively differentiated policy bundle from the Conservative offer: day-one rights, ending zero-hours exploitation, collective-bargaining expansion. Highly visible to a base constituency; union-backed so it has supply-side durability.

A secondary candidate is **Post-Ideological Pragmatism (Starmerism)** (ε ≈ 0.35) as a positioning lens — "not ideological, just what works" is differentiated from Conservative ideological populism and Reform insurgent identity, though it is intentionally *low* visibility (a stance, not a slogan).

### b. Commodity-leverage candidates (top 3)

Components where Labour should *not* try to out-innovate the competition because the policy space is already commoditised — voters expect the pledge, and differentiation must come from credibility of delivery rather than novelty of content:

1. **NHS Commitment** (Commodity +utility, ε ≈ 0.88) — every major UK party since 1948 has pledged to defend the NHS. The commitment itself is a utility; the differentiation is in delivery vehicles (waiting list targets, workforce plans). Don't contest the label — harvest the trust premium Labour still has on the topic.
2. **Fiscal Rules / Tax Pledges** (Product +rental, ε ≈ 0.70) — "iron-clad" fiscal rules have become the standard entry ticket for any 21st-century UK opposition. Rachel Reeves's framing mirrors Gordon Brown's 1997 playbook. Treat as commodity-of-credibility: match the Conservatives to neutralise the attack.
3. **Housing Pledge (1.5m homes)** (Product +rental, ε ≈ 0.55) — housing targets are table stakes in 2024 (Conservatives pledged 300k/yr, LibDems 380k, Labour 1.5m over a parliament). The number is commoditising; differentiation must come from planning-reform specifics.

### c. Dependency risks (top 3)

Visible components resting on less-mature or fragile foundations (user-visible promises that depend on custom-built or externally-controlled machinery):

1. **Five Missions Narrative → Policy Forum / National Policy Forum** — a user-facing Genesis-stage narrative depends on an internal, semi-contested policy-making body where affiliated unions and CLPs can dilute or reshape pledges. If the forum churns, the narrative loses coherence.
2. **Workers Rights Package → Affiliated Trade Unions** — the single most-differentiated policy bundle depends on unions whose own priorities may outpace what a centrist electoral coalition can sustain in office. Highly visible pledge, politically-controlled foundation.
3. **Party Brand / Leadership Image → Polling / Focus Groups** — the Starmer "change" brand is reverse-engineered from polling. If the polling signal noisily shifts (e.g., Gaza-related dissent among Muslim communities, a media-manufactured scandal), the brand has no independent source of meaning to fall back on.

A close fourth: **NHS Commitment → Shadow Cabinet** — high-visibility pledge depends on the credibility of Wes Streeting's reform agenda, which is itself contested within the party.

### d. Suggested gameplays

Named plays from Wardley's 61-play catalogue:

- **#1 Focus on user needs** — the Five Missions Narrative re-anchors the party on electorate needs rather than internal factional debates. Core play; reinforce it.
- **#26 Differentiation** — on Workers Rights, GB Energy, and the Mission framing. These are the identity-forming differentiators; do not dilute them in office.
- **#44 Tower and Moat** — the Missions Narrative is the tower; Post-Ideological Pragmatism and Campaign Strategy (McSweeney's operation) are the moat. Protect the tower by keeping delivery credible.
- **#56 First mover** on GB Energy — establish the public-energy-company category before the Conservatives copy it. Legislation in the first session is the first-mover lock-in.
- **#36 Directed investment** on Polling / Focus Groups and Constituency Targeting Model — the party's winning operation is built on data and segmentation sophistication (McSweeney's Blue Labour-influenced targeting). Keep investing.
- **#43 Sensing Engines (ILC — Innovate, Leverage, Commoditise)** — the party's policy forum should operate as a sensing engine: spot movement in civic organisations (food banks, tenants' unions, NHS campaigns), leverage into policy experiments, commoditise the winners into manifesto pledges.
- **#15 Open Approaches** on VAT-on-private-schools and breakfast clubs — these small, concrete policies can be open-sourced as campaign messaging without losing distinctiveness, because the *delivery infrastructure* (schools, HMRC) is the moat.
- **#29 Harvesting** on the commoditised pledges (NHS, fiscal rules, housing targets) — don't reinvent; match the commodity envelope and compete on delivery credibility.
- **#45 Two factor** — Labour uniquely has two reinforcing user groups: the electorate (votes) and members + affiliated unions (activism + money). Each strengthens the other. The risk: decisions that please one can alienate the other (e.g., Gaza, Rosie Duffield). Manage the two-sided tension deliberately.
- **#41 Alliances** with civic organisations (38 Degrees, Hope Not Hate, climate groups) — reduces grassroots canvassing cost and adds credibility on specific issues without policy concessions.
- **#7 Education** on GB Energy — voters do not yet have a mental model of what a public energy company does. Explaining before launch reduces inertia forms #6 (confusion over method) and #8 (skill acquisition cost — voters learning a new civic concept).

### e. Doctrine notes

Checking the map against Wardley's 40 doctrine principles:

- **Doctrine #1 Focus on user needs** — satisfied; the map is correctly anchored on the Electorate, with a second anchor for Members to represent the two user-types.
- **Doctrine #10 Know your users** — satisfied by the two-anchor structure. The constituency sub-segments (Red Wall, Middle-Class Swing, Young, Scottish, Muslim, etc.) add resolution.
- **Doctrine #13 Manage inertia** — partially satisfied. The map flags the Affiliated Trade Unions and NEC as deep-machinery dependencies; these carry consumer inertia (members' habitual expectations) and supplier inertia (existing power structures). Needs active management, not just acknowledgement.
- **Doctrine #12 Have a systematic mechanism of learning** — Polling / Focus Groups + Sensing Engines (ILC) via the Policy Forum provide this in principle; in practice the forum's institutional conservatism limits the learning loop. Mild violation.
- **Doctrine #33 There is no one culture** — the map shows Red Wall, Middle-Class Swing, Trade Union Members, and Muslim Communities as distinct constituencies. The party must run different messaging cultures (pioneer/settler/town-planner equivalents) for each.
- **Possible violation — Doctrine #23 Be pragmatic** — the Fiscal Rules / Tax Pledges component is rigid to the point of constraining mission delivery. Over-constraining future choice for near-term electoral credibility is a classic trade-off but is worth flagging.

### f. Climatic context

Which of Wardley's 27 climatic patterns are actively shaping this map:

- **#3 Everything evolves** — the Starmer-era positioning is itself evolution of the New Labour / Blair-era template, now commoditised. The Five Missions are Labour's attempt to innovate past a commoditised centre-left script.
- **#15–17 Inertia** — Affiliated Trade Unions' inherited power in candidate selection and policy forum is a high-weight supplier-side inertia; it simultaneously underwrites differentiation (Workers Rights) and constrains pragmatism (any attempt to moderate union-preferred positions triggers internal conflict).
- **#18 Evolution is not measurable over time or adoption** — directly relevant to this map. The position of the Five Missions Narrative on the evolution axis is a judgment about novelty-in-market, not about when Labour announced it.
- **#27 Product-to-utility punctuated equilibrium** — the NHS Commitment sits well past this punctuation. Housing Pledges are currently punctuating: the market has shifted from "party-specific housing vision" to "commoditised numeric target".
- **#22 Competitors will copy** — GB Energy, Mission framing, and the Workers Rights package will be partially copied by the Conservatives or emulated by LibDems within 2–3 years. The first-mover window is narrow.
- **#24 Competition drives evolution** — the 2019–2024 cycle in which the Conservative Party internalised many Labour-style public-spending positions has accelerated commoditisation of what was previously a Labour differentiator (NHS funding, Levelling Up ≈ regional policy).

### g. Deep-placement notes

Components where I ran closer-look reasoning rather than relying on a single cheat-sheet pass:

- **Five Missions Narrative (ε ≈ 0.25, Genesis)** — cheat-sheet rows pointed at Genesis (novel, exciting, leadership-dependent, few UK precedents). Confirmed by: the framing was new in the September 2023 conference; the New Labour "pledge card" of 1997 is a historical analogue, not a direct precedent; no other 2024 UK party uses the same mission-driven frame. No downward adjustment.
- **NHS Commitment (ε ≈ 0.88, Commodity +utility)** — all four cheat-sheet rows unambiguous Stage IV (universal ubiquity since 1948, commonly-understood, standard — "defend the NHS" is table stakes). Noted: the *policy-delivery vehicles* within that commitment (workforce plan, reform package) are not Stage IV; only the symbolic pledge is.
- **Workers Rights Package (ε ≈ 0.35, Custom Built)** — rows disagreed: the general idea of labour-market regulation is Stage III–IV, but the specific 2024 "New Deal for Working People" bundle (day-one rights, zero-hours restriction, expanded collective bargaining) is more novel. Placed at edge of Genesis / Custom Built to reflect the bundle rather than the category. Uncertainty range: 0.30–0.45.
- **Housing Pledge (ε ≈ 0.55, early Product +rental)** — initial cheat-sheet placed around 0.45 (Custom Built, because the *delivery* is uncertain), but considering that all three major parties have numeric housing targets in 2024, the commitment itself is commoditising to Product. Shifted up. Delivery-mechanism is a separate story.
- **Post-Ideological Pragmatism / Starmerism (ε ≈ 0.35)** — novel in UK Labour tradition (which has cycled between Blairite third-way and Corbyn-era socialism); too early in its life to be a stable product. Rows gave 0.25–0.45 range. Placed mid-range as a Custom Built positioning stance.

### h. Caveat

Evolution placements and `evolve` trajectories here are **scenarios, not forecasts**. Wardley's climatic pattern #18 states explicitly: *"you cannot measure evolution over time or adoption."* Political positioning evolves in response to events, adversary behaviour, and contingent crises. This map is a May 2024 snapshot; a post-election, in-office map would look different (many pledges move from Genesis/Custom to Product as they become delivery programmes; new Custom-Built differentiation must be created to replace them, or the party drifts into pure commodity positioning and loses identity).

---

## Validation record

```
$ python3 ${CLAUDE_SKILL_DIR}/scripts/validate_owm.py draft.owm
OK: 45 components/anchors, 78 edges — no violations.
```

All edges satisfy ν(source) ≥ ν(target); all coordinates are in [0, 1]; no typo'd edge endpoints.

---

## Summary — differentiating vs commoditising

| | Differentiating (Genesis / Custom Built) | Commoditising (Product (+rental) / Commodity (+utility)) |
|---|---|---|
| **Narrative** | Five Missions; Post-Ideological Pragmatism | Change slogan; generic "time for change" framing |
| **Policy levers** | Workers Rights (New Deal); GB Energy / Clean Power; mission-based government | NHS pledge; fiscal rules; housing numeric targets; education funding baselines |
| **Constituencies** | Red Wall recovery targeting (Custom); Young/first-time voter digital play | Union-aligned Working-Class Base; Middle-Class Swing messaging (well-worn) |
| **Media** | Social / digital campaigning ML segmentation; grassroots sensing | Broadcast-media relations; press strategy with tabloids |
| **Machinery** | Campaign Strategy (McSweeney operation — novel discipline in Labour) | CLPs; NEC; affiliated-union structure; NPF |
| **Values** | *(none in differentiating zone — values are Knowledge layer, deliberately commoditised)* | Equality, Fairness, Opportunity, Community, Responsibility — all widely accepted, low-visibility Knowledge |

**The strategic read:** Labour's moat in May 2024 is a combination of **novel framing (Missions)** + **concrete differentiated policy (GB Energy, Workers Rights)** + **disciplined campaign operation (McSweeney / polling / targeting)**, sitting on top of **commoditised positional pledges (NHS, fiscal rules, housing)** that neutralise attacks. The core values layer is deliberately held as widely-shared, uncontested Knowledge — values are not where parties differentiate. Differentiation happens in the **policy bundles and narrative** that translate shared values into a specific offer.

The main risks: (1) the differentiators will be copied within 2–3 years; (2) the machinery layer (unions, NEC) holds veto power that can dilute differentiation in office; (3) the brand is polling-derived, so it has thin independent identity to fall back on if polling signal shifts.
