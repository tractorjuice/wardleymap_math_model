# Doctrine — 40 Universal Principles

**Doctrine** is the set of universal principles a strategist should apply *regardless of the map*. Where climatic patterns describe what the environment does to you, and gameplays describe context-specific moves, doctrine describes how you should conduct yourself at all times.

Wardley organises doctrine into **4 phases** (a progressive maturity path) and **6 categories** (cross-cutting themes). An organisation rarely satisfies all 40 — doctrine is both a checklist and a growth path.

Source: Simon Wardley's [Medium book](https://medium.com/wardleymaps). Earlier form: his [2016 blog post](https://blog.gardeviance.org/2016/05/wardleys-doctrine.html) listed ~15 principles without phase structure; the 40-principle form is the current canonical version.

---

## Phases

| Phase | Name | Meaning |
|---|---|---|
| I | **Stop Self-Destructive Behaviour** | Get basics right: alignment, language, transparency |
| II | **Becoming More Context Aware** | Understand users, inertia, failure; act appropriately |
| III | **Better for Less** | Optimise flow, seek talent, continuous improvement |
| IV | **Continuously Evolving** | Design for permanent change; ecosystems, no core |

Doctrine is **cumulative** — Phase III organisations still apply Phase I principles. Phases are a maturity ladder, not a menu.

---

## Categories

- **Communication** — how information flows
- **Development** — how things are built
- **Learning** — how knowledge compounds
- **Leading** — how direction is set
- **Operations** — how work runs day-to-day
- **Structure** — how teams and decisions are shaped

---

# Phase I — Stop Self-Destructive Behaviour (9 principles)

### 1. Focus on user needs
**Category:** Development

Prioritise the stakeholder's requirements over internal structure, past investment, or technology preferences. Anchor the map on real user needs (the tuple's `U`), not on internal deliverables.

*Recognise it when:* the first draft of a map has "IT department" or "monthly reporting" at the top instead of the actual user.
*Violation signal:* the anchor is an internal artefact, not a person with a need.

### 2. Use a systematic mechanism of learning
**Category:** Learning

Bias towards data. Decisions should update when evidence arrives. This principle underpins the cheat-sheet-based evolution scoring — you re-score when signals change.

*Violation signal:* "we decided X in 2021 and it's still our position" — without reference to whether 2021's signals still hold.

### 3. Use a common language
**Category:** Communication

Shared vocabulary is a precondition for shared strategy. This is why the map is so powerful: it gives a team the same words for the same things.

*Violation signal:* different teams calling the same thing different names, or the same name for different things.

### 4. Be transparent
**Category:** Communication

Bias towards open. Maps should be visible across the organisation. Assumptions should be stated, not hidden.

*Violation signal:* a strategy team maintains the "real" map privately; departments get a sanitised version.

### 5. Challenge assumptions
**Category:** Communication

Speak up and question. Maps exist precisely to surface assumptions for challenge. If every assumption in a map is accepted immediately, the map isn't working.

*Violation signal:* a map workshop produces no debates.

### 6. Remove bias and duplication
**Category:** Development

Eliminate redundancy and prejudiced thinking. Two components doing essentially the same thing is duplication; a component named after the team that owns it (rather than the capability) is bias.

*Violation signal:* you have "SRE team" and "Platform team" as separate components when they overlap substantially.

### 7. Use appropriate methods
**Category:** Development

Agile for Genesis. Six Sigma for Commodity. Each evolution stage wants a different management style (see `climatic-patterns.md` #8). This operationalises that climatic pattern.

*Violation signal:* one methodology applied uniformly across the whole map (e.g., "we're all-in on agile").

### 8. Focus on high situational awareness
**Category:** Communication

Understand what's being considered before reacting. The map IS the situational awareness artefact — its purpose is to let you see the terrain before acting on it.

*Violation signal:* strategic decisions made without first drawing or consulting the map.

### 9. Think small (as in know the details)
**Category:** Operations

Decompose coarse components. A map with "Cloud Platform" as one node hides more than it shows. Break it into the actual constituent capabilities.

*Violation signal:* components so coarse that you can't score them on the cheat sheet.

Note: principle #20 (also "Think small") is a *different* principle about team size. Not a typo.

---

# Phase II — Becoming More Context Aware (15 principles)

### 10. Know your users
**Category:** Development

Not just the paying customer. Users include shareholders, regulators, staff, partners, suppliers. Multi-anchor maps (`|U| ≥ 2`) operationalise this — the tuple allows multiple user-need nodes.

*Violation signal:* the map has one anchor when the real business has two or more distinct user types.

### 11. Focus on the outcome not a contract
**Category:** Development

Worth-based development. Measure what value is produced, not what spec was met. Relates to pattern-based outcomes rather than feature-list completion.

### 12. Use appropriate tools
**Category:** Development

Mapping. Financial models. Pioneer-Settler-Town-Planner. The right tool depends on what you're asking. Wardley Mapping is *a* tool; don't force every question through it.

### 13. Manage inertia
**Category:** Operations

The single most-cited doctrine principle. Inertia is resistance to evolution — practices, political capital, previous investment, human capital. `inertia.md` enumerates the 17 structured forms.

*How to apply:* for every stuck component, identify which of the 17 forms apply. Don't bundle them into a generic "change management" line item.
*Violation signal:* "we tried to change it but it was too hard" with no further analysis.

### 14. Manage failure
**Category:** Operations

Address unsuccessful outcomes constructively. Pre-mortems. Post-mortems. Error budgets. Don't hide failures or let them recur.

### 15. Think FIRE (fast, inexpensive, restrained, elegant)
**Category:** Development

Formerly FIST (fast, inexpensive, simple, tiny). Applied particularly to experimentation in Genesis/Custom components. Do the smallest thing that tests the hypothesis.

*Old acronym FIST is deprecated.* Use FIRE.

### 16. Be pragmatic
**Category:** Development

Results matter more than ideology. Doctrine itself is pragmatic — override any of these principles when the map evidence warrants.

### 17. Effectiveness over efficiency
**Category:** Operations

Impact first, resource optimisation second. Don't let efficiency gains harm user-facing effectiveness. Relates to climatic pattern #24 ("Efficiency enables innovation") — you industrialise foundations to free capacity for effectiveness work.

### 18. A bias towards action
**Category:** Learning

Learn by playing the game. A map is a thinking tool, but thinking without acting produces nothing. Pick a gameplay, execute, observe, re-map.

### 19. Think aptitude and attitude
**Category:** Structure

Capability *and* mindset. The right person for a Genesis component (pioneer) is wrong for a Commodity component (town planner). Match aptitude + attitude to the evolution stage.

*Organisational, outside the formal model — but the map surfaces the mismatch.*

### 20. Think small (as in teams, two pizza)
**Category:** Structure

Small teams. Two-pizza rule (a team should be small enough to feed with two pizzas). Distinct from principle #9 which is about detail in the map; this is about team size.

*Organisational, outside the formal model.*

### 21. Distribute power and decision making
**Category:** Structure

Decentralise authority. Each team/cell should have autonomy over its part of the map. Don't funnel every decision through one strategy function.

### 22. Use standards where appropriate
**Category:** Development

Apply standardisation *selectively*. Standards are valuable at Stage IV (Commodity); they are premature at Stage I (Genesis). Standardising too early kills innovation; standardising too late leaves you with proprietary lock-in.

*Rule of thumb:* only standardise components with `ε ≥ 0.75`.

### 23. Strategy is iterative not linear
**Category:** Leading

Fast reactive cycles. Make a move, re-map, make another move. Five-year plans in Wardley mapping are suspect — the map changes faster than that.

### 24. Move fast
**Category:** Leading

"Imperfect plan executed today is better than perfect plan tomorrow." Relates to principle #18 (bias towards action) and to the map being out of date the moment you stop updating it.

---

# Phase III — Better for Less (11 principles)

### 25. Set exceptional standards
**Category:** Operations

"Great is just not good enough." This doesn't contradict #22 (use standards *where appropriate*); it's about the *quality bar* for what you do build.

### 26. Optimise flow
**Category:** Operations

Remove bottlenecks. Connects to gameplay #5 (Optimising Flow). The map reveals where flow is constrained — often at the boundary between evolution stages.

### 27. Do better with less
**Category:** Operations

Continual improvement. Minimise resource use per unit of value produced.

### 28. Seek the best
**Category:** Structure

Recruit and retain top talent. Relates to gameplay #38 (Creating centres of gravity).

*Organisational, outside the formal model.*

### 29. A bias towards the new
**Category:** Learning

Be curious, take appropriate risks. Increase exploration weight in Genesis and Custom work. Counterbalance against the natural corporate pull toward safe Commodity.

### 30. Provide purpose, mastery & autonomy
**Category:** Structure

Meaningful work, skill growth, self-direction. This is Dan Pink's *Drive*, adopted into doctrine.

*Organisational, outside the formal model.*

### 31. Strategy is complex
**Category:** Leading

There will be uncertainty. Accept it; use uncertainty distributions (Beta priors in the formal model) rather than false precision.

### 32. Commit to the direction, be adaptive along the path
**Category:** Leading

"Crossing the river by feeling the stones." Fix the direction (where you're going on the map) but let the tactical path adjust to obstacles.

### 33. There is no one culture
**Category:** Structure

Different stages want different cultures. Pioneers, Settlers, Town Planners each need different environments. Large organisations should partition their map and assign different cultures to each band.

### 34. Be humble
**Category:** Leading

Listen, be selfless, have fortitude.

*Organisational, outside the formal model.*

### 35. Be the owner
**Category:** Leading

Take responsibility.

*Organisational, outside the formal model.*

---

# Phase IV — Continuously Evolving (5 principles)

### 36. Think big
**Category:** Leading

Inspire others, provide direction. The anchor set `U` should reflect ambitious user needs, not existing products. Map to where you want to be, not only where you are.

### 37. Exploit the landscape
**Category:** Leading

Leverage the environment strategically. Don't just respond to climatic patterns — position so that climatic patterns carry you forward. Gameplay selection is how you exploit the landscape.

### 38. There is no core
**Category:** Leading

Everything is transient. Today's differentiator is tomorrow's commodity. Today's commodity is yesterday's differentiator. Plan for generation transitions (multi-wave evolution).

### 39. Listen to your ecosystems
**Category:** Learning

Ecosystems are future-sensing engines. This is the core insight behind gameplay #43 (Sensing Engines / ILC). Your ecosystem sees the market before you do.

### 40. Design for constant evolution
**Category:** Structure

Build adaptability into all systems. Don't architect for a fixed map — architect for a map that will change. Components should be replaceable; boundaries should be cleanly defined so that commoditising one component doesn't cascade.

---

## Using doctrine in a Wardley Map

When the skill produces a strategic analysis, it should cite violated doctrine principles. Common patterns:

| What the map shows | Doctrine violated | How to flag |
|---|---|---|
| Internal function as anchor (not a user) | #1, #10 | "Anchor should be user-facing need, not internal output." |
| Single anchor for a clearly two-sided business | #10 | "Use multi-anchor (`|U| ≥ 2`) — both user types matter." |
| Same methodology applied across all stages | #7 | "Apply stage-appropriate method." |
| Coarse components ("Platform", "Infrastructure") | #9 | "Decompose — you can't score a Stage for 'Platform'." |
| Stuck component with no inertia analysis | #13 | "Identify which of the 17 inertia forms applies." |
| Thin Knowledge layer | #2, #7 | "Underspecified Knowledge dependencies; expand." |
| Standardisation at Stage II | #22 | "Premature standardisation — component not yet commoditised." |
| Single evolution trajectory with no uncertainty | #31 | "Strategy is complex — use uncertainty ranges." |

---

## Doctrine vs. gameplay

| | Doctrine | Gameplay |
|---|---|---|
| Count | ~40 | ~61 |
| Context-dependent | **No** (universal) | **Yes** |
| Applied | Always | When map shape suggests it |
| Effect on math | Constraints on the mapping process | Transformations of the map |

**The common error:** invoking a gameplay without first satisfying Phase I doctrine. Example: using "Harvesting" (#29) without having "Focus on user needs" (#1) set up first — you end up harvesting components your customers don't actually need.

---

## Historical notes

1. **FIRE replaced FIST.** Older documents may use FIST (fast, inexpensive, simple, tiny). Wardley updated to FIRE (fast, inexpensive, restrained, elegant).
2. **Count drift.** Earlier enumerations had ~15 principles. The 40-principle / 4-phase / 6-category form is the mature version.
3. **Placement ambiguities.** *Be transparent* (#4) and *Think big* (#36) have moved across phases between editions.
4. **"Think small" twice on purpose.** #9 (Phase I, "know details") and #20 (Phase II, "two pizza") are distinct.

---

## Caveats

1. **Claims, not proofs.** Doctrine comes from consulting experience and military strategy. Not empirically validated that adopting more of it correlates with better outcomes.
2. **Not everything is in the math.** Principles #19, #20, #28, #30, #34, #35 are organisational practices that sit outside the `(V, E, U, ν, ε, t)` tuple.
3. **Not a checklist.** Doctrine is a growth path. Phase IV moves on a Phase I foundation will misfire.
4. **Pragmatism overrides.** Principle #16 explicitly: results matter more than ideology. Override any principle when the map evidence warrants — and be honest that you're doing so.
