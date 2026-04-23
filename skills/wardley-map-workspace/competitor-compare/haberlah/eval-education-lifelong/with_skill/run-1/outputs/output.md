# Wardley Map Analysis: Lifelong Education and Learning Landscape (2026)

## Purpose

This map answers the question: **Across the lifelong education and learning
landscape in 2026, which components are industrialised (Commodity/Product), which
are still artisanal (Custom-Built/Genesis), and where do power and
curriculum-shaping decide who gets included?** It is a landscape map with seven
anchors (students, employees, employers, educators, institutions, government and
regulators, and the wider community) rather than a single-firm build-vs-buy map.
The strategic use of the map is to locate the fragile and contested components
that most determine access, portability, and the legitimacy of qualifications.

## Strategic Context (answered from the brief)

The skill's Step 1 asks for four things. Because this benchmark provides the
scenario as a single prompt, the answers below were inferred directly from the
brief — they were not solicited from a live user.

| Question | Answer used |
|---|---|
| Strategic question | "What's industrialised, what's still artisanal, and where do power and curriculum shape who gets included?" |
| User anchors | Students, Employees, Employers, Educators, Institutions, Government and Regulators, Community — the seven named in the brief |
| Core needs | Capability (skills/knowledge), Inclusion, Status and Brand — the three visible outcomes through which learning delivers value |
| Scope boundary | Global lifelong education ecosystem (cradle-to-career plus continuing education), not one country and not one institution |

## Value Chain Overview

Working backward from the seven anchors to the infrastructure they rely on
produces 20 components grouped into six horizontal bands:

- **Outcome band (visible)**: Capability, Inclusion, Status and Brand
- **Curriculum band**: Formal Curriculum, Informal Curriculum, Skills Frameworks
- **Credential band**: Degrees, Micro-credentials (inertia), Digital Identity
- **Assessment and trust band**: Assessment, Certification Standards,
  Accreditation, Verification
- **Delivery and learning-means band**: AI Tutors, Community Learning, Online
  Delivery, Physical Delivery, Funding
- **Infrastructure band (invisible)**: Content Libraries, Compute and Connectivity

## OWM (OnlineWardleyMaps) Text Block

```
title Lifelong Education and Learning Landscape (2026)
style wardley

anchor Students [0.97, 0.42]
anchor Employees [0.97, 0.56]
anchor Employers [0.97, 0.70]
anchor Educators [0.93, 0.32]
anchor Institutions [0.93, 0.52]
anchor Government [0.93, 0.18]
anchor Community [0.93, 0.80]

component Capability [0.86, 0.40]
component Inclusion [0.84, 0.22]
component Status and Brand [0.82, 0.60]

component Formal Curriculum [0.74, 0.46]
component Informal Curriculum [0.72, 0.28]
component Skills Frameworks [0.66, 0.56]

component Degrees [0.62, 0.82]
component Micro-credentials [0.58, 0.32] inertia
component Digital Identity [0.54, 0.16]

component Assessment [0.48, 0.62]
component Certification Standards [0.44, 0.72]
component Accreditation [0.40, 0.78]
component Verification [0.36, 0.30]

component AI Tutors [0.32, 0.22]
component Community Learning [0.30, 0.36]

component Online Delivery [0.24, 0.74]
component Physical Delivery [0.22, 0.90]
component Funding [0.18, 0.68]

component Content Libraries [0.12, 0.82]
component Compute and Connectivity [0.06, 0.94]

Students->Capability
Students->Inclusion
Students->Degrees
Students->Micro-credentials
Students->Formal Curriculum
Students->Informal Curriculum

Employees->Capability
Employees->Micro-credentials
Employees->Skills Frameworks

Employers->Skills Frameworks
Employers->Certification Standards
Employers->Status and Brand
Employers->Capability

Educators->Formal Curriculum
Educators->Informal Curriculum
Educators->Assessment
Educators->AI Tutors

Institutions->Degrees
Institutions->Status and Brand
Institutions->Accreditation
Institutions->Funding

Government->Inclusion
Government->Accreditation
Government->Certification Standards
Government->Funding

Community->Community Learning
Community->Informal Curriculum
Community->Inclusion

Capability->Formal Curriculum
Capability->Informal Curriculum
Capability->Skills Frameworks

Status and Brand->Degrees
Status and Brand->Accreditation

Inclusion->Funding
Inclusion->Digital Identity
Inclusion->Physical Delivery

Formal Curriculum->Assessment
Formal Curriculum->Accreditation
Formal Curriculum->Online Delivery
Formal Curriculum->Physical Delivery

Informal Curriculum->AI Tutors
Informal Curriculum->Community Learning
Informal Curriculum->Online Delivery

Skills Frameworks->Micro-credentials
Skills Frameworks->Certification Standards
Skills Frameworks->Assessment

Degrees->Assessment
Degrees->Accreditation
Degrees->Verification

Micro-credentials->Assessment
Micro-credentials->Verification
Micro-credentials->Digital Identity

Digital Identity->Verification

Assessment->AI Tutors
Assessment->Online Delivery
Assessment->Physical Delivery

Verification->Content Libraries

Certification Standards->Accreditation
Certification Standards->Verification

Accreditation->Funding

AI Tutors->Content Libraries
AI Tutors->Compute and Connectivity

Community Learning->Physical Delivery

Online Delivery->Content Libraries
Online Delivery->Compute and Connectivity

Physical Delivery->Funding

Funding->Compute and Connectivity

Content Libraries->Compute and Connectivity

evolve Micro-credentials 0.55
evolve Digital Identity 0.40
evolve AI Tutors 0.45
evolve Skills Frameworks 0.70
evolve Verification 0.55
evolve Online Delivery 0.88

annotation 1 [[0.60, 0.40]] Micro-credentials have inertia: incumbent degree model and rankings resist the badge stack despite Open Badges 3.0 and LER initiatives.
annotation 2 [[0.34, 0.10]] AI Tutors moved from Genesis to early Custom-Built (2023-2026); Khanmigo, Squirrel AI, GPT-5 tutors widespread but outcome evidence thin.
annotation 3 [[0.52, 0.08]] Digital Identity (learner wallets, verifiable credentials) is the unlock for portable micro-credentials - still pre-standard.
annotation 4 [[0.86, 0.12]] Inclusion is contested and bespoke per jurisdiction; curriculum-shaping power sits here, not in the delivery stack.
annotation 5 [[0.58, 0.88]] Degrees are Commodity in form but Product-to-Commodity in prestige: everyone has one, but brand hierarchy (status) is how employers sort.
```

## Interactive React Artifact

```jsx
import React, { useState } from "react";

const COMPONENTS = [
  { id: "students", name: "Students", x: 0.42, y: 0.97, stage: "Anchor", anchor: true,
    rationale: "Primary learner anchor. Multiple needs: capability, inclusion, recognised credentials." },
  { id: "employees", name: "Employees", x: 0.56, y: 0.97, stage: "Anchor", anchor: true,
    rationale: "Adult-learner anchor. Cares about portable skills and micro-credentials for mobility." },
  { id: "employers", name: "Employers", x: 0.70, y: 0.97, stage: "Anchor", anchor: true,
    rationale: "Employer anchor. Hires on status, brand, and skills frameworks; funds corporate learning." },
  { id: "educators", name: "Educators", x: 0.32, y: 0.93, stage: "Anchor", anchor: true,
    rationale: "Teacher / faculty / trainer anchor. Shapes curriculum and assessment; increasingly works with AI tutors." },
  { id: "institutions", name: "Institutions", x: 0.52, y: 0.93, stage: "Anchor", anchor: true,
    rationale: "Schools, universities, bootcamps, corporate academies. Controls degrees, brand, and funding flows." },
  { id: "government", name: "Government", x: 0.18, y: 0.93, stage: "Anchor", anchor: true,
    rationale: "Government and regulators. Sets inclusion policy, accreditation frameworks, funding, and standards." },
  { id: "community", name: "Community", x: 0.80, y: 0.93, stage: "Anchor", anchor: true,
    rationale: "Wider community: families, civil society, informal networks. Drives community learning and informal curriculum." },

  { id: "capability", name: "Capability", x: 0.40, y: 0.86, stage: "Product",
    rationale: "The underlying user need (skills + knowledge applied). Well-understood concept with OECD/UNESCO frameworks; Product-stage construct even where measurement is contested." },
  { id: "inclusion", name: "Inclusion", x: 0.22, y: 0.84, stage: "Custom-Built",
    rationale: "Every jurisdiction drafts its own inclusion policy. Bespoke, politically contested, no standard measurement. This is where curriculum-shaping power sits." },
  { id: "status", name: "Status and Brand", x: 0.60, y: 0.82, stage: "Product",
    rationale: "Rankings (QS, THE, Shanghai), Ivy/Russell/C9 hierarchies, employer brand preferences. Well-established market; mature measurement even where contested." },

  { id: "formal", name: "Formal Curriculum", x: 0.46, y: 0.74, stage: "Product",
    rationale: "National curricula, degree syllabi, accredited programmes. Documented, comparable, reviewable. Clear Product stage with multiple providers (boards, universities, vendors)." },
  { id: "informal", name: "Informal Curriculum", x: 0.28, y: 0.72, stage: "Custom-Built",
    rationale: "YouTube, Substack, podcasts, bootcamps, on-the-job learning. Massive variety, no standardisation, bespoke per creator and community. Custom-Built with some Genesis edges." },
  { id: "skills", name: "Skills Frameworks", x: 0.56, y: 0.66, stage: "Product",
    rationale: "ESCO (EU), O*NET (US), SFIA, Lightcast taxonomies. Multiple competing frameworks with published mappings; clear Product stage." },

  { id: "degrees", name: "Degrees", x: 0.82, y: 0.62, stage: "Commodity",
    rationale: "Bachelor's/Master's/PhD are universal and standardised across the Bologna process and equivalents. Signalling hierarchy is Commodity in form even where prestige varies." },
  { id: "micro", name: "Micro-credentials", x: 0.32, y: 0.58, stage: "Custom-Built", inertia: true,
    rationale: "Open Badges 3.0, Coursera/edX/LinkedIn certs, Learning and Employment Records (LER). Standards emerging but fragmented; inertia because employers and institutions still weight the degree heavily." },
  { id: "digital-id", name: "Digital Identity", x: 0.16, y: 0.54, stage: "Genesis",
    rationale: "Learner wallets on EU Digital Identity Wallet (eIDAS 2), W3C Verifiable Credentials, Europass. Production pilots exist but no cross-border adoption at scale." },

  { id: "assessment", name: "Assessment", x: 0.62, y: 0.48, stage: "Product",
    rationale: "Standardised exams (SAT, A-levels, Gaokao), LMS-based online assessment, proctoring vendors. Mature Product stage with active AI-era disruption." },
  { id: "certification", name: "Certification Standards", x: 0.72, y: 0.44, stage: "Product",
    rationale: "Professional certification bodies (ACCA, CISSP, AWS, PMI). Well-defined, multiple vendors, clear pricing. Product stage." },
  { id: "accreditation", name: "Accreditation", x: 0.78, y: 0.40, stage: "Product",
    rationale: "Quality assurance agencies (QAA, SACSCOC, WASC, EQAR). Stable mature market; Commodity in rich jurisdictions but Product globally." },
  { id: "verification", name: "Verification", x: 0.30, y: 0.36, stage: "Custom-Built",
    rationale: "Degree verification is bespoke: transcript requests, third-party checks (HEDD, NSC), nascent blockchain solutions (MIT Blockcerts). Standards fragmenting; clearly Custom-Built despite long history." },

  { id: "ai-tutors", name: "AI Tutors", x: 0.22, y: 0.32, stage: "Custom-Built",
    rationale: "Khan Academy Khanmigo, Squirrel AI, Duolingo Max, GPT-5 tutors. Widely deployed since 2023-2024 but per-vendor bespoke; outcome evidence thin and contested." },
  { id: "community-learning", name: "Community Learning", x: 0.36, y: 0.30, stage: "Custom-Built",
    rationale: "Apprenticeships, guilds, mentoring circles, local communities of practice. Tacit knowledge transfer; high variation; resistant to industrialisation." },

  { id: "online", name: "Online Delivery", x: 0.74, y: 0.24, stage: "Product",
    rationale: "LMS (Canvas, Moodle, Blackboard), MOOC platforms (Coursera, edX, FutureLearn), video conferencing. Mature market with multiple competing vendors and pricing transparency." },
  { id: "physical", name: "Physical Delivery", x: 0.90, y: 0.22, stage: "Commodity",
    rationale: "Classrooms, labs, campuses, training centres. Utility in rich countries; Product where capacity is a constraint. Overall Commodity." },
  { id: "funding", name: "Funding", x: 0.68, y: 0.18, stage: "Product",
    rationale: "Government grants, student loans, corporate L&D budgets, ISAs, scholarships. Well-understood financial instruments with competitive markets." },

  { id: "content", name: "Content Libraries", x: 0.82, y: 0.12, stage: "Commodity",
    rationale: "Open Educational Resources (OER), publisher catalogues (Pearson, Cengage, Elsevier), MERLOT, OpenStax. Utility-priced or free. Supply abundant." },
  { id: "compute", name: "Compute and Connectivity", x: 0.94, y: 0.06, stage: "Commodity",
    rationale: "Cloud (AWS, GCP, Azure), broadband, 5G, mobile devices. The classic utility stack underlying every online and AI-assisted learning activity." }
];

const LINKS = [
  ["students","capability"],["students","inclusion"],["students","degrees"],["students","micro"],["students","formal"],["students","informal"],
  ["employees","capability"],["employees","micro"],["employees","skills"],
  ["employers","skills"],["employers","certification"],["employers","status"],["employers","capability"],
  ["educators","formal"],["educators","informal"],["educators","assessment"],["educators","ai-tutors"],
  ["institutions","degrees"],["institutions","status"],["institutions","accreditation"],["institutions","funding"],
  ["government","inclusion"],["government","accreditation"],["government","certification"],["government","funding"],
  ["community","community-learning"],["community","informal"],["community","inclusion"],
  ["capability","formal"],["capability","informal"],["capability","skills"],
  ["status","degrees"],["status","accreditation"],
  ["inclusion","funding"],["inclusion","digital-id"],["inclusion","physical"],
  ["formal","assessment"],["formal","accreditation"],["formal","online"],["formal","physical"],
  ["informal","ai-tutors"],["informal","community-learning"],["informal","online"],
  ["skills","micro"],["skills","certification"],["skills","assessment"],
  ["degrees","assessment"],["degrees","accreditation"],["degrees","verification"],
  ["micro","assessment"],["micro","verification"],["micro","digital-id"],
  ["digital-id","verification"],
  ["assessment","ai-tutors"],["assessment","online"],["assessment","physical"],
  ["verification","content"],
  ["certification","accreditation"],["certification","verification"],
  ["accreditation","funding"],
  ["ai-tutors","content"],["ai-tutors","compute"],
  ["community-learning","physical"],
  ["online","content"],["online","compute"],
  ["physical","funding"],
  ["funding","compute"],
  ["content","compute"]
];

const EVOLUTIONS = [
  { id: "micro", to: 0.55 },
  { id: "digital-id", to: 0.40 },
  { id: "ai-tutors", to: 0.45 },
  { id: "skills", to: 0.70 },
  { id: "verification", to: 0.55 },
  { id: "online", to: 0.88 }
];

const W = 1200, H = 760, PAD = { top: 60, right: 230, bottom: 70, left: 180 };
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
                fill={i%2===0 ? "#fafafa" : "#fff"} />
        ))}
        {[0.25,0.5,0.75].map(m => (
          <line key={m} x1={xS(m)} y1={PAD.top} x2={xS(m)} y2={H-PAD.bottom}
                stroke="#ccc" strokeDasharray="4 4"/>
        ))}
        <text x={PAD.left} y={40} fontSize="16" fontWeight="600" fill="#111">
          Lifelong Education and Learning Landscape — 2026
        </text>
        <text x={xS(0.125)} y={H-PAD.bottom+18} fontSize="11" textAnchor="middle" fill="#555">Genesis</text>
        <text x={xS(0.375)} y={H-PAD.bottom+18} fontSize="11" textAnchor="middle" fill="#555">Custom-Built</text>
        <text x={xS(0.625)} y={H-PAD.bottom+18} fontSize="11" textAnchor="middle" fill="#555">Product (+Rental)</text>
        <text x={xS(0.875)} y={H-PAD.bottom+18} fontSize="11" textAnchor="middle" fill="#555">Commodity (+Utility)</text>
        <text x={xS(0.5)} y={H-PAD.bottom+40} fontSize="12" textAnchor="middle" fill="#333">Evolution</text>
        <text x={30} y={PAD.top+10} fontSize="11" fill="#555">Visible</text>
        <text x={30} y={H-PAD.bottom-5} fontSize="11" fill="#555">Invisible</text>
        <text x={20} y={(PAD.top+H-PAD.bottom)/2} fontSize="12" transform={`rotate(-90 20 ${(PAD.top+H-PAD.bottom)/2})`}
              textAnchor="middle" fill="#333">Value chain / Visibility</text>

        {LINKS.map(([a,b],i) => {
          const A = byId[a], B = byId[b];
          if (!A || !B) return null;
          const op = (dim(a)||dim(b)) ? 0.08 : 0.45;
          const x1=xS(A.x), y1=yS(A.y), x2=xS(B.x), y2=yS(B.y);
          const cx = (x1+x2)/2, cy = (y1+y2)/2 + 16;
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
              <circle cx={cx} cy={cy} r="7" fill={fill} stroke="#222" strokeWidth="1.5"/>
              <text x={cx+11} y={cy+4} fontSize="11" fill="#111">
                {c.name}
              </text>
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
                     style={{ fontSize: "10px", lineHeight: "1.35", color: "#333" }}>
                  {c.rationale}
                </div>
              </foreignObject>
            </g>
          );
        })()}

        {/* Figure legend */}
        <g transform={`translate(${W-PAD.right+10}, ${PAD.top+10})`}>
          <rect x="0" y="0" width="210" height="240" fill="#fff" stroke="#222"/>
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

          <text x="10" y="158" fontSize="10" fontWeight="600" fill="#111">Stages (x-axis)</text>
          <text x="10" y="174" fontSize="9" fill="#555">Genesis       0.00–0.17</text>
          <text x="10" y="188" fontSize="9" fill="#555">Custom-Built  0.18–0.39</text>
          <text x="10" y="202" fontSize="9" fill="#555">Product       0.40–0.69</text>
          <text x="10" y="216" fontSize="9" fill="#555">Commodity     0.70–1.00</text>
        </g>
      </svg>
    </div>
  );
}
```

## Component Evolution Assessment

| Component | Stage | Position [vis, mat] | Rationale |
|---|---|---|---|
| Students | Anchor | [0.97, 0.42] | Primary learner anchor. Multiple needs: capability, inclusion, recognised credentials. Placed left-of-centre on x because students' focus is on novel skill acquisition. |
| Employees | Anchor | [0.97, 0.56] | Adult-learner anchor. Cares about portable skills and micro-credentials for mobility. Placed mid-axis. |
| Employers | Anchor | [0.97, 0.70] | Employer anchor. Hires on status, brand, and skills frameworks. Placed right-of-centre — biased toward mature, standardised signals. |
| Educators | Anchor | [0.93, 0.32] | Teachers, faculty, trainers. Shapes curriculum and assessment and increasingly co-works with AI tutors — skews left toward Custom-Built activity. |
| Institutions | Anchor | [0.93, 0.52] | Schools, universities, bootcamps, corporate academies. Controls degrees, brand, and funding flows. |
| Government | Anchor | [0.93, 0.18] | Government and regulators. Sets inclusion policy, accreditation frameworks, standards. Positioned far-left because their formative work is in the contested Custom-Built/Genesis policy space. |
| Community | Anchor | [0.93, 0.80] | Wider community: families, civil society, informal networks. Drives community learning and informal curriculum, often at scale in mature forms. |
| Capability | Product | [0.86, 0.40] | The underlying user need — skills plus knowledge applied. Well-understood concept with OECD/UNESCO/ALFA+ frameworks; Product-stage construct even where measurement is contested. |
| Inclusion | Custom-Built | [0.84, 0.22] | Every jurisdiction drafts its own inclusion policy (SEND code, ADA/Section 504, EU accessibility directive). Bespoke, politically contested, no standard measurement. This is where curriculum-shaping power concentrates. |
| Status and Brand | Product | [0.82, 0.60] | Rankings (QS, THE, Shanghai, FT), Ivy/Russell/C9 hierarchies, employer-reputation lists. Well-established market; mature measurement even where contested. |
| Formal Curriculum | Product | [0.74, 0.46] | National curricula, degree syllabi, accredited programmes. Documented, comparable, reviewable. Clear Product stage with multiple providers (boards, universities, publishers). |
| Informal Curriculum | Custom-Built | [0.72, 0.28] | YouTube, Substack, podcasts, bootcamps, on-the-job learning. Massive variety, no standardisation, bespoke per creator and community. Custom-Built with some Genesis edges. |
| Skills Frameworks | Product | [0.66, 0.56] | ESCO (EU), O*NET (US), SFIA, Lightcast/Burning Glass taxonomies. Multiple competing frameworks with published mappings; clear Product with consolidation pressure. |
| Degrees | Commodity | [0.62, 0.82] | Bachelor's/Master's/PhD are universal and standardised across the Bologna process and equivalents. Signalling hierarchy is Commodity in form even where prestige varies. |
| Micro-credentials | Custom-Built (inertia) | [0.58, 0.32] | Open Badges 3.0, Coursera/edX/LinkedIn certs, Learning and Employment Records (LER). Standards emerging but fragmented; inertia because employers and institutions still weight the degree heavily despite decade-long push. |
| Digital Identity | Genesis | [0.54, 0.16] | Learner wallets on EU Digital Identity Wallet (eIDAS 2), W3C Verifiable Credentials, Europass. Production pilots exist but no cross-border adoption at scale as of 2026. |
| Assessment | Product | [0.48, 0.62] | Standardised exams (SAT, A-levels, Gaokao), LMS-based online assessment, proctoring vendors (ProctorU, Examity, Respondus). Mature Product stage with active AI-era disruption. |
| Certification Standards | Product | [0.44, 0.72] | Professional certification bodies (ACCA, CISSP, AWS, PMI, Cisco). Well-defined, multiple vendors, clear pricing. Mid-to-late Product stage. |
| Accreditation | Product | [0.40, 0.78] | Quality assurance agencies (QAA, SACSCOC, WASC, EQAR, CHEA). Stable mature market; Commodity in rich jurisdictions but Product globally. |
| Verification | Custom-Built | [0.36, 0.30] | Degree verification is bespoke: transcript requests, third-party checks (HEDD, NSC), nascent blockchain solutions (MIT Blockcerts, Greenlight Credentials). Standards fragmenting; clearly Custom-Built despite long history. |
| AI Tutors | Custom-Built | [0.32, 0.22] | Khan Academy Khanmigo, Squirrel AI, Duolingo Max, GPT-5-class tutors. Widely deployed since 2023-2024 but per-vendor bespoke; outcome evidence thin and contested. Early Custom-Built, late-Genesis edges. |
| Community Learning | Custom-Built | [0.30, 0.36] | Apprenticeships, guilds, mentoring circles, local communities of practice. Tacit knowledge transfer; high variation; resistant to industrialisation. |
| Online Delivery | Product | [0.24, 0.74] | LMS (Canvas, Moodle, Blackboard, D2L), MOOC platforms (Coursera, edX, FutureLearn), video conferencing. Mature market with multiple competing vendors and pricing transparency. On the edge of Commodity. |
| Physical Delivery | Commodity | [0.22, 0.90] | Classrooms, labs, campuses, training centres. Utility in rich countries; Product where capacity is a constraint. Overall Commodity. |
| Funding | Product | [0.18, 0.68] | Government grants, student loans, corporate L&D budgets, Income Share Agreements, scholarships. Well-understood financial instruments with competitive markets. |
| Content Libraries | Commodity | [0.12, 0.82] | Open Educational Resources (OER), publisher catalogues (Pearson, Cengage, Elsevier), MERLOT, OpenStax, MIT OCW. Utility-priced or free. Supply abundant. |
| Compute and Connectivity | Commodity | [0.06, 0.94] | Cloud (AWS, GCP, Azure), broadband, 5G, mobile devices. The classic utility stack underlying every online and AI-assisted learning activity. |

## Key Strategic Observations

1. **The delivery stack is industrialised; the credential stack is not.** Physical
   Delivery, Online Delivery, Content Libraries, and Compute are firmly in the
   Product-Commodity band. Degrees themselves are Commodity as *forms*. But the
   pieces that make a credential *portable* — Micro-credentials, Digital
   Identity, Verification — are Custom-Built or Genesis. This is why every
   learner in 2026 still depends on transcript requests and paper-or-PDF proof,
   even though the learning happened on cloud infrastructure.

2. **The inclusion question lives at the top-left of the map.** The brief asks
   where power and curriculum shape who gets included. Inclusion (Custom-Built,
   visibility 0.84) is high-visibility and low-maturity — which in Wardley terms
   is exactly where political contestation concentrates. Curriculum-shaping power
   operates *above* the technical delivery stack and is not industrialised by
   anyone. AI delivery does not resolve this; it inherits it.

3. **Micro-credentials carry the strongest inertia signal on the map.** The
   standards (Open Badges 3.0, LERs, skills taxonomies) have existed for over a
   decade, yet employers and institutions still default to degrees. The inertia
   marker captures the gap between what the infrastructure *could* support and
   what Status and Brand *actually rewards*. Without Digital Identity reaching
   Custom-Built-to-Product in the next 24 months, micro-credentials stall.

4. **AI Tutors crossed into Custom-Built, not Product.** Widespread deployment
   since Khanmigo (2023) does not make AI tutors Product. Each vendor's
   pedagogy, safety layer, and data pipeline is bespoke; outcome evidence is
   thin; regulators in several jurisdictions (EU AI Act Annex III, Chinese MoE
   guidance) class education-AI as high-risk. Expect Product stage within 24-36
   months, conditional on evidence.

5. **The power map and the delivery map are decoupled.** The upper bands
   (Inclusion, Status, Curriculum) are where access and legitimacy are decided;
   the lower bands (Delivery, Infrastructure, Funding) are industrialised
   utilities. Efficiency gains in the lower bands do not automatically cascade
   into equity gains in the upper bands — a structural reason why
   industrialised delivery has not, on its own, closed attainment gaps.

## Doctrine Check

- **Know your users (Phase I, Communication):** Seven anchors, each with a
  distinct dependency pattern. Students, Employees, and Community lean toward
  informal and inclusion components; Employers and Institutions lean toward
  Status, Brand, and Skills Frameworks; Government and Educators lean toward
  Accreditation, Inclusion, and Assessment. The map refuses to collapse these
  into a single "learner."
- **Focus on user needs (Phase I, Leading):** The outcome band — Capability,
  Inclusion, Status and Brand — is drawn from the brief's explicit user
  priorities, not from institutional capabilities.
- **Use appropriate methods (Phase I, Development):** The map reveals a
  method mismatch. Genesis components (Digital Identity) and Custom-Built
  components (AI Tutors, Verification, Micro-credentials) are being integrated
  into regulatory and procurement processes designed for Product/Commodity.
  Applying Six-Sigma-style accreditation gates to Genesis infrastructure will
  either slow adoption or force premature standardisation.
- **Manage inertia (Phase II, Leading):** Micro-credentials carries an inertia
  marker. The forcing functions on the map — Digital Identity, Skills
  Frameworks evolution, Employer adoption — are external to institutions and
  will prevail if they converge, even if institutions resist.
- **Remove bias and duplication (Phase I, Operations):** Skills Frameworks is
  a duplication hot spot (ESCO / O*NET / SFIA / Lightcast all mapping
  overlapping territory). The map predicts consolidation as employer hiring
  systems force an interchange layer.
- **Think FIRE (Phase II, Operations):** Community Learning and Informal
  Curriculum are the most FIRE-aligned components and are systematically
  underfunded relative to Formal Curriculum despite strong outcome evidence
  for apprenticeship and peer learning.

## Build vs. Buy Assessment

| Component | Recommendation | Rationale |
|---|---|---|
| Inclusion (Custom-Built, politically contested) | Build / shape | No vendor produces this; governments and institutions shape it directly through policy. This is where strategic voice matters. |
| Digital Identity (Genesis) | Build-with-standards or invest | No market alternative reaches scale. Pick a standards track (eIDAS 2 + W3C VC) and implement; do not build a proprietary wallet. |
| Micro-credentials (Custom-Built, inertia) | Build within an open standard | Open Badges 3.0 + LER is the best-positioned open track; institutions that bet on closed-stack vendor lock-in will strand. |
| AI Tutors (Custom-Built) | Hybrid: buy platform, own the pedagogy | Platform (Khanmigo, Duolingo Max, Squirrel) is cheaper to rent; the pedagogy, safety layer, and assessment integration are still a differentiator for institutions. |
| Community Learning (Custom-Built) | Build / facilitate | Cannot be bought. Institutions and communities co-produce it. Underinvested relative to outcome evidence. |
| Formal Curriculum (Product) | Buy / reuse | Accredited syllabi, open content, textbook catalogues are abundant. Reinvention is waste except for differentiation. |
| Skills Frameworks (Product → Commodity) | Buy / adopt standard | ESCO, O*NET, SFIA, Lightcast. Pick one for your geography and map to the others. Do not build yet-another-taxonomy. |
| Assessment (Product) | Buy, audit for AI-era integrity | Proctoring, LMS-integrated assessment, item banks are Product-stage. AI-era cheating risks need a separate integrity layer. |
| Certification Standards / Accreditation (Product) | Buy / comply | Mature market; institutions comply with QA agencies rather than build alternatives. |
| Online Delivery (Product) | Buy / rent | Canvas, Moodle, Blackboard, D2L. Nobody builds an LMS in 2026 except to differentiate at the edges. |
| Physical Delivery (Commodity) | Buy / outsource | Estate, facilities management. Commodity, managed on cost. |
| Content Libraries (Commodity) | Buy / use OER | Free or low-cost. No case for in-house content for general subjects. |
| Compute and Connectivity (Commodity) | Buy / outsource | Hyperscaler cloud plus ISP. The AI-era reference is explicit: do not rebuild commodities. |

## Evolution Predictions (12–24 months, through 2028)

- **Micro-credentials**: 0.32 → 0.55. Open Badges 3.0 adoption, employer-led
  skills-based hiring, and EU Digital Credentials for Learning regulation push
  this from Custom-Built deep into Product. (Evolution arrow on map.)
- **Digital Identity**: 0.16 → 0.40. EU Digital Identity Wallet (eIDAS 2) full
  rollout 2026-2027 and equivalent US / Singapore / India programmes bring this
  from Genesis to Custom-Built. (Evolution arrow on map.)
- **AI Tutors**: 0.22 → 0.45. Evidence accumulates, regulatory guidance
  stabilises, vendor ecosystems consolidate. Late Custom-Built edging into
  Product. (Evolution arrow on map.)
- **Skills Frameworks**: 0.56 → 0.70. Employer hiring systems force
  interoperability; ESCO/O*NET alignment deepens. Product → Commodity. (Evolution
  arrow on map.)
- **Verification**: 0.30 → 0.55. W3C VC-based issuer networks (Blockcerts,
  Velocity Network, European Blockchain Services Infrastructure) reach
  production. (Evolution arrow on map.)
- **Online Delivery**: 0.74 → 0.88. Continued consolidation; AI co-pilots embedded
  in LMS as standard; Commodity. (Evolution arrow on map.)
- **Inclusion**: holds Custom-Built. Political contestation, not technological
  maturity, governs progress. No evolution arrow — the component is not on a
  technology path.
- **Degrees**: Commodity in form but a status-driven market; unlikely to move
  further but at long-term erosion risk as Micro-credentials + Verification
  mature together.

## Where Power and Curriculum Shape Inclusion (the brief's explicit question)

Mapping this explicitly to the map's topology:

- **Curriculum power** concentrates in three places: who sets **Formal
  Curriculum** (governments, accreditation bodies, publishers), who sets
  **Informal Curriculum** (platform operators, creators, communities), and who
  sets **Skills Frameworks** (governments + large employers + taxonomy
  vendors). These three components sit in the upper-middle band of the map.
- **Inclusion power** sits at [0.84, 0.22] — high-visibility, Custom-Built —
  and is exercised through Funding, Digital Identity, and Physical Delivery.
  Who writes inclusion policy (usually Government, with Community pressure)
  determines which learners reach which parts of the stack.
- **The gap between the two** is the contested zone. Industrialised delivery
  (Online, Physical, Content, Compute) is nominally open to all but is gated by
  Funding, Digital Identity access, and Accreditation gatekeeping. Equity
  interventions that target only the lower bands (e.g. device programmes) do
  not address the upper-band gatekeepers.

## What's Industrialised vs. Still Artisanal (the brief's explicit question)

**Industrialised (Commodity / late Product):**
- Compute and Connectivity, Content Libraries, Physical Delivery (Commodity)
- Degrees (Commodity in form)
- Online Delivery, Funding, Accreditation, Certification Standards, Assessment,
  Skills Frameworks, Status and Brand, Formal Curriculum, Capability (Product)

**Still Artisanal (Custom-Built / Genesis):**
- Digital Identity (Genesis)
- Inclusion, Informal Curriculum, Micro-credentials, Verification, AI Tutors,
  Community Learning (Custom-Built)

**Structural implication:** Everything that delivers learning at scale is
industrialised. Everything that decides *who gets access* and *what the
learning counts for* is artisanal. The map's shape is the answer to the brief's
framing question.

## Open Questions

1. Does EU Digital Identity Wallet adoption actually drive cross-jurisdictional
   credential portability, or does sovereignty fragmentation keep learner
   wallets siloed per bloc?
2. Do employers' skills-based hiring commitments translate into
   micro-credential acceptance at hiring gates, or does degree-based screening
   persist because of legal-defensibility concerns?
3. Does AI Tutor outcome evidence stabilise enough in 12-24 months to move the
   component into Product, or does regulatory caution (EU AI Act high-risk
   classification) slow the transition regardless of technical readiness?

---

*This analysis was produced following the haberlah `wardley-mapping` skill
(SKILL.md Steps 1-7). The Step 1 strategic-context questions were answered from
the scenario brief because no live user was available. No iteration against an
external validator was performed; this is a first complete pass per the
benchmark contract. Manual validation confirms zero visibility-constraint
violations, zero cycles, and all positions within [0,1].*
