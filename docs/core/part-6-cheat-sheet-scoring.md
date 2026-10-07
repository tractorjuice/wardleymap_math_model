# Part 6 — Cheat-Sheet Evolution Scoring

The earlier parts placed components on the evolution axis using a small bag of signals (ubiquity, certainty, publication mix) or a single logistic score. That is a **seed**, not the canonical placement. Simon Wardley's actual method is the **evolution cheat sheet** — a 19-row characteristic table where each row has a distinct descriptor for each of the four stages. You score a component row by row, and the cheat sheet tells you where it sits.

Part 4's $(\mathrm{ubiq} + \mathrm{cert})/2$ formula uses 2 of the 19 rows. This part defines this repository's numerical aggregation convention over applicable characteristics, with a disagreement diagnostic. The cheat sheet is Wardley's; the arithmetic aggregation and probability representation are proposed extensions, not his canonical calculation.

---

## 1. The cheat sheet

Reproduced from Simon Wardley's original cheat-sheet table (Figure 17 in [*Finding a Path*](https://medium.com/wardleymaps/finding-a-path-cdb1249078c0), and discussed in [*What's in a Wardley Map and the need for a cheat sheet*](https://blog.gardeviance.org/2016/04/whats-in-wardley-map-and-need-for-cheat.html)). The [Evolve tool](https://hiredthought.com/2019/02/04/evolve-a-quick-reference-for-wardley-mapping/) operationalises the same table.

| # | Characteristic | I — Genesis | II — Custom Built | III — Product (+rental) | IV — Commodity (+utility) |
|---|---|---|---|---|---|
| 1 | **Activities** | Genesis | Custom | Product (+rental) | Commodity (+utility) |
| 2 | **Practices** | Novel | Emerging | Good | Best |
| 3 | **Data** | Unmodelled | Divergent | Convergent | Modelled |
| 4 | **Knowledge** | Concept | Hypothesis | Theory | Accepted |
| 5 | **Ubiquity** | Rare | Slowly increasing consumption | Rapidly increasing consumption | Widespread and stabilising |
| 6 | **Certainty** | Poorly understood | Rapid increases in learning | Rapid increases in use / fit for purpose | Commonly understood (in terms of use) |
| 7 | **Publication Types** | Describe the wonder of the thing | Build / construct / awareness and learning | Maintenance / operations / installation / features | Focused on use |
| 8 | **Market** | Undefined | Forming | Growing | Mature |
| 9 | **Knowledge Management** | Uncertain | Learning on use | Learning on operation | Known / accepted |
| 10 | **Market Perception** | Chaotic (non-linear) | Domain of experts | Increasing expectations of use | Ordered (appearance of being linear) / trivial |
| 11 | **User Perception** | Different / confusing / exciting / surprising | Leading edge / emerging | Common / disappointed if not used or available | Standard / expected |
| 12 | **Perception in Industry** | Competitive advantage / unpredictable / unknown | Competitive advantage / ROI / case examples | Advantage through implementation / features | Cost of doing business / accepted |
| 13 | **Focus of Value** | High future worth | Seeking profit / ROI? | High profitability | High volume / reducing margin |
| 14 | **Understanding** | Poorly understood / unpredictable | Increasing understanding / development of measures | Increasing education / constant refinement of needs & measures | Believed to be well defined / stable / measurable |
| 15 | **Comparison** | Constantly changing / unstable | Learning from others / some evidential support | Feature difference | Essential / operational advantage |
| 16 | **Failure** | High / tolerated / assumed | Moderate / unsurprising but disappointed | Not tolerated, focus on constant improvement | Operational efficiency, surprised by failure |
| 17 | **Market Action** | Gambling / driven by gut | Exploring a "found" value | Market analysis / listening to customers | Metric driven / build what is needed |
| 18 | **Efficiency** | Reducing cost of change (experimentation) | Reducing cost of waste (learning) | Reducing cost of waste (learning) | Reducing cost of deviation (volume) |
| 19 | **Decision Drivers** | Heritage / culture | Analysis & synthesis | Analysis & synthesis | Previous experience |

Note on row 19: the "Heritage / culture" at Genesis and "Previous experience" at Commodity appears counter-intuitive. It is, however, what Wardley publishes — the reading is that in Genesis you have no data so you fall back on heritage/culture, and in Commodity the domain is settled so you rely on prior experience with similar commodities.

---

## 2. Formalizing the score

### 2.1 Per-row scoring

For each row $r$ in the cheat sheet, the mapper picks the stage $s_r(v) \in \{1, 2, 3, 4\}$ that best describes component $v$ in that dimension.

If evidence genuinely straddles stages, record the alternatives and their rationale. An explicit midpoint interpolation may be used for plotting (e.g., III–IV gives 0.750), but it adds an assumption rather than resolving the uncertainty.

Convert each stage to its band midpoint:

$$m(s) = \frac{s - \tfrac{1}{2}}{4}$$

So stage I → 0.125, II → 0.375, III → 0.625, IV → 0.875 (the midpoints of the four stage bands in Part 1 §4.1).

### 2.2 Aggregate to $\varepsilon(v)$

Let $R$ be the nonempty set of applicable rows you use (see §3). The proposed evolution score is the (optionally weighted) mean of the per-row midpoints:

$$\varepsilon(v) = \sum_{r \in R} w_r \cdot m(s_r(v)), \quad w_r\ge0,\quad \sum_{r \in R} w_r = 1$$

The unweighted case $w_r = 1/|R|$ is the sensible default.

Stages are ordinal. Equal band widths and averaging assume equal numerical spacing; they do not establish a measurable interval scale. Report the characteristic profile and stage interpretation alongside the plotting coordinate. With midpoint scores alone, the aggregate lies in $[0.125,0.875]$; placements outside that interval need a separately documented adjustment.

### 2.3 Row disagreement and evidence uncertainty

Measure dispersion across the selected characteristics as:

$$H(v) = \sum_{r \in R} w_r \cdot \bigl(m(s_r(v)) - \varepsilon(v)\bigr)^2.$$

$H$ describes row disagreement, not $\mathrm{Var}(\varepsilon)$ or estimator precision. High $H$ can indicate a mixed characteristic profile, a transition, or conflicting assessments. Low $H$ can reflect consistent but weak or duplicated evidence. Neither establishes confidence by itself.

Record three distinct items: the characteristic profile and $H$; source provenance, applicability and missing evidence; and disagreement across independent mappers or repeated assessments. Rows sharing a source are correlated, so do not divide $H$ by the number of rows to manufacture a standard error. Missing rows remain missing; do not impute Commodity or zero uncertainty.

Use stage alternatives or an explicitly elicited range when confidence is unmeasured. If using Part 1 §6's Beta approximation, justify its variance independently and check its moment bounds. Row agreement must not automatically yield a zero-width distribution.

---

## 3. Which rows to use

Consult the full sheet, but score only applicable, supported characteristics. Rows 1–4 describe alternative component types; select the relevant type vocabulary rather than counting all four as independent evidence. Common practical subsets:

- **Quick-look (4 rows)**: Ubiquity, Certainty, User Perception, Publication Types. These four cover the forces Wardley emphasises most in prose and are usually the easiest to assess from external evidence.
- **Activity-focused (7 rows)**: rows 5–11 (Ubiquity through User Perception). Drops the "Activities/Practices/Data/Knowledge" header rows which mostly restate stage labels, and drops the later rows about organisational decision-making that matter more for doctrine than placement.
- **Full-sheet assessment**: examine all 19 rows in a workshop; exclude inapplicable type rows and record missing evidence. More rows do not automatically produce more confidence.

Whichever subset you pick, document it. A score computed against 4 rows and a score computed against 19 rows are not directly comparable.

---

## 4. Worked example — "Managed Kubernetes"

A component like managed Kubernetes (e.g., EKS, GKE) in 2025. Scoring 7 rows:

| Row | Stage picked | Reasoning | $m(s)$ |
|---|---|---|---|
| Ubiquity | IV | Widespread among cloud-native orgs | 0.875 |
| Certainty | III | Well-understood but still evolving fast | 0.625 |
| Publication Types | III–IV | Mostly operations/install guides; some "focused on use" case studies | 0.750 |
| Market | III | Growing, not yet mature | 0.625 |
| Market Perception | III | Increasing expectations of use | 0.625 |
| User Perception | III | Common; teams disappointed when not available | 0.625 |
| Perception in Industry | III | Advantage through implementation quality | 0.625 |

Unweighted mean:

$$\varepsilon(\text{K8s}) = \frac{0.875 + 0.625 + 0.750 + 0.625 + 0.625 + 0.625 + 0.625}{7} \approx 0.679$$

Disagreement across the 7 rows, using the unrounded mean $\bar m$:

$$H = \tfrac{1}{7}\bigl[(0.875-\bar m)^2 + (0.750-\bar m)^2 + 5(0.625-\bar m)^2\bigr] \approx 0.008291.$$

Thus the plotting seed is approximately 0.679 and the row standard deviation is approximately 0.091. This describes the characteristic spread; it is not a confidence interval or a justified narrow Beta prior. The example is an illustrative 2025 assessment, not a current market measurement; its source quality and mapper agreement would need separate assessment.

---

## 5. Caveats

1. **Market-relative ubiquity.** Wardley: "you need to understand the applicable market first." A component that is "widespread" in enterprise but "rare" in consumer gets different Ubiquity scores in different maps. Name your market before you score.

2. **Stages are conventions, not quartiles.** The band midpoints $m(s) \in \{0.125, 0.375, 0.625, 0.875\}$ assume a uniform quartile partition of $[0,1]$. Wardley does not fix the boundaries at exact quartiles. If your dataset calibrates differently, adjust $m(s)$.

3. **Not a forecast.** The cheat sheet tells you *where a component is now*, not where it is going. For movement, see Part 1 §5 (dynamics) — but remember the climatic pattern *"you cannot measure evolution over time or adoption."*

4. **Disagreement is a diagnostic.** A mixed profile may indicate transition or conflicting evidence. Preserve that profile, and assess confidence separately.

5. **The mapper still owns the result.** Cheat-sheet scoring is more disciplined than a gut call, but it's still a judgment. The table is a prompt to think across 19 dimensions, not a calculator that removes the mapper.
