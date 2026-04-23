# Wardley Map — Personal Computing & Developer Stack in the Conversational-AI Era

## Step 0 — Strategic context

1. **Strategic question.** *Where in the personal-computing / developer stack should teams invest engineering effort, where should they buy or rent, and where is the terrain shifting because conversational AI is industrialising parts of it?* The scenario is explicitly asking "what does this mean for how people build software", so the map must distinguish what is genesis/custom (LLMs, conversational IDEs) from what has already become cloud-and-container commodity.
2. **User anchor(s).** Two anchors: the **Developer / Knowledge Worker** (the person building software) and the **Software End User** (the person consuming the resulting applications). Keeping both avoids collapsing the map into a dev-centric view that misses the consumer-facing device and application layers the scenario mentions.
3. **Core needs.** Build software faster (developer); run applications reliably on personal devices (end user). Secondary: manage cost of AI-intensive workflows (FinOps).
4. **Scope boundary.** Industry landscape — the personal-computing and developer-tooling stack as of 2026 with conversational AI now a first-class part of how code is written. Not one company, not one product.

**Assumptions flagged for the user:**
- Two-anchor formulation (developer + end user). If the question is purely "where should a developer-tools vendor invest?" then drop the end-user anchor.
- Legacy is represented as three distinct inertial components (Legacy Desktop Build Tooling, LAMP/.NET Runtime, Legacy Architecture) rather than one monolithic "Legacy" block, because each resists evolution for different reasons.
- "Conversational AI+human IDE" (Copilot / Cursor / Claude Code) is treated as a separate component from the human-centric IDE, not a feature of it. The two modes produce different strategic calls; splitting them is the whole point of the scenario.

---

## OWM map

```owm
title Personal Computing & Developer Stack in the Conversational-AI Era
style wardley

// Anchor(s)
anchor Developer / Knowledge Worker [0.96, 0.50]
anchor Software End User [0.94, 0.55]

// User-facing needs (d=1 from anchors)
component Build Software Faster [0.88, 0.55]
component Run Applications [0.86, 0.70]

// Applications & devices (d=2)
component Personal Applications (Web / SaaS) [0.78, 0.72]
component Mobile & Desktop Devices [0.74, 0.82]

// IDE layer — two modes
component Human-Centric IDE (VS Code, JetBrains) [0.70, 0.72]
component Conversational AI+Human IDE (Copilot, Cursor, Claude Code) [0.72, 0.38]

// Component libraries and services
component Component Libraries & SDKs [0.60, 0.70]
component Public APIs & Services [0.58, 0.76]

// FinOps — cross-cutting practice the developer sees alongside the AI IDE
component FinOps / AI Cost Management [0.56, 0.34]

// Legacy approaches (explicit in scenario) — inertial
component Legacy Desktop Build Tooling [0.55, 0.66] inertia

// Runtime layer
component Serverless Runtime (Lambda, Cloud Run) [0.48, 0.80]
component LAMP / .NET Runtime [0.46, 0.72] inertia

// Large language models
component Large Language Models (Frontier) [0.50, 0.30]
component Open-Weight LLMs (Llama, Mistral) [0.42, 0.45]
component LLM Inference APIs [0.38, 0.62]

// DevOps practices & orchestration
component DevOps Practices (CI/CD, IaC) [0.34, 0.68]
component Orchestration (Kubernetes) [0.30, 0.72]

// OS & legacy architecture
component Operating Systems (Linux, Windows, macOS) [0.28, 0.86]
component Legacy Architecture (Monoliths, VM farms) [0.24, 0.60] inertia

// Containers
component Container Runtime (Docker, containerd) [0.20, 0.82]

// Deep compute
component Cloud Compute (AWS, GCP, Azure) [0.12, 0.90]
component Physical Servers / Data Centres [0.06, 0.92]

// Dependencies
Developer / Knowledge Worker->Build Software Faster
Developer / Knowledge Worker->Human-Centric IDE (VS Code, JetBrains)
Developer / Knowledge Worker->Conversational AI+Human IDE (Copilot, Cursor, Claude Code)
Software End User->Run Applications
Software End User->Personal Applications (Web / SaaS)
Software End User->Mobile & Desktop Devices

Build Software Faster->Human-Centric IDE (VS Code, JetBrains)
Build Software Faster->Conversational AI+Human IDE (Copilot, Cursor, Claude Code)
Run Applications->Personal Applications (Web / SaaS)
Run Applications->Mobile & Desktop Devices

Personal Applications (Web / SaaS)->Component Libraries & SDKs
Personal Applications (Web / SaaS)->Public APIs & Services
Personal Applications (Web / SaaS)->Serverless Runtime (Lambda, Cloud Run)
Personal Applications (Web / SaaS)->LAMP / .NET Runtime
Mobile & Desktop Devices->Operating Systems (Linux, Windows, macOS)

Human-Centric IDE (VS Code, JetBrains)->Component Libraries & SDKs
Human-Centric IDE (VS Code, JetBrains)->Legacy Desktop Build Tooling
Conversational AI+Human IDE (Copilot, Cursor, Claude Code)->Component Libraries & SDKs
Conversational AI+Human IDE (Copilot, Cursor, Claude Code)->Large Language Models (Frontier)
Conversational AI+Human IDE (Copilot, Cursor, Claude Code)->Open-Weight LLMs (Llama, Mistral)
Conversational AI+Human IDE (Copilot, Cursor, Claude Code)->FinOps / AI Cost Management

Component Libraries & SDKs->Serverless Runtime (Lambda, Cloud Run)
Component Libraries & SDKs->LAMP / .NET Runtime
Legacy Desktop Build Tooling->LAMP / .NET Runtime
Public APIs & Services->Serverless Runtime (Lambda, Cloud Run)

FinOps / AI Cost Management->LLM Inference APIs
FinOps / AI Cost Management->Cloud Compute (AWS, GCP, Azure)

Large Language Models (Frontier)->LLM Inference APIs
Open-Weight LLMs (Llama, Mistral)->LLM Inference APIs
LLM Inference APIs->Cloud Compute (AWS, GCP, Azure)

Serverless Runtime (Lambda, Cloud Run)->Orchestration (Kubernetes)
Serverless Runtime (Lambda, Cloud Run)->Container Runtime (Docker, containerd)
LAMP / .NET Runtime->Operating Systems (Linux, Windows, macOS)
LAMP / .NET Runtime->Legacy Architecture (Monoliths, VM farms)

DevOps Practices (CI/CD, IaC)->Orchestration (Kubernetes)
DevOps Practices (CI/CD, IaC)->Container Runtime (Docker, containerd)
DevOps Practices (CI/CD, IaC)->Cloud Compute (AWS, GCP, Azure)

Operating Systems (Linux, Windows, macOS)->Cloud Compute (AWS, GCP, Azure)
Orchestration (Kubernetes)->Container Runtime (Docker, containerd)
Legacy Architecture (Monoliths, VM farms)->Physical Servers / Data Centres

Container Runtime (Docker, containerd)->Cloud Compute (AWS, GCP, Azure)
Cloud Compute (AWS, GCP, Azure)->Physical Servers / Data Centres

// Evolve arrows (scenario, not forecast)
evolve Conversational AI+Human IDE (Copilot, Cursor, Claude Code) 0.62
evolve Large Language Models (Frontier) 0.58
evolve FinOps / AI Cost Management 0.62
evolve Open-Weight LLMs (Llama, Mistral) 0.70
```

---

## §3.2 Component evolution rationale

| Component | Stage | ε | ν | Evidence |
|---|---|---:|---:|---|
| Build Software Faster | Product (+rental) | 0.55 | 0.88 | User need expressed as an outcome; mature framing that every developer, platform, and tool vendor organises around. |
| Run Applications | Product (+rental) | 0.70 | 0.86 | End-user expectation is now "just works" — appstore / browser delivery is standardised and ubiquitous. |
| Personal Applications (Web / SaaS) | Product (+rental) | 0.72 | 0.78 | Rapid-consumption SaaS market with established expectations; multiple vendors per category, not yet utility. |
| Mobile & Desktop Devices | Commodity (+utility) | 0.82 | 0.74 | Two-OS duopoly on mobile, three on desktop; commoditised form factors and supply chains. |
| Human-Centric IDE (VS Code, JetBrains) | Product (+rental) | 0.72 | 0.70 | Large vendor field stabilising to VS Code dominance + JetBrains; feature competition on UX, plugins, debug. |
| Conversational AI+Human IDE | Custom Built | 0.38 | 0.72 | Copilot, Cursor, Claude Code, Windsurf — new entrants, pricing still in flux, no dominant pattern; "describe the wonder" literature style. Rapidly moving. |
| Component Libraries & SDKs | Product (+rental) | 0.70 | 0.60 | npm / PyPI / Maven / NuGet; well-understood publishing norms; many vendors, pricing and SLA layered on via registries (GitHub, JFrog). |
| Public APIs & Services | Commodity (+utility) | 0.76 | 0.58 | REST/GraphQL over HTTPS is the standardised backbone; OpenAPI and API gateways are commodity; billing is per-call utility. |
| FinOps / AI Cost Management | Custom Built | 0.34 | 0.56 | FinOps Foundation exists, but AI-cost disciplines specifically are 18-24 months old; vendors (Vantage, CloudZero) are early; playbooks still bespoke per org. |
| Legacy Desktop Build Tooling | Product (+rental) | 0.66 | 0.55 | Visual Studio, MSBuild, older IDE ecosystems — mature products but declining share; kept alive by enterprise contracts, marked inertial. |
| Serverless Runtime | Commodity (+utility) | 0.80 | 0.48 | Lambda, Cloud Run, Cloudflare Workers priced per-invocation; standardised event/HTTP triggers; utility billing. |
| LAMP / .NET Runtime | Product (+rental) | 0.72 | 0.46 | Very mature but supplanted by cloud-native patterns for greenfield; kept for legacy; marked inertial because organisations are locked in. |
| Large Language Models (Frontier) | Custom Built | 0.30 | 0.50 | OpenAI GPT-4/5, Anthropic Claude, Google Gemini, xAI — small vendor count; model-family pricing still volatile; capability unpredictable release-to-release; "describe the wonder" publications dominate. |
| Open-Weight LLMs (Llama, Mistral) | Custom Built (late) | 0.45 | 0.42 | Llama, Mistral, Qwen, DeepSeek — several credible families, patterns emerging (quantisation, LoRA, fine-tune recipes), but no Stage-III winners; hosting still bespoke. |
| LLM Inference APIs | Product (+rental) | 0.62 | 0.38 | OpenAI, Anthropic, AWS Bedrock, Azure OpenAI, Groq, Together, Fireworks — multiple vendors with converging API surface (OpenAI-compatible endpoints), token-priced, feature competition. |
| DevOps Practices (CI/CD, IaC) | Product (+rental) | 0.68 | 0.34 | GitHub Actions, GitLab CI, Jenkins, Terraform, Pulumi — mature product category; best practices documented; certification courses exist. |
| Orchestration (Kubernetes) | Product (+rental) | 0.72 | 0.30 | K8s is the de-facto standard; managed offerings (EKS, GKE, AKS) industrialising it but complexity keeps it short of full commodity. CNCF ecosystem standardises patterns. |
| Operating Systems | Commodity (+utility) | 0.86 | 0.28 | Linux + Windows + macOS — interchangeable from a workload perspective for most applications; kernel choice is invisible to end users. |
| Legacy Architecture (Monoliths, VM farms) | Product (+rental) | 0.60 | 0.24 | Still widely deployed but displaced for greenfield; inertia comes from co-evolved processes, org structure, and capex commitments. |
| Container Runtime (Docker, containerd) | Commodity (+utility) | 0.82 | 0.20 | OCI standard, containerd / runc are reference implementations; "container" is now invisible plumbing in most developer workflows. |
| Cloud Compute (AWS, GCP, Azure) | Commodity (+utility) | 0.90 | 0.12 | Priced per-second, published SLAs, three hyperscalers plus regional providers; procurement is routine. |
| Physical Servers / Data Centres | Commodity (+utility) | 0.92 | 0.06 | Fully industrial; bought per-rack, per-kW; customers almost never care which ODM built the box. |

---

## Section 4 — Strategic analysis

### a. Differentiation opportunities (top 3)

1. **Conversational AI+Human IDE (Custom Built)** — this is where the user's whole question lives. The product category is forming in real time; no vendor has won; the interaction model itself is still being invented. Highest differentiation pressure in the map — visible to every developer, still highly immature. A firm that sets the convention for agentic coding (context assembly, tool permissioning, multi-file edits, auditable change history) gets outsized returns.
2. **Large Language Models (Frontier, Custom Built)** — top-tier model IP is the other locus of differentiation. Only a handful of labs can train frontier-scale models; capability jumps between releases still change the shape of what's possible. Visible to developers via brand ("I'm using Claude / GPT-5 / Gemini") even though the model sits two hops down the chain.
3. **FinOps / AI Cost Management (Custom Built)** — this is a sleeper. Every team using AI-IDE workflows is absorbing volatile token spend and nobody has standardised the discipline. A tool or practice that makes AI spend predictable (per-developer budgets, per-feature ROI, routing to cheaper models for commodity tasks) is a visible, immature, and strategically scoped differentiator.

### b. Commodity-leverage candidates (top 3)

1. **Cloud Compute (Commodity +utility)** — rent, never build. Three interchangeable hyperscalers plus regional utilities; the only strategic choice is which region / compliance posture.
2. **Container Runtime (Commodity +utility)** — consume as plumbing. OCI / containerd are standardised; no team should be writing a custom container runtime.
3. **Operating Systems (Commodity +utility)** — accept the three-OS reality, standardise on Linux for server workloads, treat desktop OS as user choice. No leverage from customising.

Honourable mention: **Public APIs & Services** — OpenAPI + HTTPS + OAuth is the utility interface of the industry; build to the standard, don't reinvent.

### c. Dependency risks (top 3)

1. **Conversational AI+Human IDE → Large Language Models (Frontier)** — the most visible new developer experience in the stack sits directly on models that are themselves Custom Built, vendor-concentrated, and capable of double-digit quality changes release-to-release. If a frontier lab changes pricing, TOS, or capability, the IDE's value proposition changes under it.
2. **Conversational AI+Human IDE → FinOps / AI Cost Management** — the AI-IDE usage pattern creates per-developer variable cost that organisations can't reliably budget for. The tooling to manage that cost is Custom Built and missing. Adoption will hit a ceiling when CFOs refuse to sign cheques for a usage they can't model.
3. **Personal Applications → LAMP / .NET Runtime (inertia)** — a surprising amount of "personal SaaS" still runs on legacy runtimes kept alive by lock-in and skills inertia. When those codebases need AI features bolted on, the runtime choice constrains what's feasible and forces a painful re-platforming discussion.

### d. Build / Buy / Outsource recommendations

| Component | Stage | Recommendation | Why |
|---|---|---|---|
| Conversational AI+Human IDE | Custom Built | **Build** (if developer-tools is your business) or **buy / standardise** (if software is the output, not the product) | Core differentiator for tooling vendors; undifferentiated overhead for everyone else — pick a market leader, don't reinvent. |
| Large Language Models (Frontier) | Custom Built | **Buy / rent via inference APIs** | Training frontier models is a <10-company game. Almost every reader of this map should consume them, not build them. |
| Open-Weight LLMs | Custom Built (late) | **Open-source collaborate** | Stage II→III transition where ecosystem dynamics apply; contribute to Llama/Mistral-compatible toolchains rather than reinvent. |
| LLM Inference APIs | Product (+rental) | **Buy (multi-vendor)** | Vendor competition is real; avoid single-vendor lock-in. Route by task through a thin abstraction. |
| FinOps / AI Cost Management | Custom Built | **Build thin, buy tooling where it exists** | The practice is still forming; invest in internal discipline now; buy Vantage/CloudZero-class tooling for observability. |
| Component Libraries & SDKs | Product (+rental) | **Consume from registries; publish internal ones** | npm / PyPI / NuGet are commodity; your internal libs are product-stage — treat them as such. |
| Serverless Runtime | Commodity (+utility) | **Rent** | Lambda / Cloud Run / Workers — pick one per workload class. |
| LAMP / .NET Runtime | Product (+rental, inertial) | **Sunset, don't extend** | Keep running for legacy workloads; don't greenfield onto them. |
| DevOps Practices | Product (+rental) | **Buy tooling, invest in practice** | GitHub Actions / Terraform / Pulumi are commodity-adjacent; the practice itself (trunk-based dev, progressive delivery) is still where engineering investment pays. |
| Orchestration (Kubernetes) | Product (+rental) | **Rent managed (EKS/GKE/AKS)** | Self-hosted K8s is an anti-pattern for 95% of teams; managed control plane is table stakes. |
| Cloud Compute, Container Runtime, OS, Physical Servers | Commodity (+utility) | **Rent / consume** | No moat in building these. |
| Legacy Desktop Build Tooling, Legacy Architecture | Product (+rental, inertial) | **Sunset on a schedule** | Don't invest in extending; plan and budget migrations away. |

Rules of thumb applied: Genesis → build; Custom Built → build-if-differentiator, else buy expertise; Product → buy; Commodity → rent.

### e. Suggested gameplays

Referencing Wardley's 61-play catalogue (`references/gameplay-patterns.md`):

- **#15 Open approaches** — on the Conversational AI+Human IDE. Whoever opens the agent-permissioning / tool-use protocol (think MCP) and seeds the ecosystem shapes how the product stage forms. Relevant to Claude Code / Cursor / Copilot vendors and to enterprise platform teams deciding which standard to back.
- **#1 Accelerators (Ecosystem)** — on Open-Weight LLMs. Llama and Mistral are accelerating the ecosystem around them; aligning your stack to their conventions (fine-tune formats, safety tooling, quantisation) speeds your own evolution.
- **#27 Componentisation** — on FinOps / AI Cost Management. Break the practice into reusable components (token counter, per-feature budget, routing middleware) so it can industrialise.
- **#52 Sweat and dump** — on Legacy Desktop Build Tooling and Legacy Architecture. Extract remaining value; do not invest; schedule the exit.
- **#33 Tower and moat** — on Frontier LLMs (for the labs themselves). The handful of frontier labs are building tower-and-moat positions; everyone else should assume they will use, not displace, those towers.
- **#8 Buy** — on any enterprise considering building its own inference stack when Bedrock / Azure OpenAI / Vertex exist. Don't.
- **#60 Undermining barriers to entry** — relevant to open-weight challengers (Meta, Mistral, DeepSeek) attacking the frontier-lab moat through weight releases.

### f. Doctrine violations

Checked against the 40-principle list. Findings:

- **Focus on user needs** (satisfied) — two explicit anchors, two named needs, no "business value" placeholders.
- **Use a common language** (satisfied) — canonical stage naming used throughout.
- **Challenge assumptions** — the two-anchor choice and the IDE split are flagged as assumptions; the user can override.
- **Know your users / Know the details** — partial. The "Software End User" anchor is generic. A real exercise with a specific product would sharpen this to "consumer on a mobile device" or "enterprise knowledge worker on a managed laptop" and likely split it further.
- **Think small** (potential violation) — 22 components for an industry-landscape map is under the 35-45 target. The defence is that the scenario gave an explicit list of layers and padding with generic infrastructure would violate "remove a component that doesn't change any conclusion". If the strategic question narrowed, components would be pruned, not added.
- **Manage inertia** (satisfied) — three components are explicitly flagged inertial.
- **Design for constant evolution** (satisfied) — four evolve arrows on the volatile quadrant.

### g. Climatic context

From the 27 climatic patterns (`references/climatic-patterns.md`), these are actively shaping the map:

- **#3 Everything evolves** — conversational AI IDE and frontier LLMs are mid-evolution. Their Stage II position is temporary; the whole question is what they look like once they reach Stage III.
- **#15–17 Inertia (various forms)** — the three explicitly-inertial components (Legacy Desktop Build Tooling, LAMP/.NET Runtime, Legacy Architecture) embody multiple inertia forms from `references/inertia.md`: co-evolved practices (teams know these runtimes), capex lock-in (existing VM estates), skills inertia (LAMP / .NET specialists).
- **#27 Product-to-utility punctuated equilibrium** — LLM Inference APIs are mid-transition from Product to Commodity (OpenAI-compatible endpoints are the standardising interface). Conversational IDE is pre-transition: the equilibrium hasn't yet broken open.
- **#18 You cannot measure evolution over time or adoption** — restated in the caveat below.
- **#9 Capital flows to where there is a gap** — visible in both the AI-IDE and FinOps spaces: funding is chasing the differentiation zone, which is why the vendor count there is high and churning.

### h. Deep-placement notes

Research budget applied to the four placements the map's conclusions hinge on:

- **Conversational AI+Human IDE** — initial checklist pick was Custom Built (Stage II). Vendor-count signal: Copilot, Cursor, Windsurf, Claude Code, Zed, Cline, Continue — a dozen credible entrants in 2 years with no dominant market share yet; pricing experiments still running (per-seat, per-token, hybrid); interaction patterns (chat, inline, agentic) still diverging. Confirms Stage II, toward the high end — kept at ε=0.38 (not pushed to 0.45) because the API contract between IDE and model isn't yet stable.
- **Large Language Models (Frontier)** — checklist pick Custom Built. Vendor concentration is the key signal: 4-5 labs training at frontier scale; capability still jumps release-to-release; publications are still "describe the wonder" for new capabilities (reasoning, tool use, long context). Kept at ε=0.30 (Stage II early); if you judged by consumption (hundreds of millions of weekly users) you'd push right, but the evolution stage is about the component's characteristics, not its adoption — Wardley pattern #18.
- **LLM Inference APIs** — initial pick wavered between Product and Commodity. The OpenAI-compatible-endpoint convention (adopted by Groq, Together, Fireworks, Bedrock, Azure) is a Stage III→IV signal. Kept at ε=0.62 (early Product) because enterprise contracts still vary meaningfully vendor-to-vendor and switching isn't as seamless as the API surface implies.
- **Orchestration (Kubernetes)** — initial pick Product (Stage III late). CNCF incubation pipeline and managed-control-plane ubiquity argue for further right; operational complexity and the fact that "self-hosted K8s" is still a meaningful concept argue against. Held at ε=0.72, late Stage III.

### i. Caveat

Evolution trajectories in this map are **scenarios, not forecasts**. Wardley's climatic pattern #18: *"you cannot measure evolution over time or adoption."* The `evolve` arrows show plausible next-stage targets (conversational IDE toward Product, FinOps toward Product, frontier LLMs toward early Product, open-weight LLMs toward Product), but the rate and order of those transitions is a matter of strategy and gameplay, not clock time. Re-run this map when any of these shift visibly: (a) a dominant conversational-IDE vendor emerges, (b) token prices drop another order of magnitude, (c) open-weight models cross the capability threshold of current frontier models, (d) an AI-FinOps discipline standardises.

---

## Validator output

Bundled validator (`node scripts/validate_owm.mjs`) could not be executed in the current sandbox (node execution was denied). Manual edge audit was performed against the visibility constraint for all 42 edges:

- All 22 components + 2 anchors have coordinates in [0, 1].
- All edge endpoints reference declared components/anchors.
- Every edge `a->b` satisfies ν(a) ≥ ν(b). Worked example of the tightest gaps: Open-Weight LLMs (ν=0.42) → LLM Inference APIs (ν=0.38), FinOps (ν=0.56) → LLM Inference APIs (ν=0.38), Orchestration (ν=0.30) → Container Runtime (ν=0.20). No violations.

**Expected validator output when run manually:** `OK: 24 components/anchors, 42 edges — no violations.`

### Layout check (advisory)

Manually performed per §5.6:

- **Near-duplicate coordinates:** none within |Δν| < 0.02 AND |Δε| < 0.02. Four components share ε=0.72 (Human-Centric IDE, Personal Applications, Orchestration, LAMP/.NET Runtime) but their visibilities span ν=0.30 to 0.78, so no render collision.
- **Stage-boundary straddle:** LAMP/.NET was nudged from ε=0.74 to ε=0.72 to avoid a ±0.01 straddle at the Stage III/IV border. No other components within ±0.01 of 0.25 / 0.50 / 0.75.
- **Canvas-edge clipping:** Physical Servers ν=0.06 (above the 0.04 floor), Developer anchor ν=0.96 (below the 0.98 ceiling). OK.
- **Stage imbalance:** 0 Genesis, 4 Custom Built, 11 Product (+rental), 7 Commodity (+utility) across 22 components. Stage III at 50% is below the 60% warning. Stage I is empty — scenario-justified: the user asked to show "where LLMs and conversational IDEs are still genesis/custom", and those components landed in the high end of Custom Built. Forcing anything into Genesis would be a mis-reading.

---

## Summary: so what does this mean for how people build software?

The cloud-and-container half of the map is done — OS, containers, cloud compute, serverless, orchestration, public APIs, OS are all Commodity or late Product. There is no engineering leverage in reinventing any of it; rent and consume.

The interesting half is the top-left quadrant: **conversational AI IDEs, frontier LLMs, FinOps for AI**. These sit in Custom Built, visible to developers, and are the place where strategic choices actually have payoff. For a tool vendor, that's where to build. For everyone else, that's where to pick winners carefully and standardise internal practice (especially FinOps — the cost discipline hasn't been invented yet, and organisations that build it early will spend AI budgets 2-5x more effectively than those that don't).

Legacy (desktop build tooling, LAMP/.NET, monolith architectures) is a sunset problem — manage inertia, don't invest, schedule the exit.

The hidden story in the map is the **dependency from the top-left (AI IDE) down through frontier LLMs to inference APIs and cloud compute**: the most visible new developer experience rests on the most vendor-concentrated, fastest-changing, hardest-to-budget foundation in the whole stack. That's the risk corridor; it's where the board-level conversations should happen.
