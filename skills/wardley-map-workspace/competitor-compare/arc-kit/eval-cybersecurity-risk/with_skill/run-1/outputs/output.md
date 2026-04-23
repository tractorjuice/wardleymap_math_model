# Wardley Map: Cybersecurity Risk Management from the Executive's Point of View (May 2023)

**Anchor:** Executives (Board / CEO / CFO / Audit & Risk Committee receiving CISO reporting) — they own the cybersecurity risk posture and sign off on mitigation / transfer / acceptance decisions.

**Date:** 2026-04-22 (scenario date-stamp: May 2023)

**Scope:** Cybersecurity risk management as an enterprise capability, viewed top-down from the executive. Covers the P&L / compliance / risk-appetite drivers, the governance and assessment apparatus, the quantification methods, the operational security stack, and the emerging LLM angle on both defence and risk surface.

---

## Step 1 - Context

| Question | Answer |
|----------|--------|
| Primary user | Executives (Board, CEO, CFO, Audit & Risk Committee, receiving reporting from CISO) |
| User need | Manage cybersecurity risk to an acceptable level given P&L impact, compliance obligations, and stated risk appetite |
| Scope | Enterprise capability — treatment of cyber risk end-to-end, from boardroom to SOC tooling |
| Primary goal | Identify what is commoditised tooling vs. expert judgement, and where regulation is forcing the shape of the map |
| Industry | Cross-industry (generic enterprise), with regulated-sector emphasis (financial services, critical national infrastructure) |
| Depth | Standard (~25 components) including the explicit LLM-defence and LLM-risk components |
| Scenario time | May 2023 (pre-EU AI Act adoption, post NIST AI RMF v1.0 Jan 2023, post 2021-22 cyber insurance market correction, GPT-4 era) |

## Step 2 - Value Chain

Working downward from the anchor (Executives):

1. **Anchor:** Executives — ultimate owners of cyber risk posture.
2. **Executive drivers:** P&L Impact, Compliance Obligations, Risk Appetite — the three forces that shape every downstream decision the user asked to see.
3. **Governance / Risk-posture layer:** Mitigation / Transfer / Accept Mix, Cyber Insurance, Risk Register — the artefacts that translate appetite into action.
4. **Risk Assessment layer:** Risk Assessment Methodology, Risk Identification Practice, Asset Inventory — how risks get onto the register.
5. **Frameworks:** Risk Framework (NIST CSF, ISO 27005), Compliance Framework (ISO 27001, SOC 2, PCI DSS, GDPR) — the external structures that dictate the shape of the methodology.
6. **Risk Quantification:** Risk Matrices (most commoditised), Likelihood/Impact Scoring (product), FAIR Quantification (still bespoke/expert).
7. **Operational Security:** Reporting to Board, Incident Response, Security Monitoring, SOC Tooling (SIEM/XDR), Security Testing, Pen Testing, Bug Bounty — the doing side.
8. **Emerging — LLM angle:**
   - **LLM-Assisted Defence** (defensive copilots for SOC analysts) — custom/emerging in May 2023.
   - **LLM-as-Risk** (prompt injection, training-data leakage, shadow-AI) — a *new risk type* that must be tracked on the register; genesis in May 2023.

Dependencies flow downward: executives depend on drivers, drivers on governance, governance on assessment, assessment on frameworks and quantification, methodology on identification and inventory, reporting on monitoring, and so on. See draft.owm for full edge set.

## Step 3 - Evolution Positioning

Scored using arc-kit Step 6 rubric (Ubiquity × Certainty averaged) with May 2023 market evidence.

| Component | Stage | Position (X) | Visibility (Y) | Rationale |
|---|---|---|---|---|
| Executives | Commodity | 0.80 | 0.97 | Anchor. Executive accountability for cyber is now universal (SEC 10-K, UK FCA, EU NIS2 in draft). |
| P&L Impact | Commodity | 0.90 | 0.88 | Loss quantification is a mature accounting discipline; breach-loss data is now routine input. |
| Compliance Obligations | Commodity | 0.82 | 0.88 | Obligations are well-defined statutory artefacts (GDPR, SOX, HIPAA, PCI DSS). |
| Risk Appetite | Product | 0.55 | 0.88 | Concept is established, but every board articulates it differently; appetite-statement templates are still productising. |
| Mitigation/Transfer/Accept Mix | Product | 0.60 | 0.78 | Standard framing (NIST, ISO), but every organisation's mix is bespoke. |
| Cyber Insurance | Commodity | 0.75 | 0.78 | Mature, multi-vendor market. Post-2021-22 correction has tightened underwriting — the product is well-understood. |
| Risk Register | Product | 0.68 | 0.72 | GRC platforms (ServiceNow, Archer, OneTrust) have productised the register. Content is bespoke; tooling is product. |
| Risk Assessment Methodology | Product | 0.55 | 0.65 | Established methodology families (NIST 800-30, ISO 27005, OCTAVE) but choice-and-tailoring is still expert work. |
| Risk Identification Practice | Product | 0.45 | 0.65 | Practice is recognisable but organisation-specific; trained roles rather than a product. |
| Asset Inventory | Commodity | 0.72 | 0.65 | CMDB / cloud-asset discovery is solidly productised and trending toward commodity. |
| Risk Framework (NIST CSF / ISO 27005) | Product | 0.72 | 0.55 | Widely adopted industry frameworks; NIST CSF 2.0 was in public draft in 2023 - still moving right. |
| Compliance Framework (ISO 27001 / SOC 2 / PCI / GDPR) | Commodity | 0.85 | 0.55 | Standards are stable, auditable, and routine. **The regulatory obligations sit here and shape everything above them.** |
| Risk Matrices | Commodity | 0.78 | 0.48 | Ubiquitous 5x5 heat-map; entrenched despite academic critique. **Inertia point.** |
| Likelihood/Impact Scoring | Product | 0.62 | 0.48 | Multiple recognised approaches; productised inside GRC platforms. |
| FAIR Quantification | Custom | 0.32 | 0.48 | FAIR Institute body-of-knowledge is mature but practitioners are scarce; monetary quantification is still expert judgement. **Inertia point.** |
| Reporting to Board | Product | 0.70 | 0.60 | Board-level cyber dashboards are now a product category (Panaseer, Balbix) — maturing fast. |
| Incident Response | Commodity | 0.78 | 0.42 | IR retainer services and runbooks are a mature market (CrowdStrike, Mandiant, Unit 42). |
| Security Monitoring | Commodity | 0.85 | 0.38 | SOC-as-a-service and cloud-delivered monitoring are highly commoditised. |
| SOC Tooling (SIEM/XDR) | Commodity | 0.72 | 0.35 | SIEM is old-commodity; XDR is accelerating right. Multi-vendor, consumption-priced. |
| Security Testing | Product | 0.62 | 0.42 | Discipline as a whole is productised; individual tests remain expert-delivered. |
| Pen Testing | Product | 0.70 | 0.32 | Well-established service market; productising further via continuous pen-test platforms. |
| Bug Bounty | Product | 0.55 | 0.32 | HackerOne / Bugcrowd / Intigriti have productised the programme layer; still bespoke per-scope. |
| LLM-Assisted Defence | Custom | 0.20 | 0.28 | **May 2023:** Microsoft Security Copilot just announced (Mar 2023); early SOC-analyst copilots; custom-built and accelerating. |
| LLM-as-Risk (prompt injection, data leakage) | Genesis | 0.12 | 0.55 | **May 2023:** the risk itself is newly named (OWASP LLM Top 10 did not yet exist - published Aug 2023); regulators are reaching for it via NIST AI RMF (Jan 2023) and the EU AI Act draft. Genuinely genesis. |

### Quantitative cross-check (arc-kit Section 6)

Evolution score E(c) = (Ubiquity + Certainty) / 2 for the three components the scenario explicitly asks to be placed on the commodity-vs-expert axis:

| Component | U | C | E(c) | Stage (score) |
|---|---|---|---|---|
| Compliance Framework | 0.90 | 0.85 | 0.88 | Commodity |
| Risk Matrices | 0.90 | 0.70 | 0.80 | Commodity (but by consensus, not rigour) |
| FAIR Quantification | 0.25 | 0.40 | 0.33 | Custom-Built |
| LLM-Assisted Defence | 0.15 | 0.25 | 0.20 | Genesis / Custom boundary |
| LLM-as-Risk | 0.15 | 0.10 | 0.13 | Genesis |

### Dependency-risk spot-check (arc-kit Section B)

R(a,b) = visibility(a) × (1 - evolution(b)).

| a depends on b | vis(a) | evol(b) | R | Reading |
|---|---|---|---|---|
| Risk Register depends on FAIR Quantification (via Methodology) | 0.72 | 0.32 | 0.49 | Moderate-high — register quality is hostage to bespoke expert scoring. |
| Risk Register depends on LLM-as-Risk | 0.72 | 0.12 | 0.63 | **High risk** — executives rely on a register that is tracking a genesis-stage risk type; blind spots likely. |
| Security Monitoring depends on LLM-Assisted Defence | 0.38 | 0.20 | 0.30 | Moderate — SOC outcomes increasingly depend on tools that are still custom. |

## Step 4 - Movement

- **Natural evolution (drift right):**
  - Compliance Framework -> 0.92 (DORA, NIS2 making it even more standardised in EU).
  - Risk Framework (NIST CSF / ISO 27005) -> 0.80 (NIST CSF 2.0 draft in 2023).
  - Cyber Insurance -> 0.82 (underwriting standards tightening after 2021-22 market correction).
  - SOC Tooling (SIEM/XDR) -> 0.85 (managed XDR is eating the SIEM-only market).
  - Bug Bounty -> 0.70 (platform consolidation).
- **Acceleration (>>):**
  - **LLM-Assisted Defence** — accelerating fast from 0.20 toward 0.45; Microsoft Security Copilot announcement (Mar 2023), crowd of SOC-copilot startups. Regulatory pull (NIST AI RMF) and competitive push (CrowdStrike Charlotte AI etc.) are forcing pace.
  - **LLM-as-Risk** — accelerating from 0.12 toward 0.30 as regulators explicitly call it out.
- **Inertia (x):**
  - **Risk Matrices** — entrenched despite well-known critique (Hubbard, Thomas). Board audiences expect heat-maps; replacing with FAIR faces cultural resistance.
  - **FAIR Quantification** — held at ~0.32-0.45 by scarcity of qualified quantitative analysts; this is the biggest single expert-judgement bottleneck in the map.

## Step 5 - Visual Map

```text
Title: Cybersecurity Risk Management from the Executive's Point of View (May 2023)
Anchor: Executives (Board / C-suite)
Date: May 2023

                    Genesis    Custom     Product    Commodity
                       |          |          |          |
Visible            ----+----------+----------+----------+----
                                                       Executives    <- anchor
                                                       P&L Impact
                                                       Compliance Obligations
                                  Risk Appetite
                                             Cyber Insurance ->
                                             Mitigation/Transfer/Accept Mix ->
                                             Risk Register ->
                                             Asset Inventory ->
                                             Risk Assessment Methodology
                                             Risk Identification Practice
                                             Reporting to Board ->
                                             Risk Framework (NIST CSF / ISO 27005) ->
                                                           Compliance Framework ->
                                                           Risk Matrices (x inertia)
                                             Likelihood/Impact Scoring
                       FAIR Quantification (x inertia)
                                             Security Testing
                                             Incident Response ->
                                             Security Monitoring ->
                                             SOC Tooling (SIEM/XDR) ->
                                             Pen Testing
                                             Bug Bounty ->
                       LLM-as-Risk >>
                       LLM-Assisted Defence >>
Hidden             ----+----------+----------+----------+----

Legend: -> evolving, >> accelerating, x inertia
```

## Step 6 - Analysis

### Completeness
- Anchor (Executives) is clearly defined and placed top-right.
- Three executive drivers explicitly shown: P&L Impact, Compliance Obligations, Risk Appetite.
- Downstream apparatus covered: Risk Identification Practice, Asset Inventory, Risk Register, Risk Assessment Methodology, Risk Quantification (three variants), Risk Framework, Compliance Framework.
- Mitigation / Transfer / Accept Mix and Cyber Insurance both present.
- Operational stack covered: Monitoring, SOC Tooling, Reporting, Incident Response, Security Testing, Pen Testing, Bug Bounty.
- LLM angle: both Defence (tool) and Risk (risk-type) components present.
- Dependencies and movement arrows all included (see draft.owm).

### Positioning
- Commodity cluster (right): Compliance Framework, Cyber Insurance, Asset Inventory, Incident Response, Security Monitoring, SOC Tooling, Risk Matrices.
- Product cluster (centre-right): Risk Register, Risk Framework, Risk Assessment Methodology, Pen Testing, Bug Bounty, Board Reporting, Likelihood/Impact Scoring.
- Custom cluster (centre-left): FAIR Quantification, LLM-Assisted Defence.
- Genesis (left): LLM-as-Risk.
- Visibility constraint: every dependency edge has visibility(a) >= visibility(b); no upward-pointing dependencies.

### Key Insights

**What is commoditised tooling?**
- Compliance frameworks, asset inventory, security monitoring, SOC tooling (SIEM/XDR), incident response, cyber insurance, risk matrices. Buying decisions here are about vendor selection and cost optimisation, not architecture.

**What is still expert judgement?**
- **FAIR Quantification** is the single biggest expert-judgement bottleneck — monetary risk quantification is still scarce talent.
- **Risk Appetite articulation** — every board is its own snowflake.
- **Risk Assessment Methodology tailoring** — framework choice is a commodity; tailoring it to the organisation is not.
- **Risk Identification Practice** — a trained human discipline, not a product.
- **LLM-Assisted Defence** deployment is custom today — every SOC copilot integration is bespoke.

**Where regulation is forcing the shape of the map:**
- The Compliance Framework cluster (ISO 27001, SOC 2, PCI DSS, GDPR, and the rising DORA/NIS2 wave) sits at commodity and **pulls everything above it rightward**. Risk framework choice and methodology are being dragged toward NIST CSF / ISO 27005 standardisation because audit evidence demands it.
- **NIST AI RMF (Jan 2023)** and the **EU AI Act** are the forcing function that will pull LLM-as-Risk out of genesis far faster than a purely technical market would.
- Cyber Insurance underwriting post-2021-22 is now a *regulatory* force in disguise: underwriters demand MFA, EDR, backups — they are effectively dictating the minimum SOC stack.

**Regulatory-driven directional shape:**
- Things forced right by regulators: Compliance Framework, Risk Framework, Risk Register (via audit evidence), Cyber Insurance.
- Things that remain custom because regulators have not yet specified them: FAIR quantification (no regulator mandates monetary quantification yet), LLM-Assisted Defence, LLM-as-Risk.

### Inertia Points
- **Risk Matrices (x):** culturally entrenched at boardroom level. Replacement by FAIR quantification is technically correct but blocked by executive expectation of heat-map dashboards.
- **FAIR Quantification (x):** talent-scarcity inertia — there simply are not enough qualified FAIR analysts to productise the practice at pace.

### Opportunities
- Productise FAIR quantification inside GRC platforms (this is a clear commodity-leverage opportunity: visibility is moderate, evolution is low).
- Bundle LLM-Assisted Defence into SOC-as-a-service offerings (accelerate the settlers-to-planners handoff).
- Treat LLM-as-Risk as a first-class risk-register entry *now*, ahead of regulator enforcement — the map shows executives' visibility into this risk is high but its maturity is near-zero, creating a dangerous blind spot.
- Use cyber-insurance underwriting questionnaires as a de-facto baseline compliance checklist.

### Threats
- **Blind-spot on LLM-as-Risk:** register dependency on a genesis-stage risk (R = 0.63) means executives are accountable for a risk they cannot yet quantify.
- **Heat-map theatre:** risk matrices may be satisfying boards while obscuring material tail risk that FAIR would surface.
- **Underwriter capture:** if cyber insurers become the de-facto regulator, risk posture becomes a function of insurance pricing, not executive appetite.
- **LLM-Assisted Defence concentration:** dependence on a small set of hyperscaler-owned copilots (Microsoft Security Copilot) creates vendor-concentration risk.

## Output Format

```yaml
wardley_map:
  metadata:
    title: "Cybersecurity Risk Management from the Executive's Point of View (May 2023)"
    author: "arc-kit wardley-mapping skill (blind benchmark run)"
    date: "2026-04-22"
    scenario_date: "2023-05"
    version: "1.0"
    scope: "Enterprise cyber risk capability, executive-anchored"

  anchor:
    user: "Executives (Board, CEO, CFO, Audit & Risk Committee)"
    need: "Manage cybersecurity risk to an acceptable level given P&L, compliance, and stated risk appetite"

  components:
    - name: "Executives"
      evolution: "Commodity"
      position: 0.80
      visibility: 0.97
      depends_on: ["P&L Impact", "Compliance Obligations", "Risk Appetite", "Reporting to Board"]
      notes: "Anchor. Accountability universally mandated."
      movement: "none"
    - name: "P&L Impact"
      evolution: "Commodity"
      position: 0.90
      visibility: 0.88
      depends_on: ["Cyber Insurance", "Mitigation/Transfer/Accept Mix"]
      notes: "Mature accounting discipline."
      movement: "none"
    - name: "Compliance Obligations"
      evolution: "Commodity"
      position: 0.82
      visibility: 0.88
      depends_on: ["Compliance Framework", "Risk Framework"]
      notes: "Statutory obligations dictate structure."
      movement: "none"
    - name: "Risk Appetite"
      evolution: "Product"
      position: 0.55
      visibility: 0.88
      depends_on: ["Risk Register", "Mitigation/Transfer/Accept Mix"]
      notes: "Every board articulates it differently."
      movement: "none"
    - name: "Mitigation/Transfer/Accept Mix"
      evolution: "Product"
      position: 0.60
      visibility: 0.78
      depends_on: ["Risk Assessment Methodology"]
      notes: "Standard framing, bespoke mix."
      movement: "evolving"
    - name: "Cyber Insurance"
      evolution: "Commodity"
      position: 0.75
      visibility: 0.78
      depends_on: ["Risk Assessment Methodology", "Risk Register"]
      notes: "Mature market; post-2021-22 underwriting discipline."
      movement: "evolving"
    - name: "Risk Register"
      evolution: "Product"
      position: 0.68
      visibility: 0.72
      depends_on: ["Risk Assessment Methodology", "Asset Inventory", "LLM-as-Risk"]
      notes: "GRC platforms have productised the tooling."
      movement: "evolving"
    - name: "Risk Assessment Methodology"
      evolution: "Product"
      position: 0.55
      visibility: 0.65
      depends_on: ["Risk Identification Practice", "Asset Inventory", "Risk Framework", "Likelihood/Impact Scoring", "FAIR Quantification", "Risk Matrices"]
      notes: "Framework families standard; tailoring bespoke."
      movement: "none"
    - name: "Risk Identification Practice"
      evolution: "Product"
      position: 0.45
      visibility: 0.65
      depends_on: ["Asset Inventory", "Security Testing", "Security Monitoring", "LLM-as-Risk"]
      notes: "Trained practice, not a product."
      movement: "none"
    - name: "Asset Inventory"
      evolution: "Commodity"
      position: 0.72
      visibility: 0.65
      depends_on: []
      notes: "CMDB / cloud-asset discovery productised."
      movement: "evolving"
    - name: "Risk Framework (NIST CSF / ISO 27005)"
      evolution: "Product"
      position: 0.72
      visibility: 0.55
      depends_on: []
      notes: "NIST CSF 2.0 in draft (2023)."
      movement: "evolving"
    - name: "Compliance Framework (ISO 27001 / SOC 2 / PCI / GDPR)"
      evolution: "Commodity"
      position: 0.85
      visibility: 0.55
      depends_on: []
      notes: "Stable, auditable; regulatory centre of gravity."
      movement: "evolving"
    - name: "Risk Matrices"
      evolution: "Commodity"
      position: 0.78
      visibility: 0.48
      depends_on: []
      notes: "Ubiquitous heat-map; inertia point."
      movement: "inertia"
    - name: "Likelihood/Impact Scoring"
      evolution: "Product"
      position: 0.62
      visibility: 0.48
      depends_on: []
      notes: "Productised in GRC platforms."
      movement: "none"
    - name: "FAIR Quantification"
      evolution: "Custom"
      position: 0.32
      visibility: 0.48
      depends_on: []
      notes: "Talent-scarcity bottleneck; inertia point."
      movement: "inertia"
    - name: "Reporting to Board"
      evolution: "Product"
      position: 0.70
      visibility: 0.60
      depends_on: ["Security Monitoring", "Risk Register"]
      notes: "Cyber dashboards are a product category."
      movement: "evolving"
    - name: "Incident Response"
      evolution: "Commodity"
      position: 0.78
      visibility: 0.42
      depends_on: ["Security Monitoring", "SOC Tooling (SIEM/XDR)"]
      notes: "Mature retainer market."
      movement: "none"
    - name: "Security Monitoring"
      evolution: "Commodity"
      position: 0.85
      visibility: 0.38
      depends_on: ["SOC Tooling (SIEM/XDR)"]
      notes: "SOC-as-a-service commoditised."
      movement: "evolving"
    - name: "SOC Tooling (SIEM/XDR)"
      evolution: "Commodity"
      position: 0.72
      visibility: 0.35
      depends_on: []
      notes: "XDR accelerating rightward."
      movement: "evolving"
    - name: "Security Testing"
      evolution: "Product"
      position: 0.62
      visibility: 0.42
      depends_on: ["Pen Testing", "Bug Bounty"]
      notes: "Discipline productised; delivery expert-led."
      movement: "none"
    - name: "Pen Testing"
      evolution: "Product"
      position: 0.70
      visibility: 0.32
      depends_on: []
      notes: "Continuous pen-test platforms productising further."
      movement: "none"
    - name: "Bug Bounty"
      evolution: "Product"
      position: 0.55
      visibility: 0.32
      depends_on: []
      notes: "HackerOne/Bugcrowd/Intigriti."
      movement: "evolving"
    - name: "LLM-Assisted Defence"
      evolution: "Custom"
      position: 0.20
      visibility: 0.28
      depends_on: ["SOC Tooling (SIEM/XDR)", "Security Monitoring"]
      notes: "May 2023: Microsoft Security Copilot just announced; accelerating."
      movement: "accelerating"
    - name: "LLM-as-Risk (prompt injection, data leakage)"
      evolution: "Genesis"
      position: 0.12
      visibility: 0.55
      depends_on: []
      notes: "OWASP LLM Top 10 not yet published in May 2023; regulators pulling it into the register via NIST AI RMF and EU AI Act draft."
      movement: "accelerating"

  analysis:
    opportunities:
      - "Productise FAIR quantification inside GRC platforms."
      - "Bundle LLM-Assisted Defence into SOC-as-a-service."
      - "Treat LLM-as-Risk as first-class risk-register entry ahead of enforcement."
      - "Use cyber-insurance underwriting as de-facto compliance baseline."
    threats:
      - "Blind-spot on LLM-as-Risk (dependency risk R=0.63)."
      - "Risk-matrix heat-map theatre obscures tail risk."
      - "Underwriter capture — insurers become de-facto regulator."
      - "LLM-Assisted Defence vendor-concentration risk (hyperscaler copilots)."
    inertia_points:
      - component: "Risk Matrices"
        reason: "Boardroom expectation; cultural entrenchment despite academic critique"
      - component: "FAIR Quantification"
        reason: "Scarcity of qualified quantitative analysts"

  recommendations:
    immediate:
      - "Add LLM-as-Risk to the risk register explicitly, even if scoring is qualitative for now."
      - "Map current SOC stack against cyber-insurance questionnaire to find the regulatory-de-facto baseline."
    short_term:
      - "Pilot FAIR quantification on the top-10 risk register entries; build a settler-stage practice."
      - "Run a controlled LLM-Assisted Defence pilot with an SOC-analyst copilot; measure mean-time-to-triage delta."
    long_term:
      - "Replace board risk matrices with FAIR-driven loss-exceedance curves once quantitative maturity allows."
      - "Participate in NIST AI RMF and EU AI Act working groups to shape the LLM-as-Risk standardisation rather than react to it."
      - "Position on NIST CSF 2.0 ahead of adoption to avoid a retrofit."
```

## Analysis Checklist (arc-kit)

- **Completeness:** anchor, components, dependencies, and movement all present. All items named in the scenario prompt are explicitly mapped (including mitigation/transfer/acceptance, cyber insurance, FAIR, likelihood/impact, risk matrices, pen testing, bug bounty, LLM defence and LLM risk).
- **Positioning:** every dependency respects visibility(a) >= visibility(b). Stages assigned using arc-kit Section A rubric; cross-checked with E(c) = (U+C)/2 for the four scenario-critical components.
- **Insights:** commodity-vs-expert split, regulatory shaping, and LLM duality all surfaced. Dependency-risk spot-check run on the three riskiest edges.
- **Strategic:** opportunities, threats, inertia, and phased recommendations provided.
