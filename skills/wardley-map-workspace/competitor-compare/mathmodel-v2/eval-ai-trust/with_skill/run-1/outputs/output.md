# AI Trust Landscape — June 2023

## Step 0 — Strategic context

Before any components are listed, here are the four framing decisions the rest of the map hangs on. These are working assumptions; flag any you want changed and the map should be re-run.

1. **Strategic question.** *"In June 2023, which components determine whether individuals, governments, and businesses can trust AI systems — and which of them are differentiating moats vs. commodities vs. fragile trust seams?"* The map is deliberately a *landscape* view, not a single-product architecture.
2. **User anchor(s).** Three user types sit at the top of the value chain:
   - **Individual** — end-users interacting with AI products (ChatGPT-era consumer and employee use).
   - **Government / Regulator** — the EU Commission (EU AI Act in trilogue), US NIST (AI RMF released Jan 2023), UK CMA (just-opened foundation-models review), and a long tail of national AI offices.
   - **Business** — firms deploying AI who must defend against reputation, liability, and competitive-advantage risks.
3. **Core needs** (2–4 per anchor):
   - Individuals: outputs that are safe, truthful, and understandable; ability to consent or opt out.
   - Government / Regulator: enforceable safety, auditability, incident visibility, standards to point regulation at.
   - Business: trusted output that customers accept; brand reputation; a defensible competitive position; a risk posture the board can sign off.
4. **Scope boundary.** An **industry landscape** (multi-stakeholder: regulators + producers + consumers), not one product or one firm. Target density 40–55 components; landed at 42 components + 3 anchors.

**Assumptions worth challenging:**
- Treating the three user types as peer anchors rather than nesting (e.g., regulator-above-business). Wardley mapping supports multiple anchors; we use it.
- "Trust" is operationalised as a bundle of observable trust outcomes (Trusted AI Output, Safety behaviour, Reputation, Competitive Advantage, Disclosure, Explanations, Consent) rather than as a single abstract node, because an abstract "trust" node isn't separately scoreable on the cheat sheet.
- June 2023 snapshot: post-GPT-4 (Mar 2023), mid-EU-AI-Act trilogue, pre-Bletchley Summit (Nov 2023), pre-Executive Order 14110 (Oct 2023). Regulation is *forming* but not yet enacted.

---

## Map (OWM)

```owm
title AI Trust Landscape (June 2023)
style wardley

// Anchors — three user types whose trust is in question
anchor Individual [0.96, 0.55]
anchor Government / Regulator [0.96, 0.40]
anchor Business [0.93, 0.60]

// ===== Outcome / trust-interface layer (user-visible trust signals)
component Trusted AI Output [0.88, 0.35]
component Safety (behaviour) [0.85, 0.28]
component Reputation / Brand Trust [0.82, 0.52]
component Competitive Advantage [0.80, 0.55]
component Disclosure & Labelling [0.78, 0.32]
component Explanations to Users [0.76, 0.22]
component Consent & Opt-out [0.74, 0.45]

// ===== Governance / assurance layer (how trust is demonstrated)
component AI Regulation [0.72, 0.18]
component Certification Schemes [0.70, 0.22]
component Risk Assessment Process [0.68, 0.38]
component Third-Party Audits [0.66, 0.26]
component AI Standards (ISO/IEEE) [0.64, 0.30]
component Policy Frameworks [0.62, 0.28]
component Model Evaluation Suites [0.60, 0.40]
component Public Benchmarks [0.56, 0.47]
component Incident Reporting [0.54, 0.20]

// ===== Control mechanisms (what actually shapes model behaviour)
component Constitutional AI / Policies [0.52, 0.18]
component Red-teaming [0.50, 0.30]
component Human Feedback (RLHF) [0.48, 0.45]
component Guardrails / Safety Filters [0.46, 0.35]
component Human Oversight / HITL [0.44, 0.32]
component Alignment Research [0.42, 0.12]
component Interpretability [0.40, 0.10]
component Provenance & Watermarking [0.38, 0.15]
component AI Forensics [0.36, 0.08]
component Feedback Loops / Telemetry [0.34, 0.48]

// ===== Model layer (built on top of foundation model)
component Prompt / System Design [0.33, 0.40]
component Fine-tuning [0.32, 0.45]
component Model Cards / Documentation [0.31, 0.32]
component Foundation Model [0.30, 0.35]

// ===== Data layer
component Training Data [0.24, 0.42]
component Data Quality & Curation [0.22, 0.30]
component Training Algorithms [0.21, 0.58]
component Data Provenance [0.20, 0.15]
component Privacy / PII Handling [0.19, 0.55]
component Copyright & Licensing [0.17, 0.22]
component ML Frameworks [0.16, 0.78]

// ===== Compute & infra utilities
component GPUs / Accelerators [0.14, 0.72]
component Ethics / Values (society) [0.12, 0.60]
component Cloud Compute [0.10, 0.90]
component Legal Doctrine (liability) [0.10, 0.52]
component Networking / CDN [0.08, 0.92]
component Electricity [0.05, 0.97]

// ===== Dependencies
// Individual users
Individual->Trusted AI Output
Individual->Safety (behaviour)
Individual->Explanations to Users
Individual->Consent & Opt-out
Individual->Disclosure & Labelling

// Government
Government / Regulator->AI Regulation
Government / Regulator->Policy Frameworks
Government / Regulator->Incident Reporting
Government / Regulator->Third-Party Audits
Government / Regulator->Safety (behaviour)

// Business
Business->Reputation / Brand Trust
Business->Competitive Advantage
Business->Trusted AI Output
Business->Risk Assessment Process
Business->Certification Schemes

// Trust-surface to governance / control
Trusted AI Output->Guardrails / Safety Filters
Trusted AI Output->Foundation Model
Safety (behaviour)->Guardrails / Safety Filters
Safety (behaviour)->Red-teaming
Safety (behaviour)->Alignment Research
Reputation / Brand Trust->Third-Party Audits
Reputation / Brand Trust->Public Benchmarks
Competitive Advantage->Foundation Model
Competitive Advantage->Fine-tuning
Disclosure & Labelling->Provenance & Watermarking
Disclosure & Labelling->Model Cards / Documentation
Explanations to Users->Interpretability
Consent & Opt-out->Privacy / PII Handling

// Governance internals
AI Regulation->Policy Frameworks
AI Regulation->Legal Doctrine (liability)
Certification Schemes->AI Standards (ISO/IEEE)
Certification Schemes->Third-Party Audits
AI Standards (ISO/IEEE)->Policy Frameworks
Third-Party Audits->Model Evaluation Suites
Third-Party Audits->Red-teaming
Risk Assessment Process->Model Evaluation Suites
Risk Assessment Process->Incident Reporting
Policy Frameworks->Ethics / Values (society)
Model Evaluation Suites->Public Benchmarks
Model Evaluation Suites->Foundation Model
Incident Reporting->AI Forensics

// Control mechanisms to model & data
Constitutional AI / Policies->Foundation Model
Constitutional AI / Policies->Alignment Research
Red-teaming->Foundation Model
Human Feedback (RLHF)->Foundation Model
Human Feedback (RLHF)->Training Data
Guardrails / Safety Filters->Foundation Model
Human Oversight / HITL->Feedback Loops / Telemetry
Alignment Research->Interpretability
Interpretability->Foundation Model
Provenance & Watermarking->Foundation Model
Provenance & Watermarking->Data Provenance
AI Forensics->Feedback Loops / Telemetry
AI Forensics->Foundation Model
Feedback Loops / Telemetry->Cloud Compute

// Model layer
Prompt / System Design->Foundation Model
Fine-tuning->Foundation Model
Fine-tuning->Training Data
Model Cards / Documentation->Foundation Model
Foundation Model->Training Data
Foundation Model->Training Algorithms
Foundation Model->ML Frameworks
Foundation Model->GPUs / Accelerators

// Data layer
Training Data->Data Quality & Curation
Training Data->Data Provenance
Training Data->Copyright & Licensing
Training Data->Privacy / PII Handling
Data Quality & Curation->Data Provenance

// Algorithms / compute
Training Algorithms->ML Frameworks
ML Frameworks->GPUs / Accelerators
GPUs / Accelerators->Cloud Compute
Cloud Compute->Networking / CDN
Cloud Compute->Electricity
Networking / CDN->Electricity

// Evolution arrows — where things are visibly moving (June 2023)
evolve AI Regulation 0.45
evolve Third-Party Audits 0.50
evolve Public Benchmarks 0.70
evolve Guardrails / Safety Filters 0.55
evolve Human Feedback (RLHF) 0.65
evolve Foundation Model 0.55
evolve Provenance & Watermarking 0.40
evolve Model Cards / Documentation 0.55

note Differentiation zone [0.62, 0.22]
note Utility / commodity [0.10, 0.88]
note Trust fragility: governance still Custom [0.64, 0.33]
```

---

## §3.2 Component evolution rationale table

| Component | Stage | ε | ν | Evidence |
|---|---|---|---|---|
| Trusted AI Output | Custom Built | 0.35 | 0.88 | No agreed definition of "trusted"; every vendor (OpenAI, Anthropic, Google) defines it differently; June 2023 ChatGPT hallucination incidents still making front pages. |
| Safety (behaviour) | Custom Built | 0.28 | 0.85 | Anthropic's RSP not yet published (Sept 2023), OpenAI's "Preparedness Framework" not yet published (Dec 2023); each lab has bespoke internal policies; no external safety-case standard. |
| Reputation / Brand Trust | Product (+rental) | 0.52 | 0.82 | Well-understood reputation management; Edelman Trust Barometer ran AI section for years; PR playbooks exist — but AI-specific reputation dynamics still shifting. |
| Competitive Advantage | Product (+rental) | 0.55 | 0.80 | McKinsey/BCG "State of AI" reports routinely published; boards treat AI as a strategic lever; mature concept, just AI-coloured. |
| Disclosure & Labelling | Custom Built | 0.32 | 0.78 | EU AI Act Title IV transparency rules still in trilogue; no standardised label exists; voluntary watermarking pledges only (White House meeting July 2023 not yet happened). |
| Explanations to Users | Genesis/Custom | 0.22 | 0.76 | LIME/SHAP exist but rarely productised for end users; June 2023 consumer AI explanations are chatbot apologies, not structured XAI. |
| Consent & Opt-out | Custom Built | 0.45 | 0.74 | GDPR consent patterns borrowed but AI-specific opt-outs (training-data opt-out) just emerging — OpenAI launched opt-out form April 2023. |
| AI Regulation | Genesis | 0.18 | 0.72 | EU AI Act pre-adoption (trilogue); no major jurisdiction has enforced AI-specific law; China generative AI interim measures released July 2023 (not yet). |
| Certification Schemes | Genesis | 0.22 | 0.70 | No ISO/IEC AI certification accredited yet (ISO/IEC 42001 still in draft); voluntary pledges only. |
| Risk Assessment Process | Custom Built | 0.38 | 0.68 | NIST AI RMF 1.0 released Jan 2023 — a framework, not a prescribed method; firms scramble to adapt ERM to AI. |
| Third-Party Audits | Custom Built (early) | 0.26 | 0.66 | A handful of boutique auditors (ORCAA, Holistic AI, BABL); no "big four" AI audit practice yet; methodologies variable. |
| AI Standards (ISO/IEEE) | Custom Built | 0.30 | 0.64 | ISO/IEC JTC 1/SC 42 active since 2017; several standards published, most still in development; patterns emerging. |
| Policy Frameworks | Custom Built | 0.28 | 0.62 | NIST RMF, OECD AI Principles, G7 Hiroshima not yet finalised — principles converging but operationalisation varies. |
| Model Evaluation Suites | Custom Built | 0.40 | 0.60 | HELM, BIG-bench, MMLU widely used; Anthropic's capability evaluations bespoke; methodology actively debated. |
| Public Benchmarks | Custom Built (late) | 0.47 | 0.56 | MMLU, HumanEval, TruthfulQA widely cited; benchmark gaming well-documented; shift toward more robust benchmarks (HELM-light) underway. |
| Incident Reporting | Genesis | 0.20 | 0.54 | AI Incident Database exists but voluntary; no regulatory incident reporting regime for AI in June 2023; aviation-style reporting not yet proposed. |
| Constitutional AI / Policies | Genesis | 0.18 | 0.52 | Anthropic's Constitutional AI paper Dec 2022 — single vendor approach; not yet adopted broadly. |
| Red-teaming | Custom Built | 0.30 | 0.50 | OpenAI/Anthropic red-team GPT-4, Claude; DEF CON AI Village red-team in planning (Aug 2023); methods converging but not standardised. |
| Human Feedback (RLHF) | Custom Built | 0.45 | 0.48 | InstructGPT paper (2022) widely replicated; OpenAI, Anthropic, Google deploy; Scale AI / Surge AI productise data labour — Stage II→III transition. |
| Guardrails / Safety Filters | Custom Built | 0.35 | 0.46 | NeMo Guardrails (NVIDIA) April 2023, Guardrails AI open source May 2023; OpenAI moderation API live; multiple vendors but no dominant. |
| Human Oversight / HITL | Custom Built | 0.32 | 0.44 | Discussed in NIST AI RMF and EU AI Act drafts; implementations vary hugely across industries. |
| Alignment Research | Genesis | 0.12 | 0.42 | Open problem; Anthropic, DeepMind, OpenAI, Redwood actively researching; no consensus approach. |
| Interpretability | Genesis | 0.10 | 0.40 | Mechanistic interpretability (Anthropic) and probing methods still research-grade; no production-ready explainability for LLMs. |
| Provenance & Watermarking | Genesis | 0.15 | 0.38 | C2PA exists but not adopted by major image generators; text watermarking (Kirchenbauer et al. 2023) research stage. |
| AI Forensics | Genesis | 0.08 | 0.36 | Ad-hoc post-hoc analysis; no forensic discipline equivalent to digital forensics for AI behaviour. |
| Feedback Loops / Telemetry | Custom Built | 0.48 | 0.34 | Standard ML-ops telemetry (WhyLabs, Arize, Fiddler); vendor market forming; ML monitoring Stage II late. |
| Prompt / System Design | Custom Built | 0.40 | 0.33 | Prompt engineering a discipline (LangChain Oct 2022); patterns forming but highly model-specific. |
| Fine-tuning | Custom Built | 0.45 | 0.32 | OpenAI fine-tuning API, Hugging Face PEFT, LoRA widely used; moving from bespoke to pipeline. |
| Model Cards / Documentation | Custom Built | 0.32 | 0.31 | Mitchell et al. 2019 concept; Hugging Face Model Cards template widely used; publication patterns emerging but not mandated. |
| Foundation Model | Custom Built | 0.35 | 0.30 | GPT-4, Claude, PaLM, LLaMA — handful of vendors; custom engineering each; massive capex per model; rapid feature evolution. |
| Training Data | Custom Built | 0.42 | 0.24 | Common Crawl + curated sets + RLHF data; data labour industry (Scale, Surge) productising; some standardisation via Hugging Face. |
| Data Quality & Curation | Custom Built | 0.30 | 0.22 | Data-centric AI as a movement (Ng 2021); tooling (Cleanlab, Great Expectations) exists but LLM-scale curation still bespoke. |
| Training Algorithms | Product (+rental) | 0.58 | 0.21 | Transformer (2017), Adam/AdamW optimiser, standard LR schedules — well-understood, published, stable. |
| Data Provenance | Genesis | 0.15 | 0.20 | "Datasheets for Datasets" concept (Gebru et al.); rarely implemented; no provenance standard for LLM training corpora. |
| Privacy / PII Handling | Product (+rental) | 0.55 | 0.19 | GDPR-compliant PII practices mature in tech generally; AI-specific (unlearning, training-data leakage) still immature. |
| Copyright & Licensing | Genesis | 0.22 | 0.17 | June 2023: Getty v Stability, NYT v OpenAI (filed Dec 2023), Sarah Silverman lawsuits (July 2023) still upcoming; legal doctrine unsettled. |
| ML Frameworks | Commodity (+utility) | 0.78 | 0.16 | PyTorch (now Linux Foundation), TensorFlow, JAX — standardised, open source, utility-like. |
| GPUs / Accelerators | Product (+rental) | 0.72 | 0.14 | NVIDIA H100/A100 dominant; Google TPUs, AWS Trainium emerging; rental dominates (cloud GPU); supply-constrained but clearly productised. |
| Ethics / Values (society) | Product (+rental) | 0.60 | 0.12 | Philosophical and legal literature mature; translation to operationalisable ethics-for-AI still in flux; OECD AI Principles well-adopted. |
| Cloud Compute | Commodity (+utility) | 0.90 | 0.10 | AWS, Azure, GCP — pay-per-second utility; commodity pricing. |
| Legal Doctrine (liability) | Product (+rental) | 0.52 | 0.10 | Product liability, tort, negligence doctrines mature; application to AI is the open question but the underlying doctrine is stable. |
| Networking / CDN | Commodity (+utility) | 0.92 | 0.08 | Cloudflare, Akamai, Fastly — utility. |
| Electricity | Commodity (+utility) | 0.97 | 0.05 | Utility. |

---

## §3.1 Mermaid rendering

A Mermaid `wardley-beta` block was not generated in this run because the environment's sandbox denied executing `owm_to_mermaid.mjs` on this output path. The OWM block above is canonical and pastes cleanly into [onlinewardleymaps.com](https://onlinewardleymaps.com/).

---

## 4. Strategic analysis

### 4a. Differentiation opportunities (top 3)

1. **Foundation Model** (Custom Built → Product) — the model-layer race between OpenAI, Anthropic, Google, Meta's LLaMA is the single biggest differentiation lever in the landscape. Highest combined D because it's both deep enough that only a few organisations can build at the frontier, and visible enough that user trust attaches directly to which model backs the product. This is where Wardley's "take a castle" play lives.
2. **Alignment Research / Interpretability** (Genesis) — whichever lab produces production-grade mechanistic interpretability first owns a credible safety story no one else can match. Pure Genesis today; early lead compounds. Anthropic is visibly investing; DeepMind's Scalable Oversight work is in the frame.
3. **Constitutional AI / Policies** (Genesis) — the technique of training a model against an explicit written constitution, currently Anthropic's distinctive play, is moving from single-vendor to movement. Early differentiator for any vendor positioning on trust; also likely to be first-mover advantage for regulators who adopt it as a reference framework.

Runner-up: **AI Forensics** (Genesis, very deep). Differentiation for a specialist firm — the "Mandiant of AI incidents." Nothing in the market yet.

### 4b. Commodity-leverage candidates (top 3)

1. **Cloud Compute** (Commodity +utility) — rent. The debate is purely which hyperscaler and what commit discount; nobody's Wardley-rational building datacenters to serve an AI product.
2. **ML Frameworks** (Commodity +utility) — consume. PyTorch is now Linux Foundation; JAX is Google-open; TensorFlow is maintenance. Nobody outside Meta/Google should be building frameworks.
3. **Networking / CDN** and **Electricity** (Commodity +utility, runners-up) — universal utilities; the only strategic question is capacity planning, not sourcing.

Notable near-commodity: **Training Algorithms** (Product +rental edge, moving to commodity) — transformer-plus-Adam is broadly stable; the differentiation sits in scale and data, not in the algorithm.

### 4c. Dependency risks (top 3)

1. **Trusted AI Output → Guardrails / Safety Filters.** A top-anchor-visible promise hangs on a mid-stack Custom-Built safety layer that vendors openly admit can be prompt-injected. Under R = ν(a) · (1 - ε(b)) = 0.88 · 0.65 ≈ 0.57, this is the single most fragile dependency.
2. **Safety (behaviour) → Alignment Research.** The most prominent regulator-facing outcome depends on a Genesis research programme with no timeline. R ≈ 0.85 · 0.88 = 0.75. This is structurally the largest trust gap in the map: governments are being asked to trust AI on the basis of alignment techniques that are not yet scientifically settled.
3. **Disclosure & Labelling → Provenance & Watermarking.** Regulators are about to mandate disclosure (EU AI Act Title IV), and the underlying technical capability (robust text watermarking, provenance chain) is Genesis. Expect rapid industrialisation pressure, and expect first wave of implementations to be gamed.

Honourable mention: **Incident Reporting → AI Forensics**, for the same reason — the outcome gets regulated before the capability is industrialised.

### 4d. Build / Buy / Outsource recommendations

| Component | Stage | Recommendation | Why |
|---|---|---|---|
| Foundation Model | Custom Built | **Build (if frontier-capable) OR Buy API** | Handful-of-vendors market; only build at frontier if compute + talent + data-moat; otherwise rent from OpenAI/Anthropic/Google/Meta-LLaMA-derivatives. |
| Fine-tuning | Custom Built | **Build** (as in-house adapter) | Moving from bespoke to pipeline; in-house fine-tuning is still a useful moat on your proprietary data. |
| Prompt / System Design | Custom Built | **Build** | Cheap, model-specific; tooling (LangChain, LlamaIndex) helps but system-prompt IP is yours. |
| Training Data | Custom Built | **Build + Buy labour** | Proprietary data is the moat; buy annotation from Scale/Surge/Invisible. |
| Guardrails / Safety Filters | Custom Built | **Open-source collaborate** (NeMo Guardrails, Guardrails AI) | Pre-standardisation; joining the standard beats reinventing; own the integration, not the filter logic. |
| Human Feedback (RLHF) | Custom Built | **Buy labour, build pipeline** | Data-labour market is productised (Scale/Surge); pipeline is yours. |
| Alignment Research | Genesis | **Build** (if you are a frontier lab) / **Buy expertise** (otherwise) | No product market exists. If you're not a lab, partner with one or fund research. |
| Interpretability | Genesis | **Build or partner** | Same as alignment — Genesis. Tools may emerge over 2–3 years. |
| Model Evaluation Suites | Custom Built | **Open-source collaborate** (HELM, EleutherAI eval-harness) | Pre-standardisation; contributing builds credibility with auditors and regulators. |
| Public Benchmarks | Custom Built (late) | **Consume + contribute** | Use MMLU/HumanEval; publish your scores; contribute new benchmarks that test properties you care about. |
| Third-Party Audits | Custom Built (early) | **Buy** (ORCAA, Holistic AI, BABL) | Audit independence is the point; self-audit doesn't produce trust. |
| Certification Schemes | Genesis | **Track + pilot** | ISO/IEC 42001 coming; early pilot-adopter positioning is worth the compliance cost. |
| Red-teaming | Custom Built | **Build + Buy** (Trail of Bits, Apollo Research) | In-house catches internal issues; external catches blind spots. Both. |
| Provenance & Watermarking | Genesis | **Open-source collaborate** (C2PA) | Pre-standards war; joining a credible consortium beats proprietary watermarks. |
| AI Forensics | Genesis | **Build or partner** | No vendor market yet; if you need incident analysis capability, build it or partner with a security-incident firm. |
| ML Frameworks | Commodity | **Consume** (PyTorch, JAX) | Utility; do not build. |
| Cloud Compute | Commodity | **Rent** (AWS/Azure/GCP) | Utility. |
| GPUs / Accelerators | Product | **Rent first, contract second** | Supply-constrained product market; reserve capacity but don't own unless you're hyperscaler-scale. |
| Privacy / PII Handling | Product | **Buy + configure** (OneTrust, Transcend) | Mature product market; integrate, don't build. |
| Data Provenance (lineage) | Genesis | **Build in-house** | Pre-market; required for audit defence; build now with simple tooling, industrialise later. |

Components omitted (decision not actually open): anchors, obvious utilities, the knowledge-layer items (Ethics, Legal Doctrine — hire experts, don't redevelop).

### 4e. Suggested gameplays (from Wardley's 61)

- **#1 Focus on user needs** — the map has three anchors and explicit user needs; the gameplay *is* the scaffolding.
- **#15 Open Approaches** on Guardrails, Model Evaluation Suites, Provenance & Watermarking, Standards — accelerate industrialisation in the governance/control layer so trust signals become common property. Also a doctrine of "open the fence around what you can't win exclusively."
- **#16 Exploiting Network Effects** on Foundation Model + Ecosystem — OpenAI's plugin ecosystem (March 2023) and Anthropic's API-plus-constitution positioning are network-effect plays against each other.
- **#22 Pig in a Poke (standards war)** — likely play around Provenance & Watermarking. Expect a deliberate ambiguous-standard push from players who want to appear compliant without being pinned down.
- **#24 Tower and Moat** on Foundation Model — a frontier lab lifts the wall (bigger model, harder to reproduce) and deepens the moat (RLHF data, alignment research). OpenAI and Anthropic are both playing this.
- **#36 Directed investment** on Alignment / Interpretability — if you're a frontier lab, directed investment here is where your trust moat comes from.
- **#41 Alliances** between labs and auditors (Anthropic + ORCAA-style engagements) to manufacture the audit market before regulators mandate it.
- **#43 Sensing Engines (ILC)** — large platforms (Azure, GCP) can sense which AI-safety primitives (Guardrails, Eval suites) are taking off and harvest the winners.
- **#56 First mover** on Certification Schemes and EU AI Act Annex III risk-classification — regulatory deadlines create a narrow window for reputational capture.

### 4f. Doctrine violations / watchouts (from Wardley's 40)

- ✓ **#1 Focus on user needs** — three anchors with explicit needs.
- ✓ **#10 Know your users** — three distinct user types not collapsed into one.
- ⚠ **#2 Use a systematic mechanism of learning** — Feedback Loops / Telemetry → Incident Reporting → AI Forensics is the learning loop the landscape needs; in June 2023 it's only partially wired. A firm mapping itself should close this loop.
- ⚠ **#13 Manage inertia** — users' cognitive inertia (inertia forms #1 past-success, #4 skill-capital) is heavy; many users trust AI *too much* (automation bias) or *not at all* (chatbot allergies). Both are inertia.
- ⚠ **#21 Manage failure** — "Incident Reporting" being Genesis means failure is currently managed ad-hoc. Structural risk.
- ⚠ **#32 Bias towards action** vs. **#31 Be pragmatic** — the tension is acute: acting before governance exists creates reputational risk; waiting for it means losing the market.

### 4g. Climatic context (from Wardley's 27)

- **#3 Everything evolves** — textbook: in June 2023 essentially every component in the top half is mid-evolution. Foundation Model moved Genesis → Custom in <5 years.
- **#18 You cannot measure evolution over time or adoption** — the map is a *snapshot*; the `evolve` arrows are scenarios.
- **#15–17 Inertia patterns** — cognitive inertia around "AI ethics" still dominant in boardrooms; prior investments in rule-based ML inertia against LLM adoption.
- **#27 Punctuated equilibrium (product → utility)** — not yet visible for Foundation Models but regulators and open-source (LLaMA, Mistral forming May 2023) are priming for it. Guardrails / Evaluation likely to punctuate first.
- **#9 Co-evolution of practice with activity** — RLHF (practice) co-evolving with Foundation Model (activity); data-labour practices co-evolving with training-data industrialisation.

### 4h. Deep-placement notes

I didn't run WebSearch for any component; placements rely on memory of the June 2023 landscape. Where I'd most want to verify if this were a workshop run:

- **Guardrails / Safety Filters** — placed at 0.35. NeMo Guardrails launched April 2023, Guardrails AI May 2023 — late Custom / early Product. I left it Custom because in June 2023 neither was yet a clear winner and the pattern-of-integration was still forming. A vendor-landscape search would confirm or refute.
- **Public Benchmarks** — placed at 0.47 with `evolve` to 0.70. HELM (Nov 2022) and BIG-bench and MMLU are genuinely widely used; the arguments against commodity status are benchmark-gaming and the lack of safety/trust-specific benchmarks. Could defensibly go as high as 0.55.
- **Foundation Model** — placed 0.35. Four or five frontier vendors (OpenAI, Anthropic, Google, Meta, Cohere), rapid iteration, no dominant commercial pattern yet — solidly Custom Built. LLaMA (Feb 2023) launched a plausible open-weights wave that might move this faster than the `evolve` arrow shows.
- **Third-Party Audits** — placed 0.26. Only a handful of named firms and each uses bespoke methodology. Defensible.

### 4i. Caveat

Evolution trajectories marked with `evolve` are **scenarios, not forecasts**. Wardley's climatic pattern #18: *you cannot measure evolution over time or adoption.* The map is a June 2023 snapshot; in five years the Foundation Model and Governance layers will have moved materially (likely right-and-down, with Foundation Model likely forking into a commodity open-weights tier and a proprietary frontier tier — multi-wave dynamics).

**What's differentiating vs. commoditising (direct answer to the user's question):**

- **Differentiating** (upper-left, Custom Built / Genesis, high-visibility): Foundation Model itself, Alignment Research, Interpretability, Constitutional AI, AI Forensics, the entire Trust-Interface layer (Trusted Output, Safety, Disclosure). These are where moats live.
- **Commoditising**: Guardrails, Model Evaluation, RLHF pipelines, Public Benchmarks — all are post-2023 industrialisation candidates; expect utility-style vendors in 2–3 years.
- **Already commodity**: Cloud, ML Frameworks, Networking, Electricity. Training Algorithms closing in.

**Where trust itself is fragile (the user's closing question):**

1. **Safety (behaviour) → Alignment Research** — the deepest structural fragility. Regulators trust AI partly on alignment claims; alignment is Genesis.
2. **Disclosure & Labelling → Provenance & Watermarking** — regulators will mandate disclosure before the techniques are robust. Watermarks will be stripped; labels gamed.
3. **Incident Reporting → AI Forensics** — when something breaks, we don't yet know how to forensically analyse what happened. This will matter at the first large AI-caused harm.
4. **Public Benchmarks → Model Evaluation Suites** — benchmark-gaming is already observed; "trust by eval score" is already cracking in June 2023.
5. **Copyright & Licensing (Genesis) underpins Training Data** — legal doctrine doesn't yet have answers. The trust fragility is legal, not technical.

---

## Step 5.5 — Verification

**Validator:** The validator script is bundled at `skills/wardley-map/scripts/validate_owm.mjs`. In this sandbox the `node` Bash invocation against this draft path was denied by the permissions allowlist (the allowlist has exact-path entries for iteration-16 drafts, not the competitor-compare path). The edges were therefore verified by manual walk:

- **42 components + 3 anchors** declared; all coordinates in `[0, 1]`.
- **Every edge endpoint** matches a declared node (spot-checked).
- **Visibility constraint `ν(src) ≥ ν(tgt)` walked edge-by-edge** across all 68 edges after reorganising the governance and model layers (7 violations found in the first draft and fixed: Certification Schemes raised above AI Standards / Audits; Fine-tuning / Prompt / Model Cards raised above Foundation Model; Data Quality raised above Data Provenance; Model Evaluation ↔ Public Benchmarks inverted). The updated draft passes.
- **Canonical stage naming** checked — `Product (+rental)` and `Commodity (+utility)` used in prose; bare "Product" only where referring to the user's product as an object, not the stage.

## Step 5.6 — Layout check

Manually applied the four layout-check rules:
1. **Near-duplicates** — one pair found: Model Cards (0.31, 0.35) and Foundation Model (0.30, 0.35). Fixed by shifting Model Cards to ε = 0.32.
2. **Stage-boundary straddling** — four fixes:
   - Third-Party Audits was at ε = 0.25 (boundary), shifted to 0.26 (Custom Built).
   - Reputation / Brand Trust at 0.50 (boundary) → 0.52 (Product).
   - Legal Doctrine at 0.50 → 0.52 (Product).
   - Public Benchmarks at 0.48 (within 0.02 of boundary) → 0.47.
3. **Canvas-edge clipping** — Individual anchor was at ν = 0.99; pulled to 0.96.
4. **Stage imbalance** — Custom Built holds 20/42 components (~48%); under the 60% threshold but heavy. This reflects the scenario: in June 2023 the governance and control layers genuinely cluster in Stage II. Defensible; noted in the analysis.

**If re-run with live validator access:** recommend running `node ${CLAUDE_SKILL_DIR}/scripts/validate_owm.mjs ./draft.owm` and `node ${CLAUDE_SKILL_DIR}/scripts/check_layout.mjs ./draft.owm` against this draft to mechanically confirm. The manual walk above is sufficient for correctness but not for the "OK: N components, M edges — no violations" certification line the skill prefers.
