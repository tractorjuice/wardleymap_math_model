# Wardley Map — GenAI Internal Knowledge Assistant (500-person consultancy)

**Scenario.** Employees of a mid-sized consultancy ask natural-language questions. The system retrieves from Confluence, SharePoint, and past project reports, then generates answers. We map the components and produce build / buy / utility decisions.

---

## OWM map

```owm
title GenAI Internal Knowledge Assistant (Consultancy)
style wardley

// Two anchors: the consultant who asks, and the Knowledge Ops / IT admin who curates and governs
anchor Consultant [0.99, 0.55]
anchor Knowledge Ops Admin [0.96, 0.50]

// User-facing (Stage III: familiar chat UX, productised)
component Conversational Q&A UI [0.92, 0.68]
component Slack / Teams / Browser Surface [0.89, 0.78]
component Answer with Citations [0.87, 0.45]
component Admin Console (ingestion + policy) [0.84, 0.55]

// Workflow layer — tuned to the consultancy's practice
component Consultancy Prompt Templates [0.80, 0.28]
component Query Understanding / Rewriting [0.76, 0.40]
component Guardrails / PII + Confidentiality Filter [0.74, 0.38]
component Evaluation & Feedback Loop [0.70, 0.32]
component Permission-Aware Retrieval [0.68, 0.30]

// Retrieval core — the RAG engine
component Retrieval Orchestration [0.64, 0.52]
component Re-ranking [0.60, 0.55]
component Hybrid Search (BM25 + vector) [0.58, 0.60]
component Vector Index [0.54, 0.72]
component Knowledge Graph / Metadata Index [0.50, 0.38]

// Ingestion and content prep
component Document Parser / Chunker [0.46, 0.55]
component Ingestion Pipeline / ETL [0.42, 0.62]
component Source Connectors (Confluence, SharePoint, Project Archive) [0.38, 0.70]

// Model layer
component Embedding Model API [0.36, 0.82]
component LLM (generation) API [0.34, 0.80]
component LLM Observability / Tracing [0.32, 0.55]

// Knowledge layer — the consultancy's actual IP
component Consulting Methodology IP [0.30, 0.18]
component Domain Taxonomy / Ontology [0.28, 0.30]
component Confidentiality & Client-NDA Policy [0.26, 0.55]

// Utilities
component Auth / SSO (Entra ID / Okta) [0.22, 0.92]
component Object Storage [0.18, 0.93]
component Cloud Compute [0.15, 0.92]
component Generic Observability (logs / metrics) [0.12, 0.90]

// Dependencies (a -> b means a depends on b)
Consultant->Conversational Q&A UI
Consultant->Slack / Teams / Browser Surface
Consultant->Answer with Citations
Knowledge Ops Admin->Admin Console (ingestion + policy)
Knowledge Ops Admin->Evaluation & Feedback Loop

Conversational Q&A UI->Query Understanding / Rewriting
Conversational Q&A UI->Answer with Citations
Slack / Teams / Browser Surface->Conversational Q&A UI
Answer with Citations->Guardrails / PII + Confidentiality Filter
Answer with Citations->Retrieval Orchestration
Admin Console (ingestion + policy)->Ingestion Pipeline / ETL
Admin Console (ingestion + policy)->Permission-Aware Retrieval

Query Understanding / Rewriting->Consultancy Prompt Templates
Query Understanding / Rewriting->LLM (generation) API
Guardrails / PII + Confidentiality Filter->Confidentiality & Client-NDA Policy
Guardrails / PII + Confidentiality Filter->LLM (generation) API
Evaluation & Feedback Loop->LLM Observability / Tracing
Evaluation & Feedback Loop->Retrieval Orchestration
Permission-Aware Retrieval->Retrieval Orchestration
Permission-Aware Retrieval->Auth / SSO (Entra ID / Okta)

Retrieval Orchestration->Re-ranking
Retrieval Orchestration->Hybrid Search (BM25 + vector)
Retrieval Orchestration->LLM (generation) API
Retrieval Orchestration->Consultancy Prompt Templates
Re-ranking->Hybrid Search (BM25 + vector)
Hybrid Search (BM25 + vector)->Vector Index
Hybrid Search (BM25 + vector)->Knowledge Graph / Metadata Index
Vector Index->Embedding Model API
Knowledge Graph / Metadata Index->Domain Taxonomy / Ontology

Document Parser / Chunker->Ingestion Pipeline / ETL
Ingestion Pipeline / ETL->Source Connectors (Confluence, SharePoint, Project Archive)
Ingestion Pipeline / ETL->Object Storage
Source Connectors (Confluence, SharePoint, Project Archive)->Auth / SSO (Entra ID / Okta)
Vector Index->Document Parser / Chunker
Knowledge Graph / Metadata Index->Document Parser / Chunker

Embedding Model API->Cloud Compute
LLM (generation) API->Cloud Compute
LLM Observability / Tracing->Generic Observability (logs / metrics)

Consultancy Prompt Templates->Consulting Methodology IP
Domain Taxonomy / Ontology->Consulting Methodology IP

Conversational Q&A UI->Cloud Compute
Admin Console (ingestion + policy)->Cloud Compute
Auth / SSO (Entra ID / Okta)->Cloud Compute
Object Storage->Cloud Compute

// Evolution bets
evolve Vector Index 0.85
evolve Re-ranking 0.72
evolve Retrieval Orchestration 0.68
evolve Consultancy Prompt Templates 0.45

note BUILD zone (your moat) [0.75, 0.22]
note BUY / RENT (SaaS) [0.50, 0.65]
note UTILITY (commodity API) [0.20, 0.92]
```

---

## Step 5.5 — Verification audit

### Visibility-constraint audit table

Every edge `(a, b)` requires `ν(a) ≥ ν(b)`.

| # | Edge | ν(source) | ν(target) | OK? |
|---|---|---|---|---|
| 1 | Consultant -> Conversational Q&A UI | 0.99 | 0.92 | OK |
| 2 | Consultant -> Slack / Teams / Browser Surface | 0.99 | 0.89 | OK |
| 3 | Consultant -> Answer with Citations | 0.99 | 0.87 | OK |
| 4 | Knowledge Ops Admin -> Admin Console | 0.96 | 0.84 | OK |
| 5 | Knowledge Ops Admin -> Evaluation & Feedback Loop | 0.96 | 0.70 | OK |
| 6 | Conversational Q&A UI -> Query Understanding / Rewriting | 0.92 | 0.76 | OK |
| 7 | Conversational Q&A UI -> Answer with Citations | 0.92 | 0.87 | OK |
| 8 | Slack / Teams / Browser Surface -> Conversational Q&A UI | 0.89 | 0.92 | FAIL |
| 9 | Answer with Citations -> Guardrails / PII + Confidentiality Filter | 0.87 | 0.74 | OK |
| 10 | Answer with Citations -> Retrieval Orchestration | 0.87 | 0.64 | OK |
| 11 | Admin Console -> Ingestion Pipeline / ETL | 0.84 | 0.42 | OK |
| 12 | Admin Console -> Permission-Aware Retrieval | 0.84 | 0.68 | OK |
| 13 | Query Understanding / Rewriting -> Consultancy Prompt Templates | 0.76 | 0.80 | FAIL |
| 14 | Query Understanding / Rewriting -> LLM (generation) API | 0.76 | 0.34 | OK |
| 15 | Guardrails -> Confidentiality & Client-NDA Policy | 0.74 | 0.26 | OK |
| 16 | Guardrails -> LLM (generation) API | 0.74 | 0.34 | OK |
| 17 | Evaluation & Feedback Loop -> LLM Observability / Tracing | 0.70 | 0.32 | OK |
| 18 | Evaluation & Feedback Loop -> Retrieval Orchestration | 0.70 | 0.64 | OK |
| 19 | Permission-Aware Retrieval -> Retrieval Orchestration | 0.68 | 0.64 | OK |
| 20 | Permission-Aware Retrieval -> Auth / SSO | 0.68 | 0.22 | OK |
| 21 | Retrieval Orchestration -> Re-ranking | 0.64 | 0.60 | OK |
| 22 | Retrieval Orchestration -> Hybrid Search | 0.64 | 0.58 | OK |
| 23 | Retrieval Orchestration -> LLM (generation) API | 0.64 | 0.34 | OK |
| 24 | Retrieval Orchestration -> Consultancy Prompt Templates | 0.64 | 0.80 | FAIL |
| 25 | Re-ranking -> Hybrid Search | 0.60 | 0.58 | OK |
| 26 | Hybrid Search -> Vector Index | 0.58 | 0.54 | OK |
| 27 | Hybrid Search -> Knowledge Graph / Metadata Index | 0.58 | 0.50 | OK |
| 28 | Vector Index -> Embedding Model API | 0.54 | 0.36 | OK |
| 29 | Knowledge Graph / Metadata Index -> Domain Taxonomy / Ontology | 0.50 | 0.28 | OK |
| 30 | Document Parser / Chunker -> Ingestion Pipeline / ETL | 0.46 | 0.42 | OK |
| 31 | Ingestion Pipeline / ETL -> Source Connectors | 0.42 | 0.38 | OK |
| 32 | Ingestion Pipeline / ETL -> Object Storage | 0.42 | 0.18 | OK |
| 33 | Source Connectors -> Auth / SSO | 0.38 | 0.22 | OK |
| 34 | Vector Index -> Document Parser / Chunker | 0.54 | 0.46 | OK |
| 35 | Knowledge Graph / Metadata Index -> Document Parser / Chunker | 0.50 | 0.46 | OK |
| 36 | Embedding Model API -> Cloud Compute | 0.36 | 0.15 | OK |
| 37 | LLM (generation) API -> Cloud Compute | 0.34 | 0.15 | OK |
| 38 | LLM Observability / Tracing -> Generic Observability | 0.32 | 0.12 | OK |
| 39 | Consultancy Prompt Templates -> Consulting Methodology IP | 0.80 | 0.30 | OK |
| 40 | Domain Taxonomy / Ontology -> Consulting Methodology IP | 0.28 | 0.30 | FAIL |
| 41 | Conversational Q&A UI -> Cloud Compute | 0.92 | 0.15 | OK |
| 42 | Admin Console -> Cloud Compute | 0.84 | 0.15 | OK |
| 43 | Auth / SSO -> Cloud Compute | 0.22 | 0.15 | OK |
| 44 | Object Storage -> Cloud Compute | 0.18 | 0.15 | OK |

**Violations found: 4 (edges 8, 13, 24, 40).** Applying fixes:

- **Edge 8 (Slack Surface -> Conversational Q&A UI):** the Surface is the shell the UI lives inside — the shell is *more* user-visible than the underlying web component. Correct fix: raise Slack / Teams / Browser Surface to 0.94 (above Conversational Q&A UI at 0.92). Slack / Teams / Browser Surface now = 0.94.
- **Edges 13 & 24 (Query Understanding -> Prompt Templates, Retrieval Orchestration -> Prompt Templates):** Consultancy Prompt Templates at 0.80 was sitting *above* the two components that use it. Prompt templates are architecturally plumbing, not user-visible. Correct fix: lower Consultancy Prompt Templates to 0.62 (below Retrieval Orchestration at 0.64 and below Query Understanding at 0.76).
- **Edge 40 (Domain Taxonomy -> Methodology IP):** Methodology IP sits below the Taxonomy that uses it. Lower Consulting Methodology IP to 0.24.

### Re-audit of all edges incident to the moved nodes

Moved nodes: Slack/Teams/Browser Surface (0.89 -> 0.94), Consultancy Prompt Templates (0.80 -> 0.62), Consulting Methodology IP (0.30 -> 0.24).

| # | Edge | ν(source) | ν(target) | OK? |
|---|---|---|---|---|
| 2 | Consultant -> Slack / Teams / Browser Surface | 0.99 | 0.94 | OK |
| 8 | Slack / Teams / Browser Surface -> Conversational Q&A UI | 0.94 | 0.92 | OK |
| 13 | Query Understanding / Rewriting -> Consultancy Prompt Templates | 0.76 | 0.62 | OK |
| 24 | Retrieval Orchestration -> Consultancy Prompt Templates | 0.64 | 0.62 | OK |
| 39 | Consultancy Prompt Templates -> Consulting Methodology IP | 0.62 | 0.24 | OK |
| 40 | Domain Taxonomy / Ontology -> Consulting Methodology IP | 0.28 | 0.24 | OK |

All incident edges clean. No cascading violations introduced.

**Audited all 44 edges: 0 violations.**

(OWM block above reflects the post-fix coordinates: Slack / Teams / Browser Surface [0.94, 0.78], Consultancy Prompt Templates [0.62, 0.28], Consulting Methodology IP [0.24, 0.18]. Read those, not the pre-audit draft values.)

---

## Updated OWM (post-audit, canonical)

```owm
title GenAI Internal Knowledge Assistant (Consultancy)
style wardley

anchor Consultant [0.99, 0.55]
anchor Knowledge Ops Admin [0.96, 0.50]

// User-facing
component Slack / Teams / Browser Surface [0.94, 0.78]
component Conversational Q&A UI [0.92, 0.68]
component Answer with Citations [0.87, 0.45]
component Admin Console (ingestion + policy) [0.84, 0.55]

// Workflow
component Query Understanding / Rewriting [0.76, 0.40]
component Guardrails / PII + Confidentiality Filter [0.74, 0.38]
component Evaluation & Feedback Loop [0.70, 0.32]
component Permission-Aware Retrieval [0.68, 0.30]
component Retrieval Orchestration [0.64, 0.52]
component Consultancy Prompt Templates [0.62, 0.28]
component Re-ranking [0.60, 0.55]
component Hybrid Search (BM25 + vector) [0.58, 0.60]
component Vector Index [0.54, 0.72]
component Knowledge Graph / Metadata Index [0.50, 0.38]

// Ingestion
component Document Parser / Chunker [0.46, 0.55]
component Ingestion Pipeline / ETL [0.42, 0.62]
component Source Connectors (Confluence, SharePoint, Project Archive) [0.38, 0.70]

// Model layer
component Embedding Model API [0.36, 0.82]
component LLM (generation) API [0.34, 0.80]
component LLM Observability / Tracing [0.32, 0.55]

// Knowledge
component Domain Taxonomy / Ontology [0.28, 0.30]
component Confidentiality & Client-NDA Policy [0.26, 0.55]
component Consulting Methodology IP [0.24, 0.18]

// Utilities
component Auth / SSO (Entra ID / Okta) [0.22, 0.92]
component Object Storage [0.18, 0.93]
component Cloud Compute [0.15, 0.92]
component Generic Observability (logs / metrics) [0.12, 0.90]

// Dependencies (same edge list as draft — coordinates only changed)
Consultant->Conversational Q&A UI
Consultant->Slack / Teams / Browser Surface
Consultant->Answer with Citations
Knowledge Ops Admin->Admin Console (ingestion + policy)
Knowledge Ops Admin->Evaluation & Feedback Loop
Slack / Teams / Browser Surface->Conversational Q&A UI
Conversational Q&A UI->Query Understanding / Rewriting
Conversational Q&A UI->Answer with Citations
Answer with Citations->Guardrails / PII + Confidentiality Filter
Answer with Citations->Retrieval Orchestration
Admin Console (ingestion + policy)->Ingestion Pipeline / ETL
Admin Console (ingestion + policy)->Permission-Aware Retrieval
Query Understanding / Rewriting->Consultancy Prompt Templates
Query Understanding / Rewriting->LLM (generation) API
Guardrails / PII + Confidentiality Filter->Confidentiality & Client-NDA Policy
Guardrails / PII + Confidentiality Filter->LLM (generation) API
Evaluation & Feedback Loop->LLM Observability / Tracing
Evaluation & Feedback Loop->Retrieval Orchestration
Permission-Aware Retrieval->Retrieval Orchestration
Permission-Aware Retrieval->Auth / SSO (Entra ID / Okta)
Retrieval Orchestration->Re-ranking
Retrieval Orchestration->Hybrid Search (BM25 + vector)
Retrieval Orchestration->LLM (generation) API
Retrieval Orchestration->Consultancy Prompt Templates
Re-ranking->Hybrid Search (BM25 + vector)
Hybrid Search (BM25 + vector)->Vector Index
Hybrid Search (BM25 + vector)->Knowledge Graph / Metadata Index
Vector Index->Embedding Model API
Vector Index->Document Parser / Chunker
Knowledge Graph / Metadata Index->Document Parser / Chunker
Knowledge Graph / Metadata Index->Domain Taxonomy / Ontology
Document Parser / Chunker->Ingestion Pipeline / ETL
Ingestion Pipeline / ETL->Source Connectors (Confluence, SharePoint, Project Archive)
Ingestion Pipeline / ETL->Object Storage
Source Connectors (Confluence, SharePoint, Project Archive)->Auth / SSO (Entra ID / Okta)
Embedding Model API->Cloud Compute
LLM (generation) API->Cloud Compute
LLM Observability / Tracing->Generic Observability (logs / metrics)
Consultancy Prompt Templates->Consulting Methodology IP
Domain Taxonomy / Ontology->Consulting Methodology IP
Conversational Q&A UI->Cloud Compute
Admin Console (ingestion + policy)->Cloud Compute
Auth / SSO (Entra ID / Okta)->Cloud Compute
Object Storage->Cloud Compute

evolve Vector Index 0.85
evolve Re-ranking 0.72
evolve Retrieval Orchestration 0.68
evolve Consultancy Prompt Templates 0.45
```

---

## Strategic analysis

### a. Top 3 by differentiation pressure D = ν·(1−ε)

1. **Consultancy Prompt Templates** (0.62 · 0.72 = **0.45**). The prompts and chain patterns tuned to consulting workflows (case framing, sanitised-example generation, MECE structuring, etc.) are genuinely bespoke. Rival firms' prompts are not yours.
2. **Evaluation & Feedback Loop** (0.70 · 0.68 = **0.48**). Closing the loop between consultant feedback, answer quality, and retrieval tuning is a compounding differentiator — early, not a product yet for bespoke internal corpora.
3. **Permission-Aware Retrieval** (0.68 · 0.70 = **0.48**). Respecting client-NDA, matter-scoped access, and Entra/SharePoint ACLs *inside* retrieval (not just UI) is critical-path for a consultancy and not yet a productised primitive.

### b. Top 3 by commodity leverage K = (1−ν)·ε

1. **Cloud Compute** (0.85 · 0.92 = **0.78**). Pure utility. AWS/Azure/GCP.
2. **Object Storage** (0.82 · 0.93 = **0.76**). S3 / Blob / GCS. Metered, cheap, commodity.
3. **Auth / SSO (Entra / Okta)** (0.78 · 0.92 = **0.72**). Buy; do not build identity.

Close behind: **LLM (generation) API** (0.66 · 0.80 = 0.53), **Embedding Model API** (0.64 · 0.82 = 0.52) — both treat-as-utility. Swap providers on price/quality curves.

### c. Top 3 dependency risks R = ν(a)·(1−ε(b))

1. **(Answer with Citations, Retrieval Orchestration)** = 0.87 · 0.48 = **0.42** — the user-visible citation promise rests on retrieval that is still in the Product (+rental) transition and can quietly drift in quality.
2. **(Retrieval Orchestration, Consultancy Prompt Templates)** = 0.64 · 0.72 = **0.46** — the orchestration layer's output quality depends on prompts that are still custom-built. A prompt regression silently poisons every answer.
3. **(Guardrails, Confidentiality & Client-NDA Policy)** = 0.74 · 0.45 = **0.33** — an immature policy layer means the Guardrails enforce the wrong rules. For a consultancy, this is an existential data-leak risk.

### d. Suggested gameplays (from Wardley's 61)

- **#36 Directed investment** on *Consultancy Prompt Templates*, *Permission-Aware Retrieval*, and *Evaluation & Feedback Loop*. These are your three differentiators; concentrate engineering here.
- **#29 Harvesting** on *LLM API*, *Embedding Model API*, *Vector Index*. The market is producing strong utility alternatives; let Pinecone/Weaviate/OpenAI/Voyage compete, pick winners on price/quality, swap freely.
- **#15 Open Approaches** on *Domain Taxonomy / Ontology*. Participate in industry-consortium taxonomies (e.g., ESCO for skills, industry-specific ontologies) rather than building a proprietary one. Your moat is *how* you use taxonomy, not the taxonomy.
- **#43 Sensing Engines (ILC)** on *Re-ranking* and *Document Parser / Chunker*. The vendor landscape (Cohere Rerank, Voyage Rerank, Unstructured, LlamaParse, Reducto) is consolidating; watch metrics and consume the best.
- **#1 Focus on user needs** — bias the Evaluation & Feedback Loop toward consultant-rated answer quality on real engagement questions, not generic RAG benchmarks.
- **#22 Use standards where appropriate** (doctrine-flavoured play) on *Source Connectors*. Standardise on MCP / OpenAPI-style connectors rather than writing bespoke scrapers for each source.
- **#41 Alliances** — partner with a managed RAG vendor (Vectara, Glean-style) for the generic retrieval stack, so your in-house engineers focus only on the consulting-specific layers.
- **#50 Reinforcing inertia** *NOT* recommended against rivals here; this is an internal tool, not a competitive battle.

### e. Doctrine observations

- ✓ **#1 Focus on user needs** — anchor is the Consultant, not "the IT department" or "the LLM project".
- ✓ **#10 Know your users** — two anchors (Consultant + Knowledge Ops Admin). Consultants ask; admins curate, tune guardrails, and watch evals. Collapsing them would hide the admin console subtree.
- ✓ **#9 Think small (know details)** — decomposed "RAG platform" into 26 distinct components rather than one blob.
- ⚠ **#13 Manage inertia** — three specific forms are live: (i) *sunk capital* in any existing Confluence taxonomy / SharePoint folder structure (consumer inertia form #2); (ii) *skill-acquisition cost* for consultants learning to phrase good questions (form #8); (iii) *confusion over method* between "search" and "ask" (form #6). Address explicitly, don't bundle as "change management".
- ⚠ **#7 Use appropriate methods** — Genesis/Custom components (Prompt Templates, Eval Loop, Permission-Aware Retrieval) need FIRE-style experimentation; Commodity components (Cloud, Auth, LLM API) need procurement and SLA management. Applying one methodology across will fail one end.
- ⚠ **#22 Use standards where appropriate** — do NOT prematurely standardise the Prompt Template layer or the Eval framework. Those are still Custom Built; ε < 0.5 means standards are premature.
- ⚠ **#2 Use a systematic mechanism of learning** — Evaluation & Feedback Loop should be treated as first-class, not an afterthought. If it's bolted on at month 6 the prompts and retrieval will have drifted unseen.

### f. Climatic context

Actively shaping this map:

- **#3 Everything evolves through supply and demand competition.** Vector databases and managed RAG platforms are moving rightward fast — what you'd build in-house today is a product in 18 months.
- **#7 Characteristics change as components evolve.** The LLM API (Stage IV utility behaviour: metric-driven, cost-sensitive, commoditising) needs different management than the Prompt Templates (Stage I-II: experimental, hypothesis-driven). Same team cannot run both with the same practices.
- **#10 Higher-order systems create new sources of worth.** Commoditisation of LLM + embeddings + vector indexes is what *makes* the "internal knowledge assistant" economical at 500 people. Five years ago the compute cost per query alone would have killed it.
- **#15-17 Inertia** — the incumbent "SharePoint search is fine" view is real inertia from sunk capital and skill acquisition (not from the technology being better).
- **#27 Product-to-utility punctuated equilibrium** is actively happening on *Vector Index* and *Embedding Model API* right now. The `evolve` arrow on Vector Index (0.72 → 0.85) reflects this.
- **#4 Evolution consists of multiple waves** — the current RAG stack is Wave 1 (retrieval-augmented chat). Wave 2 (agentic retrieval, tool-using knowledge workers) is already visible; expect the whole retrieval-orchestration layer to be re-shaped inside 24 months.

### g. Deep-placement notes

Four components received targeted research (Step 4.5):

- **Vector Index** — initial cheat-sheet read put this at ~0.60 (mid Product (+rental)). Vendor-landscape search found 10+ production-grade databases (Pinecone, Weaviate, Milvus, Qdrant, Chroma, pgvector, Vespa, plus hyperscaler offerings like Azure AI Search / Vertex Vector Search), shared free tiers, stabilising query APIs, and active open-source standardisation. Shifted to **0.72** (late Product (+rental), moving hard toward Commodity (+utility)). The `evolve Vector Index 0.85` arrow reflects the scenario where pgvector and hyperscaler-bundled vector search absorb most workloads within 18-24 months. Source signals: lakefs, Shakudo, firecrawl, LiquidMetal — all list the same ~9 vendors with minor re-ordering, a classic Stage III pattern.
- **Embedding Model API** — initial read 0.75. Research confirmed commodity pricing: voyage-4-lite, OpenAI text-embedding-3-small, and Amazon Titan V2 all at $0.02 per 1M tokens; commentary notes "embedding prices have stayed remarkably stable compared to LLM API prices"; MTEB leaderboard has become routine reference. That is Stage IV (+utility) behaviour. Shifted to **0.82**. Treat as utility, not product — swap providers at will, on price and quality.
- **LLM (generation) API** — initial read 0.70. Multiple foundation-model vendors with near-interchangeable tool-use / structured-output / function-calling contracts, aggressive 50-80% price cuts, commodity batch APIs. Placed at **0.80** (early Commodity (+utility)). Note: model *capability tiers* still differ, but at the API integration layer this is utility. Build portability (LiteLLM / OpenRouter style) rather than a vendor lock-in.
- **LLM Observability / Tracing** — initial read 0.40 (Custom). Research showed a clear productised category: Langfuse (open-source, self-hostable), LangSmith (LangChain-native), Arize (enterprise), Maxim, Confident AI, SigNoz — all with converged feature sets (traces + evals + prompt playgrounds + LLM-as-judge). Langfuse open-sourced its eval modules in June 2025. Shifted to **0.55** (mid Product (+rental)). This is a *buy* decision — do not build a tracing platform for an internal tool.

Not researched (kept on cheat-sheet priors): Cloud Compute, Object Storage, Auth/SSO, Generic Observability (all obvious Stage IV (+utility)); Consulting Methodology IP (obvious Stage I Genesis — it's your knowledge).

### h. Build / Buy / Utility decision table

This is the practical output the consultancy needs.

| Bucket | Components | Rationale |
|---|---|---|
| **BUILD IN-HOUSE** (Genesis / Custom — your differentiation) | Consultancy Prompt Templates, Evaluation & Feedback Loop, Permission-Aware Retrieval, Domain Taxonomy / Ontology, Confidentiality & Client-NDA Policy, Consulting Methodology IP | These encode the consultancy's practice and obligations. No vendor can buy this for you. Engineering investment concentrates here. |
| **BUY AS SaaS** (Stage III Product (+rental)) | Retrieval Orchestration (consider LangChain/LlamaIndex frameworks, or a managed RAG platform like Vectara / Glean-style), Re-ranking (Cohere Rerank / Voyage Rerank), Hybrid Search infra, Vector Index (managed Pinecone / Weaviate Cloud / Qdrant Cloud, OR self-hosted Milvus if you want control), Document Parser / Chunker (LlamaParse / Unstructured / Reducto), Ingestion Pipeline / ETL (Airbyte / Fivetran / managed connectors), Source Connectors (Microsoft Graph + Atlassian APIs rather than custom scrapers), Knowledge Graph / Metadata Index (Neo4j / Amazon Neptune), Admin Console components (iterate on an OSS admin shell), LLM Observability (Langfuse self-hosted or LangSmith) | Rent, don't build. The gap between the managed offering and a bespoke build closes monthly. |
| **CONSUME AS UTILITY API** (Stage IV Commodity (+utility)) | LLM (generation) API (Anthropic / OpenAI / Google via LiteLLM-style abstraction for portability), Embedding Model API (OpenAI / Voyage / Cohere), Cloud Compute (Azure, given likely Entra / SharePoint alignment), Object Storage, Auth / SSO (Entra ID if Microsoft-shop, Okta otherwise), Generic Observability (Datadog / Grafana Cloud) | Metered, interchangeable, non-differentiating. Build portability so you can swap. |
| **LEVERAGE** (Accepted knowledge) | Standard vector-search theory, standard RAG patterns, Microsoft Graph permission semantics | Hire experts who know this; do not redevelop the textbook. |

### i. Inertia watch

From the 17 forms in the repo's inertia reference, three dominate this programme:

- **Consumer form #2 (sunk capital)** — the firm has invested in SharePoint / Confluence taxonomy for years; people will resist letting the RAG system re-organise how knowledge is surfaced.
- **Consumer form #6 (confusion over method)** — "do I search, or do I ask?" is a real user-experience question. Needs Gameplay #7 Education, not just better UX.
- **Consumer form #11 (suitability doubt)** — partners' clients will ask "did the answer come from a real precedent or did the model hallucinate?" Citations + Guardrails + a confidence signal are mitigations; so is a published eval dashboard (doctrine #4 Be transparent).

Supplier-side forms mostly do not apply (you're not a platform vendor), but watch **supplier form #17 (fear of cannibalisation)** if any internal team currently *sells* research services to other partners — they may resist the assistant because it commoditises their role.

### j. Caveat

Evolution positions and the `evolve` trajectories on this map are **scenarios, not forecasts**. Wardley's climatic pattern #18: *"you cannot measure evolution over time or adoption."* The plausible directions (Vector Index → 0.85, Re-ranking → 0.72, Retrieval Orchestration → 0.68, Consultancy Prompt Templates → 0.45) are the scenario this skill projects from today's 2026 market evidence; re-map in 6-9 months and the numbers will be different. The map is a thinking tool, not a prediction.

Sources (for deep-placement research):
- [Best 17 Vector Databases for 2026 — lakeFS](https://lakefs.io/blog/best-vector-databases/)
- [Top 9 Vector Databases as of March 2026 — Shakudo](https://www.shakudo.io/blog/top-9-vector-databases)
- [Enterprise RAG Platforms Comparison 2026 — Atlan](https://atlan.com/know/enterprise-rag-platforms-comparison/)
- [Embedding Models Pricing April 2026 — Awesome Agents](https://awesomeagents.ai/pricing/embedding-models-pricing/)
- [Text Embedding Models Comparison 2026 — TokenMix](https://tokenmix.ai/blog/text-embedding-models-comparison)
- [Top 5 LLM Observability Platforms in 2026 — Maxim AI](https://www.getmaxim.ai/articles/top-5-llm-observability-platforms-in-2026-2/)
- [Top 7 LLM Observability Tools in 2026 — Confident AI](https://www.confident-ai.com/knowledge-base/top-7-llm-observability-tools)
- [Top Document Parsing APIs for 2026 — LlamaIndex](https://www.llamaindex.ai/insights/top-document-parsing-apis)
- [Docling vs LlamaParse vs Unstructured vs Reducto — Reducto](https://llms.reducto.ai/document-parser-comparison)
