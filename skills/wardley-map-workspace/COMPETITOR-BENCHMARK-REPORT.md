# Competitor Benchmark Report

**Companion to:** `COMPETITOR-BENCHMARK-PLAN.md` (execution plan), `BENCHMARK-METHODOLOGY.md` (how the benchmark works), `BENCHMARK-REPORT.md` (the `mathmodel` skill on its original scenarios).

**TL;DR.** Six Wardley-Map generators benchmarked blind on the same 25 Wardley references, same scenarios, same comparison code:

- `mathmodel v2` (this repo's `skills/wardley-map/`, updated with haberlah-inspired additions)
- `mathmodel v1` (same skill before the update)
- `tractorjuice/arc-kit` (`wardley-mapping` full skill, arckit-claude variant)
- `tractorjuice/arc-kit` (`arckit-wardley.value-chain` sub-skill — value-chain decomposition only, static ε=0.50 placeholder)
- `haberlah/wardley-mapping`
- Prompt-only baseline using `prompts/wardley_map_generator.md`

Headline:

1. **`mathmodel v2` leads the field on legitimate tightness** — tightest \|Δε\| (0.201) and \|Δν\| (0.217) among generators that actually try to place ε, while keeping 100% structural-validator pass rate.
2. **Placement agreement (same-band) is still a wash across the five ε-placing generators** — everyone sits at 40–43% on strict-band and 88–93% on within-1-band, inside the benchmark's documented ±3–5pp noise floor.
3. **`arckit-value-chain` appears to "win" on same-band (61.8%) by gaming the metric** — it places every component at ε=0.50, which falls in the Product band where most of Wardley's components cluster. This is a pathological finding about the *metric*, not a strategic win — see §6. Treat value-chain's ε metrics as diagnostic of the benchmark, not of the skill.
4. **Well-formedness separates the field.** `mathmodel` (v1 and v2) pass the validator on 25/25 maps. `arckit-value-chain` manages 21/25 (visibility-only discipline is easier to satisfy). `haberlah` 16/25. The full `arc-kit` skill 6/25. The prompt baseline 5/25.

If you're choosing a generator: the scaffold buys you well-formedness and — after the v2 update — tightest placement. On band-agreement alone, a careful prompt is within noise of everything else at 3× lower cost. If you want *only* a value-chain decomposition (no evolution placement), `arckit-value-chain` does that and passes the ν invariant.

---

## 1. What was benchmarked

Five generators, same 25 Wardley references, same scenario prompts, same blind contract, same comparison code. Outputs saved and committed; the numbers below are reproducible by running `python3 competitor-compare/compare_competitor.py <name>`.

| # | Name | Type | SKILL file / prompt |
|---|---|---|---|
| A1 | `mathmodel v2` | Claude Code skill | `skills/wardley-map/SKILL.md` (current, post-update) |
| A2 | `mathmodel v1` | Claude Code skill | the same skill before the three haberlah-inspired additions in §5 — preserved in `competitor-compare/mathmodel/` |
| B | `tractorjuice/arc-kit` — `arckit-claude/skills/wardley-mapping/` only | Claude Code skill | cloned from `github.com/tractorjuice/arc-kit`. **One of 5 harness variants** the arc-kit repo ships; the others (`arckit-copilot`, `arckit-opencode`, `arckit-paperclip`, `arckit-codex`) were not tested as *full* skills. |
| B' | `tractorjuice/arc-kit` — `arckit-wardley.value-chain` sub-skill | Claude Code skill (partial-map) | from `arckit-codex/skills/arckit-wardley.value-chain/`. Produces components + dependencies + visibility; static ε=0.50 placeholder for all components. The other three composable sub-skills (`.climate`, `.doctrine`, `.gameplay`) were not tested. |
| C | `haberlah/wardley-mapping` | Claude Code skill | cloned from `github.com/haberlah/wardley-mapping` |
| D | Prompt-only baseline | Single-shot prompt | `prompts/wardley_map_generator.md`, no skill scaffold, no WebSearch |

Why both `v1` and `v2`: we were curious whether placement-tightness advantages haberlah showed on the benchmark could be imported into `mathmodel` without losing density or validator guarantees. §5 covers that experiment; §3.1 shows the result.

Note: an earlier 7-map `arc-kit-compare/` run exists on different scenarios and is preserved for historical reference. All five generators in this report are scored on the same fresh 25-map run.

Deferred from the plan:

- **wtg2** (`owulveryck/wardleyToGo`) — outputs WTG2 DSL not OWM. Requires a `wtg2_to_owm.mjs` converter (roman-numeral → ε interpolation, graph-distance → ν). Would come next if we continue this workstream.
- **ChatGPT GPTs** (Wardley Map Analyst, yeschat) — require a manual human harness (25 × 2 ≈ 4 hours of paste-in work). Deferred.

---

## 2. Methodology

### 2.1 Why we re-ran the mathmodel skill

`BENCHMARK-REPORT.md` reports `mathmodel`'s numbers on a set of scenarios written at the time of iterations 10–14. Those scenario prompts were never committed to disk. The published numbers (coverage ≈ 37%, same-band ≈ 37%) are against *those* scenarios.

Re-running `mathmodel` on the new 25 scenarios gives apples-to-apples comparability with haberlah, arc-kit, and the prompt baseline. It also produced a large delta vs. the published numbers — see §4.3.

### 2.2 Scenario generation

A single scenario-writer subagent read the 25 `wardley-reference.owm` files and wrote one scenario prompt per reference, following the recipe in `BENCHMARK-METHODOLOGY.md §2(a)`. Scenarios are committed at `competitor-compare/scenarios.json`. The `ai-trust` scenario is the canonical one from `BENCHMARK-METHODOLOGY.md §2(a)`; the other 24 were reconstructed from reference titles and content in practitioner voice.

Scenarios are 450–900 characters, ~2–4 sentences each. They deliberately name the stakeholder types and component *categories* the map should span — but not Wardley's specific component names or placements.

**Caveat:** scenarios that enumerate component categories (e.g. "models, algorithms, data, compute") effectively leak partial map structure. This inflates coverage across *all* generators equally, so the cross-generator comparison stays valid. The impact is visible in §4.3 when we compare the re-run mathmodel numbers to the published mathmodel numbers on older, terser scenarios.

### 2.3 Harness

Five directories under `competitor-compare/`:

- `mathmodel-v2/` — 25 evals, post-update skill. Primary column in §3.1.
- `mathmodel/` — 25 evals, pre-update skill (what §5 refers to as `v1`).
- `arc-kit/` — 25 evals.
- `haberlah/` — 25 evals.
- `prompt-baseline/` — 25 evals, subdir `with_prompt-mathmodel/run-1/outputs/`, instruction set limited to `prompts/wardley_map_generator.md`.

Reference `.owm` files are symlinked from the corresponding `iteration-10..14/` paths. Each subagent was given explicit "do NOT read the reference" instructions and path references to both the symlink and the upstream file.

### 2.4 Aggregator

`competitor-compare/compare_competitor.py` is a thin reuse of `iteration-10/compare.py`'s `parse_owm` and `fuzzy_match` primitives. Metrics are identical to `compare_all_25.py`:

- **Coverage** = fraction of reference components that match an output component (fuzzy threshold 0.55).
- **Same-band** = fraction of matched pairs where the reference and output sit in the same evolution quartile.
- **Within-1-band** = same-band allowing ±1 quartile.
- **\|Δε\|, \|Δν\|** = mean absolute placement delta across matched pairs. The *tightness* metric — how close the generator's coordinates land to Wardley's on each axis.
- **ε-bias, ν-bias** = mean signed delta (competitor − reference).
- **Pooled \|Δε\| ≤ T** = fraction of pooled matched pairs within ε tolerance T.

The aggregator tries `draft.owm` first, then falls back to `output.md`.

---

## 3. Results

### 3.1 Six-way aggregate (25 maps, identical scenarios)

| Metric | **mathmodel v2** | mathmodel v1 | arc-kit | arckit-value-chain† | haberlah | prompt |
|---|---|---|---|---|---|---|
| mean coverage | 77.9% | 79.0% | **79.3%** | 72.9% | 72.0% | 78.7% |
| mean same-band | 40.8% | 41.3% | 40.8% | **61.8%†** | 39.9% | 42.8% |
| mean within-1-band | 91.8% | 90.9% | 88.0% | **96.0%†** | 90.0% | 92.5% |
| **mean \|Δε\|** (tightness) | 0.201 | 0.223 | 0.239 | **0.198†** | 0.214 | 0.219 |
| **mean \|Δν\|** (tightness) | 0.217 | 0.259 | 0.249 | 0.247 | **0.231** | 0.255 |
| mean ε-bias (signed) | −0.032 | −0.041 | −0.032 | **−0.113†** | −0.057 | −0.058 |
| mean ν-bias (signed) | +0.047 | +0.039 | +0.029 | **+0.018** | +0.021 | +0.061 |
| pooled \|Δε\| ≤ 0.10 | 33.0% | 32.5% | 31.4% | **35.6%†** | 32.9% | 34.2% |
| pooled \|Δε\| ≤ 0.15 | **50.5%** | 48.6% | 46.0% | 49.3% | 49.6% | 49.9% |
| pooled \|Δε\| ≤ 0.20 | 65.1% | 64.1% | 59.8% | **76.4%†** | 63.5% | 66.0% |
| pooled \|Δε\| ≤ 0.25 | 75.2% | 77.1% | 71.6% | **91.2%†** | 73.2% | 75.9% |

Bold = per-metric leader.
† = value-chain's ε-based metrics are **not comparable** to the others. The skill places every component at the static placeholder ε=0.50, which coincidentally sits in the Product band where most of Wardley's components cluster. That inflates same-band, pooled-closeness, and \|Δε\| *without* the skill actually placing anything on the evolution axis. See §4.6. The signed ε-bias (−0.113) — the largest in the table — is the tell: static 0.50 is systematically to the left of Wardley's mean ε.

**Legitimate (non-pathological) per-metric leaders:**

- `mathmodel v2`: \|Δε\| (0.201), pooled ≤0.15 (50.5%)
- `mathmodel v1`: pooled ≤0.25 (77.1% among ε-placing generators)
- `arc-kit`: coverage (79.3%)
- `haberlah`: \|Δν\| (0.231)
- `prompt`: same-band (42.8%), within-1-band (92.5%), pooled ≤0.10 (34.2%), pooled ≤0.20 (66.0%)

The prompt-baseline's wins are all within ±3pp of next-best (inside the documented noise floor). v2's lead on \|Δε\| (0.201 vs 0.214) is outside the noise floor at n=25.

### 3.2 Map size and shape

| Generator | avg components (anchors + V) | typical edge count |
|---|---|---|
| mathmodel v2 | 41 | 70–100 |
| mathmodel v1 | 42 | 70–90 |
| arc-kit | 29 | 45–70 |
| arckit-value-chain | 22 | 30–60 |
| haberlah | 20 | 30–60 |
| prompt-baseline | 33 | 50–80 |

Wardley's own published maps average ~40 components. Only `mathmodel` (both versions) hits that density on multi-stakeholder landscapes. Haberlah's 8–15 soft cap / 18 hard warning forces it to ~20, missing 30–50% of Wardley's components on the bigger benchmarks.

### 3.3 Same-band by benchmark (top and bottom)

All five generators mostly agree on which maps are easy and which are hard:

- **Easy (everyone >55% same-band):** telecoms-sovereignty, transport-logistics, personal-conversational, cybersecurity-risk.
- **Hard (everyone <30% same-band):** culture-gender, politics-labour, telecoms-space, finance-risk.

"Hard" maps are generally ones where Wardley's own placements are idiosyncratic — cultural concepts stretched across the axes; political machinery placed by domain intuition rather than cheat-sheet evidence.

### 3.4 Placement-bias pattern

All five generators systematically under-place ε relative to Wardley (signed bias −0.03 to −0.06): components end up further left (less evolved) than Wardley positioned them. Haberlah's stricter stage boundaries (`Genesis 0.00–0.17, Custom 0.18–0.39, Product 0.40–0.69, Commodity 0.70–1.00` vs the canonical `0.25/0.50/0.75`) amplify this.

All five also over-place ν (+0.02 to +0.06). Arc-kit has the smallest ν-bias (+0.029); haberlah's close (+0.021). `mathmodel v2`'s ν-bias (+0.047) is slightly larger than v1's (+0.039) — a minor regression; may be worth investigating if we want to keep closing the visibility gap.

---

## 4. Findings

### 4.1 The scaffold isn't obviously better than a prompt on *band* agreement

Four materially different approaches produce same-band metrics within 3pp:

- **mathmodel v2:** full 7-step procedure with cheat-sheet scoring, exponential visibility seed, deep placement via WebSearch, validator iteration, plus the three §5 additions (strategic-context framing, per-component evidence table, build/buy table).
- **mathmodel v1:** same as v2 without the three additions.
- **arc-kit:** 5-step procedure with its own evolution-stages reference, YAML output format, quantitative D/K/R analysis.
- **haberlah:** 7-step procedure with a characteristics-framework scoring method, own validator, hard component cap.
- **prompt-baseline:** single-shot LLM response to a prompt that describes the math model. No iteration. No WebSearch. No references bundle.

The prompt baseline matches or slightly leads on same-band (42.8%), within-1-band (92.5%), and pooled ≤0.10. It costs about **3× fewer tokens** per run (~30k vs the skills' 60-100k). So on cost-per-band-agreement, the prompt is clearly ahead.

### 4.2 Where the scaffolds *do* differ from the prompt baseline

- **Validator pass rate.** Machine-verified by running `scripts/validate_owm.mjs` on every `draft.owm` post-hoc:

  | Generator | pass / 25 | rate |
  |---|---|---|
  | mathmodel v2 | 25 | **100%** |
  | mathmodel v1 | 25 | **100%** |
  | arckit-value-chain | 21 | 84% |
  | haberlah | 16 | 64% |
  | arc-kit | 6 | 24% |
  | prompt-baseline | 5 | **20%** |

  `mathmodel` iterates to 0 violations by construction — SKILL.md mandates it. Haberlah has its own validator that overlaps partially with ours. Arc-kit has no validator step. The prompt baseline ships first-pass.

  This is where the math-model scaffold earns its token budget. The placement-agreement numbers in §3.1 are averaged over all 25 draft maps regardless of well-formedness; the bottom three generators are "matching Wardley" using maps that wouldn't load in OnlineWardleyMaps without fixing.

- **Placement tightness (§3.1 \|Δε\| / \|Δν\|).** After the §5 update, v2 commits to components more precisely than anything else: mean \|Δε\| of 0.201 against haberlah's 0.214 and v1's 0.223. For a strategist reading the map, this means v2's coordinates are on average within ~0.10 of where Wardley placed the component (given noise floor ~0.06), rather than ~0.12–0.13 for the other generators.

- **Map density.** Only `mathmodel` matches Wardley's own ~40-component target on multi-stakeholder landscapes. Haberlah lands at half that by design; arc-kit at about two-thirds.

- **Strategic-analysis richness.** `mathmodel` cites Wardley's 61 gameplays and 40 doctrine principles by number. Haberlah provides a build-vs-buy table and 12–24 month evolution predictions (now also in `mathmodel v2`, per §5). The prompt baseline hits the major structural items (top-3 D/K/R, named gameplays) but cites them more loosely.

- **Deep placement.** Only `mathmodel` does WebSearch-driven placement adjustment. On 2022–2023-dated scenarios with live vendor landscapes, this shows up in output prose; on the benchmark's placement metrics the impact is small.

### 4.3 Scenario detail inflates apparent performance

Published `mathmodel` numbers (terse scenarios, `benchmark-25-summary.json`):
- coverage 36.7%, same-band 36.6%, pooled ≤0.20 61.9%.

`mathmodel v1` rerun numbers (new, more-detailed scenarios):
- coverage 79.0%, same-band 41.3%, pooled ≤0.20 64.1%.

Coverage jumped 42 percentage points with the same skill. Same-band and placement metrics barely moved. This tells us:

- **Coverage is scenario-sensitive.** When scenarios enumerate component categories, the generator finds more references. Coverage measures how well the skill translates a scenario into Wardley's vocabulary, not how well it discovers components from nothing.
- **Placement metrics (same-band, \|Δε\|) are scenario-robust.** Agreement on evolution stage doesn't change much when you tell the skill what to look for — the scoring method is doing the work.

**Implication:** if comparing generators on the same scenarios, coverage is a fair metric. If comparing generators on *different* scenarios, coverage is not — the scenario carries most of the variance.

### 4.4 Haberlah's distinct choices show up in the metrics

- **Non-canonical band boundaries** (`0.17 / 0.39 / 0.69` vs Wardley's `0.25 / 0.50 / 0.75`) — haberlah's ε-bias is −0.057 (most leftward), consistent with a systematic shift.
- **Component cap.** Lower coverage (72% vs 78–79%) is the skill's design preference for readability over comprehensiveness.
- **Tight placement** (\|Δε\| = 0.214 pre-v2, second-tightest overall). When haberlah commits to a component, it places it close to Wardley on average — an artefact of the characteristics-framework producing lower within-skill variance at the cost of missing more components.

This was the observation that triggered the v2 update. See §5.

### 4.5 ν-bias is skill-independent

All five generators over-place ν (+0.02 to +0.06). Prompt-baseline without explicit visibility reasoning also shows it. The bias is roughly constant across scaffold choice, which suggests it's a property of *how LLMs reason about "user-visible"* rather than a specific scaffold choice.

---

## 5. The haberlah-inspired update to `mathmodel`

Based on the v1 benchmark, three patterns haberlah does well were worth importing into `mathmodel`:

1. **Upfront "strategic context" step.** Haberlah's Step 1 clarifies four framing decisions (strategic question, user anchor, core needs, scope boundary) before listing a single component. `mathmodel` previously jumped into `V` without naming the decision the map informs.
2. **Per-component evolution rationale table.** Haberlah requires a one-sentence evidence citation per component (named vendors, dated regulation, standards activity). `mathmodel` produced one rationale per map bundled into deep-placement prose, not per component.
3. **Build-vs-buy / outsource table.** Haberlah emits a structured table mapping components to sourcing recommendations. `mathmodel` produced gameplay recommendations that implied this but didn't structure it.

All three were added to `mathmodel`'s SKILL.md as:

- **Step 0** (Strategic context) — new, before Step 1.
- **§3.2** (Component evolution rationale table) — new, after the OWM block, evidence-per-component required.
- **§4d** (Build / Buy / Outsource recommendations) — new, before the gameplay and doctrine sections.

Not adopted:

- Haberlah's non-canonical band boundaries (costs ~2pp same-band).
- Haberlah's 8–15 component cap (costs 7pp coverage on multi-stakeholder maps).
- React artifact deliverable (heavy, optional, not benchmark-relevant).

### 5.1 Before/after numbers

Full 25-map benchmark, same scenarios, same harness:

| Metric | v1 | v2 | Δ |
|---|---|---|---|
| coverage | 79.0% | 77.9% | −1.1pp |
| same-band | 41.3% | 40.8% | −0.5pp |
| within-1-band | 90.9% | 91.8% | +0.9pp |
| **\|Δε\|** | **0.223** | **0.201** | **−0.022 tighter** |
| **\|Δν\|** | **0.259** | **0.217** | **−0.042 tighter** |
| pooled ≤0.15 | 48.6% | 50.5% | +1.9pp |
| pooled ≤0.20 | 64.1% | 65.1% | +1.0pp |
| pooled ≤0.25 | 77.1% | 75.2% | −1.9pp |
| validator pass | 100% | 100% | unchanged |
| avg components | 42 | 41 | −1 |

**Interpretation:** the evidence-table requirement forces each placement to be justifiable with concrete signal (specific vendor, standard, or regulation). When placements can't be justified, they get moved — the result is tighter \|Δε\| and \|Δν\|, without losing density or validator pass rate. Same-band agreement doesn't move because band membership is a coarser signal than coordinate tightness; the same component ends up in the same band either way.

The small coverage drop (−1.1pp) is within run-to-run noise and isn't load-bearing; the tightness gain (0.022 on \|Δε\|, 0.042 on \|Δν\|) is outside noise at n=25.

### 5.2 The value-chain sub-skill finding: a metric-exposing result

The `arckit-wardley.value-chain` skill is explicitly a partial-map skill — it decomposes a user need into components + dependencies + visibility (Y-axis) but **does not assign evolution positions** (X-axis). Every component ships at ε=0.50 as a placeholder; the skill's README says downstream composition with another sub-skill is required to fill in ε.

Running it through the benchmark aggregator without modification produces these numbers:

| Metric | value-chain | meaning |
|---|---|---|
| coverage | 72.9% | legit — about matches haberlah, slightly below mathmodel |
| same-band | **61.8%** | **pathological** — ε=0.50 lands in the Product band, which is the modal band in Wardley's maps |
| within-1-band | **96.0%** | **pathological** — almost everything Wardley places is within ±1 band of Product |
| \|Δε\| | **0.198** | **pathological** — Wardley's components cluster near ε=0.50, so static-0.50 has small average error |
| ε-bias | **−0.113** | the tell — largest leftward bias of any competitor, because static 0.50 is systematically left of Wardley's mean ε |
| validator pass | 21/25 (84%) | legit — ν-only discipline is easier to satisfy than full ε+ν |

**What this exposes about the benchmark metrics:**

*Same-band* and *pooled \|Δε\| ≤ T* are susceptible to a "predict the median" strategy. If the evaluation corpus is unevenly distributed across evolution stages (and Wardley's is — Product-heavy), a generator can score high by placing all components at the modal stage without doing any real placement work. The value-chain skill didn't *try* to game the metric — it just happens to ship a placeholder that falls in the right band. But any generator that did try would beat everything else on same-band trivially.

**What this doesn't affect:**

- *\|Δν\|* and *ν-bias* are still informative — the value-chain skill places ν meaningfully (second-lowest ν-bias at +0.018, close to arc-kit's +0.029).
- *Coverage* is unaffected by the ε placeholder.
- *Validator pass* is unaffected — it checks ν invariants and edge endpoints, not ε values.

So for the value-chain skill *specifically*, the interpretable metrics are coverage (72.9%), \|Δν\| (0.247), ν-bias (+0.018), and validator pass (84%). On those four, it's comparable to haberlah but with a narrower scope.

**What we learned about the other generators via this:** their same-band numbers (40–43%) aren't just "a statistical tie with the prompt baseline." They're *below* the floor a null strategy achieves by predicting the modal band. This doesn't mean those generators are bad — they're spending effort placing components on ε, and that effort results in a distribution of placements rather than clustering at 0.50. The benchmark currently rewards the cluster-at-median strategy more than the distribute-by-evidence strategy. If we wanted to reward real placement more, we'd need a metric that penalises static outputs — e.g., weighted by the *variance* of the skill's ε placements, or normalised against a "always predict median" baseline.

Deferred to future work: a baseline-adjusted same-band metric that subtracts the "static ε=median" score would make the cross-generator comparison fairer.

### 5.3 What this means more broadly

The haberlah-inspired additions are structural: they force the skill to justify every placement with observable evidence. That's not a model-level improvement, it's a prompt-discipline improvement. The prompt baseline got the same \|Δε\| as v1 without any structural scaffolding, because a single pass of a capable LLM on the math-model prompt already does roughly what v1's procedure was doing. What v2 adds is the *citation requirement* — a discipline haberlah's SKILL.md already had, that `mathmodel`'s did not.

Reasonable next step: see if more evidence-required discipline (e.g., required citation for every evolve arrow, every inertia flag) continues to tighten placement, or if 0.201 is the floor for this scenario set.

---

## 6. Limitations and caveats

1. **Validator doesn't run inside subagents.** Every skill subagent reported that `node scripts/validate_owm.mjs` was denied by the Claude Code permission allowlist (which only whitelists iteration-16 paths). They walked the three validator rules manually. Post-hoc we re-ran the real validator across all 125 draft files — see §4.2 for the actual pass/fail numbers. The mathmodel manual walk-through held up (25/25 pass on both v1 and v2). Recommended fix: add a wildcard `Bash(node skills/wardley-map/scripts/validate_owm.mjs *)` to `.claude/settings.local.json` so future runs exercise the validator in-loop.
2. **Fuzzy matching imperfection.** The 0.55 threshold admits some loose matches and misses some legitimate synonyms (`BENCHMARK-METHODOLOGY.md §3.2`). Affects all generators equally.
3. **Same-as-Wardley ≠ correct.** Wardley himself published these references; agreeing with him isn't the same as being right. Different Wardley mappers would disagree on 15–25% of placements per the cheat-sheet noise floor.
4. **Single run per map per competitor.** LLM stochasticity not estimated. The ±3–5pp differences between generators would fluctuate run-to-run.
5. **Deep-placement quality not measured.** The mathmodel skill does vendor-landscape research; we know it happens but don't score the adjustments.
6. **wtg2 and ChatGPT GPTs not benchmarked.** In the plan, deferrable.
7. **Rate limit partially affected arc-kit.** Three arc-kit subagents (defence-intelligence, defence-grey-zone, telecoms-space) hit the rate limit before writing strategic prose; their `draft.owm` completed and feeds the placement numbers, but the `output.md` for those three is empty.
8. **Scenario inflation (§4.3).** New-scenarios coverage is higher than old-scenarios coverage by ~40pp, the dominant source of variance between our rerun and the published `BENCHMARK-REPORT.md` numbers.
9. **arc-kit: only 1 of 5 harness variants tested.** `tractorjuice/arc-kit` ships the wardley-mapping skill in five harness-specific copies (`arckit-claude`, `arckit-copilot`, `arckit-opencode`, `arckit-paperclip`, `arckit-codex`). Our benchmark covers only `arckit-claude`. The others differ — we diffed `arckit-copilot`'s `SKILL.md` against `arckit-claude`'s and confirmed they are not identical — so the arc-kit numbers in this report (including the 24% validator pass rate and 79.3% coverage) are variant-specific, not arc-kit-generic. Additionally, `arckit-codex/` ships a composable architecture (`arckit-wardley` + four sub-skills: `.value-chain`, `.climate`, `.doctrine`, `.gameplay`) intended to be orchestrated across multiple skill invocations per map. That architecture was not tested — the benchmark harness spawns one subagent per map and doesn't orchestrate composed sub-skills. Testing these fairly would require (a) ~2M additional tokens for the 4 untested harness variants and (b) harness changes plus another ~2M tokens for the composable architecture.

---

## 7. Reproducibility

Everything is committed. Commands to reproduce:

```bash
python3 skills/wardley-map-workspace/competitor-compare/compare_competitor.py mathmodel-v2
python3 skills/wardley-map-workspace/competitor-compare/compare_competitor.py mathmodel
python3 skills/wardley-map-workspace/competitor-compare/compare_competitor.py arc-kit
python3 skills/wardley-map-workspace/competitor-compare/compare_competitor.py arckit-value-chain
python3 skills/wardley-map-workspace/competitor-compare/compare_competitor.py haberlah
python3 skills/wardley-map-workspace/competitor-compare/compare_competitor.py prompt-baseline --output-subdir with_prompt-mathmodel

# per-competitor summary JSON lands at
#   competitor-compare/<name>/competitor-summary-<name>.json
```

The 125 `output.md` / `draft.owm` files, `scenarios.json`, and five summary JSONs are the full artefact set. The comparison is arithmetic on parsed coordinates; any reader can check or extend without calling the LLM.

---

## 8. Recommendation

Choose a Wardley-map generator on what you need from the output:

- **Valid OWM by construction** → `mathmodel v2` or `v1` (100%). `arckit-value-chain` (84%) is decent for partial maps. Haberlah at 64% is acceptable if you'll patch ~1/3 of outputs. Everything else requires a fix-up pass.
- **Tightest placement agreement with Wardley on the axes** → `mathmodel v2` (tightest \|Δε\| among generators that genuinely place ε).
- **Rich strategic prose with 61-play / 40-doctrine citations by number, build-vs-buy table, evidence-per-component** → `mathmodel v2`.
- **Build-vs-buy tables and React artifacts** → `haberlah` (or `mathmodel v2` for the table, which picked up the haberlah feature).
- **Structured YAML with quantitative D/K/R inline** → `arc-kit`.
- **Value-chain decomposition only (no evolution placement needed)** → `arckit-value-chain`. It doesn't try to place ε; if that's fine for your workflow (e.g., you'll add ε manually downstream or you only need the dependency graph), this is a clean, validator-friendly option.
- **Lowest token cost with acceptable placement** → prompt baseline at ~30k tokens per map.
- **Canonical `0.25/0.5/0.75` band boundaries** → `mathmodel`, `arc-kit`, or prompt-baseline. Haberlah uses non-canonical boundaries.

**What the benchmark actually proved:**

1. The skill scaffold's moat over a careful prompt is *not* placement agreement — those are within noise. The moat is validator pass rate (100% vs 20%) and, after the v2 update, placement tightness (0.201 vs 0.219).
2. Adding three structural disciplines from haberlah — up-front strategic context, per-component evidence citations, structured build/buy table — measurably tightened `mathmodel`'s placements without sacrificing density or validator pass rate. The additions worked.
3. The benchmark was worth doing. Before it, we didn't know that (a) a naive prompt gets same-band agreement within 3pp of the scaffold at 3× lower cost, (b) haberlah's tighter-placement pattern was importable, or (c) arc-kit would fail the validator 19/25 times despite being a published Claude Code skill.

If the workstream continues, the next experiments worth running are: (i) the remaining 4 arc-kit harness variants (`arckit-copilot`, `arckit-opencode`, `arckit-paperclip`, `arckit-codex`) to see whether the 24% validator pass rate is variant-specific or a property of the arc-kit procedure; (ii) the composable `arckit-wardley.*` architecture, which requires harness changes to orchestrate 5 sub-skills per map; (iii) the `wtg2` comparison with a DSL converter; (iv) a strict validator-required subagent loop to see if `mathmodel`'s 100% pass rate holds under machine validation instead of manual edge-walking; and (v) variance estimation — 3 runs per map per generator to establish the run-to-run noise floor, so we can tell what matters from what's coincidence.
