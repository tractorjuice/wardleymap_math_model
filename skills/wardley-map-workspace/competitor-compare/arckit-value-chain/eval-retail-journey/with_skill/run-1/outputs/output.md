# Wardley Value Chain — Connected Retail Customer Journey

**Document ID**: ARC-RETAIL-WVCH-001-v1.0
**Date**: 2026-04-23
**Document Type**: Wardley Value Chain
**Command**: arckit.wardley.value-chain
**Project**: Connected Retail Customer Journey
**Classification**: PUBLIC

> **Note**: This output is a **partial map** — the `$arckit-wardley.value-chain`
> skill produces Y-axis (visibility) decomposition only. Evolution positions
> are deliberately held at a placeholder ε = 0.50 for every component; the
> downstream `$arckit-wardley` command assigns evolution. The scenario's
> request for "where the retail experience is still custom and where it's
> hardened into commodity" is therefore addressed qualitatively in the
> critical-path analysis rather than through X-axis positions.

---

## 1. Executive Summary

**Anchor**: *"Customer can meet their retail need through a connected,
trusted, multi-channel journey."* A secondary anchor (Producer) sits
alongside, representing the supply-side party that places goods and
services into the chain.

18 components were identified across roughly six visibility levels, from
the directly-experienced **Shopping Experience** down to commodity
**Cloud Hosting**. Three strategic observations fall out of the
decomposition:

1. The experience layer (engagement & discovery, sensory/physical-virtual,
   returns, trust & privacy) is the main site of differentiation — it is
   the broad band of capabilities sitting just below the customer need
   and fans out into multiple channels.
2. The channel layer (store, e-commerce, telesales) is a convergence
   point: three distinct delivery modes feed the same Order Management
   capability below them, which is a candidate for commodity-isation.
3. Below Order Management the chain is almost entirely commodity
   infrastructure (payment rails, fulfilment/logistics, identity, data
   platform, cloud), none of which should be a source of retail
   differentiation.

## 2. Users and Personas

| User | Primary need |
|---|---|
| Customer (consumer) | Meet a retail need (discover, evaluate, buy, return goods/services) through a trusted, convenient channel of their choice. |
| Producer (supplier) | Place goods and services into a channel where they reach the right customers at the right time. |

## 3. Value Chain Diagram

### ASCII sketch (Y-axis = visibility)

```
   1.00  Customer ◆        Producer ◆
         │                 │
   0.92  Retail Need Fulfilment
         │
   0.85  Shopping Experience
         │ ├─────────────┬─────────────┬────────────────┐
   0.82  │              Goods and Services Offering
   0.75  Engagement & Discovery
   0.72  Sensory / Physical-Virtual Experience
   0.68  Returns Handling
   0.64  Trust and Privacy
         │
   0.60  Channel Delivery
         │ ├────────────────┬────────────────┐
   0.55  Physical Store    E-commerce        Telesales
         │
   0.50  Societal and Demographic Insight
   0.40  Customer Identity
   0.38  Order Management
   0.28  Fulfilment and Logistics
   0.22  Payment Processing
   0.18  Data and Analytics Platform
   0.08  Cloud Hosting
```

### OWM syntax (paste into https://create.wardleymaps.ai)

```owm
title Connected Retail Customer Journey — Value Chain

anchor Customer [0.98, 0.50]
anchor Producer [0.95, 0.50]

component Retail Need Fulfilment [0.92, 0.50]
component Shopping Experience [0.85, 0.50]
component Goods and Services Offering [0.82, 0.50]
component Engagement and Discovery [0.75, 0.50]
component Sensory and Physical-Virtual Experience [0.72, 0.50]
component Returns Handling [0.68, 0.50]
component Trust and Privacy [0.64, 0.50]
component Channel Delivery [0.60, 0.50]
component Physical Store [0.55, 0.50]
component E-commerce Storefront [0.55, 0.50]
component Telesales [0.55, 0.50]
component Societal and Demographic Insight [0.50, 0.50]
component Customer Identity [0.40, 0.50]
component Order Management [0.38, 0.50]
component Fulfilment and Logistics [0.28, 0.50]
component Payment Processing [0.22, 0.50]
component Data and Analytics Platform [0.18, 0.50]
component Cloud Hosting [0.08, 0.50]

Customer -> Retail Need Fulfilment
Producer -> Goods and Services Offering
Retail Need Fulfilment -> Shopping Experience
Retail Need Fulfilment -> Goods and Services Offering
Shopping Experience -> Engagement and Discovery
Shopping Experience -> Sensory and Physical-Virtual Experience
Shopping Experience -> Returns Handling
Shopping Experience -> Trust and Privacy
Goods and Services Offering -> Channel Delivery
Engagement and Discovery -> Channel Delivery
Engagement and Discovery -> Societal and Demographic Insight
Sensory and Physical-Virtual Experience -> Channel Delivery
Returns Handling -> Fulfilment and Logistics
Returns Handling -> Order Management
Trust and Privacy -> Customer Identity
Channel Delivery -> Physical Store
Channel Delivery -> E-commerce Storefront
Channel Delivery -> Telesales
Physical Store -> Order Management
E-commerce Storefront -> Order Management
E-commerce Storefront -> Customer Identity
Telesales -> Order Management
Societal and Demographic Insight -> Data and Analytics Platform
Customer Identity -> Data and Analytics Platform
Order Management -> Payment Processing
Order Management -> Fulfilment and Logistics
Payment Processing -> Cloud Hosting
Fulfilment and Logistics -> Cloud Hosting
Data and Analytics Platform -> Cloud Hosting
Customer Identity -> Cloud Hosting

style wardley
```

<details>
<summary>Mermaid <code>wardley-beta</code> equivalent</summary>

```mermaid
wardley-beta
title Connected Retail Customer Journey — Value Chain
size [1100, 800]

anchor Customer [0.98, 0.50]
anchor Producer [0.95, 0.50]

component "Retail Need Fulfilment" [0.92, 0.50]
component "Shopping Experience" [0.85, 0.50]
component "Goods and Services Offering" [0.82, 0.50]
component "Engagement and Discovery" [0.75, 0.50]
component "Sensory and Physical-Virtual Experience" [0.72, 0.50]
component "Returns Handling" [0.68, 0.50]
component "Trust and Privacy" [0.64, 0.50]
component "Channel Delivery" [0.60, 0.50]
component "Physical Store" [0.55, 0.50]
component "E-commerce Storefront" [0.55, 0.50]
component Telesales [0.55, 0.50]
component "Societal and Demographic Insight" [0.50, 0.50]
component "Customer Identity" [0.40, 0.50]
component "Order Management" [0.38, 0.50]
component "Fulfilment and Logistics" [0.28, 0.50]
component "Payment Processing" [0.22, 0.50]
component "Data and Analytics Platform" [0.18, 0.50]
component "Cloud Hosting" [0.08, 0.50]

Customer -> "Retail Need Fulfilment"
Producer -> "Goods and Services Offering"
"Retail Need Fulfilment" -> "Shopping Experience"
"Retail Need Fulfilment" -> "Goods and Services Offering"
"Shopping Experience" -> "Engagement and Discovery"
"Shopping Experience" -> "Sensory and Physical-Virtual Experience"
"Shopping Experience" -> "Returns Handling"
"Shopping Experience" -> "Trust and Privacy"
"Goods and Services Offering" -> "Channel Delivery"
"Engagement and Discovery" -> "Channel Delivery"
"Engagement and Discovery" -> "Societal and Demographic Insight"
"Sensory and Physical-Virtual Experience" -> "Channel Delivery"
"Returns Handling" -> "Fulfilment and Logistics"
"Returns Handling" -> "Order Management"
"Trust and Privacy" -> "Customer Identity"
"Channel Delivery" -> "Physical Store"
"Channel Delivery" -> "E-commerce Storefront"
"Channel Delivery" -> Telesales
"Physical Store" -> "Order Management"
"E-commerce Storefront" -> "Order Management"
"E-commerce Storefront" -> "Customer Identity"
Telesales -> "Order Management"
"Societal and Demographic Insight" -> "Data and Analytics Platform"
"Customer Identity" -> "Data and Analytics Platform"
"Order Management" -> "Payment Processing"
"Order Management" -> "Fulfilment and Logistics"
"Payment Processing" -> "Cloud Hosting"
"Fulfilment and Logistics" -> "Cloud Hosting"
"Data and Analytics Platform" -> "Cloud Hosting"
"Customer Identity" -> "Cloud Hosting"
```

</details>

## 4. Component Inventory

| # | Component | Visibility | Description | Dependencies (down) |
|---|---|---|---|---|
| 1 | Customer | 0.98 | Anchor user with a retail need. | Retail Need Fulfilment |
| 2 | Producer | 0.95 | Supplier anchor placing goods into the chain. | Goods and Services Offering |
| 3 | Retail Need Fulfilment | 0.92 | Overall capability of meeting the customer's retail need end-to-end. | Shopping Experience, Goods and Services Offering |
| 4 | Shopping Experience | 0.85 | Composite experience layer sitting on top of the channels. | Engagement & Discovery, Sensory/Physical-Virtual, Returns Handling, Trust & Privacy |
| 5 | Goods and Services Offering | 0.82 | The assortment of products and services being offered for purchase. | Channel Delivery |
| 6 | Engagement and Discovery | 0.75 | How customers find, browse, and are marketed to. | Channel Delivery, Societal & Demographic Insight |
| 7 | Sensory and Physical-Virtual Experience | 0.72 | The sight/touch/sound dimension of shopping across physical and virtual spaces. | Channel Delivery |
| 8 | Returns Handling | 0.68 | Post-purchase return, refund, and exchange capability. | Fulfilment and Logistics, Order Management |
| 9 | Trust and Privacy | 0.64 | Practices that give the customer confidence (data handling, security cues, review trust). | Customer Identity |
| 10 | Channel Delivery | 0.60 | Umbrella capability coordinating the multi-channel mix. | Physical Store, E-commerce Storefront, Telesales |
| 11 | Physical Store | 0.55 | Bricks-and-mortar channel. | Order Management |
| 12 | E-commerce Storefront | 0.55 | Web/app digital sales channel. | Order Management, Customer Identity |
| 13 | Telesales | 0.55 | Voice/phone-assisted sales channel. | Order Management |
| 14 | Societal and Demographic Insight | 0.50 | Understanding of segment behaviour, demographics, cultural trends. | Data and Analytics Platform |
| 15 | Customer Identity | 0.40 | Identification, authentication, and profile management. | Data and Analytics Platform, Cloud Hosting |
| 16 | Order Management | 0.38 | Order capture, state tracking, orchestration across channels. | Payment Processing, Fulfilment and Logistics |
| 17 | Fulfilment and Logistics | 0.28 | Picking, shipping, delivery, returns logistics. | Cloud Hosting |
| 18 | Payment Processing | 0.22 | Authorising and settling payment. | Cloud Hosting |
| 19 | Data and Analytics Platform | 0.18 | Storage and analysis of behavioural and transactional data. | Cloud Hosting |
| 20 | Cloud Hosting | 0.08 | Commodity compute, storage, and network. | (terminal) |

## 5. Dependency Matrix (direct X, indirect I)

Rows depend on columns. Abbreviated for readability (only the most
load-bearing relationships shown; all X marks match the OWM edge list).

|  | ShopExp | Goods | Eng&Disc | Sens | Ret | Trust | Chan | Store | Ecom | Tele | Soc | Id | Order | Fulfil | Pay | Data | Cloud |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Customer | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I |
| Retail Need | X | X | I | I | I | I | I | I | I | I | I | I | I | I | I | I | I |
| Shop Experience | — | — | X | X | X | X | I | I | I | I | I | I | I | I | I | I | I |
| Goods & Services | — | — | — | — | — | — | X | I | I | I | — | — | I | I | I | — | I |
| Eng & Discovery | — | — | — | — | — | — | X | I | I | I | X | — | I | I | I | I | I |
| Channel Delivery | — | — | — | — | — | — | — | X | X | X | — | — | I | I | I | — | I |
| Order Management | — | — | — | — | — | — | — | — | — | — | — | — | — | X | X | — | I |

## 6. Critical Path Analysis

**Primary critical path** (anchor → deepest commodity):

```
Customer → Retail Need Fulfilment → Shopping Experience →
Engagement and Discovery → Channel Delivery → E-commerce Storefront →
Order Management → Payment Processing → Cloud Hosting
```

**Bottlenecks and single points of failure**:

- **Order Management** is a convergence bottleneck: all three channels
  funnel into it, and it controls both Payment Processing and
  Fulfilment and Logistics. Any degradation here breaks the entire
  customer-facing chain regardless of channel.
- **Cloud Hosting** is the universal terminal commodity; four
  mid-chain components depend on it directly. Resilience there is a
  table-stakes requirement.
- **Customer Identity** is a second convergence point — both the
  E-commerce Storefront and the Trust & Privacy layer depend on it —
  making it a high-value-high-risk component.

**Resilience gaps**:

- Telesales and Physical Store both depend on Order Management but
  *not* directly on Customer Identity; offline-capable identity
  fallback is implicit in the current chain but not an explicit
  component.
- Returns Handling goes through both Fulfilment/Logistics and Order
  Management but does not currently have a dedicated reverse-logistics
  analytics loop back to Data and Analytics Platform. That could be a
  follow-on refinement.

**Where the experience is custom vs commodity** (qualitative, since
this skill does not set X-axis):

- **Still custom / differentiating** (top of chain): Shopping
  Experience, Engagement and Discovery, Sensory & Physical-Virtual
  Experience, Trust and Privacy, and the specific Goods and Services
  Offering. These are where brand and differentiation live.
- **Hardened into commodity** (bottom of chain): Payment Processing,
  Cloud Hosting, most of Fulfilment and Logistics, Customer Identity
  (as a utility capability), and the Data and Analytics Platform as a
  commodity substrate.
- **Transitioning** (middle of chain): E-commerce Storefront,
  Order Management, Societal and Demographic Insight — these are
  widely available as products/rental in 2026 but retailers still
  often build custom versions.

The downstream `$arckit-wardley` step is where these X-axis positions
would be assigned formally.

## 7. Validation Checklist

**Completeness**:

- [x] Chain starts with a genuine user need ("meet a retail need"), not a solution.
- [x] All significant dependencies between components are captured.
- [x] Chain reaches commodity level (Cloud Hosting, Payment Processing).
- [x] No orphan components — every component has at least one connection.
- [x] All components are capabilities/activities, not people or teams.

**Accuracy**:

- [x] Dependencies reflect real-world technical and operational relationships.
- [x] Visibility ordering consistent with dependency direction (parents ≥ children for all edges).
- [x] No component is both a user-facing capability and a deep commodity.

**Usefulness**:

- [x] Granularity is appropriate for strategic decision making (18 components, 6 visibility levels).
- [x] Each component can be meaningfully positioned on the evolution axis in the follow-on map.
- [x] Chain reveals strategic insights about differentiation (experience layer) vs commodity (below Order Management).

**Mathematical validation (per wardleymap_math_model)**:

- [x] DAG acyclicity — no cycles (manually traced).
- [x] Visibility ordering — ν(src) ≥ ν(tgt) for every edge.
- [x] Anchor constraint — Customer (0.98) and Producer (0.95) both ≥ 0.90.

## 8. Visibility Assessment

| Component | Visibility | Rationale |
|---|---|---|
| Customer / Producer | 0.98 / 0.95 | Anchors. Customer is the end user; Producer is a secondary supplier anchor explicitly called out by the scenario. |
| Retail Need Fulfilment | 0.92 | Direct expression of the customer need — one level below the anchor. |
| Shopping Experience | 0.85 | The layer the customer *feels* — failure here is immediately obvious. |
| Goods and Services Offering | 0.82 | Directly visible as "what's for sale" but slightly below experience, because the assortment exists independently of how it is presented. |
| Engagement & Discovery | 0.75 | Noticed when absent (empty store, stale recommendations) but one step removed from the core transaction. |
| Sensory / Physical-Virtual | 0.72 | Strongly felt but usually only noticed when degraded. |
| Returns Handling | 0.68 | Visible only when used, but failure is highly conspicuous when it happens. |
| Trust and Privacy | 0.64 | Hidden until a signal (cookie banner, breach, review) surfaces it. |
| Channel Delivery | 0.60 | The umbrella capability — partially visible via channel choice. |
| Physical Store / E-commerce / Telesales | 0.55 | Named channels the customer can pick. |
| Societal & Demographic Insight | 0.50 | Invisible to the individual customer but shapes almost everything above. |
| Customer Identity | 0.40 | Essential but largely hidden behind login/KYC flows. |
| Order Management | 0.38 | Hidden from the customer but central to operations. |
| Fulfilment and Logistics | 0.28 | Invisible except at the doorstep (or at returns). |
| Payment Processing | 0.22 | Commodity infrastructure, invisible apart from the checkout moment. |
| Data and Analytics Platform | 0.18 | Entirely back-office. |
| Cloud Hosting | 0.08 | Deepest commodity; the customer has no awareness. |

## 9. Assumptions and Open Questions

**Assumptions**:

1. "Customer" is a single consumer persona rather than a B2B buyer;
   B2B would change the weighting of Telesales and potentially add a
   contracts/quoting layer.
2. "Producer" is modelled as a secondary anchor to honour the
   scenario's phrasing; in a strict one-anchor formulation Producer
   could instead be modelled as an upstream component feeding the
   Goods and Services Offering.
3. The three channel types (store, e-commerce, telesales) are the
   ones explicitly listed in the scenario. A real modern retailer
   would likely also include marketplace, social commerce, and live
   commerce channels — these can be added without structural change.
4. Evolution positions are held at the skill-mandated ε = 0.50
   placeholder. The real strategic question ("where is it custom vs
   commodity?") is addressed qualitatively in §6 and should be made
   formal by running `$arckit-wardley`.

**Open questions for the user / follow-on step**:

- Should Producer be promoted to a co-equal anchor or demoted to an
  internal component?
- Which geography is the chain drawn for? Societal/demographic
  influence varies sharply, and the evolution position of several
  components (especially telesales and physical store) is
  geography-dependent.
- Is there a loyalty/identity tier that should be separated out from
  Customer Identity (CRM/loyalty often sits between identity and the
  experience layer)?

---

### Next Steps

- Run `$arckit-wardley` to assign evolution positions and produce the
  full 2-axis Wardley Map.
- Optionally run `$arckit-wardley.doctrine` to assess doctrinal
  maturity for executing differentiation in the experience layer.
- Validate the chain with a retail operations stakeholder before
  committing to it strategically.

---

**Generated by**: ArcKit `$arckit-wardley.value-chain` (competitor-benchmark run)
**Generated on**: 2026-04-23 GMT
**Project**: Connected Retail Customer Journey
**Generation Context**: Scenario prompt only — no external REQ/STKE/PRIN documents provided.
