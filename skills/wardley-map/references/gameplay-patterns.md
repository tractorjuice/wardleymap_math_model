# Gameplay Patterns — 61 Strategic Plays

Simon Wardley's **61 gameplays** in **12 categories**. Source: [*On 61 different forms of gameplay*, 2015](https://blog.gardeviance.org/2015/05/on-61-different-forms-of-gameplay.html).

Unlike doctrine, gameplays are **context-dependent** — they work in some landscapes and fail in others. The skill cites them by name and number when recommending strategic moves.

---

## How to read a gameplay

Each entry below includes:
- **Wardley's short description** (from the 2015 blog post).
- **Mechanism** — which math-model parameters it affects (`r_v` evolution rate, `c_v` inertia, `ν` visibility, `ε` evolution score, `E` edges, or organisational/structural changes outside the formal model).
- **When to use** — what map shape or situation makes it appropriate.
- **When NOT to use** — the anti-pattern where it backfires.
- **Pairs well with** — other gameplays that combine into common sequences.

Not every play gets full depth here — the most common 20–25 are expanded; the rest get a one-line entry with their mechanism.

---

## 1. Basic Operations (6)

*Organisational-level moves that improve the player's own readiness.*

### 1. Focus on user needs
*"Focus the organisation on user needs rather than internal needs."*

**Mechanism:** map-structural. Strengthens edges from anchor set `U`; often reveals missing components when the organisation has been building for itself rather than users.

**When to use:** always. This is nearly doctrine, not just gameplay (see doctrine #1). As a *gameplay*, it means: if the map shows components that have no path back to a user need, re-anchor.

**When NOT to use:** never in reverse. You don't move *away* from user needs.

**Pairs with:** #26 Differentiation (differentiation is only differentiation if a user values it), #42 Co-creation.

### 2. Situational Awareness
*"Remove alignment issues between business, IT and other groups."*

**Mechanism:** map-structural, improves `τ` accuracy and `ν / ε` estimates by integrating multiple viewpoints.

**When to use:** when teams are visibly out of sync on strategy.

### 3. Effective & Efficient
*"Removal of bias and duplication within an organisation."*

**Mechanism:** lowers inertia weights `λ_i` on supplier-side forms (#15–17).

### 4. Structure & Culture
*"Implementation of cell-based & PST (Pioneer-Settler-Town-Planner) structures."*

**Mechanism:** organisational. Partitions `V` by evolution band and assigns different cultures to each.

**Pairs with:** doctrine #33 (There is no one culture).

### 5. Optimising Flow
*"Risk, performance, information and financial flow can be analysed."*

**Mechanism:** raises `r_v` on own chain by removing bottlenecks.

**Pairs with:** doctrine #26 (Optimise flow).

### 6. Channel Conflict
*"Exploiting new channels and conflict within existing channels."*

**Mechanism:** edge `E` mutation. Adds new channel edges; can redirect user traffic.

---

## 2. User Perception (7)

*Plays that change how users think about a component rather than the component itself. Primary effect is on `ν`, not `ε`.*

### 7. Education
*"Overcoming user inertia to a change through education."*

**Mechanism:** lowers consumer-side inertia forms #6 (Confusion over method) and #8 (Skill acquisition cost).

**When to use:** when a technically superior alternative is being resisted because users don't know how to adopt it.

**When NOT to use:** when the real blocker is political (#3) or economic (#2), not educational. Education on top of a political block wastes energy.

**Pairs with:** #15 Open Approaches, #42 Co-creation.

### 8. Bundling
*"Hiding a disadvantageous change by bundling the change with other needs."*

**Mechanism:** `ν` shift on the bundled component — hides it behind a more wanted one.

**When to use:** introducing a necessary but unloved change (e.g., a price rise bundled with a feature the user wanted).

**When NOT to use:** if users can easily unbundle and reject your change.

### 9. Creating artificial needs
*"Creating and elevating an artificial need through marketing."*

**Mechanism:** raises `ν` on a target component by manufacturing user perception of importance.

**Note:** ethically grey. Use sparingly.

### 10. Confusion of Choice
*"Preventing users from making rational decisions by overwhelming them."*

**Mechanism:** raises competitor's consumer-side inertia form #6 (Confusion over method).

**Note:** ethically grey. Often deployed defensively against a simpler rival.

### 11. FUD (Fear, Uncertainty, Doubt)
*"Creating fear, uncertainty and doubt over a change."*

**Mechanism:** raises competitor's consumer-side inertia forms #7 (Supplier-trust) and #11 (Suitability doubt).

**Note:** classic incumbent defensive play. *Not a form of inertia itself* — it's a gameplay that induces inertia in the competitor's customers.

### 12. Artificial competition
*"Creating two competing bodies to become the focus of competition."*

**Mechanism:** map-structural — introduces a decoy to absorb attention.

### 13. Lobbying
*"Persuading Government of a favourable position."*

**Mechanism:** suppresses competitor's `r_v` via regulation.

**Note:** also *not a form of inertia*. It's a gameplay that induces regulatory friction, which in turn creates inertia in the market.

---

## 3. Accelerators (5)

*Raise `r_v` for components whose rightward movement benefits the player.*

### 14. Market Enablement
*"Encouraging the development of competition in a market."*

**Mechanism:** raises `r_v` sector-wide on components you want commoditised (so you can consume them as utilities).

**When to use:** you're a buyer who wants more suppliers.

### 15. Open Approaches
*"Encouraging competition through open source, open data, open APIs."*

**Mechanism:** `r_v` up dramatically; `c_v` down by removing inertia forms #2 (sunk capital in proprietary), #8 (retraining), #12 (second-sourcing risk).

**When to use:** your component is becoming a commodity and you want to accelerate that — because you make money elsewhere (on a higher-order system the commoditised component enables).

**When NOT to use:** the component IS your differentiation. Don't open-source your moat.

**Famous examples:** Google opening Android (commoditised OS so Google could sell ads on top); Kubernetes (commoditised orchestration so cloud providers could sell managed services on top).

**Pairs with:** #29 Harvesting (open-source, watch what emerges, acquire winners), #45 Two factor.

### 16. Exploiting Network Effects
*"Increases the marginal value with increased number of users."*

**Mechanism:** super-linear `r_v` boost — rate itself scales with adoption.

**When to use:** you're on a two-sided platform or any market where user count begets user count.

**Pairs with:** #45 Two factor (this is the network effect play specialised for two-sided markets).

### 17. Co-operation
*"Working with others. Sounds easy, actually it's not."*

**Mechanism:** joint `u_v(t)` across multiple players; pools strategic action.

### 18. Industrial Policy
*"Government investment in a field."*

**Mechanism:** raises baseline `r_{0,v}` via public investment (infrastructure, R&D grants, tax credits).

---

## 4. Deaccelerators (4)

*Lower `r_v` for components whose commoditisation would hurt the player. Note Wardley's spelling — not "Decelerators".*

### 19. Exploiting existing constraints
*"Finding a constraint and reinforcing it."*

**Mechanism:** suppresses `r_v` by reinforcing a chokepoint.

**When to use:** you have something the market can't easily route around (spectrum, land, patented process).

### 20. Patents & IPR
*"Preventing competitors from developing a space."*

**Mechanism:** suppresses competitor's `r_v`.

**When to use:** you're ahead in a valuable space and the patent system recognises your innovation.

**When NOT to use:** when the component is already well on its way to being commoditised; patents then delay but don't prevent.

### 21. Creating constraints
*"Supply chain manipulation with a view of creating constraint."*

**Mechanism:** manufactures a new bottleneck in the competitor's supply chain.

### 22. Limitation of competition
*"Through regulatory or other means."*

**Mechanism:** suppresses sector `r_v` via regulatory friction.

---

## 5. Dealing with Toxicity (3)

*Plays for disposing of components that are locked in but should be let go.*

### 23. Disposal of liability
*"Overcoming the internal inertia to disposal."*

**Mechanism:** lowers inertia forms #2 (sunk capital) and #3 (political capital) — internal resistance to writing off a toxic asset.

### 24. Sweat & Dump
*"Exploiting a 3rd party to take over operating the toxic asset."*

**Mechanism:** edge mutation + ownership transfer.

**Famous example:** outsourcing a mainframe environment to a third party who runs it to end-of-life on your behalf. You get rid of the asset; they take the operational margin.

### 25. Pig in a poke
*"Creating a situation where others believe the toxic asset has value."*

**Mechanism:** `ν` up + selective disclosure.

**Note:** ethically grey at best. Often crosses into misrepresentation.

---

## 6. Market (6)

*Plays that exploit the shape of the current market.*

### 26. Differentiation
*"Creating a visible difference through user needs."*

**Mechanism:** raises `ν` on the distinguishing feature by tying it to a real user need (not a manufactured one — that's #9).

**When to use:** your component is Stage II–III and you're competing on features.

**Pairs with:** #1 Focus on user needs (differentiation is only meaningful against real needs).

### 27. Pricing policy
*"Exploiting supply and demand effects."*

**Mechanism:** economic — outside the core map model.

### 28. Exploiting buyer / supplier power
*"Creating a position of strength for yourself."*

**Mechanism:** map-structural. Positioning in the dependency graph such that buyers need you or suppliers depend on you.

### 29. Harvesting
*"Allowing others to develop upon your offerings and harvesting."*

**Mechanism:** monitor `ε` trajectories of ecosystem components; acquire the winners once they emerge.

**Famous example:** Amazon watching which products sell well on its marketplace, then launching its own private-label version.

**Pairs with:** #15 Open Approaches (open a platform, let ecosystem grow, harvest the emergent winners), #43 Sensing Engines.

### 30. Standards game
*"Driving a market to a standard to create a cost of transition."*

**Mechanism:** `τ` coercion + raises competitor's switching-cost inertia (#9 Re-architecture, #14 Strategic-control loss).

**Famous example:** Microsoft's Office file-format strategy; Apple's MFi licensing.

### 31. Signal distortion
*"Exploiting commonly used signals in the market by manipulation."*

**Mechanism:** map misdirection — manipulates the signals competitors use to plan.

---

## 7. Defensive (4)

### 32. Threat acquisition
*"Buying up those companies that may threaten your market."*

**Mechanism:** map merge — absorbs competitor into own tuple.

**Famous example:** Facebook acquiring Instagram and WhatsApp before either could disrupt it.

### 33. Raising barriers to entry
*"Increasing expectations within a market."*

**Mechanism:** sector-wide `ι` (inertia) raise — makes it costlier for new entrants.

### 34. Procrastination
*"Do nothing and allow competition to drive a system."*

**Mechanism:** `u_v(t) = 0` deliberately. Sometimes the right move is to wait for market forces.

**When to use:** the component is heading toward commoditisation anyway, and active intervention would only cost money without changing the outcome.

**When NOT to use:** a disruptor is emerging that requires active response. Procrastination here is Kodak's strategy, and Kodak is dead.

### 35. Defensive regulation
*"Using Government's to create protection for your market."*

**Mechanism:** suppresses sector `r_v`.

---

## 8. Attacking (5)

### 36. Directed investment
*"VC approach to a specific or identified future change."*

**Mechanism:** raises `r_v` on chosen component via concentrated resources.

**When to use:** you've identified a Genesis/Custom component that will become strategic and you want to accelerate it.

**Pairs with:** #37 Experimentation (investment without experimentation is gambling), #58 Weak Signal (detect which components to invest in).

### 37. Experimentation
*"Use of specialists groups, hackdays and other mechanisms."*

**Mechanism:** map exploration — generates candidate components to add to `V`.

**Pairs with:** doctrine #15 FIRE (experimentation should be fast, inexpensive, restrained, elegant).

### 38. Creating centres of gravity
*"Creating a focus of talent to encourage market focus."*

**Mechanism:** lowers own #4 (human capital inertia); can pull talent from competitors raising theirs.

### 39. Undermining barriers to entry
*"Identifying a barrier and reducing it."*

**Mechanism:** sector-wide inertia reduction — attackers' version of #33.

### 40. Fool's mate
*"Using a constraint to force industrialisation."*

**Mechanism:** raises `r_v` via a constraint that forces the target component to commoditise.

**Famous example:** AWS forcing on-prem infrastructure to industrialise by offering a utility alternative. The "constraint" was CapEx vs OpEx economics.

**Pairs with:** #40's actual naming comes from chess — a fool's mate is a checkmate in very few moves. In Wardley terms: a play that forces your opponent into a losing position quickly.

---

## 9. Ecosystem (7)

### 41. Alliances
*"Working with other companies to drive evolution."*

**Mechanism:** joint `r_v` up; edge mutation between maps.

### 42. Co-creation
*"Working with end users to drive evolution."*

**Mechanism:** raises `r_v`; users directly contribute to `V`.

### 43. Sensing Engines (ILC)
*"Using consumption data to detect future success."*

**Mechanism:** observability of `ε` across the ecosystem. Classic Innovate-Leverage-Commoditise cycle: innovate to create options, leverage ecosystem activity to detect winners, commoditise the winners.

**Famous example:** AWS reading its own API call patterns to decide what services to launch next.

**Pairs with:** #29 Harvesting, #58 Weak Signal.

### 44. Tower and Moat
*"Dominating a future position and prevent future competitors."*

**Mechanism:** edge mutation + inertia raise. Occupy the valuable position; dig a moat around it.

### 45. Two factor
*"Bringing together consumers and producers."*

**Mechanism:** edge mutation — creates the two-sided matching structure.

**When to use:** your business model requires matching two user types (buyers and sellers, clients and freelancers, riders and drivers).

**Pairs with:** #16 Exploiting Network Effects (two-factor markets are the canonical network-effect play).

### 46. Co-opting
*"Copying competitors move and undermining ecosystem advantage."*

**Mechanism:** map copy + raises competitor inertia.

### 47. Embrace & Extend
*"Capturing an existing ecosystem."*

**Mechanism:** map merge + extension — support an existing standard, then add proprietary extensions that lock users in.

**Famous example:** Microsoft's historical approach to protocols and formats.

---

## 10. Competitor (7)

*Plays directed specifically at a named rival.*

### 48. Tech Drops
*"Creating a 'follow me' situation and dropping large technology changes."*

**Mechanism:** raises `r_v` beyond rivals' ability to keep up.

### 49. Fragmentation
*"Exploiting pricing effects, constraints and co-opting."*

**Mechanism:** `ν` split + inertia up on rival's market.

### 50. Reinforcing inertia
*"Identifying inertia within a competitor."*

**Mechanism:** raises competitor's inertia forms specifically. Find their weakest form (e.g., sunk capital in the old model) and amplify it.

**Famous example:** taunting a declining competitor to double down on their losing strategy.

**Pairs with:** #11 FUD (FUD + reinforcing inertia is a classic incumbent-disruption playbook).

### 51. Sapping
*"Opening up multiple fronts on a competitor."*

**Mechanism:** multi-front `u_v(t)` — stretch competitor's attention and resources.

### 52. Misdirection
*"Sending false signals to competitors."*

**Mechanism:** signal on competitor's map to induce bad decisions.

### 53. Restriction
*"Limiting a competitors ability to adapt."*

**Mechanism:** suppresses competitor's `r_v` via external constraints.

### 54. Talent Raid
*"Removing core talent from a competitor."*

**Mechanism:** raises competitor's human-capital inertia (form #4).

---

## 11. Positional (4)

*Plays about where to be, not what to do.*

### 55. Land grab
*"Identifying and position a company to capture a future market space."*

**Mechanism:** map-structural pre-commitment. Take the space before competitors realise it's valuable.

### 56. First mover
*"Exploiting first mover advantage especially with industrialisation."*

**Mechanism:** raises `r_v` early; captures lock-in benefits.

**Pairs with:** #30 Standards game (first mover + setting the standard = durable advantage).

**Contrast:** #57 Fast follower.

### 57. Fast follower
*"Exploiting fast follower advantage into uncharted spaces."*

**Mechanism:** delayed `r_v` boost — let someone else prove the market, then move in.

**When first mover beats fast follower:** network-effect markets, standards markets.
**When fast follower beats first mover:** markets where early-mover costs (product/market fit discovery) outweigh the lock-in benefits.

### 58. Weak Signal
*"Use of common economic patterns to identify where and when."*

**Mechanism:** observability. Reading climatic patterns and publication shifts to identify where to position.

**Pairs with:** #43 Sensing Engines, #36 Directed investment.

---

## 12. Poison (3)

*Plays designed to make a space unusable to rivals.*

### 59. Licensing
*"Use of licensing to prevent future competitor moves."*

**Mechanism:** suppresses sector `r_v` via licensing regime.

### 60. Insertion
*"Either through talent or misdirection, encouraging false moves."*

**Mechanism:** false `V` additions — seed misinformation that leads competitor into unproductive paths.

### 61. Design to fail
*"Removing potential future threats by poisoning a market space."*

**Mechanism:** `ε` sabotage — make the space look smaller or less profitable than it is.

**Note:** adversarial and often ethically grey.

---

## Totals

6 + 7 + 5 + 4 + 3 + 6 + 4 + 5 + 7 + 7 + 4 + 3 = **61** ✓

---

## Composing gameplays — common sequences

Real strategy is a sequence, not a single play. Common patterns:

### The ILC cycle (gameplay #43 expanded)

1. **#55 Land grab** on an emerging Genesis component.
2. **#36 Directed investment** + **#37 Experimentation** to mature it.
3. **#43 Sensing Engines** to detect adjacent moves in the ecosystem.
4. Once approaching Product stage, **#15 Open Approaches** to accelerate to Commodity.
5. Once commoditised, **#29 Harvesting** of the winners built on your platform.

AWS, Google Cloud, and Azure all visibly run versions of this sequence.

### The disruptor playbook

1. **#39 Undermining barriers to entry** — identify and reduce entry costs.
2. **#40 Fool's mate** — force incumbent component to commoditise.
3. **#50 Reinforcing inertia** — amplify incumbent's sunk-capital resistance.
4. **#11 FUD** — seed doubt about incumbent's future.
5. **#56 First mover** in the new paradigm.

### The incumbent defence

1. **#32 Threat acquisition** — buy threats before they scale.
2. **#11 FUD** — seed doubt about alternatives.
3. **#33 Raising barriers to entry** — make new entry costlier.
4. **#35 Defensive regulation** — codify protection in law.
5. **#20 Patents & IPR** — protect the current position legally.

---

## Play selection as optimisation

Given a current map `M_t` and projected horizon `T`, picking gameplays is a discrete optimisation over a 61-item action set. Intractable in general, useful in scoped planning exercises. See `mathematical-models.md` §8 for the formulation.

---

## Not inertia

Three plays commonly misfiled as inertia:

- **#8 Bundling** — gameplay, not inertia. Bundling is a *move*; inertia is *resistance*.
- **#11 FUD** — gameplay that *induces* inertia in the competitor's customers.
- **#13 Lobbying** — gameplay that *induces* regulatory friction.

See `inertia.md` for the 17 structured forms of inertia.

---

## Caveats

1. **Mechanism labels are interpretations.** Wardley's one-line descriptions leave room for reading. The mechanism column encodes this skill's reading; a mapper may reasonably disagree.

2. **Context-dependence is everything.** Unlike doctrine, gameplays only work in certain landscapes and climates. "Procrastination" (#34) is catastrophic in a fast-moving market and correct in a saturated one.

3. **Competitor plays assume you have a competitor map.** Plays targeting `V_competitor` require you to have (or project) a map of the rival's value chain.

4. **The 61 is the 2015 count.** Community sources have since added or re-grouped some. This skill uses the original 2015 taxonomy because it's the authoritative primary source.

5. **Not everything is a play.** Doctrine is what you do always. Gameplays are what you do in response to the map. Confusing the two is the most common beginner error.

6. **Ethics matter.** Several plays (#9, #10, #11, #25, #31, #52, #60, #61) are ethically grey at best. Document whether you're using them and why. They may be legal and effective but corrode trust over time.
