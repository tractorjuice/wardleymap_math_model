# AI Trust Landscape — Wardley Map (June 2023)

**Scenario time-context:** mid-2023. Components are scored as they were understood then — GPT-4 recently released (March 2023), Claude API live, PaLM 2 announced (May 2023), LLaMA-2 not yet out, EU AI Act Parliament position adopted 14 June 2023 with trilogue just beginning, NIST AI RMF out since January, White House voluntary commitments not yet signed, Anthropic's Claude constitution published May 2023.

---

## Map

```owm
title AI Trust Landscape (June 2023)
style wardley

// Three anchors: who needs to trust AI
anchor Individual [0.99, 0.40]
anchor Government [0.98, 0.20]
anchor Business [0.97, 0.45]

// Outcome layer (what "trust" delivers to each user)
component Safety [0.92, 0.18]
component Reputation [0.90, 0.60]
component Competitive Advantage [0.88, 0.35]
component Regulatory Compliance [0.86, 0.15]

// User-facing AI application layer
component AI Product / Service [0.82, 0.40]
component User Consent & Disclosure [0.78, 0.25]

// Governance layer (visible to regulators and boards)
component AI Regulations [0.75, 0.12]
component Voluntary Commitments [0.72, 0.16]
component Policy Frameworks [0.68, 0.18]
component Certifications [0.66, 0.14]
component Third-Party Audits [0.62, 0.12]
component Transparency Reports [0.60, 0.22]

// Control mechanisms (how trust is actually produced)
component Red Teaming [0.58, 0.22]
component Benchmarks & Evals [0.56, 0.42]
component Guardrails & Content Filters [0.54, 0.32]
component Content Provenance / Watermarking [0.52, 0.18]
component Constitutional AI [0.50, 0.10]
component Incident Reporting [0.48, 0.18]
component Interpretability & Forensics [0.46, 0.12]
component Feedback Loops (RLHF pipeline) [0.44, 0.32]

// Technical stack: models and methods
component Fine-tuning Methods [0.42, 0.35]
component Prompting / RAG [0.40, 0.25]
component Foundation Models [0.38, 0.40]
component Training Data [0.34, 0.40]
component Data Curation & Provenance [0.32, 0.30]
component ML Algorithms (Transformers) [0.30, 0.70]

// Deep infrastructure
component Accelerated Compute (GPUs) [0.22, 0.78]
component Cloud Infrastructure [0.18, 0.90]
component Power & Energy [0.10, 0.95]

// Knowledge layer
component AI Safety Research [0.28, 0.15]
component ML Engineering Talent [0.24, 0.35]

// Dependencies (a -> b means "a depends on b")
Individual->AI Product / Service
Individual->Safety
Individual->User Consent & Disclosure
Government->AI Regulations
Government->Safety
Government->Third-Party Audits
Business->AI Product / Service
Business->Reputation
Business->Competitive Advantage
Business->Regulatory Compliance

AI Product / Service->Foundation Models
AI Product / Service->Guardrails & Content Filters
AI Product / Service->Benchmarks & Evals
AI Product / Service->Red Teaming
User Consent & Disclosure->Content Provenance / Watermarking
User Consent & Disclosure->Transparency Reports

Safety->Red Teaming
Safety->Constitutional AI
Safety->Interpretability & Forensics
Safety->Guardrails & Content Filters
Safety->Incident Reporting

Reputation->Transparency Reports
Reputation->Certifications
Reputation->Incident Reporting
Reputation->Benchmarks & Evals

Competitive Advantage->Foundation Models
Competitive Advantage->Fine-tuning Methods
Competitive Advantage->Data Curation & Provenance

Regulatory Compliance->AI Regulations
Regulatory Compliance->Voluntary Commitments
Regulatory Compliance->Policy Frameworks
Regulatory Compliance->Third-Party Audits

AI Regulations->Policy Frameworks
Voluntary Commitments->Policy Frameworks
Third-Party Audits->Benchmarks & Evals
Third-Party Audits->Interpretability & Forensics
Certifications->Third-Party Audits
Transparency Reports->Incident Reporting

Benchmarks & Evals->Foundation Models
Red Teaming->Foundation Models
Red Teaming->AI Safety Research
Constitutional AI->AI Safety Research
Constitutional AI->Feedback Loops (RLHF pipeline)
Content Provenance / Watermarking->Foundation Models
Guardrails & Content Filters->Foundation Models
Interpretability & Forensics->Foundation Models
Interpretability & Forensics->AI Safety Research
Feedback Loops (RLHF pipeline)->Foundation Models
Feedback Loops (RLHF pipeline)->ML Engineering Talent
Incident Reporting->Foundation Models

Foundation Models->ML Algorithms (Transformers)
Foundation Models->Training Data
Foundation Models->Accelerated Compute (GPUs)
Foundation Models->ML Engineering Talent
Fine-tuning Methods->Foundation Models
Fine-tuning Methods->Training Data
Prompting / RAG->Foundation Models
Training Data->Data Curation & Provenance
ML Algorithms (Transformers)->AI Safety Research
Accelerated Compute (GPUs)->Cloud Infrastructure
Cloud Infrastructure->Power & Energy

evolve Foundation Models 0.65
evolve Benchmarks & Evals 0.60
evolve AI Regulations 0.45
evolve Third-Party Audits 0.50
evolve Content Provenance / Watermarking 0.45
evolve Constitutional AI 0.35

note Trust moat / build here [0.60, 0.20]
note Commodity / rent [0.20, 0.88]
note Fragile foundation [0.45, 0.15]
```

---

## Strategic analysis

Three user types sit at the top — an Individual asking "should I believe this output", a Government asking "is this system safe for society and compliant with law", and a Business asking "does using this AI help me without ruining my reputation or exposing me to regulatory risk". Each user's trust in AI depends on a different slice of the chain, but they share a technical floor (Foundation Models, Compute, Data) and a governance ceiling (Regulations, Audits, Certifications).

The striking feature of this map in June 2023 is how much of the trust machinery is still in Genesis. The outcome components — Safety and Regulatory Compliance — are highly visible to users and they sit on a foundation that is mostly Custom Built (the technical stack) or barely-crystallised Genesis (the governance and control layers). That mismatch is what makes trust fragile right now.

### a. Differentiation opportunities (top 3)

1. **Constitutional AI / alignment techniques** (Genesis) — Anthropic published Claude's constitution one month before this map. As a method for producing trustworthy model behaviour without exhaustive human labelling, it is the most uncharted high-leverage component. Visible to safety-conscious enterprise buyers and regulators, and nowhere near commoditised. Highest differentiation pressure in the control layer.
2. **Interpretability & Forensics** (Genesis) — the ability to explain why a model produced a specific output is the linchpin of audits, incident investigations, and regulatory defensibility. No vendor has productised this. Whoever wins it defines the audit category.
3. **Benchmarks & Evals** (Custom Built, edging toward Product (+rental)) — MMLU, HELM, BIG-bench are widely cited but no single benchmark owns the stage; contamination concerns are emerging. A vendor or standards body that produces the canonical "trust-relevant" eval captures enormous influence over procurement decisions.

(Runners-up: Red Teaming as a repeatable practice, and Data Curation & Provenance — both are Custom Built differentiators for teams who can execute.)

### b. Commodity-leverage candidates (top 3)

1. **Cloud Infrastructure** (Commodity +utility) — AWS, Azure, GCP. Rent, don't build. Everyone including OpenAI rents.
2. **Power & Energy** (Commodity +utility) — classic utility; the only AI-trust wrinkle is concentration risk if a single data-centre region loses power, not a build decision.
3. **Accelerated Compute (GPUs)** (Commodity +utility, but with supply shock) — NVIDIA A100/H100 availability was constrained in mid-2023, so the utility thesis has a short-run crack. Still rent, but with second-sourcing (TPU, MI300) on the roadmap. Harvest NVIDIA, watch alternatives.

(ML Algorithms — Transformers — is late Product (+rental): published architectures, open implementations, not worth reinventing. Harvest the open-source stacks like PyTorch/HuggingFace.)

### c. Dependency risks (top 3)

These are edges where a visible component rests on an immature foundation — the dominant risk shape on this map.

1. **AI Product / Service → Foundation Models (Custom Built)** — every deployed AI product depends on a model whose behaviour is not yet fully understood, whose safety properties are emergent rather than engineered, and whose capability surface shifts with each vendor release. This is the risk the Individual feels most directly.
2. **Regulatory Compliance → AI Regulations (Genesis)** — businesses are being asked to comply with rules that do not yet exist as law. The EU AI Act is in trilogue on 14 June 2023; NIST AI RMF is voluntary. Any compliance programme built now is building against a moving spec — the classic risk of anchoring a visible obligation to a Genesis-stage foundation.
3. **Safety → Interpretability & Forensics (Genesis)** — Safety is the single most user-visible outcome component, and the primary mechanism for demonstrating safety after the fact is Genesis-stage research, not a productised toolchain. Every serious incident exposes this fragility.

(Also: Third-Party Audits → Benchmarks & Evals — audits only carry weight if the evals they rely on are themselves credible, and in June 2023 they mostly aren't yet.)

### d. Suggested gameplays

- **#15 Open Approaches** on Benchmarks & Evals and Content Provenance / Watermarking — open, shared standards make the trust layer credible and neutralise "trust us" from individual vendors. C2PA already fits this pattern for provenance; HELM is a partial example for evals.
- **#36 Directed investment** on Constitutional AI and Interpretability & Forensics — these are the highest-differentiation control mechanisms. Pour engineering into them while they are still Genesis.
- **#43 Sensing Engines (ILC)** on Foundation Models — watch capability and safety metrics as an ecosystem; the winner-take-most dynamic means late readers lose.
- **#29 Harvesting** on Cloud Infrastructure, GPUs (for now), and ML Algorithms — use the best available; do not reinvent.
- **#16 Exploiting Network Effects** on Benchmarks & Evals — once your eval is the one cited in procurement RFPs, the benchmark becomes a choke point; pair with #15.
- **#56 First mover** on Regulatory Compliance tooling — EU AI Act deadlines are coming, but compliance products do not yet exist. Narrow window.
- **#45 Two factor** on Third-Party Audits — auditors need vendors, vendors need audit legitimacy for procurement. Seed both sides.
- **#1 Focus on user needs** — three distinct user types (individual, government, business) means three distinct "trust" propositions. Avoid one-size-fits-all messaging.

### e. Doctrine notes

- Correctly applied **#10 Know your users** — three anchors for the three substantively different users whose definition of "trust" differs.
- Correctly applied **#1 Focus on user needs** — Safety, Reputation, Competitive Advantage, Regulatory Compliance are the four user-visible outcomes, each tied to at least one anchor.
- Watch **#2 Use a systematic mechanism of learning** — Feedback Loops (RLHF pipeline) is the learning mechanism inside foundation-model development, and Incident Reporting is the learning mechanism at the governance layer. Both are Custom Built at best; neither is an industry standard yet.
- Watch **#13 Manage inertia** — the technical stack is producing new capabilities faster than the governance layer can absorb them (see climatic context below). That is a recipe for inertia-driven regulatory overreach.
- Minor concern on **#6 Use appropriate methods (think small)** — some vendors are trying to build the whole stack (model + evals + audit + compliance) in one company; the map suggests most of those layers should be separate entities for credibility.

### f. Climatic context

- **#3 Everything evolves** — the entire left-hand side of the map is in early-stage evolution; every component on the left will move right over the next 2-4 years. The `evolve` arrows are the most plausible trajectories, not forecasts.
- **#27 Product-to-utility punctuated equilibrium** — Foundation Models are in the middle of this transition. GPT-4, Claude, PaLM 2 are being productised through APIs; the "utility model inference" phase has started but is not dominant. Expect a war as multiple vendors and open-source releases (LLaMA and successors, incoming) compete.
- **#15 Inertia from past success** — large organisations whose decision-making was built around deterministic software are resisting probabilistic AI systems. That inertia is slowing both adoption and the standardisation of trust controls.
- **#16 Inertia from sunk capital** — enterprises with heavy investment in pre-LLM NLP or classical ML are reluctant to rewrite; this shows up as slower adoption of Foundation Models in regulated sectors.
- **#17 Inertia from regulation / uncertainty** — nobody wants to ship high-risk AI until the EU AI Act is finalised; this is a short-term freeze on Stage-III transitions for safety-critical applications.
- **#22 Competitors will catch up** — OpenAI's lead at this moment is not durable on model capability alone; the moats will come from evals, feedback loops, data, and trust controls.
- **#7 Componentisation accelerates change** — APIs like OpenAI's, Anthropic's, Google's are componentising what used to be bespoke ML work. That accelerates the whole right-ward drift.

### g. Deep-placement notes

Five components warranted targeted research beyond the cheat-sheet pass:

- **Foundation Models** — initial cheat-sheet rows disagreed sharply. Ubiquity shot up with ChatGPT crossing 100M users by January 2023; Certainty lagged (safety and capability properties still emergent); User Perception was still "leading edge" rather than "expected"; Publication Types were split between "describe the wonder" (Stage I) and "features and comparisons" (Stage III). Vendor-landscape search confirmed a handful of serious players (OpenAI, Anthropic, Google, Meta on the open side) with rapid productisation. Settled on **ε = 0.40** — mid-Custom Built, explicitly flagged as in transition, with an `evolve` arrow to 0.65 reflecting the product-to-utility war already underway.
- **Benchmarks & Evals** — widespread academic adoption of MMLU, HELM, BIG-bench by mid-2023, but no single benchmark owns the category and data-contamination concerns were emerging. Multiple eval frameworks (OpenAI Evals open-sourced March 2023, EleutherAI harness, HELM). Placed at **ε = 0.42** — Custom Built trending to Product (+rental) (evolve to 0.60).
- **EU AI Act / AI Regulations** — 14 June 2023 was literally the day Parliament adopted its negotiating position; first trilogue meeting the same day; final agreement would not come until December 2023 and full application years later. Not yet law anywhere. Confirmed **ε = 0.12** — firmly Genesis. The NIST AI RMF (January 2023) is voluntary guidance, also Genesis-stage as a compliance mechanism.
- **Constitutional AI** — Anthropic's paper from December 2022, Claude's constitution published May 2023 (one month before the scenario date). Only one major vendor practising it in production; no multi-vendor adoption yet. Confirmed **ε = 0.10** — Genesis. Evolve target 0.35 reflects plausible spread of the method as other labs experiment.
- **Content Provenance / Watermarking (C2PA)** — C2PA spec v1.4 in 2023, White House engaging, but no mainstream generative-AI watermarking products yet (Google SynthID would arrive August 2023, after the scenario date). Placed at **ε = 0.18** — Genesis edging toward Custom Built.

### h. Caveat

All positions on this map are a snapshot of June 2023 understanding, and the `evolve` arrows are scenarios, not forecasts. Wardley's climatic pattern #18 is explicit: *"you cannot measure evolution over time or adoption."* The arrows express which transitions are most plausible given the current ecosystem pressures — they are not calendar predictions. In particular, the speed at which Foundation Models industrialise depends on regulatory timing and on whether the open-weights ecosystem (post-LLaMA) forces a faster utility transition.

---

## What's differentiating vs commoditising, at a glance

- **Differentiating** (build / invest): Constitutional AI, Interpretability & Forensics, Benchmarks & Evals (if you own them), Data Curation & Provenance, Red Teaming as a repeatable practice, Fine-tuning Methods, bespoke RLHF pipelines.
- **Commoditising** (rent / harvest): Cloud Infrastructure (already Commodity +utility), Power, GPUs (utility with current supply shock), ML Algorithms / Transformers (late Product +rental, open-source), Prompting / RAG patterns (Genesis pattern, rapidly becoming library-code).
- **Where trust is fragile**: the governance layer (Regulations, Audits, Certifications) is still Genesis while the things it governs (Foundation Models, AI Products) are already in production. Every user-facing Safety claim rests on Interpretability research that does not yet generalise. Compliance programmes are being built against a spec that does not yet exist. These are the load-bearing cracks in the current trust story.

---

## Validator

```
OK: 34 components/anchors, 61 edges — no violations.
```

(Run via `python3 ${CLAUDE_SKILL_DIR}/scripts/validate_owm.py draft.owm`.)
