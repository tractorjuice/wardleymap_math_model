# Executive View of Cybersecurity Risk Management — May 2023

## Step 0 — Strategic context

**Strategic question.** Where should an executive invest incremental cyber-risk spend in May 2023 — specifically, which parts of the apparatus are commoditised (and should be bought / rented as utilities), which remain expert judgement (and therefore attract premium pay, retention and external advisory cost), and where are regulatory obligations dictating shape rather than the executive's own risk appetite?

**User anchor.** The Executive / Board. The map is drawn from the seat of someone who signs off on risk appetite, reads heatmaps monthly, buys cyber insurance annually and is personally on the hook if the company is breached. The CISO is the downstream translator, not the anchor.

**Core needs the executive has.**
1. Know how much cyber risk the business actually carries (in £ / $ terms if possible).
2. Keep the company out of regulatory and insurance trouble.
3. Not be the one who approved the inadequate control when the breach happens.
4. Allocate the next dollar of security budget where it buys down the most residual risk.

**Scope boundary.** Enterprise-scale cybersecurity risk management as a landscape (not one SOC, not one product). Time-stamped to May 2023 — this matters for the LLM components (ChatGPT is 6 months old; the Biden AI EO is 5 months away; cyber-insurance premiums are still re-setting after the 2021–2022 ransomware-driven hard market).

**Assumptions flagged for user correction.**
- Single executive/board anchor (not separately modelling CEO vs. Audit Committee vs. CFO). A mid-market company with a single exec sponsor fits cleanly; a FTSE 100 with three committees might need three anchors.
- "Enterprise" scope — not consumer, not critical national infrastructure. Critical infrastructure would push Compliance Frameworks higher (NIS2, CIRCIA) and add sector-specific regulators.
- Jurisdiction is implicitly US/UK/EU. APAC regulatory obligations would reshape the compliance layer.

---

## Map

```owm
title Executive View of Cybersecurity Risk Management (May 2023)
style wardley

// Anchors - the executive is the primary decision-maker
anchor Executive / Board [0.96, 0.55]

// User-visible executive drivers (why the exec cares)
component P&L / Shareholder Value [0.93, 0.70]
component Regulatory Obligations [0.90, 0.62]
component Risk Appetite Statement [0.88, 0.40]
component Board Risk Reporting [0.85, 0.55]

// Translation layer (CISO function)
component CISO Function [0.80, 0.55]
component Risk Identification Practice [0.75, 0.35]
component Risk Assessment Methodology [0.72, 0.45]

// Frameworks (standards layer)
component Compliance Frameworks (ISO 27001, SOC 2) [0.68, 0.82]
component Risk Frameworks (NIST CSF, ISO 31000) [0.66, 0.72]
component FAIR Quantification [0.62, 0.46]
component Likelihood / Impact Scoring [0.60, 0.78]
component Risk Matrices (Heatmaps) [0.58, 0.85]

// Risk register + treatment decisions
component Risk Register [0.74, 0.70]
component Mitigation / Transfer / Acceptance Mix [0.62, 0.42]
component Cyber Insurance [0.55, 0.58]

// Asset & data foundation
component Asset Inventory [0.52, 0.65]
component CMDB / Asset Discovery Tools [0.40, 0.72]
component Threat Intelligence Feeds [0.42, 0.66]

// Operational security layer
component Security Operations (SOC) [0.50, 0.55]
component SIEM / XDR Tooling [0.38, 0.72]
component SOAR / Automation [0.35, 0.55]
component Continuous Monitoring [0.45, 0.68]
component Vulnerability Management [0.40, 0.77]

// Testing / assurance
component Security Testing Programme [0.48, 0.52]
component Penetration Testing [0.42, 0.70]
component Bug Bounty [0.35, 0.60]
component Red Team Exercises [0.38, 0.45]

// Incident response
component Incident Response [0.45, 0.62]
component IR Playbooks / Runbooks [0.33, 0.58]
component Forensics & Investigation [0.30, 0.50]

// LLM angle (May 2023 - very early)
component LLM-Assisted Defence (SOC copilot) [0.32, 0.15]
component LLM as Attack Vector (prompt injection, shadow AI) [0.70, 0.12]
component LLM Governance Policy [0.58, 0.18]

// Expert judgement & knowledge
component Security Expertise (internal) [0.25, 0.30]
component External Advisory / Consultancy [0.22, 0.55]
component Audit Evidence Collection [0.28, 0.70]

// Commodity infrastructure the whole apparatus runs on
component Identity / SSO [0.18, 0.85]
component Endpoint Protection (EDR) [0.22, 0.78]
component Cloud Security Posture Management [0.20, 0.68]
component Logging / Log Storage [0.12, 0.90]
component Cloud Utilities (compute, storage, network) [0.08, 0.92]

// Dependencies
Executive / Board->P&L / Shareholder Value
Executive / Board->Regulatory Obligations
Executive / Board->Risk Appetite Statement
Executive / Board->Board Risk Reporting
Board Risk Reporting->CISO Function
Risk Appetite Statement->CISO Function
Regulatory Obligations->Compliance Frameworks (ISO 27001, SOC 2)
P&L / Shareholder Value->Cyber Insurance
CISO Function->Risk Identification Practice
CISO Function->Risk Assessment Methodology
CISO Function->Risk Register
CISO Function->Mitigation / Transfer / Acceptance Mix
Risk Assessment Methodology->Risk Frameworks (NIST CSF, ISO 31000)
Risk Assessment Methodology->FAIR Quantification
Risk Assessment Methodology->Likelihood / Impact Scoring
Likelihood / Impact Scoring->Risk Matrices (Heatmaps)
FAIR Quantification->Threat Intelligence Feeds
Risk Register->Asset Inventory
Risk Register->Risk Assessment Methodology
Risk Identification Practice->Asset Inventory
Risk Identification Practice->Threat Intelligence Feeds
Asset Inventory->CMDB / Asset Discovery Tools
Mitigation / Transfer / Acceptance Mix->Cyber Insurance
Mitigation / Transfer / Acceptance Mix->Security Operations (SOC)
Mitigation / Transfer / Acceptance Mix->Security Testing Programme
Mitigation / Transfer / Acceptance Mix->LLM Governance Policy
Compliance Frameworks (ISO 27001, SOC 2)->Audit Evidence Collection
Compliance Frameworks (ISO 27001, SOC 2)->Risk Frameworks (NIST CSF, ISO 31000)
Security Operations (SOC)->Continuous Monitoring
Security Operations (SOC)->Incident Response
Security Operations (SOC)->Vulnerability Management
Security Operations (SOC)->LLM-Assisted Defence (SOC copilot)
Continuous Monitoring->SIEM / XDR Tooling
Continuous Monitoring->SOAR / Automation
Continuous Monitoring->Logging / Log Storage
SIEM / XDR Tooling->Logging / Log Storage
SIEM / XDR Tooling->Cloud Utilities (compute, storage, network)
SOAR / Automation->Cloud Utilities (compute, storage, network)
Vulnerability Management->Endpoint Protection (EDR)
Vulnerability Management->Cloud Security Posture Management
Security Testing Programme->Penetration Testing
Security Testing Programme->Bug Bounty
Security Testing Programme->Red Team Exercises
Penetration Testing->Security Expertise (internal)
Penetration Testing->External Advisory / Consultancy
Red Team Exercises->Security Expertise (internal)
Bug Bounty->External Advisory / Consultancy
Incident Response->IR Playbooks / Runbooks
Incident Response->Forensics & Investigation
Forensics & Investigation->Security Expertise (internal)
Forensics & Investigation->Logging / Log Storage
IR Playbooks / Runbooks->Security Expertise (internal)
Risk Identification Practice->LLM as Attack Vector (prompt injection, shadow AI)
LLM Governance Policy->LLM-Assisted Defence (SOC copilot)
LLM-Assisted Defence (SOC copilot)->Cloud Utilities (compute, storage, network)
Endpoint Protection (EDR)->Cloud Utilities (compute, storage, network)
Cloud Security Posture Management->Cloud Utilities (compute, storage, network)
Logging / Log Storage->Cloud Utilities (compute, storage, network)
Identity / SSO->Cloud Utilities (compute, storage, network)
CMDB / Asset Discovery Tools->Cloud Utilities (compute, storage, network)
Audit Evidence Collection->Logging / Log Storage
Audit Evidence Collection->External Advisory / Consultancy
CISO Function->Security Expertise (internal)
CISO Function->External Advisory / Consultancy
Executive / Board->Identity / SSO

evolve FAIR Quantification 0.65
evolve LLM-Assisted Defence (SOC copilot) 0.45
evolve Cyber Insurance 0.72
evolve Bug Bounty 0.75
evolve LLM Governance Policy 0.50

note Expert judgement zone [0.35, 0.30]
note Commoditised tooling [0.20, 0.88]
note Regulation-forced shape [0.72, 0.78]
note Genesis - LLM frontier [0.35, 0.12]
```

---

## 3.2 — Component evolution rationale

| Component | Stage | ε | ν | Evidence |
|---|---|---|---|---|
| P&L / Shareholder Value | Product (+rental) | 0.70 | 0.93 | Running concept of the firm; boards talk about it in standard language; ISS/Glass Lewis rate boards on risk disclosure quality. |
| Regulatory Obligations | Product (+rental) | 0.62 | 0.90 | GDPR, SOX, HIPAA, PCI DSS, NYDFS 500, SEC cyber-disclosure rule (proposed Mar 2022, finalising in 2023) — well-understood regimes with accumulating case law. |
| Risk Appetite Statement | Custom Built | 0.40 | 0.88 | Every board has one; almost every one is bespoke; consultancies (Deloitte, PwC) sell the drafting; no generic template "just works". |
| Board Risk Reporting | Product (+rental) | 0.55 | 0.85 | Multiple GRC vendors (ServiceNow GRC, Archer, LogicGate, Diligent) offer board-reporting modules; still requires heavy bespoke wiring. |
| CISO Function | Product (+rental) | 0.55 | 0.80 | Role is now standard in large enterprises; reporting line (to CEO / CFO / CIO) still disputed; CISO salary benchmarks published annually. |
| Risk Identification Practice | Custom Built | 0.35 | 0.75 | Frameworks exist (NIST IDENTIFY), but the workshop-level practice is bespoke per company; consultancy-driven. |
| Risk Assessment Methodology | Custom Built | 0.45 | 0.72 | Multiple competing approaches (qualitative, semi-quant, FAIR); no dominant standard; most firms blend. |
| Compliance Frameworks (ISO 27001, SOC 2) | Commodity (+utility) | 0.82 | 0.68 | ISO 27001:2022 standard; SOC 2 Type II mandatory for SaaS B2B sales since ~2018; thousands of certified auditors; Vanta/Drata automate compliance-as-a-product. |
| Risk Frameworks (NIST CSF, ISO 31000) | Product (+rental) | 0.72 | 0.66 | NIST CSF 2.0 in draft May 2023; ISO 31000 widely referenced; training courses and certifications (CRISC) mature. |
| FAIR Quantification | Custom Built | 0.46 | 0.62 | Open FAIR standard; FAIR Institute growing; RiskLens (commercial tool) only real vendor — still adoption early, most boards see heatmaps not £ figures. |
| Likelihood / Impact Scoring | Commodity (+utility) | 0.78 | 0.60 | 5×5 scoring is ubiquitous; every audit firm uses it; criticised as pseudo-precise but universally deployed. |
| Risk Matrices (Heatmaps) | Commodity (+utility) | 0.85 | 0.58 | Red-amber-green is the universal boardroom visual; standard even though widely critiqued (Tony Cox, 2008). |
| Risk Register | Product (+rental) | 0.70 | 0.74 | GRC tools all ship risk-register modules; workflow is standardised; content is bespoke. |
| Mitigation / Transfer / Acceptance Mix | Custom Built | 0.42 | 0.62 | The 4-T decision (treat/transfer/tolerate/terminate) is framework-standard, but which control fits which risk is judgement-heavy. |
| Cyber Insurance | Product (+rental) | 0.58 | 0.55 | Hard market 2021–2023: premiums doubled, coverage shrank, ransomware exclusions standardising — vendors (AIG, Beazley, Coalition, At-Bay) maturing fast post-Lloyd's 2022 war-exclusion. |
| Asset Inventory | Product (+rental) | 0.65 | 0.52 | Every framework requires it; practice ranges from spreadsheet to CMDB; execution quality varies wildly. |
| CMDB / Asset Discovery Tools | Product (+rental) | 0.72 | 0.40 | ServiceNow CMDB, Axonius, Runzero, JupiterOne — mature commercial category. |
| Threat Intelligence Feeds | Product (+rental) | 0.66 | 0.42 | Recorded Future, Mandiant, CrowdStrike feeds; MISP open-source; STIX/TAXII standards; clear market. |
| Security Operations (SOC) | Product (+rental) | 0.55 | 0.50 | SOC-as-a-service a real category (Arctic Wolf, ReliaQuest, eSentire); in-house vs managed is an active build/buy call. |
| SIEM / XDR Tooling | Product (+rental) | 0.72 | 0.38 | Splunk, Sentinel, Chronicle, Elastic, Panther; XDR re-shuffle happening (CrowdStrike, SentinelOne, Palo Alto) but product market is dense and priced. |
| SOAR / Automation | Product (+rental) | 0.55 | 0.35 | Palo Alto XSOAR, Splunk SOAR, Tines; consolidation underway; bespoke playbooks still dominate. |
| Continuous Monitoring | Product (+rental) | 0.68 | 0.45 | 24/7 monitoring is expected practice; many service offerings; still requires bespoke tuning. |
| Vulnerability Management | Commodity (+utility) | 0.77 | 0.40 | Qualys, Tenable, Rapid7 — three-horse race since mid-2010s; utility-ish pricing; CVSS scoring standard. |
| Security Testing Programme | Product (+rental) | 0.52 | 0.48 | Most enterprises have one; scope and cadence bespoke; dominated by service models. |
| Penetration Testing | Product (+rental) | 0.70 | 0.42 | CREST/OSCP-qualified firms; ~1-2 week engagements priced openly; commoditising at the low end via pen-test-as-a-service (Cobalt, HackerOne PTaaS). |
| Bug Bounty | Product (+rental) | 0.60 | 0.35 | HackerOne, Bugcrowd, Intigriti, YesWeHack — platform market mature; programme design still bespoke and judgement-heavy. |
| Red Team Exercises | Custom Built | 0.45 | 0.38 | TIBER-EU, CBEST frameworks exist but every engagement is bespoke; practitioners are scarce senior talent. |
| Incident Response | Product (+rental) | 0.62 | 0.45 | IR retainers standard (Mandiant, Unit 42, Kroll, Coveware); NIST SP 800-61 sets process; execution quality varies. |
| IR Playbooks / Runbooks | Product (+rental) | 0.58 | 0.33 | Templates available; tabletop exercises standardised; content still customised to estate. |
| Forensics & Investigation | Product (+rental) | 0.50 | 0.30 | DFIR firms are a mature market; EnCase/FTK/Axiom commodity tools; still expert-led. |
| LLM-Assisted Defence (SOC copilot) | Genesis | 0.15 | 0.32 | May 2023 — Microsoft Security Copilot announced 28 Mar 2023 (preview only); Google Sec-PaLM announced Apr 2023; no GA product; wonder-press dominates literature. |
| LLM as Attack Vector | Genesis | 0.12 | 0.70 | OWASP LLM Top 10 project only started Apr 2023; ChatGPT Mar 2023 data-leak incident; prompt-injection and shadow-AI concerns emerging in board conversations. |
| LLM Governance Policy | Genesis | 0.18 | 0.58 | EU AI Act in trilogue; NIST AI RMF published Jan 2023; most boards have no policy yet — drafting is bespoke. |
| Security Expertise (internal) | Custom Built | 0.30 | 0.25 | CISSP, OSCP, CCSP certify baseline, but senior expertise is scarce, costly, and retained with difficulty; market still craft. |
| External Advisory / Consultancy | Product (+rental) | 0.55 | 0.22 | Big-4, Mandiant, IBM X-Force, boutiques — well-priced market of experts-for-hire. |
| Audit Evidence Collection | Product (+rental) | 0.70 | 0.28 | Drata, Vanta, Secureframe, Tugboat — GRC-automation category has matured fast 2021–2023. |
| Identity / SSO | Commodity (+utility) | 0.85 | 0.18 | Okta, Azure AD, Ping — utility-priced; OIDC/SAML standards; procurement routine. |
| Endpoint Protection (EDR) | Commodity (+utility) | 0.78 | 0.22 | CrowdStrike Falcon, Microsoft Defender, SentinelOne, Carbon Black — commodity feature set, price/performance competition. |
| Cloud Security Posture Management | Product (+rental) | 0.68 | 0.20 | Wiz, Prisma Cloud, Orca, Lacework — category exists since ~2019; Wiz's 2023 valuation run shows active product-market fit. |
| Logging / Log Storage | Commodity (+utility) | 0.90 | 0.12 | S3, CloudWatch, Loki, Elastic — utility billing, petabyte-scale, interchangeable. |
| Cloud Utilities (compute, storage, network) | Commodity (+utility) | 0.92 | 0.08 | AWS, Azure, GCP — per-second utility billing, commodity layer. |

---

## 3.1 — Mermaid rendering

> Note: the Mermaid `wardley-beta` conversion script is available but I could not execute it in this environment (sandbox blocks node execution of the bundled script against this path). The OWM block above is canonical and validates cleanly against the structural rules — paste it at [onlinewardleymaps.com](https://onlinewardleymaps.com/) to render.

---

## 4. Strategic analysis

### a. Differentiation opportunities (top 3)

1. **Risk Identification Practice** (Custom Built, deep in the value chain from the exec's perspective, ν=0.75) — the practice that actually shapes which risks ever reach the board. Still bespoke, consultancy-led, and the single biggest lever on whether the whole downstream apparatus is pointed at the right things. Differentiation here (better workshops, better taxonomy, better ingestion of emerging-tech risk) shifts the quality of everything downstream.
2. **FAIR Quantification** (Custom Built, transitioning, ε=0.46 → 0.65 target) — moving a board from heatmaps to £-quantified loss distributions is a genuine differentiator for the CISO and the CFO alike. Early movers get to set the quant baseline; laggards get shown quant by auditors five years later.
3. **Risk Appetite Statement** (Custom Built, highly visible to the board, ν=0.88) — a sharp appetite statement tied to loss quantiles beats the typical vague "low-to-moderate" wording. High user visibility (every board meeting touches it) and still pre-Product.

### b. Commodity-leverage candidates (top 3)

1. **Cloud Utilities** (Commodity +utility) — don't run self-hosted infra for security tooling; rent.
2. **Logging / Log Storage** (Commodity +utility) — petabyte-scale log retention is a utility; don't engineer a SIEM storage tier.
3. **Vulnerability Management**, **Endpoint Protection (EDR)**, **Identity / SSO** (all Commodity +utility) — the three most commoditised security-tool categories. Buy from the market leader, reassess on price every 2 years, do not build.

### c. Dependency risks (top 3)

1. **CISO Function → Security Expertise (internal)** — the whole translation layer from board to apparatus depends on scarce, hard-to-retain senior humans. If your CISO or two senior engineers leave, the risk register becomes noise.
2. **Risk Identification Practice → LLM as Attack Vector (Genesis)** — your entire risk identification apparatus depends on recognising a class of threat that is itself Genesis. Almost no risk register in May 2023 has prompt injection, shadow-ChatGPT, or training-data poisoning as populated rows.
3. **Forensics & Investigation → Security Expertise** — when the breach happens at 2am, the forensics hand-off to internal expertise is where evidence gets lost if the bench is thin.

### d. Build / Buy / Outsource recommendations

| Component | Stage | Recommendation | Why |
|---|---|---|---|
| Risk Appetite Statement | Custom Built | **Build** with external advisory | Board-facing, bespoke, genuine differentiator. |
| Risk Identification Practice | Custom Built | **Build** + retain external advisors | Core IP of the CISO function; drives everything downstream. |
| FAIR Quantification | Custom Built (transitioning) | **Build** with RiskLens or Open FAIR | Scarce tooling market; early-mover advantage with the board. |
| Risk Register | Product (+rental) | **Rent** (ServiceNow GRC, Archer, LogicGate) | Commercial market mature; no moat in in-house register software. |
| Cyber Insurance | Product (+rental), transitioning | **Buy** (named markets) — but price in aggressive premium increases | Market is hardening; waiting another year costs more and excludes more. |
| Compliance Frameworks | Commodity (+utility) | **Rent** automation (Drata/Vanta/Secureframe) | Audit-evidence collection is utility-grade; don't build internal tooling. |
| SIEM / XDR | Product (+rental) | **Buy** (Sentinel / Splunk / Chronicle / CrowdStrike) | Commercial market dense; in-house SIEMs are a sunk-cost trap. |
| SOC | Product (+rental) | **Outsource** the commodity tier; **Build** bespoke threat-hunting | MSSPs handle 24/7 L1/L2 cheaply; L3 hunters are where in-house differentiates. |
| Penetration Testing | Product (+rental) | **Buy** engagements; consider Cobalt-style PTaaS for continuous coverage | Skilled market, priced openly. |
| Bug Bounty | Product (+rental) | **Rent** platform (HackerOne/Bugcrowd); design in-house | Platform is commodity; programme design is still craft. |
| EDR / Identity / Logging / Cloud | Commodity (+utility) | **Rent** | Utility markets; re-tender every 2 years on price and integration. |
| LLM-Assisted Defence | Genesis | **Experiment small; don't commit** | Too early; Microsoft Security Copilot is preview-only in May 2023. |
| LLM Governance Policy | Genesis | **Build** quickly with external counsel | No one has a template; first-mover reduces exposure when the EU AI Act lands. |
| Red Team | Custom Built | **Buy** (CREST firms, TIBER-EU panel) | Expert market, not a build candidate at most enterprises. |

### e. Suggested gameplays

- **#1 Focus on user needs** — the exec's need is *risk visibility in £*, not a heatmap. Point the map at FAIR + Risk Register + Board Reporting.
- **#36 Directed investment** — concentrate spend on Risk Identification, FAIR Quantification, and SOC L3 threat-hunting. Harvest everywhere else.
- **#29 Harvesting** — SIEM/XDR, EDR, Identity, Logging, Cloud — take the best commercial offer; revisit on price.
- **#15 Open Approaches** on LLM Governance Policy — contribute to OWASP LLM Top 10, NIST AI RMF community; industry-scale cover is faster than single-company drafting.
- **#58 Pig in a poke** to watch for — MSSP contracts can lock you in; negotiate portability of detection logic.
- **#56 First mover** on cyber-insurance renewals — the market is hardening fast; lock in while coverage is broader.
- **#41 Alliances** — cyber-insurance carriers are starting to require specific controls (MFA, EDR, offline backups); align with one carrier's stack early.
- **#26 Differentiation** on CISO communication to the board — quant-led reporting is a hiring-magnet and a moat.
- **#18 Exploiting constraint** — the SEC cyber-disclosure rule (proposed 2022, finalising 2023) forces every public company to raise Board Risk Reporting quality; being six months ahead is a visible strategic win.

### f. Doctrine notes

- ✓ **#1 Focus on user needs** — map anchored on Executive / Board; their needs explicitly enumerated.
- ⚠ **#10 Know your users** — single anchor simplifies real governance (Board vs. Audit Committee vs. CEO vs. CFO vs. customers-as-beneficiaries-of-security). For a FTSE-100 company, re-split the anchor.
- ⚠ **#13 Manage inertia** — heavy inertia around heatmaps (form #1 past success, form #10 political capital) is a known blocker to FAIR adoption. Call it out to the board *before* it kills the programme.
- ✓ **#2 Use a systematic mechanism of learning** — Continuous Monitoring → SIEM → SOAR loop is built in; Risk Register should feed from incident post-mortems (currently often doesn't).
- ⚠ **#29 Listen to your ecosystem** — LLM components are present but many organisations' ecosystems haven't surfaced shadow-AI risk yet; the map makes it visible deliberately.

### g. Climatic context

Seven of the 27 climatic patterns are actively shaping this map:

- **#3 Everything evolves** — cyber insurance, pen-testing-as-a-service, compliance automation and LLM governance are all mid-transition.
- **#11 Past success breeds inertia** — heatmaps are still boardroom standard despite two decades of critique.
- **#15–17 Inertia forms** — sunk cost in existing GRC tools, political capital in risk-matrix culture, skill scarcity in FAIR.
- **#18 You cannot measure evolution over time or adoption** — the LLM components are placed by cheat-sheet indicators, not by how long they've existed.
- **#27 Product-to-utility punctuated equilibrium** — Compliance Automation (Drata/Vanta) is actively punctuating the traditional audit-consultancy market; EDR is mid-commoditisation.
- **#8 Components can coevolve with practice** — LLM-Assisted Defence will coevolve with LLM-safety-engineering practice over the next 2–3 years; don't place the practice as mature before the component is.
- **#12 Efficiency enables innovation** — commoditised Cloud/Logging/EDR *is the reason* anyone can afford to experiment with LLM defence at all.

### h. Deep-placement notes

I ran closer checks on five components where cheat-sheet priors were uncertain in May 2023:

1. **Cyber Insurance (ε=0.58 → 0.72 target)** — initial instinct Product-early. Checking the hard-market literature (Lloyd's 2022 exclusions, Coalition/At-Bay growth, ransomware premium doubling 2021–2022) and the standardising exclusions (war, ransomware, acts of state) confirms it's Product actively industrialising toward utility. Moved to 0.58.
2. **Compliance Frameworks (ε=0.82)** — initial instinct Product. Looking at Drata/Vanta/Secureframe's growth through 2022–2023, the trajectory is clearly commoditisation: controls library → automated evidence collection → continuous compliance. SOC 2 Type II is now table-stakes for B2B SaaS. Stage IV confirmed.
3. **Bug Bounty (ε=0.60 → 0.75 target)** — HackerOne/Bugcrowd are platforms but programme design (scope, payout curves, triage SLAs) remains bespoke. Placed at early Product; `evolve` arrow points to commoditisation as the platforms absorb more design work.
4. **LLM-Assisted Defence (ε=0.15)** — Microsoft Security Copilot was only announced 28 March 2023 (preview). Google's Sec-PaLM announcement April 2023. No GA product in May 2023. Genesis is correct; `evolve` to 0.45 by ~2025 is a plausible scenario.
5. **FAIR Quantification (ε=0.46 → 0.65 target)** — the FAIR Institute has been active since 2014 but adoption is still minority; RiskLens is the only notable commercial tool. Custom Built is correct; the evolve points at Product as more GRC tools integrate FAIR workflows (mid-decade).

### i. Caveat

Evolution trajectories (the `evolve` arrows) are **scenarios, not forecasts**. Wardley's climatic pattern #18: *"you cannot measure evolution over time or adoption."* Every dated reference in this map (SEC rule, AI Act, insurance-market hardening) is a stated condition in May 2023, not a prediction about when transitions complete.

---

## Map verification

- **Validator (structural):** OWM draft was written to `./draft.owm` alongside this file. Per the skill's §5.5, I attempted to run `node skills/wardley-map/scripts/validate_owm.mjs` against it; the bash invocation was denied by the sandbox permission policy in this environment. I instead walked every edge (~64 edges) manually against the validator's three rules:
  1. All coordinates in [0, 1] — confirmed.
  2. All edge endpoints declared — confirmed (every source/target matches a declared `anchor`/`component`).
  3. ν(source) ≥ ν(target) — two violations were found and fixed: `Risk Register → Risk Assessment Methodology` (Register raised to ν=0.74) and `Mitigation Mix → LLM Governance Policy` (Governance lowered to ν=0.58 and its outgoing edge re-pointed from the Attack Vector to the Defence component so governance sits correctly in the mitigation chain).
- **Layout check (advisory):** also walked manually. One near-duplicate collision was fixed (SOC at [0.50, 0.55] and Security Testing at [0.48, 0.55] were Δν=0.02; nudged Security Testing to ε=0.52). One additional Mitigation Mix / FAIR collision was fixed (Mitigation Mix moved to ε=0.42). One canvas-edge clip on the anchor (ν=0.99 → 0.96). One stage-boundary straddle (Vuln Mgmt ε=0.75 → 0.77; FAIR ε=0.48 → 0.46) fixed.
- **Stage distribution:** Genesis 3 (7%), Custom Built 7 (17%), Product 23 (56%), Commodity 8 (20%). Product-heavy, which fits the scenario's framing question (commoditised-vs-expert-judgement is precisely about where Stage III ends).
- **Component count:** 41 components + 1 anchor. Within the 35–45 target band for a "landscape of an industry or domain" per the density guidance.
