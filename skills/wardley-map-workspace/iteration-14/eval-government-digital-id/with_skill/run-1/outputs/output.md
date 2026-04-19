# Wardley Map — Government Digital Identity (November 2022)

**Scenario.** How a nation-state provides and governs citizen digital ID: authentication, credential issuance, verification, legal frameworks, trust infrastructure, privacy, and service integration (banking, health, tax, welfare). Landscape view — multi-stakeholder (citizens, relying parties, government, standards bodies).

**Why two anchors.** A digital-ID scheme is a two-sided system. If you map only citizens, you miss the banks, tax agencies, health services and welfare offices that are the *relying parties* whose needs co-determine the design. The scheme succeeds only if both sides adopt it — doctrine #10 ("Know your users") mandates the multi-anchor treatment.

---

## Map (OWM)

```owm
title Government Digital Identity (Nov 2022)
style wardley

// Anchors — two user types
anchor Citizen [0.98, 0.55]
anchor Relying Party [0.95, 0.65]

// Service integrations (RP-side adapters — sit just below Relying Party anchor)
component Bank / Financial Onboarding Adapter [0.90, 0.55]
component Tax & Welfare Adapter [0.88, 0.45]
component Health Service Adapter [0.86, 0.40]
component e-Signature Integration [0.84, 0.55]
component Age & Entitlement Verification [0.82, 0.35]

// Citizen-facing
component Digital ID Wallet / App [0.88, 0.40]
component Authentication UX [0.85, 0.55]
component Onboarding / Enrolment [0.83, 0.45]
component Account Recovery [0.78, 0.35]
component Consent & Disclosure [0.80, 0.30]
component Credential Presentation [0.75, 0.35]

// Relying-party-facing APIs
component Verifier API [0.72, 0.55]
component Authentication API (OIDC/SAML) [0.70, 0.75]
component Attribute Exchange API [0.68, 0.50]
component Assurance Level Signalling [0.65, 0.45]

// Identity proofing and credentials
component Identity Proofing (document + selfie) [0.60, 0.55]
component Liveness Detection [0.55, 0.40]
component Biometric Matching [0.52, 0.65]
component Credential Issuance [0.58, 0.45]
component Revocation & Status Registry [0.50, 0.50]

// Trust and interop fabric
component Federation / Trust Broker [0.48, 0.55]
component Trust Framework (policy + scheme) [0.45, 0.35]
component Identity Attribute Schema [0.42, 0.55]
component Cryptographic Standards (FIDO2, mDL, VC) [0.40, 0.35]
component Certificate Authority / PKI [0.35, 0.80]

// Authoritative data
component Authoritative Attribute Sources [0.38, 0.55]
component Civil / Population Register [0.32, 0.70]

// Legal and governance (sit below the things that depend on them)
component Accessibility & Inclusion Policy [0.30, 0.45]
component Data Protection Regime [0.28, 0.65]
component Independent Audit & Redress [0.26, 0.40]
component Primary Legislation [0.22, 0.40]
component Parliamentary / Civil Oversight [0.18, 0.35]

// Deep infrastructure
component Device Secure Hardware [0.20, 0.65]
component Key Management (HSM / Secure Enclave) [0.18, 0.80]
component Public-Key Infrastructure [0.15, 0.85]
component Cloud Hosting & Compute [0.10, 0.92]
component Network / TLS / DNS [0.06, 0.95]

// Knowledge
component Identity Assurance Knowledge [0.14, 0.50]
component Cryptography Research [0.12, 0.55]

// Dependencies — Citizen side
Citizen->Digital ID Wallet / App
Citizen->Authentication UX
Citizen->Onboarding / Enrolment
Citizen->Account Recovery
Citizen->Consent & Disclosure
Citizen->Credential Presentation

// Dependencies — Relying-party side
Relying Party->Bank / Financial Onboarding Adapter
Relying Party->Tax & Welfare Adapter
Relying Party->Health Service Adapter
Relying Party->e-Signature Integration
Relying Party->Age & Entitlement Verification
Relying Party->Verifier API
Relying Party->Authentication API (OIDC/SAML)
Relying Party->Attribute Exchange API
Relying Party->Assurance Level Signalling

// Service integrations to RP-facing APIs
Bank / Financial Onboarding Adapter->Attribute Exchange API
Bank / Financial Onboarding Adapter->Authentication API (OIDC/SAML)
Tax & Welfare Adapter->Authentication API (OIDC/SAML)
Tax & Welfare Adapter->Attribute Exchange API
Health Service Adapter->Authentication API (OIDC/SAML)
Health Service Adapter->Attribute Exchange API
e-Signature Integration->Credential Presentation
e-Signature Integration->Key Management (HSM / Secure Enclave)
Age & Entitlement Verification->Attribute Exchange API

// Citizen-facing to core
Digital ID Wallet / App->Credential Presentation
Digital ID Wallet / App->Authentication UX
Digital ID Wallet / App->Device Secure Hardware
Authentication UX->Authentication API (OIDC/SAML)
Authentication UX->Biometric Matching
Onboarding / Enrolment->Identity Proofing (document + selfie)
Onboarding / Enrolment->Credential Issuance
Account Recovery->Identity Proofing (document + selfie)
Consent & Disclosure->Attribute Exchange API
Credential Presentation->Cryptographic Standards (FIDO2, mDL, VC)
Credential Presentation->Revocation & Status Registry

// Relying-party APIs to core
Verifier API->Federation / Trust Broker
Verifier API->Trust Framework (policy + scheme)
Authentication API (OIDC/SAML)->Federation / Trust Broker
Attribute Exchange API->Federation / Trust Broker
Attribute Exchange API->Authoritative Attribute Sources
Assurance Level Signalling->Trust Framework (policy + scheme)

// Identity proofing chain
Identity Proofing (document + selfie)->Liveness Detection
Identity Proofing (document + selfie)->Biometric Matching
Identity Proofing (document + selfie)->Civil / Population Register
Credential Issuance->Certificate Authority / PKI
Credential Issuance->Key Management (HSM / Secure Enclave)
Credential Issuance->Identity Attribute Schema
Revocation & Status Registry->Public-Key Infrastructure

// Trust fabric to foundations
Trust Framework (policy + scheme)->Primary Legislation
Trust Framework (policy + scheme)->Data Protection Regime
Trust Framework (policy + scheme)->Accessibility & Inclusion Policy
Federation / Trust Broker->Certificate Authority / PKI
Federation / Trust Broker->Cryptographic Standards (FIDO2, mDL, VC)
Certificate Authority / PKI->Public-Key Infrastructure
Cryptographic Standards (FIDO2, mDL, VC)->Cryptography Research
Identity Attribute Schema->Authoritative Attribute Sources

// Authoritative data
Authoritative Attribute Sources->Civil / Population Register
Civil / Population Register->Primary Legislation

// Legal chain
Primary Legislation->Parliamentary / Civil Oversight
Data Protection Regime->Primary Legislation
Data Protection Regime->Independent Audit & Redress
Accessibility & Inclusion Policy->Primary Legislation
Independent Audit & Redress->Parliamentary / Civil Oversight

// Infra
Biometric Matching->Cloud Hosting & Compute
Liveness Detection->Cloud Hosting & Compute
Federation / Trust Broker->Cloud Hosting & Compute
Verifier API->Cloud Hosting & Compute
Authentication API (OIDC/SAML)->Cloud Hosting & Compute
Attribute Exchange API->Cloud Hosting & Compute
Cloud Hosting & Compute->Network / TLS / DNS
Public-Key Infrastructure->Network / TLS / DNS
Key Management (HSM / Secure Enclave)->Public-Key Infrastructure

// Knowledge
Identity Proofing (document + selfie)->Identity Assurance Knowledge
Trust Framework (policy + scheme)->Identity Assurance Knowledge
Cryptographic Standards (FIDO2, mDL, VC)->Identity Assurance Knowledge

// Evolution scenarios
evolve Digital ID Wallet / App 0.60
evolve Credential Presentation 0.55
evolve Cryptographic Standards (FIDO2, mDL, VC) 0.60
evolve Trust Framework (policy + scheme) 0.55
evolve Liveness Detection 0.60
evolve Identity Proofing (document + selfie) 0.72

note Differentiation zone [0.75, 0.30]
note Trust plumbing [0.45, 0.55]
note Utility foundations [0.10, 0.93]
```

---

## Strategic analysis

### a. Differentiation opportunities (top 3)

These are visible, uncharted, and where a government scheme either builds an advantage — or is outbuilt by BigTech wallets.

1. **Digital ID Wallet / App** (Custom Built, edging to Product) — the single most visible surface. In November 2022 the EU was drafting EUDI Wallet specs, the UK was rebuilding after Verify's collapse, and Apple/Google had just announced passkeys + mDL support. The government wallet is where sovereignty and citizen trust are earned or lost. If the state doesn't ship a credible wallet, Apple Wallet and Google Wallet will become the de-facto identity layer and the state becomes a dependent attribute issuer.
2. **Consent & Disclosure** (Custom Built) — selective disclosure ("prove you're over 18 without revealing birthdate") is a genuine Genesis-to-Custom capability in Nov 2022. W3C VCs and ISO 18013-5 mDL both support it but few production systems exercise it. Whoever nails the privacy UX earns durable legitimacy.
3. **Trust Framework (policy + scheme)** (Custom Built) — not a piece of software but a political-technical artefact: who can issue, who can verify, what liability applies, what assurance levels mean. Nations with a coherent trust framework (Estonia, Denmark, Singapore) run circles around nations without one (UK pre-One-Login). Highest long-term leverage, lowest visibility to non-experts.

### b. Commodity-leverage candidates (top 3)

Deep, mature — rent or consume, don't rebuild.

1. **Cloud Hosting & Compute** and **Network / TLS / DNS** (Commodity +utility) — utility infrastructure. A government should buy from cloud providers under appropriate data-residency constraints, not run bespoke data centres.
2. **Public-Key Infrastructure** and **Certificate Authority / PKI** (Commodity +utility, edging to pure utility) — PKI and CA operations are well understood. Use existing CA software stacks, existing HSM vendors, existing PKIX standards. A government's differentiator is not how it runs a CA; it is which policies the CA enforces.
3. **Authentication API (OIDC/SAML)** (Product +rental, late) — OIDC is a 2014-era standard with mature open-source and commercial implementations (Keycloak, Auth0, Okta, ForgeRock). No state should write a SAML library in 2022. Use off-the-shelf federation software and spend engineering budget on the wallet and the trust framework.

### c. Dependency risks (top 3)

Edges where a visible component leans on a fragile, immature, or contested foundation.

1. **Digital ID Wallet / App → Device Secure Hardware** — the wallet's security model depends on phone TEEs / Secure Enclaves whose behaviour, attestation format, and update cadence are set by Apple and Google. A national wallet has zero control over the platform it runs on. Platform vendors can change the rules (e.g., attestation APIs, background execution limits) unilaterally. This is the most fragile load-bearing edge on the map.
2. **Onboarding / Enrolment → Identity Proofing (document + selfie)** — inclusion fails here. Citizens without a passport/driving-licence, or with darker skin tones that biometric matchers perform worse on, are locked out. The Nov-2022 state of face-match accuracy is mid Product — it works for the median user and discriminates at the tails (documented in NIST FRVT 1:1). The visible onboarding step rides on an uneven foundation.
3. **Federation / Trust Broker → Cryptographic Standards (FIDO2, mDL, VC)** — trust broker selects and enforces a standard, but in Nov-2022 the standards landscape is unresolved: ISO 18013-5 mDL (just published Sep 2021), W3C VCs (Custom Built, multiple profiles), OIDC4VC/SIOP (drafts), SD-JWT (new). Choose the wrong standard and you write off tens of millions of pounds in five years. Standards risk is real.

### d. Suggested gameplays

Drawn from the 61-play catalogue.

- **#1 Focus on user needs** — the two-anchor (Citizen + Relying Party) structure operationalises this. In practice: every proposed feature should trace to a citizen use-case or a relying-party integration, not to a ministry KPI.
- **#15 Open Approaches on Cryptographic Standards and Trust Framework** — publish specs, reference implementations, and conformance tests. The EU's EUDI ARF (Architecture and Reference Framework) is an explicit version of this play. Nations that open-source their wallet SDK (cf. IDunion, Aries) accelerate their own ecosystem AND reduce lock-in to any single vendor.
- **#41 Alliances** on **Identity Proofing** and **Cryptographic Standards** — no country has enough internal signal on document fraud or face-spoof attacks. Alliances (eIDAS, ICAO MRTDs, FIDO Alliance) pool adversarial signal. Genuine public-interest alliance, not M&A.
- **#42 Co-creation** on **Consent & Disclosure UX** — the privacy affordance is only trusted if civil society validated it. Run with advocacy groups (AccessNow, EFF, Privacy International) in the design process; their stamp of approval is the moat.
- **#36 Directed investment** on **Digital ID Wallet / App** — this is the top-D component. Concentrate engineering on the wallet and its UX; everything else is plumbing.
- **#56 First mover** on **mDL / EUDI Wallet** conformance — ISO 18013-5 mDL is newly published; EUDI is nascent. A country that ships a compliant wallet in 2023 and pushes it as the reference implementation wins the regional standards game (see also **#30 Standards game**).
- **#29 Harvesting** on **Liveness Detection** and **Biometric Matching** — don't build; watch iProov, Onfido, Jumio, Yoti, IDEMIA emerge, then procure or acquire. Early 2020s has many vendors converging.
- **#37 Experimentation** (FIRE) on **Selective Disclosure UX** — small pilots with SD-JWT / BBS+ before committing nationally.
- **#22 Limitation of competition — to avoid** — on the citizen wallet side, governments are tempted to mandate the state wallet. This breaks #1 (user choice) and invites legitimate opposition. Better to compete on quality and let the wallet be *recognised-but-not-mandatory* (the EUDI model).

### e. Doctrine violations / risks to watch

- Doctrine **#10 Know your users** — satisfied: two anchors (Citizen + Relying Party). A stricter reading would argue for a third: *digitally-excluded citizen* (no smartphone, low-literacy, disability). That is often the population the scheme fails, and folding them into the generic Citizen anchor hides the problem. Flag as a candidate refinement.
- Doctrine **#13 Manage inertia** — governments have enormous inertia in this domain. Sunk capital in legacy identity systems (smart-card schemes, paper registries, bespoke government gateways) and political capital in procurement contracts make wallet programmes notoriously slow. UK Verify (shuttered 2022) is the textbook failure. The map should explicitly list which of the 17 inertia forms apply to the programme (usually #2 sunk capital, #3 political capital, #9 re-architecture cost, #14 strategic-control loss).
- Doctrine **#7 Use appropriate methods** — a common failure mode: applying Stage-IV procurement methodology (fixed-price, multi-year, big-five integrators) to Stage-II components (wallet, proofing). Output: costly programmes that deliver late and badly. Wallet teams should be FIRE (#15), small, in-sourced.
- Doctrine **#22 Use standards where appropriate** — there is a live risk of the opposite: standardising Stage-II components prematurely (picking one VC profile and locking out others) is dangerous in Nov-2022. Standards should be applied to PKI, OIDC, cryptography; held open on VC profiles and wallet protocols.
- Doctrine **#4 Be transparent** — digital ID programmes across the world have conspicuous transparency failures (SPID procurement disputes in Italy, Aadhaar court litigation in India, GOV.UK Verify's undisclosed performance data). Publish failure rates, demographic breakdowns, and audit reports as a default.
- Doctrine **#8 Focus on high situational awareness** — in multiple jurisdictions, the ID programme is owned by a digital agency, the legal basis by a justice ministry, the data protection layer by a separate regulator, and banks by yet another. Without a shared map the stakeholders cannot align. The skill's own output *is* the situational-awareness artefact.

### f. Climatic context

Which of the 27 climatic patterns are actively shaping this landscape in November 2022:

- **#3 Everything evolves** + **#5 No choice over evolution** — identity proofing, biometric matching, and federation are all drifting right. The question is not "will we commoditise" but "who runs the commodity". If governments don't lead, Apple/Google/Microsoft will.
- **#4 Multi-wave evolution** — authentication is *already* on its second wave: passwords (S1 saturating) → 2FA/SMS (chasm) → FIDO2/passkeys (taking off in 2022). National ID schemes built on the old wave have inertia; the new wave is likely disruptive on a 3-5-year horizon.
- **#17 Inertia can kill** — legacy smart-card schemes (Belgium's eID, Germany's nPA historical usage patterns) are deep sunk capital that resist the wallet-first future. Managing inertia is the programme's central task.
- **#22 Two forms of disruption** — both kinds are live here. **Genesis-driven:** self-sovereign identity (SSI) / decentralised identifiers are a Genesis component that *could* disrupt federation entirely, or could fizzle. **Product-to-utility:** federation and authentication are mid-transition from Product to Utility, with the wallet as the industrialising form.
- **#27 Product-to-utility punctuated equilibrium** — the wallet is the punctuation. When (and if) mDL and EUDI wallets reach critical mass, the old federation-broker architecture compresses rapidly. Governments that do not have a wallet at the moment of transition will be absorbed into the BigTech-wallet ecosystem on BigTech's terms.
- **#11 Future value ∝ uncertainty** — selective disclosure, verifiable credentials, and zero-knowledge proofs are Custom Built in Nov-2022. Their future value is high precisely because their present state is uncertain. Portfolio a few pilots.
- **#18 You cannot measure evolution over time or adoption** — do not believe any consultant's PowerPoint that says "100% citizen digital ID adoption by Q4 2026". The `evolve` arrows in the map are scenarios, not forecasts.

### g. Deep-placement notes

No external research was run in this pass — the skill's deep-placement budget (3-5) was not exercised because the scenario is a landscape assessment at a known reference date (Nov 2022) for which the author's priors are stable. If the map were being used for a procurement decision I would run targeted searches on:

- **Biometric Matching** — NIST FRVT 1:1 leaderboards to confirm vendor landscape (Thales, Idemia, NEC, Paravision, Clearview, Mobai) and current demographic-parity numbers. Initial placement ε = 0.65 (Product, feature competition) is likely correct but the demographic-fairness dimension may pull specific sub-components left.
- **Liveness Detection** — iBeta PAD Level 1/2 certifications and ISO/IEC 30107-3 vendor coverage. Placement ε = 0.40 (Custom Built → Product) is consistent with the still-contested passive-vs-active debate; worth confirming with a vendor-count search.
- **Cryptographic Standards (FIDO2, mDL, VC)** — this is bimodal. FIDO2 is Stage III (well into Product). mDL (ISO 18013-5) is Stage II (published Sep 2021, implementations new). W3C VCs are Stage II (specs stable but profiles diverging). The single-point ε = 0.35 is a weighted average; in a high-stakes analysis this component would be split into three.
- **Trust Framework** — cross-country comparison (Estonia RIA, Denmark MitID, Singapore SingPass, Belgium CSAM/itsme, eIDAS 2.0 ARF) would anchor placement. Current ε = 0.35 reflects my reading that the *generic* trust framework is a Custom Built artefact, but specific national schemes vary widely (Estonia is near-Commodity, UK near-Genesis post-Verify).

### h. Caveat

Evolution trajectories (the `evolve` arrows) and the climatic narratives above are **scenarios, not forecasts**. Wardley's climatic pattern #18 stands: *"you cannot measure evolution over time or adoption."* Read the `evolve` targets as "plausible 2-4 year trajectories if current standards efforts consolidate and reasonable engineering investment happens", not as deadlines.

In particular, the BigTech-wallet-vs-state-wallet question is a live strategic contest, not an arithmetic inevitability. Nations that invest in wallet UX and trust governance shape one outcome; nations that defer shape a very different one.

---

## Where digital ID is fragile (direct answer to the scenario question)

Pulling the fragility thread out of the map explicitly:

1. **Inclusion-at-enrolment.** Biometric matching and document-based proofing are the load-bearing step for everyone who isn't already in the civil register. The people most likely to be failed by the scheme — the homeless, recent migrants, the elderly, disabled citizens, anyone without a standard document — are precisely those who most need access to welfare, health, and banking. This is a visible/fragile edge (`Onboarding → Identity Proofing`) and a legitimacy risk for the whole programme.
2. **Platform dependency.** The wallet is a mobile app whose secure hardware, attestation format, and background-execution policy are owned by Apple and Google. The state cannot patch the platform; it can only ask. A single hostile platform change can break a national scheme.
3. **Legal basis drift.** The `Trust Framework → Primary Legislation → Parliamentary Oversight` chain holds only if the enabling legislation is recent, binding, and judicially respected. Where the legal basis predates the scheme (retrofitted to an old ID act, or running on ministerial order) the scheme is one successful court challenge away from collapse. Aadhaar's constitutional cases and the UK ID Cards Act 2006 (repealed 2010) illustrate the range.
4. **Standards-stack gamble.** Building on mDL, VC, OIDC4VCI, or SIOP in Nov-2022 is a bet. The winners of the 2023-2025 standards race aren't settled. A wallet built on a loser requires re-engineering.
5. **Concentration in civil register.** The civil / population register is the single source of truth for "is this person real". A breach, politicisation, or system failure there propagates to every relying party. Regimes have historically weaponised civil registers against minorities (Rwanda 1994, Netherlands WWII); the fragility is not only technical but institutional.
6. **Private-sector substitution.** BigTech wallets (Apple Wallet, Google Wallet, MS Authenticator) are simultaneously allies and competitors. If state wallets lag, the market goes around them and the state becomes a credential issuer into a foreign-owned wallet, conceding the citizen-facing trust surface.
7. **Vendor concentration in biometrics and HSMs.** A small number of vendors (IDEMIA, Thales, NEC for biometrics; Thales, Utimaco, Entrust for HSMs) serve most national programmes. Supply-chain disruption or coordinated pricing hurts governments with thin domestic capability.

---

## Validator output

```
$ python3 ${CLAUDE_SKILL_DIR}/scripts/validate_owm.py draft.owm
OK: 41 components/anchors, 75 edges — no violations.
```

(43 nodes in full: 2 anchors + 41 components; 6 `evolve` targets; 3 `note` markers.)
