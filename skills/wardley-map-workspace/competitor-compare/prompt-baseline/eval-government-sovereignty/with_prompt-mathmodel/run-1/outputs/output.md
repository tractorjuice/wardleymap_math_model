# National Sovereignty from a Government's Point of View (April 2023)

## 1. Anchors U and user needs

Four anchors — the sovereignty map has no single user:

- **Supranational Layer** (treaties, UN, WTO, EU/NATO, supranational courts) — needs legitimacy, treaty compliance, dispute-resolution mechanics.
- **Government** (the state as actor) — needs to preserve authority, monopoly of legitimate force, legal jurisdiction, solvency.
- **Corporations and Shareholders** — need enforceable property rights, predictable regulation, functional markets, protected supply chains.
- **Society** — needs security, belonging, fairness, services, credible elections.

## 2. Components V

See the OWM file for full list. Grouped logically:

- **Pillars (value-chain children of the anchors):** Territorial, Economic, Political, Digital, Cultural, Security sovereignty.
- **Legitimacy / feedback:** Election Legitimacy, Perception of Success, Public Belonging, and the five social norms (Integrity, Benevolence, Fairness, Competency, Identity).
- **Theatres:** Land, Supply Chain, Cyber, CNI.
- **Legal frame:** International Law, National Laws.
- **Crisis response.**
- **Media mix:** Mainstream Media, Social Media, Education, Art, Propaganda.
- **Awareness apparatus:** Territorial, Supply-Chain, Digital-Chain awareness.
- **Capability layer:** Intelligence, Military, Cyber, Diplomatic, Regulatory, Industrial.
- **Infrastructure:** Surveillance Sensors, Telecoms Networks, Cloud Compute, Semiconductors, Energy Grid, Data Platforms.
- **Inertia markers:** Legacy CNI Assets, Domestic Fab Base.

## 3. Dependencies E

Full list in `draft.owm`. Key chains:

- Government → pillars → theatres → awareness → capability → infrastructure. This is the backbone.
- Society → Public Belonging / Perception of Success → Media mix → Telecoms / Cloud / Data. This is the legitimacy feedback path.
- Election Legitimacy depends on all five social norms — legitimacy is a composite signal.
- Political Sovereignty loops back through Perception of Success and Public Belonging — the feedback the scenario asks for.
- Supranational Layer sits above International Law and co-anchors Economic and Political Sovereignty (treaties, trade regimes).

DAG check: the loops (Political Sovereignty ↔ legitimacy/perception) are modelled as directed dependencies downward from the pillar to the signals that *feed it*, so the visibility constraint is still satisfiable.

## 4. Visibility ν (Y-axis)

Seeded from shortest-path distance to the nearest anchor, then adjusted:

- Pillars lifted to 0.82–0.88 — they are the first thing each anchor names.
- Social norms kept high (0.74–0.76) even though they are semantically diffuse — Society and Government think about them directly.
- Theatres placed 0.62–0.68 — the government reasons about them but they are not what society experiences.
- Legal frame lifted (0.70–0.72) above theatres — laws are what the government directly exercises even though graph distance might put them lower.
- Media mix 0.52–0.60 — it shapes what anchors perceive but sits below perception/belonging.
- Awareness apparatus 0.42–0.46 — sensing layer.
- Capability layer 0.29–0.34.
- Infrastructure 0.13–0.20.

Hard constraint ν(a) ≥ ν(b) checked on every declared edge.

## 5. Evolution ε (X-axis) — quick 4-row cheat-sheet scoring

Representative scorings (stage → band midpoint):

- **Territorial Sovereignty** — Ubiquity IV, Certainty IV, Perception IV, Publication III. ≈ (0.875+0.875+0.875+0.625)/4 = **0.81** → placed at 0.65 to acknowledge contested-borders reality in April 2023 (Ukraine, Taiwan). Flagged in transition.
- **Digital Sovereignty** — Ubiquity II, Certainty I, Perception II, Publication I. ≈ (0.375+0.125+0.375+0.125)/4 = **0.25** → placed at 0.28. Custom-built / Genesis boundary.
- **Election Legitimacy** — Ubiquity III, Certainty II, Perception II, Publication II. ≈ 0.38 → 0.42. In transition (post-2020, post-Brexit, deepfake era).
- **Mainstream Media** — Ubiquity IV, Certainty IV, Perception IV, Publication IV → **0.875** → placed 0.75 (still Stage III/IV boundary because business model is in flux).
- **Social Media** — Ubiquity IV, Certainty III, Perception III, Publication IV → ~0.75 → placed 0.80.
- **Telecoms / Cloud / Energy Grid** — all four rows IV → **0.875** → placed 0.85–0.90.
- **Semiconductors** — Ubiquity IV, Certainty IV, Perception III, Publication III → ≈ 0.75, but placed at **0.55** because April 2023 is the CHIPS Act / EU Chips Act moment — the *supply* of advanced nodes is contested and being actively re-nationalised. Flagged in transition.
- **Digital-Chain Awareness** — Ubiquity I, Certainty I, Perception II, Publication I → ≈ 0.19 → 0.22.

## 6. Stage bands applied

- **Genesis [0, 0.25):** Digital Sovereignty, Benevolence, Integrity, Identity, Public Belonging, Supply-Chain Awareness (edge), Digital-Chain Awareness, Domestic Fab Base.
- **Custom Built [0.25, 0.5):** Political Sovereignty, Cultural Sovereignty, Cyber Theatre, Cyber Capability, Art, Election Legitimacy, Fairness, Competency, Perception of Success, Propaganda, Crisis Response.
- **Product (+rental) [0.5, 0.75):** Territorial, Economic, Security Sovereignty; Land / Supply Chain / CNI theatres; International Law, National Laws, Intelligence, Diplomatic, Regulatory, Industrial capability; Education; Semiconductors; Data Platforms.
- **Commodity (+utility) [0.75, 1]:** Mainstream Media, Social Media, Military Capability, Surveillance Sensors, Telecoms Networks, Cloud Compute, Energy Grid.

That's the answer to the scenario's final question — the right-hand side (Telecoms, Cloud, Energy, Surveillance Sensors, Social Media) is *industrialised infrastructure*; the left side (Digital Sovereignty, Digital-Chain Awareness, Identity/Benevolence norms, Domestic Fab Base) is the *contested and fragile frontier*.

## 7. Derived heuristics

Using D(v) = ν · (1−ε), K(v) = (1−ν) · ε, and R(a,b) = ν(a) · (1−ε(b)).

### Top 3 by D (differentiation pressure)

| Component | ν | ε | D |
|---|---|---|---|
| Digital Sovereignty | 0.84 | 0.28 | **0.605** |
| Cultural Sovereignty | 0.82 | 0.30 | 0.574 |
| Political Sovereignty | 0.86 | 0.38 | 0.533 |

Reasoning: each is a pillar the state is *expected* to provide but the delivery model is genuinely undefined in 2023 — "digital sovereignty" means different things in Brussels, Beijing, and Washington. High D = this is where sovereignty strategy has teeth.

### Top 3 by K (commodity leverage)

| Component | ν | ε | K |
|---|---|---|---|
| Telecoms Networks | 0.18 | 0.88 | **0.722** |
| Energy Grid | 0.13 | 0.85 | 0.740 |
| Cloud Compute | 0.16 | 0.90 | 0.756 |

Reasoning: these are utility-grade. Commodity leverage plays — procure as utility, mandate resilience and sovereignty via regulation rather than by owning the asset. Mainstream Media (K ≈ 0.30) and Social Media (K ≈ 0.34) are also high-K but governments cannot cleanly "outsource" these without ceding legitimacy channels.

### Top 3 dependency risks by R

| Edge (a → b) | ν(a) | ε(b) | R |
|---|---|---|---|
| Election Legitimacy → Identity (norm) | 0.82 | 0.27 | **0.599** |
| Government → Digital Sovereignty | 0.97 | 0.28 | 0.698 |
| Critical National Infrastructure → Digital-Chain Awareness | 0.62 | 0.22 | 0.484 |

Reasoning: in every case a highly visible user-need-adjacent node is sitting on a Genesis / early-Custom foundation. The top row is the *live* 2023 vulnerability — election legitimacy depending on a barely-formed sense of national identity amplified through volatile media.

Also worth noting: Society → Public Belonging (R = 0.95·0.72 = 0.684) and Corporations and Shareholders → Digital Sovereignty (R = 0.96·0.72 = 0.691) — the anchors themselves are directly exposed to the immaturity of the pillars they rely on.

## 8. Suggested gameplays (Wardley 61-play catalogue)

- **Play: Commoditise / Utility Provider** — target Telecoms, Cloud, Energy Grid. The state's play is not to own them but to *regulate them as utilities* with sovereignty clauses (analogous to Cloud ACT / GAIA-X). Also applicable to Surveillance Sensors (procure as standard kit rather than bespoke).
- **Play: Open Source / Open Approaches** — target Digital-Chain Awareness and Cyber Capability. Sovereign visibility into software supply chains requires SBOM adoption, open scanners, shared threat intelligence.
- **Play: Standards Game** — target Digital Sovereignty, International Law. Whoever sets the standard (AI Act, DSA, CBAM, chip export controls) sets the frontier. April 2023 is mid-fight on all three.
- **Play: Pig in a Poke / Tower and Moat** (competitor-facing) — target Semiconductors, Industrial Capability. Subsidy-led re-shoring (CHIPS Act) is a tower-and-moat play — build a protected domestic position before the window closes.
- **Play: Ecosystem Alliance** — target Supranational Layer, International Law. NATO+EU+G7 tech coordination as a co-opetition alliance around AI, chips, export controls.
- **Play: Sensory Capture / Signal Distortion** (defensive framing) — target Media mix and Propaganda. The state must *recognise* this play is being used against it (foreign influence ops) as much as it is tempted to use it itself.
- **Play: Undermining Barriers to Entry** — target Domestic Fab Base inertia. Public capital + talent visas + academic pipelines to break the sunk-capital / political-capital lock-in.
- **Play: Pre-emptive Strike / Fast Follower** — target Cyber Capability and Digital-Chain Awareness. Build the awareness stack before a rival's dependency graph can be weaponised.

## 9. Doctrine / doctrine-violation notes

- **Know your users (Phase II)** — this map has *four* anchors because sovereignty has four legitimate customers. Getting this wrong (e.g., a map that treats Society as the only anchor) leads to classic civil-service blind spots. Good.
- **Use a common language / map** — the catalogue of social norms (Integrity, Benevolence, Fairness, Competency, Identity) is unusual for a Wardley map; the justification is that *legitimacy is the product* the Government is selling to Society, and norms are its features.
- **Use appropriate methods** — Stage I / Genesis components (Digital Sovereignty, Digital-Chain Awareness) MUST be treated agile / experimental. Putting them under a Stage IV procurement process is the canonical doctrine violation and directly produces the fragility the scenario asks about.
- **Focus on high situational awareness** — the Awareness apparatus sits low on Y (sensing layer) but is *load-bearing*. Under-investing here is a doctrine violation; the three awareness nodes are the only route from theatres into capability.
- **Think small ("as a team, as a contract")** — Domestic Fab Base is a >$50bn programme. This is a doctrine violation by necessity, which is why it's marked as inertia — it will resist evolution.
- **Design for constant evolution** — the map's right-hand side has been stable for decades (Telecoms, Energy, Media) but is now being reframed as sovereignty problems. Explicit movement flagged via `evolve` on Digital Sovereignty, Cyber Theatre, Semiconductors etc. as a *scenario*, not a forecast (per the climatic pattern).
- **Potential missing nodes** — Climate / ecological sovereignty; Financial Sovereignty as distinct from Economic (e.g., payments rails, sanctions plumbing, CBDC). Both defensible to add in a longer pass; kept folded into Economic Sovereignty and CNI for this draft.

## 10. Evolution dynamics note

Applied the logistic form dε/dt = r · ε · (1−ε) informally to set `evolve` targets on Digital Sovereignty, Cyber Theatre, Digital-Chain Awareness, Cyber Capability, and Semiconductors. These are **scenarios**, not forecasts — in April 2023 these are the components under active geopolitical pressure, and the prompt's climatic pattern explicitly says evolution cannot be measured over time. The logistic only tells us that *if* these evolve, they will do so with accelerating-then-decelerating adoption — it does not tell us *when*.

## 11. Where sovereignty is industrialised vs contested

- **Industrialised infrastructure (bottom-right quadrant, ε ≥ 0.75):** Telecoms Networks, Cloud Compute, Energy Grid, Military Capability, Surveillance Sensors, Social Media, Mainstream Media. Sovereign strategy here is about *terms of use* (jurisdiction, regulation, procurement), not invention.
- **Contested and fragile frontier (top-left, ε < 0.4 and ν high):** Digital Sovereignty, Cultural Sovereignty, Political Sovereignty, Election Legitimacy, and the five social norms. This is where sovereignty is being *re-negotiated* — and where the feedback loop Perception → Belonging → Legitimacy → Political Sovereignty is most fragile.
- **The hinge:** Digital-Chain Awareness (ν=0.42, ε=0.22) and Semiconductors-with-Domestic-Fab-Base inertia (ε≈0.30–0.55). These are low-visibility but load-bearing components whose maturity gates whether the top-left quadrant can ever be industrialised.

See `draft.owm` for the OWM source.
