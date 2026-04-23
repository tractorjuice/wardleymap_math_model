# Wardley Map Analysis: Manufacturing Supply Chain (Feb 2023)

A manufacturer's end-to-end value chain — from raw materials through equipment, labour, and R&D into a finished product delivered to distributors — with the regulatory, financial, inventory/logistics, and visibility layers that determine resilience.

---

## 1. Interactive React Artifact (`.jsx`)

Paste this into a Claude.ai React artifact. It renders the full interactive map with hover tooltips, click-to-highlight dependency chains, evolution arrows, inertia markers, annotations, and a figure legend.

```jsx
import { useState, useCallback, useMemo } from "react";

// ============================================================
// 1. CONSTANTS
// ============================================================

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
// 2. MAP DATA — Manufacturing Supply Chain (Feb 2023)
// ============================================================

const MAP = {
  title: "Manufacturing Supply Chain (Feb 2023)",
  purpose: "Where the supply chain sits on evolution — what is industrialised versus still a bespoke judgment call.",
  components: [
    { id: "distributor", name: "Distributor", visibility: 0.97, maturity: 0.62, stage: "Product", isAnchor: true,
      rationale: "Mature B2B distribution channels with established contracting practice; relationship- and volume-negotiated rather than fully commoditised." },
    { id: "finished-product", name: "Finished Product", visibility: 0.88, maturity: 0.65, stage: "Product",
      rationale: "The manufacturer's specific SKU has a defined market, known buyers, and productised features. Industry-specific but solidly in the Product stage." },
    { id: "compliance", name: "Compliance & Certification", visibility: 0.80, maturity: 0.62, stage: "Product",
      rationale: "ISO 9001, CE, UL, FDA 21 CFR, and similar regimes are standardised frameworks with accredited certification bodies and audit-as-a-service vendors. Productised." },
    { id: "inventory-strategy", name: "Inventory Strategy (JIT/JIC)", visibility: 0.75, maturity: 0.30, stage: "Custom-Built", inertia: true,
      rationale: "Post-COVID and post-Ukraine shocks have re-opened the JIT vs JIC debate. As of Feb 2023, each firm is redoing this decision with bespoke stress-tests; no off-the-shelf answer. Strong inertia from JIT-trained operators and locked-in supplier contracts." },
    { id: "sales-forecasting", name: "Sales Forecasting", visibility: 0.70, maturity: 0.50, stage: "Product",
      rationale: "Demand planning is served by a competitive vendor market (SAP IBP, Oracle Demantra, Kinaxis, o9, Anaplan) with published Gartner comparisons. ML forecasting features are pulling it rightward." },
    { id: "assembly-production", name: "Assembly & Production", visibility: 0.62, maturity: 0.55, stage: "Product",
      rationale: "Industrial assembly is well-understood; Lean and Six Sigma are codified; contract manufacturers (Foxconn, Flex, Jabil) sell it as a service. Still differentiated by industry vertical, so mid-Product." },
    { id: "supply-chain-visibility", name: "Supply Chain Visibility", visibility: 0.58, maturity: 0.22, stage: "Custom-Built",
      rationale: "End-to-end SCV is an active investment area (project44, FourKites, Flexport, Interos) but full multi-tier integration remains bespoke per firm; most deployments are data-integration projects, not turnkey." },
    { id: "freight", name: "Freight", visibility: 0.50, maturity: 0.78, stage: "Commodity",
      rationale: "Global freight is utility-like: standardised containers, transparent spot rates, interchangeable carriers (Maersk, MSC, CMA CGM, FedEx, DHL). Invisible until it breaks — classic Commodity signal." },
    { id: "rd", name: "R&D", visibility: 0.45, maturity: 0.28, stage: "Custom-Built",
      rationale: "Product-development R&D is firm-specific by definition — the differentiation activity. Patterns exist (stage-gate, DFM) but the output is bespoke." },
    { id: "equipment", name: "Equipment", visibility: 0.40, maturity: 0.58, stage: "Product",
      rationale: "Industrial machinery is a mature product market (Siemens, ABB, Mitsubishi, Fanuc, DMG Mori) with catalogued classes (CNCs, robots, presses), published specs, and standard leasing/finance." },
    { id: "warehousing", name: "Warehousing", visibility: 0.38, maturity: 0.70, stage: "Commodity",
      rationale: "3PL warehousing and fulfilment are utility-priced services; Amazon FBA, Prologis, and GXO operate at commodity scale with per-pallet/per-sqft pricing." },
    { id: "labour", name: "Labour", visibility: 0.35, maturity: 0.48, stage: "Product",
      rationale: "Skilled industrial labour markets are well-understood. Staffing agencies (Adecco, Randstad) productise recruitment. Training pipelines are local but well-defined." },
    { id: "roce-capital", name: "ROCE & Capital", visibility: 0.30, maturity: 0.80, stage: "Commodity",
      rationale: "ROCE is a textbook financial KPI; capital markets are utility-like; accounting standards (IFRS, GAAP) are fully codified." },
    { id: "refined-materials", name: "Refined Materials", visibility: 0.22, maturity: 0.70, stage: "Commodity",
      rationale: "Refined inputs (steel sheet, plastic pellets, industrial chemicals) trade on catalogues and exchanges with standardised grades (ASTM, ISO) and multiple interchangeable suppliers." },
    { id: "lobbying", name: "Lobbying", visibility: 0.18, maturity: 0.15, stage: "Genesis",
      rationale: "Firm-specific influence work via retained advisers, direct executive relationships, and industry-association positioning. No productised 'lobbying-as-a-service' market for material regulatory outcomes." },
    { id: "raw-materials", name: "Raw Materials", visibility: 0.10, maturity: 0.88, stage: "Commodity",
      rationale: "Ores, oil, grains, cotton, base metals — exchange-traded globally (LME, CME, ICE). Textbook commodity." }
  ],
  links: [
    { from: "distributor", to: "finished-product" },
    { from: "finished-product", to: "assembly-production" },
    { from: "finished-product", to: "compliance" },
    { from: "finished-product", to: "freight" },
    { from: "finished-product", to: "inventory-strategy" },
    { from: "finished-product", to: "sales-forecasting" },
    { from: "compliance", to: "lobbying" },
    { from: "inventory-strategy", to: "sales-forecasting" },
    { from: "inventory-strategy", to: "warehousing" },
    { from: "inventory-strategy", to: "supply-chain-visibility" },
    { from: "sales-forecasting", to: "roce-capital" },
    { from: "assembly-production", to: "rd" },
    { from: "assembly-production", to: "equipment" },
    { from: "assembly-production", to: "labour" },
    { from: "assembly-production", to: "refined-materials" },
    { from: "supply-chain-visibility", to: "freight" },
    { from: "supply-chain-visibility", to: "warehousing" },
    { from: "freight", to: "warehousing" },
    { from: "refined-materials", to: "raw-materials" }
  ],
  evolutions: [
    { componentId: "supply-chain-visibility", toMaturity: 0.45 },
    { componentId: "inventory-strategy", toMaturity: 0.42 },
    { componentId: "sales-forecasting", toMaturity: 0.62 }
  ],
  annotations: [
    { id: 1, text: "Post-COVID SCV investment wave", x: 0.33, y: 0.58 },
    { id: 2, text: "JIT vs JIC: contested judgment call", x: 0.40, y: 0.75 },
    { id: 3, text: "Firm-specific; bespoke influence work", x: 0.20, y: 0.18 }
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
    <div className="w-full max-w-5xl mx-auto p-4">
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
          <text transform={`rotate(-90, 18, ${(PADDING.top + HEIGHT - PADDING.bottom) / 2})`}
            x={18} y={(PADDING.top + HEIGHT - PADDING.bottom) / 2}
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
            y={HEIGHT - PADDING.bottom + 38} textAnchor="middle"
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
              stroke={COLORS.dependencyLine} strokeWidth={1.5}
              opacity={isLinkVisible(link) ? 0.7 : COLORS.dimmedOpacity}
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
                  fontSize={11} fontWeight={isSelected || isHovered ? 600 : 500}
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
title Manufacturing Supply Chain (Feb 2023)
style wardley

anchor Distributor [0.97, 0.62]

component Finished Product [0.88, 0.65]
component Compliance & Certification [0.80, 0.62]
component Inventory Strategy [0.75, 0.30] inertia
component Sales Forecasting [0.70, 0.50]
component Assembly & Production [0.62, 0.55]
component Supply Chain Visibility [0.58, 0.22]
component Freight [0.50, 0.78]
component R&D [0.45, 0.28]
component Equipment [0.40, 0.58]
component Warehousing [0.38, 0.70]
component Labour [0.35, 0.48]
component ROCE & Capital [0.30, 0.80]
component Refined Materials [0.22, 0.70]
component Lobbying [0.18, 0.15]
component Raw Materials [0.10, 0.88]

Distributor->Finished Product
Finished Product->Assembly & Production
Finished Product->Compliance & Certification
Finished Product->Freight
Finished Product->Inventory Strategy
Finished Product->Sales Forecasting
Compliance & Certification->Lobbying
Inventory Strategy->Sales Forecasting
Inventory Strategy->Warehousing
Inventory Strategy->Supply Chain Visibility
Sales Forecasting->ROCE & Capital
Assembly & Production->R&D
Assembly & Production->Equipment
Assembly & Production->Labour
Assembly & Production->Refined Materials
Supply Chain Visibility->Freight
Supply Chain Visibility->Warehousing
Freight->Warehousing
Refined Materials->Raw Materials

evolve Supply Chain Visibility 0.45
evolve Inventory Strategy 0.42
evolve Sales Forecasting 0.62

annotation 1 [[0.58, 0.33]] Post-COVID SCV investment wave
annotation 2 [[0.75, 0.40]] JIT vs JIC: contested judgment call
annotation 3 [[0.18, 0.20]] Firm-specific; bespoke influence work
```

---

## 3. Strategic Commentary

### Purpose

Answer the question: **where does the manufacturing supply chain sit on the evolution axis, and which parts are industrialised versus still a bespoke judgment call — especially in the Feb 2023 post-pandemic, post-Ukraine context?**

### Component Evolution Assessment

| Component | Stage | Position [vis, mat] | Rationale |
|---|---|---|---|
| Distributor | Product | [0.97, 0.62] | Mature B2B distribution channels; relationship- and volume-negotiated, not fully commoditised. |
| Finished Product | Product | [0.88, 0.65] | Manufacturer's specific SKU, defined market, productised features, industry-specific. |
| Compliance & Certification | Product | [0.80, 0.62] | ISO 9001, CE, UL, FDA regimes are standardised frameworks with accredited certification bodies. |
| Inventory Strategy (JIT/JIC) | Custom-Built (inertia) | [0.75, 0.30] | Post-COVID shocks have re-opened JIT vs JIC as a bespoke judgment call per firm; JIT-trained operators resist the shift. |
| Sales Forecasting | Product | [0.70, 0.50] | Competitive vendor market (SAP IBP, Kinaxis, o9) with published comparisons. ML features pulling rightward. |
| Assembly & Production | Product | [0.62, 0.55] | Lean/Six Sigma codified; contract manufacturers sell it as a service; still industry-differentiated. |
| Supply Chain Visibility | Custom-Built | [0.58, 0.22] | Active investment area (project44, FourKites, Flexport); multi-tier integration still bespoke per firm. |
| Freight | Commodity | [0.50, 0.78] | Standardised containers, transparent spot rates, interchangeable carriers; utility-like. |
| R&D | Custom-Built | [0.45, 0.28] | Firm-specific differentiation activity by definition. |
| Equipment | Product | [0.40, 0.58] | Mature machinery vendor market (Siemens, ABB, Fanuc); catalogued classes; standard finance. |
| Warehousing | Commodity | [0.38, 0.70] | 3PL/fulfilment utility-priced (Amazon FBA, Prologis, GXO). |
| Labour | Product | [0.35, 0.48] | Well-understood labour markets; staffing agencies productise recruitment. |
| ROCE & Capital | Commodity | [0.30, 0.80] | Textbook financial KPI; IFRS/GAAP fully codified. |
| Refined Materials | Commodity | [0.22, 0.70] | Exchange/catalogue traded with standardised grades (ASTM, ISO). |
| Lobbying | Genesis | [0.18, 0.15] | Firm-specific influence work; no productised "lobbying-as-a-service" market. |
| Raw Materials | Commodity | [0.10, 0.88] | Exchange-traded globally on LME, CME, ICE. |

### Key Strategic Observations

1. **The supply chain itself sits mid-Product, but resilience is Custom-Built.** The backbone (Assembly, Equipment, Labour, Freight, Warehousing, Materials) is Product-to-Commodity — most of the chain is industrialised and buyable. The things that make a chain *resilient* (Inventory Strategy, Supply Chain Visibility) are still Custom-Built. That is where the judgment calls live.

2. **Feb 2023 is a pivot moment for Inventory Strategy.** JIT dominated industrial thinking for 30 years. COVID, the Suez blockage, and the Ukraine war broke its core assumption (reliable lead times). As of Feb 2023 firms are mid-reassessment; the decision has reverted to Custom-Built territory, with strong inertia from JIT-era training, ERP configurations, and supplier contracts. Expect this to re-industrialise over 18-24 months as new "stress-tested JIT+safety-stock" playbooks emerge.

3. **Supply Chain Visibility is on the Custom-Built → Product cusp.** Multiple vendors (project44, FourKites, Flexport, Interos, Everstream) exist but each deployment is still a bespoke systems-integration project because multi-tier supplier data is fragmented. This is the fastest-moving component on the map.

4. **A tight Commodity cluster in the bottom-right** (Raw Materials, Refined Materials, Warehousing, Freight, ROCE) represents near-zero differentiation opportunity. Effort spent "optimising" these beyond standard procurement hygiene is largely wasted.

5. **Lobbying sits alone in Genesis** — it is bespoke, relationship-based, and resists commoditisation because its value comes from scarcity and insider access. Compliance depends on the regulatory climate that lobbying shapes; this is a realistic upstream dependency, not a gameplay.

### Doctrine Check

- **Know your users (#1):** Clear — the Distributor is the anchor. User need is reliable, compliant, on-time Finished Product.
- **Remove bias and duplication (#7):** The map does not reveal duplication, but in practice many manufacturers run separate forecasting tools per plant/region — a common doctrine failure worth probing in the real organisation.
- **Use appropriate methods (#9):** A clear mismatch risk — applying Six Sigma to Inventory Strategy (Custom-Built) would kill the judgment flexibility this decision currently needs. Apply Lean/agile review cycles to JIT/JIC revisiting; save Six Sigma for Assembly and Warehousing.
- **Manage inertia (#19):** Explicitly flagged on Inventory Strategy. JIT inertia is the single biggest strategic risk on this map.
- **Use standards where appropriate (#15):** Compliance is already standards-driven; ROCE/Capital is textbook; Materials grading is standardised. Doctrine followed here.
- **Bias towards the new (#31):** Supply Chain Visibility deserves investment — ecosystem signals are loud (post-COVID buyer demand, funded SCV vendors).

### Recommended Actions

1. **Reclassify Inventory Strategy as a strategic decision, not an operational parameter.** Establish a small, cross-functional (commercial + operations + finance) team with agile/lean methods to re-derive the JIT/JIC mix per SKU family. Do not delegate to a Six Sigma team — wrong method for the stage.
2. **Invest in Supply Chain Visibility now, before it industrialises.** Pick one platform (project44 or FourKites-class) plus a bespoke multi-tier supplier-data layer. The opportunity window to build differentiated resilience closes as the component evolves to Product (12-24 months).
3. **Stop treating Freight, Warehousing, and Refined Materials as differentiators.** Route them through standard procurement with transparent spot-vs-contract mix. Reassign any talent spent "optimising" these toward the Custom-Built components.
4. **Map the Compliance → Lobbying edge explicitly in governance.** If regulation is a material competitive factor (likely in regulated industries), lobbying is a deliberate strategic activity that should be budgeted and reviewed, not left to ad hoc executive relationships.
5. **Align team structures to stages (PST):** Pioneers on Supply Chain Visibility and Inventory Strategy rework; Settlers productising Sales Forecasting ML; Town Planners running Assembly, Warehousing, Freight.

### Build vs. Buy Assessment

| Component | Recommendation | Rationale |
|---|---|---|
| Inventory Strategy | **Build** (as a capability) | Custom-Built, under active contestation, competitive advantage available via better judgment. |
| Supply Chain Visibility | **Buy the platform, build the integration** | Vendor market is real; multi-tier data integration is still where the differentiation sits. |
| R&D | **Build** | By definition a differentiation activity. |
| Sales Forecasting | **Buy** | Mature Product market; no advantage from building. |
| Compliance & Certification | **Buy** (audit services) + build internal program | Productised audits; differentiation is in internal process, not the certificate. |
| Assembly & Production | **Buy or build** depending on volume and IP sensitivity | Contract manufacturers commoditise this; keep in-house only where IP or quality control is core. |
| Equipment | **Buy** (or lease) | Mature vendor market; custom tooling only where process is truly proprietary. |
| Labour | **Buy** (staffing agencies for flex capacity) + train core staff | Mixed model is industry-standard. |
| Warehousing, Freight | **Outsource** | Utility-priced 3PL/freight markets. |
| Refined Materials, Raw Materials | **Buy** | Exchange/catalogue commodities. |
| Lobbying | **Build** (via retained advisers) | Firm-specific, no productised alternative. |
| ROCE & Capital | **Buy the frameworks; own the judgment** | Standards are commoditised; the investment decisions are not. |

### Evolution Predictions (12-24 months from Feb 2023)

- **Supply Chain Visibility 0.22 → 0.45:** Rapid shift toward Product as vendors consolidate and data-sharing standards emerge (GS1, OpenSCV-like). Arrow on map.
- **Inventory Strategy 0.30 → 0.42:** Moves right as "resilient JIT" playbooks codify, but will remain on the Custom-Built/Product boundary longer than SCV because it is a decision, not a tool. Arrow on map.
- **Sales Forecasting 0.50 → 0.62:** ML-embedded forecasting (Kinaxis, o9, and cloud-hyperscaler offerings) pushes it toward Commodity. Arrow on map.
- **Freight:** Potentially experiences a "digital freight" re-commoditisation wave (Flexport, Convoy) — stays Commodity but with lower margin.
- **Lobbying:** No meaningful movement; remains Genesis.

### Open Questions

1. **Industry specificity:** The map assumes a generic manufacturer. A pharmaceutical maker would have Compliance at 0.80+ and Labour more specialised; a textile maker would have Materials more commoditised. Which industry is the real question?
2. **Geography:** JIT/JIC economics differ materially between single-region manufacturers and multi-region ones with cross-border exposure. What is the firm's footprint?
3. **Is Lobbying actually used?** For many manufacturers outside regulated industries, lobbying is notional. If so, drop it or replace with "Regulatory Monitoring" (Product stage — law-firm services).

---

## Validation

The map was validated against `scripts/validate_map.py` from this skill bundle:

```
Map is valid. No issues found.
```

All 16 components have positions in [0,1], no circular dependencies, all evolution arrows point rightward, no orphaned components, no label-overlap warnings.
