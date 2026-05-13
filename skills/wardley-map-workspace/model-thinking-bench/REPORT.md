# Model × thinking benchmark — `ai-trust`

**Pilot run.** 1 scenario, 3 models, 2 thinking states, 3 replicates per cell = 18 runs.

Closes the model/thinking gap flagged in [BENCHMARK-AUDIT.md](../BENCHMARK-AUDIT.md) §B5 — sampling parameters and model choice were never varied in the original 25-map benchmark. Here we hold the scenario fixed and vary model + thinking.

---

## 1. What was tested

| Axis | Values |
|---|---|
| Model | `claude-opus-4-7`, `claude-sonnet-4-6`, `claude-haiku-4-5-20251001` |
| Thinking | off; on (Opus 4.7 → `thinking.type.adaptive`, `output_config.effort=high`; Sonnet/Haiku → `thinking.type.enabled`, `budget_tokens=10000`, `interleaved-thinking-2025-05-14` beta) |
| Replicates | 3 per cell |
| Scenario | `ai-trust` — June 2023 AI trust landscape (matches `BENCHMARK-REPORT.md` row 1) |
| Reference | `iteration-10/eval-ai-trust/wardley-reference.owm` (3 anchors, 34 components) |

**Harness:** Anthropic SDK directly, bypassing Claude Code's subagent layer (which doesn't expose `thinking_budget` or `effort`). Full `wardley-map` skill (`SKILL.md` + `references/`, 118k chars) inlined as a cached system prompt. `bash` (local, sandboxed with the validator script) and `web_search` (Anthropic server-side, max 8 calls) tools provided. Streaming enabled (required by the SDK at `max_tokens ≥ 32k`). Each cell saves `outputs/output.md` + `timing.json` with full usage and per-turn stop reasons.

**Total cost:** ~$44 (Opus $36, Sonnet $7, Haiku $2). 12.5M cache reads vs 1.4M raw input ≈ 90% cache hit ratio.

---

## 2. Results

| model | thinking | n | valid% | comps | coverage | same-band | \|Δε\| | \|Δν\| | ν-bias | ε-bias | dur(s) | turns |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| haiku-4-5 | off | 3 | 100% | 36.0 | 33.3% | 26.7% | 0.223 | 0.332 | +0.229 | +0.043 | 179 | 10.7 |
| haiku-4-5 | on | 3 | 100% | 37.7 | 38.2% | 34.8% | 0.200 | 0.307 | +0.225 | +0.089 | 224 | 11.0 |
| opus-4-7 | off | 3 | 100% | **43.7** | **47.1%** | 31.6% | **0.185** | 0.220 | +0.223 | −0.016 | 225 | 12.0 |
| opus-4-7 | on | 3 | 100% | 42.0 | **48.0%** | 34.8% | **0.177** | 0.233 | +0.244 | +0.052 | 291 | 7.0 |
| sonnet-4-6 | off | 3 | 67% | 22.7 | 41.2% | **35.7%** | 0.190 | **0.165** | **+0.115** | −0.044 | 261 | 12.7 |
| sonnet-4-6 | on | 3 | 100% | 36.0 | 45.1% | 34.8% | 0.200 | 0.275 | +0.241 | −0.056 | 518 | 6.3 |

- **valid%** = validator pass rate (clean exit from `node scripts/validate_owm.mjs`).
- **coverage** = fraction of Wardley's 34 reference components fuzzy-matched (threshold 0.55).
- **same-band** = of matched components, % in the same evolution band (Genesis/Custom/Product/Commodity).
- **|Δε|, |Δν|** = median absolute placement deltas on matched components.
- **ν-bias, ε-bias** = mean signed delta (ours − Wardley); positive = over-place. ν-bias matches the +0.02 to +0.06 pattern in `COMPETITOR-BENCHMARK-REPORT.md` §3.3 ("all generators over-place visibility").

---

## 3. Findings

### 3.1 Model dominates over thinking on coverage and tight ε

Opus 4.7 leads on coverage (47-48%) and \|Δε\| (~0.18) regardless of thinking state. The Opus thinking-on lift over Opus thinking-off is **+0.9pp coverage** — well inside the run-to-run noise floor (`coverage_stdev` ≈ 0.017-0.029 per cell). Thinking pays for itself on smaller models more than on Opus.

| | coverage lift from thinking | \|Δε\| lift from thinking |
|---|---|---|
| Haiku | +4.9pp | −0.023 |
| Sonnet | +3.9pp | +0.010 (slight regression) |
| Opus | +0.9pp | −0.008 |

Reading: **thinking lifts Haiku toward Sonnet, lifts Sonnet's density but not its placement, and adds almost nothing for Opus.** The benchmark's prior single-model numbers (matching Sonnet/Opus range with thinking-inherited-from-harness, validator pass 100%) are consistent with the Opus/Sonnet-thinking-on row here.

### 3.2 Sonnet thinking-off is the weird cell

Sonnet without thinking produced only **22.7 components on average** (half of Opus) and **only 67% validator pass** (2/3 cells). But the components it does place have the **tightest |Δν| (0.165)** and **lowest ν-bias (+0.115)** of any cell in the matrix.

Interpretation: Sonnet without thinking is conservative — it stops early, produces a sparse map, gets some placements wrong enough to fail the validator, but the matched ones are well-placed. **Turning thinking on for Sonnet fixes density (22.7 → 36) and validator pass (67% → 100%) at the cost of doubling latency (261s → 518s) and regressing ν-bias to the same +0.24 over-place pattern every other cell shows.** Sonnet thinking-on is the slowest cell in the entire matrix.

### 3.3 Same-band % is structurally flat

All six conditions cluster between **26.7% and 35.7%** strict-band agreement. The model/thinking axes do not move this needle materially. This matches `BENCHMARK-REPORT.md` §3.2's finding that the residual placement disagreement is dominated by genuine ambiguity in Wardley's own scoring (cheat-sheet rows disagree on his maps too), not by model capability. **Placement agreement appears to be capped at ~35% same-band on this scenario regardless of which Claude is reasoning.**

### 3.4 Density matches Wardley on Opus only

Wardley's `ai-trust` has 34 components. Reproducing his density target:

| Cell | mean components | gap vs Wardley |
|---|---|---|
| Opus off / on | 43.7 / 42.0 | +9 to +10 |
| Sonnet on | 36.0 | +2 |
| Haiku off / on | 36.0 / 37.7 | +2 to +4 |
| Sonnet off | 22.7 | **−11** |

Only Sonnet-without-thinking under-produces. Every other cell hits or slightly overshoots Wardley's density. The over-shoot may inflate the headline coverage numbers because of false-positive matches — see §6.

### 3.5 ν over-placement is universal except Sonnet-off

Every cell except Sonnet thinking-off has ν-bias between **+0.22 and +0.24** — over-placing user-visibility by 22-24 percentage points on average. This is the same systematic bias `COMPETITOR-BENCHMARK-REPORT.md` §4 documented across `mathmodel`, `arc-kit`, `haberlah`, and `prompt-baseline`. **The bias is not eliminated by either bigger model or more thinking** — it appears to be a property of how LLMs interpret "user-visible" rather than scaffold or capability.

---

## 4. What this changes for the 25-map benchmark

1. **The headline `mathmodel v2` numbers in `COMPETITOR-BENCHMARK-REPORT.md` are roughly the Opus-thinking-inherited row here** — 47-48% coverage, \|Δε\| 0.18, density 42-43, validator 100%. Consistent.
2. **The audit's B5 concern (sampling not pinned) is real but bounded.** Across 3 reps per cell, `coverage_stdev` was 0.017-0.078 — i.e. ±1.7 to ±7.8 percentage points run-to-run on a single map. The 25-map benchmark's between-iteration deltas of 2-5pp are below this floor for individual maps; aggregate differences across 25 maps should average down, but per-map comparisons are noisier than the published tables imply.
3. **Smaller models are a viable cost/quality tradeoff for some axes.** Haiku-with-thinking gets 38% coverage at $0.32/cell vs Opus's 48% at ~$6/cell. For a thicker benchmark sweep where coverage trends matter more than the absolute headline, Haiku-on is 5-10× cheaper.

---

## 5. Caveats

- **N=1 scenario.** `ai-trust` is the highest-public-discussion map in the corpus; `BENCHMARK-AUDIT.md` A4 explicitly flagged training-data leakage for this map (bare model recovers 20/37 of Wardley's components without the skill). Effect sizes may be inflated and not transfer to lower-leakage maps like `agriculture-regen` or `culture-gender`.
- **N=3 replicates per cell.** Enough to compute a per-cell stdev; not enough to pin the matrix tightly. Run-to-run coverage spreads (0.017-0.078) are not negligible relative to between-condition deltas.
- **Web search is live.** Each replicate hits the live web; results vary. This contributes to the variance estimate above and is one reason between-cell deltas under ~5pp are not interpretable.
- **Opus 4.7 uses adaptive thinking, Sonnet/Haiku use enabled-with-budget.** The two thinking interfaces are not directly comparable — `effort=high` and `budget_tokens=10000` may not represent the same compute envelope. The "thinking lift" rows in §3.1 are within-model comparisons only, not cross-model.
- **Same-band % is computed on matched components only.** A cell that matched 12 components and placed them perfectly scores 100% same-band even though its coverage is poor. Pair coverage and same-band together when reading the table.
- **Validator pass is per-cell, not per-replicate within a cell.** The 67% on Sonnet thinking-off means 2 of 3 reps passed; the 33% that failed contributed broken OWM that may still have been parsed for the placement metrics.

---

## 6. Suggested follow-ups

1. **Repeat on a low-leakage scenario.** `agriculture-regen` or `culture-gender` — both flagged in the audit as below the median public-discussion profile. Repeating the matrix there would tell us whether Opus's coverage lead survives when training-data overlap is weaker.
2. **Cross-model placement-axis study.** Hold model fixed at Opus thinking-on, repeat on 5 maps × 3 reps = 15 cells. Tightens the per-map variance estimate, lets `BENCHMARK-AUDIT.md` A3 (replication gap) close cleanly.
3. **Validate Sonnet-thinking-off's tighter ν.** It's the only signal in this matrix where a smaller model genuinely outperforms Opus on a placement axis. If reproducible across maps, it would suggest the production skill should run Sonnet-no-thinking for visibility-placement and Opus for component density — i.e. a two-stage architecture.
4. **Cost-per-coverage frontier.** Plot $/cell vs coverage_mean: Haiku-on at $0.32 / 38% vs Opus-on at $6 / 48% is the obvious efficient point unless density matters.

---

## Reproduction

```sh
cd skills/wardley-map-workspace/model-thinking-bench
export ANTHROPIC_API_KEY=...
python3 run_bench.py                    # all 18 cells (resumable)
python3 run_bench.py --model=haiku      # filter
python3 aggregate.py                    # rebuild matrix_summary.{json,md} + cell_metrics.json
```

Artifacts: `cell_metrics.json` (per-cell raw metrics), `matrix_summary.json` (per-condition aggregates), `matrix_summary.md` (this table), `run_summary.json` (last run's pass/fail/skip), `outputs/eval-ai-trust/<model>/thinking-<state>/run-<n>/{outputs/output.md, timing.json}`.
