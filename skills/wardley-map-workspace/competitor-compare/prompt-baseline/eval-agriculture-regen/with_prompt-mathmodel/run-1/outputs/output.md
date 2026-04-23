# Wardley Map — Regenerative Farming Landscape (August 2022)

Generated using only `prompts/wardley_map_generator.md` (prompt-only baseline). The OWM source is in `draft.owm` in this directory.

## 1. Scoping notes

August 2022 context that shaped this map:

- Russia's invasion of Ukraine in Feb 2022 had just spiked synthetic-fertiliser (ammonia / urea) prices, briefly exposing the petrochemical tail of industrial agriculture.
- UK's Environmental Land Management scheme (ELM / SFI) was publishing early Standards; the EU CAP 2023–27 reform was locked in but eco-schemes were undefined in practice.
- UN Food Systems Summit follow-up (2021 → 2022) and the run-up to COP27 in Sharm el-Sheikh (Nov 2022) were the main multilateral venues.
- CBD COP15 (Kunming-Montreal) was drafted but not yet agreed (agreement came Dec 2022 — so in Aug 2022 it's still a draft on the table).
- The regenerative label was hot commercially but still had no harmonised outcome-based grading; "Regenerative Organic Certified" (ROC), Savory's EOV, and retailer-specific frameworks were competing.
- Soil-carbon MRV (measurement, reporting, verification) was an active VC / corporate-offset market but methodology disputes were live.

These shape where I placed labels, measurement, and treaties on the evolution axis.

## 2. Tuple summary

- **Anchors U (4):** Consumer, Farmer, National Government, Supranational Body (UN / FAO / IPCC). Four because the landscape genuinely has four user types with different needs — retailers appear as a mediating component, not an anchor, because they satisfy consumer demand.
- **|V| ≈ 39** components across six layers (user-facing outputs, mediating institutions, farm practices, measurement stack, energy matrix, conservation substrate + treaties).
- **Component types τ** (implicit): the map mixes Activities (practices, output), Data (measurement, traceability), Knowledge (agronomy, soil microbiology), and treaty/policy artefacts. I did not explicitly annotate τ because the scenario asked for the landscape, not a build/buy decomposition.

## 3. Evolution placements — highlights

Placements follow the 4-row cheat-sheet method (Ubiquity, Certainty, User Perception, Publication Types), averaged and rounded to one decimal:

| Component | Stage | ε |
|---|---|---|
| Fossil Fuel Energy | IV | 0.96 |
| Photosynthesis | IV (natural universal) | 0.95 |
| Synthetic Fertiliser (N-P-K) | IV | 0.92 |
| Monoculture Cropping | IV | 0.85 |
| Food Retail Shelf | IV | 0.82 |
| Land Tenure / Property Rights | IV | 0.85 |
| Farm Management Software | III | 0.65 |
| On-Pack Eco-Label | III | 0.60 |
| Policy Levers (Subsidies / Taxes) | III | 0.55 |
| Retailer Sourcing Standard | III | 0.55 |
| No-Till / Reduced Till | III | 0.50 |
| Cover Cropping | II | 0.45 |
| Certification Body (Regen specifically) | II | 0.50 |
| Remote Sensing / Satellite MRV | II | 0.45 |
| National Farm Payment Scheme | II | 0.40 |
| Crop Diversity / Intercropping | II | 0.30 |
| Regen Ag Knowledge (Agronomy) | II | 0.30 |
| Soil Carbon Measurement | II | 0.28 |
| Carbon / Climate Label | I–II | 0.25 |
| Agroforestry | I–II | 0.22 |
| Soil Microbial Community (as a managed object) | I–II | 0.22 |
| Outcome-Based Grading Schema | I | 0.20 |
| Soil Microbiology Science | I | 0.18 |
| Mycorrhizal Networks (as a managed object) | I | 0.15 |

Photosynthesis and fossil fuels look paradoxical on a Wardley axis because they are natural/physical universals, not products. I placed them in Stage IV because in terms of market ubiquity and standardisation they behave like commodity inputs — every farm taps them, they're understood at the level of certainty required to use them, and publications treat them as routine. This is a known modelling edge case for "natural" components.

## 4. What's still knowledge-based vs locked-in

**Still knowledge-based (ε < 0.4), expected to move but has not):**

- Agroforestry, crop diversity / intercropping, integrated livestock grazing
- Outcome-based grading, soil-carbon MRV methodology, regen agronomy as a codified discipline
- Soil microbiology science and specifically the management of mycorrhizal networks
- The Kunming-Montreal biodiversity text (a draft in Aug 2022)

This cluster is the map's "Stage I–II island". The practices work — there's decades of research and case-study evidence — but the recipes are not commoditised; every farm tailors them; training, agronomic support, and context-specific knowledge are the bottlenecks.

**Industrial practice locked in (ε > 0.8, marked `inertia` where resistance is structural):**

- Monoculture cropping + synthetic fertiliser + pesticides/herbicides, all tethered to petrochemical feedstocks and fossil fuel energy.
- Extractive industrial practice itself as a bundled pattern.
- Land tenure patterns that lock short-horizon leasing against long-horizon soil investment.

Inertia forms most visibly in play (see §6):
- **Sunk capital** (farm machinery designed for monoculture + spray regimes).
- **Supplier inertia** — agrochemical majors' distribution channels.
- **Co-evolved practice / skill fit** — agronomists, extension services, lender risk models all assume the industrial recipe.
- **Second-sourcing risk** for farmers moving off N-P-K without a trusted replacement protocol.

## 5. Supply-chain awareness picture

Tracing from consumer to soil:

- Consumer → Label → Certification → Traceability → Farm Management Software / Remote Sensing → Practice → Soil
- Every hop currently loses resolution. The labels in 2022 (Regenerative Organic Certified, LEAF Marque, Demeter, various retailer-specific "regen" marks) are **Stage II/III product-level** signals that do not yet carry verified outcome data.
- Supply-chain traceability is improving (blockchain pilots, satellite MRV, retailer direct-sourcing programmes) but sits around ε ≈ 0.35 — clearly in Custom Built. Retailers are building bespoke stacks; there is no shared utility layer.
- The Carbon / Climate label is still Genesis-adjacent (ε ≈ 0.25). Soil-carbon claims are methodologically contested and rely on MRV that is itself transitioning.

The **gap between visible labels (ν ≈ 0.72) and the underlying measurement they depend on (ν ≈ 0.28–0.44)** is the structurally fragile part of this landscape — a long dependency with an immature base.

## 6. Strategic analysis

### (a) Top 3 by differentiation pressure D(v) = ν(v)·(1 − ε(v))

1. **Policy Levers (Subsidies / Taxes)** — D = 0.82 · 0.45 = **0.369**. Visible to farmers and consumers, still in Product stage with room to move toward outcome-based commodity grading. A national government that gets this right defines its agricultural decade.
2. **On-Pack Eco-Label** — D = 0.74 · 0.40 = **0.296**. Directly shapes consumer purchase; fragmented standards mean a retailer / certifier that locks in a widely trusted label captures the story.
3. **Retailer Sourcing Standard** — D = 0.70 · 0.45 = **0.315**. Bigger-than-it-looks lever: major retailers setting outcome-based sourcing rules can force practice change faster than policy in the short term.

(Certification Body D = 0.68 · 0.50 = 0.340 is also in this cluster; I ordered by strategic leverage, not raw D.)

### (b) Top 3 by commodity leverage K(v) = (1 − ν(v))·ε(v)

1. **Fossil Fuel Energy** — K = 0.90 · 0.96 = **0.864**. Already a utility; the leverage play is *substitution*, not management.
2. **Petrochemical Feedstocks** — K = 0.86 · 0.95 = **0.817**. Same logic; the August 2022 price shock proved this.
3. **Synthetic Fertiliser (N-P-K)** — K = 0.80 · 0.92 = **0.736**. Commoditised globally but geographically fragile (Russia/Belarus potash, Ukraine urea). The substitution candidates (biological N fixation, precision application) sit far left.

### (c) Top 3 dependency risks R(a, b) = ν(a)·(1 − ε(b))

1. **(Carbon / Climate Label, Soil Carbon Measurement)** — R = 0.72 · 0.72 = **0.518**. A highly visible consumer-facing claim depending on Stage I–II measurement science. A methodology challenge can discredit the whole claim.
2. **(On-Pack Eco-Label, Outcome-Based Grading Schema)** — R = 0.74 · 0.80 = **0.592**. Labels are trusted because they imply an outcome grading that doesn't yet exist as a shared commodity.
3. **(Consumer Purchase Decision, Supply-Chain Traceability)** — via Retail Shelf, R = 0.90 · 0.65 = **0.585**. Visible decision depending on a still-custom-built traceability layer — vulnerable to greenwashing scandals.

### (d) Suggested gameplays (named from Wardley's catalogue)

Referencing the 61-play catalogue in `docs/catalogues/gameplay.md`:

- **Open Approaches** on Outcome-Based Grading Schema and Soil Carbon MRV — a public / open-standard grading regime accelerates Stage I–II content toward Stage III and undercuts fragmented certifier rent-seeking.
- **Use of Standards / Enforcement of Standards** on Supply-Chain Traceability and Certification — governments or retailer consortia can force convergence on a single traceability spec (an ISO-style move).
- **Co-opetition** among retailers on outcome-based sourcing — agree on a pre-competitive baseline for regen claims so the category grows; compete on quality above it.
- **Harvesting** — corporate players (food majors, ag-tech) will acquire early MRV start-ups; expect consolidation by 2024.
- **Pig in a Poke** risk — unscrupulous certifiers slap "regen" on weakly audited supply; retailers should avoid a race-to-the-bottom label.
- **Directed investment / Patience** on Regen Ag Knowledge (Agronomy) — treat extension services and farmer peer-networks as a Stage I component that needs patient capital, not quarterly ROI.
- **Sensible supplier exit / Second-sourcing** for fertiliser — the 2022 price shock is the trigger; biological N fixation + precision application become credible alternatives.
- **Undermining barriers to entry** for new measurement tech — satellite MRV plus soil sensors could commoditise the knowledge layer.

### (e) Doctrine violations / stresses

Referencing the 40-principle doctrine in `docs/catalogues/doctrine.md`:

- **"Focus on user needs" / "Know your users"** — the regen movement risks speaking past consumers; labels proliferate, consumer understanding does not. The map's four anchors make the multi-user reality explicit, which is the first doctrine fix.
- **"Use a common language"** — there is no shared definition of "regenerative" across certifiers, retailers, and governments. This is the single biggest doctrine gap in August 2022.
- **"Challenge assumptions"** — the assumption that industrial yield always beats regen yield is routinely repeated; the evidence at 2022 is actually mixed (e.g. rotational grazing, cover crops) and context-dependent. Assumption unchallenged.
- **"Manage inertia"** — ag incumbents have classic sunk-capital and co-evolved-practice inertia; anyone promoting transition must plan for it explicitly (subsidy transition paths, lender education, machinery retrofits).
- **"Think small"** — many national schemes (CAP, US Farm Bill) batch large programmes. The doctrinal move is to let many small, outcome-based contracts run in parallel and evolve the winners.
- **"Use standards where appropriate"** vs **"Be pragmatic"** — the temptation is to lock in a premature grading standard; patience at Stage I–II is doctrine-consistent.

## 7. What I did not do

- I did not forecast a time path for any evolution; the `evolve` markers are scenario targets, not predictions (per §9 of the prompt).
- I did not run the full 19-row cheat sheet; the 4-row quick method is what the prompt calls for as default and was used here.
- I did not annotate τ (component types) because the scenario asked for landscape, not build/buy framing.
- I did not render the map; the OWM file is in `draft.owm` and can be pasted into `onlinewardleymaps.com` for visualisation.
