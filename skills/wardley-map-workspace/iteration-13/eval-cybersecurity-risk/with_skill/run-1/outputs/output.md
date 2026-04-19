# Enterprise Cybersecurity Risk Management — Wardley Map (May 2023)

**Scenario:** Cybersecurity risk management in a mid-to-large enterprise, May 2023. Covers threat intelligence, vulnerability management, incident response, identity & access, compliance/regulation, risk quantification, security operations, and controls.

**Anchors (2):** the **CISO / Board** (strategic risk owner) and an **Employee / Business User** (endpoint user who consumes security controls as a cost of doing work). Two anchors are needed because several components — SSO, awareness training, email security — are primarily shaped by the employee-facing experience while almost everything else is shaped by the CISO's governance agenda.

---

## Map

```owm
title Enterprise Cybersecurity Risk Management (May 2023)
style wardley

// Anchors — two user types
anchor CISO / Board [0.99, 0.50]
anchor Employee / Business User [0.95, 0.60]

// User-facing governance & reporting (ν 0.80-0.92)
component Board Risk Reporting [0.90, 0.35]
component Executive Risk Dashboard [0.87, 0.45]
component Security Awareness Training [0.85, 0.70]
component SSO Access Experience [0.84, 0.80]
component Incident Response Playbooks [0.82, 0.55]

// Strategic risk & compliance programmes (ν 0.65-0.78)
component Cyber Risk Quantification (FAIR) [0.76, 0.30]
component Cyber Insurance [0.78, 0.55]
component Third-Party / Vendor Risk [0.72, 0.50]
component Compliance & Audit Management [0.70, 0.65]
component Security Controls Framework [0.66, 0.70]

// Security functions — what the CISO manages as services (ν 0.58-0.72)
component Zero Trust Architecture [0.72, 0.30]
component Incident Response (function) [0.70, 0.50]
component Security Operations Centre (SOC) [0.68, 0.55]
component Threat Hunting [0.62, 0.35]
component Penetration Testing / Red Team [0.60, 0.55]
component Digital Forensics [0.58, 0.55]

// Defensive tooling (ν 0.45-0.60)
component Threat Intelligence Platform [0.58, 0.55]
component Vulnerability Management [0.56, 0.70]
component SOAR [0.56, 0.45]
component SIEM [0.54, 0.65]
component EDR / XDR [0.52, 0.55]
component DLP [0.48, 0.60]
component Email Security Gateway [0.46, 0.80]

// Identity stack (ν 0.40-0.72)
component MFA [0.68, 0.80]
component Identity Governance (IGA) [0.55, 0.50]
component Privileged Access Mgmt (PAM) [0.45, 0.55]

// Architectural controls (ν 0.28-0.42)
component Cloud Security Posture Mgmt (CSPM) [0.40, 0.55]
component Network Segmentation [0.35, 0.70]
component SBOM / Software Supply Chain [0.32, 0.30]
component Endpoint Management [0.30, 0.75]

// Foundations (ν 0.08-0.22)
component Asset Inventory / CMDB [0.22, 0.60]
component Threat Intel Feeds [0.20, 0.70]
component Log & Telemetry Pipeline [0.18, 0.75]
component Directory Services [0.15, 0.85]
component Cryptography / PKI [0.12, 0.82]
component Regulatory Frameworks (NIST / GDPR / DORA) [0.10, 0.70]
component Cloud Utilities [0.06, 0.92]

// Dependencies — CISO / Board
CISO / Board->Board Risk Reporting
CISO / Board->Executive Risk Dashboard
CISO / Board->Cyber Risk Quantification (FAIR)
CISO / Board->Cyber Insurance
CISO / Board->Compliance & Audit Management
CISO / Board->Third-Party / Vendor Risk
CISO / Board->Incident Response Playbooks
CISO / Board->Zero Trust Architecture
CISO / Board->Security Operations Centre (SOC)

// Employee / Business user
Employee / Business User->SSO Access Experience
Employee / Business User->Security Awareness Training
Employee / Business User->Email Security Gateway

// Reporting chain
Board Risk Reporting->Cyber Risk Quantification (FAIR)
Board Risk Reporting->Executive Risk Dashboard
Executive Risk Dashboard->SIEM
Executive Risk Dashboard->Vulnerability Management
Executive Risk Dashboard->Compliance & Audit Management

// Risk & compliance
Cyber Risk Quantification (FAIR)->Threat Intelligence Platform
Cyber Risk Quantification (FAIR)->Asset Inventory / CMDB
Cyber Insurance->Cyber Risk Quantification (FAIR)
Cyber Insurance->Security Controls Framework
Third-Party / Vendor Risk->Security Controls Framework
Compliance & Audit Management->Security Controls Framework
Compliance & Audit Management->Regulatory Frameworks (NIST / GDPR / DORA)
Security Controls Framework->Regulatory Frameworks (NIST / GDPR / DORA)

// Incident response chain
Incident Response Playbooks->Incident Response (function)
Incident Response Playbooks->SOAR
Incident Response (function)->Security Operations Centre (SOC)
Incident Response (function)->Digital Forensics

// Security functions → tools
Security Operations Centre (SOC)->SIEM
Security Operations Centre (SOC)->SOAR
Security Operations Centre (SOC)->EDR / XDR
Security Operations Centre (SOC)->Threat Hunting
Threat Hunting->Threat Intelligence Platform
Threat Hunting->Log & Telemetry Pipeline
Digital Forensics->Log & Telemetry Pipeline
Penetration Testing / Red Team->Vulnerability Management

// Zero Trust consumes identity/network primitives
Zero Trust Architecture->Identity Governance (IGA)
Zero Trust Architecture->Network Segmentation
Zero Trust Architecture->MFA
Zero Trust Architecture->Privileged Access Mgmt (PAM)

// Tool dependencies
Threat Intelligence Platform->Threat Intel Feeds
Vulnerability Management->Asset Inventory / CMDB
SIEM->Log & Telemetry Pipeline
SOAR->SIEM
SOAR->EDR / XDR
EDR / XDR->Endpoint Management
EDR / XDR->Log & Telemetry Pipeline
DLP->Endpoint Management
Email Security Gateway->Threat Intel Feeds

// Identity dependencies
SSO Access Experience->MFA
SSO Access Experience->Directory Services
MFA->Directory Services
Identity Governance (IGA)->Directory Services
Privileged Access Mgmt (PAM)->Directory Services
Privileged Access Mgmt (PAM)->Cryptography / PKI

// Cloud / architecture
Cloud Security Posture Mgmt (CSPM)->Cloud Utilities
Cloud Security Posture Mgmt (CSPM)->Asset Inventory / CMDB
Network Segmentation->Cloud Utilities
SBOM / Software Supply Chain->Asset Inventory / CMDB
Endpoint Management->Cloud Utilities

// Foundational → cloud
Asset Inventory / CMDB->Cloud Utilities
Threat Intel Feeds->Cloud Utilities
Log & Telemetry Pipeline->Cloud Utilities
Directory Services->Cloud Utilities
Cryptography / PKI->Cloud Utilities

evolve Cyber Risk Quantification (FAIR) 0.55
evolve Zero Trust Architecture 0.55
evolve SBOM / Software Supply Chain 0.55
evolve SOAR 0.65

note Differentiation zone [0.60, 0.25]
note Utility / rent [0.10, 0.92]
```

**Validator result:** `OK: 39 components/anchors, 66 edges — no violations.`

---

## Strategic analysis

### a. Differentiation opportunities (top 3)

Enterprise cybersecurity is overwhelmingly a buy-and-integrate market, so genuine differentiation in a corporate security programme lives in a narrow band: governance artefacts the board consumes, and the architectural overlay that ties commodity tooling into a coherent posture.

1. **Board Risk Reporting** (Custom Built, edging into Product (+rental)) — how the CISO tells the story of cyber risk to the board. Every enterprise does this, almost no two do it well. The component closest to the Board anchor with the most unmodelled content: risk tolerance statements, scenario narratives, regulatory exposure framing. This is where a CISO earns or loses credibility.
2. **Cyber Risk Quantification (FAIR)** (Custom Built) — the translation layer from technical telemetry into monetary expected loss. FAIR is a published method but in May 2023 enterprise adoption is patchy, tooling (RiskLens, Axio) is early Product (+rental), and most firms run bespoke spreadsheets. This is the component that turns a qualitative heat-map into a number the CFO will argue with — genuine strategic leverage.
3. **Zero Trust Architecture** (Custom Built) — not a product you buy but an architectural stance that composes IGA + MFA + network segmentation + PAM into a coherent model. Post-NIST SP 800-207 and the 2021 US federal Executive Order, the pattern is named but enterprise implementations are still bespoke. A coherent Zero Trust architecture is defensible; a collection of Zero Trust vendors is not.

### b. Commodity-leverage candidates (top 3)

Rent, don't build. These components are deep in the stack, mature, and hyperscaler-adjacent.

1. **Cloud Utilities** (Commodity +utility) — compute, storage, networking. Treat as a metered utility; never re-platform.
2. **Directory Services** (Commodity +utility) — Active Directory / Entra ID / Okta Directory. Multiple vendors, fully standardised protocols (LDAP, SCIM, SAML, OIDC). Pay a vendor; do not build.
3. **Cryptography / PKI** (Commodity +utility) — certificate authorities, HSMs, KMS. Cloud-native KMS (AWS KMS, Azure Key Vault, GCP KMS) have commoditised what was a custom build ten years ago. Also watchable: **MFA** is in the same bucket at edge-of-Commodity (+utility) — buy, don't build.

### c. Dependency risks (top 3)

These are the visible-on-fragile-foundation edges where a board-level or user-facing commitment is pinned on an immature layer.

1. **CISO / Board → Cyber Risk Quantification (FAIR)** — the board is increasingly asking "what's our cyber risk in dollars?" but the answer depends on a method still in Custom Built. The risk is either a false precision that misleads the board, or a breakdown of trust when a quantified estimate proves wildly wrong after an incident. Highest-exposure edge in the map.
2. **CISO / Board → Zero Trust Architecture** — strategic commitments (often mandated by regulators post-2021) rest on an architectural pattern that is industry-named but enterprise-implementations are bespoke. Most enterprises are buying "Zero Trust" as a marketing label from vendors without the architecture underneath.
3. **Cyber Insurance → Cyber Risk Quantification (FAIR)** — insurers now demand quantified loss estimates to price premiums; insureds are using immature internal FAIR models to produce those estimates. The whole economic hedge rests on a Custom Built methodology. Post-2022 insurer pull-back (Lloyd's war-exclusion clauses, capacity crunches) makes this especially exposed.

Secondary risks worth noting: **SOC → Threat Hunting** (SOC effectiveness increasingly depends on a Custom-Built practice with scarce talent), and **Incident Response Playbooks → SOAR** (automated response depends on SOAR which is still industrialising — SOAR vendor consolidation through 2022-23 left many enterprises mid-migration).

### d. Suggested gameplays

- **#36 Directed investment** on **Board Risk Reporting** and **Cyber Risk Quantification (FAIR)** — these are the two highest-D components a CISO can actually influence. Everything below them is a commodity fight.
- **#15 Open Approaches** on **SBOM / Software Supply Chain** — post-Log4j and US Executive Order 14028, SBOM is a forced industrialisation. Join CycloneDX / SPDX rather than fighting a proprietary format.
- **#29 Harvesting** on **EDR/XDR, SIEM, SOAR, Vulnerability Management** — the vendor consolidation in 2022–2023 (Microsoft Sentinel + Defender bundle, Palo Alto Cortex, CrowdStrike Falcon platform) is rewarding buyers who wait and consolidate on a winning stack.
- **#41 Alliances** on **Cyber Insurance** and **Threat Intel Feeds** — alliance with insurer(s) aligns risk quantification with underwriting models; ISAC/ISAO participation is essentially a doctrine move for threat intel.
- **#26 Differentiation** on **Security Awareness Training** — most of the market is commodity compliance-checkbox training; a genuinely engaging programme is a disproportionate risk reducer (Verizon DBIR data consistently shows human error as the top vector).
- **#43 Sensing Engines (ILC)** on **AI-assisted SOC tooling** (not explicitly mapped — emerging in May 2023 with Microsoft Security Copilot announced in March). Watch the Genesis space; don't bet the SOC budget on it yet.
- **#7 Education** on **Zero Trust Architecture** inside the business — the biggest obstacle to Zero Trust is not tooling but business-unit inertia (users experience it as friction). Pre-empt consumer-side inertia forms #6 (confusion over method) and #8 (skill-acquisition cost).

### e. Doctrine notes

- **#1 Focus on user needs** — two anchors correctly represent both the CISO (whose "need" is defensible risk posture) and the Employee (whose "need" is unobtrusive, usable controls). A map with only the CISO anchor would hide the large number of controls whose effectiveness is gated on employee adoption (awareness training, MFA, email security, SSO UX).
- **#10 Know your users** — two anchors are correct; if the enterprise is regulated, a third anchor (**Regulator / Auditor**) would often be warranted. For a "mid-to-large enterprise" non-regulated default this is folded into the CISO's duties.
- **#13 Manage inertia** — the map contains significant inertia loci: legacy Active Directory (sunk capital / re-architecture cost, inertia forms #2 and #9), SIEM migration fatigue (form #9), and the human-capital inertia around SOC analyst roles (#4). These are real constraints on any transformation programme.
- **⚠ #2 Use a systematic mechanism of learning** — possible violation: most enterprises treat incident post-mortems as one-offs, not as inputs back into FAIR models or controls framework revisions. The map edge `Cyber Risk Quantification → Threat Intelligence` should be bidirectional in practice; it's not in most programmes.
- **⚠ #25 Set exceptional standards** (on commoditising infrastructure) — enterprises often over-customise what should be commodity (bespoke SIEM parsers, custom MFA shims); doctrine says accept the standard unless differentiation is real.

### f. Climatic context

- **#3 Everything evolves** — the whole right-hand half of this map (MFA, SIEM, EDR, VM, directory) was Custom Built 10 years ago. It will all be deeper into Commodity (+utility) in 5 years. Plan for the slide.
- **#15–17 Inertia** — the three Wardley inertia climatics bite hard in enterprise security: past success with point products creates resistance to platform consolidation; existing practices (perimeter defence) resist Zero Trust; and existing political capital (CISO's reputation built on legacy stack) resists re-tooling.
- **#27 Product → utility punctuated equilibrium** — SIEM is visibly in a "war": Splunk's IPO-era dominance eroding under Microsoft Sentinel / Chronicle / hyperscaler-native pricing; classic Stage III → Stage IV transition with price competition intensifying.
- **#4 Multi-wave evolution** — Identity has gone through multiple waves (on-prem AD → federation → SSO/SAML → OIDC + passwordless/FIDO2). Passwordless (in May 2023) is a new wave, not a refinement of MFA.
- **#20 Efficiency enables new sources of worth** — the commoditisation of cloud KMS, log pipelines, and telemetry has enabled higher-order products (CSPM, XDR, cloud-native SIEM) that were uneconomical a decade ago. Expect the same pattern on the next layer up (AI-assisted SOC, automated risk quantification) in the next 2–4 years.

### g. Deep-placement notes

I ran targeted placements on four components where the initial cheat-sheet pass was either borderline or the domain was fast-moving in May 2023:

1. **Cyber Risk Quantification (FAIR)** — initial cheat-sheet rows disagreed (method is published, so Certainty = III; Ubiquity is low, so II; User Perception mixed between "leading edge" and "common"). **Vendor landscape (May 2023):** RiskLens, Axio, Kovrr, ThreatConnect Risk Quantifier — a small handful, all early Product (+rental). Publications still "case studies and how-to" not "operations". **Placement confirmed at ε = 0.30 (Custom Built)** with an evolve target of 0.55 within 3–5 years as insurers and SEC disclosure rules force standardisation.
2. **Zero Trust Architecture** — initial placement wavered between II and III. **Publication type check:** NIST SP 800-207 (2020), CISA Zero Trust Maturity Model v2 (April 2023) — explicit maturity models signal early Product (+rental) industrialisation but enterprise implementations remain bespoke. **Vendor count:** many "Zero Trust" branded offerings (Zscaler, Cloudflare, Palo Alto Prisma, Cisco, Netskope) but no dominant architecture pattern. **Held at ε = 0.30 (Custom Built)**; the pattern is named but not yet standardised at the architecture level. Evolve target 0.55 reflects the CISA maturity model accelerating the transition.
3. **SBOM / Software Supply Chain** — initial cheat-sheet said Genesis/Custom (ε ≈ 0.15). **Regulatory signal:** US Executive Order 14028 (May 2021), NIST SSDF, CycloneDX and SPDX standards active. **Open-source activity:** very high — Sigstore, SLSA, in-toto all active in 2022–2023. **Placed at ε = 0.30** — still Custom Built but industrialising fast under regulatory pressure. Evolve target 0.55 reflects the expected 2025 compliance deadlines.
4. **SOAR** — initial placement was ε ≈ 0.55 (mid Product (+rental)). **Vendor consolidation:** Palo Alto acquired Demisto (2019), Splunk acquired Phantom (2018), IBM Resilient, Swimlane, Tines — clear consolidation pattern. **Bundled into XDR platforms by Microsoft, Palo Alto, CrowdStrike (2022-23).** Moved down to **ε = 0.45** because "standalone SOAR" is being cannibalised by XDR platform SOAR features — the component is more in transition than mature. Evolve target 0.65 reflects the expected absorption into platforms.

The other components were either obvious commodities (Cloud Utilities, Directory Services, Cryptography, MFA, Email Security Gateway) or obvious Custom Built / Product (+rental) placements where cheat-sheet agreement was high and no extra research would have moved the needle.

### h. Caveat

Evolution trajectories (the `evolve` arrows and the deep-placement target values) are **scenarios, not forecasts**. Wardley's climatic pattern #18 stands: *"you cannot measure evolution over time or adoption."* FAIR might industrialise in 3 years under SEC pressure, or stall for 10 if regulators back off. Zero Trust might commoditise into CASB/SSE product categories, or remain a bespoke architectural layer indefinitely. Treat the targets as directions of travel, not dates.

---

## Where cyber risk is most exposed — summary

The map says the answer in three lines:

1. **The board-facing governance layer is Custom Built.** Everything the CISO uses to *explain* risk (Board Risk Reporting, Cyber Risk Quantification, Cyber Insurance underwriting inputs) is still bespoke in May 2023. This is simultaneously the largest differentiation opportunity and the largest dependency risk, because misleading quantification produces overconfident strategic bets.
2. **The middle tooling layer is commoditising under you.** SIEM, EDR, VM, SOAR, IGA — all in Product (+rental), visibly consolidating into a handful of platforms (Microsoft, Palo Alto, CrowdStrike). The slide toward Commodity (+utility) is underway. The strategic error is to invest engineering differentiation there; harvest the winner and redirect budget upward.
3. **The deep foundations are already utilities.** Cloud, directory, crypto, regulatory frameworks — treat as given. The mistake is either re-building them (wasted spend) or assuming they are the locus of risk (they are not; the exposure is in the Custom Built governance layer above them).

**The single most exposed point:** the reliance of the board-level narrative (Board Risk Reporting, Cyber Insurance underwriting) on Cyber Risk Quantification methodology that is still Custom Built. Fix that edge and the rest of the programme becomes defensible. Leave it and every other control decision is being made on shaky foundations.
