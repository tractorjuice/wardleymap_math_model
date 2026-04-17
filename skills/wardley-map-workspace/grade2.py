#!/usr/bin/env python3
"""Iteration-2 grader — same logic as iteration 1, but configs are with_skill / old_skill."""
import sys
from pathlib import Path

# Reuse grading logic from iteration-1 grader
sys.path.insert(0, str(Path(__file__).parent))
from grade import GRADERS

import json

ITERATION = Path("/workspaces/wardleymap_math_model/skills/wardley-map-workspace/iteration-2")


def main():
    for eval_dir in sorted(ITERATION.iterdir()):
        if not eval_dir.is_dir():
            continue
        grader = GRADERS.get(eval_dir.name)
        if not grader:
            continue
        for config in ["with_skill", "old_skill"]:
            out = eval_dir / config / "run-1" / "outputs" / "output.md"
            if not out.exists():
                print(f"MISSING: {out}")
                continue
            text = out.read_text()
            results = grader(text)
            passed = sum(1 for r in results if r["passed"])
            total = len(results)
            grading = {
                "eval_id": eval_dir.name,
                "config": config,
                "summary": {
                    "passed": passed,
                    "failed": total - passed,
                    "total": total,
                    "pass_rate": round(passed / total, 4) if total else 0.0,
                },
                "expectations": results,
            }
            (eval_dir / config / "run-1" / "grading.json").write_text(
                json.dumps(grading, indent=2)
            )
            print(f"{eval_dir.name}/{config}: {passed}/{total}")


if __name__ == "__main__":
    main()
