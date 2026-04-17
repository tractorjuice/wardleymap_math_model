# Wardley Map Generator Prompt

Use this prompt to generate a Wardley Map grounded in this repo's formal math model. Output is in OWM (Online Wardley Maps) format, compatible with [create.wardleymaps.ai](https://create.wardleymaps.ai/) and [onlinewardleymaps.com](https://onlinewardleymaps.com/).

The prompt reflects the canonical model as of the current repo state — see Part 1 for the core definitions, Part 6 for cheat-sheet scoring, and the Inertia / Gameplay Catalogue / Doctrine docs for extensions.

---

## Prompt

```
You are a Wardley Mapping assistant using a formal mathematical model. Given a description of a system, business, or domain, generate a Wardley Map following the procedure below.

## 1. Mathematical Model

A Wardley Map is a tuple:

    M = (V, E, U, ν, ε, t)

Where:
- V = set of components
- E ⊆ V × V = directed dependency edges. (a, b) ∈ E means "a depends on b".
- U ⊆ V = anchor set — one or more user-need nodes. Real maps often have multiple user types (e.g., "Business" and "Public").
- ν: V → [0, 1] = visibility function (Y-axis). Higher = closer to the user.
- ε: V → [0, 1] = evolution function (X-axis). Higher = more commoditised.
- t = time (optional, only needed for dynamics)

Optional extension — component types τ: V \ U → {A, P, D, K}:
- A = Activity (what the organisation does)
- P = Practice (how it does it)
- D = Data (information it uses)
- K = Knowledge (concepts, theories it relies on)

Use τ when the map benefits from distinguishing types (e.g., showing that practices co-evolve with activities).

## 2. Components V and Anchors U

List components as concrete nouns. Start with the anchor set U (user needs), then Activities, Practices, Data, Knowledge the user needs to have satisfied.

## 3. Dependencies E

For each component, list what it depends on: (A, B) means "A depends on B".

Note: the dependency graph is typically a DAG in practice but this is NOT a hard constraint. The only hard rule is the visibility constraint in §4.

## 4. Visibility ν (Y-axis)

Visibility is a JUDGMENT about value chain position — not a pure graph property. Seed it from distance, then adjust.

Seed via shortest distance from the anchor set:

    d(v) = min over u ∈ U of { path length from u to v }
    ν(v) = 1 / (1 + d(v))

Then override where the seed disagrees with value-chain judgment:
- Raise ν for a component the user thinks about directly (e.g., a branded payment widget) even if it's deep in the graph.
- Lower ν for a component that's technically close but architecturally invisible (e.g., a CDN).

The one HARD rule: for every edge (a, b) ∈ E, require ν(a) ≥ ν(b). Components must sit above their dependencies. If your initial ν assignments violate this, adjust.

## 5. Evolution ε (X-axis)

IMPORTANT: evolution is NOT maturity and NOT time-based. Wardley's own climatic pattern states "you cannot measure evolution over time or adoption."

Score each component against a subset of Wardley's 19-row cheat sheet (quick 4-row method):

For each component, pick the stage (I–IV) that best describes it in each of these four rows:

| Row | Stage I (Genesis) | Stage II (Custom Built) | Stage III (Product +rental) | Stage IV (Commodity +utility) |
|---|---|---|---|---|
| Ubiquity (in market) | Rare | Slowly increasing | Rapidly increasing | Widespread, stabilising |
| Certainty | Poorly understood | Rapid learning | Rapid use / fit for purpose | Commonly understood |
| User Perception | Different / exciting / surprising | Leading edge | Common / expected | Standard |
| Publication Types | Describe the wonder | Build / construct / awareness | Maintenance / operations / features | Focused on use |

Map each stage to its band midpoint:
- Stage I → 0.125
- Stage II → 0.375
- Stage III → 0.625
- Stage IV → 0.875

Average the four scores to get ε(v). If the rows disagree strongly, flag the component as "in transition" and report the range.

For a more thorough placement, score against all 19 cheat-sheet rows — see Part 6 of this repo.

## 6. Stage Bands

- Genesis: [0, 0.25)
- Custom Built: [0.25, 0.5)
- Product (+rental): [0.5, 0.75)
- Commodity (+utility): [0.75, 1.0]

Canonical names include the parenthesized suffixes. Stage III covers products AND rental/licensing; Stage IV covers commodities AND utility services.

## 7. Derived Heuristics (optional)

The three metrics below are HEURISTICS PROPOSED BY THIS REPOSITORY, not canonical Wardley concepts. Treat them as attention prompts, not validated strategic criteria.

- Differentiation pressure: D(v) = ν(v) · (1 − ε(v))
  High D = visible + immature = possible advantage zone.
- Commodity leverage: K(v) = (1 − ν(v)) · ε(v)
  High K = deep + mature = candidate for outsourcing / utility.
- Dependency risk: R(a, b) = ν(a) · (1 − ε(b))
  High R = visible component depending on fragile foundation.

## 8. Output Format (OWM)

Produce the map in OWM text syntax. Coordinates are [visibility, evolution] with both values in [0, 1].

    title Map Title
    style wardley

    // Anchor(s)
    anchor User Need Name [ν, ε]

    // Components
    component Name [ν, ε]

    // Dependencies (component → what it depends on)
    Component A->Component B

    // Optional: evolution movements
    evolve Component Name [target ε]

    // Optional: strategic notes
    note Note text [ν, ε]

    // Optional: inertia marker
    component Legacy [ν, ε] inertia

    // Optional: pipeline
    pipeline Platform [start_ε, end_ε]

Include multiple anchors if the scenario has more than one user type. Use the `inertia` marker only when a specific component is resisting evolution — ideally reference which of the 17 forms (see the Inertia doc) applies.

## 9. Strategic Analysis

After the OWM output, provide:

a. Top 3 components by D (differentiation pressure) — with brief reasoning.
b. Top 3 by K (commodity leverage) — with brief reasoning.
c. Top 3 dependency risks by R — edge (a, b) and why.
d. Suggested gameplays from Wardley's 61-play catalogue (see the Gameplay Catalogue doc for the full list). Name each play and which component(s) it targets. Prefer named Wardley plays over generic recommendations.
e. Relevant doctrine violations (see the Doctrine doc for the 40 principles) if any jump out — e.g., missing anchor, unclear user, underspecified Knowledge layer.

Do NOT forecast evolution trajectories as predictions. If you simulate dynamics, use the logistic form

    dε/dt = r · ε · (1 − ε)

and explicitly label the result as a scenario, not a forecast. Wardley's climatic pattern is that evolution cannot be measured over time.

## 10. Now generate the map

Scenario:

[INSERT YOUR SCENARIO HERE]
```

---

## Example Output

Scenario: *A small e-commerce platform selling handmade crafts, serving both end customers and the artisans who list products.*

```owm
title Handmade Crafts E-Commerce
style wardley

// Two anchors — this is a two-sided marketplace
anchor Customer Purchase [0.98, 0.60]
anchor Artisan Listing [0.95, 0.45]

// Layer 1 — directly user-facing
component Online Storefront [0.82, 0.65]
component Artisan Portal [0.80, 0.40]

// Layer 2 — supporting activities
component Product Discovery [0.70, 0.45]
component Shopping Cart [0.68, 0.75]
component Product Catalog [0.55, 0.55]
component Payment Processing [0.50, 0.85]
component Order Management [0.48, 0.60]

// Layer 3 — operational components
component Shipping Integration [0.38, 0.75]
component Inventory System [0.35, 0.50]
component Customer Support [0.32, 0.45]
component Fraud Detection [0.30, 0.40]

// Layer 4 — infrastructure
component Cloud Compute [0.18, 0.90]
component Database [0.15, 0.88]
component CDN [0.10, 0.92]

// Dependencies
Customer Purchase->Online Storefront
Artisan Listing->Artisan Portal
Online Storefront->Product Discovery
Online Storefront->Shopping Cart
Online Storefront->Product Catalog
Artisan Portal->Product Catalog
Artisan Portal->Inventory System
Product Discovery->Product Catalog
Shopping Cart->Payment Processing
Shopping Cart->Order Management
Shopping Cart->Fraud Detection
Order Management->Shipping Integration
Order Management->Inventory System
Customer Support->Order Management
Online Storefront->Cloud Compute
Product Catalog->Database
Online Storefront->CDN

// Evolution projections (scenario, not forecast)
evolve Fraud Detection 0.65
evolve Product Discovery 0.60

// Notes
note High differentiation zone [0.65, 0.30]
note Outsource candidates [0.20, 0.88]
```

Strategic analysis:

- **Top D (differentiation):** Fraud Detection (0.30 × 0.60 = 0.18), Artisan Portal (0.80 × 0.60 = 0.48 — but already anchored-adjacent), Product Discovery (0.70 × 0.55 = 0.39). Product Discovery is the strongest true differentiation play.
- **Top K (commodity leverage):** CDN (0.90 × 0.92 ≈ 0.83), Cloud Compute (0.82 × 0.90 ≈ 0.74), Database (0.85 × 0.88 ≈ 0.75). All three should be treated as utilities.
- **Top R (dependency risk):** (Shopping Cart, Fraud Detection) = 0.68 × 0.60 = 0.41 — visible checkout depending on immature fraud logic.
- **Suggested gameplays:** *Open Approaches* (#15) on Product Discovery to accelerate it toward Product stage; *Harvesting* (#29) on ML vendors in the fraud space; *Directed investment* (#36) on Artisan Portal as a differentiator.
- **Doctrine note:** This map has two anchors (Customer, Artisan) — good Phase II doctrine ("Know your users"). Watch that the Artisan Portal doesn't drift into Phase I "Focus on user needs" confusion if roadmap prioritisation forgets the artisan side.

---

## Customisation Options

**For multi-wave evolution scenarios:**
```
Model evolution across multiple generations (per the Multi-Wave Evolution doc):
- For each key component, identify its past, current, and emerging generations.
- Use piecewise logistic curves per generation.
- Flag chasms (periods where old gen is saturated and new gen hasn't taken off).
```

**For component typing:**
```
Annotate each component with its type τ ∈ {A, P, D, K}:
- Activities are typical map nodes.
- Practices should have at least one Activity that depends on them.
- Data and Knowledge usually sit lower in visibility.
Use onlinewardleymaps' component colouring to distinguish types.
```

**For inertia-aware dynamics:**
```
For components that are stuck, specify which of Wardley's 17 inertia forms apply
(see the Inertia doc). Common ones: sunk capital, human capital, political capital,
re-architecture cost, second-sourcing risk.
```

**For build/buy/outsource framing:**
```
For components with ε > 0.75, default to "buy" or "outsource".
For ε ∈ [0.5, 0.75], consider "buy" but evaluate differentiation potential.
For ε < 0.5, default to "build" — or partner with a specialist.
```

---

## OWM Format Reference

| Element | Syntax | Example |
|---------|--------|---------|
| Title | `title Name` | `title My Map` |
| Style | `style wardley` | `style wardley` |
| Anchor | `anchor Name [v, e]` | `anchor Customer Need [0.95, 0.5]` |
| Component | `component Name [v, e]` | `component API [0.45, 0.72]` |
| Dependency | `A->B` | `Website->API` |
| Evolution | `evolve Name target` | `evolve API 0.85` |
| Note | `note Text [v, e]` | `note Risk area [0.5, 0.3]` |
| Pipeline | `pipeline Name [s, e]` | `pipeline Platform [0.3, 0.8]` |
| Inertia marker | `component Name [v, e] inertia` | `component Legacy [0.4, 0.3] inertia` |
| Label offset | `component Name [v, e] label [-x, y]` | `component API [0.5, 0.7] label [-10, 5]` |

Coordinates: `[visibility, evolution]` — both 0–1.
- Visibility: 1.0 = top (anchor), 0.0 = bottom (deepest dependency).
- Evolution: 0.0 = Genesis (left), 1.0 = Commodity +utility (right).

---

## References to the Repo

- [Part 1](../Part%201%20-%20Core%20Mathematical%20Model%20for%20Wardley%20Mapping.md) — tuple, visibility options, dynamics ODE
- [Part 6](../Part%206%20-%20Cheat-Sheet%20Evolution%20Scoring.md) — full 19-row cheat sheet and formal scoring
- [Inertia](../Inertia%20-%20Forms%20of%20Resistance%20to%20Evolution.md) — 17 forms of resistance
- [Multi-Wave Evolution](../Multi-Wave%20Evolution%20and%20Punctuated%20Equilibrium.md) — multi-generation dynamics
- [Component Types](../Component%20Types%20and%20the%20Type%20Function.md) — τ extension
- [Gameplay Catalogue](../Gameplay%20Catalogue%20-%2061%20Plays%20with%20Math-Model%20Effects.md) — 61 plays
- [Doctrine](../Doctrine%20-%2040%20Principles%20as%20Model%20Constraints.md) — 40 universal principles
