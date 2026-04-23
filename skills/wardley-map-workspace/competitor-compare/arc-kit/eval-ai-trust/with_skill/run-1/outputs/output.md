# AI Trust Landscape — June 2023

**Anchor:** Stakeholder (individual, government, business)
**User need:** Trust in AI systems (i.e. belief that AI outputs and decisions are safe, accurate, fair, auditable, and accountable).
**Scope:** Cross-industry AI governance and deployment, covering technical substrate, governance apparatus, control mechanisms, and outcomes.
**Date:** 2023-06.

## Map

See `draft.owm` for the OnlineWardleyMaps source. A visual rendering (axes):

```text
                        Genesis        Custom-Built     Product        Commodity
                        (0.00-0.25)    (0.25-0.50)      (0.50-0.75)    (0.75-1.00)

Anchor (Stakeholder) ------------------------*----------------
                                              0.55

Visible
                                     Trust *
                                        *  Safety, Reputation, CompAdv
                                     (outcomes cluster)

                            Policy *
                            Regs  *
                            Audits *

                            Benchmarks      *
                            Safety bench  *
                            Red team        *
                            Const. AI *
                            Forensics *

                                                  * Foundation models
                                                            * Algorithms
                                                            * Training data
Hidden                                                                 * Compute
```

## Components — positioning and sourcing

| # | Component | Visibility | Evolution | Stage | Sourcing signal |
|---|-----------|-----------|-----------|-------|-----------------|
| 1 | Trust in AI systems | 0.90 | 0.20 | Genesis/Custom | Meta-need — cannot be "built" directly |
| 2 | Safety (outcome) | 0.82 | 0.18 | Genesis/Custom | Emergent property; no standards body |
| 3 | Reputation (outcome) | 0.82 | 0.35 | Custom-Built | Shaped by brand + audit behaviour |
| 4 | Competitive advantage (outcome) | 0.82 | 0.50 | Custom/Product boundary | Shifts as models commoditise |
| 5 | Regulations | 0.70 | 0.22 | Genesis/Custom | EU AI Act in trilogue; US EO not yet signed |
| 6 | Policy and sector guidance | 0.72 | 0.30 | Custom-Built | National AI strategies proliferating |
| 7 | Audits (AI assurance) | 0.58 | 0.15 | Genesis | Handful of firms; no ISO standard |
| 8 | Benchmarks (evals: HELM, MMLU, BIG-Bench) | 0.55 | 0.38 | Custom-Built | Fragmented; leaderboard-driven |
| 9 | Safety benchmarks (TruthfulQA, RealToxicityPrompts, etc.) | 0.52 | 0.30 | Custom-Built | Emerging, contested |
| 10 | Red teaming and feedback loops (incl. RLHF) | 0.48 | 0.42 | Custom-Built (moving) | Patterns from OpenAI/Anthropic papers |
| 11 | Constitutional AI | 0.44 | 0.10 | Genesis | Dec 2022 Anthropic paper; few replications |
| 12 | Forensics (provenance, watermarking, deepfake detection) | 0.40 | 0.12 | Genesis | C2PA starting; watermarking unreliable |
| 13 | Foundation models (GPT-4, Claude, PaLM-2, LLaMA) | 0.35 | 0.55 | Product | Multiple vendors, feature competition |
| 14 | Training data (Common Crawl, C4, RedPajama) | 0.22 | 0.70 | Product/Commodity | Shared corpora dominant |
| 15 | Algorithms (transformer + RLHF techniques) | 0.18 | 0.62 | Product | Training recipes public since GPT-3 paper |
| 16 | Compute (GPU / cloud) | 0.08 | 0.88 | Commodity | Hyperscaler utility (AWS/Azure/GCP); H100 shortage tightens supply temporarily |

## Step 5 — Analysis

### Completeness

- Anchor clearly defined (three stakeholder classes collapsed into one anchor for a single map).
- Technical substrate, governance apparatus, control mechanisms, outcomes all represented.
- Dependencies drawn downward; visibility constraint $\nu(a) \ge \nu(b)$ preserved for every edge.
- Movement arrows (evolve statements) added for the seven components most likely to shift over the next 12-24 months.

### Positioning rationale

- **Compute** is utility; the GPU shortage of 2023 is a supply shock, not a reversal of commoditisation.
- **Algorithms and training data** are Product-stage: training stacks (Megatron, FSDP) and corpora (Common Crawl, C4) are shared commons.
- **Foundation models** are mid-Product: GPT-4, Claude, PaLM-2 compete on features; open-weights (LLaMA, Falcon) accelerate commoditisation but each model still ships with proprietary RLHF data and safety tuning.
- **Red teaming / RLHF** is Custom-Built but has textbook patterns and is moving toward Product as third parties (Scale, Surge) productise the service.
- **Constitutional AI, forensics, audits** are genuinely Genesis — no standard, few practitioners, high variance.
- **Regulations and policy** are governance artefacts. Treated as components because stakeholders depend on them to establish trust; positioned Custom-Built because drafts exist but nothing is operational at scale in June 2023 (EU AI Act not yet finalised).

### What's differentiating — apply Differentiation Pressure $D(v) = \nu \cdot (1 - \varepsilon)$

| Component | $\nu$ | $\varepsilon$ | $D(v)$ | Reading |
|-----------|------|--------|--------|---------|
| Trust in AI systems | 0.90 | 0.20 | **0.72** | High — the meta-outcome every vendor is fighting for |
| Safety (outcome) | 0.82 | 0.18 | **0.67** | High — commercial winners will be those who can demonstrate safety |
| Reputation (outcome) | 0.82 | 0.35 | 0.53 | Moderate-high — brand-led |
| Regulations | 0.70 | 0.22 | 0.55 | Moderate-high — first-mover governance wins influence |
| Policy and sector guidance | 0.72 | 0.30 | 0.50 | Moderate-high |
| Audits | 0.58 | 0.15 | 0.49 | Moderate — whoever defines the audit standard wins the category |
| Benchmarks | 0.55 | 0.38 | 0.34 | Moderate — HELM-like works differentiate |
| Red teaming / feedback loops | 0.48 | 0.42 | 0.28 | Low-moderate — becoming tablestakes |
| Constitutional AI | 0.44 | 0.10 | **0.40** | Moderate — Anthropic's differentiator today; likely to diffuse |
| Forensics | 0.40 | 0.12 | 0.35 | Moderate — huge latent value, no winner yet |

**Differentiating today:** constitutional AI techniques, model-specific RLHF datasets, audit methodology, safety benchmark authorship, forensics tooling. Companies that own **defensible intellectual property in any of these** will still matter after the models themselves commoditise.

### What's commoditising — apply Commodity Leverage $K(v) = (1 - \nu) \cdot \varepsilon$

| Component | $\nu$ | $\varepsilon$ | $K(v)$ | Reading |
|-----------|------|--------|--------|---------|
| Compute (GPU/cloud) | 0.08 | 0.88 | **0.81** | Very high — consume as utility |
| Training data | 0.22 | 0.70 | 0.55 | Moderate-high — shared corpora dominate |
| Algorithms | 0.18 | 0.62 | 0.51 | Moderate-high — open research, open code |
| Foundation models | 0.35 | 0.55 | 0.36 | Moderate — open-weights accelerate this |

**Commoditising:** compute, training data, transformer recipes, and — over the next 12-24 months — foundation models themselves. The `evolve Foundation models 0.75` arrow signals a shift from Product toward Commodity, driven by open-weights and by inference APIs converging on OpenAI-compatible standards.

### Where trust is fragile — apply Dependency Risk $R(a,b) = \nu(a) \cdot (1 - \varepsilon(b))$

| Trust-critical edge | $R$ | Why it's fragile |
|--------------------|-----|------------------|
| Safety → Forensics | 0.82 × 0.88 = **0.72** | High-visibility safety outcome depends on Genesis-stage forensics |
| Safety → Constitutional AI | 0.82 × 0.90 = **0.74** | Same: safety riding on a 6-month-old technique |
| Safety → Safety benchmarks | 0.82 × 0.70 = **0.57** | Moderate: benchmarks exist but contested |
| Reputation → Audits | 0.82 × 0.85 = **0.70** | Reputation depends on an audit ecosystem that barely exists |
| Trust → Regulations | 0.90 × 0.78 = **0.70** | Trust waiting on governance artefacts that aren't operational yet |
| Trust → Audits | 0.90 × 0.85 = **0.76** | Highest — no mature third-party assurance |

**The five fragilities:**

1. **Audit gap.** Reputation and trust both depend on AI audits (visibility 0.58, evolution 0.15). There is no equivalent of SOC 2 for AI systems in June 2023. A single high-profile model failure with no independent audit trail will shake trust across the sector.
2. **Forensics are Genesis.** Watermarking is defeatable, C2PA provenance is not widely deployed, deepfake detection is a cat-and-mouse arms race. When safety is tested, forensics won't answer the question "what did the model actually do, when, on what inputs?"
3. **Regulatory lag.** Regulations ($\varepsilon = 0.22$) are behind foundation models ($\varepsilon = 0.55$). The EU AI Act is in trilogue but not yet enforced; the US has only voluntary White House commitments. The gap between capability and governance is the widest it has ever been.
4. **Benchmark fragility.** Benchmarks (0.38) are more mature than the safety benchmarks that feed them (0.30) and are already being gamed. A public eval becomes a training set within weeks. Trust built on leaderboard numbers is pre-revealed.
5. **Constitutional AI is one paper deep.** Only Anthropic has deployed it at scale; the technique has not been independently validated on other model families at publication date. It is positioned as a trust mechanism but is Genesis-stage.

### Inertia points

| Component | Inertia source | Manifestation |
|-----------|----------------|---------------|
| Regulations | Political process speed; jurisdictional fragmentation | EU AI Act slow to finalise; US federal inaction |
| Policy | National security anxieties, incumbency protection | Conflicting strategies (US, EU, UK, China) |
| Foundation models | Vendor lock-in on RLHF tuning, safety rails, retrieval APIs | Harder to swap than the model weights alone suggest |
| Training data | Copyright litigation (NYT vs. OpenAI in motion) | May force data provenance retrofits |

### Climatic patterns in play

- **Everything evolves** (all components on the map are moving — the question is rate, not direction).
- **Efficiency enables innovation**: commodity compute and commodity foundation models enable the genesis-stage work in audits, forensics, and constitutional AI to emerge at all.
- **Higher-order systems create new value**: trust, safety, audits are higher-order components built on commoditising lower layers.
- **No choice over evolution (Red Queen)**: proprietary model moats are thinning; differentiation must shift to the control + outcome layers.
- **Rates vary by ecosystem**: the consumer-facing AI ecosystem is evolving at the fastest rate in tech history; the regulatory ecosystem runs at the pace of legislatures. The gap is the single most important feature of the map.

### Gameplay patterns worth considering

- **Open source play** on training data and algorithms (already happening: RedPajama, LLaMA release) — accelerates commoditisation of the lower layers.
- **Open approach / standards setting** on benchmarks, audits, and forensics — whoever authors the standards wins the category. MLCommons, C2PA, NIST AI RMF are already in this move.
- **Education** to establish Constitutional AI, RLHF, and safety techniques as vocabulary — early trust-leader advantage.
- **Lobbying / Counterplay** (watch for it) — incumbents may shape regulations to raise barriers to open-weights challengers. EU AI Act drafts have been pulled in both directions during 2023.
- **Pig in a poke** risk for buyers: paying for "safety" or "alignment" where the underlying components are still Genesis and effectiveness is unproven.

## Recommendations

### Immediate (next 3-6 months)

1. **Audit instrumentation.** If you are a deployer: log every prompt, response, model version, and RLHF update. The audit standard is coming; having the data is prerequisite.
2. **Don't buy safety theatre.** Demand evidence of red-team results, eval coverage, and failure-mode catalogues from vendors — not "constitutional AI" marketing.
3. **Track the EU AI Act trilogue weekly.** High-risk designation will reshape the Policy/Regulations layer with direct cost implications for foundation model deployers.

### Short-term (6-18 months)

1. **Invest where differentiation pressure is high** ($D > 0.4$): audits, benchmarks (especially safety), forensics, and domain-specific RLHF datasets. These are the future moats.
2. **Consume commoditising layers** ($K > 0.5$): don't train your own foundation model unless that is your product. Use inference APIs and fine-tune.
3. **Build redundancy across models.** With Foundation models moving from Product (0.55) toward Commodity (0.75), lock-in risk is rising-then-falling; architect for model portability.

### Long-term (18+ months)

1. **Own the control layer.** The durable advantage is in forensics, provenance, and audit methodology, not in model weights.
2. **Expect a trust crisis.** The map's fragilities (audit gap, forensics Genesis, regulatory lag) compound. One high-profile incident — model misuse in an election, a hallucinated medical recommendation, a deepfake fraud — will accelerate evolution of regulations and audits simultaneously. Position to benefit from that acceleration, not to be caught by it.
3. **Constitutional AI and red teaming will productise.** Treat today's Genesis/Custom components as tomorrow's Products. The second-wave winners will be those who industrialised these practices before the vendors did.

## Summary: the three questions

- **What's differentiating?** Constitutional AI, audit methodology, safety-benchmark authorship, forensics, domain-specific RLHF datasets, regulatory first-mover positioning.
- **What's commoditising?** Compute, training corpora, transformer algorithms, and — within 18 months — foundation models themselves.
- **Where is trust fragile?** Everywhere above the Foundation-models layer depends on Genesis-stage components (audits, forensics, constitutional AI) or on lagging governance artefacts (regulations not yet operational). The trust narrative is held up by scaffolding that has not yet been tested. A single high-profile failure, with no audit trail to explain it, could puncture the whole layer.
