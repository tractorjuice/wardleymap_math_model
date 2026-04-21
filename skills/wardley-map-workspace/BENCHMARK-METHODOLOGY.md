# Benchmark Methodology

**Companion to:** `BENCHMARK-REPORT.md` (which focuses on results).

This document describes how the benchmark actually works — end-to-end — in enough detail to reproduce, extend, or critique it. Read this if you want to understand what a "same-band" number is actually measuring, or if you want to add a new benchmark map.

---

## 1. What the benchmark answers

**Question:** when the `wardley-map` skill is given a free-form scenario description, how closely does the map it produces match a map Simon Wardley himself produced for the same topic?

**Test-set:** `swardley/WARDLEY-MAP-REPOSITORY` on GitHub, a corpus of ~60 Wardley maps in OWM text format, CC-BY-SA. We sample from this corpus.

**"Closely" means four distinct things**, and the benchmark reports all four:

1. **Component overlap** — fraction of Wardley's components that also appear (by name or fuzzy-match) in our map
2. **Stage-band agreement** — for components that appear in both maps, whether they land in the same evolution-axis quartile
3. **Placement closeness** — continuous `|Δε|` distribution regardless of band
4. **Directional bias** — mean signed Δε and Δν (are we systematically higher/lower than Wardley?)

Each measures something different. None is "the" agreement number.

---

## 2. End-to-end flow of a single benchmark

Pick any one of the 25 benchmarks in the workspace. The flow is:

```
Wardley's .owm file
       │
       │  (a) scenario-derivation (human)
       ▼
 Scenario prompt ─────────────────────┐
       │                               │
       │  (b) spawn subagent           │
       │      (Task/Agent tool)        │
       ▼                               │
 Subagent runs 7-step skill            │  (Wardley's
 procedure                             │   map NEVER
       │                               │   visible to
       │  (c) writes draft.owm         │   subagent)
       ▼                               │
 validate_owm.mjs                       │
       │                               │
       │  (d) iterate until clean      │
       ▼                               │
 Final output.md (map + analysis)      │
       │                               │
       │  (e) comparison                │
       └──► compare_all_25.py ◄─────────┘
                │
                ▼
        Aggregate metrics
```

### 2(a) Scenario derivation

Given a Wardley `.owm` file, the human (or an orchestrator) writes a natural-language scenario prompt that:

1. **States the topic** at a concrete enough level that a mapper can enumerate components (e.g., "Map the landscape of regenerative farming").
2. **Lists the stakeholders** the scenario should cover (e.g., "farmers, consumers, regulators, certifiers").
3. **Hints at the scope** (e.g., "including supply chains, measurement, funding, practices").
4. **Pins to a date** if the reference map is dated (e.g., "It's August 2022").
5. **Does NOT expose** Wardley's placements, component names, or map shape.

Example — for `ai/TRUST` dated June 2023:

> "It's June 2023. Map the AI trust landscape — what components determine whether individuals, government, and business can trust AI systems. Include technical components (models, algorithms, data, compute), governance components (regulations, audits, benchmarks, policy), control mechanisms (forensics, feedback loops, constitution), and outcome components (safety, reputation, competitive advantage). Tell me what's differentiating vs. commoditising and where trust itself is fragile."

The scenario is expected to be realistic — something a user would actually type. It summarises the scenario in a way the skill's users would pose it, not in Wardley's own vocabulary.

**The blind contract:** the subagent must not read the reference file. This is enforced by (i) not mentioning the file path, (ii) explicitly saying "do NOT read `wardley-reference.owm`", and (iii) checking subagent's tool use post-hoc (we can verify from the task transcript whether the file was read, though we typically trust the instruction).

### 2(b) Spawn the subagent

A subagent is spawned with the scenario prompt and the skill path. Example prompt template:

```
Benchmark task. Do NOT look at /workspaces/.../eval-<name>/wardley-reference.owm.

Skill: /workspaces/wardleymap_math_model/skills/wardley-map/SKILL.md

Scenario: <scenario text>

Read SKILL.md, follow full procedure (exponential seed,
deep placement, validator). Save final output to:
/workspaces/.../eval-<name>/with_skill/run-1/outputs/output.md.
```

The subagent runs autonomously. Typical runtime: 5-6 minutes. Typical cost: 70-90K tokens.

### 2(c) The subagent's internal pipeline

This is the skill's 7-step procedure, briefly:

1. **Components and anchors** — list `V` and identify the anchor set `U`. Density guidance targets 20-30 / 35-45 / 40-55 depending on scenario type.
2. **Dependencies** — build `E` as "depends-on" edges.
3. **Visibility ν** — seed `ν(v) = exp(−0.6 · d(v))` from graph distance to nearest anchor; override by judgment.
4. **Evolution ε** — score each component against a 4-row cheat-sheet subset (Ubiquity, Certainty, User Perception, Publication Types); aggregate using band midpoints `m(s) = (s − 0.5)/4`.
5. **Deep placement** — pick 3-5 components where rows disagree, strategic importance is high, or the domain is specialised; run WebSearch for vendor landscape, publication-type evidence, regulatory status, open-source activity. Adjust ε based on findings.
6. **Verification** — write the draft OWM to a file; run `scripts/validate_owm.mjs`; fix any reported violations; re-run until exit-code 0.
7. **Strategic analysis** — stage-first prose covering differentiation, commodity leverage, dependency risks, named gameplays from the 61-play catalogue, doctrine violations, climatic context, deep-placement findings, caveat.

### 2(d) The validator

`skills/wardley-map/scripts/validate_owm.mjs` is a Node (ESM) script that parses an OWM block and checks three invariants:

- Every component and anchor has coordinates in [0, 1]
- Every edge endpoint is declared as a component or anchor (no typos)
- For every edge `(a, b)`, `ν(a) ≥ ν(b)` (the visibility hard rule)

Exit-code 0 if clean, 1 otherwise with human-readable violation list. The skill instructs the subagent to iterate until clean. Across the 25-map benchmark, initial drafts had 1-13 violations; all fixed in 1-4 iterations.

### 2(e) Comparison

After all subagent runs complete, `compare_all_25.py` reads every `(reference, output)` pair and computes the metrics described in §3.

---

## 3. Metrics in detail

### 3.1 Parsing an OWM file

`parse_owm(text)` uses a regex that catches lines of the form:

```
(anchor|component) <name> [<visibility>, <evolution>]
```

It returns two dicts: anchors and components, each mapping `name → (ν, ε)`. Lines inside ` ```owm ` fences are preferred when present. Comments (`//`, `#`) and evolve/note/pipeline lines are ignored. Labels like `label [-10, 5]` are discarded.

### 3.2 Fuzzy name matching

For each of Wardley's components, we look for a match in our components. The match function checks, in this order:

1. **Exact match** (case-insensitive) → similarity score 1.0
2. **Substring containment** (either direction) → 0.9
3. **Word overlap** — Jaccard-like score on tokenised names
4. **SequenceMatcher ratio** from difflib

A candidate matches if the best score ≥ 0.55. The 0.55 threshold is a judgment call — lower would allow more matches but pollute the matched set with loose equivalents; higher would miss legitimate synonyms.

**Known false positives** this can produce:
- AI TRUST's `Training` (meaning "the act of training a model") matches our `Training Data` (meaning "the corpus used"), because they share the word "training".
- Generic names like `Policy` in one map match `Policy Frameworks` in the other.

The comparison report documents each match explicitly so false positives can be identified.

**Known false negatives:**
- Wardley's idiosyncratic short names (`Dr Google`, `believed`, `constitution`) don't match our operational terms even when the concept is similar.
- Abstract nodes Wardley treats as first-class (`OUTPUT`, `ACCESS`, `Bias`) are rarely reached for by our skill, so there's nothing to match against.

### 3.3 Band membership

```python
def stage_of(eps):
    if eps < 0.25: return 0  # Genesis
    if eps < 0.5:  return 1  # Custom Built
    if eps < 0.75: return 2  # Product (+rental)
    return 3                 # Commodity (+utility)
```

Strict same-band: `stage_of(ε_ref) == stage_of(ε_ours)`.
Within 1 band: `abs(stage_of(ε_ref) − stage_of(ε_ours)) ≤ 1`.

### 3.4 Closeness distribution

Across all matched pairs across all benchmarks (the pooled set — 358 pairs for n=25), we report the cumulative fraction at thresholds `|Δε| ≤ {0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50}`.

The useful thresholds have interpretations:

- **0.05** — fine-grained precision match
- **0.10** — within scoring-method noise (see §4)
- **0.20** — within strategic tolerance (build/buy/utility call doesn't change)
- **0.25** — within one band-width

### 3.5 Directional bias

For each matched pair, `Δε = ε_ours − ε_ref` (signed). Mean gives ε-bias. Same for ν-bias. Positive ε-bias means our skill places things further right (more industrialised) than Wardley on average.

### 3.6 Near-boundary miss

A pair is a "near-boundary miss" if `|Δε| ≤ 0.10` but `stage_of(ε_ref) ≠ stage_of(ε_ours)`. This counts the strict-band failures that are actually close placements straddling a band line. Reported both as absolute count and as fraction of strict-band misses.

---

## 4. The noise floor of cheat-sheet scoring

This matters for interpreting the metrics but isn't usually explicit.

The 4-row cheat-sheet method produces ε as the average of 4 row picks, each of which can be 1/2/3/4 (mapped to band midpoints 0.125 / 0.375 / 0.625 / 0.875).

Sensitivity of the mean:

- **One row changing by one stage** (e.g., picking Stage III instead of Stage II for one row): shifts the mean by `(0.625 - 0.375) / 4 = 0.0625`.
- **Two rows changing by one stage each**: shifts by `~0.125`.
- **One row changing by two stages** (rare): shifts by `0.125`.

A `|Δε|` of ~0.10 corresponds to **one row's worth of disagreement** on the 4-row method. That's the level of disagreement you'd get if the same mapper scored the same component twice on different days, or if two careful mappers read the evidence slightly differently on one of the four dimensions.

Implications:

- **|Δε| ≤ 0.10 is effectively noise.** Treating it as meaningful agreement or disagreement is over-reading the data.
- **|Δε| ≈ 0.15-0.25 is genuine but small** — within one band-width and within two rows' worth of disagreement.
- **|Δε| > 0.25 is large** — beyond band-width, beyond noise, and typically beyond strategic tolerance.

The full 19-row method (used when the scenario warrants depth) has finer resolution: one row's shift is ~0.013. But most runs use the 4-row subset, so noise floor ~0.10 is the working assumption.

---

## 5. What the benchmark does NOT measure

Knowing what's out of scope is as important as knowing what's in scope.

1. **Strategic quality.** The maps produce prose analyses with named gameplays and doctrine references. The benchmark does not compare these to Wardley's own analyses. A map can score well on placement and still give bad strategic advice, or vice versa.
2. **Dependency structure.** The benchmark compares component placements but not which edges exist between them. Two maps can have identical ν/ε placements for every component and entirely different dependency graphs.
3. **Deep placement quality.** The skill's WebSearch-driven placement adjustments are not evaluated. We know they happen (self-reported by subagents); we don't know if each individual adjustment was correct.
4. **Narrative coherence.** The strategic-analysis sections read well or badly. No metric captures this.
5. **Real-world usefulness.** Nothing here tests whether the maps actually drive good decisions. This would require user studies.

---

## 6. Known limitations

1. **Single-author corpus.** Every reference is Simon Wardley's own work. Faithfulness to Wardley's style is not the same as faithfulness to ground truth. Different Wardley mappers would produce different maps.
2. **Fuzzy matching biases.** False positives inflate disagreement (matched components that aren't really equivalent show large placement deltas). False negatives understate coverage.
3. **Time-pinning is imperfect.** Subagents have 2026 priors and can't fully suppress them even when instructed to pin to 2022-2023. This shows up as ε-drift on dated scenarios.
4. **Scenario-derivation variance.** The scenario prompt is written by a human; different prompts produce different maps. The benchmark could be more rigorous by using multiple prompt variants per reference map.
5. **Small n.** 25 maps in 18 domains. Aggregate metrics have ±3-5pp noise. Per-benchmark numbers are much noisier.
6. **No replication.** Each benchmark is run once. The skill uses deep placement which involves stochastic LLM choices; a second run would produce a somewhat different map. We do not estimate run-to-run variance.
7. **Chance baselines are rough.** The "random placement" baselines cited in the report use the observed ε distribution but don't account for correlated placements (e.g., infrastructure always commodity). True chance baselines would need Monte Carlo simulation.

---

## 7. How to add a new benchmark

### 7.1 Find a Wardley map

Browse <https://github.com/swardley/WARDLEY-MAP-REPOSITORY> or use the GitHub API. Pick a map in a domain you want to test. Look for:

- `.owm` text format (some are `.svg` images only — skip those unless you want to OCR)
- File size > 2 KB (a reasonable density of components)
- A title with a date, if possible (eases time-pinning)

### 7.2 Fetch and stash

```bash
curl -fsSL "https://raw.githubusercontent.com/swardley/WARDLEY-MAP-REPOSITORY/main/<path>" \
  > /tmp/wm-<shortname>.owm
mkdir -p skills/wardley-map-workspace/iteration-NN/eval-<shortname>/with_skill/run-1/outputs
cp /tmp/wm-<shortname>.owm \
   skills/wardley-map-workspace/iteration-NN/eval-<shortname>/wardley-reference.owm
```

### 7.3 Write a scenario prompt

Rules:

- State the topic in a practitioner's voice
- Name the stakeholder types involved
- List the dimensions you want covered (technical / regulatory / operational / etc.)
- Include a date if the reference is dated
- Don't leak Wardley's component names or placements

### 7.4 Spawn the subagent

Use the Task / Agent tool with the scenario prompt, the skill path, and the output path. Add the "do NOT read the reference" instruction explicitly.

### 7.5 Save timing on completion

When the subagent returns its completion notification, save `total_tokens` and `duration_ms` to `with_skill/run-1/timing.json`. The aggregator expects this file.

### 7.6 Add to the aggregator

Edit `compare_all_25.py` (or a new `compare_all_N.py`) to append:

```python
("new-benchmark-name",
 "iteration-NN/eval-<shortname>/wardley-reference.owm",
 "iteration-NN/eval-<shortname>/with_skill/run-1/outputs/output.md",
 "Domain"),
```

Rerun the aggregator; the new benchmark is included automatically.

---

## 8. How to rerun comparisons without rerunning the skill

All the reference files and output files are committed to the workspace, so the comparison is reproducible without calling the skill again:

```bash
cd skills/wardley-map-workspace
python3 compare_all_25.py
```

Outputs: per-map table, aggregate statistics, pooled `|Δε|` distribution, near-boundary miss count. Also writes `benchmark-25-summary.json`.

To modify the comparison (e.g., change the fuzzy threshold, add a new metric), edit `compare.py` or `compare_all_25.py` and rerun. The source maps don't change.

---

## 9. Data artefacts

Each eval directory contains:

| Path | Purpose |
|---|---|
| `eval-<name>/wardley-reference.owm` | Held-out reference map from Wardley's repo |
| `eval-<name>/eval_metadata.json` | Scenario prompt and (optionally) assertions |
| `eval-<name>/with_skill/run-1/outputs/output.md` | Skill's generated map + strategic analysis |
| `eval-<name>/with_skill/run-1/outputs/draft.owm` | Validator working file (pre-final iteration) |
| `eval-<name>/with_skill/run-1/timing.json` | Token count + duration from task notification |
| `eval-<name>/with_skill/run-1/grading.json` | (Some runs) assertion grading output |

Per-run artefacts are kept for post-hoc analysis: if the fuzzy matcher is improved, or a different metric is added, re-running `compare_all_25.py` against the same artefacts produces updated numbers without any LLM calls.

---

## 10. Reproducibility notes

**Skill version.** The skill at commit `44daa72` on `origin/main` is the version under test. Earlier iterations used reciprocal decay for visibility, a buggy `|Δε| < 0.25` same-stage metric, and no density guidance. Those are documented in the metric-history paragraph of §2.2 in the main report.

**Corpus version.** References were fetched from `main` branch of the swardley repo at the time of each iteration. If Wardley updates his maps, the references in this workspace will not automatically update — they are snapshots. To rerun with current versions, re-fetch.

**LLM determinism.** The subagent runs are not fully reproducible — the underlying model samples stochastically for non-trivial prompts, and the WebSearch tool returns live (time-varying) results. Reruns of the same scenario would produce substantially similar maps but not identical ones. The reported numbers are point estimates, not means over multiple runs.

**Human factors.** The scenario prompts are human-written. Someone else asking the skill "map sustainability supply chains" with slightly different framing would get a different map. This is a feature — the skill is meant to respond to the user's actual scenario — but it means the benchmark is testing the combination of (scenario prompt, skill).

---

## 11. How to critique these numbers

Looking at the report and not believing the headline? Here's what to check:

- **Are the fuzzy matches actually equivalent?** Open any `output.md` alongside its `wardley-reference.owm` and scan the `MATCHES` list in the comparison output. If many are loose, the placement metrics are unreliable.
- **Did the subagent peek at the reference?** Read the subagent's completion summary; it usually reports which files it read. A peek would inflate agreement dramatically.
- **Is the scenario prompt fair?** A prompt that implicitly nudges the skill toward Wardley's framing (e.g., mentioning "constitution" for AI trust) would inflate coverage. The prompts in this benchmark were written blind — check them.
- **Is `|Δε|` the right unit?** Wardley doesn't publish uncertainties on his placements. If you think `|Δε| = 0.15` is large, then strict agreement is what matters. If you think it's within noise, then strategic tolerance (`≤ 0.20`) is what matters. The report reports both.

The benchmark is designed to be inspectable all the way down. The comparison script is 200 lines of Python with no ML; the metrics are arithmetic on parsed coordinates; the outputs are plain text. Any conclusion should be verifiable from the artefacts without taking the numbers on trust.
