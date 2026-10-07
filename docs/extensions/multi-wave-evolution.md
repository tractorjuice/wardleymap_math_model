# Multi-Wave Adoption and Evolution Assessment

Part 1 §5 supplies a stylized evolution scenario. This extension models diffusion of multiple generations while keeping **adoption** separate from **evolution placement**. Neither model is a validated forecast.

Wardley distinguishes the evolution of an act from the diffusion of each implementation in [*Map Evolution, Not Maturity*](https://medium.com/mappingpractice/map-evolution-not-maturity-bae6ea1a2743) and [his cheat-sheet explanation](https://blog.gardeviance.org/2016/04/whats-in-wardley-map-and-need-for-cheat.html). A newly adopted utility implementation does not become Genesis merely because few customers have adopted it.

## 1. Define generations and the market

For component $v$, let $G_v$ contain implementation generations ordered by introduction. For each generation $g$, record:

- $t_g^{\mathrm{start}}$: introduction time in the named market.
- $A_g(t)\in[0,1]$: fraction of that market using the generation.
- $\varepsilon_g(t)\in[0,1]$: a separately assessed evolution placement, supported by Part 6's applicable characteristics and dated evidence.

Do not assign historical evolution scores from age or an assumed terminal stage. The generations of compute, for example, describe implementation changes; their dates alone do not score evolution.

State the denominator and whether adoption overlaps. If customers use several generations, $\sum_g A_g$ may exceed 1. These are penetration fractions, not mutually exclusive market shares. For exclusive shares, use a model with an unadopted state and transfers that conserve total share; the penetration equations below do not impose that conservation.

## 2. Adoption dynamics

### 2.1 Single-generation diffusion

For $t\ge t_g^{\mathrm{start}}$:

$$\frac{dA_g}{dt}=k_g(t)A_g(1-A_g),\qquad k_g(t)\ge0.$$

Set $A_g(t)=0$ before introduction and specify an introduction event

$$A_g(t_g^{\mathrm{start}})=a_{0,g},\qquad 0<a_{0,g}<1.$$

This is an explicit initial-condition reset at introduction. Multiplying the derivative by a start-time indicator is insufficient: a logistic trajectory initialized at exactly zero stays zero forever. Alternatively, model an external entry flow explicitly. Rates have units of inverse time.

For constant $k_g$ after introduction, the analytic solution is

$$A_g(t)=\frac{1}{1+\frac{1-a_{0,g}}{a_{0,g}}e^{-k_g(t-t_g^{\mathrm{start}})}}.$$

### 2.2 Displacement of older generations

An exploratory penetration model allows newer generations to reduce older ones:

$$\frac{dA_g}{dt}=k_g(t)A_g(1-A_g)-\sum_{g'>g}\mu_{g',g}A_{g'}A_g,\qquad \mu_{g',g}\ge0.$$

Apply this only after the relevant introduction events. It preserves each continuous-time fraction in $[0,1]$: the derivative is zero at 0 and nonpositive at 1. It does not conserve $\sum_g A_g$, nor guarantee that the assessed evolution of the act moves monotonically. Numerical integration must also respect the bounds; a large Euler step can violate them.

Use

$$k_g(t)=\max(0,k_{0,g}+u_g(t)-c_g(t))$$

for scenario actions and structured inertia, with all terms in inverse-time units. These parameters describe adoption resistance, not evidence that the market's evolution placement has reversed or stalled.

## 3. Evolution placement and a composition summary

Assess the underlying act directly against the cheat sheet in its market. Adoption simulations do not replace that assessment.

For a descriptive summary of the adopted implementations, define

$$C(v,t)=\frac{\sum_{g\in G_v}A_g(t)\varepsilon_g(t)}{\sum_{g\in G_v}A_g(t)},\qquad \sum_g A_g(t)>0.$$

$C$ is a **composition index**, not the canonical evolution coordinate $\varepsilon(v,t)$. With overlapping adoption it weights usage incidences, potentially counting the same customer more than once. With exclusive shares it is conditional on adoption. Preserve the generation profile; one mean can hide a mixture of very different implementations.

If all $A_g=0$, $C$ is undefined: report “no adopted generations,” not a zero score. A cheat-sheet assessment of the act may still be possible.

For one adopted generation,

$$C(v,t)=\varepsilon_g(t).$$

Adoption cancels. For example, $A_g=0.1$ and $\varepsilon_g=0.8$ give $C=0.8$, not $0.08$. There is no reduction to Part 1's evolution logistic unless an additional evolution dynamic is independently specified. Only the adoption equation reduces to single-generation logistic diffusion.

## 4. Chasms and strategic phases

A descriptive adoption gap between generations can be written as

$$\Delta_{g,g+1}=t_{g+1}^{\mathrm{takeoff}}-t_g^{\mathrm{saturation}},$$

with declared thresholds, such as 0.1 for takeoff and 0.9 for saturation. Positive values indicate a gap; negative values indicate overlap. If a threshold is never reached, its crossing time and the gap are undefined, or censored at the observation horizon. Inertia may delay takeoff; it does not determine the gap by itself.

Wardley's Peace / War / Wonder language concerns competitive conditions and industrialization. Assess those conditions from market evidence; do not derive the phases from arbitrary adoption quartiles. A new diffusion wave does not automatically reset the underlying act to Genesis. Generations, adoption gaps and phase labels are scenario descriptions, not a clock for predicting evolution.

## 5. Worked composition example — storage

Suppose a hypothetical named market has three implementation groups, with independently assigned scores:

| Implementation | Adoption penetration | Assessed score |
|---|---:|---:|
| On-prem SAN | 0.30 | 0.65 |
| Commodity arrays | 0.30 | 0.80 |
| Cloud object storage | 0.80 | 0.90 |

These illustrative inputs are not historical measurements or current vendor assessments. Customers may use multiple groups, so penetration sums to 1.4. The composition index is

$$C=\frac{0.30(0.65)+0.30(0.80)+0.80(0.90)}{1.40}=0.825.$$

This reports the supplied adoption-weighted profile. It does not establish the evolution placement of “storage,” which requires its own market assessment. If penetrations change to 0.05, 0.15 and 0.95 while the supplied scores stay fixed, $C\approx0.8761$. That change describes composition, not a demonstrated evolution trajectory.

## 6. Reporting requirements

Report the market and observation date, generation definitions, denominators, overlap assumptions, positive introduction seeds, rate units, source provenance and uncertainty. Keep observed assessments distinct from simulated trajectories. Check sensitivity to seeds, displacement rates and thresholds, and identify unsupported parameters. Use scenario results to discuss assumptions; do not present them as predicted evolution or automatically infer build/buy decisions.
