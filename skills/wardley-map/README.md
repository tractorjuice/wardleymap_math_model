# wardley-map — Claude Code Skill

A portable Claude Code skill that generates Wardley Maps from a scenario description using a formal mathematical model. The primary output is OWM-format text (compatible with [create.wardleymaps.ai](https://create.wardleymaps.ai) and [onlinewardleymaps.com](https://onlinewardleymaps.com)) plus a strategic analysis grounded in Wardley's cheat sheet, 61 gameplays, and 40 doctrine principles. The skill can also emit a Mermaid `wardley-beta` block for GitHub-native rendering.

## Install

**For one project only:**

```bash
mkdir -p .claude/skills
cp -r path/to/wardley-map .claude/skills/
```

**For all your projects:**

```bash
mkdir -p ~/.claude/skills
cp -r path/to/wardley-map ~/.claude/skills/
```

Either path makes the skill discoverable by Claude Code. No restart needed.

## Use

In a Claude Code session:

```
/wardley-map a small e-commerce platform selling handmade crafts
```

Claude will produce:

1. An OWM-format map with anchor(s), components, visibility/evolution coordinates, and dependencies.
2. A strategic analysis: top differentiation opportunities, commodity candidates, dependency risks, suggested Wardley gameplays (named from the 61-play catalogue), and doctrine violations if any.

If you invoke `/wardley-map` with no arguments, Claude will ask for a scenario description first.

Ask for "render this on GitHub" or "emit a Mermaid block" and Claude will also run the OWM output through `scripts/owm_to_mermaid.mjs` and include a `wardley-beta` fenced block beside the OWM — see SKILL.md §3.1.

## What's in this skill

- `SKILL.md` — the skill body (procedure + OWM output format + when to consult each reference).
- `evals/evals.json` — test cases with assertions used to validate the skill.
- `scripts/validate_owm.mjs` — deterministic OWM validator. Checks coordinate ranges, edge endpoint existence, and the `ν(a) ≥ ν(b)` visibility constraint. Called by Step 5.5 before submitting any map.
- `scripts/check_layout.mjs` — advisory layout checker (Step 5.6). Catches near-duplicate coordinates that render on top of each other, components landing on stage boundaries, canvas-edge clipping, and stage-distribution imbalance. Exits 0 by default; pass `--strict` to hard-fail on warnings.
- `scripts/owm_to_mermaid.mjs` — optional post-step converter that emits a Mermaid `wardley-beta` block from a validated OWM draft. See SKILL.md §3.1. Always double-quotes names to sidestep Mermaid's bare-name restrictions (no hyphens, no reserved-keyword prefixes).
- `references/` — bundled reference material the skill loads on demand:
  - `climatic-patterns.md` — 27 patterns across 6 categories.
  - `doctrine.md` — 40 principles across 4 phases.
  - `evolution-stages.md` — 19-row cheat sheet, scoring procedure, worked examples.
  - `gameplay-patterns.md` — 61 gameplays with mechanisms and common sequences.
  - `inertia.md` — 17 structured forms of inertia.
  - `mapping-examples.md` — three complete worked maps (tea shop, freelance marketplace, SaaS invoicing).
  - `mathematical-models.md` — the tuple, dynamics, heuristics, type function.

The skill is self-contained; you don't need the parent repository to use it.

## What the skill implements

| Aspect | Implementation |
|---|---|
| Tuple | `M = (V, E, U, ν, ε, t)` — anchor *set* `U ⊆ V`, optional time |
| Visibility | Judgment primitive seeded by `1/(1+d(v))`; hard rule `ν(a) ≥ ν(b)` for edges |
| Evolution | Cheat-sheet scoring (4-row quick; 19-row full in `cheat-sheet.md`) |
| Stages | Genesis / Custom Built / Product (+rental) / Commodity (+utility) |
| Dynamics | Logistic S-curve `dε/dt = rε(1-ε)` — labeled as scenario, not forecast |
| Strategic moves | Named from the 61-play catalogue in `gameplays.md` |
| Doctrine check | Flags violations against the 40 principles in `doctrine.md` |
| Inertia | 17 structured forms in `inertia.md` |

## Caveats

1. **Not a forecast tool.** Wardley's climatic pattern is *"you cannot measure evolution over time or adoption."* Evolution trajectories from this skill are scenarios for exploration, not predictions.
2. **D, K, R metrics are heuristics.** Differentiation pressure, commodity leverage, and dependency risk are proposed by this skill's math model, not canonical Wardley concepts.
3. **Mapper judgment wins.** Graph-distance visibility and cheat-sheet scoring produce *seeds*. A human mapper's judgment about value-chain position may override them.
4. **Market-relative ubiquity.** Score "ubiquity" against a named market; there's no universal scale.

## Origin

This skill is derived from [wardleymap_math_model](https://github.com/tractorjuice/wardleymap_math_model), a documentation-only repository that formalises Wardley Mapping as a mathematical model. The skill is a self-contained distillation of the operational parts of that repo.

Wardley Mapping itself is Simon Wardley's framework — see his [Medium book](https://medium.com/wardleymaps) and [blog](https://blog.gardeviance.org/) for primary sources. Wardley has not endorsed quantitative formalisations of his framework; treat this skill as an aid for disciplined mapping, not a substitute for Wardley's thinking.

## Licence

Inherits the parent repository's terms. Uses Wardley's cheat sheet, doctrine, and gameplays — which are CC-BY-SA — with attribution.
