# Wardley Value Chain — Defence Grey Zone

**Document ID:** ARC-001-WVCH-001-v1.0
**Date:** 2026-04-23
**Command:** `arckit-wardley.value-chain`
**Classification:** PUBLIC
**Status:** Partial map — value chain only (evolution axis is a placeholder ε=0.50 across all components; a subsequent `$arckit-wardley` run is required to position components on the evolution axis and produce a strategically actionable map).

---

## 1. Executive Summary

**Anchor:** A state maintains its sovereignty under contested below-threshold competition.

This value chain decomposes the defence grey zone from the perspective of the state that is defending (or projecting) sovereignty without crossing the threshold of open armed conflict. Eighteen components are identified across six dependency levels, from the four contested sovereignty pillars (cyber, territorial, economic, cultural) down through statecraft, effect delivery and theatre operations to the shared landscape layer, proxy operator capacity and the crypto rails that underpin deniable flows.

Three strategic insights fall out of the decomposition:

1. **Attribution is a shared bottleneck.** Four mid-chain components (Treaties and Norms, Ethics Framework, Accountability Mechanisms, Consequence Management) all depend on Attribution. Whether it is weaponised-commodity or genuinely novel drives the whole chain.
2. **Crypto Rails sit deep in the infrastructure layer.** They are the commodity substrate under both deniability and proxy operator capacity — which is why their policy treatment (sanctions, mixing, exchange attestation) shapes grey-zone plausibility.
3. **Legitimacy is a parallel chain to Statecraft.** Cultural sovereignty routes through Legitimacy rather than Statecraft, and Legitimacy draws on the Ethics Framework — so hearts-and-minds effects have a different dependency structure from coercive / kinetic effects.

## 2. Users and Personas

| User type | Primary need |
|---|---|
| Supranational (UN, NATO, EU) | Maintain the rules-based order; preserve escalation thresholds |
| National government (executive / MoD / MFA) | Preserve sovereignty across all four pillars; manage escalation |
| National intelligence / security service | Detect, attribute, and counter below-threshold effects |
| Private / proxy operator | Execute effects at arm's length from the sponsor |
| Citizens / affected population | Continue daily life; retain trust in institutions |

The anchor is written from the perspective of the **national government** as the sovereign actor. Supranationals appear as part of the Treaties-and-Norms layer; proxies and crypto rails appear as commodity-layer enablers; citizens are the ultimate legitimacy constituency for the Cultural Sovereignty pillar.

## 3. Value Chain Diagram

### ASCII outline

```
visibility
  0.98  Sovereignty Maintenance
          |
  0.88  Cyber | Territorial | Economic | Cultural Sovereignty
          |        |             |           |
  0.78  Statecraft                       Legitimacy
  0.74       Effect Delivery
  0.72       Theatre Operations
  0.68       Situational Awareness
  0.62       Consequence Management
  0.55  Treaties and Norms           Ethics Framework
  0.48  Accountability Mechanisms
  0.42  Attribution        Deniability Management
  0.30       Proxy Operator Capacity
  0.18       Landscape Layer
  0.12       Crypto Rails
```

### OWM syntax

```owm
title Defence Grey Zone — Value Chain (ArcKit partial map, ε placeholders)

anchor Sovereignty Maintenance [0.98, 0.50]

component Cyber Sovereignty [0.88, 0.50]
component Territorial Integrity [0.88, 0.50]
component Economic Sovereignty [0.88, 0.50]
component Cultural Sovereignty [0.88, 0.50]

component Statecraft [0.78, 0.50]
component Legitimacy [0.78, 0.50]
component Effect Delivery [0.74, 0.50]
component Theatre Operations [0.72, 0.50]
component Situational Awareness [0.68, 0.50]
component Consequence Management [0.62, 0.50]

component Treaties and Norms [0.55, 0.50]
component Ethics Framework [0.55, 0.50]
component Accountability Mechanisms [0.48, 0.50]
component Attribution [0.42, 0.50]
component Deniability Management [0.42, 0.50]

component Proxy Operator Capacity [0.30, 0.50]
component Landscape Layer [0.18, 0.50]
component Crypto Rails [0.12, 0.50]

Sovereignty Maintenance -> Cyber Sovereignty
Sovereignty Maintenance -> Territorial Integrity
Sovereignty Maintenance -> Economic Sovereignty
Sovereignty Maintenance -> Cultural Sovereignty

Cyber Sovereignty -> Statecraft
Cyber Sovereignty -> Effect Delivery
Cyber Sovereignty -> Situational Awareness
Territorial Integrity -> Statecraft
Territorial Integrity -> Theatre Operations
Economic Sovereignty -> Statecraft
Economic Sovereignty -> Theatre Operations
Cultural Sovereignty -> Legitimacy
Cultural Sovereignty -> Effect Delivery

Statecraft -> Treaties and Norms
Statecraft -> Accountability Mechanisms
Statecraft -> Deniability Management
Legitimacy -> Ethics Framework
Legitimacy -> Accountability Mechanisms
Effect Delivery -> Theatre Operations
Effect Delivery -> Consequence Management
Theatre Operations -> Situational Awareness
Theatre Operations -> Proxy Operator Capacity
Situational Awareness -> Landscape Layer
Consequence Management -> Attribution
Consequence Management -> Ethics Framework

Treaties and Norms -> Attribution
Ethics Framework -> Attribution
Accountability Mechanisms -> Attribution
Attribution -> Landscape Layer
Deniability Management -> Proxy Operator Capacity
Deniability Management -> Crypto Rails

Proxy Operator Capacity -> Landscape Layer
Proxy Operator Capacity -> Crypto Rails
Landscape Layer -> Crypto Rails

style wardley
```

<details>
<summary>Mermaid <code>wardley-beta</code> equivalent</summary>

```mermaid
wardley-beta
title Defence Grey Zone — Value Chain (ArcKit partial map)
size [1100, 800]

anchor "Sovereignty Maintenance" [0.98, 0.50]

component "Cyber Sovereignty" [0.88, 0.50]
component "Territorial Integrity" [0.88, 0.50]
component "Economic Sovereignty" [0.88, 0.50]
component "Cultural Sovereignty" [0.88, 0.50]

component Statecraft [0.78, 0.50]
component Legitimacy [0.78, 0.50]
component "Effect Delivery" [0.74, 0.50]
component "Theatre Operations" [0.72, 0.50]
component "Situational Awareness" [0.68, 0.50]
component "Consequence Management" [0.62, 0.50]

component "Treaties and Norms" [0.55, 0.50]
component "Ethics Framework" [0.55, 0.50]
component "Accountability Mechanisms" [0.48, 0.50]
component Attribution [0.42, 0.50]
component "Deniability Management" [0.42, 0.50]

component "Proxy Operator Capacity" [0.30, 0.50]
component "Landscape Layer" [0.18, 0.50]
component "Crypto Rails" [0.12, 0.50]

"Sovereignty Maintenance" -> "Cyber Sovereignty"
"Sovereignty Maintenance" -> "Territorial Integrity"
"Sovereignty Maintenance" -> "Economic Sovereignty"
"Sovereignty Maintenance" -> "Cultural Sovereignty"

"Cyber Sovereignty" -> Statecraft
"Cyber Sovereignty" -> "Effect Delivery"
"Cyber Sovereignty" -> "Situational Awareness"
"Territorial Integrity" -> Statecraft
"Territorial Integrity" -> "Theatre Operations"
"Economic Sovereignty" -> Statecraft
"Economic Sovereignty" -> "Theatre Operations"
"Cultural Sovereignty" -> Legitimacy
"Cultural Sovereignty" -> "Effect Delivery"

Statecraft -> "Treaties and Norms"
Statecraft -> "Accountability Mechanisms"
Statecraft -> "Deniability Management"
Legitimacy -> "Ethics Framework"
Legitimacy -> "Accountability Mechanisms"
"Effect Delivery" -> "Theatre Operations"
"Effect Delivery" -> "Consequence Management"
"Theatre Operations" -> "Situational Awareness"
"Theatre Operations" -> "Proxy Operator Capacity"
"Situational Awareness" -> "Landscape Layer"
"Consequence Management" -> Attribution
"Consequence Management" -> "Ethics Framework"

"Treaties and Norms" -> Attribution
"Ethics Framework" -> Attribution
"Accountability Mechanisms" -> Attribution
Attribution -> "Landscape Layer"
"Deniability Management" -> "Proxy Operator Capacity"
"Deniability Management" -> "Crypto Rails"

"Proxy Operator Capacity" -> "Landscape Layer"
"Proxy Operator Capacity" -> "Crypto Rails"
"Landscape Layer" -> "Crypto Rails"
```

</details>

## 4. Component Inventory

| # | Component | ν | Description | Depends on |
|---|---|---|---|---|
| 1 | Sovereignty Maintenance | 0.98 | Anchor: state's need to retain authority over its territory, population, economy, narrative and digital space under persistent below-threshold contest | 2, 3, 4, 5 |
| 2 | Cyber Sovereignty | 0.88 | Control of national digital space — networks, identities, data flows — against intrusion and manipulation | 6, 8, 10 |
| 3 | Territorial Integrity | 0.88 | Control of physical territory and its approaches (land, maritime, air, space) against below-threshold incursion | 6, 9 |
| 4 | Economic Sovereignty | 0.88 | Resilience of finance, energy, supply chains and critical industry against coercion | 6, 9 |
| 5 | Cultural Sovereignty | 0.88 | Shared national narrative, public trust, and institutional legitimacy under information contest | 7, 8 |
| 6 | Statecraft | 0.78 | The deliberate conduct of policy through diplomatic, economic, military and informational instruments | 12, 14, 16 |
| 7 | Legitimacy | 0.78 | The perceived lawful and rightful basis for an actor's conduct, held by domestic and international audiences | 13, 14 |
| 8 | Effect Delivery | 0.74 | Coerce / deter / hearts-and-minds / kinetic / propaganda — the five effect types in the scenario | 9, 11 |
| 9 | Theatre Operations | 0.72 | Activity across the five theatres: land, electronic, space, social media, finance | 10, 17 |
| 10 | Situational Awareness | 0.68 | Physical, virtual and supply-chain awareness feeding decision cycles | 18 |
| 11 | Consequence Management | 0.62 | Handling friendly fire, unintended effects, escalation risk and second-order consequences | 13, 15 |
| 12 | Treaties and Norms | 0.55 | Rules-based instruments (UN Charter, Budapest Convention, LOAC, export controls) that set thresholds | 15 |
| 13 | Ethics Framework | 0.55 | Just-war, distinction, proportionality, information ethics — the moral rails under operations | 15 |
| 14 | Accountability Mechanisms | 0.48 | Parliamentary, judicial, ombudsman and press oversight of state conduct | 15 |
| 15 | Attribution | 0.42 | Technical and political assignment of responsibility for an effect to an actor | 18 |
| 16 | Deniability Management | 0.42 | Deliberate construction of plausible deniability across the operation | 16a, 16b |
| 17 | Proxy Operator Capacity | 0.30 | Private, criminal or volunteer operator supply chain used at arm's length from sponsor | 18, 19 |
| 18 | Landscape Layer | 0.18 | Physical / virtual / supply-chain substrate — cables, satellites, ports, BGP, clouds, shipping | 19 |
| 19 | Crypto Rails | 0.12 | Commodity settlement layer for deniable flows — tokens, mixers, on/off ramps |  |

(ν is the visibility score from the arckit scale in Step 5 of the skill. The evolution axis is deferred to the full-map command; all components carry the ε=0.50 placeholder in this partial map.)

## 5. Dependency Matrix

Direct (X) and indirect (I) dependencies. Rows are dependants; columns are dependencies.

|  | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 Sov. Maintenance | X | X | X | X | I | I | I | I | I | I | I | I | I | I | I | I | I | I |
| 2 Cyber Sov. |  |  |  |  | X |  | X |  | X | I | I | I | I | I | I | I | I | I |
| 3 Territorial |  |  |  |  | X |  |  | X | I |  | I |  | I | I | I | I | I | I |
| 4 Economic |  |  |  |  | X |  |  | X | I |  | I |  | I | I | I | I | I | I |
| 5 Cultural |  |  |  |  |  | X | X |  | I | I |  | I | I | I |  | I | I | I |
| 6 Statecraft |  |  |  |  |  |  |  |  |  |  | X |  | X | I | X | I | I | I |
| 7 Legitimacy |  |  |  |  |  |  |  |  |  |  |  | X | X | I |  |  |  |  |
| 8 Effect Delivery |  |  |  |  |  |  |  | X | I | X |  | I |  | I |  | I | I | I |
| 9 Theatre Ops |  |  |  |  |  |  |  |  | X |  |  |  |  | I |  | X | I | I |
| 10 Situational Aw. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | X | I |
| 11 Consequence Mgt |  |  |  |  |  |  |  |  |  |  |  | X |  | X |  |  | I | I |
| 12 Treaties |  |  |  |  |  |  |  |  |  |  |  |  |  | X |  |  | I |  |
| 13 Ethics |  |  |  |  |  |  |  |  |  |  |  |  |  | X |  |  | I |  |
| 14 Accountability |  |  |  |  |  |  |  |  |  |  |  |  |  | X |  |  | I |  |
| 15 Attribution |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | X | I |
| 16 Deniability |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | X | I | X |
| 17 Proxy Operator |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | X | X |
| 18 Landscape |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | X |

## 6. Critical Path Analysis

**Deepest critical path (anchor to deepest commodity):**

Sovereignty Maintenance → Cyber Sovereignty → Statecraft → Deniability Management → Crypto Rails

**Convergence bottlenecks (single points of failure):**

- **Attribution** — four mid-chain components converge on it (Treaties, Ethics, Accountability, Consequence Management). If attribution is cheap and fast, the whole chain above it hardens. If it remains genuinely novel and contested, the chain stays weak regardless of how well-resourced the upper layers are.
- **Landscape Layer** — every lower path passes through it. Physical, virtual and supply-chain substrate is the common commodity floor.
- **Crypto Rails** — the terminal commodity. Deniability Management, Proxy Operator Capacity and Landscape Layer all end here.

**Resilience gaps:**

- Situational Awareness has only one downward dependency (Landscape Layer) — loss of awareness in one layer (e.g. supply-chain) has no sibling fallback at this level of the chain; this is a candidate for further decomposition in a full map.
- Legitimacy has no direct link to Treaties and Norms in this chain — a deliberate modelling choice (domestic legitimacy ≠ international legality) but worth validating.

## 7. Validation Checklist

**Completeness**

- [x] Chain starts with a genuine user need (not a solution or capability)
- [x] All significant dependencies between components captured
- [x] Chain reaches commodity level (Crypto Rails, Landscape Layer)
- [x] No orphan components (every node has at least one connection)
- [x] All components are activities, capabilities or practices — not actors

**Accuracy**

- [x] Dependencies reflect real-world technical and operational relationships
- [x] Visibility ordering consistent with dependency direction (ν(parent) ≥ ν(child) on every edge)
- [x] No component is simultaneously user-facing and infrastructure

**Usefulness**

- [x] Granularity appropriate for strategic decision-making (18 components, 6 levels)
- [x] Each component is meaningfully positionable on the evolution axis in a subsequent full-map pass
- [x] Chain reveals at least one strategic insight (three are documented above)

**Mathematical constraints (from `tractorjuice/wardleymap_math_model`)**

- [x] DAG acyclicity — no edge returns upward
- [x] Visibility ordering on every edge (see Section 8)
- [x] Anchor has ν ≥ 0.90 (ν=0.98)

## 8. Visibility Assessment

| Component | ν | Reasoning |
|---|---|---|
| Sovereignty Maintenance | 0.98 | Anchor; the state-level outcome under which everything else exists |
| Cyber / Territorial / Economic / Cultural Sovereignty | 0.88 | The four pillars named in the scenario; directly felt when contested |
| Statecraft / Legitimacy | 0.78 | Proximate instruments / perceptions that citizens and allies experience |
| Effect Delivery | 0.74 | One step below statecraft — the category of effect applied |
| Theatre Operations | 0.72 | Specific theatre activity executing an effect |
| Situational Awareness | 0.68 | Decision input layer; not user-facing but close to operations |
| Consequence Management | 0.62 | Post-effect handling; visible when something goes wrong (friendly fire) |
| Treaties and Norms / Ethics Framework | 0.55 | Rule systems that shape but do not directly perform operations |
| Accountability Mechanisms | 0.48 | Oversight — visible only at moments of scrutiny |
| Attribution | 0.42 | Operates below the political surface most of the time |
| Deniability Management | 0.42 | Active concealment — visible only when it fails |
| Proxy Operator Capacity | 0.30 | Deliberately obscured supply layer |
| Landscape Layer | 0.18 | Substrate — largely invisible until damage occurs |
| Crypto Rails | 0.12 | Deep commodity — invisible to citizens, visible to regulators only in aggregate |

## 9. Assumptions and Open Questions

**Assumptions**

- The anchor is the defending state, not the attacker. An offensive chain would share most mid-layer components but reverse the polarity on Deniability Management and Legitimacy.
- Supranationals (UN, NATO, EU) are modelled inside Treaties and Norms and Accountability Mechanisms rather than as separate components, because at the value-chain level they are capability-shaping instruments, not standalone activities.
- Citizens / people appear as the constituency for Legitimacy and Cultural Sovereignty rather than as a component, consistent with the arckit rule that components are capabilities, not actors.
- Effect Delivery is a single component holding all five effect types (coerce, deter, hearts-and-minds, kinetic, propaganda). In a full map these are candidates for separate positioning since propaganda is effectively commodity on social-media rails while kinetic below-threshold effects are closer to custom-built.
- Theatres (land, electronic, space, social media, finance) are collapsed into Theatre Operations for the same reason.

**Open questions for full-map (`$arckit-wardley`) pass**

1. Which effect types are now weaponised-commodity (propaganda on social media, ransomware as a service, sanctions packages) and which are still genuinely novel (orbital interference, deepfake-at-scale, algorithmic cultural corrosion)? This is the headline question in the scenario and must be answered on the evolution axis, not on the visibility axis.
2. Where does Attribution sit on evolution? Cyber attribution has moved from Genesis toward Custom-Built / early Product; kinetic-in-grey-zone attribution (e.g. sabotaged cables) is still largely Genesis. Split this component in the full map.
3. Should Crypto Rails be split into regulated (exchanges, stablecoins) versus unregulated (mixers, privacy coins) for the evolution pass? Their evolution trajectories are diverging.
4. Is the Ethics Framework the same component for state-on-state effects as for state-on-citizen effects (lethal autonomous weapons, domestic surveillance, civil-protest policing)? Consider a split.
5. Does the chain need to represent alliance / coalition capability as a separate component, or is that adequately handled inside Statecraft and Treaties and Norms?

## External References

No external documents were provided. This chain is derived solely from the scenario text and the arckit-wardley.value-chain skill procedure.

---

**Generated by:** ArcKit `$arckit-wardley.value-chain` (blind competitor benchmark run)
**Generated on:** 2026-04-23
**AI Model:** claude-opus-4-7 (1M context)
**Generation Context:** Single-scenario blind run against the `defence-grey-zone` benchmark in `skills/wardley-map-workspace/competitor-compare/arckit-value-chain/`.
