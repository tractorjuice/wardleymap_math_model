# Government Digital Identity — Wardley Map (November 2022)

Scenario framing: map the landscape of government digital identity with explicit coverage of actors (government, society, citizens, corporations, entities, bad actors), the service → claims/credentials → identity → identification → identifiers → authority chain, the trust layer (benevolence, capability, integrity), regulation/rules/exception apparatus, power (over, with, to), and the transport layer beneath. Show where identity tech is still novel vs. standardised, and where tensions between centralised authority, self-sovereign identity, and bad-actor rule-exploitation sit.

## 1. Mathematical model summary

Using the canonical tuple $\mathcal{M} = (V, E, U, \nu, \varepsilon, t)$:

- $|U| = 6$ anchors (multi-user: Government, Society, Citizens, Corporations, Entities, Bad Actors — the last is adversarial and mapped intentionally).
- $|V| \approx 34$ components across services, power, trust, regulation, claims/credentials, identity, identification, identifiers, authority, and transport.
- Visibility $\nu$ was seeded by $\nu(v) = 1/(1+d(v))$ from the nearest anchor, then adjusted so that the one hard rule $\nu(a) \ge \nu(b)$ for every edge $(a,b) \in E$ holds.
- Evolution $\varepsilon$ was scored via the 4-row quick cheat sheet (Ubiquity, Certainty, User Perception, Publication Types) averaged to band midpoints.

## 2. Evolution scoring — worked examples (4-row method)

Scoring convention: Stage I=0.125, II=0.375, III=0.625, IV=0.875. Average.

| Component | Ubiquity | Certainty | User Perception | Publications | $\varepsilon$ | Stage |
|---|---|---|---|---|---|---|
| The Internet | IV | IV | IV | IV | 0.875 | Commodity +utility |
| PKI | IV | IV | III | IV | 0.813 | Commodity +utility |
| Cryptographic Primitives | IV | IV | III | IV | 0.813 | Commodity +utility |
| Physical Identification (e.g. passport, driving licence) | IV | IV | III | III | 0.750 | Commodity / Product boundary |
| Centralised Authority | III | IV | III | III | 0.688 | Product +rental |
| Credentials (generic) | III | III | III | III | 0.625 | Product +rental |
| Digital Identification | III | II | III | III | 0.531 | Product +rental |
| Claims | III | III | II | III | 0.531 | Product +rental |
| Verifiable Credentials (W3C VC) | II | II | I | II | 0.281 | Custom Built |
| Decentralised Authority | II | II | I | I | 0.219 | Custom Built / Genesis border |
| Self-Sovereign Identity | I | I | I | I | 0.125 | Genesis |
| Rule Exploitation (by bad actors) | II | I | I | II | 0.250 | Genesis / Custom boundary |

The two-mode landscape is visible: the **transport + traditional-ID substrate is commoditised**, while **SSI / VC / decentralised authority are still Genesis–Custom Built** as of November 2022 (W3C DID Core Rec reached TR in July 2022, VC Data Model 1.1 in March 2022 — broadly "built and constructed" but not in normal-user use). This matches Wardley's "you cannot measure evolution over time" — placement is by cheat-sheet properties, not calendar age.

## 3. OWM output

The machine-readable map is in `draft.owm`. Key shape:

- **Anchors**: six, reflecting the actor list in the scenario. Bad Actors is a legitimate anchor — their "need" is to exploit the rules/exception surface, and modelling them lets us put Rule Exploitation on the map where trust and regulation have to absorb it.
- **Layers, top→bottom**: Services → Power → Trust → Regulation → Claims/Credentials → Identity → Identification → Identifiers → Authority → Transport.
- **Evolve arrows**: VC → 0.55, SSI → 0.40, Decentralised Authority → 0.45, Digital Identification → 0.70 — labelled as scenario not forecast, as required.
- **Inertia**: Physical Identification marked with an inertia flag. The inertia here is *sunk capital* (passport-issuing infrastructure), *political capital* (sovereignty norms around who issues the canonical ID), and *human capital* (border-guard / notary workflows) — per the Inertia doc's 17-form taxonomy these are forms #1, #5, #4 respectively.

## 4. Strategic analysis

### (a) Top 3 by differentiation pressure $D(v) = \nu(v) \cdot (1 - \varepsilon(v))$

| # | Component | $\nu$ | $\varepsilon$ | $D$ | Reading |
|---|---|---|---|---|---|
| 1 | Rule Exploitation | 0.86 | 0.20 | 0.69 | High-visibility adversarial surface that is still novel — an attention zone for defenders, not an advantage. Differentiation pressure from the defender side: design rules + exception handling so novel abuse patterns can be contained. |
| 2 | Power To | 0.80 | 0.30 | 0.56 | Citizen-side empowerment (self-representation, consent, authorisation) is visible to citizens but still conceptually novel in public-service delivery. Real differentiation zone for a government or vendor that can operationalise it. |
| 3 | Power With | 0.80 | 0.35 | 0.52 | Collective / mutual-trust empowerment (federations, credential wallets across domains). Again visible, still novel in practice. |

Honourable mentions: Trust: Benevolence ($D=0.52$), Trust: Integrity ($D=0.44$), Exception Handling ($D=0.43$).

### (b) Top 3 by commodity leverage $K(v) = (1 - \nu(v)) \cdot \varepsilon(v)$

| # | Component | $\nu$ | $\varepsilon$ | $K$ | Reading |
|---|---|---|---|---|---|
| 1 | The Internet | 0.08 | 0.95 | 0.874 | Pure utility — consume, never build. |
| 2 | Cryptographic Primitives | 0.12 | 0.80 | 0.704 | Use vetted libraries / HSM / KMS — never roll your own. |
| 3 | PKI | 0.16 | 0.75 | 0.630 | Use managed PKI / commodity certificate infrastructure. |

Also-rans: Centralised Authority (0.74·0.70 = 0.518), Physical Identification (0.56·0.75 = 0.420 — but its inertia blocks simple "outsource" treatment).

### (c) Top 3 dependency risks $R(a,b) = \nu(a) \cdot (1 - \varepsilon(b))$

| # | Edge $(a, b)$ | $\nu(a)$ | $\varepsilon(b)$ | $R$ | Reading |
|---|---|---|---|---|---|
| 1 | (Power To, Self-Sovereign Identity) | 0.80 | 0.15 | 0.68 | A visible promise (citizen empowerment) resting on a Genesis-stage substrate. If SSI stalls, "Power To" narrative collapses. |
| 2 | (Power With, Decentralised Authority) | 0.80 | 0.20 | 0.64 | Federated / peer-trust models depend on decentralised-authority tooling that is not yet mature. |
| 3 | (Rule Exploitation, Exception Handling) | 0.86 | 0.35 | 0.56 | Bad actors exploit rule-exception pathways; exception handling itself is still Custom Built. The defender's mitigation surface is immature, which is exactly the risk. |

### (d) Suggested gameplays (from the 61-play catalogue)

- **Pioneer–Settler–Town Planner** (organisational doctrine play) on VC / SSI work — keep Pioneers on the SSI/VC research, Settlers productising wallets, Town Planners operating centralised ID rails. Don't mix modes.
- **Open approaches / Open source** on Verifiable Credentials and DID resolvers — standards-track (W3C VC, DID Core) deliberately *accelerated* toward Product stage; picking commercial openness here reduces incumbency lock-in.
- **Co-operation / Alliances** on Decentralised Authority — no single government can unilaterally ship this; eIDAS 2.0 EU Digital Identity Wallet is the real-world example of this play happening.
- **Standards game** on Credentials / Verifiable Credentials — whoever shapes the schema and revocation conventions shapes the ecosystem. UK, EU, India (Aadhaar-style), NIST are all playing this.
- **Harvesting** on wallet vendors once the VC ecosystem settles — government and large incumbents will pick off successful Pioneers.
- **Exploiting constraint / Sensing engagement** on bad-actor rule exploitation — treat adversary telemetry as a first-class input into the rules/exception loop. (Anti-gameplay: *Fear, Uncertainty, Doubt* and *Lobbying* are the bad-actor / incumbent plays we should expect against SSI; name them early.)
- **Restriction of movement / Sweat and dump** are anti-patterns to watch — legacy ID vendors will try to keep nation-states on closed stacks.

### (e) Doctrine observations (40-principle catalogue)

- **Phase I – "Focus on user needs" / "Know your users"**: map has six anchors including an adversarial one. Strong on user-type diversity; watch for the classic pitfall of treating "Citizens" as monolithic (age, disability, digital-access gradients all matter for physical ↔ digital ID choice).
- **Phase II – "Use a common language" / "Challenge assumptions"**: the scenario's own vocabulary (identity vs identification vs identifiers; mutable vs immutable vs connectedness) is exactly the common-language discipline Wardley asks for. The map preserves that separation.
- **Phase II – "Think small"**: the Claims → Credentials → Identity chain respects component granularity; the Power (over/with/to) triad keeps the social-power concept decomposed rather than aggregated into a single "governance" blob.
- **Phase III – "Design for constant evolution"**: inertia flag on Physical ID acknowledges that redesign pressure exists but won't resolve on its own. The evolve arrows on VC/SSI/Decentralised Authority / Digital Identification mark the expected directions of travel.
- **Watch-outs**:
  - *Missing anchor:* No "Auditors / Regulators-as-distinct-actor" — in some jurisdictions the auditor is materially distinct from the regulator. Consider adding if that's load-bearing for the analysis.
  - *Underspecified Knowledge layer:* The map is mostly activities and data. A deeper pass would add Knowledge nodes (cryptographic theory, identity philosophy, legal personhood) and Practice nodes (KYC, AML) with $\tau$ annotations.
  - *"You cannot measure evolution over time or adoption":* The November 2022 framing is only used to justify *current-state* placements against the cheat sheet, not to forecast speed.

## 5. Tensions the scenario asked about, located on the map

1. **Centralised authority vs self-sovereign identity** sits along the bottom-right to middle-left diagonal: Centralised Authority at $\varepsilon \approx 0.70$ (Product/Commodity) vs SSI at $\varepsilon \approx 0.15$ (Genesis). The map shows them *both* as dependencies of different Power modes: Power Over → Centralised Authority, Power To → SSI. That's the architectural form of the tension.
2. **Bad-actor rule exploitation** is the Rule Exploitation node ($\nu = 0.86$, $\varepsilon = 0.20$) — visible, novel, and plugged into Rules + Exception Handling. Its high $D$ says this is where defender investment belongs.
3. **Novel vs standardised** — the note markers separate the two clusters: standardised substrate (PKI, Internet, Physical ID) bottom-right; novel superstructure (VC, SSI, Decentralised Authority) middle-left.

## 6. Heuristics caveat

As stated in Section 7 of the prompt, $D$, $K$, and $R$ are attention heuristics proposed by this repository, not canonical Wardley metrics. They are used above as prompts for where to look, not as scores to optimise.

## 7. No forecast, only scenario

Evolution arrows in the OWM are scenario not forecast. Any time-based dynamic would use

$$\frac{d\varepsilon}{dt} = r \, \varepsilon \, (1 - \varepsilon)$$

with an explicit label that this is stylised — per Wardley's climatic pattern that evolution cannot be measured over time.
