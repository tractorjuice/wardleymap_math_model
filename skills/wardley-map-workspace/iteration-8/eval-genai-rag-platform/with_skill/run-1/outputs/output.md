# Wardley Map — GenAI Internal Knowledge Assistant (500-person Consultancy)

**Scenario.** Employees across a 500-person consultancy ask questions in natural language. The system retrieves answers from Confluence, SharePoint, and past project reports, then generates grounded responses with citations. The brief asks: *map the components and tell us what to build in-house, buy as SaaS, or consume as a utility API.*

Two anchors are used: **Employee (Consultant)** — the day-to-day user — and **Knowledge Ops / Admin** — who configures sources, permissions, and audits. This matches doctrine #10 ("Know your users") for a system with meaningfully distinct roles.

---

## Map (OWM)

```owm
title GenAI Internal Knowledge Assistant (500-person Consultancy)
style wardley

// Two anchors: end-user employees + an internal admin/ops persona
anchor Employee (Consultant) [0.98, 0.55]
anchor Knowledge Ops / Admin [0.92, 0.50]

// User-facing layer
component Natural Language Q&A UI [0.90, 0.62]
component Chat / Conversation History [0.85, 0.70]
component Answer with Context [0.82, 0.45]
component Citations & Source Links [0.80, 0.55]
component Admin / Governance Console [0.78, 0.55]
component Feedback & Thumbs-up/down [0.72, 0.60]

// Application / orchestration layer
component RAG Orchestration (LangChain-style) [0.68, 0.60]
component Prompt Templates & Guardrails [0.65, 0.50]
component Query Rewriting / Expansion [0.60, 0.45]
component Re-ranking [0.58, 0.55]
component Hybrid Retrieval (BM25 + Vector) [0.56, 0.60]
component Hallucination / Grounding Check [0.55, 0.30]
component Permission-aware Filter (ACL mirror) [0.54, 0.35]
component Agentic Tool Use (optional) [0.52, 0.25]

// Retrieval and indexing
component Vector Database [0.48, 0.72]
component Keyword / Lexical Index [0.46, 0.88]
component LLM Inference API [0.45, 0.88]
component Evaluation Practice (LLM-as-judge) [0.46, 0.35]
component Chunking & Indexing Pipeline [0.42, 0.55]
component Embedding Models API [0.40, 0.85]
component PII / Secret Redaction [0.40, 0.50]
component Document Parsers (PDF/Office) [0.38, 0.80]
component LLM Output Caching [0.36, 0.70]

// Data sources (connectors)
component Confluence Connector [0.44, 0.72]
component SharePoint Connector [0.44, 0.72]
component Project Reports Ingestion [0.44, 0.45]
component Change Data Capture / Sync [0.43, 0.55]

// Security / compliance (cross-cutting, deeper)
component SSO / Identity [0.32, 0.92]
component Audit Log [0.30, 0.75]
component Secrets Manager [0.16, 0.90]

// Knowledge & practice (left-edge)
component Prompt Engineering Practice [0.25, 0.45]
component Firm-specific Terminology & Taxonomy [0.22, 0.20]
component Consultancy Methodology Knowledge [0.20, 0.15]

// Infrastructure utilities
component Observability / Tracing [0.18, 0.78]
component Object Storage [0.15, 0.92]
component Cloud Compute [0.12, 0.92]

// Dependencies
Employee (Consultant)->Natural Language Q&A UI
Employee (Consultant)->Answer with Context
Employee (Consultant)->Citations & Source Links
Employee (Consultant)->Chat / Conversation History
Employee (Consultant)->Feedback & Thumbs-up/down
Knowledge Ops / Admin->Admin / Governance Console
Knowledge Ops / Admin->Audit Log

Natural Language Q&A UI->RAG Orchestration (LangChain-style)
Natural Language Q&A UI->Chat / Conversation History
Answer with Context->Citations & Source Links
Answer with Context->RAG Orchestration (LangChain-style)
Citations & Source Links->Hybrid Retrieval (BM25 + Vector)
Admin / Governance Console->Audit Log
Admin / Governance Console->Permission-aware Filter (ACL mirror)
Feedback & Thumbs-up/down->Evaluation Practice (LLM-as-judge)

RAG Orchestration (LangChain-style)->Prompt Templates & Guardrails
RAG Orchestration (LangChain-style)->Query Rewriting / Expansion
RAG Orchestration (LangChain-style)->Hybrid Retrieval (BM25 + Vector)
RAG Orchestration (LangChain-style)->Re-ranking
RAG Orchestration (LangChain-style)->LLM Inference API
RAG Orchestration (LangChain-style)->Hallucination / Grounding Check
RAG Orchestration (LangChain-style)->Agentic Tool Use (optional)
RAG Orchestration (LangChain-style)->LLM Output Caching
Prompt Templates & Guardrails->Prompt Engineering Practice
Prompt Templates & Guardrails->Firm-specific Terminology & Taxonomy
Query Rewriting / Expansion->LLM Inference API
Re-ranking->LLM Inference API
Hallucination / Grounding Check->LLM Inference API

Hybrid Retrieval (BM25 + Vector)->Vector Database
Hybrid Retrieval (BM25 + Vector)->Keyword / Lexical Index
Hybrid Retrieval (BM25 + Vector)->Permission-aware Filter (ACL mirror)
Vector Database->Chunking & Indexing Pipeline
Keyword / Lexical Index->Chunking & Indexing Pipeline
Chunking & Indexing Pipeline->Embedding Models API
Chunking & Indexing Pipeline->Document Parsers (PDF/Office)
Chunking & Indexing Pipeline->PII / Secret Redaction
Chunking & Indexing Pipeline->Object Storage

Document Parsers (PDF/Office)->Object Storage
Embedding Models API->Cloud Compute
LLM Inference API->Cloud Compute
LLM Output Caching->Cloud Compute

Permission-aware Filter (ACL mirror)->SSO / Identity
Permission-aware Filter (ACL mirror)->Confluence Connector
Permission-aware Filter (ACL mirror)->SharePoint Connector
PII / Secret Redaction->Secrets Manager

Confluence Connector->Change Data Capture / Sync
SharePoint Connector->Change Data Capture / Sync
Project Reports Ingestion->Change Data Capture / Sync
Change Data Capture / Sync->Object Storage
Change Data Capture / Sync->Chunking & Indexing Pipeline

Evaluation Practice (LLM-as-judge)->LLM Inference API
Evaluation Practice (LLM-as-judge)->Consultancy Methodology Knowledge
Agentic Tool Use (optional)->LLM Inference API

Natural Language Q&A UI->SSO / Identity
Audit Log->Object Storage
Observability / Tracing->Cloud Compute

evolve Vector Database 0.85
evolve RAG Orchestration (LangChain-style) 0.75
evolve Hallucination / Grounding Check 0.55
evolve Permission-aware Filter (ACL mirror) 0.60

note BUILD zone (differentiation) [0.55, 0.20]
note BUY / RENT (Stage III) [0.45, 0.65]
note UTILITY / CONSUME (Stage IV) [0.15, 0.92]
```

---

## Strategic Analysis

### a. Top 3 by differentiation pressure D = ν · (1 − ε)

Reminder: D is a skill-defined heuristic, not a canonical Wardley concept — treat as attention prompt.

1. **Answer with Context** — D = 0.82 × 0.55 = **0.451**. This is the actual user-facing payload (grounded answer + context). It is Stage II–III because "good" answers for a consultancy (nuanced, methodology-aware, citeable) are not yet a solved problem off-the-shelf — the look-and-feel of the answer is where your product is judged.
2. **Agentic Tool Use (optional)** — D = 0.52 × 0.75 = **0.390**. Clearly Genesis / Custom Built for internal-knowledge use — letting the assistant take actions (create a Jira ticket, summarise into a deck) rather than just answer. If it works, it is an adoption multiplier. If it is half-baked, it is a liability.
3. **Hallucination / Grounding Check** — D = 0.55 × 0.70 = **0.385**. Stage II (Custom Built). Open-source and vendor tooling exists (Ragas, TruLens, NeMo Guardrails) but nothing is at Stage III yet for the consultancy case where "grounded in *our* methodology docs" is the bar. A defensible internal evaluator is a real moat.

Honourable mention: **Permission-aware Filter (ACL mirror)** at D = 0.54 × 0.65 = 0.351 — see also in risks (c) below; it is both a differentiator and a risk concentrator.

### b. Top 3 by commodity leverage K = (1 − ν) · ε

Reminder: K is a skill-defined heuristic — flags "consume as utility" candidates.

1. **Cloud Compute** — K = 0.88 × 0.92 = **0.810**. Pure utility. AWS / Azure / GCP.
2. **Object Storage** — K = 0.85 × 0.92 = **0.782**. Utility. S3 / Blob / GCS.
3. **Secrets Manager** — K = 0.84 × 0.90 = **0.756**. Consume the cloud provider's offering.

The more interesting Stage IV (Commodity +utility) calls for this domain — already effectively utilities but worth calling out because they were not in 2023:

- **LLM Inference API** — K = 0.55 × 0.88 = 0.484. Pricing collapsed ~10–100x since 2023 across OpenAI/Anthropic/Gemini/DeepSeek; at-or-near-utility.
- **Embedding Models API** — K = 0.60 × 0.85 = 0.510. Three providers tied at $0.02/MTok; benchmarks converging.
- **SSO / Identity** — K = 0.68 × 0.92 = 0.626. Okta / Entra ID / Auth0.

### c. Top 3 dependency risks R = ν(a) · (1 − ε(b))

1. **(RAG Orchestration → Agentic Tool Use)** — R = 0.68 × 0.75 = **0.510**. A visible orchestrator calling into a Genesis-stage capability. If you ship "the assistant can do things for you" before agent behaviour is safe, failures are user-visible and damage trust. Mitigation: keep agentic features behind a feature flag, scope tightly.
2. **(Admin / Governance Console → Permission-aware Filter)** — R = 0.78 × 0.65 = **0.507**. Admins depend on the filter to mirror Confluence/SharePoint ACLs correctly; ACL-mirroring at scale is not a solved problem (this is the single most common failure mode in enterprise RAG — leaking cross-permission data). Admins need governance that is only as good as the filter.
3. **(RAG Orchestration → Hallucination / Grounding Check)** — R = 0.68 × 0.70 = **0.476**. The orchestrator trusts an immature guardrail to decide what is safe to emit. Classic fragile-foundation pattern.

### d. Suggested gameplays (Wardley's 61-play catalogue)

- **#1 Focus on user needs** — the two anchors (Employee + Knowledge Ops) must both be served. Most internal-assistant projects over-optimise for the employee experience and under-invest in governance; that is where they die politically.
- **#36 Directed investment** on **Answer with Context**, **Hallucination / Grounding Check**, and **Permission-aware Filter (ACL mirror)** — the three components that carry the product's credibility. Put your engineering effort here, not on infrastructure or orchestration scaffolding.
- **#29 Harvesting** on **RAG Orchestration (LangChain-style)**, **Vector Database**, **Embedding Models API**, **LLM Inference API** — these markets are consolidating; let vendors bake off, adopt the winners. Your moat is not here.
- **#15 Open Approaches** on **Evaluation Practice (LLM-as-judge)** — publishing the firm's eval rubric externally (sanitised) buys credibility with partners and clients and costs you nothing; the rubric is not the moat, the grounded answers are.
- **#43 Sensing Engines (ILC)** on new entrants in the enterprise-RAG category (Glean, Vectara, Ragie, GoSearch, Atlan). Route a fraction of traffic to a managed vendor and compare; harvest wherever a vendor objectively beats your in-house build.
- **#41 Alliances** on **Confluence Connector** / **SharePoint Connector** — prefer a multi-source connector provider (Unstructured.io, LlamaHub connectors, or a BYO-Glean posture) over writing one-off connectors per source. Connectors are a tarpit of edge cases.
- **#34 Procrastination** on **Agentic Tool Use** — the market has not stabilised, deadlines for "agentic" features are founder-LinkedIn noise, and the reputational risk of a bad autonomous action dwarfs the feature value. Wait six months, revisit.
- **#7 Education** on **Prompt Engineering Practice** and **Evaluation Practice** — internal enablement lowers consumer-side inertia (form #6 confusion over method, form #8 skill acquisition) and is cheap.
- **#44 Tower and Moat** on **Firm-specific Terminology & Taxonomy** + **Consultancy Methodology Knowledge** — these are the components no generic SaaS can ship, and they are what makes your assistant answer like *your* firm rather than like ChatGPT.

### e. Doctrine notes (violations and watches)

- ✓ **#1 Focus on user needs** — two anchors explicitly identified.
- ✓ **#10 Know your users** — Employee and Knowledge Ops roles surfaced separately; their needs diverge (Employee wants fast answers; Admin wants auditable permissions).
- ⚠ **#2 Use a systematic mechanism of learning** — the **Feedback & Thumbs-up/down → Evaluation Practice** loop is drawn but must actually feed back into Prompt Templates and retrieval tuning. Most RAG projects build the button and never close the loop. Budget time for it.
- ⚠ **#13 Manage inertia** — expect resistance on three fronts: (inertia form #8) consultants' skill-acquisition cost of trusting a new tool over Google+Confluence; (form #9) re-architecture cost if you later need to swap Vector DB; (form #14) strategic-control loss fears from partners worried about IP leakage to a foundation-model provider. Address the third with procurement contracts and a "no training on our data" clause.
- ⚠ **#15 Use appropriate methods** — different evolution stages need different methods. Agile / pioneering for **Answer with Context** and **Hallucination Check**; product-management / settler cadence for **RAG Orchestration**; operations / town-planner cadence for **Cloud Compute** and **Vector Database**. Avoid one team running all of it in the same weekly sprint.
- ⚠ **#19 Think small (as in know the details)** — "connectors" hides a lot. Confluence and SharePoint ACLs have idiosyncratic rules (site vs space permissions, inherited permissions, group expansion) that a generic connector will fumble. Do not hand-wave this.

### f. Climatic context — which patterns are shaping this map

- **#3 Everything evolves through supply and demand competition** — LLM APIs, embeddings, and vector DBs have all moved from Genesis (2022) through Custom/Product and are now, for general use, near-commodity. Planning on today's prices is safe; planning on today's *vendor landscape* is not.
- **#7 Characteristics change as components evolve** — applies to **Vector Database**: in 2023 it was a specialist Genesis-like purchase; in 2026 pgvector-in-Postgres is a perfectly reasonable default for a 500-person firm. Treat it as boring.
- **#10 Higher-order systems create new sources of worth** — commoditisation of LLM + embedding + vector search is *why* an internal-knowledge assistant is economic at your firm's size now. Your build decision is a direct child of this pattern.
- **#11 Future value is inversely proportional to certainty** — the components you should engineer are the *uncertain* ones (grounded answers, ACL-safe retrieval, agentic behaviour), not the certain ones (compute, storage, auth).
- **#15–17 Inertia triad** — see doctrine #13 notes above.
- **#18 You cannot measure evolution over time or adoption** — any "our vector DB will be fully commoditised by Q3 2027" projection is a scenario, not a forecast. See caveat (h).
- **#27 Product-to-utility punctuated equilibrium** — the LLM inference market is mid-transition from Product (+rental) to Commodity (+utility), with the shift punctuated by each pricing-war round. Expect another step-down within 12 months.

### g. Deep-placement notes — what targeted research actually changed

Four components were flagged for deep placement (cheat-sheet rows disagreed, or the placement carried high strategic weight):

- **Vector Database** — initial cheat-sheet placement ~0.55 (mid-Product). Vendor-landscape search showed Pinecone ~70% managed share, pgvector near-ubiquity in PostgreSQL deployments, Qdrant + Weaviate + Milvus + Chroma as well-funded alternatives, and migration playbooks (Pinecone → self-hosted Qdrant) becoming standard practice. This is Stage III-leaning-IV. Shifted to **ε = 0.72**. *Finding:* do not build a vector DB; rent managed for < 50M vectors, self-host once bigger.
- **LLM Inference API** — initial cheat-sheet ~0.78. Research confirmed Stage IV: flagship-model prices down ~10–100x since 2023 (Opus dropped 67% last year); 300+ models compared across providers; RAG-document pipelines now effectively tied across vendors on price and caching. Held at **ε = 0.88** and treat as utility. *Finding:* multi-provider abstraction (via LiteLLM / OpenRouter) is now cheap insurance — commoditisation is real but vendor lock-in remains avoidable.
- **Embedding Models API** — initial ~0.72. Research showed three vendors (Voyage, OpenAI, Amazon Titan) tied at $0.02/MTok, Voyage 4 MoE setting new benchmarks (Jan 2026), Gemini Embedding 2 adding multimodal. Competition has shifted from cost to capability. Moved up to **ε = 0.85**. *Finding:* consume as utility; hedge on Voyage for quality + a cheap default for volume.
- **Enterprise RAG (the whole orchestration layer / "RAG Orchestration")** — initial ~0.50. Research showed an explicit "managed RAG-as-a-service" category (Vectara, Ragie), full-stack internal-assistant SaaS (Glean, GoSearch, Atlan), and the big clouds' zero-ops offerings (Azure AI Search, AWS Bedrock Knowledge Bases, Vertex AI Search). Orchestration-as-a-service is Stage III, with a real question of whether a 500-person firm should skip the in-house orchestration and adopt Glean-or-equivalent end-to-end. Shifted to **ε = 0.60** and marked `evolve 0.75` — expect further consolidation. *Finding:* at 500-person scale, the "buy a Glean-class product" path deserves a 2-week bake-off against the in-house build.

One validator-line summary of the final map:

```
OK: 38 components/anchors, 56 edges — no violations.
```

### h. Caveat

Evolution trajectories on this map (the `evolve` arrows on Vector Database, RAG Orchestration, Hallucination Check, and Permission-aware Filter) are **scenarios, not forecasts**. Wardley's climatic pattern #18: *"you cannot measure evolution over time or adoption."* The rate of movement depends on competitor behaviour, regulation, and aggregate demand that you do not control. Re-map this system every 6 months — the vector-DB and LLM-inference positions in particular will move.

---

## Build / Buy / Utility summary

The brief asks explicitly for the three-bucket decision. Here it is, with each component placed by its evolution stage:

| Decision | Components | Why |
|---|---|---|
| **BUILD in-house** (Stages I–II, high D) | Answer with Context; Hallucination / Grounding Check; Permission-aware Filter (ACL mirror); Firm-specific Terminology & Taxonomy; Consultancy Methodology Knowledge; Evaluation Practice (LLM-as-judge); Prompt Templates & Guardrails; Admin / Governance Console | These are either genuinely novel for your firm (grounded answers tuned to consultancy methodology, ACL-correct retrieval) or are the pieces that carry your identity and cannot be outsourced. |
| **BUY as SaaS / rent** (Stage III — Product +rental) | RAG Orchestration framework (LangChain / LlamaIndex / Haystack or managed Vectara/Ragie); Vector Database (Pinecone managed, Qdrant Cloud, or pgvector if you are already Postgres-heavy); Document Parsers (Unstructured.io, Azure Document Intelligence); PII/Secret Redaction (Presidio, Nightfall); Connectors (Glean / Unstructured.io / LlamaHub); Observability for LLMs (LangSmith, Arize, Langfuse); Chat / Conversation History (framework feature) | These are active, competitive markets with clear leaders. Owning them costs engineering time that yields no moat. |
| **CONSUME as utility API** (Stage IV — Commodity +utility) | LLM Inference API (multi-provider via OpenRouter / LiteLLM); Embedding Models API (Voyage / OpenAI / Titan); Cloud Compute; Object Storage; SSO / Identity; Secrets Manager; Keyword / Lexical Index (Elasticsearch / OpenSearch managed); LLM Output Caching (provider-native) | Utility pricing, multiple interchangeable providers. Do not engineer. |
| **LEVERAGE (knowledge)** | Consultancy Methodology Knowledge; Firm-specific Terminology & Taxonomy; Prompt Engineering Practice | Hire domain experts, capture in knowledge components, refresh with #42 Co-creation and #43 Sensing Engines. Not code. |

A sharper meta-call: if you are a 500-person consultancy with modest engineering bench, **seriously evaluate "buy Glean-class end-to-end"** against building. Your moat is the answers, not the plumbing. Use #43 Sensing Engines (ILC) — a short paid pilot of one enterprise RAG SaaS vs an in-house baseline — before committing. The pieces where you *must* keep in-house IP regardless (Hallucination Check tuned to your methodology, Answer with Context style, Permission-aware Filter correctness, Evaluation Practice) can sit on top of either substrate.

---

## Sources used in deep placement

- [Best Vector Databases in 2026 (Firecrawl)](https://www.firecrawl.dev/blog/best-vector-databases)
- [Pinecone vs Weaviate vs Qdrant vs pgvector — Core Systems 2026](https://core.cz/en/blog/2026/vector-databases-2026/)
- [Vector Database Market Size & Share 2026–2035 (Fundamental Business Insights)](https://www.fundamentalbusinessinsights.com/industry-report/vector-database-market-13287)
- [Enterprise RAG Platforms Comparison 2026 (Atlan)](https://atlan.com/know/enterprise-rag-platforms-comparison/)
- [Glean: Best RAG features in enterprise search](https://www.glean.com/perspectives/best-rag-features-in-enterprise-search)
- [Top 5 RAG Frameworks and Tools for Enterprise AI in 2026 (Second Talent)](https://www.secondtalent.com/resources/top-rag-frameworks-and-tools-for-enterprise-ai-applications/)
- [LLM API Pricing 2026 (PE Collective)](https://pecollective.com/blog/llm-pricing-comparison-2026/)
- [OpenAI vs Anthropic API Pricing Comparison 2026 (Finout)](https://www.finout.io/blog/openai-vs-anthropic-api-pricing-comparison)
- [Voyage 3.5 vs OpenAI vs Cohere Embedding Models 2026 (BuildMVPFast)](https://www.buildmvpfast.com/blog/best-embedding-model-comparison-voyage-openai-cohere-2026)
- [Embedding Models Pricing April 2026 (Awesome Agents)](https://awesomeagents.ai/pricing/embedding-models-pricing/)
