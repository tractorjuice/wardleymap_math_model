# Cybersecurity Risk Management — Executive View (May 2023)

A Wardley Map from the executive / board perspective, covering the governance drivers (P&L, compliance, risk appetite), the assessment apparatus (identification, inventory, registers, methodology, FAIR, likelihood-impact, matrices, frameworks), the treatment mix (mitigate / transfer / accept) and cyber insurance, the operational stack (monitoring, SOC, reporting, IR, pen test, bug bounty, security testing), and the emerging LLM angle on both sides of the fence.

Generated following `prompts/wardley_map_generator.md` — formal model M = (V, E, U, ν, ε, t), cheat-sheet scoring for ε, distance-seeded ν with value-chain overrides.

---

## 1. Model

- **U (anchor):** `Executives` — the board / CEO / CFO / CISO-to-board interface. Single anchor; the cybersecurity function exists in service of this user.
- **V:** 38 components across 7 layers (drivers → governance → assessment → ops → tooling → LLM angle → infra).
- **E:** directed dependency graph; all edges respect the visibility constraint ν(a) ≥ ν(b).
- **ν (Y):** seeded by distance from `Executives`, then lifted where executives think directly about the component (e.g., `Cyber Insurance`, `Compliance Frameworks`) and pushed down where it is architecturally invisible (foundation LLM APIs, telemetry pipelines).
- **ε (X):** four-row cheat-sheet placement, described component-by-component below.
- **t:** May 2023.

## 2. OWM Output

See `draft.owm`.

## 3. Evolution — cheat-sheet reasoning (condensed)

| Component | Ubiquity | Certainty | User-perception | Publication | Stage | ε |
|---|---|---|---|---|---|---|
| P&L Impact Decision | III | III | III | III | III | 0.62 |
| Risk Appetite | II | II | II | II | II | 0.35 — still "leading-edge" as a quantified, dashboarded concept |
| Compliance Obligation | III | III | III | III | III | 0.58 |
| Board Risk Reporting | III | III | III | III | III | 0.55 |
| Risk Treatment Mix | II-III | II | III | II | II-III | 0.45 |
| Cyber Insurance | III | III | III | III | III | 0.62 — 2023 was the **hard-market** year, still fit-for-purpose but being re-underwritten |
| Compliance Frameworks (ISO/SOC2/NIST CSF) | IV | IV | IV | IV | IV | 0.78 |
| Regulatory Frameworks (GDPR/DORA/NIS2/SEC) | III-IV | III | III | III | III-IV | 0.70 — GDPR mature, DORA/NIS2/SEC-cyber still rolling out in 2023 |
| Risk Register | IV | IV | IV | IV | IV | 0.72 — a generic concept but still often run in spreadsheets |
| Risk Assessment Methodology | III | II | III | III | III | 0.55 |
| Risk Identification Practice | II-III | II-III | III | II | II-III | 0.50 |
| Risk Quantification (FAIR) | II | II | II | II | II | 0.28 — named, but still expert-judgement-heavy |
| Likelihood/Impact Scoring | IV | III | IV | III | III-IV | 0.70 |
| Risk Matrix (Heatmap) | IV | IV | IV | IV | IV | 0.80 — widespread, arguably a **doctrine liability**, hence inertia marker |
| Asset Inventory | III | III | III | III | III | 0.65 — CMDB products exist, but real-world coverage is patchy |
| Threat Intelligence | II-III | II-III | III | II-III | II-III | 0.55 |
| Security Reporting / Dashboards | III-IV | III | III | III-IV | III | 0.72 |
| Incident Response Process | III | III | III | III | III | 0.55 |
| SOC | III | III | III | III | III | 0.62 |
| Continuous Monitoring | IV | III | IV | IV | III-IV | 0.74 |
| Pen Testing | III | III | III | III | III | 0.68 — productised but still bespoke engagement |
| Bug Bounty | II-III | III | II-III | III | II-III | 0.55 — HackerOne/Bugcrowd make it a product; enterprise adoption still growing |
| Red / Purple Team | II | II | II | II | II | 0.38 |
| Security Testing (SAST/DAST) | IV | IV | IV | III-IV | IV | 0.75 |
| SIEM | III-IV | III-IV | IV | III-IV | III-IV | 0.72 |
| EDR / XDR | III-IV | III | IV | III-IV | III-IV | 0.70 |
| Vulnerability Scanning | IV | IV | IV | IV | IV | 0.85 |
| IAM | IV | IV | IV | IV | IV | 0.82 |
| CSPM | III | III | III | III | III | 0.60 |
| **LLM-Augmented Defence** | **I** | **I-II** | **I** | **I** | **I** | **0.18** — in May 2023, Microsoft Security Copilot was preview-only, most SOC copilots were hackathon demos |
| **LLM-Assisted Threat** | **I** | **I-II** | **I** | **I** | **I** | **0.15** — WormGPT not public until Jul 2023; evidence of LLM-crafted phishing anecdotal |
| Foundation LLM APIs | III | III | III | III | III | 0.55 — OpenAI + Anthropic GA but pricing/quota still shifting |
| Log / Telemetry Pipeline | IV | IV | IV | IV | IV | 0.78 |
| Cloud Compute & Storage | IV | IV | IV | IV | IV | 0.92 |
| Network / Firewall Infra | IV | IV | IV | IV | IV | 0.88 |

## 4. Strategic Analysis

### (a) Top 3 by **D (differentiation pressure)** — D = ν·(1−ε)

| Rank | Component | ν | 1−ε | D |
|---|---|---|---|---|
| 1 | **Risk Appetite** (quantified, dashboard-grade) | 0.90 | 0.65 | **0.585** |
| 2 | **Risk Assessment Methodology** | 0.66 | 0.45 | **0.297** |
| 3 | **Risk Quantification (FAIR)** | 0.58 | 0.72 | **0.418** — actually #2 on raw numbers |

Corrected ranking: **Risk Appetite (0.585), FAIR (0.418), Risk Assessment Methodology (0.297)**.

**Why these three.** The executive's primary lever — "how much risk do we tolerate, priced in P&L terms" — remains **expert judgement**, not product. FAIR is the only serious attempt to quantify it with a named methodology, and it's still Stage II: known, growing, but not in a turnkey product a CFO trusts. The assessment methodology itself sits above FAIR and is where differentiated firms distance themselves from heatmap-theatre.

### (b) Top 3 by **K (commodity leverage)** — K = (1−ν)·ε

| Rank | Component | 1−ν | ε | K |
|---|---|---|---|---|
| 1 | Cloud Compute & Storage | 0.92 | 0.92 | 0.846 |
| 2 | Network / Firewall Infra | 0.90 | 0.88 | 0.792 |
| 3 | Vulnerability Scanning | 0.76 | 0.85 | 0.646 |

**Action:** buy-as-utility. No CISO should be building their own VM scanner, firewall, or S3 equivalent. Tick-box decisions — the interesting question is which SaaS supplier.

### (c) Top 3 dependency risks **R(a,b) = ν(a)·(1−ε(b))**

| Rank | Edge | ν(a) | 1−ε(b) | R | Why it matters |
|---|---|---|---|---|---|
| 1 | Risk Appetite → Risk Treatment Mix | 0.90 | 0.55 | 0.495 | Executives act on a Stage-II treatment concept |
| 2 | Risk Register → Risk Quantification (FAIR) | 0.72 | 0.72 | 0.518 | Board register inheriting immature quantification |
| 3 | Risk Assessment Methodology → Risk Quantification (FAIR) | 0.66 | 0.72 | 0.475 | Same root cause — the methodology rests on immature quant |

The pattern is that **executive-visible risk figures rest on genuinely immature quantification practice** — the single biggest doctrine problem in cyber risk as of May 2023. The #2 and #3 share a root cause: FAIR.

A fourth risk worth calling out: `SOC → LLM-Augmented Defence` (R ≈ 0.44 × 0.82 = 0.36) — if SOC workflows rebuild around copilots while the copilots are Genesis, hallucination and prompt injection risk is being absorbed into the IR pipeline.

### (d) Suggested gameplays (from the 61-play catalogue)

| Play | Target component(s) | Reason |
|---|---|---|
| **Open Approaches** (#15) | Risk Quantification (FAIR), Risk Matrix | The FAIR Institute is already semi-open. Pushing open reference datasets accelerates its move toward Stage III and reduces the #1/#3 dependency risks above. |
| **Buy** (#36, directed investment) | SIEM, EDR/XDR, CSPM, IAM | Standard: these are Stage III-IV; only build the **integration glue**. |
| **Embrace & Extend** (#24) | LLM-Augmented Defence | Take Stage-III vendor SOC copilots, embed in your IR runbooks, extend with internal knowledge — a cheap defensible position before the category matures. |
| **Weak Signal** (#31 / #47) | LLM-Assisted Threat | Track the threat's evolution; invest in phishing detection retraining and code-supply-chain monitoring. In May 2023 this is still Genesis — the cheap time to prepare. |
| **Pig in a Poke** / **Pre-emptive purchase** (#41) | Cyber Insurance | Hard-market 2023 — lock in coverage and negotiate policy language now, before forced maturity pushes premiums further. |
| **Industrialisation** (#43) | Risk Matrix (Heatmap) | Candidate for deliberate **retirement**, not industrialisation — replace with FAIR-style loss-exceedance curves. |
| **Pressure on Supplier** (#14) | Compliance Frameworks, Regulatory Frameworks | Influence ISO/NIST working groups so the standards don't over-specify Stage II practices as mandatory. |

### (e) Doctrine observations

- **Doctrine #1 (Focus on user needs)** — anchor is `Executives`, and the scenario asks for the executive view. This is correct. But a real CISO map should also carry a `Customer` or `Regulator` anchor — regulators are increasingly co-users of risk reporting under DORA, NIS2, and the SEC 8-K rules.
- **Doctrine #4 (Use a common language / map)** — `Risk Matrix` is marked **inertia**: it's a Stage-IV widespread artefact that's *actively harmful* at the scale most firms use it (Cox, Hubbard). Retiring it requires replacing a shared language, not just a tool.
- **Doctrine #12 (Think small)** — the LLM-Augmented Defence row is one place to *deliberately* keep teams small and exploratory; don't burden with SOC-integration SLAs before the category stabilises.
- **Doctrine #17 (Know your user's needs better than they do)** — the board may ask for a single "cyber risk score". Giving them one (a heatmap cell) is compliance-with-request but doctrine-violating; giving them a loss-exceedance curve is harder but right.
- **Gap (Knowledge layer)** — this map under-specifies *Knowledge* (K in the τ extension): the actuarial basis under FAIR, the threat-model taxonomies under TI, the statistical basis under likelihood/impact. A future version should colour those nodes explicitly (per `docs/extensions/component-types.md`).

## 5. What's commoditised, what's still expert judgement, where regulation forces shape

- **Commoditised (ε > 0.75, buy-as-utility):** Cloud Compute, Network/Firewall Infra, Vulnerability Scanning, IAM, Compliance Frameworks artefacts, Risk Matrices (unfortunately), Log/Telemetry Pipeline, SAST/DAST, Continuous Monitoring, SIEM baseline, Risk Register.
- **Still product-grade but not commodity (ε 0.5–0.75):** SOC, EDR/XDR, Pen Testing, CSPM, Cyber Insurance, Asset Inventory, Risk Assessment Methodology, P&L Impact, Board Reporting, Incident Response, Regulatory Frameworks.
- **Expert judgement / pre-product (ε < 0.5):** Risk Appetite (strategic framing), FAIR quantification, Red/Purple Team, LLM-Augmented Defence, LLM-Assisted Threat, Risk Treatment Mix (as an optimised portfolio).
- **Regulation forcing shape:** GDPR already mature; DORA (Jan 2025 live in EU), NIS2 (Oct 2024 live), SEC cyber-disclosure rule (proposed Mar 2022, adopted Jul 2023) are **pulling the compliance and reporting stack rightward** — forcing ISO 27001/SOC 2 artefacts, IR playbooks, and board reporting to industrialise. The DORA angle in particular is forcing `Cyber Insurance`, `Incident Response`, and `Third-Party Risk` to co-evolve.

## 6. Map caveats

- Single anchor (executives) — this is deliberate per the scenario, but be aware a full CISO map would also carry Regulator and Customer anchors.
- LLM nodes are placed on May-2023 evidence: foundation-model APIs available, but defence copilots were preview-grade. Placement should re-baseline quarterly.
- FAIR's placement at ε=0.28 is contested; some practitioners would argue Stage III. Kept at II to reflect **true enterprise adoption**, not methodology maturity.
- Evolution movements are **scenarios, not forecasts** — Wardley's climatic pattern explicitly warns against time/adoption-based evolution claims.
