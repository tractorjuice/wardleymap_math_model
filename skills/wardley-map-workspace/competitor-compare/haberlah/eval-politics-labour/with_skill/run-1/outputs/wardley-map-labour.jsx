/**
 * Wardley Map React Artifact — UK Labour Party Preparing for Government (May 2024)
 *
 * Generated from the wardley-mapping skill (haberlah/wardley-mapping).
 * Renders an interactive map of Labour's value landscape in the final
 * weeks before the 2024 UK general election, distinguishing the
 * industrialised political machinery from the governing apparatus
 * still being invented.
 */

import { useState, useCallback, useMemo } from "react";

// ============================================================
// CONSTANTS
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
// COORDINATES
// ============================================================

function toSvgX(maturity) {
  return PADDING.left + maturity * (WIDTH - PADDING.left - PADDING.right);
}

function toSvgY(visibility) {
  return PADDING.top + (1 - visibility) * (HEIGHT - PADDING.top - PADDING.bottom);
}

// ============================================================
// MAP DATA — UK Labour Party (May 2024)
// ============================================================

const LABOUR_MAP = {
  title: "UK Labour Party — Preparing for Government (May 2024)",
  purpose:
    "What parts of Labour's political machinery are industrialised versus still being invented in the final weeks before the 2024 general election?",
  components: [
    // Anchors
    { id: "voters", name: "UK Voters", visibility: 0.97, maturity: 0.50, stage: "Product", rationale: "The electorate whose verdict in the 2024 general election is the ultimate user need driving every other component.", isAnchor: true },
    { id: "starmer", name: "Keir Starmer", visibility: 0.95, maturity: 0.58, stage: "Product", rationale: "The leader as a political product: well known, professionally managed, still actively being positioned as a government-ready alternative.", isAnchor: true },
    { id: "members", name: "Labour Members", visibility: 0.93, maturity: 0.42, stage: "Custom-Built", rationale: "A specific, contested constituency whose policy and selection rights are bespoke to this party; expectations differ sharply from voters at large.", isAnchor: true },

    // Visible value proposition
    { id: "victory", name: "Electoral Victory", visibility: 0.88, maturity: 0.45, stage: "Custom-Built", rationale: "Winning a working majority after 14 years of opposition is a one-off, campaign-specific outcome — not a repeatable Product." },
    { id: "trust", name: "Public Trust", visibility: 0.86, maturity: 0.36, stage: "Custom-Built", rationale: "Post-Corbyn, Labour is rebuilding credibility on economy and security; this is actively being constructed voter-by-voter, not a commoditised brand asset." },
    { id: "platform", name: "Policy Platform", visibility: 0.84, maturity: 0.40, stage: "Custom-Built", rationale: "The Five Missions / pre-manifesto platform is still being finalised in May 2024; it is a bespoke political product of this specific leadership." },

    // Campaign / engagement machinery
    { id: "campaign", name: "Campaign Strategy", visibility: 0.78, maturity: 0.58, stage: "Product", rationale: "Professionalised campaign operation under McSweeney using familiar modern GE playbook (target seats, messaging discipline, digital ads, GOTV); multiple vendors and precedents exist." },
    { id: "media", name: "Media Relations", visibility: 0.76, maturity: 0.72, stage: "Product", rationale: "Mature practice across UK parties: press office, briefing cycles, broadcast bid management; approaching utility in its established workflows." },
    { id: "engagement", name: "Public Engagement", visibility: 0.74, maturity: 0.55, stage: "Product", rationale: "Canvassing, hustings and town-halls are a century-old practice; digital engagement layered on top is still evolving but the core is well-understood." },
    { id: "volunteers", name: "Volunteer Mobilisation", visibility: 0.72, maturity: 0.65, stage: "Product", rationale: "Long-established activist model with standard tools (Contact Creator, Ecanvasser-style apps); organisers and training are a commodity skill-set inside the party." },
    { id: "stakeholders", name: "Stakeholder Engagement", visibility: 0.70, maturity: 0.52, stage: "Product", rationale: "Structured engagement with unions, civil society and devolved administrations runs through well-trodden channels, though the balance is being re-set." },
    { id: "fundraising", name: "Fundraising", visibility: 0.68, maturity: 0.68, stage: "Product", rationale: "Regulated donor funnel (affiliated unions, high-value donors, membership) is a codified, multi-vendor practice with clear compliance infrastructure." },
    { id: "private", name: "Private Sector Collaboration", visibility: 0.66, maturity: 0.36, stage: "Custom-Built", rationale: "Starmer/Reeves business charm-offensive, CEO round-tables and the 'partnership with business' framing are an actively invented capability for this iteration of Labour." },

    // Policy apparatus
    { id: "ppframework", name: "Party Policy Framework", visibility: 0.64, maturity: 0.55, stage: "Product", rationale: "Codified machinery (National Policy Forum, Clause V, Conference) with well-defined rules and a long institutional history; clearly in the Product stage." },
    { id: "research", name: "Research & Policy Dev", visibility: 0.60, maturity: 0.42, stage: "Custom-Built", rationale: "In-house policy units plus a bespoke ecosystem of aligned think-tanks (Labour Together, IPPR, Resolution Foundation); recognisable pattern but every leadership re-builds it." },
    { id: "democracy", name: "Internal Party Democracy", visibility: 0.58, maturity: 0.48, stage: "Product", rationale: "Long-established selection, NEC and Conference mechanisms — well-defined Product — but actively contested over candidate selections and rule changes." },

    // Substantive policy areas
    { id: "antidisc", name: "Anti-Discrimination Policy", visibility: 0.55, maturity: 0.56, stage: "Product", rationale: "Mature statutory framework (Equality Act 2010, public-sector equality duty); Labour inherits well-defined delivery mechanics." },
    { id: "nhs", name: "Healthcare Access (NHS)", visibility: 0.52, maturity: 0.64, stage: "Product", rationale: "Vast NHS delivery machinery with standard commissioning, workforce and regulatory apparatus; Labour is inheriting a Product it must reform, not invent." },
    { id: "education", name: "Education Access", visibility: 0.49, maturity: 0.60, stage: "Product", rationale: "Schools, FE, HE funding and regulation run on well-understood levers (DfE, Ofsted, OfS, SFA); Labour's reforms (VAT on fees, breakfast clubs) plug into that Product." },
    { id: "security", name: "National Security", visibility: 0.50, maturity: 0.72, stage: "Commodity", rationale: "Intelligence and defence apparatus (MI5/6, MoD, NSA) is utility-like state infrastructure; policy levers are commoditised across successive governments." },
    { id: "intl", name: "International Relations", visibility: 0.46, maturity: 0.68, stage: "Product", rationale: "FCDO, embassy network and multilateral memberships are a mature Product/utility stack; Labour's variation is positioning and emphasis, not new machinery." },
    { id: "community", name: "Community Programs", visibility: 0.44, maturity: 0.46, stage: "Custom-Built", rationale: "A mix of mature third-sector infrastructure and new Labour-specific programs (e.g. Sure Start revival, youth hubs); the delivery model is still being re-specified." },
    { id: "workers", name: "Workers' Rights (New Deal)", visibility: 0.42, maturity: 0.30, stage: "Custom-Built", rationale: "The New Deal for Working People is a flagship, bespoke policy package (day-one rights, ban on zero-hour exploitation, Fair Work Agency) still being drafted — Custom-Built by design." },
    { id: "econeq", name: "Economic Equality", visibility: 0.40, maturity: 0.22, stage: "Custom-Built", rationale: "Labour's fiscal/tax framing (tight rules + targeted reform) is bespoke to Reeves's approach post-2022; no off-the-shelf delivery pattern from past governments applies." },
    { id: "social", name: "Social Justice", visibility: 0.38, maturity: 0.38, stage: "Custom-Built", rationale: "Umbrella area where Labour is stitching together child poverty, criminal justice, welfare reform and more; delivery vehicles are still in formation." },
    { id: "infra", name: "Infrastructure Development", visibility: 0.36, maturity: 0.50, stage: "Product", rationale: "NSIP regime, planning law and HS2-era delivery models are a recognisable Product; Labour is layering on a National Wealth Fund and planning reform, not replacing the stack." },
    { id: "investment", name: "Public Sector Investment", visibility: 0.34, maturity: 0.34, stage: "Custom-Built", rationale: "Post-austerity capital envelope under new fiscal rules is being freshly designed; departmental spending architecture is stable but the allocation regime is bespoke." },
    { id: "housing", name: "Housing Policy", visibility: 0.32, maturity: 0.26, stage: "Custom-Built", rationale: "Despite decades of debate, the UK has not industrialised housing supply; Labour's '1.5m homes' pledge requires inventing a planning and delivery vehicle that does not yet exist.", inertia: true },
    { id: "climate", name: "Climate Action (GB Energy)", visibility: 0.29, maturity: 0.14, stage: "Genesis", rationale: "GB Energy is a novel publicly-owned investment vehicle — there is no UK precedent; the £28bn Green Prosperity Plan has been scaled back and its delivery shape is still forming." },
    { id: "digital", name: "Digital Transformation", visibility: 0.26, maturity: 0.42, stage: "Custom-Built", rationale: "GDS and departmental digital teams exist (Product) but Labour's ambition for cross-government digital reform, AI adoption and data infrastructure is still a bespoke programme." },

    // Infrastructure / utilities
    { id: "voterdata", name: "Voter Data & Analytics", visibility: 0.18, maturity: 0.72, stage: "Product", rationale: "Electoral roll, Experian/YouGov/Datapraxis-style commercial data services and standard MI tooling (Contact Creator, Campaign Lab) behave as a Product with utility elements." },
    { id: "civilservice", name: "Civil Service Apparatus", visibility: 0.15, maturity: 0.86, stage: "Commodity", rationale: "Permanent, neutral Whitehall machinery is the commodity substrate of any UK government; Labour inherits it at near-zero switching cost on day one." },
    { id: "funding", name: "Funding Infrastructure", visibility: 0.12, maturity: 0.78, stage: "Commodity", rationale: "Donor law, PPERA caps, membership dues collection and union affiliation are commoditised regulatory rails shared across all UK parties." },
    { id: "regulation", name: "Electoral Regulation", visibility: 0.10, maturity: 0.88, stage: "Commodity", rationale: "Electoral Commission, returning officers, ballot logistics and spending limits are utility-grade state infrastructure that every party plugs into." }
  ],
  links: [
    // Anchors -> visible
    { from: "voters", to: "victory" },
    { from: "voters", to: "trust" },
    { from: "voters", to: "platform" },
    { from: "starmer", to: "victory" },
    { from: "starmer", to: "trust" },
    { from: "starmer", to: "platform" },
    { from: "members", to: "platform" },
    { from: "members", to: "democracy" },
    { from: "members", to: "volunteers" },

    // Visible -> campaign / apparatus
    { from: "victory", to: "campaign" },
    { from: "victory", to: "engagement" },
    { from: "trust", to: "media" },
    { from: "trust", to: "stakeholders" },
    { from: "platform", to: "ppframework" },
    { from: "platform", to: "research" },

    // Campaign wiring
    { from: "campaign", to: "media" },
    { from: "campaign", to: "engagement" },
    { from: "campaign", to: "volunteers" },
    { from: "campaign", to: "fundraising" },
    { from: "campaign", to: "voterdata" },
    { from: "engagement", to: "volunteers" },
    { from: "engagement", to: "voterdata" },
    { from: "stakeholders", to: "private" },
    { from: "fundraising", to: "funding" },

    // Policy apparatus wiring
    { from: "ppframework", to: "democracy" },
    { from: "ppframework", to: "research" },
    { from: "research", to: "econeq" },
    { from: "research", to: "workers" },
    { from: "research", to: "antidisc" },
    { from: "research", to: "social" },
    { from: "research", to: "nhs" },
    { from: "research", to: "education" },
    { from: "research", to: "housing" },
    { from: "research", to: "infra" },
    { from: "research", to: "investment" },
    { from: "research", to: "climate" },
    { from: "research", to: "security" },
    { from: "research", to: "intl" },
    { from: "research", to: "digital" },
    { from: "research", to: "community" },

    // Policy -> civil service
    { from: "nhs", to: "civilservice" },
    { from: "education", to: "civilservice" },
    { from: "infra", to: "civilservice" },
    { from: "investment", to: "civilservice" },
    { from: "security", to: "civilservice" },
    { from: "intl", to: "civilservice" },
    { from: "digital", to: "civilservice" },
    { from: "housing", to: "civilservice" },
    { from: "climate", to: "civilservice" },
    { from: "community", to: "civilservice" },
    { from: "workers", to: "civilservice" },
    { from: "econeq", to: "civilservice" },

    // Utilities
    { from: "campaign", to: "regulation" },
    { from: "fundraising", to: "regulation" },
    { from: "media", to: "regulation" },
    { from: "voterdata", to: "regulation" },
    { from: "volunteers", to: "funding" }
  ],
  evolutions: [
    { componentId: "campaign", toMaturity: 0.70 },
    { componentId: "private", toMaturity: 0.55 },
    { componentId: "climate", toMaturity: 0.42 },
    { componentId: "digital", toMaturity: 0.55 },
    { componentId: "housing", toMaturity: 0.42 },
    { componentId: "research", toMaturity: 0.55 },
    { componentId: "infra", toMaturity: 0.58 }
  ],
  annotations: [
    { id: 1, text: "Campaign operation industrialising under McSweeney — nearing Product maturity.", x: 0.42, y: 0.78 },
    { id: 2, text: "Business engagement being actively invented as a governing capability.", x: 0.24, y: 0.66 },
    { id: 3, text: "Climate and housing delivery vehicles are still Custom-Built / Genesis.", x: 0.22, y: 0.32 },
    { id: 4, text: "Governing utilities (civil service, electoral regulation) Labour inherits day one.", x: 0.92, y: 0.15 }
  ]
};

// ============================================================
// HELPERS
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
// COMPONENT
// ============================================================

export default function WardleyMap() {
  const [hoveredId, setHoveredId] = useState(null);
  const [selectedId, setSelectedId] = useState(null);
  const [tooltipPos, setTooltipPos] = useState({ x: 0, y: 0 });

  const map = LABOUR_MAP;

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
          {STAGE_LABELS.map((_, i) => {
            const x0 = toSvgX(i === 0 ? 0 : STAGE_BOUNDARIES[i - 1]);
            const x1 = toSvgX(i < STAGE_BOUNDARIES.length ? STAGE_BOUNDARIES[i] : 1);
            return (
              <rect key={`stage-bg-${i}`} x={x0} y={PADDING.top}
                width={x1 - x0} height={HEIGHT - PADDING.top - PADDING.bottom}
                fill={COLORS.stageFills[i]} />
            );
          })}

          {STAGE_BOUNDARIES.map((b, i) => (
            <line key={`grid-${i}`}
              x1={toSvgX(b)} y1={PADDING.top}
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
              <text key={`stage-label-${i}`} x={cx} y={HEIGHT - PADDING.bottom + 20}
                textAnchor="middle" fontSize={11}
                fill={COLORS.stageLabel} fontWeight={500}>{label}</text>
            );
          })}
          <text x={(PADDING.left + WIDTH - PADDING.right) / 2}
            y={HEIGHT - PADDING.bottom + 38}
            textAnchor="middle" fontSize={12} fill={COLORS.axisLabel} fontWeight={600}>
            Evolution
          </text>

          <defs>
            <marker id="evo-arrow" viewBox="0 0 10 10" refX={9} refY={5}
              markerWidth={6} markerHeight={6}
              orient="auto-start-reverse" fill={COLORS.evolutionArrow}>
              <path d="M 0 0 L 10 5 L 0 10 z" />
            </marker>
          </defs>

          {map.links.map((link, i) => {
            const from = componentMap[link.from];
            const to = componentMap[link.to];
            if (!from || !to) return null;
            const visible = isLinkVisible(link);
            return (
              <path key={`link-${i}`} d={dependencyPath(from, to)} fill="none"
                stroke={COLORS.dependencyLine} strokeWidth={1.5}
                opacity={visible ? 0.7 : COLORS.dimmedOpacity}
                style={{ transition: "opacity 0.2s" }} />
            );
          })}

          {map.evolutions.map((evo, i) => {
            const comp = componentMap[evo.componentId];
            if (!comp) return null;
            const x1 = toSvgX(comp.maturity);
            const x2 = toSvgX(evo.toMaturity);
            const y = toSvgY(comp.visibility);
            const visible = isVisible(comp.id);
            return (
              <line key={`evo-${i}`} x1={x1 + 8} y1={y} x2={x2 - 4} y2={y}
                stroke={COLORS.evolutionArrow} strokeWidth={2} strokeDasharray="6 3"
                markerEnd="url(#evo-arrow)"
                opacity={visible ? 0.9 : COLORS.dimmedOpacity}
                style={{ transition: "opacity 0.2s" }} />
            );
          })}

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
                  <circle cx={cx} cy={cy} r={3} fill={COLORS.componentStroke} />
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

          {(map.annotations || []).map(ann => {
            const ax = toSvgX(ann.x);
            const ay = toSvgY(ann.y);
            return (
              <g key={`ann-${ann.id}`}>
                <circle cx={ax} cy={ay} r={10}
                  fill="#3b82f6" opacity={0.15} />
                <text x={ax} y={ay + 4} textAnchor="middle"
                  fontSize={10} fontWeight={700} fill="#3b82f6">
                  {ann.id}
                </text>
              </g>
            );
          })}
        </svg>

        {hoveredComp && (
          <div
            className="absolute pointer-events-none z-10 px-3 py-2 rounded shadow-lg text-xs max-w-xs"
            style={{
              left: tooltipPos.x + 16,
              top: tooltipPos.y - 10,
              backgroundColor: COLORS.tooltipBg,
              color: COLORS.tooltipText,
            }}>
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
