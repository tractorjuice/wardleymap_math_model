# Government Digital Identity — Wardley Map (November 2022)

## Scope

A strategic landscape map of government digital identity as of November 2022. The map captures the full socio-technical stack — from the citizens, society, government, corporations, and entities who consume or produce identity assurance, through the value chain of service → claims → credentials → identity → identification → identifiers → authority, the horizontal trust and power layers that modulate it, the regulation/rules/exception apparatus, and the internet transport layer underneath. Bad actors appear as a hostile user whose "need" is the exploitation of the rules and exception apparatus.

## Anchors (Users / Actors)

| Actor | Role |
|-------|------|
| Society | Diffuse user. Needs coherent norms and trust; consumes "power with" through shared frameworks. |
| Citizens | Primary individual user. Needs a usable identity that unlocks services without surrendering control; consumes "power to" through self-sovereign options. |
| Government | Dual role — user of identity assurance and producer of regulation, centralised authority, and issuing authority. Wields "power over". |
| Corporations | Relying parties. Need verifiable claims about counterparties to serve customers and comply with KYC/AML. |
| Entities | Non-human actors (agents, IoT devices, legal entities). Need credentials that bind to non-biometric identifiers. |
| Bad actors | Adversarial user. Their "value chain" is the exception apparatus and the ambiguity between rules and enforcement. |

## Value Chain (top to bottom, visible to hidden)

1. **Service** — the consumable thing (apply for benefits, pay tax, open a bank account, cross a border, log into a corporate SaaS).
2. **Claims** — assertions made by or about a subject (age over 18, resident of country X, holder of qualification Y).
3. **Credentials** — containers that carry claims (paper certificates, PDFs, physical cards, and increasingly W3C Verifiable Credentials).
4. **Identity** — the persistent abstraction the claims and credentials attach to.
5. **Identification (physical and digital)** — the act of resolving a presenter to their identity. Physical (passport inspection, face-to-face) is commodity. Digital (remote onboarding, liveness detection, federated login) is product-stage and still evolving fast.
6. **Identifiers (mutable, immutable, connectedness)** — the data used to do the resolving. Mutable (email, phone, username) are commodity. Immutable (biometrics, DIDs) are mixed — biometrics are product, DIDs custom. Connectedness identifiers (device graph, social graph, behavioural fingerprint) are custom and ethically contested.
7. **Authority (centralised, decentralised, issuing)** — who has the right to issue or assert. Centralised (national ID registry) and issuing (passport office, DMV) are commodity institutions. Decentralised (DID registries, SSI ecosystems) is custom-built and emerging.
8. **Internet** — the transport layer beneath everything. Commodity utility.

Cutting across the chain:

- **Trust layer** (benevolence, capability, integrity) — McKnight-style trust antecedents, currently custom-built conceptual scaffolding in academic and policy circles, productising slowly in trust frameworks.
- **Regulation / rules / exception apparatus** — the governance stack. Regulation (GDPR, eIDAS, REAL ID) is commodity. Specific rules (eIDAS 2.0 wallet requirements, published November 2022 as draft) are custom. The exception apparatus (fraud response, dispute resolution, identity recovery) is custom and uneven.
- **Power (over, with, to)** — Pamela Hinds' power framing as a layer that orients the authority triangle. Power Over aligns with centralised authority; power With aligns with trust frameworks and rules-of-the-game; power To aligns with self-sovereign identity and decentralised authority.

## OnlineWardleyMaps Source

```owm
title Government Digital Identity (November 2022)

anchor Society [0.98, 0.62]
anchor Citizens [0.95, 0.78]
anchor Government [0.97, 0.25]
anchor Corporations [0.95, 0.45]
anchor Entities [0.93, 0.10]
anchor Bad Actors [0.94, 0.92]

component Service [0.88, 0.68]
component Claims [0.80, 0.55]
component Credentials [0.72, 0.50]
component Verifiable Credentials [0.70, 0.22]
component Identity [0.64, 0.40]
component Physical Identification [0.56, 0.88]
component Digital Identification [0.56, 0.58]
component Mutable Identifiers [0.48, 0.78]
component Immutable Identifiers [0.48, 0.50]
component Connectedness Identifiers [0.48, 0.30]
component Centralised Authority [0.34, 0.82]
component Issuing Authority [0.34, 0.70]
component Decentralised Authority [0.34, 0.22]
component Self-Sovereign Identity [0.32, 0.15]
component Benevolence [0.58, 0.20]
component Capability [0.56, 0.42]
component Integrity [0.54, 0.28]
component Trust Framework [0.44, 0.32]
component Regulation [0.22, 0.88]
component Rules [0.22, 0.48]
component Exception Apparatus [0.22, 0.30]
component Power Over [0.40, 0.85]
component Power With [0.40, 0.40]
component Power To [0.40, 0.18]
component Internet [0.06, 0.95]

Society->Service
Citizens->Service
Citizens->Identity
Citizens->Power To
Government->Service
Government->Regulation
Government->Centralised Authority
Government->Power Over
Corporations->Service
Corporations->Claims
Entities->Credentials
Bad Actors->Exception Apparatus
Bad Actors->Rules

Service->Claims
Service->Trust Framework
Service->Internet
Claims->Credentials
Claims->Identity
Credentials->Verifiable Credentials
Credentials->Identity
Verifiable Credentials->Decentralised Authority
Verifiable Credentials->Self-Sovereign Identity
Identity->Physical Identification
Identity->Digital Identification
Physical Identification->Mutable Identifiers
Physical Identification->Immutable Identifiers
Physical Identification->Issuing Authority
Digital Identification->Mutable Identifiers
Digital Identification->Immutable Identifiers
Digital Identification->Connectedness Identifiers
Digital Identification->Internet
Mutable Identifiers->Issuing Authority
Immutable Identifiers->Issuing Authority
Immutable Identifiers->Centralised Authority
Connectedness Identifiers->Decentralised Authority
Centralised Authority->Issuing Authority
Centralised Authority->Regulation
Decentralised Authority->Self-Sovereign Identity
Decentralised Authority->Internet
Issuing Authority->Regulation
Trust Framework->Benevolence
Trust Framework->Capability
Trust Framework->Integrity
Trust Framework->Regulation
Regulation->Rules
Rules->Exception Apparatus
Power Over->Centralised Authority
Power Over->Regulation
Power With->Trust Framework
Power With->Rules
Power To->Self-Sovereign Identity
Power To->Decentralised Authority

evolve Verifiable Credentials 0.55
evolve Self-Sovereign Identity 0.45
evolve Decentralised Authority 0.50
evolve Digital Identification 0.72
evolve Connectedness Identifiers 0.62
evolve Trust Framework 0.58
```

Paste into [OnlineWardleyMaps](https://create.wardleymaps.ai) to render.

## Component Position Table

| Component | Visibility | Evolution | Stage | Notes |
|---|---|---|---|---|
| Service | 0.88 | 0.68 | Product | The visible thing citizens use — well-understood as a concept, many vendors and GOV.UK-style patterns. |
| Claims | 0.80 | 0.55 | Product | OIDC claims, SAML attributes — standardised containers. |
| Credentials | 0.72 | 0.50 | Product (edge) | Paper/PDF/card credentials are commodity; VCs pull the category leftward. |
| Verifiable Credentials | 0.70 | 0.22 → 0.55 | Genesis/Custom, rapidly evolving | W3C VC 1.1 is a rec, but deployments are pilots. EUDI wallet will push hard. |
| Identity | 0.64 | 0.40 | Custom-Built | The abstraction is contested — centralised vs. self-sovereign models differ fundamentally. |
| Physical Identification | 0.56 | 0.88 | Commodity | Passports, driving licences, face-to-face verification. |
| Digital Identification | 0.56 | 0.58 → 0.72 | Product, evolving | Remote onboarding, liveness, NFC chip reads — productised but still tightening. |
| Mutable Identifiers | 0.48 | 0.78 | Commodity | Email, phone number, username. |
| Immutable Identifiers | 0.48 | 0.50 | Product (mixed) | Biometrics product-stage; DIDs custom. |
| Connectedness Identifiers | 0.48 | 0.30 → 0.62 | Custom-Built, evolving fast | Device/social/behavioural graph identifiers — ethically charged, commercially active. |
| Centralised Authority | 0.34 | 0.82 | Commodity | Civil registries, national ID systems — well-understood institutions. |
| Issuing Authority | 0.34 | 0.70 | Product/Commodity | Passport offices, DMVs, universities. |
| Decentralised Authority | 0.34 | 0.22 → 0.50 | Genesis/Custom, evolving | DID methods, verifiable data registries. |
| Self-Sovereign Identity | 0.32 | 0.15 → 0.45 | Genesis, evolving | SSI as a model — pilots (Ontario, BC, EU wallet) pulling it right. |
| Benevolence | 0.58 | 0.20 | Genesis/Custom | Trust construct — not a deployable component, a design target. |
| Capability | 0.56 | 0.42 | Custom-Built | Assurance frameworks (NIST SP 800-63, GPG 45) measure this. |
| Integrity | 0.54 | 0.28 | Custom-Built | Cryptographic integrity is product-level; institutional integrity is custom. |
| Trust Framework | 0.44 | 0.32 → 0.58 | Custom-Built, evolving | eIDAS trust lists, Open ID Federation — formalising. |
| Regulation | 0.22 | 0.88 | Commodity | GDPR, eIDAS, REAL ID, sectoral AML/KYC law. |
| Rules | 0.22 | 0.48 | Custom-Built | Specific scheme rules — eIDAS 2.0 draft, UK Trust Framework beta. |
| Exception Apparatus | 0.22 | 0.30 | Custom-Built | Fraud response, recovery, redress, dispute — uneven across sectors. |
| Power Over | 0.40 | 0.85 | Commodity | Coercive state power is an ancient institution. |
| Power With | 0.40 | 0.40 | Custom-Built | Collaborative, deliberative governance — still being designed. |
| Power To | 0.40 | 0.18 | Genesis/Custom | Agency-granting design — emerging in SSI and consent frameworks. |
| Internet | 0.06 | 0.95 | Commodity | Utility transport. |

## Movement (evolution arrows)

- `Verifiable Credentials 0.22 → 0.55` — EUDI wallet regulation (draft Nov 2022), mDL (ISO 18013-5) now standardised, multiple US state pilots.
- `Self-Sovereign Identity 0.15 → 0.45` — Ontario and BC pilots, Sovrin network, Gaia-X, EUDI's wallet-as-SSI framing.
- `Decentralised Authority 0.22 → 0.50` — W3C DID 1.0 rec (June 2022), emerging DID method registries.
- `Digital Identification 0.58 → 0.72` — remote KYC/onboarding maturing; face matching commoditising.
- `Connectedness Identifiers 0.30 → 0.62` — ad-tech identity graphs and behavioural biometrics rapidly productising.
- `Trust Framework 0.32 → 0.58` — UK DCMS Trust Framework, OpenID Federation, eIDAS trust lists converging into product-stage frameworks.

## Inertia points

| Component | Inertia source | Consequence |
|---|---|---|
| Centralised Authority | Past success of civil registries, sunk cost, institutional identity of the state | Blocks or slows adoption of decentralised alternatives; politically necessary to preserve, not just remove |
| Physical Identification | Legal acceptance networks (who accepts what document) encode decades of investment | Digital alternatives must preserve physical fallbacks for years |
| Regulation | Regulatory cycles are 5-10 years; GDPR is still absorbing the last change | New identity models must fit inside existing rails before rails move |
| Issuing Authority | Organisational identity — a passport office that stops issuing passports ceases to exist | Blocks authority delegation even when technically trivial |

## Tensions (the three the user asked about)

### 1. Centralised authority vs. self-sovereign identity

Centralised Authority (0.34, 0.82) is commodity and politically anchored. Self-Sovereign Identity (0.32, 0.15 → 0.45) is genesis-to-custom and rapidly evolving. They share the same **horizontal band** (around visibility 0.32-0.34) because both are authoritative layers, but they occupy opposite ends of the evolution axis. The EUDI wallet tries to straddle both — an SSI-flavoured wallet whose root of trust is centralised governmental issuance. This is the productive tension, not a contradiction to eliminate.

- **Centralised authority's strategic move**: productise issuance into the wallet format (absorb SSI's UX, keep the root of trust). This is a classic "co-opt" gameplay.
- **SSI's strategic move**: commoditise verifiable credentials fast enough that wallets become an ecosystem rather than a state monopoly. Race to ILC (innovate-leverage-commoditise) before the state captures the standard.

### 2. Bad-actor exploitation of rules

Bad actors anchor at (0.94, 0.92) — highly visible in the threat landscape, their value chain consumes the **Exception Apparatus** (0.22, 0.30) and the **Rules** (0.22, 0.48) rather than the identity stack itself. The strategic insight: bad actors win where rules and exception apparatus are custom-built and uneven. They aren't attacking the commodity regulation — they're arbitraging the gap between commodity regulation and custom exception handling.

- Examples: APP fraud (UK), identity theft via synthetic identity (US), SIM-swap exploiting mutable-identifier recovery, KYC arbitrage across jurisdictions.
- Commoditising the exception apparatus (shared fraud databases, standardised redress) is the primary defence. The UK's Online Safety Bill and EU's DSA (both active in Nov 2022) are early moves in that direction.

### 3. Genesis vs. commodity split across identifier types

A single map layer — Identifiers — spans three evolutionary stages simultaneously:

- Mutable (0.48, 0.78) — commodity
- Immutable (0.48, 0.50) — product (biometrics lead; DIDs lag)
- Connectedness (0.48, 0.30 → 0.62) — custom, evolving fast

This isn't an accident — it's the **"co-evolution of practice and technology"** climatic pattern. Each new identifier type enables new identification patterns, which enable new authority models, which re-shape who has standing to make claims. Strategy-wise: invest in immutable identifier standards (DIDs, mDL) now, because they are the control point that both centralised and decentralised authority will converge on.

## Decision metrics (selected components)

Applying the arc-kit skill's formulas: `D(v) = visibility × (1 - evolution)`, `K(v) = (1 - visibility) × evolution`.

| Component | Vis | Evol | D(v) Differentiation | K(v) Leverage | Verdict |
|---|---|---|---|---|---|
| Service | 0.88 | 0.68 | 0.28 | 0.08 | Moderate — standardise where possible, keep UX/brand differentiated. |
| Verifiable Credentials | 0.70 | 0.22 | **0.55** | 0.07 | Invest — differentiator for any state wanting to lead EUDI adoption. |
| Digital Identification | 0.56 | 0.58 | 0.24 | 0.26 | Buy/configure — commercial platforms mature (Onfido, Yoti, ID.me). |
| Connectedness Identifiers | 0.48 | 0.30 | 0.34 | 0.16 | Evaluate carefully — ethics and regulation gate investment. |
| Centralised Authority | 0.34 | 0.82 | 0.06 | **0.54** | Consume as institutional utility. |
| Internet | 0.06 | 0.95 | 0.00 | **0.89** | Consume as utility. |
| Regulation | 0.22 | 0.88 | 0.03 | **0.69** | Consume as utility — comply with, don't try to build. |
| Trust Framework | 0.44 | 0.32 | **0.30** | 0.18 | Build now — product-stage frameworks emerging, early positioning matters. |

## Dependency risk (selected)

| Dependency | R(a,b) = vis(a) × (1 - evol(b)) | Risk |
|---|---|---|
| Service → Verifiable Credentials | 0.88 × 0.78 = **0.69** | High — visible services depending on genesis-stage tech. Add fallbacks. |
| Service → Internet | 0.88 × 0.05 = 0.04 | Low — utility transport. |
| Digital Identification → Connectedness Identifiers | 0.56 × 0.70 = **0.39** | Moderate — rapidly evolving identifier class, monitor. |
| Identity → Digital Identification | 0.64 × 0.42 = 0.27 | Low-moderate — product-stage. |

## Strategic insights

**Opportunities**

- Productise Verifiable Credentials and Trust Frameworks together — these are co-evolving and the state that gets there first sets the regional standard (EU is moving; UK, Canada, Singapore are contenders).
- Commoditise the exception apparatus — shared fraud intelligence and standardised redress is low-glamour, high-leverage.
- Reframe power as a design choice — explicit "power to" affordances (consent UX, portable identity, right-to-delete) are a product-stage differentiator in EU markets post-GDPR.

**Threats**

- Bad-actor arbitrage of the exception-apparatus / rules gap. Custom-stage exception apparatus is where the most value is lost.
- Centralised authority inertia vs. EU wallet timeline — member states that drag their feet will find EUDI sets the tone.
- Connectedness identifier commoditisation outside of regulation — ad-tech and behavioural biometrics mature faster than governance.

**Doctrine weaknesses (Wardley doctrine applied to this landscape)**

- "Know your users" — six distinct user classes here (incl. bad actors and entities) and most national digital-ID programmes still optimise for one (citizens) or two (citizens + corporates).
- "Use appropriate methods" — applying commodity-style tendering to custom-stage SSI work has produced expensive failures (e.g. some US state pilots).
- "Think fast, inexpensive, restrained, elegant (FIRE)" — EUDI architecture has yet to demonstrate FIRE; watch for inertia in the wallet ecosystem.

## Recommendations

**Immediate (0-6 months)**

- Pick a pilot jurisdiction / cohort to launch an mDL + VC issuance flow. The standards are now stable enough (ISO 18013-5, W3C VC 1.1, DID 1.0).
- Publish a trust-framework scoping document that names benevolence, capability, integrity as explicit design requirements — do not let "trust" stay implicit.
- Instrument the exception apparatus — metrics on time-to-recovery, fraud loss per channel. Measurement precedes commoditisation.

**Short-term (6-18 months)**

- Migrate relying-party integrations from SAML/OIDC-only to a VC-capable posture. The product-stage infrastructure is arriving in 2023-2024 via EUDI.
- Build power-to affordances (consent UX, portable credentials, audit trails) as default product features, not optional settings.
- Establish cross-authority identifier standards — at minimum, an immutable-identifier policy covering both biometrics and DIDs.

**Long-term (18+ months)**

- Position to absorb or co-opt SSI — decide whether to run a national wallet, endorse a private wallet, or federate. Default inaction cedes the commodity wallet layer to big tech.
- Invest in "power with" governance — multi-stakeholder trust frameworks. These are the only governance form resilient to the centralised-vs-decentralised dichotomy.

## Analysis Checklist

- Completeness: anchor set covers all six requested actor classes; core chain is represented end-to-end; trust, regulation, and power layers are present; transport (internet) anchors the bottom.
- Positioning: commodities (internet, regulation, physical ID, centralised authority) are on the right; genesis components (SSI, power to, decentralised authority) are on the left; product components are clustered in the middle.
- Movement: six evolution arrows flag the fastest-moving pieces.
- Insights: three explicit tensions addressed (centralised vs SSI, bad-actor exploitation, identifier split).
- Strategic: gameplay implications (co-opt, ILC, FIRE), climatic patterns (co-evolution, commoditisation, inertia), and doctrine weaknesses called out.
