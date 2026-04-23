# Value Chain: Gender as a Cultural Construct (March 2022)

> **Note**: This is a *partial* Wardley Map produced by the `arckit-wardley.value-chain` skill. Only visibility (Y-axis) is assessed. Evolution (X-axis) is a placeholder (ε = 0.50 for every component) and would be set by running the follow-up `$arckit-wardley` command.

## 1. Executive Summary

- **Anchor**: "A person can have and express a coherent gendered self."
- **Components**: 24 components across 7 visibility bands, from the user-facing *Gendered Self* down to the biological substrate (*Genetic Markers*, *Environment*).
- **Key insight**: The chain separates a thin, individual-emergent upper layer (*Gender Expression*, *Identity*, *Lived Experience*, *Sexual Orientation/Identity*) from a deep, industrialised middle band of collective structures (*Family*, *Corporation*, *Nation*, *Patriarchy*, *Matriarchy*) that concentrate into two power commodities — *Authority and Power* and *Social Class* — before terminating at *Property and Ownership* and the biology layer.
- **Power concentration**: Six distinct collective structures converge on *Authority and Power* (visibility 0.30), which in turn dominates *Social Class* (0.28) and then *Property and Ownership* (0.26). This funnel is the answer to "where does power concentrate."
- **Individual vs industrialised**: the split sits at roughly ν ≈ 0.55. Above that line are the emergent, personal components; below is social machinery.

## 2. Users and Personas

| User | Primary need |
|---|---|
| The gendered person (primary) | Have and express a coherent gendered self; be recognised and not excluded |
| The social theorist / strategist (secondary) | See where power concentrates and which layers are individual vs industrialised |
| The institutional actor (tertiary) | Understand which structures (family, nation, corporation, patriarchy, matriarchy) carry and enforce gender roles |

## 3. Value Chain Diagram

### 3.1 ASCII skeleton

```
ν ≈ 0.95 │ Gendered Self (ANCHOR)
         │      │
ν ≈ 0.82 │ ┌────┼────┐
         │ Expr  Id   Lived Experience
ν ≈ 0.70 │ │     │       │
         │ │  Sexual Id / Sexual Orientation, Self-Expression, Exclusion
ν ≈ 0.58 │ Memory & Stories, Symbols & Roles, Values & Beliefs, Rights
         │            │
ν ≈ 0.50 │          Identity
         │            │
ν ≈ 0.40 │ Family, Corporation, Nation, Patriarchy, Matriarchy  ← industrialised social machinery
         │            │
ν ≈ 0.30 │       Authority & Power
         │            │
ν ≈ 0.28 │        Social Class
         │            │
ν ≈ 0.26 │     Property & Ownership
         │
ν ≈ 0.18 │        Phenotype
         │            │
ν ≈ 0.12 │       Epigenetics
         │        /       \
ν ≈ 0.08 │ Environment   Genetic Markers (0.04)
```

### 3.2 OWM (paste into https://create.wardleymaps.ai)

```text
title Gender as a Cultural Construct (March 2022)

anchor Gendered Self [0.95, 0.50]

component Gender Expression [0.86, 0.50]
component Gender Identity [0.84, 0.50]
component Lived Experience [0.82, 0.50]
component Sexual Orientation [0.72, 0.50]
component Sexual Identity [0.70, 0.50]
component Self-Expression [0.68, 0.50]
component Exclusion [0.66, 0.50]
component Memory and Stories [0.60, 0.50]
component Symbols and Roles [0.58, 0.50]
component Values and Beliefs [0.56, 0.50]
component Rights [0.54, 0.50]
component Identity [0.50, 0.50]
component Family [0.44, 0.50]
component Corporation [0.42, 0.50]
component Nation [0.40, 0.50]
component Patriarchy [0.38, 0.50]
component Matriarchy [0.36, 0.50]
component Authority and Power [0.30, 0.50]
component Social Class [0.28, 0.50]
component Property and Ownership [0.26, 0.50]
component Phenotype [0.18, 0.50]
component Epigenetics [0.12, 0.50]
component Environment [0.08, 0.50]
component Genetic Markers [0.04, 0.50]

Gendered Self -> Gender Expression
Gendered Self -> Gender Identity
Gendered Self -> Lived Experience
Gender Expression -> Symbols and Roles
Gender Expression -> Self-Expression
Gender Identity -> Sexual Identity
Gender Identity -> Sexual Orientation
Gender Identity -> Identity
Lived Experience -> Memory and Stories
Lived Experience -> Exclusion
Lived Experience -> Self-Expression
Sexual Orientation -> Identity
Sexual Identity -> Identity
Self-Expression -> Values and Beliefs
Exclusion -> Authority and Power
Exclusion -> Social Class
Exclusion -> Rights
Memory and Stories -> Symbols and Roles
Memory and Stories -> Family
Symbols and Roles -> Values and Beliefs
Values and Beliefs -> Family
Values and Beliefs -> Nation
Values and Beliefs -> Corporation
Values and Beliefs -> Patriarchy
Values and Beliefs -> Matriarchy
Values and Beliefs -> Rights
Rights -> Nation
Rights -> Authority and Power
Identity -> Phenotype
Family -> Authority and Power
Family -> Property and Ownership
Corporation -> Authority and Power
Corporation -> Property and Ownership
Nation -> Authority and Power
Nation -> Social Class
Patriarchy -> Authority and Power
Patriarchy -> Social Class
Matriarchy -> Authority and Power
Authority and Power -> Social Class
Social Class -> Property and Ownership
Phenotype -> Environment
Phenotype -> Epigenetics
Phenotype -> Genetic Markers
Epigenetics -> Environment
Epigenetics -> Genetic Markers

style wardley
```

### 3.3 Mermaid wardley-beta equivalent

<details>
<summary>Mermaid value-chain (no sourcing decorators at value-chain stage)</summary>

```mermaid
wardley-beta
title Gender as a Cultural Construct (March 2022)
size [1100, 800]

anchor "Gendered Self" [0.95, 0.50]

component "Gender Expression" [0.86, 0.50]
component "Gender Identity" [0.84, 0.50]
component "Lived Experience" [0.82, 0.50]
component "Sexual Orientation" [0.72, 0.50]
component "Sexual Identity" [0.70, 0.50]
component "Self-Expression" [0.68, 0.50]
component Exclusion [0.66, 0.50]
component "Memory and Stories" [0.60, 0.50]
component "Symbols and Roles" [0.58, 0.50]
component "Values and Beliefs" [0.56, 0.50]
component Rights [0.54, 0.50]
component Identity [0.50, 0.50]
component Family [0.44, 0.50]
component Corporation [0.42, 0.50]
component Nation [0.40, 0.50]
component Patriarchy [0.38, 0.50]
component Matriarchy [0.36, 0.50]
component "Authority and Power" [0.30, 0.50]
component "Social Class" [0.28, 0.50]
component "Property and Ownership" [0.26, 0.50]
component Phenotype [0.18, 0.50]
component Epigenetics [0.12, 0.50]
component Environment [0.08, 0.50]
component "Genetic Markers" [0.04, 0.50]

"Gendered Self" -> "Gender Expression"
"Gendered Self" -> "Gender Identity"
"Gendered Self" -> "Lived Experience"
"Gender Expression" -> "Symbols and Roles"
"Gender Expression" -> "Self-Expression"
"Gender Identity" -> "Sexual Identity"
"Gender Identity" -> "Sexual Orientation"
"Gender Identity" -> Identity
"Lived Experience" -> "Memory and Stories"
"Lived Experience" -> Exclusion
"Lived Experience" -> "Self-Expression"
"Sexual Orientation" -> Identity
"Sexual Identity" -> Identity
"Self-Expression" -> "Values and Beliefs"
Exclusion -> "Authority and Power"
Exclusion -> "Social Class"
Exclusion -> Rights
"Memory and Stories" -> "Symbols and Roles"
"Memory and Stories" -> Family
"Symbols and Roles" -> "Values and Beliefs"
"Values and Beliefs" -> Family
"Values and Beliefs" -> Nation
"Values and Beliefs" -> Corporation
"Values and Beliefs" -> Patriarchy
"Values and Beliefs" -> Matriarchy
"Values and Beliefs" -> Rights
Rights -> Nation
Rights -> "Authority and Power"
Identity -> Phenotype
Family -> "Authority and Power"
Family -> "Property and Ownership"
Corporation -> "Authority and Power"
Corporation -> "Property and Ownership"
Nation -> "Authority and Power"
Nation -> "Social Class"
Patriarchy -> "Authority and Power"
Patriarchy -> "Social Class"
Matriarchy -> "Authority and Power"
"Authority and Power" -> "Social Class"
"Social Class" -> "Property and Ownership"
Phenotype -> Environment
Phenotype -> Epigenetics
Phenotype -> "Genetic Markers"
Epigenetics -> Environment
Epigenetics -> "Genetic Markers"
```

</details>

## 4. Component Inventory

| # | Component | ν | Band | Description |
|---|---|---|---|---|
| 1 | Gendered Self | 0.95 | Anchor | The lived, coherent gendered self the person presents and experiences |
| 2 | Gender Expression | 0.86 | User-facing | Outward performance: dress, speech, mannerism, style |
| 3 | Gender Identity | 0.84 | User-facing | Internal sense of one's gender |
| 4 | Lived Experience | 0.82 | High | Accumulated experience of being gendered — what happens to and for the person |
| 5 | Sexual Orientation | 0.72 | High | Pattern of attraction |
| 6 | Sexual Identity | 0.70 | High | Self-labelling of sexual category |
| 7 | Self-Expression | 0.68 | Medium-High | Broader expressive repertoire drawn on by Gender Expression |
| 8 | Exclusion | 0.66 | Medium-High | Mechanisms by which some identities are pushed out of the accepted range |
| 9 | Memory and Stories | 0.60 | Medium-High | Narrative layer — personal and shared stories that codify roles |
| 10 | Symbols and Roles | 0.58 | Medium-High | The symbolic vocabulary that roles use (clothing signs, titles, rituals) |
| 11 | Values and Beliefs | 0.56 | Medium-High | Carried values and beliefs that institutions embed |
| 12 | Rights | 0.54 | Medium-High | Formal/informal entitlements attached to gendered persons |
| 13 | Identity | 0.50 | Medium | Generic selfhood from which gender identity differentiates |
| 14 | Family | 0.44 | Medium | Kinship structure — the first collective |
| 15 | Corporation | 0.42 | Medium | Industrialised economic collective; codifies workplace gender norms |
| 16 | Nation | 0.40 | Medium | Polity; legal recognition and citizenship layer |
| 17 | Patriarchy | 0.38 | Medium | Male-dominant authority configuration |
| 18 | Matriarchy | 0.36 | Medium | Female-dominant authority configuration |
| 19 | Authority and Power | 0.30 | Low | Who can compel whom — the power commodity |
| 20 | Social Class | 0.28 | Low | Stratification produced by concentrated authority |
| 21 | Property and Ownership | 0.26 | Low | Material-claims layer over which class is enforced |
| 22 | Phenotype | 0.18 | Low | Observable bodily characteristics |
| 23 | Epigenetics | 0.12 | Infrastructure | Regulatory layer sitting between genotype and phenotype |
| 24 | Environment | 0.08 | Infrastructure | Context that drives epigenetic regulation |
| 25 | Genetic Markers | 0.04 | Infrastructure | DNA-level substrate |

## 5. Dependency Matrix

Direct dependencies only (X). Indirect not shown for brevity; see the OWM graph.

| From \ To | GExp | GId | LiE | SxO | SxI | SlE | Exc | MSt | SyR | VaB | Rig | Idn | Fam | Cor | Nat | Pat | Mat | A&P | ScC | P&O | Phe | Epi | Env | Gen |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gendered Self | X | X | X |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Gender Expression |  |  |  |  |  | X |  |  | X |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Gender Identity |  |  |  | X | X |  |  |  |  |  |  | X |  |  |  |  |  |  |  |  |  |  |  |  |
| Lived Experience |  |  |  |  |  | X | X | X |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Sexual Orientation |  |  |  |  |  |  |  |  |  |  |  | X |  |  |  |  |  |  |  |  |  |  |  |  |
| Sexual Identity |  |  |  |  |  |  |  |  |  |  |  | X |  |  |  |  |  |  |  |  |  |  |  |  |
| Self-Expression |  |  |  |  |  |  |  |  |  | X |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Exclusion |  |  |  |  |  |  |  |  |  |  | X |  |  |  |  |  |  | X | X |  |  |  |  |  |
| Memory and Stories |  |  |  |  |  |  |  |  | X |  |  |  | X |  |  |  |  |  |  |  |  |  |  |  |
| Symbols and Roles |  |  |  |  |  |  |  |  |  | X |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Values and Beliefs |  |  |  |  |  |  |  |  |  |  | X |  | X | X | X | X | X |  |  |  |  |  |  |  |
| Rights |  |  |  |  |  |  |  |  |  |  |  |  |  |  | X |  |  | X |  |  |  |  |  |  |
| Identity |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | X |  |  |  |
| Family |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | X |  | X |  |  |  |  |
| Corporation |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | X |  | X |  |  |  |  |
| Nation |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | X | X |  |  |  |  |  |
| Patriarchy |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | X | X |  |  |  |  |  |
| Matriarchy |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | X |  |  |  |  |  |  |
| Authority and Power |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | X |  |  |  |  |  |
| Social Class |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | X |  |  |  |  |
| Phenotype |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | X | X | X |
| Epigenetics |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | X | X |

## 6. Critical Path Analysis

**Deepest chain from anchor to commodity**:

`Gendered Self → Gender Identity → Identity → Phenotype → Epigenetics → Genetic Markers`

(six steps; biological floor).

**Power funnel** (the concentration path the scenario asks for):

`Values and Beliefs → {Family, Corporation, Nation, Patriarchy, Matriarchy} → Authority and Power → Social Class → Property and Ownership`

Five distinct collective structures converge into *Authority and Power* (in-degree 7 counting Exclusion, Rights, Family, Corporation, Nation, Patriarchy, Matriarchy). Power concentrates here.

**Bottlenecks / single points of failure**:

- *Values and Beliefs* (ν 0.56) — fans out to 6 children and is the chokepoint between individual expression and collective machinery. Shifts in values propagate downward through every institution.
- *Authority and Power* (ν 0.30) — the single node every institutional path passes through before reaching *Social Class* and *Property and Ownership*.
- *Identity* (ν 0.50) — every form of orientation/identity collapses into this generic node before it touches phenotype.

**Resilience gaps**:

- No feedback edge from *Rights* back up to *Exclusion* — resistance is modelled, but institutional response to resistance is not.
- *Memory and Stories* feeds *Family* directly but not *Nation*, though national mythology is a real mechanism; noted as an assumption below.

## 7. Validation Checklist

### Completeness
- [x] Chain starts with a genuine user need (*Gendered Self*, not a product or solution)
- [x] All significant dependencies captured (42 edges across 24 components + anchor)
- [x] Chain reaches commodity-level substrate (Genetic Markers, Environment)
- [x] No orphan components (Rights and Corporation were fixed with parent edges from Values and Beliefs / Exclusion)
- [x] All components are capabilities, practices, or structures — not people

### Accuracy
- [x] Dependencies reflect plausible real-world relationships
- [x] Visibility ordering consistent with dependency direction: every edge a→b satisfies ν(a) ≥ ν(b)
- [x] No component is both user-facing and infrastructure
- [x] DAG — the graph is strictly downward in visibility, so no cycles possible

### Usefulness
- [x] Granularity suitable for strategic discussion
- [x] Each component can be positioned on an evolution axis in the follow-up `$arckit-wardley` step
- [x] At least one strategic insight: the *Authority and Power* funnel is where power concentrates, and the ~0.55 visibility line is the individual-vs-industrialised divide

### Mathematical constraints (from `tractorjuice/wardleymap_math_model`)
- [x] DAG acyclicity — satisfied (verified by inspection; strict downward visibility)
- [x] Visibility ordering ν(a) ≥ ν(b) for every edge — verified by enumeration
- [x] Anchor at visibility ≥ 0.90 — Gendered Self at 0.95

## 8. Visibility Assessment

| Component | ν | Rationale |
|---|---|---|
| Gendered Self | 0.95 | Anchor; directly lived by the user |
| Gender Expression | 0.86 | Immediately visible; any change registers instantly with the user |
| Gender Identity | 0.84 | One step behind expression; internally felt |
| Lived Experience | 0.82 | Continuously accumulated; user experiences it directly |
| Sexual Orientation | 0.72 | Close to the user; felt but requires articulation |
| Sexual Identity | 0.70 | Labelling of orientation; one abstraction step down |
| Self-Expression | 0.68 | Broad repertoire underlying specific gender expression |
| Exclusion | 0.66 | Experienced acutely when it happens; otherwise invisible background |
| Memory and Stories | 0.60 | Carried but usually unexamined |
| Symbols and Roles | 0.58 | Absorbed from culture; only visible when made strange |
| Values and Beliefs | 0.56 | Rarely articulated; infer-able from behaviour |
| Rights | 0.54 | Visible when contested; otherwise taken for granted |
| Identity | 0.50 | Generic self; mostly implicit |
| Family | 0.44 | Institutional structure; persistent but backgrounded |
| Corporation | 0.42 | Industrialised collective; visible through employment |
| Nation | 0.40 | Statutory backdrop; mostly invisible in daily life |
| Patriarchy | 0.38 | Power pattern; invisible to those privileged by it |
| Matriarchy | 0.36 | Power pattern; rare in 2022 at societal scale |
| Authority and Power | 0.30 | Commodity mechanism; operationalised rather than seen |
| Social Class | 0.28 | Stratification outcome; visible when crossing |
| Property and Ownership | 0.26 | Legal-economic layer; rarely surfaced |
| Phenotype | 0.18 | Biological; lived-through rather than examined |
| Epigenetics | 0.12 | Invisible regulatory layer |
| Environment | 0.08 | Pervasive context; invisible by default |
| Genetic Markers | 0.04 | Deep infrastructure |

## 9. Assumptions and Open Questions

**Assumptions**:

1. The anchor is the *individual's* gendered self, not a society's aggregate gender regime. This is consistent with the scenario's "individual and emergent versus … industrialised social machinery" framing.
2. *Patriarchy* and *Matriarchy* are modelled as parallel structures; in 2022 global terms they are asymmetric in prevalence, but the skill treats them as structurally equivalent components.
3. *Rights* receives parent edges from *Values and Beliefs* and *Exclusion* because rights are produced both by values articulated into law and by resistance to exclusion. Other plausible parents (e.g., direct from *Lived Experience*) were omitted to keep the chain minimal.
4. *Corporation* is placed below *Values and Beliefs* because corporations codify and transmit gendered values (dress codes, roles, pay structures). They could alternatively be peers of *Family*/*Nation*.
5. Biology (phenotype, genetic markers, epigenetics, environment) is deliberately placed at the bottom per the scenario's "Underneath, include the biological substrate," reflecting that biology is the substrate, not the determinant, of gender as a construct.
6. ε = 0.50 is a placeholder for every component. Real evolution positions require the follow-up `$arckit-wardley` step with a cheat-sheet scoring pass; that step would almost certainly place *Genetic Markers*/*Environment* further right (commodity-like) and *Gender Identity* further left (more individual/emergent) than 0.50.

**Open questions**:

1. Should *Religion* be an explicit component? It arguably sits beside *Values and Beliefs* and feeds *Patriarchy*/*Matriarchy*. Currently subsumed into *Values and Beliefs*.
2. Should *Race* or *Ethnicity* be modelled? The scenario mentions neither; they would complicate the hierarchy of authority.
3. Is *Matriarchy* overstated by being peer with *Patriarchy*? Most global 2022 systems are patriarchal; matriarchy exists but is not structurally dominant.
4. *Lived Experience* → *Self-Expression* is a soft (USES) dependency; lived experience *shapes* self-expression but does not technically gate it. Captured as `->` per the skill's rule.

## 10. Metadata

- **Anchor**: Gendered Self (ν = 0.95)
- **Components**: 24 + anchor
- **Edges**: 42
- **Visibility bands used**: 7 (0.04–0.95)
- **Evolution**: placeholder (ε = 0.50 for all components — value-chain stage only)
- **Date**: 2026-04-23 (scenario context: March 2022)
- **Generated by**: `arckit-wardley.value-chain` skill (partial-map variant)
- **Model**: claude-opus-4-7[1m]
