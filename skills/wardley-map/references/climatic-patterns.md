# Climatic Patterns

**Climatic patterns** are, per Simon Wardley, *"those things which change the map regardless of your actions"* — the rules of the game driven by aggregate forces like supply-and-demand competition.

They sit alongside **Doctrine** (universal organisational principles — see `doctrine.md`) and **Gameplay** (context-specific plays — see `gameplay-patterns.md`) in Wardley's strategy framework.

Where doctrine says *what you should always do*, climatic patterns say *what the environment will do to you whether you like it or not*.

---

## Provenance and count

The canonical enumeration lives in Wardley's Medium book, specifically Figure 27 in [*Exploring the map*](https://medium.com/wardleymaps/exploring-the-map-ad0266fad59b) (Chapter 3). The figure is an image; textual transcriptions by the community expand it to 27 patterns across 6 categories.

Wardley himself refers to *"about 30 common economic patterns"* in [*Doctrine, Climate and Context Specific gameplay*](https://blog.gardeviance.org/2016/04/doctrine-climate-and-context-specific.html). The exact count varies across editions; **27 is the current community consensus** and what this reference uses.

Prior versions of this repo said "23 patterns" — that was wrong.

---

## Categories

| Category | Count | Focus |
|---|---:|---|
| Competitors | 2 | How rival actors move the map |
| Components | 7 | How elements evolve |
| Financial | 5 | Value, capital, and energy flows |
| Inertia | 3 | Resistance to evolution |
| Prediction | 6 | What is and isn't forecastable |
| Speed | 4 | Rate and cadence of change |
| **Total** | **27** | |

---

## The 27 patterns

### Competitors (2)

**1. Competitor actions will change the game.**
Your rivals' moves actively reshape the landscape you're mapping. A map is not a static picture of "your" business — it is a snapshot of a contested space.
*Implication:* re-map regularly. A six-month-old map is probably obsolete.

**2. Most competitors have poor situational awareness.**
Most organisations don't map. They operate on intuition, precedent, and power politics. This is a strategic advantage for mappers — but it is not permanent.
*Implication:* you can win by being more aware than your competitors for as long as they remain unaware. Plan for the window.

### Components (7)

**3. Everything evolves through supply and demand competition.**
Activities, practices, data, and knowledge all drift from Genesis toward Commodity under competitive pressure. Nothing stays on the left forever if the market cares.
*Implication:* components you currently differentiate on will commoditise. Plan for the transition.

**4. Evolution consists of multiple waves of diffusion with many chasms.**
Evolution isn't a single smooth curve — it's many S-curves (mainframes → minicomputers → PCs → servers → VMs → cloud) separated by chasms where the old generation saturates but the new one hasn't taken off.
*Implication:* a single-logistic model of a component's evolution is incomplete. See `mathematical-models.md` §4 for the multi-wave form.

**5. No choice over evolution.**
You cannot opt out of evolution. The Red Queen forces participation; you choose only how to respond. This is the "everything evolves" pattern with teeth.
*Implication:* "we'll stick with our on-prem SAN" is not a strategy, it's a deferral.

**6. Commoditisation does not equal centralisation.**
A component can be fully industrialised yet still exist in many centralised or decentralised forms (e.g., electricity is a commodity but comes from many providers).
*Implication:* don't conflate "mature" with "monopoly". Commodity markets can still have many suppliers.

**7. Characteristics change as components evolve.**
Uncharted components (Genesis, Custom) and industrialised components (Product, Commodity) behave oppositely on almost every dimension — user perception, failure tolerance, efficiency focus, decision-making style. This is what the cheat sheet formalises.
*Implication:* apply different management practices to different parts of the map. See `evolution-stages.md`.

**8. No single method fits all.**
Agile / Lean / Six Sigma each fit a different part of the evolution axis. Agile dies on a commodity; Six Sigma dies in Genesis.
*Implication:* pick the method that matches the component's stage. Doctrine #7 ("Use appropriate methods") operationalises this.

**9. Components can co-evolve.**
Practices and activities evolve together. When an activity shifts from Product to Commodity, the practices around it shift too (often to "DevOps" / "SRE" / "infrastructure-as-code" style).
*Implication:* when you commoditise an activity, expect the supporting practices to need updating.

### Financial (5)

**10. Higher-order systems create new sources of worth.**
When a lower layer industrialises (e.g., cloud compute), new higher-order systems become possible (e.g., SaaS apps that would have been uneconomical on on-prem infra).
*Implication:* commoditising a lower layer is not just cost reduction — it unlocks new business models above it.

**11. Future value is inversely proportional to the certainty we have over it.**
Things that are novel and uncertain carry the highest potential value. Things that are certain and industrialised have the lowest differentiation value (but can be huge volume businesses).
*Implication:* balance a portfolio across the axis. Don't sit entirely on Commodity.

**12. Efficiency does not mean a reduced spend.**
Industrialising a component often *grows* total spend on it via Jevons paradox. Efficient electricity didn't reduce total electricity consumption; it grew it by orders of magnitude.
*Implication:* budgeting "we'll save X% by moving to commodity Y" often underestimates the induced demand.

**13. Evolution to higher-order systems increases energy/resource consumption.**
Aggregate consumption grows as the stack matures. Compute consumption is vastly larger in the cloud era than the mainframe era, despite each unit of compute being vastly cheaper.
*Implication:* capacity planning based on current consumption and efficiency gains is systematically wrong.

**14. Capital flows to new areas of value.**
Investment migrates toward emerging higher-order systems. VC capital chases AI; chased cloud; chased mobile before that.
*Implication:* being on the left of the axis (uncharted) attracts capital; being on the right attracts fewer, larger, more defensive investors.

### Inertia (3)

**15. Past success breeds inertia.**
Prior wins create resistance to change. The more successful you've been with the old model, the harder it is to change.
*Implication:* large incumbents are usually more inert than small insurgents. This is exploitable — see gameplay #50 (Reinforcing inertia).

**16. Inertia increases with the success of the past model.**
Not just "past success breeds inertia" but specifically: the *bigger* the past success, the *harder* it is to change. Kodak had more inertia than a small camera shop.
*Implication:* being the leader in the old paradigm is the worst position in the new paradigm.

**17. Inertia can kill an organisation.**
When evolution crosses a boundary (product to utility) and you don't, the gap between your position and the industry's kills you. See also *"Shifts from product to utility tend to demonstrate a punctuated equilibrium"* (#27).
*Implication:* monitor which components on your map are approaching a commoditisation boundary. Manage inertia actively (doctrine #13).

See `inertia.md` for the 17 structured forms of inertia.

### Prediction (6)

**18. You cannot measure evolution over time or adoption.**
This is perhaps Wardley's most-cited climatic pattern. Evolution is a *position* on a ubiquity × certainty axis, not a function of time or adoption percentage.
*Implication:* any forecast of "component X will be at stage Y by 2028" is suspect. Dynamics models (see `mathematical-models.md`) are scenario tools, not predictions.

**19. The less evolved something is, the more uncertain it is.**
Genesis and Custom Built components are inherently unpredictable. Their behaviour, cost, adoption, and even existence are open questions.
*Implication:* don't plan precise budgets or timelines for Genesis components. Use options-thinking, not project-planning.

**20. Not everything is random.**
Weak signals and patterns exist despite apparent chaos. You cannot predict individual component trajectories, but you can detect shifts (see gameplays #43 Sensing Engines, #58 Weak Signal).
*Implication:* track weak signals systematically. Publication shifts, price transparency, supplier count — these are readable.

**21. The economy has cycles.**
Peace (incremental improvement within a paradigm), War (industrialisation boundary crossing, massive structural change), and Wonder (new generation emerging) cycles recur.
*Implication:* identify which phase each component is in. Different phases reward different strategies.

**22. There are two different forms of disruption.**
- Genesis-driven disruption: new uncharted component emerges (smartphone disrupts camera). Unpredictable.
- Product-to-utility disruption: existing component industrialises (cloud disrupts on-prem). Predictable.
*Implication:* Genesis disruption requires option-thinking; product-to-utility disruption requires inertia management.

**23. A "war" (point of industrialisation) causes organisations to evolve.**
Industrialisation boundaries force rapid structural change. Companies that don't evolve die.
*Implication:* when a component is approaching utility stage, expect heavy M&A, restructuring, and consolidation in that industry.

### Speed (4)

**24. Efficiency enables innovation.**
Industrialising a lower component frees capacity for novel higher-order work. You can't innovate in application-layer AI while your team is hand-provisioning servers.
*Implication:* don't resist commoditising your foundations — it's what lets you innovate on top of them.

**25. Evolution of communication can increase the speed of evolution overall.**
Better communications infrastructure compresses evolution cycles across the whole economy (internet → social → mobile).
*Implication:* communications advances often signal acceleration across multiple other markets.

**26. Change is not always linear.**
Chasms and punctuated jumps are normal. Don't expect smooth progress; expect long quiet periods interrupted by rapid transitions.
*Implication:* plan for discontinuities. A 5-year roadmap based on linear extrapolation of the last 2 years will be wrong.

**27. Shifts from product to utility demonstrate a punctuated equilibrium.**
The pattern that causes inertia to be fatal. Product-to-utility transitions are compressed: rapid destruction of the old model + rapid creation of new models in a short window.
*Implication:* when you detect a product-to-utility transition, act fast. The window is small.

---

## How the skill uses these

When generating a Wardley Map, the skill uses climatic patterns to:

1. **Ground claims about the map's future.** Statements like "this component will commoditise" invoke patterns #3, #5. Statements like "this is a fragile position" invoke #11, #17.
2. **Justify why certain gameplays fit.** Open Approaches (#15) accelerates #3; Harvesting (#29) exploits #11; Reinforcing inertia (#50) exploits #15 and #16.
3. **Stop the reader from over-forecasting.** Every output ends with the #18 caveat: evolution is not measurable over time.
4. **Identify context.** Which phase of the Peace/War/Wonder cycle (#21) is the component in? What's the dominant disruption type (#22)?

---

## Eight key patterns to remember

If you only remember eight:

1. **#3** Everything evolves (nothing stays custom forever).
2. **#5** No choice over evolution (you can't opt out).
3. **#7** Characteristics change as components evolve (apply different management).
4. **#11** Future value is inversely proportional to certainty (options have value).
5. **#15–17** Past success breeds inertia and can kill (manage it).
6. **#18** You cannot measure evolution over time or adoption (no forecasts).
7. **#24** Efficiency enables innovation (commoditise to free capacity).
8. **#27** Product-to-utility is punctuated equilibrium (act fast when you see it).

---

## Caveats

1. **Wording varies.** Community transcriptions differ slightly on some pattern names (e.g., "Past success breeds inertia" vs "Success breeds inertia"). The meanings are stable.
2. **Count varies across editions.** Wardley says "about 30"; community lists 27; older docs cite 23 or 16. Use "around 27" as a safe number.
3. **Image-first canonical source.** Figure 27 in Wardley's Medium book is the authoritative artifact. Any text list is a transcription with possible minor drift.
4. **Not gameplays.** FUD, Lobbying, Bundling are gameplays (`gameplay-patterns.md` #11, #13, #8), not climatic patterns. Keep taxonomies separate.
