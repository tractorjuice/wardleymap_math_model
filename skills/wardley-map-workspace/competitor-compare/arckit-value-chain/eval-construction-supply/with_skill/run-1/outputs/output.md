# Value Chain: UK Construction Supply Chain (March 2023)

Produced with `arckit-wardley.value-chain` (partial-map skill — value-chain decomposition only; evolution ε fixed at 0.50 placeholder).

## Executive Summary

- **Anchor**: A household occupies a safe, compliant home.
- **Components**: 22 (1 anchor + 21 dependencies) across 7 visibility levels.
- **Strategic insights**:
  1. Two parallel construction modes — *bespoke site construction* and *modular/prefab assembly* — sit side-by-side at the same visibility level, signalling the central strategic question: which capabilities are ready to industrialise.
  2. Labour certification & training is a chokepoint: both skilled and unskilled labour depend on it, and it is a recognised CNI concern for local supply.
  3. International material supply and energy & fuel sit at the deepest infrastructure level — post-2022 energy shock and post-Brexit import friction make these material risk factors for the chain above.
  4. Building regulations feed both planning and inspection: a shared constraint rather than a component to be built or bought.

## Users and Personas

| User | Primary need |
|------|--------------|
| Private homebuyer | Purchase a habitable, mortgage-eligible home |
| Social tenant | Allocated a safe, compliant dwelling |
| Government (national / local) | Deliver housing targets; maintain CNI resilience |
| Mortgage lender | Lend against compliant, insurable assets |
| Building inspector / QA body | Certify conformance with Building Regulations |

## Step 2 — Anchor

```text
Anchor:  Household occupies a safe, compliant home
User:    Citizens (private owners, social tenants), acting via government / landlord / lender intermediaries
Outcome: A habitable dwelling that meets Building Regulations, handed over on schedule and financeable
```

Passes the anchor test: multiple valid delivery modes satisfy this need (new-build site construction, modular/prefab, refurb, social housing programme).

## Step 3–5 — Decomposition, Dependencies, Visibility

### Component Inventory

| # | Component | Visibility | Role |
|---|-----------|-----------:|------|
| A | Safe Compliant Home | 0.97 | Anchor — household outcome |
| 1 | Home Purchase / Tenancy | 0.90 | Acquisition transaction |
| 2 | Completed Dwelling Handover | 0.88 | Physical delivery event |
| 3 | Mortgage & Finance | 0.82 | Funding for purchase |
| 4 | Building Inspection & Certification | 0.80 | QA / sign-off |
| 5 | Construction Delivery | 0.72 | End-to-end build programme |
| 6 | Planning Permission | 0.68 | Consent layer |
| 7 | Bespoke Site Construction | 0.62 | Traditional craft mode |
| 8 | Modular / Prefab Assembly | 0.58 | Industrialised mode (inc. factory-mode, test-driven) |
| 9 | Blueprints & Design | 0.55 | Architectural / engineering design |
| 10 | Building Regulations | 0.50 | Shared regulatory constraint |
| 11 | Skilled Labour | 0.48 | Certified trades |
| 12 | Unskilled Labour | 0.45 | General site operatives |
| 13 | Factory Manufacture of Components | 0.42 | Prefab panels, pods, MMC |
| 14 | Equipment & Machinery | 0.40 | Plant hire, tools |
| 15 | Labour Certification & Training | 0.35 | CSCS, apprenticeships, NVQs |
| 16 | Building Materials Distribution | 0.32 | Merchants (traditional, integrated, platform) |
| 17 | Recycled & Novel Materials | 0.25 | CLT, recycled aggregate, substitutables |
| 18 | Raw Building Materials | 0.20 | Cement, steel, aggregate, timber |
| 19 | Logistics & Transport | 0.15 | Road/rail/port movement |
| 20 | International Material Supply Chain | 0.10 | Imports, overseas production |
| 21 | Energy & Fuel | 0.06 | Deep commodity infrastructure |

### Dependency Matrix (direct only)

Dependencies flow downward (higher visibility -> lower visibility). Visibility ordering ν(a) >= ν(b) holds on every edge.

| From | -> | To |
|------|----|----|
| Safe Compliant Home | -> | Home Purchase, Handover, Inspection |
| Home Purchase | -> | Mortgage & Finance |
| Handover | -> | Construction Delivery, Inspection |
| Inspection | -> | Building Regulations |
| Construction Delivery | -> | Planning, Bespoke, Modular, Blueprints |
| Planning Permission | -> | Building Regulations |
| Bespoke Site Construction | -> | Skilled Labour, Unskilled Labour, Equipment, Distribution |
| Modular / Prefab | -> | Factory Manufacture, Blueprints, Skilled Labour |
| Factory Manufacture | -> | Distribution, Equipment |
| Skilled Labour | -> | Certification & Training |
| Unskilled Labour | -> | Certification & Training |
| Distribution | -> | Raw Materials, Recycled/Novel, Logistics |
| Recycled / Novel | -> | Raw Materials |
| Raw Materials | -> | International Supply Chain |
| Logistics | -> | Energy & Fuel |
| Equipment & Machinery | -> | Energy & Fuel |
| International Supply | -> | Energy & Fuel |

### Critical Path (anchor to deepest infrastructure)

```
Safe Compliant Home
  -> Completed Dwelling Handover
    -> Construction Delivery
      -> Bespoke Site Construction
        -> Building Materials Distribution
          -> Raw Building Materials
            -> International Material Supply Chain
              -> Energy & Fuel
```

Single points of failure:
- **Labour Certification & Training** (both labour categories depend on it).
- **Building Materials Distribution** (shared by bespoke site, factory, and recycled-material routes).
- **Energy & Fuel** (depended on by logistics, equipment, and the international chain — 2022 energy shock is the quantitative signal).

Resilience gaps:
- No local substitute for *International Material Supply Chain* if imports disrupted (e.g. post-Brexit friction, 2022 timber/steel price spikes).
- Training pipeline is slow-moving; labour shortages in skilled trades cannot be resolved within a construction programme cycle.

## Step 6 — Validation Checklist

**Completeness**
- [x] Anchor is a genuine user need (safe compliant home), not a solution.
- [x] Dependencies span demand side, delivery, QA, labour, materials, logistics, regulation.
- [x] Chain reaches commodity level (Energy & Fuel, International Material Supply Chain).
- [x] No orphan components; every non-anchor component has >= 1 dependency.
- [x] All components are capabilities/activities, not people or organisations (e.g. *Building Inspection & Certification*, not "building inspectors").

**Accuracy**
- [x] Visibility ordering is consistent with dependency direction on every edge.
- [x] No component is simultaneously user-facing and deep infrastructure.
- [x] Bespoke and modular modes are parallel (neither dominates), reflecting March 2023 reality.

**Usefulness**
- [x] Granularity supports strategic decisions on industrialisation.
- [x] Every component can plausibly take an evolution position in a follow-on mapping step.
- [x] Chain reveals at least three strategic insights (labour bottleneck, materials chokepoint, regulation as shared constraint).

## OWM Output

```wardley
title Construction Supply Chain (March 2023)

anchor Safe Compliant Home [0.97, 0.50]

component Home Purchase / Tenancy [0.90, 0.50]
component Completed Dwelling Handover [0.88, 0.50]
component Mortgage & Finance [0.82, 0.50]
component Building Inspection & Certification [0.80, 0.50]
component Construction Delivery [0.72, 0.50]
component Planning Permission [0.68, 0.50]
component Bespoke Site Construction [0.62, 0.50]
component Modular / Prefab Assembly [0.58, 0.50]
component Blueprints & Design [0.55, 0.50]
component Building Regulations [0.50, 0.50]
component Skilled Labour [0.48, 0.50]
component Unskilled Labour [0.45, 0.50]
component Factory Manufacture of Components [0.42, 0.50]
component Equipment & Machinery [0.40, 0.50]
component Labour Certification & Training [0.35, 0.50]
component Building Materials Distribution [0.32, 0.50]
component Recycled & Novel Materials [0.25, 0.50]
component Raw Building Materials [0.20, 0.50]
component Logistics & Transport [0.15, 0.50]
component International Material Supply Chain [0.10, 0.50]
component Energy & Fuel [0.06, 0.50]

Safe Compliant Home -> Home Purchase / Tenancy
Safe Compliant Home -> Completed Dwelling Handover
Safe Compliant Home -> Building Inspection & Certification
Home Purchase / Tenancy -> Mortgage & Finance
Completed Dwelling Handover -> Construction Delivery
Completed Dwelling Handover -> Building Inspection & Certification
Building Inspection & Certification -> Building Regulations
Construction Delivery -> Planning Permission
Construction Delivery -> Bespoke Site Construction
Construction Delivery -> Modular / Prefab Assembly
Construction Delivery -> Blueprints & Design
Planning Permission -> Building Regulations
Bespoke Site Construction -> Skilled Labour
Bespoke Site Construction -> Unskilled Labour
Bespoke Site Construction -> Equipment & Machinery
Bespoke Site Construction -> Building Materials Distribution
Modular / Prefab Assembly -> Factory Manufacture of Components
Modular / Prefab Assembly -> Blueprints & Design
Modular / Prefab Assembly -> Skilled Labour
Factory Manufacture of Components -> Building Materials Distribution
Factory Manufacture of Components -> Equipment & Machinery
Skilled Labour -> Labour Certification & Training
Unskilled Labour -> Labour Certification & Training
Building Materials Distribution -> Raw Building Materials
Building Materials Distribution -> Recycled & Novel Materials
Building Materials Distribution -> Logistics & Transport
Raw Building Materials -> International Material Supply Chain
Recycled & Novel Materials -> Raw Building Materials
Logistics & Transport -> Energy & Fuel
Equipment & Machinery -> Energy & Fuel
International Material Supply Chain -> Energy & Fuel

style wardley
```

## Visibility Assessment

| Component | Visibility | Rationale |
|-----------|-----------:|-----------|
| Safe Compliant Home | 0.97 | Anchor — the end outcome |
| Home Purchase / Tenancy | 0.90 | Direct transaction the household engages in |
| Completed Dwelling Handover | 0.88 | Visible event, keys, snagging |
| Mortgage & Finance | 0.82 | Visible product, not the home itself |
| Building Inspection & Certification | 0.80 | Visible via completion certificate / warranty |
| Construction Delivery | 0.72 | Observable as "the site" but not interacted with daily |
| Planning Permission | 0.68 | Public but abstract to end household |
| Bespoke Site Construction | 0.62 | Trade activity one step below delivery |
| Modular / Prefab Assembly | 0.58 | Parallel delivery mode |
| Blueprints & Design | 0.55 | Design artefacts, one step removed |
| Building Regulations | 0.50 | Shared constraint layer |
| Skilled Labour | 0.48 | Craft activity on site / in factory |
| Unskilled Labour | 0.45 | Site activity beneath skilled trades |
| Factory Manufacture of Components | 0.42 | Off-site industrial activity |
| Equipment & Machinery | 0.40 | Supporting plant |
| Labour Certification & Training | 0.35 | Upstream pipeline |
| Building Materials Distribution | 0.32 | Merchant layer (traditional / integrated / platform) |
| Recycled & Novel Materials | 0.25 | Specialist material stream |
| Raw Building Materials | 0.20 | Upstream commodity inputs |
| Logistics & Transport | 0.15 | Deep operational layer |
| International Material Supply Chain | 0.10 | Invisible to household yet systemically critical |
| Energy & Fuel | 0.06 | Deepest commodity dependency |

## Assumptions and Open Questions

- UK-centric (Building Regulations, social-housing framing, CSCS/NVQ training references) consistent with March 2023 context.
- *Distributors* (traditional, integrated, platform) collapsed into one component — a subsequent map can separate them to analyse the platform threat to traditional merchants.
- *Mortgage lenders* shown as a capability (Mortgage & Finance) rather than an actor, per the skill's "capabilities not actors" rule.
- Handover is treated as a discrete step distinct from Construction Delivery to capture snagging / warranty / QA-linked risk.
- Evolution axis left at ε=0.50 placeholder (partial-map skill); the follow-on `arckit-wardley` command would place each component on the evolution axis — for example, `Mortgage & Finance` is commodity while `Modular / Prefab Assembly` is custom-built / early product in March 2023.

## Potential Issues / Next Steps

- Next step: run an evolution-axis positioning pass. Expected separation: bespoke craft (custom-built) vs factory manufacture (product/commodity) will reveal the industrialisation frontier the scenario asks about.
- Consider splitting Building Materials Distribution into `Traditional Merchant`, `Integrated Merchant`, `Platform Distributor` for a merchant-channel strategy map.
- Consider adding `Critical National Infrastructure Oversight` as a parallel constraint to Building Regulations if the CNI angle is pursued further.
