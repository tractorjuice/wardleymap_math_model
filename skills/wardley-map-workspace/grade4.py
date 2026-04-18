#!/usr/bin/env python3
"""Iteration-4 grader — same as iter-3 logic."""
import sys, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from grade import GRADERS

ITERATION = Path("/workspaces/wardleymap_math_model/skills/wardley-map-workspace/iteration-4")

for eval_dir in sorted(ITERATION.iterdir()):
    if not eval_dir.is_dir():
        continue
    grader = GRADERS.get(eval_dir.name)
    if not grader:
        continue
    out = eval_dir / "with_skill" / "run-1" / "outputs" / "output.md"
    if not out.exists():
        print(f"MISSING: {out}")
        continue
    text = out.read_text()
    results = grader(text)
    passed = sum(1 for r in results if r["passed"])
    total = len(results)
    grading = {
        "eval_id": eval_dir.name,
        "config": "with_skill",
        "summary": {"passed": passed, "failed": total - passed, "total": total,
                    "pass_rate": round(passed/total, 4) if total else 0.0},
        "expectations": results,
    }
    (eval_dir / "with_skill" / "run-1" / "grading.json").write_text(json.dumps(grading, indent=2))
    print(f"{eval_dir.name}: {passed}/{total}")
