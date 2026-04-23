/**
 * Wardley Map React Artifact — Space-Based Telecoms (February 2023)
 *
 * Generated via the haberlah/wardley-mapping skill. Matches the OWM draft in
 * the same run folder. Built on templates/artifact-template.jsx — structure
 * and coordinate mapping follow the template verbatim; only SAMPLE_MAP is
 * replaced with the scenario data.
 */

import { useState, useCallback, useMemo } from "react";

// ============================================================
// 1. CONSTANTS (from style-constants.json)
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
  dimmedOpacity: 0.15,
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
// 3. MAP DATA
// ============================================================

const MAP = {
  title: "Space-Based Telecoms (February 2023)",
  purpose:
    "Where space telecoms has commoditised and where LEO / NTN is still novel — consumer, corporate, and government access stack, satellite subsystems, control, and the supply chain underneath.",
  components: [
    // Anchors
    { id: "consumers", name: "Consumers", visibility: 0.97, maturity: 0.45, stage: "Product", isAnchor: true,
      rationale: "End consumers buying connectivity or broadcast. The user at the top of the chain." },
    { id: "corporations", name: "Corporations", visibility: 0.97, maturity: 0.55, stage: "Product", isAnchor: true,
      rationale: "Enterprise buyers of maritime/aviation/backhaul connectivity — a second anchor with its own procurement logic." },
    { id: "government", name: "Government", visibility: 0.97, maturity: 0.65, stage: "Product", isAnchor: true,
      rationale: "Defence, civil agencies, regulators. Drives sovereign capability and sits above regulation." },

    // User-visible services
    { id: "network-access", name: "Network Access", visibility: 0.90, maturity: 0.55, stage: "Product",
      rationale: "Network access as a user-facing service is a mature expectation (fixed, mobile, and now space-enabled). Product-stage because offerings compete on feature/price." },
    { id: "broadcast", name: "Broadcast", visibility: 0.82, maturity: 0.85, stage: "Commodity",
      rationale: "DTH satellite broadcast has been standardised and utility-priced since the 1990s. Viewers never think about it until a signal is lost." },
    { id: "space-regulation", name: "Space Regulation", visibility: 0.82, maturity: 0.50, stage: "Product",
      rationale: "ITU spectrum coordination and national regulators (FCC, Ofcom, ANATEL) are institutionalised, but mega-constellation / NTN rules are still being written — hence centre-right of Product, with inertia on the novel frontier." },

    // Access-stack topology
    { id: "mobile-topology", name: "Mobile Topology (4G/5G)", visibility: 0.74, maturity: 0.78, stage: "Commodity",
      rationale: "4G is fully commoditised globally; 5G is late Product / early Commodity by Feb 2023." },
    { id: "fibre-topology", name: "Fibre Topology", visibility: 0.74, maturity: 0.86, stage: "Commodity",
      rationale: "Fibre transport is utility infrastructure — regulated, standardised, pay-per-bit." },
    { id: "ntn-topology", name: "NTN Topology", visibility: 0.74, maturity: 0.30, stage: "Custom-Built", inertia: true,
      rationale: "3GPP Release 17 NTN was frozen in mid-2022. Integration with terrestrial networks is still bespoke per operator in Feb 2023. Inertia flagged because 5G standards bodies had to force this conversation." },
    { id: "physical-network", name: "Physical Network", visibility: 0.66, maturity: 0.80, stage: "Commodity",
      rationale: "IP/MPLS transit and submarine cable are commodity utilities. Invisible until outage." },

    // Edge and terminal
    { id: "user-terminals", name: "User Terminals (Phased Array)", visibility: 0.58, maturity: 0.38, stage: "Custom-Built",
      rationale: "Electronically steered phased-array terminals (Starlink Dishy, Kymeta, ThinKom) are still expensive, heavily subsidised, and not yet interoperable. Moving toward Product but not there." },
    { id: "ground-stations", name: "Ground Stations", visibility: 0.60, maturity: 0.58, stage: "Product",
      rationale: "AWS Ground Station (2018), Azure Orbital (2020) and KSAT's network have turned ground-segment-as-a-service into a rentable Product. Still competitive, not yet utility-priced." },
    { id: "spectrum", name: "Spectrum (Ku/Ka/V)", visibility: 0.56, maturity: 0.70, stage: "Product",
      rationale: "Ku and Ka are mature, well-coordinated via ITU filings. V-band is still carving out rules — overall centre-right Product because most traffic is on the mature bands." },

    // Satellite platform
    { id: "leo-microsats", name: "LEO Microsats", visibility: 0.48, maturity: 0.35, stage: "Custom-Built",
      rationale: "Post-Starlink / OneWeb / Planet, mass-produced LEO buses exist, but each operator iterates hardware every generation. Design is still a competitive differentiator — Custom-Built moving to Product." },
    { id: "geo-satellites", name: "GEO Satellites", visibility: 0.48, maturity: 0.78, stage: "Commodity",
      rationale: "GEO buses have been a regulated product market since the 1970s. Airbus, Boeing, Lockheed, Thales, Maxar compete on standardised platforms. Firmly Commodity." },

    // Satellite subsystems
    { id: "beamforming", name: "Beamforming / Beam-Steering", visibility: 0.38, maturity: 0.32, stage: "Custom-Built", inertia: true,
      rationale: "Digital multi-beam phased-array processors are still being iterated in-house by each major operator. Silicon providers (Anokiwave, Analog Devices) exist but integration is bespoke. Inertia because operators protect their digital payload IP." },
    { id: "sat-antennas", name: "Satellite Antennas", visibility: 0.38, maturity: 0.65, stage: "Product",
      rationale: "Reflector and horn antennas have competing vendors (Airbus, Thales, L3Harris, Viasat). Digital and metamaterial variants are earlier but the bulk of the market is Product." },
    { id: "optical-isl", name: "Optical Sat-to-Sat Comms", visibility: 0.38, maturity: 0.18, stage: "Genesis",
      rationale: "Starlink's v1.5 / v2-mini with lasercom was deploying through 2022–23; Mynaric and TESAT supply others. In Feb 2023 this is still Genesis — real-world at-scale operation just beginning." },
    { id: "propulsion", name: "Satellite Propulsion (Kr/Xe)", visibility: 0.30, maturity: 0.55, stage: "Product",
      rationale: "Hall-effect thrusters are commercially available (Busek, Aerojet, Safran). Starlink's Krypton thrusters are newer; Xenon is very mature. Centre Product." },
    { id: "thermal", name: "Thermal Control (TE/Rad/Cryo)", visibility: 0.30, maturity: 0.62, stage: "Product",
      rationale: "Radiative radiators and heat pipes are off-the-shelf. Thermoelectric and cryogenic cooling are Product-stage for most classes of payload. Exotic cryogens (infrared/astronomy) push the left edge." },
    { id: "sat-power", name: "Satellite Power", visibility: 0.30, maturity: 0.82, stage: "Commodity",
      rationale: "Space-grade triple-junction solar cells and Li-ion batteries are standardised and competitively priced — a commoditised subsystem." },

    // Launch and orbit services
    { id: "launchers", name: "Launchers", visibility: 0.22, maturity: 0.58, stage: "Product",
      rationale: "Falcon 9 / rideshare is moving launch toward Commodity on $/kg, but the market is still competitive (ULA, Arianespace, Rocket Lab, ISRO, CASC). Reusability is a Product differentiator, not yet a utility." },
    { id: "orbit-tracking", name: "Orbit Tracking", visibility: 0.22, maturity: 0.68, stage: "Product",
      rationale: "18 SPCS / Space-Track provides the baseline; LeoLabs, COMSPOC, ExoAnalytic sell commercial orbital data. Well-understood, multiple vendors." },
    { id: "debris-tracking", name: "Debris Tracking", visibility: 0.22, maturity: 0.42, stage: "Custom-Built",
      rationale: "Commercial SSA for < 10 cm debris is emerging (LeoLabs radar, NorthStar optical). Government SSA catalogues are still the authoritative source — Custom-Built moving to Product." },

    // Ops and supply chain underneath
    { id: "fleet-management", name: "Fleet Management", visibility: 0.14, maturity: 0.35, stage: "Custom-Built",
      rationale: "Each operator builds their own constellation OSS/BSS (Starlink in-house, OneWeb on Airbus-built stack, Iridium on Motorola heritage). No dominant product for fleet management yet." },
    { id: "automation", name: "Automation", visibility: 0.14, maturity: 0.22, stage: "Custom-Built",
      rationale: "Autonomous conjunction assessment and automated manoeuvre planning is emerging (Starlink is public about it) but still bespoke to each operator. Early Custom-Built." },
    { id: "supply-chain", name: "Supply-Chain Awareness", visibility: 0.06, maturity: 0.22, stage: "Custom-Built",
      rationale: "Component traceability, ITAR compliance, and space-heritage databases are still a patchwork of vendor-specific tools. Tragedy-of-the-commons style problem." },
  ],
  links: [
    // Anchor -> service
    { from: "consumers", to: "network-access" },
    { from: "corporations", to: "network-access" },
    { from: "government", to: "network-access" },
    { from: "consumers", to: "broadcast" },
    { from: "corporations", to: "broadcast" },
    { from: "government", to: "broadcast" },
    { from: "consumers", to: "space-regulation" },
    { from: "corporations", to: "space-regulation" },
    { from: "government", to: "space-regulation" },

    // Service -> topology
    { from: "network-access", to: "mobile-topology" },
    { from: "network-access", to: "fibre-topology" },
    { from: "network-access", to: "ntn-topology" },
    { from: "broadcast", to: "ntn-topology" },
    { from: "broadcast", to: "geo-satellites" },

    // Topology -> transport
    { from: "mobile-topology", to: "physical-network" },
    { from: "fibre-topology", to: "physical-network" },
    { from: "ntn-topology", to: "physical-network" },
    { from: "ntn-topology", to: "user-terminals" },
    { from: "ntn-topology", to: "ground-stations" },
    { from: "ntn-topology", to: "spectrum" },

    { from: "physical-network", to: "ground-stations" },

    // Edge -> satellite platform
    { from: "user-terminals", to: "leo-microsats" },
    { from: "user-terminals", to: "geo-satellites" },
    { from: "ground-stations", to: "leo-microsats" },
    { from: "ground-stations", to: "geo-satellites" },
    { from: "spectrum", to: "space-regulation" },
    { from: "spectrum", to: "leo-microsats" },
    { from: "spectrum", to: "geo-satellites" },

    // Satellite -> subsystems
    { from: "leo-microsats", to: "beamforming" },
    { from: "leo-microsats", to: "sat-antennas" },
    { from: "leo-microsats", to: "optical-isl" },
    { from: "leo-microsats", to: "propulsion" },
    { from: "leo-microsats", to: "thermal" },
    { from: "leo-microsats", to: "sat-power" },
    { from: "geo-satellites", to: "sat-antennas" },
    { from: "geo-satellites", to: "propulsion" },
    { from: "geo-satellites", to: "thermal" },
    { from: "geo-satellites", to: "sat-power" },

    // Satellite -> launch / ops
    { from: "leo-microsats", to: "launchers" },
    { from: "geo-satellites", to: "launchers" },
    { from: "leo-microsats", to: "orbit-tracking" },
    { from: "geo-satellites", to: "orbit-tracking" },
    { from: "leo-microsats", to: "fleet-management" },
    { from: "geo-satellites", to: "fleet-management" },

    // Ops stack
    { from: "orbit-tracking", to: "debris-tracking" },
    { from: "fleet-management", to: "orbit-tracking" },
    { from: "fleet-management", to: "automation" },
    { from: "debris-tracking", to: "automation" },
    { from: "automation", to: "supply-chain" },

    // Regulation cross-cuts launch and orbit
    { from: "launchers", to: "space-regulation" },
    { from: "orbit-tracking", to: "space-regulation" },
    { from: "debris-tracking", to: "space-regulation" },

    // Supply chain underneath hardware
    { from: "launchers", to: "supply-chain" },
    { from: "propulsion", to: "supply-chain" },
    { from: "sat-power", to: "supply-chain" },
    { from: "sat-antennas", to: "supply-chain" },
    { from: "thermal", to: "supply-chain" },
  ],
  evolutions: [
    { componentId: "ntn-topology", toMaturity: 0.48 },
    { componentId: "user-terminals", toMaturity: 0.55 },
    { componentId: "leo-microsats", toMaturity: 0.52 },
    { componentId: "optical-isl", toMaturity: 0.35 },
    { componentId: "beamforming", toMaturity: 0.50 },
    { componentId: "fleet-management", toMaturity: 0.48 },
    { componentId: "debris-tracking", toMaturity: 0.58 },
  ],
  annotations: [
    { id: 1, text: "LEO / NTN frontier: still novel in Feb 2023", x: 0.20, y: 0.78 },
    { id: 2, text: "Commoditised subsystems — buy, do not build", x: 0.82, y: 0.30 },
    { id: 3, text: "Regulation as cross-cutting climate", x: 0.50, y: 0.50 },
  ],
};

// ============================================================
// 4. HELPERS
// ============================================================

function findDependencyChain(componentId, links, direction = "both") {
  const connected = new Set([componentId]);
  let changed = true;
  while (changed) {
    changed = false;
    for (const link of links) {
      if (direction !== "downstream" && connected.has(link.to) && !connected.has(link.from)) {
        connected.add(link.from);
        changed = true;
      }
      if (direction !== "upstream" && connected.has(link.from) && !connected.has(link.to)) {
        connected.add(link.to);
        changed = true;
      }
    }
  }
  return connected;
}

function computeLabelOffsets(components) {
  const offsets = {};
  const positions = components.map((c) => ({
    id: c.id,
    sx: toSvgX(c.maturity),
    sy: toSvgY(c.visibility),
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
        if (sy <= other.sy) {
          dy = -14;
        } else {
          dy = 16;
        }
      }
    }

    if (sx + dx + comp.name.length * 6 > WIDTH - PADDING.right) {
      dx = -(comp.name.length * 6 + 10);
    }
    if (sy + dy < PADDING.top + 10) {
      dy = 14;
    }

    offsets[comp.id] = comp.labelOffset || { dx, dy };
  }
  return offsets;
}

// ============================================================
// 5. MAIN COMPONENT
// ============================================================

export default function WardleyMap() {
  const [hoveredId, setHoveredId] = useState(null);
  const [selectedId, setSelectedId] = useState(null);
  const [tooltipPos, setTooltipPos] = useState({ x: 0, y: 0 });

  const map = MAP;

  const labelOffsets = useMemo(() => computeLabelOffsets(map.components), [map.components]);

  const selectedChain = useMemo(() => {
    if (!selectedId) return null;
    return findDependencyChain(selectedId, map.links);
  }, [selectedId, map.links]);

  const componentMap = useMemo(() => {
    const m = {};
    map.components.forEach((c) => {
      m[c.id] = c;
    });
    return m;
  }, [map.components]);

  const isVisible = useCallback(
    (id) => {
      if (!selectedChain) return true;
      return selectedChain.has(id);
    },
    [selectedChain]
  );

  const isLinkVisible = useCallback(
    (link) => {
      if (!selectedChain) return true;
      return selectedChain.has(link.from) && selectedChain.has(link.to);
    },
    [selectedChain]
  );

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
      {map.purpose && <p className="text-sm text-gray-500 mb-3">{map.purpose}</p>}

      <div className="relative border border-gray-200 rounded bg-white">
        <svg
          viewBox={`0 0 ${WIDTH} ${HEIGHT}`}
          className="w-full h-auto"
          style={{ fontFamily: "'Segoe UI', system-ui, -apple-system, sans-serif" }}
          onClick={() => setSelectedId(null)}
        >
          {/* Layer 1: Stage column fills */}
          {STAGE_LABELS.map((_, i) => {
            const x0 = toSvgX(i === 0 ? 0 : STAGE_BOUNDARIES[i - 1]);
            const x1 = toSvgX(i < STAGE_BOUNDARIES.length ? STAGE_BOUNDARIES[i] : 1);
            return (
              <rect
                key={`stage-bg-${i}`}
                x={x0}
                y={PADDING.top}
                width={x1 - x0}
                height={HEIGHT - PADDING.top - PADDING.bottom}
                fill={COLORS.stageFills[i]}
              />
            );
          })}

          {/* Layer 2: Grid lines */}
          {STAGE_BOUNDARIES.map((b, i) => (
            <line
              key={`grid-${i}`}
              x1={toSvgX(b)}
              y1={PADDING.top}
              x2={toSvgX(b)}
              y2={HEIGHT - PADDING.bottom}
              stroke={COLORS.gridLine}
              strokeDasharray="6 4"
              strokeWidth={1}
            />
          ))}

          {/* Layer 3: Axes */}
          <line
            x1={PADDING.left}
            y1={PADDING.top}
            x2={PADDING.left}
            y2={HEIGHT - PADDING.bottom}
            stroke={COLORS.axisLine}
            strokeWidth={1.5}
          />
          <text x={PADDING.left - 10} y={PADDING.top - 8} textAnchor="middle" fontSize={11} fill={COLORS.axisLabel} fontWeight={500}>
            Visible
          </text>
          <text x={PADDING.left - 10} y={HEIGHT - PADDING.bottom + 18} textAnchor="middle" fontSize={11} fill={COLORS.axisLabel} fontWeight={500}>
            Invisible
          </text>
          <text
            transform={`rotate(-90, ${18}, ${(PADDING.top + HEIGHT - PADDING.bottom) / 2})`}
            x={18}
            y={(PADDING.top + HEIGHT - PADDING.bottom) / 2}
            textAnchor="middle"
            fontSize={12}
            fill={COLORS.axisLabel}
            fontWeight={600}
          >
            Value Chain
          </text>

          <line
            x1={PADDING.left}
            y1={HEIGHT - PADDING.bottom}
            x2={WIDTH - PADDING.right}
            y2={HEIGHT - PADDING.bottom}
            stroke={COLORS.axisLine}
            strokeWidth={1.5}
          />
          {STAGE_LABELS.map((label, i) => {
            const xStart = i === 0 ? 0 : STAGE_BOUNDARIES[i - 1];
            const xEnd = i < STAGE_BOUNDARIES.length ? STAGE_BOUNDARIES[i] : 1;
            const cx = toSvgX((xStart + xEnd) / 2);
            return (
              <text
                key={`stage-label-${i}`}
                x={cx}
                y={HEIGHT - PADDING.bottom + 20}
                textAnchor="middle"
                fontSize={11}
                fill={COLORS.stageLabel}
                fontWeight={500}
              >
                {label}
              </text>
            );
          })}
          <text
            x={(PADDING.left + WIDTH - PADDING.right) / 2}
            y={HEIGHT - PADDING.bottom + 38}
            textAnchor="middle"
            fontSize={12}
            fill={COLORS.axisLabel}
            fontWeight={600}
          >
            Evolution
          </text>

          {/* Layer 5: Dependency lines */}
          <defs>
            <marker
              id="evo-arrow"
              viewBox="0 0 10 10"
              refX={9}
              refY={5}
              markerWidth={6}
              markerHeight={6}
              orient="auto-start-reverse"
              fill={COLORS.evolutionArrow}
            >
              <path d="M 0 0 L 10 5 L 0 10 z" />
            </marker>
          </defs>

          {map.links.map((link, i) => {
            const from = componentMap[link.from];
            const to = componentMap[link.to];
            if (!from || !to) return null;
            const visible = isLinkVisible(link);
            return (
              <path
                key={`link-${i}`}
                d={dependencyPath(from, to)}
                fill="none"
                stroke={COLORS.dependencyLine}
                strokeWidth={1.5}
                opacity={visible ? 0.6 : COLORS.dimmedOpacity}
                style={{ transition: "opacity 0.2s" }}
              />
            );
          })}

          {/* Layer 6: Evolution arrows */}
          {map.evolutions.map((evo, i) => {
            const comp = componentMap[evo.componentId];
            if (!comp) return null;
            const x1 = toSvgX(comp.maturity);
            const x2 = toSvgX(evo.toMaturity);
            const y = toSvgY(comp.visibility);
            const visible = isVisible(comp.id);
            return (
              <line
                key={`evo-${i}`}
                x1={x1 + 8}
                y1={y}
                x2={x2 - 4}
                y2={y}
                stroke={COLORS.evolutionArrow}
                strokeWidth={2}
                strokeDasharray="6 3"
                markerEnd="url(#evo-arrow)"
                opacity={visible ? 0.9 : COLORS.dimmedOpacity}
                style={{ transition: "opacity 0.2s" }}
              />
            );
          })}

          {/* Layer 7: Inertia markers */}
          {map.components
            .filter((c) => c.inertia)
            .map((comp) => {
              const x = toSvgX(comp.maturity);
              const y = toSvgY(comp.visibility);
              const visible = isVisible(comp.id);
              return (
                <g
                  key={`inertia-${comp.id}`}
                  opacity={visible ? 1 : COLORS.dimmedOpacity}
                  style={{ transition: "opacity 0.2s" }}
                >
                  <rect x={x + 9} y={y - 8} width={4} height={16} fill={COLORS.inertiaBar} rx={1} />
                  <rect x={x + 15} y={y - 8} width={4} height={16} fill={COLORS.inertiaBar} rx={1} />
                </g>
              );
            })}

          {/* Layer 8: Components */}
          {map.components.map((comp) => {
            const cx = toSvgX(comp.maturity);
            const cy = toSvgY(comp.visibility);
            const isSelected = selectedId === comp.id;
            const isHovered = hoveredId === comp.id;
            const visible = isVisible(comp.id);
            const offset = labelOffsets[comp.id] || { dx: 10, dy: -12 };

            return (
              <g
                key={comp.id}
                opacity={visible ? 1 : COLORS.dimmedOpacity}
                style={{ transition: "opacity 0.2s", cursor: "pointer" }}
                onMouseEnter={(e) => handleComponentHover(e, comp)}
                onMouseLeave={() => setHoveredId(null)}
                onClick={(e) => {
                  e.stopPropagation();
                  setSelectedId((prev) => (prev === comp.id ? null : comp.id));
                }}
              >
                <circle
                  cx={cx}
                  cy={cy}
                  r={comp.isAnchor ? 8 : 6}
                  fill={COLORS.componentFill}
                  stroke={isSelected || isHovered ? COLORS.componentStrokeSelected : COLORS.componentStroke}
                  strokeWidth={isSelected ? 2.5 : isHovered ? 2.5 : 1.8}
                />
                {comp.isAnchor && <circle cx={cx} cy={cy} r={3} fill={COLORS.componentStroke} />}
                <text
                  x={cx + offset.dx}
                  y={cy + offset.dy}
                  fontSize={11}
                  fontWeight={isSelected || isHovered ? 600 : 500}
                  fill={COLORS.labelText}
                >
                  {comp.name}
                </text>
              </g>
            );
          })}

          {/* Layer 9: Annotations */}
          {(map.annotations || []).map((ann) => {
            const ax = toSvgX(ann.x);
            const ay = toSvgY(ann.y);
            return (
              <g key={`ann-${ann.id}`}>
                <circle cx={ax} cy={ay} r={10} fill="#3b82f6" opacity={0.15} />
                <text x={ax} y={ay + 4} textAnchor="middle" fontSize={10} fontWeight={700} fill="#3b82f6">
                  {ann.id}
                </text>
              </g>
            );
          })}
        </svg>

        {/* Tooltip */}
        {hoveredComp && (
          <div
            className="absolute pointer-events-none z-10 px-3 py-2 rounded shadow-lg text-xs max-w-xs"
            style={{
              left: tooltipPos.x + 16,
              top: tooltipPos.y - 10,
              backgroundColor: COLORS.tooltipBg,
              color: COLORS.tooltipText,
            }}
          >
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
        <div className="text-xs font-semibold text-gray-600 mb-2 uppercase tracking-wide">Figure Legend</div>
        <div className="flex flex-wrap gap-x-6 gap-y-2 text-xs text-gray-600">
          <div className="flex items-center gap-1.5">
            <svg width="16" height="16" viewBox="0 0 16 16">
              <circle cx="8" cy="8" r="5" fill="white" stroke="#333" strokeWidth="1.5" />
            </svg>
            <span>Component</span>
          </div>
          <div className="flex items-center gap-1.5">
            <svg width="16" height="16" viewBox="0 0 16 16">
              <circle cx="8" cy="8" r="6" fill="white" stroke="#333" strokeWidth="1.5" />
              <circle cx="8" cy="8" r="2.5" fill="#333" />
            </svg>
            <span>User / Anchor</span>
          </div>
          <div className="flex items-center gap-1.5">
            <svg width="20" height="16" viewBox="0 0 20 16">
              <line x1="2" y1="8" x2="18" y2="8" stroke="#aaa" strokeWidth="1.5" />
            </svg>
            <span>Dependency</span>
          </div>
          <div className="flex items-center gap-1.5">
            <svg width="24" height="16" viewBox="0 0 24 16">
              <line x1="2" y1="8" x2="18" y2="8" stroke="#d94040" strokeWidth="2" strokeDasharray="5 3" />
              <polygon points="18,4 24,8 18,12" fill="#d94040" />
            </svg>
            <span>Evolution (predicted movement)</span>
          </div>
          <div className="flex items-center gap-1.5">
            <svg width="16" height="16" viewBox="0 0 16 16">
              <rect x="4" y="2" width="3" height="12" fill="#333" rx="1" />
              <rect x="9" y="2" width="3" height="12" fill="#333" rx="1" />
            </svg>
            <span>Inertia (resistance to change)</span>
          </div>
        </div>
        <div className="flex gap-0 mt-2 text-xs">
          {STAGE_LABELS.map((label, i) => (
            <div
              key={i}
              className="flex-1 text-center py-1 border-r last:border-r-0 border-gray-200"
              style={{ backgroundColor: COLORS.stageFills[i] }}
            >
              <span className="text-gray-500 font-medium">{label}</span>
            </div>
          ))}
        </div>
      </div>

      {map.annotations && map.annotations.length > 0 && (
        <div className="mt-2 text-xs text-gray-500">
          {map.annotations.map((ann) => (
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
