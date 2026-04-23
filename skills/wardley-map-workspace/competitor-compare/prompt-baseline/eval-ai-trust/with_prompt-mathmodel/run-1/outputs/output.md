```owm
title AI Trust Landscape (June 2023)
style wardley

// Anchors — three distinct user types per the scenario
anchor Individual Trust [0.98, 0.30]
anchor Government Oversight [0.97, 0.25]
anchor Business Adoption [0.96, 0.55]

// Outcome layer — what users actually perceive
component AI Safety [0.88, 0.25]
component Reputation [0.87, 0.45]
component Competitive Advantage [0.85, 0.35]
component Regulatory Compliance [0.84, 0.20]

// Trust-bearing, user-visible capabilities
component Explainability [0.78, 0.20]
component Fairness Guarantees [0.76, 0.18]
component Human Oversight [0.74, 0.30]
component Alignment Assurance [0.72, 0.15]

// Governance layer
component AI Regulation [0.68, 0.22]
component Third-Party Audits [0.66, 0.28]
component Policy Frameworks [0.64, 0.24]
component Standardised Benchmarks [0.62, 0.40]
component Certification Schemes [0.60, 0.20]

// Control mechanisms
component Constitutional AI [0.58, 0.18]
component RLHF Feedback Loops [0.56, 0.45]
component Red-Teaming [0.54, 0.30]
component Model Forensics [0.52, 0.15]
component Content Provenance [0.50, 0.22]
component Watermarking [0.48, 0.25]

// Technical model layer
component Foundation Models [0.42, 0.58]
component Fine-Tuning Pipelines [0.40, 0.55]
component Prompt Engineering [0.38, 0.60]
component Evaluation Harnesses [0.36, 0.40]
component Guardrail Libraries [0.34, 0.35]

// Data layer
component Training Data Curation [0.28, 0.35]
component Data Provenance [0.26, 0.18]
component Synthetic Data [0.24, 0.30]
component Data Governance Tooling [0.22, 0.42]

// Compute and infrastructure
component GPU Clusters [0.16, 0.72]
component Cloud Inference [0.14, 0.82]
component Model Hosting APIs [0.18, 0.70]
component Energy Supply [0.08, 0.92]

// Dependencies — Individual Trust
Individual Trust->AI Safety
Individual Trust->Explainability
Individual Trust->Fairness Guarantees
Individual Trust->Content Provenance

// Dependencies — Government Oversight
Government Oversight->Regulatory Compliance
Government Oversight->AI Regulation
Government Oversight->Third-Party Audits
Government Oversight->Policy Frameworks

// Dependencies — Business Adoption
Business Adoption->Reputation
Business Adoption->Competitive Advantage
Business Adoption->Regulatory Compliance
Business Adoption->AI Safety

// Outcomes depend on trust-bearing capabilities
AI Safety->Alignment Assurance
AI Safety->Human Oversight
AI Safety->Red-Teaming
Reputation->Fairness Guarantees
Reputation->Explainability
Competitive Advantage->Foundation Models
Competitive Advantage->Fine-Tuning Pipelines
Regulatory Compliance->AI Regulation
Regulatory Compliance->Certification Schemes
Regulatory Compliance->Third-Party Audits

// Trust-bearing capabilities depend on governance + controls
Explainability->Evaluation Harnesses
Explainability->Model Forensics
Fairness Guarantees->Standardised Benchmarks
Fairness Guarantees->Evaluation Harnesses
Human Oversight->RLHF Feedback Loops
Alignment Assurance->Constitutional AI
Alignment Assurance->RLHF Feedback Loops
Alignment Assurance->Red-Teaming

// Governance dependencies
AI Regulation->Policy Frameworks
Third-Party Audits->Standardised Benchmarks
Third-Party Audits->Model Forensics
Certification Schemes->Standardised Benchmarks
Standardised Benchmarks->Evaluation Harnesses

// Control mechanisms depend on models/data
Constitutional AI->Foundation Models
RLHF Feedback Loops->Foundation Models
RLHF Feedback Loops->Fine-Tuning Pipelines
Red-Teaming->Foundation Models
Red-Teaming->Guardrail Libraries
Model Forensics->Foundation Models
Model Forensics->Training Data Curation
Content Provenance->Watermarking
Content Provenance->Data Provenance

// Technical layer dependencies
Foundation Models->Training Data Curation
Foundation Models->GPU Clusters
Foundation Models->Cloud Inference
Fine-Tuning Pipelines->Foundation Models
Fine-Tuning Pipelines->Training Data Curation
Prompt Engineering->Foundation Models
Evaluation Harnesses->Foundation Models
Evaluation Harnesses->Training Data Curation
Guardrail Libraries->Foundation Models
Guardrail Libraries->Model Hosting APIs

// Data layer
Training Data Curation->Data Governance Tooling
Training Data Curation->Data Provenance
Synthetic Data->Foundation Models
Data Governance Tooling->Data Provenance

// Infrastructure
GPU Clusters->Energy Supply
Cloud Inference->GPU Clusters
Cloud Inference->Energy Supply
Model Hosting APIs->Cloud Inference

// Evolution movements (scenario, not forecast)
evolve Foundation Models 0.72
evolve RLHF Feedback Loops 0.62
evolve Standardised Benchmarks 0.58
evolve AI Regulation 0.45
evolve Third-Party Audits 0.50
evolve Model Hosting APIs 0.85

// Inertia — components stuck or resisting evolution
component Legacy Compliance Processes [0.70, 0.30] inertia

// Notes
note Fragile trust zone: visible capabilities sitting on immature foundations [0.75, 0.18]
note Commoditising fast — compute / hosting [0.15, 0.80]
note Differentiation zone: controls + alignment [0.55, 0.18]
```

## Strategic Analysis

### a. Top 3 components by D (differentiation pressure) = ν · (1 − ε)

1. **Alignment Assurance** — D = 0.72 × 0.85 = **0.612**. Highly user-visible (business, government, individuals all care), still deeply uncertain (pre-Stage II). This is the single biggest strategic differentiator available in June 2023 — whoever can credibly claim *aligned* outputs wins trust.
2. **Fairness Guarantees** — D = 0.76 × 0.82 = **0.623**. Surfaces directly in user trust and regulatory compliance; methods (bias benchmarks, counterfactual testing) are still rapidly evolving. Differentiation through fairness-by-design.
3. **Explainability** — D = 0.78 × 0.80 = **0.624**. Individuals and regulators both demand it; the field is still between Genesis and Custom-Built (LIME/SHAP exist but are not yet standardised products). Strong differentiator for enterprise AI vendors.

### b. Top 3 components by K (commodity leverage) = (1 − ν) · ε

1. **Energy Supply** — K = 0.92 × 0.92 = **0.846**. Pure utility. Buy, don't build.
2. **Cloud Inference** — K = 0.86 × 0.82 = **0.705**. Hyperscaler land (AWS Bedrock, Azure OpenAI, GCP Vertex). Outsource.
3. **GPU Clusters** — K = 0.84 × 0.72 = **0.605**. Moving rapidly toward utility, though supply-constrained in June 2023. Rent via hyperscaler; don't own unless you're a foundation-model lab.

### c. Top 3 dependency risks by R = ν(a) · (1 − ε(b))

1. **(AI Safety → Alignment Assurance)** — R = 0.88 × 0.85 = **0.748**. The entire safety outcome rides on a Genesis-stage capability. This is *the* fragile-trust node in June 2023: users and regulators demand safety, but its foundation is still a research problem.
2. **(Regulatory Compliance → AI Regulation)** — R = 0.84 × 0.78 = **0.655**. EU AI Act not yet passed, US still at executive-order stage, China diverging. Compliance outcomes depend on a regulatory layer that is itself immature and fragmented.
3. **(Reputation → Fairness Guarantees)** — R = 0.87 × 0.82 = **0.713**. Reputational damage (e.g., biased image generator, discriminatory hiring screen) is already happening, but fairness methods are not yet mature enough to *prevent* it reliably.

### d. Suggested gameplays (Wardley's 61-play catalogue)

- **Open Approaches** on Standardised Benchmarks and Evaluation Harnesses. Accelerate evolution toward Product/Commodity stage; HELM, BIG-bench, and safety benchmarks already show the pattern. Open standards reduce industry-wide audit cost and raise the floor for trust.
- **Fool's Mate / Pig in a poke (constraint shaping)** on AI Regulation. Large labs are actively trying to shape the regulatory layer (e.g., by calling for licensing regimes) — recognise this as a deliberate play and don't take it at face value.
- **Sensing Engines / Experimentation** on Red-Teaming. Institutionalise adversarial testing as a continuous capability, not a pre-launch gate.
- **Cross-Subsidy** on Foundation Models → Model Hosting APIs. The API layer is commoditising; defensibility migrates to fine-tuning + guardrails + vertical data.
- **Pressure Relief Valve / Safe Harbour** on Third-Party Audits. Position independent audit bodies as the mechanism that lets regulators say "good enough for now" while controls mature.
- **Harvesting** on Guardrail Libraries. Nascent vendors (Guardrails AI, NeMo Guardrails) are viable acquisition targets for hyperscalers wanting to bundle trust into their API product.

### e. Doctrine observations

- **Multiple users are correctly captured** (three anchors: Individual, Government, Business) — good Phase II "Know your users" doctrine.
- **Knowledge layer is thin.** Alignment Assurance and Constitutional AI straddle Activity/Knowledge; a stricter τ-typed pass would separate the K nodes (the *theories* of alignment) from the A nodes (the *practices* of implementing them). In June 2023 this distinction matters because alignment is primarily a Knowledge problem, and mapping it as an Activity overstates how actionable it is.
- **Watch "focus on user needs":** the three user types have *divergent* needs. Individuals want explainability and non-harm; governments want auditability and compliance; businesses want competitive advantage without reputational hits. A single-anchor map would collapse this and hide the tension.
- **Challenge assumptions:** the strong industry narrative that "bigger models = better" pushes everything toward Foundation Models as the anchor of value. The map suggests the opposite — the differentiation has migrated up into the control/governance layer while the model layer itself commoditises.

## What's Differentiating vs. Commoditising (June 2023)

**Commoditising fast:**
- Cloud Inference, GPU Clusters, Model Hosting APIs — hyperscaler utility territory.
- Foundation-model *access* (via API) — GPT-4, Claude, PaLM 2, Llama 2 (about to drop) — the interface is standardising on chat-completion-style endpoints.
- Prompt Engineering — already largely a practice, headed toward commodity tooling.

**Differentiating:**
- Alignment, Explainability, Fairness, Human Oversight — the trust-bearing capabilities where methods are still immature.
- Standardised Benchmarks and Third-Party Audits — whoever sets the measurement defines the market.
- Model Forensics and Content Provenance (C2PA, watermarking) — Genesis-stage but mandatory once deepfake pressure hits.

**Where trust itself is fragile:**
1. **Alignment is the load-bearing node.** Safety as an *outcome* sits on alignment as a *Genesis-stage capability*. That mismatch — high visibility, low maturity — is the defining fragility of the June 2023 landscape.
2. **Regulation is lagging and fragmented.** EU AI Act not yet final; US relying on voluntary commitments; different jurisdictions heading different directions. Business compliance claims depend on a layer that hasn't set its own ground rules.
3. **Benchmarks don't measure what matters.** Current benchmarks (MMLU, HumanEval) measure capability, not trust. Trust-relevant benchmarks (truthfulness, harm, bias) exist but aren't yet standardised or third-party-certified — so "we passed the benchmark" claims are weak evidence.
4. **Data provenance is invisible.** Most users and regulators cannot see training data. Until Data Provenance matures, every trust claim is partly a faith claim.
5. **Feedback loops concentrate power.** RLHF depends on labelled preference data, which depends on who labels and how — a governance gap hidden inside a technical component.

*Caveat on dynamics:* the `evolve` targets above are scenario placeholders using the logistic form dε/dt = r·ε·(1 − ε). They are not forecasts. Wardley's climatic pattern is that evolution cannot be measured over time.
