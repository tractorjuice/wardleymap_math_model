# Wardley Map Analysis: Regenerative Farming Landscape (August 2022)

## Purpose

This map answers the brief directly: **In August 2022, where along the farming value chain is regenerative agriculture still knowledge-based, where has industrial (extractive) practice locked in, and how much supply-chain awareness links the soil to the shopping basket?** It is a landscape map covering a sector — not a build-vs-buy decision for a single firm. The strategic decision it supports is *where intervention is most leveraged*: at the treaty layer, the certification layer, the measurement layer, or the practice layer itself.

## Strategic Context (answered from the brief)

The skill's Step 1 asks four clarifying questions. Because this benchmark delivers the scenario as a single prompt, the answers below were inferred from the brief — they were not solicited from a live user.

| Question | Answer used |
|---|---|
| Strategic question | "Where is regenerative farming still knowledge-based, where has industrial lock-in commoditised the extractive model, and what does the supply-chain awareness picture look like?" |
| User anchors | Farmers, Consumers, Retailers, Certification Bodies, National Governments, UN/supranational bodies — all six are named in the brief |
| Core needs | Regenerative practices at farm level; measurable soil outcomes; credible labelling; treaty/policy cover; supply-chain visibility for buyers |
| Scope boundary | Global food system, August 2022, sector-level (no single firm) |

## Value Chain Overview

The map stacks six anchors at the top and follows the chain down through four bands:

- **Market-visibility band (0.75–0.86)**: Supply-Chain Awareness, Eco-Label/Grading, Regenerative Certification, Organic Certification — how the farm connects to the consumer.
- **Policy & measurement band (0.55–0.72)**: Farm Subsidies & Policy, Climate & Biodiversity Treaties, Soil Carbon Measurement, Regenerative Practices — the instruments that reward or constrain behaviour.
- **Practice band (0.38–0.50)**: Crop Rotation & Diversity, Monoculture at Scale, Conservation & Substrate — what is actually being done on the land.
- **Substrate band (0.15–0.28)**: Soil Microbiome, Photosynthesis, Petrochemical Inputs — the physical and chemical energy matrix beneath the soil.

The key tension the map reveals: the industrial side (Monoculture + Petrochemical Inputs) is deep in Commodity; the regenerative side is spread from Genesis (Soil Microbiome, Soil Carbon Measurement) through Custom-Built (Regenerative Practices, Regenerative Certification) with no component yet at Product.

## OWM (OnlineWardleyMaps) Text Block

```
title Regenerative Farming Landscape (August 2022)
style wardley

anchor Consumers [0.97, 0.70]
anchor Farmers [0.97, 0.40]
anchor Retailers [0.94, 0.62]
anchor National Governments [0.94, 0.30]
anchor UN / Supranational Bodies [0.94, 0.18]
anchor Certification Bodies [0.94, 0.50]

component Supply-Chain Awareness [0.86, 0.30]
component Eco-Label / Grading [0.82, 0.45]
component Regenerative Certification [0.78, 0.18]
component Organic Certification [0.75, 0.70]
component Farm Subsidies & Policy [0.72, 0.40]
component Climate & Biodiversity Treaties [0.68, 0.32]
component Soil Carbon Measurement [0.62, 0.15]
component Regenerative Practices [0.55, 0.22]
component Crop Rotation & Diversity [0.50, 0.50]
component Monoculture at Scale [0.48, 0.88] inertia
component Conservation & Substrate [0.38, 0.28]
component Soil Microbiome [0.28, 0.12]
component Photosynthesis [0.18, 0.95]
component Petrochemical Inputs [0.15, 0.85] inertia

Consumers->Eco-Label / Grading
Consumers->Supply-Chain Awareness
Consumers->Organic Certification
Retailers->Supply-Chain Awareness
Retailers->Eco-Label / Grading
Retailers->Organic Certification
Farmers->Regenerative Practices
Farmers->Monoculture at Scale
Farmers->Crop Rotation & Diversity
Farmers->Farm Subsidies & Policy
Certification Bodies->Regenerative Certification
Certification Bodies->Organic Certification
Certification Bodies->Soil Carbon Measurement
National Governments->Farm Subsidies & Policy
National Governments->Climate & Biodiversity Treaties
UN / Supranational Bodies->Climate & Biodiversity Treaties

Supply-Chain Awareness->Eco-Label / Grading
Supply-Chain Awareness->Regenerative Certification
Supply-Chain Awareness->Organic Certification
Eco-Label / Grading->Regenerative Certification
Eco-Label / Grading->Organic Certification
Regenerative Certification->Soil Carbon Measurement
Regenerative Certification->Regenerative Practices
Organic Certification->Crop Rotation & Diversity
Organic Certification->Conservation & Substrate
Farm Subsidies & Policy->Monoculture at Scale
Farm Subsidies & Policy->Regenerative Practices
Farm Subsidies & Policy->Crop Rotation & Diversity
Farm Subsidies & Policy->Climate & Biodiversity Treaties
Climate & Biodiversity Treaties->Soil Carbon Measurement
Soil Carbon Measurement->Soil Microbiome
Soil Carbon Measurement->Conservation & Substrate
Regenerative Practices->Crop Rotation & Diversity
Regenerative Practices->Conservation & Substrate
Regenerative Practices->Soil Microbiome
Crop Rotation & Diversity->Soil Microbiome
Crop Rotation & Diversity->Photosynthesis
Monoculture at Scale->Petrochemical Inputs
Monoculture at Scale->Photosynthesis
Conservation & Substrate->Soil Microbiome
Soil Microbiome->Photosynthesis

evolve Regenerative Certification 0.45
evolve Soil Carbon Measurement 0.40
evolve Supply-Chain Awareness 0.55
evolve Regenerative Practices 0.45
evolve Climate & Biodiversity Treaties 0.55

annotation 1 [[0.50, 0.10]] Lock-in zone: Monoculture + Petrochemical Inputs are Commodity with explicit inertia — subsidies, seed/fertiliser supply chains, and insurance are optimised for this state.
annotation 2 [[0.28, 0.18]] Knowledge frontier: Soil Microbiome and Soil Carbon Measurement are Genesis — the scientific foundations of regen farming are not yet measurable at scale.
annotation 3 [[0.85, 0.18]] Supply-chain awareness is Custom-Built; each retailer's traceability stack is bespoke. It's the bottleneck translating farm practice into consumer choice.
annotation 4 [[0.70, 0.85]] Regen vs. organic: Organic is Product (mature standards, 50+ years); Regenerative is Genesis (ROC launched 2020, Savory EOV, Regen Network all competing, no consensus).
```

## Interactive React Artifact

```jsx
import React, { useState } from "react";

const COMPONENTS = [
  { id: "consumers", name: "Consumers", x: 0.70, y: 0.97, stage: "Anchor", anchor: true,
    rationale: "One of six named user groups. Drive demand via purchase behaviour, read labels more than supply-chain data." },
  { id: "farmers", name: "Farmers", x: 0.40, y: 0.97, stage: "Anchor", anchor: true,
    rationale: "Practice-level anchor. Choice of practice is bounded by subsidy incentives and the supply chain they sell into." },
  { id: "retailers", name: "Retailers", x: 0.62, y: 0.94, stage: "Anchor", anchor: true,
    rationale: "Gatekeepers between farm and consumer; drive private-label eco claims and retailer-specific traceability schemes." },
  { id: "nat-gov", name: "National Governments", x: 0.30, y: 0.94, stage: "Anchor", anchor: true,
    rationale: "Policy anchor. Hold subsidy purse strings (CAP, US Farm Bill, USDA) and implement treaty commitments." },
  { id: "un", name: "UN / Supranational Bodies", x: 0.18, y: 0.94, stage: "Anchor", anchor: true,
    rationale: "FAO, UNFCCC, UNCCD, CBD. Set the treaty frame (Koronivia, post-2020 Biodiversity Framework in final drafting for COP15 Dec 2022)." },
  { id: "cert-bodies", name: "Certification Bodies", x: 0.50, y: 0.94, stage: "Anchor", anchor: true,
    rationale: "Organic regulators (USDA NOP, EU 2018/848), Regenerative Organic Alliance, Savory Institute, Regen Network. Translate practice into market signal." },

  { id: "supply-awareness", name: "Supply-Chain Awareness", x: 0.30, y: 0.86, stage: "Custom-Built",
    rationale: "Each retailer runs a bespoke traceability stack (Walmart/IBM Food Trust, Tesco traceability, Carrefour blockchain pilot). No cross-industry standard in 2022." },
  { id: "eco-label", name: "Eco-Label / Grading", x: 0.45, y: 0.82, stage: "Custom-Built",
    rationale: "Dozens of competing eco-scores (Eco-Score, Foundation Earth, Planet Score, HowGood) announced 2021-22; the EU PEF methodology still under consultation. Fragmented, bespoke, not comparable." },
  { id: "regen-cert", name: "Regenerative Certification", x: 0.18, y: 0.78, stage: "Genesis",
    rationale: "ROC (Regenerative Organic Certified) launched 2020 with 3 pilot farms at scale in 2022. Savory EOV and Regen Network A Greener World compete with incompatible criteria. No consensus definition of 'regenerative'." },
  { id: "organic-cert", name: "Organic Certification", x: 0.70, y: 0.75, stage: "Product",
    rationale: "USDA National Organic Program (2002), EU 2092/91→2018/848, IFOAM since 1972. Well-defined, enforced, tradeable, mutual-recognition treaties between blocs. 50+ years of codification." },
  { id: "subsidies", name: "Farm Subsidies & Policy", x: 0.40, y: 0.72, stage: "Product",
    rationale: "CAP (EU, ~€55bn/yr), US Farm Bill (~$25bn/yr), direct-payment and coupled schemes. Mature instruments but being re-tooled — CAP 2023-27 eco-schemes approved 2022; US Inflation Reduction Act (signed 16 Aug 2022) adds $19.5bn for climate-smart ag." },
  { id: "treaties", name: "Climate & Biodiversity Treaties", x: 0.32, y: 0.68, stage: "Custom-Built",
    rationale: "UNFCCC Paris Agreement (2015) has no specific ag text; Koronivia Joint Work on Agriculture concludes at COP27 (Nov 2022, two months away). UNCCD, CBD post-2020 framework still being negotiated for COP15 Dec 2022. Instrument exists but ag-specific detail is bespoke per treaty." },
  { id: "soil-c-measurement", name: "Soil Carbon Measurement", x: 0.15, y: 0.62, stage: "Genesis",
    rationale: "No accepted measurement standard. Soil sampling (expensive, spatially patchy), remote sensing (coarse), models (high uncertainty). Verra VM0042 methodology approved 2020 but buffer pools 20%+ show uncertainty. MRV is the named scientific bottleneck for soil carbon markets." },
  { id: "regen-practices", name: "Regenerative Practices", x: 0.22, y: 0.55, stage: "Custom-Built",
    rationale: "No-till, cover cropping, managed grazing, silvopasture, agroforestry — each practice reasonably well-known but the *combination* and *outcome* framing is bespoke per farm. Savory, Gabe Brown, Rodale, Kiss the Ground all promote different recipes." },
  { id: "crop-rotation", name: "Crop Rotation & Diversity", x: 0.50, y: 0.50, stage: "Product",
    rationale: "Crop rotation is pre-industrial best practice, codified in extension service guidance since the 1930s (USDA, INRA). Three-field and longer rotations, legume inclusion are textbook agronomy. Well-understood, but declining in share against monoculture." },
  { id: "monoculture", name: "Monoculture at Scale", x: 0.88, y: 0.48, stage: "Commodity", inertia: true,
    rationale: "Commodity scale row-cropping (maize, soy, wheat, palm, rice) — industrial standard for ~70 years, optimised by seed genetics (Bayer/Monsanto, Corteva), synthetic-fertiliser logistics, federal crop insurance, and commodity futures markets. Catastrophic failure-intolerance. Inertia: entire input/output value chain is co-optimised." },
  { id: "conservation", name: "Conservation & Substrate", x: 0.28, y: 0.38, stage: "Custom-Built",
    rationale: "Cover cropping, minimum tillage, hedgerows, buffer strips — published playbooks (USDA NRCS, UK Countryside Stewardship) exist but adoption is uneven and each farm's implementation is bespoke to soil type and climate." },
  { id: "soil-microbiome", name: "Soil Microbiome", x: 0.12, y: 0.28, stage: "Genesis",
    rationale: "Rhizosphere microbial ecology is an active research frontier (Earth Microbiome Project, NSF Dimensions of Biodiversity). Fungal-bacterial balance, mycorrhizal networks, glomalin — partially understood but not engineerable at scale. Papers are describe-type." },
  { id: "photosynthesis", name: "Photosynthesis", x: 0.95, y: 0.18, stage: "Commodity",
    rationale: "Universal natural process, physics/chemistry fully defined since the 1960s (Calvin cycle, Hill reaction). The one true utility in the stack — free, ubiquitous, catastrophic if disrupted." },
  { id: "petrochemicals", name: "Petrochemical Inputs", x: 0.85, y: 0.15, stage: "Commodity", inertia: true,
    rationale: "Synthetic N fertiliser (Haber-Bosch since 1913), glyphosate (off-patent since 2000), phosphate rock — commodity-priced, standardised, globally traded. Inertia: $200bn+ industry with refinery assets, distribution, and subsidies. 2022 price shock (gas → urea) is a climatic not structural signal." }
];

const LINKS = [
  ["consumers","eco-label"],["consumers","supply-awareness"],["consumers","organic-cert"],
  ["retailers","supply-awareness"],["retailers","eco-label"],["retailers","organic-cert"],
  ["farmers","regen-practices"],["farmers","monoculture"],["farmers","crop-rotation"],["farmers","subsidies"],
  ["cert-bodies","regen-cert"],["cert-bodies","organic-cert"],["cert-bodies","soil-c-measurement"],
  ["nat-gov","subsidies"],["nat-gov","treaties"],
  ["un","treaties"],
  ["supply-awareness","eco-label"],["supply-awareness","regen-cert"],["supply-awareness","organic-cert"],
  ["eco-label","regen-cert"],["eco-label","organic-cert"],
  ["regen-cert","soil-c-measurement"],["regen-cert","regen-practices"],
  ["organic-cert","crop-rotation"],["organic-cert","conservation"],
  ["subsidies","monoculture"],["subsidies","regen-practices"],["subsidies","crop-rotation"],["subsidies","treaties"],
  ["treaties","soil-c-measurement"],
  ["soil-c-measurement","soil-microbiome"],["soil-c-measurement","conservation"],
  ["regen-practices","crop-rotation"],["regen-practices","conservation"],["regen-practices","soil-microbiome"],
  ["crop-rotation","soil-microbiome"],["crop-rotation","photosynthesis"],
  ["monoculture","petrochemicals"],["monoculture","photosynthesis"],
  ["conservation","soil-microbiome"],
  ["soil-microbiome","photosynthesis"]
];

const EVOLUTIONS = [
  { id: "regen-cert", to: 0.45 },
  { id: "soil-c-measurement", to: 0.40 },
  { id: "supply-awareness", to: 0.55 },
  { id: "regen-practices", to: 0.45 },
  { id: "treaties", to: 0.55 }
];

const W = 1150, H = 720, PAD = { top: 60, right: 230, bottom: 70, left: 180 };
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
          Regenerative Farming Landscape — August 2022
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
          const op = (dim(a)||dim(b)) ? 0.08 : 0.5;
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
          return (
            <g key={c.id} opacity={op}
               onMouseEnter={() => setHover(c.id)}
               onMouseLeave={() => setHover(null)}
               onClick={e => { e.stopPropagation(); setSelected(c.id === selected ? null : c.id); }}
               style={{ cursor: "pointer" }}>
              {c.inertia && <rect x={cx-2} y={cy-14} width={4} height={28} fill="#222"/>}
              <circle cx={cx} cy={cy} r="7" fill={fill} stroke="#222" strokeWidth="1.5"/>
              <text x={cx+11} y={cy+4} fontSize="11" fill="#111">{c.name}</text>
              {c.anchor && <text x={cx} y={cy+3} fontSize="9" fill="#fff" textAnchor="middle">U</text>}
            </g>
          );
        })}

        {hover && (() => {
          const c = byId[hover];
          const cx = xS(c.x), cy = yS(c.y);
          const boxW = 300;
          return (
            <g pointerEvents="none">
              <rect x={Math.min(cx+14, W-boxW-10)} y={Math.max(cy-78, PAD.top+5)}
                    width={boxW} height="72" fill="#fff" stroke="#222" strokeWidth="1"/>
              <text x={Math.min(cx+20, W-boxW-4)} y={Math.max(cy-60, PAD.top+23)}
                    fontSize="11" fontWeight="600" fill="#111">{c.name} — {c.stage}</text>
              <foreignObject x={Math.min(cx+20, W-boxW-4)} y={Math.max(cy-52, PAD.top+30)}
                             width={boxW-12} height="56">
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
          <rect x="0" y="0" width="200" height="230" fill="#fff" stroke="#222"/>
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

          <text x="10" y="155" fontSize="10" fontWeight="600" fill="#111">Stages (x-axis)</text>
          <text x="10" y="171" fontSize="9" fill="#555">Genesis      0.00–0.17</text>
          <text x="10" y="185" fontSize="9" fill="#555">Custom       0.18–0.39</text>
          <text x="10" y="199" fontSize="9" fill="#555">Product      0.40–0.69</text>
          <text x="10" y="213" fontSize="9" fill="#555">Commodity    0.70–1.00</text>
        </g>
      </svg>
    </div>
  );
}
```

## Component Evolution Assessment

| Component | Stage | Position [vis, mat] | Rationale |
|---|---|---|---|
| Consumers | Anchor | [0.97, 0.70] | One of six named user groups; purchases through labels more than supply-chain data. |
| Farmers | Anchor | [0.97, 0.40] | Practice-level anchor; choice bounded by subsidies and offtake terms. |
| Retailers | Anchor | [0.94, 0.62] | Gatekeepers between farm and consumer; drive private-label eco claims. |
| National Governments | Anchor | [0.94, 0.30] | Hold subsidy purse strings (CAP, US Farm Bill); implement treaty commitments. |
| UN / Supranational Bodies | Anchor | [0.94, 0.18] | FAO, UNFCCC, UNCCD, CBD — set the treaty frame (post-2020 GBF, Koronivia). |
| Certification Bodies | Anchor | [0.94, 0.50] | USDA NOP, EU organic, ROC, Savory, Regen Network, A Greener World. |
| Supply-Chain Awareness | Custom-Built | [0.86, 0.30] | Every retailer runs a bespoke traceability stack (Walmart/IBM Food Trust, Tesco, Carrefour blockchain pilot). No cross-industry standard in Aug 2022; EU Digital Product Passport is a 2022 legislative proposal, not yet law. |
| Eco-Label / Grading | Custom-Built | [0.82, 0.45] | Eco-Score, Foundation Earth, Planet Score, HowGood all competing for shelf space in 2021–22. EU PEF methodology in consultation. Multiple methodologies, no comparability, consumer confusion — classic Custom-Built fragmentation. |
| Regenerative Certification | Genesis | [0.78, 0.18] | ROC launched 2020 (scaled to ~20 farms globally by 2022); Savory EOV, Regen Network and A Greener World all compete with incompatible criteria. No consensus definition of "regenerative" even exists — some schemes require organic, others don't. Novel, unproven at scale. |
| Organic Certification | Product | [0.75, 0.70] | USDA NOP (2002), EU 2018/848, IFOAM since 1972. Mutual-recognition treaties between blocs. Well-understood, documented, audited, tradeable. Market fragmenting (EU pulling away on gene-editing rules) but Product stage. |
| Farm Subsidies & Policy | Product | [0.72, 0.40] | CAP (~€55bn/yr), US Farm Bill (~$25bn/yr). Mature instruments with decades of administrative codification. Being re-tooled (CAP 2023-27 eco-schemes approved 2022; US Inflation Reduction Act signed 16 Aug 2022 adds $19.5bn climate-smart ag) — Product-stage but under active feature competition. |
| Climate & Biodiversity Treaties | Custom-Built | [0.68, 0.32] | UNFCCC/Paris (2015) has no ag-specific text; Koronivia Joint Work concludes at COP27 (Nov 2022); CBD post-2020 Global Biodiversity Framework still being drafted for COP15 Dec 2022. Instrument exists as a class but ag content is bespoke per treaty, not standardised. |
| Soil Carbon Measurement | Genesis | [0.62, 0.15] | No accepted MRV standard. Soil sampling is expensive and spatially patchy; remote sensing is coarse; models are high-uncertainty. Verra VM0042 methodology approved 2020 but carries 20%+ buffer pools reflecting measurement uncertainty. Named as the scientific bottleneck for soil carbon markets. |
| Regenerative Practices | Custom-Built | [0.55, 0.22] | Constituent practices (no-till, cover cropping, managed grazing, silvopasture, agroforestry) are reasonably known, but the *combination* and outcome framing is bespoke per farm. Savory, Gabe Brown, Rodale, Kiss the Ground promote different recipes. Build-type papers abound. |
| Crop Rotation & Diversity | Product | [0.50, 0.50] | Pre-industrial best practice, codified in extension service guidance since the 1930s. Three-field and longer rotations, legume inclusion, cover crops — textbook agronomy. Well-understood but losing share to monoculture on commodity row-crops. |
| Monoculture at Scale | Commodity (inertia) | [0.48, 0.88] | Industrial-scale row-cropping (maize, soy, wheat, palm, rice) — the industry standard for ~70 years. Optimised by seed genetics (Bayer, Corteva, Syngenta), synthetic-fertiliser logistics, federal crop insurance, and commodity futures. Catastrophic failure-intolerance. Explicit inertia: every adjacent component in the input-output value chain is co-optimised for this state. |
| Conservation & Substrate | Custom-Built | [0.38, 0.28] | Cover cropping, minimum tillage, hedgerows, buffer strips — published playbooks (USDA NRCS, UK Countryside Stewardship) but adoption is uneven and each farm's implementation is soil-and-climate-specific. Build-type knowledge. |
| Soil Microbiome | Genesis | [0.28, 0.12] | Rhizosphere microbial ecology is an active research frontier (Earth Microbiome Project; NSF Dimensions of Biodiversity). Fungal-bacterial balance, mycorrhizal networks, glomalin — partially understood, not engineerable at scale. Describe-type papers. |
| Photosynthesis | Commodity | [0.18, 0.95] | Universal natural process, physics/chemistry fully defined since the 1960s (Calvin cycle, Hill reaction). The one true utility in the stack — ubiquitous, free, catastrophic if disrupted. Placed explicitly as a commodity per the brief's "energy matrix beneath the soil". |
| Petrochemical Inputs | Commodity (inertia) | [0.15, 0.85] | Synthetic N fertiliser (Haber-Bosch, 1913), glyphosate (off-patent 2000), phosphate rock — commodity-priced, standardised, globally traded. Inertia: $200bn+ industry with refinery assets, distribution infrastructure, and subsidies. 2022 price shock (European gas → urea price) is climatic disruption of a commodity, not its replacement. |

## Key Strategic Observations

1. **The map is explicitly barbell-shaped.** The industrial side (Monoculture at Scale, Petrochemical Inputs) sits at maturity 0.85–0.88 with inertia markers. The regenerative side (Soil Microbiome, Soil Carbon Measurement, Regenerative Certification) clusters at 0.12–0.18. Nothing on the regenerative side has yet reached Product. This is the brief's "what's still knowledge-based vs. where industrial practice has locked in" answered visually: industrial is commoditised, regenerative is still Genesis and Custom-Built.

2. **The scientific foundation is the weakest link.** Soil Microbiome (0.12) and Soil Carbon Measurement (0.15) are the two most left-of-map components, and both are load-bearing for every regenerative certification scheme. Until MRV (measurement, reporting, verification) of soil carbon becomes measurable at farm scale, no credible regenerative label can be priced. This is why 2022 soil carbon credits carry 20%+ buffer pools — the uncertainty is in the *science*, not the policy.

3. **Supply-chain awareness is the bottleneck translating farm into consumer.** At 0.86 visibility and 0.30 maturity, Supply-Chain Awareness is the single component every consumer-facing actor depends on but no one has commoditised. Retailers each run bespoke traceability (IBM Food Trust, blockchain pilots, private-label audits). Without a standardised supply-chain data layer, eco-labels are rhetoric and regenerative premiums can't be underwritten. Evolution arrow points right toward Product (0.55) driven by the EU Digital Product Passport proposal (March 2022) and FDA FSMA 204 traceability rule (Nov 2022).

4. **Regenerative and organic are at different stages of the same axis.** Organic Certification is Product (0.70) — 50 years of codification, USDA and EU regulatory recognition, tradeable across blocs. Regenerative Certification is Genesis (0.18) — three competing schemes (ROC, Savory EOV, Regen Network) with incompatible criteria. The evolution arrow for Regenerative (→ 0.45) predicts it will consolidate into Custom-Built / early Product by 2024–25 as one scheme dominates and regulators pick a winner. Organic is the template for what that looks like.

5. **Policy is the fastest-moving Product component.** Farm Subsidies & Policy (0.72, Product) gained two major updates within weeks either side of the map's date: CAP 2023-27 eco-schemes approved June 2022; US Inflation Reduction Act signed 16 August 2022 with $19.5bn for climate-smart ag. These are feature-level updates to a Product-stage instrument, not a stage change. They explain why the evolution arrow for Regenerative Practices points right — public money is underwriting the demand side.

6. **Monoculture has inertia but also a climatic destabilisation.** The 2022 European gas crisis pushed urea to 4x historical prices, revealing how much industrial yield depends on cheap petrochemical inputs. This doesn't move Petrochemical Inputs off Commodity — the input is still standardised and fungible — but it destabilises the *economics* of the monoculture system that depends on it. Inertia from sunk cost + insurance + futures markets resists the signal, which is exactly why the inertia marker matters.

## Doctrine Check

- **Know your users (Phase I, Communication)**: Six distinct anchors with different dependency patterns. Farmers lean on Subsidies and Practices; Consumers on Labels and Organic Cert; Retailers on Supply-Chain Awareness; Governments on Subsidies and Treaties; UN on Treaties; Certification Bodies on Regen and Organic Cert plus Soil-C Measurement. The map does *not* collapse these into a single "users" anchor — Wardley doctrine compliant.
- **Use appropriate methods (Phase I, Development)**: A critical violation visible on the map — Regenerative Certification (Genesis) is increasingly being asked to deliver audit-grade verification for soil carbon markets, which is a Six Sigma demand on an Agile-stage component. This is the method mismatch that explains high buffer pools in the voluntary carbon market.
- **Manage inertia (Phase II, Leading)**: Two inertia markers (Monoculture, Petrochemical Inputs) reflect the locked-in industrial system. Both are downstream of the Farmers anchor via Subsidies — so the inertia is as much political as technical. The map correctly flags that any strategy that ignores the inertia will fail at implementation.
- **Remove bias and duplication (Phase I, Operations)**: The Eco-Label / Grading band shows active duplication — four competing eco-scores launched 2021–22, none interoperable. This is a duplication signal that should consolidate under regulatory pressure (EU PEF, FDA) within 18–24 months.
- **Challenge assumptions (Phase I, Communication)**: The assumption most at risk in this map is that "regenerative = organic + more". Regenerative Certification schemes differ on whether synthetic inputs are ever permissible; the map positions them as separate components for that reason.

## Build vs. Buy Assessment

The brief is sector-level, not firm-level, so "build vs. buy" translates into "invest vs. leverage" for each class of actor.

| Component | Recommendation | Rationale |
|---|---|---|
| Soil Microbiome science (Genesis) | Public R&D investment | No market will fund this; needs NSF/UKRI/Horizon-scale funding. Classic Genesis: high failure tolerance, describe-type papers, no market. |
| Soil Carbon Measurement (Genesis) | Build via public-private consortium | Too uncertain for market alone; too load-bearing for regen markets to wait. Precedent: SoilC GHG inventory work under UNFCCC, USDA CEAP. |
| Regenerative Certification (Genesis) | Do not yet trust a single scheme | Multiple competing schemes; any single adoption is a bet on a pre-consolidation market. Retailers should run parallel pilots, not mass-certify. |
| Organic Certification (Product) | Leverage / buy | Mature, audited, traded. Retailers should use existing certification directly; no case for bespoke alternatives. |
| Supply-Chain Awareness (Custom-Built → Product) | Hybrid; buy traceability platform, own the data schema | Platform layer (IBM Food Trust, GS1, EPCIS) is buyable; data semantics (what attributes represent "regenerative") are still differentiating. |
| Eco-Label / Grading (Custom-Built) | Wait for regulatory consolidation | EU PEF is coming 2023–24; early adopters of any single methodology risk stranded assets. Hedge across 2–3 leading labels. |
| Farm Subsidies & Policy (Product) | Influence, don't replace | The mechanism is Product-stage; the *content* is where policy influence matters. IRA-style climate-smart ag conditioning is the template. |
| Regenerative Practices at farm level (Custom-Built) | Subsidise adoption; don't mandate | Practices work but are site-specific; mandate creates friction. Incentive-based adoption is the CAP and IRA approach. |
| Monoculture (Commodity) | Transition, don't demolish | Commodity-stage with inertia; a collapse would be catastrophic for food security. Policy tool is gradual decoupling of subsidies from commodity acreage. |
| Petrochemical Inputs (Commodity) | Substitute at the margin | Commodity with inertia. Biological N (Pivot Bio, Azotic), precision application, and crop rotation reduce demand without disrupting supply. |

## Evolution Predictions (12–24 months, i.e. through mid-2024)

- **Regenerative Certification**: 0.18 → 0.45. One or two schemes will dominate (most likely ROC + Savory EOV mutual recognition) as retailer demand forces consolidation. (Evolution arrow on map.)
- **Soil Carbon Measurement**: 0.15 → 0.40. Remote-sensing + on-farm sampling hybrid methodologies will standardise under Verra/Gold Standard + regulatory pull from the EU Carbon Removal Certification Framework (proposed Nov 2022). (Evolution arrow.)
- **Supply-Chain Awareness**: 0.30 → 0.55. EU Digital Product Passport (regulation likely 2023–24) + FDA FSMA 204 (compliance Jan 2026) push retailers toward interoperable traceability. (Evolution arrow.)
- **Regenerative Practices**: 0.22 → 0.45. IRA-funded ($19.5bn) adoption at US scale + CAP 2023-27 eco-schemes create a quasi-Product offering among cooperatives and farm-service providers. (Evolution arrow.)
- **Climate & Biodiversity Treaties**: 0.32 → 0.55. Koronivia outcomes at COP27 (Nov 2022), GBF at COP15 (Dec 2022), and the EU Nature Restoration Law (proposed June 2022) turn ag-specific treaty language from bespoke into a more standardised instrument. (Evolution arrow.)
- **Monoculture at Scale**: stays at 0.88 with inertia. 2022 petrochemical price shock causes economic stress but does not move the stage. 2023–24 may see a partial decoupling of subsidies from commodity acreage (CAP eco-schemes) but the Commodity stage itself is sticky.
- **Organic Certification**: stays at 0.70 Product. Continued gradual growth (~5%/yr in EU/US) but no stage change. EU-US tension over gene-editing rules is feature-level divergence within Product, not stage change.

## What's Knowledge-Based vs. Locked-In (the brief's explicit question)

**Knowledge-based (Genesis / Custom-Built, left of map):**
- Soil Microbiome — active research frontier
- Soil Carbon Measurement — no standard MRV at scale
- Regenerative Certification — competing pre-consolidation schemes
- Regenerative Practices — known components but bespoke recipes
- Conservation & Substrate — playbooks exist but site-specific
- Climate & Biodiversity Treaties — ag-specific text still being negotiated
- Supply-Chain Awareness — bespoke traceability per retailer
- Eco-Label / Grading — multiple incompatible methodologies

**Locked in (Commodity, right of map):**
- Monoculture at Scale (inertia) — 70-year industrial standard
- Petrochemical Inputs (inertia) — $200bn+ integrated supply chain
- Photosynthesis — universal and free (the only benign commodity in the stack)

**Product, settled but not locked:**
- Organic Certification — 50 years of codification
- Farm Subsidies & Policy — mature instrument, active feature development
- Crop Rotation & Diversity — textbook agronomy, declining share

## Supply-Chain Awareness Picture (the brief's second explicit question)

The map frames supply-chain awareness as the critical translator between what farmers do and what consumers can see. In August 2022 it is Custom-Built (0.30): every major retailer is running a bespoke traceability stack. Walmart/IBM Food Trust is the most production-ready (mandatory for leafy greens since 2019). Carrefour ran blockchain pilots since 2018. Tesco added a proprietary traceability service in 2020. GS1 EPCIS 2.0 (published 2022) is the nearest thing to a shared standard but adoption is uneven.

The two forcing functions visible on the map are the EU Digital Product Passport (European Commission proposal, March 2022, targeting 2024–27 sectoral rollouts) and the US FDA FSMA 204 Food Traceability Rule (finalised November 2022 with a January 2026 compliance date). Both pull the component right toward Product (evolution arrow → 0.55). For a farmer or a retailer in August 2022, the strategic question is whether to commit to a single platform now (risk of stranded asset) or hedge across two platforms until the regulatory winner is clear.

## Open Questions

1. Does the EU Carbon Removal Certification Framework (expected Nov 2022) pick a canonical soil-carbon methodology? If yes, it drags Soil Carbon Measurement and Regenerative Certification right faster than the map predicts.
2. Does the CAP 2023-27 eco-scheme allocation (24% of Pillar 1 = ~€9bn/yr) create enough adoption pull to move Regenerative Practices into Product within 24 months, or does member-state implementation keep it Custom-Built?
3. If petrochemical input prices stay 2–3x 2020 levels through 2023 (plausible given Russia sanctions), does the economic signal override the inertia on Monoculture at Scale, and how fast?

---

*This analysis was produced following the haberlah `wardley-mapping` skill (SKILL.md Steps 1–7). Step 1 strategic-context questions were answered from the scenario brief because no live user was available. No iteration against an external validator was performed; this is a first complete pass per the benchmark contract.*
