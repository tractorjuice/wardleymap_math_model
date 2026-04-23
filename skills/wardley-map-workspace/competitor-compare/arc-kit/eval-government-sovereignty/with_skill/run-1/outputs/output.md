# National Sovereignty from a Government Point of View

**Date:** April 2023
**Scope:** Whole-of-nation sovereignty as seen by a government — pillars, theatres, awareness apparatus, capability layer, social-trust substrate, media mix, crisis response, and legitimacy feedback loops.

## Anchors (User Need)

Four anchors sit at the top of this map because sovereignty has four audiences whose "user needs" have to be met simultaneously:

- **Supranational Layer** — treaties, alliances, multilateral institutions (NATO, EU, WTO, UN). Needs: predictable state behaviour, rules-based conformance.
- **Government** — the actor operating the map. Needs: durable legitimacy, means to project power, ability to respond to shocks.
- **Corporations and Shareholders** — domestic and foreign commercial actors. Needs: stable property rights, functioning supply chains, predictable regulation.
- **Society** — citizens and the public. Needs: felt legitimacy, security, belonging, prosperity.

All four depend on sovereignty being credibly delivered; all four can withdraw legitimacy.

## Visual Map

```text
Title: National Sovereignty (Government View)
Anchors: Supranational Layer, Government, Corporations/Shareholders, Society
Date: 2023-04

                          Genesis      Custom        Product       Commodity
                             |            |             |             |
Visible   +------------------+------------+-------------+-------------+-----+
(high)    |  Digital-Sov  Cultural-Sov   Society  Govt   Corps  Supranat.  |
          |     (.22)      (.32)          (.30) (.42)   (.58)    (.35)     |
          |                                                                |
          |           Election Legitimacy x (.40)                          |
          |                                                                |
          |  Digital-Sov   Cultural   Political   Economic   Security  Terr|
          |  Pillar        Pillar     Pillar      Pillar     Pillar    Pil|
          |   (.22)        (.32)      (.40)       (.55)      (.62)    (.70)|
          |                                                                |
          |         Perception of Success (.45)   Public Belonging (.35)   |
          |                                                                |
          |  Identity Integrity Benevolence Fairness Competency            |
          |   (.25)    (.30)      (.38)      (.46)    (.54)                |
          |                                                                |
          |  Art  Propaganda   Education  Social Media ->  Mainstream x    |
          |(.28)    (.34)->>    (.66)       (.72)->>        (.78)          |
          |                                                                |
          |  International Law (.45)         Domestic Laws (.72)           |
          |                                                                |
          |  Cyber (.35) ->   Supply Chain (.55)   CNI (.68)   Land (.82)  |
          |                                                                |
          |        Crisis Response (.48)                                   |
          |                                                                |
          |  Digital-Chain  Supply-Chain ->>     Territorial               |
          |  Awareness       Awareness           Awareness                 |
          |   (.20)            (.40)              (.78)                    |
          |                                                                |
Hidden    |                 Capability Layer (.48)                         |
(low)     +----------------------------------------------------------------+

Legend:
  ●   Current position (X = evolution score 0-1)
  ->  Natural evolution rightward
  ->> Acceleration (force pushing component right faster than baseline)
  x   Inertia (resistance to movement)
```

Industrialised, commoditised right-hand side: **Land, Mainstream Media, Domestic Laws, Territorial Awareness, Supply Chain (just tipped into Product), Social Media**.
Still contested / custom-genesis on the left: **Digital Sovereignty, Digital-Chain Awareness, Cultural Sovereignty, Identity, Art, Integrity, Benevolence, Propaganda, Cyber (early Product)**.

## Structured Output

```yaml
wardley_map:
  metadata:
    title: "National Sovereignty (Government Point of View)"
    author: "arc-kit wardley-mapping skill, blind run"
    date: "2023-04-15"
    version: "1.0"
    scope: "Whole-of-nation sovereignty: pillars, theatres, awareness, capability, norms, media, legitimacy."

  anchors:
    - user: "Supranational Layer"
      need: "Predictable, rules-based state behaviour and alliance conformance."
    - user: "Government"
      need: "Durable legitimacy and effective means to project sovereign power."
    - user: "Corporations and Shareholders"
      need: "Stable property rights, functioning supply chains, predictable regulation."
    - user: "Society"
      need: "Felt legitimacy, security, belonging, prosperity."

  components:
    # Anchors
    - name: "Supranational Layer"
      evolution: "Custom-Built"
      position: 0.35
      visibility: 0.97
      depends_on: ["Political Sovereignty", "Economic Sovereignty", "International Law"]
      notes: "Post-2022 institutional reconfiguration (NATO expansion, export-control coalitions). Fragile but high-visibility."
      movement: "evolving"

    - name: "Government"
      evolution: "Custom-Built"
      position: 0.42
      visibility: 0.96
      depends_on: ["Election Legitimacy", "Political Sovereignty", "Economic Sovereignty",
                   "Territorial Sovereignty", "Security Sovereignty", "Digital Sovereignty",
                   "Cultural Sovereignty"]
      notes: "Anchor actor operating the map."
      movement: "none"

    - name: "Corporations and Shareholders"
      evolution: "Product"
      position: 0.58
      visibility: 0.94
      depends_on: ["Economic Sovereignty", "Digital Sovereignty", "Supply Chain"]
      notes: "Globalised and well-understood actor pattern; their reliance on state-provided stability creates sovereignty demand."
      movement: "none"

    - name: "Society"
      evolution: "Custom-Built"
      position: 0.30
      visibility: 0.95
      depends_on: ["Election Legitimacy", "Cultural Sovereignty", "Political Sovereignty"]
      notes: "The final legitimising anchor; its withdrawal is what turns a pillar fragile."
      movement: "none"

    # Election legitimacy
    - name: "Election Legitimacy"
      evolution: "Custom-Built"
      position: 0.40
      visibility: 0.88
      depends_on: ["Perception of Success", "Public Belonging",
                   "Integrity", "Benevolence", "Fairness", "Competency", "Identity"]
      notes: "Appears procedural (Product-like) but in 2023 is openly contested in multiple democracies; trust in process is custom-built, not commodity."
      movement: "inertia"

    # Pillars of sovereignty
    - name: "Political Sovereignty"
      evolution: "Custom-Built"
      position: 0.40
      visibility: 0.82
      depends_on: ["International Law", "Domestic Laws", "Fairness", "Competency"]
      notes: "Stable in form, contested in content as norms of legitimate rule shift."
      movement: "evolving"

    - name: "Economic Sovereignty"
      evolution: "Product"
      position: 0.55
      visibility: 0.82
      depends_on: ["Supply Chain", "Domestic Laws", "Perception of Success"]
      notes: "Globalisation made this Product-like; post-2022 friend-shoring is pulling it slightly leftward in practice even as the institutional apparatus remains mature."
      movement: "evolving"

    - name: "Territorial Sovereignty"
      evolution: "Product"
      position: 0.70
      visibility: 0.83
      depends_on: ["Land", "International Law"]
      notes: "Doctrine, borders, defence — deeply institutionalised but Ukraine war shows industrialised conventional sovereignty can still be violently contested."
      movement: "none"

    - name: "Security Sovereignty"
      evolution: "Product"
      position: 0.62
      visibility: 0.82
      depends_on: ["CNI", "Cyber", "Land", "Crisis Response"]
      notes: "Mature kinetic side, still-maturing cyber/hybrid side."
      movement: "evolving"

    - name: "Digital Sovereignty"
      evolution: "Genesis → Custom"
      position: 0.22
      visibility: 0.82
      depends_on: ["Cyber", "CNI", "Supply Chain"]
      notes: "The genuinely fragile pillar in April 2023: cloud dependence on a handful of foreign hyperscalers, chip supply bottlenecks, and contested platform regulation. Accelerating right under CHIPS/IRA, EU Chips Act, UK semiconductor strategy."
      movement: "accelerating"

    - name: "Cultural Sovereignty"
      evolution: "Custom-Built"
      position: 0.32
      visibility: 0.81
      depends_on: ["Identity", "Art", "Education"]
      notes: "Always contested; resists industrialisation by nature. Inertia from identity politics and historical narrative disputes."
      movement: "inertia"

    # Perception and belonging (feedback)
    - name: "Perception of Success"
      evolution: "Custom-Built"
      position: 0.45
      visibility: 0.75
      depends_on: ["Mainstream Media", "Social Media", "Competency"]
      notes: "Feeds back into legitimacy; mediated through the media mix."
      movement: "none"

    - name: "Public Belonging"
      evolution: "Custom-Built"
      position: 0.35
      visibility: 0.75
      depends_on: ["Identity", "Education", "Art", "Social Media"]
      notes: "Who counts as 'us'? In 2023 fragile, polarised; feeds back into legitimacy."
      movement: "none"

    # Social norms (trust substrate)
    - name: "Integrity"
      evolution: "Custom-Built"
      position: 0.30
      visibility: 0.70
      depends_on: ["Mainstream Media"]
      notes: "Trust that rulers mean what they say."
      movement: "inertia"

    - name: "Benevolence"
      evolution: "Custom-Built"
      position: 0.38
      visibility: 0.70
      depends_on: ["Mainstream Media"]
      notes: "Trust that the state acts in citizens' interest."
      movement: "none"

    - name: "Fairness"
      evolution: "Custom-Built"
      position: 0.46
      visibility: 0.70
      depends_on: ["Domestic Laws"]
      notes: "Procedural fairness is the most industrialised of the norms."
      movement: "none"

    - name: "Competency"
      evolution: "Product"
      position: 0.54
      visibility: 0.70
      depends_on: ["Education"]
      notes: "The 'can they actually deliver?' perception; semi-objective and feeds into Perception of Success."
      movement: "none"

    - name: "Identity"
      evolution: "Custom-Built"
      position: 0.25
      visibility: 0.70
      depends_on: ["Education", "Art"]
      notes: "Contested; inherently resistant to commoditisation."
      movement: "inertia"

    # Media mix
    - name: "Social Media"
      evolution: "Product → Commodity"
      position: 0.72
      visibility: 0.62
      depends_on: []
      notes: "Utility-like reach but adversarial / weaponised; accelerating right as generative content floods it."
      movement: "accelerating"

    - name: "Mainstream Media"
      evolution: "Commodity"
      position: 0.78
      visibility: 0.62
      depends_on: []
      notes: "Industrialised but declining legitimacy — inertia from incumbents whose business model is broken."
      movement: "inertia"

    - name: "Education"
      evolution: "Product"
      position: 0.66
      visibility: 0.62
      depends_on: []
      notes: "State-scale education is Product-grade utility but curriculum content is politically contested."
      movement: "none"

    - name: "Art"
      evolution: "Custom-Built"
      position: 0.28
      visibility: 0.62
      depends_on: []
      notes: "Cultural production; inherently custom/genesis."
      movement: "none"

    - name: "Propaganda"
      evolution: "Custom-Built"
      position: 0.34
      visibility: 0.62
      depends_on: ["Social Media", "Mainstream Media"]
      notes: "Included explicitly per brief. Accelerating right with generative AI lowering production costs and foreign influence operations industrialising."
      movement: "accelerating"

    # Laws
    - name: "International Law"
      evolution: "Custom-Built"
      position: 0.45
      visibility: 0.58
      depends_on: ["Domestic Laws"]
      notes: "Treaty-by-treaty, enforcement patchy — still Custom-Built for most practical purposes."
      movement: "none"

    - name: "Domestic Laws"
      evolution: "Product → Commodity"
      position: 0.72
      visibility: 0.58
      depends_on: ["Capability Layer"]
      notes: "Industrialised: courts, statutes, regulatory bodies."
      movement: "none"

    # Theatres
    - name: "Land"
      evolution: "Commodity"
      position: 0.82
      visibility: 0.50
      depends_on: ["Territorial Awareness"]
      notes: "Physical territory, mapped and surveyed; the most industrialised theatre."
      movement: "none"

    - name: "Supply Chain"
      evolution: "Product"
      position: 0.55
      visibility: 0.50
      depends_on: ["Supply-Chain Awareness"]
      notes: "Post-COVID, post-Ukraine the industry is rewriting assumptions; visibility tooling productising fast."
      movement: "evolving"

    - name: "Cyber"
      evolution: "Custom → Product"
      position: 0.35
      visibility: 0.50
      depends_on: ["Digital-Chain Awareness"]
      notes: "National cyber defence still custom-built in most states; NCSC-grade capability is productising."
      movement: "evolving"

    - name: "CNI"
      evolution: "Product"
      position: 0.68
      visibility: 0.50
      depends_on: ["Digital-Chain Awareness", "Supply-Chain Awareness"]
      notes: "Critical National Infrastructure: mature asset inventories, regulatory overlays (NIS2 in EU; proposed US equivalents)."
      movement: "none"

    # Crisis response
    - name: "Crisis Response"
      evolution: "Custom-Built"
      position: 0.48
      visibility: 0.44
      depends_on: ["Territorial Awareness", "Supply-Chain Awareness", "Digital-Chain Awareness", "Capability Layer"]
      notes: "COVID and Ukraine war forced rapid productisation, but each crisis still exposes bespoke scaffolding."
      movement: "evolving"

    # Awareness apparatus
    - name: "Territorial Awareness"
      evolution: "Commodity"
      position: 0.78
      visibility: 0.36
      depends_on: ["Capability Layer"]
      notes: "GIS, satellite imagery, AIS — industrialised and commercially available."
      movement: "none"

    - name: "Supply-Chain Awareness"
      evolution: "Custom → Product"
      position: 0.40
      visibility: 0.36
      depends_on: ["Capability Layer"]
      notes: "Moving fast: CHIPS Act demands, EU Critical Raw Materials Act — but most governments still lack end-to-end visibility."
      movement: "accelerating"

    - name: "Digital-Chain Awareness"
      evolution: "Genesis → Custom"
      position: 0.20
      visibility: 0.36
      depends_on: ["Capability Layer"]
      notes: "SBOM, software bill-of-materials, national AI model provenance — early days in April 2023."
      movement: "evolving"

    # Capability layer (shared infrastructure)
    - name: "Capability Layer"
      evolution: "Custom-Built"
      position: 0.48
      visibility: 0.22
      depends_on: []
      notes: "Civil service skills, compute, data, analysts, procurement, legal drafting — partially industrialised; the real constraint on everything above."
      movement: "evolving"

  analysis:
    opportunities:
      - "Industrialise supply-chain awareness now — productisation path is clear (CHIPS, CRMA), and early movers lock in geopolitical leverage."
      - "Invest in digital-chain awareness (SBOMs, model provenance, cloud concentration metrics) while it is still genesis — first-mover advantage in setting the standard."
      - "Consolidate crisis response: every crisis since 2020 has generated bespoke scaffolding — package it into a standing capability (doctrine + playbooks + reserves)."
      - "Treat social norms (integrity, benevolence, fairness) as maintainable infrastructure, not weather — they compound into election legitimacy."

    threats:
      - "Digital sovereignty concentration risk: hyperscale cloud, EDA software, and advanced chips are single-vendor or single-country dependencies."
      - "Propaganda industrialisation via generative AI is accelerating faster than the integrity / benevolence norms that counter it."
      - "Election legitimacy is treated as Product (procedural, well-understood) but behaves as Custom-Built / contested — assuming it is commodity is the dangerous inertia."
      - "Cultural-sovereignty inertia: attempts to industrialise identity produce backlash; heavy-handed plays here cost public belonging."
      - "Mainstream media inertia: declining trust but still a primary norm-shaping channel creates a dangerous gap social media fills adversarially."

    inertia_points:
      - component: "Mainstream Media"
        reason: "Legacy business model and authority structure; cannot move to Commodity effectively because trust has decayed."
      - component: "Election Legitimacy"
        reason: "Political contest over rules means the process cannot be quietly industrialised without a legitimising settlement."
      - component: "Cultural Sovereignty / Identity"
        reason: "Ideologically charged — any state move to 'productise' identity triggers resistance from society anchor."
      - component: "Integrity (as a norm)"
        reason: "Hard to rebuild once decayed; depends on upstream honesty habits that span political cycles."

  recommendations:
    immediate:
      - "Stand up a National Supply-Chain Awareness Authority with a 12-month mandate to map concentration in critical categories (semis, pharma, energy, rare earths). Rationale: supply-chain awareness is productising fast — don't be the government that misses the window."
      - "Publish a Digital-Chain Awareness pilot (SBOMs for government-critical software + model-card register for public-sector AI). Rationale: genesis-stage, cheap to start, high optionality."
      - "Separate 'election administration' (productisable, make boring) from 'election legitimacy' (contested, invest in norms). Rationale: conflating them allows adversaries to attack legitimacy via administrative details."

    short_term:
      - "Industrialise crisis response: a standing cross-government crisis cadre with exercise cadence, doctrine, and interoperable data. Rationale: the custom-built scaffolding keeps getting thrown away after each event."
      - "Defensive platform regulation: treat social media reach above a threshold as utility-like CNI and regulate accordingly. Rationale: it's behaving as Commodity utility but governed as Product — close the gap before generative-AI propaganda does."
      - "Targeted reshoring / friend-shoring on a narrow list of critical inputs, with sunset clauses to avoid permanent Custom-Built inefficiency. Rationale: protect digital sovereignty without sacrificing the Product-stage benefits of trade."

    long_term:
      - "Build a Capability Layer programme (civil-service data/analytics/AI skills + shared compute + shared procurement frameworks). Rationale: every component above sits on it; weak Capability Layer is the binding constraint."
      - "Reinvest in cultural sovereignty via education and art rather than propaganda. Rationale: public belonging and identity are the only durable foundation for legitimacy; propaganda buys decay."
      - "Re-earn integrity / benevolence perception: visible, auditable competence in a few high-salience domains. Rationale: the trust substrate under election legitimacy cannot be bought, only demonstrated."
```

## Analysis Checklist

```yaml
analysis_checklist:
  completeness:
    anchor_defined: "Yes — four anchors (supranational, government, corporations, society) per brief."
    all_components_included: "Yes — 6 pillars, 4 theatres, 3 awareness components, 5 norms, 5 media, 2 laws, election legitimacy, perception, belonging, crisis response, capability layer = 33 components."
    dependencies_shown: "Yes — 60+ edges linking anchors to pillars, pillars to theatres, theatres to awareness, awareness to capability, norms into election legitimacy."
    movement_arrows_present: "Yes — accelerations on Digital Sovereignty, Supply-Chain Awareness, Social Media, Propaganda; inertia on Mainstream Media, Election Legitimacy, Cultural Sovereignty, Integrity; natural evolution on Cyber, Economic Sovereignty, Crisis Response, Capability Layer."

  positioning:
    market_based: "Components positioned by market / institutional maturity, not by how recently the government noticed them."
    commodities_on_right: "Land, Mainstream Media, Territorial Awareness, Domestic Laws, Social Media — on right."
    novels_on_left: "Digital-Chain Awareness, Digital Sovereignty, Identity, Art, Integrity — on left."

  insights:
    inertia: "Mainstream Media, Election Legitimacy, Cultural Sovereignty, Identity, Integrity."
    commoditisation_opportunities: "Supply-Chain Awareness, Crisis Response, Cyber, Digital-Chain Awareness."
    genesis_to_differentiator: "First mover on national AI model provenance / digital-chain awareness standards."
    technical_debt: "Treating election legitimacy as Product when it is Custom-Built; running crisis response as bespoke per-event."

  strategic:
    gameplay_patterns: "Defensive — regulation of commodity-utility social media as CNI. Offensive — standard-setting on SBOMs and model provenance. Ecosystem — friend-shoring alliances on critical inputs."
    invest_vs_outsource: "Invest in Capability Layer, awareness apparatus, norm maintenance. Outsource commoditised Land-surveillance, Mainstream Media distribution, Domestic-Laws tooling."
    climatic_patterns: "Co-evolution of practice and activity (digital sovereignty + cyber); commodity-to-utility transition (social media); punctuated equilibrium (Ukraine war shifting supply-chain + territorial urgency)."
    doctrine_weaknesses: "Know the users — four anchors means four legitimacy relationships, often only government-citizen is well-tracked. Use a common language — pillars/theatres/awareness vocabulary is not shared across departments."
```

## Key Takeaways

1. **Industrialised infrastructure**: Land, Mainstream Media, Territorial Awareness, Domestic Laws. These are commodities of statehood — reliable, boring, taken-for-granted. The risk here is inertia, not novelty.

2. **Contested and fragile**: Digital Sovereignty, Digital-Chain Awareness, Cultural Sovereignty, Identity, Art, Integrity, Benevolence, Propaganda. These are the places where legitimacy can be gained or lost in this decade.

3. **Dangerous mislabels**: Election Legitimacy looks Product-like (procedures, standards, institutions) but behaves Custom-Built (contested rules, trust erosion). Treating it as commodity is exactly the play that erodes it.

4. **Feedback loop**: Perception of Success and Public Belonging flow back into Election Legitimacy, which flows back up into Government and Society anchors. The media mix is the transmission belt — and it is being rewired by generative AI faster than the norms that counter it.

5. **Binding constraint**: The Capability Layer (civil service skills, compute, data, procurement) sits at the bottom of the map. Every pillar and awareness stream depends on it; under-investing there caps everything above.
