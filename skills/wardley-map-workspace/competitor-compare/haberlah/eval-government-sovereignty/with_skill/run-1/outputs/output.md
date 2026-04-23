# Wardley Map Analysis: National Sovereignty (Government View, April 2023)

A government's view of national sovereignty in April 2023: the supranational layer, government, corporations and society as anchors; the six pillars of sovereignty (territorial, economic, political, digital, cultural, security); the four theatres in which they play out (land, supply chain, cyber, CNI); the awareness apparatus and capability layer that make them operable; the social norms and election legitimacy that underwrite the government's mandate; the media mix that shapes perception; crisis response, law, and the feedback loop from felt success and belonging back into legitimacy.

The map deliberately spans 35 components (four anchors + 31 components) because the scenario asks for explicit coverage of a large, heterogeneous landscape. This is above the skill's recommended 15-18 limit and the validator flags it; per the skill's guidance the map could reasonably be split into a main map (anchors, legitimacy, pillars, theatres) plus submaps (awareness, norms, media mix). For a single-view strategic read we keep one map with careful spacing and annotations; where readability suffers, recommend generating submaps per pillar in a follow-up.

---

## 1. Interactive React Artifact (`.jsx`)

Paste this into a Claude.ai React artifact. It renders the full interactive map with hover tooltips, click-to-highlight dependency chains, evolution arrows, inertia markers, annotations, and a figure legend.

```jsx
import { useState, useCallback, useMemo } from "react";

// ============================================================
// 1. CONSTANTS
// ============================================================

const WIDTH = 1200;
const HEIGHT = 860;
const PADDING = { top: 55, right: 30, bottom: 100, left: 80 };

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
  pipelineFill: "rgba(180,180,180,0.12)",
  pipelineStroke: "#bbbbbb",
  tooltipBg: "#1a1a2e",
  tooltipText: "#f0f0f0",
  legendBorder: "#dddddd",
  title: "#1a1a1a",
  labelText: "#222222",
  dimmedOpacity: 0.15
};

const STAGE_BOUNDARIES = [0.25, 0.50, 0.75];
const STAGE_LABELS = ["Genesis", "Custom-Built", "Product (+Rental)", "Commodity (+Utility)"];

function toSvgX(maturity) {
  return PADDING.left + maturity * (WIDTH - PADDING.left - PADDING.right);
}
function toSvgY(visibility) {
  return PADDING.top + (1 - visibility) * (HEIGHT - PADDING.top - PADDING.bottom);
}

// ============================================================
// 2. MAP DATA — National Sovereignty (Government View, April 2023)
// ============================================================

const MAP = {
  title: "National Sovereignty (Government View, April 2023)",
  purpose: "Where sovereignty is industrialised infrastructure and where it is still contested and fragile.",
  components: [
    { id: "supranational", name: "Supranational", visibility: 0.98, maturity: 0.40, stage: "Custom-Built", isAnchor: true,
      rationale: "UN, G7/G20, WTO, EU, NATO are well-established institutions, but their authority vs national interest is under active re-contestation (Russia, China, trade wars)." },
    { id: "society", name: "Society", visibility: 0.96, maturity: 0.52, stage: "Product", isAnchor: true,
      rationale: "Permanent beneficiary; the people a government must serve. Always at the top of the chain." },
    { id: "government", name: "Government", visibility: 0.94, maturity: 0.65, stage: "Product", isAnchor: true,
      rationale: "The mapping actor — the modern nation-state executive is a mature institutional form though effectiveness varies." },
    { id: "corporations-shareholders", name: "Corporations & Shareholders", visibility: 0.92, maturity: 0.80, stage: "Commodity", isAnchor: true,
      rationale: "Capital-market actors operate through highly standardised corporate, securities, and accounting frameworks (IFRS, GAAP, MiFID, SEC); interchangeable across jurisdictions." },
    { id: "legitimacy", name: "Legitimacy", visibility: 0.88, maturity: 0.40, stage: "Custom-Built",
      rationale: "A government's legitimacy is a judgement made by citizens and allies; bespoke per regime, no off-the-shelf 'legitimacy product'. Under more pressure in April 2023 than in any recent decade." },
    { id: "perception-of-success", name: "Perception of Success", visibility: 0.84, maturity: 0.30, stage: "Custom-Built",
      rationale: "Narrative construction around inflation, immigration, COVID, Ukraine is bespoke per government and media cycle; no standardised measure is authoritative." },
    { id: "public-belonging", name: "Public Belonging", visibility: 0.82, maturity: 0.20, stage: "Custom-Built",
      rationale: "Social cohesion is fragmenting along political, cultural, and digital lines; no stable template exists. Trending leftward (more contested) in 2023." },
    { id: "election-legitimacy", name: "Election Legitimacy", visibility: 0.78, maturity: 0.45, stage: "Custom-Built",
      rationale: "Procedurally productised (voter rolls, ballots, counting, ODIHR/OAS observation), but perceived legitimacy has been dragged leftward by 2020 US contestation, Jan 6, and industrial-scale disinformation. Re-contested across the West." },
    { id: "territorial-sovereignty", name: "Territorial Sovereignty", visibility: 0.74, maturity: 0.78, stage: "Commodity",
      rationale: "Westphalian borders, territorial jurisdiction, military control — the oldest and most codified pillar. Well-defined in international law and state practice." },
    { id: "economic-sovereignty", name: "Economic Sovereignty", visibility: 0.72, maturity: 0.52, stage: "Product",
      rationale: "Fiscal, monetary, tax, and trade instruments are well-understood institutional products (central banks, treasuries, customs). Re-contested post-2008 and by the 2022-23 sanctions regime, but still productised." },
    { id: "security-sovereignty", name: "Security Sovereignty", visibility: 0.70, maturity: 0.62, stage: "Product",
      rationale: "Defence procurement, alliances (NATO, AUKUS), intelligence services, military doctrine are mature. Vendor markets exist. Still Product because alliance reconfiguration is bespoke per era." },
    { id: "political-sovereignty", name: "Political Sovereignty", visibility: 0.68, maturity: 0.42, stage: "Product",
      rationale: "Parliamentary/presidential institutions, civil service, judicial independence are established products. Sits below Economic because populist pressures and democratic backsliding have made it more contested in April 2023." },
    { id: "cultural-sovereignty", name: "Cultural Sovereignty", visibility: 0.66, maturity: 0.28, stage: "Custom-Built",
      rationale: "Language, historical narrative, shared myth-making, national identity — deeply bespoke per state, increasingly contested by global platforms and diaspora communication." },
    { id: "digital-sovereignty", name: "Digital Sovereignty", visibility: 0.64, maturity: 0.17, stage: "Genesis", inertia: true,
      rationale: "Emerging concept with no settled definition — EU (GAIA-X, DMA/DSA, Data Act), China (Great Firewall, localisation), US (hyperscaler dominance), India (data residency) pursuing incompatible visions. Strong inertia from globally-scaled US hyperscaler dependency." },
    { id: "land", name: "Land", visibility: 0.60, maturity: 0.86, stage: "Commodity",
      rationale: "Physical territory, border control, land registry, conventional military operations — industrialised for centuries. Ukraine war is a reminder of land's primacy, not a change in its evolution stage." },
    { id: "cni", name: "CNI", visibility: 0.58, maturity: 0.58, stage: "Product",
      rationale: "Critical National Infrastructure (energy, water, telecoms, finance, health, transport) is regulated under explicit frameworks (UK NIS, EU NIS2, US PPD-21). Vendor markets and standards exist; still Product because OT/IT convergence is uneven." },
    { id: "supply-chain", name: "Supply Chain", visibility: 0.56, maturity: 0.30, stage: "Custom-Built", inertia: true,
      rationale: "Globalised JIT chains were industrialised, but COVID, Ukraine, and semiconductor stress have re-opened JIT vs resilience as a bespoke per-sector judgement call. Strong inertia from 30 years of JIT-optimised contracts and tooling." },
    { id: "cyber", name: "Cyber", visibility: 0.54, maturity: 0.22, stage: "Custom-Built",
      rationale: "Cyber defence is a rapidly evolving attacker-defender contest. Frameworks exist (NIST CSF, MITRE ATT&CK, Zero Trust) but state-grade capability, attribution, and offensive cyber are still bespoke per nation." },
    { id: "integrity", name: "Integrity", visibility: 0.51, maturity: 0.38, stage: "Custom-Built",
      rationale: "Anti-corruption institutions exist (auditors, ombudsmen, ICAC/GRECO), but perceived integrity is judged through local culture and is actively contested in populist politics." },
    { id: "competency", name: "Competency", visibility: 0.49, maturity: 0.52, stage: "Product",
      rationale: "Professional civil service, public management, measurable delivery KPIs are widespread (NAO, GAO, OECD SIGMA). Recognisable product though quality varies enormously between states." },
    { id: "fairness", name: "Fairness", visibility: 0.47, maturity: 0.22, stage: "Custom-Built",
      rationale: "Procedural and distributive fairness norms vary by political tradition; no single canonical definition. Actively contested in tax, immigration, welfare debates." },
    { id: "benevolence", name: "Benevolence", visibility: 0.45, maturity: 0.30, stage: "Custom-Built",
      rationale: "The sense that government acts in public rather than private interest — inherently judgemental and culturally specific. Corroded by post-2016 populism and conspiracy-adjacent media." },
    { id: "identity", name: "Identity", visibility: 0.43, maturity: 0.14, stage: "Genesis",
      rationale: "Civic identity is fragmenting along digital, diaspora, and culture-war lines; no stable operational model for shared national identity in 2023. Trending earlier in stage, not later." },
    { id: "territorial-awareness", name: "Territorial Awareness", visibility: 0.40, maturity: 0.75, stage: "Commodity",
      rationale: "Satellite imagery (commercial + state), AIS, land registry, border surveillance, GIS — utility-priced in 2023 (Planet, Maxar, Sentinel) with standardised APIs. Industrialised." },
    { id: "crisis-response", name: "Crisis Response", visibility: 0.38, maturity: 0.50, stage: "Product",
      rationale: "Post-COVID, emergency powers, COBR/NSC-style structures, reasonable-worst-case planning, and vaccine/PPE procurement have been codified. Product stage — each crisis still rewrites the playbook." },
    { id: "supply-chain-awareness", name: "Supply-Chain Awareness", visibility: 0.36, maturity: 0.22, stage: "Custom-Built",
      rationale: "Multi-tier supplier visibility is an active investment area (project44, Interos, Everstream, Altana) but deployments remain bespoke systems-integration projects. Moving rightward fast." },
    { id: "digital-chain-awareness", name: "Digital-Chain Awareness", visibility: 0.34, maturity: 0.12, stage: "Genesis",
      rationale: "Software bill-of-materials (SBOM), cloud dependency mapping, firmware provenance — nascent. CISA, NCSC, ENISA publishing guidance but tooling and practice are genesis. SolarWinds & Log4Shell put this on the map." },
    { id: "capability-layer", name: "Capability Layer", visibility: 0.30, maturity: 0.48, stage: "Product",
      rationale: "The deliverable machinery of government (agencies, digital services, procurement, civil service, GDS/USDS-style units). Widely recognised product but quality varies; OECD benchmarks exist." },
    { id: "laws", name: "Laws", visibility: 0.26, maturity: 0.82, stage: "Commodity",
      rationale: "Domestic statutes, regulations, case law, drafting, and enforcement are fully codified in functioning states. Commodity infrastructure of the state." },
    { id: "international-law", name: "International Law", visibility: 0.24, maturity: 0.52, stage: "Product",
      rationale: "Treaty systems, UN Charter, Vienna Conventions, ICJ/ICC, WTO DSB exist and are productised. Enforcement is contested (Russia/Ukraine, US-China) which keeps it mid-Product not Commodity." },
    { id: "mainstream-media", name: "Mainstream Media", visibility: 0.20, maturity: 0.70, stage: "Commodity",
      rationale: "Broadcast, print, cable news — mature commoditised industries with declining margins and standardised distribution. Influence is waning but infrastructure is industrialised." },
    { id: "education", name: "Education", visibility: 0.18, maturity: 0.62, stage: "Product",
      rationale: "State education systems are institutional products with well-defined curricula, teacher training, accreditation. Vendor markets for ed-tech exist. Culture-war contestation but infrastructure is productised." },
    { id: "social-media", name: "Social Media", visibility: 0.16, maturity: 0.82, stage: "Commodity",
      rationale: "Meta, YouTube, TikTok, X operate at commodity scale with utility-like pricing and APIs. Near-monopoly attention infrastructure; the state does not control this layer." },
    { id: "art", name: "Art", visibility: 0.14, maturity: 0.55, stage: "Product",
      rationale: "Creative industries (film, TV, music, games, publishing) are productised global markets with funding bodies, IP regimes, and distribution platforms. Soft-power component." },
    { id: "propaganda", name: "Propaganda", visibility: 0.10, maturity: 0.35, stage: "Custom-Built",
      rationale: "Strategic communication, influence operations, and hostile-state information warfare. The craft is old, but 2020s forms (bot networks, deepfakes, algorithmic amplification) are still being built. Bespoke per actor." }
  ],
  links: [
    { from: "supranational", to: "international-law" },
    { from: "supranational", to: "legitimacy" },
    { from: "society", to: "legitimacy" },
    { from: "society", to: "public-belonging" },
    { from: "society", to: "perception-of-success" },
    { from: "government", to: "legitimacy" },
    { from: "government", to: "territorial-sovereignty" },
    { from: "government", to: "economic-sovereignty" },
    { from: "government", to: "political-sovereignty" },
    { from: "government", to: "security-sovereignty" },
    { from: "government", to: "digital-sovereignty" },
    { from: "government", to: "cultural-sovereignty" },
    { from: "government", to: "election-legitimacy" },
    { from: "government", to: "crisis-response" },
    { from: "corporations-shareholders", to: "economic-sovereignty" },
    { from: "corporations-shareholders", to: "digital-sovereignty" },
    { from: "corporations-shareholders", to: "supply-chain" },
    { from: "legitimacy", to: "election-legitimacy" },
    { from: "legitimacy", to: "perception-of-success" },
    { from: "legitimacy", to: "public-belonging" },
    { from: "perception-of-success", to: "capability-layer" },
    { from: "perception-of-success", to: "crisis-response" },
    { from: "public-belonging", to: "identity" },
    { from: "public-belonging", to: "cultural-sovereignty" },
    { from: "election-legitimacy", to: "integrity" },
    { from: "election-legitimacy", to: "fairness" },
    { from: "election-legitimacy", to: "competency" },
    { from: "election-legitimacy", to: "social-media" },
    { from: "election-legitimacy", to: "mainstream-media" },
    { from: "territorial-sovereignty", to: "land" },
    { from: "territorial-sovereignty", to: "territorial-awareness" },
    { from: "economic-sovereignty", to: "supply-chain" },
    { from: "economic-sovereignty", to: "cni" },
    { from: "economic-sovereignty", to: "laws" },
    { from: "security-sovereignty", to: "land" },
    { from: "security-sovereignty", to: "cyber" },
    { from: "security-sovereignty", to: "cni" },
    { from: "security-sovereignty", to: "crisis-response" },
    { from: "political-sovereignty", to: "election-legitimacy" },
    { from: "political-sovereignty", to: "international-law" },
    { from: "political-sovereignty", to: "laws" },
    { from: "digital-sovereignty", to: "cyber" },
    { from: "digital-sovereignty", to: "cni" },
    { from: "digital-sovereignty", to: "digital-chain-awareness" },
    { from: "cultural-sovereignty", to: "education" },
    { from: "cultural-sovereignty", to: "art" },
    { from: "cultural-sovereignty", to: "mainstream-media" },
    { from: "cultural-sovereignty", to: "social-media" },
    { from: "cultural-sovereignty", to: "propaganda" },
    { from: "cultural-sovereignty", to: "identity" },
    { from: "cni", to: "capability-layer" },
    { from: "supply-chain", to: "supply-chain-awareness" },
    { from: "supply-chain", to: "capability-layer" },
    { from: "cyber", to: "digital-chain-awareness" },
    { from: "cyber", to: "capability-layer" },
    { from: "integrity", to: "laws" },
    { from: "competency", to: "capability-layer" },
    { from: "fairness", to: "laws" },
    { from: "benevolence", to: "laws" },
    { from: "identity", to: "education" },
    { from: "identity", to: "social-media" },
    { from: "territorial-awareness", to: "capability-layer" },
    { from: "crisis-response", to: "capability-layer" },
    { from: "crisis-response", to: "mainstream-media" },
    { from: "supply-chain-awareness", to: "capability-layer" },
    { from: "digital-chain-awareness", to: "capability-layer" },
    { from: "capability-layer", to: "laws" },
    { from: "mainstream-media", to: "laws" },
    { from: "social-media", to: "laws" },
    { from: "propaganda", to: "mainstream-media" },
    { from: "propaganda", to: "social-media" }
  ],
  evolutions: [
    { componentId: "digital-sovereignty", toMaturity: 0.35 },
    { componentId: "supply-chain", toMaturity: 0.45 },
    { componentId: "cyber", toMaturity: 0.38 },
    { componentId: "supply-chain-awareness", toMaturity: 0.42 },
    { componentId: "digital-chain-awareness", toMaturity: 0.32 },
    { componentId: "election-legitimacy", toMaturity: 0.55 }
  ],
  annotations: [
    { id: 1, text: "Digital sovereignty: genesis/custom; EU-US-China divergence, strong industry inertia", x: 0.22, y: 0.66 },
    { id: 2, text: "Supply chain re-assessment wave post-COVID & Ukraine; JIT vs JIC re-opening", x: 0.34, y: 0.56 },
    { id: 3, text: "Contested zone: election legitimacy dragged leftward by 2020-2021 disinformation wave", x: 0.48, y: 0.78 },
    { id: 4, text: "Industrialised: Westphalian land, borders, military doctrine", x: 0.88, y: 0.60 },
    { id: 5, text: "Commodity platforms (Meta/X/TikTok) dominate the attention layer", x: 0.84, y: 0.16 }
  ]
};

// ============================================================
// 3. HELPERS
// ============================================================

function findDependencyChain(componentId, links) {
  const connected = new Set([componentId]);
  let changed = true;
  while (changed) {
    changed = false;
    for (const link of links) {
      if (connected.has(link.to) && !connected.has(link.from)) {
        connected.add(link.from); changed = true;
      }
      if (connected.has(link.from) && !connected.has(link.to)) {
        connected.add(link.to); changed = true;
      }
    }
  }
  return connected;
}

function computeLabelOffsets(components) {
  const offsets = {};
  const positions = components.map(c => ({
    id: c.id, sx: toSvgX(c.maturity), sy: toSvgY(c.visibility)
  }));
  for (const comp of components) {
    let dx = 10, dy = -12;
    const sx = toSvgX(comp.maturity), sy = toSvgY(comp.visibility);
    for (const other of positions) {
      if (other.id === comp.id) continue;
      const distX = Math.abs(sx - other.sx), distY = Math.abs(sy - other.sy);
      if (distX < 70 && distY < 25) {
        if (sy <= other.sy) dy = -14; else dy = 16;
      }
    }
    if (sx + dx + comp.name.length * 6 > WIDTH - PADDING.right) dx = -(comp.name.length * 6 + 10);
    if (sy + dy < PADDING.top + 10) dy = 14;
    offsets[comp.id] = { dx, dy };
  }
  return offsets;
}

// ============================================================
// 4. MAIN COMPONENT
// ============================================================

export default function WardleyMap() {
  const [hoveredId, setHoveredId] = useState(null);
  const [selectedId, setSelectedId] = useState(null);
  const [tooltipPos, setTooltipPos] = useState({ x: 0, y: 0 });
  const map = MAP;

  const labelOffsets = useMemo(() => computeLabelOffsets(map.components), [map.components]);
  const selectedChain = useMemo(() => selectedId ? findDependencyChain(selectedId, map.links) : null, [selectedId, map.links]);
  const componentMap = useMemo(() => {
    const m = {}; map.components.forEach(c => { m[c.id] = c; }); return m;
  }, [map.components]);

  const isVisible = useCallback((id) => !selectedChain || selectedChain.has(id), [selectedChain]);
  const isLinkVisible = useCallback((link) => !selectedChain || (selectedChain.has(link.from) && selectedChain.has(link.to)), [selectedChain]);

  const handleComponentHover = useCallback((e, comp) => {
    const svgRect = e.currentTarget.closest("svg").getBoundingClientRect();
    setHoveredId(comp.id);
    setTooltipPos({ x: e.clientX - svgRect.left, y: e.clientY - svgRect.top });
  }, []);

  const hoveredComp = hoveredId ? componentMap[hoveredId] : null;

  function dependencyPath(fromComp, toComp) {
    const x1 = toSvgX(fromComp.maturity), y1 = toSvgY(fromComp.visibility);
    const x2 = toSvgX(toComp.maturity), y2 = toSvgY(toComp.visibility);
    const midY = (y1 + y2) / 2;
    const curveOffset = Math.abs(x1 - x2) < 20 ? 15 : 0;
    return `M ${x1} ${y1} Q ${(x1 + x2) / 2 + curveOffset} ${midY} ${x2} ${y2}`;
  }

  return (
    <div className="w-full max-w-6xl mx-auto p-4">
      <h2 className="text-lg font-semibold text-gray-800 mb-1">{map.title}</h2>
      {map.purpose && <p className="text-sm text-gray-500 mb-3">{map.purpose}</p>}

      <div className="relative border border-gray-200 rounded bg-white">
        <svg viewBox={`0 0 ${WIDTH} ${HEIGHT}`} className="w-full h-auto"
          style={{ fontFamily: "'Segoe UI', system-ui, -apple-system, sans-serif" }}
          onClick={() => setSelectedId(null)}>

          {STAGE_LABELS.map((_, i) => {
            const x0 = toSvgX(i === 0 ? 0 : STAGE_BOUNDARIES[i - 1]);
            const x1 = toSvgX(i < STAGE_BOUNDARIES.length ? STAGE_BOUNDARIES[i] : 1);
            return <rect key={`sb-${i}`} x={x0} y={PADDING.top}
              width={x1 - x0} height={HEIGHT - PADDING.top - PADDING.bottom}
              fill={COLORS.stageFills[i]} />;
          })}

          {STAGE_BOUNDARIES.map((b, i) => (
            <line key={`g-${i}`} x1={toSvgX(b)} y1={PADDING.top}
              x2={toSvgX(b)} y2={HEIGHT - PADDING.bottom}
              stroke={COLORS.gridLine} strokeDasharray="6 4" strokeWidth={1} />
          ))}

          <line x1={PADDING.left} y1={PADDING.top}
            x2={PADDING.left} y2={HEIGHT - PADDING.bottom}
            stroke={COLORS.axisLine} strokeWidth={1.5} />
          <text x={PADDING.left - 10} y={PADDING.top - 8} textAnchor="middle"
            fontSize={11} fill={COLORS.axisLabel} fontWeight={500}>Visible</text>
          <text x={PADDING.left - 10} y={HEIGHT - PADDING.bottom + 18} textAnchor="middle"
            fontSize={11} fill={COLORS.axisLabel} fontWeight={500}>Invisible</text>
          <text transform={`rotate(-90, 22, ${(PADDING.top + HEIGHT - PADDING.bottom) / 2})`}
            x={22} y={(PADDING.top + HEIGHT - PADDING.bottom) / 2}
            textAnchor="middle" fontSize={12} fill={COLORS.axisLabel} fontWeight={600}>
            Value Chain
          </text>

          <line x1={PADDING.left} y1={HEIGHT - PADDING.bottom}
            x2={WIDTH - PADDING.right} y2={HEIGHT - PADDING.bottom}
            stroke={COLORS.axisLine} strokeWidth={1.5} />
          {STAGE_LABELS.map((label, i) => {
            const xs = i === 0 ? 0 : STAGE_BOUNDARIES[i - 1];
            const xe = i < STAGE_BOUNDARIES.length ? STAGE_BOUNDARIES[i] : 1;
            return <text key={`sl-${i}`} x={toSvgX((xs + xe) / 2)}
              y={HEIGHT - PADDING.bottom + 20} textAnchor="middle"
              fontSize={11} fill={COLORS.stageLabel} fontWeight={500}>{label}</text>;
          })}
          <text x={(PADDING.left + WIDTH - PADDING.right) / 2}
            y={HEIGHT - PADDING.bottom + 40} textAnchor="middle"
            fontSize={12} fill={COLORS.axisLabel} fontWeight={600}>Evolution</text>

          <defs>
            <marker id="evo-arrow" viewBox="0 0 10 10" refX={9} refY={5}
              markerWidth={6} markerHeight={6} orient="auto-start-reverse"
              fill={COLORS.evolutionArrow}>
              <path d="M 0 0 L 10 5 L 0 10 z" />
            </marker>
          </defs>

          {map.links.map((link, i) => {
            const from = componentMap[link.from], to = componentMap[link.to];
            if (!from || !to) return null;
            return <path key={`l-${i}`} d={dependencyPath(from, to)} fill="none"
              stroke={COLORS.dependencyLine} strokeWidth={1.3}
              opacity={isLinkVisible(link) ? 0.6 : COLORS.dimmedOpacity}
              style={{ transition: "opacity 0.2s" }} />;
          })}

          {map.evolutions.map((evo, i) => {
            const comp = componentMap[evo.componentId];
            if (!comp) return null;
            const y = toSvgY(comp.visibility);
            return <line key={`e-${i}`} x1={toSvgX(comp.maturity) + 8} y1={y}
              x2={toSvgX(evo.toMaturity) - 4} y2={y}
              stroke={COLORS.evolutionArrow} strokeWidth={2} strokeDasharray="6 3"
              markerEnd="url(#evo-arrow)"
              opacity={isVisible(comp.id) ? 0.9 : COLORS.dimmedOpacity}
              style={{ transition: "opacity 0.2s" }} />;
          })}

          {map.components.filter(c => c.inertia).map(comp => {
            const x = toSvgX(comp.maturity), y = toSvgY(comp.visibility);
            return <g key={`i-${comp.id}`}
              opacity={isVisible(comp.id) ? 1 : COLORS.dimmedOpacity}
              style={{ transition: "opacity 0.2s" }}>
              <rect x={x + 9} y={y - 8} width={4} height={16} fill={COLORS.inertiaBar} rx={1} />
              <rect x={x + 15} y={y - 8} width={4} height={16} fill={COLORS.inertiaBar} rx={1} />
            </g>;
          })}

          {map.components.map(comp => {
            const cx = toSvgX(comp.maturity), cy = toSvgY(comp.visibility);
            const isSelected = selectedId === comp.id;
            const isHovered = hoveredId === comp.id;
            const offset = labelOffsets[comp.id] || { dx: 10, dy: -12 };
            return (
              <g key={comp.id}
                opacity={isVisible(comp.id) ? 1 : COLORS.dimmedOpacity}
                style={{ transition: "opacity 0.2s", cursor: "pointer" }}
                onMouseEnter={(e) => handleComponentHover(e, comp)}
                onMouseLeave={() => setHoveredId(null)}
                onClick={(e) => {
                  e.stopPropagation();
                  setSelectedId(prev => prev === comp.id ? null : comp.id);
                }}>
                <circle cx={cx} cy={cy} r={comp.isAnchor ? 8 : 6}
                  fill={COLORS.componentFill}
                  stroke={isSelected || isHovered ? COLORS.componentStrokeSelected : COLORS.componentStroke}
                  strokeWidth={isSelected || isHovered ? 2.5 : 1.8} />
                {comp.isAnchor && <circle cx={cx} cy={cy} r={3} fill={COLORS.componentStroke} />}
                <text x={cx + offset.dx} y={cy + offset.dy}
                  fontSize={10.5} fontWeight={isSelected || isHovered ? 600 : 500}
                  fill={COLORS.labelText}>{comp.name}</text>
              </g>
            );
          })}

          {(map.annotations || []).map(ann => {
            const ax = toSvgX(ann.x), ay = toSvgY(ann.y);
            return <g key={`a-${ann.id}`}>
              <circle cx={ax} cy={ay} r={10} fill="#3b82f6" opacity={0.15} />
              <text x={ax} y={ay + 4} textAnchor="middle" fontSize={10}
                fontWeight={700} fill="#3b82f6">{ann.id}</text>
            </g>;
          })}
        </svg>

        {hoveredComp && (
          <div className="absolute pointer-events-none z-10 px-3 py-2 rounded shadow-lg text-xs max-w-xs"
            style={{ left: tooltipPos.x + 16, top: tooltipPos.y - 10,
              backgroundColor: COLORS.tooltipBg, color: COLORS.tooltipText }}>
            <div className="font-semibold mb-1">{hoveredComp.name}</div>
            <div className="opacity-80 mb-1">
              Stage: {hoveredComp.stage} &nbsp;|&nbsp; Position: [{hoveredComp.visibility.toFixed(2)}, {hoveredComp.maturity.toFixed(2)}]
            </div>
            <div className="opacity-90 leading-snug">{hoveredComp.rationale}</div>
          </div>
        )}
      </div>

      {/* Figure Legend */}
      <div className="mt-3 border border-gray-200 rounded p-3 bg-gray-50">
        <div className="text-xs font-semibold text-gray-600 mb-2 uppercase tracking-wide">
          Figure Legend
        </div>
        <div className="flex flex-wrap gap-x-6 gap-y-2 text-xs text-gray-600">
          <div className="flex items-center gap-1.5">
            <svg width="16" height="16" viewBox="0 0 16 16">
              <circle cx="8" cy="8" r="5" fill="white" stroke="#333" strokeWidth="1.5"/>
            </svg>
            <span>Component</span>
          </div>
          <div className="flex items-center gap-1.5">
            <svg width="16" height="16" viewBox="0 0 16 16">
              <circle cx="8" cy="8" r="6" fill="white" stroke="#333" strokeWidth="1.5"/>
              <circle cx="8" cy="8" r="2.5" fill="#333"/>
            </svg>
            <span>User / Anchor</span>
          </div>
          <div className="flex items-center gap-1.5">
            <svg width="20" height="16" viewBox="0 0 20 16">
              <line x1="2" y1="8" x2="18" y2="8" stroke="#aaa" strokeWidth="1.5"/>
            </svg>
            <span>Dependency</span>
          </div>
          <div className="flex items-center gap-1.5">
            <svg width="24" height="16" viewBox="0 0 24 16">
              <line x1="2" y1="8" x2="18" y2="8" stroke="#d94040" strokeWidth="2" strokeDasharray="5 3"/>
              <polygon points="18,4 24,8 18,12" fill="#d94040"/>
            </svg>
            <span>Evolution (predicted movement)</span>
          </div>
          <div className="flex items-center gap-1.5">
            <svg width="16" height="16" viewBox="0 0 16 16">
              <rect x="4" y="2" width="3" height="12" fill="#333" rx="1"/>
              <rect x="9" y="2" width="3" height="12" fill="#333" rx="1"/>
            </svg>
            <span>Inertia (resistance to change)</span>
          </div>
        </div>
        <div className="flex gap-0 mt-2 text-xs">
          {STAGE_LABELS.map((label, i) => (
            <div key={i} className="flex-1 text-center py-1 border-r last:border-r-0 border-gray-200"
              style={{ backgroundColor: COLORS.stageFills[i] }}>
              <span className="text-gray-500 font-medium">{label}</span>
            </div>
          ))}
        </div>
      </div>

      {map.annotations && map.annotations.length > 0 && (
        <div className="mt-2 text-xs text-gray-500">
          {map.annotations.map(ann => (
            <div key={ann.id} className="flex gap-2">
              <span className="font-semibold text-blue-500">[{ann.id}]</span>
              <span>{ann.text}</span>
            </div>
          ))}
        </div>
      )}

      <p className="text-xs text-gray-400 mt-2 italic">
        Hover over components for details. Click a component to highlight its dependency chain. Click the background to reset.
      </p>
    </div>
  );
}
```

---

## 2. OWM Text (paste into onlinewardleymaps.com, VS Code, or Obsidian)

```
title National Sovereignty (Government View, April 2023)
style wardley

anchor Supranational [0.98, 0.40]
anchor Society [0.96, 0.52]
anchor Government [0.94, 0.65]
anchor Corporations & Shareholders [0.92, 0.80]

component Legitimacy [0.88, 0.40]
component Perception of Success [0.84, 0.30]
component Public Belonging [0.82, 0.20]
component Election Legitimacy [0.78, 0.45]
component Territorial Sovereignty [0.74, 0.78]
component Economic Sovereignty [0.72, 0.52]
component Security Sovereignty [0.70, 0.62]
component Political Sovereignty [0.68, 0.42]
component Cultural Sovereignty [0.66, 0.28]
component Digital Sovereignty [0.64, 0.17] inertia
component Land [0.60, 0.86]
component CNI [0.58, 0.58]
component Supply Chain [0.56, 0.30] inertia
component Cyber [0.54, 0.22]
component Integrity [0.51, 0.38]
component Competency [0.49, 0.52]
component Fairness [0.47, 0.22]
component Benevolence [0.45, 0.30]
component Identity [0.43, 0.14]
component Territorial Awareness [0.40, 0.75]
component Crisis Response [0.38, 0.50]
component Supply-Chain Awareness [0.36, 0.22]
component Digital-Chain Awareness [0.34, 0.12]
component Capability Layer [0.30, 0.48]
component Laws [0.26, 0.82]
component International Law [0.24, 0.52]
component Mainstream Media [0.20, 0.70]
component Education [0.18, 0.62]
component Social Media [0.16, 0.82]
component Art [0.14, 0.55]
component Propaganda [0.10, 0.35]

Supranational->International Law
Supranational->Legitimacy
Society->Legitimacy
Society->Public Belonging
Society->Perception of Success
Government->Legitimacy
Government->Territorial Sovereignty
Government->Economic Sovereignty
Government->Political Sovereignty
Government->Security Sovereignty
Government->Digital Sovereignty
Government->Cultural Sovereignty
Government->Election Legitimacy
Government->Crisis Response
Corporations & Shareholders->Economic Sovereignty
Corporations & Shareholders->Digital Sovereignty
Corporations & Shareholders->Supply Chain
Legitimacy->Election Legitimacy
Legitimacy->Perception of Success
Legitimacy->Public Belonging
Perception of Success->Capability Layer
Perception of Success->Crisis Response
Public Belonging->Identity
Public Belonging->Cultural Sovereignty
Election Legitimacy->Integrity
Election Legitimacy->Fairness
Election Legitimacy->Competency
Election Legitimacy->Social Media
Election Legitimacy->Mainstream Media
Territorial Sovereignty->Land
Territorial Sovereignty->Territorial Awareness
Economic Sovereignty->Supply Chain
Economic Sovereignty->CNI
Economic Sovereignty->Laws
Security Sovereignty->Land
Security Sovereignty->Cyber
Security Sovereignty->CNI
Security Sovereignty->Crisis Response
Political Sovereignty->Election Legitimacy
Political Sovereignty->International Law
Political Sovereignty->Laws
Digital Sovereignty->Cyber
Digital Sovereignty->CNI
Digital Sovereignty->Digital-Chain Awareness
Cultural Sovereignty->Education
Cultural Sovereignty->Art
Cultural Sovereignty->Mainstream Media
Cultural Sovereignty->Social Media
Cultural Sovereignty->Propaganda
Cultural Sovereignty->Identity
CNI->Capability Layer
Supply Chain->Supply-Chain Awareness
Supply Chain->Capability Layer
Cyber->Digital-Chain Awareness
Cyber->Capability Layer
Integrity->Laws
Competency->Capability Layer
Fairness->Laws
Benevolence->Laws
Identity->Education
Identity->Social Media
Territorial Awareness->Capability Layer
Crisis Response->Capability Layer
Crisis Response->Mainstream Media
Supply-Chain Awareness->Capability Layer
Digital-Chain Awareness->Capability Layer
Capability Layer->Laws
Mainstream Media->Laws
Social Media->Laws
Propaganda->Mainstream Media
Propaganda->Social Media

evolve Digital Sovereignty 0.35
evolve Supply Chain 0.45
evolve Cyber 0.38
evolve Supply-Chain Awareness 0.42
evolve Digital-Chain Awareness 0.32
evolve Election Legitimacy 0.55

annotation 1 [[0.66, 0.22]] Digital sovereignty: genesis/custom; EU-US-China divergence, strong industry inertia
annotation 2 [[0.56, 0.34]] Supply chain re-assessment wave post-COVID & Ukraine; JIT vs JIC re-opening
annotation 3 [[0.78, 0.48]] Contested zone: election legitimacy dragged leftward by 2020-2021 disinformation wave
annotation 4 [[0.60, 0.88]] Industrialised: Westphalian land, borders, military doctrine
annotation 5 [[0.16, 0.84]] Commodity platforms (Meta/X/TikTok) dominate the attention layer
```

---

## 3. Strategic Commentary

### Purpose

Answer the question: **where is national sovereignty industrialised infrastructure and where is it still contested and fragile, as of April 2023?**

The map is drawn from the perspective of a government operating in a mature Western democracy in the first post-Ukraine-invasion spring — after a decade of populist contestation, a pandemic, a European land war, and the rise of hyperscaler-mediated public life.

### Component Evolution Assessment

| Component | Stage | Position [vis, mat] | Rationale |
|---|---|---|---|
| Supranational | Custom-Built | [0.98, 0.40] | UN/WTO/NATO/EU established but authority re-contested (Russia, China, trade wars). |
| Society | Product | [0.96, 0.52] | Permanent beneficiary anchor. |
| Government | Product | [0.94, 0.65] | Mature institutional form; effectiveness varies. |
| Corporations & Shareholders | Commodity | [0.92, 0.80] | Standardised corporate/securities frameworks (IFRS, GAAP, SEC). |
| Legitimacy | Custom-Built | [0.88, 0.40] | Bespoke per regime; under more pressure in 2023 than in any recent decade. |
| Perception of Success | Custom-Built | [0.84, 0.30] | Narrative construction; no standardised measure authoritative. |
| Public Belonging | Custom-Built | [0.82, 0.20] | Fragmenting along political/cultural/digital lines; trending leftward. |
| Election Legitimacy | Custom-Built | [0.78, 0.45] | Procedurally productised but perceptually dragged leftward by post-2020 disinfo wave. |
| Territorial Sovereignty | Commodity | [0.74, 0.78] | Oldest and most codified pillar. |
| Economic Sovereignty | Product | [0.72, 0.52] | Productised via central banks, treasuries, customs. |
| Security Sovereignty | Product | [0.70, 0.62] | Defence procurement, NATO, AUKUS mature. |
| Political Sovereignty | Product | [0.68, 0.42] | Established, but more contested than Economic in 2023. |
| Cultural Sovereignty | Custom-Built | [0.66, 0.28] | Deeply bespoke; pressured by global platforms and diaspora communication. |
| Digital Sovereignty (inertia) | Genesis | [0.64, 0.17] | Emerging concept; EU/China/US/India incompatible visions; hyperscaler lock-in. |
| Land | Commodity | [0.60, 0.86] | Industrialised for centuries; Ukraine reinforces primacy, not stage. |
| CNI | Product | [0.58, 0.58] | NIS/NIS2/PPD-21 regulated; OT/IT convergence uneven. |
| Supply Chain (inertia) | Custom-Built | [0.56, 0.30] | Post-COVID/Ukraine re-opened JIT vs resilience; 30 years of JIT inertia. |
| Cyber | Custom-Built | [0.54, 0.22] | Rapidly evolving attacker-defender; state-grade capability bespoke. |
| Integrity | Custom-Built | [0.51, 0.38] | Anti-corruption institutions exist but perception is culture-dependent. |
| Competency | Product | [0.49, 0.52] | OECD SIGMA, NAO, GAO benchmarks; delivery units productised. |
| Fairness | Custom-Built | [0.47, 0.22] | Norms vary by tradition; no canonical definition. |
| Benevolence | Custom-Built | [0.45, 0.30] | Culturally specific; corroded by populism. |
| Identity | Genesis | [0.43, 0.14] | Fragmenting along digital/diaspora/culture-war lines. |
| Territorial Awareness | Commodity | [0.40, 0.75] | Planet/Maxar/Sentinel utility-priced; standardised APIs. |
| Crisis Response | Product | [0.38, 0.50] | Post-COVID codification; each crisis still rewrites playbook. |
| Supply-Chain Awareness | Custom-Built | [0.36, 0.22] | project44/Interos/Altana real but deployments bespoke. |
| Digital-Chain Awareness | Genesis | [0.34, 0.12] | SBOM, cloud-dependency mapping nascent; SolarWinds/Log4Shell triggered it. |
| Capability Layer | Product | [0.30, 0.48] | Delivery machinery of government; varies by state. |
| Laws | Commodity | [0.26, 0.82] | Domestic statutes/regulations/enforcement fully codified. |
| International Law | Product | [0.24, 0.52] | Treaty systems productised; enforcement contested. |
| Mainstream Media | Commodity | [0.20, 0.70] | Mature commoditised industry; influence waning. |
| Education | Product | [0.18, 0.62] | State systems institutional products; vendor ed-tech markets. |
| Social Media | Commodity | [0.16, 0.82] | Meta/YouTube/TikTok/X at commodity scale; state does not control. |
| Art | Product | [0.14, 0.55] | Global creative industries productised; soft-power component. |
| Propaganda | Custom-Built | [0.10, 0.35] | Craft is old; 2020s forms (bots, deepfakes, algorithmic amplification) still being built. |

### Key Strategic Observations

1. **Two distinct zones, not one map.** The right half of the map (Territorial Sovereignty, Land, Economic Sovereignty, Security Sovereignty, Laws, Territorial Awareness, Mainstream Media, Social Media, Corporations & Shareholders) is *industrialised sovereignty* — Product to Commodity, well-understood, buyable or inherited. The left half (Digital Sovereignty, Cyber, Supply Chain, Identity, Public Belonging, Fairness, Benevolence, Digital-Chain Awareness, Propaganda, Cultural Sovereignty, Election Legitimacy) is *contested sovereignty* — Genesis to Custom-Built, bespoke, fragile, and the actual strategic battleground for a 2023 government.

2. **Sovereignty has a new fifth-column of pillars.** The Westphalian triad (Territorial, Economic, Security) sits comfortably in Product/Commodity. The modern additions — Political (dragged left by populism), Cultural (pressured by platforms), and especially Digital (genesis, with strong inertia from hyperscaler dependence) — are what governments now have to build. This is the *System of Theft* at national-strategy scale: the commoditised pillars are being transcended by new genesis pillars that the old machinery cannot produce.

3. **Legitimacy is being attacked at three different altitudes simultaneously.** Election Legitimacy (procedural, Custom-Built under contestation), Perception of Success (narrative, Custom-Built), and Public Belonging (felt, trending toward Genesis) are all weakening at once. In Wardley terms, three components that together produce the top-level outcome (Legitimacy itself) are all in the high-uncertainty left-hand zones. Governments cannot buy any of them.

4. **The attention layer (Social Media, Mainstream Media) has commoditised faster than the state can regulate it.** Social Media sits at Commodity while its primary upstream dependencies (Election Legitimacy, Cultural Sovereignty, Identity, Public Belonging) are Custom-Built/Genesis. The industrialised commodity is extracting value from non-industrialised state functions. This is a textbook climatic pattern: *commoditisation of one component enables genesis of new contested layers above it*.

5. **The Cyber / Supply Chain / Digital Sovereignty cluster is the most important strategic frontier, and the most fragile.** All three are in the Custom-Built or Genesis zone, all three have their dedicated awareness layer still nascent (Supply-Chain Awareness, Digital-Chain Awareness), and all three carry active inertia (explicit on Digital Sovereignty and Supply Chain, implicit on Cyber via legacy-estate dependencies). April 2023 is the moment these are moving — the evolution arrows on the map all point rightward into the Custom-Built/Product zone over 18-36 months.

6. **Crisis Response is the one place the state has industrialised under pressure.** Three years of COVID, Ukraine, energy, and inflation shocks have forced codification of emergency powers, COBR/NSC structures, and worst-case planning. It sits at Product. This is also the bridge between Government and Capability Layer — the single most-exercised muscle on the map.

7. **Propaganda is re-genesisising.** The conventional craft of strategic communication sits at the boundary of Custom-Built, but 2020s forms (algorithmic amplification, deepfakes, state-sponsored bot networks, influence operations at scale) are genesis again. The map positions it at maturity 0.35 but with implicit leftward drift on emerging sub-forms.

### Doctrine Check

- **Know your users (#1):** Four anchors (Supranational, Society, Government, Corporations & Shareholders) — reasonable for a polity-level map but note that "Society" is not homogeneous. Consider a submap that disaggregates Society by interest (citizens, regions, diasporas) for real strategy work.
- **Focus on user needs (#2):** The map's downstream outcome is Legitimacy. That is the user need — everything feeds back into legitimacy. Doctrine is followed.
- **Use appropriate methods (#9):** Clear mismatch risk. The Genesis/Custom-Built zone (Digital Sovereignty, Identity, Cyber, Digital-Chain Awareness) must be handled with pioneer methods (agile, experimental, small teams). If departments apply ITIL/Six Sigma procurement to Digital Sovereignty, the landscape will industrialise under US or Chinese hyperscaler logic while the government watches. This is the single biggest doctrine violation seen in most Western governments in 2023.
- **Manage inertia (#19):** Two explicit inertia markers — Digital Sovereignty (hyperscaler lock-in, procurement path dependency) and Supply Chain (JIT-era contracts and workforce). Both would need explicit inertia budgets to overcome.
- **Remove bias and duplication (#7):** The map does not yet show duplication but, in practice, Cyber, CNI, and Digital Sovereignty are each owned by different departments (MoD, CNI regulator, DSIT-equivalent) with overlapping capabilities. A real organisational overlay would reveal duplication that the landscape map hides.
- **A bias towards the new (#31):** Strategic investment should flow to the left-hand contested zone. Budgets typically still flow to the right-hand industrialised zone (defence primes, land forces, traditional media). A doctrine-aligned government reallocates.
- **Listen to your ecosystems (#37):** Signals from the EU Data Act, China's Great Firewall extensions, Russia's 2022-23 cyber escalation, and US Chips & Science Act all indicate the Digital/Cyber/Supply Chain cluster is under active evolution. A government not monitoring these is blind.

### PST Alignment

- **Pioneers** should be working on: Digital Sovereignty, Digital-Chain Awareness, Identity, emerging forms of Propaganda counter-measures. Small teams, agile, high failure tolerance.
- **Settlers** should be productising: Supply-Chain Awareness, Cyber (where NIST CSF / Zero Trust / CISA-style frameworks are crystallising), Election Legitimacy reform (from Custom-Built toward Product), Crisis Response refinement.
- **Town Planners** should be running: Land, Laws, Territorial Awareness, Economic Sovereignty instruments, Mainstream Media regulation, CNI compliance programmes. Six Sigma, ITIL, operational excellence.

The common dysfunction: governments give Pioneer work to Town Planner departments (procurement-led digital programmes) and Town Planner work to Pioneer teams (start-up-style land-use pilots). The map makes the misalignment visible.

### Recommended Actions

1. **Stand up an explicit Digital Sovereignty mission with Pioneer methods.** Not another regulatory taskforce — an operational capability that treats hyperscaler substitution, sovereign cloud, and digital-chain awareness as a genesis problem (small team, rapid experimentation, tolerant of failure). The inertia marker on this component is real: expect pushback from incumbent suppliers and procurement paths.
2. **Invest hard in Supply-Chain Awareness and Digital-Chain Awareness now, before they industrialise.** The 12-24-month window to build a differentiated sovereign visibility capability closes as project44-class vendors and SBOM tooling crystallise. Government that buys late buys commodity; government that builds now keeps the learning curve.
3. **Treat Election Legitimacy as the single highest-priority Custom-Built pillar.** Procedural fixes (paper ballots, auditability, post-election risk-limiting audits) push it rightward toward Product. Perception fixes (cross-party consensus on rules, defensive media strategy against disinformation) address the leftward drag. Do both. Do not leave this to the electoral commission alone.
4. **Regulate the attention layer without trying to own it.** Social Media sits at Commodity; the state will not re-genesisise it. Apply Town Planner methods: competition law, transparency mandates (DSA-style), election-period rules. Do not waste Pioneer effort on "build a national social network" projects — the market has settled.
5. **Institutionalise Crisis Response as a permanent capability.** It is the one muscle the state has exercised into Product stage over 2020-2023. Preserve the structures (COBR, NSC), keep the reasonable-worst-case playbooks live, do not let them decay into paper.
6. **Publish a map of sovereign dependencies on the supranational anchor.** Every pillar depends on Supranational institutions (UN, WTO, NATO, EU) which are themselves Custom-Built and re-contested. A government should know exactly which dependencies are fragile (e.g. WTO DSB appellate body, UN Security Council vetoes on Ukraine) and have contingency doctrine.
7. **Address the Propaganda asymmetry.** Hostile-state information operations (Russian IRA-successors, Chinese Ministry of State Security active-measures units) operate with Custom-Built/Genesis creativity; Western responses are Town Planner-speed. Build Pioneer capability for counter-influence operations, with legal-ethical guardrails.

### Build vs. Buy Assessment

| Component | Recommendation | Rationale |
|---|---|---|
| Digital Sovereignty | **Build** (as sovereign capability) | Genesis, strategic differentiation, no off-the-shelf sovereignty. |
| Digital-Chain Awareness | **Build** the data model + integration, **buy** the tooling where it exists | Genesis, but SBOM tooling (Anchore, Snyk, Tidelift) is catching up. Integration is the differentiator. |
| Cyber (offensive + high-end defensive) | **Build** | State-grade capability is Custom-Built by definition. |
| Cyber (routine defensive) | **Buy** | CSPM, EDR, SIEM markets are mature Product. |
| Supply-Chain Awareness | **Buy platform, build integration** | Vendor market is real; multi-tier data integration is where the differentiation lives. |
| Election Legitimacy reform | **Build** (as a programme) | No vendor sells political consensus; this is a state-craft problem. |
| Capability Layer (digital services) | **Mix**: build GDS/USDS-style units; buy cloud infrastructure | Pioneer in-house; Town Planner procurement outside. |
| Territorial Awareness | **Buy** (commercial satellite + state integration layer) | Utility-priced commodity upstream (Planet, Maxar, Sentinel) with sovereign integration. |
| Land, Territorial Sovereignty | **Inherit** | Westphalian infrastructure, neither built nor bought. |
| CNI | **Regulate, don't run** (private operators + public rules) | Mature Product; operators are commercial, regulation is Town Planner work. |
| Laws (domestic) | **Build** (parliament owns) | Commodity infrastructure of the state. |
| International Law | **Participate** (multilateral) | Productised treaty systems; participation, not ownership. |
| Mainstream Media | **Regulate, don't own** | Commodity industry; state ownership attempts fail. |
| Social Media | **Regulate** | Commodity, not state-runnable. |
| Education | **Run + allow diversity** | Product state institution with ed-tech Product add-ons. |
| Propaganda | **Build defensive** (influence-ops resilience); avoid **offensive** except under strict legal basis | Custom-Built; asymmetry risk means defensive capability is non-optional. |
| Crisis Response | **Build** (permanent cadre) | Product, but degrades without continuous exercise. |

### Evolution Predictions (12-24 months from April 2023)

- **Digital Sovereignty 0.17 → 0.35**: Moves from Genesis into Custom-Built as EU (Data Act, DMA/DSA enforcement), US (CHIPS, export controls on advanced semiconductors), and China (data-localisation push) each operationalise their version. Arrow on map.
- **Supply Chain 0.30 → 0.45**: Codifies into "resilient JIT+safety-stock+nearshoring" playbooks, partial industrialisation of friend-shoring. Arrow on map.
- **Cyber 0.22 → 0.38**: Zero-Trust frameworks, CISA-style BOD compliance, NIS2 implementation push it toward Product boundary. Arrow on map.
- **Supply-Chain Awareness 0.22 → 0.42**: Rapid vendor-market consolidation; GS1-led data-sharing standards emerge. Arrow on map.
- **Digital-Chain Awareness 0.12 → 0.32**: SBOM becomes regulatory requirement in US (EO 14028 follow-on) and EU (CRA). Arrow on map.
- **Election Legitimacy 0.45 → 0.55**: Procedural hardening (paper-trail mandates, post-election audits, AI-content disclosure rules) pulls rightward if reform succeeds; could equally drift leftward if 2024 US/UK/EU elections see another legitimacy crisis. The arrow assumes the reform path.
- **Identity**: No meaningful rightward movement expected; the fragmentation continues.
- **Public Belonging**: No meaningful rightward movement expected; probably drifts further left as AI-mediated content dissolves shared reality.

### Open Questions

1. **Which state is this map for?** The analysis assumes a Western liberal democracy. A US, UK, French, German, or Japanese map would be substantially similar. A Chinese map would have Digital Sovereignty in Product (Great Firewall mature), Election Legitimacy is not the same construct, and Public Belonging is more industrialised (top-down identity management). A Russian or Iranian map shifts further still. The pillars are universal; the positions are not.
2. **What is the right level of detail on Social Norms?** The five norms (Integrity, Benevolence, Fairness, Competency, Identity) cluster tightly in the mid-map. In a real strategy exercise, each could be a submap. The map at this scale shows them as a band rather than individuated positions.
3. **Is Corporations & Shareholders really an anchor?** From a pure government-service view, Society is the end user. But corporations/shareholders materially shape economic and digital sovereignty outcomes; treating them as an anchor (not a dependency) captures that political reality. A more classical Wardley Map might move them below Government.
4. **Submap candidates.** The map deliberately crams 35 components into one view. Cleaner presentation would split: (a) Legitimacy submap (Legitimacy, Perception, Belonging, Election Legitimacy, Social Norms), (b) Theatres submap (Land, Supply Chain, Cyber, CNI + Awareness), (c) Media Mix submap (all five media components). Each would replace one component on the main map.
5. **Where is the armed forces' kinetic capability?** It is folded into Land and Security Sovereignty. A defence-strategy map would break this out (Air, Sea, Space, Special Forces, Nuclear) as its own pillar layer.

---

## Validation

The map was validated against `scripts/validate_map.py` from this skill bundle.

```
WARNINGS (1):
  ⚠ Map has 35 components. Maps with >18 components become hard to read. Consider splitting into a main map and submaps.
✓ Map is valid with 1 warning(s).
```

All 35 components have positions in [0,1]; no circular dependencies; all six evolution arrows point rightward; no orphaned components; no label-overlap warnings after the spacing adjustments to the Social Norms cluster and the anchor row. The single warning (component count) reflects the scenario's explicit ask to cover anchors, six pillars, four theatres, three awareness layers, five norms plus election legitimacy, five media channels, capability layer, crisis response, and two legal layers — all in one view. Recommendation: in real strategic use, generate submaps for (a) Legitimacy, (b) Theatres, and (c) Media Mix to replace the dense bands on this map.
