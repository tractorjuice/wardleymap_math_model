# Wardley Map: Connected Customer Journey in Retail

**Author:** Claude Code (arc-kit wardley-mapping skill)
**Date:** 2026-04-22
**Scope:** The end-to-end retail customer journey — from customer and producer, through needs, goods, services, channels, and the experience layer, including sensory / virtual / physical dimensions, trust, privacy, engagement, returns, and the societal context shaping it all.

---

## Step 1 — Context

| | |
|---|---|
| **Primary user** | External retail customer (with Producer as secondary anchor supplying the goods and services) |
| **User need** | Get the goods and services I need, through a trusted and engaging experience, across whichever channel suits me |
| **Scope** | Entire retail organisation / multi-channel retail |
| **Primary goal** | Identify where the retail experience is still custom (differentiation opportunity) and where it has hardened into commodity infrastructure (cost / leverage opportunity) |
| **Industry / domain** | Retail — consumer |
| **Depth** | Deep analysis (30+ components, gameplay and climate implications) |

---

## Step 2 — Visual Map

```text
Title: Connected Customer Journey in Retail
Anchor: Retail customer getting goods and services through a trusted, engaging experience
Date: 2026-04-22

                    Genesis       Custom         Product       Commodity
                    0.0     0.25           0.50           0.75        1.0
                       |       |              |              |          |
Visible           +----+-------+--------------+--------------+----------+
 1.0              |                                                     |
 0.95             |                               * Customer                       (anchor)
 0.93             |                    * Producer                                  (anchor)
                  |                         |                                      |
 0.87             |                                   * Need-for-Goods
 0.86             |                         * Need-for-Convenience
 0.85             |                * Need-for-Trust
 0.84             |           * Need-for-Belonging
                  |                         |                                      |
 0.76             |                * Retail-Experience       ------>               |
 0.73             |           * Engagement-&-Discovery        ------>              |
 0.72             |                * Brand-&-Storytelling                          |
 0.70             |       * Sensory-Experience               ------>               |
                  |                                                                 |
 0.63             |                                    * Goods                      |
 0.60             |                         * Services                              |
 0.58             |                               * Product-Range                   |
 0.55             |                               * Returns-&-Refunds   ------>     |
                  |                                                                 |
 0.52             |                * Trust-&-Privacy                                |
 0.50             |           * Societal-Behaviour-&-Demographics                   |
 0.48             |                * Consent-Management      ------>                |
 0.47             |                               * Physical-Store                  |
 0.46             |                * Consent-Management                             |
 0.45             |                               * E-commerce-Site                 |
 0.44             |                * Personalisation   ------>                      |
 0.43             |                         * Mobile-App                            |
 0.42             |                                   * Telesales                   |
 0.40             |           * Social-Commerce   ------>                           |
 0.38             |       * Virtual/AR-Channel    ------>                           |
 0.38             |                * Customer-Data-Platform   ------>               |
                  |                                                                 |
 0.32             |                                         * Order-Management      |
 0.30             |                                         * Inventory             |
 0.28             |                                         * Delivery/Logistics    |
 0.27             |                               * Reverse-Logistics               |
 0.26             |                                            * Payments           |
                  |                                                                 |
 0.22             |                                         * CRM-Platform          |
Hidden            |                                                                 |
 0.10             |                                                  * Cloud-Compute|
 0.08             |                                                   * Networking  |
 0.08             |                                                   * Data-Storage|
 0.0              +----+-------+--------------+--------------+----------+
                    Genesis       Custom         Product       Commodity

Legend:
  *        Current position
  ------>  Natural evolution (rightward drift)
  x        Inertia (noted in table below)
  >>       Acceleration (noted in table below)
```

---

## Step 3 — Structured Output

```yaml
wardley_map:
  metadata:
    title: "Connected Customer Journey in Retail"
    author: "Claude Code (arc-kit wardley-mapping skill)"
    date: "2026-04-22"
    version: "1.0"
    scope: "End-to-end retail customer journey across physical, e-commerce, telesales, and emerging social/AR channels, including the trust, data, and fulfilment plumbing that supports it."

  anchor:
    user: "Retail customer (with Producer as secondary anchor)"
    need: "Obtain the goods and services I need through a trusted, engaging experience, in whichever channel suits me"

  components:
    # --- Anchors ---
    - name: "Customer"
      evolution: "Anchor"
      position: 0.55
      visibility: 0.95
      depends_on: ["Need for Goods", "Need for Convenience", "Need for Trust", "Need for Belonging"]
      notes: "Primary anchor — the end shopper."
      movement: "none"

    - name: "Producer"
      evolution: "Anchor"
      position: 0.40
      visibility: 0.93
      depends_on: ["Goods", "Services"]
      notes: "Secondary anchor — manufacturers / brands supplying goods and services into the chain."
      movement: "none"

    # --- Needs ---
    - name: "Need for Goods"
      evolution: "Commodity"
      position: 0.78
      visibility: 0.87
      depends_on: ["Goods", "Services"]
      notes: "Well-understood baseline need — to acquire products."
      movement: "none"

    - name: "Need for Convenience"
      evolution: "Product"
      position: 0.60
      visibility: 0.86
      depends_on: ["Retail Experience", "Services"]
      notes: "Expectation of frictionless purchase; rapidly commoditising."
      movement: "evolving"

    - name: "Need for Trust"
      evolution: "Custom"
      position: 0.38
      visibility: 0.85
      depends_on: ["Trust and Privacy", "Brand and Storytelling"]
      notes: "Still highly variable between retailers; major differentiator."
      movement: "evolving"

    - name: "Need for Belonging"
      evolution: "Custom"
      position: 0.30
      visibility: 0.84
      depends_on: ["Engagement and Discovery", "Brand and Storytelling"]
      notes: "Community, identity, meaning — early-stage framing in most retail."
      movement: "evolving"

    # --- Experience layer ---
    - name: "Retail Experience"
      evolution: "Custom"
      position: 0.40
      visibility: 0.76
      depends_on: ["Engagement and Discovery", "Sensory Experience", "Brand and Storytelling", "Personalisation",
                   "Physical Store", "E-commerce Site", "Mobile App", "Telesales", "Social Commerce", "Virtual / AR Channel"]
      notes: "The curated experience layer — deliberately custom; where differentiation lives."
      movement: "evolving"

    - name: "Engagement and Discovery"
      evolution: "Custom"
      position: 0.35
      visibility: 0.73
      depends_on: ["Personalisation", "Social Commerce", "E-commerce Site", "Mobile App"]
      notes: "Content, search, curation, livestream shopping — fragmented, no dominant pattern."
      movement: "evolving"

    - name: "Brand and Storytelling"
      evolution: "Custom"
      position: 0.48
      visibility: 0.72
      depends_on: []
      notes: "Inherently custom per retailer; intentionally slowed from commoditising."
      movement: "inertia"

    - name: "Sensory Experience"
      evolution: "Genesis / Custom"
      position: 0.22
      visibility: 0.70
      depends_on: ["Physical Store", "Virtual / AR Channel"]
      notes: "Touch, smell, atmosphere — only partially reproducible online; still experimental."
      movement: "evolving"

    # --- Goods and services ---
    - name: "Goods"
      evolution: "Commodity"
      position: 0.82
      visibility: 0.63
      depends_on: ["Product Range"]
      notes: "The physical product SKU — commoditised outside of truly unique items."
      movement: "none"

    - name: "Services"
      evolution: "Product"
      position: 0.55
      visibility: 0.60
      depends_on: ["Returns and Refunds", "Delivery / Logistics"]
      notes: "Warranty, click-and-collect, gift wrapping, loyalty — maturing into product-stage offerings."
      movement: "evolving"

    - name: "Product Range"
      evolution: "Product"
      position: 0.70
      visibility: 0.58
      depends_on: ["Inventory"]
      notes: "Assortment management — mature category with PIM/merchandising tools."
      movement: "none"

    - name: "Returns and Refunds"
      evolution: "Product"
      position: 0.68
      visibility: 0.55
      depends_on: ["Order Management", "Reverse Logistics"]
      notes: "Became a strategic differentiator in e-commerce (free, easy returns) — now commoditising."
      movement: "evolving"

    # --- Channels ---
    - name: "Physical Store"
      evolution: "Product"
      position: 0.72
      visibility: 0.47
      depends_on: ["Payments", "Inventory"]
      notes: "Mature channel; sensory advantage but cost-disadvantaged vs. pure digital."
      movement: "inertia"

    - name: "E-commerce Site"
      evolution: "Commodity"
      position: 0.82
      visibility: 0.45
      depends_on: ["Payments", "Order Management", "Identity"]
      notes: "Commodity layer — Shopify / BigCommerce / commerce-as-a-service."
      movement: "none"

    - name: "Mobile App"
      evolution: "Product"
      position: 0.65
      visibility: 0.43
      depends_on: ["Payments", "Order Management", "Identity"]
      notes: "Platform-standard — many commercial options; bespoke value is in the experience on top."
      movement: "evolving"

    - name: "Telesales"
      evolution: "Commodity"
      position: 0.88
      visibility: 0.42
      depends_on: ["Order Management", "CRM Platform"]
      notes: "Mature, declining channel; call-centre-as-a-service is utility."
      movement: "inertia"

    - name: "Social Commerce"
      evolution: "Custom"
      position: 0.30
      visibility: 0.40
      depends_on: ["Identity"]
      notes: "Livestream + in-feed checkout — fast-evolving, no dominant platform."
      movement: "accelerating"

    - name: "Virtual / AR Channel"
      evolution: "Genesis / Custom"
      position: 0.18
      visibility: 0.38
      depends_on: ["Identity"]
      notes: "AR try-on, virtual stores — experimental, high failure rate, high potential for sensory replication."
      movement: "accelerating"

    # --- Trust, data, societal context ---
    - name: "Trust and Privacy"
      evolution: "Custom"
      position: 0.45
      visibility: 0.52
      depends_on: ["Identity", "Consent Management"]
      notes: "Regulation (GDPR, consumer protection) is pushing standardisation — but trust itself remains custom."
      movement: "evolving"

    - name: "Identity"
      evolution: "Commodity"
      position: 0.80
      visibility: 0.48
      depends_on: ["Data Storage"]
      notes: "Auth0, Cognito, sign-in-with providers — clear utility with network effects."
      movement: "evolving"

    - name: "Consent Management"
      evolution: "Product"
      position: 0.55
      visibility: 0.46
      depends_on: ["Data Storage"]
      notes: "CMP products (OneTrust etc.) — mature enough to buy, not yet utility."
      movement: "evolving"

    - name: "Societal Behaviour and Demographics"
      evolution: "Custom"
      position: 0.28
      visibility: 0.50
      depends_on: []
      notes: "External climatic input — the 'weather' that shapes everything above; not a built component, but required on the map to reason about demographic shifts."
      movement: "none"

    - name: "Personalisation"
      evolution: "Custom"
      position: 0.42
      visibility: 0.44
      depends_on: ["Customer Data Platform", "Societal Behaviour and Demographics"]
      notes: "Primary lever for digital differentiation; moving toward product stage with ML-as-a-service."
      movement: "accelerating"

    - name: "Customer Data Platform"
      evolution: "Product"
      position: 0.48
      visibility: 0.38
      depends_on: ["Data Storage"]
      notes: "Segment, mParticle, Treasure Data — recognised product category, some pressure to commoditise."
      movement: "evolving"

    # --- Fulfilment plumbing ---
    - name: "Order Management"
      evolution: "Commodity"
      position: 0.78
      visibility: 0.32
      depends_on: ["Inventory", "Delivery / Logistics", "Payments"]
      notes: "OMS is a mature category; trending utility."
      movement: "none"

    - name: "Inventory"
      evolution: "Commodity"
      position: 0.85
      visibility: 0.30
      depends_on: ["Data Storage"]
      notes: "Inventory/WMS — utility pricing, multiple interchangeable providers."
      movement: "none"

    - name: "Delivery / Logistics"
      evolution: "Commodity"
      position: 0.80
      visibility: 0.28
      depends_on: ["Networking"]
      notes: "Third-party fulfilment is a utility (3PL, Amazon MCF, DHL APIs)."
      movement: "none"

    - name: "Reverse Logistics"
      evolution: "Product"
      position: 0.60
      visibility: 0.27
      depends_on: ["Delivery / Logistics"]
      notes: "Fast-maturing in retail; returns-as-a-service starting to emerge (Loop, Happy Returns)."
      movement: "evolving"

    - name: "Payments"
      evolution: "Commodity"
      position: 0.90
      visibility: 0.26
      depends_on: ["Networking"]
      notes: "Utility (Stripe, Adyen, open banking rails)."
      movement: "none"

    # --- Infra ---
    - name: "CRM Platform"
      evolution: "Commodity"
      position: 0.78
      visibility: 0.22
      depends_on: ["Data Storage", "Cloud Compute"]
      notes: "Mature category — Salesforce, HubSpot, Dynamics."
      movement: "none"

    - name: "Cloud Compute"
      evolution: "Commodity"
      position: 0.96
      visibility: 0.10
      depends_on: ["Networking"]
      notes: "Utility (AWS / GCP / Azure)."
      movement: "none"

    - name: "Networking"
      evolution: "Commodity"
      position: 0.97
      visibility: 0.08
      depends_on: []
      notes: "Utility internet."
      movement: "none"

    - name: "Data Storage"
      evolution: "Commodity"
      position: 0.95
      visibility: 0.08
      depends_on: ["Cloud Compute"]
      notes: "Object stores, managed databases — utility pricing."
      movement: "none"

  analysis:
    opportunities:
      - "Double down on Retail Experience + Engagement and Discovery + Sensory Experience — these are the only high-visibility, low-evolution clusters left. Differentiation lives here."
      - "Exploit AR / Virtual channel: it is the one genuinely Genesis/Custom channel with a plausible path to reproducing the sensory advantage of Physical Store online."
      - "Productize Returns and Reverse Logistics experience — most retailers treat returns as cost; competitive advantage is available to whoever makes returning as pleasant as buying."
      - "Treat Personalisation as the critical battleground: medium visibility but low evolution means differentiation pressure D(v) is high and the component is accelerating — invest before it productizes."
      - "Use Commodity Leverage on E-commerce Site, Payments, OMS, Inventory, CRM, Logistics, Cloud, Identity — any bespoke work here is technical debt."

    threats:
      - "Amazon-style commoditisation of e-commerce, logistics, and even experience layers is Red Queen pressure — standing still means losing relative ground."
      - "Platform capture: Social Commerce is evolving fast and the retailer does not own the channel (TikTok, Instagram) — disintermediation risk."
      - "Demographic shift (Gen Z / Alpha channel preferences) can bypass mature investments in Physical Store and Telesales if ignored."
      - "Regulation (privacy, consent, dark patterns) is standardising Trust and Privacy from the outside — non-compliance is existential, compliance is table stakes."
      - "Commoditisation of Personalisation via GenAI — the moat is eroding; today's custom is tomorrow's product."

    inertia_points:
      - component: "Physical Store"
        reason: "Large sunk property, staff and leases; skills biased toward bricks-and-mortar operations; customer habit keeps the channel alive even as economics worsen."
      - component: "Telesales"
        reason: "Legacy contact-centre estates and customer demographics (older segments) resist digital-only migration."
      - component: "Brand and Storytelling"
        reason: "Intentionally kept custom as a defence against commoditisation pressure — but over-reliance on it masks under-investment elsewhere."
      - component: "Returns and Refunds"
        reason: "Operationally treated as cost / back-office, not as experience — blocks the move into productized returns-as-a-service."

    climatic_patterns_in_play:
      - "Everything evolves through supply and demand (Sec 1.1): E-commerce, Payments, OMS, Logistics, Identity have all crossed into commodity. Plan accordingly."
      - "Red Queen (Sec 1.4): standing still on Retail Experience is losing ground."
      - "Co-evolution (Sec 1.6): AR/VR hardware maturing will unlock Virtual Channel and Sensory Experience simultaneously."
      - "Higher-order systems (Sec 2.1): the commoditisation of Identity + Payments + Logistics + Cloud is precisely what enables Social Commerce and Livestream as genesis-stage higher-order systems."
      - "Jevons paradox: cheaper commerce infra has driven more commerce, not less — plan capacity for more transactions, not cost savings."

  recommendations:
    immediate:
      - "Run a full audit against the map's Commodity column: any team still building custom E-commerce, Payments, OMS, CRM, Logistics, Identity, or Cloud should be reassigned. This is technical debt, not differentiation."
      - "Elevate Personalisation from a marketing-technology initiative to a strategic, board-sponsored programme — it is the single highest D(v) component on the map."
      - "Create an explicit 'Returns as Experience' product team funded from returns operational budget — flip returns from cost centre to differentiator while it is still Custom."

    short_term:
      - "Stand up a Genesis-stage AR/Virtual Channel exploration with Pioneer-profile talent, ring-fenced from run-the-business metrics."
      - "Adopt a CDP product (do not build) and make it the single source of truth feeding Personalisation; use Settlers-profile talent for this."
      - "Develop a Social Commerce posture — own your storefronts on third-party platforms now, before the channel solidifies and platform economics harden."
      - "Formalise Trust and Privacy with a Consent Management Platform and privacy-by-design principles, expecting regulation to tighten."

    long_term:
      - "Converge the channels into one 'Connected Journey' — customer, identity, order, inventory, data — served by Town Planner-run commodity platforms, so that Pioneer / Settler talent can focus on the still-Custom experience layer."
      - "Treat Sensory Experience as the long-horizon moat: whoever can reproduce touch/smell/spatial presence online wins the next cycle of differentiation."
      - "Watch demographic signals (Societal Behaviour) as input to climatic patterns — use them to time channel retirement (e.g., Physical Store portfolio shrinkage) and new-channel investment."
```

---

## Step 4 — Movement

| Component | Current | Direction | Rationale |
|---|---|---|---|
| Personalisation | Custom (0.42) | `>>` Accelerating → 0.62 | GenAI collapses the cost of personalisation; will hit Product stage soon. |
| Sensory Experience | Genesis (0.22) | `→` Evolving → 0.40 | AR / haptics maturing; patterns beginning to form. |
| Virtual / AR Channel | Genesis (0.18) | `>>` Accelerating → 0.45 | Apple Vision Pro / Quest class devices pushing custom implementations. |
| Social Commerce | Custom (0.30) | `>>` Accelerating → 0.55 | Livestream commerce and in-feed checkout solidifying into product category. |
| Returns and Refunds | Product (0.68) | `→` Evolving → 0.78 | Returns-as-a-service vendors appearing (Loop, Happy Returns). |
| Consent Management | Product (0.55) | `→` Evolving → 0.72 | Regulation is standardising the category. |
| Engagement and Discovery | Custom (0.35) | `→` Evolving → 0.55 | Search + recommendation + content converging into product-stage offerings. |
| Identity | Commodity-ish (0.80) | `→` Further into utility | Passkeys / federated identity push this firmly to utility. |
| Customer Data Platform | Product (0.48) | `→` Evolving → 0.65 | Warehouse-native CDPs driving commoditisation. |
| Physical Store | Product (0.72) | `x` Inertia | Sunk cost and skills retention. |
| Telesales | Commodity (0.88) | `x` Inertia | Legacy customer demographics. |
| Brand and Storytelling | Custom (0.48) | `x` Intentional inertia | Deliberately kept custom as an anti-commoditisation play. |

---

## Step 5 — Analysis Checklist

```yaml
completeness:
  anchor_defined: "Yes — Customer (primary) and Producer (secondary); need statement explicit."
  components_covered: "Yes — 31 components across 7 layers (needs → experience → goods/services → channels → trust/data → fulfilment → infra)."
  dependencies_shown: "Yes — explicit in draft.owm and YAML depends_on lists."
  movement_arrows_present: "Yes — evolution movement recorded in Step 4 table."

positioning:
  market_based: "Yes — positions reflect industry market maturity, not any one retailer's internal capability."
  commodity_on_right: "Yes — Payments, Cloud Compute, Networking, Data Storage, Telesales, Identity, Inventory, Logistics are all >= 0.78."
  genesis_on_left: "Yes — Virtual/AR Channel (0.18), Sensory Experience (0.22), Societal Behaviour (0.28), Need for Belonging (0.30), Social Commerce (0.30) sit in Genesis/early-Custom."

insights:
  inertia_identified: "Physical Store, Telesales, Brand, Returns-as-operational."
  commoditisation_opportunities: "E-commerce site build, payments, OMS, CRM, cloud, logistics, identity — consume, don't build."
  genesis_differentiators: "Virtual/AR Channel, Sensory Experience, Social Commerce — plant flags here."
  technical_debt_signals: "Any bespoke commerce-engine, OMS, or payments code is debt. Any custom ML stack where a CDP + managed vector store suffices is debt."

strategic:
  gameplay_applicable:
    - "Open Approaches (B2, LG) around Identity / Consent — share schemas so the ecosystem commoditises faster."
    - "Exploiting Network Effects (B3, N) on Social Commerce and Loyalty."
    - "Brand and Marketing (A5, N) on Brand and Storytelling — legitimate brand-building to slow experience-layer commoditisation."
    - "Market Enablement (B1, LG) on AR standards to unlock Virtual Channel."
    - "Cooperation (B4, N) on returns-as-a-service consortia."
  climatic_patterns_affecting:
    - "Red Queen on Retail Experience — continuous adaptation mandatory."
    - "Higher-order systems emerging above commodity commerce infra."
    - "Multiple waves of diffusion (Sec 1.7) — Social/AR are pre-chasm for most enterprises."
    - "Jevons paradox — cheaper commerce infra increases total commerce, plan capacity up."
  doctrine_weaknesses:
    - "Single management method across all stages (retailers applying retail-ops rigour to Genesis experiments) — Chapter 1.5 climatic pattern violation."
    - "Town Planner talent staffing Genesis channels (Virtual/AR) — classic handoff mismatch."
    - "No explicit 'focus on user needs' doctrine beyond 'customer' — Need for Belonging is un-owned in most retailers."
```

---

## Step 6 — Quantitative Analysis (Optional)

### Evolution scoring E(c) = (Ubiquity + Certainty) / 2

| Component | U | C | E(c) | Stage | Qualitative pos | Match? |
|---|---|---|---|---|---|---|
| Sensory Experience | 0.15 | 0.30 | 0.23 | Genesis | 0.22 | Yes |
| Virtual / AR Channel | 0.15 | 0.20 | 0.18 | Genesis | 0.18 | Yes |
| Need for Belonging | 0.25 | 0.30 | 0.28 | Custom | 0.30 | Yes |
| Social Commerce | 0.35 | 0.25 | 0.30 | Custom | 0.30 | Yes |
| Engagement and Discovery | 0.40 | 0.30 | 0.35 | Custom | 0.35 | Yes |
| Need for Trust | 0.40 | 0.35 | 0.38 | Custom | 0.38 | Yes |
| Retail Experience | 0.45 | 0.35 | 0.40 | Custom | 0.40 | Yes |
| Personalisation | 0.50 | 0.35 | 0.42 | Custom | 0.42 | Yes |
| Customer Data Platform | 0.55 | 0.40 | 0.48 | Custom → Product | 0.48 | Yes |
| Consent Management | 0.55 | 0.55 | 0.55 | Product | 0.55 | Yes |
| Services | 0.60 | 0.50 | 0.55 | Product | 0.55 | Yes |
| Returns and Refunds | 0.65 | 0.70 | 0.68 | Product | 0.68 | Yes |
| Product Range | 0.70 | 0.70 | 0.70 | Product | 0.70 | Yes |
| Physical Store | 0.75 | 0.70 | 0.73 | Product | 0.72 | Yes |
| Mobile App | 0.70 | 0.60 | 0.65 | Product | 0.65 | Yes |
| Order Management | 0.80 | 0.75 | 0.78 | Commodity | 0.78 | Yes |
| CRM Platform | 0.80 | 0.75 | 0.78 | Commodity | 0.78 | Yes |
| Identity | 0.80 | 0.80 | 0.80 | Commodity | 0.80 | Yes |
| Delivery / Logistics | 0.80 | 0.80 | 0.80 | Commodity | 0.80 | Yes |
| Goods | 0.85 | 0.80 | 0.82 | Commodity | 0.82 | Yes |
| E-commerce Site | 0.85 | 0.80 | 0.82 | Commodity | 0.82 | Yes |
| Inventory | 0.90 | 0.80 | 0.85 | Commodity | 0.85 | Yes |
| Telesales | 0.90 | 0.85 | 0.88 | Commodity | 0.88 | Yes |
| Payments | 0.95 | 0.85 | 0.90 | Commodity | 0.90 | Yes |
| Data Storage | 0.95 | 0.95 | 0.95 | Commodity | 0.95 | Yes |
| Cloud Compute | 0.95 | 0.95 | 0.95 | Commodity | 0.96 | Yes |
| Networking | 0.95 | 0.95 | 0.95 | Commodity | 0.97 | Yes |

### Decision metrics — selected components

D(v) = visibility × (1 − evolution); K(v) = (1 − visibility) × evolution

| Component | Vis | Evol | D(v) | K(v) | Verdict |
|---|---|---|---|---|---|
| Retail Experience | 0.76 | 0.40 | **0.46** | 0.14 | Invest — differentiator |
| Engagement and Discovery | 0.73 | 0.35 | **0.47** | 0.09 | Invest — differentiator |
| Sensory Experience | 0.70 | 0.22 | **0.55** | 0.07 | High differentiation pressure |
| Brand and Storytelling | 0.72 | 0.48 | **0.37** | 0.13 | Invest — experience moat |
| Personalisation | 0.44 | 0.42 | 0.26 | 0.24 | Targeted invest — moat eroding |
| Need for Trust | 0.85 | 0.38 | **0.53** | 0.06 | High differentiation pressure |
| E-commerce Site | 0.45 | 0.82 | 0.08 | **0.45** | Outsource |
| Payments | 0.26 | 0.90 | 0.03 | **0.67** | Consume as utility |
| Cloud Compute | 0.10 | 0.96 | 0.00 | **0.86** | Consume as utility |
| Order Management | 0.32 | 0.78 | 0.07 | **0.53** | Outsource / buy |
| Physical Store | 0.47 | 0.72 | 0.13 | **0.38** | Buy / rationalise estate |
| Virtual / AR Channel | 0.38 | 0.18 | **0.31** | 0.11 | Genesis invest |

### Dependency risk — highest-risk edges

R(a,b) = visibility(a) × (1 − evolution(b))

| Visible component (a) | Depends on (b) | R(a,b) | Note |
|---|---|---|---|
| Retail Experience (0.76) | Personalisation (0.42) | 0.44 | Moderate — personalisation is the long pole. |
| Retail Experience (0.76) | Sensory Experience (0.22) | **0.59** | High — user-visible Retail Experience leans on genesis-stage sensory tech. |
| Need for Trust (0.85) | Trust and Privacy (0.45) | **0.47** | Moderate-high — central to the anchor, still custom. |
| Engagement and Discovery (0.73) | Personalisation (0.42) | 0.42 | Moderate. |
| Need for Belonging (0.84) | Engagement and Discovery (0.35) | **0.55** | Moderate-high — belonging relies on an immature experience layer. |
| Customer (0.95) | Need for Trust (0.38) | **0.59** | High — the anchor's key need is not yet mature. |

### Interpretation

The numbers confirm the qualitative story:

1. **Where it's still custom** — the entire experience layer (Retail Experience, Engagement and Discovery, Sensory Experience, Personalisation, Brand, Need for Trust, Need for Belonging, Social Commerce, Virtual / AR) sits with D(v) > 0.30. That is the differentiation zone, and it is the only part of the map where custom investment is justified.
2. **Where it's hardened into commodity** — everything from E-commerce site downward (Payments, OMS, Inventory, Logistics, CRM, Identity, Cloud, Networking, Storage) has K(v) > 0.40. Custom builds here are technical debt.
3. **The crossover** — Returns, Consent Management, Mobile App, CDP are in the middle — legitimate buy-or-build, not-sure decisions, moving rightward.

**What that implies for differentiation:**

> The retail moat has migrated upward. The commerce engine has become plumbing. Differentiation now sits entirely in the experience-and-trust layer (how the customer feels, is seen, is understood, is connected to the brand) and in the two genesis-stage channels (Virtual/AR and Social Commerce) that are reproducing sensory and belonging needs online. Retailers who keep investing custom effort in commerce infrastructure are burning money that should be going to experience, trust, returns-as-experience, and AR pioneering. Retailers who commoditise their plumbing and pour the freed capacity into the top-left of the map (high visibility, low evolution) are the ones building durable advantage.
