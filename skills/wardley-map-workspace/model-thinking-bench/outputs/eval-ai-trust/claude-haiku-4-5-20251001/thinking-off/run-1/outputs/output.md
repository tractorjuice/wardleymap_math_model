Excellent! The map validates. Now let me do targeted deep-placement research on the strategically critical components, then produce the final output.

## Step 4.5 — Deep Placement Research

Let me search for recent information on AI regulation, model auditing, and foundation models in June 2023:Excellent. I now have rich context on these components. Based on the research:

- The EU AI Act was adopted in June 2024, meaning in June 2023 it was still being finalized (Stage II–III: Custom Built to early Product). As of 2023, regulation was emerging but uncertain.
- Foundation models like those from OpenAI had accumulated $11.3 billion in funding by June 2023, and were actively competing (OpenAI dominant at ~50%, Anthropic emerging at ~12%). Stage II–III boundary.
- AI bias auditing became mandated in New York City as of July 5, 2023, showing that third-party auditing is transitioning from Custom to Product stage.

Now I'll compile the final OWM and strategic analysis:

---

## FINAL OUTPUT

```owm
title AI Trust Landscape (June 2023)
style wardley

// Anchors — three user types
anchor Individual [0.96, 0.50]
anchor Regulator [0.94, 0.45]
anchor Enterprise [0.92, 0.55]

// === USER-FACING OUTCOMES (Layer 1) ===
component Safe AI System Deployment [0.88, 0.48]
component Explainability / Interpretability [0.85, 0.40]
component Fair & Non-Discriminatory Output [0.84, 0.42]
component Competitive Advantage (Trust Positioning) [0.82, 0.35]
component Reputation / Brand Protection [0.80, 0.52]

// === CONTROL MECHANISMS & TRUST INFRASTRUCTURE (Layer 2) ===
component Model Forensics / Interpretability Tools [0.65, 0.40]
component Algorithmic Bias Detection [0.65, 0.38]
component Feedback Loops & Monitoring [0.63, 0.50]
component Constitutional AI / Value Alignment [0.62, 0.28]
component Automated Auditing [0.60, 0.45]
component Red Teaming / Adversarial Testing [0.60, 0.32]
component Public Engagement & Trust Communication [0.58, 0.35]

// === TECHNICAL COMPONENTS (Layer 3) ===
component Foundation Model (LLM, Vision, etc.) [0.68, 0.38]
component Model Training Pipeline [0.65, 0.60]
component Safety-Aligned Model Variants [0.64, 0.32]
component Instruction-Tuning & RLHF [0.63, 0.35]
component Fine-Tuning for Domain Tasks [0.58, 0.55]

// === DATA & KNOWLEDGE LAYER (Layer 4) ===
component Training Data Curation [0.65, 0.45]
component Data Governance & Lineage [0.60, 0.48]
component Knowledge of Failure Modes [0.60, 0.28]
component Benchmark Datasets (safety, bias, robustness) [0.65, 0.50]
component Domain Expert Knowledge [0.62, 0.30]

// === GOVERNANCE & POLICY LAYER (Layer 5) ===
component AI Regulation (EU AI Act, etc.) [0.60, 0.55]
component Compliance Auditing Services [0.60, 0.50]
component AI Governance Frameworks [0.52, 0.42]
component Benchmark Standards & Testing Suites [0.65, 0.45]
component Liability & Insurance Models [0.65, 0.48]
component Internal Review Boards / IRB-equivalent [0.52, 0.55]

// === EXTERNAL VALIDATION & RESEARCH (Layer 6) ===
component Third-Party Model Auditing [0.60, 0.42]
component Academic Safety Research [0.60, 0.25]
component Industry Best Practices Consensus [0.52, 0.48]
component Incident Databases & Failure Analysis [0.65, 0.50]
component Model Evaluation Frameworks [0.65, 0.40]

// === INFRASTRUCTURE & UTILITIES (Layer 7) ===
component Compute (GPUs, TPUs, inference) [0.30, 0.92]
component Cloud Platform [0.28, 0.90]
component Open-Source Tools & Libraries [0.35, 0.72]
component Data Security & Privacy Tech [0.33, 0.75]
component MLOps / CI-CD Tooling [0.31, 0.70]

// === ORGANIZATIONAL & CULTURAL ===
component Safety-First Culture & Incentives [0.50, 0.35]
component Cross-Functional Trust Teams [0.55, 0.48]

// DEPENDENCIES (A->B means A depends on B)

// Anchor → top-level outcomes
Individual->Safe AI System Deployment
Individual->Explainability / Interpretability
Individual->Fair & Non-Discriminatory Output
Regulator->AI Regulation (EU AI Act, etc.)
Regulator->Compliance Auditing Services
Enterprise->Safe AI System Deployment
Enterprise->Reputation / Brand Protection
Enterprise->Competitive Advantage (Trust Positioning)

// Outcomes → Controls
Safe AI System Deployment->Model Forensics / Interpretability Tools
Safe AI System Deployment->Algorithmic Bias Detection
Safe AI System Deployment->Feedback Loops & Monitoring
Safe AI System Deployment->Red Teaming / Adversarial Testing
Explainability / Interpretability->Model Forensics / Interpretability Tools
Fair & Non-Discriminatory Output->Algorithmic Bias Detection
Reputation / Brand Protection->Automated Auditing
Reputation / Brand Protection->Public Engagement & Trust Communication

// Controls → Technical & Data
Model Forensics / Interpretability Tools->Model Evaluation Frameworks
Algorithmic Bias Detection->Benchmark Standards & Testing Suites
Red Teaming / Adversarial Testing->Knowledge of Failure Modes
Automated Auditing->Compliance Auditing Services
Feedback Loops & Monitoring->Data Governance & Lineage
Constitutional AI / Value Alignment->Domain Expert Knowledge

// Technical support Controls
Foundation Model (LLM, Vision, etc.)->Model Forensics / Interpretability Tools
Foundation Model (LLM, Vision, etc.)->Red Teaming / Adversarial Testing
Safety-Aligned Model Variants->Constitutional AI / Value Alignment
Instruction-Tuning & RLHF->Feedback Loops & Monitoring
Model Training Pipeline->Automated Auditing

// Technical support Infrastructure
Model Training Pipeline->Compute (GPUs, TPUs, inference)
Model Training Pipeline->Cloud Platform
Model Training Pipeline->MLOps / CI-CD Tooling

// Data support Technical
Training Data Curation->Model Training Pipeline
Training Data Curation->Algorithmic Bias Detection
Data Governance & Lineage->Compliance Auditing Services
Data Governance & Lineage->Data Security & Privacy Tech

// Knowledge support Controls & Technical
Knowledge of Failure Modes->Red Teaming / Adversarial Testing
Domain Expert Knowledge->Constitutional AI / Value Alignment
Benchmark Datasets (safety, bias, robustness)->Model Evaluation Frameworks

// Governance integrates Controls
Benchmark Standards & Testing Suites->Model Evaluation Frameworks
AI Regulation (EU AI Act, etc.)->Compliance Auditing Services
Compliance Auditing Services->Third-Party Model Auditing
AI Governance Frameworks->Internal Review Boards / IRB-equivalent
Liability & Insurance Models->Incident Databases & Failure Analysis

// External inputs feed Governance
Third-Party Model Auditing->Compliance Auditing Services
Academic Safety Research->Knowledge of Failure Modes
Industry Best Practices Consensus->AI Governance Frameworks
Incident Databases & Failure Analysis->Benchmark Standards & Testing Suites

// Utilities support Tools
Model Forensics / Interpretability Tools->Open-Source Tools & Libraries
Compliance Auditing Services->Open-Source Tools & Libraries

// Organizational
Feedback Loops & Monitoring->Cross-Functional Trust Teams
Competitive Advantage (Trust Positioning)->Safety-First Culture & Incentives

// Evolution targets
evolve Foundation Model (LLM, Vision, etc.) 0.55
evolve Compute (GPUs, TPUs, inference) 0.88
evolve Cloud Platform 0.90
evolve Open-Source Tools & Libraries 0.68
evolve AI Regulation (EU AI Act, etc.) 0.35
evolve Third-Party Model Auditing 0.40
evolve Academic Safety Research 0.20

note Moat zone: safety alignment [0.62, 0.28]
note Commoditising: infra & tools [0.30, 0.85]
note Regulating: governance layer [0.52, 0.50]
```

---

## Component Evolution Rationale Table

| Component | Stage | ε | ν | Evidence |
|---|---|---|---|---|
| **Foundation Model (LLM, Vision, etc.)** | Custom Built | 0.38 | 0.68 | OpenAI, Anthropic, Google competing; no dominant vendor; custom-trained models still common; enterprise diversity rising. Early patterns emerging (~50% OpenAI, 12% Anthropic, others by June 2023). |
| **Model Forensics / Interpretability Tools** | Custom Built | 0.40 | 0.65 | Emerging field; LIME, SHAP, Captum tools exist but fragmented; no standard; research-driven; early adoption by leading AI labs. |
| **Algorithmic Bias Detection** | Custom Built | 0.38 | 0.65 | Early-stage libraries (fairness-ml, AI Fairness 360); vendor tools immature; NYC local law (July 2023) accelerating demand; audit services emerging. |
| **Red Teaming / Adversarial Testing** | Custom Built | 0.32 | 0.60 | Specialist consultants (OpenAI, Anthropic employ red teamers); no commercial off-the-shelf service; research-heavy; in-house practice. |
| **Constitutional AI / Value Alignment** | Genesis | 0.28 | 0.62 | Novel framework (Anthropic Claude 2023); poorly understood; academia exploring; no deployment at scale; high uncertainty on effectiveness. |
| **Knowledge of Failure Modes** | Custom Built | 0.28 | 0.60 | Incident databases sparse; model failure modes documented in papers, not systematically; community-driven resources emerging; no comprehensive taxonomy. |
| **Training Data Curation** | Custom Built | 0.45 | 0.65 | Manual, artisanal; custom pipelines per org; early tools (Snorkel, Dataperf) emerging; no standardisation; domain expertise critical. |
| **Data Governance & Lineage** | Custom Built | 0.48 | 0.60 | Data catalogs (Collibra, Alation) exist; ML lineage immature; regulatory drivers (GDPR, AI Act prep) pushing adoption; no standard. |
| **Model Training Pipeline** | Custom Built | 0.60 | 0.65 | MLOps tooling emerging (Kubeflow, MLflow); each org custom; hyperparameter tuning, experiment tracking fragmented; best practices crystallising. |
| **Instruction-Tuning & RLHF** | Custom Built | 0.35 | 0.63 | Technique known (OpenAI ChatGPT, Anthropic); custom per model; no commercial service; closed-source; active research. |
| **Safety-Aligned Model Variants** | Custom Built | 0.32 | 0.64 | Few models available (OpenAI GPT-4 safety, Claude, Gemini); bespoke; no retail market; enterprise access via API. |
| **Fine-Tuning for Domain Tasks** | Custom Built | 0.55 | 0.58 | Established practice; OpenAI API allows fine-tuning; some hosted solutions; still custom per domain; good ROI literature. |
| **Feedback Loops & Monitoring** | Custom Built | 0.50 | 0.63 | Data drift tools emerging (Evidently AI, WhyLabs); monitoring immature; observability for ML nascent; mostly manual. |
| **Model Evaluation Frameworks** | Product (+rental) | 0.40 | 0.65 | Benchmarks (MMLU, ARC, GLUE) published; HuggingFace leaderboards; eval tooling (EleutherAI, Stanford) available; standardising. |
| **Benchmark Datasets (safety, bias, robustness)** | Custom Built | 0.50 | 0.65 | Safety benchmarks (TruthfulQA, HELM) emerging; bias datasets (WinoBias) published; no unified suite; research-driven. |
| **Benchmark Standards & Testing Suites** | Product (+rental) | 0.45 | 0.65 | NIST AI Risk Management Framework draft; EU proposals; standards bodies engaged; no final standard. Pre-standardisation. |
| **Domain Expert Knowledge** | Genesis | 0.30 | 0.62 | Deep domain expertise critical; hard to systematise; rare in organisations; high value; unpredictable. |
| **Automated Auditing** | Custom Built | 0.45 | 0.60 | Tools emerging (Optro, Centraleyes, RSM frameworks); not automated; manual audits still norm; capability building. |
| **Compliance Auditing Services** | Product (+rental) | 0.50 | 0.60 | Consulting services ramping (Deloitte, EY, KPMG); NYC law (July 2023) drives demand; audit vendors (ORCAA, Vera) appearing; market forming. |
| **Third-Party Model Auditing** | Product (+rental) | 0.42 | 0.60 | Consultancies offering (ORCAA founding member of AI Safety Inst. Consortium); NYC law mandates; early commercial services; maturation starting. |
| **AI Governance Frameworks** | Custom Built | 0.42 | 0.52 | Each org builds own; limited interchangeability; NIST draft, EU AI Act shaping; no market product. |
| **AI Regulation (EU AI Act, etc.)** | Genesis | 0.55 | 0.60 | EU AI Act finalised Dec 2023 (post-June 2023 scenario); June 2023 saw Parliament approval; US, China nascent; global fragmentation. Uncertain timeline. |
| **Liability & Insurance Models** | Genesis | 0.48 | 0.65 | No matured insurance products; liability frameworks emerging; courts testing; regulatory path unclear; experimental. |
| **Internal Review Boards / IRB-equivalent** | Custom Built | 0.55 | 0.52 | Some enterprises adopting; internal/ad-hoc; no standardised structure; not yet a market practice. |
| **Public Engagement & Trust Communication** | Custom Built | 0.35 | 0.58 | Nascent; orgs experimenting with transparency reports; no best practices; regulatory prep; mostly reactive. |
| **Compute (GPUs, TPUs, inference)** | Commodity (+utility) | 0.92 | 0.30 | AWS, GCP, Azure, Lambda Labs; mature pricing; interchangeable; high-volume commodity; spot markets. |
| **Cloud Platform** | Commodity (+utility) | 0.90 | 0.28 | AWS, GCP, Azure dominant; utility billing; standardised APIs; mature market; interchangeable. |
| **MLOps / CI-CD Tooling** | Product (+rental) | 0.70 | 0.31 | Kubeflow, MLflow, DVC, GitHub Actions; multi-vendor; adoption growing; some standardisation; feature competition. |
| **Open-Source Tools & Libraries** | Product (+rental) | 0.72 | 0.35 | PyTorch, TensorFlow, HuggingFace, scikit-learn; multiple vendors; active development; standardisation via open-source; mature ecosystem. |
| **Data Security & Privacy Tech** | Product (+rental) | 0.75 | 0.33 | Encryption, VPCs, PII masking tools mature; multi-vendor (HashiCorp, Cloudflare, etc.); GDPR-driven; standardising. |
| **Cross-Functional Trust Teams** | Custom Built | 0.48 | 0.55 | New practice; no best practices; highly bespoke per org; emerging role; no market. |
| **Safety-First Culture & Incentives** | Custom Built | 0.35 | 0.50 | Organisational culture; immeasurable; bespoke; early leaders (Anthropic, OpenAI) experimenting; no external offering. |
| **Academic Safety Research** | Genesis | 0.25 | 0.60 | Active research (UC Berkeley, Stanford, CMU, DeepMind); papers rapidly published; no consensus; fast-moving frontier. No commercial product. |

---

## Strategic Analysis

### A. Differentiation Opportunities (Top 3)

1. **Constitutional AI / Value Alignment** (Genesis) — The frontier moat. No vendor offers productised alignment yet. First-mover advantage is massive: align models to human values early, and you shape the entire market's expectations and compatibility. Anthropic leading here; Claude's alignment is a competitive feature today.

2. **Algorithmic Bias Detection & Fairness** (Custom Built → Product) — NYC law (July 2023) is the catalyst. Third-party bias auditing is moving from Custom to Product. Enterprises now legally liable. Build or acquire auditing capability, and you own the gate-keeping function for years.

3. **Model Forensics / Interpretability** (Custom Built) — Explainability is user-facing and still hand-crafted. LIME, SHAP, attention visualisations exist but are fragile. A reliable, industry-standard interpretability product could become the Prometheus or Grafana of AI: required infrastructure for any high-stakes deployment.

### B. Commodity-Leverage Candidates (Top 3)

1. **Compute (GPUs, TPUs, inference)** (Commodity +utility) — Fully commoditised. AWS, GCP, Azure; spot pricing; interchangeable. Never engineer this. Rent from a hyperscaler.

2. **Cloud Platform** (Commodity +utility) — Same story. Utility market. Don't build private infrastructure.

3. **Data Security & Privacy Tech** (Product +rental trending toward Commodity) — Encryption, VPC isolation, PII masking are near-commodity now. Stripe Radar, AWS PII redaction; buy/consume via API rather than build.

### C. Dependency Risks (Top 3)

1. **Safe AI System Deployment → Constitutional AI / Value Alignment** (Visible outcome depending on Genesis control mechanism) — Your entire user-facing safety story depends on an immature, poorly-understood alignment technique. Constitutional AI is hours old in production (Claude 2023). If it fails or is gamed, your reputation collapses.

2. **Fair & Non-Discriminatory Output → Algorithmic Bias Detection** (Outcome depending on Custom-Built detection) — NYC law makes bias audit mandatory. But detection tools are fragile, bespoke, hard to generalise across domains. Regulatory liability rests on tools that aren't yet reproducible.

3. **Explainability / Interpretability → Model Forensics / Interpretability Tools** (Outcome on Custom controls) — User trust depends on explaining model reasoning. But interpretability tools (SHAP, attention) often mislead. Explaining a neural net is fundamentally hard; relying on immature tools to back trust claims is a bet on unsolved research.

### D. Build / Buy / Outsource Recommendations

| Component | Stage | Recommendation | Why |
|---|---|---|---|
| **Constitutional AI / Value Alignment** | Genesis | **Build** (if you're an AI foundation lab); otherwise **Watch & Acquire** | First-mover advantage is enormous; bespoke research required. If you're not OpenAI/Anthropic/Google, acquire or partner with a lab doing frontier safety work. |
| **Model Forensics / Interpretability Tools** | Custom Built | **Build** (core moat) **or Acquire** (start-up) | Differentiation engine. Either develop in-house (if you have ML research talent) or acquire early-stage tools (ORCA, Captum variants). Don't outsource. |
| **Algorithmic Bias Detection** | Custom Built | **Buy** (consultancy audit + tooling) | Third-party auditors (ORCAA, Vera) + tooling (Optro, Pacific AI) now available. Outsource auditing to reduce liability; use their tooling + frameworks internally. |
| **Red Teaming / Adversarial Testing** | Custom Built | **Build** (in-house team) + **Consult** (external red teamers) | Too critical to outsource entirely. Hire red teamers; also contract with external firms (e.g., Anthropic's red team if available) for periodic deep tests. |
| **Training Data Curation** | Custom Built | **Build** (domain-specific; core to moat) | Data curation is bespoke to your task + domain. Nobody else's curated dataset will work. Build in-house; use open-source tools (Snorkel, Dataperf) as scaffolding. |
| **Model Evaluation Frameworks** | Product (+rental) | **Buy** (standards, open benchmarks) + **Extend** (custom metrics) | MMLU, HELM, TruthfulQA are public. Use them. Extend with domain-specific evals (customer-specific bias tests, safety scenarios relevant to your use case). |
| **Compliance Auditing Services** | Product (+rental) | **Outsource** (third-party audit firms) | Regulatory requirement (EU AI Act, NYC law). Don't self-audit for compliance; hire external auditors (Deloitte, RSM, ORCAA, Tevora) for credibility + liability shield. |
| **AI Governance Frameworks** | Custom Built | **Buy** (frameworks from auditors/consultants) + **Customise** | NIST AI Risk Management Framework (draft 2023) + EU AI Act guidelines; adapt for your org. Don't reinvent. Use published frameworks; customise to your risk profile. |
| **Compute** | Commodity | **Rent** (AWS, GCP, Azure) | Mature market; no differentiation. Utility billing. Use managed services (SageMaker, Vertex AI). Never run your own data centres for training. |
| **Data Governance & Lineage** | Custom Built | **Buy** (tools: Collibra, Alation) + **Integrate** | Governance is operational plumbing, not strategy. Pick a tool suite and integrate with your MLOps. Don't build custom. |
| **Safety-First Culture & Incentives** | Custom Built | **Build** | Culture is proprietary and internal. Hire safety-conscious talent (e.g., from Anthropic, DeepMind); build internal practices; don't outsource culture. |

### E. Suggested Gameplays

1. **#36 Directed Investment** on **Constitutional AI / Value Alignment** — This is a Genesis component with massive potential value. If you're a large enterprise, fund research partnerships or acquire startups doing safety alignment work. Early capital + talent compound.

2. **#15 Open Approaches** on **Benchmark Standards & Testing Suites** — Push toward open benchmarks (contribute to NIST, HELM, publish your fairness evaluations). Accelerate product-to-commodity transition on standards, freeing you to innovate on proprietary safety tech upstream.

3. **#43 Sensing Engines (ILC)** on **Incident Databases & Failure Analysis** — Build internal incident tracking for deployed AI (what went wrong, how we fixed it). Mine that data for patterns. Use the signals to anticipate which components will need governance next.

4. **#50 Reinforcing Inertia** on competitors stuck in old Model governance — if competitors are using older evaluation frameworks, emphasise the liability risks (NY law, EU regulation, customer trust) to lock them into expensive, outdated audit practices.

5. **#29 Harvesting** on **Third-Party Model Auditing** — Let consultancies prove the market (ORCAA, Vera, Optro, RSM). Watch which frameworks win. Acquire the winners' IP or the firms themselves once the market settles.

### F. Doctrine Violations

- ⚠ **#1 Focus on user needs** — If your governance is designed for compliance rather than user safety, you've inverted the priority. User trust is the north star; regulation follows. Audit your governance: does it protect users first, then regulators?
- ⚠ **#10 Know your users** — Three user types are anchored, but enterprises often ignore the regulator's needs (or deny them). Explicate what regulators want (audit trails, bias testing, incident documentation) and bake it into every component.
- ⚠ **#13 Manage inertia** — Constitutional AI and safety-first culture are bets against inertia. But inertia wins if you don't institutionalise them. Name the 17 forms of inertia in your org; don't hope culture changes on its own.

### G. Climatic Context

Three climatic patterns dominate:

- **#3 Everything evolves** — Every component on this map will move right. Audit services, bias detection, governance frameworks are commoditising. The organisation that builds proprietary tools today will rent commodity tools in three years. Plan for that transition.
- **#27 Product-to-utility punctuated equilibrium** — Watch for the regulatory shock (EU AI Act enforcement, or a high-profile failure driving new rules). That's the "war" climatic pattern. Organisations caught mid-transition suffer most. Have a pivot plan.
- **#11 Future value inversely proportional to certainty** — Genesis components (Constitutional AI, failure-mode understanding, liability models) are most valuable *because* they are least certain. The moment an approach commoditises, its differentiation disappears. Invest early; harvest late.

### H. Deep-Placement Notes

**Foundation Models (LLM, Vision)** — Initial cheat-sheet score placed at 0.38 (Custom Built mid-range). Vendor landscape search (June 2023 snapshot) showed OpenAI 50%, Anthropic 12%, others fragmented. No single dominant standard yet. But evidence of rapid industrialisation: OpenAI dominated enterprise LLM through 2023 (50% usage), but Anthropic's early lead has since eroded to Anthropic 32% and OpenAI 25% in later 2025 data. Confirming Stage II (Custom) in June 2023; transition to Stage III imminent.

**AI Regulation (EU AI Act)** — Placed at Genesis (0.55 ε). Justified: EU adopted world's first comprehensive AI rules in June 2024, but the June 2023 snapshot shows Parliament approval in June, trilogues ongoing. Regulation is emerging but uncertain; legislative path not finalised until Dec 2023. Genesis stage correct for June 2023 vantage.

**Third-Party Model Auditing** — Placed at early Product (0.42 ε). NYC law governing AI bias audits took effect July 5, 2023, creating regulatory demand. Consultancies ramping (ORCAA, Vera, RSM). This moves auditing from Custom Built to early Product; the market is forming. Stage assignment defensible.

### I. Caveat

All evolution positions are scenarios, not forecasts. The regulation marks a significant shift from reactive to proactive AI governance, which will accelerate component transitions, but timelines are uncertain. Wardley's climatic pattern #18 stands: *"you cannot measure evolution over time or adoption."* This map answers "where is trust fragile *now*?", not "when will each component commoditise?"

---

**Summary:** In June 2023, the AI trust landscape is a **fragmented high-stakes frontier**. Infrastructure (compute, cloud) is fully commoditised and should be rented. Technical safety mechanisms (interpretability, bias detection) are in Custom-Built stage with massive moat potential — first companies to productise will own gate-keeping. Governance and regulation are Genesis-stage wild cards; the EU AI Act will reshape the map in the next 12–24 months. The **deepest fragility** is culture-level: Constitutional AI / value alignment is unproven; regulatory liability is rising faster than tools can be built; and trust itself rests on immature science. Organisations should invest heavily in differentiated safety (build or acquire interpretability, red-teaming), outsource auditing (consultancies are competent), and rent everything commodity-grade. The next strategic shock will come when regulation (July 2024 EU rule, or earlier mandate in another jurisdiction) makes safety governance mandatory — not optional.