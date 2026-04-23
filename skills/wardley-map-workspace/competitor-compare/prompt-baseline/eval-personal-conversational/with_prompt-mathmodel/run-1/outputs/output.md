# Personal Computing in the Conversational AI Era

Scenario: map the personal-computing technology landscape now that conversational AI is reshaping the developer stack — anchored on the user/developer need, coming down through applications and devices, the IDE (in two modes), component libraries and services, legacy approaches, runtimes (Serverless, LAMP/.NET), large language models and FinOps, operating systems and orchestration, containers, DevOps and legacy architecture, and compute (servers and cloud).

## 1. Mathematical model

Map tuple: `M = (V, E, U, ν, ε, t)`.

- `U` = anchor set = `{Developer, Build Working Software}` — the developer is the user; the need is delivering working software.
- `V` = 22 components across 7 layers (applications/devices, two IDE modes, libraries/services/legacy, runtimes + LLMs + FinOps, OS/orchestration/containers, DevOps + legacy architecture, compute).
- `E` = directed dependencies `(a, b)` meaning "a depends on b".
- `ν` = visibility, seeded from graph distance then adjusted for value-chain judgment. Hard rule enforced: `ν(a) ≥ ν(b)` for every edge.
- `ε` = evolution, scored via the quick 4-row cheat sheet (Ubiquity / Certainty / User Perception / Publication Types) and mapped to band midpoints `{0.125, 0.375, 0.625, 0.875}`.

## 2. Evolution scoring (quick 4-row cheat sheet)

Representative scorings behind the placements below.

| Component | Ubiquity | Certainty | User Perception | Publications | Mean ε | Stage |
|---|---|---|---|---|---|---|
| Cloud Compute | IV | IV | IV | IV | 0.875 | Commodity +utility |
| Operating Systems | IV | IV | IV | IV | 0.875 | Commodity +utility |
| Containers | IV | IV | IV | IV | 0.875 | Commodity +utility (~0.85) |
| LAMP / .NET Runtime | IV | IV | IV | IV | 0.875 | Commodity +utility |
| Personal Devices | IV | IV | IV | IV | 0.875 | Commodity +utility |
| Orchestration (K8s) | III | IV | III | IV | 0.75 | Product → Commodity |
| Serverless Runtime | III | III | III | III | 0.625 | Product (+rental) |
| Managed Services (APIs) | III | III | III | IV | 0.69 | Product → Commodity |
| Component Libraries | III | III | III | III | 0.625 | Product (+rental) |
| DevOps Practice | III | III | III | III | 0.625 | Product (+rental) (Practice) |
| Applications | IV | III | IV | III | 0.75 | Product → Commodity |
| IDE (Human-centric) | III | III | III | III | 0.625 | Product (+rental) |
| IDE (Conversational AI+Human) | I | II | I | I | 0.19 | Genesis → Custom |
| Conversational AI Assistant | II | II | I | I | 0.25 | Genesis → Custom |
| Large Language Models | II | II | II | I | 0.31 | Custom Built (transitioning) |
| FinOps (LLM cost governance) | I | II | I | I | 0.19 | Genesis |
| Legacy Coding Approaches | II | IV | II | III | 0.50 | stuck between Custom and Product; inertia |
| Legacy Architecture | I | IV | I | III | 0.38 | inertia, not evolving |

Rows disagree for **LLMs** (highly discussed, infrastructure-like vendors exist, but underlying behaviour still poorly understood and rapidly changing) — flagged "in transition" with range ε ≈ [0.22, 0.40]; the plot uses 0.28.

## 3. OWM map

```owm
title Personal Computing in the Conversational AI Era
style wardley

// Anchor — the user and their need
anchor Developer [0.98, 0.55]
anchor Build Working Software [0.94, 0.50]

// Layer 1 — applications and devices directly used
component Applications [0.86, 0.80]
component Personal Devices [0.84, 0.88]

// Layer 2 — development surface (IDE in two modes)
component IDE (Human-centric) [0.76, 0.70]
component IDE (Conversational AI+Human) [0.78, 0.18]
component Conversational AI Assistant [0.74, 0.22]

// Layer 3 — building blocks consumed by the IDE
component Component Libraries [0.64, 0.72]
component Managed Services (APIs) [0.62, 0.78]
component Legacy Coding Approaches [0.60, 0.30] inertia

// Layer 4 — runtimes and intelligence plane
component Serverless Runtime [0.52, 0.72]
component LAMP / .NET Runtime [0.50, 0.88]
component Large Language Models [0.54, 0.28]
component FinOps (LLM cost governance) [0.48, 0.20]

// Layer 5 — platform / orchestration
component Operating Systems [0.40, 0.90]
component Orchestration (Kubernetes) [0.38, 0.78]
component Containers [0.34, 0.85]

// Layer 6 — delivery practice and legacy architecture
component DevOps Practice [0.30, 0.70]
component Legacy Architecture [0.28, 0.35] inertia

// Layer 7 — compute substrate
component Servers [0.16, 0.82]
component Cloud Compute [0.12, 0.92]

// Dependencies (A -> B means A depends on B)
Developer->Build Working Software
Build Working Software->Applications
Build Working Software->Personal Devices
Build Working Software->IDE (Human-centric)
Build Working Software->IDE (Conversational AI+Human)

Applications->Component Libraries
Applications->Managed Services (APIs)
Applications->Serverless Runtime
Applications->LAMP / .NET Runtime

IDE (Human-centric)->Component Libraries
IDE (Human-centric)->Legacy Coding Approaches
IDE (Human-centric)->DevOps Practice

IDE (Conversational AI+Human)->Conversational AI Assistant
IDE (Conversational AI+Human)->Component Libraries
IDE (Conversational AI+Human)->Managed Services (APIs)
IDE (Conversational AI+Human)->DevOps Practice

Conversational AI Assistant->Large Language Models
Conversational AI Assistant->FinOps (LLM cost governance)

Managed Services (APIs)->Serverless Runtime
Managed Services (APIs)->Orchestration (Kubernetes)

Serverless Runtime->Containers
Serverless Runtime->Operating Systems
LAMP / .NET Runtime->Operating Systems
LAMP / .NET Runtime->Servers

Large Language Models->Cloud Compute
FinOps (LLM cost governance)->Cloud Compute

Orchestration (Kubernetes)->Containers
Containers->Operating Systems
Operating Systems->Servers
Operating Systems->Cloud Compute

DevOps Practice->Orchestration (Kubernetes)
DevOps Practice->Containers
Legacy Architecture->Servers
Legacy Coding Approaches->LAMP / .NET Runtime

Personal Devices->Operating Systems
Servers->Cloud Compute

// Evolution movements (scenario, not forecast)
evolve Conversational AI Assistant 0.55
evolve IDE (Conversational AI+Human) 0.55
evolve Large Language Models 0.60
evolve FinOps (LLM cost governance) 0.55

// Strategic annotations
note Genesis/custom frontier: LLMs + conversational IDE [0.66, 0.10]
note Commoditised base: cloud + containers + OS [0.20, 0.95]
note High differentiation zone [0.70, 0.15]
note Outsource / utility candidates [0.15, 0.90]
```

## 4. Strategic analysis

### a. Top 3 by D = ν · (1 − ε) — differentiation pressure

1. **IDE (Conversational AI+Human)** — D = 0.78 · 0.82 = **0.64**. Highly visible to the developer, still Genesis/Custom. This is the single largest true differentiation zone in the stack; product experiences that move first on conversational editing become sticky.
2. **Conversational AI Assistant** — D = 0.74 · 0.78 = **0.58**. User-adjacent co-author; deep moats today are in fine-tuning, context retrieval, and UX, not in the base model.
3. **Large Language Models** — D = 0.54 · 0.72 = **0.39**. Still novel enough (and costly enough) that differentiated models and routing yield real advantage — but watch: LLMs are evolving fast and the D-value will collapse as they commoditise.

### b. Top 3 by K = (1 − ν) · ε — commodity leverage

1. **Cloud Compute** — K = 0.88 · 0.92 = **0.81**. Already a utility; rent it. Any self-host argument must clear a very high bar.
2. **Operating Systems** — K = 0.60 · 0.90 = **0.54**. Commodity substrate. Use mainstream distros; do not differentiate here.
3. **Containers** — K = 0.66 · 0.85 = **0.56**. Runtime commoditised (OCI + k8s). Consume managed container platforms; do not build your own.

### c. Top 3 dependency risks by R(a, b) = ν(a) · (1 − ε(b))

1. **(IDE (Conversational AI+Human), Conversational AI Assistant)** — R = 0.78 · 0.78 = **0.61**. The most visible new developer surface depends on an immature assistant layer — failure modes (hallucination, context drift, latency) directly hit the developer.
2. **(Conversational AI Assistant, Large Language Models)** — R = 0.74 · 0.72 = **0.53**. Single-model dependency risk; model regressions, licence changes, or price moves propagate straight to the IDE.
3. **(Conversational AI Assistant, FinOps (LLM cost governance))** — R = 0.74 · 0.80 = **0.59**. FinOps around LLM spend is itself Genesis — a brittle control plane underpinning a high-visibility cost driver.

### d. Suggested gameplays (Wardley's 61-play catalogue)

- **#15 Open Approaches (open source / open data)** on Component Libraries and on the conversational IDE extension surface — accelerate evolution of shared parts, keep differentiation in the orchestration and UX.
- **#29 Harvesting** on LLM vendors and managed-API providers — let the ecosystem shake out, then consume the winners as utilities.
- **#36 Directed investment** on the IDE (Conversational AI+Human) and the Conversational AI Assistant — these are the highest-D components, deserve deliberate build investment.
- **#39 Co-evolution of Practice with Activity** — DevOps Practice must evolve alongside the conversational IDE; expect "AI-native DevOps" practices to emerge (prompt review, eval gating, FinOps telemetry as first-class CI signal).
- **#9 Standards Game** on model/tool interfaces (e.g. MCP-style tool-use, prompt formats) — whoever sets the interface captures the ecosystem.
- **#23 Exploiting Constraint / bottleneck** on GPU/accelerator supply feeding LLMs — the constraint sits upstream of Cloud Compute; capacity contracts matter.
- **#7 Pig in a poke** warning on "agentic IDE" vendors — many early products will mis-sell Genesis as Product.

### e. Doctrine observations

- **Phase I — Focus on user needs**: anchor is explicit (Developer, Build Working Software). OK.
- **Phase II — Know your users / know the details**: the map could benefit from a second anchor for *Operators* (SRE/platform team) — they consume DevOps Practice and Orchestration directly. A single-developer anchor under-represents this.
- **Phase III — Use appropriate methods**: Genesis components (LLMs, Conversational IDE, FinOps) should be built experimentally (in-house, reduced-scope trials); Product components (Serverless, Component Libraries) should be bought; Commodity components (Cloud, OS, Containers) should be consumed as utility. The map respects this.
- **Phase III — Think FIRE (Fast, Inexpensive, Restrained, Elegant)** for the conversational IDE build — do not over-architect Genesis work.
- **Phase IV — Manage inertia**: two explicit `inertia` markers (Legacy Coding Approaches, Legacy Architecture) flag resistance. Likely forms (from the 17): *sunk capital* (existing .NET/LAMP estate), *human capital* (skills in legacy coding), *re-architecture cost* (rewriting onto serverless + LLM-assisted workflows), *political capital* (teams invested in current tooling). Explicitly name these when planning the transition.
- **Doctrine gap — Knowledge layer under-specified**: the K (Knowledge) component of component typing is implicit. If you apply τ, treat *prompt-engineering patterns* and *evaluation rubrics* as Knowledge components co-evolving with the IDE (Conversational AI+Human) Activity — they are the leading-edge knowledge that decides whether the conversational IDE delivers value.

## 5. What this means for how people build software

- The **bottom of the stack has commoditised**: cloud, containers, OS, orchestration, and even most runtimes are utilities or near-utilities. Differentiation here is effectively nil.
- A **new Genesis/Custom frontier has opened at the top**: conversational IDE, LLM-assisted coding, and LLM FinOps are immature, volatile, and where the advantage lives right now.
- **Two IDE modes coexist**: human-centric IDEs are Product-stage and stable; conversational AI+human IDEs are Genesis. Expect a decade-scale migration, with inertia (sunk tooling, mental models, review processes) slowing the transition.
- **Legacy coding approaches and architecture act as brakes** — they are deliberately marked `inertia`. Surface and name the forms of inertia rather than trying to force evolution.
- **FinOps for LLM usage is itself Genesis** — it sits next to LLMs and governs them, and is a credible differentiator for teams that operate at scale.
- The repo's three derived metrics (D, K, R) are *heuristics*, not canonical Wardley concepts; use them as attention prompts, not strategic verdicts. The logistic form `dε/dt = r · ε · (1 − ε)` referenced in the `evolve` directives is a scenario, not a forecast — Wardley's climatic pattern is that evolution cannot be measured over time.
