# Inertia — 17 Forms (Reference)

Simon Wardley enumerates the forms of resistance to evolution. His 2016 post says *"about sixteen"* forms, but his [2013 blog post](https://blog.gardeviance.org/2013/01/intertia.html) that enumerates them in prose contains **17** — listed below.

Use when the skill identifies stuck components: name which form(s) of inertia apply rather than using a generic "high friction" label.

## Consumer side — Disruption to past norms (5)

1. **Supplier relationship change** — Changing business relationships from old suppliers to new.
2. **Sunk capital** — Loss in financial or physical capital from prior purchases.
3. **Political capital** — Loss in political capital from the person who made the prior decision.
4. **Human capital** — Loss as existing skillsets and practices change.
5. **Barrier-to-entry erosion** — Threat that lower barriers mean more competition.

## Consumer side — Transition to the new (5)

6. **Confusion over method** — "Isn't this just hosting?" kind of doubt.
7. **Supplier-trust concerns** — Transparency, trust, security of supply with new suppliers.
8. **Skill acquisition cost** — Cost of new skillsets (distributed architecture, designing for failure, etc.).
9. **Re-architecture cost** — Re-architecting legacy estates (built on N+1 / scale-up assumptions).
10. **Governance change** — Concerns over new governance and management.

## Consumer side — Agency of the new (4)

11. **Suitability doubt** — Is the activity really suitable for utility/volume operations?
12. **Second-sourcing risk** — Do we have choice? Multiple providers?
13. **Price-competition loss** — Moving from competitive product market to single-supplier lock-in.
14. **Strategic-control loss** — Increased dependency on a supplier.

## Supplier side — Resistance from past norms (3)

15. **Past-success data / cannibalisation fear** — Existing business model data + fear of cannibalising it.
16. **Rewards and culture** — Internal incentives reinforce the current model.
17. **Financial-market expectations** — Shareholders won't trade a high-margin business for utility unknowns.

---

## Note on count

The count is **17** in Wardley's primary source (the 2013 prose enumeration). He uses the phrase *"about sixteen"* in a later post, possibly because a consolidated chart merged items #15's two clauses. This skill's reference matches the 17-item primary source.

## Not inertia

Three concepts often misfiled as inertia are actually **gameplays** (see `gameplays.md`):

- **FUD** (gameplay #11)
- **Lobbying** (gameplay #13)
- **Bundling** (gameplay #8)

Gameplays are moves a player *chooses*. Inertia is resistance a player *encounters*.

## Mathematical integration

In the logistic dynamics:

    dε_v/dt = r_v(t) · ε_v(t) · (1 − ε_v(t))
    r_v(t) = r₀ + u_v(t) − c_v(t)

replace the single `c_v(t)` with a structured sum:

    c_v(t) = Σᵢ λᵢ · ιᵢ(v, t)

where `ιᵢ ∈ [0, 1]` is the severity of inertia form `i` for component `v`, and `λᵢ ≥ 0` is a per-form weight. Clamp `r_v(t)` to be non-negative — evolution is monotonic-forward.

Consumer-side and supplier-side inertia respond to different counter-measures, so tracking them separately is useful:

    c_v(t) = c_consumer + c_supplier
