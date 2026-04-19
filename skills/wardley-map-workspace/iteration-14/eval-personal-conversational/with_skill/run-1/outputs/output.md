# Wardley Map — Modern Conversational Technology Landscape

**Scenario:** Map the landscape of modern conversational technology (voice assistants, chatbots, LLM-powered agents). Include language models, speech (ASR, TTS), dialogue management, knowledge retrieval, personalisation, privacy, and user experience. What's differentiating vs. commoditising?

Two anchors are used — **End User** (someone who talks to an assistant/bot/agent to get something done) and **Developer** (someone building a conversational product on top of the stack). Both are valid users; the strategic picture changes depending on whose map you're looking at, and most real businesses in this space serve both.

---

## 1. Map (OWM)

```owm
title Modern Conversational Technology Landscape
style wardley

// Anchors
anchor End User [0.99, 0.60]
anchor Developer [0.95, 0.45]

// User-facing surfaces
component Voice Assistant UX [0.88, 0.55]
component Chatbot UX [0.87, 0.70]
component LLM Agent UX [0.86, 0.30]
component Personalisation / Memory [0.80, 0.30]
component Multi-turn Dialogue Flow [0.78, 0.50]
component Wake-word / Barge-in [0.74, 0.70]

// Developer-facing surfaces
component Agent SDK / Framework [0.82, 0.35]
component Prompt / Flow Authoring [0.80, 0.55]
component Eval & Observability (LLM) [0.76, 0.30]

// Core conversational logic
component Multi-agent Orchestration [0.72, 0.18]
component Planning & Reasoning [0.70, 0.20]
component Tool Use / Function Calling [0.68, 0.40]
component Dialogue Management [0.66, 0.45]
component Intent / Slot Understanding [0.62, 0.70]

// Knowledge retrieval
component Knowledge Retrieval (RAG) [0.58, 0.55]
component Re-ranker [0.54, 0.45]
component Enterprise Knowledge Base [0.50, 0.55]
component Vector Database [0.42, 0.70]
component Embeddings Model [0.38, 0.80]

// Safety & privacy
component Guardrails [0.60, 0.35]
component Safety / Content Moderation [0.56, 0.45]
component Privacy Controls & Consent [0.52, 0.40]
component Data Governance [0.28, 0.35]
component Audit Logging [0.22, 0.75]

// Speech layer
component ASR (Speech-to-Text) [0.52, 0.75]
component TTS (Text-to-Speech) [0.50, 0.70]
component Voice Cloning [0.44, 0.25]
component Speaker Diarisation [0.40, 0.55]

// Foundation models (deep layer — many things depend on them)
component Frontier LLM [0.36, 0.55]
component Open-weight LLM [0.30, 0.60]
component Small / On-device LLM [0.30, 0.35]
component Fine-tuning (SFT / RLHF) [0.32, 0.45]

// Personalisation data
component User Profile Store [0.36, 0.65]
component Conversation Memory Store [0.34, 0.30]

// Inference & infrastructure
component Model Serving / Inference [0.22, 0.55]
component GPU Compute [0.16, 0.80]
component Cloud Compute [0.12, 0.92]
component Object Storage [0.10, 0.92]
component Identity / Auth [0.20, 0.90]
component Telephony / VoIP [0.24, 0.88]

// Dependencies — end-user side
End User->Voice Assistant UX
End User->Chatbot UX
End User->LLM Agent UX
End User->Personalisation / Memory
End User->Multi-turn Dialogue Flow
Voice Assistant UX->Wake-word / Barge-in
Voice Assistant UX->ASR (Speech-to-Text)
Voice Assistant UX->TTS (Text-to-Speech)
Voice Assistant UX->Multi-turn Dialogue Flow
Chatbot UX->Multi-turn Dialogue Flow
Chatbot UX->Intent / Slot Understanding
LLM Agent UX->Multi-agent Orchestration
LLM Agent UX->Planning & Reasoning
LLM Agent UX->Tool Use / Function Calling
Multi-turn Dialogue Flow->Dialogue Management
Personalisation / Memory->Conversation Memory Store
Personalisation / Memory->User Profile Store

// Developer side
Developer->Agent SDK / Framework
Developer->Prompt / Flow Authoring
Developer->Eval & Observability (LLM)
Agent SDK / Framework->Dialogue Management
Agent SDK / Framework->Tool Use / Function Calling
Prompt / Flow Authoring->Dialogue Management
Eval & Observability (LLM)->Audit Logging

// Core dialogue & reasoning
Dialogue Management->Frontier LLM
Dialogue Management->Knowledge Retrieval (RAG)
Dialogue Management->Guardrails
Intent / Slot Understanding->Frontier LLM
Tool Use / Function Calling->Frontier LLM
Planning & Reasoning->Frontier LLM
Multi-agent Orchestration->Planning & Reasoning
Multi-agent Orchestration->Tool Use / Function Calling

// Retrieval stack
Knowledge Retrieval (RAG)->Enterprise Knowledge Base
Knowledge Retrieval (RAG)->Vector Database
Knowledge Retrieval (RAG)->Re-ranker
Vector Database->Embeddings Model
Re-ranker->Frontier LLM
Embeddings Model->Model Serving / Inference

// Speech stack
ASR (Speech-to-Text)->Model Serving / Inference
TTS (Text-to-Speech)->Model Serving / Inference
TTS (Text-to-Speech)->Voice Cloning
ASR (Speech-to-Text)->Speaker Diarisation

// Foundation models
Frontier LLM->Model Serving / Inference
Open-weight LLM->Model Serving / Inference
Small / On-device LLM->Model Serving / Inference
Fine-tuning (SFT / RLHF)->Open-weight LLM
Dialogue Management->Open-weight LLM
Dialogue Management->Small / On-device LLM

// Safety & privacy
Guardrails->Safety / Content Moderation
Guardrails->Privacy Controls & Consent
Safety / Content Moderation->Frontier LLM
Privacy Controls & Consent->Data Governance
User Profile Store->Data Governance
Conversation Memory Store->Data Governance
Data Governance->Audit Logging

// Infra
Model Serving / Inference->GPU Compute
GPU Compute->Cloud Compute
Cloud Compute->Object Storage
Voice Assistant UX->Telephony / VoIP
Chatbot UX->Identity / Auth
LLM Agent UX->Identity / Auth
User Profile Store->Identity / Auth

// Evolution targets (scenarios, not forecasts)
evolve Frontier LLM 0.75
evolve Knowledge Retrieval (RAG) 0.78
evolve Tool Use / Function Calling 0.65
evolve Vector Database 0.85
evolve Agent SDK / Framework 0.60
evolve Personalisation / Memory 0.55

// Strategic annotations
note Differentiation zone [0.75, 0.22]
note Industrialising core [0.55, 0.60]
note Utility infra [0.15, 0.90]
```

Validator result: **OK: 42 components/anchors, 62 edges — no violations.**

---

## 2. Strategic analysis

### a. Differentiation opportunities (top 3)

Components that are user-visible and still left of the Product/Commodity boundary — the places where a smart team can still out-execute the market.

1. **Multi-agent Orchestration (Genesis).** Nobody knows yet how to reliably compose 3+ specialised agents to complete a multi-step task in production. Academic work, a few frontier products (Devin, Manus, Claude Code's own sub-agent system), and a lot of demos. Highest D on the map — high visibility (at the top of an agent product) × very low ε. The winner here defines how work itself gets automated.
2. **Planning & Reasoning (Genesis → Custom Built).** Closely adjacent. Chain-of-thought, tree search, and reasoning-tuned models are the substrate; how you steer them for reliable real-world planning is still bespoke per application. This is where "my agent actually works" becomes a moat.
3. **Personalisation / Memory (Custom Built).** Every consumer assistant vendor is trying to turn transient chat into durable, usable long-term memory. The technical question (what to remember, when to retrieve, how to forget) is wide open; the product question (does the user trust it?) is wider. Users value this directly, so the visibility premium is real.

Honourable mentions: **LLM Agent UX** (same Genesis column but slightly less central than Orchestration), **Eval & Observability (LLM)** (developer-facing but strategically load-bearing — if you can't measure you can't ship).

### b. Commodity-leverage candidates (top 3)

Deep, mature components — rent, don't build.

1. **Cloud compute and Object storage (Commodity +utility).** Uncontested — use AWS/GCP/Azure. Building your own data centre is a Genesis-era choice for 99% of players.
2. **GPU compute (Commodity +utility, contested).** Still sole-sourced in practice (NVIDIA) but the consumption pattern is utility-like. Buy capacity from hyperscalers and specialised clouds (CoreWeave, Lambda, Modal); reserve self-hosting only if inference volume justifies it.
3. **Embeddings model (Commodity +utility).** OpenAI, Cohere, Voyage, Jina, and several open-weight options (BGE, GTE) offer interchangeable quality for most retrieval tasks. The days when a custom embedding model was a moat are over. Consume as an API; fine-tune only on genuinely domain-specific corpora.

Also strongly in the commodity zone: **Identity / Auth**, **Telephony / VoIP**, **Wake-word / Barge-in** (established speech patterns), **Chatbot UX** widgets (Intercom, Drift, and OSS equivalents cover the generic case).

### c. Dependency risks (top 3)

Visible user-facing components resting on immature foundations.

1. **LLM Agent UX → Multi-agent Orchestration.** The whole pitch of "just describe your task and the agent figures it out" is load-bearing on an orchestration layer that is still Genesis. Product promises are running ahead of capability; reliability incidents propagate straight to the user.
2. **Personalisation / Memory → Conversation Memory Store.** A user-visible "remember me" promise depends on a data substrate (what is stored, for how long, with what retrieval semantics) that is still being invented. Gets worse as privacy regulation tightens around the memory store.
3. **Dialogue Management → Frontier LLM.** This is less fragile than it looks — Frontier LLM is at the Product boundary, not Custom — but the risk is *vendor concentration*, not immaturity. A production dialogue manager hard-wired to one LLM vendor inherits their pricing, availability, and policy changes.

### d. Suggested gameplays

Named Wardley plays against this landscape.

- **#36 Directed investment** on **Multi-agent Orchestration** and **Planning & Reasoning**. These are the top-D components. Investment without experimentation is gambling; pair with #37.
- **#37 Experimentation** across the Genesis column. FIRE projects (fast, inexpensive, restrained, elegant) testing orchestration patterns; kill what doesn't work within weeks.
- **#43 Sensing Engines (ILC)** on **Agent SDK / Framework** and **Tool Use / Function Calling**. Watch which patterns community adoption converges on (LangGraph vs AutoGen vs MCP-style protocols), then harvest the winner. Don't bet the farm on one SDK early.
- **#15 Open Approaches** on components you want commoditised but do not make money from: **Embeddings Model**, **Vector Database**, **Guardrails primitives**. You're a consumer of these; accelerating their commoditisation helps you. For most players, don't open-source your own Orchestration or Memory layer — that's your moat.
- **#29 Harvesting** on **Vector Database** and **Agent SDK / Framework**. Let Pinecone, Weaviate, Qdrant, Milvus, pgvector duke it out for a year; then migrate to whichever became the de facto standard.
- **#45 Two factor** — you have two user types on this map (End User and Developer). A successful conversational-tech platform creates flywheels between them: developer tools produce better end-user experiences, which create training/eval data, which improves developer tools. This is the core strategic shape for platform plays (OpenAI, Anthropic, Google).
- **#30 Standards game** on **Tool Use / Function Calling** — the emerging fight over agent-tool protocols (MCP, OpenAI function schema, custom JSON contracts) is a classic standards race. Whichever standard wins influences switching costs across the whole map.
- **#16 Exploiting Network Effects** on **Enterprise Knowledge Base + RAG**. The more an enterprise's knowledge lives inside your retrieval stack, the more valuable the assistant becomes — and the higher the switching cost.
- **#44 Tower and Moat** on **Personalisation / Memory**. Once a user has three years of memory in your assistant, a competitor with a cold start cannot match the experience at any price. Dig the moat by explicit UX around "things I remember about you".

### e. Doctrine notes

- Checked: **#1 Focus on user needs** and **#10 Know your users** — map has two anchors (End User + Developer), not one. Correct for this space.
- Watch: **#13 Manage inertia**. Two real inertias on this map: (1) consumer-side #6 Confusion over method — non-technical users don't know when to type, when to talk, or what an agent can do. (2) supplier-side — teams with existing chatbot stacks (intent/entity based) are slow to migrate to LLM-native dialogue management; their sunk capital in intent models is a drag (form #2).
- Watch: **#2 Use a systematic mechanism of learning**. **Eval & Observability (LLM)** is deliberately placed at high visibility on the developer anchor — if this is absent, the whole stack degrades silently. Many current agent products are shipping without serious eval; this is a doctrine violation in flight.
- Watch: **#7 Use appropriate methods (we're not all the same)**. Pioneer-Settler-Town-Planner applies heavily here: Genesis components (Orchestration, Planning) need pioneer culture; Product-stage components (RAG pipelines, ASR integration) want settler/engineer culture; Commodity infra wants town-planner operational excellence. Mixing cultures across stages is the classic mis-alignment.

### f. Climatic context

Patterns actively shaping this map:

- **#3 Everything evolves.** Components like LLM, RAG, vector DB have moved from Genesis to mid-Product in under five years. The map you draw today will be wrong in 18 months.
- **#17 Capital flows to the new.** Enormous investment is chasing the Genesis column (agents, orchestration). Expect the rate of evolution there to be faster than historical norms, not slower.
- **#27 Product-to-utility punctuated equilibrium (a "war").** The transition of Frontier LLMs from Product (feature competition: "our model is smarter") to Utility (API-metered interchangeable capability) is happening now. Open-weight models (Llama, Mistral, Qwen) are the commoditising force; hyperscaler inference APIs are the utility providers. This is a textbook #27 event in flight.
- **#15 / #16 Inertia** from prior-generation chatbot stacks (intent/entity) and legacy IVR telephony assistants. Real drag on migration to LLM-native dialogue.
- **#18 You cannot measure evolution over time or adoption.** Restated here because this field is full of "by 2027 agents will…" forecasts. The cheat sheet places what *is*, not what *will be*.

### g. Deep-placement notes

I ran targeted checks on four high-stakes components rather than researching every node. Summary:

- **Frontier LLM (placed 0.55, edge of Product).** Cheat-sheet rows split II/III: User Perception is clearly Stage III (people expect ChatGPT-like answers), but Certainty and Publication Types still have a Stage II signal (new papers weekly, benchmark goalposts moving). Vendor landscape: OpenAI, Anthropic, Google, Meta, xAI, Mistral, Cohere — handful of frontier players plus ~6 serious open-weight contenders. That's classic mid-Product. Confirmed at 0.55 with evolution pressure toward 0.75 as capabilities stabilise and prices compress. **Deep placement confirms Stage III for Frontier LLM.**
- **Knowledge Retrieval (RAG) (placed 0.55).** Cheat sheet put this mid-II in late 2023; by 2026 vendor landscape and publication type both read Stage III — extensive "RAG best practices" operational guides, many vendors (LlamaIndex, LangChain, pgvector, bespoke stacks), and shifting attention to agentic retrieval and graph RAG as the next frontier. **Shifted from initial 0.45 (mid-Custom) to 0.55 (early Product).** Evolution target of 0.78 is plausible within ~2 years.
- **Vector Database (placed 0.70).** Dedicated vendor concentration (Pinecone, Weaviate, Qdrant, Chroma, Milvus) is still growing but pgvector/Postgres integrations and commodity cloud offerings (AWS OpenSearch, Azure AI Search with vector) are undercutting standalone vendors. Publication type is dominated by operations guides and performance benchmarks. **Stage III mid-to-late, heading toward commodity.** Evolution target 0.85 reflects this — the bundling into general-purpose DBs is the commoditising force.
- **Multi-agent Orchestration (placed 0.18, Genesis).** Publication type is overwhelmingly "describe the wonder" — research papers, breathless threads, and early-adopter demos. Vendor count is small and fragmenting (CrewAI, AutoGen, LangGraph, OpenAI Swarm, custom stacks). User perception is "exciting / confusing". All four cheat-sheet rows converge on Stage I. **Deep placement confirms Genesis.** This is the map's highest-D component and the one where 2026-era strategy is most contested.

### h. Caveat

Evolution trajectories shown (the `evolve` arrows) and the strategic calls above are *scenarios, not forecasts*. Wardley's climatic pattern #18: *"you cannot measure evolution over time or adoption."* The cheat-sheet placements describe where components sit today; where they actually end up depends on which gameplays are executed by which players, how regulation moves, and whether any of the Genesis bets in the left column materialise. Re-map in 12 months.

---

## Quick answer to the scenario question

**What's differentiating (build here):** Multi-agent Orchestration, Planning & Reasoning, Personalisation / Memory, LLM Agent UX, domain-specific fine-tuning — the whole Genesis / Custom-Built left column at the top of the map.

**What's industrialising (use carefully, don't own):** Frontier LLMs, RAG pipelines, Tool Use / Function Calling, Dialogue Management patterns, Agent SDKs. Treat these as Stage III Product (+rental) — pick winners, don't bet heavily on single vendors, design for swap.

**What's commoditising (rent, don't build):** Cloud compute, GPU compute (increasingly), Object storage, Identity / Auth, Telephony / VoIP, Embeddings models, Wake-word detection, basic chat widgets. These are Stage IV Commodity (+utility) — utility services to consume, not capabilities to build.
