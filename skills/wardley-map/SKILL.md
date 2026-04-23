---
name: wardley-map
description: Generate a Wardley Map from a scenario description using a formal mathematical model. Produces OWM-format output (with an optional Mermaid wardley-beta block for GitHub rendering) and strategic analysis grounded in Wardley's cheat sheet, 61 gameplays, and 40 doctrine principles. Use this skill whenever the user asks for strategic reasoning about the components of a business, product, or system — specifically when they mention any of value chain, strategic positioning, competitive landscape, strategic moat, component evolution, genesis-to-commodity spectrum, build-vs-buy across multiple components, where to invest engineering effort, what to commoditise or outsource, mapping a business or platform or marketplace strategically, or explicitly "Wardley map". Always trigger when "Wardley" appears in the request. Also trigger when the user describes a business or system and asks about strategic roadmap, moats, or board-level positioning — even without naming the framework. Skip for flowcharts, UX journey maps, process swimlanes, architecture diagrams, data pipeline diagrams, skills matrices, MECE breakdowns, Porter's five forces, marketing positioning statements, or definitional questions about what a Wardley map is.
argument-hint: <scenario description>
allowed-tools: Read, Grep, WebSearch, WebFetch, Bash, Write
---

# Wardley Map Generator

Generate a Wardley Map for the scenario in `$ARGUMENTS`, following the formal mathematical model below. Output OWM text plus a strategic analysis.

If `$ARGUMENTS` is empty, ask the user for a scenario description before proceeding.

---

## 1. The mathematical model

A Wardley Map is the tuple:

    M = (V, E, U, ν, ε, t)

- **V** = set of components
- **E ⊆ V × V** = directed dependency edges. `(a, b) ∈ E` means "a depends on b".
- **U ⊆ V** = anchor set — one or more user-need nodes. Real maps often have multiple user types.
- **ν: V → [0, 1]** = visibility function (Y-axis). Higher = closer to the user.
- **ε: V → [0, 1]** = evolution function (X-axis). Higher = more commoditised.
- **t** = time (optional; used only for dynamics)

Optional: **τ: V \ U → {A, P, D, K}** — component type (Activity, Practice, Data, Knowledge). Use when the map benefits from distinguishing types.

---

## 2. Procedure

### Step 0 — Strategic context (frame before you list)

Before listing any component, state — in the output, not just internally — the four framing decisions the rest of the map hangs on. Maps built without an explicit question tend to generalise, producing plausible-looking outputs that don't answer anything.

1. **Strategic question.** What decision does this map inform? ("Should we build or buy our auth system?" is stronger than "map our architecture".)
2. **User anchor(s).** Who sits at the top of the value chain? Name them.
3. **Core needs.** The 2–4 most important needs those users have.
4. **Scope boundary.** One product? One business unit? An industry landscape? Specify.

If the user's scenario didn't pin any of these down, pick the most defensible answer, record it in an "Assumptions" block at the top of the output, and flag it as an assumption the user can correct. **A map with the wrong question in mind gets the wrong components.** It's better to be wrong visibly than wrong invisibly.

### Step 1 — List components and anchors

- Anchor set `U`: the user need(s). If the scenario has multiple user types (e.g., customer AND artisan), use multiple anchors.
- Then list Activities, Practices, Data, Knowledge the users depend on.
- Use concrete nouns, not slogans.

**Density guidance — how many components?**

Wardley's own published maps average **~40 components**. Use scenario type as a target:

| Scenario type | Target count | Examples |
|---|---:|---|
| Single product or narrow function | 20–30 | tea shop, one checkout flow, single SaaS feature |
| Landscape of an industry or domain | 35–45 | retail customer journey, SaaS invoicing market, cybersecurity posture |
| Multi-stakeholder system (regulators + producers + consumers) | 40–55 | AI trust, sustainability supply chain, healthcare |

These are *targets, not caps*. But past evals have shown a consistent pattern: when maps drift above ~55 components, the extras rarely add strategic information and often over-decompose commodity infrastructure (listing CDN, DB, object storage, monitoring, load balancer separately when one "Cloud utilities" node would suffice).

**Rule of thumb for "should I add this component?"** — if removing it wouldn't change any conclusion in the strategic analysis (sections 4a–4f), leave it out. A 40-component map with every component doing strategic work is more useful than a 60-component map with 20 components that are there for completeness.

**Common over-additions to avoid:**
- Infrastructure that applies uniformly across the map — include one representative (e.g., "Cloud utilities") rather than five separate nodes (Compute, DB, CDN, Storage, Monitoring).
- Adjacent systems the user mentioned but the strategic question doesn't hinge on.
- Abstract qualities (reliability, performance, trust-ness) that aren't separately scoreable on the cheat sheet — fold into the components they qualify.
- Every subtype of a practice. "Agile" is one practice node; don't add Scrum, Kanban, XP as separate nodes unless they make different strategic calls.

**Signs you're under-decomposed** (rare but real):
- A component spans two different evolution stages (split it).
- Two user types depend on the same node for very different reasons (split it).
- The node carries both public-facing behaviour and deep-infra behaviour (split it — visibility constraint will force you to anyway).

### Step 2 — Dependencies

For each component, list `(a, b)` edges meaning "a depends on b". The dependency graph is typically a DAG but this is NOT a hard constraint. The only hard rule is the visibility constraint in Step 3.

### Step 3 — Visibility ν (Y-axis)

Visibility is a **judgment about value chain position**, not a pure graph property. Seed from distance, then adjust:

    d(v) = min over u ∈ U of { shortest path length from u to v }
    ν(v) = exp(−0.6 · d(v))          (exponential decay, default)

Seed values at typical depths:

| d(v) | ν seed | Typical meaning |
|---:|---:|---|
| 0 | 1.00 | The anchor itself |
| 1 | 0.55 | Directly user-facing component |
| 2 | 0.30 | Mid-chain supporting component |
| 3 | 0.17 | Deep supporting layer |
| 4 | 0.09 | Infrastructure / utility layer |
| 5 | 0.05 | Foundational commodity |
| 6 | 0.03 | Atomic utilities (power, water, DNS) |

**Do not be afraid to place deep infrastructure below ν = 0.1.** Wardley's own maps routinely have components at ν = 0.04 — 0.10 for deep commodity foundations. Our past maps systematically placed infrastructure too high; the exponential default counteracts that.

Then override where judgment disagrees:
- Raise ν for a component the user thinks about directly even if deep in the graph (e.g., a branded payment widget).
- Lower ν for a component that's technically close but architecturally invisible (e.g., a CDN).

Alternative seeds (use when the default doesn't fit):
- **Reciprocal decay** `ν(v) = 1 / (1 + d(v))` — gentler; caps deep components at ~0.2. Use for shallow maps where you don't want deep values.
- **Constraint optimisation** — solve for a full layout that respects every edge constraint, useful when distances violate the hard rule due to shortcuts.

**Hard rule:** for every edge `(a, b) ∈ E`, require `ν(a) ≥ ν(b)`. Enforced by the validator in Step 5.5.

### Step 4 — Evolution ε (X-axis)

**IMPORTANT:** Evolution is NOT maturity and NOT time-based. Wardley's climatic pattern states *"you cannot measure evolution over time or adoption."*

**4a. Concrete indicator checklists (fast path).** Read the "Stage indicators — concrete checklists" section of `references/evolution-stages.md`. For each component, check the four indicators (ubiquity / certainty / market / failure-mode) against the four stages. If all four dimensions point to the same stage, record that stage pick and use its band midpoint — skip the 4-row cheat sheet for this component.

**4b. 4-row cheat sheet (fallback when checklists disagree).** When the indicator checklists pick different stages for a component, run the 4-row cheat-sheet subset (full 19-row table in `cheat-sheet.md`):

| Row | Stage I (Genesis) | Stage II (Custom Built) | Stage III (Product +rental) | Stage IV (Commodity +utility) |
|---|---|---|---|---|
| Ubiquity (in market) | Rare | Slowly increasing | Rapidly increasing | Widespread, stabilising |
| Certainty | Poorly understood | Rapid learning | Rapid use / fit for purpose | Commonly understood |
| User Perception | Different / exciting | Leading edge | Common / expected | Standard |
| Publication Types | Describe the wonder | Build / construct / awareness | Maintenance / operations / features | Focused on use |

Map stage picks to band midpoints:
- I → 0.125, II → 0.375, III → 0.625, IV → 0.875

`ε(v) = mean of the four row picks`.

Flag components where rows disagree strongly as "in transition" and report the range.

**Record evidence as you score.** For each component, capture a one-line evidence citation — the observable signal that justifies the stage (vendor count, publication style, standards activity, recent regulation, market shakeout, etc.). Example: `AI Diagnostic Assistant — Stage II → "several startups (Aidoc, Viz.ai), FDA clearances trickling, no dominant vendor, clinician-led pilots dominate the literature"`. This becomes the rationale column in the output table (§3.2) and is the difference between a defensible map and an opinion.

### Step 4.5 — Deep placement (selective research)

After the initial cheat-sheet pass, **do not research every component** — that is expensive and unnecessary for obvious commodities (CDN, cloud compute, SMTP) or obvious Genesis bets the user has told you about. Instead, identify components that warrant a closer look, then do 1–2 targeted searches per flagged component.

**A component should be flagged for deep placement when any of:**

1. **Cheat-sheet rows disagree.** If `Var(ε) > 0.03` across the 4 (or 19) rows you scored, the rows are pointing at different stages — usually a sign of in-transition or of the mapper's priors being shaky.
2. **Strategically critical.** Top 3 by D (differentiation pressure), top 3 by K (commodity leverage), top 3 by R (dependency risk), or any component with an `evolve` target. Your whole strategy hinges on these placements being right.
3. **Specialised or recent domain.** Components in regulated industries (health, finance, defence), in markets that formed in the last 2-3 years, or in geographies the model's priors may not cover well.
4. **User disputes the placement.** If the user's scenario hints at a different stage than the cheat sheet suggests, research before overriding.

**For each flagged component, run 1-2 targeted searches:**

- **Vendor count & concentration:** `[component] vendor landscape [year]`, `[component] market share`. A handful of vendors → Stage II–III; many vendors with a few dominant → Stage III; few commodity utilities dominating → Stage IV.
- **Publication type:** `[component] research papers recent`, `[component] implementation case studies`. Papers describing the wonder → Stage I. How-to guides and comparisons → Stage III. Operations/ops maintenance guides → Stage IV.
- **Regulatory status:** `[component] regulation [jurisdiction]`. Emerging regulation is a Stage III → IV signal (industrialisation forces standards).
- **Open source activity:** `[component] open source`, `[component] CNCF` (or similar foundations). Active open-source standardisation accelerates Stage III → IV transitions.

**Apply findings:**

- If evidence confirms the cheat-sheet placement: note "deep placement confirms Stage X for [component]" — move on.
- If evidence contradicts: update `ε(v)`. In your strategic analysis, explicitly note what you found and how it shifted the placement (e.g., "initial cheat-sheet score put this at 0.55; vendor-landscape search showed 40+ active vendors and recent CNCF incubation, moving it to 0.72").
- If evidence is sparse or conflicting: widen the uncertainty range on that component. Plot as a range, not a point.

**Budget:** 3-5 deep placements per map is typical. Don't research every single component — that's both expensive and noise. The map's credibility depends on the key placements being defensible; obvious commodities can stay obvious.

### Step 5 — Stage bands

- Genesis: [0, 0.25)
- Custom Built: [0.25, 0.5)
- Product (+rental): [0.5, 0.75)
- Commodity (+utility): [0.75, 1.0]

Stage III covers products AND rental/licensing; Stage IV covers commodities AND utility services.

**Always use the parenthesised forms in prose** — write "Product (+rental)" and "Commodity (+utility)", not the bare "Product" / "Commodity". This matters because the suffixes carry meaning: Stage III isn't just "products", it's products *and* the rental/licensing business models that share its characteristics; likewise Stage IV is commodities *and* utility services. Using the bare names in your strategic analysis loses that distinction.

### Step 5.5 — Verification (before writing the OWM block)

After deep placement has moved coordinates around, **re-check two things before you emit the OWM output**. Skipping this is the most common source of quality regressions.

**1. Visibility constraint — run the validator, don't walk it mentally.**

Mental edge-walking fails on maps with more than ~20 edges. Past evals show that even with explicit instruction, subagents ship maps with silent violations. So we validate mechanically.

**Procedure (required):**

1. Write your draft OWM block to a workspace-local file (not `/tmp/` — some sandboxes deny writes there). A good pattern is to co-locate it with the final output, e.g., `./draft.owm` or alongside wherever you'll save the map.

2. Run the bundled validator against that file:
   ```bash
   node "${CLAUDE_SKILL_DIR}/scripts/validate_owm.mjs" ./draft.owm
   ```

   (The `CLAUDE_SKILL_DIR` variable resolves to this skill's root directory. If it isn't set, use the absolute path to the skill's `scripts/validate_owm.mjs`. Node.js is guaranteed available in every Claude Code install.)

3. If the validator exits 0, you're done — include the "OK: N components, M edges — no violations" line in your output section g.

4. If it reports violations, fix them (either raise source `ν` or lower target `ν` per the validator's suggestion). **Rerun the validator after every fix** — adjustments cascade and can break neighbouring edges.

5. Keep iterating validator → fix → validator until it exits 0. Only then ship the OWM block.

**Do not submit a map that hasn't been validated.** The validator is fast (< 1 second); running it is not optional. Claiming "I audited all edges" without having run the script has, in past evals, left real violations in the output.

**What the validator checks:**
- Every component/anchor has coordinates in `[0, 1]`.
- Every edge endpoint exists as a declared component/anchor (catches typos).
- For every edge `a->b`, `ν(a) ≥ ν(b)` (the hard rule).

**2. Canonical stage naming in prose.** When you write strategic analysis text and the words "Product" or "Commodity" appear, they should be "Product (+rental)" and "Commodity (+utility)". Scan your analysis before submitting. The bare forms lose the meaning of the stages (Stage III isn't only products — it's products and the rental/licensing business models that share its characteristics; Stage IV covers commodities and utility services).

If in doubt, search-and-replace: bare "Commodity" → "Commodity (+utility)", bare "Product" (when referring to the stage) → "Product (+rental)". Don't rewrite cases where "Product" means the user's actual product, only stage references.

### Step 5.6 — Layout check (advisory)

The validator catches structural errors; it doesn't catch visual-render problems that occur when coordinates are valid but sub-optimal. Run the layout checker against the same draft:

```bash
node "${CLAUDE_SKILL_DIR}/scripts/check_layout.mjs" ./draft.owm
```

It flags four classes of issue, each with a concrete fix:

1. **Near-duplicate coordinates** (`|Δν| < 0.02 AND |Δε| < 0.02`). Two nodes at effectively the same position render on top of each other. Past skill outputs have produced 7+ pairs of components at literally identical coordinates (from cheat-sheet midpoints agreeing). **Fix these**: nudge one of the pair by 0.03 in the direction of its actual semantic position (a component that's slightly more industrialised shifts +0.03 in ε; slightly higher-visibility shifts +0.03 in ν).
2. **Stage-boundary straddling** (component within ±0.01 of ε ∈ {0.25, 0.50, 0.75}). Looks accidentally "in both stages" on render. Advisory — fix by nudging ε±0.03 into whichever stage the cheat sheet actually picks. If truly between stages, leave it and say so in the analysis.
3. **Canvas-edge clipping** (anchor at ν > 0.98 or < 0.02; node at ε > 0.99 or < 0.01). The label gets cut by the rendered border. Pull back to ν = 0.96 / 0.04 and ε = 0.97 / 0.03 respectively.
4. **Stage imbalance** (>60% of components in one stage, or any stage empty). Often signals a part of the landscape is under-mapped. Re-check that stage's scope; extend or defend as appropriate.

The layout checker is advisory by default (exits 0 even with warnings). If your pipeline wants to hard-fail on warnings, pass `--strict`. After any coordinate nudge, **re-run `validate_owm.mjs`** — moving a node can break the visibility hard rule on its edges. Iterate validator → layout-check → fix until both are clean.

Near-duplicates are the highest-value catch; past benchmark subagents have shipped maps with 5-7 collision pairs that the validator passes silently. Fixing them is the difference between a readable map and a pile of overlapping labels.

### Step 6 — Derived heuristics (label as such)

The three metrics below are **heuristics proposed by this skill's math model, not canonical Wardley concepts**. Treat as attention prompts only.

- Differentiation pressure: `D(v) = ν(v) · (1 − ε(v))` — high = visible + immature = possible advantage.
- Commodity leverage: `K(v) = (1 − ν(v)) · ε(v)` — high = deep + mature = candidate for outsourcing / utility.
- Dependency risk: `R(a, b) = ν(a) · (1 − ε(b))` — high = visible depending on fragile foundation.

---

## 3. Output format (OWM)

Produce the map in OWM text syntax. Coordinates are `[visibility, evolution]` with both values in `[0, 1]`.

```
title Map Title
style wardley

// Anchor(s)
anchor User Need Name [ν, ε]

// Components
component Name [ν, ε]

// Dependencies (component → what it depends on)
Component A->Component B

// Optional
evolve Component Name target_ε
note Note text [ν, ε]
component Legacy [ν, ε] inertia
pipeline Platform [start_ε, end_ε]
```

Include multiple `anchor` lines if the scenario has more than one user type.

### 3.2 Required — Component evolution rationale table

After the OWM block, emit a table with one row per component (anchors excluded). This is the evidence record behind every placement — readers (and future reviewers) check it to see whether the map is defensible or guessed.

| Component | Stage | ε | ν | Evidence |
|---|---|---|---|---|
| *e.g. AI Diagnostic Assistant* | Custom Built | 0.38 | 0.44 | *Several startups (Aidoc, Viz.ai); FDA clearances trickling; clinician-led pilots dominate literature.* |
| *e.g. Cloud Compute* | Commodity (+utility) | 0.90 | 0.08 | *AWS, GCP, Azure — priced per-second, published standards, utility billing.* |

Evidence cells should be **one sentence**, concrete, and preferably cite named vendors, standards, or events. Generic ("widely used, mature") is weak evidence; specific ("SOC 2 Type II required for enterprise deals since 2021") is strong. This table is where the skill's 16 iterations of placement discipline pay off; without it, placements look authoritative but aren't reviewable.

### 3.1 Optional — Mermaid wardley-beta block (for GitHub rendering)

OWM is the authoritative output (pastes into [onlinewardleymaps.com](https://onlinewardleymaps.com/) and runs through the validator). For documents that will be viewed on GitHub, optionally also emit a [Mermaid `wardley-beta`](https://mermaid.js.org/) block so the map renders inline. Convert the OWM draft with the bundled script:

```bash
node "${CLAUDE_SKILL_DIR}/scripts/owm_to_mermaid.mjs" ./draft.owm
```

Include the Mermaid block *after* the OWM block in your final output, wrapped in a ```` ```mermaid ```` fence. Both blocks describe the same map — the OWM is canonical, the Mermaid is a rendering target.

The converter always double-quotes component/anchor/edge names because Mermaid's `wardley-beta` grammar forbids hyphens and several reserved-keyword prefixes in bare names (e.g. a component called "labelling" collides with the `label` keyword). Quoting uses the STRING alternative of the grammar and accepts any text verbatim.

If the Mermaid render surfaces a parse error, it's almost always one of: a stray unquoted name in text you added manually (quote it), a `/` in a name that the converter should have replaced with ` and ` (rerun the converter), or a pipeline declaration that doesn't map cleanly to Mermaid's block form (drop the pipeline and emit its children as regular components).

---

## 4. Strategic analysis

After the OWM output, produce the sections below. **Write in qualitative terms first, numbers second.** Wardley's framework is about stages and rank, not decimals — `ε = 0.625` is not meaningfully different from `0.63` or `0.61` to a strategist. When you refer to a component in prose, lead with its **stage** ("Genesis / Custom Built / Product (+rental) / Commodity (+utility)") and only add the numeric `ε` in parentheses if it clarifies (e.g., "edge of Product/Commodity boundary"). For D, K, R, give a **rank order** with reasoning; don't lead with raw products of two-decimal numbers.

**a. Differentiation opportunities (top 3).** List in rank order, leading with the component and a one-sentence "why". Stage label first, numeric D second or omitted. Example: "**Matching Algorithm** (Custom Built → Product) — the platform's core IP, actively industrialising. Highest differentiation leverage." Not: "Matching Algorithm (0.62 × 0.65 = 0.40)".

**b. Commodity-leverage candidates (top 3).** Same pattern. "**Cloud compute** (Commodity +utility) — rent, don't build."

**c. Dependency risks (top 3).** Edge `(a, b)` where a visible component depends on an immature foundation. Describe the risk qualitatively. "**Checkout → Fraud detection** — visible checkout experience depends on in-house ML that is still Custom Built."

**d. Build / Buy / Outsource recommendations.** For each component where the strategic question hinges on sourcing, give a one-line call and a reason grounded in its stage:

| Component | Stage | Recommendation | Why |
|---|---|---|---|
| *e.g. Matching Algorithm* | Custom Built | **Build** | Core IP, differentiation-zone, no competitive product market yet. |
| *e.g. Payment rails* | Commodity | **Rent** (Stripe / Adyen) | Utility market; building is strict-worse than renting. |
| *e.g. Fraud detection* | Product, transitioning | **Buy** (Sift / Stripe Radar) | Competitive vendor market; in-house ML has no moat. |
| *e.g. Auth protocols* | Product (standardising) | **Open-source collaborate** | OIDC / SAML / WebAuthn — join the standard rather than reinvent. |

Rules of thumb: Genesis → **build** (nobody else has it yet). Custom Built → **build** only if it's a differentiator; otherwise **buy external expertise**. Product → **buy**. Commodity → **rent / consume as utility**. Stage II → III boundaries where ecosystem dynamics apply → **open-source collaborate**. Only include components where the sourcing decision is actually open; skip the obvious ones.

**e. Suggested gameplays** — name each play from Wardley's 61-play catalogue (full list in `references/gameplay-patterns.md`) and which component(s) it targets. Prefer named Wardley plays over generic advice. Cite by number and name (e.g., "#15 Open Approaches on Component X").

**f. Doctrine violations** — if any of Wardley's 40 doctrine principles are clearly violated (missing anchor, unclear user, underspecified Knowledge layer), flag them. Full list in `references/doctrine.md`.

**g. Climatic context** — which of the 27 climatic patterns (see `references/climatic-patterns.md`) are actively shaping this map? Common: #3 Everything evolves, #15–17 Inertia, #27 Product-to-utility punctuated equilibrium.

**h. Deep-placement notes** — for any component where you ran targeted research (see step 4.5), note what you found and how it shifted the placement. Example: "Fraud Detection — initial cheat-sheet 0.35 (Custom). Vendor search found mature providers (Sift, Stripe Radar) and standardising APIs — shifted to 0.55 (early Product)." List the 2-4 components you did deep placement on. If you did none, say so.

**i. Caveat** — remind the user that evolution trajectories are scenarios, not forecasts. Wardley's climatic pattern #18: *"you cannot measure evolution over time or adoption."*

---

## 5. Dynamics (optional, only if asked)

If the user explicitly asks for simulated evolution over time, use the logistic form:

    dε/dt = r · ε · (1 − ε)

where `r = r₀ + u(t) − c(t)`:
- `r₀`: baseline market pressure
- `u(t)`: strategic actions (named Wardley gameplays)
- `c(t)`: inertia (17 forms enumerated in `references/inertia.md`)

Clamp `r` to be non-negative — evolution is monotonic-forward.

For multi-generation components (e.g., compute: mainframe → PC → cloud), use the multi-wave form from `references/mathematical-models.md` §4 instead of a single S-curve.

Always label output as "scenario, not forecast."

---

## Supporting files in this skill

All reference material lives in `references/`:

- `references/evolution-stages.md` — the four stages, the 19-row cheat sheet, scoring procedure, and worked examples.
- `references/climatic-patterns.md` — the 27 patterns across 6 categories. Consult when reasoning about how the environment shapes a map.
- `references/doctrine.md` — the 40 doctrine principles across 4 phases. Consult when checking for doctrine violations in the map.
- `references/gameplay-patterns.md` — the 61 gameplays with mechanisms and common sequences. Consult when recommending strategic moves.
- `references/inertia.md` — the 17 forms of resistance to evolution.
- `references/mathematical-models.md` — the tuple, dynamics (logistic + multi-wave), derived heuristics, gameplay transformations, doctrine-as-constraints. Consult when precise formulation is needed.
- `references/mapping-examples.md` — three worked Wardley Maps (tea shop, freelance marketplace, SaaS invoicing) showing the full output format the skill should produce.

The top-level `README.md` is for humans installing the skill; ignore it when executing.

The skill is a self-contained package; use `${CLAUDE_SKILL_DIR}/references/<file>.md` to reference files from shell commands. From markdown links, relative paths like `[cheat sheet](references/evolution-stages.md)` work.

### When to read which reference

- **Always skim** `references/mapping-examples.md` first when generating a new map — it anchors the output format.
- **Read when scoring evolution:** `references/evolution-stages.md` (for the cheat sheet).
- **Read when recommending moves:** `references/gameplay-patterns.md` (for play names and mechanisms).
- **Read when flagging doctrine issues:** `references/doctrine.md` (for phase assignments and descriptions).
- **Read when explaining "why" this evolution/inertia matters:** `references/climatic-patterns.md`.
- **Read when asked for dynamics or math:** `references/mathematical-models.md`.
- **Read when inertia comes up:** `references/inertia.md` (for the specific 17 forms).
