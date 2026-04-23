# Wardley Value Chain: Personal Computing in the Age of Conversational AI

## Executive Summary

Anchor: **Developer** with the need to **build software productively** in a landscape where conversational AI has become a first-class partner in the IDE. The chain captures 20 components across 7 visibility tiers, from the developer at the top down through applications, IDE modes (human-only vs. conversational AI+human), component libraries and services, runtime choices (Serverless vs. LAMP/.NET), large language models and FinOps, operating systems and orchestration, containers, DevOps and legacy architecture, and finally commodity compute (servers and cloud).

Key strategic insights:

1. The **IDE has bifurcated** into two co-existing modes — human-only and conversational AI+human — both served by the same libraries and services, but only the AI+human IDE depends on the LLM tier.
2. **LLMs are a new, parallel branch** of the stack: they sit at medium visibility, share cloud compute with the rest of the stack, and introduce **FinOps** as a mandatory adjacent discipline because token economics is now a first-class cost.
3. The stack has **commoditised from containers downward** (containers → DevOps / legacy architecture → servers → cloud), leaving LLMs and conversational IDEs as the remaining genesis/custom frontier where differentiation is concentrated.

This is a value-chain-only decomposition — evolution positions are a placeholder (ε = 0.50) and are assigned in the subsequent `$arckit-wardley` step.

## Users and Personas

| User | Primary need | Role in chain |
| --- | --- | --- |
| Developer (individual contributor) | Build software productively using both classical and AI-assisted tools | Anchor |
| Team lead / architect | Choose runtime, IDE mode, and build-vs-buy for LLM features | Consumes same chain, different lens |
| Operator / SRE | Keep the stack running across containers, orchestration, and cloud | Lives in the lower half of the chain |

For this chain the anchor is the **individual developer** — the productivity outcome is what the upper half of the stack exists to deliver.

## Anchor Statement

```text
Anchor: Developer can build software productively given a stack that now includes conversational AI
User:   Individual developer building applications on personal-computing devices
Outcome: Developer reaches a working, deployable artefact with fewer manual steps, using whichever IDE mode (human-only or AI+human) best fits the task
```

## Value Chain Diagram (ASCII)

```text
                               Developer  (0.95)
                                   |
                        Build Software Productively  (0.90)
                              /              \
                     Applications (0.82)    Devices (0.78)
                      /        \                 \
          IDE Human (0.74)   IDE AI+Human (0.72)   \
             |   \              |    \              \
             |   Libraries (0.62)    Services (0.60)  \
             |   |      \          /   |               \
             Legacy Approaches (0.58)  Large Language Models (0.46)
                    |                     |       \
          Runtime Serverless (0.50)   FinOps (0.44)  \
          Runtime LAMP/.NET (0.48)       |             \
               |                         |              \
               +---- Operating Systems (0.36) -----------+
               +---- Orchestration Tools (0.34)
                              |
                         Containers (0.26)
                          /         \
                    DevOps (0.20)   Legacy Architecture (0.18)
                          \         /
                          Servers (0.10)
                              |
                         Cloud Compute (0.08)
```

## OWM Code

Paste into <https://create.wardleymaps.ai> to render the value chain. Evolution (X) is a placeholder 0.50 across all components — this is a value-chain-only artifact.

```text
title Personal Computing in the Age of Conversational AI

anchor Developer [0.95, 0.02]
component Build Software Productively [0.90, 0.50]
component Applications [0.82, 0.50]
component Devices [0.78, 0.50]
component IDE (Human) [0.74, 0.50]
component IDE (Conversational AI + Human) [0.72, 0.50]
component Component Libraries [0.62, 0.50]
component Services [0.60, 0.50]
component Legacy Approaches [0.58, 0.50]
component Runtime (Serverless) [0.50, 0.50]
component Runtime (LAMP / .NET) [0.48, 0.50]
component Large Language Models [0.46, 0.50]
component FinOps [0.44, 0.50]
component Operating Systems [0.36, 0.50]
component Orchestration Tools [0.34, 0.50]
component Containers [0.26, 0.50]
component DevOps [0.20, 0.50]
component Legacy Architecture [0.18, 0.50]
component Servers [0.10, 0.50]
component Cloud Compute [0.08, 0.50]

Developer->Build Software Productively
Build Software Productively->Applications
Build Software Productively->Devices
Applications->IDE (Human)
Applications->IDE (Conversational AI + Human)
IDE (Human)->Component Libraries
IDE (Human)->Services
IDE (Human)->Legacy Approaches
IDE (Conversational AI + Human)->Component Libraries
IDE (Conversational AI + Human)->Services
IDE (Conversational AI + Human)->Large Language Models
Component Libraries->Runtime (Serverless)
Component Libraries->Runtime (LAMP / .NET)
Services->Runtime (Serverless)
Services->Runtime (LAMP / .NET)
Legacy Approaches->Runtime (LAMP / .NET)
Large Language Models->FinOps
Large Language Models->Cloud Compute
Runtime (Serverless)->Operating Systems
Runtime (Serverless)->Orchestration Tools
Runtime (LAMP / .NET)->Operating Systems
FinOps->Cloud Compute
Operating Systems->Containers
Orchestration Tools->Containers
Containers->DevOps
Containers->Legacy Architecture
DevOps->Servers
DevOps->Cloud Compute
Legacy Architecture->Servers
Servers->Cloud Compute
Devices->Operating Systems

style wardley
```

<details>
<summary>Mermaid wardley-beta equivalent</summary>

```mermaid
wardley-beta
title Personal Computing in the Age of Conversational AI
size [1100, 800]

anchor Developer [0.95, 0.02]
component "Build Software Productively" [0.90, 0.50]
component Applications [0.82, 0.50]
component Devices [0.78, 0.50]
component "IDE (Human)" [0.74, 0.50]
component "IDE (Conversational AI + Human)" [0.72, 0.50]
component "Component Libraries" [0.62, 0.50]
component Services [0.60, 0.50]
component "Legacy Approaches" [0.58, 0.50]
component "Runtime (Serverless)" [0.50, 0.50]
component "Runtime (LAMP / .NET)" [0.48, 0.50]
component "Large Language Models" [0.46, 0.50]
component FinOps [0.44, 0.50]
component "Operating Systems" [0.36, 0.50]
component "Orchestration Tools" [0.34, 0.50]
component Containers [0.26, 0.50]
component DevOps [0.20, 0.50]
component "Legacy Architecture" [0.18, 0.50]
component Servers [0.10, 0.50]
component "Cloud Compute" [0.08, 0.50]

Developer -> "Build Software Productively"
"Build Software Productively" -> Applications
"Build Software Productively" -> Devices
Applications -> "IDE (Human)"
Applications -> "IDE (Conversational AI + Human)"
"IDE (Human)" -> "Component Libraries"
"IDE (Human)" -> Services
"IDE (Human)" -> "Legacy Approaches"
"IDE (Conversational AI + Human)" -> "Component Libraries"
"IDE (Conversational AI + Human)" -> Services
"IDE (Conversational AI + Human)" -> "Large Language Models"
"Component Libraries" -> "Runtime (Serverless)"
"Component Libraries" -> "Runtime (LAMP / .NET)"
Services -> "Runtime (Serverless)"
Services -> "Runtime (LAMP / .NET)"
"Legacy Approaches" -> "Runtime (LAMP / .NET)"
"Large Language Models" -> FinOps
"Large Language Models" -> "Cloud Compute"
"Runtime (Serverless)" -> "Operating Systems"
"Runtime (Serverless)" -> "Orchestration Tools"
"Runtime (LAMP / .NET)" -> "Operating Systems"
FinOps -> "Cloud Compute"
"Operating Systems" -> Containers
"Orchestration Tools" -> Containers
Containers -> DevOps
Containers -> "Legacy Architecture"
DevOps -> Servers
DevOps -> "Cloud Compute"
"Legacy Architecture" -> Servers
Servers -> "Cloud Compute"
Devices -> "Operating Systems"
```

</details>

## Component Inventory

| # | Component | Visibility | Description | Depends on |
| - | --- | --- | --- | --- |
| 1 | Developer | 0.95 (anchor) | Individual developer building software; the user need | Build Software Productively |
| 2 | Build Software Productively | 0.90 | The purposeful outcome the stack exists to satisfy | Applications, Devices |
| 3 | Applications | 0.82 | The software artefacts developers produce and interact with | IDE (Human), IDE (AI+Human) |
| 4 | Devices | 0.78 | Personal-computing hardware (laptops, workstations, mobile) the developer uses | Operating Systems |
| 5 | IDE (Human) | 0.74 | Classical IDE mode — edit, compile, debug, test, refactor with human-only control | Component Libraries, Services, Legacy Approaches |
| 6 | IDE (Conversational AI + Human) | 0.72 | AI-assisted IDE mode — chat, completion, agentic refactor, natural-language edits | Component Libraries, Services, Large Language Models |
| 7 | Component Libraries | 0.62 | Reusable packages and SDKs (npm, NuGet, PyPI, etc.) the IDE pulls in | Runtime (Serverless), Runtime (LAMP / .NET) |
| 8 | Services | 0.60 | External APIs and managed services called from the developer's code | Runtime (Serverless), Runtime (LAMP / .NET) |
| 9 | Legacy Approaches | 0.58 | Established patterns (monolithic apps, server-side rendering, procedural scripts) still in wide use | Runtime (LAMP / .NET) |
| 10 | Runtime (Serverless) | 0.50 | Event-driven execution runtimes (AWS Lambda, Cloud Run, Azure Functions) | Operating Systems, Orchestration Tools |
| 11 | Runtime (LAMP / .NET) | 0.48 | Classical long-running runtimes — Linux/Apache/MySQL/PHP stack, .NET | Operating Systems |
| 12 | Large Language Models | 0.46 | Foundation models serving code completions, chat, and agent calls | FinOps, Cloud Compute |
| 13 | FinOps | 0.44 | Discipline of managing token / compute cost, budgets, and rate limits | Cloud Compute |
| 14 | Operating Systems | 0.36 | Host OS (Linux, Windows, macOS) on devices and in the runtime | Containers |
| 15 | Orchestration Tools | 0.34 | Kubernetes, ECS, Nomad — schedule and manage container workloads | Containers |
| 16 | Containers | 0.26 | Docker / OCI — portable units of deployment | DevOps, Legacy Architecture |
| 17 | DevOps | 0.20 | CI/CD, infra-as-code, release automation | Servers, Cloud Compute |
| 18 | Legacy Architecture | 0.18 | VMs, bare-metal deployments, classical hosted environments | Servers |
| 19 | Servers | 0.10 | Physical and virtual server hardware | Cloud Compute |
| 20 | Cloud Compute | 0.08 | Commodity cloud — AWS / Azure / GCP raw compute | Terminal |

## Dependency Matrix (direct only)

Rows depend on columns. `X` = direct dependency.

|  | Apps | Dev | IDE-H | IDE-AI | Libs | Svcs | Leg-A | RT-S | RT-L | LLM | FO | OS | Orch | Cntr | DO | Leg-Arch | Srv | Cloud |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Build Software Productively | X | X |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Applications |  |  | X | X |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Devices |  |  |  |  |  |  |  |  |  |  |  | X |  |  |  |  |  |  |
| IDE (Human) |  |  |  |  | X | X | X |  |  |  |  |  |  |  |  |  |  |  |
| IDE (AI+Human) |  |  |  |  | X | X |  |  |  | X |  |  |  |  |  |  |  |  |
| Component Libraries |  |  |  |  |  |  |  | X | X |  |  |  |  |  |  |  |  |  |
| Services |  |  |  |  |  |  |  | X | X |  |  |  |  |  |  |  |  |  |
| Legacy Approaches |  |  |  |  |  |  |  |  | X |  |  |  |  |  |  |  |  |  |
| Runtime (Serverless) |  |  |  |  |  |  |  |  |  |  |  | X | X |  |  |  |  |  |
| Runtime (LAMP / .NET) |  |  |  |  |  |  |  |  |  |  |  | X |  |  |  |  |  |  |
| Large Language Models |  |  |  |  |  |  |  |  |  |  | X |  |  |  |  |  |  | X |
| FinOps |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | X |
| Operating Systems |  |  |  |  |  |  |  |  |  |  |  |  |  | X |  |  |  |  |
| Orchestration Tools |  |  |  |  |  |  |  |  |  |  |  |  |  | X |  |  |  |  |
| Containers |  |  |  |  |  |  |  |  |  |  |  |  |  |  | X | X |  |  |
| DevOps |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | X | X |
| Legacy Architecture |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | X |  |
| Servers |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | X |

## Critical Path Analysis

**Deepest path (AI+human branch)**:

```text
Developer → Build Software Productively → Applications → IDE (AI+Human)
         → Large Language Models → FinOps → Cloud Compute
```

**Deepest path (classical branch)**:

```text
Developer → Build Software Productively → Applications → IDE (Human)
         → Services → Runtime (Serverless) → Orchestration Tools
         → Containers → DevOps → Cloud Compute
```

**Bottlenecks and single points of failure**:

- **Cloud Compute** is the terminal commodity for both branches; outage here breaks the entire stack (both classical and AI-assisted).
- **Large Language Models** is a single point of failure for the AI+human IDE branch but *not* for the human-only branch — a useful resilience property.
- **Operating Systems** and **Containers** are the two chokepoints through which almost every runtime path flows.
- **FinOps** is a soft bottleneck — LLM cost is a run-rate constraint that can throttle AI-assisted capacity before any technical failure occurs.

**Resilience gaps**:

- No observability / monitoring component is listed at the infra tier — likely omitted in the user's narrative but a common gap to flag for the next iteration.
- No security / identity component — same flag.

## Validation Checklist

Completeness:

- [x] Chain starts with a genuine user need (Developer → build software productively), not a solution.
- [x] All significant dependencies between the narrative's listed components are captured.
- [x] Chain reaches commodity level (Cloud Compute).
- [x] No orphan components — every component has at least one incoming or outgoing edge.
- [x] All components are capabilities/activities, not people or teams (Developer is the anchor user, not a component).

Accuracy:

- [x] Dependencies reflect real-world technical relationships (IDE → libraries/services/LLM, runtimes → OS, containers → DevOps, etc.).
- [x] Visibility ordering is consistent with dependency direction — parent components always have visibility at or above children.
- [x] No component is simultaneously user-facing and infrastructure.

Usefulness:

- [x] Granularity is strategic (20 components, within the skill's 8–20 target range).
- [x] Each component can later be positioned on the evolution axis.
- [x] Chain reveals strategic insights (LLM/IDE-AI as genesis/custom; containers-and-below as commodity; FinOps as a newly-mandatory discipline).

Math-model constraints:

- [x] DAG — no cycles.
- [x] Visibility ordering: for every edge A → B, ν(A) ≥ ν(B).
- [x] Anchor has visibility ≥ 0.90 (Developer = 0.95).

## Visibility Assessment

| Component | Visibility | Justification |
| --- | --- | --- |
| Developer | 0.95 | Anchor — the user whose need the chain exists to serve. |
| Build Software Productively | 0.90 | The purposeful outcome; directly experienced as "did I ship?" |
| Applications | 0.82 | What the developer produces and runs; immediately visible. |
| Devices | 0.78 | Physical artefact the developer touches every working minute. |
| IDE (Human) | 0.74 | The primary classical tool; failure is immediately noticed. |
| IDE (Conversational AI + Human) | 0.72 | Newer tool surface; equally visible when used. |
| Component Libraries | 0.62 | One step removed — developer sees package manager output. |
| Services | 0.60 | One step removed — developer sees API responses, not infra. |
| Legacy Approaches | 0.58 | Visible as a choice of pattern more than an artefact. |
| Runtime (Serverless) | 0.50 | Deployment target; visible when things go wrong. |
| Runtime (LAMP / .NET) | 0.48 | Same role, classical runtimes. |
| Large Language Models | 0.46 | Visible indirectly through IDE-AI quality; not directly touched. |
| FinOps | 0.44 | Visible through budgets and throttling, not through UI. |
| Operating Systems | 0.36 | Largely hidden behind IDE and runtime abstractions. |
| Orchestration Tools | 0.34 | Operator concern; developer sees deployment manifests only. |
| Containers | 0.26 | Infrastructure primitive; hidden from application-level developers. |
| DevOps | 0.20 | Pipelines visible only when they fail. |
| Legacy Architecture | 0.18 | Deep infra for legacy workloads. |
| Servers | 0.10 | Commodity hardware layer; invisible to developers day-to-day. |
| Cloud Compute | 0.08 | Deep commodity; users unaware it exists unless it goes down. |

## Assumptions and Open Questions

**Assumptions**:

1. The "Developer" anchor is the individual contributor — not a product manager, CTO, or end-user of the developer's application.
2. "IDE (Human)" and "IDE (Conversational AI + Human)" are treated as two distinct components in the same layer, not a single IDE with two modes — this reflects the strategic reality that they evolve at different rates.
3. "Legacy Approaches" (a set of established patterns) depends on "Runtime (LAMP / .NET)" because that is the runtime where those patterns predominate; it does not depend on Serverless.
4. LLMs are treated as a runtime-adjacent tier, drawing from cloud compute and consuming FinOps, rather than as a library inside the IDE, because token-economic and latency constraints make them behave as external services, not as linked libraries.
5. FinOps is modelled as a capability/practice that sits between LLMs and cloud compute — it governs the cost interface between them rather than being infrastructure itself.

**Open questions for the next iteration**:

1. Should observability / monitoring be added as an explicit component? The user's narrative did not mention it.
2. Should identity / auth be added as an explicit component?
3. Does the user want the "Devices" branch expanded (GPU vs. CPU laptops, edge NPUs) given that local inference is an emerging alternative to cloud LLMs?
4. Does the user want evolution positions assigned now, or is this strictly a value-chain deliverable? (Current output assumes the latter — ε = 0.50 across all non-anchor components.)
