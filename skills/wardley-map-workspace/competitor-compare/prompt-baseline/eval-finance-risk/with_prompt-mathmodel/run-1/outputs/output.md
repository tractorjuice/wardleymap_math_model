# Risk Management in Financial Services — Wardley Map

Generated from the prompt-only baseline (`prompts/wardley_map_generator.md`), first pass, no iteration. No skill files, no validator, no web search consulted.

## 1. Model tuple M = (V, E, U, nu, epsilon, t)

- **Anchor set U** — three user/demand types: `Public`, `Corporations`, `Governments`. Multi-anchor is required because the scenario explicitly names all three as the demand side.
- **V** — 28 components spanning: providers (retail banking, insurance, lending); the trust-and-assets bridge (trust, customer trust layer, identity/KYC, AUM); oversight (regulation, rating agencies, sovereignty); five named risk types (credit, systemic, cybersecurity, cascade failure, third-party); cross-cutting concepts flagged in the scenario (cost, value, supply-chain awareness — plus trust which doubled as a node); and data/infrastructure (risk models, transaction data, core banking platform, cloud infrastructure, payment rails).
- **E** — directed edges where `A->B` means "A depends on B". The graph contains the accountability chain back to society (Society Accountability -> Regulation / Trust) and the demand chain (Public / Corporations / Governments -> providers).
- **nu** — seeded via distance from the anchor set, then adjusted so that every edge satisfies nu(a) >= nu(b).
- **epsilon** — scored against the quick 4-row cheat sheet (Ubiquity, Certainty, User Perception, Publication Types) and averaged to a band midpoint.
- **t** — scenario-level evolution arrows provided; explicitly not a forecast.

## 2. OWM output

See `draft.owm` in this folder.

## 3. Cheat-sheet evolution scoring (quick 4-row method)

For brevity the table below summarises the averaged epsilon and the dominant stage. Components are grouped.

| Component | Ubiquity | Certainty | User Perception | Publication | Avg epsilon | Stage |
|---|---|---|---|---|---|---|
| Retail Banking | IV | IV | IV | III | 0.81 | IV Commodity/utility |
| Insurance | III | III | III | III | 0.625 | III Product |
| Lending | III | IV | III | III | 0.69 | III Product |
| Assets Under Management | III | III | III | III | 0.625 | III |
| Customer Trust Layer | II | II | II | II | 0.375 | II Custom Built |
| Identity and KYC | III | III | III | IV | 0.69 | III |
| Regulation | II | II | II | II | 0.375 | II (lagging — see note) |
| Rating Agencies | IV | III | III | III | 0.69 | III |
| Sovereignty Concerns | I | I | II | II | 0.25 | I->II |
| Credit Risk | IV | IV | III | III | 0.75 | III/IV |
| Systemic Risk | II | II | III | II | 0.44 | II |
| Cybersecurity Risk | III | II | III | II | 0.53 | III |
| Cascade Failure Risk | II | I | I | II | 0.28 | II |
| Third-Party Risk | II | II | II | II | 0.375 | II |
| Cost | IV | IV | IV | IV | 0.875 | IV |
| Value | II | II | II | II | 0.375 | II |
| Trust | II | II | II | II | 0.375 | II (genesis-adjacent as a measured construct) |
| Supply Chain Awareness | I | I | II | II | 0.25 | I->II |
| Risk Models | II | II | III | II | 0.44 | II-III |
| Transaction Data | IV | IV | III | III | 0.78 | III/IV |
| Core Banking Platform | III | III | III | III | 0.625 | III |
| Cloud Infrastructure | IV | IV | IV | IV | 0.875 | IV |
| Payment Rails | IV | IV | IV | IV | 0.875 | IV |

Scenario-axis answers the user explicitly asked for:

- **Cost** is far right (~0.82) — mature, commodified, optimised.
- **Value** is middle-left (~0.40) — Stage II, still judgmental and idiosyncratic per institution.
- **Trust** (as a construct the industry can measure/price) is Stage II (~0.40). The operational *Customer Trust Layer* is slightly more evolved (~0.45) but still Custom Built.
- **Supply Chain Awareness** sits at ~0.28 (Stage I->II): post-SolarWinds/LOG4J the industry names the problem, but operational practice is immature.
- **Regulation** sits at ~0.38 and is marked `inertia`. The risks it covers — especially Cybersecurity Risk (~0.53), Third-Party Risk (~0.38 but with stronger external forcing) and Cascade Failure Risk (~0.28 but moving) — are either ahead of it on the evolution axis or moving faster. Cybersecurity Risk in particular has stronger market-pull than Regulation; hence the scenario's "regulation lagging" callout.

## 4. Derived heuristics (prompt Section 7 — attention prompts only)

**Differentiation pressure D(v) = nu(v) * (1 - epsilon(v))**

| Rank | Component | D |
|---|---|---|
| 1 | Trust | 0.88 * (1-0.40) = 0.528 |
| 2 | Sovereignty Concerns | 0.60 * (1-0.25) = 0.450 |
| 3 | Customer Trust Layer | 0.74 * (1-0.45) = 0.407 |

Trust and the Customer Trust Layer are the clearest advantage zones: visible to the user, not yet commoditised. Sovereignty is visible to Governments and deliberately un-commoditised.

**Commodity leverage K(v) = (1 - nu(v)) * epsilon(v)**

| Rank | Component | K |
|---|---|---|
| 1 | Payment Rails | (1-0.10) * 0.88 = 0.792 |
| 2 | Cloud Infrastructure | (1-0.12) * 0.90 = 0.792 |
| 3 | Transaction Data | (1-0.22) * 0.80 = 0.624 |

All three should be treated as utilities. None belong in the differentiation budget.

**Dependency risk R(a, b) = nu(a) * (1 - epsilon(b))**

| Rank | Edge | R |
|---|---|---|
| 1 | (Retail Banking, Cascade Failure Risk) | 0.82 * (1-0.28) = 0.590 |
| 2 | (Insurance, Systemic Risk) | 0.80 * (1-0.44) = 0.448 |
| 3 | (Retail Banking, Third-Party Risk) | 0.82 * (1-0.375) = 0.512 |

The ordering above gives (Retail Banking, Cascade Failure Risk) > (Retail Banking, Third-Party Risk) > (Insurance, Systemic Risk). Highly visible providers are leaning on immature risk categories. The Regulation->Retail Banking / Insurance / Lending edges also carry real R because Regulation is less evolved than what it governs — this is the "regulation lagging" the scenario flags.

## 5. Suggested gameplays (from Wardley's 61-play catalogue)

- **Pig in a poke / Misdirection** on *Cost* signals — established providers can use commoditised Cost reporting to mask where Value sits. Counter-play: demand transparent Value metrics.
- **Open Approaches (open source / open data)** on *Risk Models* and *Supply Chain Awareness* — these are Stage II and benefit from collective maturation. Shared SBOM-style standards for the financial sector are the concrete move.
- **Harvesting** on the *Cloud Infrastructure / Payment Rails* layer — buy, don't build.
- **Defensive regulation / Lobbying** is what incumbents already play to *keep* Regulation at Stage II; the counter-play for a challenger or a regulator is **Sensing engines** (monitor Third-Party Risk and Cybersecurity Risk signals) plus **Market enablement** to accelerate Regulation toward Stage III.
- **Directed investment** on the *Customer Trust Layer* — this is the differentiation zone (high D) and deserves build-not-buy treatment.
- **Tower-and-moat** around a strong *Identity and KYC* capability if the provider wants a genuine competitive advantage.

## 6. Doctrine observations (from the 40-principle catalogue)

- **Phase I "Focus on user needs"** — the map has three anchors (Public, Corporations, Governments), which avoids the common single-user doctrine violation. Governments are anchored to Regulation and Sovereignty, not directly to providers, reflecting their indirect demand.
- **Phase II "Know the details"** / **"Challenge assumptions"** — Regulation is marked `inertia` to make explicit that it is *not* the most evolved thing on the map. Treating regulation as if it were Stage IV is a frequent doctrine violation in finance maps.
- **Phase III "Use appropriate methods"** — Cloud Infrastructure, Payment Rails, Transaction Data at epsilon >= 0.8 should be bought/rented, not built; the scenario's supply-chain-awareness concern argues against naive outsourcing of the *dependency layer*, which is why Supply Chain Awareness sits as a Stage II *practice* depending on those utilities.
- **Phase IV "Remove duplication and bias"** — the map deliberately collapses "risk management" into five named categories rather than re-listing them under each provider; this is a doctrine-aligned simplification.
- Potential violations flagged: the Knowledge layer is thin (Risk Models is the only explicit K-type node). A fuller map would add components for *Statistical inference*, *Regulatory theory*, and *Sovereignty doctrine* as Knowledge nodes.

## 7. Regulation-lagging-risk analysis (the scenario's headline question)

The scenario asks specifically where regulation is lagging the risk it is meant to cover. Comparing epsilon(Regulation) = 0.38 against the five risk types:

| Risk | epsilon | Relationship |
|---|---|---|
| Credit Risk | 0.75 | Regulation far behind — but the risk is well-understood in aggregate; lag is manageable. |
| Cybersecurity Risk | 0.53 | Regulation clearly behind; this is the loudest lag. |
| Third-Party Risk | 0.375 | Parity on the evolution axis but risk is moving faster (evolve arrow to 0.60). Regulation is about to be overtaken. |
| Systemic Risk | 0.44 | Rough parity; post-2008 frameworks have caught up. |
| Cascade Failure Risk | 0.28 | Regulation is slightly *ahead* (0.38 vs 0.28), but both are immature. The concern is that this risk is going to accelerate faster than regulatory science. |

Primary "regulation lags the risk" callouts: **Cybersecurity Risk** and **Third-Party Risk**. Both are market-driven and moving faster than regulatory process can keep up.

## 8. Constraints observed

- Every edge (a, b) in the map satisfies nu(a) >= nu(b).
- Coordinates are all inside [0, 1].
- Anchors sit at visibility >= 0.95.
- Only one `inertia` marker is used (Regulation), with the scenario's justification explicit.
- `evolve` arrows are labeled as scenarios, not forecasts, per the prompt's climatic-pattern reminder.

## 9. Not done (first-pass, no iteration)

- No multi-wave treatment of provider generations (retail banking clearly has multi-wave structure — branch, online, neobank, embedded — but the scenario did not request it).
- No formal 19-row cheat-sheet scoring; the 4-row quick method was used per the prompt.
- No tau (component type) annotation — the map would benefit from it, especially to make the Knowledge-layer thinness visible.
- No logistic dynamics simulation.
