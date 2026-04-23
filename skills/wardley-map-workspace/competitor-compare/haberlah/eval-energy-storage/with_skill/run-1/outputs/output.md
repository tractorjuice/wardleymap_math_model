# Wardley Map Analysis: Electrical Energy Storage Landscape (April 2023)

## Purpose

Identify where the **distributed fault-tolerant grid** is evolving faster than
the **traditional single-machine control model**, and where **material supply
chain risk** is biting the energy-storage value chain, so utilities,
operators, and platform vendors can target investment and divest inertia.

## Scope Boundary

End-to-end view from consumer activity down through grid control, storage, and
underlying material supply chain. April 2023 snapshot. 18 top-level
components plus three platform sub-capabilities.

---

## Component Evolution Assessment

| Component | Stage | Position [vis, mat] | Rationale |
|---|---|---|---|
| Consumers | Commodity | [0.97, 0.88] | Universal end-user of electrical energy. Anchor. |
| Activity | Product/Commodity | [0.93, 0.72] | "Use electricity" is a universally understood, standardised activity — demand profiles are modelled at grid scale. |
| Control | Product | [0.87, 0.55] | Grid operator function is well-defined with established TSO/ISO organisations, but the control paradigm itself is under evolutionary pressure (traditional vs distributed). |
| Electricity Generation | Commodity | [0.80, 0.80] | Mature, regulated, many providers. Wholesale markets. |
| Traditional Grid | Commodity (inertia) | [0.72, 0.82] | Single-machine view is universal and standardised across incumbent TSOs, but resistant to the distributed model. Inertia marker: regulatory, capex, and operational muscle memory anchor it in place. |
| Distributed Grid | Custom-Built | [0.70, 0.30] | TCP/IP-style fault-tolerant grid — microgrids, virtual power plants, grid-forming inverter pilots. Multiple organisations building their own variants (AEMO, CAISO trials; ENTSO-E work). No off-the-shelf dominant solution yet. Strongly trending rightward. |
| SCADA | Commodity | [0.63, 0.78] | Established OT systems. IEC 60870, DNP3. Multiple vendors (GE, Siemens, ABB, Schneider). |
| Auto Generation Control (AGC) | Commodity | [0.55, 0.72] | Decades-old balancing primitive. Standard across balancing authorities. |
| Spinning Reserve | Commodity | [0.50, 0.82] | Regulated ancillary service with defined market rules and procurement. |
| Fast-Response Systems | Product | [0.48, 0.42] | Grid-forming inverters, battery frequency response (e.g., Hornsdale, FFR markets in UK). Multiple vendors, commercial product market, still actively evolving. |
| Energy Platform | Custom-Built | [0.62, 0.36] | DERMS / ADMS platforms in 2023 are largely bespoke integration projects. Early product offerings (AutoGrid, Uplight) but no dominant standard. |
| Pre-approval / Discovery | Genesis | [0.57, 0.10] | Automated DER discovery and pre-approval workflows were nascent in 2023 — IEEE 1547-2018 provided the interface, adoption was patchy. |
| Adaptive | Genesis | [0.45, 0.14] | Adaptive / self-reconfiguring platform behaviour was in research / early pilot stage. |
| Plug-and-play | Custom-Built | [0.53, 0.22] | Standards existed (IEEE 1547, OpenADR 2.0) but real PnP DER integration still required custom work. |
| Electrical Storage | Product (rental) | [0.42, 0.55] | Li-ion grid batteries a commercial product market with multiple vendors (Tesla, Fluence, BYD). Pricing still declining, feature competition active. |
| Hydro Storage | Commodity | [0.38, 0.88] | Pumped hydro is the oldest grid-scale storage. Understood, standardised, long-lived assets. |
| Hydrogen Storage | Genesis | [0.36, 0.15] | Green hydrogen for grid storage was at pilot / demonstration scale in 2023. High uncertainty on round-trip efficiency, cost trajectory. |
| Sources | Commodity | [0.26, 0.78] | Fossil, renewable, nuclear primary energy sources — regulated, traded, universal. |
| Stockpile | Product | [0.20, 0.68] | Fuel and capacity reserves — structured, regulated, well-understood but not fully commoditised across all source types. |
| Material Supply Chain | Product (inertia) | [0.13, 0.55] | Li, Co, Ni, rare-earth markets exist and function, but concentration (China processing ~70%+ of Li, ~80%+ of rare-earth refining) and long ramp times (7-10 years for new mines) create structural inertia — the market is "Product" but supply elasticity is "Custom-Built." Inertia marker warranted. |
| Supply Chain Awareness | Custom-Built | [0.08, 0.18] | Critical mineral traceability and provenance tooling was still emerging in 2023 (US IRA, EU CRMA were only just shaping requirements). Bespoke visibility projects. |

---

## Key Strategic Observations

1. **Two grid models, two evolution speeds.** The Traditional Grid sits at
   [0.72, 0.82] with inertia. The Distributed Grid sits at [0.70, 0.30] with a
   predicted evolution to 0.55 in 12-24 months. The distributed model is
   covering ~0.25 units of maturity per cycle; the traditional model moves
   <0.05. This is a textbook **climatic pattern: past success breeds inertia**
   — incumbents profited from the single-machine view and are resisting the
   evolution that TCP/IP-style fault-tolerance makes inevitable.

2. **The platform stack is compressing toward Product.** Pre-approval /
   discovery, adaptive behaviour, and plug-and-play sit in Genesis / early
   Custom-Built today, but all three have evolution arrows pointing into
   Product range by 2025. Once the platform layer commoditises, a **War phase**
   hits the incumbent control stack — AGC and SCADA-centric architectures
   lose their monopoly on grid orchestration.

3. **Storage is a three-speed market.** Hydro (commodity), Electrical
   (product, moving to commodity), Hydrogen (genesis). Strategically, the
   battle for the next decade is in Electrical Storage's rightward march and
   whether Hydrogen escapes Genesis.

4. **Material supply chain is the hidden structural risk.** Material Supply
   Chain sits in Product but carries an inertia marker — the market exists
   but supply cannot respond at the speed of downstream demand. Electrical
   Storage's evolution from 0.55 → 0.75 directly loads this node. Every unit
   of battery deployment is a unit of pressure on Li, Co, Ni, graphite, and
   rare-earth supply lines. **This is where the value chain will break
   first** if the platform and grid layers evolve on schedule.

5. **Supply chain awareness is under-invested.** At visibility 0.08 and
   maturity 0.18, it is the lowest-visibility, most-novel component, yet it
   is the only node that gives Control any early warning about the material
   node below. A genesis tooling gap at the foot of the value chain is a
   classic **doctrine failure: know your users / focus on high situational
   awareness** — operators cannot see the risk biting them.

---

## Doctrine Check

- **Know your users** — Partially. Consumers and Activity are anchored, but
  the map exposes a missing user perspective: the **grid operator as user of
  the platform layer**. Distributed Grid treats Control as a consumer but
  the platform layer should be designed around operator workflows.
- **Remove bias and duplication** — Each utility / ISO building its own
  bespoke DERMS (Energy Platform at 0.36, Custom-Built) is textbook
  doctrine-violating duplication. Sector-wide co-opting on open-source
  platform standards is the obvious counter.
- **Use appropriate methods** — The Traditional Grid is Commodity and
  correctly demands Six Sigma / ITIL discipline. Applying those methods to
  Distributed Grid (Custom-Built) or the platform capabilities (Genesis)
  would suffocate evolution. Mismatched methods are a live risk in
  vertically integrated utilities that try to manage pilots with the same
  governance as the transmission network.
- **Manage inertia** — Two inertia markers (Traditional Grid, Material
  Supply Chain) are identified explicitly. Naming them is half the battle.
- **Use standards where appropriate** — IEEE 1547-2018 and OpenADR 2.0
  exist at the platform boundary but are under-enforced. Standards adoption
  is the cheapest way to accelerate Plug-and-play's rightward march.
- **Focus on high situational awareness** — Supply Chain Awareness at
  [0.08, 0.18] is a doctrine failure: the organisation literally cannot see
  the risk it is running.

---

## Recommended Actions

1. **Invest in Distributed Grid (Custom-Built → Product).** This is the
   highest-leverage rightward move on the map. Grid-forming inverters,
   virtual power plants, and microgrid controllers are the foundation of the
   next decade's grid. Use **Pioneers** to pilot, **Settlers** to productise
   within 24 months.

2. **Open-source the Energy Platform layer.** Co-opt competitors on
   discovery, adaptive, and plug-and-play. Drive these three sub-capabilities
   from Genesis/Custom-Built to Product via shared open standards (extend
   IEEE 1547, OpenADR). This is the **Open Source Play** — commoditise a
   duplication point and compete on the differentiated layers above.

3. **Hedge Material Supply Chain before deployment scales.** Long-term
   offtake agreements, cell chemistry diversification (LFP alongside NMC),
   and stockpile policy for critical minerals. The inertia marker here is
   a hard structural constraint — the evolution of Electrical Storage
   *depends* on defusing it.

4. **Build Supply Chain Awareness as a genesis investment.** Traceability,
   provenance, and dependency graphs for critical minerals. This is the
   sensing engine for the whole lower value chain. Low-cost today, doctrine-
   aligned, and becomes regulatorily required as IRA / CRMA land.

5. **Decide explicitly on Traditional Grid inertia.** Either invest in
   managed decline (retire the single-machine paradigm on a published
   timeline) or defend it (and accept the strategic cost). The worst
   outcome is drift — resisting evolution by default while also not
   maintaining the commodity infrastructure to utility-grade reliability.

---

## Build vs. Buy Assessment

| Component | Recommendation | Rationale |
|---|---|---|
| Distributed Grid | **Build / Invest** | Custom-Built stage; competitive differentiation is still achievable; no dominant product exists. Pioneers + Settlers. |
| Energy Platform | **Build on open standards, then co-opt** | Custom-Built but evolving. Open-source core to commoditise faster than any single vendor can, capture ecosystem position. |
| Pre-approval / Discovery, Adaptive, Plug-and-play | **Build with a view to commoditise** | Genesis/Custom. Invest now, standardise fast. |
| Fast-Response Systems | **Buy** | Product stage. Commercial market (Tesla, Fluence, Wärtsilä, Hitachi Energy). Feature competition, not differentiation. |
| Electrical Storage | **Buy, with supply-chain hedging** | Product stage. Buy product, but lock in cell supply. |
| Hydrogen Storage | **Build / Pilot** | Genesis. Experimental. Only invest where the site economics actually work. |
| Hydro Storage | **Buy / Utility** | Commodity. Existing asset base. Don't build new unless geography demands it. |
| SCADA, AGC, Spinning Reserve | **Buy** | Commodity. Buy from vendors, outsource operations where appropriate. |
| Material Supply Chain | **Contract / Hedge** | Product-with-inertia. Offtakes, diversification, stockpile policy. |
| Supply Chain Awareness | **Build** | Custom-Built/Genesis. No dominant vendor. Strategic sensing capability. |

---

## Evolution Predictions (12-24 months — through mid-2025)

- **Distributed Grid**: 0.30 → 0.55 (Custom-Built → Product). Fastest move on
  the map. Driven by renewable integration pressure, grid-forming inverter
  maturity, and regulator appetite.
- **Fast-Response Systems**: 0.42 → 0.68. Product stage consolidation;
  frequency-response markets (UK Dynamic Containment, AEMO FCAS) are maturing.
- **Energy Platform**: 0.36 → 0.55. Custom-Built → Product as first-wave
  DERMS vendors consolidate and open standards harden.
- **Plug-and-play**: 0.22 → 0.45. Standards adoption accelerating.
- **Adaptive / Pre-approval**: Genesis → Custom-Built. Slower than platform
  overall — research-to-pilot transitions.
- **Electrical Storage**: 0.55 → 0.75. Product (rental) → Commodity, driven by
  LFP cell commoditisation and scale.
- **Hydrogen Storage**: 0.15 → 0.35. Genesis → Custom-Built. Slower. Depends
  on electrolyser cost curve and green-H₂ policy support (IRA 45V,
  REPowerEU).
- **Supply Chain Awareness**: 0.18 → 0.40. Pulled rightward by regulation
  (IRA, EU CRMA) more than by market demand.

**Climatic patterns in play:**
- *Past success breeds inertia* — Traditional Grid, Material Supply Chain.
- *Commoditisation enables higher-order genesis* — Fast-Response Systems
  and Energy Platform enable VPP business models that did not exist.
- *Future value is inversely proportional to certainty* — Hydrogen Storage,
  Adaptive, Supply Chain Awareness are the low-certainty / high-optionality
  bets.
- *Peace-War-Wonder* — Distributed Grid's rightward march is a **War** phase
  against the Traditional Grid control paradigm. The **Wonder** that
  follows is the genesis of grid-native applications (autonomous VPPs,
  dynamic local markets, peer-to-peer energy) above the commoditised
  distributed control layer.

---

## Open Questions

1. **Standards convergence on the platform layer.** Does IEEE 1547 + OpenADR
   + IEC 61850 converge fast enough to let Plug-and-play evolve on schedule,
   or do regional dialects fracture the market? The evolution arrow on
   Plug-and-play assumes convergence.

2. **Material supply elasticity.** Li, Co, Ni, and rare-earth extraction
   ramp times are 5-10 years. If Electrical Storage hits 0.75 by 2025 as
   predicted, is the material layer physically able to supply it, or does
   price volatility become the limiting constraint? This would pull
   Electrical Storage's evolution back.

3. **Hydrogen's Genesis → Custom-Built transition.** Is 2023-2025 the
   inflection, or does hydrogen remain stuck at Genesis because round-trip
   efficiency economics don't close? The answer determines whether the
   three-way storage mix (electrical / hydro / hydrogen) actually forms or
   whether it collapses to a two-way mix.
