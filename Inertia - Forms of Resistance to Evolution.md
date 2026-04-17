# Inertia — Forms of Resistance to Evolution

In Wardley Mapping, **inertia** is resistance to the forces of evolution: the reasons why a component that *should* be moving rightward on the X-axis doesn't, or moves slower than market conditions would suggest. Part 1 §5 bundles inertia into a single scalar $c_v(t)$. That is a flattening of a structured concept Wardley enumerates in detail. This doc enumerates the forms and gives a structured drag term that replaces $c_v(t)$.

---

## 1. Wardley's enumeration

**Primary source**: Simon Wardley, ["Bits or pieces? — Inertia"](https://blog.gardeviance.org/2013/01/intertia.html) (2013). Referenced also in ["A pet favourite — Inertia"](https://blog.gardeviance.org/2014/02/a-pet-favourite-inertia.html) (2014, consolidated chart as Figure 3) and ["Wardley's Doctrine"](https://blog.gardeviance.org/2016/05/wardleys-doctrine.html) (2016).

Wardley writes there are **"about sixteen"** forms of inertia. The 2013 blog post that enumerates them in full contains **17** items, grouped under four headings (three consumer-side, one supplier-side). The "about sixteen" phrasing appears to reflect a consolidated chart, not a precise count; the 17-item list is what Wardley actually published in prose.

We reproduce all 17 below, grouped as Wardley groups them, quoting his wording where it is short enough.

### Group A — Consumer: disruption to past norms (5)

1. **Supplier relationship change.** Changing business relationships from old suppliers to potentially new suppliers.
2. **Sunk capital.** A loss in financial or physical capital through prior purchasing of a product — the previous investment has to be written off.
3. **Political capital.** A loss in political capital through having been the person who made the prior purchasing decision.
4. **Human capital.** A loss in human capital as existing skillsets and practices change.
5. **Barrier-to-entry erosion.** A threat that barriers to entry will be reduced, resulting in increased competition.

### Group B — Consumer: transition to the new (5)

6. **Confusion over method.** Confusion over the new methods of providing the activity (e.g., "isn't this just hosting?").
7. **Supplier-trust concerns.** Concerns over the new suppliers as relationships are reformed — transparency, trust, security of supply.
8. **Skill acquisition cost.** Cost of acquiring new skillsets as practices co-evolve (designing for failure, distributed architecture, etc.).
9. **Re-architecture cost.** Cost of re-architecting existing estates that consume the activity (legacy built on N+1 / scale-up assumptions).
10. **Governance change.** Concerns over changes to governance and management.

### Group C — Consumer: agency of the new (4)

11. **Suitability doubt.** Suitability of the activity for provision in this new form (is it really suitable for utility/volume operations?).
12. **Second-sourcing risk.** Lack of second-sourcing options (do we have choice? are there multiple providers?).
13. **Price-competition loss.** Existence of pricing competition and switching between alternative suppliers — moving from a competitive product market to single-supplier lock-in.
14. **Strategic-control loss.** Loss of strategic control through increased dependency on a supplier.

### Group D — Supplier: resistance from past norms (3)

15. **Past-success data / cannibalisation fear.** "All the data the company has demonstrates the past success of current business models and concerns would be raised over cannibalisation of the existing business."
16. **Rewards and culture.** "The rewards and culture of the company are likely to be built on the current business model hence reinforcing internal resistance to change."
17. **Financial-market expectations.** "External expectations of the financial markets are likely to reinforce continual improvement of the existing model" — shareholders won't swap a high-margin business for an unestablished utility one.

> **Note on the count.** Wardley's own 2016 post says *"about sixteen"*; his 2013 enumeration has 17. The cleanest way to get exactly 16 is to merge #15's two clauses ("past-success data" and "cannibalisation fear") into a single form, but that is a reconciliation, not a direct quote. This document presents 17 because that is what the primary source publishes.

> **What is NOT inertia.** Three concepts commonly misfiled here — **FUD (Fear, Uncertainty, Doubt)**, **Lobbying**, and **Bundling** — are Wardley **gameplays** from his [61 gameplays catalogue](https://blog.gardeviance.org/2015/05/on-61-different-forms-of-gameplay.html), not forms of inertia. Gameplays are strategic moves that a player may choose; inertia is the resistance a strategist encounters. Keep the taxonomies separate.

---

## 2. Formalizing inertia in the dynamics

Part 1 §5 gave the logistic evolution dynamics:

$$\frac{d\varepsilon_v}{dt} = r_v(t)\,\varepsilon_v(t)\,(1-\varepsilon_v(t))$$

with $r_v(t) = r_{0,v} + u_v(t) - c_v(t)$, where $c_v(t)$ was an unspecified "inertia" scalar. Replace it with a structured sum over the 17 forms:

$$c_v(t) = \sum_{i=1}^{17} \lambda_i \cdot \iota_i(v, t)$$

Where:
- $\iota_i(v, t) \in [0,1]$ is the **severity** of inertia form $i$ for component $v$ at time $t$ — 0 if the form doesn't apply, 1 if it is a dominant drag.
- $\lambda_i \ge 0$ is a **weight** per form — how much this form slows evolution relative to the others. The default $\lambda_i = \lambda$ (uniform) is a reasonable starting point; calibrate against observed history if you can.

### 2.1 Consumer vs. supplier decomposition

Consumer-side (forms 1–14) and supplier-side (forms 15–17) inertia can be tracked separately since they respond to different counter-measures:

$$c_v(t) = c_v^{\text{consumer}}(t) + c_v^{\text{supplier}}(t)$$

- Consumer-side inertia is addressed by **enabling transition** — education, migration tooling, second-sourcing options.
- Supplier-side inertia is addressed by **incentive redesign** — changing rewards, managing market expectations, isolating the new business model from the old P&L.

Mixing them into one scalar loses this actionable distinction.

### 2.2 Observable proxies

Some forms have plausible quantitative proxies; most do not.

| Form | Possible proxy |
|---|---|
| 2. Sunk capital | Book value of existing systems / annual capex |
| 4. Human capital | Size of team holding obsolete skills |
| 8. Skill acquisition cost | Training-cost estimate for required new skills |
| 9. Re-architecture cost | Estimated rewrite effort (engineer-months) |
| 12. Second-sourcing risk | Herfindahl-Hirschman index of supplier market |
| 16. Rewards and culture | Fraction of executive compensation tied to existing model |

For the rest, treat $\iota_i$ as a mapper-assigned score on $\{0, 0.25, 0.5, 0.75, 1\}$, like a cheat-sheet row.

### 2.3 Bounded rate constraint

Inertia is a drag, not a reversal. If $c_v(t) > r_{0,v} + u_v(t)$ the raw rate $r_v(t)$ would go negative — evolution moving backwards. Wardley's climatic patterns ("everything evolves", "no choice over evolution") treat evolution as monotonic-forward, so clamp:

$$r_v(t) = \max\!\left(0,\; r_{0,v} + u_v(t) - c_v(t)\right)$$

This stalls evolution rather than reversing it.

---

## 3. Worked example — private-cloud → public-cloud migration (2015 enterprise)

A component "Compute Platform" sitting at $\varepsilon \approx 0.55$ (Product/Rental) that *should* be evolving toward $\varepsilon \approx 0.9$ (Commodity/Utility). Why it's stuck:

| Form | Severity $\iota_i$ | Notes |
|---|---|---|
| 2. Sunk capital | 0.9 | Three-year amortisation on on-prem hardware |
| 3. Political capital | 0.7 | CIO championed the private-cloud build-out two years ago |
| 4. Human capital | 0.6 | Ops team's skills are VMware/Cisco, not AWS |
| 7. Supplier-trust concerns | 0.5 | Security/compliance uncertainty over public cloud |
| 9. Re-architecture cost | 0.8 | Legacy apps assume scale-up VMs |
| 14. Strategic-control loss | 0.6 | "We don't want to be locked into AWS" |
| 15. Past-success data | 0.4 | (This is supplier-side; barely applies to the consumer org) |

With uniform weight $\lambda_i = 0.1$ and $r_{0,v} = 0.2$:

$$c_v = 0.1 \cdot (0.9 + 0.7 + 0.6 + 0.5 + 0.8 + 0.6 + 0.4) = 0.45$$

$$r_v = \max(0, 0.2 + 0 - 0.45) = 0$$

Evolution stalls — consistent with what actually happened in many 2014–2017 enterprise clouds. To unstick, the $u_v(t)$ strategy term must target the specific forms (amortisation write-off plan for #2, retraining budget for #4, compliance review for #7, etc.) rather than generically "push harder."

---

## 4. When inertia itself evolves

Inertia is not constant. Past-success data (#15) weakens as the old business model's numbers deteriorate. Re-architecture cost (#9) falls as migration tooling matures. So $\iota_i(v, t)$ is a function of time, and modeling it as constant over a scenario horizon is a simplification.

A second-order refinement: inertia of form $i$ decays on its own timescale $\tau_i$:

$$\frac{d\iota_i}{dt} = -\frac{\iota_i(v,t)}{\tau_i} + \text{shocks}(t)$$

Different forms have very different $\tau_i$. Sunk capital decays on the asset depreciation schedule (years). Political capital decays on the executive tenure cycle (months to years). Financial-market expectations can snap over a single earnings call.

---

## 5. Relationship to doctrine and gameplay

- **Doctrine** ("Know your users", "Remove bias and duplication", etc.) reduces the baseline level of many inertia forms — a well-run organisation simply has less accumulated drag.
- **Gameplays** (open-source, standards-setting, bundling, FUD) are targeted interventions: some raise inertia in competitors (e.g., FUD); others lower it in the market (open-source).

Inertia lives between these: doctrine sets the background, gameplay changes the specifics.
