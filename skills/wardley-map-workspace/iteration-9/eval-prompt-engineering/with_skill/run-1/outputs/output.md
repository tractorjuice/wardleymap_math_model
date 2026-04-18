# Wardley Map — Production-Grade Prompt Engineering Capability

**Scenario:** Engineering team wants to move prompt engineering from code comments and vibes to a production-grade capability: prompt versioning, systematic evaluation, A/B testing against live traffic, observability, continuous-improvement feedback loop. Decide what to build in-house vs buy SaaS vs consume as utility API.

---

## Map (OWM)

```owm
title Production-Grade Prompt Engineering Capability
style wardley

// Anchors — three user types for this platform capability
anchor Product Engineer [0.98, 0.55]
anchor ML/Applied Scientist [0.95, 0.45]
anchor Product Manager [0.93, 0.60]

// User-facing surfaces
component Prompt Authoring UI [0.88, 0.55]
component Prompt Playground [0.86, 0.60]
component Eval Results Dashboard [0.84, 0.55]
component Experiment Console (A/B results) [0.82, 0.50]
component Feedback Capture (thumbs/rating) [0.80, 0.70]

// Prompt lifecycle core
component Prompt Registry (versioning) [0.74, 0.55]
component Prompt Deployment / Release Channels [0.70, 0.50]
component Prompt Template Runtime [0.68, 0.60]
component Feature Flagging / Traffic Split [0.69, 0.78]

// Evaluation layer
component Offline Eval Runner [0.62, 0.45]
component Golden Dataset Curation [0.58, 0.40]
component LLM-as-Judge Scorers [0.56, 0.35]
component Human Review Workflow [0.54, 0.30]
component Heuristic / Regex Scorers [0.52, 0.70]
component Regression Suites (CI) [0.63, 0.55]

// Observability / telemetry
component Trace Collection (spans) [0.60, 0.65]
component Prompt/Response Logging [0.58, 0.70]
component Token and Cost Metering [0.50, 0.75]
component Latency / Error Monitoring [0.45, 0.88]
component PII Redaction on Logs [0.42, 0.55]

// Production routing & runtime
component LLM Gateway / Model Router [0.55, 0.65]
component Guardrails (policy / safety) [0.48, 0.45]
component Semantic / Prompt Cache [0.40, 0.55]
component Rate Limiting and Quotas [0.38, 0.85]

// Feedback loop
component Production Trace Sampling [0.59, 0.55]
component Auto Dataset Mining (from traffic) [0.60, 0.35]
component Annotation Tooling [0.42, 0.50]

// Foundational data & infra
component OpenTelemetry Instrumentation [0.35, 0.80]
component Event Bus / Queue [0.28, 0.90]
component Data Warehouse (evals + traces) [0.25, 0.85]
component Object Storage [0.18, 0.92]
component Cloud Compute [0.15, 0.92]
component Auth / SSO [0.20, 0.92]
component Secrets Management [0.18, 0.90]

// Model supply
component Frontier LLM APIs [0.30, 0.75]
component Open-weight / Self-hosted LLM [0.25, 0.50]
component Embedding APIs [0.22, 0.85]

// Knowledge / practice
component Prompt Eng. Review Practice [0.15, 0.35]
component Eval Methodology Knowledge [0.10, 0.40]

// Dependencies — anchor edges
Product Engineer->Prompt Authoring UI
Product Engineer->Prompt Playground
Product Engineer->Eval Results Dashboard
Product Engineer->Experiment Console (A/B results)
ML/Applied Scientist->Prompt Playground
ML/Applied Scientist->Eval Results Dashboard
ML/Applied Scientist->Golden Dataset Curation
ML/Applied Scientist->Human Review Workflow
Product Manager->Experiment Console (A/B results)
Product Manager->Feedback Capture (thumbs/rating)
Product Manager->Eval Results Dashboard

// Authoring / playground -> registry & runtime
Prompt Authoring UI->Prompt Registry (versioning)
Prompt Playground->Prompt Registry (versioning)
Prompt Playground->LLM Gateway / Model Router
Prompt Registry (versioning)->Prompt Deployment / Release Channels
Prompt Deployment / Release Channels->Prompt Template Runtime
Prompt Deployment / Release Channels->Feature Flagging / Traffic Split
Prompt Template Runtime->LLM Gateway / Model Router

// Experiment console chain
Experiment Console (A/B results)->Feature Flagging / Traffic Split
Experiment Console (A/B results)->Data Warehouse (evals + traces)
Feature Flagging / Traffic Split->Prompt Template Runtime

// Eval layer
Eval Results Dashboard->Offline Eval Runner
Eval Results Dashboard->Regression Suites (CI)
Offline Eval Runner->Golden Dataset Curation
Offline Eval Runner->LLM-as-Judge Scorers
Offline Eval Runner->Heuristic / Regex Scorers
Offline Eval Runner->Human Review Workflow
Regression Suites (CI)->Offline Eval Runner
LLM-as-Judge Scorers->LLM Gateway / Model Router
Golden Dataset Curation->Object Storage
Human Review Workflow->Annotation Tooling

// Observability
Prompt Template Runtime->Trace Collection (spans)
Trace Collection (spans)->OpenTelemetry Instrumentation
Trace Collection (spans)->Prompt/Response Logging
Prompt/Response Logging->PII Redaction on Logs
Prompt/Response Logging->Data Warehouse (evals + traces)
Token and Cost Metering->Data Warehouse (evals + traces)
Latency / Error Monitoring->OpenTelemetry Instrumentation

// Feedback loop
Feedback Capture (thumbs/rating)->Event Bus / Queue
Production Trace Sampling->Prompt/Response Logging
Auto Dataset Mining (from traffic)->Production Trace Sampling
Auto Dataset Mining (from traffic)->Golden Dataset Curation
Annotation Tooling->Data Warehouse (evals + traces)

// Runtime deps
LLM Gateway / Model Router->Frontier LLM APIs
LLM Gateway / Model Router->Open-weight / Self-hosted LLM
LLM Gateway / Model Router->Guardrails (policy / safety)
LLM Gateway / Model Router->Semantic / Prompt Cache
LLM Gateway / Model Router->Rate Limiting and Quotas
LLM Gateway / Model Router->Token and Cost Metering

// Embedding use by dataset mining
Auto Dataset Mining (from traffic)->Embedding APIs

// Infra / auth
Prompt Authoring UI->Auth / SSO
Prompt Registry (versioning)->Data Warehouse (evals + traces)
Prompt Registry (versioning)->Object Storage
LLM Gateway / Model Router->Secrets Management
Data Warehouse (evals + traces)->Cloud Compute
Event Bus / Queue->Cloud Compute
Object Storage->Cloud Compute

// Knowledge edges
Golden Dataset Curation->Eval Methodology Knowledge
LLM-as-Judge Scorers->Eval Methodology Knowledge
Prompt Authoring UI->Prompt Eng. Review Practice

evolve Prompt Registry (versioning) 0.75
evolve LLM Gateway / Model Router 0.82
evolve LLM-as-Judge Scorers 0.55
evolve Auto Dataset Mining (from traffic) 0.55

note Differentiation zone [0.55, 0.32]
note Rent — Stage III [0.55, 0.68]
note Utility — Stage IV [0.20, 0.90]
```

**Validator result:** `OK: 42 components/anchors, 60 edges — no violations.`

---

## Strategic analysis

### a. Top 3 by Differentiation pressure D = ν·(1−ε)

> Heuristic from this skill's math model, not canonical Wardley.

1. **Human Review Workflow** (0.54 × 0.70 = 0.38) — how your team captures expert judgement on model output is the unfair edge. Annotation UX, SME routing, reviewer calibration — nobody else's process works for your domain.
2. **LLM-as-Judge Scorers** (0.56 × 0.65 = 0.36) — the *scoring rubrics specific to your product's failure modes* are your moat. Generic "faithfulness" scorers are commoditising fast, but your specific accept/reject criteria for your domain are differentiating.
3. **Golden Dataset Curation** (0.58 × 0.60 = 0.35) — the labelled traffic that reflects *your* users doing *your* tasks. This compounds with every release cycle and is the single asset a competitor cannot copy.

Runners-up worth noting: **Auto Dataset Mining (from traffic)** (0.60 × 0.65 = 0.39 — actually edges #3 out if you treat it as differentiation; listed here because it is the machinery that populates #3 above), **Guardrails (policy/safety)** (0.48 × 0.55 = 0.26).

### b. Top 3 by Commodity leverage K = (1−ν)·ε

> Heuristic.

1. **Cloud Compute** (0.85 × 0.92 = 0.78) — AWS/GCP/Azure. Stage IV (+utility). Do not engineer.
2. **Object Storage** (0.82 × 0.92 = 0.75) — S3/GCS. Utility.
3. **Auth / SSO** (0.80 × 0.92 = 0.74) — Okta/Entra/Clerk/WorkOS. Utility.

Also saturating in the K-high band: **Event Bus / Queue** (0.72 × 0.90 = 0.65), **Latency / Error Monitoring** (0.55 × 0.88 = 0.48), **Rate Limiting and Quotas** (0.62 × 0.85 = 0.53), **Embedding APIs** (0.78 × 0.85 = 0.66), **Frontier LLM APIs** (0.70 × 0.75 = 0.525), **Secrets Management** (0.82 × 0.90 = 0.74).

### c. Top 3 Dependency risks R = ν(a)·(1−ε(b))

> Heuristic.

1. **(Prompt Authoring UI, Prompt Registry (versioning))** = 0.88 × 0.45 = 0.40 — the authoring surface depends on a registry whose semantics (branching, approval, rollback) are still in transition across vendors. If you pick the wrong abstraction now, migration hurts.
2. **(Eval Results Dashboard, Offline Eval Runner)** = 0.84 × 0.55 = 0.46 — the whole visibility the team gets into quality sits on an eval runner that is itself immature. If the runner's scoring semantics shift, every historical result needs recomputing.
3. **(Experiment Console, Feature Flagging / Traffic Split)** = 0.82 × 0.22 = 0.18 — low R in absolute terms because flagging is mature, but included because it is the mechanism your A/B strategy depends on. A subtler risk: **(Experiment Console, Data Warehouse)** = 0.82 × 0.15 = 0.12, but the *semantic* risk is that the traffic split abstraction must handle prompt-level variants cleanly, not just flag-on/flag-off.

Honourable mention: **(Auto Dataset Mining, Production Trace Sampling)** = 0.60 × 0.45 = 0.27 — your feedback loop hinges on sampling policy correctness (representativeness, PII safety).

### d. Suggested gameplays (from Wardley's 61)

- **#1 Focus on user needs** — anchors are Product Engineer, ML/Applied Scientist, PM. Do not let a vendor roadmap define your UI; your authoring/playground UI is the daily surface for three personas who think very differently.
- **#36 Directed investment** on the four BUILD components: **Human Review Workflow**, **LLM-as-Judge Scorers (your rubrics)**, **Golden Dataset Curation**, **Auto Dataset Mining**. These are Stage I–II and your moat lives here.
- **#29 Harvesting** on **LLM Gateway / Model Router** — the open source (LiteLLM) and SaaS (Portkey, OpenRouter, Cloudflare AI Gateway) markets are fragmenting fast; pick a standards-compatible one, don't build.
- **#15 Open Approaches** on **OpenTelemetry Instrumentation** and **Prompt/Response Logging schema** — adopt OTel GenAI semantic conventions so you are not locked into one observability vendor. Export your traces cleanly.
- **#56 First mover** on the **Feedback Loop (Auto Dataset Mining → Golden Dataset → Offline Eval Runner)** — this compounding-data flywheel is a first-mover prize within your own product. Shipping it 6 months earlier means 6 months of labelled production data the competition does not have.
- **#45 Two factor** / **#16 Exploiting Network Effects** — if your product surfaces prompts to end-users (agents, workflows), the feedback flywheel becomes a proper network effect. Worth recognising.
- **#43 Sensing Engines (ILC)** — watch the prompt-management vendor race (Braintrust, Langfuse, PromptLayer, Maxim, Confident AI, LangSmith). Do not marry one until the category consolidates; keep your registry abstracted behind a thin internal interface so you can swap.
- **#41 Alliances / Second-sourcing** on **Frontier LLM APIs** — never route to a single provider; the gateway exists precisely to keep optionality.
- **#55 Play Chess (not checkers)** — because `evolve LLM Gateway / Model Router → 0.82` and `evolve Prompt Registry → 0.75`, the prompt-management SaaS category is heading to Stage III Product (+rental) / early Stage IV Commodity (+utility). Don't start a 2-year build on a category that will be a commodity API in 18 months.

### e. Doctrine violations / notes

- ✓ **#1 Focus on user needs** — three anchors distinguish Engineer, ML/Applied Scientist, PM. The capability is not one-size-fits-all.
- ✓ **#2 Use a systematic mechanism of learning** — the feedback loop (Feedback Capture → Auto Dataset Mining → Golden Dataset → Offline Eval Runner → Eval Results Dashboard) is the map's backbone. Without it, "continuous improvement" is vibes.
- ⚠ **#10 Know your users** — watch for the *fourth* persona that creeps in: compliance/security reviewers. If your product is regulated (health, finance), add a fourth anchor.
- ⚠ **#13 Manage inertia** — the current "prompts in code comments" practice has three inertia forms actively pushing back: **#8 Skill acquisition cost** (engineers don't want to learn new tooling), **#9 Re-architecture cost** (extracting prompts from code is grunt work), and **#14 Strategic-control loss** (engineers perceive a prompt registry as taking code authority away from them). Plan migration as a staged rollout, not a mandate.
- ⚠ **#17 Use appropriate methods** — resist the temptation to build the **Prompt Registry** in-house just because Git is familiar. Git is the wrong abstraction for non-engineer PMs editing prompts. Use a managed product (Stage III).
- ⚠ **#22 Distribute power and decision-making** — the registry's approval workflow should let PMs and domain experts ship without engineer-in-the-loop for every change. That is the whole point.

### f. Climatic context

- **#3 Everything evolves** — prompt management went from "Jupyter notebook" (Stage I) in 2023 to a crowded vendor market (Stage II→III) in 2024–2026. The category itself is evolving under you.
- **#17 No single method fits all** — prompt-authoring needs differ wildly by persona: engineer (wants Git), PM (wants Notion), ML scientist (wants eval-first). One tool won't serve all three equally.
- **#18 You cannot measure evolution over time or adoption** — the evolve arrows in this map are *scenarios*, not forecasts.
- **#19 Efficiency enables innovation** — commoditising LLM access (gateway) and observability (OTel) frees budget to fund the differentiation work (eval rubrics, dataset curation).
- **#27 Product-to-utility punctuated equilibrium** — LLM Gateway and Prompt Registry categories are both in transition from Stage III Product (+rental) toward Stage IV Commodity (+utility). Expect consolidation, acquisitions (Humanloop → Anthropic, Langfuse → ClickHouse already happened), and price compression within 18–24 months.
- **#15 / #16 / #17 Inertia trio** — see doctrine notes above; inertia to leaving code-comment prompts is real and must be managed.

### g. Deep-placement notes

I ran targeted research on 5 components in this fast-moving space.

1. **Prompt Registry (versioning)** — initial cheat-sheet read put this at ε ≈ 0.45 (late Stage II Custom Built). Vendor-landscape search (2026) found a crowded market: Maxim AI, PromptLayer, Langfuse, LangSmith, Braintrust, Confident AI, ZenML's catalogue list, plus prompts-in-Git workflows (Promptfoo, Confident AI's git-based mode). Category characteristics: "Git-like" is the common metaphor, feature parity is converging, acquisitions are happening. **Shifted to ε = 0.55 (Stage III Product (+rental))** and set an `evolve` target to 0.75, reflecting the visible move toward commodity-like API offerings within 12–24 months.

2. **LLM Gateway / Model Router** — initial read ε ≈ 0.55. 2026 landscape search found: LiteLLM (OSS, widely deployed), Portkey (SaaS enterprise), OpenRouter (SaaS marketplace, 300+ models via 60+ providers), Cloudflare AI Gateway, Kong AI Gateway, Vercel AI Gateway, TrueFoundry. A Q1-2026 consolidation event (Helicone acquired; LiteLLM supply-chain incident referenced) confirms active Stage III → IV transition. **Held at ε = 0.65 now, `evolve` target 0.82** (Stage IV Commodity (+utility) within the horizon) — the pattern matches "utility API" destination.

3. **LLM Observability / Trace Collection** — initial read split: Trace Collection itself is becoming standardised (OpenTelemetry GenAI semantic conventions), but LLM-specific observability platforms (Langfuse, Arize Phoenix, LangSmith, Braintrust, Helicone, TruLens) are still Stage II–III. Phoenix alone has 7,800+ GitHub stars. Langfuse acquired by ClickHouse in 2025, signalling consolidation. **Split the placement:** Trace Collection (spans) at ε = 0.65 (standardising), OpenTelemetry Instrumentation at ε = 0.80 (mature standard), Prompt/Response Logging at ε = 0.70 (product-stage offerings widespread).

4. **LLM-as-Judge Scorers** — initial cheat-sheet read ε ≈ 0.30. 2026 search shows: 50+ "research-backed metrics" libraries (Confident AI, DeepEval, RAGAS, Arize), papers still flowing, vendor offerings differentiating rapidly. Publication type mix ("describing the wonder" + "build guides") indicates Stage II Custom Built with a leading edge into Stage III. **Held at ε = 0.35** with `evolve` target 0.55 — and critically, this justifies BUILD on your *domain-specific rubrics* while BUYING a generic judge-runner library.

5. **Prompt A/B Testing (Feature Flagging / Traffic Split for prompts)** — initial read was conflicted: general-purpose feature flagging is Stage IV (LaunchDarkly, Split, Unleash), but *prompt-aware* traffic splitting is Stage II–III (Langfuse, Braintrust, Traceloop, Dynatrace's recent release all feature this as 2025–2026 capability). **Held at ε = 0.78 for the generic flagging capability** (most of the value can be had from a Stage IV feature-flag service plus a thin adapter), with a warning in the strategic analysis that the prompt-specific A/B semantics (canary, shadow test, cost-per-variant) may require vendor features and may still be volatile.

Components explicitly *not* deep-researched (obvious Stage IV utility): Cloud Compute, Object Storage, Auth/SSO, Event Bus, Secrets Management, Latency monitoring, Rate Limiting.

### h. Caveat

Evolution trajectories in this map (the four `evolve` arrows) are **scenarios, not forecasts**. Wardley's climatic pattern #18: *"you cannot measure evolution over time or adoption."* The prompt-tooling category is moving fast — Humanloop was acquired by Anthropic in late 2024; Langfuse was acquired by ClickHouse in 2025; Helicone was acquired in Q1 2026; LiteLLM had a supply-chain incident in the same quarter. Re-map every 6 months.

---

## Build / Buy / Utility — the decision table

| Bucket | Components | Rationale | Notes / candidates |
|---|---|---|---|
| **BUILD in-house** (Stage I–II, differentiation) | Golden Dataset Curation, Human Review Workflow, LLM-as-Judge Scorers *(your rubrics, not the runner)*, Auto Dataset Mining (from traffic), Production Trace Sampling policy, your domain-specific **Guardrails** rules, the **Prompt Eng. Review Practice** itself, **Eval Methodology Knowledge** | This is your moat. The *labelled data from your users*, *your rubrics*, and *your review process* are the only things a competitor cannot acquire. They compound with every release. | Invest directed engineering here (gameplay #36). Do not outsource these. |
| **BUY SaaS / RENT** (Stage III Product (+rental)) | Prompt Registry (versioning), Prompt Authoring UI, Prompt Playground, Eval Results Dashboard, Experiment Console (A/B results), Offline Eval Runner, Regression Suites (CI), Trace Collection, Prompt/Response Logging, Annotation Tooling, Feature Flagging / Traffic Split, Semantic / Prompt Cache | Crowded vendor market, rapidly converging feature sets, high cost to build equivalently. Pick one end-to-end platform *or* compose two or three. | Candidates: Braintrust, Langfuse (OSS/self-host option), LangSmith (if LangChain-heavy), Maxim AI, PromptLayer, Confident AI, Humanloop (now Anthropic), Traceloop. Feature flags: LaunchDarkly / Split / Unleash / Statsig. |
| **CONSUME as utility API** (Stage IV Commodity (+utility)) | LLM Gateway / Model Router, Frontier LLM APIs, Embedding APIs, Cloud Compute, Object Storage, Auth / SSO, Event Bus / Queue, Data Warehouse, Secrets Management, Latency / Error Monitoring, Rate Limiting and Quotas, OpenTelemetry Instrumentation, PII Redaction on Logs | Pure utility; pay per use; no defensibility in owning these. | Gateway: LiteLLM (OSS) or Portkey / OpenRouter / Cloudflare AI Gateway. Models: Anthropic, OpenAI, Google, plus an open-weight fallback. Warehouse: Snowflake/BigQuery/Databricks. Everything standard. |
| **LEVERAGE as accepted knowledge** | Eval Methodology Knowledge, Prompt Eng. Review Practice | Don't redevelop the literature; hire people who know it. | Standing prompt-review rituals, reading group, one eval scientist on staff. |

### Strategic sequencing (6-quarter plan)

1. **Q1 — Foundation.** Pick and adopt: LLM Gateway (e.g., LiteLLM self-hosted for data control), SaaS prompt-management + observability (Langfuse or Braintrust), OpenTelemetry GenAI instrumentation. Stand up a Golden Dataset v0 (50–200 hand-curated examples per product feature).
2. **Q2 — Evaluation.** Wire CI regression suites against Golden Dataset. Ship LLM-as-Judge scorers (generic + first domain-specific rubric). Start collecting production traces and feedback (thumbs-up/down).
3. **Q3 — A/B in production.** Feature-flag prompt variants to ≤5% traffic. Wire Experiment Console to Data Warehouse. Close the loop: eval metrics on both control and variant, statistical significance, auto-rollback.
4. **Q4 — Feedback flywheel.** Auto Dataset Mining from production traces. Human annotation tooling. Dataset grows continuously from traffic, not one-off curation sprints.
5. **Q5 — Moat deepens.** Domain-specific judge rubrics per product surface. Review workflow with SME routing. This is now your competitive asset.
6. **Q6 — Re-evaluate.** The SaaS vendor market has consolidated; revisit BUY decisions. Sense whether any Stage III BUY items have moved to Stage IV Commodity (+utility) and re-platform if warranted (gameplay #43 Sensing Engines / ILC).

---

## Validator line (Step 5.5)

```
OK: 42 components/anchors, 60 edges — no violations.
```

