# Cybersecurity Risk Management — Wardley Map (Mid-to-Large Enterprise, May 2023)

## Scenario

Map cyber risk management in a mid-to-large enterprise as at May 2023. Scope covers threat intelligence, vulnerability management, incident response, identity and access, compliance/regulation, risk quantification, security operations, and controls. The map frames the question: *what differentiates a strong security programme from an average one, what should be treated as a utility, and where is cyber risk most exposed?*

The map is anchored on three user types:

- **Board & Regulator** — consumes risk reports, regulatory attestations, cyber insurance posture. Drives accountability and disclosure.
- **CISO & Security Leadership** — owns the risk register and the response plan; authorises controls and investment.
- **Business Users** — the protected population; also the consumer of MFA/SSO prompts and awareness training.

---

## Map (OWM)

```owm
title Cybersecurity Risk Management (Mid-to-Large Enterprise, May 2023)
style wardley

// Anchors — three user types who "need" cyber risk outcomes
anchor Board & Regulator [0.99, 0.55]
anchor CISO & Security Leadership [0.97, 0.45]
anchor Business Users [0.95, 0.70]

// User-facing outcomes and artefacts
component Board Cyber Risk Report [0.90, 0.45]
component Regulatory Attestation [0.88, 0.55]
component Risk Register [0.86, 0.55]
component Security Awareness Training [0.85, 0.78]
component Incident Response Plan [0.84, 0.55]
component Cyber Insurance Posture [0.82, 0.55]

// Risk quantification and governance (emerging discipline)
component FAIR Risk Quantification [0.80, 0.32]
component Control Effectiveness Assessment [0.78, 0.45]
component GRC Platform [0.70, 0.60]
component Third-Party Risk Management [0.74, 0.55]

// Identity layer (highly visible to users via MFA / SSO prompts)
component Identity & Access Management [0.74, 0.68]
component Multi-Factor Authentication [0.72, 0.80]
component Single Sign-On [0.70, 0.82]
component Zero Trust Architecture [0.76, 0.40]
component Identity Threat Detection (ITDR) [0.76, 0.28]
component Passwordless Authentication [0.76, 0.35]
component Privileged Access Management [0.58, 0.55]

// Core security capability layer
component Threat Intelligence [0.58, 0.50]
component Vulnerability Management [0.66, 0.60]
component Incident Response Operations [0.68, 0.55]
component Security Operations (SOC) [0.66, 0.60]
component Threat Hunting [0.62, 0.38]
component Detection Engineering [0.56, 0.35]

// Controls framework — knowledge artefacts
component NIST CSF / ISO 27001 [0.56, 0.68]
component MITRE ATT&CK Framework [0.50, 0.60]
component SBOM / Software Supply Chain [0.54, 0.25]

// Security tooling (product stage, mostly)
component GenAI Security Copilot [0.72, 0.10]
component AI-Driven Threat Detection [0.55, 0.22]
component SIEM [0.52, 0.65]
component SOAR [0.54, 0.55]
component Security Data Lake [0.48, 0.25]
component EDR / XDR [0.50, 0.70]
component CNAPP / CSPM [0.42, 0.55]
component Web / Cloud Proxy (SSE) [0.46, 0.62]
component DLP [0.52, 0.60]
component Email Security Gateway [0.50, 0.80]
component Vulnerability Scanners [0.42, 0.78]
component Patch Management [0.45, 0.75]
component CAASM / Attack Surface Mgmt [0.40, 0.30]
component Deception / Honeypots [0.30, 0.30]

// Asset and data foundation
component Asset Inventory [0.38, 0.55]
component Log Collection & Retention [0.35, 0.72]
component Endpoint Agents [0.40, 0.75]
component Network Telemetry [0.32, 0.72]

// Crypto and secrets
component Secrets Management [0.30, 0.60]
component PKI & Certificate Management [0.25, 0.82]
component Cryptography [0.22, 0.92]

// Network and infra foundations
component Firewalls [0.28, 0.82]
component Backup & Disaster Recovery [0.26, 0.80]
component Directory Services [0.30, 0.88]
component Cloud Infrastructure [0.18, 0.88]
component Internet / DNS [0.12, 0.95]
component Network Infrastructure [0.10, 0.90]
component Electricity [0.05, 0.97]

// Knowledge / specialist inputs
component Threat Intel Feeds (ISACs) [0.48, 0.62]
component Security Analyst Talent [0.45, 0.30]
component Threat Actor Research [0.42, 0.18]

// Dependencies — anchors to top-level outcomes
Board & Regulator->Board Cyber Risk Report
Board & Regulator->Regulatory Attestation
Board & Regulator->Cyber Insurance Posture
CISO & Security Leadership->Risk Register
CISO & Security Leadership->Incident Response Plan
CISO & Security Leadership->Board Cyber Risk Report
CISO & Security Leadership->Regulatory Attestation
CISO & Security Leadership->Control Effectiveness Assessment
CISO & Security Leadership->Third-Party Risk Management
Business Users->Security Awareness Training
Business Users->Multi-Factor Authentication
Business Users->Single Sign-On

// Top-level outcomes depend on risk quantification and governance
Board Cyber Risk Report->FAIR Risk Quantification
Board Cyber Risk Report->Risk Register
Board Cyber Risk Report->Control Effectiveness Assessment
Regulatory Attestation->GRC Platform
Regulatory Attestation->Control Effectiveness Assessment
Risk Register->GRC Platform
Risk Register->Threat Intelligence
Incident Response Plan->Incident Response Operations
Cyber Insurance Posture->Control Effectiveness Assessment
Cyber Insurance Posture->FAIR Risk Quantification

// Risk quantification layer
FAIR Risk Quantification->Threat Intelligence
FAIR Risk Quantification->Asset Inventory
Control Effectiveness Assessment->NIST CSF / ISO 27001
Control Effectiveness Assessment->Vulnerability Management
Control Effectiveness Assessment->Identity & Access Management
GRC Platform->NIST CSF / ISO 27001
Third-Party Risk Management->GRC Platform

// Core capabilities depend on tooling
Threat Intelligence->Threat Intel Feeds (ISACs)
Threat Intelligence->Threat Actor Research
Threat Intelligence->MITRE ATT&CK Framework
Vulnerability Management->Vulnerability Scanners
Vulnerability Management->Patch Management
Vulnerability Management->Asset Inventory
Vulnerability Management->CAASM / Attack Surface Mgmt
Vulnerability Management->SBOM / Software Supply Chain
Incident Response Operations->Security Operations (SOC)
Incident Response Operations->SOAR
Incident Response Operations->EDR / XDR
Incident Response Operations->Security Analyst Talent
Security Operations (SOC)->SIEM
Security Operations (SOC)->Security Data Lake
Security Operations (SOC)->Detection Engineering
Security Operations (SOC)->Threat Hunting
Security Operations (SOC)->Security Analyst Talent
Detection Engineering->MITRE ATT&CK Framework
Detection Engineering->Log Collection & Retention
Threat Hunting->Log Collection & Retention
Threat Hunting->Threat Intelligence
Threat Hunting->AI-Driven Threat Detection

// Identity depends on foundations
Identity & Access Management->Single Sign-On
Identity & Access Management->Multi-Factor Authentication
Identity & Access Management->Directory Services
Identity & Access Management->Privileged Access Management
Privileged Access Management->Directory Services
Privileged Access Management->Secrets Management
Single Sign-On->Directory Services
Multi-Factor Authentication->Directory Services
Passwordless Authentication->PKI & Certificate Management
Passwordless Authentication->Identity & Access Management
Identity Threat Detection (ITDR)->Identity & Access Management
Identity Threat Detection (ITDR)->SIEM

// Zero Trust and controls frameworks
Zero Trust Architecture->Identity & Access Management
Zero Trust Architecture->Web / Cloud Proxy (SSE)
Zero Trust Architecture->Network Telemetry
NIST CSF / ISO 27001->MITRE ATT&CK Framework

// Tooling dependencies
SIEM->Log Collection & Retention
SIEM->Cloud Infrastructure
SOAR->SIEM
SOAR->EDR / XDR
Security Data Lake->Log Collection & Retention
Security Data Lake->Cloud Infrastructure
EDR / XDR->Endpoint Agents
CNAPP / CSPM->Cloud Infrastructure
DLP->Endpoint Agents
DLP->Email Security Gateway
Email Security Gateway->Cloud Infrastructure
Web / Cloud Proxy (SSE)->Cloud Infrastructure
Web / Cloud Proxy (SSE)->Network Infrastructure
Vulnerability Scanners->Asset Inventory
Patch Management->Asset Inventory
CAASM / Attack Surface Mgmt->Asset Inventory
CAASM / Attack Surface Mgmt->Cloud Infrastructure
Deception / Honeypots->Network Infrastructure

// GenAI dependencies
GenAI Security Copilot->SIEM
GenAI Security Copilot->Threat Intelligence
GenAI Security Copilot->Cloud Infrastructure
AI-Driven Threat Detection->Security Data Lake
AI-Driven Threat Detection->Log Collection & Retention

// Asset and data foundation
Asset Inventory->Cloud Infrastructure
Asset Inventory->Directory Services
Log Collection & Retention->Cloud Infrastructure
Endpoint Agents->Cloud Infrastructure
Network Telemetry->Network Infrastructure

// Crypto and secrets
Secrets Management->PKI & Certificate Management
Secrets Management->Cryptography
PKI & Certificate Management->Cryptography

// Foundational
Firewalls->Network Infrastructure
Backup & Disaster Recovery->Cloud Infrastructure
Backup & Disaster Recovery->Cryptography
Directory Services->Cloud Infrastructure
Cloud Infrastructure->Electricity
Network Infrastructure->Electricity
Internet / DNS->Network Infrastructure
Internet / DNS->Electricity
Cryptography->Electricity

// Evolution bets (next 18-36 months)
evolve FAIR Risk Quantification 0.55
evolve GenAI Security Copilot 0.45
evolve CAASM / Attack Surface Mgmt 0.55
evolve Passwordless Authentication 0.58
evolve SBOM / Software Supply Chain 0.55
evolve Zero Trust Architecture 0.60
evolve Security Data Lake 0.50
evolve Detection Engineering 0.55

// Annotation zones
note Differentiation zone [0.70, 0.25]
note Rent / buy [0.35, 0.85]
note Utility floor [0.10, 0.95]
```

Validator: **OK: 60 components/anchors, 107 edges — no violations** (see section (g) below).

---

## Strategic analysis

Read the map left-to-right: *everything on the right of ε ≈ 0.70 is a utility you should rent; everything on the left of ε ≈ 0.35 is either a bet you fund or a risk you accept*. The specific cybersecurity answer to "what differentiates vs. what is commodity" is sharper than it first appears, because cyber security is asymmetric — commodity controls keep up with commodity attacks, but new attack classes (supply chain, identity-tier, AI-augmented) live in Genesis and Custom Built, which is exactly where the enterprise *cannot* buy its way to protection off the shelf.

### a. Differentiation opportunities (top 3)

These are the user-visible components still in Genesis or Custom Built — where building bespoke yields real advantage and where a vendor won't save you.

1. **FAIR Risk Quantification** (Custom Built, ε ≈ 0.32) — the bridge between technical telemetry and board-level language. Boards in 2023 are increasingly asking for dollar-denominated loss exposure, not "red/amber/green". Enterprises that can speak this language win budget and insurance terms. Adoption is still under a quarter of large enterprises, so this is the single highest-leverage differentiation move available to a CISO who wants to change the conversation.
2. **Zero Trust Architecture** (Custom Built, ε ≈ 0.40) — every Zero Trust deployment is bespoke because it's a re-architecture, not a product you buy. The reference frameworks exist (NIST SP 800-207, US EO 14028), but translation into a specific enterprise's identity, network, and app topology is where the engineering lives. A mature Zero Trust programme is a credible moat against credential-based and lateral-movement attacks, and it is what most ransomware operators still can't easily bypass.
3. **Detection Engineering** (Custom Built, ε ≈ 0.35) — off-the-shelf SIEM rules catch commodity attacks. The attacker TTPs that hurt mid-to-large enterprises (business email compromise chains, abuse of valid accounts, cloud-specific kill chains) need detections written against *your* telemetry, *your* environment, by engineers who understand both ATT&CK and your normal. This is where a good security team pulls ahead of a well-tooled-but-generic one.

### b. Commodity-leverage candidates (top 3)

These are deep, mature components that belong on someone else's P&L. A mid-to-large enterprise building any of these in-house is wasting engineering payroll.

1. **Email Security Gateway** (Commodity (+utility), ε ≈ 0.80) — Proofpoint, Mimecast, Microsoft Defender for Office, Abnormal. Rent, don't build. This is the single highest-volume, highest-automation security control and nobody has built a bespoke email gateway that outperformed the market in a decade.
2. **Multi-Factor Authentication** / **Single Sign-On** (Commodity (+utility), ε ≈ 0.80–0.82) — Okta, Entra ID (Azure AD), Duo, Ping. These are utilities; if you're still running homegrown SSO in 2023, you have an engineering liability, not a security investment.
3. **PKI & Certificate Management** (Commodity (+utility), ε ≈ 0.82) — DigiCert, Entrust, Let's Encrypt at the internet edge; cloud provider KMS for internal. The exception is the crypto-agility work you need for post-quantum readiness, but that's policy and inventory, not building a CA from scratch.

Honorable mentions: **Firewalls** (Commodity (+utility)) — the network-perimeter box is fully commoditised; the only interesting question is whether you even need one given Zero Trust; **Backup & Disaster Recovery** (Commodity (+utility)); **Vulnerability Scanners** (near-Commodity (+utility)) — Tenable, Qualys, Rapid7 are interchangeable at the utility level.

### c. Dependency risks (top 3)

Edges where a user-visible component depends on an immature or fragile foundation. These are where cyber risk is *most exposed* for the enterprise.

1. **Board Cyber Risk Report → FAIR Risk Quantification** — the most board-visible artefact in the map depends on a Custom Built analytical discipline that most enterprises implement ad-hoc. If the Board reads a dollar-loss figure without understanding it's drawn from a handful of SME judgement calls, the report gives false precision. This is the most common *credibility* failure in the current cyber-GRC conversation and it happens constantly.
2. **Incident Response Plan → Incident Response Operations → Security Analyst Talent** — the plan (Product (+rental), common and expected) sits on an operations layer that ultimately depends on scarce human capital (Custom Built, ε ≈ 0.30). A third of mid-market SOCs are under-staffed or running on outsourced MSSPs who don't know your environment. When the incident arrives at 3 a.m., this is the single fragility that determines outcome.
3. **Vulnerability Management → CAASM / Attack Surface Management** and **Vulnerability Management → SBOM / Software Supply Chain** — a Product (+rental) stage, board-visible capability is depending on two Custom Built foundations. Log4Shell (Dec 2021) showed that enterprises didn't know where their vulnerable dependencies ran; SBOM and CAASM are the response, but both are still too immature to trust as complete sources of truth. This is exactly the exposure attackers exploited in the 2020–2023 supply-chain wave.

Honourable mention: **Threat Hunting → AI-Driven Threat Detection** — a Custom Built practice depending on a Custom Built tool is an accelerating bet, not a stable foundation. Expect this pairing to drift for 18–24 months.

### d. Suggested gameplays

Named from Wardley's 61-play catalogue; each targets specific components on this map.

- **#36 Directed investment** on **FAIR Risk Quantification**, **Detection Engineering**, and **Zero Trust Architecture**. These are the three highest-differentiation components and they all repay concentrated engineering spend. Do not spread this investment thin across every Custom Built component.
- **#29 Harvesting** on **CAASM / Attack Surface Management** and **CNAPP / CSPM**. Both categories are consolidating; let the vendor landscape sort itself out, run parallel PoCs, and standardise on the winner in 12–18 months rather than betting now. Axonius, JupiterOne, Wiz, Orca — the field will narrow.
- **#43 Sensing Engines (ILC)** on **GenAI Security Copilot**. Microsoft Security Copilot was announced March 2023; it's invitation-only preview. Enrol in previews, generate usage data, but *do not make this an architectural commitment yet*. The Innovate-Leverage-Commoditise cycle will clarify winners by mid-2024.
- **#15 Open Approaches** on **SBOM / Software Supply Chain** and **MITRE ATT&CK**. Both are already open standards; contribute telemetry and detections back. Your engineering time is better spent contributing to SPDX/CycloneDX tooling than building proprietary SBOM infrastructure.
- **#41 Alliances** on **Threat Intelligence** via sector ISACs (FS-ISAC, H-ISAC, E-ISAC, etc.). The quality of commercial threat intel has plateaued; sector-specific peer intel is now the differentiator.
- **#1 Focus on user needs** across the whole programme — the CISO's real user is the Board/Regulator, but the security team still builds for itself more often than it admits. Every investment should trace back to an explicit risk scenario that Board would recognise.
- **#30 Standards game** — defensively, track NIST CSF 2.0 (in draft during 2023), SEC cyber-disclosure rules (proposed 2022), EU NIS2 (adopted Dec 2022), EU DORA (passed Jan 2023). Regulatory standardisation is a climatic force reshaping the right-hand side of this map.

### e. Doctrine violations

Checked against Wardley's 40 doctrine principles.

- Risk of violating **#1 Focus on user needs**: Many enterprise security programmes anchor implicitly on "the security team" rather than on Board, regulator, or business user. This map deliberately uses three explicit anchors to resist that trap.
- Risk of violating **#7 Use appropriate methods**: Running Agile across everything is a common pathology in security. It fits Genesis bets (FAIR modelling, GenAI pilots); it does not fit Commodity (+utility) patching SLA ops, which want Six Sigma discipline. Mid-market programmes often apply one method everywhere and lose on both ends.
- Risk of violating **#10 Know your users**: A single "the business" anchor is a doctrine smell — the Board, the auditor, the developer, and the call-centre user have different needs. This map uses three anchors; realistic implementations may need more (engineer/developer, customer-facing workforce, third parties).
- Risk of violating **#13 Manage inertia**: Cybersecurity programmes accumulate sunk capital in legacy SIEMs, on-prem firewalls, and proprietary PKI. **Inertia form #2 Sunk capital** and **#9 Re-architecture cost** are common in SIEM migrations to cloud-native stacks.
- Risk of violating **#2 Use a systematic mechanism of learning**: Many enterprises still rely on annual pentest reports for evidence of control effectiveness. Control Effectiveness Assessment should be continuous, not annual.

### f. Climatic context

Which of Wardley's 27 climatic patterns are actively reshaping this map in May 2023?

- **#3 Everything evolves** — the whole right-hand column of this map (MFA, SSO, email gateways, firewalls) was differentiation 15 years ago and is utility now. The current differentiators will follow.
- **#4 Multi-wave evolution** — Identity has been through at least three waves (on-prem AD → cloud directory → passwordless/Zero Trust). Each wave displaces rather than replaces; legacy AD will persist in mid-market for another decade.
- **#15–17 Inertia patterns** — *every* mid-to-large enterprise has accumulated inertia in legacy SIEMs, on-prem DCs, proprietary PKI, and headcount-heavy SOCs. Migration is a decade-long programme, not a project.
- **#27 Product-to-utility punctuated equilibrium** — currently visible in SIEM (cloud-native Microsoft Sentinel, Google Chronicle, Panther, Cribl disrupting Splunk); CASB/SWG → SSE/SASE (Zscaler, Netskope, Cato, Palo Alto Prisma); EDR absorbing into XDR platforms. Three simultaneous wars on the right half of the map.
- **#14 Capital flows to new areas** — VC money in 2023 was pouring into CNAPP, AI-security, and identity-threat detection — confirming the left side of this map as the 18–36 month front.
- **#18 You cannot measure evolution over time** — regulator-driven standardisation (NIS2, DORA, SEC, SOX-like cyber) is *also* an accelerator on the X-axis, outside pure supply-demand dynamics.

### g. Deep-placement notes

Three components got targeted deep-placement review rather than a pure cheat-sheet score:

- **GenAI Security Copilot** — cheat-sheet initial: Genesis strongly (all four rows: rare, poorly understood, "wonder" publication types, "different / exciting"). Microsoft Security Copilot was announced 28 March 2023 (eight weeks before the map date) and was invitation-only at that time. CrowdStrike, Palo Alto, and SentinelOne had not yet announced their GenAI offerings (most came in H2 2023). Google Cloud Duet AI was not yet in security. **Confirmed Genesis at ε = 0.10**, with evolve target of 0.45 over 18–24 months reflecting the speed at which hyperscaler-backed categories usually cross the chasm.
- **FAIR Risk Quantification** — cheat-sheet put this at Custom Built (Stage II). Deep check: FAIR Institute founded 2007; Open FAIR standard since 2013; Gartner 2022 Market Guide for Cyber-Risk Quantification shows ~10 named vendors (RiskLens/Safe, Axio, Kovrr, CyberSaint, Balbix, CRQ tools inside GRC suites); enterprise adoption estimated at 20–25% of large enterprises. Publications are mostly "build/construct/case-studies" not "focused on use". **Confirmed Custom Built at ε = 0.32**. Evolve target 0.55 reflects likely crossing into early Product (+rental) over 24 months as regulatory pressure (SEC rules) drives adoption.
- **CAASM / Attack Surface Management** — cheat-sheet initial at low Custom Built. Deep check: Gartner named the category in 2021; active vendors include Axonius, JupiterOne, Panaseer, IBM Randori, Microsoft Defender EASM, Palo Alto Cortex Xpanse, Qualys CSAM. 10–15 vendors, most under 5 years old as standalone products. Publications are "build/construct". **Confirmed Custom Built at ε = 0.30**. Evolve target 0.55 — this category will likely either consolidate into CNAPP/XDR platforms or settle as a standalone Product (+rental) tier by 2025.

No deep placement needed for obvious Commodity (+utility) components (Cloud Infrastructure, Electricity, DNS, Email Gateway, MFA) or for widely published Product (+rental) stage tools (SIEM, EDR/XDR, SSO).

### h. Caveat

Evolution trajectories (`evolve` arrows) on this map are scenarios, not forecasts. Regulatory shocks (SEC final rules, NIS2 deadlines) and exogenous events (a major supply-chain breach, a nation-state escalation, a GenAI jailbreak that weaponises Copilot-style tools) could reshape several positions faster than the map predicts. Wardley's climatic pattern #18: *"you cannot measure evolution over time or adoption."*

---

## Where cyber risk is most exposed — the short answer

If the map had to compress to one sentence: **a May 2023 mid-to-large enterprise is over-invested in the right-hand half of the map (commodity tooling that every peer has) and under-invested in the left-hand half (risk quantification, detection engineering, Zero Trust, supply-chain visibility) — which is exactly where modern attacks operate.**

The three specific exposure hotspots:

1. **The board-reporting stack** (FAIR Quantification, Control Effectiveness) is a Custom Built foundation supporting a user-visible outcome. Credibility gap.
2. **Supply-chain visibility** (SBOM, CAASM) is Custom Built under a Product (+rental) stage Vulnerability Management function. Blind-spot gap.
3. **Identity-tier attack detection** (ITDR) is Custom Built under a Product (+rental) stage IAM. Lateral-movement gap.

The strategic move: treat the right-hand side as pure utility (rent, standardise, commoditise your own spend), free up engineering capacity, and direct it at the three Custom Built exposures where in-house engineering actually changes the risk posture.

---

*Validator output, for the record:*

```
OK: 60 components/anchors, 107 edges — no violations.
```
