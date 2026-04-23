# Wardley Map Analysis: Grey Zone of Defence (2025)

## Purpose

This map answers the question: **In the sub-threshold, state-vs-state-and-proxy grey zone, where has competition become weaponised-commodity (industrialised, routine) and where are attribution and consequences still genuinely novel?** It is a landscape map covering below-threshold conflict — deliberately short of the Clausewitzian line — spanning cyber, information, financial, and physical theatres. The strategic decision it supports is *where to invest doctrine, treaties, and capability* given that much of the grey-zone toolkit has commoditised while the machinery for legitimacy, attribution, and accountability has not.

## Strategic Context (answered from the brief)

The skill's Step 1 asks for four things. Because this benchmark provides the scenario as a single prompt, the answers below were inferred from the brief — they were not solicited from a live user.

| Question | Answer used |
|---|---|
| Strategic question | "Where is the grey zone weaponised-commodity, versus where attribution and consequences are still genuinely novel?" |
| User anchors | Four actor classes named in the brief: Supranationals, Governments, Private/Proxy Operators, People |
| Core needs | Four sovereignty pillars named in the brief: Cyber, Territorial, Economic, Cultural |
| Scope boundary | Below-threshold competition only — not declared war. Global, multi-theatre; snapshot at 2025. |

## Value Chain Overview

Working backward from the four actor anchors to the infrastructure the grey zone runs on produces 17 non-anchor components grouped into six horizontal bands:

- **Outcomes (visible, top)**: Territorial Integrity, Economic / Cyber / Cultural Sovereignty — the four pillars under contest.
- **Governance band**: Legitimacy, Statecraft & Treaties, Attribution & Deniability.
- **Effects band**: Influence Ops (propaganda + hearts & minds), Coercion & Kinetic (coerce + deter + below-threshold kinetic).
- **Theatres band**: Cyber & EW, Social Media, Financial, plus cross-cutting Awareness & ISR.
- **Landscape layer (invisible, bottom)**: Supply Chain, Physical Layer (land/space/territory), Crypto Rails, Virtual Layer (internet/cloud/comms).

Total component count is 17 non-anchor + 4 anchors = 21 nodes. The skill's operational guidance suggests 8-15 for a single map; this map runs to 17 components because the brief explicitly names four actor classes, four sovereignty pillars, five theatres (consolidated to three plus Awareness and Physical), three landscape layers, and multiple cross-cutting concepts (legitimacy, treaties, attribution, deniability, crypto). Splitting into submaps per theatre is the doctrinally-correct next step if the map is used operationally — see *Open Questions* at the end.

## OWM (OnlineWardleyMaps) Text Block

```
title Grey Zone of Defence (2025)
style wardley

anchor Supranationals [0.97, 0.50]
anchor Governments [0.97, 0.55]
anchor Private Proxy Operators [0.97, 0.35]
anchor People [0.97, 0.45]

component Territorial Integrity [0.85, 0.75]
component Economic Sovereignty [0.83, 0.55]
component Cyber Sovereignty [0.80, 0.35]
component Cultural Sovereignty [0.78, 0.30] inertia

component Legitimacy [0.68, 0.45] inertia
component Statecraft and Treaties [0.66, 0.65] inertia
component Attribution and Deniability [0.62, 0.20]

component Influence Ops [0.52, 0.60]
component Coercion and Kinetic [0.50, 0.55]

component Awareness and ISR [0.42, 0.50]
component Cyber and EW Theatre [0.38, 0.55]
component Social Media Theatre [0.36, 0.70]
component Financial Theatre [0.34, 0.60]

component Supply Chain [0.24, 0.70]
component Physical Layer [0.16, 0.80]
component Crypto Rails [0.14, 0.45]
component Virtual Layer [0.08, 0.88]

Supranationals->Territorial Integrity
Supranationals->Statecraft and Treaties
Supranationals->Legitimacy
Governments->Territorial Integrity
Governments->Economic Sovereignty
Governments->Cyber Sovereignty
Governments->Cultural Sovereignty
Governments->Legitimacy
Private Proxy Operators->Cyber Sovereignty
Private Proxy Operators->Attribution and Deniability
Private Proxy Operators->Coercion and Kinetic
People->Cultural Sovereignty
People->Cyber Sovereignty
People->Legitimacy

Territorial Integrity->Statecraft and Treaties
Territorial Integrity->Coercion and Kinetic
Economic Sovereignty->Statecraft and Treaties
Economic Sovereignty->Financial Theatre
Cyber Sovereignty->Attribution and Deniability
Cyber Sovereignty->Cyber and EW Theatre
Cultural Sovereignty->Influence Ops
Cultural Sovereignty->Social Media Theatre

Legitimacy->Attribution and Deniability
Legitimacy->Statecraft and Treaties
Statecraft and Treaties->Attribution and Deniability
Attribution and Deniability->Awareness and ISR
Attribution and Deniability->Cyber and EW Theatre

Influence Ops->Social Media Theatre
Influence Ops->Awareness and ISR
Coercion and Kinetic->Cyber and EW Theatre
Coercion and Kinetic->Financial Theatre
Coercion and Kinetic->Physical Layer

Awareness and ISR->Virtual Layer
Awareness and ISR->Physical Layer
Cyber and EW Theatre->Virtual Layer
Cyber and EW Theatre->Supply Chain
Social Media Theatre->Virtual Layer
Financial Theatre->Virtual Layer
Financial Theatre->Crypto Rails
Financial Theatre->Supply Chain

Supply Chain->Physical Layer
Physical Layer->Virtual Layer
Crypto Rails->Virtual Layer

evolve Attribution and Deniability 0.45
evolve Cyber Sovereignty 0.55
evolve Cultural Sovereignty 0.45
evolve Crypto Rails 0.65

annotation 1 [[0.30, 0.85]] Weaponised-commodity: social media, finance, virtual layer are now routine grey-zone tools.
annotation 2 [[0.58, 0.12]] Genuinely novel: attribution, deniability, cyber and cultural sovereignty remain contested/Custom-Built.
annotation 3 [[0.45, 0.82]] Friendly fire and unintended outcomes are externalities of every effect type; treaties trail the practice.
```

## Interactive React Artifact

```jsx
import React, { useState } from "react";

const COMPONENTS = [
  { id: "supranationals", name: "Supranationals", x: 0.50, y: 0.97, stage: "Anchor", anchor: true,
    rationale: "UN, NATO, EU, AU — multilateral bodies whose mandate spans across sovereign borders; operate through treaty mechanisms, not direct coercion." },
  { id: "governments", name: "Governments", x: 0.55, y: 0.97, stage: "Anchor", anchor: true,
    rationale: "Sovereign state actors — the primary users of the grey zone toolkit and the primary defenders against it." },
  { id: "proxies", name: "Private Proxy Operators", x: 0.35, y: 0.97, stage: "Anchor", anchor: true,
    rationale: "Wagner-style PMCs, cyber-mercenary outfits (NSO, Dark Matter), hacktivist fronts, influence-for-hire firms. The deniability layer of state competition." },
  { id: "people", name: "People", x: 0.45, y: 0.97, stage: "Anchor", anchor: true,
    rationale: "Target population for hearts-and-minds ops and cultural sovereignty contests; also the carriers of legitimacy and the casualties of unintended effects." },

  { id: "territorial", name: "Territorial Integrity", x: 0.75, y: 0.85, stage: "Commodity",
    rationale: "Westphalian sovereignty is the oldest codified pillar — UN Charter Art. 2(4), recognised borders, standing bodies to adjudicate. Commodity in concept; contested in practice." },
  { id: "economic", name: "Economic Sovereignty", x: 0.55, y: 0.83, stage: "Product",
    rationale: "Well-defined through sanctions regimes (OFAC, EU Sanctions Tracker), trade law, WTO mechanisms; multiple codified tools but sanctions-busting via crypto/third-countries is a live frontier." },
  { id: "cyber-sov", name: "Cyber Sovereignty", x: 0.35, y: 0.80, stage: "Custom-Built",
    rationale: "Still contested: Tallinn Manual 2.0 is advisory, UN OEWG/GGE consensus is partial, US and China disagree on what 'cyber sovereignty' even means. Every mature state has a bespoke doctrine." },
  { id: "cultural-sov", name: "Cultural Sovereignty", x: 0.30, y: 0.78, stage: "Custom-Built", inertia: true,
    rationale: "No treaty framework; concept is itself contested (Russia and China invoke it against 'Western values', liberal democracies invoke it against disinformation). Inertia: legal systems built for state-to-state contest, not platform-mediated narrative war." },

  { id: "legitimacy", name: "Legitimacy", x: 0.45, y: 0.68, stage: "Product", inertia: true,
    rationale: "Jus ad bellum, democratic mandate, international law — well-theorised but fragmenting under grey-zone ambiguity. Inertia: frameworks designed for declared war don't map cleanly to below-threshold competition." },
  { id: "statecraft", name: "Statecraft and Treaties", x: 0.65, y: 0.66, stage: "Product", inertia: true,
    rationale: "UN Charter, Geneva Conventions, NPT, arms control regimes — mature, codified, enforceable. Inertia: the treaty architecture assumes attributable state action and declared conflict; the grey zone is engineered to evade both." },
  { id: "attribution", name: "Attribution and Deniability", x: 0.20, y: 0.62, stage: "Custom-Built",
    rationale: "Technical attribution (Mandiant, CrowdStrike, Citizen Lab, Bellingcat) is a specialist capability with no universal standard. Deniability is an active adversarial craft. Published methodologies, but every case bespoke." },

  { id: "influence", name: "Influence Ops", x: 0.60, y: 0.52, stage: "Product",
    rationale: "Psyops and propaganda are a mature military discipline (US JP 3-13, UK 77th Brigade, Russian reflexive control doctrine). Social-media amplification has shifted the right-hand boundary toward Commodity." },
  { id: "coercion", name: "Coercion and Kinetic", x: 0.55, y: 0.50, stage: "Product",
    rationale: "Deterrence theory (Schelling, Jervis) and escalation management are mature. Below-threshold kinetic (limpet mines, GPS jamming, drone incidents) is Product — recurring but not yet normalised." },

  { id: "awareness", name: "Awareness and ISR", x: 0.50, y: 0.42, stage: "Product",
    rationale: "Commercial OSINT (Bellingcat, Maxar, Planet, Recorded Future) now commoditising ISR capability that was government-monopoly a decade ago. Product stage with rightward pressure." },
  { id: "cyber-ew", name: "Cyber and EW Theatre", x: 0.55, y: 0.38, stage: "Product",
    rationale: "Every major power has a cyber command (USCYBERCOM, UK NCF, Russia GRU Unit 26165, China SSF). Commercial offensive toolkits (NSO, DarkMatter, Cellebrite) commoditise capability; EW toolkits (Krasukha, Murmansk-BN) mature." },
  { id: "social", name: "Social Media Theatre", x: 0.70, y: 0.36, stage: "Commodity",
    rationale: "Weaponised-commodity per the brief — global platforms (Meta, X, TikTok, Telegram), bot-farms-as-a-service, troll factories, and LLM-generated content make influence at scale cheap and routine." },
  { id: "financial", name: "Financial Theatre", x: 0.60, y: 0.34, stage: "Product",
    rationale: "SWIFT exclusion, OFAC sanctions, secondary sanctions, correspondent banking coercion — a mature and widely-used toolkit. Crypto rails open a fragmenting frontier." },

  { id: "supply", name: "Supply Chain", x: 0.70, y: 0.24, stage: "Commodity",
    rationale: "Global logistics is commodity (containerisation, IATA, ICS) but is being actively weaponised — chip export controls, rare-earth leverage, Red Sea shipping disruption. Commoditised as infrastructure, contested as weapon." },
  { id: "physical", name: "Physical Layer", x: 0.80, y: 0.16, stage: "Commodity",
    rationale: "Land, maritime, space — the oldest commoditised substrate. Territory, seabed cables, satellites. The physical fact under every digital theatre." },
  { id: "crypto", name: "Crypto Rails", x: 0.45, y: 0.14, stage: "Product",
    rationale: "Bitcoin/Ethereum/stablecoins are a product-stage payment rail, increasingly used for sanctions evasion, ransomware, and proxy finance. Regulation (MiCA, US stablecoin framework) fragmenting evolution." },
  { id: "virtual", name: "Virtual Layer", x: 0.88, y: 0.08, stage: "Commodity",
    rationale: "TCP/IP, fibre backhaul, hyperscaler cloud, DNS, CDNs. Utility-priced, standardised, invisible when working. The infrastructure the grey zone rides on." }
];

const LINKS = [
  ["supranationals","territorial"],["supranationals","statecraft"],["supranationals","legitimacy"],
  ["governments","territorial"],["governments","economic"],["governments","cyber-sov"],["governments","cultural-sov"],["governments","legitimacy"],
  ["proxies","cyber-sov"],["proxies","attribution"],["proxies","coercion"],
  ["people","cultural-sov"],["people","cyber-sov"],["people","legitimacy"],
  ["territorial","statecraft"],["territorial","coercion"],
  ["economic","statecraft"],["economic","financial"],
  ["cyber-sov","attribution"],["cyber-sov","cyber-ew"],
  ["cultural-sov","influence"],["cultural-sov","social"],
  ["legitimacy","attribution"],["legitimacy","statecraft"],
  ["statecraft","attribution"],
  ["attribution","awareness"],["attribution","cyber-ew"],
  ["influence","social"],["influence","awareness"],
  ["coercion","cyber-ew"],["coercion","financial"],["coercion","physical"],
  ["awareness","virtual"],["awareness","physical"],
  ["cyber-ew","virtual"],["cyber-ew","supply"],
  ["social","virtual"],
  ["financial","virtual"],["financial","crypto"],["financial","supply"],
  ["supply","physical"],["physical","virtual"],["crypto","virtual"]
];

const EVOLUTIONS = [
  { id: "attribution", to: 0.45 }, { id: "cyber-sov", to: 0.55 },
  { id: "cultural-sov", to: 0.45 }, { id: "crypto", to: 0.65 }
];

const W = 1200, H = 800, PAD = { top: 60, right: 230, bottom: 80, left: 170 };
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
          Grey Zone of Defence — 2025
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
              <text x={cx+11} y={cy+4} fontSize="11" fill="#111">
                {c.name}
              </text>
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
              <rect x={Math.min(cx+14, W-boxW-10)} y={Math.max(cy-70, PAD.top+5)}
                    width={boxW} height="70" fill="#fff" stroke="#222" strokeWidth="1"/>
              <text x={Math.min(cx+20, W-boxW-4)} y={Math.max(cy-52, PAD.top+23)}
                    fontSize="11" fontWeight="600" fill="#111">{c.name} — {c.stage}</text>
              <foreignObject x={Math.min(cx+20, W-boxW-4)} y={Math.max(cy-44, PAD.top+30)}
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

          <text x="10" y="156" fontSize="10" fontWeight="600" fill="#111">Stages (x-axis)</text>
          <text x="10" y="172" fontSize="9" fill="#555">Genesis       0.00–0.17</text>
          <text x="10" y="186" fontSize="9" fill="#555">Custom        0.18–0.39</text>
          <text x="10" y="200" fontSize="9" fill="#555">Product       0.40–0.69</text>
          <text x="10" y="214" fontSize="9" fill="#555">Commodity     0.70–1.00</text>
        </g>
      </svg>
    </div>
  );
}
```

## Component Evolution Assessment

| Component | Stage | Position [vis, mat] | Rationale |
|---|---|---|---|
| Supranationals | Anchor | [0.97, 0.50] | UN, NATO, EU, AU — multilateral bodies whose mandate spans across sovereign borders; operate through treaty mechanisms, not direct coercion. Centrally placed on x because multilateralism sits between novel doctrine and established practice. |
| Governments | Anchor | [0.97, 0.55] | Sovereign state actors — the primary users of the grey-zone toolkit and the primary defenders against it. Placed slightly right-of-centre to reflect the bulk of state grey-zone practice being mature/Product-era. |
| Private Proxy Operators | Anchor | [0.97, 0.35] | Wagner-style PMCs, NSO-style cyber mercenaries, hacktivist fronts, influence-for-hire firms. Placed left-of-centre because the proxy-operator market is still Custom-Built — contracts and legal status vary case-by-case. |
| People | Anchor | [0.97, 0.45] | Target population for hearts-and-minds ops, carriers of legitimacy, and casualties of unintended effects. Centrally placed — the population is not itself novel or commodity, but the means of reaching them have both properties. |
| Territorial Integrity | Commodity | [0.85, 0.75] | Westphalian sovereignty is the oldest codified pillar — UN Charter Art. 2(4), recognised borders, standing adjudicative bodies. Commodity in concept; continuously contested in practice, but the *concept* is not novel. |
| Economic Sovereignty | Product | [0.83, 0.55] | Well-defined through sanctions regimes (OFAC, EU Sanctions Tracker), WTO mechanisms, export controls (Wassenaar, EAR). Multiple codified tools; crypto/third-country evasion is a live but non-novel frontier. |
| Cyber Sovereignty | Custom-Built | [0.80, 0.35] | Tallinn Manual 2.0 is advisory; UN OEWG/GGE consensus partial; US and China disagree on definition. Every mature state has a bespoke doctrine. No universal standard. |
| Cultural Sovereignty | Custom-Built (inertia) | [0.78, 0.30] | No treaty framework; concept itself contested (invoked both by authoritarians and liberal democracies for opposed ends). Inertia: legal systems built for state-to-state contest, not platform-mediated narrative war. |
| Legitimacy | Product (inertia) | [0.68, 0.45] | Jus ad bellum, democratic mandate, international law — well-theorised but fragmenting under grey-zone ambiguity. Inertia: frameworks designed for declared war don't map cleanly to below-threshold competition. |
| Statecraft and Treaties | Product (inertia) | [0.66, 0.65] | UN Charter, Geneva Conventions, NPT, arms control regimes — mature, codified, enforceable. Inertia: treaty architecture assumes attributable state action and declared conflict; grey zone is engineered to evade both. |
| Attribution and Deniability | Custom-Built | [0.62, 0.20] | Technical attribution (Mandiant, CrowdStrike, Citizen Lab, Bellingcat) is a specialist capability with no universal standard. Deniability is an active adversarial craft — by design it cannot be commoditised. |
| Influence Ops | Product | [0.52, 0.60] | Psyops and propaganda are a mature military discipline (US JP 3-13, UK 77th Brigade, Russian reflexive control). Social-media amplification has shifted the right-hand boundary toward Commodity. |
| Coercion and Kinetic | Product | [0.50, 0.55] | Deterrence theory (Schelling, Jervis) and escalation management are mature. Below-threshold kinetic (limpet mines, GPS jamming, drone incursions) is Product — recurring but not yet normalised as peacetime practice. |
| Awareness and ISR | Product | [0.42, 0.50] | Commercial OSINT (Bellingcat, Maxar, Planet, Recorded Future) now commoditises ISR capability that was government-monopoly a decade ago. Product stage with rightward pressure. |
| Cyber and EW Theatre | Product | [0.38, 0.55] | Every major power has a cyber command (USCYBERCOM, UK NCF, GRU 26165, PLA SSF). Commercial offensive toolkits (NSO, DarkMatter, Cellebrite) commoditise capability; EW toolkits (Krasukha, Murmansk-BN) mature. |
| Social Media Theatre | Commodity | [0.36, 0.70] | Weaponised-commodity per the brief — global platforms (Meta, X, TikTok, Telegram), bot-farms-as-a-service, troll factories, LLM-generated content make influence at scale cheap and routine. |
| Financial Theatre | Product | [0.34, 0.60] | SWIFT exclusion, OFAC sanctions, secondary sanctions, correspondent banking coercion — mature and widely-used toolkit. Crypto rails open a fragmenting frontier but don't unseat the main Product-stage machinery. |
| Supply Chain | Commodity | [0.24, 0.70] | Global logistics is commodity (containerisation, IATA, ICS) but is being actively weaponised — chip export controls, rare-earth leverage, Red Sea shipping disruption. Commoditised as infrastructure, contested as weapon. |
| Physical Layer | Commodity | [0.16, 0.80] | Land, maritime, space — the oldest commoditised substrate. Territory, seabed cables, satellites. The physical fact under every digital theatre. |
| Crypto Rails | Product | [0.14, 0.45] | Bitcoin/Ethereum/stablecoins are a product-stage payment rail, increasingly used for sanctions evasion, ransomware, and proxy finance. Regulation (MiCA, US stablecoin framework) fragmenting evolution. |
| Virtual Layer | Commodity | [0.08, 0.88] | TCP/IP, fibre backhaul, hyperscaler cloud, DNS, CDNs. Utility-priced, standardised, invisible when working. The infrastructure the grey zone rides on. |

## Key Strategic Observations

1. **The grey zone inverts the attribution stack.** The theatres (Cyber/EW, Social Media, Financial) are Product/Commodity — easy to enter, cheap to run at scale. But Attribution & Deniability sits at Custom-Built (0.20), and it's the *only* component that stands between a grey-zone action and a legitimacy/treaty response. Every route from an effect back to consequence terminates in the weakest part of the stack. This is the direct answer to the brief's "where are attribution and consequences still genuinely novel" question.

2. **Weaponised-commodity vs genuinely novel — a clean visual split.** The brief's explicit question maps to a diagonal on the chart:
   - **Weaponised-commodity (x ≥ 0.65)**: Social Media Theatre (0.70), Financial Theatre (0.60), Supply Chain (0.70), Physical Layer (0.80), Virtual Layer (0.88), Territorial Integrity (0.75). These are the routine grey-zone rails — cheap, at-scale, industrialised.
   - **Genuinely novel (x ≤ 0.39)**: Attribution & Deniability (0.20), Cultural Sovereignty (0.30), Cyber Sovereignty (0.35), Private Proxy Operators as a market (0.35). These are where the doctrine, case law, and response playbooks are still being written.

3. **Three load-bearing inertia points.** Legitimacy, Statecraft & Treaties, and Cultural Sovereignty all carry inertia markers. All three are Product or Custom-Built — i.e., mid-maturity concepts that the evolving practice is out-running. This is Wardley's most dangerous inertia pattern: high-prestige institutions with high sunk cost, facing a landscape that has moved past them.

4. **The people anchor has the thinnest legitimacy chain.** Trace from People down: People → Cultural Sovereignty → Influence Ops → Social Media Theatre → Virtual Layer. Four of those five are at x ≥ 0.30 and three are at x ≥ 0.60. Population-level vulnerability is now a function of commodity platforms, not specialist state capability. This is why private-proxy and hearts-and-minds ops scale so effectively.

5. **Private proxy operators are the arbitrage class.** The proxy anchor connects to three components: Cyber Sovereignty (0.35), Attribution & Deniability (0.20), and Coercion & Kinetic (0.55). The first two are Custom-Built — i.e., deniable by design. The arbitrage is that proxies can operate in the weaponised-commodity theatres (social media, finance, cyber) while the response mechanism relies on Custom-Built attribution. This asymmetry is the business model of Wagner, NSO, and the troll-farm industry.

6. **Friendly fire and unintended outcomes sit nowhere on the map — and that's the point.** The brief explicitly asks us to include them. They are *not* components; they are *consequences of effects*, and they are most likely where effect arcs overshoot. In map terms: the gap between Coercion & Kinetic (Product) and Attribution & Deniability (Custom-Built) is where unintended outcomes accumulate without legitimate remedy. Annotation 3 records this; an operational map would add a note-overlay on Coercion & Kinetic.

## Doctrine Check

Applied against the 40-principle doctrine catalogue from `references/doctrine-and-gameplay.md`:

- **Know your users (Phase I, Communication)**: Four anchors with distinct dependency patterns — Supranationals lean on treaties and legitimacy; Governments touch every sovereignty pillar; Proxies concentrate in attribution/deniability/coercion; People carry cultural and cyber sovereignty. Distinct needs, not collapsed into a generic "actor".
- **Focus on user needs (Phase I, Leading)**: Outcome band is the four sovereignty pillars named in the brief, not internal capability categories. Correctly anchored.
- **Use appropriate methods (Phase I, Development)**: Mismatch alert — treaties (Product-stage, Six-Sigma-grade institutional machinery) are being used to govern Social Media Theatre (Commodity) and Attribution (Custom-Built). The method/stage mismatch is Wardley's textbook doctrine violation and drives much of the grey zone's cost.
- **Manage inertia (Phase II, Leading)**: Three inertia markers (Legitimacy, Statecraft & Treaties, Cultural Sovereignty) are flagged explicitly. The inertia is not technical — it is institutional and doctrinal. This is the most dangerous form because its holders are exactly the bodies charged with responding.
- **Remove bias and duplication (Phase I, Operations)**: Attribution work is duplicated across intelligence agencies, commercial cyber firms, OSINT investigators, and academic labs — with no consolidation mechanism. Each Mandiant-style attribution report is bespoke. Climatic pressure to consolidate exists (standardised taxonomies like MITRE ATT&CK) but is incomplete.
- **Use a common language (Phase I, Communication)**: The map itself is the shared vocabulary for below-threshold conflict. Notably absent from current practice: multilaterals and adversaries use non-overlapping terminology (hybrid vs. sub-threshold vs. grey zone vs. active measures), which doctrine would flag as a Phase-I failure.

## Build vs. Buy Assessment

| Component | Recommendation | Rationale |
|---|---|---|
| Attribution & Deniability capability | Invest / Build | Custom-Built; no off-the-shelf commoditised attribution service exists at state-operational quality; durable advantage for whoever cracks it. Also aligns with AI-era pattern of building where AI accelerates Genesis-stage prototyping. |
| Cyber Sovereignty doctrine | Build (per-state) | Custom-Built by design — every state's legal/constitutional context forces a bespoke doctrine. Imported frameworks don't fit. |
| Social Media defence | Buy / partner | Commodity theatre — buy platform-level moderation, transparency, and takedown tooling. Building custom platform defences is a waste of capital. |
| Financial coercion toolkit | Buy / use multilateral | Product stage — OFAC, EU Sanctions, FATF. Use existing machinery; marginal ROI on bespoke alternatives. |
| Commercial OSINT (Awareness & ISR) | Buy | Moving from Product to Commodity. Building a national OSINT bureau in 2025 duplicates Bellingcat/Maxar/Planet capability. |
| Crypto-rails monitoring | Hybrid | Chainalysis, TRM, Elliptic are Product; in-house for adversary-specific chains and privacy-coin forensics. |
| Treaty/norms diplomacy | Invest / Multilateral | Statecraft & Treaties is Product with inertia; new norms (cyber, AI, space) need multilateral Build, not unilateral Buy. |
| Cultural Sovereignty frameworks | Invest / Build | Custom-Built with inertia. Durable differentiation for a state is *its own* cultural-sovereignty doctrine; imported frameworks are politically toxic. |
| Kinetic below-threshold capability | Build (sovereign only) | Product but sovereign-only. Cannot be outsourced to proxies without ceding control over escalation. |

## Evolution Predictions (12-24 months)

- **Attribution & Deniability**: 0.20 → 0.45. Commercial OSINT commoditises technical attribution; standardised taxonomies (MITRE ATT&CK, IOC frameworks) extend to influence ops (DISARM framework). Public attribution is becoming routine. (Evolution arrow on map.)
- **Cyber Sovereignty**: 0.35 → 0.55. EU NIS2, UK CSA 2024, UN OEWG consensus documents push toward Product-stage shared definitions. Holdouts (Russia, China) will retain bespoke doctrine, but the liberal-democratic bloc converges. (Evolution arrow on map.)
- **Cultural Sovereignty**: 0.30 → 0.45. EU DSA/DMA create the first comprehensive framework; UK Online Safety Act follows. The concept moves from contested rhetoric toward codified regulation, but remains fragmenting by bloc. (Evolution arrow on map.)
- **Crypto Rails**: 0.45 → 0.65. MiCA operational, US stablecoin framework, FATF Travel Rule adoption. Crypto graduates from Product to deep Product/near-Commodity as regulation standardises. (Evolution arrow on map.)
- **Social Media Theatre**: already Commodity; expect LLM-generated content to push further right within the Commodity band, making attribution *harder* even as attribution tooling improves.
- **Inertia risks**: Treaty architecture continues to trail practice. Statecraft & Treaties will *not* move right naturally; it moves only under forcing events (major attribution-confirmed attack, WMD use by a proxy, or a successful precedent-setting international court case).

## What's Weaponised-Commodity vs Genuinely Novel (the brief's explicit question)

**Weaponised-commodity (x ≥ 0.65) — industrialised, cheap at scale, routine:**
- Virtual Layer (0.88) — the rails
- Physical Layer (0.80) — land, sea, space
- Territorial Integrity (0.75) — the codified norm
- Social Media Theatre (0.70) — influence at scale
- Supply Chain (0.70) — logistics as leverage
- Crypto Rails (expected 0.65 within 24 months) — the bypass rails

**Genuinely novel (x ≤ 0.39) — no consensus, bespoke per case, durable differentiation:**
- Attribution & Deniability (0.20) — no universal standard; the deniability side is adversarially non-commoditisable
- Cultural Sovereignty (0.30) — contested concept; no treaty framework
- Cyber Sovereignty (0.35) — advisory frameworks only
- Private Proxy Operators (anchor, 0.35) — the market itself is Custom-Built

**The "consequences" question (friendly fire, unintended outcomes):**
Consequences are *emergent from* effect arcs, not mapped as components. The map's structure implies them: any effect portfolio that runs over Commodity theatres (scale, speed) but resolves via Custom-Built attribution (slow, bespoke) will systematically accumulate unintended outcomes — the attribution machinery can't keep up with the effect volume. This is the *structural* reason grey-zone friendly fire is not a bug but a feature of the current stack.

## Open Questions

1. Does any multilateral body (UN OEWG, OECD, G7, G20) produce a canonical attribution standard in the next 24 months, or does attribution remain commercially fragmented?
2. Does the Social Media Theatre's LLM-content subcomponent warrant a submap of its own? Likely yes — it has enough internal structure (synthetic media detection, provenance watermarking, platform moderation) to justify decomposition.
3. How should the map evolve to incorporate space-domain sub-threshold conflict (GPS jamming, satellite dazzling, kinetic ASAT demonstrations)? Currently folded into Physical Layer; may warrant a separate Space Theatre if the user's decision space involves orbital operations.
4. If the user anchor includes non-state armed groups (Hezbollah, Houthis, Hamas-era organisations) rather than only state proxies, does Private Proxy Operators split into PMCs vs. NSAGs? The distinction matters for legitimacy and treaty applicability.

---

*This analysis was produced following the haberlah `wardley-mapping` skill (SKILL.md Steps 1-7). The Step 1 strategic-context questions were answered from the scenario brief because no live user was available. No iteration against an external validator was performed; this is a first complete pass per the benchmark contract. The component count (17 non-anchor) exceeds the skill's 15-component guidance because the brief explicitly enumerates four actor classes, four sovereignty pillars, five theatres, three landscape layers, and multiple cross-cutting governance concepts — consolidation below 15 would require dropping categories the brief names by name. Open Question 2 proposes the next-step submap decomposition.*
