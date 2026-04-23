# Wardley Map: Risk Management Across the Financial Services Landscape

**Anchor:** Risk management for financial services — demanded by the public, corporations, and governments, delivered by retail banking, insurance, and lending providers, and shaped by regulation, rating agencies, and sovereignty concerns.

**Date:** 2026-04-22

**Scope:** Cross-industry capability view of the financial services risk landscape, with emphasis on the evolution position of cost, value, trust, and supply-chain awareness, and the lag of regulation relative to the risks it is meant to cover.

---

## Step 1 — Context

| Question | Answer |
|----------|--------|
| Primary user | Three anchors: Public (retail consumers), Corporations (business customers), Governments (regulators + sovereign users) |
| User need | Risk management across the financial services landscape |
| Scope | Entire financial services sector as a capability cross-cut |
| Primary goal | Identify where regulation lags risk; position cost/value/trust/supply-chain awareness on the evolution axis |
| Industry | Financial services |
| Depth | Standard (~20 components) |

## Step 2 — Value Chain

Working downward from the three demand anchors:

1. **Anchors:** Public, Corporations, Governments — these create demand for financial services and for the risk management wrapped around them.
2. **Providers:** Retail Banking, Insurance, Lending — deliver services to anchors.
3. **Trust-and-assets layer:** Trust, Assets, Customer Relationship — the intermediating surface between providers and their customers.
4. **Risk types:** Credit, Systemic, Cybersecurity, Cascade Failure, Third-Party — the risk surface providers must actively manage.
5. **Shaping forces:** Regulation, Rating Agencies, Sovereignty Concerns — external forces shaping how providers operate.
6. **Evolution-axis concepts:** Cost, Value, Supply-Chain Awareness — cross-cutting attributes the user explicitly asked to be positioned.
7. **Accountability chain:** Accountability → Society — how the consequences travel back to the public.

## Step 3 — Evolution Positioning

| Component | Stage | Evolution (X) | Visibility (Y) | Rationale |
|---|---|---|---|---|
| Public | Commodity | 0.88 | 0.97 | Consumer demand anchor at the top of the map; mature and ubiquitous. |
| Corporations | Commodity | 0.86 | 0.95 | Business demand anchor with established purchasing behaviour. |
| Governments | Commodity | 0.80 | 0.93 | Sovereign demand anchor — slowest-moving, near-top visibility. |
| Retail Banking | Commodity | 0.80 | 0.85 | Mature multi-vendor consumer industry, utility-like core services. |
| Insurance | Commodity | 0.78 | 0.80 | Mature industry; core products are well understood and competitively priced. |
| Lending | Commodity | 0.76 | 0.82 | Well understood, many providers; credit products are largely commoditised. |
| Trust | Product | 0.70 | 0.70 | Widely understood concept operationalised via brand and regulation, still differentiating between providers. |
| Assets | Commodity | 0.68 | 0.78 | Assets-under-management is a well understood, ubiquitous capability. |
| Customer Relationship | Product | 0.72 | 0.72 | CRM and account management are productised; feature competition still exists. |
| Credit Risk | Commodity | 0.85 | 0.65 | Century-old discipline — scoring, probability-of-default models are standard. Most commoditised of the risk types. |
| Systemic Risk | Product | 0.58 | 0.55 | Post-2008 frameworks (stress tests, capital requirements) make this productised across regulators. |
| Cybersecurity Risk | Product | 0.53 | 0.55 | Frameworks exist (NIST, ISO 27001) but threat surface is still evolving fast. |
| Cascade Failure Risk | Custom | 0.50 | 0.50 | Recognised post-2008 and post-COVID but tooling/quantification is bespoke and immature. |
| Third-Party Risk | Custom | 0.52 | 0.50 | Known as a discipline but operationalisation varies widely provider to provider. |
| Regulation | Custom/Product | 0.45 | 0.42 | **Lags the risk it covers** — sits to the left of cyber, third-party, and cascade risks. Chronic product-stage inertia. |
| Rating Agencies | Custom/Product | 0.43 | 0.55 | Oligopolistic utility-like service; entrenched business model. |
| Sovereignty Concerns | Custom | 0.40 | 0.30 | Emerging as a first-class risk (data residency, CBDCs, sanctions) but still bespoke per jurisdiction. |
| Cost | Commodity | 0.88 | 0.40 | Cost is a well-measured, universal attribute — the **most commoditised** of the four cross-cutting concepts. |
| Value | Product | 0.60 | 0.40 | Value is understood and routinely quantified but still negotiated contextually. |
| Supply-Chain Awareness | Custom | 0.28 | 0.28 | Still largely bespoke in financial services despite being mature in other industries — an inertia point. |
| Accountability | Custom | 0.45 | 0.20 | Formally required but operationally bespoke; board-level responsibility still being standardised. |
| Society | Genesis | 0.15 | 0.10 | Ultimate stakeholder in the accountability chain; society-as-explicit-stakeholder framing is still emerging in finance. |

## Step 4 — Movement

- Natural evolution (drift right): Cost, Rating Agencies, Credit Risk — all commoditising further.
- Acceleration: Cybersecurity Risk (threat-driven), Third-Party Risk (post-outage awareness), Supply-Chain Awareness (regulatory push).
- Inertia: **Regulation** is explicitly marked with inertia — it is being pushed right by the evolving risk surface but its institutional structure resists rapid movement.
- Cascade Failure Risk is moving from Custom toward Product as climate change, pandemics, and interconnected systems force standardisation.

## Step 5 — Visual Map

```text
Title: Risk Management Across the Financial Services Landscape
Anchor: Risk management for public / corporations / governments
Date: 2026-04-22

                    Genesis    Custom     Product    Commodity
                       |          |          |          |
Visible            ----+----------+----------+----------+----
                                                   Public   <- anchor
                                                   Govts
                                                   Corps
                                                   Retail Banking ->
                                                   Lending
                                                   Insurance
                                                   Assets
                                 Customer Relationship (Product)
                       Society
                                                   Credit Risk ->
                                                   Rating Agencies ->
                                         Trust (Product)
                                         Value
                                 Systemic Risk
                                 Cybersecurity Risk >>
                                 Regulation (x inertia) ->
                       Accountability
                       Sovereignty Concerns
                       Supply-Chain Awareness >>
                       Cascade Failure Risk ->
                       Third-Party Risk >>
                                                   Cost ->
Hidden             ----+----------+----------+----------+----

Legend: -> evolving, >> accelerating, x inertia
```

## Step 6 — Analysis

### Completeness
- Anchor is clearly defined (three demand-side anchors).
- Risk types, providers, shaping forces, cross-cutting attributes, and accountability chain are all present.
- Dependencies are shown (see OWM `depends_on` edges).
- Movement arrows present for the eight components experiencing the most change.

### Positioning
- Commodities (right-hand side): Cost, Credit Risk, Rating Agencies, Retail Banking, Insurance, Lending, Assets.
- Genuine Custom/Genesis items (left): Supply-Chain Awareness, Cascade Failure Risk, Accountability, Society. These are the "not-yet-productised" areas.
- **Regulation sits at Product (0.45) while the risks it covers — Cybersecurity, Third-Party, Cascade Failure — are at Custom-or-less. This is the regulatory lag the user asked about.**

### Key Insights

**Where regulation is lagging risk:**
- Cybersecurity Risk, Third-Party Risk, Cascade Failure Risk, and Supply-Chain Awareness are all to the **left** of Regulation on the evolution axis. Regulation is a Product-stage response to risks that are still Custom-stage in understanding and tooling. This is the central strategic finding.

**Evolution-axis observations the user asked for:**
- **Cost** — furthest right (0.30 on visibility, but 0.88 on evolution → Commodity). Cost is the most measured, most commoditised attribute.
- **Value** — Product stage (0.60 evolution). Understood and quantified but still contextual.
- **Trust** — Product stage (0.70). A durable differentiator for providers but broadly productised via brand and regulation.
- **Supply-Chain Awareness** — Custom stage (0.28 evolution). Financial services is materially behind other industries on this despite third-party risk being obviously present.

### Inertia Points
- **Regulation:** institutional and political structure resists pace of risk evolution.
- **Rating Agencies:** oligopoly with entrenched incentives.
- **Supply-Chain Awareness:** providers resist the cost of operationalising it without a regulatory mandate.

### Opportunities
- Productise Cascade Failure and Third-Party risk tooling — clear commoditisation path, currently Custom.
- Turn Supply-Chain Awareness into a product category (analogous to SBOM in software).
- Accelerate accountability frameworks as a first-class product — board-level tooling is still bespoke.

### Threats
- The regulatory-lag gap widens as risk types evolve faster than regulation; this creates systemic tail risk borne by Society.
- Rating-agency dependency creates single-point-of-failure exposure for providers.

## Output Format

```yaml
wardley_map:
  metadata:
    title: "Risk Management Across the Financial Services Landscape"
    author: "arc-kit wardley-mapping skill (blind benchmark run)"
    date: "2026-04-22"
    version: "1.0"
    scope: "Financial services risk capability cross-cut"

  anchor:
    user: "Public, Corporations, Governments"
    need: "Risk management across financial services"

  components:
    - name: "Public"
      evolution: "Commodity"
      position: 0.88
      visibility: 0.97
      depends_on: ["Retail Banking", "Insurance", "Lending"]
      notes: "Consumer demand anchor"
      movement: "none"
    - name: "Corporations"
      evolution: "Commodity"
      position: 0.86
      visibility: 0.95
      depends_on: ["Retail Banking", "Insurance", "Lending"]
      notes: "Business demand anchor"
      movement: "none"
    - name: "Governments"
      evolution: "Commodity"
      position: 0.80
      visibility: 0.93
      depends_on: ["Regulation", "Sovereignty Concerns", "Retail Banking"]
      notes: "Sovereign demand anchor"
      movement: "none"
    - name: "Retail Banking"
      evolution: "Commodity"
      position: 0.80
      visibility: 0.85
      depends_on: ["Trust", "Assets", "Customer Relationship", "Credit Risk", "Cybersecurity Risk", "Systemic Risk"]
      notes: "Mature multi-vendor provider"
      movement: "evolving"
    - name: "Insurance"
      evolution: "Commodity"
      position: 0.78
      visibility: 0.80
      depends_on: ["Trust", "Assets", "Customer Relationship", "Credit Risk", "Cascade Failure Risk", "Third-Party Risk"]
      notes: "Mature provider; cascade and third-party concentration"
      movement: "evolving"
    - name: "Lending"
      evolution: "Commodity"
      position: 0.76
      visibility: 0.82
      depends_on: ["Trust", "Assets", "Customer Relationship", "Credit Risk", "Third-Party Risk"]
      notes: "Commoditised credit products"
      movement: "evolving"
    - name: "Trust"
      evolution: "Product"
      position: 0.70
      visibility: 0.70
      depends_on: ["Regulation", "Rating Agencies"]
      notes: "Intermediating brand/institutional capability"
      movement: "evolving"
    - name: "Assets"
      evolution: "Commodity"
      position: 0.68
      visibility: 0.78
      depends_on: ["Rating Agencies"]
      notes: "Assets-under-management; utility-like"
      movement: "none"
    - name: "Customer Relationship"
      evolution: "Product"
      position: 0.72
      visibility: 0.72
      depends_on: ["Regulation"]
      notes: "CRM/account management as product"
      movement: "evolving"
    - name: "Credit Risk"
      evolution: "Commodity"
      position: 0.85
      visibility: 0.65
      depends_on: ["Rating Agencies"]
      notes: "Mature discipline; standard models"
      movement: "evolving"
    - name: "Systemic Risk"
      evolution: "Product"
      position: 0.58
      visibility: 0.55
      depends_on: ["Regulation"]
      notes: "Post-2008 stress-test frameworks"
      movement: "evolving"
    - name: "Cybersecurity Risk"
      evolution: "Product"
      position: 0.53
      visibility: 0.55
      depends_on: ["Regulation"]
      notes: "Frameworks exist; threat surface evolving fast"
      movement: "accelerating"
    - name: "Cascade Failure Risk"
      evolution: "Custom"
      position: 0.50
      visibility: 0.50
      depends_on: ["Regulation"]
      notes: "Known but bespoke; climate/pandemic driven"
      movement: "evolving"
    - name: "Third-Party Risk"
      evolution: "Custom"
      position: 0.52
      visibility: 0.50
      depends_on: ["Regulation", "Supply-Chain Awareness"]
      notes: "Operationally bespoke despite being widely known"
      movement: "accelerating"
    - name: "Regulation"
      evolution: "Custom"
      position: 0.45
      visibility: 0.42
      depends_on: ["Cost", "Value", "Accountability"]
      notes: "Institutional lag vs the risks it covers — sits to the LEFT of cyber/third-party/cascade risks"
      movement: "inertia"
    - name: "Rating Agencies"
      evolution: "Custom"
      position: 0.43
      visibility: 0.55
      depends_on: ["Cost"]
      notes: "Oligopolistic utility"
      movement: "evolving"
    - name: "Sovereignty Concerns"
      evolution: "Custom"
      position: 0.40
      visibility: 0.30
      depends_on: ["Accountability"]
      notes: "Data residency, CBDCs, sanctions"
      movement: "none"
    - name: "Cost"
      evolution: "Commodity"
      position: 0.88
      visibility: 0.40
      depends_on: ["Society"]
      notes: "Most commoditised cross-cutting attribute"
      movement: "evolving"
    - name: "Value"
      evolution: "Product"
      position: 0.60
      visibility: 0.40
      depends_on: ["Society"]
      notes: "Quantified but contextual"
      movement: "none"
    - name: "Supply-Chain Awareness"
      evolution: "Custom"
      position: 0.28
      visibility: 0.28
      depends_on: ["Accountability"]
      notes: "Behind other industries; inertia point"
      movement: "accelerating"
    - name: "Accountability"
      evolution: "Custom"
      position: 0.45
      visibility: 0.20
      depends_on: ["Society"]
      notes: "Chain back to society; bespoke"
      movement: "none"
    - name: "Society"
      evolution: "Genesis"
      position: 0.15
      visibility: 0.10
      depends_on: []
      notes: "Ultimate stakeholder in the accountability chain"
      movement: "none"

  analysis:
    opportunities:
      - "Productise Cascade Failure and Third-Party risk tooling."
      - "Turn Supply-Chain Awareness into a first-class product category for financial services."
      - "Standardise board-level accountability tooling."
    threats:
      - "Regulatory lag widens as cyber, third-party, and cascade risks evolve faster than regulation."
      - "Rating-agency concentration creates single-point-of-failure exposure."
      - "Sovereignty fragmentation raises per-jurisdiction bespoke cost."
    inertia_points:
      - component: "Regulation"
        reason: "Institutional and political structure resists pace of risk evolution"
      - component: "Rating Agencies"
        reason: "Oligopoly with entrenched incentives"
      - component: "Supply-Chain Awareness"
        reason: "No regulatory forcing function; providers resist operationalisation cost"

  recommendations:
    immediate:
      - "Acknowledge the regulatory-lag gap explicitly in risk committees."
      - "Stand up a third-party risk register as a productised internal capability."
    short_term:
      - "Adopt supply-chain awareness practice analogous to software SBOM."
      - "Reduce rating-agency monoculture by diversifying signal sources."
    long_term:
      - "Participate in standards bodies to productise cascade-failure risk frameworks."
      - "Elevate accountability tooling to a first-class board-level product."
```

## Analysis Checklist (arc-kit)

- Completeness: anchor, components, dependencies, movement all present.
- Positioning: visibility/evolution constraints respected (nu(a) >= nu(b) for each dependency).
- Insights: regulatory lag, rating-agency inertia, supply-chain gap all surfaced.
- Strategic: opportunities/threats/inertia/recommendations provided.
