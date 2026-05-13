Both validator and layout checker pass cleanly. Here's the map and analysis.

## Strategic framing

- **Question:** What components determine whether individuals, government, and business can trust AI systems — and where is trust most fragile in June 2023?
- **User anchors:** Three — Individual end-users; Government Regulator; Business User (enterprise deploying AI).
- **Core needs:** Individuals → safety, privacy, recourse, honest disclosure. Government → public safety, oversight, accountability. Business → competitive advantage, brand reputation, compliance posture, bounded liability.
- **Scope:** Industry landscape of the AI trust ecosystem as of mid-2023 (GPT-4 launched March 2023, Claude available, EU AI Act in trilogue, NIST AI RMF released January 2023, no voluntary commitments yet signed).
- **Key assumption (correctable):** "Trust" here means *justified reliance* — not merely sentiment. So outcome qualities like Model Safety and Fairness are treated as components with mechanism-level dependencies, not as marketing positions.

## The map (OWM)

```owm
title AI Trust Landscape — June 2023
style wardley

// Three anchors: individuals, government regulators, business users
anchor Individual [0.98, 0.50]
anchor Government Regulator [0.96, 0.40]
anchor Business User [0.97, 0.60]

// User-facing experiences and outcomes
component AI Product Experience [0.88, 0.58]
component Brand Reputation [0.86, 0.65]
component Public Safety Outcomes [0.86, 0.40]
component Competitive Advantage [0.84, 0.53]
component Compliance Posture [0.82, 0.45]
component Disclosure & Labels [0.80, 0.35]
component Recourse Mechanisms [0.78, 0.28]
component Liability Exposure [0.76, 0.30]

// Outcome qualities
component Output Reliability [0.74, 0.47]
component Model Safety [0.72, 0.32]
component Fairness & Non-Discrimination [0.70, 0.38]
component Privacy Preservation [0.68, 0.55]

// Governance layer
component Certification Regimes [0.66, 0.20]
component EU AI Act (in trilogue) [0.62, 0.22]
component US Executive Action [0.60, 0.28]
component Third-Party AI Audits [0.60, 0.18]
component ISO/IEC AI Standards [0.58, 0.48]
component Voluntary Industry Commitments [0.56, 0.30]
component NIST AI RMF [0.54, 0.40]
component Incident Reporting [0.46, 0.20]
component Frontier Model Forum (forming) [0.44, 0.12]

// Control mechanisms
component Red Teaming [0.52, 0.38]
component User Feedback Loops [0.52, 0.60]
component Safety Evaluations [0.50, 0.35]
component Model Cards & Datasheets [0.50, 0.62]
component Eval Benchmarks (HELM, MMLU) [0.48, 0.58]
component C2PA Content Provenance [0.44, 0.42]
component RLHF [0.42, 0.55]
component Watermarking [0.40, 0.16]
component Constitutional AI [0.38, 0.12]
component AI Forensics [0.34, 0.15]
component Mechanistic Interpretability [0.30, 0.10]
component Alignment Research [0.26, 0.14]

// Technical layer
component Foundation Models [0.40, 0.53]
component Regulatory Expertise [0.40, 0.32]
component Fine-tuning Pipeline [0.36, 0.58]
component Domain Ethics Knowledge [0.34, 0.30]
component Training Data [0.32, 0.55]
component Data Labeling Services [0.30, 0.65]
component Synthetic Data [0.26, 0.32]
component Model Hosting / Inference [0.24, 0.65]
component ML & Safety Talent [0.22, 0.38]
component GPUs / AI Accelerators [0.18, 0.65]
component ML Frameworks [0.14, 0.85]
component Cloud Compute [0.10, 0.90]

// Individual dependencies
Individual->AI Product Experience
Individual->Disclosure & Labels
Individual->Recourse Mechanisms
Individual->Privacy Preservation
Individual->Public Safety Outcomes

// Government dependencies
Government Regulator->Public Safety Outcomes
Government Regulator->EU AI Act (in trilogue)
Government Regulator->US Executive Action
Government Regulator->Incident Reporting

// Business dependencies
Business User->Competitive Advantage
Business User->Brand Reputation
Business User->Compliance Posture
Business User->AI Product Experience
Business User->Liability Exposure

// User-facing → outcomes
AI Product Experience->Foundation Models
AI Product Experience->Output Reliability
AI Product Experience->Model Safety
Brand Reputation->Model Safety
Brand Reputation->Fairness & Non-Discrimination
Brand Reputation->Disclosure & Labels
Competitive Advantage->Foundation Models
Competitive Advantage->Fine-tuning Pipeline
Competitive Advantage->ML & Safety Talent
Public Safety Outcomes->Model Safety
Public Safety Outcomes->Third-Party AI Audits
Public Safety Outcomes->Incident Reporting
Compliance Posture->NIST AI RMF
Compliance Posture->ISO/IEC AI Standards
Compliance Posture->EU AI Act (in trilogue)
Compliance Posture->Regulatory Expertise
Disclosure & Labels->Watermarking
Disclosure & Labels->C2PA Content Provenance
Disclosure & Labels->Model Cards & Datasheets
Recourse Mechanisms->AI Forensics
Recourse Mechanisms->Incident Reporting
Liability Exposure->Third-Party AI Audits
Liability Exposure->Model Cards & Datasheets

// Outcomes → mechanisms
Model Safety->Red Teaming
Model Safety->Safety Evaluations
Model Safety->RLHF
Model Safety->Constitutional AI
Model Safety->Alignment Research
Model Safety->Mechanistic Interpretability
Fairness & Non-Discrimination->Eval Benchmarks (HELM, MMLU)
Fairness & Non-Discrimination->Training Data
Fairness & Non-Discrimination->Safety Evaluations
Privacy Preservation->Training Data
Privacy Preservation->Synthetic Data
Output Reliability->Eval Benchmarks (HELM, MMLU)
Output Reliability->Foundation Models
Output Reliability->User Feedback Loops

// Governance internal
EU AI Act (in trilogue)->Third-Party AI Audits
EU AI Act (in trilogue)->Incident Reporting
EU AI Act (in trilogue)->Regulatory Expertise
US Executive Action->Voluntary Industry Commitments
US Executive Action->NIST AI RMF
Voluntary Industry Commitments->Frontier Model Forum (forming)
Voluntary Industry Commitments->Red Teaming
NIST AI RMF->Eval Benchmarks (HELM, MMLU)
NIST AI RMF->Model Cards & Datasheets
ISO/IEC AI Standards->NIST AI RMF
Certification Regimes->Third-Party AI Audits
Certification Regimes->ISO/IEC AI Standards
Third-Party AI Audits->Eval Benchmarks (HELM, MMLU)
Third-Party AI Audits->Safety Evaluations
Third-Party AI Audits->Model Cards & Datasheets
Incident Reporting->AI Forensics

// Mechanisms → research/talent
Red Teaming->Safety Evaluations
Red Teaming->ML & Safety Talent
Safety Evaluations->Eval Benchmarks (HELM, MMLU)
Safety Evaluations->Foundation Models
Eval Benchmarks (HELM, MMLU)->Foundation Models
Model Cards & Datasheets->Foundation Models
Model Cards & Datasheets->Training Data
User Feedback Loops->Foundation Models
RLHF->Foundation Models
RLHF->Data Labeling Services
RLHF->ML & Safety Talent
Constitutional AI->Alignment Research
Watermarking->Alignment Research
AI Forensics->Alignment Research
Mechanistic Interpretability->Alignment Research
Alignment Research->ML & Safety Talent
Regulatory Expertise->Domain Ethics Knowledge

// Technical chain
Foundation Models->Fine-tuning Pipeline
Foundation Models->Training Data
Foundation Models->Model Hosting / Inference
Foundation Models->ML Frameworks
Fine-tuning Pipeline->Training Data
Fine-tuning Pipeline->Data Labeling Services
Fine-tuning Pipeline->GPUs / AI Accelerators
Training Data->Data Labeling Services
Model Hosting / Inference->GPUs / AI Accelerators
Model Hosting / Inference->Cloud Compute
GPUs / AI Accelerators->Cloud Compute

// Evolution trajectories
evolve Watermarking 0.55
evolve EU AI Act (in trilogue) 0.55
evolve Third-Party AI Audits 0.55
evolve Foundation Models 0.78
evolve Constitutional AI 0.45
evolve C2PA Content Provenance 0.65
evolve Mechanistic Interpretability 0.35

note Differentiation zone [0.75, 0.20]
note Genesis trust mechanisms [0.25, 0.06]
note Commodity infrastructure [0.12, 0.92]
```

Validator: `OK: 48 components/anchors, 95 edges — no violations.` Layout check clean.

## Component evolution rationale

| Component | Stage | ε | ν | Evidence |
|---|---|---:|---:|---|
| AI Product Experience | Product (+rental) | 0.58 | 0.88 | ChatGPT, Claude, Bard, Copilot are commercial products; feature competition dominates. |
| Brand Reputation | Product (+rental) | 0.65 | 0.86 | Mature concept; companies actively differentiating on "responsible AI" branding. |
| Public Safety Outcomes | Custom Built | 0.40 | 0.86 | Concept invoked widely but no agreed definition; UK AI Safety Summit being planned. |
| Competitive Advantage | Product (+rental) | 0.53 | 0.84 | Established business concept applied to AI; multiple vendor benchmarks emerging. |
| Compliance Posture | Custom Built | 0.45 | 0.82 | Enterprise AI compliance programs being formed bespoke; no off-the-shelf playbook. |
| Disclosure & Labels | Custom Built | 0.35 | 0.80 | "AI-generated" disclosure norms in flux; no standard label exists across platforms. |
| Recourse Mechanisms | Custom Built | 0.28 | 0.78 | EU AI Act draft mandates redress but no operational pattern; few real-world examples. |
| Liability Exposure | Custom Built | 0.30 | 0.76 | AI-specific liability frameworks not yet settled; case law in early stages. |
| Output Reliability | Custom Built | 0.47 | 0.74 | Hallucination is a known unsolved problem; reliability varies wildly across tasks. |
| Model Safety | Custom Built | 0.32 | 0.72 | Each frontier lab uses bespoke safety methodology; no industry-wide protocol. |
| Fairness & Non-Discrimination | Custom Built | 0.38 | 0.70 | Bias-audit methods exist but contested; fairness metrics still actively debated. |
| Privacy Preservation | Product (+rental) | 0.55 | 0.68 | GDPR-era practices apply; DP and federated learning have commercial offerings. |
| Certification Regimes | Genesis | 0.20 | 0.66 | No mature AI certification body yet; first pilots from BSI, IEEE, ISO underway. |
| EU AI Act (in trilogue) | Genesis | 0.22 | 0.62 | Council/Parliament texts diverging; final text expected late 2023, not yet law. |
| US Executive Action | Custom Built | 0.28 | 0.60 | Blueprint for AI Bill of Rights (Oct 2022) non-binding; EO still drafting. |
| Third-Party AI Audits | Genesis | 0.18 | 0.60 | Handful of pioneers (BABL, ORCAA, Eticas, Holistic AI); no standard methodology. |
| ISO/IEC AI Standards | Custom Built | 0.48 | 0.58 | ISO/IEC 42001 in draft; ISO/IEC 23894 (risk) and 22989 (terminology) published. |
| Voluntary Industry Commitments | Custom Built | 0.30 | 0.56 | White House voluntary commitments announced but not yet signed (came July 2023). |
| NIST AI RMF | Custom Built | 0.40 | 0.54 | Version 1.0 released January 2023; early enterprise adoption, profiles forming. |
| Incident Reporting | Genesis | 0.20 | 0.46 | AI Incident Database exists but no mandatory reporting regime; sparse coverage. |
| Frontier Model Forum (forming) | Genesis | 0.12 | 0.44 | Anthropic/Google/Microsoft/OpenAI alliance formally launched July 2023. |
| Red Teaming | Custom Built | 0.38 | 0.52 | Each lab runs custom red-team programs; DEF CON GRT public exercise August 2023. |
| User Feedback Loops | Product (+rental) | 0.60 | 0.52 | Thumbs-up/down patterns standard in ChatGPT, Claude, Bard; RLHF data pipeline. |
| Safety Evaluations | Custom Built | 0.35 | 0.50 | ARC Evals (now METR) doing dangerous-capability evals bespoke for OpenAI/Anthropic. |
| Model Cards & Datasheets | Product (+rental) | 0.62 | 0.50 | Standardised since Mitchell et al. 2018; Hugging Face cards near-universal. |
| Eval Benchmarks (HELM, MMLU) | Product (+rental) | 0.58 | 0.48 | HELM, MMLU, BIG-bench, HumanEval all widely cited; leaderboard culture entrenched. |
| C2PA Content Provenance | Custom Built | 0.42 | 0.44 | C2PA spec v1.3 published; Adobe, Microsoft, BBC pilots; consumer adoption nil. |
| RLHF | Product (+rental) | 0.55 | 0.42 | Used in InstructGPT, ChatGPT, Claude, Bard; rapidly becoming the default alignment recipe. |
| Watermarking | Genesis | 0.16 | 0.40 | Kirchenbauer et al. paper January 2023; OpenAI exploring; no production deployment. |
| Constitutional AI | Genesis | 0.12 | 0.38 | Anthropic paper December 2022; single-vendor technique; no third-party use yet. |
| AI Forensics | Genesis | 0.15 | 0.34 | Academic discipline forming; tooling for tracing model outputs essentially non-existent. |
| Mechanistic Interpretability | Genesis | 0.10 | 0.30 | Anthropic, Redwood, DeepMind teams; circuits-level work; no operational application. |
| Alignment Research | Genesis | 0.14 | 0.26 | Field rapidly growing post-GPT-4; no consensus methodology; high disagreement. |
| Foundation Models | Product (+rental) | 0.53 | 0.40 | GPT-4 (March), Claude (March), PaLM 2 (May), LLaMA leaked; per-token pricing. |
| Regulatory Expertise | Custom Built | 0.32 | 0.40 | Specialist law firms (e.g. Wilson Sonsini, Hogan Lovells) building practices; scarce. |
| Fine-tuning Pipeline | Product (+rental) | 0.58 | 0.36 | OpenAI fine-tuning API, Hugging Face Transformers, LoRA tooling all commercial. |
| Domain Ethics Knowledge | Custom Built | 0.30 | 0.34 | Field exists but applied AI ethics consulting still bespoke; few certifications. |
| Training Data | Product (+rental) | 0.55 | 0.32 | Common Crawl, The Pile, RedPajama; commercial dataset markets emerging. |
| Data Labeling Services | Product (+rental) | 0.65 | 0.30 | Scale AI, Surge, Snorkel — multi-vendor product market with feature competition. |
| Synthetic Data | Custom Built | 0.32 | 0.26 | Used in alignment (Anthropic's CAI, Phi-1); commercial vendors (Gretel, Mostly AI) emerging. |
| Model Hosting / Inference | Product (+rental) | 0.65 | 0.24 | Together, Replicate, Modal, AWS Bedrock, Azure ML — competitive vendor market. |
| ML & Safety Talent | Custom Built | 0.38 | 0.22 | Bidding wars for safety researchers; no standard credential pathway; very scarce. |
| GPUs / AI Accelerators | Product (+rental) | 0.65 | 0.18 | NVIDIA H100 supply-constrained; AMD MI300, Google TPU, custom silicon competing. |
| ML Frameworks | Commodity (+utility) | 0.85 | 0.14 | PyTorch dominant, JAX/TF stable; foundation-quality utility status. |
| Cloud Compute | Commodity (+utility) | 0.90 | 0.10 | AWS, GCP, Azure — utility pricing, interchangeable for most workloads. |

## Strategic analysis

### a. Differentiation opportunities (top 3)

1. **Model Safety** (Custom Built) — the largest visible-but-immature surface, and the one frontier labs are actually competing on. Anthropic's Constitutional AI, OpenAI's RLHF + red-team, DeepMind's safety teams are all racing to define what "safe enough" means. Whoever sets the operational standard captures defensible reputation.
2. **Disclosure & Labels** (Custom Built) — highly visible to all three user types (individuals expect to know, regulators are codifying, business needs it for compliance). The mechanism layer (watermarking + provenance) is Genesis, so being first with a credible system is a real moat. C2PA-style cross-vendor watermarking is a candidate standards-game play.
3. **Recourse Mechanisms** (Custom Built) — when AI gets something wrong, what happens? Almost no one has answered this operationally. EU AI Act will mandate it. First credible recourse system becomes a regulatory reference point.

### b. Commodity-leverage candidates (top 3)

1. **Cloud Compute** (Commodity +utility) — rent from AWS/GCP/Azure; building data centre capacity for AI workloads has terrible economics outside hyperscaler scale.
2. **ML Frameworks** (Commodity +utility) — PyTorch is effectively utility-grade; consuming it is correct, contributing to it is collaborative play (#15), forking it is wasteful.
3. **Data Labeling Services** (Product +rental) — Scale AI, Surge, Snorkel, Appen compete on cost and quality; in-house labeling teams burn capital that should be spent on differentiating components above.

### c. Dependency risks (where trust is fragile) — top 3

1. **Public Safety Outcomes → Third-Party AI Audits.** Government's anchor depends on an auditing industry that, in June 2023, has perhaps ten serious firms globally and no standard methodology. The EU AI Act is being drafted around an audit ecosystem that does not yet operationally exist. This is the single biggest trust gap in the map.
2. **Disclosure & Labels → Watermarking.** "Is this AI-generated?" is the most-asked individual-level trust question, and the underlying technical mechanism is Genesis — a handful of academic papers, no production deployment, demonstrably attackable. Society is loading expectations onto a technique that doesn't yet work robustly.
3. **Recourse Mechanisms → AI Forensics.** Right of redress is meaningless without the ability to trace what a model did and why. Forensics tooling is Genesis. So individuals' regulatory protections are stacked on top of techniques that don't exist yet at production scale.

Honourable mention: **Model Safety → Constitutional AI / Alignment Research / Mechanistic Interpretability.** The entire safety stack rests on Genesis-stage research. This is the systemic fragility critics point to.

### d. Build / Buy / Outsource recommendations

| Component | Stage | Recommendation | Why |
|---|---|---|---|
| Model Safety methodology | Custom Built | **Build** (internally + open) | The core differentiator; this is where reputation is won or lost. |
| Foundation Models | Product (+rental) | **Buy or Build** by player — for most businesses, **buy** via API | Vendor market is real; building from scratch only makes sense for ≤5 labs globally. |
| Red Teaming | Custom Built | **Build + contract** specialists | Practice still bespoke; outside firms (Trail of Bits, NCC) starting to offer. |
| Safety Evaluations | Custom Built | **Buy expertise** (ARC/METR, Apollo) | Independent evals are higher-trust than self-eval; pay specialists. |
| Eval Benchmarks | Product (+rental) | **Consume + contribute** | HELM, MMLU, BIG-bench are usable off-the-shelf; contribute domain benchmarks. |
| Watermarking / Provenance | Genesis → Custom | **Open-source collaborate** (C2PA, SynthID) | Standard-setting play (#30); going proprietary on watermarking is a losing position. |
| Third-Party Audits | Genesis | **Hire pioneers, fund development** | Industry needs to exist; early movers can shape it. |
| Cloud, GPUs, Hosting | Product → Commodity | **Rent** | Hyperscaler / NVIDIA economics; don't burn capital here. |
| ML Frameworks | Commodity (+utility) | **Consume** | PyTorch / JAX are utilities. |
| Data Labeling | Product (+rental) | **Buy** (Scale, Surge) | Mature vendor market. |
| Constitutional AI / Interpretability | Genesis | **Research** (in-house if frontier lab, partner if not) | Pure R&D; option value is high but no operational play yet. |

### e. Suggested gameplays

- **#15 Open Approaches** on Eval Benchmarks, Model Cards, C2PA, Watermarking — accelerate these from Custom/Genesis to Product/Commodity. Going proprietary on trust signals is self-defeating; the signal is only valuable if everyone reads it the same way.
- **#30 Standards game** on NIST AI RMF, ISO/IEC 42001, C2PA — whoever defines the operational standards shapes the audit and certification industry built on top.
- **#41 Alliances / #17 Co-operation** — Frontier Model Forum is exactly this play, executed in real time by the four largest labs. Expect more.
- **#18 Industrial Policy** on Alignment Research and Mechanistic Interpretability — government grant funding to grow these from Genesis. Already happening (UK Frontier AI Taskforce, US AI Safety Institute being scoped).
- **#43 Sensing Engines (ILC)** on Incident Reporting — a mandatory incident database is the ecosystem-sensing infrastructure regulators don't yet have.
- **#56 First mover** on EU AI Act — the EU is making this play deliberately, setting de facto global rules via the "Brussels effect."
- **#45 Two factor** on Voluntary Commitments + Frontier Model Forum — labs and government create a two-sided structure for self-regulation under regulatory threat.
- **#11 FUD risk** — incumbents may use "AI safety" rhetoric to raise barriers to entry against open-source models. Watch for this gameplay being executed as if it were doctrine.

### f. Doctrine notes

- ✓ **#10 Know your users** — multi-anchor map is correct; AI trust without distinguishing individual / government / business produces incoherent strategy.
- ⚠ **#2 Use a systematic mechanism of learning** — Incident Reporting is the missing learning loop. The whole AI safety system has no equivalent of aviation's NTSB. Treat this as a doctrine gap, not just a capability gap.
- ⚠ **#13 Manage inertia** — frontier labs have sunk capital in proprietary safety techniques (inertia form #2) and political capital in current voluntary regimes (form #3). Expect resistance when mandatory audit regimes arrive.
- ⚠ **#22 Use standards where appropriate** — the temptation will be to standardise too early on immature techniques (watermarking, interpretability). Standards at Stage IV; for now, profiles and guidelines.
- ⚠ **#7 Use appropriate methods** — the same management style won't work across Alignment Research (needs FIRE / agile / experimentation) and Compliance Posture (needs process discipline). Frontier labs need both cultures.

### g. Climatic context

- **#3 Everything evolves** — Foundation Models will commoditise; the trust mechanisms above must mature in step or the gap becomes catastrophic.
- **#11 Future value inversely proportional to certainty** — Genesis trust mechanisms (Constitutional AI, Mech Interp, Watermarking) carry the highest option value. Most will be subsumed; whichever wins becomes critical infrastructure.
- **#15–17 Past success breeds inertia** — incumbents in the old paradigm of "ship fast, fix problems later" (essentially all of pre-2023 ML practice) carry maximum inertia into a regulated era.
- **#22 Two forms of disruption** — both at play. Genesis-driven (a new model paradigm) is unpredictable; product-to-utility (Foundation Models commoditising via open weights — LLaMA, Mistral) is predictable and underway.
- **#23 War causes evolution** — Bletchley Park (Nov 2023), Hiroshima Process, EU AI Act trilogue — the regulatory "war" is forcing rapid component evolution across the governance band.
- **#27 Product-to-utility punctuated equilibrium** — Foundation Models are mid-transition. Open-weight Llama-2 (released July 2023, just after this map's date) accelerates it.

### h. Deep-placement notes

I worked from priors for most components but flagged five for closer scrutiny:

- **Third-Party AI Audits** — held at Genesis (ε=0.18). In June 2023, perhaps a dozen firms (BABL, ORCAA, Eticas, Holistic AI, Credo, Trail of Bits) offering AI audit services with materially different methodologies. No accreditation body. ISO/IEC 42006 (auditing requirements) not yet drafted. Solidly Genesis.
- **C2PA Content Provenance** — placed at ε=0.42 (mid Custom Built). C2PA 1.3 spec exists since 2022; Adobe, Microsoft, BBC, Sony piloting; but consumer-facing deployment in mid-2023 was negligible. Standard mature, adoption emerging.
- **Constitutional AI** — placed at ε=0.12 (deep Genesis). Single Anthropic paper (Dec 2022); no third-party implementations in production; technique is Anthropic-specific. Could shift toward Product if the "constitutional" framing becomes a category — `evolve` target 0.45 reflects that scenario.
- **Watermarking** — placed at ε=0.16 (Genesis). Kirchenbauer et al. paper January 2023; OpenAI exploration but no shipping product; Google's SynthID came September 2023. Genesis confirmed.
- **Foundation Models** — placed at ε=0.53 (early Product +rental). GPT-4, Claude, PaLM 2 all commercial APIs by May 2023; per-token pricing; Hugging Face hosting hundreds of variants. Early Stage III; the `evolve 0.78` target reflects the punctuated-equilibrium transition open weights will drive.

### i. Caveat

Evolution trajectories on this map are **scenarios, not forecasts**. Wardley's climatic pattern #18 stands firmly here: *"you cannot measure evolution over time or adoption."* The June 2023 placements describe positions, not destinies. In particular: the Genesis cluster (Constitutional AI, Mech Interp, Watermarking, Forensics) could evolve in any of several directions over 18–24 months — toward operational Product status, toward being subsumed by a rival technique, or toward being mandated by regulation before the underlying technique works. The trust fragility identified above (Public Safety → Audits, Disclosure → Watermarking, Recourse → Forensics) is the strategically important finding regardless of which way the trajectories resolve.