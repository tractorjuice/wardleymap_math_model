# Competitor Benchmark Plan

**Companion to:** `BENCHMARK-METHODOLOGY.md` (how our benchmark works) and `BENCHMARK-REPORT.md` (results for the `wardley-map` skill).

This document lists every other publicly available Wardley-Map generator we could locate, classifies each by how easily it plugs into the existing 25-map benchmark, and defines the procedure for running it. The goal: produce an apples-to-apples table — `same-band %`, `|Δε|` distribution, ν/ε bias, coverage — for every competitor against the same Wardley corpus the mathmodel skill is already scored on.

---

## 1. Candidate list

Categorised by how much adaptation the benchmark needs. "Native" = outputs OWM (or trivially convertible) and runs inside Claude Code, so it drops into `arc-kit-compare`'s existing pattern.

### 1A. Native Claude Code skills (drop-in, OWM output)

| # | Name | Source | Output | Notes |
|---|---|---|---|---|
| 1 | `wardley-map` (ours) | `skills/wardley-map/` | OWM + Mermaid + prose | The mathmodel baseline. Already benchmarked on all 25 maps. |
| 2 | `arc-kit` `wardley-mapping` | `github.com/tractorjuice/arc-kit` | OWM + strategic prose | Already partially benchmarked on 7 maps in `arc-kit-compare/`. Plan: extend to all 25. |
| 3 | `haberlah/wardley-mapping` | `github.com/haberlah/wardley-mapping` | OWM + React artifact + prose | Confirmed Claude Code skill. Ships with `SKILL.md`; install to `~/.claude/skills/`. Untested here. |

### 1A'. Native Claude Code skills (non-OWM DSL — need converter)

| # | Name | Source | Output | Notes |
|---|---|---|---|---|
| 3b | `wtg2` | `github.com/owulveryck/wardleyToGo/tree/main/wtg2` | **WTG2 DSL** (not OWM) | Claude Code skill with frontmatter. Generates `.wtg2` files. WTG2 uses roman-numeral evolution positions (e.g. `II.7`) and richer annotations (five capitals, qualified inertia, climatic patterns, EVT/PST team types). **Blocked by: WTG2→OWM converter.** Without it, our aggregator can't parse the output. Two options: (i) write a converter in `competitor-compare/wtg2/wtg2_to_owm.mjs` — roman-numeral→ε mapping is straightforward, visibility requires walking the dependency graph same as our own skill does; (ii) extend `parse_owm` to read `.wtg2` natively. Option (i) is cleaner because the rest of the pipeline stays OWM-only. |

### 1B. Non-skill LLM baselines (prompt only, no skill framework)

These aren't skills but are frequently cited as "just prompt a model." Worth running as control baselines so the skill-vs-no-skill uplift is quantified.

| # | Name | Source | Output | Notes |
|---|---|---|---|---|
| 4 | In-tree standalone prompt | `prompts/wardley_map_generator.md` | OWM | Single-shot prompt, no skill scaffolding. Run via Claude and GPT-4 variants. |
| 5 | `lethain` prompt pattern | `lethain.com/ces-ai-generate-wardley-map-llm/` | OWM | Published single-prompt recipe using OWM DSL. Reproduces as baseline. |
| 6 | `craftingengstrategy` AI companion | `craftingengstrategy.com/aic/generate-wardley-map-with-llm/` | OWM | Same idea, different prompt wording. |

### 1C. ChatGPT-hosted GPTs (manual harness required)

| # | Name | URL | Output | Notes |
|---|---|---|---|---|
| 7 | Wardley Map Analyst | `chat.openai.com/g/g-Cic0bH5CF` | OWM (claimed) | Generates and analyses maps. Requires a ChatGPT Plus account and manual paste-in of the 25 scenarios. |
| 8 | Wardley Mapping (yeschat) | `yeschat.ai/gpts-ZxX0pFlA` | OWM / SVG | Free-tier GPT clone. |
| 9 | Learn Wardley Mapping | `chat.openai.com/g/g-sg6zS89Hi` | Pedagogical | Probably not a map generator — **likely skip** unless we confirm it can emit OWM. |
| 10 | Wardley Map Syntax Expert | `chat.openai.com/g/g-6vfuL6SXd` | Syntax fixer | Scope is syntax correction, not generation — **skip**. |
| 11 | Introduction to Wardley Mapping | `chat.openai.com/g/g-v6OW6JOQ7` | Pedagogical — **skip**. |

### 1D. Web apps and libraries (out of scope, listed for completeness)

Excluded from the benchmark because they either (a) don't generate maps from free-form scenarios — they render maps from user-authored OWM — or (b) are chat-with-existing-map rather than map-generation. Listed so future contributors don't waste time re-evaluating:

- `damonsk/onlinewardleymaps` — renderer/editor, not a generator.
- `anjackson/ipywardley` — Jupyter renderer.
- `wardleymap` and `ipywardley` PyPI packages — renderers.
- `tractorjuice/wardley_chat_with_map` — chats about an existing map.
- `IanSimon23/wardley_maps` — drag-and-drop editor.
- Streamlit learn-apps (`claude-chatbot`, `learnwardleymapping`) — pedagogical.

---

## 2. Targets in scope

Priority order for implementation:

1. **arc-kit (#2)** — extend the existing 7-map `arc-kit-compare` to the full 25.
2. **haberlah (#3)** — a fresh, drop-in Claude Code skill. Highest novelty-per-effort.
3. **standalone prompt (#4)** — the naive-LLM baseline. Run on Claude Opus 4.7 and GPT-4o.
4. **wtg2 (#3b)** — needs a WTG2→OWM converter first. Defer until the three OWM-native competitors are benchmarked, because the converter is a separate engineering task and shouldn't block the main comparison. Genuinely interesting as a side-by-side because WTG2 forces a richer strategic vocabulary (five capitals, qualified inertia) — worth testing whether more structure in the DSL produces tighter ε/ν placements or just more noise.
5. **Wardley Map Analyst GPT (#7)** — one external GPT, manual harness. Ceiling on "what a polished GPT can do."
6. **yeschat GPT (#8)** — second GPT, free-tier.
7. **lethain / craftingengstrategy prompts (#5, #6)** — diminishing returns but cheap once the harness exists.

Targets beyond #3 are optional — the comparison report can stand on the first three.

---

## 3. Test harness

Three harness patterns, matched to the three categories above.

### 3.1 Pattern A — Native Claude Code skill

Used for arc-kit (#2) and haberlah (#3). Mirrors `arc-kit-compare/` exactly.

```
skills/wardley-map-workspace/competitor-compare/
├── <competitor-name>/
│   ├── skill/                           # git-cloned competitor skill
│   ├── eval-<benchmark>/                # one directory per map
│   │   ├── wardley-reference.owm        # symlinked from iteration-10…14
│   │   └── with_skill/run-1/
│   │       ├── outputs/output.md        # competitor's final map
│   │       ├── outputs/draft.owm
│   │       └── timing.json
│   └── compare.py                       # same parse_owm + fuzzy_match as iteration-10
```

**Procedure per map** (reuses the spawn pattern in `BENCHMARK-METHODOLOGY.md §2(b)`):

1. `git clone` the competitor into `competitor-compare/<name>/skill/`.
2. Symlink or copy the 25 `wardley-reference.owm` files from `iteration-10…14` into `eval-<name>/`.
3. Reuse the exact scenario prompt from each iteration's `eval_metadata.json`. Do not rewrite — identical prompts are essential for apples-to-apples.
4. Spawn a subagent with: skill path = `competitor-compare/<name>/skill/SKILL.md`, scenario prompt, blind instruction ("do NOT read `wardley-reference.owm`"), output path.
5. Save `timing.json` from the subagent's completion notification.
6. Run the aggregator.

**Aggregator:** copy `arc-kit-compare/compare.py` to `competitor-compare/<name>/compare.py`; point `BENCHMARKS` at all 25 evals. No new metric code needed — `parse_owm` + `fuzzy_match` + `stage_of` are shared.

### 3.2 Pattern B — Standalone prompt, no skill

Used for #4–#6. The subagent gets only the prompt text and the scenario, with no skill framework, no references, no validator.

```
competitor-compare/prompt-baseline/
├── prompts/
│   ├── mathmodel.md                  # prompts/wardley_map_generator.md verbatim
│   ├── lethain.md                  # extracted from the published blog post
│   └── crafting-eng-strategy.md    # extracted from the published article
├── eval-<benchmark>/with_prompt-<variant>/run-1/
│   └── outputs/output.md
└── compare.py
```

**Procedure:**
1. Spawn a subagent whose system prompt is *only* the variant prompt + the scenario. No access to the 19-row cheat sheet, the 17-form inertia taxonomy, the validator, etc.
2. Require the output be a fenced `owm` block at the top of `output.md`.
3. Run the *same* validator (`scripts/validate_owm.mjs`) post-hoc — but do **not** feed violations back to the subagent. Count first-pass validation rate as its own metric; the validator output doesn't affect the comparison score.
4. Aggregate with the shared script.

Run two models for each prompt variant: `claude-opus-4-7` and `gpt-4o` (via the OpenAI SDK if available in the harness, otherwise skip the GPT arm and report partial).

### 3.3 Pattern D — Native skill with non-OWM DSL (converter-first)

Used for `wtg2` (#3b). Same flow as Pattern A **plus** a conversion step before the aggregator:

```
competitor-compare/wtg2/
├── skill/                              # git-cloned owulveryck/wardleyToGo/wtg2
├── wtg2_to_owm.mjs                     # one-shot converter, Node (ESM)
├── eval-<benchmark>/with_skill/run-1/
│   ├── outputs/output.md               # skill's native markdown deliverable
│   ├── outputs/draft.wtg2              # raw WTG2 block
│   └── outputs/draft.owm               # *converted* OWM, what the aggregator reads
```

**Converter requirements** (for `wtg2_to_owm.mjs`):

1. Parse the `.wtg2` DSL. Roman numerals with decimal subdivisions (e.g. `II.7`) map to ε: `I=[0,0.25) II=[0.25,0.5) III=[0.5,0.75) IV=[0.75,1.0]`, with the decimal as linear interpolation inside the band (so `II.7` → `0.25 + 0.25 * 0.7 = 0.425`).
2. Visibility isn't first-class in WTG2 — it's implied by node order in the value chain. Compute ν the same way our own skill does: graph distance from the nearest anchor, then `ν = exp(−0.6 · d)`. This is a judgment call: we're imposing our visibility model on someone else's map. Document this in the report as a caveat — a different visibility model would produce different ν numbers for the same underlying map.
3. Preserve edge endpoints 1:1; skip annotations (gameplays, capitals, inertia) since the aggregator ignores them anyway.
4. Write a fenced `owm` block plus a JSON sidecar `draft.conversion.json` describing every non-trivial choice, so the conversion is auditable.

Run the converter post-hoc on saved `draft.wtg2` files; do **not** call the converter from inside the subagent (it would conflate skill performance with converter bugs).

### 3.4 Pattern C — External ChatGPT GPT (manual harness)

Used for #7 and #8. No API access to ChatGPT store GPTs, so this is human-in-the-loop.

```
competitor-compare/chatgpt-gpts/
├── wardley-map-analyst/
│   └── eval-<benchmark>/with_gpt/run-1/outputs/output.md
└── yeschat/
    └── eval-<benchmark>/with_gpt/run-1/outputs/output.md
```

**Procedure (per map, manual):**
1. Open the GPT in a fresh conversation.
2. Paste the scenario prompt verbatim.
3. Ask "Output the full map as an OWM text block." (If the GPT produces an image or SVG only, request the DSL explicitly. If it refuses, log the refusal and skip the map.)
4. Copy the OWM block into `output.md`.
5. Record wall-clock duration; leave `timing.json.tokens` as `null`.

Budget: 25 maps × 2 GPTs × ~5 min each = ~4 hours of manual time. Do all 25 for one GPT before moving to the next to keep scenario framing fresh.

Known risks with this pattern:
- **Drift.** GPT behaviour changes between runs. Document the date tested.
- **Refusal / derailment.** Some GPTs will lecture on methodology instead of producing a map. Retry once; otherwise record as "no output" and exclude from the aggregate.
- **DSL deviation.** Some GPTs use a slightly different DSL. Pre-write a sed/awk normaliser in `competitor-compare/chatgpt-gpts/normalise.mjs` that maps common deviations to canonical OWM before validation.

---

## 4. What gets measured

For every competitor, the comparison reports the same metrics as the mathmodel skill:

- Coverage = (matched components) / (reference components), with fuzzy threshold 0.55.
- Strict same-band % and within-one-band %.
- Pooled `|Δε|` distribution at thresholds 0.05 / 0.10 / 0.15 / 0.20 / 0.25.
- Mean signed Δε (bias right) and mean signed Δν (bias up).
- Near-boundary miss count.
- **New metric:** first-pass validator pass rate (how many of the 25 maps are structurally well-formed without iteration). Relevant for the prompt baseline and external GPTs; the mathmodel skill iterates to 100% by construction.
- **New metric:** wall-clock / token cost per map. Already captured for the mathmodel skill; collect it for competitors too so the quality/cost tradeoff is visible.

Single consolidated output: `COMPETITOR-BENCHMARK-REPORT.md`, with one table per competitor and a head-to-head summary row.

---

## 5. Blind-contract considerations

The mathmodel benchmark enforces that the subagent must not read the reference `.owm`. Competitors need the same contract or the comparison is meaningless:

- **Pattern A (skill).** Same as the mathmodel run — explicit "do NOT read" instruction in the subagent prompt.
- **Pattern B (prompt).** Subagent has no tools beyond the prompt; file access trivially withheld.
- **Pattern C (GPT).** We cannot sandbox a ChatGPT GPT. Mitigation: scenarios do not name Wardley's specific map, and the reference `.owm` is not on the public web under the same title. GPTs may still have seen the map in training data (the `swardley/WARDLEY-MAP-REPOSITORY` is public), which is a ceiling on external-GPT results that we have to disclose in the report.

---

## 6. Deliverables

1. **`COMPETITOR-BENCHMARK-PLAN.md`** — this document. *(done)*
2. **`competitor-compare/`** directory mirroring the structure in §3.
3. **Per-competitor aggregator output** — one JSON + one table per competitor, committed alongside the raw `output.md` files so the comparison is reproducible without any LLM calls (same principle as §8 of `BENCHMARK-METHODOLOGY.md`).
4. **`COMPETITOR-BENCHMARK-REPORT.md`** — narrative summary. Roughly: one section per competitor (setup, results, caveats), a head-to-head comparison table, and a "cost per same-band point" chart if the numbers support one.

---

## 7. Explicitly out of scope

- **Strategic-analysis quality.** Same as the mathmodel benchmark — we compare placements, not prose. Competitor prose is retained for inspection but not scored.
- **Dependency-graph similarity.** Still out of scope. (A useful future metric, but adds scope here.)
- **Multi-run variance.** Each competitor is run once per map, same as the mathmodel skill. Don't try to estimate variance without first establishing it for our own skill — that's a separate project.
- **Prompt-engineering bakeoff.** We test the competitor as distributed, not re-engineered. If the haberlah skill underperforms because its prompt is weak, the report says so; we don't rewrite its prompt to "be fair."

---

## 8. Order of work (when executed)

1. Finish `arc-kit-compare` — extend from 7 → 25 maps. Smallest diff, validates the harness.
2. Run `haberlah/wardley-mapping` on all 25. First external skill.
3. Run the mathmodel standalone prompt on all 25. Establishes the no-skill floor.
4. Build `wtg2_to_owm.mjs`; run `wtg2` skill on all 25; convert; aggregate.
5. (Optional) Run the two ChatGPT GPTs manually.
6. Write `COMPETITOR-BENCHMARK-REPORT.md`.

Steps 1–3 are ~1 day of subagent runtime + aggregation. Step 4 adds a half-day of converter engineering before the skill can run. Step 5 is the long pole if attempted.
