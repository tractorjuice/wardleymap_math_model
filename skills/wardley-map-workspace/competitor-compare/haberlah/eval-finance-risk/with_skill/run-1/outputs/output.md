# Wardley Map Analysis: Risk Management in Financial Services

## Purpose

How does risk management operate across the financial services landscape, and where is regulation lagging the risk it is meant to cover? Specifically: where do cost, value, trust, and supply-chain awareness sit on the evolution axis, and what does the accountability chain back to society look like when those positions shift?

This map traces demand from the public, corporations, and governments through the provider layer (retail banking, insurance, lending), the trust-and-assets substrate, the risk types that threaten the system, and the accountability chain that runs from society back up into regulation.

---

## Strategic Context

- **Strategic question:** Where is regulation lagging risk evolution, and what build/buy/outsource decisions follow from the map?
- **User anchors:** Public, Corporations, Governments — three distinct demand sources with overlapping but non-identical needs.
- **Core needs:** Access to banking, insurance cover, lending capacity; confidence that the system is supervised; accountability when it fails.
- **Scope:** Financial services sector at a national-plus-systemic-global level, as of 2024-2026. Single main map (18 components + 3 anchors = 21 nodes); exceeds the 8-15 guideline because the scenario explicitly requires this breadth. Submap splits flagged in "Open Questions" below.

---

## Deliverable 1 — OWM Text Block

```owm
title Risk Management in Financial Services
style wardley

anchor Public [0.97, 0.55]
anchor Corporations [0.95, 0.50]
anchor Governments [0.96, 0.45]

component Retail Banking [0.78, 0.82]
component Insurance [0.76, 0.72]
component Lending [0.74, 0.70]
component Trust [0.68, 0.35] inertia
component Assets [0.62, 0.78]
component Rating Agencies [0.58, 0.68]
component Regulation [0.62, 0.42] inertia
component Value [0.54, 0.55]
component Cost [0.52, 0.82]
component Sovereignty [0.50, 0.22]
component Credit Risk [0.46, 0.78]
component System Risk [0.42, 0.52]
component Cybersecurity Risk [0.38, 0.38]
component Third-party Risk [0.34, 0.30]
component Cascade Failure Risk [0.30, 0.18]
component Supply-chain Awareness [0.22, 0.16]
component Society [0.26, 0.48]
component Accountability Chain [0.14, 0.32]

Public->Retail Banking
Public->Insurance
Corporations->Lending
Corporations->Insurance
Corporations->Retail Banking
Governments->Regulation
Governments->Sovereignty
Retail Banking->Trust
Retail Banking->Assets
Retail Banking->Cost
Insurance->Trust
Insurance->Assets
Insurance->Rating Agencies
Lending->Trust
Lending->Assets
Lending->Rating Agencies
Lending->Credit Risk
Retail Banking->Regulation
Insurance->Regulation
Lending->Regulation
Rating Agencies->Credit Risk
Trust->Value
Assets->Value
Value->Cost
Regulation->Sovereignty
Regulation->System Risk
Regulation->Cybersecurity Risk
Retail Banking->Cybersecurity Risk
Insurance->System Risk
Lending->System Risk
System Risk->Cascade Failure Risk
Cybersecurity Risk->Third-party Risk
Third-party Risk->Supply-chain Awareness
Cascade Failure Risk->Supply-chain Awareness
Regulation->Society
Society->Accountability Chain
Supply-chain Awareness->Accountability Chain

evolve Cybersecurity Risk 0.58
evolve Third-party Risk 0.52
evolve Supply-chain Awareness 0.40
evolve Regulation 0.58
evolve Sovereignty 0.40
evolve Cascade Failure Risk 0.38

annotation 1 [[0.42, 0.36]] Regulation lags the risks it is meant to cover
annotation 2 [[0.22, 0.18]] Supply-chain awareness is weakly instrumented
annotation 3 [[0.68, 0.38]] Trust carries inertia: bespoke to each institution
```

---

## Deliverable 2 — Component Evolution Assessment

| Component | Stage | Position [vis, mat] | Rationale |
|---|---|---|---|
| Public | Anchor | [0.97, 0.55] | Consumer demand for financial services; broad, stable, price-sensitive. |
| Corporations | Anchor | [0.95, 0.50] | Business demand for capital, settlement, risk transfer; sophisticated buyers. |
| Governments | Anchor | [0.96, 0.45] | Sovereign demand for stable markets and tax revenue; also the rule-setter. |
| Retail Banking | Commodity | [0.78, 0.82] | Ubiquitous, utility-priced (current accounts, payments). Multiple interchangeable providers; failure is catastrophic ("bank run"). Clearly Commodity / Utility. |
| Insurance | Product (+Rental) | [0.76, 0.72] | Well-defined product categories (life, health, property, liability); many competing providers; comparable via rating agencies. Drifting toward Commodity in personal lines, still Product in specialty. |
| Lending | Product (+Rental) | [0.74, 0.70] | Credit products are standardised (mortgage, term loan, revolver) with multiple providers and published pricing. Securitisation has pushed it further right than 10 years ago. |
| Trust | Custom-Built (inertia) | [0.68, 0.35] | Reputational capital is bespoke to each institution; not fungible; cannot be bought off the shelf. Inertia marker: incumbents resist any evolution that would make trust transferable (open banking, portable identity). |
| Assets | Commodity | [0.62, 0.78] | Underlying assets (cash, securities, real estate, derivatives) trade on standardised, deeply liquid markets with transparent pricing. |
| Rating Agencies | Product (+Rental) | [0.58, 0.68] | Three dominant providers (Moody's, S&P, Fitch) with standardised methodologies; users compare their ratings and occasionally switch. Not yet a utility because methodology still differentiates. |
| Regulation | Custom-Built (inertia) | [0.62, 0.42] | Each jurisdiction's rulebook is bespoke; Basel III/IV provides common scaffolding but implementation is local, slow, and politically negotiated. Inertia marker: regulation consistently lags the risks it targets — the central observation of this map. |
| Value | Product | [0.54, 0.55] | Valuation methodologies (DCF, mark-to-market, actuarial) are well-documented and trainable; multiple tool vendors; still enough variance across firms to matter. |
| Cost | Commodity | [0.52, 0.82] | Cost accounting is fully commoditised; standard frameworks (activity-based, transfer pricing); pay-per-use tooling. |
| Sovereignty | Custom-Built | [0.50, 0.22] | In financial services sovereignty over data, settlement rails, and digital currency is still being defined; no agreed pattern; live political debate (CBDCs, cross-border data, crypto regulation). |
| Credit Risk | Commodity | [0.46, 0.78] | Credit scoring, PD/LGD/EAD modelling, IFRS 9 — a codified, trainable, standardised discipline. Failure is not tolerated by regulators. Firmly Commodity. |
| System Risk | Product | [0.42, 0.52] | Stress tests, DSIB/GSIB designations, macroprudential tooling exist and are practised; methodology is converging but still argued over. |
| Cybersecurity Risk | Custom-Built | [0.38, 0.38] | Threat landscape changes faster than frameworks; bespoke controls per firm; MITRE/NIST common vocabulary emerging but implementation is still specialist work. Evolution pressure is high. |
| Third-party Risk | Custom-Built | [0.34, 0.30] | Vendor risk management is bespoke: each firm runs its own questionnaires, audits, monitoring. Shared utilities (e.g. TPRM consortia) are emerging but nascent. |
| Cascade Failure Risk | Genesis | [0.30, 0.18] | Interconnected-failure modelling (e.g. across payment rails, CCPs, cloud providers) is early research, not codified practice. No agreed framework; regulators commission papers, not rules. |
| Supply-chain Awareness | Genesis | [0.22, 0.16] | Visibility into the full stack of providers, cloud vendors, third-country exposures, and concentrated suppliers is weak and mostly manual; SBOM-equivalents for financial services barely exist. |
| Society | Product | [0.26, 0.48] | The concept of societal accountability for financial-system outcomes (post-2008, post-COVID) is well-articulated; inquiry mechanisms, media scrutiny, and political channels are mature. |
| Accountability Chain | Custom-Built | [0.14, 0.32] | Bespoke per event: Senior Managers Regime (UK), Sarbanes-Oxley (US), national inquiries — the mechanism exists but each case reinvents procedure. |

---

## Deliverable 3 — Key Strategic Observations

1. **Regulation sits well left of the risks it is meant to cover.** Regulation is at Custom-Built (0.42) while Credit Risk is at Commodity (0.78). That gap is defensible for the oldest risk types (Basel caught up). The alarming gap is for the newer risks: Cybersecurity (0.38), Third-party (0.30), Cascade Failure (0.18), Supply-chain Awareness (0.16). Regulation is structurally a lagging indicator of risk evolution, but the lag is growing because the newest risks evolve faster than the rule-making cycle.

2. **The trust-and-assets layer is bifurcated.** Assets are Commodity (fungible, liquid, market-priced). Trust is Custom-Built with inertia. This is the single biggest structural asymmetry in financial services: every provider is trying to differentiate on trust while operating on commoditised assets. It explains why brand, scandal, and conduct matter so much even when the underlying product is identical across firms.

3. **Three Genesis components cluster at the bottom-left.** Cascade Failure Risk, Supply-chain Awareness, and arguably Sovereignty are all early-stage concerns that will drive the next generation of regulation. Firms that build capability here now are investing in what will be required within 5-10 years.

4. **The provider layer (Retail Banking, Insurance, Lending) is the most industrialised strip of the value chain.** All three sit 0.70-0.82 on maturity. This is where margin compression is structural and where build-vs-buy heavily favours buy. It is also where innovation must come from adjacent components (trust, risk modelling, customer experience) rather than from the core product itself.

5. **The accountability chain (vis ~0.14-0.26) is almost out of view.** Society and Accountability Chain are deliberately placed low on visibility because demand-side actors rarely see them until a crisis occurs. Their low visibility and modest maturity mean that when a crisis hits, the chain activates slowly and bespoke-ly — which is exactly what the scenario flagged as worth examining.

---

## Doctrine Check

| Principle | Reading on this map |
|---|---|
| **Know your users** | Three anchors (Public, Corporations, Governments) are explicit and have distinct demand profiles. Pass. |
| **Remove bias and duplication** | Third-party Risk and Supply-chain Awareness overlap. Kept separate because the scenario distinguishes them, but many firms conflate them — duplicated effort signal. |
| **Use appropriate methods** | Regulators apply Six Sigma / ITIL style rules (appropriate for Commodity Credit Risk). Applying the same methods to Genesis Cascade Failure Risk is a method mismatch — it is what produces check-the-box outputs with no real coverage. |
| **Manage inertia** | Two explicit inertia markers: Trust and Regulation. Both are correctly flagged; both resist evolution for structural reasons (reputational capital cannot be commoditised without destroying its value; regulation cannot move faster than political consensus). |
| **Strategy is iterative** | Evolution arrows show predicted 12-24 month movement on six components. Re-map annually. |
| **There is no core** | The components that incumbents consider "core" (Trust, Retail Banking franchise) are the ones most exposed to the next wave of commoditisation (open banking, portable identity). |

---

## Recommended Actions

1. **Invest ahead of regulation on Cybersecurity, Third-party, and Supply-chain risk.** These are the three components where the regulation-lag is largest and where Pioneer-stage thinking is required. Build internal capability now; it will become compliance capability within 3-5 years.

2. **Treat Credit Risk, Cost, Assets, and Retail Banking as Buy / Outsource.** These are Commodity. Running bespoke teams on commodity components is a doctrine failure ("appropriate methods"). Industry utilities and vendor platforms will match in-house output at a fraction of cost.

3. **Protect Trust via structure, not marketing.** Trust's inertia is a feature not a bug for incumbents — but only if it is backed by visible accountability. When Accountability Chain activates and is weak, Trust collapses rapidly (cf. 2008). The recommended move is to over-invest in Accountability Chain build-out while it is still Custom-Built (0.14, 0.32) — this is cheap insurance on Trust.

4. **Map Rating Agencies' evolution explicitly.** At 0.68 they are late Product. ESG rating, cyber rating, and climate-transition rating are Genesis-to-Custom extensions where the three incumbents have not locked in position. This is where a sensing-engine gameplay could work: aggregate data through a platform and commoditise a new rating category.

5. **Push for standardisation in Supply-chain Awareness.** Cross-firm consortia (analogous to SBOM in software) would pull this component from Genesis into Custom-Built in 2-3 years. Incumbents gain regulatory predictability; new entrants gain a cheaper path to compliance. Co-opting gameplay.

---

## Build vs. Buy Assessment

| Component | Recommendation | Rationale |
|---|---|---|
| Credit Risk | Buy / Use Utilities | Commodity. Standard vendor platforms and rating-agency data are the norm; in-house work is duplication. |
| Cost | Buy | Commodity. Accounting stacks are fully productised. |
| Retail Banking (core rails) | Buy / Outsource | Commodity. Core banking platforms (Temenos, Thought Machine, Mambu) are now credible buy options for all but the largest incumbents. |
| Rating Agencies' output | Buy | Product. Subscribe to services; do not rebuild. |
| System Risk modelling | Buy + Customise | Product-stage tooling exists but stress-test calibration is still firm-specific. |
| Cybersecurity Risk tooling | Buy (tools) + Build (operating model) | Custom-Built stage overall. Tools are productised; the operating model (SOC + response) is still bespoke. |
| Third-party Risk | Build (to start), Consortia (target) | Custom-Built. Near-term bespoke; medium-term move toward shared utilities. |
| Cascade Failure Risk modelling | Build / Invest | Genesis. No market alternative. Pioneer investment. |
| Supply-chain Awareness | Build / Invest | Genesis. No product market yet. Pioneer investment. |
| Trust | Build (structural) | Not a buy. Reputational capital is Custom-Built and must be owned. |
| Accountability Chain | Build (operating) | Custom-Built. Must be owned by the firm and exercised visibly. |

---

## Evolution Predictions (12-24 months)

Six evolution arrows on the map:

- **Cybersecurity Risk** 0.38 → 0.58 (Custom-Built → Product). NIS2, DORA, SEC cyber rules are pulling it right; productised SOC/XDR offerings are credible.
- **Third-party Risk** 0.30 → 0.52 (Custom-Built → Product). DORA Article 28, TPRM consortia.
- **Supply-chain Awareness** 0.16 → 0.40 (Genesis → Custom-Built). Concentration-risk scrutiny on cloud providers and critical vendors.
- **Cascade Failure Risk** 0.18 → 0.38 (Genesis → Custom-Built). Central-bank-commissioned research hardening into expected practice.
- **Regulation** 0.42 → 0.58 (Custom-Built → Product). Regulatory tech (RegTech) and cross-border harmonisation pulling Regulation toward Product-stage tooling — this narrows the regulation-to-risk gap modestly.
- **Sovereignty** 0.22 → 0.40 (Genesis → Custom-Built). CBDC, data-residency, crypto regimes crystallising country-by-country.

Inertia on Trust and Regulation is real. Expect Regulation to move slower than the arrow suggests; the arrow is conditional on regulators being willing to industrialise compliance interfaces.

---

## Open Questions

1. **Should Retail Banking, Insurance, and Lending be submaps?** All three have internal value chains (deposit-taking vs payments vs lending inside Retail Banking, for example) that could justify splitting each into its own map. The main map stays the same; each provider component becomes a submap reference.
2. **Is Trust one component or three?** Brand trust, operational trust, and fiduciary trust may behave differently on the evolution axis and should probably be separated in v2 of this map.
3. **Where should "AI-in-banking" live?** Not in scope of the original scenario but likely to become a Pioneer component by next year, sitting between Cybersecurity Risk and System Risk with high uncertainty and high leverage. Flag for next revision.

---

## Deliverable (Interactive Artifact) — React Component

The following React component renders an interactive Wardley Map with hover tooltips, click-to-highlight dependency chains, a figure legend, and evolution stage shading. It follows the architecture in `templates/artifact-template.jsx`.

```jsx
import { useState, useCallback, useMemo } from "react";

// --- Canvas / style constants ---
const WIDTH = 1100;
const HEIGHT = 780;
const PADDING = { top: 55, right: 30, bottom: 95, left: 70 };
const COLORS = {
  background: "#ffffff",
  stageFills: ["#fef9f0", "#fefcf7", "#f7faf7", "#f0f6fe"],
  gridLine: "#e2e2e2",
  axisLine: "#555555",
  axisLabel: "#666666",
  stageLabel: "#888888",
  componentFill: "#ffffff",
  componentStroke: "#333333",
  componentStrokeSelected: "#1a73e8",
  dependencyLine: "#aaaaaa",
  evolutionArrow: "#d94040",
  inertiaBar: "#333333",
  tooltipBg: "#1a1a2e",
  tooltipText: "#f0f0f0",
  legendBorder: "#dddddd",
  labelText: "#222222",
  dimmedOpacity: 0.15
};
const STAGE_BOUNDARIES = [0.25, 0.50, 0.75];
const STAGE_LABELS = ["Genesis", "Custom-Built", "Product (+Rental)", "Commodity (+Utility)"];

const toSvgX = (m) => PADDING.left + m * (WIDTH - PADDING.left - PADDING.right);
const toSvgY = (v) => PADDING.top + (1 - v) * (HEIGHT - PADDING.top - PADDING.bottom);

const MAP = {
  title: "Risk Management in Financial Services",
  purpose: "Where regulation lags the risk it is meant to cover",
  components: [
    { id: "public", name: "Public", visibility: 0.97, maturity: 0.55, stage: "Anchor", rationale: "Consumer demand for financial services: deposits, payments, insurance, credit.", isAnchor: true },
    { id: "corporations", name: "Corporations", visibility: 0.95, maturity: 0.50, stage: "Anchor", rationale: "Business demand for capital, settlement, and risk transfer.", isAnchor: true },
    { id: "governments", name: "Governments", visibility: 0.96, maturity: 0.45, stage: "Anchor", rationale: "Sovereign demand for stable markets; also the rule-setter.", isAnchor: true },
    { id: "retail-banking", name: "Retail Banking", visibility: 0.78, maturity: 0.82, stage: "Commodity", rationale: "Ubiquitous, utility-priced accounts and payments; interchangeable providers; catastrophic failure tolerance." },
    { id: "insurance", name: "Insurance", visibility: 0.76, maturity: 0.72, stage: "Product", rationale: "Standard product categories (life, health, P&C) with many competing providers and comparable ratings." },
    { id: "lending", name: "Lending", visibility: 0.74, maturity: 0.70, stage: "Product", rationale: "Standardised credit products; securitisation has pushed it further right; multiple providers with published pricing." },
    { id: "trust", name: "Trust", visibility: 0.68, maturity: 0.35, stage: "Custom-Built", rationale: "Reputational capital bespoke to each institution; not fungible; cannot be bought off the shelf.", inertia: true },
    { id: "assets", name: "Assets", visibility: 0.62, maturity: 0.78, stage: "Commodity", rationale: "Underlying assets trade on deeply liquid, standardised markets with transparent pricing." },
    { id: "rating", name: "Rating Agencies", visibility: 0.58, maturity: 0.68, stage: "Product", rationale: "Three dominant providers with standardised methodologies; users compare and occasionally switch." },
    { id: "regulation", name: "Regulation", visibility: 0.62, maturity: 0.42, stage: "Custom-Built", rationale: "Bespoke per jurisdiction; Basel scaffolding but local implementation; consistently lags the risks it targets.", inertia: true },
    { id: "value", name: "Value", visibility: 0.54, maturity: 0.55, stage: "Product", rationale: "Valuation methodologies (DCF, mark-to-market, actuarial) are documented and trainable; tool vendors exist." },
    { id: "cost", name: "Cost", visibility: 0.52, maturity: 0.82, stage: "Commodity", rationale: "Cost accounting fully commoditised; standard frameworks and pay-per-use tooling." },
    { id: "sovereignty", name: "Sovereignty", visibility: 0.50, maturity: 0.22, stage: "Custom-Built", rationale: "Sovereignty over data, settlement rails, and digital currency still being defined; live political debate (CBDCs, crypto)." },
    { id: "credit-risk", name: "Credit Risk", visibility: 0.46, maturity: 0.78, stage: "Commodity", rationale: "PD/LGD/EAD modelling, IFRS 9 — codified, trainable, standardised; failure not tolerated by regulators." },
    { id: "system-risk", name: "System Risk", visibility: 0.42, maturity: 0.52, stage: "Product", rationale: "Stress tests, GSIB designations, macroprudential tooling exist and are practised; methodology converging." },
    { id: "cyber-risk", name: "Cybersecurity Risk", visibility: 0.38, maturity: 0.38, stage: "Custom-Built", rationale: "Threat landscape changes faster than frameworks; MITRE/NIST vocabulary emerging; implementation is specialist." },
    { id: "third-party-risk", name: "Third-party Risk", visibility: 0.34, maturity: 0.30, stage: "Custom-Built", rationale: "Vendor risk management is bespoke per firm; shared utilities nascent." },
    { id: "cascade-risk", name: "Cascade Failure Risk", visibility: 0.30, maturity: 0.18, stage: "Genesis", rationale: "Interconnected-failure modelling across payment rails, CCPs, cloud providers is early research, not codified practice." },
    { id: "sca", name: "Supply-chain Awareness", visibility: 0.22, maturity: 0.16, stage: "Genesis", rationale: "Visibility into full provider stack, cloud vendors, third-country exposures is weak and mostly manual." },
    { id: "society", name: "Society", visibility: 0.26, maturity: 0.48, stage: "Product", rationale: "Societal accountability mechanisms (inquiries, media, political channels) are mature." },
    { id: "accountability", name: "Accountability Chain", visibility: 0.14, maturity: 0.32, stage: "Custom-Built", rationale: "Bespoke per event: Senior Managers Regime, SOX, national inquiries — mechanism exists but each case reinvents procedure." }
  ],
  links: [
    { from: "public", to: "retail-banking" },
    { from: "public", to: "insurance" },
    { from: "corporations", to: "lending" },
    { from: "corporations", to: "insurance" },
    { from: "corporations", to: "retail-banking" },
    { from: "governments", to: "regulation" },
    { from: "governments", to: "sovereignty" },
    { from: "retail-banking", to: "trust" },
    { from: "retail-banking", to: "assets" },
    { from: "retail-banking", to: "cost" },
    { from: "insurance", to: "trust" },
    { from: "insurance", to: "assets" },
    { from: "insurance", to: "rating" },
    { from: "lending", to: "trust" },
    { from: "lending", to: "assets" },
    { from: "lending", to: "rating" },
    { from: "lending", to: "credit-risk" },
    { from: "retail-banking", to: "regulation" },
    { from: "insurance", to: "regulation" },
    { from: "lending", to: "regulation" },
    { from: "rating", to: "credit-risk" },
    { from: "trust", to: "value" },
    { from: "assets", to: "value" },
    { from: "value", to: "cost" },
    { from: "regulation", to: "sovereignty" },
    { from: "regulation", to: "system-risk" },
    { from: "regulation", to: "cyber-risk" },
    { from: "retail-banking", to: "cyber-risk" },
    { from: "insurance", to: "system-risk" },
    { from: "lending", to: "system-risk" },
    { from: "system-risk", to: "cascade-risk" },
    { from: "cyber-risk", to: "third-party-risk" },
    { from: "third-party-risk", to: "sca" },
    { from: "cascade-risk", to: "sca" },
    { from: "regulation", to: "society" },
    { from: "society", to: "accountability" },
    { from: "sca", to: "accountability" }
  ],
  evolutions: [
    { componentId: "cyber-risk", toMaturity: 0.58 },
    { componentId: "third-party-risk", toMaturity: 0.52 },
    { componentId: "sca", toMaturity: 0.40 },
    { componentId: "regulation", toMaturity: 0.58 },
    { componentId: "sovereignty", toMaturity: 0.40 },
    { componentId: "cascade-risk", toMaturity: 0.38 }
  ],
  annotations: [
    { id: 1, text: "Regulation lags the risk it targets", x: 0.36, y: 0.48 },
    { id: 2, text: "Supply-chain awareness is weak", x: 0.18, y: 0.24 },
    { id: 3, text: "Trust carries inertia", x: 0.38, y: 0.72 }
  ]
};

function findDependencyChain(id, links) {
  const set = new Set([id]);
  let changed = true;
  while (changed) {
    changed = false;
    for (const l of links) {
      if (set.has(l.to) && !set.has(l.from)) { set.add(l.from); changed = true; }
      if (set.has(l.from) && !set.has(l.to)) { set.add(l.to); changed = true; }
    }
  }
  return set;
}

function computeLabelOffsets(components) {
  const out = {};
  const pos = components.map(c => ({ id: c.id, sx: toSvgX(c.maturity), sy: toSvgY(c.visibility) }));
  for (const c of components) {
    let dx = 10, dy = -12;
    const sx = toSvgX(c.maturity), sy = toSvgY(c.visibility);
    for (const o of pos) {
      if (o.id === c.id) continue;
      if (Math.abs(sx - o.sx) < 80 && Math.abs(sy - o.sy) < 22) {
        dy = sy <= o.sy ? -14 : 16;
      }
    }
    if (sx + dx + c.name.length * 6 > WIDTH - PADDING.right) dx = -(c.name.length * 6 + 10);
    if (sy + dy < PADDING.top + 10) dy = 14;
    out[c.id] = { dx, dy };
  }
  return out;
}

export default function WardleyMap() {
  const [hoveredId, setHoveredId] = useState(null);
  const [selectedId, setSelectedId] = useState(null);
  const [tip, setTip] = useState({ x: 0, y: 0 });

  const map = MAP;
  const offs = useMemo(() => computeLabelOffsets(map.components), [map.components]);
  const chain = useMemo(() => selectedId ? findDependencyChain(selectedId, map.links) : null, [selectedId, map.links]);
  const byId = useMemo(() => Object.fromEntries(map.components.map(c => [c.id, c])), [map.components]);
  const isV = useCallback((id) => !chain || chain.has(id), [chain]);
  const isLV = useCallback((l) => !chain || (chain.has(l.from) && chain.has(l.to)), [chain]);
  const onHover = useCallback((e, c) => {
    const r = e.currentTarget.closest("svg").getBoundingClientRect();
    setHoveredId(c.id);
    setTip({ x: e.clientX - r.left, y: e.clientY - r.top });
  }, []);
  const hovered = hoveredId ? byId[hoveredId] : null;

  function depPath(a, b) {
    const x1 = toSvgX(a.maturity), y1 = toSvgY(a.visibility);
    const x2 = toSvgX(b.maturity), y2 = toSvgY(b.visibility);
    const mx = (x1 + x2) / 2, my = (y1 + y2) / 2;
    const curve = Math.abs(x1 - x2) < 20 ? 15 : 0;
    return `M ${x1} ${y1} Q ${mx + curve} ${my} ${x2} ${y2}`;
  }

  return (
    <div className="w-full max-w-5xl mx-auto p-4">
      <h2 className="text-lg font-semibold text-gray-800 mb-1">{map.title}</h2>
      <p className="text-sm text-gray-500 mb-3">{map.purpose}</p>
      <div className="relative border border-gray-200 rounded bg-white">
        <svg viewBox={`0 0 ${WIDTH} ${HEIGHT}`} className="w-full h-auto"
          style={{ fontFamily: "'Segoe UI', system-ui, sans-serif" }}
          onClick={() => setSelectedId(null)}>

          {STAGE_LABELS.map((_, i) => {
            const x0 = toSvgX(i === 0 ? 0 : STAGE_BOUNDARIES[i - 1]);
            const x1 = toSvgX(i < STAGE_BOUNDARIES.length ? STAGE_BOUNDARIES[i] : 1);
            return <rect key={i} x={x0} y={PADDING.top} width={x1 - x0}
              height={HEIGHT - PADDING.top - PADDING.bottom} fill={COLORS.stageFills[i]} />;
          })}

          {STAGE_BOUNDARIES.map((b, i) => (
            <line key={i} x1={toSvgX(b)} y1={PADDING.top}
              x2={toSvgX(b)} y2={HEIGHT - PADDING.bottom}
              stroke={COLORS.gridLine} strokeDasharray="6 4" strokeWidth={1} />
          ))}

          <line x1={PADDING.left} y1={PADDING.top} x2={PADDING.left}
            y2={HEIGHT - PADDING.bottom} stroke={COLORS.axisLine} strokeWidth={1.5} />
          <line x1={PADDING.left} y1={HEIGHT - PADDING.bottom}
            x2={WIDTH - PADDING.right} y2={HEIGHT - PADDING.bottom}
            stroke={COLORS.axisLine} strokeWidth={1.5} />
          <text x={PADDING.left - 10} y={PADDING.top - 8} textAnchor="middle"
            fontSize={11} fill={COLORS.axisLabel} fontWeight={500}>Visible</text>
          <text x={PADDING.left - 10} y={HEIGHT - PADDING.bottom + 18} textAnchor="middle"
            fontSize={11} fill={COLORS.axisLabel} fontWeight={500}>Invisible</text>
          <text transform={`rotate(-90, 18, ${(PADDING.top + HEIGHT - PADDING.bottom) / 2})`}
            x={18} y={(PADDING.top + HEIGHT - PADDING.bottom) / 2} textAnchor="middle"
            fontSize={12} fill={COLORS.axisLabel} fontWeight={600}>Value Chain</text>
          {STAGE_LABELS.map((lab, i) => {
            const a = i === 0 ? 0 : STAGE_BOUNDARIES[i - 1];
            const b = i < STAGE_BOUNDARIES.length ? STAGE_BOUNDARIES[i] : 1;
            return <text key={i} x={toSvgX((a + b) / 2)} y={HEIGHT - PADDING.bottom + 20}
              textAnchor="middle" fontSize={11} fill={COLORS.stageLabel} fontWeight={500}>{lab}</text>;
          })}
          <text x={(PADDING.left + WIDTH - PADDING.right) / 2} y={HEIGHT - PADDING.bottom + 38}
            textAnchor="middle" fontSize={12} fill={COLORS.axisLabel} fontWeight={600}>Evolution</text>

          {map.links.map((l, i) => {
            const a = byId[l.from], b = byId[l.to];
            if (!a || !b) return null;
            return <path key={i} d={depPath(a, b)} fill="none"
              stroke={COLORS.dependencyLine} strokeWidth={1}
              opacity={isLV(l) ? 1 : COLORS.dimmedOpacity} />;
          })}

          {map.evolutions.map((e, i) => {
            const c = byId[e.componentId];
            if (!c) return null;
            const x1 = toSvgX(c.maturity), y1 = toSvgY(c.visibility);
            const x2 = toSvgX(e.toMaturity);
            return <g key={i} opacity={isV(e.componentId) ? 1 : COLORS.dimmedOpacity}>
              <defs>
                <marker id={`arr-${i}`} viewBox="0 0 10 10" refX="9" refY="5"
                  markerWidth="6" markerHeight="6" orient="auto">
                  <path d="M 0 0 L 10 5 L 0 10 z" fill={COLORS.evolutionArrow} />
                </marker>
              </defs>
              <line x1={x1 + 8} y1={y1} x2={x2 - 4} y2={y1}
                stroke={COLORS.evolutionArrow} strokeWidth={1.4}
                strokeDasharray="4 3" markerEnd={`url(#arr-${i})`} />
            </g>;
          })}

          {map.components.map((c) => {
            const sx = toSvgX(c.maturity), sy = toSvgY(c.visibility);
            const off = offs[c.id];
            const isSel = selectedId === c.id;
            const r = c.isAnchor ? 7 : 6;
            return <g key={c.id} opacity={isV(c.id) ? 1 : COLORS.dimmedOpacity}
              onClick={(e) => { e.stopPropagation(); setSelectedId(c.id); }}
              onMouseEnter={(e) => onHover(e, c)}
              onMouseLeave={() => setHoveredId(null)}
              style={{ cursor: "pointer" }}>
              {c.inertia && <line x1={sx + 10} y1={sy - 10} x2={sx + 10} y2={sy + 10}
                stroke={COLORS.inertiaBar} strokeWidth={3} />}
              <circle cx={sx} cy={sy} r={r} fill={c.isAnchor ? "#fff7e0" : COLORS.componentFill}
                stroke={isSel ? COLORS.componentStrokeSelected : COLORS.componentStroke}
                strokeWidth={isSel ? 2 : 1.2} />
              <text x={sx + off.dx} y={sy + off.dy} fontSize={11}
                fill={COLORS.labelText} fontWeight={c.isAnchor ? 600 : 400}>{c.name}</text>
            </g>;
          })}

          {map.annotations.map((a) => (
            <g key={a.id}>
              <circle cx={toSvgX(a.x)} cy={toSvgY(a.y)} r={10}
                fill="#fff7e0" stroke="#c7a550" strokeWidth={1} />
              <text x={toSvgX(a.x)} y={toSvgY(a.y) + 4} textAnchor="middle"
                fontSize={10} fill="#7a6020" fontWeight={600}>{a.id}</text>
            </g>
          ))}

          <text x={PADDING.left} y={PADDING.top - 20} fontSize={13}
            fill={COLORS.labelText} fontWeight={700}>{map.title}</text>

          {/* Figure Legend */}
          <g transform={`translate(${WIDTH - 260}, ${HEIGHT - 80})`}>
            <rect x={0} y={0} width={230} height={70} fill="#fafafa"
              stroke={COLORS.legendBorder} strokeWidth={1} rx={4} />
            <text x={8} y={12} fontSize={10} fontWeight={700} fill="#333">Legend</text>
            <circle cx={18} cy={26} r={5} fill="#fff" stroke="#333" strokeWidth={1} />
            <text x={30} y={29} fontSize={9} fill="#333">Component</text>
            <line x1={100} y1={26} x2={130} y2={26} stroke="#aaa" strokeWidth={1} />
            <text x={134} y={29} fontSize={9} fill="#333">Dependency</text>
            <line x1={8} y1={42} x2={30} y2={42} stroke={COLORS.evolutionArrow}
              strokeWidth={1.4} strokeDasharray="4 3" />
            <text x={34} y={45} fontSize={9} fill="#333">Evolve arrow</text>
            <line x1={100} y1={36} x2={100} y2={48} stroke="#333" strokeWidth={3} />
            <text x={106} y={45} fontSize={9} fill="#333">Inertia</text>
            <circle cx={160} cy={42} r={7} fill="#fff7e0" stroke="#c7a550" />
            <text x={170} y={45} fontSize={9} fill="#333">Annotation</text>
            <text x={8} y={62} fontSize={9} fill="#333">Columns: Genesis / Custom / Product / Commodity</text>
          </g>
        </svg>

        {hovered && (
          <div style={{
            position: "absolute", left: tip.x + 12, top: tip.y + 12,
            background: COLORS.tooltipBg, color: COLORS.tooltipText,
            padding: "8px 10px", borderRadius: 4, fontSize: 12,
            maxWidth: 300, pointerEvents: "none", zIndex: 10
          }}>
            <div style={{ fontWeight: 700 }}>{hovered.name}</div>
            <div style={{ opacity: 0.8, fontSize: 11 }}>
              {hovered.stage} — [{hovered.visibility.toFixed(2)}, {hovered.maturity.toFixed(2)}]
            </div>
            <div style={{ marginTop: 4 }}>{hovered.rationale}</div>
          </div>
        )}
      </div>
    </div>
  );
}
```

---

## Map Summary

- **Components:** 18 (plus 3 anchors = 21 total nodes).
- **Dependencies:** 37.
- **Evolution arrows:** 6.
- **Inertia markers:** 2 (Trust, Regulation).
- **Annotations:** 3.
- **Stages represented:** Genesis (2), Custom-Built (6; 2 with inertia), Product (6), Commodity (4), plus 3 Anchors.

The principal finding is the structural lag between Regulation (Custom-Built, 0.42) and the risks it is meant to cover — particularly the three Genesis-to-Custom-Built risks (Cascade Failure, Supply-chain Awareness, Third-party) that sit far below the accountability chain in visibility. Closing that gap is the highest-leverage strategic move the system can make, and it requires Pioneer-stage investment in components that do not yet have markets.
