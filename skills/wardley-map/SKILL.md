---
name: wardley-map
description: Generate a Wardley Map from a scenario description using a formal mathematical model. Produces OWM-format output and strategic analysis grounded in Wardley's cheat sheet, 61 gameplays, and 40 doctrine principles. Use this skill whenever the user asks for strategic reasoning about the components of a business, product, or system — specifically when they mention any of value chain, strategic positioning, competitive landscape, strategic moat, component evolution, genesis-to-commodity spectrum, build-vs-buy across multiple components, where to invest engineering effort, what to commoditise or outsource, mapping a business or platform or marketplace strategically, or explicitly "Wardley map". Always trigger when "Wardley" appears in the request. Also trigger when the user describes a business or system and asks about strategic roadmap, moats, or board-level positioning — even without naming the framework. Skip for flowcharts, UX journey maps, process swimlanes, architecture diagrams, data pipeline diagrams, skills matrices, MECE breakdowns, Porter's five forces, marketing positioning statements, or definitional questions about what a Wardley map is.
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

### Step 1 — List components and anchors

- Anchor set `U`: the user need(s). If the scenario has multiple user types (e.g., customer AND artisan), use multiple anchors.
- Then list Activities, Practices, Data, Knowledge the users depend on.
- Use concrete nouns, not slogans.

### Step 2 — Dependencies

For each component, list `(a, b)` edges meaning "a depends on b". The dependency graph is typically a DAG but this is NOT a hard constraint. The only hard rule is the visibility constraint in Step 3.

### Step 3 — Visibility ν (Y-axis)

Visibility is a **judgment about value chain position**, not a pure graph property. Seed from distance, then adjust:

    d(v) = min over u ∈ U of { shortest path length from u to v }
    ν(v) = 1 / (1 + d(v))

Then override where judgment disagrees:
- Raise ν for a component the user thinks about directly even if deep in the graph.
- Lower ν for a component that's technically close but architecturally invisible.

**Hard rule:** for every edge `(a, b) ∈ E`, require `ν(a) ≥ ν(b)`.

### Step 4 — Evolution ε (X-axis)

**IMPORTANT:** Evolution is NOT maturity and NOT time-based. Wardley's climatic pattern states *"you cannot measure evolution over time or adoption."*

Use a 4-row cheat-sheet subset (full 19-row table in `cheat-sheet.md`):

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
   python3 "${CLAUDE_SKILL_DIR}/scripts/validate_owm.py" ./draft.owm
   ```

   (The `CLAUDE_SKILL_DIR` variable resolves to this skill's root directory. If it isn't set, use the absolute path to the skill's `scripts/validate_owm.py`.)

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

---

## 4. Strategic analysis

After the OWM output, produce the sections below. **Write in qualitative terms first, numbers second.** Wardley's framework is about stages and rank, not decimals — `ε = 0.625` is not meaningfully different from `0.63` or `0.61` to a strategist. When you refer to a component in prose, lead with its **stage** ("Genesis / Custom Built / Product (+rental) / Commodity (+utility)") and only add the numeric `ε` in parentheses if it clarifies (e.g., "edge of Product/Commodity boundary"). For D, K, R, give a **rank order** with reasoning; don't lead with raw products of two-decimal numbers.

**a. Differentiation opportunities (top 3).** List in rank order, leading with the component and a one-sentence "why". Stage label first, numeric D second or omitted. Example: "**Matching Algorithm** (Custom Built → Product) — the platform's core IP, actively industrialising. Highest differentiation leverage." Not: "Matching Algorithm (0.62 × 0.65 = 0.40)".

**b. Commodity-leverage candidates (top 3).** Same pattern. "**Cloud compute** (Commodity +utility) — rent, don't build."

**c. Dependency risks (top 3).** Edge `(a, b)` where a visible component depends on an immature foundation. Describe the risk qualitatively. "**Checkout → Fraud detection** — visible checkout experience depends on in-house ML that is still Custom Built."

**d. Suggested gameplays** — name each play from Wardley's 61-play catalogue (full list in `references/gameplay-patterns.md`) and which component(s) it targets. Prefer named Wardley plays over generic advice. Cite by number and name (e.g., "#15 Open Approaches on Component X").

**e. Doctrine violations** — if any of Wardley's 40 doctrine principles are clearly violated (missing anchor, unclear user, underspecified Knowledge layer), flag them. Full list in `references/doctrine.md`.

**f. Climatic context** — which of the 27 climatic patterns (see `references/climatic-patterns.md`) are actively shaping this map? Common: #3 Everything evolves, #15–17 Inertia, #27 Product-to-utility punctuated equilibrium.

**g. Deep-placement notes** — for any component where you ran targeted research (see step 4.5), note what you found and how it shifted the placement. Example: "Fraud Detection — initial cheat-sheet 0.35 (Custom). Vendor search found mature providers (Sift, Stripe Radar) and standardising APIs — shifted to 0.55 (early Product)." List the 2-4 components you did deep placement on. If you did none, say so.

**h. Caveat** — remind the user that evolution trajectories are scenarios, not forecasts. Wardley's climatic pattern #18: *"you cannot measure evolution over time or adoption."*

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
