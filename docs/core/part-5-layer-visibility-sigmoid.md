# Layer-Based Visibility and Optional Sigmoid Seeds

[Part 1](part-1-core-model.md) defines the current formal model; [Part 6](part-6-cheat-sheet-scoring.md) defines the proposed scoring convention over Wardley's cheat sheet. This part supplies alternative placement seeds. Its earlier claim that adoption S-curves directly describe evolution is superseded: diffusion over time and evolution placement are distinct.

## 1. Layering needs an explicit graph rule

An edge $(a,b)$ means “a depends on b.” Breadth-first search assigns **shortest** distance from an anchor. That distance can violate downward dependency ordering when a deep dependency is also directly reachable by a shortcut. BFS and topological layering are not interchangeable.

For an anchor-reachable DAG with no incoming dependency edges to anchors, use a topological ordering and define **longest-path layers**:

$$\ell(u)=0\quad(u\in U),\qquad \ell(v)=1+\max_{a:(a,v)\in E}\ell(a)\quad(v\notin U).$$

Every edge then increases layer by at least one. Topological sorting provides the processing order, not the layer number. An unreachable component needs scope or dependency review before a layer can be assigned.

For cycles, collapse strongly connected components before layering; nodes in the same component share a layer. If a component includes an anchor with incoming dependencies, review that anchor definition or use Part 1's constrained projection. Strict vertical separation around a cycle is impossible.

## 2. Convert layers to visibility seeds

A fixed decay convention gives

$$\hat\nu(v)=e^{-\alpha\ell(v)},\qquad \alpha>0.$$

Choose and record $\alpha$; the production skill uses 0.6 as a provisional convention. Adding an unrelated deeper branch does not rescale existing layers. Adding a new dependency can legitimately change layers and therefore their seeds. Mapper overrides must still satisfy the edge constraints; use Part 1's projection when needed.

The earlier relative-depth seed

$$\hat\nu(v)=1-\frac{\ell(v)}{L},\qquad L=\max_v\ell(v)$$

is an optional drawing convention for $L>0$. Adding a deeper branch changes all non-anchor coordinates, so values are not stable across map revisions. For $L=0$, assign anchors 1 without dividing by zero. Record the normalization and avoid comparing raw coordinates between differently normalized maps.

## 3. Multiple user perspectives

Keep the anchor set explicit. A combined map seeds position from the chosen graph rule across all anchors; it may conceal differences in how individual users experience a shared dependency. Separate maps or per-anchor assessments are appropriate when those perspectives differ. A single averaged coordinate cannot resolve a disagreement about scope.

## 4. An optional sigmoid score

If observable signals $x(v)$ are used for a provisional seed, a bounded transformation is

$$\hat\varepsilon(v)=\sigma(b+w^\top x(v))=\frac{1}{1+e^{-(b+w^\top x(v))}}.$$

The intercept $b$, weights $w$, signal definitions and normalization must be stated. A sigmoid bounds the output; it does not establish that the signals measure evolution or that the output is calibrated. Its nonlinearity is a scoring choice, not evidence of an adoption trajectory.

Cross-check the seed against applicable cheat-sheet characteristics. Where evidence conflicts, preserve the characteristic profile and explain the adjustment. Do not tune weights against the final evaluation corpus or interpret fitted coordinates as forecast probabilities.

## 5. Diffusion scenarios are separate

Logistic adoption can model the penetration of a particular implementation under scenario assumptions. It cannot determine the evolution placement of the underlying act. For separate adoption variables, introduction events, displacement assumptions and composition summaries, use the [multi-wave extension](../extensions/multi-wave-evolution.md).

## 6. Practical workflow

1. Name the market, observation date, users and user needs.
2. Declare the depends-on graph; review disconnected nodes, cycles and anchor definitions.
3. Choose one layering rule and record its parameters.
4. Seed visibility, then check every dependency after mapper overrides.
5. Assess evolution using Part 6; preserve sources, row disagreement and evidence confidence separately.
6. If simulating adoption, label its trajectories as scenarios and keep them separate from assessed coordinates.

Layering and sigmoid seeds organize assumptions. Claims of improved accuracy require independent evaluation, repeated assessments and sensitivity checks.
