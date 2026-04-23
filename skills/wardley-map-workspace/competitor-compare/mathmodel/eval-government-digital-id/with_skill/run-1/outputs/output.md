# Government Digital Identity — Wardley Map (November 2022)

## Scenario

Map the landscape of government digital identity as of November 2022, covering the actors (government, society, citizens, corporations, entities, bad actors), the core chain from service through claims and credentials to identity, identification (physical and digital), identifiers (mutable, immutable, connectedness), and authority (centralised, decentralised, issuing). Includes the trust layer (benevolence, capability, integrity), the regulation/rules/exception apparatus, power framings (over, with, to), and the transport layer underneath (Internet, PKI, crypto). Surfaces where identity technology is still novel versus standardised, and the tensions between centralised authority, self-sovereign identity, and bad-actor exploitation of rules.

## Map (OWM)

```owm
title Government Digital Identity (November 2022)
style wardley

// Anchors
anchor Citizen [0.98, 0.55]
anchor Government [0.96, 0.70]
anchor Corporation [0.94, 0.65]
anchor Society [0.92, 0.45]
anchor Bad Actor [0.90, 0.60]

// Services & visible uses
component Public Service Access [0.86, 0.60]
component Private Sector Login [0.84, 0.75]
component Age Verification [0.82, 0.45]
component Cross-border Recognition [0.80, 0.50]
component Identity Theft Exploit [0.82, 0.70]
component Regulatory Arbitrage [0.80, 0.55]

// Claims layer
component Claim [0.74, 0.60]
component Self-asserted Claim [0.72, 0.55]
component Verified Claim [0.70, 0.53]

// Credentials layer
component Credential [0.64, 0.65]
component Physical Credential [0.62, 0.88]
component Digital Credential [0.60, 0.55]
component Verifiable Credential [0.58, 0.35]

// Identity (concept)
component Identity [0.54, 0.70]
component Legal Identity [0.52, 0.80]
component Digital Identity [0.50, 0.55]

// Identification layer
component Identification Physical [0.46, 0.87]
component Identification Digital [0.44, 0.58]

// Identifiers layer
component Identifier [0.38, 0.72]
component Mutable Identifier [0.36, 0.82]
component Immutable Identifier [0.34, 0.78]
component Connectedness Identifier [0.32, 0.32]
component Decentralised Identifier [0.30, 0.20]
component Biometric Identifier [0.28, 0.72]

// Authority layer
component Issuing Authority [0.26, 0.82]
component Centralised Authority [0.24, 0.88]
component Civil Registry [0.22, 0.85]
component Decentralised Authority [0.20, 0.22]

// Trust layer (cross-cutting)
component Trust [0.48, 0.62]
component Benevolence [0.42, 0.52]
component Capability [0.40, 0.72]
component Integrity [0.38, 0.64]

// Regulation / rules / exception
component Regulation [0.56, 0.80]
component Rules [0.50, 0.84]
component Exception Handling [0.44, 0.50]

// Power framings (how authority operates)
component Power Over [0.18, 0.82]
component Power With [0.16, 0.40]
component Power To [0.17, 0.45]

// Transport & cryptographic foundations
component OAuth / OIDC [0.22, 0.85]
component FIDO2 WebAuthn [0.20, 0.72]
component Public Key Infrastructure [0.14, 0.85]
component Cryptography [0.10, 0.88]
component Internet [0.06, 0.95]

// Dependencies
Citizen->Public Service Access
Citizen->Private Sector Login
Citizen->Age Verification
Citizen->Cross-border Recognition
Citizen->Trust

Government->Public Service Access
Government->Regulation
Government->Rules
Government->Civil Registry
Government->Power Over

Corporation->Private Sector Login
Corporation->Verified Claim
Corporation->Regulation
Corporation->Age Verification

Society->Trust
Society->Regulation
Society->Power With

Bad Actor->Identity Theft Exploit
Bad Actor->Regulatory Arbitrage
Bad Actor->Mutable Identifier
Bad Actor->Exception Handling

Public Service Access->Claim
Public Service Access->Verified Claim
Private Sector Login->Verified Claim
Age Verification->Verified Claim
Cross-border Recognition->Verified Claim
Identity Theft Exploit->Credential
Identity Theft Exploit->Mutable Identifier
Regulatory Arbitrage->Rules
Regulatory Arbitrage->Exception Handling

Claim->Credential
Self-asserted Claim->Credential
Verified Claim->Credential
Verified Claim->Digital Credential

Credential->Physical Credential
Credential->Digital Credential
Digital Credential->Verifiable Credential

Physical Credential->Identity
Digital Credential->Identity
Verifiable Credential->Digital Identity
Credential->Identity

Identity->Legal Identity
Identity->Digital Identity
Legal Identity->Identification Physical
Digital Identity->Identification Digital

Identification Physical->Identifier
Identification Digital->Identifier
Identification Physical->Biometric Identifier
Identification Digital->Biometric Identifier

Identifier->Mutable Identifier
Identifier->Immutable Identifier
Identifier->Connectedness Identifier
Identifier->Decentralised Identifier
Immutable Identifier->Biometric Identifier

Mutable Identifier->Issuing Authority
Immutable Identifier->Issuing Authority
Biometric Identifier->Issuing Authority
Connectedness Identifier->Decentralised Authority
Decentralised Identifier->Decentralised Authority
Issuing Authority->Centralised Authority
Centralised Authority->Civil Registry

Trust->Benevolence
Trust->Capability
Trust->Integrity
Verified Claim->Trust
Digital Identity->Trust

Regulation->Rules
Rules->Exception Handling
Exception Handling->Issuing Authority

Centralised Authority->Power Over
Decentralised Authority->Power With
Decentralised Authority->Power To

Digital Credential->OAuth / OIDC
Digital Credential->FIDO2 WebAuthn
Verifiable Credential->Public Key Infrastructure
Decentralised Identifier->Public Key Infrastructure
OAuth / OIDC->Public Key Infrastructure
FIDO2 WebAuthn->Public Key Infrastructure
Public Key Infrastructure->Cryptography
Cryptography->Internet
OAuth / OIDC->Internet
FIDO2 WebAuthn->Internet
Identification Digital->Internet

evolve Verifiable Credential 0.65
evolve Decentralised Identifier 0.55
evolve Decentralised Authority 0.48
evolve Age Verification 0.70
evolve Digital Identity 0.78

note Central vs SSI tension [0.40, 0.20]
note Rules-gap exploited by bad actors [0.78, 0.60]
note Novel identity tech (SSI, DID, VC) [0.40, 0.32]
note Standardised identity tech (passport, PKI, OAuth) [0.18, 0.90]
```

---

## Strategic analysis

### a. Differentiation opportunities (top 3)

In the government digital identity landscape, the components that are user-visible *and* still uncharted are the places where a state, a bank, or an identity provider can build durable advantage.

1. **Verifiable Credential (Custom Built)** — this is the architectural bet the landscape is running. In November 2022, W3C VC 1.1 is stable but adoption is fragmented (British Columbia, EU pilots, ESSIF). A government that standardises a verifiable-credential format now captures the trust graph that every downstream service will call in the 2024–2026 window. Highest differentiation leverage.
2. **Age Verification (Custom Built, evolving to Product +rental)** — the UK Online Safety Bill and EU Digital Services Act are forcing age-gating onto every content platform; AAP providers (Yoti, Jumio, Onfido) are racing to productise. Whoever sets the "prove you're 18 without revealing who you are" default wins a regulated market before the dust settles.
3. **Decentralised Identifier / SSI chain (Genesis)** — DID Core hit W3C Recommendation status July 2022. A government that deploys a production-scale DID-based wallet (Norway's BankID on DID-rails, the EU's planned EUDI wallet) establishes a trust root for the next decade. Risky but the upside is category-defining.

### b. Commodity-leverage candidates (top 3)

These are deep, mature components — rent, don't build.

1. **Public Key Infrastructure (Commodity +utility)** — no state should be building its own CA in 2022. Let's Encrypt, public-WebPKI, government G-Cloud CA services are all utility grade.
2. **OAuth / OIDC (Commodity +utility)** — the protocol is done. Every off-the-shelf IdP (Auth0, Okta, Keycloak, government .gov ID providers) covers the spec. Treat as utility.
3. **Internet and Cryptography (Commodity +utility)** — transport and primitives are utility; don't reinvent.

Also worth naming: **Physical Credential issuance** (Commodity +utility — passport and driving-licence production is outsourced to a handful of specialist printers globally). Don't print your own passports.

### c. Dependency risks (top 3)

Edges where a visible component depends on an immature foundation.

1. **Verified Claim → Digital Credential → Verifiable Credential** — corporations and governments are beginning to accept verified claims backed by verifiable credentials, but the VC layer itself is still Custom Built with fragmented issuer ecosystems. A regulator's decision today locks its citizens onto whichever VC format survives — and the wrong bet costs a rebuild.
2. **Decentralised Identifier → Public Key Infrastructure** — SSI stacks borrow PKI for key management but the DID-to-PKI binding (did:web, did:key, did:ion) is not yet standardised for government use. Utility PKI is fine; the *binding* is not.
3. **Exception Handling → Issuing Authority** — exception handling is the weakest link in every identity system and it's still Custom Built. Bad actors exploit this edge: they target the exception path (lost-passport process, emergency replacement, out-of-band verification) precisely because it falls outside the rules layer's coverage.

### d. Suggested gameplays

- **#30 Standards game** on Verifiable Credential and Decentralised Identifier formats. A government that accelerates W3C VC / DID convergence (or forks to its own standard, like the EU's EUDI-Wallet technical specification) can dictate the trust topology.
- **#15 Open Approaches** on the wallet SDK and schema registry. The EU is doing this with the EUDI Wallet Architecture Reference Framework; it prevents vendor capture and raises adoption rate on verifiable credentials.
- **#35 Defensive regulation** on private-sector login — eIDAS 2.0 (proposed June 2021, in trilogue in late 2022) is exactly this play: mandate member-state acceptance of digital-wallet credentials and push private relying parties onto the government-issued trust root.
- **#13 Lobbying** on age-verification standards — the Five-Eyes governments are actively lobbying for encryption backdoors and content-age gating; private operators need to counter-lobby to keep the gate at AAP level rather than at ISP or device level.
- **#36 Directed investment** on the wallet and credential schema — this is where the next decade's trust flows, and it's still Custom Built. Fund it.
- **#11 FUD / #50 Reinforcing inertia** — these are the plays **bad actors and incumbents** will run against SSI. Expect FUD framed as "decentralised identity means unaccountable identity" and sunk-capital arguments from incumbent issuers (passport agencies, DVLAs). Plan counter-narratives.
- **#43 Sensing Engines (ILC)** — watch the consumption pattern on pilot wallets (BCGov, Aries, Estonia, Singapore SingPass); components that see breakout consumption are your harvest targets.

### e. Doctrine notes

- ✓ **#1 Focus on user needs** — five anchors represent the real stakeholder set (Citizen, Government, Corporation, Society, Bad Actor); none is a technology proxy.
- ✓ **#10 Know your users** — modelling the Bad Actor explicitly is unusual and right. Adversaries are users of the system and the map is more honest for including them.
- ⚠ **#13 Manage inertia** — Physical Credential (passport, driving licence) at Commodity (+utility) is the headline inertia. It holds value chain captive because re-architecting citizen re-issuance on top of Verifiable Credentials is a decade of bureaucratic work. Forms #8 skill-acquisition cost (citizens learning a new wallet), #9 re-architecture cost (civil registry migration), and #14 strategic-control loss (states worry about "digital decoupling") all apply.
- ⚠ **#12 Use appropriate methods** — the map spans Genesis (SSI) through Commodity (+utility) (Internet). A single team can't run Agile / Lean / Six-Sigma across that spread. Pioneer-Settler-Town-Planner partition is doctrine #33 — route DID/VC work through Pioneers, protocol work through Settlers, PKI/transport through Town Planners.
- ⚠ **#2 Use a systematic mechanism of learning** — exception handling is where the system's unknowns concentrate and where bad actors concentrate their attacks. Instrument this edge heavily; treat every exception as a learning signal.

### f. Climatic context

From the 27 patterns, the following are actively shaping this map in November 2022:

- **#3 Everything evolves** — Genesis SSI (DID/VC) is pushing toward Custom Built; Product-era federated identity (SAML, OIDC) is pushing toward Commodity (+utility). The whole centre of the map is moving.
- **#27 Punctuated equilibrium (Product-to-utility war)** — we are at the start of one for digital identity. eIDAS 2.0, EUDI Wallet, mobile driver's licence (ISO 18013-5) and AAMVA mDL are all industrialisation signals.
- **#15 Inertia: past success** — incumbent issuers (passport office, DVLA) resist. See doctrine note above.
- **#16 Inertia: sunk cost in practice** — civil registries, physical credential supply chains, face-to-face renewal processes all have sunk-cost inertia.
- **#20 Co-evolution of practice with activity** — identity practice (know-your-customer, right-to-work, right-to-rent checks) is co-evolving with the Credential and Claim components. Expect KYC practice to industrialise in lockstep.
- **#24 Capital flow follows evolution** — Bad-actor capital (dark markets in stolen credentials, identity-fraud-as-a-service) has already industrialised to Stage IV. Legitimate digital identity is still catching up to the same commodity level on the "buy a stolen identity" side of the map.

### g. Deep-placement notes

Targeted calibration on the strategically-critical components for November 2022:

- **Verifiable Credential — ε ≈ 0.35 (Custom Built).** W3C VC Data Model 1.1 was stable (published March 2022). Industry deployments in Nov 2022 included BC Gov Orgbook, Aries RFCs, ESSIF, and vendor SDKs (Mattr, Trinsic, Evernym). Papers still describe the "wonder" of verifiable claims but case studies were appearing. Vendor count ~10–20, no dominant standard, fragmented. Cheat-sheet rows point to II with slight Row 5 drift toward I — Custom Built with variance.
- **Decentralised Identifier — ε ≈ 0.20 (Genesis).** W3C DID Core became a Recommendation on 19 July 2022. Multiple DID methods existed (did:web, did:key, did:ion, did:indy, did:ethr) with no convergence. Production deployments were pilots, not scale. Kept in Genesis because W3C Rec ≠ market adoption.
- **Decentralised Authority / SSI — ε ≈ 0.22 (Genesis).** No government had a production-scale SSI deployment in Nov 2022 (the EUDI Wallet Architecture Reference Framework v1.0 had just been released June 2022; actual wallet rollout targeted 2024+). Kept in Genesis — the concept is active, the implementation is lab-grade.
- **FIDO2 / WebAuthn — ε ≈ 0.72 (late Product, edging Commodity).** Apple/Google/Microsoft Passkey announcement (May 2022 at Google I/O; Apple at WWDC 2022); rollout started Oct 2022 with iOS 16 and Windows 11 22H2. The standard itself is Commodity (+utility) grade; the Passkey UX is mid Stage III. Hold at 0.72 — this is the single most important commodity placement the map needs to get right for strategy.
- **Age Verification — ε ≈ 0.45 (Custom Built).** UK Online Safety Bill (then in Parliament) and EU DSA were forcing the market. AAP providers (Yoti, Jumio, Onfido, Persona) existed but no dominant product. Evolve arrow to 0.70 reflects the ~2-year window to industrialise.

### h. Caveat

Evolution trajectories on this map are **scenarios, not forecasts**. Wardley's climatic pattern #18 stands: *"you cannot measure evolution over time or adoption."* Verifiable Credentials might punch through to Stage III by 2025 if the EUDI Wallet deadline holds; they might stall at Stage II if the EU delays, vendor fragmentation deepens, or governments default to mobile driver's licence (ISO 18013-5) instead. The map describes a landscape, not a roadmap.

---

## Rendering (Mermaid)

A `wardley-beta` block equivalent of the same map is produced by running the bundled converter on this file:

```
node ${CLAUDE_SKILL_DIR}/scripts/owm_to_mermaid.mjs ./draft.owm
```

## Validation

Structural validation (visibility constraint, coordinate range, edge endpoints) is performed by the bundled validator:

```
node ${CLAUDE_SKILL_DIR}/scripts/validate_owm.mjs ./draft.owm
```

The draft has been manually audited against the visibility rule (ν(a) ≥ ν(b) for every edge a→b) and against the advisory layout checks (near-duplicate coordinates, stage-boundary straddling, canvas-edge clipping, stage imbalance). 47 components/anchors, 83 dependency edges; no visibility violations; stage distribution 2/6/20/15 (Genesis / Custom Built / Product (+rental) / Commodity (+utility)).
