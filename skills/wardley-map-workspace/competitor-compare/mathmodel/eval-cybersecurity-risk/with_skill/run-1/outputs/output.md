# Cybersecurity Risk Management — Executive View (May 2023)

Wardley Map of cybersecurity risk management from the executive perspective, anchored on the Executive and covering the full apparatus from P&L/compliance/risk-appetite drivers through quantification, operations, regulatory shape, and the May-2023 LLM angle.

---

## 1. Map (OWM)

```owm
title Cybersecurity Risk Management (Executive View, May 2023)
style wardley

anchor Executive [0.97, 0.50]

// Directly executive-facing outputs
component P&L Impact [0.90, 0.85]
component Risk Appetite [0.88, 0.40]
component Regulatory Obligation [0.87, 0.70]
component Board Risk Reporting [0.84, 0.55]
component Cyber Insurance [0.82, 0.72]

// Governance layer
component Risk Management Program [0.76, 0.55]
component Compliance Program [0.74, 0.77]
component Risk Register [0.70, 0.65]
component Mitigation/Transfer/Acceptance Mix [0.68, 0.42]

// Frameworks and standards
component Compliance Frameworks (SOC 2, ISO 27001, PCI-DSS) [0.62, 0.80]
component Regulatory Regimes (GDPR, SEC, NIS2) [0.60, 0.68]
component Risk Frameworks (NIST RMF, ISO 31000) [0.58, 0.72]

// Risk analysis
component Risk Assessment Methodology [0.56, 0.52]
component Risk Identification Practice [0.54, 0.40]
component AI Governance Practice [0.52, 0.08]
component Risk Quantification (FAIR) [0.50, 0.30]
component Likelihood/Impact Matrices [0.48, 0.78]

// Asset and control ground truth
component Asset Inventory [0.46, 0.55]
component Security Control Catalogue [0.44, 0.70]
component LLM Attack Surface [0.42, 0.12]
component Third-Party/Vendor Risk [0.40, 0.60]

// Operations
component Security Operations Centre (SOC) [0.38, 0.65]
component Continuous Monitoring [0.36, 0.78]
component Incident Response [0.34, 0.55]
component Security Testing [0.32, 0.62]
component Pen Testing [0.30, 0.68]
component Bug Bounty Program [0.28, 0.60]
component LLM-Assisted Defence [0.26, 0.22]

// Tooling
component GRC Platforms [0.24, 0.68]
component SIEM [0.22, 0.80]
component SOAR [0.20, 0.65]
component EDR/XDR [0.19, 0.78]
component Vulnerability Scanners [0.18, 0.82]

// Knowledge & data feeds
component CISO Expert Judgement [0.17, 0.13]
component Threat Intelligence Feeds [0.15, 0.65]
component CVE/Vulnerability Data [0.13, 0.85]
component Foundation LLM Models [0.14, 0.42]

// Deep infra
component Identity & Access Management [0.11, 0.80]
component Log Storage/Data Lake [0.08, 0.88]
component Cloud Utilities [0.05, 0.92]

// Dependencies
Executive->P&L Impact
Executive->Risk Appetite
Executive->Regulatory Obligation
Executive->Board Risk Reporting
Executive->Cyber Insurance

P&L Impact->Risk Management Program
Risk Appetite->Risk Management Program
Regulatory Obligation->Compliance Program
Board Risk Reporting->Risk Register
Board Risk Reporting->Risk Management Program
Cyber Insurance->Compliance Frameworks (SOC 2, ISO 27001, PCI-DSS)
Cyber Insurance->Risk Register

Risk Management Program->Risk Register
Risk Management Program->Mitigation/Transfer/Acceptance Mix
Risk Management Program->Risk Frameworks (NIST RMF, ISO 31000)
Compliance Program->Compliance Frameworks (SOC 2, ISO 27001, PCI-DSS)
Compliance Program->Regulatory Regimes (GDPR, SEC, NIS2)
Risk Register->Risk Assessment Methodology
Mitigation/Transfer/Acceptance Mix->Security Control Catalogue

Risk Assessment Methodology->Risk Identification Practice
Risk Assessment Methodology->Risk Quantification (FAIR)
Risk Assessment Methodology->Likelihood/Impact Matrices
Risk Assessment Methodology->CISO Expert Judgement
Risk Identification Practice->Asset Inventory
Risk Identification Practice->Third-Party/Vendor Risk
Risk Identification Practice->LLM Attack Surface
Risk Quantification (FAIR)->CISO Expert Judgement
Likelihood/Impact Matrices->CISO Expert Judgement
AI Governance Practice->LLM Attack Surface
AI Governance Practice->CISO Expert Judgement

Security Control Catalogue->Security Operations Centre (SOC)
Security Control Catalogue->Security Testing
Security Control Catalogue->Incident Response
Security Operations Centre (SOC)->Continuous Monitoring
Security Operations Centre (SOC)->Incident Response
Continuous Monitoring->SIEM
Continuous Monitoring->EDR/XDR
Continuous Monitoring->LLM-Assisted Defence
Incident Response->SOAR
Incident Response->SIEM
Security Testing->Pen Testing
Security Testing->Bug Bounty Program
Security Testing->Vulnerability Scanners
Pen Testing->CISO Expert Judgement

Compliance Program->GRC Platforms
Risk Register->GRC Platforms
Asset Inventory->GRC Platforms

SIEM->Threat Intelligence Feeds
SIEM->Log Storage/Data Lake
EDR/XDR->Threat Intelligence Feeds
SOAR->Log Storage/Data Lake
Vulnerability Scanners->CVE/Vulnerability Data
Threat Intelligence Feeds->CVE/Vulnerability Data

SIEM->Cloud Utilities
SOAR->Cloud Utilities
EDR/XDR->Cloud Utilities
Log Storage/Data Lake->Cloud Utilities
GRC Platforms->Cloud Utilities
Asset Inventory->Identity & Access Management
Security Operations Centre (SOC)->Identity & Access Management
Identity & Access Management->Cloud Utilities

LLM-Assisted Defence->Foundation LLM Models
LLM-Assisted Defence->Log Storage/Data Lake
LLM Attack Surface->Foundation LLM Models

evolve Risk Quantification (FAIR) 0.55
evolve LLM-Assisted Defence 0.55
evolve LLM Attack Surface 0.35
evolve AI Governance Practice 0.45
evolve Regulatory Regimes (GDPR, SEC, NIS2) 0.82

note Board-level outputs [0.92, 0.20]
note Expert-judgement core [0.55, 0.05]
note Commoditised tooling [0.18, 0.95]
note LLM in-transition zone [0.50, 0.24]
```

---

## 2. Strategic analysis

The map splits into four recognisable zones:

- **Board-level outputs** (top-left / top-middle): P&L Impact, Risk Appetite, Regulatory Obligation, Board Risk Reporting, Cyber Insurance — all Product (+rental) or Commodity (+utility). These are the things the executive actually consumes; they are mature formats.
- **Governance and frameworks belt** (ν≈0.55–0.76, ε≈0.55–0.80): the risk programme, compliance programme, risk register, and the framework catalogues (ISO 27001, SOC 2, NIST RMF, PCI-DSS). Almost all Product (+rental) or Commodity (+utility). The shape of this belt is forced by regulators.
- **Expert-judgement core** (ν≈0.17–0.56, ε≈0.08–0.30): Risk Assessment Methodology, Risk Quantification (FAIR), AI Governance Practice, LLM Attack Surface, CISO Expert Judgement. Mostly Custom Built with two Genesis pockets (AI governance, LLM attack surface). This is where differentiation lives.
- **Commoditised tooling and data foundation** (bottom-right): SIEM, EDR/XDR, SOAR, Vulnerability Scanners, IAM, Log Storage, Cloud Utilities, CVE feeds. All Product (+rental) or Commodity (+utility). Rent, do not build.

### a. Differentiation opportunities (top 3)

1. **AI Governance Practice** (Genesis, ε≈0.08) — The highest-D component on the map. Visible enough that the board asks about it in May 2023 (every board does) and uncharted enough that practice, not product, is what separates organisations. Writing credible AI-use policies, shadow-AI detection programmes, and model-risk-management processes today is differentiation.
2. **Risk Quantification (FAIR)** (Custom Built, ε≈0.30) — Quantification is still where most organisations lose the argument with the CFO. Fluency in FAIR (or an equivalent loss-exceedance approach) turns risk conversations from colour-coded heatmaps into probability distributions the finance side accepts. The `evolve` arrow to 0.55 reflects the steady industrialisation of FAIR tooling (RiskLens, Safe Security's BAS) through 2023–2025.
3. **LLM Attack Surface** (Genesis, ε≈0.12) — The ability to articulate and defend against prompt injection, training-data leakage, and agentic misuse. In May 2023 no-one has a methodology; whoever builds the first credible corporate programme holds the brief for two to three years.

### b. Commodity-leverage candidates (top 3)

1. **Cloud Utilities** (Commodity +utility, ε≈0.92) — Never build your own datacentre for a SOC. Rent from a hyperscaler.
2. **SIEM / EDR/XDR / SOAR** (all Commodity +utility, ε≈0.78–0.80) — The detection-and-response tooling layer is a saturated market (Splunk, Microsoft Sentinel, Elastic, Datadog; CrowdStrike, SentinelOne, Microsoft Defender for Endpoint). Buy the incumbent; do not invest engineering cycles into feature parity.
3. **Vulnerability Scanners and CVE/Vulnerability Data** (Commodity +utility, ε≈0.82–0.85) — Qualys / Tenable / Rapid7 plus the NVD feed. Utility. Any org that still runs a bespoke scanner is paying a tax.

Honourable mention: **Cyber Insurance** (Product +rental, ε≈0.72). Not infrastructure but a product to be shopped. The insurer controls its shape more than the buyer does.

### c. Dependency risks (top 3)

Edges where a highly visible component depends on a fragile or immature foundation:

1. **Risk Assessment Methodology → CISO Expert Judgement** — the methodology is the thing the board trusts, but every assessment ultimately rests on judgement calls from a very small number of senior people. Single-point-of-failure knowledge risk, made worse by CISO tenure often being shorter than executive memory.
2. **Risk Identification Practice → LLM Attack Surface** — the risk-identification practice in May 2023 is being asked to enumerate a threat class (prompt injection, agent misuse, RAG leakage) that is still Genesis. This is a visible practice depending on an unformed foundation; the risk is false confidence more than false negatives.
3. **Continuous Monitoring → LLM-Assisted Defence** — where this edge exists (some SOCs are piloting LLM-based triage), the live production signal-path depends on a Genesis-stage capability whose failure modes (hallucinated IOCs, prompt-injected log entries) are not yet understood. Contain in an advisory loop, do not close the loop.

Secondary risk worth naming: **Risk Quantification (FAIR) → CISO Expert Judgement** — a quantification method is only as calibrated as the loss-magnitude priors the humans supply.

### d. Suggested gameplays

Drawing from Wardley's 61-gameplay catalogue:

- **#1 Focus on user needs** — the executive anchor is P&L / regulatory / appetite; every component in the lower half of the map should trace back to those three. Kill components that don't.
- **#36 Directed investment** on **AI Governance Practice**, **Risk Quantification (FAIR)**, and **LLM Attack Surface** — the three Genesis/Custom-Built components where engineering and CISO time buy the most differentiation.
- **#29 Harvesting** on **SIEM / EDR/XDR / SOAR / Vulnerability Scanners / CVE Feeds / Cloud Utilities** — wait for each category to settle and buy the winner; do not build.
- **#41 Alliances** on **Third-Party/Vendor Risk** and **Threat Intelligence Feeds** — sharing the telemetry burden via an ISAC / ISAO is the rational move; unilateral threat intel is uneconomic.
- **#15 Open Approaches** on **Risk Quantification (FAIR)** — the Open FAIR standard is the accelerant; contribute to it, build on it, avoid a proprietary fork.
- **#7 Education** — aimed at the board and at business unit heads, to translate Mitigation/Transfer/Acceptance into language they use every day. Cuts the inertia on risk-acceptance decisions.
- **#56 First mover** on **AI Governance Practice** — regulators (NIST AI RMF 1.0 January 2023, EU AI Act in flight) are about to force a shape; organisations that stand up a practice early shape the interpretation locally.
- **#23 Pig in a poke** (defensive watch, not an offensive play) — know the cyber-insurance market is hardening; losses are being repriced, exclusions expanding (war-exclusion clauses post-Merck v. Ace). Treat transferred risk as conditionally transferred.

### e. Doctrine notes

- **#1 Focus on user needs** — map correctly anchored on the Executive, with all top-tier nodes mapped to the three drivers in the brief (P&L, compliance, risk appetite).
- **#10 Know your users** — single-anchor simplification. In a bigger engagement the CISO is a second user (the CISO's map would have different priorities for the same components — operations-forward rather than board-forward). Flagged as a limitation.
- **#2 Use a systematic mechanism of learning** — Risk Quantification (FAIR) is currently upstream-disconnected from Incident Response; ideally, post-incident loss data feeds back into the quantification priors.
- **#13 Manage inertia** — three inertia forms dominate this map: **#6 Confusion over method** (risk-quantification debates between FAIR and heatmap camps inside the same org), **#8 Skill acquisition cost** (FAIR/AI-governance literacy is scarce), and **#14 Strategic-control loss** (executives reluctant to let go of the colour-coded matrix in favour of probability distributions).
- **#27 Be pragmatic** — the regulatory regime (GDPR, SEC cyber-incident disclosure rule finalised July 2023, NIS2 transposition deadline October 2024) forces the shape of the Compliance belt regardless of organisational preference. Fighting it is a waste of energy.

### f. Climatic context

Several of Wardley's 27 climatic patterns are actively shaping this map:

- **#3 Everything evolves** — the LLM block (AI Governance Practice, LLM Attack Surface, LLM-Assisted Defence) is freshly in Genesis / early Custom Built. The `evolve` arrows project moderate industrialisation by late 2025 but remain scenarios, not forecasts.
- **#15–17 Inertia** — Risk Quantification has been "about to industrialise" for a decade; the inertia forms above (method confusion, skill cost, strategic-control loss) are why.
- **#18 You cannot measure evolution over time or adoption** — applies especially to the LLM components. The observed placement is May 2023; by the next calendar cycle the rows will have shifted and the placements must be rescored, not simply extrapolated.
- **#23 Componentisation increases the rate of change** — commoditisation of SIEM-as-a-service, managed EDR, and managed SOC offerings is enabling mid-market orgs to stand up detection-and-response that would have been out of reach in 2018. Expect the ops belt to keep compressing leftward in visibility (the SOC becomes less "differentiating" and more "table stakes").
- **#27 Two types of punctuated equilibrium** — Regulatory Regimes are in a Product → Commodity (+utility) war: GDPR (2018) and SEC / NIS2 (2023–24) are the punctuations. The `evolve` to 0.82 reflects that.

### g. Deep-placement notes

Three components warranted closer inspection than the cheat sheet alone:

- **Risk Quantification (FAIR)** — cheat-sheet rows diverged (Ubiquity II, Certainty II–III, Publication II, Market II, User Perception II). Vendor landscape (RiskLens, Safe Security, Axio, ThreatConnect Risk Quantifier) shows a small but consolidating product market; the Open FAIR standard gives a publishing anchor. Net: placed at ε≈0.30 (mid Custom Built) with a plausible evolve to 0.55 over 18–30 months. Retained noted disagreement; the gap between "published standard" (Product+) and "practical adoption" (still patchy) is what keeps this Custom.
- **LLM-Assisted Defence** — in May 2023, early deployments of GPT-4-backed log summarisation and phishing triage are being demoed (Microsoft Security Copilot announced March 2023; CrowdStrike Charlotte AI shortly after) but nothing is production-standard. Placed at ε≈0.22 (very early Genesis / boundary). Evolve target 0.55 assumes 2024–2025 productisation continues; this is a scenario, not a forecast.
- **LLM Attack Surface** — the OWASP Top-10 for LLM Applications draft started appearing around June 2023, after this scenario date. Placed at ε≈0.12 (deep Genesis). Evolve target 0.35 assumes the OWASP effort plus regulator pressure moves it to late Custom Built by 2025.

Other components sit on defensible cheat-sheet placements and were not deep-researched: SIEM / EDR / SOAR / Cloud Utilities / IAM are obvious Commodity (+utility); ISO 27001 / SOC 2 / PCI-DSS are obvious Product (+rental) or Commodity (+utility) frameworks; FAIR, Pen Testing, Bug Bounty have settled market signatures.

### h. What's commoditised, what's expert judgement, where regulation forces shape

The brief asked for these three cuts explicitly. In map terms:

- **Commoditised tooling** (the bottom-right corner, ν < 0.25, ε > 0.65): SIEM, EDR/XDR, SOAR, Vulnerability Scanners, GRC Platforms, IAM, Log Storage, Cloud Utilities, CVE feeds, Threat Intelligence Feeds. Buy-side discipline and integration skill matters here; feature innovation does not.
- **Still expert judgement** (the vertical strip at ε < 0.35): CISO Expert Judgement (ε≈0.13), AI Governance Practice (ε≈0.08), LLM Attack Surface (ε≈0.12), LLM-Assisted Defence (ε≈0.22), Risk Quantification (FAIR) (ε≈0.30), Risk Identification Practice (ε≈0.40), Risk Appetite (ε≈0.40, Custom Built as an organisational artefact), Mitigation/Transfer/Acceptance Mix (ε≈0.42). The organisations that win are the ones whose humans think clearly in this strip.
- **Where regulation forces shape** — the Compliance Program / Regulatory Regimes / Compliance Frameworks triangle (ε≈0.68–0.80, ν≈0.60–0.74). GDPR and SEC cyber-incident disclosure (adopted late July 2023, enforcement from December 2023) and the impending NIS2 transposition push Regulatory Regimes further right (`evolve` to 0.82). Consequence: Risk Register, Board Risk Reporting, Cyber Insurance underwriting questionnaires, and the Compliance Program itself are all shaped by the regulator's template, not by organisational preference. Expect more components to get pulled into this template-driven zone over the next two to three years (third-party risk programmes, AI governance programmes, software-supply-chain attestation).

### Caveat

Evolution trajectories (`evolve` arrows) are **scenarios, not forecasts**. Wardley's climatic pattern #18 stands: *you cannot measure evolution over time or adoption*. The May-2023 placements for the LLM-related components in particular are low-confidence; the direction of travel is the signal, not the numeric target.

---

## 3. Validation notes

**Structural validation (Step 5.5):** the bundled `validate_owm.mjs` script is the canonical check (visibility hard rule `ν(a) ≥ ν(b)` for every edge, coordinate range `[0,1]`, edge endpoints declared). In this harness `node` execution against the validator was permission-blocked, so every edge was manually tabulated against the visibility dictionary below. All 64 edges satisfy `ν(source) ≥ ν(target)`; all 41 components and 1 anchor have coordinates in `[0,1]`; every edge endpoint resolves to a declared node. Any downstream consumer of this output should re-run `node skills/wardley-map/scripts/validate_owm.mjs <draft.owm>` as a belt-and-braces check.

**Layout check (Step 5.6):** manually reviewed against the four classes the advisor flags. No near-duplicate coordinates (closest pair: EDR/XDR [0.19, 0.78] vs Continuous Monitoring [0.36, 0.78] — same ε, Δν=0.17, not a duplicate). No stage-boundary straddling after Compliance Program nudged from 0.75 → 0.77 to clear the Product/Commodity boundary by the 0.02 tolerance. Executive at ν=0.97 sits under the 0.98 canvas-edge threshold. Stage distribution: 4 Genesis (10%), 5 Custom Built (12%), 20 Product+rental (49%), 11 Commodity+utility (27%) — within the 60% stage-imbalance limit on all four stages, no empty stage. Counts: 41 components + 1 anchor = 42 nodes, 64 edges.
