# Evolution Cheat Sheet (Reference)

Full 19-row version of Simon Wardley's evolution cheat sheet. Use this when SKILL.md's 4-row quick method is insufficient (e.g., when rows disagree or the component is unusual).

Source: Simon Wardley's [Medium book](https://medium.com/wardleymaps) (Figure 17 in *Finding a Path*) and [*What's in a Wardley Map and the need for a cheat sheet*](https://blog.gardeviance.org/2016/04/whats-in-wardley-map-and-need-for-cheat.html).

| # | Characteristic | I — Genesis | II — Custom Built | III — Product (+rental) | IV — Commodity (+utility) |
|---|---|---|---|---|---|
| 1 | Activities | Genesis | Custom | Product (+rental) | Commodity (+utility) |
| 2 | Practices | Novel | Emerging | Good | Best |
| 3 | Data | Unmodelled | Divergent | Convergent | Modelled |
| 4 | Knowledge | Concept | Hypothesis | Theory | Accepted |
| 5 | Ubiquity | Rare | Slowly increasing consumption | Rapidly increasing consumption | Widespread and stabilising |
| 6 | Certainty | Poorly understood | Rapid increases in learning | Rapid increases in use / fit for purpose | Commonly understood (in terms of use) |
| 7 | Publication Types | Describe the wonder of the thing | Build / construct / awareness and learning | Maintenance / operations / installation / features | Focused on use |
| 8 | Market | Undefined | Forming | Growing | Mature |
| 9 | Knowledge Management | Uncertain | Learning on use | Learning on operation | Known / accepted |
| 10 | Market Perception | Chaotic (non-linear) | Domain of experts | Increasing expectations of use | Ordered (appearance of being linear) / trivial |
| 11 | User Perception | Different / confusing / exciting / surprising | Leading edge / emerging | Common / disappointed if not used | Standard / expected |
| 12 | Perception in Industry | Competitive advantage / unpredictable / unknown | Competitive advantage / ROI / case examples | Advantage through implementation / features | Cost of doing business / accepted |
| 13 | Focus of Value | High future worth | Seeking profit / ROI? | High profitability | High volume / reducing margin |
| 14 | Understanding | Poorly understood / unpredictable | Increasing understanding / development of measures | Increasing education / refinement of needs | Believed well defined / stable / measurable |
| 15 | Comparison | Constantly changing / unstable | Learning from others / some evidential support | Feature difference | Essential / operational advantage |
| 16 | Failure | High / tolerated / assumed | Moderate / unsurprising but disappointed | Not tolerated, constant improvement | Operational efficiency, surprised by failure |
| 17 | Market Action | Gambling / driven by gut | Exploring a "found" value | Market analysis / listening to customers | Metric driven / build what is needed |
| 18 | Efficiency | Reducing cost of change (experimentation) | Reducing cost of waste (learning) | Reducing cost of waste (learning) | Reducing cost of deviation (volume) |
| 19 | Decision Drivers | Heritage / culture | Analysis & synthesis | Analysis & synthesis | Previous experience |

## Scoring procedure

For each row, pick the stage (1–4) that best describes the component. Convert via band midpoints:

- Stage I → 0.125, II → 0.375, III → 0.625, IV → 0.875

Average (optionally weighted) across rows:

    ε(v) = (1/|R|) · Σ m(s_r)

Variance across rows = uncertainty:

    Var(ε) = (1/|R|) · Σ (m(s_r) − ε(v))²

High variance means the component is in transition. Plot with an error bar instead of a point.

## Caveats

1. **Market-relative ubiquity.** You must name the applicable market before scoring — "widespread in enterprise" is different from "widespread for consumers".
2. **Row 19 oddity.** "Heritage / culture" at Genesis and "Previous experience" at Commodity is counter-intuitive but reflects Wardley's published table. Some practitioners dispute this row.
3. **Stages are conventions.** The quartile boundaries are conventional; Wardley doesn't fix them precisely.
4. **Not a forecast.** The cheat sheet places a component **now**, not where it's going.
