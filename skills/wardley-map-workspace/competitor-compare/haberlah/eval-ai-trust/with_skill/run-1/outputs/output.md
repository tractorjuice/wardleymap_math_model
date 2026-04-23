# Wardley Map Analysis: AI Trust Landscape (June 2023)

## Purpose

This map answers the question: **In June 2023, which components determine whether individuals, government, and business can trust AI systems — and where is that trust most fragile?** It is a landscape map, not a build-vs-buy map for any single firm; the strategic decision it supports is *where to invest attention and capital in the AI trust stack* given that foundation models have just crossed into broad public use (ChatGPT, GPT-4, Claude, Bard) while the governance, control, and evaluation machinery around them is still nascent.

## Strategic Context (answered from the brief)

The skill's Step 1 asks for four things. Because this benchmark provides the scenario as a single prompt, the answers below were inferred directly from the brief — they were not solicited from a live user.

| Question | Answer used |
|---|---|
| Strategic question | "Where is trust in AI systems fragile, and what's differentiating vs. commoditising in June 2023?" |
| User anchors | Individuals, Government, Business — the three trust-holding constituencies named in the brief |
| Core needs | Trusted AI output, Safety, Reputation, Competitive advantage |
| Scope boundary | The public AI ecosystem in June 2023 — foundation-model era; not a single firm's stack |

## Value Chain Overview

Working backward from the three anchors to the infrastructure they depend on produces 15 components grouped into four horizontal bands:

- **Outcome band (visible)**: Trusted AI Output, Safety, Reputation, Competitive Advantage
- **Governance band**: Regulations, AI Policy, Audits, Benchmarks
- **Control-mechanism band**: Feedback Loops, Constitution, Forensics
- **Technical band (invisible)**: AI Models, Algorithms, Training Data, Compute

## OWM (OnlineWardleyMaps) Text Block

```
title AI Trust Landscape (June 2023)
style wardley

anchor Individuals [0.96, 0.50]
anchor Government [0.96, 0.40]
anchor Business [0.96, 0.60]

component Trusted AI Output [0.86, 0.15]
component Safety [0.82, 0.25]
component Reputation [0.80, 0.55]
component Competitive Advantage [0.78, 0.60]
component Regulations [0.70, 0.20]
component AI Policy [0.64, 0.25]
component Audits [0.60, 0.30]
component Benchmarks [0.55, 0.45]
component Feedback Loops [0.48, 0.32]
component Constitution [0.45, 0.10]
component Forensics [0.42, 0.10]
component AI Models [0.33, 0.33] inertia
component Algorithms [0.25, 0.60]
component Training Data [0.20, 0.35]
component Compute [0.10, 0.82]

Individuals->Trusted AI Output
Individuals->Safety
Government->Safety
Government->Regulations
Business->Reputation
Business->Competitive Advantage
Business->Trusted AI Output

Trusted AI Output->Safety
Trusted AI Output->Forensics
Trusted AI Output->Benchmarks
Trusted AI Output->Constitution

Safety->Audits
Safety->Feedback Loops
Safety->Regulations

Reputation->Audits
Reputation->Benchmarks
Reputation->AI Policy

Competitive Advantage->AI Models
Competitive Advantage->Training Data

Regulations->Audits
Regulations->AI Policy
AI Policy->Audits
Audits->AI Models
Audits->Training Data

Benchmarks->AI Models
Feedback Loops->AI Models
Constitution->AI Models
Forensics->AI Models

AI Models->Algorithms
AI Models->Training Data
AI Models->Compute
Training Data->Compute
Algorithms->Compute

evolve AI Models 0.55
evolve Benchmarks 0.65
evolve Regulations 0.40
evolve Feedback Loops 0.55

annotation 1 [[0.40, 0.12]] Fragile: Constitution and Forensics are Genesis-stage; trust depends on them but neither is proven at scale.
annotation 2 [[0.72, 0.22]] EU AI Act still in trilogue June 2023 — regulatory regime is nascent.
annotation 3 [[0.15, 0.82]] Compute (NVIDIA H100 / hyperscaler GPU) is the only true commodity in the stack.
```

## Interactive React Artifact

```jsx
import React, { useState } from "react";

const COMPONENTS = [
  { id: "individuals", name: "Individuals", x: 0.50, y: 0.96, stage: "Anchor", anchor: true,
    rationale: "One of three trust-holding constituencies; wants AI that is safe and honest." },
  { id: "government", name: "Government", x: 0.40, y: 0.96, stage: "Anchor", anchor: true,
    rationale: "Regulator anchor; trust flows through enforceable safety guarantees." },
  { id: "business", name: "Business", x: 0.60, y: 0.96, stage: "Anchor", anchor: true,
    rationale: "Deployer anchor; trust determines adoption, reputation, and competitive position." },
  { id: "trusted-output", name: "Trusted AI Output", x: 0.15, y: 0.86, stage: "Genesis",
    rationale: "Concept of 'trustworthy output' still being defined in June 2023 — no cross-industry consensus on what it means operationally." },
  { id: "safety", name: "Safety", x: 0.25, y: 0.82, stage: "Custom-Built",
    rationale: "Every lab uses bespoke safety evals (OpenAI red-team, Anthropic harmlessness, DeepMind Sparrow). No standard definition or measurement." },
  { id: "reputation", name: "Reputation", x: 0.55, y: 0.80, stage: "Product",
    rationale: "Reputation as a business concept is well-understood and measurable; multiple established methodologies (NPS, brand tracking)." },
  { id: "comp-advantage", name: "Competitive Advantage", x: 0.60, y: 0.78, stage: "Product",
    rationale: "Classic strategy outcome; Porter-era frameworks make this a mature construct though its AI drivers are novel." },
  { id: "regulations", name: "Regulations", x: 0.20, y: 0.70, stage: "Custom-Built",
    rationale: "EU AI Act in trilogue (May 2023 Parliament vote); US executive action still months away. Jurisdiction-specific, bespoke, not yet enforced." },
  { id: "ai-policy", name: "AI Policy", x: 0.25, y: 0.64, stage: "Custom-Built",
    rationale: "Internal corporate AI use-policies being drafted ad-hoc in 2023; no standard template or vendor." },
  { id: "audits", name: "Audits", x: 0.30, y: 0.60, stage: "Custom-Built",
    rationale: "Boutique AI-audit firms (ORCAA, Trail of Bits, Holistic AI) exist but each audit is bespoke; no certified methodology." },
  { id: "benchmarks", name: "Benchmarks", x: 0.45, y: 0.55, stage: "Product",
    rationale: "HELM, MMLU, BIG-bench, HumanEval are widely cited and comparable across models — Product stage, though still fragmenting." },
  { id: "feedback", name: "Feedback Loops", x: 0.32, y: 0.48, stage: "Custom-Built",
    rationale: "RLHF / RLAIF becoming standard but every lab's pipeline is bespoke; data labelling, reward-model training, and PPO setup are not commoditised." },
  { id: "constitution", name: "Constitution", x: 0.10, y: 0.45, stage: "Genesis",
    rationale: "Anthropic's Constitutional AI paper (Dec 2022) introduced the approach; only one production deployment in June 2023. Novel, unproven at scale." },
  { id: "forensics", name: "Forensics", x: 0.10, y: 0.42, stage: "Genesis",
    rationale: "AI-output detection is pre-Genesis; OpenAI withdrew its classifier Jan 2023 for low accuracy. Watermarking proposals unpublished or unreliable." },
  { id: "ai-models", name: "AI Models", x: 0.33, y: 0.33, stage: "Custom-Built", inertia: true,
    rationale: "GPT-4 released March 2023, Claude June 2023, Llama 2 imminent. A handful of frontier labs; closed weights; bespoke training. Inertia from 3-year training cycles and $100M+ sunk cost." },
  { id: "algorithms", name: "Algorithms", x: 0.60, y: 0.25, stage: "Product",
    rationale: "Transformer (2017), RLHF (2017-2022), diffusion — published, open, taught in graduate courses. Third-party implementations are plentiful." },
  { id: "training-data", name: "Training Data", x: 0.35, y: 0.20, stage: "Custom-Built",
    rationale: "CommonCrawl is commodity but frontier training mixes are proprietary blends; licensed data (books, code, images) is bespoke per lab." },
  { id: "compute", name: "Compute", x: 0.82, y: 0.10, stage: "Commodity",
    rationale: "Hyperscaler GPU (AWS P5, GCP A3, Azure ND) with NVIDIA H100/A100 — billed per hour, standardised API, multiple providers. Supply-constrained but not differentiated." }
];

const LINKS = [
  ["individuals","trusted-output"],["individuals","safety"],
  ["government","safety"],["government","regulations"],
  ["business","reputation"],["business","comp-advantage"],["business","trusted-output"],
  ["trusted-output","safety"],["trusted-output","forensics"],["trusted-output","benchmarks"],["trusted-output","constitution"],
  ["safety","audits"],["safety","feedback"],["safety","regulations"],
  ["reputation","audits"],["reputation","benchmarks"],["reputation","ai-policy"],
  ["comp-advantage","ai-models"],["comp-advantage","training-data"],
  ["regulations","audits"],["regulations","ai-policy"],
  ["ai-policy","audits"],
  ["audits","ai-models"],["audits","training-data"],
  ["benchmarks","ai-models"],["feedback","ai-models"],["constitution","ai-models"],["forensics","ai-models"],
  ["ai-models","algorithms"],["ai-models","training-data"],["ai-models","compute"],
  ["training-data","compute"],["algorithms","compute"]
];

const EVOLUTIONS = [
  { id: "ai-models", to: 0.55 }, { id: "benchmarks", to: 0.65 },
  { id: "regulations", to: 0.40 }, { id: "feedback", to: 0.55 }
];

const W = 1100, H = 700, PAD = { top: 60, right: 220, bottom: 70, left: 170 };
const xS = m => PAD.left + m * (W - PAD.left - PAD.right);
const yS = v => PAD.top + (1 - v) * (H - PAD.top - PAD.bottom);

export default function WardleyMap() {
  const [selected, setSelected] = useState(null);
  const [hover, setHover] = useState(null);
  const byId = Object.fromEntries(COMPONENTS.map(c => [c.id, c]));

  function related(id) {
    if (!id) return new Set();
    const keep = new Set([id]);
    let changed = true;
    while (changed) {
      changed = false;
      for (const [a, b] of LINKS) {
        if (keep.has(a) && !keep.has(b)) { keep.add(b); changed = true; }
        if (keep.has(b) && !keep.has(a)) { keep.add(a); changed = true; }
      }
    }
    return keep;
  }
  const highlighted = related(selected);
  const dim = id => selected && !highlighted.has(id);

  return (
    <div style={{ fontFamily: "-apple-system,Segoe UI,Helvetica,Arial,sans-serif", background: "#fff" }}>
      <svg width={W} height={H} onClick={() => setSelected(null)}>
        <rect x={PAD.left} y={PAD.top} width={W-PAD.left-PAD.right} height={H-PAD.top-PAD.bottom} fill="#fff" stroke="#222"/>
        {[0.125,0.375,0.625,0.875].map((m,i) => (
          <rect key={i} x={xS(m-0.125)} y={PAD.top} width={xS(m+0.125)-xS(m-0.125)} height={H-PAD.top-PAD.bottom}
                fill={i%2===0 ? "#fafafa" : "#fff"} />
        ))}
        {[0.25,0.5,0.75].map(m => (
          <line key={m} x1={xS(m)} y1={PAD.top} x2={xS(m)} y2={H-PAD.bottom}
                stroke="#ccc" strokeDasharray="4 4"/>
        ))}
        <text x={PAD.left} y={40} fontSize="16" fontWeight="600" fill="#111">
          AI Trust Landscape — June 2023
        </text>
        <text x={xS(0.125)} y={H-PAD.bottom+18} fontSize="11" textAnchor="middle" fill="#555">Genesis</text>
        <text x={xS(0.375)} y={H-PAD.bottom+18} fontSize="11" textAnchor="middle" fill="#555">Custom-Built</text>
        <text x={xS(0.625)} y={H-PAD.bottom+18} fontSize="11" textAnchor="middle" fill="#555">Product (+Rental)</text>
        <text x={xS(0.875)} y={H-PAD.bottom+18} fontSize="11" textAnchor="middle" fill="#555">Commodity (+Utility)</text>
        <text x={xS(0.5)} y={H-PAD.bottom+40} fontSize="12" textAnchor="middle" fill="#333">Evolution →</text>
        <text x={30} y={PAD.top+10} fontSize="11" fill="#555">Visible</text>
        <text x={30} y={H-PAD.bottom-5} fontSize="11" fill="#555">Invisible</text>
        <text x={20} y={(PAD.top+H-PAD.bottom)/2} fontSize="12" transform={`rotate(-90 20 ${(PAD.top+H-PAD.bottom)/2})`}
              textAnchor="middle" fill="#333">Value chain / Visibility</text>

        {LINKS.map(([a,b],i) => {
          const A = byId[a], B = byId[b];
          if (!A || !B) return null;
          const op = (dim(a)||dim(b)) ? 0.08 : 0.55;
          const x1=xS(A.x), y1=yS(A.y), x2=xS(B.x), y2=yS(B.y);
          const cx = (x1+x2)/2, cy = (y1+y2)/2 + 18;
          return <path key={i} d={`M${x1},${y1} Q${cx},${cy} ${x2},${y2}`} stroke="#777"
                       strokeWidth="1" fill="none" opacity={op}/>;
        })}

        {EVOLUTIONS.map((e,i) => {
          const c = byId[e.id];
          if (!c) return null;
          const x1=xS(c.x), x2=xS(e.to), y=yS(c.y);
          return (
            <g key={i} opacity={dim(e.id)?0.15:0.85}>
              <line x1={x1} y1={y} x2={x2-8} y2={y} stroke="#c0392b"
                    strokeWidth="1.5" strokeDasharray="5 3"/>
              <polygon points={`${x2},${y} ${x2-8},${y-4} ${x2-8},${y+4}`} fill="#c0392b"/>
            </g>
          );
        })}

        {COMPONENTS.map(c => {
          const cx = xS(c.x), cy = yS(c.y);
          const op = dim(c.id) ? 0.15 : 1;
          const fill = c.anchor ? "#222" : "#fff";
          const textColor = c.anchor ? "#fff" : "#111";
          return (
            <g key={c.id} opacity={op}
               onMouseEnter={() => setHover(c.id)}
               onMouseLeave={() => setHover(null)}
               onClick={e => { e.stopPropagation(); setSelected(c.id === selected ? null : c.id); }}
               style={{ cursor: "pointer" }}>
              {c.inertia && <rect x={cx-2} y={cy-14} width={4} height={28} fill="#222"/>}
              <circle cx={cx} cy={cy} r="7" fill={fill} stroke="#222" strokeWidth="1.5"/>
              <text x={cx+11} y={cy+4} fontSize="11" fill={c.anchor ? "#111" : "#111"}>
                {c.name}
              </text>
              {c.anchor && <text x={cx} y={cy+3} fontSize="9" fill={textColor} textAnchor="middle">U</text>}
            </g>
          );
        })}

        {hover && (() => {
          const c = byId[hover];
          const cx = xS(c.x), cy = yS(c.y);
          const boxW = 280;
          return (
            <g pointerEvents="none">
              <rect x={Math.min(cx+14, W-boxW-10)} y={Math.max(cy-70, PAD.top+5)}
                    width={boxW} height="64" fill="#fff" stroke="#222" strokeWidth="1"/>
              <text x={Math.min(cx+20, W-boxW-4)} y={Math.max(cy-52, PAD.top+23)}
                    fontSize="11" fontWeight="600" fill="#111">{c.name} — {c.stage}</text>
              <foreignObject x={Math.min(cx+20, W-boxW-4)} y={Math.max(cy-44, PAD.top+30)}
                             width={boxW-12} height="48">
                <div xmlns="http://www.w3.org/1999/xhtml"
                     style={{ fontSize: "10px", lineHeight: "1.3", color: "#333" }}>
                  {c.rationale}
                </div>
              </foreignObject>
            </g>
          );
        })()}

        {/* Figure legend */}
        <g transform={`translate(${W-PAD.right+10}, ${PAD.top+10})`}>
          <rect x="0" y="0" width="195" height="220" fill="#fff" stroke="#222"/>
          <text x="10" y="16" fontSize="11" fontWeight="600" fill="#111">Legend</text>

          <circle cx="20" cy="36" r="6" fill="#fff" stroke="#222"/>
          <text x="32" y="40" fontSize="10" fill="#333">Component</text>

          <circle cx="20" cy="56" r="6" fill="#222"/>
          <text x="32" y="60" fontSize="10" fill="#333">Anchor (user)</text>

          <line x1="10" y1="78" x2="30" y2="78" stroke="#777" strokeWidth="1"/>
          <text x="34" y="82" fontSize="10" fill="#333">Dependency</text>

          <line x1="10" y1="98" x2="26" y2="98" stroke="#c0392b" strokeWidth="1.5" strokeDasharray="5 3"/>
          <polygon points="30,98 24,95 24,101" fill="#c0392b"/>
          <text x="34" y="102" fontSize="10" fill="#333">Evolution arrow</text>

          <rect x="18" y="112" width="4" height="20" fill="#222"/>
          <text x="34" y="126" fontSize="10" fill="#333">Inertia marker</text>

          <text x="10" y="150" fontSize="10" fontWeight="600" fill="#111">Stages (x-axis)</text>
          <text x="10" y="166" fontSize="9" fill="#555">Genesis      0.00–0.17</text>
          <text x="10" y="180" fontSize="9" fill="#555">Custom       0.18–0.39</text>
          <text x="10" y="194" fontSize="9" fill="#555">Product      0.40–0.69</text>
          <text x="10" y="208" fontSize="9" fill="#555">Commodity    0.70–1.00</text>
        </g>
      </svg>
    </div>
  );
}
```

## Component Evolution Assessment

| Component | Stage | Position [vis, mat] | Rationale |
|---|---|---|---|
| Individuals | Anchor | [0.96, 0.50] | One of three trust-holding constituencies in the brief; placed centrally on x because individual trust is a neutral aggregate. |
| Government | Anchor | [0.96, 0.40] | Regulator / policymaker anchor; placed left-of-centre to reflect its bias toward novel/regulatory concerns. |
| Business | Anchor | [0.96, 0.60] | Deployer / commercial anchor; placed right-of-centre to reflect its bias toward commercial/mature inputs. |
| Trusted AI Output | Genesis | [0.86, 0.15] | In June 2023 there is no cross-industry agreement on what a "trustworthy AI output" even is. NIST AI RMF (Jan 2023) is freshly published and is a framework, not a definition. |
| Safety | Custom-Built | [0.82, 0.25] | OpenAI, Anthropic, DeepMind, Meta each run bespoke safety programmes with non-comparable eval suites. Recognised as a need but not standardised. |
| Reputation | Product | [0.80, 0.55] | Business reputation is a mature construct with established measurement (NPS, brand tracking, media monitoring). The AI-specific reputational risks are novel but the measurement methods are not. |
| Competitive Advantage | Product | [0.78, 0.60] | Strategy/economics concept with standard frameworks (resource-based view, Porter's five forces). Its *AI drivers* are new, but the outcome itself is well-defined. |
| Regulations | Custom-Built | [0.70, 0.20] | EU AI Act in trilogue after Parliament's May 2023 vote; US has only the Blueprint for an AI Bill of Rights (Oct 2022, non-binding). Each jurisdiction is drafting bespoke regimes; nothing is enforced on AI specifically. |
| AI Policy | Custom-Built | [0.64, 0.25] | Corporate AI use-policies are being drafted ad-hoc; no standard vendor template. Early consultancy offerings exist but each engagement is bespoke. |
| Audits | Custom-Built | [0.60, 0.30] | Boutique firms (ORCAA, Trail of Bits, Holistic AI, Credo) exist and charge premium rates for bespoke AI audits. No certified methodology comparable to SOC 2 or ISO 27001 yet. |
| Benchmarks | Product | [0.55, 0.45] | HELM (Stanford CRFM, Nov 2022), MMLU (2020), BIG-bench (2022), HumanEval (2021) are widely cited with comparable numbers across models. Fragmenting and gameable, but Product stage. |
| Feedback Loops | Custom-Built | [0.48, 0.32] | RLHF is the de facto method post-InstructGPT (2022), but each lab's data-labelling, reward-model and PPO pipeline is bespoke. Third-party RLHF-as-a-service (Scale, Surge) is early Product at best. |
| Constitution | Genesis | [0.45, 0.10] | Anthropic's Constitutional AI paper (Dec 2022) introduced the approach; only Claude ships it in production in June 2023. Novel; not independently replicated. |
| Forensics | Genesis | [0.42, 0.10] | OpenAI withdrew its AI-text classifier Jan 2023 citing low accuracy. Watermarking (Kirchenbauer et al., 2023) is a preprint with no production deployment. Fundamentally pre-product. |
| AI Models | Custom-Built (inertia) | [0.33, 0.33] | Frontier models (GPT-4, Claude, PaLM 2, Llama) are bespoke, closed-weight, built by a handful of labs with $100M+ training runs. Inertia flag: 3-year training cycles and sunk cost resist rapid evolution. API access is product-like but the models themselves are not a product. |
| Algorithms | Product | [0.25, 0.60] | Transformer (Attention Is All You Need, 2017), RLHF (2017–2022), diffusion (2020) are all published, open, and taught as standard curriculum. Reference implementations plentiful (HuggingFace, nanoGPT). |
| Training Data | Custom-Built | [0.20, 0.35] | CommonCrawl is commodity, but the frontier labs' actual training mixes (licensed books, filtered web, code, synthetic data) are bespoke and secret. Data-vendor market is early (Scale, Appen) but fragmenting. |
| Compute | Commodity | [0.10, 0.82] | NVIDIA H100 / A100 on hyperscalers (AWS P5, GCP A3, Azure ND) — hourly pricing, standardised APIs, fungible across providers. Supply-constrained but commoditised. The one true utility in the stack. |

## Key Strategic Observations

1. **The trust stack inverts the compute stack.** Compute is the most mature component (Commodity) but sits at the bottom of the value chain. The things that actually *produce trust* — Constitution, Forensics, Trusted AI Output itself — are the *least* mature (Genesis). Trust is load-bearing on the weakest part of the stack.

2. **A cluster of Genesis components at mid-visibility is a structural fragility.** Constitution, Forensics, and Trusted AI Output all sit in the 0.10–0.20 maturity band. Whenever individuals or government ask "can we trust this output?", the dependency chain terminates in three novel, unproven mechanisms. This is the direct answer to the brief's "where is trust fragile" question.

3. **Models have inertia; everything *around* them is evolving faster.** AI Models are Custom-Built with strong inertia (3-year training cycles, $100M+ sunk cost, closed-weight moat). Meanwhile Benchmarks, Feedback Loops, and Regulations are all predicted to move right within 12–18 months. The control and evaluation layer is commoditising *faster than the thing it's trying to control*.

4. **The governance band is a three-way race between regulators, auditors, and benchmarks.** Benchmarks are the furthest right (Product), Audits and Regulations trail at Custom-Built. The industry reading: for the next 12 months, benchmark scores will be the de facto regulatory proxy — whatever the AI Act ultimately requires.

5. **Differentiation is migrating into Training Data and Constitution.** Algorithms are published (Product); Compute is rented (Commodity); Models themselves will commoditise as open weights catch up (Llama 2 two months away in June 2023). The durable moats are (a) proprietary training data and (b) novel alignment approaches like Constitutional AI. Expect attention and capital to concentrate there.

## Doctrine Check

- **Know your users (Phase I, Communication)**: The map has three distinct anchors with different dependency patterns — individuals and government lean on Safety and Regulations; business leans on Reputation, Competitive Advantage, and raw Model capability. Multiple anchors are correctly represented rather than collapsed into "users".
- **Focus on user needs (Phase I, Leading)**: The outcome band (Trusted AI Output, Safety, Reputation, Competitive Advantage) is explicitly drawn from user needs, not from internal capability.
- **Use appropriate methods (Phase I, Development)**: The map reveals a likely method mismatch — Genesis components (Constitution, Forensics) require agile experimentation, but they are becoming load-bearing for regulatory compliance, which demands Six Sigma-grade assurance. This is a doctrine violation waiting to happen.
- **Manage inertia (Phase II, Leading)**: AI Models carry an explicit inertia marker. Frontier labs' training-cycle length and sunk cost will resist the evolution arrow pointing them toward Product; open-weights competitors (Meta, Mistral) are the external forcing function.
- **Remove bias and duplication (Phase I, Operations)**: Benchmarks are fragmenting (HELM, MMLU, BIG-bench, HumanEval, internal evals). This is a duplication signal that should — and likely will — consolidate as regulators demand canonical measurement.

## Build vs. Buy Assessment

| Component | Recommendation | Rationale |
|---|---|---|
| Constitution / Forensics (Genesis) | Invest / Build | No market alternative exists; any advance here is a durable advantage, and the AI-era patterns reference is explicit that AI accelerates prototyping at Genesis. |
| AI Models (Custom-Built, inertia) | Build only if you are a frontier lab; otherwise buy API | Training frontier models is a $100M+ capability bet. Downstream deployers should consume via API. |
| Training Data (Custom-Built) | Build proprietary blends | Public web is commodity; proprietary data is where durable differentiation is migrating (AI-era pattern: value migration upward). |
| Audits / AI Policy / Regulations-compliance | Buy-or-contract (bespoke) | Boutique firms exist; methodology not yet standardised, so expect premium pricing and bespoke engagements. |
| Benchmarks (Product) | Buy / use published | HELM, MMLU, HumanEval are free and comparable; running your own is only justified for specialised domains. |
| Feedback Loops (Custom-Built → Product) | Hybrid | Scale AI / Surge handle labelling; the reward-model and RL training are still worth owning. The "prototype first, decide second" pattern from the AI-era reference applies: prototype with vendors, own the long-term pipeline. |
| Algorithms (Product) | Buy / use open-source | Transformer and RLHF reference implementations are production-ready open source. No economic case for reinvention. |
| Compute (Commodity) | Buy / outsource | Hyperscaler GPU. AI-era reference is explicit: don't rebuild commodities. |

## Evolution Predictions (12–24 months, i.e. through mid-2025)

- **AI Models**: 0.33 → 0.55. Open weights (Llama 2, Mistral, Falcon) commoditise the Custom-Built frontier. Closed-weight frontier labs retain a lead but the gap compresses. (Evolution arrow on map.)
- **Benchmarks**: 0.45 → 0.65. Regulators (especially the EU AI Act conformity-assessment track) will demand canonical evaluation, pushing benchmarks deeper into Product. (Evolution arrow on map.)
- **Regulations**: 0.20 → 0.40. EU AI Act enters force (projected 2024–2025); US executive action plus state-level laws (Colorado, NYC) come online. Still bespoke-per-jurisdiction, but crossing into late Custom-Built. (Evolution arrow on map.)
- **Feedback Loops (RLHF)**: 0.32 → 0.55. RLHF-as-a-service (Scale, Surge, OpenAI fine-tuning) matures; DPO / RLAIF reduce labelling cost. (Evolution arrow on map.)
- **Constitution**: likely stays Genesis through 2024; expected to become Custom-Built only if independently replicated by a second lab.
- **Forensics**: highest uncertainty — either breakthrough watermarking standardises it rapidly, or it remains Genesis indefinitely because the underlying problem is adversarial.
- **Inertia risks**: Frontier labs with $100M+ sunk cost in closed-weight models face the AI-era "inertia paradox" — open-weights competitors can replicate capability in weeks, while the incumbent resists restructuring its stack.

## What's Differentiating vs. Commoditising (the brief's explicit question)

**Commoditising (buy, don't build):**
- Compute (already commodity)
- Algorithms (Product, open-source)
- Benchmarks (Product → deeper Product)
- Basic training data (CommonCrawl, open code corpora)

**Still differentiating (build, invest):**
- Proprietary training data blends (licensed books, curated code, synthetic data)
- Constitutional-style alignment methods
- Forensics / watermarking (whoever cracks this owns the trust layer)
- AI-orchestration / context-engineering skills (AI-era reference; not shown explicitly but implicit in Feedback Loops)

**Fragile (trust depends on these but they are Genesis):**
- Constitution (one production deployment globally)
- Forensics (active failure — OpenAI classifier withdrawn)
- Trusted AI Output itself (no industry definition)

## Open Questions

1. Does the EU AI Act's conformity assessment regime pick a canonical benchmark suite, or does it defer to "state of the art"? The answer determines whether Benchmarks evolve to Product or Commodity.
2. Do open-weights frontier models (Llama 2, Mistral) actually close the gap with closed-weight labs within 12 months, or does the compute/data moat hold?
3. Does any jurisdiction mandate provenance/forensics for AI outputs? If yes, it forces Forensics from Genesis to Custom-Built via regulatory pull regardless of technical maturity.

---

*This analysis was produced following the haberlah `wardley-mapping` skill (SKILL.md Steps 1–7). The Step 1 strategic-context questions were answered from the scenario brief because no live user was available. No iteration against an external validator was performed; this is a first complete pass per the benchmark contract.*
