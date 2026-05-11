# Wardley maps — Mermaid rendering

Five maps from [`swardley/WARDLEY-MAP-REPOSITORY`](https://github.com/swardley/WARDLEY-MAP-REPOSITORY) converted to Mermaid's `wardley-beta` diagram type (mermaid 11.14+). Rendered inline on GitHub when you open each `.md` file.

| Map | Date pinned | Notes |
|---|---|---|
| [ai-trust](ai-trust.md) | June 2023 | 3 anchors, 34 components. Abstract Wardley vocabulary (OUTPUT, ACCESS, CONTROLS, DATA). |
| [manufacturing](manufacturing.md) | Feb 2023 | 44 components. No explicit anchors in the source. |
| [culture-gender](culture-gender.md) | March 2022 | 25 components. Unusual cultural-contest application. |
| [telecoms-sovereignty](telecoms-sovereignty.md) | Oct 2022 | 49 components. Many-layered infrastructure stack. |
| [agriculture-regen](agriculture-regen.md) | Aug 2022 | 50 components, 4 notes. IRA-week snapshot. |

## Conversion pipeline

`scripts/owm_to_mermaid.mjs` (Node) parses each `.owm` source and emits a Mermaid block. The converter:

- Keeps `title`, custom `evolution` stages, `anchor`, `component`, dependency links (`->`), flow links (`+>`), `note`, `evolve`, pipelines, label offsets, inertia, and build/buy/outsource/market decorators where the OWM source maps cleanly to Mermaid.
- Drops OWM-only directives such as `style wardley`, axis overrides, `ecosystem`, `submap`, `url`, and pioneer/settler/townplanner markers.
- Always double-quotes component, anchor, and edge names. Mermaid 11.15 supports unquoted hyphenated names, but quoted `STRING` names are still the safest representation for slashes, punctuation, reserved-keyword prefixes, and numeric labels.
- Drops links whose endpoints aren't declared — OWM reference maps sometimes include links to components that were never introduced.

## Reproducing

```bash
node scripts/owm_to_mermaid.mjs path/to/wardley-reference.owm > out.mermaid
```

Wrap the output in a ```` ```mermaid ```` fenced block in a Markdown file and view on GitHub.
