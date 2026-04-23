# Wardley Map Analysis: Energy Disruption Landscape (July 2022)

## Strategic Context (Step 1 — answered from the scenario)

- **Strategic question**: Where in the July-2022 energy landscape is **disruption** most likely in the next 12-24 months — and where is *capital-locked infrastructure* going to resist it? Secondarily: what does the externality-pricing and supply-chain-awareness picture look like, and who pays when the two gaps bite?
- **User anchors**: three in tension — the **Consumer of Today** (expecting cheap, always-on power), the **Consumer of Tomorrow** (demanding sustainability, survivability, and microgeneration agency), and **Society & Government** (carrying the public-good, energy-security, and CO2 mandate). The "today vs tomorrow" split is the scenario's own framing; mapping them as *separate* anchors is what lets the evolution arrows tell a useful story.
- **Core needs**: (a) meet today's demand at today's price, (b) meet tomorrow's demand while decarbonising and surviving supply shocks, (c) price externalities and maintain a social licence for the energy system.
- **Scope boundary**: a mid-to-large OECD energy system in July 2022 — i.e. post-Russia/Ukraine invasion, mid-Nord-Stream crisis, hydrogen-strategy announcements fresh, battery costs down ~85% vs 2010, EU REPowerEU and US IRA in flight but not yet law. Where July-2022 matters I note it explicitly below.

---

## Three Deliverables

### 1. Interactive React artifact

The `.jsx` component below renders the map inline with SVG, hover tooltips showing the evolution rationale for each component, click-to-highlight dependency chains, a professional figure legend with evolution-stage shading, and dashed evolution arrows for the seven components expected to move rightward over the next 12-24 months.

```jsx
import { useState, useCallback, useMemo } from "react";

// ============================================================
// CONSTANTS — mirror of assets/style-constants.json (inlined)
// ============================================================
const WIDTH = 1100;
const HEIGHT = 820;
const PADDING = { top: 55, right: 30, bottom: 95, left: 80 };

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
  title: "#1a1a1a",
  labelText: "#222222",
  dimmedOpacity: 0.15,
};

const STAGE_BOUNDARIES = [0.25, 0.5, 0.75];
const STAGE_LABELS = ["Genesis", "Custom-Built", "Product (+Rental)", "Commodity (+Utility)"];

function toSvgX(m) {
  return PADDING.left + m * (WIDTH - PADDING.left - PADDING.right);
}
function toSvgY(v) {
  return PADDING.top + (1 - v) * (HEIGHT - PADDING.top - PADDING.bottom);
}

// ============================================================
// MAP DATA
// ============================================================
const MAP = {
  title: "Energy Disruption Landscape (July 2022)",
  purpose: "Where is disruption most likely, where is capital locked in, and what does the externality picture look like?",
  components: [
    { id: "consumer-today", name: "Consumer Today", visibility: 0.97, maturity: 0.80, stage: "Commodity", rationale: "The householder or industrial user expecting cheap, always-on electricity. A fully-commoditised expectation in OECD markets — and the July-2022 price spikes are the shock that makes the rest of this map move.", isAnchor: true },
    { id: "consumer-tomorrow", name: "Consumer Tomorrow", visibility: 0.94, maturity: 0.30, stage: "Custom-Built", rationale: "The emerging prosumer: microgeneration, V2G, demand response, sustainability-aware purchasing. Role is well understood in aggregate but the day-to-day behaviour pattern is still bespoke per household.", isAnchor: true },
    { id: "society", name: "Society & Government", visibility: 0.91, maturity: 0.55, stage: "Product", rationale: "The public-good, energy-security, and net-zero mandate holder. Long-established institutional form; post-Ukraine the mandate shifted sharply from climate-primary to security-and-climate.", isAnchor: true },
    { id: "demand", name: "User Demand", visibility: 0.86, maturity: 0.85, stage: "Commodity", rationale: "Aggregated electricity demand. Forecasted as a utility function; well-understood load curves with a known diurnal and seasonal shape." },
    { id: "security", name: "Energy Security", visibility: 0.82, maturity: 0.62, stage: "Product", rationale: "A policy construct. Long-standing framework (IEA reserves, N-1 rules, capacity mechanisms) but post-invasion the definition and weightings are being re-negotiated — product-stage with fresh competitive pressure." },
    { id: "sustainability", name: "Sustainability", visibility: 0.78, maturity: 0.45, stage: "Product", rationale: "Near-universal discourse, multiple competing definitions (ESG, Taxonomy, science-based targets). In Product stage as a concept; implementation varies widely. Moving rightward fast." },
    { id: "survivability", name: "Survivability", visibility: 0.73, maturity: 0.22, stage: "Custom-Built", rationale: "The resilience / ability-to-function-through-shocks framing. Named in NATO, EU, and corporate risk language post-2022 but no agreed methodology for measuring it in energy systems — still bespoke frameworks per jurisdiction." },
    { id: "education", name: "Energy Education", visibility: 0.69, maturity: 0.32, stage: "Custom-Built", rationale: "Public and school-age energy literacy. Disparate, under-funded, jurisdiction-specific; some mature curricula exist (Germany, Denmark) but no Product-stage template." },
    { id: "public-good", name: "Public Good Framing", visibility: 0.64, maturity: 0.24, stage: "Custom-Built", rationale: "Whether electricity is a market good or a social right. Contested in July 2022: Spain's 'Iberian exception', UK's windfall-tax debate, proposals to cap generator revenues. Still pre-product; no stable template." },
    { id: "price", name: "Price", visibility: 0.61, maturity: 0.88, stage: "Commodity", rationale: "Wholesale electricity price in EUR/MWh or equivalent. Utility-traded, transparent, tick-by-tick. Completely commoditised market mechanism — albeit with extreme volatility in mid-2022." },
    { id: "cost-ext", name: "Cost with Externalities", visibility: 0.56, maturity: 0.18, stage: "Custom-Built", rationale: "Price plus carbon, health, and supply-chain externalities. Methodologies exist (SCC, DEFRA carbon values, LCA) but no single agreed figure — each jurisdiction picks its own. Near-Genesis operationally; Custom-Built as a discipline." },
    { id: "spot", name: "Spot Market", visibility: 0.54, maturity: 0.84, stage: "Commodity", rationale: "Day-ahead and intraday exchanges (EPEX, Nord Pool, ERCOT). Utility infrastructure with standardised products, clearing, and settlement." },
    { id: "otc", name: "OTC Market", visibility: 0.50, maturity: 0.76, stage: "Commodity", rationale: "Bilateral forwards, PPAs, hedges. Mature market with ISDA-style contracts; commoditised but less standardised than spot." },
    { id: "distribution", name: "Distribution", visibility: 0.46, maturity: 0.90, stage: "Commodity", rationale: "Low- and medium-voltage networks to the end user. Utility-grade infrastructure; DNOs/DSOs with regulated rate-of-return models. Inertia: 40+ year asset lives, monopoly franchises.", inertia: true },
    { id: "regulation", name: "Regulation", visibility: 0.43, maturity: 0.52, stage: "Product", rationale: "Energy-market regulators (Ofgem, BNetzA, FERC, AEMC). Mature institutional form with multiple operating models. Inertia: primary legislation moves at multi-year cadence and is struggling to keep up with the 2022 shock.", inertia: true },
    { id: "transmission", name: "Transmission", visibility: 0.40, maturity: 0.82, stage: "Commodity", rationale: "High-voltage network and TSOs. Utility infrastructure; synchronous-area governance well-established. Inertia: interconnector projects take 10-15 years, siting law is slow.", inertia: true },
    { id: "co2", name: "CO2 Apparatus", visibility: 0.39, maturity: 0.34, stage: "Custom-Built", rationale: "Emissions trading (EU ETS, UK ETS, California CaT, regional RGGI), carbon border adjustments (CBAM in flight), offset markets. Multiple competing schemes with different coverage and price levels — Custom-Built as a global system, Product within ETS-style jurisdictions." },
    { id: "generation", name: "Generation", visibility: 0.34, maturity: 0.74, stage: "Commodity", rationale: "The generation layer as a whole — the bulk-power supply function. Utility-grade with competitive wholesale markets. The *mix* underneath is where evolution pressure lives." },
    { id: "fossil", name: "Fossil", visibility: 0.32, maturity: 0.92, stage: "Commodity", rationale: "Coal and fuel-oil thermal plant. Peak commodity — standardised, utility-priced, but in structural decline. Included because existing fleet still sets price at the margin in crisis conditions." },
    { id: "renewable", name: "Renewable", visibility: 0.30, maturity: 0.60, stage: "Product", rationale: "Utility-scale wind (onshore + offshore) and solar PV. Multiple vendors, LCOE below fossil in most geographies by 2022, competitive auction markets. Product stage moving towards Commodity as standardisation deepens." },
    { id: "control", name: "Grid Control Systems", visibility: 0.28, maturity: 0.72, stage: "Product", rationale: "SCADA, EMS/DMS, wholesale-market operators' IT. Well-established Product category with 3+ major vendors (GE Grid, Hitachi ABB, Siemens, OSI). Feature competition; not yet fully commoditised." },
    { id: "gas", name: "Gas", visibility: 0.26, maturity: 0.86, stage: "Commodity", rationale: "Natural-gas CCGT and OCGT. Commodity by all measures, but July 2022 exposes an extreme supplier-concentration risk and price volatility that utility markets are supposed not to have. Inertia: 20-30 year plant and pipeline assets.", inertia: true },
    { id: "solar-micro", name: "Solar Microgen", visibility: 0.24, maturity: 0.54, stage: "Product", rationale: "Rooftop and residential PV with optional battery. Mature Product category with standardised panels, inverters, and installer ecosystems. Consumer-financeable on 5-10 year payback in most OECD markets by mid-2022." },
    { id: "nuclear", name: "Nuclear", visibility: 0.22, maturity: 0.68, stage: "Product", rationale: "Large-reactor GW-scale fission. Well-defined Product category but with fewer viable vendors; EPR/AP1000 cost overruns well-documented. SMR wave sits as a pipeline of Custom-Built designs that have not yet delivered. Inertia: multi-decade build times, public-acceptance cycles.", inertia: true },
    { id: "electrical-storage", name: "Electrical Storage", visibility: 0.18, maturity: 0.48, stage: "Product", rationale: "Lithium-ion grid batteries. Crossing the Custom-Built→Product boundary in mid-2022: Tesla, Fluence, Wärtsilä, CATL, Sungrow all supplying utility-scale; LCOE falling; multi-hour durations shipping. Warranties and financing still fragmented." },
    { id: "potential", name: "Potential Energy Storage", visibility: 0.14, maturity: 0.85, stage: "Commodity", rationale: "Pumped hydro. Century-old utility-grade asset class with standardised engineering and financial treatment. Not expanding fast because new sites are rare, but the existing fleet is commoditised." },
    { id: "hydrogen", name: "Hydrogen Storage", visibility: 0.10, maturity: 0.22, stage: "Custom-Built", rationale: "Electrolytic hydrogen stored in salt caverns or tanks for re-electrification or industrial use. Demonstrator and early-commercial projects only in July 2022; hydrogen strategies published but infrastructure largely bespoke." },
    { id: "reserves", name: "Strategic Reserves", visibility: 0.06, maturity: 0.60, stage: "Product", rationale: "IEA-mandated 90-day oil stocks, gas-storage targets (EU 80% by Nov 2022), coal reserves. Product-stage institutional mechanism; July 2022 stress-testing the stored-gas rule in particular." },
    { id: "supply-chain", name: "Supply-Chain Awareness", visibility: 0.04, maturity: 0.14, stage: "Genesis", rationale: "End-to-end material and component traceability — lithium, nickel, silicon-wafer, rare earths, transformer steel. Near-Genesis: ad-hoc reporting, proliferating frameworks (CSRD, UFLPA, EU Battery Passport) but no operating standard. The bottom-left vulnerability of the entire map." },
    { id: "capital", name: "Capital Intensity", visibility: 0.02, maturity: 0.42, stage: "Product", rationale: "The sheer cost of energy-system build-out — regulated-asset-base returns, project finance, green bonds. A well-understood Product-stage discipline; cost of capital spiked in mid-2022 with rate rises, reshaping what is bankable." },
  ],
  links: [
    { from: "consumer-today", to: "demand" },
    { from: "consumer-today", to: "price" },
    { from: "consumer-tomorrow", to: "sustainability" },
    { from: "consumer-tomorrow", to: "survivability" },
    { from: "consumer-tomorrow", to: "education" },
    { from: "consumer-tomorrow", to: "solar-micro" },
    { from: "society", to: "public-good" },
    { from: "society", to: "security" },
    { from: "society", to: "sustainability" },
    { from: "society", to: "regulation" },
    { from: "demand", to: "distribution" },
    { from: "demand", to: "price" },
    { from: "security", to: "reserves" },
    { from: "security", to: "generation" },
    { from: "security", to: "gas" },
    { from: "sustainability", to: "renewable" },
    { from: "sustainability", to: "co2" },
    { from: "sustainability", to: "cost-ext" },
    { from: "survivability", to: "supply-chain" },
    { from: "survivability", to: "hydrogen" },
    { from: "education", to: "public-good" },
    { from: "public-good", to: "cost-ext" },
    { from: "public-good", to: "regulation" },
    { from: "price", to: "spot" },
    { from: "price", to: "otc" },
    { from: "cost-ext", to: "co2" },
    { from: "cost-ext", to: "supply-chain" },
    { from: "spot", to: "generation" },
    { from: "otc", to: "generation" },
    { from: "distribution", to: "transmission" },
    { from: "distribution", to: "control" },
    { from: "distribution", to: "capital" },
    { from: "transmission", to: "generation" },
    { from: "transmission", to: "control" },
    { from: "transmission", to: "capital" },
    { from: "generation", to: "fossil" },
    { from: "generation", to: "gas" },
    { from: "generation", to: "renewable" },
    { from: "generation", to: "nuclear" },
    { from: "generation", to: "solar-micro" },
    { from: "generation", to: "electrical-storage" },
    { from: "generation", to: "potential" },
    { from: "generation", to: "hydrogen" },
    { from: "renewable", to: "electrical-storage" },
    { from: "renewable", to: "capital" },
    { from: "nuclear", to: "capital" },
    { from: "solar-micro", to: "electrical-storage" },
    { from: "fossil", to: "reserves" },
    { from: "gas", to: "reserves" },
    { from: "hydrogen", to: "capital" },
    { from: "potential", to: "capital" },
    { from: "regulation", to: "co2" },
    { from: "regulation", to: "supply-chain" },
    { from: "control", to: "capital" },
    { from: "control", to: "electrical-storage" },
  ],
  evolutions: [
    { componentId: "renewable", toMaturity: 0.78 },
    { componentId: "solar-micro", toMaturity: 0.72 },
    { componentId: "electrical-storage", toMaturity: 0.66 },
    { componentId: "hydrogen", toMaturity: 0.42 },
    { componentId: "co2", toMaturity: 0.58 },
    { componentId: "cost-ext", toMaturity: 0.46 },
    { componentId: "supply-chain", toMaturity: 0.38 },
  ],
  annotations: [
    { id: 1, text: "Disruption frontier: tomorrow's survivability built on immature storage and externality pricing", x: 0.20, y: 0.12 },
    { id: 2, text: "Locked-in capital: fossil, gas, transmission, distribution — the inertia spine of the system", x: 0.88, y: 0.38 },
    { id: 3, text: "Storage is the pivot: electrical crossing into Product; hydrogen still bespoke", x: 0.50, y: 0.20 },
    { id: 4, text: "Externality apparatus is the weakest rail — if the map has a single point of failure, it is here", x: 0.30, y: 0.10 },
  ],
};

function findChain(id, links) {
  const s = new Set([id]);
  let changed = true;
  while (changed) {
    changed = false;
    for (const l of links) {
      if (s.has(l.from) && !s.has(l.to)) { s.add(l.to); changed = true; }
      if (s.has(l.to) && !s.has(l.from)) { s.add(l.from); changed = true; }
    }
  }
  return s;
}

function computeLabelOffsets(components) {
  const offsets = {};
  const positions = components.map(c => ({ id: c.id, sx: toSvgX(c.maturity), sy: toSvgY(c.visibility) }));
  for (const c of components) {
    let dx = 10, dy = -12;
    const sx = toSvgX(c.maturity), sy = toSvgY(c.visibility);
    for (const o of positions) {
      if (o.id === c.id) continue;
      if (Math.abs(sx - o.sx) < 80 && Math.abs(sy - o.sy) < 22) {
        dy = sy <= o.sy ? -14 : 18;
      }
    }
    if (sx + dx + c.name.length * 6.2 > WIDTH - PADDING.right) dx = -(c.name.length * 6.2 + 12);
    if (sy + dy < PADDING.top + 10) dy = 16;
    offsets[c.id] = { dx, dy };
  }
  return offsets;
}

export default function WardleyMap() {
  const [hoveredId, setHoveredId] = useState(null);
  const [selectedId, setSelectedId] = useState(null);
  const [tooltipPos, setTooltipPos] = useState({ x: 0, y: 0 });

  const map = MAP;
  const labelOffsets = useMemo(() => computeLabelOffsets(map.components), [map.components]);
  const selectedChain = useMemo(() => selectedId ? findChain(selectedId, map.links) : null, [selectedId, map.links]);
  const componentMap = useMemo(() => Object.fromEntries(map.components.map(c => [c.id, c])), [map.components]);

  const isVisible = useCallback(id => !selectedChain || selectedChain.has(id), [selectedChain]);
  const isLinkVisible = useCallback(l => !selectedChain || (selectedChain.has(l.from) && selectedChain.has(l.to)), [selectedChain]);

  const onHover = useCallback((e, c) => {
    const r = e.currentTarget.closest("svg").getBoundingClientRect();
    setHoveredId(c.id);
    setTooltipPos({ x: e.clientX - r.left, y: e.clientY - r.top });
  }, []);

  const hoveredComp = hoveredId ? componentMap[hoveredId] : null;

  function depPath(a, b) {
    const x1 = toSvgX(a.maturity), y1 = toSvgY(a.visibility);
    const x2 = toSvgX(b.maturity), y2 = toSvgY(b.visibility);
    const midY = (y1 + y2) / 2;
    const off = Math.abs(x1 - x2) < 20 ? 15 : 0;
    return `M ${x1} ${y1} Q ${(x1 + x2) / 2 + off} ${midY} ${x2} ${y2}`;
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
            return <rect key={`sb-${i}`} x={x0} y={PADDING.top} width={x1 - x0}
              height={HEIGHT - PADDING.top - PADDING.bottom} fill={COLORS.stageFills[i]} />;
          })}
          {STAGE_BOUNDARIES.map((b, i) => (
            <line key={`g-${i}`} x1={toSvgX(b)} y1={PADDING.top} x2={toSvgX(b)} y2={HEIGHT - PADDING.bottom}
              stroke={COLORS.gridLine} strokeDasharray="6 4" strokeWidth={1} />
          ))}

          <line x1={PADDING.left} y1={PADDING.top} x2={PADDING.left} y2={HEIGHT - PADDING.bottom}
            stroke={COLORS.axisLine} strokeWidth={1.5} />
          <text x={PADDING.left - 10} y={PADDING.top - 8} textAnchor="middle" fontSize={11}
            fill={COLORS.axisLabel} fontWeight={500}>Visible</text>
          <text x={PADDING.left - 10} y={HEIGHT - PADDING.bottom + 18} textAnchor="middle" fontSize={11}
            fill={COLORS.axisLabel} fontWeight={500}>Invisible</text>
          <text transform={`rotate(-90, 22, ${(PADDING.top + HEIGHT - PADDING.bottom) / 2})`}
            x={22} y={(PADDING.top + HEIGHT - PADDING.bottom) / 2}
            textAnchor="middle" fontSize={12} fill={COLORS.axisLabel} fontWeight={600}>
            Value Chain
          </text>

          <line x1={PADDING.left} y1={HEIGHT - PADDING.bottom} x2={WIDTH - PADDING.right}
            y2={HEIGHT - PADDING.bottom} stroke={COLORS.axisLine} strokeWidth={1.5} />
          {STAGE_LABELS.map((label, i) => {
            const x0 = i === 0 ? 0 : STAGE_BOUNDARIES[i - 1];
            const x1 = i < STAGE_BOUNDARIES.length ? STAGE_BOUNDARIES[i] : 1;
            return <text key={`sl-${i}`} x={toSvgX((x0 + x1) / 2)} y={HEIGHT - PADDING.bottom + 20}
              textAnchor="middle" fontSize={11} fill={COLORS.stageLabel} fontWeight={500}>{label}</text>;
          })}
          <text x={(PADDING.left + WIDTH - PADDING.right) / 2} y={HEIGHT - PADDING.bottom + 38}
            textAnchor="middle" fontSize={12} fill={COLORS.axisLabel} fontWeight={600}>Evolution</text>

          <defs>
            <marker id="evo-arrow" viewBox="0 0 10 10" refX={9} refY={5} markerWidth={6}
              markerHeight={6} orient="auto-start-reverse" fill={COLORS.evolutionArrow}>
              <path d="M 0 0 L 10 5 L 0 10 z" />
            </marker>
          </defs>

          {map.links.map((l, i) => {
            const a = componentMap[l.from], b = componentMap[l.to];
            if (!a || !b) return null;
            return <path key={`l-${i}`} d={depPath(a, b)} fill="none" stroke={COLORS.dependencyLine}
              strokeWidth={1.5} opacity={isLinkVisible(l) ? 0.7 : COLORS.dimmedOpacity}
              style={{ transition: "opacity 0.2s" }} />;
          })}

          {map.evolutions.map((e, i) => {
            const c = componentMap[e.componentId];
            if (!c) return null;
            const x1 = toSvgX(c.maturity), x2 = toSvgX(e.toMaturity), y = toSvgY(c.visibility);
            return <line key={`e-${i}`} x1={x1 + 8} y1={y} x2={x2 - 4} y2={y}
              stroke={COLORS.evolutionArrow} strokeWidth={2} strokeDasharray="6 3"
              markerEnd="url(#evo-arrow)" opacity={isVisible(c.id) ? 0.9 : COLORS.dimmedOpacity}
              style={{ transition: "opacity 0.2s" }} />;
          })}

          {map.components.filter(c => c.inertia).map(c => {
            const x = toSvgX(c.maturity), y = toSvgY(c.visibility);
            return <g key={`in-${c.id}`} opacity={isVisible(c.id) ? 1 : COLORS.dimmedOpacity}
              style={{ transition: "opacity 0.2s" }}>
              <rect x={x + 9} y={y - 8} width={4} height={16} fill={COLORS.inertiaBar} rx={1} />
              <rect x={x + 15} y={y - 8} width={4} height={16} fill={COLORS.inertiaBar} rx={1} />
            </g>;
          })}

          {map.components.map(c => {
            const cx = toSvgX(c.maturity), cy = toSvgY(c.visibility);
            const sel = selectedId === c.id, hov = hoveredId === c.id;
            const off = labelOffsets[c.id] || { dx: 10, dy: -12 };
            return <g key={c.id} opacity={isVisible(c.id) ? 1 : COLORS.dimmedOpacity}
              style={{ transition: "opacity 0.2s", cursor: "pointer" }}
              onMouseEnter={e => onHover(e, c)} onMouseLeave={() => setHoveredId(null)}
              onClick={e => { e.stopPropagation(); setSelectedId(p => p === c.id ? null : c.id); }}>
              <circle cx={cx} cy={cy} r={c.isAnchor ? 8 : 6} fill={COLORS.componentFill}
                stroke={sel || hov ? COLORS.componentStrokeSelected : COLORS.componentStroke}
                strokeWidth={sel ? 2.5 : hov ? 2.5 : 1.8} />
              {c.isAnchor && <circle cx={cx} cy={cy} r={3} fill={COLORS.componentStroke} />}
              <text x={cx + off.dx} y={cy + off.dy} fontSize={11}
                fontWeight={sel || hov ? 600 : 500} fill={COLORS.labelText}>{c.name}</text>
            </g>;
          })}

          {(map.annotations || []).map(a => {
            const ax = toSvgX(a.x), ay = toSvgY(a.y);
            return <g key={`a-${a.id}`}>
              <circle cx={ax} cy={ay} r={10} fill="#3b82f6" opacity={0.15} />
              <text x={ax} y={ay + 4} textAnchor="middle" fontSize={10} fontWeight={700}
                fill="#3b82f6">{a.id}</text>
            </g>;
          })}
        </svg>

        {hoveredComp && (
          <div className="absolute pointer-events-none z-10 px-3 py-2 rounded shadow-lg text-xs max-w-xs"
            style={{ left: tooltipPos.x + 16, top: tooltipPos.y - 10,
              backgroundColor: COLORS.tooltipBg, color: COLORS.tooltipText }}>
            <div className="font-semibold mb-1">{hoveredComp.name}</div>
            <div className="opacity-80 mb-1">
              Stage: {hoveredComp.stage} &nbsp;|&nbsp; [{hoveredComp.visibility.toFixed(2)}, {hoveredComp.maturity.toFixed(2)}]
            </div>
            <div className="opacity-90 leading-snug">{hoveredComp.rationale}</div>
          </div>
        )}
      </div>

      <div className="mt-3 border border-gray-200 rounded p-3 bg-gray-50">
        <div className="text-xs font-semibold text-gray-600 mb-2 uppercase tracking-wide">Figure Legend</div>
        <div className="flex flex-wrap gap-x-6 gap-y-2 text-xs text-gray-600">
          <div className="flex items-center gap-1.5">
            <svg width="16" height="16" viewBox="0 0 16 16"><circle cx="8" cy="8" r="5" fill="white" stroke="#333" strokeWidth="1.5"/></svg>
            <span>Component</span></div>
          <div className="flex items-center gap-1.5">
            <svg width="16" height="16" viewBox="0 0 16 16"><circle cx="8" cy="8" r="6" fill="white" stroke="#333" strokeWidth="1.5"/><circle cx="8" cy="8" r="2.5" fill="#333"/></svg>
            <span>User / Anchor</span></div>
          <div className="flex items-center gap-1.5">
            <svg width="20" height="16" viewBox="0 0 20 16"><line x1="2" y1="8" x2="18" y2="8" stroke="#aaa" strokeWidth="1.5"/></svg>
            <span>Dependency</span></div>
          <div className="flex items-center gap-1.5">
            <svg width="24" height="16" viewBox="0 0 24 16"><line x1="2" y1="8" x2="18" y2="8" stroke="#d94040" strokeWidth="2" strokeDasharray="5 3"/><polygon points="18,4 24,8 18,12" fill="#d94040"/></svg>
            <span>Evolution (predicted movement)</span></div>
          <div className="flex items-center gap-1.5">
            <svg width="16" height="16" viewBox="0 0 16 16"><rect x="4" y="2" width="3" height="12" fill="#333" rx="1"/><rect x="9" y="2" width="3" height="12" fill="#333" rx="1"/></svg>
            <span>Inertia (resistance)</span></div>
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
          {map.annotations.map(a => (
            <div key={a.id} className="flex gap-2">
              <span className="font-semibold text-blue-500">[{a.id}]</span>
              <span>{a.text}</span>
            </div>
          ))}
        </div>
      )}

      <p className="text-xs text-gray-400 mt-2 italic">
        Hover for details. Click a component to highlight its dependency chain. Click the background to reset.
      </p>
    </div>
  );
}
```

### 2. OWM text block

```owm
title Energy Disruption Landscape (July 2022)
style wardley

anchor Consumer Today [0.97, 0.80]
anchor Consumer Tomorrow [0.94, 0.30]
anchor Society & Government [0.91, 0.55]

component User Demand [0.86, 0.85]
component Energy Security [0.82, 0.62]
component Sustainability [0.78, 0.45]
component Survivability [0.73, 0.22]
component Energy Education [0.69, 0.32]
component Public Good Framing [0.64, 0.24]
component Price [0.61, 0.88]
component Cost with Externalities [0.56, 0.18]
component Spot Market [0.54, 0.84]
component OTC Market [0.50, 0.76]
component Distribution [0.46, 0.90] inertia
component Regulation [0.43, 0.52] inertia
component Transmission [0.40, 0.82] inertia
component CO2 Apparatus [0.39, 0.34]
component Generation [0.34, 0.74]
component Fossil [0.32, 0.92]
component Renewable [0.30, 0.60]
component Grid Control Systems [0.28, 0.72]
component Gas [0.26, 0.86] inertia
component Solar Microgen [0.24, 0.54]
component Nuclear [0.22, 0.68] inertia
component Electrical Storage [0.18, 0.48]
component Potential Energy Storage [0.14, 0.85]
component Hydrogen Storage [0.10, 0.22]
component Strategic Reserves [0.06, 0.60]
component Supply-Chain Awareness [0.04, 0.14]
component Capital Intensity [0.02, 0.42]

Consumer Today->User Demand
Consumer Today->Price
Consumer Tomorrow->Sustainability
Consumer Tomorrow->Survivability
Consumer Tomorrow->Energy Education
Consumer Tomorrow->Solar Microgen
Society & Government->Public Good Framing
Society & Government->Energy Security
Society & Government->Sustainability
Society & Government->Regulation
User Demand->Distribution
User Demand->Price
Energy Security->Strategic Reserves
Energy Security->Generation
Energy Security->Gas
Sustainability->Renewable
Sustainability->CO2 Apparatus
Sustainability->Cost with Externalities
Survivability->Supply-Chain Awareness
Survivability->Hydrogen Storage
Energy Education->Public Good Framing
Public Good Framing->Cost with Externalities
Public Good Framing->Regulation
Price->Spot Market
Price->OTC Market
Cost with Externalities->CO2 Apparatus
Cost with Externalities->Supply-Chain Awareness
Spot Market->Generation
OTC Market->Generation
Distribution->Transmission
Distribution->Grid Control Systems
Distribution->Capital Intensity
Transmission->Generation
Transmission->Grid Control Systems
Transmission->Capital Intensity
Generation->Fossil
Generation->Gas
Generation->Renewable
Generation->Nuclear
Generation->Solar Microgen
Generation->Electrical Storage
Generation->Potential Energy Storage
Generation->Hydrogen Storage
Renewable->Electrical Storage
Renewable->Capital Intensity
Nuclear->Capital Intensity
Solar Microgen->Electrical Storage
Fossil->Strategic Reserves
Gas->Strategic Reserves
Hydrogen Storage->Capital Intensity
Potential Energy Storage->Capital Intensity
Regulation->CO2 Apparatus
Regulation->Supply-Chain Awareness
Grid Control Systems->Capital Intensity
Grid Control Systems->Electrical Storage

evolve Renewable 0.78
evolve Solar Microgen 0.72
evolve Electrical Storage 0.66
evolve Hydrogen Storage 0.42
evolve CO2 Apparatus 0.58
evolve Cost with Externalities 0.46
evolve Supply-Chain Awareness 0.38

annotation 1 [[0.12, 0.20]] Disruption frontier: tomorrow's survivability built on immature storage and externality pricing
annotation 2 [[0.38, 0.88]] Locked-in capital: fossil, gas, transmission, distribution
annotation 3 [[0.20, 0.50]] Storage is the pivot: electrical crossing into Product; hydrogen still bespoke
annotation 4 [[0.10, 0.30]] Externality apparatus is the weakest rail in the system
```

### 3. Strategic commentary

## Purpose

Understand, in July 2022, **where disruption is most likely** across the energy system, **where capital-locked infrastructure will resist** it, and what the **externality-pricing and supply-chain-awareness** gaps imply for the cost of transition.

## Component Evolution Assessment

| Component | Stage | [vis, mat] | Rationale |
|---|---|---|---|
| Consumer Today | Commodity | [0.97, 0.80] | Anchor. Householder/industrial user expecting cheap, always-on electricity. |
| Consumer Tomorrow | Custom-Built | [0.94, 0.30] | Anchor. Emerging prosumer: microgen, V2G, demand response — bespoke per household. |
| Society & Government | Product | [0.91, 0.55] | Anchor. Public-good, security, net-zero mandate holder. Mandate re-negotiated post-Ukraine. |
| User Demand | Commodity | [0.86, 0.85] | Aggregate load — forecasted as a utility function with known diurnal/seasonal shape. |
| Energy Security | Product | [0.82, 0.62] | IEA reserves, N-1 rules, capacity mechanisms; definition in flux post-invasion. |
| Sustainability | Product | [0.78, 0.45] | Universal discourse, multiple competing definitions (ESG, Taxonomy, SBTs). |
| Survivability | Custom-Built | [0.73, 0.22] | Resilience framing; named in policy post-2022 but no agreed measurement. |
| Energy Education | Custom-Built | [0.69, 0.32] | Jurisdiction-specific, under-funded, no Product-stage template. |
| Public Good Framing | Custom-Built | [0.64, 0.24] | Contested: Iberian exception, windfall-tax debate, revenue caps — no stable template. |
| Price | Commodity | [0.61, 0.88] | Wholesale €/MWh — utility-traded, transparent, tick-by-tick. |
| Cost with Externalities | Custom-Built | [0.56, 0.18] | SCC, DEFRA values, LCA — no single agreed figure. Near-Genesis operationally. |
| Spot Market | Commodity | [0.54, 0.84] | EPEX, Nord Pool, ERCOT — utility infrastructure. |
| OTC Market | Commodity | [0.50, 0.76] | Bilateral forwards, PPAs, hedges on ISDA-style contracts. |
| Distribution | Commodity (inertia) | [0.46, 0.90] | DNOs/DSOs, regulated rate-of-return, 40+ year assets. |
| Regulation | Product (inertia) | [0.43, 0.52] | Ofgem, BNetzA, FERC, AEMC — primary legislation slow vs shock. |
| Transmission | Commodity (inertia) | [0.40, 0.82] | TSOs; interconnector builds take 10-15 years. |
| CO2 Apparatus | Custom-Built | [0.39, 0.34] | EU ETS, CBAM, offsets — multiple competing schemes, no global standard. |
| Generation | Commodity | [0.34, 0.74] | Bulk-power supply; competitive wholesale. Mix underneath is where pressure lives. |
| Fossil | Commodity | [0.32, 0.92] | Coal/oil thermal in structural decline but still price-setting at the margin. |
| Renewable | Product | [0.30, 0.60] | Wind, utility solar PV; LCOE below fossil in most geographies by 2022. |
| Grid Control Systems | Product | [0.28, 0.72] | SCADA, EMS/DMS — GE, Hitachi ABB, Siemens, OSI. |
| Gas | Commodity (inertia) | [0.26, 0.86] | CCGT/OCGT commodity; mid-2022 exposes concentration risk. 20-30 year assets. |
| Solar Microgen | Product | [0.24, 0.54] | Rooftop PV + battery; consumer-financeable on 5-10 year payback. |
| Nuclear | Product (inertia) | [0.22, 0.68] | Large-reactor fission; SMR wave not yet delivered. Multi-decade cycles. |
| Electrical Storage | Product | [0.18, 0.48] | Li-ion grid batteries crossing Custom-Built→Product in mid-2022. |
| Potential Energy Storage | Commodity | [0.14, 0.85] | Pumped hydro — century-old utility asset class, limited new sites. |
| Hydrogen Storage | Custom-Built | [0.10, 0.22] | Demonstrator and early-commercial; strategies published, infra bespoke. |
| Strategic Reserves | Product | [0.06, 0.60] | IEA oil stocks, EU gas-storage targets being stress-tested mid-2022. |
| Supply-Chain Awareness | Genesis | [0.04, 0.14] | End-to-end lithium/nickel/silicon traceability — ad-hoc, no operating standard. |
| Capital Intensity | Product | [0.02, 0.42] | RAB returns, project finance, green bonds. Cost of capital spiked mid-2022. |

## Key Strategic Observations

1. **The map has a lopsided shape — and it tells you where to look.** The *supply* half (generation, transmission, distribution, fossil, gas, grid control) clusters firmly in the Commodity/Product right-hand side: a textbook mature utility system. The *new demand*, *externality*, and *future-storage* half (Consumer Tomorrow, Survivability, Cost with Externalities, Hydrogen, Supply-Chain Awareness) is pushed hard into the Genesis/Custom-Built left. The gap between those two halves is where the disruption happens — and where the July-2022 price shock exposes unpriced risk.

2. **Capital intensity is the inertia spine.** Distribution, Transmission, Gas, Nuclear all carry inertia markers for the same reason: they are capital-locked on multi-decade timescales. Capital Intensity itself sits bottom-left as a near-invisible Product-stage dependency — a rising cost of capital in mid-2022 (rate hikes) changes *the shape of what is bankable*, not merely its cost. That is the quietest but most powerful shock on the map.

3. **Storage is the pivot, and it is evolving at two different speeds.** Electrical storage (li-ion) is crossing the Custom-Built→Product boundary *right now* in mid-2022. Hydrogen storage is still firmly Custom-Built and will be for 3-5 years; pumped hydro is a Commodity but site-constrained. If your strategy assumes hydrogen is the grid-storage answer by 2025, the map disagrees.

4. **The externality rail is the weakest link in the whole system.** Cost with Externalities, CO2 Apparatus, and Supply-Chain Awareness are all low-visibility *and* low-maturity — three of the four lowest-maturity components are exactly the rails that are supposed to price the transition. If the map has a single point of failure, it is here: you cannot steer a market whose externalities are not priced, and in July 2022 they essentially are not.

5. **"Consumer Tomorrow" is an aggregation of Custom-Built components and therefore fragile.** Every component Consumer Tomorrow depends on (Sustainability, Survivability, Education, Solar Microgen) is Product or earlier, and two of them — Survivability and Education — are barely out of Genesis. This makes Consumer Tomorrow a fragile anchor: a political or economic shock can easily push a marginal household back to Consumer Today behaviour. A corollary: the right strategic investment for "tomorrow" behaviour is less about the generation layer and more about the *literacy and survivability* rails that decide whether the behaviour sticks.

6. **Public-good framing is where the climatic pattern "capital flows where it's valued" will bite.** Public Good Framing is Custom-Built and contested. In a crisis (July 2022 is one), governments reach for it as a tool — price caps, windfall taxes, revenue clawbacks. But because it is pre-Product, the *templates* are ad-hoc and tend to be retrospective and distorting. Expect more of this in 2023.

## Doctrine Check

- **Know your users**: Three anchors identified, explicitly in tension. Pass — though most incumbents optimise for Consumer Today and treat Consumer Tomorrow as a PR stance rather than a live customer.
- **Focus on user needs, not capability**: Mixed. Utility investment tends to be capability-driven (more generation, more grid); the actual Tomorrow-side need is *survivability and affordability under shock*, which few operators are organised to deliver.
- **Use appropriate methods**: Serious mismatch on the externality rail. CO2 Apparatus is being governed with Product-stage regulatory methods (ETS cap-setting, auction rules) while the underlying Cost-with-Externalities discipline is still Custom-Built — the governance is over-engineered relative to the underlying science. Conversely, Hydrogen Storage is being funded with Commodity-style long-term utility contracts when it needs Agile/Lean pilot methods.
- **Manage inertia**: Four explicit inertia markers (Distribution, Transmission, Gas, Nuclear, Regulation). These are the five fronts where evolution will be fought hardest — and where strategic effort should be *managing resistance*, not routing around it.
- **Use standards where appropriate**: Strong at the market and grid layer (ENTSO-E, IEEE, IEC). Weak at the Tomorrow layer — no standards for survivability metrics, microgen-to-grid interop, or supply-chain traceability.
- **Bias to action**: The 17-form inertia catalogue here is largely supplier inertia (capital, existing contracts, political commitments). Action needs to accept that the inertia is real and focus on the disruption frontier components (Storage, Externalities, Solar Microgen) where the resistance is lower.

## Recommended Actions

1. **Treat Electrical Storage as a buy, not a build.** Li-ion grid batteries are crossing into Product in mid-2022: Tesla, Fluence, Wärtsilä, CATL, Sungrow. Any utility or corporate that is still RFP-ing bespoke battery systems is subsidising the vendor's product roadmap. Redirect internal engineering to *siting* and *grid integration* — those are the durable differentiators.
2. **Invest in the externality rail as a Genesis-stage bet.** Cost with Externalities and Supply-Chain Awareness are near-Genesis. Fund small, experimental teams (internal or consortium) on three fronts: (a) internal shadow carbon price that actually binds decisions, (b) component-level supply-chain traceability for the 10-20 critical inputs, (c) externality-inclusive LCOE for the next capital allocation cycle. Do not governance-board this to maturity — that kills it.
3. **Re-frame Hydrogen as a Custom-Built pilot portfolio, not an infrastructure programme.** In July 2022, hydrogen is three-to-five years short of Product. Fund a portfolio of 3-5 pilots (industrial heat, grid balancing, transport) with hard kill criteria. Avoid the trap of committing production-scale capital on the basis of a published strategy document.
4. **Manage Distribution and Transmission inertia, don't route around it.** These are 40-year assets. The strategy should be *accelerating planned renewal* into DSO-ready formats (flexibility markets, real-time data sharing, DER integration) rather than waiting for Grid 2.0. The next 5-year regulatory price-control window is the decision point.
5. **Treat the Consumer Tomorrow anchor as a fragile population, not a market segment.** Protect it through the Survivability and Education rails — not by selling more microgen. The components Consumer Tomorrow depends on are mostly Custom-Built; a single winter of high prices reverts the marginal household to Consumer Today. Strategic robustness sits upstream of the tariff.

## Build vs. Buy Assessment

| Component | Recommendation | Rationale |
|---|---|---|
| Distribution, Transmission, Gas generation | **Keep / manage** | Commodity infrastructure with 20-40 year asset lives; decisions are about renewal cadence and protocol upgrades, not build-vs-buy. |
| Renewable (utility), Solar Microgen | **Buy via auction/PPA** | Product stage with multiple vendors; LCOE competition is live; no reason to vertically integrate at the panel/turbine level. |
| Electrical Storage | **Buy** | Crossing into Product in mid-2022; the differentiator is siting and market participation, not the cell chemistry. |
| Hydrogen Storage | **Build (small portfolio)** | Custom-Built. Pilot-stage. A portfolio of 3-5 pilots is right; a production-scale build is wrong. |
| Nuclear (existing) | **Extend / lifetime** | Commodity-adjacent Product; life-extension is generally bankable in 2022 economics. Avoid betting large new-build on non-delivered SMR designs. |
| Grid Control Systems | **Buy** | Product stage with 3+ credible vendors. Do not build in-house EMS/DMS. |
| Cost with Externalities, CO2 apparatus | **Build internally** | Near-Genesis / Custom-Built. Your internal capability to *use* externality pricing in decisions is part of your moat. |
| Supply-Chain Awareness | **Build as consortium** | Genesis. No single organisation can do this alone; a sector consortium (batteries, silicon, transformer steel) is the right venue. |
| Regulation | **Engage, don't build** | Product-stage institutional form — but with inertia. Strategic value is in shaping the next price-control / market-reform cycle. |

## Evolution Predictions (12-24 months, i.e. through late 2023-2024)

Drawn as dashed red arrows on the map:

- **Renewable 0.60 → 0.78**: utility wind and solar standardise further under repeat-auction regimes (EU REPowerEU, US IRA once enacted). Move into deep Product / early Commodity.
- **Solar Microgen 0.54 → 0.72**: consumer-financed rooftop + battery becomes a mainline Product in most OECD retail markets; installer ecosystems harden.
- **Electrical Storage 0.48 → 0.66**: from border-of-Product to mid-Product. Multi-hour li-ion standardised for utility duration; longer-duration still open.
- **Hydrogen Storage 0.22 → 0.42**: from near-Custom-Built to mid-Custom-Built. Pilots mature, some production capacity, but *not* a Product category by 2024.
- **CO2 Apparatus 0.34 → 0.58**: from mid-Custom-Built to mid-Product as EU CBAM enters force, more jurisdictions adopt ETS-compatible schemes, voluntary offset market is reformed post-SBTi.
- **Cost with Externalities 0.18 → 0.46**: from near-Genesis to mid-Custom-Built as internal shadow pricing becomes mainstream in capital-allocation committees.
- **Supply-Chain Awareness 0.14 → 0.38**: from Genesis to Custom-Built as CSRD, UFLPA, EU Battery Passport, IRA domestic-content force component-level traceability.

## Open Questions

1. **If CO2 Apparatus moves to Product by 2024 but Cost with Externalities lags in Custom-Built, who arbitrages the mismatch?** The risk is that carbon is priced (ETS, CBAM) on assumptions that the underlying externality accounting has not yet settled — producing a market that clears at a price that is both binding and wrong.
2. **Does the July-2022 capital-cost spike permanently re-rank the generation mix?** Nuclear and long-duration storage are the most capital-sensitive; renewables are second-most; gas CCGT is the least. A higher cost-of-capital regime tilts deployment toward gas longer than the climate rhetoric suggests — the map may need an inertia marker on *capital* itself.
3. **Will the Consumer Tomorrow anchor survive a second crisis winter (2022-23)?** If Survivability and Education components fail to mature fast enough, the anchor collapses back into Consumer Today and the political support for the rest of the transition wavers. This is the scenario-risk the map most needs its holder to war-game.

---

## Notes on the run

- **Components**: 30 (3 anchors + 27 non-anchor).
- **Anchor count**: 3 (Consumer Today, Consumer Tomorrow, Society & Government).
- **Evolutions**: 7 (Renewable, Solar Microgen, Electrical Storage, Hydrogen, CO2 Apparatus, Cost with Externalities, Supply-Chain Awareness).
- **Inertia markers**: 5 (Distribution, Transmission, Gas, Nuclear, Regulation).
- **Divergences from the haberlah workflow**:
  - Step 1 asks the skill to clarify strategic context *with the user*. The scenario is fixed, so I answered the four questions from the scenario myself (in the Strategic Context section above) rather than asking.
  - Step 2 recommends 8-15 components and flags >15 as "suggest submaps". I carried 30 components (3 anchors + 27 non-anchor) because the brief explicitly names 5 generation types, 4 storage types, 3 transmission/production/distribution stages, 5 market-layer pieces, 4 consumer-facing pieces, and 3 control/regulation/CO2 pieces, plus capital intensity and supply-chain awareness as explicit asks. Splitting into submaps would fragment the central narrative (the gap between the mature supply side and the immature externality/tomorrow side), which is the map's strategic point. I noted the deviation here and accepted the readability cost.
  - I used three user anchors rather than one. The skill's SKILL.md says "at least one user/anchor at the top of the chain" but the OWM reference shows multi-anchor examples, and the scenario's own today-vs-tomorrow framing makes the multi-anchor setup necessary to show the evolution tension.
  - Step 4 asks to run `validate_map.py` "if available". I did not execute it (this is a blind first-pass); I did the manual checks it calls out (positions in [0,1]; no cycles; arrows right-pointing; every referenced component exists; one+ anchor at top; no components within 0.06 on both axes). I additionally checked the Wardley-math visibility constraint ν(a) ≥ ν(b) on every dependency, which is stricter than the haberlah validator.
  - I did not run `parse_owm.py` because the scenario supplied prose, not existing OWM text.
