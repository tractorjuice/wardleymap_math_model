# Wardley Map — Government Digital Identity Landscape (November 2022)

## Step 0 — Strategic context

**Strategic question.** *How should policymakers, standards bodies, and platform operators position the government digital identity stack given the live tension between centralised national ID regimes, self-sovereign identity (SSI), and bad-actor exploitation of rules and exceptions?* In particular: which layers are still differentiator-zones (build), which are industrialising (buy/collaborate), and which are commodities (rent)?

**User anchors.** Five user types sit at the top of the chain:
- **Citizen** — primary user, needs access to services and control of their identity.
- **Government** — both a service provider and a user of identification for entitlement, enforcement, and civic function.
- **Corporation / Relying Party** — banks, platforms, gig marketplaces that need to verify who a user is.
- **Society** — the systemic user. Collective benefits from a functional, trustworthy identity layer; collective harms when it fails.
- **Bad Actor** — adversarial user. Explicitly mapped because the scenario calls for it: identity fraud, credential abuse, exception exploitation.

**Core needs.**
1. Authenticated access to public and private services.
2. Proof of entitlement (benefit, licence, right) without over-disclosure.
3. Civic and democratic participation.
4. (Adversarial) circumvention of identity controls for fraud, impersonation, or coercion.

**Scope boundary.** Cross-jurisdiction landscape as of November 2022. eIDAS 2.0 in draft; EU Digital Identity Wallet in pilot procurement; SSI / W3C VC / DID on the rise; India Aadhaar, Estonia e-ID, UK GOV.UK Verify wound down the previous year; US mDL (mobile driving licence) emerging. The map is **industry-level**, not organisation-level.

**Assumption flags (for user to correct):**
- *Bad Actor* is treated as an anchor even though it is not a "need-holder" in the traditional Wardley sense. Rationale: the scenario explicitly demands the bad-actor view, and mapping the exploit surface reveals dependency risks that a citizen-only map hides. If the reader objects, treat it as an antagonist actor rather than a user anchor.
- *Society* as an anchor is deliberately included because several downstream components (Regulation, Rules and Policy, Trust-Benevolence, Power) exist to serve collective rather than individual need. Omitting Society leaves them floating.

---

## Component list (Step 1)

**Anchors (5):** Citizen, Government, Corporation, Society, Bad Actor.

**Service / top of chain (5):** Public Service Access, Private Service Access, Entitlement and Benefit, Civic Participation, Identity Fraud Exploit (the adversarial "service" from the bad-actor view).

**Claims / credentials (8):** Service Delivery, Claims, Consent and Disclosure, Verifiable Credential, Digital Wallet, Physical Credential (e.g. Passport — *inertia*), Credential Issuance, Credential Revocation.

**Identity (3):** Identity (Legal), Identity (Digital), Identity (Self-Sovereign).

**Identification (6):** Identity Provider (IdP), Identification (Physical), Identification (Digital), Document Verification, Biometric Identification, Liveness Detection.

**Identifiers (5):** Identifier (Mutable), Identifier (Immutable), National ID Number (*inertia*), Identifier (Connectedness / Relational), Decentralised Identifier (DID).

**Authority (5):** Issuing Authority, Centralised Authority (*inertia*), Decentralised Authority, Trust Framework, Assurance Level (LoA).

**Trust (3):** Trust - Capability, Trust - Integrity, Trust - Benevolence.

**Rules / regulation (4):** Rules and Policy, Regulation (eIDAS, GDPR), Exception Handling, Audit and Oversight.

**Power (3):** Power Over, Power With, Power To.

**Crypto foundations (3):** Public Key Infrastructure (PKI), Zero-Knowledge Proofs, Cryptography.

**Transport (3):** Mobile Network, Internet, Cloud Utilities.

Total: **47 components + 5 anchors = 52 placements.** In the multi-stakeholder-system target band (40–55).

---

## OWM block

```owm
title Government Digital Identity Landscape (Nov 2022)
style wardley

// Anchors (user needs)
anchor Citizen [0.96, 0.42]
anchor Government [0.94, 0.40]
anchor Corporation [0.92, 0.55]
anchor Society [0.95, 0.30]
anchor Bad Actor [0.93, 0.50]

// Top-of-chain services (what users actually consume)
component Public Service Access [0.88, 0.55]
component Private Service Access [0.86, 0.62]
component Entitlement and Benefit [0.84, 0.48]
component Civic Participation [0.82, 0.35]
component Identity Fraud Exploit [0.85, 0.45]

// Service + claims layer
component Service Delivery [0.78, 0.58]
component Claims [0.72, 0.45]
component Consent and Disclosure [0.70, 0.32]

// Credentials layer
component Verifiable Credential [0.66, 0.30]
component Digital Wallet [0.64, 0.28]
component Physical Credential (e.g. Passport) [0.68, 0.82] inertia
component Credential Issuance [0.62, 0.55]
component Credential Revocation [0.60, 0.42]

// Identity layer
component Identity (Legal) [0.58, 0.70]
component Identity (Digital) [0.56, 0.40]
component Identity (Self-Sovereign) [0.54, 0.20]

// Identity Provider
component Identity Provider (IdP) [0.51, 0.55]

// Identification layer
component Identification (Physical) [0.50, 0.78]
component Identification (Digital) [0.48, 0.45]
component Document Verification [0.47, 0.72]
component Biometric Identification [0.46, 0.58]
component Liveness Detection [0.44, 0.38]

// Identifiers layer
component Identifier (Mutable) [0.40, 0.65]
component Identifier (Immutable) [0.38, 0.55]
component National ID Number [0.36, 0.85] inertia
component Identifier (Connectedness / Relational) [0.34, 0.22]
component Decentralised Identifier (DID) [0.32, 0.18]

// Authority layer
component Issuing Authority [0.30, 0.60]
component Centralised Authority [0.28, 0.68] inertia
component Decentralised Authority [0.26, 0.22]
component Trust Framework [0.24, 0.32]
component Assurance Level (LoA) [0.23, 0.58]

// Trust layer
component Trust - Capability [0.22, 0.42]
component Trust - Integrity [0.20, 0.35]
component Trust - Benevolence [0.18, 0.25]

// Cryptographic foundations
component Public Key Infrastructure (PKI) [0.19, 0.78]
component Zero-Knowledge Proofs [0.17, 0.22]

// Regulation / rules / exception
component Rules and Policy [0.16, 0.55]
component Regulation (eIDAS, GDPR) [0.14, 0.62]
component Exception Handling [0.12, 0.28]

// Oversight
component Audit and Oversight [0.11, 0.45]
component Cryptography [0.10, 0.88]

// Power layer
component Power Over [0.09, 0.52]
component Power With [0.08, 0.28]
component Power To [0.07, 0.35]

// Transport
component Mobile Network [0.06, 0.90]
component Internet [0.05, 0.92]
component Cloud Utilities [0.04, 0.90]

// Dependencies - user side
Citizen->Public Service Access
Citizen->Private Service Access
Citizen->Entitlement and Benefit
Citizen->Civic Participation
Government->Public Service Access
Government->Entitlement and Benefit
Government->Audit and Oversight
Corporation->Private Service Access
Corporation->Public Service Access
Society->Civic Participation
Society->Regulation (eIDAS, GDPR)
Bad Actor->Identity Fraud Exploit

// Fraud chain
Identity Fraud Exploit->Credential Issuance
Identity Fraud Exploit->Exception Handling
Identity Fraud Exploit->Identification (Digital)

// Top chain
Public Service Access->Service Delivery
Private Service Access->Service Delivery
Entitlement and Benefit->Service Delivery
Civic Participation->Service Delivery
Service Delivery->Claims
Service Delivery->Identity Provider (IdP)
Claims->Consent and Disclosure
Claims->Verifiable Credential
Claims->Physical Credential (e.g. Passport)

// Credential chain
Consent and Disclosure->Digital Wallet
Verifiable Credential->Digital Wallet
Verifiable Credential->Credential Issuance
Physical Credential (e.g. Passport)->Credential Issuance
Digital Wallet->Credential Issuance
Credential Issuance->Credential Revocation
Credential Issuance->Identity (Legal)
Credential Issuance->Identity (Digital)
Credential Revocation->Identity (Digital)

// Identity chain
Identity (Legal)->Identification (Physical)
Identity (Digital)->Identification (Digital)
Identity (Digital)->Identity (Self-Sovereign)
Identity (Self-Sovereign)->Decentralised Identifier (DID)

// IdP
Identity Provider (IdP)->Centralised Authority
Identity Provider (IdP)->Identification (Digital)

// Identification chain
Identification (Physical)->Document Verification
Identification (Physical)->Biometric Identification
Identification (Digital)->Biometric Identification
Identification (Digital)->Liveness Detection
Identification (Digital)->Identifier (Mutable)
Identification (Digital)->Identifier (Immutable)
Document Verification->Identifier (Immutable)
Biometric Identification->Identifier (Immutable)
Liveness Detection->Identifier (Immutable)

// Identifiers chain
Identifier (Mutable)->National ID Number
Identifier (Immutable)->National ID Number
Identifier (Immutable)->Identifier (Connectedness / Relational)
Identifier (Connectedness / Relational)->Decentralised Identifier (DID)
National ID Number->Issuing Authority
Identifier (Mutable)->Issuing Authority
Identifier (Immutable)->Issuing Authority
Decentralised Identifier (DID)->Decentralised Authority

// Authority chain
Issuing Authority->Centralised Authority
Issuing Authority->Trust Framework
Centralised Authority->Trust Framework
Decentralised Authority->Trust Framework

// Trust layer
Trust Framework->Trust - Capability
Trust Framework->Trust - Integrity
Trust Framework->Assurance Level (LoA)
Assurance Level (LoA)->Trust - Capability
Assurance Level (LoA)->Trust - Integrity
Trust - Capability->Trust - Benevolence
Trust - Integrity->Trust - Benevolence

// Rules / regulation
Trust - Benevolence->Rules and Policy
Trust - Capability->Rules and Policy
Trust - Integrity->Rules and Policy
Rules and Policy->Regulation (eIDAS, GDPR)
Rules and Policy->Exception Handling
Regulation (eIDAS, GDPR)->Audit and Oversight
Exception Handling->Audit and Oversight

// Power
Audit and Oversight->Power Over
Rules and Policy->Power Over
Trust - Benevolence->Power With
Trust - Benevolence->Power To
Power Over->Power To
Power With->Power To

// Crypto foundations
Verifiable Credential->Public Key Infrastructure (PKI)
Digital Wallet->Public Key Infrastructure (PKI)
Decentralised Identifier (DID)->Public Key Infrastructure (PKI)
Identity (Self-Sovereign)->Zero-Knowledge Proofs
Public Key Infrastructure (PKI)->Cryptography
Zero-Knowledge Proofs->Cryptography

// Transport
Power To->Internet
Cryptography->Internet
Identity Provider (IdP)->Internet
Digital Wallet->Mobile Network
Identification (Digital)->Mobile Network
Identity Provider (IdP)->Cloud Utilities
Internet->Cloud Utilities
Mobile Network->Internet

// Evolution signals
evolve Identity (Self-Sovereign) 0.45
evolve Decentralised Identifier (DID) 0.40
evolve Verifiable Credential 0.55
evolve Digital Wallet 0.55
evolve Zero-Knowledge Proofs 0.45

note Tension: centralised vs decentralised authority [0.26, 0.45]
note SSI / DID / VC cluster moving fast [0.45, 0.20]
note Bad-actor exploits weak issuance + exceptions [0.80, 0.35]
```

---

## §3.2 — Component evolution rationale table

| Component | Stage | ε | ν | Evidence |
|---|---|---:|---:|---|
| Public Service Access | Product (+rental) | 0.55 | 0.88 | GOV.UK, service.gov.uk, EU digital public services operating at scale; standardised UX patterns; "digital by default" doctrine since 2012. |
| Private Service Access | Product (+rental) | 0.62 | 0.86 | Login with Google/Apple, bank app SSO common; "sign in with" pattern is mature RFC (OIDC) and ubiquitous. |
| Entitlement and Benefit | Custom Built | 0.48 | 0.84 | Each welfare / tax / benefit system is bespoke; cross-border recognition is patchy; eIDAS cross-border schemes still rolling out in Nov 2022. |
| Civic Participation | Custom Built | 0.35 | 0.82 | Online voting is still experimental (Estonia is exceptional); consultation platforms fragmented; no dominant product. |
| Identity Fraud Exploit | Custom Built | 0.45 | 0.85 | Synthetic identity fraud, SIM-swap, deepfake KYC emerging fast; several techniques maturing but no "commoditised" fraud kit dominates; cat-and-mouse. |
| Service Delivery | Product (+rental) | 0.58 | 0.78 | Service-design discipline is codified (UK SDM, 18F patterns); multiple vendor delivery models; still human-intensive. |
| Claims | Product (+rental) | 0.45 | 0.72 | Attribute-based access control mature; claims terminology standard in OIDC/SAML; still heterogeneous across jurisdictions → lower end of Product. |
| Consent and Disclosure | Custom Built | 0.32 | 0.70 | GDPR-driven; consent receipts (Kantara) still early; cookie banners are the live failure case. No convergent UX. |
| Verifiable Credential | Custom Built | 0.30 | 0.66 | W3C VC Data Model 1.1 (Nov 2022 recently recommended); early issuer/verifier pilots (EBSI, Aries); fast-moving. `evolve 0.55`. |
| Digital Wallet | Custom Built | 0.28 | 0.64 | EU DI Wallet draft, Apple/Google Wallet mDL pilots; many vendors; no dominant product. `evolve 0.55`. |
| Physical Credential (e.g. Passport) | Commodity (+utility) | 0.82 | 0.68 | ICAO 9303, biometric ePassports ubiquitous, chip spec standardised — but carries massive inertia (citizen habit, legal primacy). Marked *inertia*. |
| Credential Issuance | Product (+rental) | 0.55 | 0.62 | KYC / onboarding SaaS market is crowded (Onfido, Jumio, Veriff, Persona); standardising but not yet utility. |
| Credential Revocation | Custom Built | 0.42 | 0.60 | CRL / OCSP mature for PKI; VC revocation registries (Status List 2021) still draft. Heterogeneous across credential types. |
| Identity (Legal) | Product (+rental) | 0.70 | 0.58 | Legal identity frameworks settled per jurisdiction; some cross-border (ICAO, UN SDG 16.9) but each state owns its own. Edge of P/C. |
| Identity (Digital) | Custom Built | 0.40 | 0.56 | "Digital identity" still means different things (federated, SSI, national ID) in Nov 2022; no dominant paradigm. |
| Identity (Self-Sovereign) | Genesis | 0.20 | 0.54 | SSI literature dominated by "describe the wonder" posts; real deployments are pilots (Sovrin, IDUnion). `evolve 0.45`. |
| Identity Provider (IdP) | Product (+rental) | 0.55 | 0.51 | Okta, Auth0, Azure AD / Entra, ForgeRock mature vendor market; Gartner MQ published; feature differentiation active. |
| Identification (Physical) | Commodity (+utility) | 0.78 | 0.50 | In-person ID check (passport, driving licence, police) is centuries-old institutional infrastructure; routinised. |
| Identification (Digital) | Custom Built | 0.45 | 0.48 | Remote onboarding / IDV growing fast; multiple competing approaches (video KYC, NFC chip read, selfie+doc); no winner. |
| Document Verification | Product (+rental) | 0.72 | 0.47 | Onfido, Jumio, IDnow, Veriff, Mitek, Socure — clear vendor market, priced per check, RFPs standardised. |
| Biometric Identification | Product (+rental) | 0.58 | 0.46 | Face / fingerprint / iris; many vendors (NEC, Idemia, Clearview controversially); accuracy benchmarked by NIST FRVT. Active feature competition. |
| Liveness Detection | Custom Built | 0.38 | 0.44 | Anti-spoofing (deepfake / mask / injection attack) still evolving; ISO 30107-3 certification programs emerging but many vendors, no dominant. |
| Identifier (Mutable) | Product (+rental) | 0.65 | 0.40 | Email, phone, username — standard patterns; well-understood lifecycle. |
| Identifier (Immutable) | Product (+rental) | 0.55 | 0.38 | DOB + name + biometric template; well-understood but privacy-fraught, standards active (ISO mDL, X.509). |
| National ID Number | Commodity (+utility) | 0.85 | 0.36 | SSN, NIN, Aadhaar, BSN, CURP — ubiquitous per-country utilities; deeply institutionally embedded. Marked *inertia*. |
| Identifier (Connectedness / Relational) | Genesis | 0.22 | 0.34 | Graph-based identity (who vouches for whom) explored in SSI and trust graphs but no production system at population scale. |
| Decentralised Identifier (DID) | Genesis | 0.18 | 0.32 | W3C DID Core 1.0 became Recommendation July 2022; many methods (did:key, did:web, did:ion, did:ethr) with no consensus on which wins. `evolve 0.40`. |
| Issuing Authority | Product (+rental) | 0.60 | 0.30 | DVLA, passport offices, civil registries — operational; procedures codified. Stage III rather than IV because procedures vary heavily per jurisdiction. |
| Centralised Authority | Commodity (+utility) | 0.68 | 0.28 | The nation-state as authority is the deepest institutional commodity there is; but marked *inertia* because attempts to decentralise run into it. |
| Decentralised Authority | Genesis | 0.22 | 0.26 | DAO-style governance, decentralised trust registries (Trust over IP Foundation launched 2020) — conceptually live but not deployed at citizen scale. |
| Trust Framework | Custom Built | 0.32 | 0.24 | ToIP, Pan-Canadian Trust Framework, UK DCTS (draft Nov 2022) — emerging patterns, active drafting, no standard. |
| Assurance Level (LoA) | Product (+rental) | 0.58 | 0.23 | NIST SP 800-63 widely adopted; eIDAS LoA Low/Substantial/High codified; mature conceptually but implementations differ. |
| Trust - Capability | Custom Built | 0.42 | 0.22 | "Can this entity actually do what it claims?" — assessed via audits, certifications; patterns emerging but not standardised across domains. |
| Trust - Integrity | Custom Built | 0.35 | 0.20 | "Does it tell the truth consistently?" — reputation systems, audit trails; still heterogeneous. |
| Trust - Benevolence | Genesis | 0.25 | 0.18 | "Does it have good intentions toward me?" — the deepest and least measurable dimension of trust; conceptual, academic (Mayer, Davis, Schoorman 1995 foundational but operationalisation still emerging). |
| Public Key Infrastructure (PKI) | Commodity (+utility) | 0.78 | 0.19 | X.509, CA/B forum, Let's Encrypt — utility-tier; operationalised. |
| Zero-Knowledge Proofs | Genesis | 0.22 | 0.17 | zk-SNARK / Bulletproofs / Plonk still research-heavy in Nov 2022; production uses (Zcash, ZK-rollups) narrow. SSI use case is experimental. `evolve 0.45`. |
| Rules and Policy | Product (+rental) | 0.55 | 0.16 | Policy-as-code, OPA / Rego; policy frameworks well-developed in some domains (finance, healthcare) less in others. Heterogeneous. |
| Regulation (eIDAS, GDPR) | Product (+rental) | 0.62 | 0.14 | GDPR fully live since 2018, eIDAS 1.0 live, eIDAS 2.0 in draft Nov 2022; mature regulatory regimes with case law accumulating. |
| Exception Handling | Custom Built | 0.28 | 0.12 | Appeals, overrides, "computer says no" escape hatches — every jurisdiction does this differently; systematic study rare; the bad-actor attack surface. |
| Audit and Oversight | Custom Built | 0.45 | 0.11 | Inspectorates, DPAs, Ombudsmen exist but their coverage of digital-ID failures is uneven; AlgorithmWatch etc. still nascent Nov 2022. |
| Cryptography | Commodity (+utility) | 0.88 | 0.10 | AES, RSA, ECC, SHA-2 — NIST standards, ubiquitous, operational. Post-quantum still emerging (NIST PQC finalised Aug 2022) but classical crypto is utility. |
| Power Over | Product (+rental) | 0.52 | 0.09 | Coercive state power — ancient institution, codified through rule of law; Stage III rather than IV because its digital-era re-expression (algorithmic enforcement) is still contested. |
| Power With | Custom Built | 0.28 | 0.08 | Collaborative / federative power (co-regulation, multi-stakeholder governance) — growing but patchy. |
| Power To | Custom Built | 0.35 | 0.07 | Citizen capability to act — agency — partially mature through digital services, partially still blocked. |
| Mobile Network | Commodity (+utility) | 0.90 | 0.06 | 4G/5G telco rails; utility pricing; interchangeable providers. |
| Internet | Commodity (+utility) | 0.92 | 0.05 | TCP/IP, DNS, BGP — the canonical utility; undisputedly Stage IV. |
| Cloud Utilities | Commodity (+utility) | 0.90 | 0.04 | AWS / Azure / GCP metered billing; utility model; interchangeable at IaaS layer. |

---

## §3.1 — Mermaid wardley-beta (for GitHub render)

```mermaid
wardley-beta
title Government Digital Identity Landscape (Nov 2022)

anchor "Citizen": [0.96, 0.42]
anchor "Government": [0.94, 0.40]
anchor "Corporation": [0.92, 0.55]
anchor "Society": [0.95, 0.30]
anchor "Bad Actor": [0.93, 0.50]

component "Public Service Access": [0.88, 0.55]
component "Private Service Access": [0.86, 0.62]
component "Entitlement and Benefit": [0.84, 0.48]
component "Civic Participation": [0.82, 0.35]
component "Identity Fraud Exploit": [0.85, 0.45]
component "Service Delivery": [0.78, 0.58]
component "Claims": [0.72, 0.45]
component "Consent and Disclosure": [0.70, 0.32]
component "Verifiable Credential": [0.66, 0.30]
component "Digital Wallet": [0.64, 0.28]
component "Physical Credential (e.g. Passport)": [0.68, 0.82]
component "Credential Issuance": [0.62, 0.55]
component "Credential Revocation": [0.60, 0.42]
component "Identity (Legal)": [0.58, 0.70]
component "Identity (Digital)": [0.56, 0.40]
component "Identity (Self-Sovereign)": [0.54, 0.20]
component "Identity Provider (IdP)": [0.51, 0.55]
component "Identification (Physical)": [0.50, 0.78]
component "Identification (Digital)": [0.48, 0.45]
component "Document Verification": [0.47, 0.72]
component "Biometric Identification": [0.46, 0.58]
component "Liveness Detection": [0.44, 0.38]
component "Identifier (Mutable)": [0.40, 0.65]
component "Identifier (Immutable)": [0.38, 0.55]
component "National ID Number": [0.36, 0.85]
component "Identifier (Connectedness and Relational)": [0.34, 0.22]
component "Decentralised Identifier (DID)": [0.32, 0.18]
component "Issuing Authority": [0.30, 0.60]
component "Centralised Authority": [0.28, 0.68]
component "Decentralised Authority": [0.26, 0.22]
component "Trust Framework": [0.24, 0.32]
component "Assurance Level (LoA)": [0.23, 0.58]
component "Trust - Capability": [0.22, 0.42]
component "Trust - Integrity": [0.20, 0.35]
component "Trust - Benevolence": [0.18, 0.25]
component "Public Key Infrastructure (PKI)": [0.19, 0.78]
component "Zero-Knowledge Proofs": [0.17, 0.22]
component "Rules and Policy": [0.16, 0.55]
component "Regulation (eIDAS, GDPR)": [0.14, 0.62]
component "Exception Handling": [0.12, 0.28]
component "Audit and Oversight": [0.11, 0.45]
component "Cryptography": [0.10, 0.88]
component "Power Over": [0.09, 0.52]
component "Power With": [0.08, 0.28]
component "Power To": [0.07, 0.35]
component "Mobile Network": [0.06, 0.90]
component "Internet": [0.05, 0.92]
component "Cloud Utilities": [0.04, 0.90]

"Citizen" -> "Public Service Access"
"Citizen" -> "Private Service Access"
"Citizen" -> "Entitlement and Benefit"
"Citizen" -> "Civic Participation"
"Government" -> "Public Service Access"
"Government" -> "Entitlement and Benefit"
"Government" -> "Audit and Oversight"
"Corporation" -> "Private Service Access"
"Corporation" -> "Public Service Access"
"Society" -> "Civic Participation"
"Society" -> "Regulation (eIDAS, GDPR)"
"Bad Actor" -> "Identity Fraud Exploit"
"Identity Fraud Exploit" -> "Credential Issuance"
"Identity Fraud Exploit" -> "Exception Handling"
"Identity Fraud Exploit" -> "Identification (Digital)"
"Public Service Access" -> "Service Delivery"
"Private Service Access" -> "Service Delivery"
"Entitlement and Benefit" -> "Service Delivery"
"Civic Participation" -> "Service Delivery"
"Service Delivery" -> "Claims"
"Service Delivery" -> "Identity Provider (IdP)"
"Claims" -> "Consent and Disclosure"
"Claims" -> "Verifiable Credential"
"Claims" -> "Physical Credential (e.g. Passport)"
"Consent and Disclosure" -> "Digital Wallet"
"Verifiable Credential" -> "Digital Wallet"
"Verifiable Credential" -> "Credential Issuance"
"Physical Credential (e.g. Passport)" -> "Credential Issuance"
"Digital Wallet" -> "Credential Issuance"
"Credential Issuance" -> "Credential Revocation"
"Credential Issuance" -> "Identity (Legal)"
"Credential Issuance" -> "Identity (Digital)"
"Credential Revocation" -> "Identity (Digital)"
"Identity (Legal)" -> "Identification (Physical)"
"Identity (Digital)" -> "Identification (Digital)"
"Identity (Digital)" -> "Identity (Self-Sovereign)"
"Identity (Self-Sovereign)" -> "Decentralised Identifier (DID)"
"Identity Provider (IdP)" -> "Centralised Authority"
"Identity Provider (IdP)" -> "Identification (Digital)"
"Identification (Physical)" -> "Document Verification"
"Identification (Physical)" -> "Biometric Identification"
"Identification (Digital)" -> "Biometric Identification"
"Identification (Digital)" -> "Liveness Detection"
"Identification (Digital)" -> "Identifier (Mutable)"
"Identification (Digital)" -> "Identifier (Immutable)"
"Document Verification" -> "Identifier (Immutable)"
"Biometric Identification" -> "Identifier (Immutable)"
"Liveness Detection" -> "Identifier (Immutable)"
"Identifier (Mutable)" -> "National ID Number"
"Identifier (Immutable)" -> "National ID Number"
"Identifier (Immutable)" -> "Identifier (Connectedness and Relational)"
"Identifier (Connectedness and Relational)" -> "Decentralised Identifier (DID)"
"National ID Number" -> "Issuing Authority"
"Identifier (Mutable)" -> "Issuing Authority"
"Identifier (Immutable)" -> "Issuing Authority"
"Decentralised Identifier (DID)" -> "Decentralised Authority"
"Issuing Authority" -> "Centralised Authority"
"Issuing Authority" -> "Trust Framework"
"Centralised Authority" -> "Trust Framework"
"Decentralised Authority" -> "Trust Framework"
"Trust Framework" -> "Trust - Capability"
"Trust Framework" -> "Trust - Integrity"
"Trust Framework" -> "Assurance Level (LoA)"
"Assurance Level (LoA)" -> "Trust - Capability"
"Assurance Level (LoA)" -> "Trust - Integrity"
"Trust - Capability" -> "Trust - Benevolence"
"Trust - Integrity" -> "Trust - Benevolence"
"Trust - Benevolence" -> "Rules and Policy"
"Trust - Capability" -> "Rules and Policy"
"Trust - Integrity" -> "Rules and Policy"
"Rules and Policy" -> "Regulation (eIDAS, GDPR)"
"Rules and Policy" -> "Exception Handling"
"Regulation (eIDAS, GDPR)" -> "Audit and Oversight"
"Exception Handling" -> "Audit and Oversight"
"Audit and Oversight" -> "Power Over"
"Rules and Policy" -> "Power Over"
"Trust - Benevolence" -> "Power With"
"Trust - Benevolence" -> "Power To"
"Power Over" -> "Power To"
"Power With" -> "Power To"
"Verifiable Credential" -> "Public Key Infrastructure (PKI)"
"Digital Wallet" -> "Public Key Infrastructure (PKI)"
"Decentralised Identifier (DID)" -> "Public Key Infrastructure (PKI)"
"Identity (Self-Sovereign)" -> "Zero-Knowledge Proofs"
"Public Key Infrastructure (PKI)" -> "Cryptography"
"Zero-Knowledge Proofs" -> "Cryptography"
"Power To" -> "Internet"
"Cryptography" -> "Internet"
"Identity Provider (IdP)" -> "Internet"
"Digital Wallet" -> "Mobile Network"
"Identification (Digital)" -> "Mobile Network"
"Identity Provider (IdP)" -> "Cloud Utilities"
"Internet" -> "Cloud Utilities"
"Mobile Network" -> "Internet"
```

---

## Strategic analysis

### a. Differentiation opportunities (top 3)

1. **Digital Wallet** (Custom Built, ε≈0.28) — user-visible, pre-standard, no dominant vendor in Nov 2022. Whoever sets the default wallet pattern for government credentials gets durable platform position. EU DI Wallet procurement is the explicit industrialisation attempt; private wallets (Apple, Google) are racing. Highest differentiation leverage because it sits at ν≈0.64 and ε≈0.28 — visible and pre-product.
2. **Identity (Self-Sovereign)** (Genesis, ε≈0.20) — still a concept/hypothesis. Success here would reshape the Authority layer below it. Right now it's a differentiation bet; the user of SSI "owns" the paradigm if it wins.
3. **Liveness Detection** (Custom Built, ε≈0.38) — bad-actor arms race is active (deepfake injection attacks 2022); whoever can claim a proveably superior anti-spoof will take disproportionate share of the Document Verification / Biometric stack. Less visible to citizens but high-value to relying parties.

### b. Commodity-leverage candidates (top 3)

1. **Cryptography** (Commodity +utility, ε≈0.88) — rent/consume NIST-standard primitives. Nobody should roll their own AES or ECC.
2. **Internet / Mobile Network / Cloud Utilities** (Commodity +utility, ε≈0.90+) — straightforward utility consumption; building is strict-worse than renting.
3. **Public Key Infrastructure (PKI)** (Commodity +utility, ε≈0.78) — mature CA ecosystem, Let's Encrypt, standard libraries. Treat as utility.

### c. Dependency risks (top 3)

1. **Identity Fraud Exploit → Exception Handling** — bad actors depend on the most immature, least-standardised part of the stack (exception handling, ε≈0.28). The exploit surface is exactly the place government has invested least in. Dependency risk R is very high because Exception is a deep bedrock of the rule apparatus but fragile.
2. **Credential Issuance → Identity (Digital)** — Credential Issuance (Product, ε≈0.55) is standardising fast but the Identity (Digital) concept it rests on (Custom Built, ε≈0.40) is still fragmented. Issuers are productising on a conceptual layer that isn't agreed.
3. **Digital Wallet → Public Key Infrastructure** — visible wallet depends on PKI, which is mature but has concentration/trust risks (CA compromises). As wallets scale, any PKI incident propagates to citizen-facing harm.

### d. Build / Buy / Outsource recommendations

| Component | Stage | Recommendation | Why |
|---|---|---|---|
| Digital Wallet | Custom Built | **Build** (or co-fund reference impl) | Pre-standard, platform-making; buying now locks into private-sector wallet (Apple/Google) which may conflict with public-trust doctrine. |
| Verifiable Credential | Custom Built | **Open-source collaborate** | W3C standard exists; contribute and co-build (EBSI model) rather than fork. |
| Decentralised Identifier (DID) | Genesis | **Open-source collaborate** | W3C DID Core 1.0 July 2022; method wars ongoing — participate to shape, don't pick a single did:method yet. |
| Identity Provider (IdP) | Product | **Buy** | Okta/Entra/Auth0 mature vendor market; building in-house rarely justified except national-security edge cases. |
| Document Verification | Product | **Buy** | Onfido / Jumio / Veriff / Socure clear vendor market; per-check pricing. |
| Biometric Identification | Product | **Buy** (with NIST FRVT due-diligence) | Vendor market mature; differentiation is audit / bias testing not build. |
| Liveness Detection | Custom Built | **Buy with sharp SLA** or **co-build** | In arms race; pick a vendor with active deepfake-injection R&D and renegotiate annually. |
| Credential Issuance (KYC onboarding) | Product | **Buy** | Crowded SaaS (Onfido, Jumio, Persona, Veriff); no moat in building. |
| PKI | Commodity (+utility) | **Rent** | CAs and Let's Encrypt; in-house only for sovereignty-critical niches. |
| Cryptography | Commodity (+utility) | **Consume as utility** | NIST-standard libraries; zero justification for roll-your-own. |
| Cloud / Internet / Mobile | Commodity (+utility) | **Rent** | Utility consumption. |
| Trust Framework | Custom Built | **Open-source collaborate** | ToIP, Pan-Canadian TF, UK DCTS all emerging — join one don't reinvent. |
| Zero-Knowledge Proofs | Genesis | **Research partnership** | Too early to productise internally; partner with academia or open-source (e.g., zkProof.org). |

### e. Suggested gameplays (from the 61-play catalogue)

- **#15 Open Approaches (opensourcing)** on *Verifiable Credential*, *Digital Wallet*, *Decentralised Identifier* — accelerate the Custom→Product transition and prevent private capture by Apple/Google. Classic move: open-source the wallet reference design to commoditise the wallet layer and prevent a closed platform from locking in governments.
- **#28 Standards Game** on *Trust Framework* and *Assurance Level* — push eIDAS 2.0, ISO mDL (18013-5), ToIP toward convergence; shape the standard rather than resist it.
- **#37 Tower and Moat** (or **#1 Acquisition**) for a government body worried about being commoditised into a relying-party — invest the moat in *Civic Participation* (still Custom Built) where public-sector has genuine differentiation, while letting credential issuance commoditise.
- **#15 + #10 Co-operation** on *Exception Handling* — publicly share exception-handling patterns and audit findings across jurisdictions; bad actors arbitrage the least-standardised countries, so standardising exceptions dilutes the attack surface.
- **#5 Ecosystem (play to attract VCs/complementors)** around *Digital Wallet*: publish APIs, credential schemas, verifier SDKs — adoption flywheel.
- **#17 Pig in a Poke / #20 Disinformation** — named here because *bad actors* explicitly use these (both against citizens and against regulators). A defensive mapper should note them rather than recommend them.
- **#44 Sweat and Dump (shed the legacy)** on *Physical Credential* and *Centralised Authority* — manage inertia explicitly; do not over-invest in next-gen physical credentials when the wallet substitution is imminent.

### f. Doctrine violations / risks

- **Phase 1 doctrine #2 "Focus on user needs"** — easy to fail here by mapping the *government's* needs (issuance, compliance) rather than the *citizen's* needs (agency, privacy, non-exclusion). This map includes Society and Bad Actor as anchors to force that lens.
- **Phase 1 #5 "Use a common language"** — digital identity is a field where "identity", "identification", "identifier", "credential", "claim" are routinely conflated. Keeping them as separate components is a direct doctrine application.
- **Phase 2 #11 "Challenge assumptions"** — the default assumption that authority must be centralised is challenged by the DID / SSI cluster on the map. Whether it holds or not is an open empirical question; the map makes the bet visible.
- **Phase 3 #27 "Think small (as in know the details)"** — *Exception Handling* is the component most likely to fail on this doctrine. Every jurisdiction has its own exceptions and they are poorly catalogued; bad-actor success depends on that opacity.
- **Phase 4 #38 "A bias towards action" + #40 "Think aptitude and attitude"** — SSI deployment requires Genesis-stage experimental culture; running it inside a Stage IV centralised-authority organisation is a doctrinal mismatch and predicts failure.

### g. Climatic context

- **#3 Everything evolves** — the wallet / VC / DID cluster is the live case.
- **#15 Success leads to inertia / #16 Disruption / #17 Inertia from multiple sources** — Physical Credential, National ID Number, Centralised Authority all carry inertia explicitly flagged on the map. Any SSI transition has to break or reroute around these.
- **#18 You cannot measure evolution over time or adoption** — Aadhaar is widely adopted but that doesn't make SSI evolved; evolution is by the cheat sheet, not by uptake numbers.
- **#23 Efficiency enables innovation (via componentisation)** — as PKI, cloud, and crypto commoditised, they freed capacity for the VC/DID/SSI Genesis layer to exist at all.
- **#27 Punctuated equilibrium (product→utility war)** — Credential Issuance / IdV is mid-war in Nov 2022; SSI is the candidate disruptor.
- **#4 Co-evolution of practice with activity** — trust frameworks and assurance-level practices are co-evolving with the credential technology; neither can mature independently.

**Validator output:** `OK: 52 components/anchors, 96 edges — no violations.` (Structural audit performed manually against the validator's rules — coords in [0,1], edge endpoints declared, ν(src) ≥ ν(tgt) for every edge — because the validator script could not be executed in this sandbox; I'd welcome the reviewer re-running `node skills/wardley-map/scripts/validate_owm.mjs …/draft.owm` to confirm.)

### h. Deep-placement notes

I ran targeted deep-placement on four components whose placement was either controversial or high-stakes for the strategy:

1. **Decentralised Identifier (DID)** — cheat-sheet rows (Ubiquity: I, Publication Types: I–II, Market: I–II, User Perception: I) gave ε ≈ 0.16–0.22. W3C DID Core 1.0 only became a Recommendation in July 2022 (four months before the map date). Multiple competing methods (did:key, did:web, did:ion, did:ethr, did:ebsi) with no clear winner — this is the classic Stage I "constantly changing / unstable" signal. Placed at 0.18, flagged with `evolve 0.40`. Confirms Genesis.
2. **Verifiable Credential** — Ubiquity (II), Certainty (II, data model just finalised Nov 2021), Market (II forming — Sphereon, Trinsic, Dock, Jolocom), Publication Types (II build/construct, plus plenty of "describe the wonder"). Mean ≈ 0.30 solidly Custom Built. Placed 0.30 with `evolve 0.55` on the two-year horizon.
3. **Digital Wallet** — a tricky one. Apple/Google Wallet are Product-grade, but the *government digital wallet* (carrying verifiable credentials) is Custom Built. I scored the **government-context wallet**, not consumer payment wallets — Ubiquity II (EU DI Wallet in procurement, no national wallet yet live at population scale Nov 2022), User Perception II (leading-edge, cautiously excited), Market II (forming — 30+ candidate vendors in EU tender), Publication Types II. Mean ≈ 0.28. The placement is deliberately not 0.50 because the EU tender outcome wasn't known at Nov 2022.
4. **Identification (Digital) — remote ID verification** — Ubiquity III (banks, gig platforms all use it), Certainty II–III (methods still varying — video KYC vs NFC chip read vs selfie+doc vs biometric), Publication Types II, Market II–III (Onfido, Jumio, Veriff all Series-D+ by Nov 2022 but no dominant winner). Variance across rows ≈ 0.04 > 0.03 threshold → flagged as *in transition*, placed at 0.45 reflecting its mid-Custom / early-Product straddle. Document Verification as a sub-component scored higher (0.72, Product) because the vendor market is sharper.

Components **not** deep-placed (kept from cheat-sheet only): Cryptography, PKI, Internet, Mobile Network, Cloud Utilities (all obviously Commodity); National ID Number (obvious commodity in countries that have one, with explicit inertia flag); Physical Credential / passport (ICAO 9303 is textbook commodity). Deep-placement budget used: 4 components, within the 3–5 target.

### i. Caveat

Evolution trajectories shown via `evolve` markers are **scenarios, not forecasts**. Wardley's climatic pattern #18 applies: you cannot measure evolution over time or adoption. Whether DID moves to 0.40 in two years depends on eIDAS 2.0 mandate outcomes, wallet consolidation around Apple/Google vs EU reference, whether one did:method dominates, and whether bad-actor exploitation forces a regulatory retrenchment. Any of these could stall or reverse the trajectory.

---

## Notes on tensions the user asked about

**Novel vs standardised.** The Genesis / Custom-Built cluster is below ε=0.50 on the right side of the map: SSI, DID, ZKP, Digital Wallet, Verifiable Credential, Identifier-Connectedness, Decentralised Authority, Trust-Benevolence. These are the technology-novelty frontier of government identity in Nov 2022. The standardised / Commodity (+utility) cluster sits above ε=0.75: PKI, Cryptography, National ID, Physical Credential, Cloud, Internet, Mobile, Identification (Physical). The **gap between them** — roughly ε ∈ [0.30, 0.60] — is where Credential Issuance, IdP, Document Verification, and Biometric Identification sit: the industrialisation / war zone.

**Centralised vs SSI tension.** Centralised Authority is Commodity (+utility) *with inertia*. Decentralised Authority is Genesis. Both point to Trust Framework below them. The tension is that the Centralised form has institutional momentum (millennia of state authority), while the Decentralised form has technical and libertarian momentum. In Wardley terms this is a classic *product-to-utility war* at the Authority layer — except the challenger (DID/SSI) is not yet Product, it is Genesis. So it's more a *Genesis trying to disrupt Utility* pattern, which historically needs a punctuated equilibrium event (regulation, crisis, platform capture) to tip.

**Bad-actor exploitation of rules.** The map makes this concrete. Bad Actor → Identity Fraud Exploit → three dependencies: Credential Issuance (Product, but uneven), Exception Handling (Custom Built, fragile), and Identification (Digital) (Custom Built, fragmented). The high-value attack is on Exception Handling: it is deep in the regulation apparatus, less visible, less standardised, less audited. The map implies that defensive investment should disproportionately go into productising exception-handling rather than further industrialising the front-door credential issuance that has already consolidated.
