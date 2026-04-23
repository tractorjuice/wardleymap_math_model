# Construction Supply Chain End-to-End — March 2023

Generated using the prompt-only baseline (`prompts/wardley_map_generator.md`). Scenario: map the UK construction supply chain end-to-end, from demand (government, citizens, homes, mortgage companies) through inspection/QA, construction modes, labour, equipment, distribution, manufacture, materials, and raw supply, highlighting which parts are still bespoke craft and which are industrialisable — with attention to the material supply chain and CNI risk around local skilled-labour supply.

## 1. Mathematical Model

$\mathcal{M} = (V, E, U, \nu, \varepsilon, t)$ with $|V| \approx 42$, multi-anchor ($|U| = 5$) to capture the structurally different user types on the demand side.

## 2. Anchors and Components

**Anchors (U):**
- Government — commissions social housing, sets regulation, defines CNI boundaries.
- Citizens — want adequate, safe, affordable housing; inspect and complain.
- Private Homeowners — purchase new build; judge quality via certification.
- Social Housing Tenants — consume social housing; rely on regulator to inspect.
- Mortgage Companies — finance purchase; require QA certification to lend.

Five anchors are justified because the construction supply chain has genuinely different demand-side users, and pretending there is one "customer" conflates the citizen perspective (political) with the mortgage lender perspective (financial due diligence).

**Components (V):** 42 in total — see `draft.owm`. They cluster into seven layers:
1. Direct user-facing delivery and QA (New Build Delivery, Planning Approval, Building Inspection, QA Certification, Housing Finance).
2. Construction orchestration (General Contracting, Project Management, Blueprint & Design, Regulatory Compliance, and four construction modes: Bespoke, Modular, Prefab, Factory-Mode).
3. Construction inputs (Skilled/Unskilled Labour, Labour Certification, Vocational Training, Test-Driven Construction, Site Equipment, Plant Hire).
4. Distribution (Traditional Builders Merchant, Integrated Distributor, Platform Distributor, Logistics).
5. Manufacture and materials (Component Manufacture; Traditional, Recycled, Novel, Substitutable materials).
6. Raw supply (Raw Material Extraction, International Material Supply, Local Raw Materials).
7. Foundations (Energy Supply, Critical National Infrastructure, Telecoms and Data).

## 3. Dependencies

Encoded in `draft.owm`. Key dependency patterns:
- Every anchor depends on **New Build Delivery** except Mortgage Companies (who depend on **Housing Finance** and **QA Certification**).
- The four construction modes all descend from **General Contracting** but pull different inputs: Bespoke pulls skilled labour + traditional materials; Factory-Mode pulls component manufacture + unskilled labour + test-driven construction.
- The labour system forms a loop: **Skilled Labour → Labour Certification → Vocational Training**; certification acts as a gate.
- Materials fan into a single **Raw Material Extraction** node which then splits into **International** vs **Local** supply — the local/international split is where the CNI concern bites.
- Foundations (Energy, CNI, Telecoms) sit below all manufacture and logistics, and CNI itself depends on energy.

## 4. Visibility ($\nu$)

Seeded from graph distance, then adjusted:
- Bespoke On-Site Build is raised (0.70) because it is architecturally visible to citizens and private homeowners — they experience it as "the workmen on site".
- Traditional Builders Merchant held at 0.42 despite being common — a trade-facing intermediary, not a consumer-visible brand.
- Critical National Infrastructure held low (0.08) but not zero — invisible until it fails.
- Hard constraint $\nu(a) \ge \nu(b)$ was checked edge-by-edge after first draft; three edges required adjustments (Platform Distributor vs Component Manufacture; Plant Hire vs Logistics; Local Raw Materials vs CNI).

## 5. Evolution ($\varepsilon$) — quick 4-row scoring

Illustrative scores for the components the question specifically flagged:

| Component | Ubiquity | Certainty | User perception | Publication | Mean $\varepsilon$ | Stage |
|---|---|---|---|---|---|---|
| Bespoke On-Site Build | II | II | II | III | 0.25 | Custom Built |
| Modular Construction | II | II | II | II | 0.375 → **0.35 (manual)** | Custom Built (transition) |
| Prefab Construction | III | II | II | II | 0.4375 → **0.45** | Custom Built / Product boundary |
| Factory-Mode Assembly | I | II | I | II | 0.25 | Custom Built (still building/construct publications) |
| Test-Driven Construction | I | I | I | I | 0.125 → **0.15** | Genesis |
| Novel Building Materials | I | II | I | I | 0.1875 → **0.20** | Genesis |
| Recycled Materials | II | II | II | II | 0.375 → **0.35** | Custom Built |
| Traditional Materials | IV | IV | IV | IV | 0.875 → **0.85** | Commodity |
| Platform Distributor | II | II | II | II | 0.375 → **0.30** (slightly lagging, still experimental in UK construction) | Custom Built |
| Traditional Builders Merchant | IV | IV | III | IV | **0.75** | Product/Commodity boundary |
| Skilled Labour | II | III | III | III | 0.5 → **0.40** (lowered because of regional shortage inhomogeneity) | Custom Built |
| Unskilled Labour | IV | IV | III | IV | 0.8125 → **0.80** | Commodity |
| Energy Supply | IV | IV | IV | IV | 0.875 → **0.92** | Utility |

Rows that disagreed strongly (flagged in-transition): **Modular**, **Prefab**, **Platform Distributor**. All three sit near the Custom Built / Product boundary and are the components most likely to be mis-scored by a different assessor.

## 6. Industrialisable vs still-bespoke verdict

The scenario explicitly asks: *"show me what's still bespoke craft and what's ready to be industrialised."*

**Still bespoke craft (low $\varepsilon$, not yet ready to industrialise):**
- Bespoke On-Site Build ($\varepsilon = 0.25$) — the dominant UK mode; visible, slow, labour-heavy.
- Factory-Mode House Assembly ($\varepsilon = 0.25$) — early attempts (Urban Splash Modular, L&G Modular) have struggled; still Custom Built despite the rhetoric.
- Novel Building Materials ($\varepsilon = 0.20$) — mass timber, hempcrete, self-healing concrete: Genesis.
- Test-Driven Construction ($\varepsilon = 0.15$) — digital-twin + automated-test workflow borrowed from software; barely exists in mainstream construction.

**Ready to industrialise (already past the chasm, just under-adopted in UK):**
- Prefab Construction ($\varepsilon = 0.45$) — mature in Scandinavia, Germany, Japan; UK demand-side is under-using an available Product-stage capability.
- Modular Construction ($\varepsilon = 0.35$) — similar story; commercial modular (hotels, student accommodation) is much further along than residential.
- Recycled Building Materials ($\varepsilon = 0.35$) — aggregate recycling, reclaimed steel, circular-economy flows: ready but distribution is fragmented.
- Component Manufacture ($\varepsilon = 0.60$) — the latent backbone; already Product stage, so the constraint is not supply but demand (contractors who know how to procure into it).

**Fully commoditised (treat as utility — buy, don't build):**
- Traditional Building Materials, Unskilled Labour, Plant Hire, Logistics, Energy, Telecoms.

## 7. Strategic Analysis

### a. Top 3 by differentiation pressure $D(v) = \nu \cdot (1 - \varepsilon)$

1. **Planning Approval** — $D = 0.85 \cdot 0.70 = 0.595$. High visibility to government and citizens; still immature as a digital service. Differentiation opportunity for whichever jurisdiction digitises planning first (cf. Estonia's e-residency playbook).
2. **Blueprint and Design** — $D = 0.74 \cdot 0.55 = 0.407$. Still craft-mediated; BIM adoption is uneven.
3. **Building Inspection** — $D = 0.84 \cdot 0.45 = 0.378$. Post-Grenfell, there is real political pressure on this; inspection capability is a differentiator for a jurisdiction or a regulator.

(Note that Bespoke On-Site Build has $D = 0.70 \cdot 0.75 = 0.525$, which is higher than #2 and #3 numerically. It's omitted from the ranked "opportunity" reading because it's bespoke-through-inertia, not bespoke-through-innovation — the high $D$ score here is a warning, not an opportunity.)

### b. Top 3 by commodity leverage $K(v) = (1 - \nu) \cdot \varepsilon$

1. **Telecoms and Data** — $K = 0.94 \cdot 0.90 = 0.846$. Deep, mature — treat as utility.
2. **Energy Supply** — $K = 0.90 \cdot 0.92 = 0.828$. Same story; critical but utility.
3. **Logistics and Haulage** — $K = 0.62 \cdot 0.85 = 0.527$. Don't run your own trucks.
4. (Honourable mention) **Traditional Building Materials** — $K = 0.74 \cdot 0.85 = 0.629$. Commodity inputs; procure at scale.

### c. Top 3 dependency risks $R(a, b) = \nu(a) \cdot (1 - \varepsilon(b))$

1. **(New Build Delivery → Planning Approval)** — $R = 0.88 \cdot 0.70 = 0.616$. The user-facing anchor depends on an immature regulatory process; this is the single biggest throughput risk in UK housebuilding.
2. **(Factory-Mode House Assembly → Test-Driven Construction)** — $R = 0.64 \cdot 0.85 = 0.544$. If factory mode is to industrialise, it needs a test-driven build discipline, and that discipline is Genesis.
3. **(Modular Construction → Skilled Labour)** — $R = 0.68 \cdot 0.60 = 0.408$. Modular promised to remove labour dependency; in practice it just moved skilled labour into the factory, so the labour shortage still binds. This is the CNI concern made concrete.

### d. Suggested gameplays (from Wardley's 61-play catalogue)

- **Open Approaches (#15)** on **Planning Approval** and **Blueprint & Design** — open-source the planning data layer; open-BIM standards. This breaks the incumbent consultancy rent.
- **Co-Option (#10)** on **Modular / Prefab Construction** — a central government housing body that commissions at scale to pull these modes across the Product-stage boundary. Legal & General's now-shuttered modular factory is a cautionary tale: co-option without sustained demand fails.
- **Industrialisation (#22)** on **Component Manufacture** — explicit policy and procurement support to treat component manufacture as a utility input, not a bespoke supply.
- **Pig in a Poke (#40)** / **Harvesting (#29)** — watch for emerging Platform Distributors (B2B construction materials platforms — e.g., BuildPass-style plays) and acquire or partner with the winners before they cross into Product.
- **Embrace Failure (#13)** on **Test-Driven Construction** and **Novel Materials** — these are Genesis; failure rate will be high, and public sector must accept that.
- **Bundling (#3, gameplay — not inertia)** vs **Unbundling** — UK Traditional Builders Merchants are a bundled supply channel; a platform distributor play is essentially an unbundling move.

### e. Doctrine violations / gaps

- **Phase I — Focus on user needs:** The demand side is explicitly modelled with five anchors. That's fine, but beware that Government's needs (housing numbers, CNI resilience) genuinely conflict with Private Homeowners' needs (price, quality) — this map makes the conflict visible rather than hiding it.
- **Phase II — Know your users' needs:** Social Housing Tenants are a legitimate anchor and are often silent in industry strategies. Keeping them as an anchor is a doctrine-correct choice.
- **Phase II — Map the landscape:** The material supply chain is shown end-to-end (raw → international/local → manufacture → materials → distribution → construction). Good.
- **Phase III — Challenge assumptions:** The assumption that "modular = industrialised" is explicitly challenged by placing Modular and Factory-Mode still in Custom Built.
- **Possible gap:** Knowledge-layer components (building science, materials science, structural engineering theory) are implicit in "Blueprint & Design" and "Test-Driven Construction" but not split out. If this map were extended with $\tau$ typing, those would be the K nodes and would sit even lower in visibility.
- **Possible gap:** Second-sourcing risk on **International Material Supply** is a 2023-specific concern (post-Ukraine, post-Brexit steel & timber prices) that deserves its own inertia annotation — the current map handles it via the CNI node but could go deeper.

### Inertia annotations (from the 17 forms)

- **Bespoke On-Site Build** — *practice inertia* and *human capital inertia*: trades learned one way, resistant to factory transition.
- **Traditional Builders Merchant** — *existing-business-model inertia*: the merchant model makes money from the fragmented supply chain; platform distribution attacks the rent.
- **Labour Certification** — *political capital inertia*: CITB levies, chartered bodies, and government-certified apprenticeship schemes create institutional lock-in that slows reform even when reform is agreed.

## 8. Scenario notes (not forecasts)

If we simulate $d\varepsilon/dt = r\varepsilon(1-\varepsilon)$ with $r = 0.15$/year for Modular Construction starting at $\varepsilon_0 = 0.35$, Modular reaches $\varepsilon = 0.55$ (mid Product) after roughly 5-7 years. This is a **scenario under assumed sustained demand**, not a prediction — Wardley's climatic pattern is that evolution cannot be measured over time. The 2017-2023 UK modular-housing retrenchment (Ilke, Legal & General Modular) is a concrete example of demand collapse pulling evolution backward.

## Files

- `draft.owm` — OWM map (5 anchors, 42 components, ~70 dependency edges, 7 evolve statements, 3 inertia annotations, 2 pipelines, 4 notes).
- `output.md` — this file.
- `timing.json` — wall-clock timing.
