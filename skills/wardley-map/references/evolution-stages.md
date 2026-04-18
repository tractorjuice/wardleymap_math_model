# Evolution Stages and the Cheat Sheet

Wardley's four evolution stages and the 19-row cheat sheet used to place components precisely. This file is the canonical reference for the X-axis of every Wardley Map.

---

## The four stages

### I — Genesis

**Range:** ε ∈ [0, 0.25)
**Characteristic word:** *rare*

Novel, poorly understood, high-risk. The component has just been created or newly discovered. Few people know it exists; those who do don't agree on what it's for. The thing might fail, the market might not exist, the economics are unclear. But the potential upside is enormous — this is where differentiation lives.

**Examples (at the time of their Genesis):**
- Electricity (1800s)
- Computing (1940s)
- The web (early 1990s)
- Deep learning (early 2010s)
- Generative AI agents (2022–)

**Management style:** experimental, agile, hypothesis-driven. Use FIRE (fast, inexpensive, restrained, elegant) from doctrine. Small teams, fast iteration, tolerance for failure.

**What fails here:** rigid project plans, six sigma, market research (there's no market yet).

### II — Custom Built

**Range:** ε ∈ [0.25, 0.5)
**Characteristic word:** *emerging*

The component is being built bespoke for specific customers. It works, but every implementation is unique. There are no off-the-shelf products; you hire specialists and they custom-develop.

**Examples (at the time):**
- Early electrical systems (custom wiring per building)
- Early software (custom per client)
- Early cloud services pre-AWS (every company built their own)

**Management style:** still agile, still learning, but with more process. Teams are larger, methods are more consistent, case studies start to accumulate.

**What fails here:** trying to productise too early; trying to commoditise before patterns have emerged.

### III — Product (+rental)

**Range:** ε ∈ [0.5, 0.75)
**Characteristic word:** *rapidly increasing consumption*

The component is now sold as a product, potentially with rental/licensing variants. Feature competition is fierce. Multiple vendors exist. Consumption is growing fast. Users expect it to work and are disappointed when it doesn't.

**The "+rental" suffix matters:** Stage III covers both traditional products (buy-and-own) AND rental/subscription business models for the same thing. Salesforce (SaaS) and SAP (on-prem product) are both Stage III — different business models for the same evolution stage.

**Examples:**
- Personal computers in the 1990s
- Enterprise software (CRM, ERP) in the 2000s–2010s
- Mobile apps (most major categories)

**Management style:** lean, feature-driven, market-analysis-heavy. Listen to customers; iterate on what exists. Management-by-metrics starts being useful.

**What fails here:** ignoring feature expectations; assuming users are still excited by novelty.

### IV — Commodity (+utility)

**Range:** ε ∈ [0.75, 1.0]
**Characteristic word:** *widespread and stabilising*

Fully standardised. Feature differentiation barely matters; customers care about price, reliability, and availability. Think of it as a utility — electricity, water, cloud compute, payment rails.

**The "+utility" suffix matters:** Stage IV covers traditional commodities (interchangeable goods) AND utility services (metered access to a shared resource). Electricity, Twilio, and Stripe are all Stage IV — the latter two are utility-model commodities.

**Examples:**
- Electricity, water
- Cloud compute (AWS EC2, GCP)
- Payment processing rails
- DNS
- CDN services

**Management style:** six sigma, operational excellence, ruthless efficiency, metric-driven. Innovation is not the game; reliability and cost are.

**What fails here:** trying to differentiate on features; agile experimentation (it's too expensive at scale); not treating it as a utility.

---

## The 19-row cheat sheet

Simon Wardley's full characteristic table. For each row, pick the stage that best describes the component in that dimension.

Source: Simon Wardley's Medium book, Figure 17 in [*Finding a Path*](https://medium.com/wardleymaps/finding-a-path-cdb1249078c0), and [*What's in a Wardley Map and the need for a cheat sheet*](https://blog.gardeviance.org/2016/04/whats-in-wardley-map-and-need-for-cheat.html).

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
| 11 | **User Perception** | Different / confusing / exciting / surprising | Leading edge / emerging | Common / disappointed if not used | Standard / expected |
| 12 | **Perception in Industry** | Competitive advantage / unpredictable / unknown | Competitive advantage / ROI / case examples | Advantage through implementation / features | Cost of doing business / accepted |
| 13 | **Focus of Value** | High future worth | Seeking profit / ROI? | High profitability | High volume / reducing margin |
| 14 | **Understanding** | Poorly understood / unpredictable | Increasing understanding / development of measures | Increasing education / refinement of needs | Believed well defined / stable / measurable |
| 15 | **Comparison** | Constantly changing / unstable | Learning from others / some evidential support | Feature difference | Essential / operational advantage |
| 16 | **Failure** | High / tolerated / assumed | Moderate / unsurprising but disappointed | Not tolerated, constant improvement | Operational efficiency, surprised by failure |
| 17 | **Market Action** | Gambling / driven by gut | Exploring a "found" value | Market analysis / listening to customers | Metric driven / build what is needed |
| 18 | **Efficiency** | Reducing cost of change (experimentation) | Reducing cost of waste (learning) | Reducing cost of waste (learning) | Reducing cost of deviation (volume) |
| 19 | **Decision Drivers** | Heritage / culture | Analysis & synthesis | Analysis & synthesis | Previous experience |

### Row subsets

You don't always need all 19 rows. Common subsets:

- **Quick (4 rows):** #5 Ubiquity, #6 Certainty, #11 User Perception, #7 Publication Types. Covers the dimensions Wardley emphasises most.
- **Activity-focused (7 rows):** rows 5–11. Drops the type-label rows (Activities/Practices/Data/Knowledge) and the organisational-decision rows at the bottom.
- **Full (19 rows):** use when precision matters, e.g., workshop-grade placement of a strategically important component.

---

## Scoring procedure

### Per-row

For each row `r` you use, pick the stage `s_r ∈ {1, 2, 3, 4}` that best describes the component.

Convert to band midpoint:

```
m(s) = (s - 0.5) / 4
```

So:
- Stage I → 0.125
- Stage II → 0.375
- Stage III → 0.625
- Stage IV → 0.875

### Aggregate

Unweighted mean:

```
ε(v) = (1 / |R|) · Σ m(s_r)
```

Or weighted:

```
ε(v) = Σ w_r · m(s_r),   Σ w_r = 1
```

The unweighted case is the sensible default. Weight only if you have domain reason (e.g., for a B2C consumer product, weight #11 User Perception more heavily).

### Uncertainty

Variance across rows:

```
Var(ε) = (1 / |R|) · Σ (m(s_r) - ε)²
```

High variance means the rows disagree — the component is either in transition (e.g., ubiquity has jumped but certainty hasn't caught up) or the mapper is uncertain. Plot as a range, not a point.

---

## Worked examples

### Example A: "Payment processing" in 2026

Quick 4-row scoring:

| Row | Stage | Reasoning | m(s) |
|---|---|---|---|
| Ubiquity | IV | Universal in e-commerce | 0.875 |
| Certainty | IV | Stripe/PSP patterns well-understood | 0.875 |
| User Perception | IV | Expected; disappointed if missing | 0.875 |
| Publication Types | IV | Focused on use (integrations, best practice) | 0.875 |

Unweighted mean: **ε = 0.875** (solidly Commodity/utility). Variance: 0 — all rows agree.

Placement: top-right-ish, well into Stage IV. Build/buy: definitely **buy** (Stripe, Adyen, etc.).

### Example B: "AI copilot for invoice reconciliation" in 2026

7-row scoring:

| Row | Stage | Reasoning | m(s) |
|---|---|---|---|
| Ubiquity | II | A few vendors have it; not universal | 0.375 |
| Certainty | II–III | Methods emerging; some proven | 0.500 |
| Publication Types | II | Build/construct, case studies | 0.375 |
| Market | II | Forming | 0.375 |
| Market Perception | II | Domain of ML experts | 0.375 |
| User Perception | II | Leading-edge; cautiously excited | 0.375 |
| Perception in Industry | II | Competitive advantage | 0.375 |

Mean: **ε ≈ 0.393** (mid Custom Built). Variance: low except for Certainty which straddles II/III — flag as "in transition".

Placement: left-of-centre. Build/buy: **build** (it's still where you can differentiate). Expect this to move to Stage III in 2–3 years as vendors mature.

### Example C: "Cup of Tea" (Tea Shop map)

Quick 4-row scoring:

| Row | Stage | Reasoning | m(s) |
|---|---|---|---|
| Ubiquity | IV | Everyone knows a cup of tea | 0.875 |
| Certainty | III | Generally understood; specialist variations exist | 0.625 |
| User Perception | III | Common; expected | 0.625 |
| Publication Types | III–IV | Recipes, guides, lifestyle | 0.750 |

Mean: **ε ≈ 0.72** (late Product, edging toward Commodity). Variance: low.

Placement: the cup of tea itself is near-commodity; the *experience* (service, hospitality) is where differentiation lives — that's a separate Stage II–III component.

---

## Stage transitions — signals to watch

| From → To | Signals |
|---|---|
| Genesis → Custom | Early adopters beyond the inventor; first case studies; "is this real?" questions stop |
| Custom → Product | First productised offerings appear; vendor consolidation begins; implementation patterns emerge |
| Product → Commodity | Price competition intensifies; feature differentiation matters less; utility providers emerge; metrics replace anecdotes |
| Commodity (stable) | Few new entrants; price-per-unit trending down; regulation emerges |

A **war** (punctuated equilibrium transition, climatic pattern #27) is typically Product → Commodity. Watch for it when you see:

- Open-source alternatives appearing (climatic pattern accelerator; gameplay #15)
- A major utility provider (AWS, Stripe) entering the space
- Regulatory standardisation
- Media shift from "wonder" / "feature comparison" → "industry analyst reports about consolidation"

---

## Caveats

1. **Market-relative ubiquity.** Wardley's own caution: *"you need to understand the applicable market first"*. "Widespread in enterprise" is a different score from "widespread for consumers". Always name the market.

2. **Row 19 oddity.** "Heritage / culture" at Genesis and "Previous experience" at Commodity is counter-intuitive but reflects Wardley's published table. Some practitioners dispute this row. Read it as: in Genesis you have no data so you fall back on intuition; in Commodity the domain is so settled that you rely on prior art.

3. **Stages are conventions.** The quartile boundaries [0.25, 0.5, 0.75] are conventional; Wardley doesn't fix them precisely. Don't obsess over whether a score of 0.49 vs 0.51 matters — the stage *descriptor* matters more than the exact number.

4. **Not a forecast.** The cheat sheet places a component *now*, not where it's going. Evolution trajectories are scenarios (see `mathematical-models.md` §4 for multi-wave dynamics), not predictions. Wardley's climatic pattern #18 stands: *you cannot measure evolution over time or adoption*.

5. **Components can be multi-valued.** A component like "Kubernetes" can legitimately be Stage III for a large enterprise and Stage IV for a mature cloud-native team. Score against the specific user/market you're mapping for.

6. **Mapper judgment wins.** The cheat sheet produces a number, but it's a *seed* for judgment, not a verdict. If the score says Stage III but your gut says Stage II — the cheat sheet is an aggregation of proxies, not ground truth. Re-inspect the rows that pushed the score.
