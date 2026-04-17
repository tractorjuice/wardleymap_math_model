---
name: wardley-map
description: Generate a Wardley Map from a scenario description using a formal mathematical model. Produces OWM-format output and strategic analysis grounded in Wardley's cheat sheet, 61 gameplays, and 40 doctrine principles. Use when the user wants a Wardley Map of a system, business, or domain, or asks to "map" something strategically.
argument-hint: <scenario description>
allowed-tools: Read, Grep
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

### Step 5 — Stage bands

- Genesis: [0, 0.25)
- Custom Built: [0.25, 0.5)
- Product (+rental): [0.5, 0.75)
- Commodity (+utility): [0.75, 1.0]

Stage III covers products AND rental/licensing; Stage IV covers commodities AND utility services.

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

After the OWM output, produce:

**a. Top 3 by differentiation pressure D** — with brief reasoning.

**b. Top 3 by commodity leverage K** — with brief reasoning.

**c. Top 3 dependency risks R** — edge `(a, b)` and why.

**d. Suggested gameplays** — name each play from Wardley's 61-play catalogue (full list in `gameplays.md`) and which component(s) it targets. Prefer named Wardley plays over generic advice.

**e. Doctrine violations** — if any of Wardley's 40 doctrine principles are clearly violated (missing anchor, unclear user, underspecified Knowledge layer), flag them. Full list in `doctrine.md`.

**f. Caveat** — remind the user that evolution trajectories are scenarios, not forecasts. Wardley's climatic pattern: *"you cannot measure evolution over time or adoption."*

---

## 5. Dynamics (optional, only if asked)

If the user explicitly asks for simulated evolution over time, use the logistic form:

    dε/dt = r · ε · (1 − ε)

where `r = r₀ + u(t) − c(t)`:
- `r₀`: baseline market pressure
- `u(t)`: strategic actions (named Wardley gameplays)
- `c(t)`: inertia (17 forms enumerated in `inertia.md`)

Clamp `r` to be non-negative — evolution is monotonic-forward.

Always label output as "scenario, not forecast."

---

## Supporting files in this skill

- `cheat-sheet.md` — Wardley's full 19-row evolution characteristic table
- `gameplays.md` — all 61 gameplays by category
- `doctrine.md` — all 40 doctrine principles by phase
- `inertia.md` — the 17 forms of inertia
- `README.md` — install instructions for humans

The skill is a self-contained package; use `${CLAUDE_SKILL_DIR}` if you need to reference these files from shell commands. From markdown links, relative paths like `[cheat-sheet](cheat-sheet.md)` work.
