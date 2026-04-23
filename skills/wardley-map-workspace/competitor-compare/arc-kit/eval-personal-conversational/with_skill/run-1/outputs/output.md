# Personal Computing in the Age of Conversational AI (2026)

Produced with the arc-kit `wardley-mapping` skill.

## Step 1 — Context

| Question | Answer |
|---|---|
| Who is the primary user? | The developer (and, transitively, the end consumer of personal computing) |
| What is the user need? | Build and ship software in a world where conversational AI is reshaping the toolchain |
| Scope | The personal-computing stack end-to-end, from user surfaces down to compute utility |
| Primary goal | Show where the stack has commoditised (cloud + containers) and where it is still genesis/custom (LLMs + conversational IDEs); draw implications for how people build software |
| Industry / domain | Personal computing & developer tools, 2026 |
| Depth | Standard map (~20 components) with movement and a strategic readout |

## Step 2 — Value Chain

Working backwards from the anchor (developer building software), the visibility-ordered value chain is:

1. Developer (anchor)
2. Build & ship software (need)
3. Applications, Devices — the user-facing surfaces
4. IDE — split into human-centric mode and conversational (AI+human) mode
5. Component Libraries & Services; Legacy approaches
6. Runtime: Serverless (FaaS), Runtime: LAMP/.Net, Large Language Models, FinOps
7. Operating Systems, Orchestration (Kubernetes)
8. Containers, DevOps, Legacy architecture
9. Compute: on-prem Servers, Cloud (hyperscaler IaaS)

Dependencies flow strictly downward (every edge satisfies $\nu(a) \ge \nu(b)$); each visible surface ultimately resolves to compute, OS, and network. Because the scenario explicitly asks about the *conversational* shift, the IDE node is modelled as two components (human-centric, conversational) so the evolution gap between them is visible on the X-axis.

## Step 3 — Evolution Positioning

Evolution is assessed from market maturity (not age), using the arc-kit `evolution-stages` indicators.

| Component | Ubiquity | Certainty | Stage | X position | Rationale |
|---|---|---|---|---|---|
| Developer (anchor) | — | — | — | 0.45 | anchor point |
| Need: Build & Ship Software | — | — | — | 0.50 | anchor need |
| Applications | widespread | defined | Product | 0.72 | Mature app layer, being reshaped by AI |
| Devices | ubiquitous | standardised | Commodity | 0.90 | Laptops/phones — utility |
| IDE (Human-centric) | common | defined | Product | 0.70 | VS Code / JetBrains — mature vendor market |
| IDE (Conversational AI+Human) | early | forming | Custom | 0.28 | Cursor / Copilot / Claude Code — still shaping |
| Component Libraries & Services | common | defined | Product | 0.68 | npm/PyPI/Maven — mature ecosystems |
| Legacy Approaches (Waterfall/Scripted) | widespread | standardised | Commodity | 0.80 | Well-known, declining but entrenched |
| Runtime: Serverless (FaaS) | common | defined | Product→Commodity | 0.66 | Lambda/Functions — productised, commoditising |
| Runtime: LAMP / .Net | widespread | standardised | Commodity | 0.85 | Canonical commodity runtime |
| Large Language Models (LLMs) | rare-common | forming | Genesis→Custom | 0.22 | Frontier capability, a few API providers, no clear winner |
| FinOps (Cloud / LLM cost governance) | forming | forming | Custom | 0.38 | Emerging practice, few standard tools |
| Operating Systems | ubiquitous | standardised | Commodity | 0.88 | Linux/Windows/macOS — utility |
| Orchestration (Kubernetes etc.) | common | defined | Product→Commodity | 0.70 | K8s is the de-facto standard |
| Containers | ubiquitous | standardised | Commodity | 0.86 | Docker/OCI — utility |
| DevOps (CI/CD, IaC, SRE) | common | defined | Product | 0.68 | Mature but still differentiable |
| Legacy Architecture (Monoliths / Pet Servers) | widespread | standardised | Commodity | 0.78 | Stable, not differentiating, with inertia |
| Compute: Servers (On-Prem) | common | standardised | Commodity | 0.78 | Well-understood, being absorbed into cloud |
| Compute: Cloud (IaaS) | ubiquitous | standardised | Commodity | 0.94 | Utility pricing, interchangeable hyperscalers |

## Step 4 — Movement

Arrows show natural evolution (→), acceleration (>>) and inertia (×):

- **→ IDE (Conversational AI+Human)** 0.28 → 0.62 — productising fast as Cursor, Copilot, Claude Code converge on stable UX patterns.
- **>> Large Language Models** 0.22 → 0.55 — acceleration: hosted API commoditisation is outpacing normal S-curve speed.
- **→ FinOps** 0.38 → 0.60 — tooling and vendor offerings maturing as LLM and cloud spend become board-level topics.
- **→ Serverless runtime** 0.66 → 0.82 — drifting into commodity.
- **→ Orchestration (K8s)** 0.70 → 0.86 — now behind managed services (EKS/GKE/AKS), operator is invisible.
- **× LAMP / .Net** — heavy inertia: works, runs a huge installed base, unlikely to move.
- **× Legacy Architecture (monoliths / pet servers)** — inertia in enterprise, despite being economically dominated by containers + orchestration.
- **× Legacy approaches (waterfall / scripted)** — inertia in org process and culture.
- **→ On-prem servers** absorbed into cloud utility over time.

## Step 5 — Analysis and Recommendations

```yaml
wardley_map:
  metadata:
    title: "Personal Computing in the Age of Conversational AI (2026)"
    date: "2026-04-22"
    version: "1.0"
    scope: "Developer-facing personal-computing stack, from user surfaces to compute utility"

  anchor:
    user: "Developer (end user)"
    need: "Build and ship software"

  components:
    - name: "Applications"
      evolution: "Product"
      position: 0.72
      visibility: 0.88
      depends_on: ["IDE (Human-centric)", "IDE (Conversational AI+Human)", "Component Libraries & Services", "Runtime: Serverless (FaaS)", "Runtime: LAMP / .Net", "Devices"]
      movement: "evolving"
      notes: "Reshaped by generative AI features; commodity app delivery but uplift from conversational IDEs."

    - name: "Devices"
      evolution: "Commodity"
      position: 0.90
      visibility: 0.86
      depends_on: ["Operating Systems"]
      movement: "none"
      notes: "Utility."

    - name: "IDE (Human-centric)"
      evolution: "Product"
      position: 0.70
      visibility: 0.78
      depends_on: ["Operating Systems", "Component Libraries & Services", "Legacy Approaches (Waterfall / Scripted)"]
      movement: "evolving"
      notes: "VS Code / JetBrains — mature, feature-competitive."

    - name: "IDE (Conversational AI+Human)"
      evolution: "Custom"
      position: 0.28
      visibility: 0.76
      depends_on: ["Large Language Models (LLMs)", "Component Libraries & Services", "Operating Systems", "FinOps (Cloud / LLM Cost Governance)"]
      movement: "accelerating"
      notes: "Cursor/Copilot/Claude Code. UX still shaping. Differentiator for now — will productise within 2–3 years."

    - name: "Component Libraries & Services"
      evolution: "Product"
      position: 0.68
      visibility: 0.68
      depends_on: ["Runtime: Serverless (FaaS)", "Runtime: LAMP / .Net"]
      movement: "evolving"
      notes: "npm/PyPI/Maven — mature, package-manager driven."

    - name: "Legacy Approaches (Waterfall / Scripted)"
      evolution: "Commodity"
      position: 0.80
      visibility: 0.66
      depends_on: ["Runtime: LAMP / .Net", "Legacy Architecture (Monoliths / Pet Servers)"]
      movement: "inertia"
      notes: "Stable, declining, entrenched in large enterprises."

    - name: "Runtime: Serverless (FaaS)"
      evolution: "Product→Commodity"
      position: 0.66
      visibility: 0.58
      depends_on: ["Orchestration Tools (Kubernetes etc.)", "Containers"]
      movement: "evolving"
      notes: "Lambda / Cloud Run / Functions. On the commoditisation slope."

    - name: "Runtime: LAMP / .Net"
      evolution: "Commodity"
      position: 0.85
      visibility: 0.56
      depends_on: ["Operating Systems", "Legacy Architecture (Monoliths / Pet Servers)"]
      movement: "inertia"
      notes: "Canonical commodity stack; huge inertia due to installed base."

    - name: "Large Language Models (LLMs)"
      evolution: "Genesis→Custom"
      position: 0.22
      visibility: 0.60
      depends_on: ["Compute: Cloud (IaaS / Hyperscaler)", "FinOps (Cloud / LLM Cost Governance)", "Containers"]
      movement: "accelerating"
      notes: "Hosted API commoditisation is outrunning normal S-curve pace; still no clear winner on approach."

    - name: "FinOps (Cloud / LLM Cost Governance)"
      evolution: "Custom"
      position: 0.38
      visibility: 0.62
      depends_on: ["Compute: Cloud (IaaS / Hyperscaler)"]
      movement: "evolving"
      notes: "Emerging practice; tooling is maturing as LLM spend becomes board-level."

    - name: "Operating Systems"
      evolution: "Commodity"
      position: 0.88
      visibility: 0.46
      depends_on: ["Compute: Servers (On-Prem)", "Compute: Cloud (IaaS / Hyperscaler)"]
      movement: "none"
      notes: "Linux/Windows/macOS — utility."

    - name: "Orchestration Tools (Kubernetes etc.)"
      evolution: "Product→Commodity"
      position: 0.70
      visibility: 0.48
      depends_on: ["Containers", "Operating Systems"]
      movement: "evolving"
      notes: "K8s via managed services (EKS/GKE/AKS). Operator invisible for most users."

    - name: "Containers"
      evolution: "Commodity"
      position: 0.86
      visibility: 0.38
      depends_on: ["Operating Systems"]
      movement: "none"
      notes: "Docker/OCI — utility."

    - name: "DevOps (CI/CD, IaC, SRE)"
      evolution: "Product"
      position: 0.68
      visibility: 0.40
      depends_on: ["Containers", "Orchestration Tools (Kubernetes etc.)", "Runtime: Serverless (FaaS)", "Legacy Architecture (Monoliths / Pet Servers)"]
      movement: "evolving"
      notes: "Toolchains are mature but still competitive; differentiable via practice, not tech."

    - name: "Legacy Architecture (Monoliths / Pet Servers)"
      evolution: "Commodity"
      position: 0.78
      visibility: 0.36
      depends_on: ["Compute: Servers (On-Prem)", "Compute: Cloud (IaaS / Hyperscaler)"]
      movement: "inertia"
      notes: "Not differentiating but stable; heavy migration cost."

    - name: "Compute: Servers (On-Prem)"
      evolution: "Commodity"
      position: 0.78
      visibility: 0.18
      depends_on: []
      movement: "evolving"
      notes: "Being absorbed into cloud utility."

    - name: "Compute: Cloud (IaaS / Hyperscaler)"
      evolution: "Commodity"
      position: 0.94
      visibility: 0.12
      depends_on: []
      movement: "none"
      notes: "Utility pricing, interchangeable hyperscalers."

  analysis:
    opportunities:
      - "Build on conversational IDE + LLM while they are still custom — this is the layer where differentiation is possible in 2026."
      - "Treat compute/containers/OS/orchestration as utility — consume, do not build."
      - "Commoditise FinOps early: LLM + cloud bills are now correlated and need a single practice to contain them."
      - "Decouple applications from the IDE mode so users can flip between human-centric and conversational without rewriting app code."

    threats:
      - "Hyperscalers absorbing the LLM stack and the conversational IDE stack vertically, collapsing differentiation windows."
      - "Inertia from LAMP/.Net + monoliths + legacy approaches producing slow migration paths that starve the new stack."
      - "Conversational IDEs leaking proprietary code to third-party LLM providers — governance / FinOps risk."
      - "Dependency risk: the most visible, rapidly-evolving work (conversational IDE) depends on a still-immature commodity (LLM API) — a high R(a,b)."

    inertia_points:
      - component: "Runtime: LAMP / .Net"
        reason: "Huge installed base, entrenched Ops skills, migration ROI unclear."
      - component: "Legacy Architecture (Monoliths / Pet Servers)"
        reason: "Business processes, data gravity, org structure aligned to it."
      - component: "Legacy Approaches (Waterfall / Scripted)"
        reason: "Compliance regimes, procurement cycles, org hierarchies."

  recommendations:
    immediate:
      - "Treat Cloud + Containers + OS + Orchestration as the commodity floor. Stop building, start consuming via managed services."
      - "Stand up a FinOps capability that covers both cloud IaaS and LLM API spend as one budget line."
    short_term:
      - "Roll out conversational IDEs (AI+human) alongside human-centric IDEs. Do not force a replacement — let the team self-select."
      - "Put a contract / policy wrapper around LLM calls so code, data, and costs are governed centrally."
    long_term:
      - "Expect conversational IDE + LLM to land at Product stage inside 2–3 years. Assume the differentiation window closes then."
      - "Plan deliberate retirement paths for LAMP/.Net monoliths — even at commodity stage, they are the anchor that stops the upper stack from moving."
```

### Strategic readout (plain English)

- **Commoditised floor:** Cloud, Containers, Operating Systems, Orchestration, LAMP/.Net runtime, DevOps tooling and Devices are now utility — the correct posture is *consume*, not *build*. This is what the scenario asks us to confirm.
- **Genesis / Custom frontier:** LLMs and Conversational IDEs are the two components still on the left of the map. Together they represent the current differentiation window — the bit of the stack where how you build software in 2026 is genuinely different from how you built it in 2021.
- **Middle tension:** FinOps sits awkwardly between the commodity floor and the genesis frontier. As LLM spend scales, FinOps gets pulled left (new tooling, custom dashboards) even while cloud FinOps pulls right (standard practice). Expect rapid maturation here.
- **What it means for how people build software:** The toolchain shape is inverting. Human-centric IDEs assumed a developer authoring every line; conversational IDEs assume the LLM authors drafts and the developer steers. That changes the skills mix (Pioneers on the conversational side, Settlers maturing the AI+human UX, Town Planners still running the commodity floor), the cost model (FinOps matters in a way it didn't), and the design target (applications are increasingly shaped by LLM affordances rather than by the capabilities of the device).

## Map (visual)

```text
Title: Personal Computing in the Age of Conversational AI (2026)
Anchor: Developer → Build & Ship Software
Date: 2026-04-22

                     Genesis       Custom       Product      Commodity
                        │             │             │             │
Visible            ┌────┼─────────────┼─────────────┼─────────────┼────┐
                   │    │             │             │             │    │
 0.95              │    │   ● Developer   ● Need                  │    │
                   │    │       │             │                   │    │
 0.85              │    │       ↓             ↓                   │    │
                   │    │                                 ● Applications ● Devices
                   │    │                                                   │
 0.75              │    │                              ● IDE-H   ● IDE-Conv │
                   │    │                                   ×    →          │
 0.65              │    │                         ● Libs+Svc    ● Legacy Approaches ×
                   │    │                              →             ×              │
 0.55              │    │   ● LLMs         ● FinOps   ● FaaS       ● LAMP/.Net ×   │
                   │    │       >>             →            →                       │
 0.45              │    │                                                 ● OS       │
                   │    │                              ● K8s                         │
 0.35              │    │                                                  ● Containers │
                   │    │                              ● DevOps   ● Legacy Arch. ×  │
                   │    │                                 →                          │
 0.15              │    │                                                 ● On-Prem ● Cloud │
Hidden             │    │                                                    →              │
                   └────┴───────────────────────────────────────────────────────────────────┘

Legend: ● Current position, → evolving, >> accelerating, × inertia
```
