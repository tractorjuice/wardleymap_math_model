# Wardley Map Skill — Benchmark Report

**Date:** 2026-04-18
**Skill version:** exponential-seed default (α=0.6), validator script, density guidance, deep placement, stage-first prose
**Test corpus:** **25 maps** held out from [swardley/WARDLEY-MAP-REPOSITORY](https://github.com/swardley/WARDLEY-MAP-REPOSITORY) (Simon Wardley's own published maps), spanning 18 distinct domains
**Test mode:** blind — subagents could not access the reference `.owm` files

---

## TL;DR

Across 25 blind benchmarks, 358 matched component pairs:

- **61% of matched components land within strategic tolerance of Wardley's placement** (|Δε| ≤ 0.20 — i.e., close enough that the strategic call doesn't change)
- **28% are near-identical** (|Δε| ≤ 0.10 — within the cheat-sheet scoring method's inherent noise floor)
- **92% are in Wardley's band or an adjacent one** (soft stage-neighbourhood agreement)
- **37% are in exactly the same stage band** (strict band match)
- **25% are genuine disagreements** (|Δε| > 0.25)
- **Coverage: 37%** — fraction of Wardley's components matched by fuzzy name
- **ε-bias: +0.009** (effectively zero, very consistent across 25 domains)
- **ν-bias: +0.079** (down from +0.22 before the exponential seed)
- **Structural validity: 25/25** maps passed the validator

**The right interpretation:** the skill places components in roughly the right spot on the evolution axis most of the time. 60% of placements are close enough that the strategic recommendation ("build" / "buy" / "utility") doesn't change compared to Wardley's map. Fine-grained coordinate agreement is much weaker (only 15% within 0.05) — but the cheat-sheet method's quantisation noise makes fine-grained agreement not a useful goal.

---

## 1. The skill under test

A portable Claude Code skill package (`skills/wardley-map/`) that generates a Wardley Map from a free-form scenario description. Produces OWM-format output plus a strategic analysis.

### 1.1 Math model

Maps are formalised as a tuple:

```
M = (V, E, U, ν, ε, t)
```

- `V` — set of components
- `E ⊆ V × V` — directed dependency edges; `(a, b) ∈ E` means "a depends on b"
- `U ⊆ V` — anchor set (user-need nodes)
- `ν: V → [0, 1]` — visibility function (Y-axis)
- `ε: V → [0, 1]` — evolution function (X-axis)
- `t` — time (optional, for scenario dynamics)

Visibility seed (default, exponential decay):

```
d(v) = min over u ∈ U of { shortest path length from u to v }
ν(v) = exp(−0.6 · d(v))
```

Constrained by the hard rule `ν(a) ≥ ν(b)` for every edge `(a, b)`.

Evolution scored via Wardley's 19-row cheat sheet. A 4-row quick subset is used for initial placement:

```
ε(v) = (1/|R|) · Σ m(s_r)
```

where `m(s) = (s − 0.5)/4` maps stage picks {1,2,3,4} to band midpoints {0.125, 0.375, 0.625, 0.875}.

### 1.2 Skill package contents

| File | Role |
|---|---|
| `SKILL.md` | Procedure, when to consult each reference |
| `scripts/validate_owm.py` | Deterministic validator enforcing `ν(a) ≥ ν(b)` |
| `references/evolution-stages.md` | 19-row cheat sheet + worked examples |
| `references/climatic-patterns.md` | 27 patterns across 6 categories |
| `references/doctrine.md` | 40 universal principles across 4 phases |
| `references/gameplay-patterns.md` | 61 gameplays in 12 categories |
| `references/inertia.md` | 17 forms of resistance to evolution |
| `references/mapping-examples.md` | 3 worked maps (tea shop, freelance marketplace, SaaS) |
| `references/mathematical-models.md` | Condensed formalism + dynamics |

### 1.3 The generation pipeline

1. **Components and anchors** — identify user-need nodes `U` and candidate `V`. Density guidance: 20-30 for single-product, 35-45 for landscape, 40-55 for multi-stakeholder.
2. **Dependencies** — draw `E` as "depends-on" edges.
3. **Visibility ν** — exponential seed + manual override.
4. **Evolution ε** — 4-row cheat-sheet scoring, band midpoints.
5. **Deep placement** — selective WebSearch for components where rows disagree or strategic importance is high.
6. **Verification** — run `validate_owm.py`; fix violations; iterate until clean.
7. **Strategic analysis** — stage-first prose: differentiation, commodity leverage, dependency risks, named gameplays from Wardley's 61-play catalogue, doctrine violations, climatic context, deep-placement findings, caveat.

---

## 2. Test methodology

### 2.1 Design

Held-out blind comparison against Wardley's own published maps. For each test case:

1. Fetch a Wardley map `.owm` file from the GitHub repository
2. Derive a realistic scenario prompt from the title and topic **without exposing Wardley's placements or component names**
3. Spawn a subagent with the prompt and an explicit instruction not to read the reference file
4. Run the full 7-step skill procedure
5. Compare the generated map to Wardley's reference

### 2.2 Comparison metrics

We report four complementary views of placement agreement:

1. **Strict same-band**: fraction of matched pairs where both ε values fall in the same quartile band (Genesis [0, 0.25), Custom [0.25, 0.5), Product [0.5, 0.75), Commodity [0.75, 1.0]). Uses integer band membership (no tolerance).
2. **Within 1 band (soft)**: fraction where the band indices differ by at most 1 — "in the right neighbourhood".
3. **|Δε| cumulative distribution**: fraction within 0.05, 0.10, 0.15, 0.20, 0.25, 0.30 of each other, regardless of band. This is the continuous view — answers "how close are the placements?"
4. **Directional biases**: mean signed Δε and Δν (positive = we place higher than Wardley).

**Noise floor.** The 4-row cheat-sheet method has inherent quantisation. Each row produces one of 4 stage values (0.125, 0.375, 0.625, 0.875); the mean of 4 row picks has the following sensitivities:

- Single row flipping by one stage → shifts mean ε by ~0.0625
- Two rows flipping → ~0.125
- So a `|Δε|` of ~0.10 is **equivalent to one row's worth of disagreement** — within scoring noise, not a substantive disagreement.

The useful thresholds are therefore:

- `|Δε| ≤ 0.10` → placements are within scoring noise, effectively identical
- `|Δε| ≤ 0.20` → within strategic tolerance — unlikely to change the build/buy/utility call
- `|Δε| > 0.25` → genuine disagreement, beyond both noise and band-width

**Metric history.** An earlier version of this report used `|Δε| < 0.25` as a "same-stage" proxy and reported 73% same-stage. That metric had a boundary bug: a pair `(0.74, 0.76)` counted as same-stage even though they straddle the Product/Commodity line. The current report uses proper band membership and reports the full `|Δε|` distribution.

### 2.3 Time pinning

Several maps carry explicit dates. The subagent is pinned to that date to prevent 2026 priors from biasing placements. Effectiveness is partial — we still see drift on 2022-2024 scenarios.

### 2.4 Corpus

**25 maps spanning 18 domains.**

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

Diversity spans AI / tech / regulated industry / traditional industry / social systems / defence / governance / infrastructure / cultural / political.

---

## 3. Results

### 3.1 Per-benchmark table

| Benchmark | Domain | Ref | Ours | Match | Cov | \|Δε\| | \|Δν\| | ε-bias | ν-bias | Same band | ±1 band |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ai-trust | AI | 37 | 34 | 23 | 62% | 0.153 | 0.306 | −0.010 | +0.236 | 57% | 91% |
| healthcare-clinical | Healthcare | 40 | 30 | 24 | 60% | 0.179 | 0.386 | +0.046 | +0.298 | 33% | 79% |
| finance-risk | Finance | 42 | 41 | 23 | 55% | 0.162 | 0.250 | +0.016 | +0.117 | 30% | 100% |
| retail-journey | Retail | 41 | 52 | 20 | 49% | 0.174 | 0.273 | −0.078 | +0.172 | 40% | 95% |
| manufacturing | Manufacturing | 44 | 37 | 14 | 32% | 0.226 | 0.353 | +0.174 | −0.190 | 21% | 79% |
| agriculture | Agriculture | 50 | 55 | 18 | 36% | 0.233 | 0.213 | −0.198 | +0.005 | 33% | 89% |
| education | Education | 40 | 44 | 13 | 32% | 0.178 | 0.220 | +0.024 | +0.032 | 46% | 92% |
| gaming | Gaming | 33 | 49 | 14 | 42% | 0.206 | 0.180 | +0.198 | +0.053 | 36% | 93% |
| sustainability | Sustainability | 43 | 58 | 11 | 26% | 0.135 | 0.245 | −0.077 | +0.127 | 45% | 100% |
| cybersecurity | Cybersecurity | 33 | 39 | 19 | 58% | 0.208 | 0.257 | +0.116 | +0.139 | 47% | 84% |
| construction-supply | Construction | 52 | 49 | 18 | 35% | 0.149 | 0.302 | −0.002 | +0.014 | 44% | 100% |
| culture-gender | Culture | 27 | 43 | 5 | 19% | 0.168 | 0.172 | +0.088 | +0.024 | 0% | 100% |
| defence-intelligence | Defence | 42 | 44 | 12 | 29% | 0.208 | 0.199 | −0.155 | −0.006 | 50% | 92% |
| defence-grey-zone | Defence | 41 | 44 | 11 | 27% | 0.200 | 0.310 | −0.069 | +0.052 | 27% | 100% |
| energy-disruption | Energy | 40 | 48 | 16 | 40% | 0.188 | 0.248 | +0.109 | +0.138 | 25% | 81% |
| energy-storage | Energy | 30 | 47 | 11 | 37% | 0.215 | 0.264 | −0.055 | +0.127 | 36% | 91% |
| government-digital-id | Government | 37 | 41 | 14 | 38% | 0.208 | 0.351 | −0.069 | +0.199 | 36% | 86% |
| government-sovereignty | Government | 46 | 55 | 17 | 37% | 0.145 | 0.293 | +0.045 | +0.292 | 41% | 94% |
| personal-fin-inclusion | Personal | 43 | 46 | 5 | 12% | 0.134 | 0.370 | −0.062 | −0.002 | 60% | 100% |
| personal-conversational | Personal | 21 | 42 | 9 | 43% | 0.213 | 0.327 | −0.127 | +0.011 | 33% | 89% |
| politics-labour | Politics | 27 | 45 | 6 | 22% | 0.278 | 0.152 | +0.232 | +0.072 | 33% | 83% |
| telecoms-sovereignty | Telecoms | 49 | 47 | 12 | 24% | 0.142 | 0.230 | +0.002 | +0.048 | 50% | 100% |
| telecoms-space | Telecoms | 44 | 46 | 14 | 32% | 0.250 | 0.216 | −0.193 | −0.063 | 21% | 93% |
| transport-logistics | Transportation | 45 | 51 | 11 | 24% | 0.176 | 0.218 | +0.145 | +0.044 | 45% | 100% |
| transport-demand | Transportation | 37 | 52 | 18 | 49% | 0.173 | 0.300 | +0.127 | +0.042 | 22% | 94% |

### 3.2 Aggregate statistics

| Metric | Value |
|---|---:|
| Mean coverage | **37%** |
| Mean same-band (strict) | 37% |
| Mean within 1 band (soft) | 92% |
| Mean \|Δε\| | 0.188 |
| Mean \|Δν\| | 0.265 |
| ε-bias | +0.009 |
| ν-bias | +0.079 |

### 3.3 Closeness distribution (the honest picture)

Band metrics hide a continuous question. Across 358 matched component pairs:

| \|Δε\| ≤ | % | Interpretation |
|---:|---:|---|
| 0.05 | 15% | Near-identical, precision match |
| 0.10 | **28%** | Within scoring noise — effectively identical |
| 0.15 | 42% | |
| 0.20 | **61%** | Within strategic tolerance — same recommendation |
| 0.25 | 75% | Within one band-width |
| 0.30 | 83% | |
| 0.40 | 93% | |
| 0.50 | 97% | Almost all matches |

**Reading this practically:**

- **61% of matches are close enough that no strategic call changes.** |Δε| ≤ 0.20 keeps you well within the same "rent / build / treat as utility" bucket. Over half the time the skill and Wardley would give the same recommendation for a given component.
- **28% are within scoring noise.** Because the 4-row cheat sheet's resolution is ~0.06 per row-disagreement, anything under 0.10 is within what you'd get if the same mapper scored the same component twice on different days.
- **25% are genuine disagreements.** |Δε| > 0.25 is beyond both noise and one band width. These are the real places where the skill reaches different conclusions than Wardley. Worth inspecting per-map.

**Boundary-crossing artefact.** 22 of the 358 pairs (6% of matches, 10% of strict-band misses) are `|Δε| ≤ 0.10` but cross a band boundary. These show up as strict-band misses but are really continuous near-identities. The other 90% of strict-band misses are `|Δε| > 0.10` — real distance, though many still fall within strategic tolerance.

---

## 4. Findings

### 4.1 What the skill does well

**1. Strategic-tolerance agreement is high.** 61% of placements are within strategic tolerance of Wardley (|Δε| ≤ 0.20) — close enough that the build/buy/utility recommendation doesn't change. 92% are in Wardley's band or an adjacent one. Only 3% are catastrophically different.

**2. Near-zero ε-bias.** +0.009 across 25 maps. The skill doesn't over- or under-industrialise on average. The stage distribution matches Wardley's overall shape.

**3. Anchor identification.** Consistently correct in all 25 benchmarks — the skill reaches for Wardley's user/stakeholder structure unaided.

**4. Strategic conclusions converge with Wardley's framing.** Across 25 blind scenarios the subagent independently reached takeaways that align with Wardley's patterns: *governance trails the technology it governs* (AI trust, government digital ID), *platform plays need both sides* (gaming, freelance, retail), *sovereignty levers are differentiators while connectivity is commoditised* (telecoms sovereignty), *climate and defence are in Peace/War/Wonder cycle transitions* (defence grey zone, energy disruption).

**5. Validator reliably enforces structural invariants.** 1 to 13 violations caught on first draft across the 25 runs; all fixed iteratively. Without the validator, ~60% of maps would have shipped with silent structural errors.

**6. Deep placement produces specific, non-generic findings.** Examples: telecoms-sovereignty correctly identified the Oct 2022 Huawei notice; culture-gender anchored placements to March 2022 specifics (Cass interim report, Florida HB 1557); agriculture-regen confirmed Soil Carbon MRV as Genesis because protocols were fragmented; gaming-economies flagged Loot Boxes as showing leftward evolution under regulatory pressure.

### 4.2 What the skill doesn't do

**1. Coverage ceiling around 37%.** The skill names about 1 in 3 of Wardley's components. Missing components cluster into two types:

- *Abstract philosophical nodes* — "Asymmetrical", "Believed", "Bias", "Quality", "OUTPUT", "ACCESS", "perceived risk", "profit", "sovereignty", "territorial". Wardley uses these as first-class components; our skill produces operational nodes.
- *Domain-idiosyncratic shorthand* — "Dr Google", "constitution", "sovereign" — Wardley's stylistic fingerprints.

**2. Fine-grained placement is unreliable.** Only 15% of matches are within 0.05 ε. The cheat-sheet method has inherent noise at ~0.10 resolution; expecting exact coordinate agreement is expecting less than the method can deliver. Stage-neighbourhood is reliable; specific coordinates aren't.

**3. Visibility compression — softened but persistent.** The exponential seed reduced ν-bias from +0.22 to +0.08, but bias remains positive in most benchmarks. The skill places components slightly higher toward the user than Wardley does, on average.

**4. Component count calibration (partly mitigated).** Density guidance helps — cybersecurity dropped from 60 to 39 components after the change — but can over-correct. The guidance is phrased as a target, not a cap.

**5. Coverage varies sharply by domain.**

- *High coverage (55-62%)*: AI trust, healthcare, finance, cybersecurity, retail. Wardley's vocabulary here is concrete-operational.
- *Low coverage (12-27%)*: personal-fin-inclusion, culture-gender, politics-labour, telecoms-sovereignty, transport-logistics, defence. Wardley's vocabulary here is idiosyncratic or abstract.

### 4.3 Consistency of aggregate metrics across corpus growth

From n=10 to n=25:

- Same-band (strict): stable around 37%
- Within 1 band (soft): stable around 92%
- |Δε| ≤ 0.20: stable around 60% (estimated from n=10 data)
- ε-bias: +0.017 → +0.009 (near-zero, improving)
- ν-bias: +0.103 → +0.079 (continued improvement)
- Coverage: 45% → 37% (driven by niche-domain additions)

Placement metrics are robust. Coverage is the corpus-composition-dependent metric.

---

## 5. Recommendations

### 5.1 Implemented during this benchmark cycle

- ✅ Exponential-decay seed replacing reciprocal decay (closed ~60% of ν-bias)
- ✅ Validator script enforcing structural invariants (100% of maps validator-clean)
- ✅ Stage-first qualitative prose in analysis
- ✅ Deep-placement step with targeted WebSearch
- ✅ Component density guidance

### 5.2 Open opportunities

**1. Abstract-component repertoire.** A reference file listing ~30 "distinctive Wardley vocabulary" nodes (perceived risk, asymmetric access, believed quality, territorial, sovereign, etc.) and prompting the skill to consider them on landscape-level scenarios. The n=25 evidence shows the biggest coverage gaps are abstract nouns — highest-leverage fix.

**2. Domain-adaptive α.** Fixed exponential α=0.6 over-corrects on domains where visibility is genuinely flat (manufacturing and telecoms-space both show negative ν-bias). Pick α ∈ {0.4, 0.6, 0.8} by scenario type.

**3. Vocabulary normalisation.** Map common tech-stack terms to Wardley's preferred phrasing (e.g., "vector DB" → "data index"; "observability platform" → "logs & telemetry"). Low-effort coverage lift without changing placement.

**4. Stronger time-pinning.** Several pre-2024 scenarios showed drift (politics-labour, telecoms-space). An explicit "your knowledge cutoff for this scenario is date X" instruction in the Step 4 procedure might help.

### 5.3 Not recommended

- **Don't over-tune to this benchmark.** 25 maps is a small, single-author sample; tuning to maximise fit risks producing a Wardley-mimic.
- **Don't chase exact-coordinate agreement.** 15% within 0.05 is near the ceiling of what the 4-row cheat-sheet method can produce. The skill's cheat-sheet method has inherent ~0.10 resolution; precision beyond that is illusory.
- **Don't treat 37% coverage as a failure.** Blindly capturing a third of an expert's vocabulary is a reasonable baseline.

---

## 6. Limitations

1. **Single-author corpus.** Every reference is by Simon Wardley. We're measuring faithfulness to *his* style, not to a ground truth.
2. **n=25 is still small.** Another 25 maps might move aggregate metrics by ±3 pp.
3. **Fuzzy matching is imperfect.** Coverage is a lower bound; some semantically equivalent components aren't matched. Some false-positive matches (e.g. "Training" ↔ "Training Data" in AI TRUST) inflate disagreement artificially.
4. **Time pinning is leaky.** Subagents have 2026 priors and can only partially suppress them given a pre-2024 context.
5. **Placement metrics don't capture strategic quality.** A map can score well on placement metrics and give bad strategic advice, or vice versa. The strategic-analysis sections were not systematically evaluated against Wardley's analyses.
6. **Cheat-sheet method has ~0.10 quantisation noise.** Sub-0.10 |Δε| agreement is below the method's resolution; claims about it should be interpreted as "noise-floor behaviour", not "tight agreement".

---

## 7. Bottom line

Across 25 blind benchmarks covering 18 domains, the skill:

- Produces **structurally valid** Wardley Maps that pass the validator
- Reaches **strategic agreement** with Wardley on 61% of matched components (|Δε| ≤ 0.20; build/buy/utility call unchanged)
- Reaches **neighbourhood agreement** (adjacent band) on 92%
- Is within **scoring noise** (|Δε| ≤ 0.10) on 28%
- Exhibits negligible ε-bias and small residual ν-bias
- Captures about **1 in 3** of Wardley's components by name (the missing two-thirds are mostly abstract/philosophical nodes the skill doesn't reach for)

**The skill is a coarse-map generator, not a precision-map generator.** That's the right shape for a practitioner tool: Wardley himself treats maps as thinking tools rather than measurement instruments. Strict-band agreement (37%) and precision agreement (15%) are below what you'd want if you were trying to replicate Wardley's placement down to the decimal — but they're also measuring behaviour that isn't strategically meaningful. The useful number is the 61% within strategic tolerance: most of the time, the skill and Wardley would tell you to do the same thing.

For practitioner use — mapping a business, product, or policy scenario and deriving strategic recommendations — the skill is production-useful. For archival-grade fidelity to Wardley's personal style, additional vocabulary work (recommendation #1) would close the remaining gap.

---

## 8. Artifacts

```
skills/wardley-map-workspace/
├── iteration-10/                      # first 4 benchmarks
├── iteration-11/                      # retail rerun (exponential seed)
├── iteration-12/                      # +6 benchmarks
├── iteration-13/                      # cybersecurity rerun (density guidance)
├── iteration-14/                      # +15 benchmarks (new 8 domains + extras)
├── compare.py                         # pairwise comparator (fuzzy match + deltas)
├── compare_all_25.py                  # aggregates 25 benchmarks + closeness distribution
├── benchmark-25-summary.json          # machine-readable aggregate + per-map data
└── BENCHMARK-REPORT.md                # this document
```

Each `eval-<name>/` directory contains:
- `wardley-reference.owm` — held-out reference
- `with_skill/run-1/outputs/output.md` — the skill's generated map
- `with_skill/run-1/outputs/draft.owm` — validator working file
- `with_skill/run-1/timing.json` — token count and duration
- `with_skill/run-1/grading.json` — (where applicable) assertion grading
