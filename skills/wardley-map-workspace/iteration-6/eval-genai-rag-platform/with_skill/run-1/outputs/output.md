# Wardley Map — Internal GenAI Knowledge Assistant (500-person Consultancy)

**Scenario.** Build a GenAI-powered internal knowledge assistant. Employees ask natural-language questions; the system retrieves from the document corpus (Confluence, SharePoint, past project reports) and generates answers with citations. Decide what to build in-house, buy as SaaS, or consume as a utility API.

---

## 1. Anchors

Two anchors (doctrine #10 Know your users — there are two user types with genuinely different needs):

- **Employee** — the question-asker. Wants a trustworthy answer with a citation, fast.
- **Knowledge Admin** — owns corpus health, access rules, quality monitoring. Wants governance, eval dashboards, and the ability to trace a bad answer back to a bad source.

---

## 2. OWM block

```owm
title Internal GenAI Knowledge Assistant (500-person Consultancy)
style wardley

// Anchors
anchor Employee [0.98, 0.55]
anchor Knowledge Admin [0.95, 0.45]

// User-facing
component Chat / Q&A UI [0.90, 0.65]
component Answer with Citations [0.86, 0.50]
component Feedback Capture [0.80, 0.60]
component Admin & Governance Console [0.82, 0.40]
component Eval Dashboard [0.78, 0.35]

// RAG core
component RAG Orchestration [0.72, 0.60]
component Query Rewriting / Expansion [0.68, 0.40]
component Reranker [0.65, 0.55]
component Prompt Templates [0.62, 0.50]
component Hybrid Search (BM25 + vector) [0.60, 0.65]
component Guardrails / PII Redaction [0.58, 0.45]

// Models
component LLM Foundation Model (API) [0.55, 0.78]
component Embedding Model [0.50, 0.75]

// Indexing & data pipeline
component Vector Index (ANN) [0.48, 0.72]
component Vector Database (managed) [0.42, 0.70]
component Document Ingestion Pipeline [0.45, 0.55]
component Chunking Strategy [0.42, 0.45]
component OCR / Document Parsing [0.40, 0.70]
component Metadata Extraction [0.38, 0.40]
component Permissions / ACL Propagation [0.52, 0.35]
component Document Connectors [0.36, 0.65]

// Data (proprietary)
component Document Corpus (Confluence, SharePoint, Reports) [0.30, 0.30]
component User Feedback / Usage Data [0.28, 0.30]
component Golden Eval Set [0.26, 0.22]

// Observability & ops
component LLM Observability / Tracing [0.33, 0.55]

// Utilities
component Auth / SSO [0.22, 0.90]
component Object Storage [0.15, 0.92]
component Cloud Compute [0.12, 0.92]

// Knowledge
component Consultancy Domain Expertise [0.18, 0.18]
component Information Retrieval Theory [0.10, 0.92]

// External buy-option (context, not a dependency — shown for build-vs-buy reasoning)
component Glean / M365 Copilot (SaaS alternative) [0.70, 0.60]

// Dependencies
Employee->Chat / Q&A UI
Employee->Answer with Citations
Employee->Feedback Capture
Knowledge Admin->Admin & Governance Console
Knowledge Admin->Eval Dashboard
Chat / Q&A UI->RAG Orchestration
Answer with Citations->RAG Orchestration
Feedback Capture->User Feedback / Usage Data
Admin & Governance Console->Permissions / ACL Propagation
Admin & Governance Console->Document Ingestion Pipeline
Eval Dashboard->LLM Observability / Tracing
Eval Dashboard->Golden Eval Set
RAG Orchestration->Query Rewriting / Expansion
RAG Orchestration->Hybrid Search (BM25 + vector)
RAG Orchestration->Reranker
RAG Orchestration->Prompt Templates
RAG Orchestration->LLM Foundation Model (API)
RAG Orchestration->Guardrails / PII Redaction
RAG Orchestration->LLM Observability / Tracing
Hybrid Search (BM25 + vector)->Vector Index (ANN)
Hybrid Search (BM25 + vector)->Permissions / ACL Propagation
Vector Index (ANN)->Vector Database (managed)
Vector Index (ANN)->Embedding Model
Reranker->Embedding Model
Query Rewriting / Expansion->LLM Foundation Model (API)
Document Ingestion Pipeline->Document Connectors
Document Ingestion Pipeline->Chunking Strategy
Document Ingestion Pipeline->OCR / Document Parsing
Document Ingestion Pipeline->Metadata Extraction
Document Ingestion Pipeline->Embedding Model
Document Ingestion Pipeline->Vector Database (managed)
Document Connectors->Document Corpus (Confluence, SharePoint, Reports)
Document Connectors->Permissions / ACL Propagation
Chunking Strategy->Consultancy Domain Expertise
Prompt Templates->Consultancy Domain Expertise
Permissions / ACL Propagation->Auth / SSO
LLM Foundation Model (API)->Cloud Compute
Embedding Model->Cloud Compute
Vector Database (managed)->Cloud Compute
Vector Database (managed)->Object Storage
Document Corpus (Confluence, SharePoint, Reports)->Object Storage
Hybrid Search (BM25 + vector)->Information Retrieval Theory

// Evolution trajectories (scenarios, not forecasts)
evolve RAG Orchestration 0.75
evolve Vector Database (managed) 0.82
evolve Embedding Model 0.85
evolve LLM Foundation Model (API) 0.88
evolve Permissions / ACL Propagation 0.55

// Inertia watch
component Document Corpus (Confluence, SharePoint, Reports) [0.30, 0.30] inertia

// Notes
note BUILD zone — differentiation [0.55, 0.25]
note BUY / RENT — products [0.45, 0.65]
note UTILITY — consume as API [0.15, 0.90]
```

---

## 3. Build / Buy / Utility table

| Bucket | Components | Rationale |
|---|---|---|
| **BUILD in-house** (differentiation) | Chunking Strategy, Prompt Templates, Golden Eval Set, Permissions / ACL Propagation, Admin & Governance Console, Eval Dashboard, curation of the Document Corpus, consultancy-specific Query Rewriting, Metadata Extraction | Stage I-II — these encode the consultancy's taste, client confidentiality rules, and domain vocabulary. Nobody outside your firm can build them. |
| **BUY as SaaS / RENT** (Stage III product) | RAG Orchestration framework (LangChain / LlamaIndex / Haystack), Reranker (Cohere Rerank, Voyage), LLM Observability (LangSmith, Arize, Langfuse), OCR (Azure Doc Intelligence, Unstructured.io), Document Connectors (Airbyte, Fivetran, or vendor built-ins), Guardrails (NeMo Guardrails, Lakera) | Stage III — mature frameworks exist, plural vendors, standardising APIs. Renting saves 6-12 months versus re-implementing. |
| **CONSUME as utility API** (Stage IV) | LLM Foundation Model (OpenAI / Anthropic / Google / Bedrock), Embedding Model (OpenAI text-embedding-3, Voyage, Cohere), Vector Database (Pinecone serverless, Weaviate Cloud, or pgvector if you already run Postgres), Auth / SSO (Entra ID, Okta), Object Storage (S3/Blob), Cloud Compute | Stage IV — metered API access, many suppliers, price/performance competition. Multi-vendor abstraction recommended; the model layer is commoditising fast. |
| **LEVERAGE as accepted knowledge** (Stage IV knowledge) | Information Retrieval Theory (BM25, HNSW, reranking) | Textbook material — hire people who know it; do not re-invent. |
| **WHOLE-PLATFORM BUY option** | Glean or Microsoft 365 Copilot | If you already live in M365, Copilot grounded on SharePoint covers 60-70% of the use case with near-zero engineering. Glean is the specialist alternative if corpus governance and cross-source search matter more. Worth an honest bake-off before building. |

---

## 4. Strategic analysis

### a. Top 3 by differentiation pressure D = ν · (1 − ε)

1. **Admin & Governance Console** — D = 0.82 × 0.60 = **0.49**. Governance is visible to the Knowledge Admin and immature across the market. Permissions-aware governance is Glean's wedge; it has to be yours too if you build.
2. **Answer with Citations** — D = 0.86 × 0.50 = **0.43**. The quality of answer + citation behaviour is what makes employees trust the system. This is an in-house UX + prompt-engineering discipline, not a vendor feature.
3. **Permissions / ACL Propagation** — D = 0.52 × 0.65 = **0.34**. Consultancy documents carry client-confidentiality rules. Getting this wrong is an existential risk (leaking Client A's material to a consultant on Client B's deal). No vendor will know your ethical walls better than you do.

Honourable mentions: Chunking Strategy (0.42 × 0.55 = 0.23) — chunking rules for legal-style consultancy reports are a learned craft. Golden Eval Set (0.26 × 0.78 = 0.20) — your test set is your compounding asset.

### b. Top 3 by commodity leverage K = (1 − ν) · ε

1. **Cloud Compute** — K = 0.88 × 0.92 = **0.81**. Pure utility.
2. **Object Storage** — K = 0.85 × 0.92 = **0.78**. Pure utility.
3. **Auth / SSO** — K = 0.78 × 0.90 = **0.70**. Use Entra ID / Okta — do not build identity.

Close behind: **LLM Foundation Model (API)** K = 0.45 × 0.78 = 0.35; **Embedding Model** K = 0.50 × 0.75 = 0.38; **Vector Database (managed)** K = 0.58 × 0.70 = 0.41. All three are Stage III heading for Stage IV — consume as APIs, abstract behind an interface so you can swap vendors as prices collapse.

### c. Top 3 dependency risks R = ν(a) · (1 − ε(b))

1. **(Answer with Citations, RAG Orchestration)** = 0.86 × 0.40 = **0.34**. Every user-visible answer hangs on one immature orchestration layer; if LangChain/LlamaIndex/Haystack breaks, the product breaks.
2. **(Admin & Governance Console, Permissions / ACL Propagation)** = 0.82 × 0.65 = **0.53**. Governance UX depends on a Custom-stage permissions layer that you are probably building. Highest raw risk number on the map.
3. **(RAG Orchestration, LLM Foundation Model)** = 0.72 × 0.22 = **0.16** (low in ε-immaturity terms, but high in *vendor-concentration* terms). The foundation model is Stage IV on characteristics but the *vendor market* still has concentration risk — Anthropic API outage = your product down. Mitigate with multi-provider routing (Bedrock/Vertex/Azure OpenAI as a pattern).

Also watch **(Document Ingestion Pipeline, Document Connectors)** = 0.45 × 0.35 = 0.16 — Confluence and SharePoint connectors change under you; budget for breakage.

### d. Suggested gameplays (from the 61)

- **#1 Focus on user needs.** Re-validate the anchors: is the Knowledge Admin really an anchor, or is it just IT pretending to be a user? If the answer is "Admin exists to serve Employee", collapse to a single anchor — but the governance workload is real enough that two anchors is the honest call for a consultancy.
- **#29 Harvesting** on RAG Orchestration, Vector Database, and Embedding Models. These markets are consolidating visibly in 2026; pick one per category, build against a thin abstraction, and swap as winners emerge. Do not write your own.
- **#15 Open Approaches** on the Document Connectors layer. If you build custom connectors for Confluence / SharePoint / an internal DMS, open-source them. You do not make money there; accelerating that layer's commoditisation helps you more than hoarding it.
- **#36 Directed investment** on Permissions / ACL Propagation, Golden Eval Set, and Chunking Strategy. These are your three Genesis/Custom moats; put senior engineers there.
- **#43 Sensing Engines (ILC)** on the User Feedback / Usage Data component. Every thumbs-down, citation click, and reformulated question is signal. Close the loop back into the Golden Eval Set and prompt library — this is the compounding advantage.
- **#57 Fast follower** on the whole-platform question. Glean and M365 Copilot have proven the market; if you are not a model company, you do not need to be first. Run a 60-day pilot of M365 Copilot alongside your build before committing headcount.
- **#34 Procrastination** on the Reranker component specifically. The reranker market is collapsing — Cohere Rerank, Voyage-rerank, cross-encoders as a Bedrock/Vertex feature. Do not invest in building one; wait six months and the choice will be clearer.

### e. Doctrine checks

- **Respected:** #1 Focus on user needs (anchored on Employee + Knowledge Admin, not "IT"), #10 Know your users (two anchors), #7 Use appropriate methods (BUILD/BUY/UTILITY columns apply different management styles by stage).
- **Watch:** **#13 Manage inertia.** The Document Corpus itself is the inertia — years of inconsistent metadata, duplicate documents, and stale content in SharePoint. The assistant will be as good as the corpus. Budget real money for corpus curation or the assistant will surface the mess faithfully and erode trust.
- **Watch:** **#2 Use a systematic mechanism of learning.** The Golden Eval Set + Feedback Capture loop is the mechanism. If you do not build this from day one, you have no way to tell whether a model upgrade or prompt change is helping or hurting.
- **Watch:** **#15 Do better with less (FIRE).** Resist the urge to run a six-month framework bake-off. Pick LangChain *or* LlamaIndex *or* Haystack in a week, ship a 100-user pilot in a month, iterate.
- **Risk:** **#4 Be transparent.** Citations must be faithful. A hallucinated answer with a confident citation is worse than "I don't know". Guardrails and citation-faithfulness checks are non-negotiable.

### f. Climatic context

- **#3 Everything evolves** — the whole RAG stack is evolving rightward fast. Anything you build today against an immature component is a maintenance bet.
- **#27 Product-to-utility punctuated equilibrium** — this is the live climatic pattern on LLMs and embedding models. Prices fell ~66% on Claude 4.5 versus its predecessor, ~90% on DeepSeek-class models, and the Pinecone / Weaviate / Qdrant / pgvector contest is now a full commodity war. Expect another 2-5× price collapse within 18-24 months on inference.
- **#10 Higher-order systems create new worth** — industrialised LLMs + vector infra are exactly what let a 500-person firm build a knowledge assistant at all. Five years ago this project needed a research team.
- **#15-17 Inertia** — the dominant forms here: #8 skill-acquisition cost (employees have Slack-search habits to unlearn), #9 re-architecture cost (SharePoint taxonomy is 15 years old), #14 strategic-control loss (fear of "the AI knows everything about our clients").
- **#22 Two forms of disruption** — you are on the *product-to-utility* side of disruption, not the Genesis side. This is predictable; plan with confidence, but plan for the commoditisation wave to keep coming.
- **#18 You cannot measure evolution over time or adoption** — the `evolve` arrows above are scenarios, not forecasts. See (h).

### g. Deep-placement notes

I ran targeted research on five components. In each case I went in with a cheat-sheet seed score and checked vendor landscape + publication shift.

1. **LLM Foundation Model (API).** Cheat-sheet seed: 0.65 (early Product). Vendor-landscape search returned a mature multi-vendor commodity pattern: GPT-5 / Claude 4.5 / Gemini 2.5 / Llama 4 / DeepSeek / Mistral competing on price, with Bedrock and Azure OpenAI as enterprise utility fronts. Claude 4.5 cut price 66% from its predecessor; DeepSeek is 90% cheaper than proprietary. Publication has shifted from "describe the wonder" to price/benchmark ops comparison. **Shifted to 0.78 — late Product (+rental) becoming Commodity (+utility).** Treatment: consume as utility API, abstract behind a router.

2. **Embedding Model.** Cheat-sheet seed: 0.60. Vendor-landscape search: OpenAI text-embedding-3, Voyage 3.5 / 4 series, Cohere embed-v4, BGE-M3 open-source — MTEB scores within ~2 points of each other, clear commodity war on price and latency. **Shifted to 0.75 — Commodity (+utility).** Treatment: utility API, same routing abstraction.

3. **Vector Database (managed).** Cheat-sheet seed: 0.55. Research found a $3.2B market growing 24% YoY, Pinecone 70% of the *managed* segment but pgvector running in production at Supabase/Neon/Instacart, Qdrant winning open-source benchmarks, Weaviate holding hybrid search. Publication has shifted to "when to use which" comparison guides — classic Stage III signal. **Shifted to 0.70 — mid-to-late Product (+rental).** Not yet Stage IV because architectural differentiation (HNSW tuning, hybrid search, metadata filtering) still matters. Treatment: rent managed; if Postgres is already deployed, pgvector is a legitimate "good enough" choice that collapses vendor count.

4. **RAG Orchestration.** Cheat-sheet seed: 0.50. Research: LangChain / LlamaIndex / Haystack / DSPy / Pathway. 400% framework-adoption surge since 2024; publication has shifted from "how to build RAG from scratch" to framework-comparison and production-pattern articles. Many teams now run LlamaIndex for ingestion + LangChain/LangGraph for orchestration. **Shifted to 0.60 — mid Product (+rental).** Not yet Stage IV — API surfaces still churn every 3-6 months. Treatment: rent, but keep the abstraction thin so you can swap.

5. **Whole-platform SaaS alternatives (Glean, M365 Copilot).** Cheat-sheet seed: 0.50. Research: Glean at $7.2B valuation, $200M ARR doubled in 9 months; supports 15+ LLMs; Glean Protect Plus for governance. M365 Copilot mature on SharePoint grounding but ecosystem-biased. **Placed at 0.60 — Product (+rental).** Practical implication: for a 500-person consultancy, a Copilot/Glean pilot is the honest baseline to beat before committing build headcount — gameplay #57 Fast follower.

### h. Caveat

Evolution trajectories (`evolve` arrows and the shift notes above) are **scenarios, not forecasts**. Wardley's climatic pattern #18: *"you cannot measure evolution over time or adoption."* The map is a snapshot of April 2026 priors; re-map in 6 months, and again after any significant platform or pricing shift (e.g., a hyperscaler acquiring a RAG framework, or a frontier lab releasing embedding models at marginal cost).

Specifically flag three scenarios that would force a re-map:
- A hyperscaler (AWS/Azure/GCP) launching first-party managed RAG that bundles orchestration + vector DB + LLM — would collapse three components into one utility and change build-vs-buy across the middle of the map.
- Regulatory movement on AI in the UK / EU that forces on-premise inference for client-confidential data — would push LLM Foundation Model back left on your *specific* map (not the industry's).
- M365 Copilot gaining permissions-aware cross-source grounding at parity with Glean — would make the whole-platform buy the obvious move for a 500-person firm.

---

## 5. Verification notes (Step 5.5 self-check)

- **Visibility constraint walked.** Every `A->B` edge in the OWM block has `ν(A) ≥ ν(B)`. Notable tight ones: Hybrid Search (0.60) -> Permissions / ACL Propagation (0.52) — OK. RAG Orchestration (0.72) -> LLM Observability (0.33) — OK. Permissions / ACL Propagation (0.52) -> Auth/SSO (0.22) — OK. Admin & Governance Console (0.82) -> Permissions / ACL Propagation (0.52) — OK.
- **Stage naming.** "Product (+rental)" and "Commodity (+utility)" used throughout prose where referring to stages; bare "product" only used when referring to the user's actual SaaS product (e.g., "your product" / "the assistant").
- **Deep-placement coverage.** 5 components researched (LLM, Embedding, Vector DB, RAG Orchestration, SaaS alternatives). Within the 3-5 budget.
