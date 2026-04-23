# Wardley Map Analysis: Clinical Decision Making in Healthcare (August 2022)

## Strategic Context (Step 1 — answered from the scenario)

- **Strategic question**: Where in the clinical-decision value chain is *bespoke judgement* being defended (and why), versus where it is being *industrialised* — and what does that imply for investment, governance, and the rules around fairness and exceptions?
- **User anchors**: four in tension — the **Patient** (who owns the ailment and the outcome), the **Medical Practitioner** (who owns the judgement), the **Medical Institution** (which owns the setting and the guidelines), and the **Payer** (who owns the permissibility and the cost side). Wardley maps allow multiple anchors, and in healthcare they pull the value chain in different directions — which is exactly the tension the map needs to surface.
- **Core needs**: (a) translate an ailment into an appropriate treatment, (b) produce a measurable clinical outcome, (c) deliver care within permissible, auditable rules, (d) handle exceptions fairly.
- **Scope boundary**: a single healthcare system (e.g. a national health service or a large integrated payer-provider), mid-2022 — i.e. before the GPT-4-era diffusion of clinical LLMs is baked in. Where August-2022 matters I note it explicitly below.

---

## Three Deliverables

### 1. Interactive React artifact

The `.jsx` component below renders the map inline with SVG, hover tooltips showing the evolution rationale for each component, click-to-highlight dependency chains, a professional figure legend with evolution-stage shading, and dashed evolution arrows for the four components expected to move rightward over the next 12-24 months.

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
  title: "Clinical Decision Making in Healthcare (Aug 2022)",
  purpose: "Where is bespoke judgement defended, where is the process industrialised, and where do fairness and exceptions sit?",
  components: [
    { id: "patient", name: "Patient", visibility: 0.97, maturity: 0.46, stage: "Product", rationale: "The person with the ailment and the outcome. Well-defined role; rights and expectations are codified in patient-charter legislation across most health systems.", isAnchor: true },
    { id: "practitioner", name: "Medical Practitioner", visibility: 0.93, maturity: 0.36, stage: "Custom-Built", rationale: "Licensed individual clinicians. Expert role, high variability per specialism and per case; training is standardised but day-to-day judgement is bespoke.", isAnchor: true },
    { id: "institution", name: "Medical Institution", visibility: 0.90, maturity: 0.58, stage: "Product", rationale: "Hospitals, clinics, GP practices. Long-established institutional form with multiple operating models (NHS trust, HMO, integrated delivery network, private hospital group).", isAnchor: true },
    { id: "payer", name: "Payer", visibility: 0.86, maturity: 0.70, stage: "Commodity", rationale: "Insurers, national health funds, single-payer bodies. Financial rails are highly standardised; claims processing is utility-grade.", isAnchor: true },
    { id: "treatment-decision", name: "Treatment Decision", visibility: 0.80, maturity: 0.38, stage: "Custom-Built", rationale: "The moment an ailment becomes a treatment plan. Still case-by-case clinician judgement for anything non-trivial; shared decision-making frameworks exist but are inconsistently applied." },
    { id: "care-setting", name: "Care Setting", visibility: 0.76, maturity: 0.52, stage: "Product", rationale: "Primary care, outpatient, inpatient, specialist, home, telehealth. The typology is well understood and patients flow through defined transitions — but patient-specific pathway choice is still bespoke." },
    { id: "outcome", name: "Measured Outcome", visibility: 0.72, maturity: 0.62, stage: "Product", rationale: "PROMs, mortality, readmission, quality-adjusted life years. Measurement frameworks are mature (ICHOM, CMS, NICE) but selection and interpretation remain contested." },
    { id: "dx-reasoning", name: "Diagnostic Reasoning", visibility: 0.68, maturity: 0.30, stage: "Custom-Built", rationale: "The clinician's mental model: hypothesis generation, differential diagnosis, Bayesian updating under uncertainty. Tacit knowledge, tutored one-to-one in training. Inertia: protected scope of practice.", inertia: true },
    { id: "cds", name: "Clinical Decision Support", visibility: 0.60, maturity: 0.44, stage: "Product", rationale: "UpToDate, DynaMed, Epic order sets, sepsis alerts. Multiple commercial and in-house CDS products exist; adoption is widespread but trust and alert-fatigue remain issues. Inertia: override culture and liability risk.", inertia: true },
    { id: "guidelines", name: "Clinical Guidelines", visibility: 0.54, maturity: 0.66, stage: "Product", rationale: "NICE, USPSTF, WHO, specialty-society guidelines. Well-codified publication process; multiple competing guideline bodies, frequent revisions. Inertia: slow update cycle vs new evidence.", inertia: true },
    { id: "formulary", name: "Permissible Treatments Formulary", visibility: 0.50, maturity: 0.76, stage: "Commodity", rationale: "Drug formularies, covered-procedures lists, prior-authorisation rules. Near-utility: standardised codes (BNF, ATC), regular publication cycles, competitive PBM market." },
    { id: "exceptions", name: "Exception & Appeals Rules", visibility: 0.46, maturity: 0.28, stage: "Custom-Built", rationale: "Off-formulary approval, individual-funding requests, compassionate use. Process exists but substance of each case is bespoke and adversarial; outcomes vary widely by payer, postcode, and advocate." },
    { id: "fairness", name: "Fairness & Equity Controls", visibility: 0.42, maturity: 0.20, stage: "Custom-Built", rationale: "Health-equity dashboards, disparities monitoring, algorithmic-fairness audits on CDS. Near-Genesis: frameworks exist (e.g. NHS Core20PLUS5 launched 2021) but implementation is early and non-uniform." },
    { id: "history-exam", name: "Patient History & Examination", visibility: 0.38, maturity: 0.55, stage: "Product", rationale: "The structured clinical interview and physical exam. Methodology is taught to a standard; templates and structured-data capture in EHRs have industrialised a large slice of it." },
    { id: "tests-imaging", name: "Diagnostic Tests & Imaging", visibility: 0.32, maturity: 0.78, stage: "Commodity", rationale: "Pathology, radiology, genomic panels. Commoditised production with standardised pricing and outsourced operations; AI read-assist is shifting some modalities further right." },
    { id: "ehr", name: "Electronic Health Record", visibility: 0.26, maturity: 0.70, stage: "Commodity", rationale: "Epic, Cerner (now Oracle Health), NHS SCR, TPP. Near-universal in OECD systems by 2022; switching costs high but the category itself is commoditised infrastructure." },
    { id: "trials", name: "Clinical Trials & Reviews", visibility: 0.22, maturity: 0.42, stage: "Product", rationale: "RCTs, Cochrane reviews, post-market surveillance. Process is mature and regulated; per-trial design remains bespoke and expensive." },
    { id: "evidence", name: "Evidence Base & Literature", visibility: 0.18, maturity: 0.58, stage: "Product", rationale: "PubMed, Cochrane Library, preprint servers. Well-indexed, widely accessible; quality and reproducibility are recognised as uneven." },
    { id: "coding", name: "Coding & Billing Standards", visibility: 0.12, maturity: 0.85, stage: "Commodity", rationale: "ICD-10, SNOMED CT, CPT, HL7, FHIR. Ubiquitous standardised taxonomies and wire formats; FHIR R4 (2019) now the default interop baseline." },
    { id: "compute", name: "Connectivity & Compute", visibility: 0.06, maturity: 0.90, stage: "Commodity", rationale: "Cloud infrastructure, HIPAA/GDPR-compliant hosting, connectivity. Utility-priced, standardised APIs, invisible until it breaks." },
  ],
  links: [
    { from: "patient", to: "treatment-decision" },
    { from: "patient", to: "outcome" },
    { from: "patient", to: "care-setting" },
    { from: "practitioner", to: "treatment-decision" },
    { from: "practitioner", to: "dx-reasoning" },
    { from: "institution", to: "care-setting" },
    { from: "institution", to: "guidelines" },
    { from: "payer", to: "formulary" },
    { from: "payer", to: "outcome" },
    { from: "payer", to: "exceptions" },
    { from: "treatment-decision", to: "dx-reasoning" },
    { from: "treatment-decision", to: "cds" },
    { from: "treatment-decision", to: "formulary" },
    { from: "treatment-decision", to: "exceptions" },
    { from: "treatment-decision", to: "fairness" },
    { from: "dx-reasoning", to: "cds" },
    { from: "dx-reasoning", to: "history-exam" },
    { from: "dx-reasoning", to: "tests-imaging" },
    { from: "cds", to: "guidelines" },
    { from: "cds", to: "ehr" },
    { from: "guidelines", to: "evidence" },
    { from: "guidelines", to: "trials" },
    { from: "formulary", to: "trials" },
    { from: "formulary", to: "coding" },
    { from: "outcome", to: "ehr" },
    { from: "outcome", to: "coding" },
    { from: "history-exam", to: "ehr" },
    { from: "tests-imaging", to: "ehr" },
    { from: "ehr", to: "compute" },
    { from: "trials", to: "evidence" },
    { from: "coding", to: "compute" },
    { from: "care-setting", to: "ehr" },
  ],
  evolutions: [
    { componentId: "cds", toMaturity: 0.62 },
    { componentId: "dx-reasoning", toMaturity: 0.48 },
    { componentId: "ehr", toMaturity: 0.82 },
    { componentId: "fairness", toMaturity: 0.42 },
  ],
  annotations: [
    { id: 1, text: "Bespoke judgement cluster: reasoning, exceptions, fairness — where clinician and patient autonomy sits", x: 0.22, y: 0.28 },
    { id: 2, text: "Industrialised cluster: formulary, coding, EHR, compute — the rails on which the system runs", x: 0.82, y: 0.18 },
    { id: 3, text: "Build-vs-buy frontier: CDS is consolidating into a Product category; in-house CDS is increasingly hard to justify", x: 0.52, y: 0.58 },
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
title Clinical Decision Making in Healthcare (Aug 2022)
style wardley

anchor Patient [0.97, 0.46]
anchor Medical Practitioner [0.93, 0.36]
anchor Medical Institution [0.90, 0.58]
anchor Payer [0.86, 0.70]

component Treatment Decision [0.80, 0.38]
component Care Setting [0.76, 0.52]
component Measured Outcome [0.72, 0.62]
component Diagnostic Reasoning [0.68, 0.30] inertia
component Clinical Decision Support [0.60, 0.44] inertia
component Clinical Guidelines [0.54, 0.66] inertia
component Permissible Treatments Formulary [0.50, 0.76]
component Exception & Appeals Rules [0.46, 0.28]
component Fairness & Equity Controls [0.42, 0.20]
component Patient History & Examination [0.38, 0.55]
component Diagnostic Tests & Imaging [0.32, 0.78]
component Electronic Health Record [0.26, 0.70]
component Clinical Trials & Reviews [0.22, 0.42]
component Evidence Base & Literature [0.18, 0.58]
component Coding & Billing Standards [0.12, 0.85]
component Connectivity & Compute [0.06, 0.90]

Patient->Treatment Decision
Patient->Measured Outcome
Patient->Care Setting
Medical Practitioner->Treatment Decision
Medical Practitioner->Diagnostic Reasoning
Medical Institution->Care Setting
Medical Institution->Clinical Guidelines
Payer->Permissible Treatments Formulary
Payer->Measured Outcome
Payer->Exception & Appeals Rules
Treatment Decision->Diagnostic Reasoning
Treatment Decision->Clinical Decision Support
Treatment Decision->Permissible Treatments Formulary
Treatment Decision->Exception & Appeals Rules
Treatment Decision->Fairness & Equity Controls
Diagnostic Reasoning->Clinical Decision Support
Diagnostic Reasoning->Patient History & Examination
Diagnostic Reasoning->Diagnostic Tests & Imaging
Clinical Decision Support->Clinical Guidelines
Clinical Decision Support->Electronic Health Record
Clinical Guidelines->Evidence Base & Literature
Clinical Guidelines->Clinical Trials & Reviews
Permissible Treatments Formulary->Clinical Trials & Reviews
Permissible Treatments Formulary->Coding & Billing Standards
Measured Outcome->Electronic Health Record
Measured Outcome->Coding & Billing Standards
Patient History & Examination->Electronic Health Record
Diagnostic Tests & Imaging->Electronic Health Record
Electronic Health Record->Connectivity & Compute
Clinical Trials & Reviews->Evidence Base & Literature
Coding & Billing Standards->Connectivity & Compute
Care Setting->Electronic Health Record

evolve Clinical Decision Support 0.62
evolve Diagnostic Reasoning 0.48
evolve Electronic Health Record 0.82
evolve Fairness & Equity Controls 0.42

annotation 1 [[0.30, 0.22]] Bespoke judgement cluster
annotation 2 [[0.18, 0.80]] Industrialised process cluster
annotation 3 [[0.58, 0.55]] Build vs. buy frontier: CDS consolidating
```

### 3. Strategic commentary

## Purpose

Understand, in August 2022, where clinical decision making is still **bespoke judgement** and where it has been **industrialised** — and what that implies for where fairness, exceptions, and the build-vs-buy frontier sit.

## Component Evolution Assessment

| Component | Stage | [vis, mat] | Rationale |
|---|---|---|---|
| Patient | Product | [0.97, 0.46] | Anchor. Rights and expectations codified in patient-charter law. |
| Medical Practitioner | Custom-Built | [0.93, 0.36] | Anchor. Licensed individuals; training standardised, day-to-day judgement bespoke. |
| Medical Institution | Product | [0.90, 0.58] | Anchor. Multiple operating models (NHS trust, HMO, IDN, private group). |
| Payer | Commodity | [0.86, 0.70] | Anchor. Claims and financial rails are utility-grade. |
| Treatment Decision | Custom-Built | [0.80, 0.38] | Still case-by-case clinician judgement for non-trivial cases. |
| Care Setting | Product | [0.76, 0.52] | Typology well defined (primary/inpatient/outpatient/telehealth); patient-specific routing is bespoke. |
| Measured Outcome | Product | [0.72, 0.62] | ICHOM, CMS, NICE frameworks mature; interpretation contested. |
| Diagnostic Reasoning | Custom-Built (inertia) | [0.68, 0.30] | Tacit, tutored. Protected scope of practice creates resistance. |
| Clinical Decision Support | Product (inertia) | [0.60, 0.44] | UpToDate, DynaMed, Epic order sets — 3+ competing products. Alert fatigue and liability drive override culture. |
| Clinical Guidelines | Product (inertia) | [0.54, 0.66] | NICE/USPSTF/WHO — well-codified, slow update cycle. |
| Permissible Treatments Formulary | Commodity | [0.50, 0.76] | Standardised codes (BNF, ATC), competitive PBM market, utility-priced. |
| Exception & Appeals Rules | Custom-Built | [0.46, 0.28] | Process exists but each case is adversarial and bespoke. |
| Fairness & Equity Controls | Custom-Built | [0.42, 0.20] | NHS Core20PLUS5 (2021) and similar are early-stage; near-Genesis in practice. |
| Patient History & Examination | Product | [0.38, 0.55] | Structured interview + exam; EHR templates have industrialised much of it. |
| Diagnostic Tests & Imaging | Commodity | [0.32, 0.78] | Pathology, radiology, genomics at standardised price points; AI read-assist shifting right. |
| Electronic Health Record | Commodity | [0.26, 0.70] | Epic, Cerner/Oracle, TPP — near-universal in OECD by 2022. |
| Clinical Trials & Reviews | Product | [0.22, 0.42] | Regulated process, bespoke per-trial design. |
| Evidence Base & Literature | Product | [0.18, 0.58] | PubMed, Cochrane — well-indexed, uneven quality. |
| Coding & Billing Standards | Commodity | [0.12, 0.85] | ICD-10, SNOMED, CPT, HL7, FHIR R4. Ubiquitous. |
| Connectivity & Compute | Commodity | [0.06, 0.90] | HIPAA/GDPR-grade cloud; utility-priced. |

## Key Strategic Observations

1. **The map has two visible clusters, and they are different worlds.** Top-left (high visibility, low maturity) is a **bespoke-judgement cluster**: Diagnostic Reasoning, Treatment Decision, Exception & Appeals, and Fairness & Equity. Bottom-right (low visibility, high maturity) is an **industrialised cluster**: EHR, Coding Standards, Formulary, Connectivity, Imaging/Tests. Clinical Decision Support sits on the seam between them — it's the bridge, and the fight over who owns it (clinicians vs institutions vs payers vs vendors) is the central strategic battle.
2. **Fairness is still Genesis-adjacent.** Despite the rhetoric, the *controls* for equity (audit, disparity dashboards, algorithmic-fairness review of CDS) sit far left of where guidelines or formularies sit. This is a major exposure: industrialised rails will encode whatever biases exist in training data, and the corrective machinery is not yet mature.
3. **Exceptions are the relief valve — and they run on adversarial custom process.** Exception & Appeals Rules are Custom-Built and high visibility. A high volume of exceptions is a signal that *either* the formulary is miscalibrated *or* the population is non-average. Either way, the lack of industrialised exception-handling is a doctrine failure around **know your users**.
4. **EHR is commoditised; what sits on top of it is not.** By 2022 the EHR layer is fully Commodity, but the components *it feeds* (CDS, Outcomes, Decision) are Product or Custom. This asymmetry means the lock-in is at the data layer and the opportunity is in the overlays — exactly inverse to how most health systems procure.
5. **Payer-driven anchors create an uncomfortable pull.** The Payer is the right-most anchor (Commodity, 0.70 maturity), but it connects to Custom-Built components (Exception & Appeals Rules, Fairness). That pull — a utility-grade actor dragging bespoke-judgement components rightward — is a significant source of the legitimacy problems around prior authorisation and coverage determinations.

## Doctrine Check

- **Know your users**: The map identifies four anchors in tension. Pass — though most institutions in practice optimise for Institution + Payer and under-weight Patient + Practitioner.
- **Focus on user needs, not capability**: Mixed. EHR procurement tends to be capability-driven; outcome measurement is need-driven.
- **Remove bias and duplication**: Major gap. Every major provider in a system typically has its own CDS overlay against the same guidelines — duplication that doesn't create competitive advantage.
- **Use appropriate methods**: Mismatch in two places. (a) Fairness controls are being rolled out with Six Sigma-style governance when they belong in Agile/experimental territory. (b) Formulary decisioning often uses committee-based Agile-lite when ITIL-style process control would fit.
- **Manage inertia**: Three explicit inertia markers (Diagnostic Reasoning, CDS, Clinical Guidelines). These are the three components where evolution will be fought hardest — and where strategic effort should go into *managing resistance*, not routing around it.
- **Use standards where appropriate**: Strong at the Commodity layer (FHIR, ICD, SNOMED). Weak at the Product layer (CDS integrations are still per-vendor).

## Recommended Actions

1. **Industrialise the exception process.** Today a patient's appeal depends on who they know and how well they argue. Move Exception & Appeals Rules from Custom-Built to Product: standardise categories, evidence thresholds, and turnaround SLAs. This is the single highest-leverage equity intervention.
2. **Stop building in-house Clinical Decision Support.** The CDS market has three or more credible Product-stage options integrated into every major EHR by 2022. The skill-report AI-era patterns will further compress this. Redirect internal CDS engineering to domain-specific overlays (e.g. a differential-diagnosis aide specialised for your patient mix) — *not* yet another generic alerting layer.
3. **Fund Fairness & Equity Controls as a Genesis-stage investment.** Small, experimental teams; rapid prototyping; publish findings. Do not try to governance-board it to maturity — that will entrench the current opacity.
4. **Keep Diagnostic Reasoning Custom-Built, but industrialise its inputs.** History & Examination, Tests & Imaging, and EHR are the feeds. Invest in the *capture* and *quality* of those, not in replacing the clinician's reasoning. Manage the inertia marker as a *feature*, not a bug — this is the component where human judgement should remain strategic.
5. **Treat the Payer↔Formulary↔Exception triangle as a single sociotechnical system.** Commissioning one of these without the others (typical today) is what generates the "algorithmic denials" backlash. Map it once, govern it jointly.

## Build vs. Buy Assessment

| Component | Recommendation | Rationale |
|---|---|---|
| Clinical Decision Support | **Buy** | Product stage with 3+ vendors (UpToDate, DynaMed, Epic, Cerner overlays). Any internal build is subsidising your vendor's roadmap. |
| Electronic Health Record | **Buy** | Commodity; decision already taken for 90%+ of provider organisations. |
| Coding, Formulary, Connectivity | **Outsource/Buy** | Commodity layer. Use FHIR R4 and standard code systems; do not reinvent. |
| Fairness & Equity Controls | **Build** | Near-Genesis; no mature product market in 2022. Your implementation is part of your evolving operating model. |
| Exception & Appeals Rules | **Build, then productise** | Bespoke today; build the internal standard, then publish/share it — leadership by de-facto standard. |
| Diagnostic Reasoning | **Retain (human + augment)** | The moat. Do not try to buy or automate the core; do buy the decision-support overlays. |
| Clinical Guidelines | **Consume (don't author from scratch)** | NICE/USPSTF/specialty societies already publish; invest in rapid *local adaptation* instead. |

## Evolution Predictions (12-24 months, i.e. through late 2023-2024)

Drawn as dashed red arrows on the map:

- **Clinical Decision Support 0.44 → 0.62**: large-language-model-backed CDS will compress the category. Reading the skill's AI-era notes: expect the Custom-Built→Product boundary to blur here first. Inertia (alert fatigue, liability) will slow adoption but not stop it.
- **Diagnostic Reasoning 0.30 → 0.48**: not because clinicians will be replaced, but because *scaffolding* (AI scribes, differential-diagnosis aides) is moving the practice step from purely tacit to partly codified. Note: this movement is likely to be overstated by vendors and understated by professional bodies.
- **Electronic Health Record 0.70 → 0.82**: further commoditisation via FHIR-native exchange, payer-provider data-sharing rules (e.g. the US CMS Interoperability Rule), and cross-border extensions.
- **Fairness & Equity Controls 0.20 → 0.42**: from near-Genesis to Custom-Built as more health systems adopt structured equity dashboards. Still not a Product category by 2024.

## Open Questions

1. Where should the line between "automated exception" and "clinician/ethics-committee exception" sit, and who is accountable when the automated one gets it wrong?
2. If LLM-backed CDS moves CDS to Commodity by 2026, what happens to the Medical Practitioner anchor — does bespoke judgement *get narrower* (concentrated on edge cases) or *get broader* (re-absorbing parts of Diagnostic Reasoning now delegated)?
3. What is the strategic response if a Payer vertically integrates into the CDS stack — does the Institution anchor weaken? (This is less hypothetical in the US than elsewhere.)

---

## Notes on the run

- **Components**: 20 (4 anchors + 16 non-anchor).
- **Anchor count**: 4 (Patient, Medical Practitioner, Medical Institution, Payer).
- **Evolutions**: 4 (CDS, Diagnostic Reasoning, EHR, Fairness).
- **Inertia markers**: 3 (Diagnostic Reasoning, CDS, Clinical Guidelines).
- **Divergences from the haberlah workflow**:
  - Step 1 asks the skill to clarify strategic context *with the user*. The scenario is fixed, so I answered the four questions from the scenario myself (in the Strategic Context section above) rather than asking.
  - Step 2 recommends 8-15 components and flags >15 as "suggest submaps". I carried 20 components (4 anchors + 16) because the brief explicitly names 7 distinct apparatus areas plus four people-types plus the bespoke-vs-industrialised and fairness-vs-exceptions distinctions. The alternative — splitting into main + submaps — would fragment the central narrative (the seam between bespoke and industrialised), which is the map's strategic point. I noted the deviation here and accepted the readability cost.
  - Step 4 asks to run `validate_map.py` "if available". I did not execute it (this is a blind first-pass); I did the manual checks it calls out (positions in [0,1]; no cycles; arrows right-pointing; every referenced component exists; one+ anchor at top; no components within 0.06 on both axes).
  - I used four user anchors rather than one. The skill's SKILL.md says "at least one user/anchor at the top of the chain" but the OWM reference shows multi-anchor examples, so this is within the skill's grammar even if the workflow language tends toward a single anchor.
