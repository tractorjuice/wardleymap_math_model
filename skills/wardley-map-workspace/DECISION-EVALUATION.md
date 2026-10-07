# Decision Evaluation Protocol

Coordinate agreement measures placement similarity. It does not establish agreement on build/buy/utility recommendations or real-world decision quality. For example, coordinates 0.49 and 0.51 are close but cross a conventional stage boundary. A decision also depends on costs, capabilities, regulation, supply options and risk.

## Reference judgments and action labels

Before generating maps, record the scenario's market, observation date, constraints and stable component IDs. Have domain mappers independently recommend actions and provide rationale and evidence; adjudicate disagreements while preserving the original judgments. A published map's coordinates alone are not action labels. Do not invent reference recommendations for the existing corpus.

Use one primary action per evaluated component:

| Label | Meaning |
|---|---|
| `experiment` | Investigate feasibility or value before committing to delivery |
| `build` | Develop or materially customize the capability internally |
| `buy` | Acquire a product or contracted implementation |
| `utility` | Consume a standardized service without owning its implementation |
| `retain` | Keep the current arrangement under stated constraints |
| `abstain` | Generated answer lacks evidence for a defensible action |

`abstain` is permitted only for generated decisions. Where experts accept several actions, adjudicate a primary evaluation target or retain that case outside exact-label scoring; do not silently collapse buy and utility. The grader measures agreement with labels, not economic correctness.

## Trial and corpus design

Treat maps used for seed selection, prompt changes or regression checks as development data, even when each generation run was blind. Reserve a new corpus, disjoint from examples, tuning maps and earlier evaluation cases, before further tuning. A generation agent must not read reference placements or judgments. Public maps may also be present in model training data; disclose that limitation.

Run at least three independent trials for each new evaluation case using frozen skill/script versions, model settings and scenario prompts. Record failures and abstentions, source access, date restrictions, tokens and duration; do not retain only the best run. Extend replication across the full corpus rather than assuming the existing two-map pilot estimates all domains. Group summaries and any bootstrap intervals by map, with trials nested within maps; component pairs are not independent samples.

Compare against a majority-action baseline fitted on development cases and an independent human-mapper baseline. Keep placement metrics, dependency metrics, recommendation agreement and any user/outcome study distinct. A score is a reference-agreement result until an outcome study supports stronger claims.

## Input schema and command

Save explicitly aligned labels in this format. This fixture illustrates the schema; it is not benchmark evidence:

```json
{
  "schema_version": 1,
  "cases": [
    {
      "id": "illustrative-storage",
      "market": "example enterprise market",
      "date": "2025-01-01",
      "reference": [
        {"id": "storage", "action": "utility", "rationale": "Adjudicated expert judgment"}
      ],
      "runs": [
        {
          "id": "run-1",
          "decisions": [
            {"id": "storage", "action": "buy", "rationale": "Generated recommendation"}
          ]
        }
      ]
    }
  ]
}
```

From the repository root:

```bash
python3 tools/compare_decisions.py decisions.json > /tmp/decision-summary.json
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tools -p 'test_compare_decisions.py'
```

The grader validates labels, context and unique IDs, and uses explicit IDs rather than fuzzy name matches. Store rationale, sources and constraints in the input for human audit; the script scores labels only and does not assess their evidence. It ignores any coordinate fields.

## Interpret the output

- **Coverage:** answered reference decisions / all reference decisions. Missing IDs and abstentions remain uncovered.
- **Agreement given answer:** correct labels / answered reference decisions. Undefined when nothing is answered; always report it with coverage.
- **Correct fraction of reference:** correct labels / all reference decisions. This denominator includes missing and abstained decisions.
- **Confusion counts:** explicit reference/predicted action pairs; extra generated IDs are reported separately.
- **Macro mean:** average each case's trial scores, then average cases equally. The pooled score instead weights component count and trial count; report the distinction.

Trial standard deviation is reported only with multiple runs; a single run gets `null`, not zero uncertainty. The script does not generate confidence intervals. Report sample sizes and uncertainty from grouped analysis when real repeated trials exist. Existing coordinate summaries are historical artifacts and must not be relabeled as decision measurements.

## Validator regression check (2026-10-07)

The revised validator was applied read-only to the 50 saved `with_skill/**/draft.owm` files in iterations 10–16. It passed 49; 40 drafts produced advisory reachability warnings. The remaining draft, `iteration-14/eval-energy-disruption/with_skill/run-1/outputs/draft.owm`, repeats `Coal Generation` and `Gas CCGT Generation` declarations to add inertia markers. The current subset requires each component to be declared once, with attributes on that declaration.

This checks saved drafts, not final map-generation quality or recommendation agreement. Historical outputs and aggregate summaries were not changed. Full OWM syntax, including one-coordinate pipeline declarations, is outside this validator's supported subset and must not be described as validated by it.
