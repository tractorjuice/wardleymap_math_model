---

## OWM Output

```owm
title AI Trust Landscape (June 2023)
style wardley

anchor Individual User [0.96, 0.60]
anchor Government / Regulator [0.95, 0.55]
anchor Enterprise [0.94, 0.65]

component User Trust in System [0.85, 0.60]
component System Safety & Robustness [0.82, 0.48]
component Regulatory Compliance Status [0.80, 0.55]
component Competitive Advantage via AI [0.78, 0.50]

component Constitutional AI & Alignment Techniques [0.62, 0.38]
component RLHF (Reinforcement Learning from Human Feedback) [0.60, 0.42]
component Monitoring & Anomaly Detection [0.58, 0.50]
component User Feedback Loops [0.55, 0.48]
component Red Teaming & Adversarial Testing [0.60, 0.35]

component Model Interpretability Methods (SHAP, attention) [0.54, 0.40]
component Model Cards & Documentation [0.54, 0.48]
component Explainability UI Components [0.50, 0.55]

component Model Evaluation Benchmarks [0.40, 0.50]
component Bias & Fairness Testing [0.52, 0.42]
component Robustness Testing [0.52, 0.38]

component AI Governance Framework [0.50, 0.40]
component Regulatory Compliance Framework (EU AI Act, etc.) [0.50, 0.38]
component Industry Standards (ISO 42001, IEEE) [0.50, 0.42]
component Internal Risk Assessment Process [0.45, 0.45]

component Third-Party AI Audits & Certification [0.52, 0.32]
component Incident Logging & Forensics [0.48, 0.50]
component External Safety Assessment [0.48, 0.35]

component Large Language Models (LLMs) [0.48, 0.45]
component Model Training Data [0.40, 0.48]
component Training & Inference Compute [0.35, 0.78]
component Cloud Infrastructure (AWS, GCP, Azure) [0.16, 0.92]

component MLOps & Model Deployment Pipeline [0.42, 0.55]
component Data Versioning & Management [0.40, 0.50]
component Model Registry [0.40, 0.52]

component Data Quality & Curation [0.38, 0.45]
component Data Provenance Tracking [0.36, 0.40]
component Synthetic Data Generation [0.35, 0.42]

component ML Safety Research & Papers [0.58, 0.25]
component AI Ethics Theory & Research [0.50, 0.28]
component Domain Expertise (application-specific) [0.38, 0.35]
component Legal & Policy Knowledge [0.48, 0.32]

component Monitoring & Logging Infrastructure [0.16, 0.85]
component Container Orchestration (Kubernetes) [0.16, 0.82]
component Database & Storage [0.16, 0.88]

Individual User->User Trust in System
Government / Regulator->Regulatory Compliance Status
Enterprise->Competitive Advantage via AI
Enterprise->User Trust in System

User Trust in System->System Safety & Robustness
User Trust in System->Regulatory Compliance Status
System Safety & Robustness->Constitutional AI & Alignment Techniques
System Safety & Robustness->RLHF (Reinforcement Learning from Human Feedback)
System Safety & Robustness->Monitoring & Anomaly Detection
System Safety & Robustness->Red Teaming & Adversarial Testing
System Safety & Robustness->Model Evaluation Benchmarks
System Safety & Robustness->Bias & Fairness Testing

Regulatory Compliance Status->Regulatory Compliance Framework (EU AI Act, etc.)
Regulatory Compliance Status->Industry Standards (ISO 42001, IEEE)
Regulatory Compliance Status->Third-Party AI Audits & Certification

Competitive Advantage via AI->Constitutional AI & Alignment Techniques
Competitive Advantage via AI->Model Interpretability Methods (SHAP, attention)

Constitutional AI & Alignment Techniques->Large Language Models (LLMs)
Constitutional AI & Alignment Techniques->ML Safety Research & Papers
RLHF (Reinforcement Learning from Human Feedback)->Large Language Models (LLMs)
RLHF (Reinforcement Learning from Human Feedback)->User Feedback Loops

Monitoring & Anomaly Detection->Incident Logging & Forensics
Red Teaming & Adversarial Testing->External Safety Assessment

Model Evaluation Benchmarks->Model Training Data
Bias & Fairness Testing->Model Training Data
Robustness Testing->Model Training Data

Model Interpretability Methods (SHAP, attention)->Large Language Models (LLMs)
Model Cards & Documentation->Model Interpretability Methods (SHAP, attention)
Model Cards & Documentation->Explainability UI Components

AI Governance Framework->Internal Risk Assessment Process
AI Governance Framework->Data Quality & Curation
Regulatory Compliance Framework (EU AI Act, etc.)->AI Governance Framework
Industry Standards (ISO 42001, IEEE)->Regulatory Compliance Framework (EU AI Act, etc.)
Industry Standards (ISO 42001, IEEE)->Legal & Policy Knowledge

Third-Party AI Audits & Certification->Incident Logging & Forensics
Third-Party AI Audits & Certification->Internal Risk Assessment Process
Third-Party AI Audits & Certification->External Safety Assessment

Large Language Models (LLMs)->Model Training Data
Large Language Models (LLMs)->Training & Inference Compute
Model Training Data->Data Quality & Curation
Model Training Data->Data Versioning & Management
Model Training Data->Domain Expertise (application-specific)
Data Quality & Curation->Data Provenance Tracking
Data Quality & Curation->Synthetic Data Generation

Training & Inference Compute->Cloud Infrastructure (AWS, GCP, Azure)
MLOps & Model Deployment Pipeline->Training & Inference Compute
MLOps & Model Deployment Pipeline->Model Registry
Model Registry->Model Evaluation Benchmarks
Data Versioning & Management->Database & Storage

Monitoring & Logging Infrastructure->Cloud Infrastructure (AWS, GCP, Azure)
Container Orchestration (Kubernetes)->Cloud Infrastructure (AWS, GCP, Azure)
Database & Storage->Cloud Infrastructure (AWS, GCP, Azure)

note Differentiation zone: Constitutional AI, Interpretability, Red Teaming [0.58, 0.33]
note Transition to commodity: Evaluation Benchmarks, MLOps, Cloud [0.35, 0.70]
note Fragility: Trust depends on immature safety & audit layers [0.65, 0.45]
```

---

## Component Evolution Rationale

| Component | Stage | ε | ν | Evidence |
|---|---|---|---|---|
| Constitutional AI & Alignment Techniques | Custom Built | 0.38 | 0.62 | Only Anthropic deploying in June 2023; published Dec 2022; methodology still experimental, no competing vendors offering same approach. |
| RLHF (Reinforcement Learning from Human Feedback) | Custom Built | 0.42 | 0.60 | Industry standard being refined by OpenAI, Anthropic; multiple implementations but no consolidation; still domain-expert-led training process. |
| Red Teaming & Adversarial Testing | Custom Built | 0.35 | 0.60 | Emerging practice; Anthropic publishing red-team results; no commercial service yet; methodologies still being developed. |
| Model Interpretability Methods (SHAP, attention) | Custom Built | 0.40 | 0.54 | SHAP, attention visualization tools exist but no standard playbook; interpretability remains unsolved; research papers dominate over operational guidance. |
| Model Cards & Documentation | Product (+rental) | 0.48 | 0.54 | Becoming standard practice (Anthropic, Google Model Cards); early tools emerging; expectation rising that models include documented evaluation results. |
| Monitoring & Anomaly Detection | Product (+rental) | 0.50 | 0.58 | Mature ML monitoring tools exist (Datadog, New Relic); applied to AI models now; multiple vendors, but AI-specific extensions still developing. |
| Model Evaluation Benchmarks | Product (+rental) | 0.50 | 0.40 | MMLU, HumanEval maturing; new harder benchmarks (GPQA, SWE-bench, MMMU) introduced 2023; multiple benchmark providers (Artificial Analysis, HELM, Epoch); evaluation infrastructure consolidating. |
| Bias & Fairness Testing | Custom Built | 0.42 | 0.52 | Methodology emerging but contested; no standard metrics; tools exist (IBM Fairness 360) but no dominant vendor; domain expertise required for interpretation. |
| Robustness Testing | Custom Built | 0.38 | 0.52 | Adversarial examples well-studied but applied testing for production LLMs nascent; no standard test suite; high uncertainty in what robustness means for language models. |
| Large Language Models (LLMs) | Custom Built | 0.45 | 0.48 | Multiple vendors (OpenAI, Google, Anthropic, Meta) each with proprietary models; no standardisation; rapid iteration; each model trained differently. |
| Model Training Data | Custom Built | 0.48 | 0.40 | Data sourcing and curation still bespoke; no public datasets at frontier quality; dataset documentation emerging but inconsistent; high domain dependence. |
| Model Registry | Product (+rental) | 0.52 | 0.40 | MLflow, Hugging Face Model Hub, cloud provider registries maturing; model versioning becoming standard practice; governance frameworks emerging. |
| AI Governance Framework | Custom Built | 0.40 | 0.50 | EU AI Act proposed but not finalised in June 2023; organisations building custom governance; no industry consensus yet on risk assessment methodology. |
| Regulatory Compliance Framework (EU AI Act, etc.) | Custom Built | 0.38 | 0.50 | EU AI Act in negotiation (finalised Dec 2023); NIST framework emerging; no enforcement yet; standards work not yet complete. |
| Industry Standards (ISO 42001, IEEE) | Custom Built | 0.42 | 0.50 | ISO/IEC 42001 published Dec 2023 (post-June 2023 snapshot); IEEE standards in early draft; standardisation bodies ramping up; no harmonised standards adopted yet. |
| Third-Party AI Audits & Certification | Genesis | 0.32 | 0.52 | Market emerging in 2023 ($1B in 2023, projected $11.7B by 2033); ISACA AAIA cert launched 2025; very few auditors with AI expertise; bespoke consulting model dominates. |
| External Safety Assessment | Genesis | 0.35 | 0.48 | Red teaming labs appearing (OpenAI, Anthropic publish results); safety evaluations starting but no standard methodology; no independent certification body yet. |
| Incident Logging & Forensics | Product (+rental) | 0.50 | 0.48 | Incident logging tools mature (ELK, Datadog); applied to AI systems now; no AI-specific forensics standard; incident databases (OECD AI Incidents Monitor) emerging. |
| Data Quality & Curation | Custom Built | 0.45 | 0.38 | Methodology varies by domain; data cleaning tools exist but no universal standard; quality metrics contested; high bespoke investment per project. |
| Data Provenance Tracking | Product (+rental) | 0.40 | 0.36 | Tools emerging (DVC, Hugging Face Dataset Card); data documentation becoming expected; Git-like versioning for data maturing. |
| Synthetic Data Generation | Custom Built | 0.42 | 0.35 | Research active; commercial tools appearing; no dominant approach; quality assessment unclear; regulatory status uncertain. |
| MLOps & Model Deployment Pipeline | Product (+rental) | 0.55 | 0.42 | Tools maturing (Kubeflow, MLflow, cloud provider MLOps); containerisation standard; model serving infrastructure consolidating; DevOps patterns applied. |
| Training & Inference Compute | Product (+rental) | 0.78 | 0.35 | Cloud compute pricing by second; AWS, GCP, Azure dominate; custom silicon emerging (Google TPU, NVIDIA H100); utility model for compute well-established. |
| Cloud Infrastructure (AWS, GCP, Azure) | Commodity (+utility) | 0.92 | 0.16 | Three dominant providers; pricing transparent; switching costs moderate; compute is fungible; utility billing model mature. |
| Database & Storage | Commodity (+utility) | 0.88 | 0.16 | Standardised APIs (SQL, S3-compatible); many vendors; utility services mature; switching costs low; commodity market. |
| Container Orchestration (Kubernetes) | Commodity (+utility) | 0.82 | 0.16 | Kubernetes de facto standard; open source, widely understood; CNCF graduation achieved; multiple distributions; fully commoditised. |
| Monitoring & Logging Infrastructure | Commodity (+utility) | 0.85 | 0.16 | Observability stack mature (Prometheus, ELK, Datadog, New Relic); standardised metrics; utility model; commodity market. |
| ML Safety Research & Papers | Genesis | 0.25 | 0.58 | Active research area (alignment, interpretability papers published weekly); no consensus on solutions; community-driven discovery; early-stage knowledge. |
| AI Ethics Theory & Research | Custom Built | 0.28 | 0.50 | Ethics frameworks emerging (fairness, transparency, accountability); ISO/IEEE ethics standards in draft; domain experts still defining concepts. |
| Domain Expertise (application-specific) | Knowledge | 0.35 | 0.38 | Irreducible to standard form; embedded in human practitioners; varies by sector (medical, financial, legal); slow to commoditise. |
| Legal & Policy Knowledge | Knowledge | 0.32 | 0.48 | EU AI Act finalising; policy frameworks emerging; legal uncertainty high; specialist lawyers developing AI expertise; governance still forming. |

---

## Strategic Analysis

### a. Differentiation opportunities (top 3)

1. **Constitutional AI & Alignment Techniques** (Custom Built, ε = 0.38) — The only vendor offering this at scale is Anthropic. This is the defensible moat: techniques to align LLMs with human values before deployment. Highest differentiation leverage because competitors haven't caught up and the underlying research is proprietary.

2. **Red Teaming & Adversarial Testing** (Custom Built, ε = 0.35) — Finding failure modes before users do. Still bespoke and methodology-light; no commodified red-teaming service exists. Organizations can own this by building internal safety evaluation capacity now.

3. **Model Interpretability & Explainability** (Custom Built, ε = 0.40) — Users demand to understand *why* the AI made a decision. SHAP and attention visualization are tools, but assembling them into trustworthy explainability is still custom engineering. Early mover advantage in transparent-by-design models.

### b. Commodity-leverage candidates (top 3)

1. **Cloud Infrastructure** (Commodity +utility, ε = 0.92) — Rent compute, don't build data centres. AWS, GCP, Azure: fungible, priced-per-second, mature. Outsource ruthlessly.

2. **Container Orchestration & Monitoring Infrastructure** (Commodity +utility, ε ≈ 0.82–0.85) — Kubernetes, observability stacks: open-source, standardised, commodity. Use managed Kubernetes; don't reinvent.

3. **Training & Inference Compute** (Product +rental boundary, ε = 0.78) — GPU/TPU access: NVIDIA dominates but cloud providers offer utility access. Buy compute cycles, not hardware; manage as a service.

### c. Dependency risks (top 3)

1. **System Safety & Robustness → Constitutional AI & Alignment Techniques** — All three user anchors (Individual, Regulator, Enterprise) depend on safety. Safety depends on alignment techniques that only one vendor (Anthropic) has proven at scale. **Risk:** if Anthropic's approach doesn't generalise or scales slower than LLM capability growth, the entire trust pyramid becomes fragile.

2. **Regulatory Compliance → EU AI Act & Governance Frameworks** — Regulatory compliance (required by Regulator anchor) depends on a regulatory framework that is still being written and standardised. **Risk:** organisations moving fast on AI face moving-target compliance requirements; regulation lags deployment by years.

3. **Third-Party Audits → Incident Logging & Forensics** — Compliance and trust mechanisms depend on incident forensics that use immature tools and methods. **Risk:** auditors have no standard playbook yet for tracing AI failures to root cause; forensics is bespoke per incident.

### d. Build / Buy / Outsource recommendations

| Component | Stage | Recommendation | Rationale |
|---|---|---|---|
| Constitutional AI / Alignment Techniques | Custom Built | **Build or partner with Anthropic** | Cutting-edge moat. No competitive alternatives. Anthropic offers API access; alternatively, build in-house if you have AI safety talent. |
| Red Teaming & Adversarial Testing | Custom Built | **Build (in-house) early** | No commercial service yet. Hire safety engineers, run red-team workshops. First-mover organisations (OpenAI, Anthropic, Google) built internal teams; you should too. |
| Model Interpretability Methods | Custom Built | **Build custom interpretability layer** | Generic tools (SHAP) exist but applying them requires domain expertise. Invest in building interpretability into your pipeline now; it will become table-stakes. |
| Model Evaluation Benchmarks | Product (+rental) | **Use external benchmarks (MMLU, GPQA, etc.) + build custom evals** | Commodity benchmarks exist; augment with task-specific evaluations you own. E.g., Hugging Face leaderboards + internal domain tests. |
| AI Governance & Risk Assessment | Custom Built | **Build, with templates from NIST/ISO** | No off-the-shelf governance box works yet. Use NIST AI RMF as scaffold; build governance tailored to your risk profile and regulatory jurisdiction. |
| Third-Party Audits & Certification | Genesis | **Hire specialist auditors (build demand) or pilot audit-as-a-service vendors** | No standard audit process exists. Organisations like DAITS, SagoGuard emerging; alternatively, hire Big Four consultants with AI practices. |
| Monitoring & Anomaly Detection | Product (+rental) | **Rent (Datadog, Splunk, cloud provider native tools)** | Mature market; many vendors; no advantage in building. Use cloud-native monitoring and extend with AI-specific metrics. |
| LLMs (models themselves) | Custom Built / Product | **Use API (GPT, Claude, Gemini) OR open-source + fine-tune** | Frontier models (GPT-4, Claude 3): rent via API (OpenAI, Anthropic, Google). Open-source models (Llama, Mistral): fine-tune if you have differentiation in data/training. Don't train from scratch unless you're a scale-up with >$100M compute budget. |
| MLOps Pipeline | Product (+rental) | **Rent (cloud provider MLOps or open-source + managed)** | Tools mature. Use SageMaker, Vertex AI, or Kubeflow. Switching cost low; don't own the plumbing. |
| Cloud Compute & Infrastructure | Commodity +utility | **Rent (AWS, GCP, Azure)** | Utility. No advantage in owning. Pay per byte stored, per inference unit consumed. |

### e. Suggested gameplays

1. **#36 Directed investment on Constitutional AI / Red Teaming** — Allocate engineering talent to build in-house safety evaluation. This is the frontier; capital concentrated here pays off soonest.

2. **#43 Sensing Engines (ILC) on Model Evaluation** — Monitor which benchmarks and evaluation methodologies are emerging, which vendors are gaining traction. Evaluate emerging audit/certification providers; harvest the winners (e.g., Anthropic's techniques, OpenAI's red-teaming).

3. **#15 Open Approaches on Governance & Standards** — Participate in ISO/IEC, IEEE, NIST working groups now while standards are still forming. Contribute to shaping governance so your implementation path aligns with eventual regulations.

4. **#50 Reinforcing inertia on legacy AI systems** — Organisations with monolithic, opaque older models will struggle under coming regulations. Use this as an opportunity to displace legacy systems by offering auditable, documented, safety-tested alternatives.

5. **#55 Land grab on Interpretability / Explainability UI** — Be the first to offer a user-facing dashboard that explains AI decisions in terms regulators and customers understand. This becomes table-stakes; early movers own the UX.

### f. Doctrine violations (if any)

- ⚠️ **Doctrine #1 (Focus on user needs)** — The map correctly anchors on three users (Individual, Regulator, Enterprise) but most organisations building AI focus only on Enterprise/Business. Missing the Individual User perspective (does the person trust this system?) and Regulator perspective (can we audit & defend it?) until too late.

- ⚠️ **Doctrine #10 (Know your users)** — Three anchors is rare; most AI strategies have only one (the customer paying for the system). Regulatory requirements and individual user trust are co-equal needs in the AI trust landscape; treating them as secondary is organisational self-sabotage.

- ⚠️ **Doctrine #13 (Manage inertia)** — Third-Party Audits is nascent; inertia forms that block adoption: sunk capital in in-house "AI ethics committees" (form #3 political capital), retraining auditors (form #8), and uncertainty about what audits even measure (form #11 suitability doubt). Organisations will resist external audits until forced by regulation.

### g. Climatic context

**#3 Everything evolves.** Constitutional AI (Custom Built) is *trending toward Product (+rental)* as more vendors and open-source alternatives emerge. By 2025–2026, expect commoditised alignment frameworks.

**#5 No choice over evolution.** Organisations cannot opt out of safety/trust evaluation. This will be table-stakes; inertia will kill those that delay.

**#15–17 Past success breeds inertia.** Incumbent AI labs (Google Brain, OpenAI's first models) were built with little transparency. This inertia makes it hard for them to add auditing, interpretability, governance *after the fact*. New entrants (e.g., frontier safety-first teams) will win by building trust *before* deployment.

**#18 You cannot measure evolution over time.** The claim "we'll commoditise safety testing by 2025" is a scenario, not a forecast. Safety testing could stay Custom Built for years if the problem remains hard.

**#27 Product-to-utility punctuated equilibrium.** When governance regulation forces standardisation (EU AI Act goes into force, NIST standards adopt ISO 42001), organisations will see a compressed window to transition from custom governance to standardised compliance. Those caught without process will face fines and reputational collapse.

### h. Deep-placement notes

- **Constitutional AI** — Initial cheat-sheet: Stage II (emerging technique, Anthropic only). Research: <cite index="1-4:5">Anthropic's Constitutional AI uses self-supervision and adversarial training to align AI systems with human values</cite>. June 2023 status: technique 6 months into publication, zero competing vendors offering equivalent. Confirmed: **Stage II (Custom Built), ε = 0.38**.

- **Model Evaluation Benchmarks** — Initial cheat-sheet: Stage III (MMLU, HumanEval mature). Research: <cite index="15-1">In 2023, AI researchers introduced several challenging new benchmarks, including MMMU, GPQA, and SWE-bench, aimed at testing the limits of increasingly capable AI systems.</cite> June 2023 status: Old benchmarks saturating, new benchmarks emerging, multiple vendors. Benchmark infrastructure transitioning. Revised: **Stage II–III (Custom→Product), ε = 0.50** (positioned between old commodity benchmarks and new custom ones).

- **EU AI Act & Regulatory Framework** — Initial cheat-sheet: Stage II (framework proposed, not finalised). Research: <cite index="25-14:15">On 6 December 2022, the European Council adopted the general orientation. On 9 December 2023, the EU Council and Parliament concluded the AI Act.</cite> June 2023 status: Post-orientation but pre-conclusion, still in legislative motion. Standards drafting begins but no implementation yet. Confirmed: **Stage II (Custom Built), ε = 0.38**.

- **Third-Party AI Audits** — Initial cheat-sheet: Genesis (nascent, no vendors). Research: <cite index="31-1">The global market for AI in auditing is projected to surge from USD 1.0 billion in 2023 to USD 11.7 billion by 2033</cite>. June 2023 status: Consulting-driven ($1B market); no standard audit process; no dominant vendor. Confirmed: **Stage II (Custom Built), ε = 0.32** — transitioning from Genesis but still bespoke.

### i. Caveat

**Evolution is a scenario, not a forecast.** Wardley's climatic pattern #18 states: *"You cannot measure evolution over time or adoption."* The placements above reflect June 2023 conditions. Actual trajectories depend on:

- **Regulatory speed:** Will the EU AI Act enforce quickly, or will watering-down delay it? (Affects Governance Framework speed).
- **Capability vs. safety race:** Will LLM capability outpace safety techniques? (Affects Constitutional AI pressure).
- **Open-source acceleration:** Will open-source models commoditise faster than proprietary ones? (Affects LLM stage).
- **Incident impact:** Will a catastrophic AI incident force rapid standardisation? (Affects audit/certification stage).

The map is a snapshot. Review quarterly as competitive and regulatory pressure shifts components rightward on the evolution axis.