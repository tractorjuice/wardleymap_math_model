# Wardley Map Analysis: Personal Computing in the Conversational AI Era

A value-chain map of the personal-computing / developer stack at the point where conversational AI is reshaping how software gets built — from the user's need at the top, through applications and devices, into the IDE layer (human-centric and conversational AI+human), component libraries and services, legacy approaches, runtimes (Serverless and LAMP/.Net), large language models and FinOps, operating systems and orchestration, containers, DevOps and legacy architecture, and the cloud compute substrate underneath.

**Strategic question:** *Where has the personal-computing stack commoditised to cloud-and-containers, where are LLMs and conversational IDEs still Genesis/Custom-Built, and what does this mean for how people build software now?*

---

## 1. Interactive React Artifact (`.jsx`)

Paste this into a Claude.ai React artifact. It renders the full interactive map with hover tooltips, click-to-highlight dependency chains, evolution arrows, inertia markers, annotations, and a figure legend.

```jsx
import { useState, useCallback, useMemo } from "react";

// ============================================================
// 1. CONSTANTS
// ============================================================

const WIDTH = 1150;
const HEIGHT = 820;
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
// 2. MAP DATA — Personal Computing in the Conversational AI Era
// ============================================================

const MAP = {
  title: "Personal Computing in the Conversational AI Era",
  purpose: "Where the developer stack has commoditised to cloud-and-containers, where LLMs and conversational IDEs are still Genesis/Custom, and what this means for how people build software.",
  components: [
    { id: "user", name: "User", visibility: 0.97, maturity: 0.50, stage: "Product", isAnchor: true,
      rationale: "The developer / end-user whose need for software drives the value chain. Wants to ship applications that run on their devices." },
    { id: "applications", name: "Applications", visibility: 0.88, maturity: 0.78, stage: "Commodity",
      rationale: "Finished software products are a mature market with app stores, SaaS distribution, and well-understood UX patterns. Users expect apps to 'just work' — classic Commodity signal." },
    { id: "devices", name: "Devices", visibility: 0.85, maturity: 0.88, stage: "Commodity",
      rationale: "PCs, laptops, phones, tablets: fully commoditised hardware. Interchangeable vendors (Apple, Dell, HP, Samsung), transparent pricing, standardised form factors, utility-like purchase behaviour." },
    { id: "conv-ai-ide", name: "Conversational AI IDE", visibility: 0.78, maturity: 0.32, stage: "Custom-Built", inertia: true,
      rationale: "Cursor, GitHub Copilot Chat, Claude Code, Windsurf, Cody, Aider — multiple competing entrants but interaction patterns (inline, chat, agentic) are still unsettled. No dominant vendor, frequent product resets, agent UX evolving weekly. Inertia comes from developer muscle memory in human-centric IDEs." },
    { id: "ide-human", name: "IDE (Human-Centric)", visibility: 0.72, maturity: 0.72, stage: "Product",
      rationale: "VS Code (dominant OSS + Microsoft), JetBrains family (paid), Vim/Emacs (edge). Well-understood market, multiple vendors, feature-based competition. Free tiers are commoditising but paid differentiation still holds." },
    { id: "component-libs", name: "Component Libraries", visibility: 0.62, maturity: 0.88, stage: "Commodity",
      rationale: "npm, PyPI, Maven Central, crates.io, Go modules: ubiquitous, standardised, free, invisible until they break. Package-registry infrastructure is utility-priced and interchangeable at the API level." },
    { id: "services", name: "Services", visibility: 0.58, maturity: 0.76, stage: "Commodity",
      rationale: "Stripe, Auth0, Twilio, SendGrid, Algolia: utility-priced external APIs with standardised contracts. Developers consume without thinking about providers. Switching costs exist but APIs are largely commodified." },
    { id: "legacy-approaches", name: "Legacy Approaches", visibility: 0.52, maturity: 0.48, stage: "Custom-Built", inertia: true,
      rationale: "Older frameworks, build patterns, and dev practices that organisations built years ago and haven't retired. Custom-Built because they're bespoke to each firm, with heavy inertia from sunk-cost investment and trained operators." },
    { id: "llms", name: "Large Language Models", visibility: 0.45, maturity: 0.54, stage: "Product",
      rationale: "OpenAI GPT, Anthropic Claude, Google Gemini, Meta Llama, Mistral: compressed from Genesis (2020) to early Product (2026) in under 4 years. Multiple vendors, token-based pricing, published benchmarks (MMLU, SWE-bench). Still differentiating on capability, so mid-Product, not yet Commodity." },
    { id: "serverless", name: "Serverless Runtime", visibility: 0.44, maturity: 0.68, stage: "Product",
      rationale: "AWS Lambda, Cloudflare Workers, Google Cloud Run, Vercel Functions, Azure Functions: competitive vendor market with overlapping feature sets. Pay-per-invocation pricing, standardised event shapes. Moving toward Commodity as runtimes converge on WASI/edge." },
    { id: "finops", name: "FinOps", visibility: 0.42, maturity: 0.35, stage: "Custom-Built",
      rationale: "FinOps Foundation (2019-) has published a framework; Vantage, CloudZero, Harness, IBM Apptio, Kion emerging as products. But LLM-cost FinOps (per-token attribution, prompt-cost budgeting, caching ROI) is still largely bespoke per organisation — new attack surface not yet productised." },
    { id: "lamp-net", name: "LAMP / .Net Runtime", visibility: 0.40, maturity: 0.85, stage: "Commodity", inertia: true,
      rationale: "Linux/Apache/MySQL/PHP and Microsoft .NET stacks: decades of deployment, exhaustively documented, utility-priced hosting. Commodity by every dimension but carries heavy organisational inertia — shops invested in these stacks resist migration even when serverless would fit better." },
    { id: "orchestration", name: "Orchestration", visibility: 0.33, maturity: 0.72, stage: "Product",
      rationale: "Kubernetes is dominant; managed offerings (EKS, GKE, AKS, OpenShift) commoditising the operator role. Still requires specialists, so mid-to-late Product. Managed control planes pulling it rightward toward Commodity." },
    { id: "os", name: "Operating Systems", visibility: 0.30, maturity: 0.92, stage: "Commodity",
      rationale: "Windows, macOS, Linux distributions (Ubuntu, RHEL, Alpine, Debian): fully standardised, POSIX/Win32 are stable APIs, invisible to end-users, catastrophic if they fail — textbook Commodity." },
    { id: "containers", name: "Containers", visibility: 0.22, maturity: 0.88, stage: "Commodity",
      rationale: "Docker + OCI standard: universal container format, transparent build pipelines, fully interchangeable runtimes (containerd, CRI-O, Podman). Utility behaviour, invisible until broken. Foundation of cloud-native deployment." },
    { id: "devops", name: "DevOps", visibility: 0.18, maturity: 0.70, stage: "Product",
      rationale: "GitHub Actions, GitLab CI, CircleCI, Jenkins, Argo CD, Flux: competitive market with published comparisons, standard pipeline primitives, certifications. Moving toward Commodity as GitOps and managed runners proliferate. Positioned at the lower layer because the scenario treats DevOps as infrastructure-facing delivery plumbing." },
    { id: "legacy-arch", name: "Legacy Architecture", visibility: 0.16, maturity: 0.62, stage: "Product", inertia: true,
      rationale: "Monoliths, VM-first deployments, on-prem-shaped designs: well-understood Product-stage architecture with severe inertia from 20+ years of sunk investment. Cheapest path of least resistance for many shops, hence it persists alongside cloud-native." },
    { id: "cloud", name: "Compute (Cloud)", visibility: 0.08, maturity: 0.92, stage: "Commodity",
      rationale: "AWS, GCP, Azure, plus second-tier (Oracle, Alibaba, OVH, Hetzner): utility-priced compute, transparent per-second pricing, interchangeable at the IaaS level for most workloads. Catastrophic when it fails (e.g. regional AWS outages making front-page news) — canonical Commodity." }
  ],
  links: [
    { from: "user", to: "applications" },
    { from: "user", to: "devices" },
    { from: "applications", to: "ide-human" },
    { from: "applications", to: "conv-ai-ide" },
    { from: "applications", to: "component-libs" },
    { from: "applications", to: "services" },
    { from: "applications", to: "legacy-approaches" },
    { from: "applications", to: "devops" },
    { from: "devices", to: "os" },
    { from: "conv-ai-ide", to: "ide-human" },
    { from: "conv-ai-ide", to: "llms" },
    { from: "conv-ai-ide", to: "component-libs" },
    { from: "ide-human", to: "component-libs" },
    { from: "ide-human", to: "services" },
    { from: "ide-human", to: "devops" },
    { from: "component-libs", to: "serverless" },
    { from: "component-libs", to: "lamp-net" },
    { from: "services", to: "serverless" },
    { from: "services", to: "lamp-net" },
    { from: "services", to: "devops" },
    { from: "legacy-approaches", to: "lamp-net" },
    { from: "legacy-approaches", to: "legacy-arch" },
    { from: "llms", to: "finops" },
    { from: "llms", to: "cloud" },
    { from: "serverless", to: "containers" },
    { from: "serverless", to: "cloud" },
    { from: "lamp-net", to: "os" },
    { from: "lamp-net", to: "containers" },
    { from: "finops", to: "cloud" },
    { from: "orchestration", to: "os" },
    { from: "orchestration", to: "containers" },
    { from: "orchestration", to: "cloud" },
    { from: "os", to: "cloud" },
    { from: "containers", to: "cloud" },
    { from: "devops", to: "cloud" },
    { from: "legacy-arch", to: "cloud" }
  ],
  evolutions: [
    { componentId: "conv-ai-ide", toMaturity: 0.55 },
    { componentId: "llms", toMaturity: 0.72 },
    { componentId: "finops", toMaturity: 0.58 },
    { componentId: "orchestration", toMaturity: 0.85 }
  ],
  annotations: [
    { id: 1, text: "Conversational IDE + LLMs: the new Genesis/Custom frontier", x: 0.28, y: 0.82 },
    { id: 2, text: "Evolution compression: LLMs moving Custom->Commodity in ~4 years", x: 0.60, y: 0.54 },
    { id: 3, text: "Inertia cluster: legacy approaches, runtimes, and architecture resist movement", x: 0.55, y: 0.25 },
    { id: 4, text: "Commoditised substrate: cloud, containers, OS, DevOps as unified utility", x: 0.80, y: 0.12 }
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
      if (distX < 80 && distY < 22) {
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
title Personal Computing in the Conversational AI Era
style wardley

anchor User [0.97, 0.50]

component Applications [0.88, 0.78]
component Devices [0.85, 0.88]
component Conversational AI IDE [0.78, 0.32] inertia
component IDE (Human-Centric) [0.72, 0.72]
component Component Libraries [0.62, 0.88]
component Services [0.58, 0.76]
component Legacy Approaches [0.52, 0.48] inertia
component Large Language Models [0.45, 0.54]
component Serverless Runtime [0.44, 0.68]
component FinOps [0.42, 0.35]
component LAMP / .Net Runtime [0.40, 0.85] inertia
component Orchestration [0.33, 0.72]
component Operating Systems [0.30, 0.92]
component Containers [0.22, 0.88]
component DevOps [0.18, 0.70]
component Legacy Architecture [0.16, 0.62] inertia
component Compute (Cloud) [0.08, 0.92]

User->Applications
User->Devices
Applications->IDE (Human-Centric)
Applications->Conversational AI IDE
Applications->Component Libraries
Applications->Services
Applications->Legacy Approaches
Applications->DevOps
Devices->Operating Systems
Conversational AI IDE->IDE (Human-Centric)
Conversational AI IDE->Large Language Models
Conversational AI IDE->Component Libraries
IDE (Human-Centric)->Component Libraries
IDE (Human-Centric)->Services
IDE (Human-Centric)->DevOps
Component Libraries->Serverless Runtime
Component Libraries->LAMP / .Net Runtime
Services->Serverless Runtime
Services->LAMP / .Net Runtime
Services->DevOps
Legacy Approaches->LAMP / .Net Runtime
Legacy Approaches->Legacy Architecture
Large Language Models->FinOps
Large Language Models->Compute (Cloud)
Serverless Runtime->Containers
Serverless Runtime->Compute (Cloud)
LAMP / .Net Runtime->Operating Systems
LAMP / .Net Runtime->Containers
FinOps->Compute (Cloud)
Orchestration->Operating Systems
Orchestration->Containers
Orchestration->Compute (Cloud)
Operating Systems->Compute (Cloud)
Containers->Compute (Cloud)
DevOps->Compute (Cloud)
Legacy Architecture->Compute (Cloud)

evolve Conversational AI IDE 0.55
evolve Large Language Models 0.72
evolve FinOps 0.58
evolve Orchestration 0.85

annotation 1 [[0.82, 0.28]] Conversational IDE + LLMs: the new Genesis/Custom frontier
annotation 2 [[0.54, 0.60]] Evolution compression: LLMs moving Custom->Commodity in ~4 years
annotation 3 [[0.25, 0.55]] Inertia cluster: legacy approaches, runtimes, and architecture resist movement
annotation 4 [[0.12, 0.80]] Commoditised substrate: cloud, containers, OS, DevOps as unified utility
```

---

## 3. Strategic Commentary

### Purpose

Answer: **where has the personal-computing / developer stack commoditised to cloud-and-containers, where are conversational AI IDEs and LLMs still Genesis/Custom-Built, and what does this mean for how people build software now?**

The map shows a stack split into three distinct regions: a **commoditised substrate** (bottom-right quadrant: cloud, containers, OS, DevOps, LAMP/.Net runtime), a **productised middle** (IDE-human, services, libraries, serverless, orchestration, applications, devices), and a **Genesis/Custom-Built frontier** (top-left: Conversational AI IDE, FinOps, LLMs straddling the Custom–Product boundary). Inertia is concentrated in four places: the Conversational AI IDE (developer habits), Legacy Approaches, LAMP/.Net, and Legacy Architecture — all components that resist movement despite market pressure.

### Component Evolution Assessment

| Component | Stage | Position [vis, mat] | Rationale |
|---|---|---|---|
| User | Anchor | [0.97, 0.50] | The developer / end-user whose need for software drives the chain. |
| Applications | Commodity | [0.88, 0.78] | Mature market (app stores, SaaS), standardised UX, utility-like consumption. |
| Devices | Commodity | [0.85, 0.88] | PCs/laptops/phones; interchangeable vendors, transparent pricing. |
| Conversational AI IDE | Custom-Built | [0.78, 0.32] (+inertia) | Cursor, Copilot Chat, Claude Code, Windsurf, Cody — competing entrants, unstable UX patterns, weekly resets. Inertia from human-IDE muscle memory. |
| IDE (Human-Centric) | Product | [0.72, 0.72] | VS Code dominant, JetBrains paid, Vim/Emacs edge. Mature feature competition. |
| Component Libraries | Commodity | [0.62, 0.88] | npm/PyPI/Maven/crates: ubiquitous, utility-priced registry infrastructure. |
| Services | Commodity | [0.58, 0.76] | Stripe/Auth0/Twilio/SendGrid/Algolia — utility APIs, standardised contracts. |
| Legacy Approaches | Custom-Built | [0.52, 0.48] (+inertia) | Bespoke per firm, decades of sunk cost, no off-the-shelf replacement. |
| Large Language Models | Product | [0.45, 0.54] | OpenAI/Anthropic/Google/Meta/Mistral. Compressed Genesis→Product in under 4 years; still differentiating on capability. |
| Serverless Runtime | Product | [0.44, 0.68] | Lambda, Workers, Cloud Run, Vercel, Azure Functions — competitive market, pay-per-invocation. |
| FinOps | Custom-Built | [0.42, 0.35] | Framework exists (FinOps Foundation); LLM-cost FinOps largely bespoke. |
| LAMP / .Net Runtime | Commodity | [0.40, 0.85] (+inertia) | Decades of deployment, fully documented; heavy organisational inertia blocks migration. |
| Orchestration | Product | [0.33, 0.72] | Kubernetes dominant; managed offerings (EKS/GKE/AKS) commoditising. |
| Operating Systems | Commodity | [0.30, 0.92] | Windows/macOS/Linux; POSIX/Win32 stable, invisible, catastrophic when broken. |
| Containers | Commodity | [0.22, 0.88] | Docker + OCI standard, interchangeable runtimes, utility behaviour. |
| DevOps | Product | [0.18, 0.70] | GitHub Actions/GitLab/CircleCI/Jenkins/Argo — competitive, standardising. |
| Legacy Architecture | Product | [0.16, 0.62] (+inertia) | Monoliths/VM-first/on-prem. Well-understood Product but severe sunk-cost inertia. |
| Compute (Cloud) | Commodity | [0.08, 0.92] | AWS/GCP/Azure: utility pricing, transparent, interchangeable IaaS. |

### Key Strategic Observations

1. **The new Genesis frontier is interactional, not infrastructural.** For the first time since mobile, the Genesis/Custom-Built stuff is *directly user-facing* (Conversational AI IDEs at 0.32 maturity) rather than buried in infrastructure. Where novel technology used to emerge from the bottom of the stack (containers, cloud, Kubernetes) and slowly climb up, conversational AI is erupting at the *top* of the developer value chain while the substrate below it was already commoditised. This inverts the usual evolution geometry.

2. **Evolution compression is pulling two components across stages in real time.** LLMs have traversed Genesis → Custom → early Product in under four years (arrow at 0.54 → 0.72). Conversational AI IDEs are following at speed (0.32 → 0.55). This is the compression effect — what took compute 30 years (servers → cloud) takes AI-driven components single-digit years. Evolution predictions must assume these arrows will *overshoot* standard timelines.

3. **The commoditised substrate is unusually deep and unified.** Cloud (0.92), OS (0.92), Containers (0.88), Libraries (0.88), Devices (0.88), LAMP/.Net (0.85), Applications (0.78), Services (0.76), Orchestration (0.72), DevOps (0.70): ten of seventeen non-anchor components sit at ≥0.70 maturity. This is what "commoditised to cloud-and-containers" looks like on a map — the entire bottom half plus the app and library layers are utility-like. Any competitive advantage built below this line is negligible.

4. **Inertia is structural, not random.** Four inertia markers cluster on a diagonal: Conversational AI IDE (top), Legacy Approaches (middle), LAMP/.Net (middle-bottom), Legacy Architecture (bottom). The top one is *pre-productisation inertia* (developer habits predating mature AI tools); the bottom three are *post-commoditisation inertia* (sunk-cost resistance to adopting more-evolved alternatives). Two different phenomena, same visual marker — strategically they require different responses.

5. **FinOps is the hidden Custom-Built bottleneck in the AI stack.** At 0.35 maturity with an arrow to 0.58, FinOps is the management layer that makes per-token LLM costs legible. It's the only Custom-Built component in the infrastructure band that doesn't have strong inertia — meaning it will move rightward fast when tooling matures. Organisations that wait for FinOps products to arrive will have been running blind on LLM spend for years.

### Doctrine Check

- **Focus on user needs** — The anchor is the user; the top of the chain (Applications, Devices, IDEs) directly reflects user needs. Clear.
- **Use appropriate methods** — *Concern flagged.* If an organisation is applying Commodity methods (Six Sigma, ITIL, outsourcing) to Genesis-stage Conversational AI IDE adoption, or conversely applying Genesis/agile methods to Commodity cloud ops, they have a method-evolution mismatch.
- **Remove duplication and bias** — The stack is lopsided toward Commodity (ten components at ≥0.70 maturity). This bias is accurate for personal computing in 2026, but flags that organisations overweighting "build on commodity" may starve the Genesis/Custom frontier of investment — the exact opposite of where differentiation now lives.
- **Think small teams** — Conversational AI IDE and FinOps are at Pioneer-team scale (small, experimental). The commoditised substrate should be consumed by Town Planner teams. Orchestration and Services are Settler territory (productising).
- **Be wary of cognitive biases** — The "we've always used LAMP" inertia is a clear example of bias. The LAMP/.Net node at 0.85 maturity with inertia is textbook: commodity technology being held as if it were custom-built because of organisational attachment.

### Recommended Actions

1. **Pilot Conversational AI IDEs for net-new greenfield work immediately; do not mandate a single vendor.** The category is at 0.32 maturity. Dominant vendor isn't decided. Running parallel pilots (e.g., Claude Code + Cursor + Copilot) lets teams learn the interaction patterns before committing. Expect to re-tool every 6-12 months through 2027 as the category matures.

2. **Treat LLMs as a purchased commodity, not a custom capability.** At 0.54 maturity with arrow to 0.72, LLMs are Product-stage. Do not train foundation models. Do consume multiple providers behind an abstraction layer (LiteLLM, Portkey) — provider swap cost will drop as the category commoditises.

3. **Build FinOps tooling now, before LLM spend scales.** At 0.35 maturity with rightward arrow, FinOps is the one place where building-ahead-of-product pays off. Per-token attribution, cache-hit measurement, and prompt-cost budgeting are table-stakes that existing SaaS vendors haven't productised yet. Custom-build a thin layer on top of cloud billing + LLM provider APIs; replace with a managed product in 12-18 months when Vantage/CloudZero/Harness close the gap.

4. **Retire LAMP/.Net where inertia is the only remaining reason to keep it.** At 0.85 maturity, these runtimes are commodity. If the only argument for keeping them is "we have expertise", that's sunk-cost inertia, not strategy. Migrate to Serverless + containers on cloud for new services; maintain LAMP/.Net only where regulatory or integration constraints demand it.

5. **Invest in the Conversational IDE ↔ DevOps integration seam.** Applications now depend on *both* Conversational AI IDE (0.32) and DevOps (0.70). The glue between them — AI-authored code → tests → PR → CI → deploy — is where productivity compounds. Standardise this pipeline (AI review bots, automated PR quality gates, LLM-cost budgets in CI) before individual developers invent fifty incompatible variants.

### Build vs. Buy Assessment (AI-Era Adjusted)

| Component | Stage | Recommendation | Rationale |
|---|---|---|---|
| Conversational AI IDE | Custom-Built | **Buy (per developer, multi-vendor)** | Dozens of competing products exist. No need to build your own. Pilot multiple; let developers choose. |
| Large Language Models | Product | **Buy (API, multi-provider)** | OpenAI/Anthropic/Google/Mistral APIs. Multi-provider abstraction layer is cheap to build. |
| FinOps | Custom-Built | **Build thin layer now; buy later** | Product vendors will catch up in 12-18 months. Build minimum viable internal dashboard today; plan migration. |
| Serverless Runtime | Product | **Buy (cloud-native)** | Mature market. No differentiation in running your own serverless platform. |
| LAMP / .Net Runtime | Commodity | **Buy or retire** | Commodity hosting is cheap. Retire where inertia is the only reason to keep it. |
| Orchestration | Product | **Buy managed (EKS/GKE/AKS)** | Unless you have Kubernetes-platform-as-a-business as your product, consume managed. |
| Operating Systems | Commodity | **Buy (distro + cloud image)** | No one builds their own OS outside of cloud providers and embedded niches. |
| Containers | Commodity | **Buy (OCI standard)** | Docker/OCI is free and universal. |
| DevOps | Product | **Buy (GitHub/GitLab/managed CI)** | Mature Product market. Self-hosted CI is inertia. |
| Compute (Cloud) | Commodity | **Buy (utility)** | AWS/GCP/Azure. Non-negotiable for most new workloads. |
| Component Libraries | Commodity | **Consume (free registries)** | npm/PyPI/Maven. Use them; don't mirror unless compliance requires it. |
| Services | Commodity | **Buy (API subscriptions)** | Stripe/Auth0/Twilio — utility-priced. Reinvention is waste. |
| Legacy Approaches | Custom-Built | **Retire over 24 months** | Inertia-driven custom. Replace with Product-stage equivalents. |
| Legacy Architecture | Product (+inertia) | **Migrate incrementally** | Strangler-fig onto cloud-native where economics justify; don't rewrite rigidly. |

### Evolution Predictions (12-24 months)

- **Conversational AI IDE → early Product (0.32 → 0.55).** One or two vendors will consolidate market share. Agent-style IDEs (Claude Code, Cursor Agent) will stabilise a standard interaction pattern. Expect inertia markers to weaken as second-generation developers trained on these tools enter the workforce.
- **LLMs → late Product / early Commodity (0.54 → 0.72).** Token pricing will converge across providers; capability gaps will narrow. Enterprise APIs (compliance, SSO, VPC integration) will become table stakes. The differentiation will shift from "which model is smartest" to "which model is cheapest at equal utility".
- **FinOps → Product (0.35 → 0.58).** Vantage/CloudZero/Harness/IBM-Apptio will publish LLM-cost SKUs; cloud providers will embed per-token billing analytics natively. The Custom-Built gap closes.
- **Orchestration → Commodity (0.72 → 0.85).** Managed K8s commoditising to the point where "running Kubernetes" is like "running a database" — purchased, not operated. Serverless/K8s hybrid platforms (ECS/Fargate, GKE Autopilot, Fly.io) further compress the layer.
- **Conversational AI IDE outpaces the others.** The compression effect (Genesis→Product in 3-5 years) suggests this arrow is the *most likely to be underestimated*. If it hits 0.60 by end-2027, a second wave of interaction disruption (multi-agent, voice-first, ambient) will already be emerging at the new Genesis frontier.

### What This Means for How People Build Software

The map collapses the answer to the scenario question into four points:

- **The stack from the cloud up to the application layer is finished as a source of competitive advantage.** Everything at or above 0.70 maturity is utility. Don't build substitutes.
- **The new Genesis/Custom frontier is how developers interact with the stack, not what the stack is made of.** Conversational AI IDEs and the LLMs they depend on are where the next 5-year moat forms — in interaction patterns, agent orchestration, context-engineering practices, and LLM-cost control (FinOps).
- **Inertia is the dominant strategic risk.** Four inertia markers in one map is a warning. The Legacy Approaches → LAMP/.Net → Legacy Architecture diagonal is exactly the path that gets out-competed by AI-built alternatives ("shadow build" pattern): a competitor with AI IDEs and managed runtimes can replicate your legacy functionality in weeks while your migration plan is still in slide review.
- **Build posture inverts at the Custom-Built boundary.** AI-era economics make prototyping cheap, so for any Product-stage SaaS dependency costing real money, run an AI-built prototype first before renewing. But at Commodity (cloud, containers, OS, DevOps, services), still buy — AI doesn't change the economics of utility consumption.

### Open Questions

1. **Will Conversational AI IDEs consolidate into one dominant vendor, or will the market remain plural like human IDEs (VS Code + JetBrains + niche)?** If plural, lock-in risk is low and multi-vendor is the right posture. If single-winner, early adoption of that vendor compounds.
2. **Does LLM FinOps merge into existing cloud FinOps, or become its own category?** If it merges, buy existing FinOps tools and wait. If it stands alone, building a dedicated LLM-cost tool now may become a product in itself.
3. **At what maturity do conversational IDEs + LLM agents absorb DevOps?** If an agent can author, test, PR, review, and deploy autonomously, the DevOps Product-stage category may compress into the IDE layer — changing the dependency shape of this entire map.
