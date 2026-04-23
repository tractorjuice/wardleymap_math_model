# Defence Intelligence Landscape — March 2023

Scenario: Map how operational decisions get made in defence intelligence, covering actors, the collection/analysis chain, trust, the decision model, adversarial capability, and regulatory constraints. Identify what is commoditised and where the bleeding edge is in March 2023.

---

## 1. Model instantiation

Tuple $\mathcal{M} = (V, E, U, \nu, \varepsilon, t)$ with $t = $ March 2023.

**Anchor set $U$ (four user types).** Real defence intelligence has multiple simultaneous consumers:

- **Military Operational Decision** — the shooter / commander who needs an answer now.
- **Government Policy Decision** — slower-tempo strategic consumer (cabinet, MoD policy).
- **Citizen Trust** — democratic oversight; consumes integrity/benevolence signals, not raw intel.
- **Opponent Operational Decision** — adversaries are also trying to act on this same landscape; treating them as a separate anchor surfaces the whole adversarial layer naturally.

**Components $V$ (40 total)** — grouped into decision, trust, targeting, analysis, adversarial, collectors, sources, sensors, and regulatory-substrate layers. See the OWM file for exact placement.

---

## 2. OWM map

See `draft.owm`. Key placements and their cheat-sheet justifications (quick 4-row method, stage → midpoint $\in \{0.125, 0.375, 0.625, 0.875\}$):

| Component | Ubiquity | Certainty | User perception | Publication | $\varepsilon$ |
|---|---|---|---|---|---|
| GPS | IV | IV | IV | IV | 0.92 (rounded to 0.92 on map) |
| Cloud Compute | IV | IV | IV | IV | 0.875 → 0.92 |
| Social Media Feeds (as data source) | IV | III | IV | III | 0.75 → 0.82 |
| OSINT (as practice) | III | III | III | III | 0.625 → 0.70 |
| Human-in-the-Loop Decision (doctrine) | III | III | III | III | 0.625 → 0.55 (under transition downward as autonomy pressure rises) |
| AI/ML Analysis Engine | II | II | II | II | 0.375 → 0.28 (productised in commercial world but defence applications still experimental for ISR fusion) |
| Prompt Engineering Defence | I | I | I | I | 0.125 → 0.10 (brand-new post-ChatGPT wave, Nov 2022) |
| Adversarial ML Hardening | I | I–II | I | I | ~0.15 |
| Crowdsourced Collection (UA war style) | II | II | II | II | 0.25 (spiked in 2022 but not yet doctrine) |

The four-row scores average into $\varepsilon(v)$; map coordinates above are judgment-adjusted within each stage band.

**Visibility seed** via $\nu(v) = 1/(1 + d(v))$ then overridden:

- Raised for *Rules of Engagement* (doctrine artefact that commanders think about directly) despite being 2 hops deep.
- Raised for *Privacy Regulation* is a candidate but kept low because it's architecturally invisible to the operator even though citizens think about it — the citizen anchor reaches it via a shorter path, preserving $\nu(a) \ge \nu(b)$ on every edge.

Every edge satisfies the hard rule $\nu(a) \ge \nu(b)$ — I manually walked the edge list.

---

## 3. Where the bleeding edge sits (March 2023)

Left of 0.25 (Genesis) in this landscape:

- **Prompt Engineering Defence** (0.10) — ChatGPT launched Nov 2022; adversarial prompt injection against LLM-assisted analysts is four months old as a named threat.
- **Adversarial ML Hardening** (0.15) — research-grade; no defence standard exists.
- **Misinformation Defence** (0.20) — practices exist (fact-check bureaux) but operationalised pipelines tied into ISR are nascent.
- **Benevolence Signalling** (0.28) — the "trust" strand after the 2022–23 erosion of institutional trust; still poorly formalised.
- **Crowdsourced Collection** (0.25) — Ukraine-era demonstration (Aerorozvidka, open-source trackers) proved the concept but doctrine hasn't caught up.

## Where the commodity is (right of 0.75, Stage IV)

- **GPS** (0.92), **Cloud Compute** (0.92), **Data Storage** (0.90) — utility.
- **Camera/EO Imagery sensors** (0.85), **Satellite Imagery** (0.75) — the imagery *primitives* are commoditised even though analytic products are not.
- **Social Media Feeds** (0.82), **Public Data Sources** (0.80) — the *raw data* is commoditised; the right to ingest it is the live battle.
- **Human Collectors (HUMINT)** (0.78) — mature practice, near-commodity in its own terms, though the *tradecraft* has legacy inertia.

---

## 4. Strategic analysis

### (a) Top 3 by Differentiation pressure $D(v) = \nu(v)(1 - \varepsilon(v))$

1. **Commander Judgment** — $D = 0.84 \cdot 0.75 = 0.63$. High visibility, low evolution — this *is* the differentiator. Institutional knowledge is irreplicable.
2. **Competence Assessment** (trust) — $D = 0.80 \cdot 0.65 = 0.52$. Visible to policy anchor, immature practice.
3. **Rules of Engagement** — $D = 0.82 \cdot 0.30 = 0.25$. Still reasonable $D$; but this is actually productised (Stage III) — see below. True #3 is **Human-on-the-Loop Decision** at $D = 0.86 \cdot 0.70 = 0.60$, which beats it, making on-the-loop autonomy the live differentiation question.

Revised top-3 by $D$: Commander Judgment (0.63), Human-on-the-Loop Decision (0.60), Competence Assessment (0.52).

### (b) Top 3 by Commodity leverage $K(v) = (1 - \nu(v)) \cdot \varepsilon(v)$

1. **GPS** — $K = 0.72 \cdot 0.92 = 0.66$. Already utility; defence has no business building its own.
2. **Cloud Compute** — $K = 0.82 \cdot 0.92 = 0.75$. Largest $K$ in the map. Defence cloud (JEDI, JWCC) arguments are about *which* utility, not whether.
3. **Data Storage** — $K = 0.84 \cdot 0.90 = 0.76$. Also the largest by product; pair with Cloud Compute as a utility buy.

Honourable mention: **Social Media Feeds** ($K = 0.62 \cdot 0.82 = 0.51$), **Satellite Imagery** ($K = 0.78 \cdot 0.75 = 0.59$).

### (c) Top 3 dependency risks $R(a,b) = \nu(a) \cdot (1 - \varepsilon(b))$

1. **(Human-on-the-Loop Decision, AI/ML Analysis Engine)** — $R = 0.86 \cdot 0.72 = 0.62$. A visible decision mode depending on an immature engine. If the ML is wrong, autonomy becomes a liability.
2. **(AI/ML Analysis Engine, Prompt Engineering Defence)** — $R = 0.60 \cdot 0.90 = 0.54$. The analytic engine depending on a near-Genesis defence is the most acute new risk — this edge is the whole LLM-era attack surface.
3. **(Intelligence Analysis, AI/ML Analysis Engine)** — $R = 0.68 \cdot 0.72 = 0.49$. Analytical fusion is starting to outsource judgment to an ML engine whose validation story is weak.

Also notable: **(Government Policy Decision, Competence Assessment)** $R = 0.96 \cdot 0.65 = 0.62$ — policy trust depends on immature trust-measurement.

### (d) Suggested gameplays (from the 61-play catalogue)

- **Open Approaches (#15)** on Prompt Engineering Defence and Adversarial ML Hardening — these are pre-competitive; shared industry response beats unilateral in-house research. This is consistent with the "open" doctrine and pulls evolution toward $\varepsilon = 0.4$.
- **Pig in a Poke / First-mover advantage (#24)** on Crowdsourced Collection — the war in Ukraine has demonstrated this as a live capability; defence establishments that formalise the pattern ahead of adversaries get an early mover advantage before it commoditises.
- **Harvesting (#29)** on the AI/ML Analysis Engine layer — let commercial ML mature, then buy/absorb the best-fit vendors rather than build bespoke.
- **Sensors (climatic) / Signal Distortion (#45)** on Misinformation Defence — both a detection play (monitor weak signals) and a counter-signalling play against adversaries.
- **Co-opt (#19)** on Social Media Feeds — partner with platform owners rather than ingest adversarially; privacy-regulation path is then a co-written policy rather than a legal fight.
- **Dedicated investment / Differentiation (#36)** on Commander Judgment and the Trust stack — this is the asymmetric advantage; treat it as the core, everything else as substrate.
- **Fast Follower (#23)** on Cloud Compute and Data Storage — there is no win here; buy utility.

### (e) Doctrine violations / tensions

- **Doctrine 1 ("Know your users")** — the scenario explicitly includes opponents as actors; the map honours this with an Opponent anchor. Without it, the adversarial layer would float disconnected. Good.
- **Doctrine 4 ("Use a common language")** — the trust triad (competence, integrity, benevolence) is modelled as a Practice stack. Many defence maps omit trust entirely, which is a doctrine miss; this map surfaces it.
- **Doctrine 9 ("Focus on high-value")** — the regulatory substrate (Privacy Regulation, Data Ownership, Cross-Border Data Law) is placed deep but matters enormously; low visibility is correct *only* from the military anchor and is raised via the Citizen anchor.
- **Potential miss — Knowledge layer.** The map is activity/practice-heavy. It does not explicitly name Knowledge nodes like *theory of deterrence*, *signal detection theory*, or *ethics of lethal autonomy* — these underpin Commander Judgment but sit implicitly. A $\tau$-typed version could make this explicit.
- **Inertia flag.** *Legacy HUMINT Tradecraft* is marked as inertia. Forms: **human capital** (careers built on the old model), **political capital** (service loyalty), **sunk training cost**. This is a consumer-side inertia from the 14 consumer forms in the Inertia doc.

---

## 5. Closing observations

- The **centre of gravity** of March-2023 defence intelligence is the join between the Analysis layer (still productising AI/ML) and the Decision layer (shifting from in-the-loop to on-the-loop). $R$-risk concentrates here.
- The **regulatory substrate** is the most under-attended strategic surface — it is Stage II–III (being actively contested in GDPR vs. national-security carve-outs) and low visibility. Adversaries without these constraints have an operational tempo advantage that cannot be closed by better sensors.
- **Trust is the hidden anchor.** If Benevolence Signalling and Integrity Verification stay at $\varepsilon < 0.3$, the whole map loses the Citizen anchor, and democratic licence for the operational apparatus erodes. This is a doctrine-level concern, not a technical one.
- **Ukraine (Feb 2022–) shapes the map.** Crowdsourced Collection, OSINT-driven target discovery, and misinformation defence have all risen in visibility relative to a pre-2022 version of this map. The evolution vectors in `evolve` statements assume continued lessons-learned pressure from that conflict.

---

## 6. Disclosure

Outputs produced from the scenario brief using `prompts/wardley_map_generator.md` only (prompt-only baseline — no skill scripts, no references files, no validator, no benchmark reference map). No ground-truth reference was read.
