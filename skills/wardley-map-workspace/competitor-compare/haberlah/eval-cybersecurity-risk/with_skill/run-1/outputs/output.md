# Wardley Map Analysis: Cybersecurity Risk Management from the Executive Seat (May 2023)

## Purpose

The decision this map informs: **as a board or executive in mid-2023, where is cybersecurity risk management a commoditised buy, where is it still expert judgement, and where are regulatory obligations forcing the shape of the apparatus?** The map anchors on executives because that is the seat from which P&L, compliance, and risk appetite are actually resolved into spend on the downstream security apparatus.

The map is dated to May 2023 deliberately. That month sits just after GPT-4's release (Mar 2023), the public naming of prompt injection by Simon Willison (Sep 2022 coined, widely cited by early 2023), Samsung's ChatGPT data-leak incident (Apr 2023), and the announcement of Microsoft Security Copilot (Mar 2023). The LLM components on this map are therefore firmly Genesis; the picture would be very different even 12 months later.

---

## Strategic Context

- **Strategic question:** Where should executive spend, attention, and accountability land across the cybersecurity risk-management value chain in May 2023?
- **User anchor:** Executives — the board and C-suite, as specified.
- **Core needs (executive-level):** protect P&L, meet compliance obligations, hold exposure inside the stated risk appetite.
- **Scope boundary:** One enterprise's cybersecurity risk-management function, single main map. 22 components + 1 anchor. Over the 8-15 target because the scenario explicitly calls out three governance pillars, two framework families, three decision options, one insurance market, six operational pillars, and the LLM dyad. A submap split is flagged under Open Questions.

---

## Deliverable 1 — OWM Text Block

```owm
title Cybersecurity Risk Management from the Executive Seat (May 2023)
style wardley

anchor Executives [0.97, 0.50]

component P&L [0.90, 0.86]
component Compliance Obligation [0.88, 0.80]
component Risk Appetite [0.86, 0.32] inertia
component Risk Register [0.78, 0.60]
component Risk Frameworks [0.74, 0.68]
component Compliance Frameworks [0.74, 0.84]
component Risk Identification [0.68, 0.38]
component Risk Assessment Methodology [0.64, 0.32] inertia
component Asset Inventory [0.60, 0.56]
component Likelihood/Impact Matrices [0.56, 0.74]
component FAIR Quantification [0.56, 0.22]
component Mitigate/Transfer/Accept [0.54, 0.36]
component Cyber Insurance [0.50, 0.54]
component Security Reporting [0.48, 0.64]
component Security Monitoring [0.42, 0.60]
component SOC Tooling (SIEM/EDR) [0.36, 0.66]
component Incident Response [0.32, 0.44] inertia
component Security Testing [0.28, 0.56]
component Pen Testing [0.24, 0.38] inertia
component Bug Bounty [0.20, 0.54]
component LLM for Defence [0.14, 0.14]
component LLM as Risk [0.10, 0.06]

Executives->P&L
Executives->Compliance Obligation
Executives->Risk Appetite
P&L->Risk Register
P&L->Cyber Insurance
Compliance Obligation->Compliance Frameworks
Compliance Obligation->Risk Frameworks
Compliance Obligation->Risk Register
Risk Appetite->Risk Register
Risk Appetite->Mitigate/Transfer/Accept
Risk Register->Risk Identification
Risk Register->Risk Assessment Methodology
Risk Identification->Asset Inventory
Risk Assessment Methodology->Likelihood/Impact Matrices
Risk Assessment Methodology->FAIR Quantification
Risk Frameworks->Risk Assessment Methodology
Risk Frameworks->Security Monitoring
Risk Frameworks->Incident Response
Compliance Frameworks->Security Testing
Compliance Frameworks->Security Reporting
Mitigate/Transfer/Accept->Cyber Insurance
Mitigate/Transfer/Accept->Security Reporting
Mitigate/Transfer/Accept->Incident Response
Mitigate/Transfer/Accept->Security Testing
Security Reporting->Security Monitoring
Security Monitoring->SOC Tooling (SIEM/EDR)
Incident Response->SOC Tooling (SIEM/EDR)
Security Testing->Pen Testing
Security Testing->Bug Bounty
SOC Tooling (SIEM/EDR)->LLM for Defence
Incident Response->LLM for Defence
Pen Testing->LLM as Risk
Risk Register->LLM as Risk
Asset Inventory->LLM as Risk

evolve FAIR Quantification 0.45
evolve Risk Assessment Methodology 0.52
evolve Pen Testing 0.56
evolve Incident Response 0.60
evolve Cyber Insurance 0.70
evolve LLM for Defence 0.38
evolve LLM as Risk 0.32

annotation 1 [[0.22, 0.12]] LLM angle: Genesis on both sides of the sword
annotation 2 [[0.32, 0.36]] Still expert craft; automation pressure rising
annotation 3 [[0.54, 0.30]] Mitigate/Transfer/Accept is where P&L meets cyber
annotation 4 [[0.76, 0.66]] Regulation is forcing Register+Frameworks rightward
```

---

## Deliverable 2 — Component Evolution Assessment

| Component | Stage | Position [vis, mat] | Rationale |
|---|---|---|---|
| Executives | Anchor | [0.97, 0.50] | Board / C-suite; the seat where P&L, compliance, and risk appetite are resolved into spend. |
| P&L | Commodity (+Utility) | [0.90, 0.86] | Profit-and-loss accounting is entirely codified (GAAP, IFRS), taught everywhere, failure is catastrophic. Invisible until it moves. |
| Compliance Obligation | Commodity | [0.88, 0.80] | The fact of being legally obligated is universal; the obligation itself is not a product — it is an input. Treated here as a commoditised condition of doing business. |
| Risk Appetite | Custom-Built (inertia) | [0.86, 0.32] | ISO 31000 / COSO ERM give scaffolding, but each board's appetite statement is bespoke, qualitative, and rarely quantified. Inertia: boards resist being tied to quantified risk budgets because it exposes them to accountability. |
| Risk Register | Product | [0.78, 0.60] | GRC platforms (Archer, ServiceNow GRC, LogicGate, Hyperproof, OneTrust) are mature with feature-competition; every enterprise above a certain size has one. |
| Risk Frameworks | Product | [0.74, 0.68] | NIST CSF, ISO 27001, CIS Controls, NIST 800-53 — multiple competing frameworks with certification bodies and training markets. Drifting toward Commodity. |
| Compliance Frameworks | Commodity | [0.74, 0.84] | SOX, PCI-DSS, HIPAA, GDPR, CCPA, SOC 2 — enshrined in law or contract, fully codified, non-negotiable, auditable against bright-line checklists. |
| Risk Identification | Custom-Built | [0.68, 0.38] | STRIDE, PASTA, OCTAVE, attack-tree analysis — techniques exist and are trainable, but the practice of running them in a real organisation is specialist and bespoke. |
| Risk Assessment Methodology | Custom-Built (inertia) | [0.64, 0.32] | The choice of methodology (qualitative vs FAIR vs mixed) is still religiously debated; every firm mixes its own blend. Inertia: GRC incumbents and risk-consultancy revenue resist methodology standardisation. |
| Asset Inventory | Product | [0.60, 0.56] | Axonius, Lansweeper, ServiceNow CMDB, JupiterOne — multiple vendors, published pricing, feature competition. Still incomplete in practice at most firms, but the tooling is productised. |
| Likelihood/Impact Matrices | Commodity | [0.56, 0.74] | Heat maps (3×3, 5×5) appear in every board pack. Utterly standardised. Widely criticised for innumeracy but universal. |
| FAIR Quantification | Genesis | [0.56, 0.22] | Factor Analysis of Information Risk is recognised (FAIR Institute, The Open Group OpenFAIR) but in May 2023 production deployments at scale are rare; mostly pilots and consulting engagements. |
| Mitigate/Transfer/Accept | Custom-Built | [0.54, 0.36] | The three-option decision taxonomy is well-established doctrine but the per-risk decisions are bespoke per firm, per risk, per financial year. |
| Cyber Insurance | Product | [0.50, 0.54] | A defined market (Beazley, AIG, Chubb, Travelers, Munich Re, Hiscox) with published capacity and rated products. But in May 2023 the market is mid-hardening: premiums up 50-150% YoY, ransomware sub-limits, war exclusions post-NotPetya/Mondelez ruling. |
| Security Reporting | Product | [0.48, 0.64] | KPI dashboards, CISO board packs, MTTR/MTTD metrics — productised across most SIEM platforms and GRC tools. |
| Security Monitoring | Product | [0.42, 0.60] | MDR/MSSP market mature (CrowdStrike Falcon Complete, Arctic Wolf, Expel, Secureworks). Buying monitoring as a service is normal. |
| SOC Tooling (SIEM/EDR) | Product | [0.36, 0.66] | Splunk, Microsoft Sentinel, Elastic Security, CrowdStrike, SentinelOne, Defender — crowded, well-differentiated, Gartner-Magic-Quadranted. Drifting toward Commodity in the core SIEM function. |
| Incident Response | Custom-Built (inertia) | [0.32, 0.44] | IR retainers are a market (Mandiant, Unit 42, Kroll, CrowdStrike Services), but the response to any given incident is bespoke, requires senior forensic judgement. Inertia: IR firms earn margins on bespoke work; resist productisation. |
| Security Testing | Product | [0.28, 0.56] | DAST/SAST/SCA tooling (Qualys, Nessus, Snyk, Veracode, Checkmarx) is mature and feature-competitive. |
| Pen Testing | Custom-Built (inertia) | [0.24, 0.38] | Boutique pen-test firms dominate; output quality is operator-dependent. PTaaS (Cobalt, HackerOne Pentest) is emerging but the core is still a craft. Inertia: consultancy day-rate business model resists automation. |
| Bug Bounty | Product | [0.20, 0.54] | HackerOne, Bugcrowd, Intigriti, YesWeHack — the marketplace pattern is mature, standardised payout structures, VDP vs paid tiers well-defined. |
| LLM for Defence | Genesis | [0.14, 0.14] | Microsoft Security Copilot announced Mar 2023, no GA. Google Sec-PaLM in preview. No production deployments at scale. Every SOC vendor has a roadmap slide; no evidence of operational value yet. |
| LLM as Risk | Genesis | [0.10, 0.06] | In May 2023: ChatGPT data-leak (Samsung, Apr 2023), prompt injection named and being weaponised, hallucinated legal citations (Mata v Avianca happening in real time), no clear controls. Risk register category is still being invented. |

---

## Deliverable 3 — Key Strategic Observations

1. **The map has two obvious stripes of commodity and one obvious stripe of Genesis, and the expert-judgement work lives in the middle.** Stripe 1 (Commodity, top-right): P&L, Compliance Obligation, Compliance Frameworks, Likelihood/Impact matrices. Stripe 2 (Commodity / late Product, middle-right): SOC Tooling, Asset Inventory, Bug Bounty, Risk Register. Stripe 3 (Genesis, bottom-left): FAIR Quantification, LLM for Defence, LLM as Risk. The middle band — Risk Appetite, Risk Assessment Methodology, Mitigate/Transfer/Accept, Incident Response, Pen Testing — is where actual human judgement lives, and that band is where most inertia markers cluster.

2. **Regulation is the strongest single force on the map.** Compliance Obligation (0.88, 0.80) → Compliance Frameworks (0.74, 0.84) → Security Testing + Security Reporting. The Compliance Frameworks column at 0.84 is the rightmost non-P&L component; compliance regimes pull the apparatus beneath them rightward (testing, reporting, monitoring) because those are the auditable evidence. Risk Frameworks (0.68) does the same for monitoring and incident response via NIST CSF and ISO 27001 control maps. The shape of the bottom half of the map is essentially carved by what regulators and auditors demand evidence of.

3. **The LLM dyad sits at the floor of the map, and that is the correct placement for May 2023.** LLM for Defence (0.14, 0.14) and LLM as Risk (0.10, 0.06) are genuinely Genesis — no production SOC copilot deployments, no codified controls for third-party LLM data leakage, no agreed pattern for LLM-specific threat modelling. The evolution arrows on these two components are the longest on the map and the most uncertain. Their visibility to executives in May 2023 is near zero; by May 2024 both will be visible, and by May 2025 LLM-for-Defence will likely be Product.

4. **Four inertia markers cluster in the judgement band.** Risk Appetite, Risk Assessment Methodology, Incident Response, and Pen Testing all carry inertia for structurally similar reasons: incumbent revenue models (consultancies, IR firms, pen-test boutiques) or incumbent governance models (boards avoiding quantified accountability) depend on keeping these components bespoke. Any effort to commoditise them will face organised resistance from the parties that profit from their current stage. This is the clearest doctrine-level warning the map produces.

5. **Cyber Insurance is the only transfer option and it is actively hardening.** P&L → Cyber Insurance is the explicit transfer path on the map. In May 2023 this path is narrowing: capacity is constrained, ransomware sub-limits are standard, war-exclusion clauses are being enforced (the Mondelez/Zurich settlement in late 2022 was the precedent). Executives who modelled risk transfer against generous 2018–2020 underwriting are looking at a changed market. The evolution arrow Cyber Insurance 0.54 → 0.70 reflects re-commoditisation as underwriting data improves, but not in a way that restores the old premia.

---

## Doctrine Check

| Principle | Reading on this map |
|---|---|
| **Know your users** | Explicit anchor on Executives, with three downstream user needs (P&L, Compliance, Risk Appetite). Pass. |
| **Focus on user needs** | Needs are financial (P&L), legal (Compliance), and governance (Appetite) — not on internal security capabilities. Pass. |
| **Use appropriate methods** | Major violation risk. Compliance Frameworks at Commodity (0.84) should be run with Six Sigma / ITIL-style controls; FAIR Quantification at Genesis (0.22) needs Pioneer-style experimentation. Many firms apply the same GRC process to both, which produces checkbox FAIR pilots that never scale. |
| **Remove bias and duplication** | Likelihood/Impact Matrices and FAIR Quantification are two methodologies serving the same purpose at wildly different evolution stages — many firms run both in parallel, neither well. The map makes the duplication visible. |
| **Manage inertia** | Four explicit inertia markers (Risk Appetite, Risk Assessment Methodology, Incident Response, Pen Testing). All are correctly flagged. The inertia is not irrational — it reflects incumbent economics — but it is the single biggest strategic obstacle on this map. |
| **Be transparent** | Risk Register at Product (0.60) means transparency tooling is available; whether it is used transparently is an organisational choice, not a tooling constraint. |
| **There is no core** | Risk Appetite and Pen Testing are both treated as "core" capabilities by most security organisations; both are ripe for evolution. Treating them as permanent core is a doctrine violation. |
| **Listen to your ecosystems** | The LLM dyad at the floor of the map *is* the weak signal. Firms that treat these components as "not yet our problem" in May 2023 will be surprised by late 2024. |

---

## Recommended Actions

1. **Stop investing in custom assessment methodology; buy the frameworks, invest in the judgement.** The combination of Risk Frameworks at Product (0.68), Risk Register at Product (0.60), and Compliance Frameworks at Commodity (0.84) means the apparatus for tracking and reporting risk is available off the shelf. Custom-built GRC methodology is a doctrine failure. Redirect that budget to the Custom-Built band where judgement actually lives: Risk Appetite articulation, Mitigate/Transfer/Accept decision quality, and Incident Response playbook maturity.

2. **Pilot FAIR quantification on a ring-fenced set of risks, not as a firm-wide replacement.** FAIR at 0.22 is Genesis; treating it as a drop-in replacement for qualitative matrices will fail because the practice, data, and tooling are not yet Product. Pick five material risks (ransomware loss, third-party breach, regulatory fine, IP theft, LLM data leakage), run FAIR on those, keep heat maps for the rest. Revisit in 12 months when the evolution arrow lands.

3. **Assume the cyber insurance market is not going back.** Model transfer capacity against 2023 underwriting, not 2019. Budget for higher retentions, more exclusions, and harder data-sharing demands from insurers. Treat premium-reduction-from-controls as a real ROI lever — insurers are now paying attention to MFA coverage, EDR coverage, and backup segregation in a way they were not three years ago.

4. **Stand up a named owner for the LLM dyad now.** Both LLM for Defence and LLM as Risk sit at Genesis in May 2023. The risk in not staffing this is asymmetric: the downside of ignoring LLM-as-risk is a data-leak incident with no controls; the downside of ignoring LLM-for-defence is being 18 months behind peers on SOC productivity in May 2025. One named accountable executive, reporting into the CISO, with explicit brief across both sides of the dyad.

5. **Professionalise the Mitigate/Transfer/Accept decision.** This component sits at the centre of the map and at Custom-Built (0.36). Every significant risk in the register should have a decision recorded, reviewed annually, with the decision tied back to the Risk Appetite statement and to the P&L consequence of being wrong. This is doctrine ("bias towards action") and most firms do it poorly or not at all.

---

## Build vs. Buy Assessment

| Component | Recommendation | Rationale |
|---|---|---|
| Risk Register | Buy | Product. GRC platforms are mature. Building custom is duplication. |
| Risk Frameworks | Adopt | Product. NIST CSF or ISO 27001 — pick, certify, operate. Do not invent your own. |
| Compliance Frameworks | Comply | Commodity / regulatory. No choice. |
| Asset Inventory | Buy | Product. Axonius, ServiceNow CMDB, JupiterOne etc. |
| Risk Identification | Buy (training) + Build (practice) | Custom-Built. Buy the training; build the in-house practice. |
| Risk Assessment Methodology | Build (framework choice) + Buy (tooling) | Custom-Built overall; the tooling layer underneath is Product. |
| FAIR Quantification | Pilot | Genesis. Ring-fenced investment only. Pioneer mode. |
| Likelihood/Impact Matrices | Keep | Commodity. Widely criticised but they work as a coarse-grained screen. |
| Mitigate/Transfer/Accept | Build (decision discipline) | Custom-Built. Cannot be outsourced; it is the board's job. |
| Cyber Insurance | Buy | Product. Evaluate carriers annually; model realistic terms. |
| Security Reporting | Buy | Product. SIEM and GRC dashboards. |
| Security Monitoring | Buy (MDR) | Product. MSSP / MDR market is mature; in-house SOC below 24×7 scale is rarely economic. |
| SOC Tooling (SIEM/EDR) | Buy | Product. Crowded, well-differentiated. |
| Incident Response | Retainer (buy capacity) + Build (playbooks) | Custom-Built. Retainers cover surge; playbooks are yours. |
| Security Testing | Buy | Product. DAST/SAST/SCA tooling. |
| Pen Testing | Buy (boutique) + Build (triage) | Custom-Built. Buy expert testers; build the internal capacity to triage and act on findings. |
| Bug Bounty | Buy (platform) | Product. HackerOne / Bugcrowd. |
| LLM for Defence | Pilot | Genesis. Do not commit to a platform in May 2023. |
| LLM as Risk | Build (controls) | Genesis. Controls must be invented — DLP at the prompt boundary, enterprise-LLM gateways, red-team prompts. |

---

## Evolution Predictions (12-24 months, i.e. May 2023 → May 2025)

Seven evolution arrows on the map, with reasoning:

- **FAIR Quantification 0.22 → 0.45 (Genesis → Custom-Built).** SEC cyber disclosure rules (finalised Jul 2023) will push FAIR-like quantification into public-company practice; RiskLens / ThreatConnect-style tooling matures. Still bespoke; not a product market.
- **Risk Assessment Methodology 0.32 → 0.52 (Custom-Built → Product).** Consolidation around framework-tool combinations (NIST CSF in ServiceNow GRC, ISO 27001 in OneTrust) makes methodology-choice a Product decision rather than a bespoke build.
- **Pen Testing 0.38 → 0.56 (Custom-Built → Product).** PTaaS (Cobalt, HackerOne Pentest, Synack) pulls the mid-market into productised continuous testing. The high-end red team remains craft.
- **Incident Response 0.44 → 0.60 (Custom-Built → Product).** SOAR platforms (Palo Alto XSOAR, Splunk Phantom, Tines) plus IR retainer standardisation plus LLM-assisted playbook execution commoditise the common-case response. Complex forensics remains craft.
- **Cyber Insurance 0.54 → 0.70 (Product → late Product / Commodity).** Better underwriting data, mandatory control attestations, and parametric / event-linked products mature. Premiums stabilise but with higher retentions as structural.
- **LLM for Defence 0.14 → 0.38 (Genesis → Custom-Built).** Security Copilot GA, Google Sec-PaLM, purpose-built detection models, LLM-assisted triage. No clear product winner yet by May 2025 but multiple credible offerings.
- **LLM as Risk 0.06 → 0.32 (Genesis → Custom-Built).** OWASP LLM Top 10 (published Aug 2023), NIST AI RMF adoption, mandatory enterprise-LLM gateways, DLP at the prompt boundary. Risk register category established but controls still bespoke.

**Inertia on Risk Appetite, Risk Assessment Methodology, Incident Response, and Pen Testing is real.** Expect actual evolution to lag the arrows in firms with large consultancy spend on these components. The arrows describe the landscape, not the pace in any individual firm.

---

## Open Questions

1. **Should the operational apparatus (Monitoring, Reporting, SOC Tooling, Incident Response, Security Testing, Pen Testing, Bug Bounty) be a submap?** It is the largest cluster on this map and has its own internal value chain. Splitting it out would free room to expand the Risk Governance half (appetite, identification, methodology, quantification) which the scenario arguably cares about more.

2. **Where does "third-party / supply-chain risk" sit?** It is implicit in Risk Identification and Asset Inventory but not explicit. For a May 2023 map this is defensible (SolarWinds was 2020-21, but the broader third-party risk function was still inside traditional risk identification for most firms); for a 2024+ map it needs to be a first-class component.

3. **Is Risk Appetite one component or three?** Financial risk appetite, regulatory risk appetite, and operational risk appetite behave differently. For an executive map the aggregated view is right; for a CRO-focused map it would need splitting.

---

## Deliverable (Interactive Artifact) — React Component

The following React component renders an interactive Wardley Map with hover tooltips, click-to-highlight dependency chains, a figure legend, and evolution-stage shading. It follows the architecture in `templates/artifact-template.jsx`.

```jsx
import { useState, useCallback, useMemo } from "react";

// --- Canvas / style constants ---
const WIDTH = 1200;
const HEIGHT = 820;
const PADDING = { top: 55, right: 30, bottom: 95, left: 75 };
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
  tooltipBg: "#1a1a2e",
  tooltipText: "#f0f0f0",
  legendBorder: "#dddddd",
  labelText: "#222222",
  dimmedOpacity: 0.15
};
const STAGE_BOUNDARIES = [0.25, 0.50, 0.75];
const STAGE_LABELS = ["Genesis", "Custom-Built", "Product (+Rental)", "Commodity (+Utility)"];

const toSvgX = (m) => PADDING.left + m * (WIDTH - PADDING.left - PADDING.right);
const toSvgY = (v) => PADDING.top + (1 - v) * (HEIGHT - PADDING.top - PADDING.bottom);

const MAP = {
  title: "Cybersecurity Risk Management from the Executive Seat (May 2023)",
  purpose: "Where cybersecurity risk management is commoditised, where it is still expert judgement, and where regulation is forcing the shape",
  components: [
    { id: "executives", name: "Executives", visibility: 0.97, maturity: 0.50, stage: "Anchor", rationale: "Board / C-suite; the seat where P&L, compliance, and risk appetite resolve into spend.", isAnchor: true },
    { id: "pnl", name: "P&L", visibility: 0.90, maturity: 0.86, stage: "Commodity", rationale: "Entirely codified (GAAP/IFRS); invisible until it moves; catastrophic failure tolerance." },
    { id: "compliance-obligation", name: "Compliance Obligation", visibility: 0.88, maturity: 0.80, stage: "Commodity", rationale: "The fact of legal obligation is universal and non-negotiable; a commoditised condition of doing business." },
    { id: "risk-appetite", name: "Risk Appetite", visibility: 0.86, maturity: 0.32, stage: "Custom-Built", rationale: "ISO 31000 / COSO scaffolding exists but each board's appetite statement is bespoke and rarely quantified.", inertia: true },
    { id: "risk-register", name: "Risk Register", visibility: 0.78, maturity: 0.60, stage: "Product", rationale: "GRC platforms (Archer, ServiceNow GRC, LogicGate, Hyperproof, OneTrust) mature and feature-competitive." },
    { id: "risk-frameworks", name: "Risk Frameworks", visibility: 0.74, maturity: 0.68, stage: "Product", rationale: "NIST CSF, ISO 27001, CIS Controls — multiple competing frameworks with certification bodies and training markets." },
    { id: "compliance-frameworks", name: "Compliance Frameworks", visibility: 0.74, maturity: 0.84, stage: "Commodity", rationale: "SOX, PCI-DSS, HIPAA, GDPR, SOC 2 — enshrined in law or contract, fully codified, auditable." },
    { id: "risk-identification", name: "Risk Identification", visibility: 0.68, maturity: 0.38, stage: "Custom-Built", rationale: "STRIDE, PASTA, OCTAVE are trainable techniques; running them in a real organisation is specialist and bespoke." },
    { id: "risk-methodology", name: "Risk Assessment Methodology", visibility: 0.64, maturity: 0.32, stage: "Custom-Built", rationale: "Qualitative vs FAIR vs mixed still religiously debated; every firm mixes its own blend.", inertia: true },
    { id: "asset-inventory", name: "Asset Inventory", visibility: 0.60, maturity: 0.56, stage: "Product", rationale: "Axonius, Lansweeper, ServiceNow CMDB, JupiterOne — multiple vendors, feature competition." },
    { id: "li-matrices", name: "Likelihood/Impact Matrices", visibility: 0.56, maturity: 0.74, stage: "Commodity", rationale: "Heat maps (3×3, 5×5) in every board pack. Utterly standardised even though widely criticised." },
    { id: "fair", name: "FAIR Quantification", visibility: 0.56, maturity: 0.22, stage: "Genesis", rationale: "FAIR Institute recognised, but in May 2023 production deployments at scale are rare; mostly pilots and consulting." },
    { id: "mta", name: "Mitigate/Transfer/Accept", visibility: 0.54, maturity: 0.36, stage: "Custom-Built", rationale: "Three-option decision taxonomy is well-established; per-risk decisions are bespoke per firm and financial year." },
    { id: "cyber-insurance", name: "Cyber Insurance", visibility: 0.50, maturity: 0.54, stage: "Product", rationale: "Defined market (Beazley, AIG, Chubb, Hiscox). In May 2023 mid-hardening: premiums up 50-150% YoY, ransomware sub-limits, war exclusions after Mondelez." },
    { id: "reporting", name: "Security Reporting", visibility: 0.48, maturity: 0.64, stage: "Product", rationale: "KPI dashboards, CISO board packs, MTTR/MTTD metrics — productised across SIEM and GRC tools." },
    { id: "monitoring", name: "Security Monitoring", visibility: 0.42, maturity: 0.60, stage: "Product", rationale: "MDR/MSSP market mature (CrowdStrike Falcon Complete, Arctic Wolf, Expel, Secureworks)." },
    { id: "soc", name: "SOC Tooling (SIEM/EDR)", visibility: 0.36, maturity: 0.66, stage: "Product", rationale: "Splunk, Microsoft Sentinel, Elastic, CrowdStrike, SentinelOne, Defender — crowded, differentiated, Gartner MQ-ed." },
    { id: "ir", name: "Incident Response", visibility: 0.32, maturity: 0.44, stage: "Custom-Built", rationale: "IR retainers are a market (Mandiant, Unit 42, Kroll), but response is bespoke; senior forensic judgement required.", inertia: true },
    { id: "security-testing", name: "Security Testing", visibility: 0.28, maturity: 0.56, stage: "Product", rationale: "DAST/SAST/SCA tooling (Qualys, Nessus, Snyk, Veracode, Checkmarx) mature and feature-competitive." },
    { id: "pentest", name: "Pen Testing", visibility: 0.24, maturity: 0.38, stage: "Custom-Built", rationale: "Boutique pen-test firms dominate; output is operator-dependent. PTaaS emerging but the core is craft.", inertia: true },
    { id: "bounty", name: "Bug Bounty", visibility: 0.20, maturity: 0.54, stage: "Product", rationale: "HackerOne, Bugcrowd, Intigriti, YesWeHack — marketplace pattern mature, payout structures standard." },
    { id: "llm-defence", name: "LLM for Defence", visibility: 0.14, maturity: 0.14, stage: "Genesis", rationale: "Microsoft Security Copilot announced Mar 2023, no GA. Every SOC vendor has a roadmap slide; no production value yet." },
    { id: "llm-risk", name: "LLM as Risk", visibility: 0.10, maturity: 0.06, stage: "Genesis", rationale: "In May 2023: Samsung ChatGPT data leak, prompt injection being weaponised, Mata v Avianca unfolding. Risk register category still being invented." }
  ],
  links: [
    { from: "executives", to: "pnl" },
    { from: "executives", to: "compliance-obligation" },
    { from: "executives", to: "risk-appetite" },
    { from: "pnl", to: "risk-register" },
    { from: "pnl", to: "cyber-insurance" },
    { from: "compliance-obligation", to: "compliance-frameworks" },
    { from: "compliance-obligation", to: "risk-frameworks" },
    { from: "compliance-obligation", to: "risk-register" },
    { from: "risk-appetite", to: "risk-register" },
    { from: "risk-appetite", to: "mta" },
    { from: "risk-register", to: "risk-identification" },
    { from: "risk-register", to: "risk-methodology" },
    { from: "risk-identification", to: "asset-inventory" },
    { from: "risk-methodology", to: "li-matrices" },
    { from: "risk-methodology", to: "fair" },
    { from: "risk-frameworks", to: "risk-methodology" },
    { from: "risk-frameworks", to: "monitoring" },
    { from: "risk-frameworks", to: "ir" },
    { from: "compliance-frameworks", to: "security-testing" },
    { from: "compliance-frameworks", to: "reporting" },
    { from: "mta", to: "cyber-insurance" },
    { from: "mta", to: "reporting" },
    { from: "mta", to: "ir" },
    { from: "mta", to: "security-testing" },
    { from: "reporting", to: "monitoring" },
    { from: "monitoring", to: "soc" },
    { from: "ir", to: "soc" },
    { from: "security-testing", to: "pentest" },
    { from: "security-testing", to: "bounty" },
    { from: "soc", to: "llm-defence" },
    { from: "ir", to: "llm-defence" },
    { from: "pentest", to: "llm-risk" },
    { from: "risk-register", to: "llm-risk" },
    { from: "asset-inventory", to: "llm-risk" }
  ],
  evolutions: [
    { componentId: "fair", toMaturity: 0.45 },
    { componentId: "risk-methodology", toMaturity: 0.52 },
    { componentId: "pentest", toMaturity: 0.56 },
    { componentId: "ir", toMaturity: 0.60 },
    { componentId: "cyber-insurance", toMaturity: 0.70 },
    { componentId: "llm-defence", toMaturity: 0.38 },
    { componentId: "llm-risk", toMaturity: 0.32 }
  ],
  annotations: [
    { id: 1, text: "LLM angle: Genesis both sides", x: 0.12, y: 0.22 },
    { id: 2, text: "Expert craft; automation pressure", x: 0.36, y: 0.32 },
    { id: 3, text: "Where P&L meets cyber", x: 0.30, y: 0.54 },
    { id: 4, text: "Regulation forcing right", x: 0.66, y: 0.76 }
  ]
};

function findDependencyChain(id, links) {
  const set = new Set([id]);
  let changed = true;
  while (changed) {
    changed = false;
    for (const l of links) {
      if (set.has(l.to) && !set.has(l.from)) { set.add(l.from); changed = true; }
      if (set.has(l.from) && !set.has(l.to)) { set.add(l.to); changed = true; }
    }
  }
  return set;
}

function computeLabelOffsets(components) {
  const out = {};
  const pos = components.map(c => ({ id: c.id, sx: toSvgX(c.maturity), sy: toSvgY(c.visibility) }));
  for (const c of components) {
    let dx = 10, dy = -12;
    const sx = toSvgX(c.maturity), sy = toSvgY(c.visibility);
    for (const o of pos) {
      if (o.id === c.id) continue;
      if (Math.abs(sx - o.sx) < 90 && Math.abs(sy - o.sy) < 22) {
        dy = sy <= o.sy ? -14 : 16;
      }
    }
    if (sx + dx + c.name.length * 6 > WIDTH - PADDING.right) dx = -(c.name.length * 6 + 10);
    if (sy + dy < PADDING.top + 10) dy = 14;
    out[c.id] = { dx, dy };
  }
  return out;
}

export default function WardleyMap() {
  const [hoveredId, setHoveredId] = useState(null);
  const [selectedId, setSelectedId] = useState(null);
  const [tip, setTip] = useState({ x: 0, y: 0 });

  const map = MAP;
  const offs = useMemo(() => computeLabelOffsets(map.components), [map.components]);
  const chain = useMemo(() => selectedId ? findDependencyChain(selectedId, map.links) : null, [selectedId, map.links]);
  const byId = useMemo(() => Object.fromEntries(map.components.map(c => [c.id, c])), [map.components]);
  const isV = useCallback((id) => !chain || chain.has(id), [chain]);
  const isLV = useCallback((l) => !chain || (chain.has(l.from) && chain.has(l.to)), [chain]);
  const onHover = useCallback((e, c) => {
    const r = e.currentTarget.closest("svg").getBoundingClientRect();
    setHoveredId(c.id);
    setTip({ x: e.clientX - r.left, y: e.clientY - r.top });
  }, []);
  const hovered = hoveredId ? byId[hoveredId] : null;

  function depPath(a, b) {
    const x1 = toSvgX(a.maturity), y1 = toSvgY(a.visibility);
    const x2 = toSvgX(b.maturity), y2 = toSvgY(b.visibility);
    const mx = (x1 + x2) / 2, my = (y1 + y2) / 2;
    const curve = Math.abs(x1 - x2) < 20 ? 15 : 0;
    return `M ${x1} ${y1} Q ${mx + curve} ${my} ${x2} ${y2}`;
  }

  return (
    <div className="w-full max-w-6xl mx-auto p-4">
      <h2 className="text-lg font-semibold text-gray-800 mb-1">{map.title}</h2>
      <p className="text-sm text-gray-500 mb-3">{map.purpose}</p>
      <div className="relative border border-gray-200 rounded bg-white">
        <svg viewBox={`0 0 ${WIDTH} ${HEIGHT}`} className="w-full h-auto"
          style={{ fontFamily: "'Segoe UI', system-ui, sans-serif" }}
          onClick={() => setSelectedId(null)}>

          {STAGE_LABELS.map((_, i) => {
            const x0 = toSvgX(i === 0 ? 0 : STAGE_BOUNDARIES[i - 1]);
            const x1 = toSvgX(i < STAGE_BOUNDARIES.length ? STAGE_BOUNDARIES[i] : 1);
            return <rect key={i} x={x0} y={PADDING.top} width={x1 - x0}
              height={HEIGHT - PADDING.top - PADDING.bottom} fill={COLORS.stageFills[i]} />;
          })}

          {STAGE_BOUNDARIES.map((b, i) => (
            <line key={i} x1={toSvgX(b)} y1={PADDING.top}
              x2={toSvgX(b)} y2={HEIGHT - PADDING.bottom}
              stroke={COLORS.gridLine} strokeDasharray="6 4" strokeWidth={1} />
          ))}

          <line x1={PADDING.left} y1={PADDING.top} x2={PADDING.left}
            y2={HEIGHT - PADDING.bottom} stroke={COLORS.axisLine} strokeWidth={1.5} />
          <line x1={PADDING.left} y1={HEIGHT - PADDING.bottom}
            x2={WIDTH - PADDING.right} y2={HEIGHT - PADDING.bottom}
            stroke={COLORS.axisLine} strokeWidth={1.5} />
          <text x={PADDING.left - 10} y={PADDING.top - 8} textAnchor="middle"
            fontSize={11} fill={COLORS.axisLabel} fontWeight={500}>Visible</text>
          <text x={PADDING.left - 10} y={HEIGHT - PADDING.bottom + 18} textAnchor="middle"
            fontSize={11} fill={COLORS.axisLabel} fontWeight={500}>Invisible</text>
          <text transform={`rotate(-90, 18, ${(PADDING.top + HEIGHT - PADDING.bottom) / 2})`}
            x={18} y={(PADDING.top + HEIGHT - PADDING.bottom) / 2} textAnchor="middle"
            fontSize={12} fill={COLORS.axisLabel} fontWeight={600}>Value Chain</text>
          {STAGE_LABELS.map((lab, i) => {
            const a = i === 0 ? 0 : STAGE_BOUNDARIES[i - 1];
            const b = i < STAGE_BOUNDARIES.length ? STAGE_BOUNDARIES[i] : 1;
            return <text key={i} x={toSvgX((a + b) / 2)} y={HEIGHT - PADDING.bottom + 20}
              textAnchor="middle" fontSize={11} fill={COLORS.stageLabel} fontWeight={500}>{lab}</text>;
          })}
          <text x={(PADDING.left + WIDTH - PADDING.right) / 2} y={HEIGHT - PADDING.bottom + 38}
            textAnchor="middle" fontSize={12} fill={COLORS.axisLabel} fontWeight={600}>Evolution</text>

          {map.links.map((l, i) => {
            const a = byId[l.from], b = byId[l.to];
            if (!a || !b) return null;
            return <path key={i} d={depPath(a, b)} fill="none"
              stroke={COLORS.dependencyLine} strokeWidth={1}
              opacity={isLV(l) ? 1 : COLORS.dimmedOpacity} />;
          })}

          {map.evolutions.map((e, i) => {
            const c = byId[e.componentId];
            if (!c) return null;
            const x1 = toSvgX(c.maturity), y1 = toSvgY(c.visibility);
            const x2 = toSvgX(e.toMaturity);
            return <g key={i} opacity={isV(e.componentId) ? 1 : COLORS.dimmedOpacity}>
              <defs>
                <marker id={`arr-${i}`} viewBox="0 0 10 10" refX="9" refY="5"
                  markerWidth="6" markerHeight="6" orient="auto">
                  <path d="M 0 0 L 10 5 L 0 10 z" fill={COLORS.evolutionArrow} />
                </marker>
              </defs>
              <line x1={x1 + 8} y1={y1} x2={x2 - 4} y2={y1}
                stroke={COLORS.evolutionArrow} strokeWidth={1.4}
                strokeDasharray="4 3" markerEnd={`url(#arr-${i})`} />
            </g>;
          })}

          {map.components.map((c) => {
            const sx = toSvgX(c.maturity), sy = toSvgY(c.visibility);
            const off = offs[c.id];
            const isSel = selectedId === c.id;
            const r = c.isAnchor ? 7 : 6;
            return <g key={c.id} opacity={isV(c.id) ? 1 : COLORS.dimmedOpacity}
              onClick={(e) => { e.stopPropagation(); setSelectedId(c.id); }}
              onMouseEnter={(e) => onHover(e, c)}
              onMouseLeave={() => setHoveredId(null)}
              style={{ cursor: "pointer" }}>
              {c.inertia && <line x1={sx + 10} y1={sy - 10} x2={sx + 10} y2={sy + 10}
                stroke={COLORS.inertiaBar} strokeWidth={3} />}
              <circle cx={sx} cy={sy} r={r} fill={c.isAnchor ? "#fff7e0" : COLORS.componentFill}
                stroke={isSel ? COLORS.componentStrokeSelected : COLORS.componentStroke}
                strokeWidth={isSel ? 2 : 1.2} />
              <text x={sx + off.dx} y={sy + off.dy} fontSize={11}
                fill={COLORS.labelText} fontWeight={c.isAnchor ? 600 : 400}>{c.name}</text>
            </g>;
          })}

          {map.annotations.map((a) => (
            <g key={a.id}>
              <circle cx={toSvgX(a.x)} cy={toSvgY(a.y)} r={10}
                fill="#fff7e0" stroke="#c7a550" strokeWidth={1} />
              <text x={toSvgX(a.x)} y={toSvgY(a.y) + 4} textAnchor="middle"
                fontSize={10} fill="#7a6020" fontWeight={600}>{a.id}</text>
            </g>
          ))}

          <text x={PADDING.left} y={PADDING.top - 20} fontSize={13}
            fill={COLORS.labelText} fontWeight={700}>{map.title}</text>

          {/* Figure Legend */}
          <g transform={`translate(${WIDTH - 280}, ${HEIGHT - 80})`}>
            <rect x={0} y={0} width={250} height={70} fill="#fafafa"
              stroke={COLORS.legendBorder} strokeWidth={1} rx={4} />
            <text x={8} y={12} fontSize={10} fontWeight={700} fill="#333">Legend</text>
            <circle cx={18} cy={26} r={5} fill="#fff" stroke="#333" strokeWidth={1} />
            <text x={30} y={29} fontSize={9} fill="#333">Component</text>
            <line x1={110} y1={26} x2={140} y2={26} stroke="#aaa" strokeWidth={1} />
            <text x={144} y={29} fontSize={9} fill="#333">Dependency</text>
            <line x1={8} y1={42} x2={30} y2={42} stroke={COLORS.evolutionArrow}
              strokeWidth={1.4} strokeDasharray="4 3" />
            <text x={34} y={45} fontSize={9} fill="#333">Evolve arrow</text>
            <line x1={110} y1={36} x2={110} y2={48} stroke="#333" strokeWidth={3} />
            <text x={116} y={45} fontSize={9} fill="#333">Inertia</text>
            <circle cx={180} cy={42} r={7} fill="#fff7e0" stroke="#c7a550" />
            <text x={190} y={45} fontSize={9} fill="#333">Annotation</text>
            <text x={8} y={62} fontSize={9} fill="#333">Columns: Genesis / Custom-Built / Product / Commodity</text>
          </g>
        </svg>

        {hovered && (
          <div style={{
            position: "absolute", left: tip.x + 12, top: tip.y + 12,
            background: COLORS.tooltipBg, color: COLORS.tooltipText,
            padding: "8px 10px", borderRadius: 4, fontSize: 12,
            maxWidth: 320, pointerEvents: "none", zIndex: 10
          }}>
            <div style={{ fontWeight: 700 }}>{hovered.name}</div>
            <div style={{ opacity: 0.8, fontSize: 11 }}>
              {hovered.stage} — [{hovered.visibility.toFixed(2)}, {hovered.maturity.toFixed(2)}]
            </div>
            <div style={{ marginTop: 4 }}>{hovered.rationale}</div>
          </div>
        )}
      </div>
    </div>
  );
}
```

---

## Map Summary

- **Components:** 22 (plus 1 anchor = 23 total nodes).
- **Dependencies:** 34.
- **Evolution arrows:** 7.
- **Inertia markers:** 4 (Risk Appetite, Risk Assessment Methodology, Incident Response, Pen Testing).
- **Annotations:** 4.
- **Stages represented:** Genesis (3 — FAIR, LLM for Defence, LLM as Risk), Custom-Built (6 — Risk Appetite, Risk Identification, Risk Assessment Methodology, Mitigate/Transfer/Accept, Incident Response, Pen Testing), Product (8 — Risk Register, Risk Frameworks, Asset Inventory, Cyber Insurance, Security Reporting, Security Monitoring, SOC Tooling, Security Testing, Bug Bounty), Commodity (4 — P&L, Compliance Obligation, Compliance Frameworks, Likelihood/Impact Matrices), plus 1 Anchor.

The principal finding is that commoditised tooling covers the top-right (compliance, frameworks, heat maps) and the lower-right (SOC, MDR, bug bounty), while the middle band — risk appetite, assessment methodology, mitigate/transfer/accept decision quality, incident response, and pen testing — is where expert judgement still dominates and where inertia is concentrated. Regulatory obligations are the strongest single force on the map, pulling compliance frameworks, reporting, and testing rightward. The LLM dyad at the floor is genuinely Genesis in May 2023 and carries the largest evolution-arrow uncertainty on the map.
