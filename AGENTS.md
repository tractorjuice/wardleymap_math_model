# Repository Guidelines

## Project Structure & Module Organization

- `docs/` contains mathematical research: `core/`, `extensions/`, `catalogues/`, `strategy/`, map examples, and articles.
- `skills/wardley-map/` is the production skill, with `SKILL.md`, reference material, Node scripts, and evaluation scenarios.
- `skills/wardley-map-workspace/` holds benchmark scripts, reference maps, iteration outputs, reports, and chart assets.
- `prompts/` contains the standalone map-generation prompt; `scripts/` contains the shared converter; `tools/` contains the Mermaid tidy hook and its tests.
- `README.md` and `llms.txt` index the documentation; `CLAUDE.md` provides detailed workflow notes.

## Build, Test, and Development Commands

There is no build system or application server. Use Node.js for dependency-free ESM tools and Python 3 for benchmark scripts. Chart renderers require Matplotlib/NumPy; the model benchmark requires `anthropic`.

```bash
node --test tools/tidy-hook.test.mjs
node skills/wardley-map/scripts/validate_owm.mjs map.owm
node skills/wardley-map/scripts/check_layout.mjs --strict map.owm
node scripts/owm_to_mermaid.mjs map.owm > map.mermaid
```

These run hook tests, validate map structure, reject layout warnings, and convert OWM to Mermaid, respectively.

## Coding Style & Naming Conventions

Follow existing style: two-space indentation and single quotes in JavaScript; four-space indentation in Python. No repository-wide formatter or linter is configured. Use kebab-case Markdown filenames, relative document links, and GitHub LaTeX (`$...$`, `$$...$$`). Add new documents to `README.md` and `llms.txt`.

Keep both `owm_to_mermaid.mjs` copies synchronized. OWM coordinates are `[visibility, evolution]`, each within `[0,1]`; dependencies must satisfy `visibility(source) >= visibility(target)`. Distinguish canonical Wardley concepts from this repository's proposed heuristics.

## Testing Guidelines

Hook tests use `node:test` and strict assertions; follow the `*.test.mjs` naming pattern with descriptive test names. No numeric coverage threshold is configured. Revalidate maps after layout changes and inspect rendered diagrams. Check placement changes against the 25-map benchmark, following `BENCHMARK-METHODOLOGY.md`; map generation must remain blind to reference maps. Comparators overwrite committed summaries; review regenerated diffs deliberately.

## Commit & Pull Request Guidelines

History mixes imperative subjects (`Add`, `Update`, `Patch`) with prefixes such as `feat:` and `docs:`. Use concise, scoped subjects. PRs should explain the change and rationale, link relevant issues, and report validation performed. Include rendered examples for visual changes and benchmark comparisons for placement or grading changes.
