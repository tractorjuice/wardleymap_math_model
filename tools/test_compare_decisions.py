import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from compare_decisions import compare


def corpus():
    return {
        "schema_version": 1,
        "cases": [{
            "id": "example", "market": "illustrative market", "date": "2025-01-01",
            "reference": [{"id": "a", "action": "build", "evolution": 0.49},
                          {"id": "b", "action": "utility"}],
            "runs": [{"id": "run-1", "decisions": [
                {"id": "a", "action": "buy", "evolution": 0.51},
                {"id": "b", "action": "utility"}]}],
        }],
    }


class DecisionComparisonTests(unittest.TestCase):
    def test_close_coordinates_do_not_hide_different_recommendations(self):
        result = compare(corpus())
        self.assertEqual(result["pooled"]["agreement_given_answer"], 0.5)
        self.assertEqual(result["pooled"]["coverage"], 1)
        self.assertIsNone(result["cases"][0]["trial_stdev_correct_fraction_of_reference"])
        self.assertIn({"reference": "build", "predicted": "buy", "count": 1},
                      result["cases"][0]["runs"][0]["confusion"])

    def test_missing_abstained_and_extra_ids_do_not_inflate_accuracy(self):
        doc = corpus()
        doc["cases"][0]["runs"][0]["decisions"] = [
            {"id": "a", "action": "abstain"}, {"id": "extra", "action": "build"}]
        result = compare(doc)
        run = result["cases"][0]["runs"][0]
        self.assertEqual(run["missing_ids"], ["b"])
        self.assertEqual(run["abstained_ids"], ["a"])
        self.assertEqual(run["extra_ids"], ["extra"])
        self.assertIsNone(result["pooled"]["agreement_given_answer"])
        self.assertEqual(result["pooled"]["correct_fraction_of_reference"], 0)

    def test_empty_predictions_are_reported_as_unanswered(self):
        doc = corpus()
        doc["cases"][0]["runs"][0]["decisions"] = []
        self.assertEqual(compare(doc)["pooled"]["coverage"], 0)

    def test_case_macro_average_does_not_overweight_more_trials(self):
        doc = corpus()
        first = doc["cases"][0]
        first["runs"].append({"id": "run-2", "decisions": first["reference"]})
        second = copy.deepcopy(first)
        second["id"] = "second"
        second["runs"] = [{"id": "run-1", "decisions": []}]
        doc["cases"].append(second)
        result = compare(doc)
        self.assertEqual(result["macro_mean_correct_fraction_of_reference"], 0.375)
        self.assertEqual(result["pooled"]["correct_fraction_of_reference"], 0.5)
        self.assertGreater(result["cases"][0]["trial_stdev_correct_fraction_of_reference"], 0)

    def test_rejects_invalid_actions_duplicate_ids_and_missing_context(self):
        variants = []
        doc = corpus()
        doc["cases"][0]["reference"][0]["action"] = "abstain"
        variants.append(doc)
        doc = corpus()
        doc["cases"][0]["runs"][0]["decisions"].append({"id": "a", "action": "build"})
        variants.append(doc)
        doc = corpus()
        doc["cases"][0]["runs"].append(doc["cases"][0]["runs"][0])
        variants.append(doc)
        doc = corpus()
        doc["cases"][0].pop("market")
        variants.append(doc)
        doc = corpus()
        doc["cases"].append(doc["cases"][0])
        variants.append(doc)
        variants.extend([{}, {"schema_version": 1, "cases": []}, {"schema_version": True, "cases": []}])
        for doc in variants:
            with self.subTest(doc=doc), self.assertRaises(ValueError):
                compare(doc)

    def test_cli_outputs_scores_and_rejects_malformed_input(self):
        script = Path(__file__).with_name("compare_decisions.py")
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "decisions.json"
            path.write_text(json.dumps(corpus()))
            result = subprocess.run([sys.executable, str(script), str(path)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0)
            self.assertEqual(json.loads(result.stdout)["trial_count"], 1)
            path.write_text('{"schema_version": 1, "cases": []}')
            result = subprocess.run([sys.executable, str(script), str(path)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertIn("Invalid decision evaluation", result.stderr)


if __name__ == "__main__":
    unittest.main()
