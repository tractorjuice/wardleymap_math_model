# Enterprise Cyber Risk Management — Wardley Map (May 2023)

**Scenario:** Mid-to-large enterprise cyber risk management. Two user types: CISO / Board (strategic risk owner) and Employee / Business User (endpoint user consuming controls as a cost of doing work).

---

## Map (OWM)

```owm
title Enterprise Cyber Risk Management (May 2023)
style wardley

// Two anchors for two user types
anchor CISO / Board [0.99, 0.55]
anchor Employee / Business User [0.97, 0.70]

// User-facing outputs / experiences
component Board Risk Report [0.90, 0.40]
component Risk Appetite Statement [0.88, 0.35]
component Regulatory Attestation [0.86, 0.55]
component Secure Access to Work Apps [0.90, 0.78]
component Security Awareness Training [0.84, 0.70]
component Phishing Reporting Button [0.82, 0.75]

// Mid-chain programmes
component Risk Quantification (FAIR / cyber) [0.72, 0.35]
component Third-Party / Supply-Chain Risk [0.68, 0.40]
component Compliance Programme [0.70, 0.60]
component Control Framework (NIST CSF / ISO 27001) [0.66, 0.75]
component Cyber Insurance [0.68, 0.60]

// Operational capabilities
component Security Operations Centre (SOC) [0.60, 0.60]
component Incident Response (IR) [0.62, 0.55]
component Threat Intelligence [0.55, 0.55]
component Vulnerability Management [0.56, 0.70]
component Red Team / Pen Test [0.56, 0.45]
component Threat Hunting [0.48, 0.35]
component Detection Engineering [0.46, 0.30]
component Purple Team Exercises [0.56, 0.30]

// Identity & access
component Identity & Access Management (IAM) [0.65, 0.75]
component Single Sign-On (SSO) [0.55, 0.85]
component Multi-Factor Authentication (MFA) [0.58, 0.82]
component Privileged Access Management (PAM) [0.65, 0.65]
component Identity Governance (IGA) [0.65, 0.55]

// Controls and tooling
component Endpoint Detection & Response (EDR) [0.42, 0.75]
component SIEM / Log Aggregation [0.34, 0.80]
component SOAR / Automation [0.38, 0.55]
component Email Security Gateway [0.40, 0.85]
component Cloud Security Posture Mgmt (CSPM) [0.36, 0.60]
component Data Loss Prevention (DLP) [0.36, 0.65]
component Secrets Management [0.30, 0.70]
component Network Segmentation / Zero Trust [0.65, 0.45]
component Backup & Recovery [0.28, 0.85]

// Knowledge / data
component Asset Inventory [0.38, 0.55]
component CVE / CVSS Feeds [0.30, 0.90]
component MITRE ATT&CK Knowledge [0.26, 0.80]
component Threat Intel Feeds [0.28, 0.75]

// Regulation (external)
component Regulators (SEC, NIS2, DORA, GDPR) [0.22, 0.55]

// Deep infrastructure / utilities
component Cloud Platform (AWS / Azure / GCP) [0.18, 0.92]
component Directory (AD / Entra ID) [0.22, 0.88]
component PKI / Certificates [0.16, 0.88]
component DNS [0.10, 0.95]
component Network Transport [0.08, 0.95]
component Patch Distribution [0.20, 0.88]

// Dependencies — CISO / Board side
CISO / Board->Board Risk Report
CISO / Board->Risk Appetite Statement
CISO / Board->Regulatory Attestation
CISO / Board->Cyber Insurance
Board Risk Report->Risk Quantification (FAIR / cyber)
Board Risk Report->Compliance Programme
Risk Appetite Statement->Risk Quantification (FAIR / cyber)
Regulatory Attestation->Compliance Programme
Compliance Programme->Control Framework (NIST CSF / ISO 27001)
Compliance Programme->Regulators (SEC, NIS2, DORA, GDPR)
Risk Quantification (FAIR / cyber)->Asset Inventory
Risk Quantification (FAIR / cyber)->Threat Intelligence
Risk Quantification (FAIR / cyber)->Third-Party / Supply-Chain Risk
Cyber Insurance->Control Framework (NIST CSF / ISO 27001)

// Dependencies — Employee / Business User side
Employee / Business User->Secure Access to Work Apps
Employee / Business User->Security Awareness Training
Employee / Business User->Phishing Reporting Button
Secure Access to Work Apps->Identity & Access Management (IAM)
Secure Access to Work Apps->Single Sign-On (SSO)
Secure Access to Work Apps->Multi-Factor Authentication (MFA)
Phishing Reporting Button->Security Operations Centre (SOC)
Phishing Reporting Button->Email Security Gateway

// SOC / IR core
Security Operations Centre (SOC)->SIEM / Log Aggregation
Security Operations Centre (SOC)->SOAR / Automation
Security Operations Centre (SOC)->Detection Engineering
Security Operations Centre (SOC)->Threat Hunting
Security Operations Centre (SOC)->Threat Intelligence
Incident Response (IR)->Security Operations Centre (SOC)
Incident Response (IR)->Backup & Recovery
Incident Response (IR)->Threat Intelligence
Detection Engineering->MITRE ATT&CK Knowledge
Detection Engineering->SIEM / Log Aggregation
Threat Hunting->MITRE ATT&CK Knowledge
Threat Hunting->SIEM / Log Aggregation
Threat Intelligence->Threat Intel Feeds
Purple Team Exercises->Detection Engineering
Purple Team Exercises->Red Team / Pen Test

// Vulnerability management
Vulnerability Management->CVE / CVSS Feeds
Vulnerability Management->Asset Inventory
Vulnerability Management->Patch Distribution
Red Team / Pen Test->Vulnerability Management

// Identity
Identity & Access Management (IAM)->Directory (AD / Entra ID)
Single Sign-On (SSO)->Directory (AD / Entra ID)
Multi-Factor Authentication (MFA)->Directory (AD / Entra ID)
Privileged Access Management (PAM)->Identity & Access Management (IAM)
Identity Governance (IGA)->Identity & Access Management (IAM)

// Controls -> infra
Endpoint Detection & Response (EDR)->SIEM / Log Aggregation
Email Security Gateway->SIEM / Log Aggregation
Cloud Security Posture Mgmt (CSPM)->Cloud Platform (AWS / Azure / GCP)
Cloud Security Posture Mgmt (CSPM)->SIEM / Log Aggregation
Data Loss Prevention (DLP)->SIEM / Log Aggregation
Secrets Management->PKI / Certificates
Network Segmentation / Zero Trust->Identity & Access Management (IAM)
Network Segmentation / Zero Trust->Network Transport
Backup & Recovery->Cloud Platform (AWS / Azure / GCP)
SIEM / Log Aggregation->Cloud Platform (AWS / Azure / GCP)
SOAR / Automation->SIEM / Log Aggregation

// Third-party
Third-Party / Supply-Chain Risk->Asset Inventory
Third-Party / Supply-Chain Risk->Threat Intel Feeds

// Deep infra
Directory (AD / Entra ID)->Cloud Platform (AWS / Azure / GCP)
PKI / Certificates->DNS
Cloud Platform (AWS / Azure / GCP)->Network Transport
Patch Distribution->Network Transport

// Controls framework feeds program
Control Framework (NIST CSF / ISO 27001)->Asset Inventory
Control Framework (NIST CSF / ISO 27001)->Identity & Access Management (IAM)
Control Framework (NIST CSF / ISO 27001)->Vulnerability Management
Control Framework (NIST CSF / ISO 27001)->Incident Response (IR)

// Awareness training feed
Security Awareness Training->MITRE ATT&CK Knowledge

// Evolve arrows (scenario, not forecast)
evolve Risk Quantification (FAIR / cyber) 0.55
evolve SOAR / Automation 0.75
evolve Network Segmentation / Zero Trust 0.65
evolve Detection Engineering 0.55
evolve Threat Hunting 0.55

// Notes
note Board-visible differentiation [0.80, 0.30]
note Utility / rent-don't-build [0.15, 0.92]
```

**Validator:** `OK: 46 components/anchors, 68 edges — no violations.`

---

## Strategic analysis

The CISO/Board and the Employee see completely different maps of the same programme. The Board's view is dominated by **risk quantification, attestation, and insurance** — components that are mostly still Custom Built and poorly industrialised. The employee's view is dominated by **identity, MFA, SSO, email security, and awareness training** — controls that are firmly Product (+rental) or Commodity (+utility). The strategic tension of a cyber programme sits exactly in that gap: the board wants a number, the number depends on Custom-Built analytics, but the controls consuming most of the budget are already commodities.

### a. Differentiation opportunities (top 3)

1. **Detection Engineering** (Custom Built) — writing, tuning, and testing detections mapped to MITRE ATT&CK is where a strong programme pulls away from an average one. High visibility through the SOC chain, low maturity, highly visible to the board when breaches are avoided. Top of the D-rank list.
2. **Risk Quantification (FAIR / cyber)** (Custom Built) — the ability to give the board a defensible loss-exceedance curve instead of a red/amber/green heat map is the single biggest differentiator at board level in 2023. Still Custom Built; a few vendors (RiskLens, Axio) exist but most programmes roll their own.
3. **Threat Hunting / Purple Team Exercises** (Custom Built) — proactive, hypothesis-driven work that strong programmes do and average ones defer. These are the components that turn a reactive SOC into a learning organisation.

### b. Commodity-leverage candidates (top 3) — treat as utility

1. **Cloud Platform, DNS, Network Transport, PKI / Certificates** (all Commodity (+utility)) — utility infrastructure; rent from hyperscalers and certificate authorities, never build.
2. **SSO, MFA, Email Security Gateway, EDR, SIEM, Backup & Recovery, CVE/CVSS Feeds** (all Commodity (+utility) or late Product (+rental)) — mature markets with clear leaders (Okta/Entra, Microsoft Defender, CrowdStrike, Splunk/Sentinel, Proofpoint/Mimecast). Buy; don't staff a team to rebuild.
3. **Patch Distribution, Directory** (Commodity (+utility)) — shipped as part of Entra/Intune/AD; consume, don't engineer. Patch Tuesday is a process, not a differentiator.

### c. Dependency risks (top 3)

1. **Board Risk Report → Risk Quantification (FAIR / cyber)** — the board's most visible output sits on top of a Custom-Built analytic capability. If the quantification model is wrong or unverifiable, the entire board narrative is wrong. This is the highest R-score edge in the map.
2. **Secure Access to Work Apps → IAM / SSO / MFA → Directory (AD / Entra ID)** — every employee's daily experience depends on a single directory. Directory compromise (Midnight Blizzard / Okta 2022-23 pattern) cascades through every downstream control. Visible user consumption on a single-vendor foundation.
3. **Incident Response (IR) → Backup & Recovery → Cloud Platform** — IR plays that assume clean backups are common; if the backup plane runs on the same cloud tenancy as the compromised environment, the recovery path is fragile. A 2023 ransomware programme should not share a trust boundary between primary and backup.

### d. Suggested gameplays (from Wardley's 61)

- **#36 Directed investment** on Detection Engineering, Threat Hunting, and Risk Quantification — the three differentiators above. This is where engineering hours buy the most programme maturity.
- **#29 Harvesting** on SSO / MFA / Email Security / EDR / SIEM — let the market pick winners; buy the leader, don't run an RFP every two years.
- **#15 Open Approaches** on Detection Engineering — contribute detections to Sigma / Elastic / Splunk content packs; this raises community signal, improves hires, and reduces maintenance burden.
- **#41 Alliances** on Threat Intelligence and Third-Party / Supply-Chain Risk — ISACs, Mandiant/Recorded Future partnerships, SecurityScorecard / BitSight; no single firm can see the threat landscape alone.
- **#45 Two-factor market shaping** — the two anchors (Board, Employee) must both be served; a programme that optimises only for the Board ("great reports, awful MFA experience") loses employee compliance, and one that optimises only for the Employee ("frictionless but unreportable") loses the board.
- **#56 First-mover on compliance** — SEC cyber disclosure rules and NIS2/DORA deadlines create a narrow window in 2023–24 for firms that industrialise attestation early.
- **#43 Sensing Engines (ILC)** on SOAR / Automation — watch which playbooks emerge from the community; harvest rather than author.

### e. Doctrine notes

- Doctrine **#10 Know your users** — satisfied. Two anchors (CISO/Board and Employee) are explicit. Many enterprise cyber maps fail here by only anchoring to the CISO.
- Doctrine **#1 Focus on user needs** — satisfied on the Employee side (Secure Access, Awareness), partially on the Board side (Risk Report is what they actually want; compliance attestations are the regulator's need passed through).
- Doctrine **#2 Use a systematic mechanism of learning** — implicitly violated by most programmes: Purple Team findings rarely feed back into Detection Engineering in a measured way. Worth instrumenting.
- Doctrine **#13 Manage inertia** — active risk. Inertia forms #2 (sunk capital in legacy SIEMs), #4 (skill acquisition for cloud security), #8 (business-unit resistance to MFA/Zero-Trust friction), #14 (strategic-control loss on Directory) are all present. Name them before the Zero-Trust programme begins.

### f. Climatic context

- **#3 Everything evolves** — visible on SIEM (Product (+rental) → Commodity (+utility) shift via cloud-native SIEMs like Sentinel, Chronicle), on SOAR (Custom Built → Product (+rental) via Tines/Torq/Palo-Alto XSOAR), and Zero-Trust Network Access (Custom Built → Product (+rental) via Zscaler/Cloudflare/Netskope).
- **#15–17 Inertia patterns** — past-success and sunk-capital inertia is strong on on-prem SIEM and legacy network-security stacks; board-level inertia on FAIR-style quantification (they are used to heat maps).
- **#27 Punctuated equilibrium / product-to-utility** — SIEM is mid-transition (Stage III → IV). Identity (SSO/MFA) has crossed the transition; EDR is crossing it now. Expect margin compression and consolidation.
- **#22 Commoditisation enables higher-order systems** — commodity IAM and logging are the substrate enabling Detection Engineering and Threat Hunting to exist as disciplines; five years ago you built SIEM, now you build on top of it.

### g. Deep-placement notes

Four components warranted closer placement given the May-2023 landscape, based on known 2022–23 market signals (no external web search run in this session; placements use vendor-count and publication-type priors from the cheat sheet):

- **SOAR / Automation** — initial instinct Stage II (Custom Built) because automation playbooks still feel bespoke. Overridden to ε = 0.55 (early Product +rental) because Palo Alto XSOAR, Splunk Phantom, Tines, Torq, and Microsoft Sentinel's playbooks are clearly packaged products by 2023. Evolve arrow to 0.75 reflects 2024–25 trajectory.
- **Zero-Trust Network Access** — placed at ε = 0.45 (late Custom Built) not higher, because although Zscaler/Cloudflare/Netskope exist as products, the *enterprise programme* of Zero Trust is still custom per organisation. Evolve to 0.65.
- **Risk Quantification (FAIR / cyber)** — kept at ε = 0.35 (Custom Built). Vendors exist (RiskLens, Axio, Kovrr) but the Open FAIR standard is still emerging in enterprise board rooms; most programmes still use heat maps. Evolve to 0.55.
- **Detection Engineering** — kept at ε = 0.30. Sigma, MITRE ATT&CK, and Detection-as-Code are gaining traction, but practice varies wildly between programmes. Evolve to 0.55. (Flagged "in transition".)

### h. Caveat

Evolution positions and `evolve` arrows are scenarios, not forecasts. Per Wardley's climatic pattern #18: *"you cannot measure evolution over time or adoption."* The arrows indicate direction of market pressure as of May 2023; a CISO should revisit placements quarterly, not treat them as a roadmap.

---

## Framing answers

- **What differentiates a strong programme from an average one?** Detection Engineering, Threat Hunting, and defensible Risk Quantification — the three Custom-Built capabilities with high board visibility. Average programmes buy Stage III products and call it a day; strong programmes build Stage II capabilities *on top of* bought products.
- **What should be treated as a utility?** Cloud, DNS, Network Transport, PKI, SSO/MFA, Email Security, EDR, SIEM storage, Backup, CVE feeds, Patch Distribution. If you have engineers running these in-house beyond configuration, you are overpaying.
- **Where is cyber risk most exposed?** (a) The Directory / IAM single-point-of-trust (every downstream control fails if it fails), (b) the Board Risk Report sitting on top of immature quantification, and (c) the Backup/Recovery plane sharing a trust boundary with the production cloud tenancy.
