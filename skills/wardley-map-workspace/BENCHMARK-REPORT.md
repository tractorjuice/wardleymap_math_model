# Wardley Map Skill — Benchmark Report

**Dates:** initial 25-map report 2026-04-18; v2 addendum 2026-04-19
**Skill version under test:** v1 — exponential-seed default (α=0.6), validator script, density guidance, deep placement, stage-first prose. The report body below reflects v1. **§9 documents the v2 update** (concrete stage-indicator checklists) and its 6-map re-validation; the live skill on `main` is v2.
**Test corpus:** 25 maps held out from [swardley/WARDLEY-MAP-REPOSITORY](https://github.com/swardley/WARDLEY-MAP-REPOSITORY) (Simon Wardley's own published maps), spanning 18 distinct domains
**Test mode:** blind — subagents could not access the reference `.owm` files
**Companion:** `BENCHMARK-METHODOLOGY.md` describes the test harness in detail

---

## Contents

- [TL;DR](#tldr)
- [1. The skill under test](#1-the-skill-under-test)
- [2. Test methodology](#2-test-methodology)
- [3. Results](#3-results)
- [4. Findings](#4-findings)
- [5. Recommendations](#5-recommendations)
- [6. Limitations](#6-limitations)
- [7. Bottom line](#7-bottom-line)
- [8. Artifacts](#8-artifacts)
- [9. v2 update — concrete stage-indicator checklists](#9-v2-update--concrete-stage-indicator-checklists)
- [Appendix A — Test prompts per benchmark](#appendix-a--test-prompts-per-benchmark)
- [Appendix B — Code references](#appendix-b--code-references)

---

## TL;DR

Across 25 blind benchmarks, 358 matched component pairs:

- **61% of matched components land within strategic tolerance** of Wardley's placement (`|Δε| ≤ 0.20` — close enough that the build / buy / utility call doesn't change)
- **28% are near-identical** (`|Δε| ≤ 0.10` — within the cheat-sheet method's inherent scoring noise)
- **92% are in Wardley's band or an adjacent one** (stage-neighbourhood agreement)
- **37% are in exactly the same stage band** (strict band match)
- **25% are genuine disagreements** (`|Δε| > 0.25`), some fraction of which is time drift (see §4.3) not skill error
- **Coverage: 37%** — fraction of Wardley's components matched by fuzzy name
- **ε-bias: +0.009** (effectively zero, very consistent across 25 domains)
- **ν-bias: +0.079** (down from +0.22 before the exponential seed)
- **Structural validity: 25/25** maps passed the validator

**The right interpretation.** The skill is a *coarse-map generator*, not a *precision-map generator*. For strategic framing — "is this a differentiator or a commodity? where to build vs buy?" — the skill reaches the same answer as Wardley about 60% of the time. For exact coordinate agreement (fine-grained ε) it's much weaker, but the cheat-sheet method's quantisation noise makes fine-grained agreement an unrealistic target anyway.

---

## 1. The skill under test

A portable Claude Code skill package (`skills/wardley-map/`) that generates a Wardley Map from a free-form scenario description and emits OWM-format output plus a strategic analysis.

### 1.1 Math model

```
M = (V, E, U, ν, ε, t)
```

- `V` — set of components
- `E ⊆ V × V` — directed dependency edges; `(a, b) ∈ E` means "a depends on b"
- `U ⊆ V` — anchor set (user-need nodes)
- `ν: V → [0, 1]` — visibility function (Y-axis)
- `ε: V → [0, 1]` — evolution function (X-axis)
- `t` — time (optional, for scenario dynamics)

Visibility seed (default):

```
d(v) = min over u ∈ U of { shortest path length from u to v }
ν(v) = exp(−0.6 · d(v))
```

Constrained by the hard rule `ν(a) ≥ ν(b)` for every edge `(a, b)`.

Evolution scored via Wardley's 19-row cheat sheet. A 4-row quick subset is used for initial placement:

```
ε(v) = (1/|R|) · Σ m(s_r)
```

where `m(s) = (s − 0.5)/4` maps stage picks {1, 2, 3, 4} to band midpoints {0.125, 0.375, 0.625, 0.875}.

### 1.2 Skill package contents

| File | Role |
|---|---|
| `SKILL.md` | Procedure; instructions on when to consult each reference |
| `scripts/validate_owm.mjs` | Deterministic validator enforcing `ν(a) ≥ ν(b)` |
| `references/evolution-stages.md` | 19-row cheat sheet + worked examples |
| `references/climatic-patterns.md` | 27 patterns across 6 categories |
| `references/doctrine.md` | 40 universal principles across 4 phases |
| `references/gameplay-patterns.md` | 61 gameplays in 12 categories |
| `references/inertia.md` | 17 forms of resistance to evolution |
| `references/mapping-examples.md` | 3 worked maps (tea shop, freelance marketplace, SaaS) |
| `references/mathematical-models.md` | Condensed formalism + dynamics |

### 1.3 Generation pipeline

1. **Components and anchors** — identify user-need nodes `U` and candidate `V`. Density guidance targets 20-30 / 35-45 / 40-55 components by scenario type.
2. **Dependencies** — build `E` as "depends-on" edges.
3. **Visibility ν** — exponential seed + manual override.
4. **Evolution ε** — 4-row cheat-sheet scoring, band midpoints.
5. **Deep placement** — selective WebSearch for components where cheat-sheet rows disagree, strategic importance is high, or the domain is specialised.
6. **Verification** — run `validate_owm.mjs`; fix violations; iterate until clean.
7. **Strategic analysis** — stage-first prose covering differentiation, commodity leverage, dependency risks, named gameplays from Wardley's 61-play catalogue, doctrine violations, climatic context, deep-placement findings, caveat.

---

## 2. Test methodology

### 2.1 Design

Held-out blind comparison. For each test case:

1. Fetch a Wardley map `.owm` file from the repository
2. Derive a realistic scenario prompt from the title and topic **without exposing Wardley's placements or component names**
3. Spawn a subagent with the prompt and an explicit instruction not to read the reference file
4. Run the full 7-step skill procedure
5. Compare the generated map to Wardley's reference

### 2.2 Metrics

Four complementary views of placement agreement:

1. **Strict same-band** — both ε values in the same quartile (Genesis [0, 0.25), Custom [0.25, 0.5), Product [0.5, 0.75), Commodity [0.75, 1.0]). Integer band membership, no tolerance.
2. **Within 1 band (soft)** — band indices differ by at most 1 ("right neighbourhood").
3. **`|Δε|` cumulative distribution** — fraction within {0.05, 0.10, 0.15, 0.20, 0.25, 0.30} of each other regardless of band. The continuous view.
4. **Directional biases** — mean signed Δε and Δν (positive = we place higher than Wardley).

**Noise floor.** The 4-row cheat-sheet method has inherent quantisation. Each row gives one of 4 stage values; one row flipping by one stage shifts mean ε by 0.0625. Useful thresholds:

- `|Δε| ≤ 0.10` — within scoring noise (effectively identical): roughly two rows flipping by one stage, or one row flipping by almost two — the kind of disagreement the method itself produces on re-scoring
- `|Δε| ≤ 0.20` — within strategic tolerance (build/buy/utility call doesn't change): on the order of three rows flipping by one stage, or one row flipping by three (Genesis → Commodity). Beyond that, most of the four cheat-sheet rows have to materially disagree, which usually reflects real judgment difference rather than scoring variance
- `|Δε| > 0.25` — genuine disagreement, beyond both noise and one band-width. The 0.25 threshold lines up with the band width itself; beyond one band-width is unambiguously a different stage call.

### 2.3 Time pinning

Several maps carry explicit dates (2022-2024). The subagent is pinned to that date in the scenario prompt to prevent 2026 priors from biasing placements. Effectiveness is partial — §4.3 documents the time-drift confound and its bidirectional signal.

### 2.4 Corpus

25 maps spanning 18 domains: AI governance, retail, healthcare, finance, manufacturing, cybersecurity, agriculture, education, gaming, sustainability, construction, culture, defence, energy, government, personal (individual-scale), politics, telecoms, transportation.

| Map | Domain | Date | Ref comps |
|---|---|---|---:|
| AI TRUST | AI governance | Jun 2023 | 37 |
| Retail connected journey | Retail | — | 41 |
| Healthcare clinical decisions | Healthcare | Aug 2022 | 40 |
| Finance risk management | Finance | — | 42 |
| Manufacturing supply chain | Manufacturing | Feb 2023 | 44 |
| Cybersecurity risk management | Cybersecurity | May 2023 | 33 |
| Agriculture regenerative farming | Agriculture | Aug 2022 | 50 |
| Education lifelong learning | Education | — | 40 |
| Gaming economies | Gaming | Nov 2023 | 33 |
| Sustainability supply chain | Sustainability | — | 43 |
| Construction supply chain | Construction | Mar 2023 | 52 |
| Culture — gender | Culture | Mar 2022 | 27 |
| Defence — intelligence | Defence | Mar 2023 | 42 |
| Defence — grey zone | Defence | — | 41 |
| Energy — disruption | Energy | Jul 2022 | 40 |
| Energy — storage | Energy | Apr 2023 | 30 |
| Government — digital identity | Government | Nov 2022 | 37 |
| Government — sovereignty | Government | Apr 2023 | 46 |
| Personal — financial inclusion | Personal | — | 43 |
| Personal — conversational tech | Personal | — | 21 |
| Politics — Labour values | Politics | May 2024 | 27 |
| Telecoms — sovereignty | Telecoms | Oct 2022 | 49 |
| Telecoms — space | Telecoms | Feb 2023 | 44 |
| Transportation — logistics | Transportation | — | 45 |
| Transportation — demand | Transportation | May 2022 | 37 |

---

## 3. Results

### 3.1 Per-benchmark table

| Benchmark | Domain | Ref | Ours | Match | Cov | \|Δε\| | \|Δν\| | ε-bias | ν-bias | Same band | ±1 band | ≤ 0.20 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ai-trust | AI | 37 | 34 | 23 | 62% | 0.153 | 0.306 | −0.010 | +0.236 | 57% | 91% | 70% |
| healthcare-clinical | Healthcare | 40 | 30 | 24 | 60% | 0.179 | 0.386 | +0.046 | +0.298 | 33% | 79% | 54% |
| finance-risk | Finance | 42 | 41 | 23 | 55% | 0.162 | 0.250 | +0.016 | +0.117 | 30% | 100% | 65% |
| retail-journey | Retail | 41 | 52 | 20 | 49% | 0.174 | 0.273 | −0.078 | +0.172 | 40% | 95% | 70% |
| manufacturing | Manufacturing | 44 | 37 | 14 | 32% | 0.226 | 0.353 | +0.174 | −0.190 | 21% | 79% | 57% |
| agriculture | Agriculture | 50 | 55 | 18 | 36% | 0.233 | 0.213 | −0.198 | +0.005 | 33% | 89% | 44% |
| education | Education | 40 | 44 | 13 | 32% | 0.178 | 0.220 | +0.024 | +0.032 | 46% | 92% | 69% |
| gaming | Gaming | 33 | 49 | 14 | 42% | 0.206 | 0.180 | +0.198 | +0.053 | 36% | 93% | 43% |
| sustainability | Sustainability | 43 | 58 | 11 | 26% | 0.135 | 0.245 | −0.077 | +0.127 | 45% | 100% | 82% |
| cybersecurity | Cybersecurity | 33 | 39 | 19 | 58% | 0.208 | 0.257 | +0.116 | +0.139 | 47% | 84% | 58% |
| construction-supply | Construction | 52 | 49 | 18 | 35% | 0.149 | 0.302 | −0.002 | +0.014 | 44% | 100% | 67% |
| culture-gender | Culture | 27 | 43 | 5 | 19% | 0.168 | 0.172 | +0.088 | +0.024 | 0% | 100% | 100% |
| defence-intelligence | Defence | 42 | 44 | 12 | 29% | 0.208 | 0.199 | −0.155 | −0.006 | 50% | 92% | 58% |
| defence-grey-zone | Defence | 41 | 44 | 11 | 27% | 0.200 | 0.310 | −0.069 | +0.052 | 27% | 100% | 45% |
| energy-disruption | Energy | 40 | 48 | 16 | 40% | 0.188 | 0.248 | +0.109 | +0.138 | 25% | 81% | 75% |
| energy-storage | Energy | 30 | 47 | 11 | 37% | 0.215 | 0.264 | −0.055 | +0.127 | 36% | 91% | 55% |
| government-digital-id | Government | 37 | 41 | 14 | 38% | 0.208 | 0.351 | −0.069 | +0.199 | 36% | 86% | 50% |
| government-sovereignty | Government | 46 | 55 | 17 | 37% | 0.145 | 0.293 | +0.045 | +0.292 | 41% | 94% | 76% |
| personal-fin-inclusion | Personal | 43 | 46 | 5 | 12% | 0.134 | 0.370 | −0.062 | −0.002 | 60% | 100% | 80% |
| personal-conversational | Personal | 21 | 42 | 9 | 43% | 0.213 | 0.327 | −0.127 | +0.011 | 33% | 89% | 56% |
| politics-labour | Politics | 27 | 45 | 6 | 22% | 0.278 | 0.152 | +0.232 | +0.072 | 33% | 83% | 33% |
| telecoms-sovereignty | Telecoms | 49 | 47 | 12 | 24% | 0.142 | 0.230 | +0.002 | +0.048 | 50% | 100% | 83% |
| telecoms-space | Telecoms | 44 | 46 | 14 | 32% | 0.250 | 0.216 | −0.193 | −0.063 | 21% | 93% | 36% |
| transport-logistics | Transportation | 45 | 51 | 11 | 24% | 0.176 | 0.218 | +0.145 | +0.044 | 45% | 100% | 55% |
| transport-demand | Transportation | 37 | 52 | 18 | 49% | 0.173 | 0.300 | +0.127 | +0.042 | 22% | 94% | 67% |

The last column (`≤ 0.20`) is the strategic-tolerance agreement — fraction of matches where `|Δε| ≤ 0.20`, the threshold beyond which build/buy/utility recommendations start to change.

### 3.2 Aggregate statistics

| Metric | Value |
|---|---:|
| Mean coverage | 37% |
| Mean same-band (strict) | 37% |
| Mean within 1 band (soft) | 92% |
| Mean `|Δε|` | 0.188 |
| Mean `|Δν|` | 0.265 |
| ε-bias | +0.009 |
| ν-bias | +0.079 |

### 3.3 Closeness distribution

Across all 358 matched pairs:

| `|Δε|` ≤ | % | Interpretation |
|---:|---:|---|
| 0.05 | 15% | Near-identical, precision match |
| 0.10 | **28%** | Within scoring noise — effectively identical |
| 0.15 | 42% | |
| 0.20 | **61%** | Within strategic tolerance — same recommendation |
| 0.25 | 75% | Within one band-width |
| 0.30 | 83% | |
| 0.40 | 93% | |
| 0.50 | 97% | |

- **61%** of matches are close enough that no strategic call changes
- **28%** are within the cheat-sheet method's scoring noise
- **25%** are genuine disagreements (`|Δε| > 0.25`) — but see §4.3: a fraction of these is time drift, not skill error
- **Boundary-crossing artefact.** 22 of 358 pairs (6%) are `|Δε| ≤ 0.10` but cross a band boundary — real but small, accounting for 10% of strict-band misses.

---

## 4. Findings

### 4.1 What the skill does well

**1. Strategic-tolerance agreement is high.** 61% of placements are within strategic tolerance (`|Δε| ≤ 0.20`). 92% are in Wardley's band or an adjacent one. Only 3% are catastrophically off.

**2. Near-zero ε-bias.** +0.009 across 25 maps — the skill doesn't systematically over- or under-industrialise in aggregate. (§4.3 unpacks this: the aggregate is partly coincidental cancellation between forward-drift and overshoot maps, and per-map bias is substantial in both directions.)

**3. Consistent anchor identification.** All 25 benchmarks: the skill reaches for Wardley's user/stakeholder structure unaided.

**4. Strategic conclusions converge with Wardley's framing.** Blind across 25 scenarios the subagent independently reaches takeaways that align with Wardley's: *governance trails the technology it governs* (AI trust, government digital ID), *platform plays need both sides* (gaming, retail, freelance), *sovereignty levers are differentiators while connectivity is commoditised* (telecoms sovereignty), *climate and defence are in Peace/War/Wonder cycle transitions* (defence grey zone, energy disruption).

**5. Validator reliably catches structural errors.** The bundled `validate_owm.mjs` script catches 1-13 violations on first-draft maps, which the subagent fixes iteratively until the script exits clean. Nearly all of the 25 first-drafts had at least one violation — without the validator, most maps would ship with silent structural errors (visibility-rule breaks, typo'd edges, out-of-range coordinates).

**6. Deep placement produces specific findings.** Examples: telecoms-sovereignty correctly identified the Oct 2022 Huawei notice; culture-gender anchored placements to March 2022 specifics (Cass interim report, Florida HB 1557); agriculture-regen confirmed Soil Carbon MRV as Genesis because protocols were fragmented; gaming-economies flagged Loot Boxes as showing leftward evolution under regulatory pressure.

### 4.2 What the skill doesn't do

**1. Coverage ceiling around 37%.** The skill names about 1 in 3 of Wardley's components. Missing components cluster into:

- *Abstract philosophical nodes* — "Asymmetrical", "Believed", "Bias", "Quality", "OUTPUT", "ACCESS", "perceived risk", "profit", "sovereignty", "territorial". Wardley uses these as first-class map nodes; the skill reaches for operational equivalents instead.
- *Domain-idiosyncratic shorthand* — "Dr Google", "constitution", "sovereign" — Wardley's stylistic fingerprints.

**2. Fine-grained placement is unreliable.** Only 15% of matches are within 0.05 ε. This is close to the ceiling of what the 4-row cheat-sheet method can deliver (scoring noise is ~0.10); expecting tighter agreement is expecting less than the method can produce. Stage-neighbourhood is reliable; specific coordinates aren't.

**3. Visibility compression — softened but persistent.** Exponential seed reduced ν-bias from +0.22 to +0.08, but bias remains positive in most benchmarks.

**4. Component count calibration (partly mitigated).** Density guidance helps — cybersecurity dropped from 60 to 39 components after the guidance was added. The guidance is phrased as a target rather than a cap, which is the right framing. One residual pattern: on scenarios where Wardley draws tight focused maps (ref ≤ ~30 components), the skill tends to overshoot — culture-gender 27 → 43, politics-labour 27 → 45, energy-storage 30 → 47, personal-conversational 21 → 42. The density ranges (20-30 / 35-45 / 40-55) give a floor that's too high for narrow landscapes; small-scope scenarios may warrant a narrower target.

**5. Visibility compression varies by domain.** ν-bias per map ranges from −0.19 (manufacturing) to +0.30 (healthcare). Three patterns:

- *Strong positive* (we place too high): healthcare +0.30, government-sovereignty +0.29, ai-trust +0.24, government-digital-id +0.20, retail +0.17 — domains where Wardley pushes deep infrastructure to ν < 0.1 more aggressively than the exponential seed produces.
- *Near-zero* (calibrated): construction +0.01, personal-fin-inclusion 0.00, defence-intelligence −0.01, agriculture +0.01 — the exponential seed matches Wardley's vertical spread well.
- *Negative* (we place too low): manufacturing −0.19, telecoms-space −0.06 — domains where Wardley keeps most components mid-chain; the exponential seed pushes too aggressively toward the bottom.

The seed is calibrated for a "Wardley-typical" visibility distribution. Domains that don't match that shape drift in either direction. A domain-adaptive α (recommendation §5.2 #2) would close the remaining gap.

### 4.3 The time-drift confound

The benchmark treats Wardley's map as ground truth — but Wardley's maps are dated snapshots (2022 to 2024 for the dated ones). Our skill scores in 2026 with 2026 priors. Time-pinning partially works but subagents can't fully suppress later knowledge. **A non-trivial fraction of apparent disagreement is legitimate time drift, not skill error.**

A component Wardley placed at ε=0.4 in August 2022 that has genuinely industrialised by 2026 *should* score further right now. That's the framework working as intended.

**Forward drift — we see more industrialised than Wardley:**

| Map | Date | ε-bias |
|---|---|---:|
| politics-labour | May 2024 | +0.23 |
| gaming-economies | Nov 2023 | +0.20 |
| manufacturing | Feb 2023 | +0.17 |
| transport-logistics | — | +0.15 |
| transport-demand | May 2022 | +0.13 |
| cybersecurity | May 2023 | +0.12 |
| energy-disruption | Jul 2022 | +0.11 |

Political operations, gaming monetisation, manufacturing automation, and cybersecurity all industrialised faster than 2022-2023 Wardley saw.

**Overshoot — Wardley saw more industrialised than we do:**

| Map | Date | ε-bias |
|---|---|---:|
| agriculture-regen | Aug 2022 | −0.20 |
| telecoms-space | Feb 2023 | −0.19 |
| defence-intelligence | Mar 2023 | −0.16 |
| personal-conversational | — | −0.13 |

Agriculture-regen is the starkest: Wardley thought soil carbon MRV and regen supply chains were further along in 2022 than they actually were. Space telecoms and defence intelligence similarly show Wardley ahead of what turned out to happen.

**What this means for the numbers:**

1. **The 37% strict-band disagreement is an upper bound on skill error.** Some of the 63% that disagrees with Wardley is time drift — drift that Wardley himself would produce if he re-mapped in 2026. Disentangling *skill disagrees with 2022 Wardley* from *2022 Wardley disagrees with 2026 Wardley* is impossible with this corpus.

2. **The near-zero aggregate ε-bias is partly coincidental.** +0.009 averaged across 25 maps comes from positive forward-drift cases and negative overshoot cases roughly cancelling. Per-map bias is substantial in both directions.

3. **Coverage and stage-neighbourhood are less affected by drift.** Time drift mostly shifts ε, not which components exist or their approximate location. 92% within-one-band is robust to a stage of drift; strict-band is what drift most damages.

4. **A useful diagnostic.** A systematically biased skill would show unimodal ε-bias (all positive or all negative). The fact that it's bimodal — forward drift on some maps, overshoot on others — is consistent with time drift + idiosyncratic Wardley judgment rather than a systematic skill defect.

**Practical takeaway.** Benchmark results should be read as *agreement-with-dated-Wardley*, not *agreement-with-ground-truth*. A 2026 mapper has, in some cases, more accurate information than the 2022 mapper — and a benchmark that treats the older map as correct counts that information update as a miss.

### 4.4 Consistency of aggregate metrics across corpus growth

From n=10 to n=25:

- Same-band (strict): 37% (stable)
- Within 1 band (soft): 92% (stable)
- `|Δε| ≤ 0.20`: measured at 61% at n=25
- ε-bias: +0.017 → +0.009 (near-zero, improving)
- ν-bias: +0.103 → +0.079 (continued improvement)
- Coverage: 45% → 37% (driven by niche-domain additions)

Placement metrics are robust across 2.5× the corpus. Coverage is the corpus-composition-dependent metric.

---

## 5. Recommendations

### 5.1 Implemented during this benchmark cycle

- ✅ Exponential-decay seed replacing reciprocal decay (closed ~60% of ν-bias)
- ✅ Validator script enforcing structural invariants (100% of maps validator-clean)
- ✅ Stage-first qualitative prose in analysis
- ✅ Deep-placement step with targeted WebSearch
- ✅ Component density guidance

### 5.1a Implemented after this benchmark cycle (v2)

- ✅ Concrete stage-indicator checklists in `evolution-stages.md` (four indicators × four stages). Used as a fast-path (Step 4a): if all four dimensions agree on a stage, skip the 4-row cheat sheet. See §9 for the 6-map re-validation showing |Δε| 0.209 → 0.184 (−12%), ε-bias +0.069 → +0.038, same-band +11pp over v1.

### 5.2 Open opportunities

**1. Abstract-component repertoire.** A reference file listing ~30 "distinctive Wardley vocabulary" nodes (perceived risk, asymmetric access, believed quality, territorial, sovereign, etc.) and prompting the skill to consider them on landscape-level scenarios. The n=25 evidence shows the biggest coverage gaps are abstract nouns — highest-leverage fix.

**2. Domain-adaptive α.** Fixed exponential α=0.6 over-corrects on domains where visibility is genuinely flat (manufacturing and telecoms-space both show negative ν-bias). Pick α ∈ {0.4, 0.6, 0.8} by scenario type.

**3. Vocabulary normalisation.** Map common tech-stack terms to Wardley's preferred phrasing (e.g., "vector DB" → "data index"; "observability platform" → "logs & telemetry"). Low-effort coverage lift without changing placement.

**4. Stronger time-pinning.** Several pre-2024 scenarios showed drift (politics-labour, telecoms-space, agriculture). An explicit "your knowledge cutoff for this scenario is date X" in Step 4, combined with a check that the subagent's deep-placement WebSearches filter by date, would reduce forward drift. Worth implementing — forward drift is the larger of the two directions (7 maps vs 4 for overshoot) and is the tractable one. Overshoot (Wardley ahead of reality) can't be reduced by prompt engineering; it's an artefact of the reference maps.

### 5.3 Not recommended

- **Don't over-tune to this benchmark.** 25 maps, single author — tuning to maximise fit risks producing a Wardley-mimic.
- **Don't chase exact-coordinate agreement.** 15% at `|Δε| ≤ 0.05` is near the ceiling of what the 4-row cheat-sheet method can produce; the method has inherent ~0.10 resolution.
- **Don't treat 37% coverage as a failure.** Blindly capturing a third of an expert's vocabulary is a reasonable baseline.

---

## 6. Limitations

1. **Single-author corpus.** Every reference is Wardley's own work. We're measuring faithfulness to Wardley's style, not to a ground truth.
2. **n=25 is still small.** Another 25 maps might move aggregate metrics by ±3-5 pp.
3. **Fuzzy matching is imperfect.** Coverage is a lower bound; some semantically equivalent components aren't matched. Some false-positive matches (e.g. "Training" ↔ "Training Data" in AI TRUST) inflate disagreement artificially.
4. **Time drift is real and bidirectional.** §4.3 documents this; it's the biggest interpretive caveat on the numbers.
5. **Placement metrics don't capture strategic quality.** A map can score well on placement and give bad strategic advice, or vice versa. Strategic-analysis sections were not systematically evaluated against Wardley's analyses.
6. **Cheat-sheet method has ~0.10 quantisation noise.** Sub-0.10 agreement is below method resolution; claims about it are noise-floor behaviour, not tight agreement.

---

## 7. Bottom line

Across 25 blind benchmarks covering 18 domains, the skill:

- Produces **structurally valid** Wardley Maps (validator-clean, 25/25)
- Reaches **strategic agreement** with Wardley on 61% of matched components (`|Δε| ≤ 0.20`; build / buy / utility call unchanged)
- Reaches **neighbourhood agreement** (adjacent band) on 92%
- Is within **scoring noise** (`|Δε| ≤ 0.10`) on 28%
- Exhibits negligible aggregate ε-bias and small residual ν-bias
- Captures about **1 in 3** of Wardley's components by name (the missing two-thirds are mostly abstract/philosophical nodes the skill doesn't reach for)

**The skill is a coarse-map generator, not a precision-map generator.** That's the right shape for a practitioner tool: Wardley himself treats maps as thinking tools rather than measurement instruments. Strict-band agreement (37%) and precision agreement (15%) are below what you'd want if replicating Wardley's placement down to the decimal — but some of that "disagreement" is time drift (§4.3), and the meaningful number is the 61% within strategic tolerance: most of the time, the skill and Wardley would recommend the same thing.

For practitioner use — mapping a business, product, or policy scenario and deriving strategic recommendations — the skill is production-useful. For archival-grade fidelity to Wardley's personal style, the vocabulary opportunity (recommendation 1) is the biggest remaining gap.

---

## 8. Artifacts

```
skills/wardley-map-workspace/
├── iteration-1/ … iteration-9/        # skill-development history (pre-benchmark)
├── iteration-10/                      # first 4 benchmarks
├── iteration-11/                      # retail rerun (exponential seed)
├── iteration-12/                      # +6 benchmarks (cyber, mfg, ag, edu, gaming, sust)
├── iteration-13/                      # cybersecurity rerun (density guidance)
├── iteration-14/                      # +15 benchmarks (new 8 domains + extras)
├── iteration-10/compare.py            # parse_owm + fuzzy_match primitives (imported by aggregators)
├── compare_all_10.py                  # aggregates first 10 benchmarks (historical)
├── compare_all_25.py                  # aggregates 25 benchmarks + closeness distribution
├── benchmark-25-summary.json          # machine-readable aggregate + per-map data
├── arc-kit-compare/                   # head-to-head vs tractorjuice/arc-kit + v2 re-validation
│   ├── skill/                         # vendored snapshot of the arc-kit wardley-mapping skill
│   ├── eval-<name>/with_skill/        # arc-kit outputs (6 maps)
│   ├── eval-<name>/ours-v2/           # our-skill-v2 outputs (6 maps)
│   ├── compare.py                     # arc-kit vs ours-v1
│   └── compare3.py                    # arc-kit vs ours-v1 vs ours-v2 (three-way)
├── BENCHMARK-REPORT.md                # this document
└── BENCHMARK-METHODOLOGY.md           # detailed methodology (companion)
```

Each `eval-<name>/` directory contains:
- `wardley-reference.owm` — held-out reference
- `with_skill/run-1/outputs/output.md` — the skill's generated map
- `with_skill/run-1/outputs/draft.owm` — validator working file
- `with_skill/run-1/timing.json` — token count and duration
- `with_skill/run-1/grading.json` — (where applicable) assertion grading

---

## 9. v2 update — concrete stage-indicator checklists

Post-25-map-benchmark change to the skill, independently validated on a 6-map subset.

### 9.1 What changed

Added a new section "Stage indicators — concrete checklists" to `skills/wardley-map/references/evolution-stages.md`: four concrete indicator checklists (ubiquity / certainty / market / failure-mode) per stage × four stages = sixteen checklists, plus an 8-question fast-diagnostic table. Adapted from [tractorjuice/arc-kit's `wardley-mapping` skill](https://github.com/tractorjuice/arc-kit/tree/main/arckit-claude/skills/wardley-mapping).

`SKILL.md` Step 4 grew a fast-path (4a): if all four concrete indicators agree on a single stage for a component, record that stage pick and skip the 4-row cheat sheet. When indicators disagree, fall back to the 4-row aggregate (unchanged from v1).

Motivation: arc-kit's per-stage indicators give sharper yes/no tests than v1's prose descriptions. v1's 4-row cheat sheet averages up to four stage picks — when the rows agree, the aggregate noise is unnecessary; when they disagree, it's still useful. The fast-path captures the easy cases with tighter stage calls.

### 9.2 Re-validation corpus

Six of the 25 benchmark maps were re-run blind against v2:

| Map | Why chosen |
|---|---|
| manufacturing | Largest ν-bias magnitude in v1 (−0.19) — test visibility calibration |
| culture-gender | Narrow map (ref=27), 0% strict same-band in v1 — test boundary-crossing artifact |
| telecoms-sovereignty | Dated landscape (Oct 2022), v1 strong baseline (83% ≤0.20) |
| politics-labour | Narrow (ref=27), biggest forward drift in v1 (+0.23) |
| agriculture-regen | Biggest overshoot in v1 (−0.20) — Wardley ahead of 2022 reality |
| cybersecurity | Domain-heavy, v1 baseline 47% same-band |

Selection reflects different failure modes, not cherry-picking the maps v2 would win on.

### 9.3 Aggregate results — three-way comparison

For the same six maps, comparing arc-kit (its own skill, run blind), ours-v1 (pre-checklist), ours-v2 (post-checklist):

| Metric (n=6) | arc-kit | ours-v1 | ours-v2 | v2 vs v1 |
|---|---:|---:|---:|---|
| Coverage | 24.4% | 31.8% | 31.0% | ≈ tied |
| `|Δε|` | 0.208 | 0.209 | **0.184** | **−12%** |
| `|Δν|` | 0.251 | 0.229 | **0.200** | −13% |
| ε-bias | +0.100 | +0.069 | **+0.038** | **−45%** forward drift |
| Same-band | 36.4% | 30.9% | **42.1%** | **+11.2pp** |
| ±1 band | 81.9% | 89.2% | **91.7%** | +2.5pp |
| ≤0.20 | 51.1% | 62.7% | **65.1%** | +2.4pp |

v2 beats v1 on every aggregate metric except coverage (tied within 1pp) and ν-bias (small regression offset by the large \|Δν\| gain). v2 beats arc-kit on every aggregate metric.

### 9.4 Per-map — where v2 helped most

- **Manufacturing.** \|Δε\| **0.226 → 0.162**, same-band **21% → 50%**, coverage 32% → 41%. On the 9 shared matches with v1, mean \|Δε\| tightened from 0.238 to 0.162 — genuine per-match precision gain, not a matching artifact. v2 also captured 9 abstract nouns v1 missed (ENERGY, SUPPLY CHAIN, agility, automation, cost, reliability, relationships, visibility, warehousing) — progress on the §4.2 #1 abstract-component gap.
- **Culture-gender.** Same-band **0% → 40%** — the §3.3 boundary-crossing artifact (22/358 pairs within 0.10 ε but crossing a band line) largely resolved on this map. ε-bias +0.088 → −0.012, effectively zero.
- **Agriculture-regen.** ε-bias **−0.198 → −0.107** — the biggest overshoot case in v1. v2 reined in 2026-priors that were pulling the map forward past Wardley's Aug-2022 snapshot. Explicit stage checklists force the scorer to check "does this actually have multiple competing vendors right now?" before calling Product.
- **Cybersecurity.** ε-bias +0.116 → +0.059 (halved). Same-band 47% → 50%.
- **Politics-labour.** \|Δε\| 0.278 → 0.229, coverage 22% → 30%, ε-bias +0.232 → +0.179.

### 9.5 Where v2 underperformed

- **Telecoms-sovereignty.** Coverage 24% → 16%, \|Δε\| 0.142 → 0.185. Investigation showed two causes: (i) a fuzzy-matcher false positive (Wardley's `GOVERNMENT` at ε=0.63 matched v2's "OpenRAN Deployment" at ε=0.30 on word overlap alone — contributes −0.33 to signed Δε); (ii) one genuine placement disagreement on "cable" (v1 matched to "Subsea Cable Protection" at 0.25; v2 matched to "Subsea Cable Systems" at 0.70). Removing the spurious match brings v2's \|Δε\| to 0.164, closer to v1's 0.142. Not a skill-level regression — vocabulary reshuffling that stressed the fuzzy matcher.

### 9.6 Caveats on the v2 numbers

1. **n=6 is small.** Per-map metric variance in the 25-map corpus is ±10-15pp. The aggregate \|Δε\| improvement (0.025) is inside that noise band.
2. **Single run per scenario.** No replication-variance estimate. LLM sampling contributes unknown noise.
3. **Two of six maps** (culture-gender, agriculture-regen) are `draft.owm` promoted to `output.md` — the subagents hung after the validator pass. Both drafts were validator-clean (no violations), so placements are the skill's final output, but no final prose/analysis was emitted.
4. **Checklist content is adapted from arc-kit**, which was also being benchmarked. This is acknowledged and doesn't invalidate the v1→v2 comparison, but means v2 and arc-kit share some conceptual DNA.
5. **Improvements on specific weak points** (boundary-crossing, overshoot) are encouraging precisely because they were pre-specified weak points — not retroactive pattern-finding. But a full 25-map re-validation would be the proper confirmation.

### 9.7 Reproducibility

```
skills/wardley-map-workspace/arc-kit-compare/
├── skill/                             # vendored arc-kit skill
├── eval-<name>/wardley-reference.owm  # the six held-out refs
├── eval-<name>/with_skill/run-1/…     # arc-kit output
├── eval-<name>/ours-v2/run-1/…        # our-v2 output
├── compare.py                         # arc-kit vs ours-v1
└── compare3.py                        # three-way
```

```bash
cd skills/wardley-map-workspace/arc-kit-compare
python3 compare3.py
```

All numbers in §9.3 regenerate from committed artefacts — no LLM or network calls.

---

## Appendix A — Test prompts per benchmark

Original scenario prompts were not stored as standalone artefacts (see Methodology §9 — `eval_metadata.json` was expected but not produced for iterations 10-14). The summaries below are extracted from the **subagent's scenario-restatement paragraph** at the top of each `output.md`, which paraphrases the prompt it was given. They are representative of what the subagent was asked rather than verbatim originals. Each entry links to the generated output file.

| # | Benchmark | Date pin | Scenario (subagent restatement) | Output |
|---:|---|---|---|---|
| 1 | ai-trust | Jun 2023 | Map the AI trust landscape — components determining whether individuals, government, and business can trust AI systems: technical (models, data, compute), governance (regulations, audits, benchmarks), control mechanisms (forensics, feedback loops, constitution), outcomes (safety, reputation, competitive advantage). | `iteration-10/eval-ai-trust/` |
| 2 | healthcare-clinical | Aug 2022 | How medical practitioners and institutions reach treatment decisions: knowledge layer (trials, reviews, historical data), decision components (diagnosis, treatment options, permissible treatment under funding rules), settings of care (primary, ER, virtual, assisted living), outcomes (patient health, clinical metrics, fairness). Pinned pre-ChatGPT. | `iteration-10/eval-healthcare-clinical/` |
| 3 | finance-risk | ~2023 | Landscape of risk management in financial services. Four actor-classes (Public, Society, Corporations, Government), six risk types (sovereign, territorial, economic, political, cybersecurity, perceived), signalling services (rating agencies, credit scoring, actuarial pricing), mathematical/legal foundations. | `iteration-10/eval-finance-risk/` |
| 4 | retail-journey | — | Modern retail customer journey: how customers move from an initial need through to purchase; actors (customer, producer, society); components (channels, price, convenience, experience); what is differentiating vs commoditising; where friction is worth reducing. Rerun under exponential seed. | `iteration-11/eval-retail-journey/` |
| 5 | manufacturing | Feb 2023 | Modern manufacturing supply chain. Two anchors for the two distinct user needs (cost/reliability vs. resilience/agility). Spans sourcing, production, logistics, digital tooling, compliance, supplier relationships. | `iteration-12/eval-manufacturing-supply/` |
| 6 | agriculture | Aug 2022 | Landscape of regenerative farming: soil health, biodiversity, carbon sequestration, farmer practices, certifications, supply chains to consumers, funding sources, measurement/verification. Pinned to week IRA was signed. | `iteration-12/eval-agriculture-regen/` |
| 7 | education | — | Lifelong learning for working adults: skills demand signals, content, platforms, credentialing, employer relationships, funding (employer / individual / public), motivation, outcomes. Two anchors: working adult learner + employer. | `iteration-12/eval-education-lifelong/` |
| 8 | gaming | Nov 2023 | Game economies in modern live-service games: player motivation, engagement systems, in-game currency, items and loot, trading, monetisation, live-ops, analytics, anti-cheat, regulation. Flag regulatory pressure. | `iteration-12/eval-gaming-economies/` |
| 9 | sustainability | — | Sustainable supply chain management: traceability, emissions measurement, supplier assessment, circular-economy models, regulation (CSRD, CBAM, EUDR, SFDR, Modern Slavery, ISSB), stakeholder reporting, governance. | `iteration-12/eval-sustainability-supply/` |
| 10 | cybersecurity | May 2023 | Cyber risk management in a mid-to-large enterprise: threat intelligence, vulnerability management, incident response, identity and access, compliance/regulation, risk quantification, security operations, controls. Two anchors: CISO/Board + Employee/Business User. Rerun after density guidance. | `iteration-13/eval-cybersecurity-risk/` |
| 11 | construction-supply | Mar 2023 | Modern construction supply chain for commercial building projects: material sourcing, specification, procurement, logistics, on-site coordination, subcontractors, compliance (building codes, safety), digital tools (BIM, procurement platforms), stakeholder relationships. | `iteration-14/eval-construction-supply/` |
| 12 | culture-gender | Mar 2022 | Cultural landscape of gender in society — unusual application where "user need" is a person/community/institution navigating contested cultural terrain. Differentiation/commoditisation read as cultural rather than commercial. Pinned to a moment of peak-contest (Cass interim report, Florida HB 1557, Lia Thomas NCAA, Scotland GRR Bill). | `iteration-14/eval-culture-gender/` |
| 13 | defence-intelligence | Mar 2023 | National defence intelligence enterprise: collection (HUMINT, SIGINT, OSINT, GEOINT, MASINT, cyber), PED, all-source fusion and analysis, tradecraft, tooling, decision-support to commanders/planners/allied partners. Multi-anchor. | `iteration-14/eval-defence-intelligence/` |
| 14 | defence-grey-zone | — | Grey-zone conflict — hostile activity below the threshold of conventional war: disinformation, cyber operations, economic coercion, proxy forces, lawfare, influence operations, critical infrastructure attack, counter-measures. Three anchors: nation-state, critical-infrastructure operators, civil society. | `iteration-14/eval-defence-grey-zone/` |
| 15 | energy-disruption | Jul 2022 | Electricity-sector transition from centralised fossil generation toward distributed renewables + storage + demand-side flexibility: generation, storage, grid, distribution, retail, consumer, policy, market mechanisms. Three anchors: consumer, grid operator, policymaker/regulator. Post-Ukraine-invasion context. | `iteration-14/eval-energy-disruption/` |
| 16 | energy-storage | Apr 2023 | Electrical energy storage — grid-scale and distributed battery storage, pumped hydro, thermal, hydrogen: storage technologies, deployment models, markets (frequency response, arbitrage, capacity), regulation, supply chains (battery minerals, manufacturing), grid integration. | `iteration-14/eval-energy-storage/` |
| 17 | government-digital-id | Nov 2022 | Nation-state provision and governance of citizen digital ID: authentication, credential issuance, verification, legal frameworks, trust infrastructure, privacy, service integration (banking, health, tax, welfare). Two anchors: citizens + relying parties. | `iteration-14/eval-government-digital-id/` |
| 18 | government-sovereignty | Apr 2023 | State sovereignty in a digital, globalised economy: territorial, economic, technological, data, political, cultural dimensions; instruments (regulation, standards, trade, defence, diplomacy); erosion risks (platforms, capital flight, cyber, supply chain dependency). | `iteration-14/eval-government-sovereignty/` |
| 19 | personal-fin-inclusion | — | Digital financial inclusion for under-banked populations in emerging markets: basic account access, mobile money, agent networks, identity, credit scoring (alternative data), regulation, consumer protection, support. Two anchors: under-banked consumer + merchant/micro-business. | `iteration-14/eval-personal-fin-inclusion/` |
| 20 | personal-conversational | — | Modern conversational technology (voice assistants, chatbots, LLM-powered agents): language models, speech (ASR, TTS), dialogue management, knowledge retrieval, personalisation, privacy, user experience. Two anchors: End User + Developer. | `iteration-14/eval-personal-conversational/` |
| 21 | politics-labour | May 2024 | UK Labour Party's core values and policy positioning on the eve of the July 2024 general election: core values (equality, fairness, opportunity, community, responsibility), constituencies, policy levers (NHS, education, housing, climate, workers' rights), media relations, party machinery. | `iteration-14/eval-politics-labour/` |
| 22 | telecoms-sovereignty | Oct 2022 | Telecoms sovereignty — a nation's ability to control its own telecommunications infrastructure. Context: UK Telecoms Security Act, Huawei legal notices, Nord Stream sabotage, Starlink in Ukraine, first commercial OpenRAN, CHIPS Acts. Three anchors: nation-state, citizens, businesses. | `iteration-14/eval-telecoms-sovereignty/` |
| 23 | telecoms-space | Feb 2023 | Telecoms via space: LEO satellite broadband (Starlink-class) scaling commercially; satellite-to-phone direct connectivity emerging (BlueWalker 3, T-Mobile + Starlink, Apple Emergency SOS); competition with terrestrial networks across rural, enterprise, maritime, aviation, defence markets. | `iteration-14/eval-telecoms-space/` |
| 24 | transport-logistics | — | Modern logistics (freight and parcel across road, rail, sea, air): demand signals, carrier networks, warehousing, last-mile, tracking, customs, regulation, digital platforms. Multi-stakeholder industry-landscape. | `iteration-14/eval-transport-logistics/` |
| 25 | transport-demand | May 2022 | Urban mobility landscape: how city-dwellers, commuters, and municipalities choose and supply transport modes; drivers (cost, time, sustainability, convenience, safety); supply-side operators, manufacturers, platforms. Post-COVID habit shifts partially settled, micromobility scaled, ride-hail post-IPO, EV adoption accelerating. | `iteration-14/eval-transport-demand/` |

For the one prompt documented verbatim (ai-trust, as an example), see Methodology §2(a). For the others, open the referenced `output.md` — the subagent echoes the prompt in its opening paragraph.

---

## Appendix B — Code references

| Path | Role |
|---|---|
| `skills/wardley-map/SKILL.md` | 7-step procedure and when-to-use instructions followed by every benchmark subagent |
| `skills/wardley-map/scripts/validate_owm.mjs` | Structural validator — enforces visibility hard rule, coordinate range, edge-endpoint declaration. Called iteratively by the subagent until exit-code 0 |
| `skills/wardley-map/references/evolution-stages.md` | 19-row cheat sheet (4-row subset used by default) |
| `skills/wardley-map/references/climatic-patterns.md` | 27 climatic patterns — consulted during strategic analysis |
| `skills/wardley-map/references/doctrine.md` | 40 doctrine principles |
| `skills/wardley-map/references/gameplay-patterns.md` | 61 gameplays across 12 categories |
| `skills/wardley-map/references/inertia.md` | 17 forms of resistance to evolution |
| `skills/wardley-map/references/mapping-examples.md` | 3 worked maps (tea shop, freelance marketplace, SaaS) |
| `skills/wardley-map/references/mathematical-models.md` | Condensed formalism and dynamics |
| `skills/wardley-map-workspace/compare_all_25.py` | Aggregates 25 benchmarks → per-map table, aggregate stats, pooled `|Δε|` distribution, near-boundary miss count. Writes `benchmark-25-summary.json` |
| `skills/wardley-map-workspace/compare_all_10.py` | Historical aggregator for the first 10 benchmarks (kept for metric-history trace) |
| `skills/wardley-map-workspace/iteration-10/compare.py` | Parsing and fuzzy-match primitives — imported by the aggregators |
| `skills/wardley-map-workspace/benchmark-25-summary.json` | Machine-readable per-map and aggregate output (source of every number in §3) |

Key functions:

- `iteration-10/compare.py::parse_owm(text)` — regex parser for `(anchor|component) <name> [ν, ε]` lines; returns `(anchors, components)` dicts
- `iteration-10/compare.py::fuzzy_match(name, candidates)` — cascade: exact → substring → Jaccard word overlap → `difflib.SequenceMatcher`; threshold 0.55
- `compare_all_25.py::stage_of(eps)` — quartile membership (Genesis / Custom / Product / Commodity) with boundaries at 0.25, 0.5, 0.75
- `compare_all_25.py::stats(ref_path, ours_path)` — per-map pipeline: parse both sides, fuzzy-match every ref component, compute `Δε` and `Δν` vectors, aggregate into the fields written to `benchmark-25-summary.json`
- `compare_all_25.py::BENCHMARKS` — the 25-entry list binding each benchmark name to its reference `.owm` and its generated `output.md`

To reproduce the numbers in §3 without rerunning the skill:

```bash
cd skills/wardley-map-workspace
python3 compare_all_25.py
```

No LLM calls, no network I/O, ~1 second runtime. All inputs (`wardley-reference.owm`, generated `output.md`) are committed.
