/**
 * Wardley Map: Transportation Logistics Landscape
 *
 * Generated via the haberlah/wardley-mapping skill. Follows the artifact
 * template at templates/artifact-template.jsx, populated with the map
 * data from draft.owm.
 */

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

// ============================================================
// 2. COORDINATE MAPPING
// ============================================================

function toSvgX(maturity) {
  return PADDING.left + maturity * (WIDTH - PADDING.left - PADDING.right);
}

function toSvgY(visibility) {
  return PADDING.top + (1 - visibility) * (HEIGHT - PADDING.top - PADDING.bottom);
}

// ============================================================
// 3. MAP DATA — Transportation Logistics Landscape
// ============================================================

const MAP = {
  title: "Transportation Logistics Landscape",
  purpose: "Where is logistics commoditised utility, and where will automated delivery or sovereignty concerns force it to evolve?",
  components: [
    { id: "the-public", name: "The Public", visibility: 0.97, maturity: 0.60, stage: "Anchor",
      rationale: "End-user of the logistics system as consumer and citizen.", isAnchor: true },
    { id: "producers", name: "Producers", visibility: 0.94, maturity: 0.48, stage: "Anchor",
      rationale: "Secondary user: manufacturers/growers whose goods must move.", isAnchor: true },
    { id: "government", name: "Government", visibility: 0.95, maturity: 0.32, stage: "Anchor",
      rationale: "Regulatory and sovereign actor, separate from end-consumers.", isAnchor: true },

    { id: "shops", name: "Shops", visibility: 0.88, maturity: 0.80, stage: "Commodity",
      rationale: "Retail is ubiquitous and commoditised; pure-play shops differ mainly on format, not existence." },
    { id: "e-commerce", name: "E-commerce", visibility: 0.86, maturity: 0.68, stage: "Product",
      rationale: "Mature category with several dominant platforms (Amazon, Shopify, Tmall) and a long tail; still evolving toward utility as integrations standardise." },

    { id: "delivery", name: "Delivery", visibility: 0.80, maturity: 0.58, stage: "Product",
      rationale: "Many competing vendors (UPS, FedEx, DPD, Evri, Amazon Logistics) with comparable service envelopes." },
    { id: "real-time-stock", name: "Real-Time Stock", visibility: 0.74, maturity: 0.30, stage: "Custom-Built",
      rationale: "Across the economy real-time inventory visibility is still patchy and bespoke; only leading retailers have it end-to-end." },
    { id: "supply-chain-awareness", name: "Supply Chain Awareness", visibility: 0.78, maturity: 0.18, stage: "Custom-Built",
      rationale: "Public/shipper ability to know what is in the supply chain is emerging - driven by post-2020 disruption - but not yet a product." },

    { id: "last-mile", name: "Last Mile", visibility: 0.66, maturity: 0.48, stage: "Product",
      rationale: "Multiple established providers; economics still painful and innovation-heavy, so not yet Commodity." },
    { id: "long-haul", name: "Long Haul", visibility: 0.60, maturity: 0.80, stage: "Commodity",
      rationale: "Trunk road/rail/sea freight is near-utility - price-driven, standardised loading units, interchangeable carriers." },
    { id: "logistics-hubs", name: "Logistics Hubs", visibility: 0.54, maturity: 0.62, stage: "Product",
      rationale: "Operated by professional 3PLs (DHL, Kuehne+Nagel, XPO); differentiation by location and automation level." },
    { id: "warehouses-storage", name: "Warehouses & Storage", visibility: 0.48, maturity: 0.82, stage: "Commodity",
      rationale: "Square-footage of pallet storage is sold on spot markets (Stord, Flexe, Flock Freight) at transparent pricing." },

    { id: "trucks-hgv", name: "Trucks (HGV)", visibility: 0.38, maturity: 0.80, stage: "Commodity",
      rationale: "Heavy trucks from a handful of global OEMs (Daimler, Volvo, Scania, Paccar) with stable specifications." },
    { id: "automated-delivery", name: "Automated Delivery", visibility: 0.34, maturity: 0.18, stage: "Custom-Built",
      rationale: "Emerging: Nuro, Starship, Amazon Scout pilots, etc. Few deployments, no standardised model yet." },
    { id: "drones-scouts", name: "Drones & Scouts", visibility: 0.30, maturity: 0.12, stage: "Genesis",
      rationale: "Active experimentation (Zipline, Wing, Amazon Prime Air). Limited routes, constant regulatory change, no stable market." },
    { id: "powertrain-fossil-electric", name: "Powertrain (Fossil/Electric)", visibility: 0.26, maturity: 0.60, stage: "Product",
      rationale: "Diesel is commoditised; electric truck/van powertrain is a fast-moving Product stage (Tesla Semi, Volvo FH Electric, BYD)." },

    { id: "traffic-telematics-data", name: "Traffic & Telematics Data", visibility: 0.42, maturity: 0.70, stage: "Commodity",
      rationale: "Road data, weather, and telematics are available as utility APIs (HERE, TomTom, Geotab); consumers and fleets alike rely on them." },

    { id: "cities", name: "Cities", visibility: 0.22, maturity: 0.86, stage: "Commodity",
      rationale: "Urban topology is a stable given - pricing in congestion, ULEZ etc." },
    { id: "rural-areas", name: "Rural Areas", visibility: 0.20, maturity: 0.72, stage: "Commodity",
      rationale: "Equally stable; the last-mile cost problem is structural, not novel." },

    { id: "regulation", name: "Regulation", visibility: 0.14, maturity: 0.66, stage: "Product",
      rationale: "Mature regulatory apparatus (driver hours, vehicle standards, customs) but steadily evolving with electrification and autonomy rules." },
    { id: "hgv-skills", name: "HGV Skills", visibility: 0.44, maturity: 0.40, stage: "Product",
      rationale: "Training and licensing are a well-understood Product-stage activity, but acute structural shortages (UK, EU, US) resist commoditisation.",
      inertia: true },
    { id: "sovereignty-cni", name: "Sovereignty (CNI/Territorial)", visibility: 0.10, maturity: 0.24, stage: "Custom-Built",
      rationale: "Each jurisdiction defines what counts as Critical National Infrastructure differently; sovereignty requirements actively resist commoditisation of foreign providers.",
      inertia: true }
  ],
  links: [
    { from: "the-public", to: "shops" },
    { from: "the-public", to: "e-commerce" },
    { from: "the-public", to: "supply-chain-awareness" },
    { from: "producers", to: "long-haul" },
    { from: "producers", to: "warehouses-storage" },
    { from: "government", to: "regulation" },
    { from: "government", to: "sovereignty-cni" },

    { from: "shops", to: "delivery" },
    { from: "shops", to: "real-time-stock" },
    { from: "e-commerce", to: "delivery" },
    { from: "e-commerce", to: "real-time-stock" },

    { from: "delivery", to: "last-mile" },
    { from: "delivery", to: "long-haul" },
    { from: "last-mile", to: "logistics-hubs" },
    { from: "long-haul", to: "logistics-hubs" },
    { from: "logistics-hubs", to: "warehouses-storage" },
    { from: "real-time-stock", to: "traffic-telematics-data" },
    { from: "supply-chain-awareness", to: "traffic-telematics-data" },

    { from: "last-mile", to: "trucks-hgv" },
    { from: "last-mile", to: "automated-delivery" },
    { from: "last-mile", to: "drones-scouts" },
    { from: "long-haul", to: "trucks-hgv" },
    { from: "long-haul", to: "automated-delivery" },
    { from: "automated-delivery", to: "drones-scouts" },

    { from: "trucks-hgv", to: "powertrain-fossil-electric" },
    { from: "automated-delivery", to: "powertrain-fossil-electric" },
    { from: "drones-scouts", to: "powertrain-fossil-electric" },

    { from: "trucks-hgv", to: "traffic-telematics-data" },
    { from: "automated-delivery", to: "traffic-telematics-data" },

    { from: "last-mile", to: "cities" },
    { from: "last-mile", to: "rural-areas" },
    { from: "logistics-hubs", to: "cities" },

    { from: "trucks-hgv", to: "hgv-skills" },
    { from: "long-haul", to: "hgv-skills" },
    { from: "long-haul", to: "regulation" },
    { from: "warehouses-storage", to: "regulation" },
    { from: "logistics-hubs", to: "sovereignty-cni" },
    { from: "warehouses-storage", to: "sovereignty-cni" }
  ],
  evolutions: [
    { componentId: "last-mile", toMaturity: 0.72 },
    { componentId: "automated-delivery", toMaturity: 0.55 },
    { componentId: "drones-scouts", toMaturity: 0.42 },
    { componentId: "real-time-stock", toMaturity: 0.72 },
    { componentId: "powertrain-fossil-electric", toMaturity: 0.82 },
    { componentId: "traffic-telematics-data", toMaturity: 0.85 },
    { componentId: "supply-chain-awareness", toMaturity: 0.50 },
    { componentId: "shops", toMaturity: 0.90 }
  ],
  annotations: [
    { id: 1, text: "Long-haul, warehousing, and shops behave as commoditised utility", x: 0.88, y: 0.48 },
    { id: 2, text: "Automated delivery / drones: Genesis/Custom-Built, poised to evolve", x: 0.15, y: 0.32 },
    { id: 3, text: "Sovereignty + CNI concerns are the main source of inertia", x: 0.24, y: 0.10 },
    { id: 4, text: "HGV skills shortage: Product-stage activity stuck behind a scarce resource", x: 0.40, y: 0.44 }
  ]
};

// ============================================================
// 4. DEPENDENCY CHAIN FINDER
// ============================================================

function findDependencyChain(componentId, links) {
  const connected = new Set([componentId]);
  let changed = true;
  while (changed) {
    changed = false;
    for (const link of links) {
      if (connected.has(link.to) && !connected.has(link.from)) {
        connected.add(link.from);
        changed = true;
      }
      if (connected.has(link.from) && !connected.has(link.to)) {
        connected.add(link.to);
        changed = true;
      }
    }
  }
  return connected;
}

// ============================================================
// 5. LABEL OFFSETS
// ============================================================

function computeLabelOffsets(components) {
  const offsets = {};
  const positions = components.map(c => ({
    id: c.id,
    sx: toSvgX(c.maturity),
    sy: toSvgY(c.visibility)
  }));

  for (const comp of components) {
    let dx = 10;
    let dy = -12;
    const sx = toSvgX(comp.maturity);
    const sy = toSvgY(comp.visibility);

    for (const other of positions) {
      if (other.id === comp.id) continue;
      const distX = Math.abs(sx - other.sx);
      const distY = Math.abs(sy - other.sy);
      if (distX < 70 && distY < 25) {
        if (sy <= other.sy) dy = -14;
        else dy = 16;
      }
    }

    if (sx + dx + comp.name.length * 6 > WIDTH - PADDING.right) {
      dx = -(comp.name.length * 6 + 10);
    }
    if (sy + dy < PADDING.top + 10) dy = 14;

    offsets[comp.id] = comp.labelOffset || { dx, dy };
  }
  return offsets;
}

// ============================================================
// 6. MAIN COMPONENT
// ============================================================

export default function WardleyMap() {
  const [hoveredId, setHoveredId] = useState(null);
  const [selectedId, setSelectedId] = useState(null);
  const [tooltipPos, setTooltipPos] = useState({ x: 0, y: 0 });

  const map = MAP;

  const labelOffsets = useMemo(
    () => computeLabelOffsets(map.components),
    [map.components]
  );

  const selectedChain = useMemo(() => {
    if (!selectedId) return null;
    return findDependencyChain(selectedId, map.links);
  }, [selectedId, map.links]);

  const componentMap = useMemo(() => {
    const m = {};
    map.components.forEach(c => { m[c.id] = c; });
    return m;
  }, [map.components]);

  const isVisible = useCallback((id) => {
    if (!selectedChain) return true;
    return selectedChain.has(id);
  }, [selectedChain]);

  const isLinkVisible = useCallback((link) => {
    if (!selectedChain) return true;
    return selectedChain.has(link.from) && selectedChain.has(link.to);
  }, [selectedChain]);

  const handleComponentHover = useCallback((e, comp) => {
    const svgRect = e.currentTarget.closest("svg").getBoundingClientRect();
    const x = e.clientX - svgRect.left;
    const y = e.clientY - svgRect.top;
    setHoveredId(comp.id);
    setTooltipPos({ x, y });
  }, []);

  const hoveredComp = hoveredId ? componentMap[hoveredId] : null;

  function dependencyPath(fromComp, toComp) {
    const x1 = toSvgX(fromComp.maturity);
    const y1 = toSvgY(fromComp.visibility);
    const x2 = toSvgX(toComp.maturity);
    const y2 = toSvgY(toComp.visibility);
    const midY = (y1 + y2) / 2;
    const curveOffset = Math.abs(x1 - x2) < 20 ? 15 : 0;
    return `M ${x1} ${y1} Q ${(x1 + x2) / 2 + curveOffset} ${midY} ${x2} ${y2}`;
  }

  return (
    <div className="w-full max-w-5xl mx-auto p-4">
      <h2 className="text-lg font-semibold text-gray-800 mb-1">{map.title}</h2>
      {map.purpose && (
        <p className="text-sm text-gray-500 mb-3">{map.purpose}</p>
      )}

      <div className="relative border border-gray-200 rounded bg-white">
        <svg
          viewBox={`0 0 ${WIDTH} ${HEIGHT}`}
          className="w-full h-auto"
          style={{ fontFamily: "'Segoe UI', system-ui, -apple-system, sans-serif" }}
          onClick={() => setSelectedId(null)}
        >
          {/* Stage column fills */}
          {STAGE_LABELS.map((_, i) => {
            const x0 = toSvgX(i === 0 ? 0 : STAGE_BOUNDARIES[i - 1]);
            const x1 = toSvgX(i < STAGE_BOUNDARIES.length ? STAGE_BOUNDARIES[i] : 1);
            return (
              <rect key={`stage-bg-${i}`}
                x={x0} y={PADDING.top}
                width={x1 - x0}
                height={HEIGHT - PADDING.top - PADDING.bottom}
                fill={COLORS.stageFills[i]} />
            );
          })}

          {/* Grid lines */}
          {STAGE_BOUNDARIES.map((b, i) => (
            <line key={`grid-${i}`}
              x1={toSvgX(b)} y1={PADDING.top}
              x2={toSvgX(b)} y2={HEIGHT - PADDING.bottom}
              stroke={COLORS.gridLine}
              strokeDasharray="6 4" strokeWidth={1} />
          ))}

          {/* Axes */}
          <line x1={PADDING.left} y1={PADDING.top}
            x2={PADDING.left} y2={HEIGHT - PADDING.bottom}
            stroke={COLORS.axisLine} strokeWidth={1.5} />
          <text x={PADDING.left - 10} y={PADDING.top - 8} textAnchor="middle"
            fontSize={11} fill={COLORS.axisLabel} fontWeight={500}>Visible</text>
          <text x={PADDING.left - 10} y={HEIGHT - PADDING.bottom + 18} textAnchor="middle"
            fontSize={11} fill={COLORS.axisLabel} fontWeight={500}>Invisible</text>
          <text
            transform={`rotate(-90, ${18}, ${(PADDING.top + HEIGHT - PADDING.bottom) / 2})`}
            x={18} y={(PADDING.top + HEIGHT - PADDING.bottom) / 2}
            textAnchor="middle" fontSize={12} fill={COLORS.axisLabel} fontWeight={600}>
            Value Chain
          </text>

          <line x1={PADDING.left} y1={HEIGHT - PADDING.bottom}
            x2={WIDTH - PADDING.right} y2={HEIGHT - PADDING.bottom}
            stroke={COLORS.axisLine} strokeWidth={1.5} />
          {STAGE_LABELS.map((label, i) => {
            const xStart = i === 0 ? 0 : STAGE_BOUNDARIES[i - 1];
            const xEnd = i < STAGE_BOUNDARIES.length ? STAGE_BOUNDARIES[i] : 1;
            const cx = toSvgX((xStart + xEnd) / 2);
            return (
              <text key={`stage-label-${i}`}
                x={cx} y={HEIGHT - PADDING.bottom + 20}
                textAnchor="middle" fontSize={11}
                fill={COLORS.stageLabel} fontWeight={500}>
                {label}
              </text>
            );
          })}
          <text x={(PADDING.left + WIDTH - PADDING.right) / 2}
            y={HEIGHT - PADDING.bottom + 38}
            textAnchor="middle" fontSize={12} fill={COLORS.axisLabel} fontWeight={600}>
            Evolution
          </text>

          <defs>
            <marker id="evo-arrow" viewBox="0 0 10 10"
              refX={9} refY={5} markerWidth={6} markerHeight={6}
              orient="auto-start-reverse" fill={COLORS.evolutionArrow}>
              <path d="M 0 0 L 10 5 L 0 10 z" />
            </marker>
          </defs>

          {/* Dependency lines */}
          {map.links.map((link, i) => {
            const from = componentMap[link.from];
            const to = componentMap[link.to];
            if (!from || !to) return null;
            const visible = isLinkVisible(link);
            return (
              <path key={`link-${i}`}
                d={dependencyPath(from, to)}
                fill="none"
                stroke={COLORS.dependencyLine}
                strokeWidth={1.5}
                opacity={visible ? 0.7 : COLORS.dimmedOpacity}
                style={{ transition: "opacity 0.2s" }} />
            );
          })}

          {/* Evolution arrows */}
          {map.evolutions.map((evo, i) => {
            const comp = componentMap[evo.componentId];
            if (!comp) return null;
            const x1 = toSvgX(comp.maturity);
            const x2 = toSvgX(evo.toMaturity);
            const y = toSvgY(comp.visibility);
            const visible = isVisible(comp.id);
            return (
              <line key={`evo-${i}`}
                x1={x1 + 8} y1={y}
                x2={x2 - 4} y2={y}
                stroke={COLORS.evolutionArrow}
                strokeWidth={2}
                strokeDasharray="6 3"
                markerEnd="url(#evo-arrow)"
                opacity={visible ? 0.9 : COLORS.dimmedOpacity}
                style={{ transition: "opacity 0.2s" }} />
            );
          })}

          {/* Inertia markers */}
          {map.components.filter(c => c.inertia).map(comp => {
            const x = toSvgX(comp.maturity);
            const y = toSvgY(comp.visibility);
            const visible = isVisible(comp.id);
            return (
              <g key={`inertia-${comp.id}`}
                opacity={visible ? 1 : COLORS.dimmedOpacity}
                style={{ transition: "opacity 0.2s" }}>
                <rect x={x + 9} y={y - 8} width={4} height={16}
                  fill={COLORS.inertiaBar} rx={1} />
                <rect x={x + 15} y={y - 8} width={4} height={16}
                  fill={COLORS.inertiaBar} rx={1} />
              </g>
            );
          })}

          {/* Components */}
          {map.components.map(comp => {
            const cx = toSvgX(comp.maturity);
            const cy = toSvgY(comp.visibility);
            const isSelected = selectedId === comp.id;
            const isHovered = hoveredId === comp.id;
            const visible = isVisible(comp.id);
            const offset = labelOffsets[comp.id] || { dx: 10, dy: -12 };

            return (
              <g key={comp.id}
                opacity={visible ? 1 : COLORS.dimmedOpacity}
                style={{ transition: "opacity 0.2s", cursor: "pointer" }}
                onMouseEnter={(e) => handleComponentHover(e, comp)}
                onMouseLeave={() => setHoveredId(null)}
                onClick={(e) => {
                  e.stopPropagation();
                  setSelectedId(prev => prev === comp.id ? null : comp.id);
                }}>
                <circle cx={cx} cy={cy}
                  r={comp.isAnchor ? 8 : 6}
                  fill={COLORS.componentFill}
                  stroke={isSelected || isHovered ? COLORS.componentStrokeSelected : COLORS.componentStroke}
                  strokeWidth={isSelected ? 2.5 : isHovered ? 2.5 : 1.8} />
                {comp.isAnchor && (
                  <circle cx={cx} cy={cy} r={3}
                    fill={COLORS.componentStroke} />
                )}
                <text x={cx + offset.dx} y={cy + offset.dy}
                  fontSize={11}
                  fontWeight={isSelected || isHovered ? 600 : 500}
                  fill={COLORS.labelText}>
                  {comp.name}
                </text>
              </g>
            );
          })}

          {/* Annotations */}
          {(map.annotations || []).map(ann => {
            const ax = toSvgX(ann.x);
            const ay = toSvgY(ann.y);
            return (
              <g key={`ann-${ann.id}`}>
                <circle cx={ax} cy={ay} r={10}
                  fill="#3b82f6" opacity={0.15} />
                <text x={ax} y={ay + 4}
                  textAnchor="middle" fontSize={10}
                  fontWeight={700} fill="#3b82f6">
                  {ann.id}
                </text>
              </g>
            );
          })}
        </svg>

        {/* Tooltip */}
        {hoveredComp && (
          <div className="absolute pointer-events-none z-10 px-3 py-2 rounded shadow-lg text-xs max-w-xs"
            style={{
              left: tooltipPos.x + 16,
              top: tooltipPos.y - 10,
              backgroundColor: COLORS.tooltipBg,
              color: COLORS.tooltipText
            }}>
            <div className="font-semibold mb-1">{hoveredComp.name}</div>
            <div className="opacity-80 mb-1">
              Stage: {hoveredComp.stage} &nbsp;|&nbsp; Position: [{hoveredComp.visibility.toFixed(2)}, {hoveredComp.maturity.toFixed(2)}]
            </div>
            <div className="opacity-90 leading-snug">{hoveredComp.rationale}</div>
          </div>
        )}
      </div>

      {/* Legend */}
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
