# Gender as a Cultural Construct (March 2022) — Wardley Map

## Scenario

Map the components that shape gender as a cultural construct. Start from identity and phenotype and work through sexual identity, sexual orientation, gender identity, and gender expression; include the lived-experience layer and how memory, stories, and symbols codify roles. Cover the collective structures (family, nation, patriarchy, matriarchy, corporation) and the values and rights/beliefs they carry, the hierarchies of authority and power, social class, property and ownership, and exclusion/self-expression. Underneath, include the biological substrate — genetic markers, epigenetics, environment. I'd like to see what's individual and emergent versus what's industrialised social machinery, and where power concentrates.

## Mathematical Model

$\mathcal{M} = (V, E, U, \nu, \varepsilon, t)$ with two anchors:

- $U = \{\text{Individual}, \text{Society}\}$ — gender is simultaneously a lived individual need and a collective organising need.
- $|V| \approx 30$ components spanning identity, codification, collective structures, power, biology.
- Evolution $\varepsilon$ set by the quick 4-row cheat-sheet method (Ubiquity / Certainty / User Perception / Publication Types).
- Visibility $\nu$ seeded from shortest distance to the nearest anchor and then judgment-adjusted so that industrialised collective machinery (which is experientially "deep" to most individuals) lands well below the directly lived-experience layer despite being short-hop in graph terms.

## Placement rationale (selected)

| Component | $\varepsilon$ | Stage | Reason |
|---|---|---|---|
| Lived Experience | 0.22 | Genesis | Unique per person, poorly understood, non-replicable — Stage I on certainty, ubiquity of *type*. |
| Gender Identity | 0.30 | Custom Built | 2022: rapid learning, public discourse, contested; *no* commodity version. |
| Matriarchy | 0.35 | Custom Built | Rare, poorly understood as a live organising principle in 2022 industrialised societies (vs. anthropological record). |
| Identity | 0.40 | Custom Built / edging Product | Well-theorised in psychology, still contested in law. |
| Memory | 0.45 | Custom Built | Individual plus culturally-scaffolded — not commoditised. |
| Phenotype | 0.55 | Product | Well-understood biology, widely catalogued. |
| Exclusion | 0.55 | Product | Widespread mechanism, extensively studied, but still actively contested in 2022. |
| Stories / Symbols | 0.60 / 0.62 | Product | Mass-produced, templated, but culturally variable. |
| Roles | 0.75 | Product / edging Commodity | Gender roles are highly templated and industrialised in family/corporate/nation contexts. |
| Values | 0.68 | Product | Packaged through media/religion/education. |
| Rights | 0.72 | Product | Codified in law, still actively expanding in 2022. |
| Beliefs | 0.80 | Commodity | Packaged, replicable, widespread. |
| Family | 0.78 | Commodity | Universal institution, many standardised forms. |
| Nation | 0.85 | Commodity | Ubiquitous, templated, Westphalian. |
| Corporation | 0.82 | Commodity | Standardised legal/organisational form. |
| Patriarchy | 0.88 | Commodity (+ inertia) | Ubiquitous, deeply institutionalised — industrialised social machinery. |
| Authority / Power | 0.82 / 0.85 | Commodity | Standardised chains of command across institutions. |
| Property / Ownership | 0.90 / 0.88 | Commodity (+utility) | Heavily codified, tradeable, utility-like infrastructure. |
| Social Class | 0.80 | Commodity | Stabilised, well-mapped, actively reproduced. |
| Environment | 0.70 | Product | Measured; standardised epidemiology. |
| Epigenetics | 0.30 | Custom Built | Still rapid-learning science in 2022. |
| Genetic Markers | 0.55 | Product | Sequencing is utility-grade; interpretation remains active research. |

## OWM map

```owm
title Gender as a Cultural Construct (March 2022)
style wardley

// Anchors
anchor Individual [0.98, 0.25]
anchor Society [0.96, 0.70]

// Layer 1 — directly experienced identity surface
component Gender Expression [0.90, 0.32]
component Self Expression [0.88, 0.28]
component Lived Experience [0.86, 0.22]
component Exclusion [0.84, 0.55]

// Layer 2 — identity constructs (individual, emergent)
component Gender Identity [0.80, 0.30]
component Sexual Orientation [0.78, 0.35]
component Sexual Identity [0.76, 0.38]
component Identity [0.74, 0.40]
component Phenotype [0.72, 0.55]

// Layer 3 — codifying mechanisms
component Stories [0.68, 0.60]
component Symbols [0.66, 0.62]
component Memory [0.64, 0.45]
component Roles [0.62, 0.75]

// Layer 4 — values, rights, beliefs
component Values [0.58, 0.68]
component Rights [0.56, 0.72]
component Beliefs [0.54, 0.80]

// Layer 5 — collective structures (industrialised social machinery)
component Family [0.50, 0.78]
component Patriarchy [0.48, 0.88] inertia
component Matriarchy [0.46, 0.35]
component Nation [0.44, 0.85]
component Corporation [0.42, 0.82]

// Layer 6 — power apparatus
component Authority [0.38, 0.82]
component Power [0.36, 0.85]
component Social Class [0.34, 0.80]
component Property [0.32, 0.90]
component Ownership [0.30, 0.88]

// Layer 7 — biological substrate
component Environment [0.22, 0.70]
component Epigenetics [0.14, 0.30]
component Genetic Markers [0.08, 0.55]

// Dependencies — Individual path
Individual->Gender Expression
Individual->Self Expression
Individual->Lived Experience
Gender Expression->Gender Identity
Self Expression->Gender Identity
Self Expression->Exclusion
Lived Experience->Gender Identity
Lived Experience->Memory
Gender Identity->Sexual Orientation
Gender Identity->Sexual Identity
Sexual Orientation->Identity
Sexual Identity->Identity
Identity->Phenotype
Identity->Genetic Markers

// Dependencies — Society path
Society->Exclusion
Society->Roles
Society->Family
Society->Nation
Society->Corporation
Roles->Stories
Roles->Symbols
Roles->Values
Stories->Memory
Symbols->Memory
Values->Beliefs
Values->Rights
Rights->Beliefs

// Collective structures carry values/rights/beliefs
Family->Values
Family->Roles
Patriarchy->Authority
Patriarchy->Power
Matriarchy->Authority
Nation->Authority
Nation->Rights
Corporation->Ownership
Corporation->Property

// Power apparatus
Authority->Social Class
Authority->Power
Power->Property
Power->Ownership
Social Class->Property
Social Class->Ownership
Ownership->Property

// Biological substrate
Phenotype->Genetic Markers
Phenotype->Epigenetics
Phenotype->Environment
Epigenetics->Genetic Markers
Epigenetics->Environment

// Codification reinforces roles
Memory->Roles
Stories->Roles
Symbols->Roles

// Evolution scenarios (NOT forecasts)
evolve Gender Identity 0.55
evolve Rights 0.82
evolve Roles 0.55

// Notes
note Individual / emergent zone [0.80, 0.20]
note Industrialised social machinery [0.40, 0.85]
note Power concentration [0.32, 0.88]
note Biological substrate [0.15, 0.50]
```

## 9. Strategic Analysis

### a. Top 3 by Differentiation pressure $D(v) = \nu(v)(1-\varepsilon(v))$

| Component | $\nu$ | $\varepsilon$ | $D$ | Reading |
|---|---|---|---|---|
| Lived Experience | 0.86 | 0.22 | 0.67 | The highest-differentiation zone: individually novel, emergent, not commoditisable. The authentic engine of new gender understanding. |
| Self Expression | 0.88 | 0.28 | 0.63 | User-facing, still Genesis/Custom — the surface where individual variation meets social templating. |
| Gender Expression | 0.90 | 0.32 | 0.61 | Visible, distinct, contested — the performative layer that differentiates culturally. |

Interpretation: the **individual / emergent** zone the user asked about is exactly this top-left region (high $\nu$, low $\varepsilon$). These components are where novel gender meaning is *produced*, before being captured by roles/stories/values.

### b. Top 3 by Commodity leverage $K(v) = (1-\nu(v))\varepsilon(v)$

| Component | $\nu$ | $\varepsilon$ | $K$ | Reading |
|---|---|---|---|---|
| Property | 0.32 | 0.90 | 0.61 | Deep + highly commoditised — legal/economic infrastructure on which gendered access rests. |
| Ownership | 0.30 | 0.88 | 0.62 | Same — the industrial plumbing. |
| Power | 0.36 | 0.85 | 0.54 | Institutional power as utility-grade machinery. |

Interpretation: this is the **"industrialised social machinery"** layer the user asked for. It is deep in the value chain from the individual's perspective but is the infrastructure that carries gendered effects (unequal pay, unequal inheritance, unequal property rights).

### c. Top 3 dependency risks $R(a,b) = \nu(a)(1-\varepsilon(b))$

| Edge | $R$ | Reading |
|---|---|---|
| (Lived Experience, Memory) | 0.86 × 0.55 = 0.47 | Highly visible individual experience depends on a still-personal, non-commoditised memory substrate — fragile and contestable. |
| (Identity, Genetic Markers) | 0.74 × 0.45 = 0.33 | Identity discourse in 2022 often appeals to genetic "ground truth" that is itself less settled than public discourse assumes. |
| (Self Expression, Exclusion) | 0.88 × 0.45 = 0.40 | Self-expression is immediately exposed to the evolving (still-contested) mechanism of social exclusion — visible component riding on a transitional foundation. |

### d. Suggested gameplays (from the 61-play catalogue)

These plays are named as analogies for social-change actors (movements, regulators, institutional reformers); they are not recommendations for strategic manipulation of individuals.

- **Open Approaches (#15)** on *Rights*: push codification into open, standardised rights frameworks so that Rights evolve faster toward commodity/utility (the `evolve Rights 0.82` arrow). Reduces the ability of single institutions to control them.
- **Undermining barriers to entry (#22)** on *Roles*: deliberately disrupt the templating that stabilises gendered Roles in Family/Corporation — makes the Commodity-stage Role layer contestable.
- **Exploiting constraint (#8)** on *Exclusion*: social-change actors in 2022 are concentrating on constraints (law, platform policy) that bind Exclusion to the Rights layer.
- **Pig in a poke / Last Man Standing (#46 / #48)** aimed at *Patriarchy* as an inertia-laden Commodity-stage structure: expose its sunk and political capital costs to accelerate divestment.
- **Co-creation (#12)** on *Stories / Symbols*: culture-producing actors (media, art) co-create new symbolic vocabulary with communities to bypass the slow codification chain.

### e. Doctrine notes

- **Phase II — Focus on user needs**: the map carries **two anchors** (Individual, Society). This is doctrinally sound: gender operates in both registers simultaneously. A one-anchor version (Individual only *or* Society only) would hide exactly the tension the user asked to see.
- **Phase II — Know your users**: Individual and Society are heterogeneous anchors; further decomposition (e.g., separating State from Market, or separating differently-situated individuals) is possible — flagged as a doctrine weakness if the map is used for real-world decisions.
- **Phase I — Use a common language**: terms like "Patriarchy", "Matriarchy", "Gender Identity" are politically loaded in 2022; any real intervention based on this map must specify operational definitions.
- **Phase IV — Manage inertia**: Patriarchy is marked with the `inertia` flag; in the 17-forms taxonomy this is primarily **political capital**, **cultural capital**, and **sunk social capital** (institutions, laws, habits).
- **Knowledge layer under-specified**: the map shows Beliefs, Values, Stories, Symbols as Product/Commodity, but the *Knowledge* (theories, scholarship) behind gender studies as a discipline is not explicitly represented. For a more rigorous version, add a $\tau$-typing pass (A/P/D/K).
- **Evolution caveats**: the three `evolve` arrows (Gender Identity → 0.55, Rights → 0.82, Roles → 0.55) are **scenarios, not forecasts**. The climatic pattern *"you cannot measure evolution over time or adoption"* applies with particular force to cultural constructs.

## Where power concentrates (direct answer)

Power in the map concentrates in the **bottom-right quadrant** — deep (low $\nu$) and highly commoditised (high $\varepsilon$): Property, Ownership, Power, Authority, Social Class, Nation, Patriarchy, Corporation. This is the industrialised social machinery. By contrast, the individual / emergent components (Lived Experience, Self Expression, Gender Expression, Gender Identity) sit top-left — high visibility to the individual, still in Genesis/Custom. The map makes the asymmetry visible: *lived gender is made at the top-left but filtered, templated and disciplined through the bottom-right*.
