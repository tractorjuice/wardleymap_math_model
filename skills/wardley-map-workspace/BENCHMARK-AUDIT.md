# Benchmark methodology audit — 2026-05-11

**Audit subject:** `BENCHMARK-METHODOLOGY.md` and `compare_all_25.py` as the harness behind `BENCHMARK-REPORT.md`.

**Audit framework:** the eval-health checklist from `anthropics/cwc-workshops/rightmodel/.claude/skills/eval-audit-and-sweep/references/audit.md` (Apache-2.0). Sections 1-4 of that doc are: task design, harness design, metrics hygiene, grader design. This audit applies each section to our benchmark.

**How to read this:** findings are framed as observations and suggestions, not directives. Many of the items below are already partially acknowledged in `BENCHMARK-METHODOLOGY.md` §6 ("Known limitations"); the audit's value is the things that section does not yet name.

**Severity convention** (from `audit.md` §5):
- **A** — likely to make the reported numbers actively misleading.
- **B** — adds noise or limits generality without flipping conclusions.

---

## Severity A findings (worth a second look)

### A1. The reference is reachable on disk

`audit.md` §4 *"Ground truth not reachable by the model"*: the expected answers must not be anywhere the system under test can read them.

`wardley-reference.owm` lives in the same `eval-<name>/` directory as the subagent's output, and the only thing stopping it from being read is the prompt-level instruction *"do NOT look at /workspaces/.../wardley-reference.owm"* (`BENCHMARK-METHODOLOGY.md` §2(b)). §2(a) notes this is policy not enforcement: *"we typically trust the instruction."*

A misleading-numbers scenario: any single subagent run that fails to honour the instruction would inflate every metric for that map, and the rest of the benchmark would absorb the shift.

**Suggestion:** move the reference outside the eval directory before each run (e.g. to a sibling `references/` tree the subagent isn't told about), or post-hoc scan each subagent transcript for `Read` calls against `wardley-reference.owm` and tag any run where the file was touched.

### A2. Infra failures are not distinguished from model failures — *partly addressed 2026-05-11*

`audit.md` §2 *"Infra failures distinguished from model failures"*: API errors, timeouts, parse failures, validator non-convergence, sandbox crashes must be a separate status field from `passed=False`.

`compare_all_25.py:126-128` is currently:
```python
if not ref_p.exists() or not ours_p.exists():
    print(f"SKIP {name}: missing file(s)")
```

That's the only error path. A subagent that crashed mid-run, that produced an unparseable `output.md`, that hit the validator's iteration ceiling, or that emitted a truncated map all land in the same place: either silently absent (skipped) or silently degraded (parsed with whatever `parse_owm` could salvage). There is no `status` column distinguishing these from a clean run.

**Suggestion:** add a per-map `status ∈ {ok, infra_error, validator_unconverged, parse_failed, no_output}` field to `benchmark-25-summary.json`, computed from whatever is in `timing.json` plus a check on `draft.owm` validator iteration count. Aggregate metrics should then be computed over `status == "ok"` rows only, with the failure count reported separately.

### A3. Each benchmark runs once; no variance estimate — *smoke-tested 2026-05-11*

`audit.md` §2 *"Multiple trials with variance reported"*: a single run gives a point estimate with no error bar.

`BENCHMARK-METHODOLOGY.md` §6.6 acknowledges *"No replication. Each benchmark is run once."* The skill uses WebSearch (live-varying) and stochastic LLM sampling (no pinned temperature, §2.6 of methodology), so run-to-run variance is plausibly large but unknown. Differences between iterations 10/12/13/14 that are smaller than this unknown noise floor are not measurable.

**Suggestion:** run each benchmark 3x on the current skill version, report mean and spread per metric, and treat anything inside one standard deviation as "no change." This is the highest-leverage fix because every other comparison ride on top of it.

### A4. Training-data contamination is plausible and not measured — *measured 2026-05-11; finding is large*

`audit.md` §1 *"Answerable from memory"*: tasks about real, named entities can be answered from a model's parametric memory even though the intent is to test a skill.

Every reference is Simon Wardley's own public work, published on GitHub since 2018+, indexed by date and topic. A 2026-trained model has plausibly seen many of these maps as raw text. We have no current way to tell whether the skill's coverage on, say, `ai-trust` reflects scenario→map reasoning or recall of the `wardley-reference.owm` content from pre-training.

`BENCHMARK-METHODOLOGY.md` §6.3 acknowledges adjacent ("Time-pinning is imperfect") but does not name training contamination.

**Suggestion:** establish a memory baseline. Pick 2-3 reference maps and feed the *scenario prompt only* (no skill, no references, no instructions) to a base model. If the base model already names half of Wardley's components, the benchmark is partly measuring memorisation.

### A5. The harness has never been run on known-good or known-bad inputs — *measured 2026-05-11; found three real bugs*

`audit.md` §2 *"Harness tested on known-good and known-bad"*: the harness should be run on (a) something that *should* score near 100% and (b) something that *should* score near chance.

`compare_all_25.py` has not been exercised on either oracle. We do not currently know:
- what the metric outputs if the subagent's output *is* the reference file (the oracle case),
- what the metric outputs if components and placements are randomised (the null case).

If the oracle doesn't approach 100% on every metric, `parse_owm` or `fuzzy_match` has a bug. If random doesn't fall close to expected chance, the metric is too lenient.

**Suggestion:** add `test_harness_oracle.py` that runs `compare_all_25.py` on (a) `output = reference` and (b) `output = randomised reference` and asserts oracle > 0.95 on coverage and randomised < expected chance.

### A6. Token, cost, and latency exist per-run but never make it into the report — *addressed (tokens/duration) 2026-05-11*

`audit.md` §3 *"Metrics reported alongside quality"*: pass rate, cost per success, and latency must appear side-by-side.

`BENCHMARK-METHODOLOGY.md` §7.5 says `total_tokens` and `duration_ms` are saved to `timing.json` per run. `compare_all_25.py` never reads those files. `BENCHMARK-REPORT.md` and `benchmark-25-summary.json` have no cost or latency columns.

That means we cannot today answer "is iteration-14 worth its tokens vs. iteration-10" or "would Haiku produce 80%-as-good maps at 20% the cost." The data is already on disk; only the aggregator is missing.

**Suggestion:** thread `timing.json` through `compare_all_25.py` and emit per-map `tokens_used`, `duration_s`, plus aggregate `tokens_per_map_p50`. This is the prerequisite for the model-sweep work in `sweep.md`.

### A7. Prompt-grader misalignment

`audit.md` §4 *"Prompt-grader agreement"*: what the prompt asks for must be what the grader rewards.

The scenario prompts ask the skill for (per `BENCHMARK-METHODOLOGY.md` §2(c)): components + dependencies + visibility + evolution + deep placement + strategic analysis + named gameplays + doctrine + climatic patterns + caveat. The grader scores: component name overlap, same-band agreement, |Δε|, |Δν|.

Dependencies, deep-placement quality, strategic analysis, gameplays, doctrine, and climatic-pattern application are entirely unmeasured (`BENCHMARK-METHODOLOGY.md` §5 acknowledges this for items 1-4). An iteration that improves any of those axes without improving placement shows as flat in the report.

**Suggestion:** add at least one grader for dependency-graph shape (e.g. shape-matching on the directed graph after fuzzy-aligning nodes). The LLM-judge layer discussed in the cwc-workshops review would cover the prose axes.

---

## Severity B findings (noise / generality)

### B1. Class imbalance across domains — *addressed 2026-05-11*

`audit.md` §1 *"Class balance"*. The 25-map corpus spans 18 domains; most domains have one map, a few (Defence, Energy, Government, Personal, Telecoms, Transportation) have two. Domain-level aggregates are not reliable; the headline averages over-weight whichever domain happens to score high.

The report does not currently publish per-domain numbers. Adding them would surface the imbalance without claiming false precision.

### B2. No inversion smoke test across iterations — *measured 2026-05-11; 12 inversions found*

`audit.md` §1 *"Inverted items as a smoke test"*: items where a clearly weaker system outscores a clearly stronger one are usually grader bugs, not capability inversions.

We have iterations 10, 11, 12, 13, 14 in the workspace. If any map's coverage / |Δε| got *worse* from iter-10 → iter-14, that pair is a candidate for a grader bug or a brittle scenario prompt. The audit script is one-liner-able once timing/status is in place.

### B3. Fuzzy matcher threshold is a single point estimate — *measured 2026-05-11; finding promoted*

`audit.md` §4 *"Not overly rigid / not too lenient"*. The 0.55 similarity threshold in `compare.py` is documented as a judgment call (`BENCHMARK-METHODOLOGY.md` §3.2) but no sensitivity analysis is published. Reported coverage and |Δε| could meaningfully change at threshold 0.50 or 0.60.

**Suggestion:** include a small table in `BENCHMARK-REPORT.md` showing how headline numbers move when the threshold sweeps over {0.45, 0.55, 0.65}. If they barely move, the threshold is robust; if they jump, the headline number needs a confidence interval.

### B4. No human baseline

`audit.md` §1 *"Human baseline"*. Nobody has measured what a trained Wardley mapper scores against Wardley's own published maps for the same scenario. Without that anchor, "62% coverage" is hard to calibrate — it could be near-ceiling or mediocre.

A cheap version: re-have Wardley's own map for an adjacent topic graded against the topic-of-interest's reference, with the matched components manually verified. Even one such anchor is informative.

### B5. Temperature and sampling parameters are not pinned

`audit.md` §2 *"Deterministic setup"*. The subagent inherits whatever sampling settings the parent harness uses; `BENCHMARK-METHODOLOGY.md` §10.3 names this as a known irreproducibility. Pinning temperature in the subagent spawn (where possible) tightens the trial-to-trial spread before adding more trials (see A3).

### B6. Spot-check rate of grader errors is not published

`audit.md` §4 *"Spot-check the failures"*. The matches list is printed by `compare_all_25.py` but the *fraction* of matches that on inspection are loose / wrong is not tracked across the benchmark. `BENCHMARK-METHODOLOGY.md` §3.2 names two known false-positive patterns but no rate.

A documented rate (e.g. "5/358 matches manually reviewed as loose") makes B3 quantitative.

---

## Sections where the methodology is in good shape

Per `audit.md` §5: *"An audit that finds nothing wrong is a valid and useful result. If a section of the eval is in good shape, say so plainly."*

- **Per-task trajectories are saved.** `output.md`, `draft.owm`, `timing.json`, and (some) `grading.json` are all kept (`BENCHMARK-METHODOLOGY.md` §9). This is the single highest-leverage habit for debuggability per `audit.md` §2.
- **Reproducible aggregation.** The comparison is pure Python on committed artefacts (`BENCHMARK-METHODOLOGY.md` §8). Re-running the aggregator costs nothing.
- **Self-aware methodology document.** §6 (Known limitations) and §11 (How to critique these numbers) already acknowledge several of the issues above and invite scrutiny. That framing is exactly what `audit.md` §5 recommends.
- **Noise-floor calculation is principled.** §4 derives |Δε| ≈ 0.10 from the cheat-sheet scoring sensitivity, and the report cites this when interpreting numbers. Most evals do not have an equivalent.
- **Boundary-aware metrics.** The "near-boundary miss" metric (§3.6) explicitly catches strict-band failures that are close placements, avoiding the binary-band trap.

---

## Prioritised next steps

If only one item from each severity were actioned, the highest leverage are:

1. **A2 + A6** (combined): wire `timing.json` and a per-run `status` field into `compare_all_25.py`. Unblocks A3, B2, and the model-sweep work.
2. **A3**: 3 trials per map on the current skill version, report spread. Single biggest gain in interpretability.
3. **A4**: one memory-baseline run to find out whether we are partly measuring training-data recall.
4. **B3**: fuzzy-threshold sensitivity row in the report. Cheap.

These four together would move the benchmark from "informative point estimates with caveats" to "calibrated estimates with measurable noise floor."

---

## Provenance

- Audit checklist: `anthropics/cwc-workshops/rightmodel/.claude/skills/eval-audit-and-sweep/references/audit.md` @ main, Apache-2.0.
- Files audited: `skills/wardley-map-workspace/BENCHMARK-METHODOLOGY.md`, `skills/wardley-map-workspace/compare_all_25.py`, `skills/wardley-map-workspace/benchmark-25-summary.json`.
- Audit date: 2026-05-11.

## Update log

- **2026-05-11 — A2 + A6 (partly).** Threaded `timing.json` and a per-map `status` field through `compare_all_25.py`. Reported numbers unchanged. New `status_counts` block surfaces that 1/25 maps (ai-trust) has no timing — a real data gap previously invisible. Timing aggregates: p50 73K tokens / 313s; max 106K / 602s; total ~1.77M tokens / ~2h17m across 24 maps. `infra_error` and `validator_unconverged` statuses still require runtime instrumentation (deferred). Cost columns deferred until we record input/output token split.

- **2026-05-11 — A3 multi-trial harness + smoke test.** Reworked `compare_all_25.py` to glob all `with_skill/run-*/` per map, run `stats()` per trial, and aggregate mean + sample stdev across trials. New columns: `N` (trial count), `±σ` (|Δε| stdev). Backward compatible — n=1 maps show stdev=0 and identical numbers. Smoke-tested with 2 maps × 2 fresh trials (4 parallel subagent spawns, ~302K tokens, ~11 min wall-clock). Findings on within-map variance:

  | Map | n | coverage σ | \|Δε\| σ | same-band σ | tokens σ |
  |---|---|---|---|---|---|
  | politics-labour | 3 | 0.0 pp | 0.036 | **16.7 pp** | 18,154 |
  | transport-demand | 3 | 5.6 pp | 0.016 | 6.0 pp | 4,866 |

  - **σ(\|Δε\|) is small** — 0.016 to 0.036, well within the §4 noise floor of 0.10. The placement metric is reasonably stable per map.
  - **σ(same-band) is brittle** — politics-labour swung 33% → 17% → 0% across three trials. The binary band-membership metric is the noisiest in the report; differences <15pp between iterations are likely within noise.
  - **Coverage is more stable than expected** — politics-labour matched the same 6 reference components in all 3 trials despite different map shapes; transport-demand σ=5.6pp.
  - **One trial produced a much bigger map** — transport-demand run-3 = 118 components (vs 52/54 in runs 1-2) but matched fewer reference components. The skill has path-dependent verbosity worth investigating, but not via the variance harness.
  - **Caveat on token deltas**: smoke-test prompts may differ from the originals — run-1 tokens were 50K (politics-labour) and 63K (transport-demand), runs 2-3 were 80K+ and 67-73K. Variance estimates here are conservative (likely an upper bound).

  Full sweep cost-projection: 50 more runs (25 maps × 2 fresh trials each) ≈ 3.6M tokens / ~5h wall-clock if launched in parallel batches.

- **2026-05-11 — A4 memory baseline (n=2).** Spawned 2 subagents with the same scenario but *no skill*, *no WebSearch*, *no file reads*. They had ~18K tokens / ~30s each (4× cheaper, 10× faster than skill runs). Compared their component output to Wardley's reference using the existing fuzzy matcher.

  | Map | Skill cov | Memory cov | Skill lift |
  |---|---|---|---|
  | ai-trust (high-profile) | 62% | **54%** | +8pp |
  | culture-gender (less-discussed) | 19% | **22%** | **−3pp** |

  - **ai-trust shows large training-data overlap.** A bare model with no skill recovers 20/37 of Wardley's reference components — including very Wardley-specific vocabulary (`constitution`, `Feedback Loop`, `Forensics`, `Benchmarks`, `Bias`, `DATA`). The skill's marginal lift is ~8pp of coverage on this map. The headline 62% is partly measuring memorisation / convergent reasoning, not the skill.
  - **culture-gender shows the inverse pattern.** Memory baseline gets 22% (slightly *more* than the skill's 19%), but on entirely generic vocabulary (`identity`, `lived experience`, `self`) — no evidence of Wardley-specific recall. The map is genuinely hard for both bare model and skill; the skill adds no measurable lift.
  - **Strategic takeaway:** "skill lift over memory baseline" is a more honest headline than raw coverage. For widely-discussed Wardley topics it's smaller than raw coverage suggests; for niche topics, the skill may not be adding value at all and should be examined for what specifically is failing.
  - **Caveats:** n=2 is too few to generalise. The fuzzy matcher has known false positives that affect both columns equally — see B6. Cannot fully distinguish "memorised the reference" from "any thoughtful mapper would name this" without inspecting matched-pair quality manually.

  Follow-up worth running: expand memory baseline to 5-7 maps spanning high/medium/low public profile, and add `skill_lift_over_memory` as a column in `BENCHMARK-REPORT.md`. Cost: ~150K tokens / ~5 min for 5 more memory runs.

- **2026-05-11 — A4 expanded (n=7).** 5 more memory baselines in parallel (~90K tok / ~30s). Profile-aware view:

  | Map | Profile | Skill cov | Memory cov | Lift | Skill \|Δε\| | Memory \|Δε\| |
  |---|---|---|---|---|---|---|
  | ai-trust | high | 62% | 54% | +8pp | 0.153 | 0.258 |
  | healthcare-clinical | med-high | 60% | 60% | **0pp** | 0.179 | 0.157 |
  | finance-risk | med-high | 55% | 60% | **−5pp** | 0.162 | 0.159 |
  | cybersecurity | med | 58% | 42% | **+16pp** | 0.208 | 0.139 |
  | construction-supply | low | 35% | 38% | −3pp | 0.149 | 0.120 |
  | telecoms-sovereignty | low | 24% | 22% | +2pp | 0.142 | 0.188 |
  | culture-gender | low | 19% | 22% | −3pp | 0.168 | 0.090 |

  - **The skill's coverage advantage is map-dependent and frequently zero.** Mean skill lift across the 7 maps is +2.3pp (range −5 to +16). On 4 of 7 maps the skill's coverage is within ±5pp of a bare model with no skill, no WebSearch, and no references.
  - **The headline 37% benchmark coverage substantially reflects topical knowledge, not skill output.** A model that has seen the AI / healthcare / finance / cybersecurity literature can produce a recognisable "AI trust map" or "clinical decision-making map" without any of the skill's apparatus.
  - **|Δε| is comparable or better on the memory baseline for 5 of 7 maps.** Caveat: the matched-pair sets differ between skill and memory-baseline columns, so the comparison is apples-to-oranges — but the rough comparability suggests cheat-sheet placement isn't dramatically more accurate than parametric priors.
  - **Where the skill *does* lift**: cybersecurity (+16pp) is the clear outlier. Worth investigating whether deep-placement WebSearch on vendor landscape is doing the work, and whether the skill could be made smaller without losing this.
  - **What the skill almost certainly still contributes** (not measured by the benchmark): the strategic-analysis prose, named gameplays, doctrine references, climatic-pattern callouts, validator-enforced visibility constraints, dependency-graph structure. The current benchmark scores none of these.

  Updated strategic takeaway: the skill should be re-evaluated against a stronger baseline (memory-only) for *every map*, not just on coverage but on what kind of strategic output it produces. The next step the audit suggests is an LLM-judge layer that scores strategic-analysis quality (per the cwc-workshops `eval-driven` two-layer pattern), since that's where the skill's value most plausibly lives.

- **2026-05-11 — B3 fuzzy-threshold sensitivity.** Swept the matcher threshold across {0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70} on the run-1 corpus and aggregated each headline metric. Result is bigger than expected and promotes B3 from "noise" to a real finding:

  | τ | matches | coverage | \|Δε\| | same-band | ≤0.20 |
  |---|---|---|---|---|---|
  | 0.40 | 769 | 78% | 0.227 | 34% | 57% |
  | 0.45 | 598 | 61% | 0.226 | 34% | 58% |
  | 0.50 | 474 | 48% | 0.229 | 36% | 59% |
  | **0.55 (default)** | **358** | **36%** | **0.186** | **37%** | **61%** |
  | 0.60 | 298 | 30% | 0.185 | 36% | 62% |
  | 0.65 | 259 | 26% | 0.183 | 35% | 63% |
  | 0.70 | 241 | 24% | 0.183 | 35% | 63% |

  - **Coverage is highly threshold-sensitive.** Core-range spread (τ ∈ {0.45, 0.55, 0.65}) is **34.5pp** — the headline "37% coverage" could plausibly be reported as 30% or 61% by moving the matcher knob ±0.10. The headline coverage number is not a property of the skill, it is partly a property of the matcher.
  - **|Δε| is comparable for τ ≥ 0.55 but jumps at τ ≤ 0.50.** Going from τ=0.55 → 0.45 adds 240 matched pairs and lifts |Δε| from 0.186 to 0.226. The 240 added pairs have implied mean |Δε| ≈ 0.286 — much worse than the tight-match population. This is direct evidence of false-positive matches with loose thresholds.
  - **Same-band agreement and ≤0.20 ("strategic tolerance") are stable.** Spread <5pp across the core range. These metrics are robust to the matcher.
  - **The 0.55 default is the right transition point** — it's where loose-match noise stops contaminating |Δε|. Tighter thresholds (0.60-0.70) don't materially improve |Δε| but lose ~10pp of coverage.

  **Strategic implication**: the report's strategic-tolerance metric ("61% within ≤0.20", "37% same-band") is robust. The coverage metric is brittle and should never be cited as a precise number — only as a range or alongside the threshold value.

- **2026-05-11 — A5 oracle + null harness check.** Ran `test_harness_oracle.py`: oracle feeds each reference as its own output; null randomises placements on the same component names with 5 seeds.

  **Null test passes (sanity-checks the metric machinery):** pooled |Δε|=0.333 (expected 0.333 for uniform random), same-band 23%±3.4pp (≈25% chance, 4 equal bands), coverage 100% on names ✓.

  **Oracle test surfaced two real grader bugs:**

  | Issue | Affected | Worst case |
  |---|---|---|
  | `fuzzy_match`: first substring match short-circuits the exact-match scan | 23/25 maps | energy-storage \|Δε\|=0.055, same-band 77% on identical input |
  | `parse_owm`: regex matches a label's `[N, M]` integer coords when component has single-coord `[v]` form | culture-gender | `family [0.78] label [15, 18]` parsed as v=15, e=18 |

  Concrete demonstrations:
  - `fuzzy_match("Apple", ["Pineapple", "Apple"])` returns `("Pineapple", 0.9)` because the iteration loop hits `"apple" in "pineapple"` and short-circuits before reaching the exact match. This routes correct components to wrong-named neighbours when reference and output share prefixes/suffixes.
  - `parse_owm` on `component family [0.78] label [15, 18]` returns `{"family [0.78] label": (15.0, 18.0)}` — the regex requires two numbers separated by a comma, skips the single-coord bracket, and grabs the label bracket instead. Culture-gender ref has 27 components, 2 of which are silently miscoded out of `[0,1]`.

  **Implications for headline numbers:**
  - Oracle drift on |Δε| is bounded — 23 maps with non-zero |Δε| sum to a mean of ~0.015. The headline |Δε|=0.186 is therefore about 8% inflated by matcher misrouting. Real |Δε| is probably ~0.171.
  - Oracle drift on same-band averages ~95% across 25 maps — so the headline 37% same-band might be ~2pp low on average from matcher misrouting.
  - Coverage is unaffected by bug #1 (substring matches still match, just to the wrong target). Coverage *would* be affected by bug #2 if a reference's parser-corrupted components also occur in the output and don't get matched.

  **Recommendation deferred:** patch `fuzzy_match` to do a full pass scoring all candidates and return the max, *not* short-circuit on first substring hit. Patch `parse_owm` to either accept single-coord components (with a default ε) or skip them with a warning. Both are small code changes but they *will* shift every headline number in `BENCHMARK-REPORT.md`, so the patch should be paired with a full re-aggregation and a "v3" report addendum. Tracked as a follow-up.

- **2026-05-11 — B1 per-domain breakdown.** Added per-domain aggregation to `compare_all_25.py` and to `BENCHMARK-REPORT.md` §4.7. 19 domains across 25 maps; 14 domains have n=1. Coverage range across domains: 19% (Culture) to 62% (AI), a 43pp spread. High-coverage domains (AI 62%, Healthcare 60%, Cybersecurity 58%, Finance 55%) are exactly the high-public-discussion domains identified in A4 — providing independent evidence that domain effects dominate at the headline level. Low-coverage domains (Culture 19%, Politics 22%, Sustainability 26%) are niche/contested topics. Per-domain numbers at n=1 are point estimates and should be read as descriptive, not statistical.

- **2026-05-11 — B2 inversion smoke test.** Scanned iter-10..16 for maps with outputs in 2+ iterations (22 maps qualified, mostly via the iter-15 v3-rerun corpus). Flagged inversions where a *later* iteration scored materially worse than an *earlier* one on the same map: coverage drop >5pp or |Δε| increase >0.04. **Found 12 inversions across the 22 multi-iteration maps**, several past the A3 noise floor (2σ ≈ 11pp on coverage):

  | Map | Earlier | Later | Metric | Δ |
  |---|---|---|---|---|
  | gaming-economies | iter-12 | iter-15 | coverage | **−18pp** |
  | manufacturing | iter-15 | iter-16 | coverage | −11pp |
  | agriculture-regen | iter-12 | iter-15 | coverage | −10pp |
  | government-sovereignty | iter-14 | iter-15 | coverage | −9pp |
  | retail-journey | iter-10 | iter-11 | coverage | −7pp |
  | telecoms-sovereignty | iter-14 | iter-15 | \|Δε\| | +0.062 |
  | energy-storage | iter-15 | iter-16 | \|Δε\| | +0.056 |
  | defence-grey-zone | iter-15 | iter-16 | \|Δε\| | +0.055 |
  | defence-grey-zone | iter-14 | iter-16 | \|Δε\| | +0.052 |
  | cybersecurity-risk | iter-12 | iter-13 | \|Δε\| | +0.047 |
  | retail-journey | iter-10 | iter-15 | \|Δε\| | +0.040 |
  | agriculture-regen | iter-12 | iter-16 | coverage | −8pp |

  Per `audit.md` §1, inversions are usually grader bugs or run-to-run noise rather than real capability inversions. The most plausible candidates:
  - **gaming-economies −18pp is anomalously large.** Worth a manual diff of iter-12 vs iter-15 outputs to confirm whether the iter-15 skill produced genuinely different component names or whether something else changed (scenario prompt revision? matcher routing the same components differently due to the A5 fuzzy_match bug?).
  - **The cluster of |Δε| inversions in iter-15/iter-16** suggests the layout-check step added in iter-16 (per BENCHMARK-REPORT.md §10) may have moved components in ways that shifted ε slightly — small per-component but visible in aggregate.
  - **Caveat from A5**: the buggy `fuzzy_match` could route the same conceptual component differently across iterations if the surrounding output components changed, producing apparent inversions that are really matcher noise. The inversion list should be re-run after the matcher patch.

  Artefact: `inversions-summary.json`.
