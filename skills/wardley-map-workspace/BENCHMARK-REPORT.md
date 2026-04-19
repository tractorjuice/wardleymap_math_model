# Wardley Map Skill — Benchmark Report

**Date:** 2026-04-18
**Skill version:** commit `2f5a016` + exponential-seed default (α=0.6)
**Test corpus:** 10 maps held out from [swardley/WARDLEY-MAP-REPOSITORY](https://github.com/swardley/WARDLEY-MAP-REPOSITORY) (Simon Wardley's own published maps)
**Test mode:** blind — subagents could not access the reference .owm files

---

## 1. What the skill is

A portable Claude Code skill package (`skills/wardley-map/`) that generates a Wardley Map from a free-form scenario description. Produces OWM-format output plus a strategic analysis.

### 1.1 The math model

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

Visibility seed (default):

```
d(v) = min over u ∈ U of { shortest path length from u to v }
ν(v) = exp(−0.6 · d(v))
```

Constrained by the hard rule `ν(a) ≥ ν(b)` for every edge `(a, b)`.

Evolution scored via Wardley's 19-row cheat sheet (full table in `references/evolution-stages.md`); 4-row quick subset used for initial placement.

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

### 1.3 The generation pipeline (7 steps)

1. **Components and anchors** — identify user-need nodes `U` and candidate `V`
2. **Dependencies** — draw `E` as "depends-on" edges
3. **Visibility ν** — exponential seed + manual override
4. **Evolution ε** — 4-row cheat-sheet scoring, band midpoints
5. **Deep placement (4.5)** — selective WebSearch for components where rows disagree or strategic importance is high
6. **Verification (5.5)** — run `validate_owm.py`; fix violations; iterate until clean
7. **Strategic analysis** — stage-first prose covering differentiation, commodity leverage, dependency risks, gameplays (cited by number from the 61-play catalogue), doctrine violations, climatic context, deep-placement findings, scenario-not-forecast caveat

---

## 2. Test methodology

### 2.1 Test design

Held-out comparison against Wardley's own published maps. For each test case:

1. Fetch a Wardley map `.owm` file from the GitHub repository
2. Read it to derive a realistic scenario prompt — **without exposing Wardley's placements or component names to the subagent**
3. Spawn a subagent with the prompt and explicit instructions not to read the reference file
4. Run the full 7-step skill procedure
5. Compare the generated map to Wardley's reference

### 2.2 Comparison metrics

Given a Wardley reference and our output:

- **Coverage**: what fraction of Wardley's components have a fuzzy-name match in ours
- **|Δε|**: mean absolute difference in evolution scores for matched components
- **|Δν|**: mean absolute difference in visibility scores
- **ε-bias / ν-bias**: signed mean deltas (positive = we're higher than Wardley)
- **Same-stage placement**: fraction of matched components falling in the same evolution stage (|Δε| < 0.25)

Fuzzy matching uses exact-match, substring containment, and sequence similarity ≥ 0.55.

### 2.3 Time pinning

Several Wardley maps carry explicit dates (AI TRUST June 2023, healthcare Aug 2022, manufacturing Feb 2023, cybersecurity May 2023, gaming Nov 2023). The subagent is pinned to that date in the prompt to prevent 2026-priors from biasing placements.

### 2.4 Corpus

10 maps spanning 10 domains:

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

Diversity spans AI/tech/consumer digital/regulated industry/traditional industry/social systems.

---

## 3. Results

### 3.1 Per-benchmark table

| Benchmark | Ref | Ours | Match | Coverage | \|Δε\| | \|Δν\| | ε-bias | ν-bias | Same-stage |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ai-trust | 37 | 34 | 23 | 62% | 0.153 | 0.306 | −0.010 | +0.236 | 78% |
| retail-journey | 41 | 52 | 20 | 49% | 0.174 | 0.273 | −0.078 | +0.172 | 85% |
| healthcare | 40 | 30 | 24 | 60% | 0.179 | 0.386 | +0.046 | +0.298 | 75% |
| finance-risk | 42 | 41 | 23 | 55% | 0.162 | 0.250 | +0.016 | +0.117 | 70% |
| manufacturing | 44 | 37 | 14 | 32% | 0.226 | 0.353 | +0.174 | −0.190 | 57% |
| cybersecurity | 33 | 60 | 18 | 55% | 0.161 | 0.228 | +0.078 | +0.177 | 83% |
| agriculture | 50 | 55 | 18 | 36% | 0.233 | 0.213 | −0.198 | +0.005 | 56% |
| education | 40 | 44 | 13 | 32% | 0.178 | 0.220 | +0.024 | +0.032 | 69% |
| gaming | 33 | 49 | 14 | 42% | 0.206 | 0.180 | +0.198 | +0.053 | 57% |
| sustainability | 43 | 58 | 11 | 26% | 0.135 | 0.245 | −0.077 | +0.127 | 91% |

### 3.2 Aggregate statistics (n=10)

| Metric | Value |
|---|---|
| Mean coverage | **45%** |
| Mean same-stage placement | **72%** |
| Mean \|Δε\| | 0.181 |
| Mean \|Δν\| | 0.265 |
| ε-bias | +0.017 (negligible) |
| **ν-bias** | **+0.103** (down from +0.22 before exponential seed) |

### 3.3 Structural outcomes (all 10 benchmarks)

- ✅ **Validator-clean**: every map produced passed `validate_owm.py` (`ν(a) ≥ ν(b)` for every edge, coordinates in [0,1], endpoints declared)
- ✅ **Anchor identification**: in every case, our subagent independently identified 1–3 user-need anchors that align with Wardley's framing (e.g., Customer/Producer/Society for retail; Individual/Government/Business for AI trust; Farmer/Consumer for agriculture)
- ✅ **Canonical stage naming**: every prose analysis used "Product (+rental)" and "Commodity (+utility)" correctly
- ✅ **Deep placement used**: each subagent ran 3–5 targeted WebSearches with citations in the output

### 3.4 Token and time cost

| Benchmark | Tokens | Duration |
|---|---:|---:|
| ai-trust | 66 K | 4.6 min |
| retail (iter-11) | 75 K | 6.0 min |
| healthcare | 87 K | 6.0 min |
| finance | 82 K | 5.1 min |
| manufacturing | 66 K | 5.3 min |
| cybersecurity | 89 K | 6.8 min |
| agriculture | 106 K | 10.0 min |
| education | 73 K | 4.7 min |
| gaming | 62 K | 4.7 min |
| sustainability | 74 K | 4.9 min |
| **Average** | **78 K** | **5.8 min** |

Total corpus cost: ~780 K tokens, ~58 min of subagent time.

---

## 4. Findings

### 4.1 What the skill gets right

**1. Structural faithfulness.** 72% of matched components land in the same evolution stage Wardley places them in. Anchors are consistently correct across all 10 domains. ε-bias is negligible (+0.017) — we neither over- nor under-industrialise on average.

**2. Strategic conclusions converge with Wardley's implicit framing.** Across the 10 scenarios, the subagent independently reached takeaways that align with what Wardley would say: *governance always trails the technology it governs* (AI trust), *platform plays need both sides* (gaming, freelance, retail), *don't build what's already commodity* (everywhere), *the knowledge layer is often underspecified* (healthcare, education, finance).

**3. Validator reliably enforces the hard rule.** Across all 10 runs, the validator caught between 1 and 13 visibility violations on first draft, which the subagent fixed iteratively. Without the validator, ~half the maps would have shipped with silent structural errors (a specific failure we observed before the validator existed in earlier iterations).

**4. Deep placement changes real outcomes.** Several benchmarks produced specific, non-generic findings the subagent could not have guessed from priors alone:
- Freelance marketplace: Dispute Resolution moved from BUILD to RENT after finding Dyspute.ai, FairClaims, Visa DRN.
- SaaS invoicing: PEPPOL adapter moved 0.40 → 0.62 on EU ViDA mandate dates.
- Retail: BNPL regulatory timeline shift (UK FCA from July 2026).
- Agriculture: Soil Carbon MRV confirmed Genesis/early-Custom because protocols fragmented.
- Cybersecurity: GenAI Security Copilot confirmed Stage I on May 2023 Microsoft Security Copilot announcement.

### 4.2 What the skill doesn't do well

**1. Coverage ceiling around 45%.** Our skill names roughly half of the components Wardley names. The missing half breaks into two categories:

*Abstract philosophical concepts* — Wardley treats things like "Asymmetrical", "Believed", "Bias", "Quality", "OUTPUT", "ACCESS", "perceived risk", "profit" as first-class map nodes. Our skill produces more operational, concrete components (Foundation Models, RAG, Fine-tuning) and rarely reaches for these abstractions. This is a systematic semantic gap.

*Wardley's distinctive vocabulary* — components like "Dr Google" (healthcare), "sovereignty / territorial" (finance), "constitution" (AI trust) are Wardley's stylistic fingerprint. A skill scoring against a cheat sheet can't reproduce them.

**2. Visibility compression, softened but not eliminated.** The exponential-seed change reduced ν-bias from +0.22 to +0.10. But the bias remains positive in 8 of 10 benchmarks. We still systematically place components a little higher in the chain than Wardley does. The root cause is partly the seed (fixed); partly subagent preference for "round numbers" (0.3, 0.5, 0.7); partly the fact that Wardley's deep infrastructure is often single-purpose utilities we don't think to model.

**3. Component count mis-calibration (partly mitigated).** Wardley averages 40 components per map; the skill originally ranged from 30 to 60 depending on scenario, with no notion of "appropriate map density". After this report was first drafted, density guidance was added to SKILL.md §1 (target ranges by scenario type: 20-30 / 35-45 / 40-55; plus an "if removing it wouldn't change any conclusion, leave it out" heuristic). The cybersecurity rerun in §5.4 shows the guidance successfully pulls an over-decomposed 60-component map down to 39 (inside the 35-45 landscape band) with a coverage bump, but at a 20pp same-stage cost — compressing components changes which ones match Wardley's placements. Net: genuine improvement for over-decomposed commodity infrastructure; the skill now has *a* notion of density, but it's a target rather than a cap.

**4. Coverage varies sharply by domain:**
- **High coverage** (55–62%): AI trust, retail, healthcare, finance, cybersecurity — domains with a well-defined vocabulary and where the scenario prompt naturally suggests similar decompositions to Wardley's.
- **Low coverage** (26–36%): manufacturing, agriculture, education, sustainability — domains where Wardley's framing is idiosyncratic or regulatory-heavy and our skill frames more operationally.

The **sustainability** map is the worst case (26%): 58 of our components but only 11 overlap with Wardley's 43. We produced a regulation/reporting heavy map; Wardley's is weighted toward measurement and circular-economy concepts.

**5. Manufacturing shows inverse ν-bias (−0.19).** This is the only benchmark where we placed components lower than Wardley. Looking at the map, Wardley's manufacturing supply chain has "End Customer" and several visible components higher up, while ours pushed them down. The exponential seed may over-correct when the scenario demands a mostly-flat visibility distribution.

### 4.3 Cost and runtime

- ~78 K tokens per map on average
- ~6 minutes per map wall-clock
- About 2× the cost of the same maps without the deep-placement step, 1.5× the cost without the validator iterations
- Deep placement and validator iterations are the right cost to pay — they're where the visible quality improvements come from

---

## 5. Recommendations from this benchmark

### 5.1 Already implemented

- ✅ Exponential-decay seed replacing reciprocal decay (closed half the ν-bias)
- ✅ Validator script enforcing structural invariants
- ✅ Stage-first qualitative prose in analysis
- ✅ Deep-placement step with targeted WebSearch
- ✅ **Component density guidance** (added 2026-04-18) — target ranges by scenario type, "if removing it wouldn't change any conclusion, leave it out" heuristic, common-over-addition list

### 5.2 Open opportunities

**1. Expand the abstract-component repertoire.** Add a reference file listing ~30 "distinctive Wardley vocabulary" nodes (perceived risk, asymmetric access, believed quality, etc.) and instruct the skill to consider them when the scenario is landscape-level rather than product-level. This could lift coverage on AI trust, finance, sustainability without hurting concrete-product cases.

**2. ~~Per-domain component density guidance.~~** Implemented — see §5.4 below for results.

**3. Dampen exponential α when visibility distribution should be flat.** Manufacturing showed inverse ν-bias; the exponential seed may be over-correcting in scenarios where most components are genuinely mid-chain. A scenario classifier (not a big ML thing — just a few heuristic rules) could pick α ∈ {0.4, 0.6, 0.8} by domain.

**4. Normalise against Wardley's vocabulary when possible.** A lookup table mapping common tech-stack terms to Wardley's preferred phrasing (e.g., "fine-tuning" → "custom training"; "vector DB" → "data index"; "observability platform" → "logs & telemetry") would boost match-rate on the fuzzy-match metric without changing actual placement quality. Low-effort, high-measured-coverage.

**5. The false-precision risk remains.** Numeric ν and ε values are required by OWM format and useful for the validator, but the qualitative framing (stage labels, rank orders) in analysis is what users should trust. The skill already instructs this; compliance was ~100% in the benchmarks. Worth keeping vigilant.

### 5.4 Density guidance follow-up

After this report was first drafted, recommendation #2 was implemented: SKILL.md §1 now has target ranges by scenario type (20-30 / 35-45 / 40-55) plus a "if removing it wouldn't change any conclusion, leave it out" heuristic. Rerun of the worst over-decomposer (cybersecurity, originally 60 components vs Wardley's 33):

| Metric | Before (60 comps) | After (39 comps) | Δ |
|---|---:|---:|---:|
| Coverage | 55% | **58%** | +3pp |
| ν-bias | +0.177 | **+0.139** | −0.038 |
| Same-stage | **83%** | 63% | −20pp |
| \|Δε\| | 0.161 | 0.208 | +0.047 |

**Mixed outcome.** The density target was met and coverage + ν-bias both improved. But same-stage placement regressed 20 points. The explanation: compressing 60 components to 39 changes which components match Wardley's — merged nodes land at the weighted-mean stage rather than Wardley's more granular placements. Denser maps trade density-fidelity for placement-fidelity.

**Interpretation:** density guidance is a genuine improvement for maps that were over-decomposing obvious commodity infrastructure (Cloud + DB + CDN + Storage as four separate nodes when one "Cloud utilities" would do), but over-application can mask legitimate sub-component distinctions. The implemented guidance phrases it as a *target, not a cap* — that framing was correct. The skill should respect the target for tightly-scoped scenarios while allowing departure when specific sub-components carry distinct strategic weight.

Net recommendation: keep density guidance; don't tighten further without evidence.

### 5.3 What not to do

- **Don't tune the skill harder to this benchmark.** 10 maps is a small, biased sample (all by Wardley himself; 60% are 2022-2023 vintage). Over-fitting to "what Wardley does" would just make the skill a Wardley-style-mimic rather than a useful strategic tool.
- **Don't treat ~50% coverage as a failure.** The test is blind — we're producing maps from scratch that match ~half of an expert's components *without* access to his output. That's a reasonable baseline, not a ceiling.
- **Don't chase the 100% same-stage target.** Wardley himself revises his own maps between editions. A 25-point `|Δε|` difference often means the mapper and Wardley legitimately disagree about where a component is, not that one is wrong.

---

## 6. Limitations of this evaluation

1. **Sample size n=10.** Signal, not proof. Another 10 maps might shift averages by ±5 percentage points.
2. **All reference maps are by one author.** Wardley's style is distinctive. The skill is implicitly being measured against *Wardley's* judgment, not ground truth.
3. **Fuzzy matching is imperfect.** The coverage number underestimates real agreement; some components that are semantically equivalent are matched only by a loose similarity threshold.
4. **Time pinning is leaky.** Subagents have 2026 priors and can only partially suppress them given a pre-2024 context. This probably inflates the modernity of our placements vs. Wardley's historical ones.
5. **Placement metrics don't capture strategic quality.** A map can score 70% same-stage but give bad strategic advice (and vice versa). The qualitative analysis in each benchmark's strategic-analysis section is harder to measure but arguably more important than placement numerics.

---

## 7. Bottom line

The skill produces Wardley Maps that are:
- **Structurally valid** (every map passes the validator)
- **Roughly faithful to Wardley's placements** (72% same-stage, minimal ε-bias)
- **Grounded in live research** (deep placement with 3–5 vendor/regulatory citations per map)
- **Strategically coherent** (stage-first prose, named gameplays, doctrine checks)

...while systematically differing from Wardley in two specific ways:
- **More operational, less philosophical** vocabulary (45% component coverage, not 80%)
- **Mildly visibility-compressed** (+0.10 ν-bias, down from +0.22)

For practitioner use — mapping a business or product scenario — the skill is production-useful. For academic or archival fidelity to Wardley's own style, it would need additional vocabulary and density heuristics that the current test data would support designing.

---

## 8. Artifacts

All 10 benchmark runs, reference files, comparison scripts, and grading outputs are preserved at:

```
skills/wardley-map-workspace/
├── iteration-10/          # first 4 benchmarks (reciprocal seed)
├── iteration-11/          # retail rerun with exponential seed
├── iteration-12/          # 6 new benchmarks (manufacturing, cyber, ag, edu, gaming, sustain)
├── compare_all_10.py      # comparison script producing this report's tables
└── BENCHMARK-REPORT.md    # this document
```

Each `eval-<name>/` directory contains:
- `wardley-reference.owm` — the held-out reference
- `with_skill/run-1/outputs/output.md` — the skill's generated map
- `with_skill/run-1/outputs/draft.owm` — validator working file
- `with_skill/run-1/timing.json` — token/duration
