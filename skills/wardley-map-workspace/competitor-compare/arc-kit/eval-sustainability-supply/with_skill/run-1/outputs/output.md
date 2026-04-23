# Supply-Chain Sustainability (Producer to Consumer)

**Anchor user:** Consumer buying a product through a supply chain that carries sustainability claims
**User need:** Buy / consume a sustainably produced product and be able to trust the sustainability signal
**Date:** 2026-04-22
**Scope:** End-to-end producer-to-consumer supply chain, plus the regulatory and compliance apparatus that surrounds it

Four actors sit on the map: the **Consumer** is the anchor, the **Retailer** mediates the commercial relationship, the **Producer** owns the physical chain, and the **Regulator** sets the rules. Their value chains intersect in two recognisable zones: an **open-market zone** on the right (ratings, labels, logistics, channels) where sustainability is commoditising and competition plays out in consumer-visible signals; and a **regulated zone** on the centre-left (laws, trade agreements, sanctions, bureaucracy, certification) where sustainability is mandated and compliance is the currency.

---

## Visual Map

```text
Title: Supply-Chain Sustainability (Producer to Consumer)
Anchor: Consumer — buy / consume a sustainable product
Date: 2026-04-22

                    Genesis    Custom     Product    Commodity
                       │          │          │          │
Visible            ┌───┼──────────┼──────────┼──────────┼───┐
                   │   │          │          │          │   │
                   │   │                         Consumer ●  │  (anchor, 0.96 vis)
                   │   │                                    │
                   │   │                    Retailer ●      │
                   │   │            Trade Agreements ●      │
                   │   │   Bureaucracy ●   Backhaul ●       │
                   │   │   Laws & Regs ●   Packaging ●      │
                   │   │                          Rating ●─→ │  commoditising
                   │   │                Last-Mile ●         │
                   │   │                 Storefront ●       │
                   │   │              Online Dist. ●        │
                   │   │                 Waste ●            │
                   │   │           Cert. Scheme ●──→        │
                   │   │        Sanctions ●                 │
                   │   │              Temp / Freshness ●    │
                   │   │              Sustainable Product ● │
                   │   │           Audit ●──→               │
                   │   │         Disclosure ●──→            │
                   │   │        Monitoring ●──→             │
                   │   │   Raw Material Sourcing ●          │
                   │   │    Reg. Guidelines ●──→            │
                   │   │     Manufacturing ●                │
                   │   │     Resource Efficiency ●──→       │
                   │   │     Complex Product Sourcing ●──→  │
                   │   │     Reusability / Circular ●──→    │
                   │   │                                    │
                   │   │   Sustainability R&D ●──→          │
Hidden             │   │                          Regulator │
                   │   │                               ●    │
                   └───┴────────────────────────────────────┘

Legend: ● Current position, → Evolution direction, × Inertia (see Inertia Points below)
```

Positions follow the OWM convention: the X-axis is evolution in [0,1] (Genesis → Commodity); the Y-axis is visibility in [0,1] (anchor near the top, infrastructure near the bottom). Full numeric positions are in the YAML block and in `draft.owm`.

---

## Value-Chain Walkthrough

Working down from the anchor:

1. **Consumer (anchor)** depends on being able to pick a **Sustainable Product** and read a **Sustainability Rating / Label** via a **Retailer**.
2. The **Retailer** pulls from three channels — **Online Distribution**, **Storefront Distribution**, and **Cooperative Distribution** — each with different logistics profiles and different inertia.
3. Both the Retailer and the Consumer-facing **Rating / Label** are underwritten by a **Certification Scheme**, which in turn draws on **Audit**, **Disclosure Reporting**, and ultimately **Monitoring**.
4. The **Producer** owns the physical chain: **Manufacturing** pulls from **Raw Material Sourcing** and **Complex Product Sourcing**, wraps outputs in **Packaging**, manages **Temperature / Freshness Handling** where applicable, and ships via **Last-Mile Transportation** (often a fleet-based commodity) backed by **Backhaul Transportation**.
5. End-of-life flows are **Waste Handling** and **Reusability / Circular Return**, both of which feed back into **Sustainability R&D**.
6. The **Regulator** sits on the other side of the map with a stack of instruments — **Laws and Regulations**, **Trade Agreements**, **Sanctions**, **Regulatory Guidelines** — all mediated by **Bureaucracy**. The Producer is pulled toward the regulatory stack through compliance dependencies, which is what creates the "regulated zone" in the centre-left.
7. **Sustainability R&D** and **Resource Efficiency** are the Genesis-leaning differentiators — novel materials, circular designs, process redesigns — where the next wave of sustainable advantage is being built.

---

## Open-Market vs Regulated Zones

One of the questions the scenario asked was *"where is sustainability open-market driven versus regulated?"* The map answers that as two distinct clusters:

- **Open-market zone (right of 0.6 evolution, high visibility)**: Ratings, labels, certification schemes, last-mile transportation, backhaul, packaging, online distribution, storefront distribution. This is where multiple vendors compete, standards converge, consumers see differences, and sustainability is a marketing and product feature. Commoditisation is the direction of travel.
- **Regulated zone (0.4-0.6 evolution, centre-band visibility)**: Laws, regulations, trade agreements, sanctions, guidelines, bureaucracy, disclosure, audit, monitoring. This is where sustainability is *mandated* — the producer has no choice — and the shape of the market is set by regulators rather than by consumers.
- **Genesis / R&D zone (left of 0.25 evolution)**: Sustainability R&D, and to a lesser extent circular-return and resource-efficiency practices. This is where differentiators are invented.

The strategic read: producers who *only* compete in the open-market zone ship table-stakes sustainability and face margin pressure from commodity ratings. Producers who invest in the R&D zone and then push novel materials / circular models through the regulated zone (standards capture, disclosure, certification) convert Genesis work into durable advantage.

---

## Structured Output

```yaml
wardley_map:
  metadata:
    title: "Supply-Chain Sustainability (Producer to Consumer)"
    author: "arc-kit wardley-mapping skill (blind eval)"
    date: "2026-04-22"
    version: "1.0"
    scope: "End-to-end producer-to-consumer supply chain, regulatory apparatus, compliance, R&D"

  anchor:
    user: "Consumer of a sustainably produced good"
    need: "Buy / consume a sustainable product and trust the sustainability signal"

  components:
    # Actors and user-facing outcomes
    - name: "Consumer"
      evolution: "Commodity"
      position: 0.96
      visibility: 0.90
      depends_on: ["Sustainable Product", "Sustainability Rating / Label", "Retailer"]
      notes: "Anchor — commodity-level demand."
      movement: "none"

    - name: "Sustainable Product"
      evolution: "Commodity"
      position: 0.88
      visibility: 0.70
      depends_on: ["Producer", "Packaging", "Certification Scheme"]
      notes: "Branded sustainable SKU; converging on product norms."
      movement: "evolving"

    - name: "Sustainability Rating / Label"
      evolution: "Commodity"
      position: 0.86
      visibility: 0.78
      depends_on: ["Certification Scheme", "Disclosure Reporting", "Audit"]
      notes: "Consumer-visible sustainability signal; commoditising as standards converge."
      movement: "accelerating"

    - name: "Retailer"
      evolution: "Commodity"
      position: 0.84
      visibility: 0.82
      depends_on:
        ["Online Distribution", "Storefront Distribution",
         "Cooperative Distribution", "Certification Scheme", "Producer"]
      notes: "Mature channel player; sustainability is a shelf-decision moderator."
      movement: "evolving"

    - name: "Producer"
      evolution: "Product"
      position: 0.78
      visibility: 0.55
      depends_on:
        ["Manufacturing", "Raw Material Sourcing", "Complex Product Sourcing",
         "Packaging", "Temperature / Freshness Handling",
         "Last-Mile Transportation", "Backhaul Transportation",
         "Resource Efficiency", "Waste Handling",
         "Laws and Regulations", "Trade Agreements", "Sanctions",
         "Regulatory Guidelines", "Disclosure Reporting", "Monitoring", "Audit"]
      notes: "The physical-chain owner; compliance pulls them centre-left."
      movement: "evolving"

    - name: "Regulator"
      evolution: "Product"
      position: 0.80
      visibility: 0.20
      depends_on:
        ["Laws and Regulations", "Trade Agreements", "Sanctions",
         "Regulatory Guidelines", "Bureaucracy", "Monitoring"]
      notes: "Institution owning the rule-set — visible instruments, invisible office."
      movement: "none"

    # Channels
    - name: "Online Distribution"
      evolution: "Product"
      position: 0.72
      visibility: 0.88
      depends_on: ["Last-Mile Transportation"]
      notes: "Mature e-commerce channel."
      movement: "evolving"
    - name: "Storefront Distribution"
      evolution: "Product"
      position: 0.70
      visibility: 0.85
      depends_on: ["Backhaul Transportation"]
      notes: "Legacy high-street channel; shrinking share."
      movement: "inertia"
    - name: "Cooperative Distribution"
      evolution: "Custom-Built"
      position: 0.68
      visibility: 0.40
      depends_on: ["Last-Mile Transportation"]
      notes: "Community / co-op model — lower evolution and lower visibility."
      movement: "inertia"

    # Sourcing / manufacturing
    - name: "Raw Material Sourcing"
      evolution: "Product"
      position: 0.55
      visibility: 0.60
      depends_on: []
      notes: "Commodity supply for some inputs, bespoke for sustainable alternatives."
      movement: "evolving"
    - name: "Complex Product Sourcing"
      evolution: "Product"
      position: 0.50
      visibility: 0.45
      depends_on: []
      notes: "Assemblies / multi-stage inputs with nested sustainability profiles."
      movement: "accelerating"
    - name: "Manufacturing"
      evolution: "Product"
      position: 0.52
      visibility: 0.55
      depends_on:
        ["Raw Material Sourcing", "Complex Product Sourcing", "Resource Efficiency"]
      notes: "Well-understood practice with per-sector specialisation."
      movement: "evolving"
    - name: "Packaging"
      evolution: "Product"
      position: 0.62
      visibility: 0.80
      depends_on: ["Raw Material Sourcing"]
      notes: "Sustainable packaging is actively commoditising."
      movement: "evolving"
    - name: "Temperature / Freshness Handling"
      evolution: "Product"
      position: 0.58
      visibility: 0.65
      depends_on: ["Backhaul Transportation"]
      notes: "Cold-chain tech maturing; sustainability adds energy-cost pressure."
      movement: "accelerating"

    # Logistics
    - name: "Last-Mile Transportation"
      evolution: "Product"
      position: 0.62
      visibility: 0.75
      depends_on: ["Backhaul Transportation"]
      notes: "Multiple vendors, electrification pressure."
      movement: "evolving"
    - name: "Backhaul Transportation"
      evolution: "Product"
      position: 0.58
      visibility: 0.85
      depends_on: []
      notes: "Global freight — mature, but emissions disclosure is a moving target."
      movement: "evolving"

    # End of life
    - name: "Reusability / Circular Return"
      evolution: "Custom-Built"
      position: 0.40
      visibility: 0.35
      depends_on: ["Sustainability R&D"]
      notes: "Early operational models — still custom per sector."
      movement: "accelerating"
    - name: "Waste Handling"
      evolution: "Product"
      position: 0.55
      visibility: 0.72
      depends_on: ["Reusability / Circular Return"]
      notes: "Municipal-utility shape in developed markets."
      movement: "evolving"

    # Regulatory
    - name: "Laws and Regulations"
      evolution: "Custom-Built"
      position: 0.48
      visibility: 0.78
      depends_on: ["Bureaucracy"]
      notes: "Jurisdiction-specific; slow to change."
      movement: "inertia"
    - name: "Trade Agreements"
      evolution: "Custom-Built"
      position: 0.52
      visibility: 0.82
      depends_on: ["Bureaucracy"]
      notes: "Bilateral / multilateral deals with sustainability clauses growing."
      movement: "evolving"
    - name: "Sanctions"
      evolution: "Custom-Built"
      position: 0.45
      visibility: 0.70
      depends_on: ["Bureaucracy"]
      notes: "Targeted instruments; episodic."
      movement: "none"
    - name: "Regulatory Guidelines"
      evolution: "Custom-Built"
      position: 0.46
      visibility: 0.55
      depends_on: ["Bureaucracy"]
      notes: "Non-binding but shaping; commoditising as disclosure standards mature."
      movement: "accelerating"
    - name: "Bureaucracy"
      evolution: "Custom-Built"
      position: 0.40
      visibility: 0.82
      depends_on: []
      notes: "Institutional machinery — resistant to change."
      movement: "inertia"

    # Compliance
    - name: "Monitoring"
      evolution: "Product"
      position: 0.52
      visibility: 0.45
      depends_on: []
      notes: "Sensors, remote-sensing, satellite + supplier reporting."
      movement: "accelerating"
    - name: "Audit"
      evolution: "Product"
      position: 0.62
      visibility: 0.55
      depends_on: ["Monitoring"]
      notes: "Big-4 + specialist sustainability auditors converging on frameworks."
      movement: "accelerating"
    - name: "Disclosure Reporting"
      evolution: "Product"
      position: 0.58
      visibility: 0.60
      depends_on: ["Monitoring"]
      notes: "Frameworks (CSRD, SEC climate rule, TCFD→ISSB) are commoditising disclosure."
      movement: "accelerating"
    - name: "Certification Scheme"
      evolution: "Product"
      position: 0.60
      visibility: 0.70
      depends_on: ["Audit", "Regulatory Guidelines"]
      notes: "Label ecosystems (e.g. Fairtrade, Rainforest Alliance, B-Corp) — mature products."
      movement: "evolving"

    # R&D / efficiency
    - name: "Sustainability R&D"
      evolution: "Genesis"
      position: 0.20
      visibility: 0.35
      depends_on: []
      notes: "Novel materials, circular models, process redesigns — differentiator source."
      movement: "evolving"
    - name: "Resource Efficiency"
      evolution: "Custom-Built"
      position: 0.45
      visibility: 0.50
      depends_on: ["Sustainability R&D"]
      notes: "Energy / water / material efficiency — practice-heavy, sector-specific."
      movement: "accelerating"

  analysis:
    opportunities:
      - "Consumer-visible Rating / Label is commoditising — first-mover advantage accrues to producers who align disclosure with emerging ISSB/CSRD before competitors."
      - "Circular-return models are Custom-Built today; a producer with a credible take-back scheme can ride the evolution curve and capture regulatory goodwill."
      - "Resource-efficiency investments pay twice — operating cost reduction plus disclosure score — so the R&D spend is double-counted in strategic terms."
      - "Bureaucracy + Certification Scheme create a defendable moat if a producer shapes the emerging standard rather than reacting to it (standards capture)."

    threats:
      - "Greenwashing risk: consumer-facing ratings commoditise faster than underlying audit, so labels without robust monitoring become negative signals."
      - "Regulatory divergence across jurisdictions (EU CSRD vs US patchwork vs UK vs APAC) forces multiple parallel compliance stacks."
      - "Storefront and cooperative distribution inertia may trap retailers in legacy logistics that cannot meet new sustainability disclosure."
      - "Complex-product sourcing opacity — nth-tier suppliers are the weakest link in scope-3 disclosure."

    inertia_points:
      - component: "Bureaucracy"
        reason: "Institutional machinery is slow to reform; new disclosure rules land on old plumbing."
      - component: "Storefront Distribution"
        reason: "Physical retail footprint is a sunk cost that resists rapid sustainability transformation."
      - component: "Cooperative Distribution"
        reason: "Community-owned models move on consensus timelines, not market timelines."
      - component: "Laws and Regulations"
        reason: "Legislative cycles lag market dynamics by 2-5 years."
      - component: "Sanctions"
        reason: "Politically driven; non-market timescales."

  recommendations:
    immediate:
      - "Publish a scope-3 disclosure pilot mapped to ISSB and CSRD — treat disclosure as a product feature, not a compliance chore."
      - "Audit the certification-scheme portfolio for overlap and retire labels that do not drive measurable purchase intent."
      - "Stand up continuous monitoring (sensor + supplier-reported data) for the top-10 emissions-contributing SKUs."
    short_term:
      - "Partner with last-mile electrification providers so the commoditisation of green logistics lands on your fleet first, not your competitors'."
      - "Reframe packaging R&D as a circular-return programme — the shift is from packaging-as-consumable to packaging-as-infrastructure."
      - "Build a regulatory-intelligence function that tracks Custom-Built → Product movements across jurisdictions (bureaucracy leaks early signals)."
    long_term:
      - "Invest in Sustainability R&D (Genesis) on novel materials with clear circularity profiles — this is the pipeline to future differentiators."
      - "Shape standards, don't chase them: participate in ISSB / CEN / ISO working groups that define the next generation of certification schemes."
      - "Move cooperative-distribution learnings upstream into mainstream retail — community-scale circular returns generalise better than retrofits."
```

---

## Analysis Checklist

- **Completeness.** Anchor defined (Consumer). All four requested actors present (Producer, Retailer, Consumer, Regulator). Supply chain covered (sourcing, manufacturing, packaging, temperature, transport — last-mile + backhaul, distribution — online/storefront/coop, end-of-life reuse and waste). Regulatory apparatus covered (laws, regulations, trade agreements, sanctions, guidelines, bureaucracy). Compliance covered (monitoring, audit, disclosure, labels, certifications, ratings). R&D and resource efficiency positioned.
- **Positioning.** Market maturity, not internal capability — certification and disclosure placed where market frameworks land (Product, commoditising), R&D placed at Genesis, bureaucracy at Custom-Built (institutional, slow). Dependencies respect visibility ordering (anchors and retailers high, regulatory instruments and R&D low-to-mid).
- **Insights.** Inertia concentrated in bureaucracy, legacy channels, and politically driven instruments. Commoditisation pressure concentrated in consumer-visible ratings, logistics, packaging. Genesis opportunity concentrated in materials R&D and circular models.
- **Strategic.** Gameplay patterns in play: **standards capture** (shape certification), **Pioneer–Settler–Town Planner split** (R&D vs operational sustainability vs compliance ops), **commoditise the complement** (make disclosure a product so labels become defensible), **co-evolution with regulator** (sense the Custom-Built → Product move before competitors).

---

## Gameplay Patterns Worth Flagging

From the arc-kit gameplay patterns reference, the ones most relevant here:

- **Standards capture / regulatory shaping** — The Custom-Built regulatory cluster is the prize. A producer who seeds the standard wins for a decade.
- **Commoditise the complement** — Disclosure frameworks are the complement to sustainable products; a producer who helps commoditise disclosure makes its own products relatively more valuable.
- **Ecosystem play** — Certification schemes aggregate upstream audit + disclosure; the ecosystem move is to offer the scheme to peers and become the de-facto rating substrate.
- **Acceleration on circular models** — Reusability / Circular Return is mid-map; a forcing move (take-back, deposit-return) can accelerate it rightward and lock in first-mover advantage.
- **Defensive inertia on bureaucracy** — Do not try to disrupt bureaucracy directly; route around it via voluntary schemes that prefigure the mandate.

---

## Climatic Patterns Acting on the Map

- **"Everything evolves" + "Commoditisation drives higher-order complexity"** — As ratings/labels commoditise, higher-order products (real-time product-level carbon, dynamic certification) emerge.
- **"No choice over evolution"** — Disclosure is a one-way street; producers cannot durably resist.
- **"Past success breeds inertia"** — Visible on storefront and cooperative distribution, and on bureaucracy.
- **"Efficiency enables innovation"** — Resource Efficiency feeds R&D budget; that loop should be protected.
- **"Red Queen"** — Consumer-visible sustainability claims evolve together with competitor claims; standing still means falling behind.

---

## Summary

The map separates a **regulated core** (centre-left: laws, trade, bureaucracy, guidelines, audit, disclosure, monitoring) from an **open-market surface** (right: retailer, channels, packaging, logistics, ratings, labels). The actors cluster as expected: **Consumer** at the top-right (anchor), **Retailer** a step below, **Producer** centre-right but pulled leftward by compliance dependencies, and **Regulator** bottom-centre-left. **Sustainability R&D** sits at Genesis and is the engine for future movement. The strategic win is to turn regulated-zone obligations (disclosure, certification) into open-market-zone differentiators (labels, ratings) while the window between "custom-built regulation" and "commodity disclosure" is still open.
