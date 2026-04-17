# Gameplay Catalogue — 61 Plays with Math-Model Effects

> **Role of this doc.** This is the **reference catalogue**: every gameplay Wardley enumerates, with its math-model mechanism. Use it to look up what a specific play does. For **applied theory on gameplay selection** (when, why, case studies) see [Strategic Mastery](Strategic%20Mastery%3A%20Creating%20Math%20Models%20for%20Wardley%20Mapping%20Gameplays.md). For **formal modelling methodology** (utility functions, optimisation, Bayesian decisions) see [Mathematical Models for Wardley Mapping Gameplay](Mathematical%20Models%20for%20Wardley%20Mapping%20Gameplay%3A%20A%20Quantitative%20Approach%20to%20Strategic%20Decision%20Making.md). These three docs are complementary — reference, applied, formal.

Wardley catalogs **61 gameplays** across **12 categories** ([Simon Wardley, *On 61 different forms of gameplay*, 2015](https://blog.gardeviance.org/2015/05/on-61-different-forms-of-gameplay.html)). Part 1's dynamics block represents strategy as a single scalar $u_v(t)$ — that flattens this catalogue beyond recognition. This doc lists every gameplay and gives each a structured effect on the math model.

> **Not inertia.** FUD, Lobbying, and Bundling are *gameplays* (listed below), not forms of inertia. The [Inertia doc](Inertia%20-%20Forms%20of%20Resistance%20to%20Evolution.md) is a separate 17-item taxonomy of resistance forces.

---

## 1. Formal gameplay structure

Each gameplay $G$ has:

- A **target set** $T_G \subseteq V_{\text{self}} \cup V_{\text{competitor}}$ — the components on your map or a competitor's map that the play acts on.
- A **mechanism** — which of the model parameters it modifies.
- A **sign and magnitude** — whether it accelerates or decelerates the target, and by how much.

Formally, a play is a transformation $G : \mathcal{M} \to \mathcal{M}$ restricted to components in $T_G$. The transformation types align with the math model:

| Mechanism | Affects | Typical sign |
|---|---|---|
| $r_v$ rate boost | Part 1 §5 dynamics | + (accelerate evolution) |
| $r_v$ rate suppression | Part 1 §5 dynamics | − (decelerate evolution) |
| $c_v$ inertia modulation | Inertia doc | ± (raise or lower drag, often on competitor) |
| $\nu$ visibility shift | Part 1 §3 | ± (make something seem more/less user-facing) |
| $\varepsilon$ direct shift | Part 1 §4 | rare — used for disruption events |
| Edge $E$ mutation | Value chain | ± (add/remove dependencies) |
| $\tau$ type coercion | Component Types | rare — forcing an Activity to become a Practice (standardisation) |

Every catalogued play below names its mechanism(s). A play often has multiple effects; the **primary** effect drives the categorisation.

---

## 2. The 61 gameplays

### Category 1 — Basic Operations (6)

Organisational-level moves that improve the player's own readiness.

| # | Play | Mechanism | Effect |
|---|---|---|---|
| 1 | Focus on user needs | Map-structural | Strengthens edges from anchor set $U$; reveals missing components |
| 2 | Situational Awareness | Map-structural | Improves $\tau$ accuracy and $\nu / \varepsilon$ estimates |
| 3 | Effective & Efficient | $\lambda_i$ down (internal) | Lowers weights on inertia forms 15–17 (supplier-side) |
| 4 | Structure & Culture | $\lambda_i$ down (internal) | Cell-based / Pioneer-Settler-Town Planner structures reduce consumer-side inertia #16 |
| 5 | Optimising Flow | $r_v$ up (own components) | Removes internal bottlenecks, raising baseline rate on own chain |
| 6 | Channel Conflict | Edge $E$ mutation | Adds new channel edges; can redirect user traffic |

### Category 2 — User Perception (7)

Plays that change how users think about a component rather than the component itself. Primary effect is on $\nu$, not $\varepsilon$.

| # | Play | Mechanism | Effect |
|---|---|---|---|
| 7 | Education | $\iota_i$ down (form #6 Confusion over method, form #8 Skill acquisition) | Overcomes consumer inertia to change |
| 8 | Bundling | $\nu$ shift | Hides an unfavourable change by coupling it to desired ones |
| 9 | Creating artificial needs | $\nu$ up on target | Elevates visibility of a component via marketing |
| 10 | Confusion of Choice | $\iota_i$ up (form #6) on competitor | Overwhelms rational decision-making |
| 11 | FUD | $\iota_i$ up (forms #7, #11) on competitor | Raises supplier-trust concerns and suitability doubt about rival |
| 12 | Artificial competition | Map-structural | Introduces a decoy competitor to absorb attention |
| 13 | Lobbying | $r_v$ down (competitor) via regulation | Persuades government to impose friction on rival's components |

### Category 3 — Accelerators (5)

Raise $r_v$ for components whose rightward movement benefits the player.

| # | Play | Mechanism | Effect |
|---|---|---|---|
| 14 | Market Enablement | $r_v$ up (sector-wide) | Encourages competition in a market you want commoditised |
| 15 | Open Approaches | $r_v$ up, $c_v$ down | Open source / open data / open APIs — dramatic rate boost by removing inertia forms #2, #8, #12 |
| 16 | Exploiting Network Effects | $r_v$ up super-linearly | Marginal value rises with users — $r_v \sim r_0 \cdot N(t)$ |
| 17 | Co-operation | $r_v$ up (joint) | Working with others; pools $u_v(t)$ across players |
| 18 | Industrial Policy | $r_v$ up via $r_{0,v}$ | Government investment raises baseline pressure |

### Category 4 — Deaccelerators (4)

Lower $r_v$ for components whose commoditisation would hurt the player. (Wardley's spelling — not "Decelerators".)

| # | Play | Mechanism | Effect |
|---|---|---|---|
| 19 | Exploiting existing constraints | $r_v$ down via reinforced constraint | Finds bottleneck; locks it in |
| 20 | Patents & IPR | $r_v$ down (competitor) | Blocks rivals from traversing the space |
| 21 | Creating constraints | $r_v$ down via supply-chain manipulation | Manufactures a new bottleneck |
| 22 | Limitation of competition | $r_v$ down (sector) via regulation | Regulatory friction slows whole sector |

### Category 5 — Dealing with Toxicity (3)

Plays for disposing of components that are locked in but should be let go.

| # | Play | Mechanism | Effect |
|---|---|---|---|
| 23 | Disposal of liability | $\iota_i$ down (forms #2, #3) | Overcomes internal inertia to divest |
| 24 | Sweat & Dump | Edge mutation + ownership transfer | A third party takes over the toxic asset |
| 25 | Pig in a poke | $\nu$ up + disclosure manipulation | Creates the appearance of value in the toxic asset |

### Category 6 — Market (6)

Plays that exploit the shape of the current market.

| # | Play | Mechanism | Effect |
|---|---|---|---|
| 26 | Differentiation | $\nu$ up on distinguishing feature | Creates visible difference tied to user needs |
| 27 | Pricing policy | Economic (outside core model) | Exploits supply/demand signals |
| 28 | Exploiting buyer / supplier power | Map-structural | Position of strength in the dependency graph |
| 29 | Harvesting | $\varepsilon$ monitor + acquisition | Let others develop on your platform; buy winners |
| 30 | Standards game | $\tau$ coercion + lock-in | Drives market to your standard, raising switching costs |
| 31 | Signal distortion | Map misdirection | Manipulates commonly used market signals |

### Category 7 — Defensive (4)

| # | Play | Mechanism | Effect |
|---|---|---|---|
| 32 | Threat acquisition | Map merge | Buy companies that threaten your market |
| 33 | Raising barriers to entry | $\iota_i$ up (sector) | Increases expectations and cost to enter |
| 34 | Procrastination | $u_v(t) = 0$ | Deliberate inaction lets competition converge on a commodity |
| 35 | Defensive regulation | $r_v$ down (sector) | Uses government to protect your market |

### Category 8 — Attacking (5)

| # | Play | Mechanism | Effect |
|---|---|---|---|
| 36 | Directed investment | $r_v$ up on chosen component | VC-style focus on an identified future change |
| 37 | Experimentation | Map exploration | Specialist groups, hackdays — generates candidate components to add to $V$ |
| 38 | Creating centres of gravity | $\lambda_i$ down (competitor-side #4) | Talent hub pulls human capital from rivals |
| 39 | Undermining barriers to entry | $\iota_i$ down (sector) | Identifies and reduces a market barrier |
| 40 | Fool's mate | $r_v$ up via forced industrialisation | Uses a constraint elsewhere to force your rival's component to commoditise |

### Category 9 — Ecosystem (7)

| # | Play | Mechanism | Effect |
|---|---|---|---|
| 41 | Alliances | $r_v$ up (joint); edge mutation | Partner companies drive evolution together |
| 42 | Co-creation | $r_v$ up; user input on $V$ | Working with end users on new components |
| 43 | Sensing Engines (ILC) | Observability of $\varepsilon$ | Innovate-Leverage-Commoditise; consumption data detects future success |
| 44 | Tower and Moat | Edge mutation + $\iota_i$ up | Dominate a future position; prevent rivals entering |
| 45 | Two factor | Edge mutation | Bring consumers and producers together on your platform |
| 46 | Co-opting | Map copy + $\iota_i$ up | Copy competitor's move and undermine their ecosystem advantage |
| 47 | Embrace & Extend | Map merge + extension | Capture an existing ecosystem by supporting then extending it |

### Category 10 — Competitor (7)

Plays directed specifically at a named rival.

| # | Play | Mechanism | Effect |
|---|---|---|---|
| 48 | Tech Drops | $r_v$ up | "Follow me" situations; drop large tech changes on rivals |
| 49 | Fragmentation | $\nu$ split + $\iota_i$ up | Exploits pricing and constraints to break up a rival's market |
| 50 | Reinforcing inertia | $\iota_i$ up (competitor) | Identifies and amplifies the rival's own inertia |
| 51 | Sapping | Multi-front $u_v(t)$ | Opens multiple competitive fronts |
| 52 | Misdirection | Signal on competitor's map | Sends false signals to mislead rival's decisions |
| 53 | Restriction | $r_v$ down (competitor) | Limits rival's ability to adapt |
| 54 | Talent Raid | $\lambda_i$ up (competitor's #4) | Removes core talent, raising competitor human-capital inertia |

### Category 11 — Positional (4)

Plays about *where* to be, not what to do.

| # | Play | Mechanism | Effect |
|---|---|---|---|
| 55 | Land grab | Map-structural pre-commitment | Position to capture a future market space |
| 56 | First mover | $r_v$ up early | Exploits first-mover advantage, especially with industrialisation |
| 57 | Fast follower | $r_v$ up delayed | Exploits fast-follower advantage into uncharted spaces |
| 58 | Weak Signal | Observability | Uses economic patterns to identify where and when to act |

### Category 12 — Poison (3)

Plays designed to make a space unusable.

| # | Play | Mechanism | Effect |
|---|---|---|---|
| 59 | Licensing | $r_v$ down (sector) | Licensing regimes that prevent future competitor moves |
| 60 | Insertion | False $V$ additions | Encourages rival to pursue false leads |
| 61 | Design to fail | $\varepsilon$ sabotage | Removes future threats by poisoning the market space |

**Totals check:** 6 + 7 + 5 + 4 + 3 + 6 + 4 + 5 + 7 + 7 + 4 + 3 = **61** ✓

---

## 3. Composing plays

Real strategy uses **sequences** of plays, not single moves. A common sequence in the ILC pattern (play #43):

1. *Land grab* (#55) on an emerging component.
2. *Directed investment* (#36) to raise its $r_v$.
3. *Experimentation* (#37) and *Sensing Engines* (#43) to detect adjacent moves.
4. As it approaches Product, *Open Approaches* (#15) to accelerate through Commodity.
5. Once commoditised, *Harvesting* (#29) of winners built on your platform.

Mathematically, a sequence is a composition:

$$\mathcal{M}' = G_5 \circ G_4 \circ G_3 \circ G_2 \circ G_1 (\mathcal{M})$$

The order matters — composing *Harvesting* before *Open Approaches* has the opposite effect. Part 5's dynamics (and the Multi-Wave doc) give you the temporal substrate against which to evaluate whether a sequence actually produces the intended trajectory.

---

## 4. Play selection as an optimisation problem

Given a current map $\mathcal{M}_t$ and a projected horizon $T$, selecting plays is a discrete optimisation:

$$\max_{G_1, G_2, \ldots \in \text{Plays}} \quad J(\mathcal{M}_T)$$

subject to:

- Budget: $\sum_i \text{cost}(G_i) \le B$
- Applicability: each $G_i$ targets a valid component
- Compatibility: some plays contradict each other (e.g., *Procrastination* #34 and *Directed investment* #36 on the same component)

$J$ is a utility on the terminal map state — e.g., sum of commodity leverage $K(v)$ weighted by strategic priority.

This formulation is sketched in [Mathematical Models for Wardley Mapping Gameplay](Mathematical%20Models%20for%20Wardley%20Mapping%20Gameplay%3A%20A%20Quantitative%20Approach%20to%20Strategic%20Decision%20Making.md) §3.1. It is intractable in general (NP-hard combinatorial search over a 61-item action set with state dependencies), but useful in small, well-scoped strategic planning exercises.

---

## 5. Caveats

1. **Mechanism labels are approximations.** Wardley's one-line descriptions of each play leave room for interpretation. The mechanism column encodes this document's reading of the primary effect; a mapper may reasonably disagree.

2. **Context-dependence is everything.** Unlike doctrine, gameplays are **context-dependent** — they only work in certain landscapes and climates. "Procrastination" is catastrophic in a fast-moving market and correct in a saturated one. The math-model effect is the same either way; whether invoking it is wise is not.

3. **Competitor plays assume a competitor map.** Plays targeting $V_{\text{competitor}}$ assume you have (or are projecting) a map of the rival's value chain. See the original Gardeviance post for Wardley's framing of competitor mapping.

4. **61 is the 2015 count.** The community has since extended or re-grouped some categories; e.g., wardleymaps.ai cites "64 gameplays across 12 categories". This doc uses the original 2015 Wardley taxonomy because it is the authoritative primary source.

5. **Not everything is a play.** Doctrine (universal principles — see the Doctrine doc) is what you do *always*, regardless of map state. Gameplays are what you do *in response to* the map. Confusing the two is the most common beginner error.
