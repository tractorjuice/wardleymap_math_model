# Government Sovereignty — Wardley Value Chain (ArcKit partial map)

**Command**: `$arckit-wardley.value-chain`
**Skill**: arckit-wardley.value-chain (partial map — Y-axis + dependencies only; ε placeholder = 0.50)
**Scenario date**: April 2023
**Generated**: 2026-04-23

## Executive Summary

This value chain decomposes the problem of maintaining **national sovereignty** from a government's point of view into 33 components across 11 dependency levels. The anchor is the **Supranational Layer** — the order of international norms, treaties and peer states inside which any single government must operate. Three immediate stakeholder groups sit below it: **Government**, **Corporations and Shareholders**, and **Society**. Beneath them sit the six **pillars of sovereignty** (territorial, economic, political, digital, cultural, security), which are satisfied through four **theatres** (land, supply chain, cyber, CNI), mediated by **legitimacy outcomes** and **social norms**, and ultimately resting on a **capability layer**, an **awareness apparatus**, and a **legal substrate** (domestic and international law).

**Key strategic insights**:

1. **Industrialised infrastructure vs. contested fragility** — The legal substrate (domestic and international law), the capability layer, and awareness systems for territory and CNI sit at the bottom of the chain and are the most industrialised and shared. The upper contested components — election legitimacy, digital sovereignty, perception of success, and the cyber / supply chain theatres — are where sovereignty is most fragile and least settled.
2. **Digital and cyber as single points of strategic failure** — Digital Sovereignty and the Cyber Theatre touch almost every pillar (economic, political, security, CNI). A shock here cascades upward into legitimacy and belonging far faster than shocks in the land or territorial theatres.
3. **Legitimacy is the feedback loop** — Election Legitimacy, Perception of Success, and Public Belonging close the loop from the media mix and norms back up to political and cultural sovereignty. Propaganda is a shared dependency of every channel in the media mix — it is an operational commodity in this chain, not a peripheral.

## Users and Personas

| Stakeholder | Primary Need |
|-------------|--------------|
| Supranational Layer (treaties, peer states, IGOs) | Predictable participation in the international order |
| Government (executive, parliament, civil service) | Ability to govern and maintain sovereignty within its territory |
| Corporations and Shareholders | Predictable regulatory, supply-chain and legal environment to operate in |
| Society (citizens, communities) | Protection, legitimacy, belonging, services |

## Value Chain Diagram (ASCII)

```text
 0.98  Supranational Layer  (anchor)
 0.92  Government   Corporations & Shareholders   Society
 0.84  Territorial  Economic  Political  Digital  Cultural  Security
 0.76  Election Legitimacy   Perception of Success   Public Belonging
 0.68  Land Theatre   Supply Chain Theatre   Cyber Theatre   CNI Theatre
 0.60  Integrity  Benevolence  Fairness  Competency  Identity (norms)
 0.52  Crisis Response
 0.44  Social Media  Mainstream Media  Education  Art  Propaganda
 0.36  Capability Layer
 0.26  Territorial Awareness   Supply Chain Awareness   Digital Chain Awareness
 0.16  Domestic Law
 0.08  International Law
```

## OWM Source

See `draft.owm` in this directory. Paste directly into https://create.wardleymaps.ai.

> **Note**: ε = 0.50 is a placeholder on every component. The arckit-value-chain skill produces a **partial map** — visibility and dependencies only. Evolution must be assigned by a subsequent `$arckit-wardley` mapping step.

## Mermaid Wardley Value Chain

<details>
<summary>Mermaid wardley-beta source</summary>

```mermaid
wardley-beta
title Government Sovereignty — Value Chain (ArcKit partial map)
size [1100, 800]

anchor "Supranational Layer" [0.98, 0.50]

component Government [0.92, 0.50]
component "Corporations and Shareholders" [0.92, 0.50]
component Society [0.92, 0.50]

component "Territorial Sovereignty" [0.84, 0.50]
component "Economic Sovereignty" [0.84, 0.50]
component "Political Sovereignty" [0.84, 0.50]
component "Digital Sovereignty" [0.84, 0.50]
component "Cultural Sovereignty" [0.84, 0.50]
component "Security Sovereignty" [0.84, 0.50]

component "Election Legitimacy" [0.76, 0.50]
component "Perception of Success" [0.76, 0.50]
component "Public Belonging" [0.76, 0.50]

component "Land Theatre" [0.68, 0.50]
component "Supply Chain Theatre" [0.68, 0.50]
component "Cyber Theatre" [0.68, 0.50]
component "CNI Theatre" [0.68, 0.50]

component "Integrity Norm" [0.60, 0.50]
component "Benevolence Norm" [0.60, 0.50]
component "Fairness Norm" [0.60, 0.50]
component "Competency Norm" [0.60, 0.50]
component "Identity Norm" [0.60, 0.50]

component "Crisis Response" [0.52, 0.50]

component "Social Media" [0.44, 0.50]
component "Mainstream Media" [0.44, 0.50]
component Education [0.44, 0.50]
component Art [0.44, 0.50]
component Propaganda [0.44, 0.50]

component "Capability Layer" [0.36, 0.50]

component "Territorial Awareness" [0.26, 0.50]
component "Supply Chain Awareness" [0.26, 0.50]
component "Digital Chain Awareness" [0.26, 0.50]

component "Domestic Law" [0.16, 0.50]
component "International Law" [0.08, 0.50]

"Supranational Layer" -> Government
"Supranational Layer" -> "Corporations and Shareholders"
"Supranational Layer" -> Society

Government -> "Territorial Sovereignty"
Government -> "Political Sovereignty"
Government -> "Digital Sovereignty"
Government -> "Security Sovereignty"
Government -> "Economic Sovereignty"
"Corporations and Shareholders" -> "Economic Sovereignty"
"Corporations and Shareholders" -> "Digital Sovereignty"
"Corporations and Shareholders" -> "Supply Chain Theatre"
Society -> "Cultural Sovereignty"
Society -> "Political Sovereignty"
Society -> "Public Belonging"

"Territorial Sovereignty" -> "Land Theatre"
"Territorial Sovereignty" -> "CNI Theatre"
"Economic Sovereignty" -> "Supply Chain Theatre"
"Economic Sovereignty" -> "CNI Theatre"
"Political Sovereignty" -> "Election Legitimacy"
"Political Sovereignty" -> "Perception of Success"
"Digital Sovereignty" -> "Cyber Theatre"
"Digital Sovereignty" -> "CNI Theatre"
"Cultural Sovereignty" -> "Public Belonging"
"Cultural Sovereignty" -> "Perception of Success"
"Security Sovereignty" -> "Land Theatre"
"Security Sovereignty" -> "Cyber Theatre"
"Security Sovereignty" -> "CNI Theatre"

"Election Legitimacy" -> "Integrity Norm"
"Election Legitimacy" -> "Fairness Norm"
"Election Legitimacy" -> "Competency Norm"
"Election Legitimacy" -> "Identity Norm"
"Perception of Success" -> "Mainstream Media"
"Perception of Success" -> "Social Media"
"Perception of Success" -> "Crisis Response"
"Public Belonging" -> "Benevolence Norm"
"Public Belonging" -> "Identity Norm"

"Land Theatre" -> "Capability Layer"
"Land Theatre" -> "Territorial Awareness"
"Supply Chain Theatre" -> "Capability Layer"
"Supply Chain Theatre" -> "Supply Chain Awareness"
"Cyber Theatre" -> "Capability Layer"
"Cyber Theatre" -> "Digital Chain Awareness"
"CNI Theatre" -> "Capability Layer"
"CNI Theatre" -> "Crisis Response"

"Integrity Norm" -> "Mainstream Media"
"Integrity Norm" -> Education
"Benevolence Norm" -> Education
"Benevolence Norm" -> Art
"Fairness Norm" -> "Domestic Law"
"Fairness Norm" -> Education
"Competency Norm" -> "Capability Layer"
"Competency Norm" -> Education
"Identity Norm" -> Art
"Identity Norm" -> Education

"Crisis Response" -> "Mainstream Media"
"Crisis Response" -> "Capability Layer"
"Crisis Response" -> "Domestic Law"

"Social Media" -> Propaganda
"Mainstream Media" -> Propaganda
Education -> "Domestic Law"
Art -> Propaganda
Propaganda -> "Capability Layer"

"Capability Layer" -> "Territorial Awareness"
"Capability Layer" -> "Supply Chain Awareness"
"Capability Layer" -> "Digital Chain Awareness"
"Capability Layer" -> "Domestic Law"

"Territorial Awareness" -> "Domestic Law"
"Territorial Awareness" -> "International Law"
"Supply Chain Awareness" -> "International Law"
"Digital Chain Awareness" -> "International Law"

"Domestic Law" -> "International Law"
```

</details>

## Component Inventory

| Component | Visibility | Layer | Role |
|-----------|-----------:|-------|------|
| Supranational Layer | 0.98 | anchor | Treaties, IGOs, peer states — the order the government participates in |
| Government | 0.92 | L1 stakeholder | Executive, parliament, civil service |
| Corporations and Shareholders | 0.92 | L1 stakeholder | Private actors with skin in sovereignty |
| Society | 0.92 | L1 stakeholder | Citizens and communities |
| Territorial Sovereignty | 0.84 | L2 pillar | Control of borders, land, airspace, maritime |
| Economic Sovereignty | 0.84 | L2 pillar | Currency, markets, trade policy |
| Political Sovereignty | 0.84 | L2 pillar | Decision rights, self-determination |
| Digital Sovereignty | 0.84 | L2 pillar | Data, platforms, compute jurisdiction |
| Cultural Sovereignty | 0.84 | L2 pillar | Language, values, shared story |
| Security Sovereignty | 0.84 | L2 pillar | Defence and internal security |
| Election Legitimacy | 0.76 | L3 outcome | Trust in the vote as authorising act |
| Perception of Success | 0.76 | L3 outcome | Public judgement of government competence |
| Public Belonging | 0.76 | L3 outcome | Shared membership of the political community |
| Land Theatre | 0.68 | L4 theatre | Where territorial control is contested |
| Supply Chain Theatre | 0.68 | L4 theatre | Where economic dependency is contested |
| Cyber Theatre | 0.68 | L4 theatre | Where digital and information integrity is contested |
| CNI Theatre | 0.68 | L4 theatre | Critical national infrastructure — energy, water, telecoms |
| Integrity Norm | 0.60 | L5 norm | Honesty of public life |
| Benevolence Norm | 0.60 | L5 norm | Care for constituents |
| Fairness Norm | 0.60 | L5 norm | Equal treatment under rules |
| Competency Norm | 0.60 | L5 norm | Delivery ability |
| Identity Norm | 0.60 | L5 norm | Who counts as "one of us" |
| Crisis Response | 0.52 | L6 | Capacity to respond to shocks and cascade failures |
| Social Media | 0.44 | L7 media | Platform-mediated public discourse |
| Mainstream Media | 0.44 | L7 media | Broadcast / print journalism |
| Education | 0.44 | L7 media | Formal learning, curriculum |
| Art | 0.44 | L7 media | Cultural production |
| Propaganda | 0.44 | L7 media | State / partisan narrative production |
| Capability Layer | 0.36 | L8 | Armed forces, agencies, civil service delivery capacity |
| Territorial Awareness | 0.26 | L9 awareness | ISR on land, maritime, airspace, borders |
| Supply Chain Awareness | 0.26 | L9 awareness | Visibility of physical & commercial dependencies |
| Digital Chain Awareness | 0.26 | L9 awareness | Visibility of digital / software / platform dependencies |
| Domestic Law | 0.16 | L10 substrate | Statute, common law, regulators |
| International Law | 0.08 | L11 substrate | UN Charter, treaty law, customary law — commodity substrate |

## Critical Path Analysis

**Primary chain (anchor to deepest commodity)**:

`Supranational Layer → Government → Political Sovereignty → Election Legitimacy → Integrity Norm → Mainstream Media → Propaganda → Capability Layer → Domestic Law → International Law`

**Bottlenecks / single points of failure**:

- **Capability Layer** — shared dependency of every theatre and of Crisis Response; degradation here degrades every sovereignty pillar.
- **Propaganda** — every media channel in the mix ultimately feeds into it, and it feeds the Capability Layer (doctrine, recruitment narrative). A hostile capture of Propaganda production damages every norm above it.
- **Digital Chain Awareness / Cyber Theatre** — the least industrialised of the theatres and awareness systems; fragile and expanding.

**Resilience gaps**:

- Only one route from Political Sovereignty through Election Legitimacy into norms — no redundant legitimacy channel.
- Corporations & Shareholders have only weak edges into the sovereignty pillars (Economic, Digital, Supply Chain Theatre), suggesting under-modelled private-sector influence on sovereignty that a mature map should refine.
- No explicit financial rails / central-bank component; subsumed under Economic Sovereignty and may need to be surfaced at the mapping stage.

## Dependency Matrix (compact)

Direct dependencies by source component (omitted for brevity when there is one; shown below for components with three or more outbound edges):

| Source | Direct dependencies |
|--------|---------------------|
| Supranational Layer | Government, Corporations and Shareholders, Society |
| Government | Territorial, Economic, Political, Digital, Cultural, Security sovereignty |
| Election Legitimacy | Integrity, Fairness, Competency, Identity norms |
| Perception of Success | Mainstream Media, Social Media, Crisis Response |
| CNI Theatre | Capability Layer, Crisis Response |
| Capability Layer | Territorial Awareness, Supply Chain Awareness, Digital Chain Awareness, Domestic Law |
| Crisis Response | Mainstream Media, Capability Layer, Domestic Law |

Full edge list is in `draft.owm`.

## Visibility Assessment

| Band | Components | Rationale |
|------|-----------|-----------|
| 0.98 | Supranational Layer | Anchor — the order the user (the government) participates in |
| 0.92 | Government, Corporations, Society | Primary actors experiencing sovereignty directly |
| 0.84 | Six pillars | How stakeholders perceive sovereignty (by kind) |
| 0.76 | Legitimacy, Perception, Belonging | Legitimacy outcomes that constituencies feel directly |
| 0.68 | Four theatres | Where sovereignty is visibly contested |
| 0.60 | Five norms | Beliefs about government that shape legitimacy — felt, not seen |
| 0.52 | Crisis Response | Only visible when invoked |
| 0.44 | Media mix | Channels — the public sees outputs, not the mechanism |
| 0.36 | Capability Layer | Operational — largely hidden from citizens |
| 0.26 | Awareness apparatus | ISR / monitoring — intentionally low-visibility |
| 0.16 | Domestic Law | Infrastructure; visible only on contact |
| 0.08 | International Law | Deepest substrate; rarely visible to citizens |

## Validation Checklist

- [x] Chain starts with a genuine user need (Supranational Layer anchors a government's sovereignty need)
- [x] All significant dependencies between components are captured
- [x] Chain reaches a commodity substrate (International Law)
- [x] No orphan components
- [x] All components are activities / capabilities / practices (stakeholders at L1 are named as actor-roles but each has a distinct need; this is a concession typical of sovereignty mapping — noted in Assumptions)
- [x] Dependencies reflect real operational relationships
- [x] Visibility ordering is consistent with dependency direction
- [x] No cycles — the few equal-visibility edges (Social/Mainstream/Art → Propaganda) all flow in one direction
- [x] Granularity is appropriate for strategic decision-making (33 components across 11 levels)
- [x] Each component can be placed on the evolution axis in a subsequent mapping step

## Where Sovereignty is Industrialised Infrastructure vs. Contested and Fragile

**Industrialised (likely utility / commodity at the subsequent mapping step)**:

- Domestic Law and International Law — legal substrate is slow-moving, broadly shared, codified.
- Territorial Awareness — centuries of ISR practice; mature.
- Mainstream Media and Education — long-established industries with stable production models.
- Capability Layer (for conventional force, policing, diplomatic corps) — industrialised in the stable democracies this scenario assumes.

**Contested and fragile (likely custom-built or product, and moving)**:

- Digital Sovereignty — unsettled legally, commercially and technically.
- Cyber Theatre and Digital Chain Awareness — nascent, under-instrumented.
- Supply Chain Awareness — exposed post-2020 as immature despite decades of global trade.
- Election Legitimacy — under sustained contestation via Social Media and Propaganda in many jurisdictions as of April 2023.
- Propaganda — technically ancient, but newly industrialising at platform scale via Social Media.

## Assumptions and Open Questions

- **Stakeholders as components at L1**: Government, Corporations and Shareholders, and Society are treated as components in this value chain because the scenario explicitly asks to anchor on them. In a strict arckit reading, L1 should be capabilities rather than actors; the concession is made deliberately here and flagged for the mapping step.
- **Compound anchor**: The scenario lists four anchors (Supranational Layer, Government, Corporations, Society). Only one is designated as the top-of-stack anchor (Supranational Layer); the others are L1 dependants. An alternative would be a single higher-level abstract anchor ("National Sovereignty"), but that would obscure the government's perspective the scenario asks for.
- **Media / Propaganda edges**: Propaganda is modelled as a dependency of the civilian media mix because, in the scenario's framing, propaganda synthesises the output of the other four channels. A stricter reading might flip edges (Propaganda → Social Media). The current direction is the one consistent with equal-visibility positioning and with Crisis Response's fall-through onto media.
- **Missing financial / central-bank rails**: Subsumed under Economic Sovereignty. The full mapping step should surface them.
- **No time-based evolution**: ε = 0.50 is a placeholder. Evolution positions require the next mapping step (`$arckit-wardley`).

## Next Steps

- Run `$arckit-wardley` to assign evolution positions to each of the 33 components.
- Revisit the Media / Propaganda edges and the Corporations dependencies before the next step.
- Consider surfacing financial infrastructure (central bank, payments, sanctions regime) as explicit components at the mapping stage.
