#!/usr/bin/env python3
"""Compare explicitly labeled recommendations; never infer actions from coordinates.

Usage: python3 tools/compare_decisions.py decisions.json
See skills/wardley-map-workspace/DECISION-EVALUATION.md for the input schema.
Prints JSON to stdout; does not overwrite benchmark artifacts.
"""
import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from statistics import mean, stdev

ACTIONS = {"experiment", "build", "buy", "utility", "retain"}


def nonempty_string(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be a nonempty string")
    return value


def decisions_by_id(items, label, allow_abstain=False):
    if not isinstance(items, list):
        raise ValueError(f"{label} must be a list")
    result = {}
    for item in items:
        if not isinstance(item, dict):
            raise ValueError(f"{label} entries must be objects")
        identity = nonempty_string(item.get("id"), f"{label} id")
        if identity in result:
            raise ValueError(f"duplicate decision id in {label}: {identity}")
        action = item.get("action")
        if not isinstance(action, str) or action not in ACTIONS | ({"abstain"} if allow_abstain else set()):
            raise ValueError(f"invalid action in {label}: {action!r}")
        result[identity] = action
    return result


def score_run(reference, predicted):
    reference_ids = set(reference)
    abstained = reference_ids & {key for key, action in predicted.items() if action == "abstain"}
    answered = (reference_ids & set(predicted)) - abstained
    correct = sum(reference[key] == predicted[key] for key in answered)
    confusion = Counter((reference[key], predicted[key]) for key in answered)
    return {
        "reference_count": len(reference),
        "answered_count": len(answered),
        "correct_count": correct,
        "coverage": len(answered) / len(reference),
        "agreement_given_answer": correct / len(answered) if answered else None,
        "correct_fraction_of_reference": correct / len(reference),
        "missing_ids": sorted(reference_ids - set(predicted)),
        "abstained_ids": sorted(abstained),
        "extra_ids": sorted(set(predicted) - reference_ids),
        "confusion": [{"reference": ref, "predicted": pred, "count": count}
                      for (ref, pred), count in sorted(confusion.items())],
    }


def compare(document):
    if not isinstance(document, dict) or type(document.get("schema_version")) is not int or document["schema_version"] != 1:
        raise ValueError("input must be an object with schema_version=1")
    cases = document.get("cases")
    if not isinstance(cases, list) or not cases:
        raise ValueError("cases must be a nonempty list")
    summaries = []
    seen_cases = set()
    for case in cases:
        if not isinstance(case, dict):
            raise ValueError("case entries must be objects")
        identity = nonempty_string(case.get("id"), "case id")
        if identity in seen_cases:
            raise ValueError(f"duplicate case id: {identity}")
        seen_cases.add(identity)
        market = nonempty_string(case.get("market"), "market")
        date = nonempty_string(case.get("date"), "observation date")
        reference = decisions_by_id(case.get("reference"), "reference")
        if not reference:
            raise ValueError(f"case {identity} needs at least one reference decision")
        runs = case.get("runs")
        if not isinstance(runs, list) or not runs:
            raise ValueError(f"case {identity} needs a nonempty runs list")
        scores = []
        seen_runs = set()
        for run in runs:
            if not isinstance(run, dict):
                raise ValueError("run entries must be objects")
            run_id = nonempty_string(run.get("id"), "run id")
            if run_id in seen_runs:
                raise ValueError(f"duplicate run id in {identity}: {run_id}")
            seen_runs.add(run_id)
            predicted = decisions_by_id(run.get("decisions"), "prediction", allow_abstain=True)
            scores.append({"id": run_id, **score_run(reference, predicted)})
        fractions = [score["correct_fraction_of_reference"] for score in scores]
        summaries.append({
            "id": identity, "market": market, "date": date, "runs": scores,
            "mean_correct_fraction_of_reference": mean(fractions),
            "trial_stdev_correct_fraction_of_reference": stdev(fractions) if len(fractions) > 1 else None,
        })
    scores = [run for case in summaries for run in case["runs"]]
    ref_count = sum(run["reference_count"] for run in scores)
    answered = sum(run["answered_count"] for run in scores)
    correct = sum(run["correct_count"] for run in scores)
    return {
        "schema_version": 1,
        "case_count": len(summaries), "trial_count": len(scores),
        "pooled": {
            "reference_count": ref_count, "answered_count": answered, "correct_count": correct,
            "coverage": answered / ref_count,
            "agreement_given_answer": correct / answered if answered else None,
            "correct_fraction_of_reference": correct / ref_count,
        },
        "macro_mean_correct_fraction_of_reference": mean(case["mean_correct_fraction_of_reference"] for case in summaries),
        "cases": summaries,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        result = compare(json.loads(args.input.read_text()))
    except (OSError, ValueError) as error:
        parser.exit(1, f"Invalid decision evaluation: {error}\n")
    json.dump(result, sys.stdout, indent=2, allow_nan=False)
    print()


if __name__ == "__main__":
    main()
