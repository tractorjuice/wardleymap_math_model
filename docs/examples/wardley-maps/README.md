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

- Keeps `title`, `anchor`, `component`, edges (`src -> dst`), and `note`.
- Drops `pipeline`, `evolution` stage overrides, `style`, `market`, `evolve`, label offsets, and comments — Mermaid `wardley-beta` doesn't support them.
- Sanitises component/anchor names: replaces `/` with ` and `, strips `()[]{}`, normalises whitespace.
- Quotes `note` text and rewrites em-dashes / apostrophes / semicolons (Mermaid's `note` parser is strict about these).
- Drops edges whose endpoints aren't declared — OWM sometimes references components that were never introduced. Stderr logs how many were kept vs dropped per map.

## Reproducing

```bash
node scripts/owm_to_mermaid.mjs path/to/wardley-reference.owm > out.mermaid
```

Wrap the output in a ```` ```mermaid ```` fenced block in a Markdown file and view on GitHub.
