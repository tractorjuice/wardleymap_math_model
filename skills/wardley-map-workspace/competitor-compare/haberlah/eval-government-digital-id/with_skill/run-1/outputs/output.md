# Wardley Map Analysis: Government Digital Identity (November 2022)

## Purpose

This map answers the question: **In November 2022, where is government digital identity technology still novel vs. standardised, and how do the tensions between centralised authority, self-sovereign identity (SSI), and bad-actor exploitation of the rule set distribute across the value chain?** It is a *landscape* map of the whole ecosystem — not a product map for any one jurisdiction. The strategic decisions it supports sit at the policy layer (eIDAS 2 trilogue, EU Digital Identity Wallet consultation), the supplier layer (national eID operators, wallet vendors, DID/VC implementers), and the defensive layer (fraud prevention, privacy protection, the "exceptions" apparatus).

## Strategic Context (answered from the brief)

The skill's Step 1 asks for four things. Because this benchmark provides the scenario as a single prompt, the answers below were inferred directly from the brief — they were not solicited from a live user.

| Question | Answer used |
|---|---|
| Strategic question | "Where is identity technology novel vs. standardised, and where do centralised-vs-SSI-vs-bad-actor tensions sit?" |
| User anchors | Government, Society, Citizens, Corporations, Entities (non-human legal persons, devices, organisations), Bad Actors — all six explicitly named in the brief |
| Core needs | Public service delivery, trust, authority (centralised / decentralised / issuing), identity / identification / identifiers, power (over / with / to), a workable rule-and-exception apparatus |
| Scope boundary | Global government digital-identity landscape as of Nov 2022 — eIDAS 2 still in legislative process; W3C VC 1.1 just recommended; national eIDs mature in some regimes, absent in others |

## Value Chain Overview

Working downward from the six anchors through service → claims → credentials → identity → identification → identifiers → transport yields 22 components plus the 6 anchors (28 total). The skill's guidance is 8–15, and flags >15. This map breaks that ceiling deliberately because the scenario explicitly names three parallel sub-chains (power, trust, regulation/rules/exceptions) that attach to the main identity chain — splitting them into submaps would obscure the tensions the map is being commissioned to show. A more focused submap of *just* the authority-and-identifier layer is a sensible follow-up.

The layers, top-to-bottom:

- **Anchors (vis ≈ 0.97)**: the six named actors, including Bad Actors whose "need" is the exception apparatus they can exploit.
- **Outcome (vis ≈ 0.88)**: Public Service — what the whole chain delivers.
- **Power layer (vis ≈ 0.82–0.84)**: Power-over (state → subject), Power-with (peer/consent), Power-to (individual agency). These are the political frames inside which the rest of the chain is legitimate.
- **Regulation / rules / exceptions (vis ≈ 0.70–0.76)**: the formal apparatus that defines what a valid identity claim is and what to do when reality doesn't match it.
- **Trust (vis ≈ 0.60–0.68)**: Trust itself, decomposed into benevolence, capability, integrity (Mayer, Davis & Schoorman 1995 formulation).
- **Claim / credential / identity (vis ≈ 0.42–0.55)**: the core chain the brief names.
- **Identification (vis ≈ 0.32–0.33)**: physical and digital — how an identity is operationally checked.
- **Authority (vis ≈ 0.24–0.25)**: Issuing Authority and its two contrasting forms (Centralised vs. Decentralised). SSI (0.40) is adjacent, pulling identification toward decentralised authority.
- **Identifiers (vis ≈ 0.15–0.18)**: Mutable (email, phone, pseudonyms), Immutable (biometrics, DIDs), Connectedness (graph-level identity signal).
- **Transport (vis ≈ 0.05)**: the Internet itself — a Commodity utility.

## OWM (OnlineWardleyMaps) Text Block

```
title Government Digital Identity (November 2022)
style wardley

anchor Citizens [0.97, 0.55]
anchor Government [0.97, 0.40]
anchor Society [0.97, 0.70]
anchor Corporations [0.97, 0.60]
anchor Entities [0.97, 0.48]
anchor Bad Actors [0.97, 0.20]

component Public Service [0.88, 0.55]
component Power-to [0.84, 0.28]
component Power-with [0.83, 0.45]
component Power-over [0.82, 0.62]
component Regulation [0.76, 0.50]
component Rules [0.70, 0.60]
component Exceptions [0.70, 0.30]
component Trust [0.68, 0.35]
component Benevolence [0.62, 0.22]
component Capability [0.61, 0.58]
component Integrity [0.60, 0.40]
component Claims [0.55, 0.55]
component Credentials [0.48, 0.50]
component Identity [0.42, 0.48]
component Self-Sovereign Identity [0.40, 0.18] inertia
component Digital Identification [0.33, 0.40]
component Physical Identification [0.32, 0.72]
component Issuing Authority [0.25, 0.62]
component Decentralised Authority [0.24, 0.20]
component Centralised Authority [0.24, 0.80]
component Mutable Identifiers [0.18, 0.55]
component Connectedness [0.16, 0.35]
component Immutable Identifiers [0.15, 0.70]
component Internet [0.05, 0.92]

Citizens->Public Service
Government->Public Service
Society->Public Service
Corporations->Public Service
Entities->Public Service
Bad Actors->Exceptions

Citizens->Power-to
Government->Power-over
Society->Power-with
Corporations->Power-with

Public Service->Claims
Public Service->Trust
Public Service->Regulation

Power-to->Self-Sovereign Identity
Power-over->Centralised Authority
Power-with->Decentralised Authority

Regulation->Rules
Regulation->Exceptions
Rules->Credentials
Exceptions->Rules

Trust->Benevolence
Trust->Capability
Trust->Integrity

Benevolence->Identity
Capability->Credentials
Integrity->Identity

Claims->Credentials
Credentials->Identity
Credentials->Issuing Authority

Identity->Digital Identification
Identity->Physical Identification

Self-Sovereign Identity->Decentralised Authority
Self-Sovereign Identity->Digital Identification

Digital Identification->Mutable Identifiers
Digital Identification->Immutable Identifiers
Digital Identification->Connectedness
Digital Identification->Issuing Authority
Physical Identification->Issuing Authority
Physical Identification->Centralised Authority

Issuing Authority->Centralised Authority
Issuing Authority->Decentralised Authority

Mutable Identifiers->Internet
Immutable Identifiers->Internet
Connectedness->Internet
Centralised Authority->Internet
Decentralised Authority->Internet
Digital Identification->Internet

evolve Self-Sovereign Identity 0.38
evolve Digital Identification 0.62
evolve Credentials 0.70
evolve Decentralised Authority 0.40
evolve Regulation 0.65
evolve Claims 0.72

annotation 1 [[0.42, 0.18]] SSI + W3C VCs/DIDs (2022 recommendations) — adoption still bespoke and pilot-stage.
annotation 2 [[0.27, 0.80]] Centralised Authority (Aadhaar, Estonia e-ID, SingPass) — Commodity in mature regimes.
annotation 3 [[0.78, 0.55]] eIDAS 2 / EU Digital Identity Wallet in trilogue November 2022.
annotation 4 [[0.72, 0.30]] Exceptions apparatus: where bad actors exploit gaps between rule and reality.
```

## Interactive React Artifact

```jsx
import React, { useState } from "react";

const COMPONENTS = [
  { id: "citizens", name: "Citizens", x: 0.55, y: 0.97, stage: "Anchor", anchor: true,
    rationale: "The primary end-users of identity services — beneficiaries of Power-to and objects of Power-over." },
  { id: "government", name: "Government", x: 0.40, y: 0.97, stage: "Anchor", anchor: true,
    rationale: "The issuer-of-last-resort and regulator. Wields Power-over through centralised authority." },
  { id: "society", name: "Society", x: 0.70, y: 0.97, stage: "Anchor", anchor: true,
    rationale: "The collective that grants legitimacy and exercises Power-with." },
  { id: "corporations", name: "Corporations", x: 0.60, y: 0.97, stage: "Anchor", anchor: true,
    rationale: "Relying parties (banks, platforms, telcos) that consume credentials and shape market evolution." },
  { id: "entities", name: "Entities", x: 0.48, y: 0.97, stage: "Anchor", anchor: true,
    rationale: "Non-human identity holders: devices, organisations, DAOs, AI agents — a growing share of identity traffic." },
  { id: "bad-actors", name: "Bad Actors", x: 0.20, y: 0.97, stage: "Anchor", anchor: true,
    rationale: "Adversaries who exploit the exception apparatus. Genesis/novel in attack vectors; their 'need' is the gap between rule and reality." },

  { id: "public-service", name: "Public Service", x: 0.55, y: 0.88, stage: "Product",
    rationale: "Delivery of identity-gated services (tax, benefits, healthcare, voting) — well-defined, comparable across jurisdictions, clearly Product." },

  { id: "power-to", name: "Power-to", x: 0.28, y: 0.84, stage: "Custom-Built",
    rationale: "Individual agency in identity decisions — still bespoke per jurisdiction (GDPR data-subject rights in EU; patchy elsewhere)." },
  { id: "power-with", name: "Power-with", x: 0.45, y: 0.83, stage: "Custom-Built",
    rationale: "Consent-based / federated identity frameworks — moving toward Product but OIDC-Federation / mDL profiles are still being standardised." },
  { id: "power-over", name: "Power-over", x: 0.62, y: 0.82, stage: "Product",
    rationale: "State authority to compel identification — a millennia-old practice, Product-stage as a political frame." },

  { id: "regulation", name: "Regulation", x: 0.50, y: 0.76, stage: "Product",
    rationale: "Identity regulation exists in most jurisdictions (eIDAS in EU, NIST 800-63 in US, DIA in AU) — Product. But eIDAS 2 is Custom-Built as it's still in trilogue." },
  { id: "rules", name: "Rules", x: 0.60, y: 0.70, stage: "Product",
    rationale: "Operational rule sets (Levels of Assurance, identity proofing) are well-documented, multiple published standards." },
  { id: "exceptions", name: "Exceptions", x: 0.30, y: 0.70, stage: "Custom-Built",
    rationale: "Exception handling (lost ID, refugees, children, homeless, stateless) is bespoke per programme — no shared methodology or vendor." },

  { id: "trust", name: "Trust", x: 0.35, y: 0.68, stage: "Custom-Built",
    rationale: "Institutional trust models in digital identity are still debated (ToIP, Rebooting Web of Trust, ENISA frameworks) — no consensus." },
  { id: "benevolence", name: "Benevolence", x: 0.22, y: 0.62, stage: "Genesis",
    rationale: "Operationalising 'does the issuer act in my interest?' is an open research question; ENISA 2022 guidance is nascent." },
  { id: "capability", name: "Capability", x: 0.58, y: 0.61, stage: "Product",
    rationale: "Issuer capability (uptime, cryptographic strength) is measurable — FIPS 140-3, Common Criteria certifications." },
  { id: "integrity", name: "Integrity", x: 0.40, y: 0.60, stage: "Custom-Built",
    rationale: "Issuer integrity (honesty about breaches, process-level assurance) varies enormously — audit regimes bespoke." },

  { id: "claims", name: "Claims", x: 0.55, y: 0.55, stage: "Product",
    rationale: "Claims-based authentication (OAuth 2.0, OIDC, SAML) is mature and widely deployed — Product. Evolving toward Commodity as VC/mDL claim profiles standardise." },
  { id: "credentials", name: "Credentials", x: 0.50, y: 0.48, stage: "Product",
    rationale: "Credentials are well-understood — multiple mature products (national eID cards, PKI certs, FIDO2, W3C VCs). Clear Product stage, evolving toward Commodity as wallet formats converge." },
  { id: "identity", name: "Identity", x: 0.48, y: 0.42, stage: "Custom-Built",
    rationale: "'Identity' as an operational construct (not a credential) remains contested across legal, technical, social domains — Custom-Built, with Genesis edges (non-human / entity identity)." },
  { id: "ssi", name: "Self-Sovereign Identity", x: 0.18, y: 0.40, stage: "Genesis", inertia: true,
    rationale: "Genesis in Nov 2022. Sovrin, Indy, ESSIF, Aries exist but no production-scale deployment outside pilots. W3C VC 1.1 rec (Nov 2022) is recent. Inertia: governments resist ceding identity monopoly.",
    evolveTo: 0.38 },

  { id: "digital-id", name: "Digital Identification", x: 0.40, y: 0.33, stage: "Custom-Built",
    rationale: "Digital identification (biometric match, live-video, document OCR) exists in many forms but implementations are bespoke per operator. Evolving fast toward Product.",
    evolveTo: 0.62 },
  { id: "physical-id", name: "Physical Identification", x: 0.72, y: 0.32, stage: "Product",
    rationale: "Passports, ID cards, driver licences with ICAO-standard MRZ / chip data — Product with high interoperability, pushing into Commodity." },

  { id: "issuing-auth", name: "Issuing Authority", x: 0.62, y: 0.25, stage: "Product",
    rationale: "Well-established institutional form — passport offices, notaries, civil registries. Product stage with clear process standards." },
  { id: "decent-auth", name: "Decentralised Authority", x: 0.20, y: 0.24, stage: "Genesis",
    rationale: "DAOs, DPKI, DIDs — the idea exists but near-zero production use for government identity in Nov 2022. Genesis.",
    evolveTo: 0.40 },
  { id: "cent-auth", name: "Centralised Authority", x: 0.80, y: 0.24, stage: "Commodity",
    rationale: "National ID programmes (India Aadhaar 1.3B, Estonia e-ID, Singapore SingPass, Nigeria NIN, Pakistan NADRA) — utility-scale, standardised, invisible when working." },

  { id: "mutable-ids", name: "Mutable Identifiers", x: 0.55, y: 0.18, stage: "Product",
    rationale: "Email, phone, username, pseudonym — common, comparable, cheap. Product moving to Commodity." },
  { id: "connectedness", name: "Connectedness", x: 0.35, y: 0.16, stage: "Custom-Built",
    rationale: "Graph-based identity signal (device fingerprint, relationship graph, behaviour biometrics) — used by risk engines but implementations bespoke." },
  { id: "immutable-ids", name: "Immutable Identifiers", x: 0.70, y: 0.15, stage: "Commodity",
    rationale: "Fingerprint, iris, face (FAR/FRR standardised by ISO/IEC 19795), DIDs — commoditised at the identifier level though wallet/issuer implementations vary." },

  { id: "internet", name: "Internet", x: 0.92, y: 0.05, stage: "Commodity",
    rationale: "Transport layer. Universal utility, standardised protocols, invisible infrastructure." }
];

const LINKS = [
  ["citizens","public-service"],["government","public-service"],["society","public-service"],
  ["corporations","public-service"],["entities","public-service"],["bad-actors","exceptions"],
  ["citizens","power-to"],["government","power-over"],["society","power-with"],["corporations","power-with"],
  ["public-service","claims"],["public-service","trust"],["public-service","regulation"],
  ["power-to","ssi"],["power-over","cent-auth"],["power-with","decent-auth"],
  ["regulation","rules"],["regulation","exceptions"],["rules","credentials"],["exceptions","rules"],
  ["trust","benevolence"],["trust","capability"],["trust","integrity"],
  ["benevolence","identity"],["capability","credentials"],["integrity","identity"],
  ["claims","credentials"],["credentials","identity"],["credentials","issuing-auth"],
  ["identity","digital-id"],["identity","physical-id"],
  ["ssi","decent-auth"],["ssi","digital-id"],
  ["digital-id","mutable-ids"],["digital-id","immutable-ids"],["digital-id","connectedness"],
  ["digital-id","issuing-auth"],["physical-id","issuing-auth"],["physical-id","cent-auth"],
  ["issuing-auth","cent-auth"],["issuing-auth","decent-auth"],
  ["mutable-ids","internet"],["immutable-ids","internet"],["connectedness","internet"],
  ["cent-auth","internet"],["decent-auth","internet"],["digital-id","internet"]
];

const EVOLUTIONS = [
  { id: "ssi", to: 0.38 },
  { id: "digital-id", to: 0.62 },
  { id: "credentials", to: 0.70 },
  { id: "decent-auth", to: 0.40 },
  { id: "regulation", to: 0.65 },
  { id: "claims", to: 0.72 }
];

const W = 1200, H = 820, PAD = { top: 60, right: 220, bottom: 80, left: 90 };
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
                fill={["#fef9f0","#fefcf7","#f7faf7","#f0f6fe"][i]} />
        ))}
        {[0.25,0.5,0.75].map(m => (
          <line key={m} x1={xS(m)} y1={PAD.top} x2={xS(m)} y2={H-PAD.bottom}
                stroke="#ccc" strokeDasharray="4 4"/>
        ))}
        <text x={PAD.left} y={40} fontSize="16" fontWeight="600" fill="#111">
          Government Digital Identity — November 2022
        </text>
        <text x={xS(0.125)} y={H-PAD.bottom+18} fontSize="11" textAnchor="middle" fill="#555">Genesis</text>
        <text x={xS(0.375)} y={H-PAD.bottom+18} fontSize="11" textAnchor="middle" fill="#555">Custom-Built</text>
        <text x={xS(0.625)} y={H-PAD.bottom+18} fontSize="11" textAnchor="middle" fill="#555">Product (+Rental)</text>
        <text x={xS(0.875)} y={H-PAD.bottom+18} fontSize="11" textAnchor="middle" fill="#555">Commodity (+Utility)</text>
        <text x={xS(0.5)} y={H-PAD.bottom+40} fontSize="12" textAnchor="middle" fill="#333">Evolution →</text>
        <text x={36} y={PAD.top+10} fontSize="11" fill="#555">Visible</text>
        <text x={36} y={H-PAD.bottom-5} fontSize="11" fill="#555">Invisible</text>
        <text x={24} y={(PAD.top+H-PAD.bottom)/2} fontSize="12"
              transform={`rotate(-90 24 ${(PAD.top+H-PAD.bottom)/2})`}
              textAnchor="middle" fill="#333">Value chain / Visibility</text>

        {LINKS.map(([a,b],i) => {
          const A = byId[a], B = byId[b];
          if (!A || !B) return null;
          const op = (dim(a)||dim(b)) ? 0.08 : 0.45;
          const x1=xS(A.x), y1=yS(A.y), x2=xS(B.x), y2=yS(B.y);
          const cx = (x1+x2)/2, cy = (y1+y2)/2 + 14;
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
              <circle cx={cx} cy={cy} r="6" fill={fill} stroke="#222" strokeWidth="1.5"/>
              <text x={cx+10} y={cy+3} fontSize="10" fill="#111">{c.name}</text>
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
                    width={boxW} height="80" fill="#fff" stroke="#222" strokeWidth="1"/>
              <text x={Math.min(cx+20, W-boxW-4)} y={Math.max(cy-52, PAD.top+23)}
                    fontSize="11" fontWeight="600" fill="#111">{c.name} — {c.stage}</text>
              <foreignObject x={Math.min(cx+20, W-boxW-4)} y={Math.max(cy-44, PAD.top+30)}
                             width={boxW-12} height="64">
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
          <text x="10" y="172" fontSize="9" fill="#555">Genesis      0.00–0.17</text>
          <text x="10" y="186" fontSize="9" fill="#555">Custom       0.18–0.39</text>
          <text x="10" y="200" fontSize="9" fill="#555">Product      0.40–0.69</text>
          <text x="10" y="214" fontSize="9" fill="#555">Commodity    0.70–1.00</text>
        </g>
      </svg>
    </div>
  );
}
```

## Component Evolution Assessment

| Component | Stage | Position [vis, mat] | Rationale |
|---|---|---|---|
| Citizens | Anchor | [0.97, 0.55] | Primary end-users of identity services. |
| Government | Anchor | [0.97, 0.40] | Issuer-of-last-resort and regulator. |
| Society | Anchor | [0.97, 0.70] | Grants legitimacy to the identity system via Power-with. |
| Corporations | Anchor | [0.97, 0.60] | Relying parties consuming credentials; shape market evolution. |
| Entities | Anchor | [0.97, 0.48] | Non-human identity holders (devices, orgs, DAOs, agents). |
| Bad Actors | Anchor | [0.97, 0.20] | Adversaries who exploit the exception apparatus. Placed left because attack innovation is Genesis-stage. |
| Public Service | Product | [0.88, 0.55] | Identity-gated services are well-defined and comparable across jurisdictions. |
| Power-to | Custom-Built | [0.84, 0.28] | Individual-agency frameworks still bespoke per jurisdiction; GDPR in EU is the most mature. |
| Power-with | Custom-Built | [0.83, 0.45] | Federated / consent-based identity (OIDC Federation, mDL profiles) standardising but not yet Product. |
| Power-over | Product | [0.82, 0.62] | State authority to compel identification is a mature construct. |
| Regulation | Product | [0.76, 0.50] | Identity regulation exists in most jurisdictions (eIDAS, NIST 800-63, DIA). eIDAS 2 is the evolving frontier. |
| Rules | Product | [0.70, 0.60] | Levels of Assurance, identity proofing practices are well-documented. |
| Exceptions | Custom-Built | [0.70, 0.30] | Handling for refugees, homeless, stateless, children, lost credentials — bespoke per programme. |
| Trust | Custom-Built | [0.68, 0.35] | Institutional trust models in digital identity contested (ToIP, ENISA, Rebooting Web of Trust). |
| Benevolence | Genesis | [0.62, 0.22] | Operationalising "issuer acts in my interest" is an open research problem. |
| Capability | Product | [0.61, 0.58] | Issuer capability measurable (FIPS 140-3, Common Criteria). |
| Integrity | Custom-Built | [0.60, 0.40] | Issuer integrity — audit regimes vary widely; no cross-jurisdiction standard. |
| Claims | Product | [0.55, 0.55] | OAuth 2.0, OIDC, SAML mature; moving to Commodity as VC/mDL profiles standardise. |
| Credentials | Product | [0.50, 0.48] | National eID cards, PKI, FIDO2, W3C VCs — multiple mature products. |
| Identity | Custom-Built | [0.48, 0.42] | "Identity" as operational construct remains contested across legal/technical/social domains. |
| Self-Sovereign Identity | Genesis (inertia) | [0.40, 0.18] | Sovrin, Indy, ESSIF, Aries exist but no production-scale outside pilots. W3C VC 1.1 rec (Nov 2022) is recent. Inertia: governments resist ceding identity monopoly. |
| Digital Identification | Custom-Built | [0.33, 0.40] | Biometric match, live-video, document OCR — bespoke per operator, evolving fast. |
| Physical Identification | Product | [0.32, 0.72] | ICAO-standard passport / ID card / chip data — high interoperability. |
| Issuing Authority | Product | [0.25, 0.62] | Passport offices, notaries, civil registries — mature institutional form. |
| Decentralised Authority | Genesis | [0.24, 0.20] | DAOs, DPKI — near-zero production use for government identity in Nov 2022. |
| Centralised Authority | Commodity | [0.24, 0.80] | Aadhaar (1.3B), Estonia e-ID, SingPass, NADRA — utility-scale where deployed. |
| Mutable Identifiers | Product | [0.18, 0.55] | Email, phone, pseudonym — common, comparable, cheap. |
| Connectedness | Custom-Built | [0.16, 0.35] | Graph-based identity signal — risk-engine proprietary, not commoditised. |
| Immutable Identifiers | Commodity | [0.15, 0.70] | Fingerprint, iris, face — ISO/IEC 19795 standardised FAR/FRR. |
| Internet | Commodity | [0.05, 0.92] | Universal transport utility. |

## Key Strategic Observations

1. **Three authority models coexist at the same visibility band but at opposite ends of evolution.** Centralised Authority is Commodity (0.80); Issuing Authority is Product (0.62); Decentralised Authority is Genesis (0.20). Wardley's climatic pattern *"characteristics change as components evolve"* predicts these three cannot be managed by the same methods, organisational structure, or commercial model — a single "identity programme" trying to cover all three will fail.

2. **The SSI–Centralised tension is structural, not merely political.** SSI (Genesis, marked with inertia) sits vertically near the authority layer but horizontally far to the left. The Power-to chain routes through it; the Power-over chain bypasses it to Centralised Authority. In Wardley terms, these are two *competing evolutionary paths for identity* that have not yet converged. November 2022 is a moment where the eIDAS 2 Wallet is attempting to bridge them, not choose between them.

3. **Trust decomposes into three components at different evolution stages.** Capability is Product (measurable, certifiable). Integrity is Custom-Built (audits are bespoke). Benevolence is Genesis (research problem). This is a *doctrine gap*: organisations tend to buy "trust" as one thing when only a third of it is actually purchasable.

4. **Bad Actors exploit the rule-to-reality gap through Exceptions.** Exceptions is the only Custom-Built component in the regulation apparatus sitting adjacent to well-defined Rules and Regulation. Attack surface = the gap between what the rules say and what actually happens. The Peace-War-Wonder cycle suggests Exceptions will not remain Custom-Built for long — biometric-based fraud, deepfake KYC, and synthetic-identity tools are commoditising the attack side faster than the defence side.

5. **The identifier layer is bifurcating.** Immutable identifiers (biometrics, DIDs) are Commodity; Mutable identifiers (email, phone) are Product; Connectedness signals (graph, device fingerprint) are Custom-Built. Expect consolidation: risk engines will buy standardised connectedness products in the next 18-24 months.

## Doctrine Check

| # | Principle | Status in this map |
|---|---|---|
| 1 | Know your users | Partially: the six named anchors are explicit but the brief groups "Entities" loosely — real implementations need to split device / org / DAO / AI-agent cases. |
| 7 | Remove bias and duplication | Duplication visible: many jurisdictions building parallel identity-verification stacks. EU's eIDAS 2 attempts to remove this within Europe; globally, duplication dominates. |
| 9 | Use appropriate methods | Frequent mismatch: Genesis-stage SSI projects often run with waterfall governance (method mismatch); Commodity-stage Centralised Authorities often run with legacy custom processes. |
| 15 | Use standards where appropriate | Standards exist for Commodity components (ICAO, ISO/IEC 19795, OIDC). Gap: Trust decomposition (benevolence/capability/integrity) lacks an operational standard. |
| 19 | Manage inertia | SSI is the clear inertia point — government inertia against ceding identity monopoly. This is the most strategic single lever in the map. |
| 37 | Listen to your ecosystems | Weak signals in Nov 2022: mDL rollouts (Apple Wallet, Google Wallet), UK gov ORCHID rebrand to gov.uk Wallet, EUDI Reference Wallet Architecture v1.0. These signal Credentials → Commodity compression. |

## Recommended Actions

*(Listed as actions the different anchor groups might consider, not instructions — this is a landscape map, not a firm's strategy map.)*

1. **For Government (issuer anchor)**: Invest in the Decentralised Authority path even if you keep Centralised as primary. Ignoring SSI risks classic *two-forms-of-disruption* — a business-model shift where citizens adopt non-government-anchored identity for day-to-day use (MetaMask/DIDs), leaving government identity relevant only for statutory acts.

2. **For Corporations (relying-party anchor)**: Buy Commodity identifier infrastructure (ICAO/ISO biometrics, OIDC), build only on Custom-Built Trust Integrity where regulated differentiation is required. Avoid building SSI stacks unless they are your core product — Genesis-stage operational risk is high.

3. **For Society / Civil Society**: Scrutinise the Exceptions apparatus. This is where bad-actor exploitation sits but also where marginalised populations are excluded. It is simultaneously a security and an inclusion problem.

4. **For Regulators (eIDAS 2 context)**: The most dangerous single move is to specify Custom-Built implementations (e.g. a single wallet reference) at regulatory level before the market has converged — this freezes components into Product stage when they should continue evolving.

5. **For Bad Actors (as threat modelling)**: Expect attacks to move left → right over the next 24 months. Current attacks exploit Custom-Built Exceptions; mature attacks will industrialise around Commodity biometrics (deepfake liveness bypass), which must be assumed already.

## Build vs. Buy Assessment

| Component | Recommendation | Rationale |
|---|---|---|
| Internet | Buy (utility) | Commodity transport; no buying decision. |
| Centralised Authority | Buy national, not custom | National eID offerings are utility-scale. Building a new one at jurisdictional scale is a 10-year programme. |
| Immutable Identifiers | Buy (standards-compliant) | ISO/IEC 19795 biometric products are commoditised. |
| Credentials (VC/mDL) | Buy, watch carefully | Product stage now; likely Commodity in 24 months. Invest in portability, not lock-in. |
| Physical Identification | Buy (ICAO-compliant) | Mature product market. |
| Claims / OIDC | Buy / use open standards | Product/Commodity stack. |
| Digital Identification | Buy, expect rapid change | Custom-Built now, moving fast to Product. Avoid 5-year vendor lock-in. |
| Trust Capability | Buy (certifications) | Product-stage assurance regime. |
| Trust Integrity | Custom / contract | Custom-Built; requires bespoke audit. |
| Trust Benevolence | Build (research) | Genesis — no off-the-shelf solution. Research collaboration only. |
| SSI | Experiment, don't bet | Genesis + inertia. Pilot in limited scope (academic credentials, mobile driver licence parallel). |
| Exceptions apparatus | Build / participate | Custom-Built and mission-critical. Civil-society engagement essential. |

## Evolution Predictions (12-24 months from November 2022)

- **Credentials → Commodity**: Apple/Google mDL + EUDIW drive wallet-side convergence. Target maturity ~0.70 by late 2024. *(evolve arrow in map)*
- **Digital Identification → Product**: Onfido, Jumio, iProov, Yoti scale biometric identity-proofing. Target ~0.62. *(evolve arrow)*
- **Decentralised Authority → Custom-Built**: Pilot-scale deployments (mDL issuance by states; academic VCs) push SSI-adjacent decentralised authority out of Genesis into early Custom-Built. Target ~0.40. *(evolve arrow)*
- **Self-Sovereign Identity → Custom-Built**: Same drivers push SSI proper out of Genesis. Target ~0.38. *(evolve arrow)*
- **Regulation → Commodity-adjacent**: eIDAS 2 adoption in 2024 standardises EU identity regulation at Commodity level for wallet interoperability. Target ~0.65. *(evolve arrow)*
- **Claims → Commodity**: OIDC4VC / mDL profiles converge; claims become a commodity layer above credentials. Target ~0.72. *(evolve arrow)*

### Inertia and counter-forces

- **Governments** resist ceding identity monopoly → slows SSI evolution. (Marked in map.)
- **Legacy KYC industry** ($30B+) resists credential-portability → slows Credentials → Commodity.
- **Privacy regulators** (EU DPAs, UK ICO) push for data-minimising designs → accelerates SSI and decentralised approaches where they serve privacy.
- **Bad-actor innovation** on deepfake biometric attacks → forces Immutable Identifier layer to re-invest in liveness (temporarily pulls it *left* toward Custom-Built for specific controls).

## Open Questions

1. **Will Entities (devices, orgs, agents) be forced into the same identity stack as citizens, or will they evolve a parallel stack?** Machine identity (SPIFFE, Workload Identity) is diverging from human identity faster than the scenario's "Entities" anchor suggests. Worth a submap.

2. **Is Benevolence operationalisable at all, or is it inherently Genesis?** The map places it at 0.22; if the answer is "no operational form is ever possible", benevolence can never evolve and must be handled by institutional design rather than technology.

3. **Where does AI-agent identity sit?** November 2022 predates the GPT-4 / agent explosion. By the time this map's predicted evolution plays out (late 2024), AI-agent identity will likely require a new trust-layer branch that doesn't exist in this map.

---

*Notes on map construction: this map exceeds the skill's 15-component guidance because the scenario brief specifies three parallel chains (power / trust / regulation-rules-exceptions) attaching to the core identity chain — the tensions the map must show require all three to be visible simultaneously. The authority-and-identifier region (SSI, Centralised Authority, Decentralised Authority, Issuing Authority, three identifier types) would be a sensible submap for a deeper pass.*
