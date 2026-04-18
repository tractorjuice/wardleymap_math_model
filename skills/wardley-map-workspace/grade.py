#!/usr/bin/env python3
"""Grade wardley-map skill outputs against eval assertions.

Writes grading.json into each run directory (with_skill/ and without_skill/).
"""
from __future__ import annotations
import json
import re
from pathlib import Path

ITERATION = Path("/workspaces/wardleymap_math_model/skills/wardley-map-workspace/iteration-1")

# Known Wardley gameplay names from the 61-play catalogue
GAMEPLAY_NAMES = [
    "Focus on user needs", "Situational Awareness", "Effective & Efficient",
    "Structure & Culture", "Optimising Flow", "Channel Conflict",
    "Education", "Bundling", "Creating artificial needs", "Confusion of Choice",
    "FUD", "Artificial competition", "Lobbying",
    "Market Enablement", "Open Approaches", "Exploiting Network Effects",
    "Co-operation", "Industrial Policy",
    "Exploiting existing constraints", "Patents & IPR", "Creating constraints",
    "Limitation of competition",
    "Disposal of liability", "Sweat & Dump", "Pig in a poke",
    "Differentiation", "Pricing policy", "Exploiting buyer", "Harvesting",
    "Standards game", "Signal distortion",
    "Threat acquisition", "Raising barriers to entry", "Procrastination",
    "Defensive regulation",
    "Directed investment", "Experimentation", "Creating centres of gravity",
    "Undermining barriers to entry", "Fool's mate",
    "Alliances", "Co-creation", "Sensing Engines", "Tower and Moat",
    "Two factor", "Co-opting", "Embrace & Extend",
    "Tech Drops", "Fragmentation", "Reinforcing inertia", "Sapping",
    "Misdirection", "Restriction", "Talent Raid",
    "Land grab", "First mover", "Fast follower", "Weak Signal",
    "Licensing", "Insertion", "Design to fail",
]


def find_owm_block(text: str) -> str:
    """Extract an OWM block or use the whole text if no explicit block."""
    m = re.search(r"```owm\s*\n(.*?)\n```", text, re.DOTALL)
    if m:
        return m.group(1)
    # Fallback: any code block with title + anchor + component
    for m in re.finditer(r"```[\w]*\s*\n(.*?)\n```", text, re.DOTALL):
        block = m.group(1)
        if "anchor" in block and "component" in block and "->" in block:
            return block
    return text  # last resort, scan whole text


def parse_coords(line: str) -> tuple[str, float, float] | None:
    """Extract 'name [v, e]' from a component/anchor line. Returns (name, v, e)."""
    m = re.match(r"\s*(?:anchor|component)\s+(.+?)\s*\[\s*([0-9.]+)\s*,\s*([0-9.]+)\s*\]", line)
    if m:
        return m.group(1).strip(), float(m.group(2)), float(m.group(3))
    return None


def parse_edges(owm: str) -> list[tuple[str, str]]:
    edges = []
    for line in owm.splitlines():
        m = re.match(r"\s*([^->/]+?)\s*->\s*([^-]+?)\s*$", line)
        if m and "//" not in line and "anchor" not in line and "component" not in line:
            edges.append((m.group(1).strip(), m.group(2).strip()))
    return edges


def coord_map(owm: str) -> dict[str, tuple[float, float]]:
    coords = {}
    for line in owm.splitlines():
        parsed = parse_coords(line)
        if parsed:
            name, v, e = parsed
            coords[name] = (v, e)
    return coords


def count_components(owm: str) -> int:
    return sum(1 for line in owm.splitlines() if re.match(r"\s*component\s+", line))


def count_anchors(owm: str) -> int:
    return sum(1 for line in owm.splitlines() if re.match(r"\s*anchor\s+", line))


def anchor_names(owm: str) -> list[str]:
    names = []
    for line in owm.splitlines():
        m = re.match(r"\s*anchor\s+(.+?)\s*\[", line)
        if m:
            names.append(m.group(1).strip().lower())
    return names


def check_visibility_constraint(owm: str) -> tuple[bool, str]:
    coords = coord_map(owm)
    edges = parse_edges(owm)
    if not edges:
        return False, "no edges parsed"
    violations = []
    checked = 0
    for a, b in edges:
        if a in coords and b in coords:
            checked += 1
            if coords[a][0] < coords[b][0]:
                violations.append(f"{a}({coords[a][0]}) < {b}({coords[b][0]})")
    if checked == 0:
        return False, "no edge endpoints matched to coordinates"
    if violations:
        return False, f"{len(violations)}/{checked} edges violate: " + "; ".join(violations[:3])
    return True, f"all {checked} edges respect nu(a) >= nu(b)"


def check_coords_in_range(owm: str) -> tuple[bool, str]:
    coords = coord_map(owm)
    if not coords:
        return False, "no coordinates parsed"
    out_of_range = [n for n, (v, e) in coords.items() if not (0 <= v <= 1 and 0 <= e <= 1)]
    if out_of_range:
        return False, f"out of [0,1]: {out_of_range[:3]}"
    return True, f"all {len(coords)} coordinates in [0,1]"


def has_gameplay(text: str) -> tuple[bool, str]:
    found = [g for g in GAMEPLAY_NAMES if g.lower() in text.lower()]
    if found:
        return True, f"cites: {', '.join(found[:3])}"
    return False, "no named gameplays found"


def grade_tea_shop(text: str) -> list[dict]:
    owm = find_owm_block(text)
    anchors = anchor_names(owm)
    coords = coord_map(owm)
    ncomp = count_components(owm)

    results = []
    # 1. OWM block
    has_owm = "anchor" in owm and "component" in owm and "->" in owm
    results.append({"text": "Output contains an OWM-format block", "passed": has_owm,
                    "evidence": "OWM block found" if has_owm else "no OWM structure"})
    # 2. Customer/user anchor at high visibility
    anchor_ok = False
    anchor_evidence = "no customer/user anchor"
    for line in owm.splitlines():
        m = re.match(r"\s*anchor\s+(.+?)\s*\[\s*([0-9.]+)\s*,", line)
        if m:
            name = m.group(1).lower()
            vis = float(m.group(2))
            if any(k in name for k in ["customer", "user", "public", "buyer", "client"]):
                if vis >= 0.9:
                    anchor_ok = True
                    anchor_evidence = f"{name} at vis={vis}"
                    break
                else:
                    anchor_evidence = f"{name} at vis={vis} (below 0.9)"
    results.append({"text": "Has a customer/user anchor at high visibility (>=0.9)",
                    "passed": anchor_ok, "evidence": anchor_evidence})
    # 3. At least 5 components
    results.append({"text": "At least 5 components identified", "passed": ncomp >= 5,
                    "evidence": f"{ncomp} components"})
    # 4. Coords in [0,1]
    ok, ev = check_coords_in_range(owm)
    results.append({"text": "Every component has [visibility, evolution] coordinates in [0,1]",
                    "passed": ok, "evidence": ev})
    # 5. Visibility constraint
    ok, ev = check_visibility_constraint(owm)
    results.append({"text": "Visibility constraint respected: for every edge a->b, nu(a) >= nu(b)",
                    "passed": ok, "evidence": ev})
    # 6. Canonical stage naming
    canon = "(+utility)" in text or "(+rental)" in text
    results.append({"text": "Uses canonical stage naming (+utility or +rental appears)",
                    "passed": canon,
                    "evidence": "found canonical" if canon else "neither +utility nor +rental found"})
    # 7. Strategic analysis present
    strat = all(k in text.lower() for k in ["differentiation", "commodity", "risk"]) or \
            all(k in text for k in [" D", " K", " R"])
    results.append({"text": "Strategic analysis present (covers D, K, R)",
                    "passed": strat,
                    "evidence": "found strategic terms" if strat else "strategic analysis terms missing"})
    # 8. Gameplay cited
    ok, ev = has_gameplay(text)
    results.append({"text": "Cites at least one specific Wardley gameplay by name",
                    "passed": ok, "evidence": ev})
    # 9. Caveat
    caveat = ("cannot measure evolution" in text.lower() or
              ("scenario" in text.lower() and "forecast" in text.lower()) or
              "climatic pattern" in text.lower())
    results.append({"text": "Caveat present that evolution is not time/maturity (scenario not forecast)",
                    "passed": caveat,
                    "evidence": "found scenario/forecast/climatic caveat" if caveat else "no evolution caveat"})
    return results


def grade_freelance(text: str) -> list[dict]:
    owm = find_owm_block(text)
    anchors = anchor_names(owm)
    nanchors = count_anchors(owm)

    results = []
    has_owm = "anchor" in owm and "component" in owm and "->" in owm
    results.append({"text": "Output contains an OWM-format block", "passed": has_owm,
                    "evidence": "OWM block found" if has_owm else "no OWM structure"})
    results.append({"text": "Uses TWO anchors (two 'anchor' lines) for the two user types",
                    "passed": nanchors >= 2,
                    "evidence": f"{nanchors} anchors: {anchors}"})
    # Both roles
    roles_ok = any(
        any(c in a for c in ["client", "buyer", "customer"]) for a in anchors
    ) and any(
        any(f in a for f in ["freelance", "worker", "seller", "provider"]) for a in anchors
    )
    results.append({"text": "Both anchors represent distinct roles (e.g., client and freelancer)",
                    "passed": roles_ok, "evidence": f"anchors: {anchors}"})
    # High visibility anchors
    coords = coord_map(owm)
    anchor_vis_ok = False
    for line in owm.splitlines():
        if re.match(r"\s*anchor\s+", line):
            parsed = parse_coords(line)
            if parsed and parsed[1] < 0.9:
                anchor_vis_ok = False
                break
            anchor_vis_ok = True
    results.append({"text": "Both anchors at high visibility (>=0.9)", "passed": anchor_vis_ok,
                    "evidence": f"anchors: {anchors}"})
    # Platform component
    platform = any(
        k in line.lower() for line in owm.splitlines() if re.match(r"\s*component\s+", line)
        for k in ["platform", "match", "marketplace"]
    )
    results.append({"text": "A platform/matching/marketplace component exists",
                    "passed": platform,
                    "evidence": "found" if platform else "not found"})
    # Two-sided dynamic
    two_sided = any(k in text.lower() for k in ["two-sided", "two sided", "network effect",
                                                   "two factor", "exploiting network"])
    results.append({"text": "Strategic analysis recognizes the two-sided dynamic",
                    "passed": two_sided, "evidence": "found" if two_sided else "not mentioned"})
    # Recommendations
    recs = all(k in text.lower() for k in ["build", "outsource"]) or \
           all(k in text.lower() for k in ["invest", "outsource"])
    results.append({"text": "Gives specific invest/outsource recommendations per component",
                    "passed": recs, "evidence": "found build/outsource terms" if recs else "missing"})
    # Gameplay
    ok, ev = has_gameplay(text)
    results.append({"text": "Cites at least one specific Wardley gameplay by name",
                    "passed": ok, "evidence": ev})
    return results


def grade_saas(text: str) -> list[dict]:
    owm = find_owm_block(text)
    ncomp = count_components(owm)
    coords = coord_map(owm)

    results = []
    has_owm = "anchor" in owm and "component" in owm and "->" in owm
    results.append({"text": "Output contains an OWM-format block", "passed": has_owm,
                    "evidence": "OWM block found" if has_owm else "no OWM structure"})
    results.append({"text": "At least 5 components identified", "passed": ncomp >= 5,
                    "evidence": f"{ncomp} components"})
    ok, ev = check_coords_in_range(owm)
    results.append({"text": "Every component has coordinates in [0,1]", "passed": ok, "evidence": ev})
    # Build/buy/outsource recs
    recs = all(k in text.lower() for k in ["build", "buy", "outsource"])
    results.append({"text": "Strategic analysis gives build/buy/outsource recommendations",
                    "passed": recs, "evidence": "all three terms found" if recs else "missing some"})
    # Payment processing at >= 0.6
    payment_ok = False
    payment_ev = "no payment component found"
    for name, (v, e) in coords.items():
        if "payment" in name.lower() or "stripe" in name.lower() or "billing" in name.lower():
            if e >= 0.6:
                payment_ok = True
                payment_ev = f"{name} at epsilon={e}"
                break
            else:
                payment_ev = f"{name} at epsilon={e} (below 0.6)"
    results.append({"text": "Payment processing at Product-to-Commodity (epsilon >= 0.6)",
                    "passed": payment_ok, "evidence": payment_ev})
    # Cloud at >= 0.8
    cloud_ok = False
    cloud_ev = "no cloud/hosting component found"
    for name, (v, e) in coords.items():
        if any(k in name.lower() for k in ["cloud", "compute", "aws", "gcp", "azure", "hosting"]):
            if e >= 0.8:
                cloud_ok = True
                cloud_ev = f"{name} at epsilon={e}"
                break
            else:
                cloud_ev = f"{name} at epsilon={e} (below 0.8)"
    results.append({"text": "Cloud infrastructure at Commodity/utility (epsilon >= 0.8)",
                    "passed": cloud_ok, "evidence": cloud_ev})
    # Gameplay
    ok, ev = has_gameplay(text)
    results.append({"text": "Cites at least one specific Wardley gameplay by name",
                    "passed": ok, "evidence": ev})
    # Caveat
    caveat = ("cannot measure evolution" in text.lower() or
              ("scenario" in text.lower() and "forecast" in text.lower()) or
              "climatic pattern" in text.lower())
    results.append({"text": "Caveat present that evolution is scenario not forecast",
                    "passed": caveat,
                    "evidence": "found" if caveat else "no caveat"})
    return results


GRADERS = {
    "eval-tea-shop-classic": grade_tea_shop,
    "eval-freelance-marketplace": grade_freelance,
    "eval-saas-invoicing": grade_saas,
}


def main():
    for eval_dir in sorted(ITERATION.iterdir()):
        if not eval_dir.is_dir():
            continue
        grader = GRADERS.get(eval_dir.name)
        if not grader:
            continue
        for config in ["with_skill", "without_skill"]:
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


def grade_genai_rag(text: str) -> list[dict]:
    owm = find_owm_block(text)
    coords = coord_map(owm)
    ncomp = count_components(owm)

    results = []
    has_owm = "anchor" in owm and "component" in owm and "->" in owm
    results.append({"text": "Output contains an OWM-format block", "passed": has_owm,
                    "evidence": "OWM block found" if has_owm else "no OWM structure"})
    # Anchor at >=0.9
    anchor_ok = False
    anchor_ev = "no anchor"
    for line in owm.splitlines():
        m = re.match(r"\s*anchor\s+(.+?)\s*\[\s*([0-9.]+)\s*,", line)
        if m:
            if float(m.group(2)) >= 0.9:
                anchor_ok = True
                anchor_ev = f"{m.group(1).strip()} at vis={m.group(2)}"
                break
    results.append({"text": "Has a user-facing anchor at high visibility (>=0.9)",
                    "passed": anchor_ok, "evidence": anchor_ev})
    results.append({"text": "At least 8 components identified (GenAI stack is multi-layered)",
                    "passed": ncomp >= 8, "evidence": f"{ncomp} components"})
    ok, ev = check_coords_in_range(owm)
    results.append({"text": "Every component has coordinates in [0,1]", "passed": ok, "evidence": ev})
    ok, ev = check_visibility_constraint(owm)
    results.append({"text": "Visibility constraint respected for all edges",
                    "passed": ok, "evidence": ev})
    canon = "(+utility)" in text or "(+rental)" in text
    results.append({"text": "Uses canonical stage naming (+utility or +rental)",
                    "passed": canon, "evidence": "found" if canon else "missing"})
    # LLM API at commodity
    llm_ok = False
    llm_ev = "no LLM / GPT / Claude / Gemini / OpenAI / Anthropic component found"
    for name, (v, e) in coords.items():
        low = name.lower()
        if any(k in low for k in ["llm", "gpt", "claude", "gemini", "openai", "anthropic",
                                    "foundation model", "language model"]):
            if e >= 0.75:
                llm_ok = True
                llm_ev = f"{name} at epsilon={e}"
                break
            else:
                llm_ev = f"{name} at epsilon={e} (below 0.75)"
    results.append({"text": "LLM API component exists at Commodity/utility (epsilon >= 0.75)",
                    "passed": llm_ok, "evidence": llm_ev})
    # Vector DB / retrieval
    retrieval_ok = any(
        any(k in name.lower() for k in ["vector", "pinecone", "weaviate", "chroma",
                                          "qdrant", "retrieval", "retriever", "index"])
        for name in coords
    )
    results.append({"text": "Vector DB or retrieval component exists",
                    "passed": retrieval_ok,
                    "evidence": "found" if retrieval_ok else "no vector DB / retrieval found"})
    # Embedding model
    embed_ok = any(
        any(k in name.lower() for k in ["embedding", "embed"])
        for name in coords
    )
    results.append({"text": "Embedding model component exists",
                    "passed": embed_ok,
                    "evidence": "found" if embed_ok else "no embedding component"})
    # Evaluation / observability
    eval_ok = any(
        any(k in name.lower() for k in ["eval", "observability", "tracing", "langsmith",
                                         "monitoring", "metric"])
        for name in coords
    )
    results.append({"text": "Evaluation/observability component exists (GenAI-specific)",
                    "passed": eval_ok,
                    "evidence": "found" if eval_ok else "no eval/observability — common gap"})
    # Build/buy/utility recommendations
    recs_ok = sum(1 for k in ["build", "buy", "utility", "api", "consume", "rent"]
                  if k in text.lower()) >= 4
    results.append({"text": "Build/buy/utility recommendations per relevant component",
                    "passed": recs_ok, "evidence": "found decision vocabulary" if recs_ok else "missing"})
    # Gameplay
    ok, ev = has_gameplay(text)
    results.append({"text": "Cites at least one specific Wardley gameplay by name",
                    "passed": ok, "evidence": ev})
    # Deep placement notes
    dp_ok = any(k in text.lower() for k in ["deep placement", "deep-placement",
                                              "initial cheat-sheet", "initial placement",
                                              "shifted from", "shifted to", "confirmed at",
                                              "web search", "vendor search"])
    results.append({"text": "Deep-placement notes present (step 4.5 used)",
                    "passed": dp_ok, "evidence": "found evidence of deep placement" if dp_ok else "no deep-placement notes"})
    # Caveat
    caveat = ("cannot measure evolution" in text.lower() or
              ("scenario" in text.lower() and "forecast" in text.lower()) or
              "climatic pattern" in text.lower())
    results.append({"text": "Caveat present that evolution is scenario not forecast",
                    "passed": caveat, "evidence": "found" if caveat else "no caveat"})
    return results


GRADERS["eval-genai-rag-platform"] = grade_genai_rag


def grade_prompt_engineering(text: str) -> list[dict]:
    owm = find_owm_block(text)
    coords = coord_map(owm)
    ncomp = count_components(owm)

    results = []
    has_owm = "anchor" in owm and "component" in owm and "->" in owm
    results.append({"text": "Output contains an OWM-format block", "passed": has_owm,
                    "evidence": "OWM found" if has_owm else "no OWM structure"})
    # High-visibility anchor
    anchor_ok = False
    anchor_ev = "no anchor"
    for line in owm.splitlines():
        m = re.match(r"\s*anchor\s+(.+?)\s*\[\s*([0-9.]+)\s*,", line)
        if m and float(m.group(2)) >= 0.9:
            anchor_ok = True
            anchor_ev = f"{m.group(1).strip()} at vis={m.group(2)}"
            break
    results.append({"text": "Has a user-facing anchor at high visibility (>=0.9)",
                    "passed": anchor_ok, "evidence": anchor_ev})
    results.append({"text": "At least 8 components identified", "passed": ncomp >= 8,
                    "evidence": f"{ncomp} components"})
    ok, ev = check_coords_in_range(owm)
    results.append({"text": "Every component has coordinates in [0,1]", "passed": ok, "evidence": ev})
    ok, ev = check_visibility_constraint(owm)
    results.append({"text": "Visibility constraint respected for all edges (validator clean)",
                    "passed": ok, "evidence": ev})
    canon = "(+utility)" in text or "(+rental)" in text
    results.append({"text": "Uses canonical stage naming (+utility or +rental)",
                    "passed": canon, "evidence": "found" if canon else "missing"})
    # LLM API at commodity
    llm_ok = False
    llm_ev = "no LLM/foundation-model component found"
    for name, (v, e) in coords.items():
        low = name.lower()
        if any(k in low for k in ["llm", "gpt", "claude", "gemini", "openai",
                                    "anthropic", "foundation model", "language model",
                                    "inference api", "model api"]):
            if e >= 0.75:
                llm_ok = True
                llm_ev = f"{name} at epsilon={e}"
                break
            else:
                llm_ev = f"{name} at epsilon={e} (below 0.75)"
    results.append({"text": "LLM API component at Commodity/utility (epsilon >= 0.75)",
                    "passed": llm_ok, "evidence": llm_ev})
    # Prompt registry / versioning
    registry_ok = any(
        any(k in name.lower() for k in ["prompt registry", "prompt version",
                                          "prompt store", "prompt library",
                                          "prompt repo", "prompt management"])
        for name in coords
    )
    # broader: "prompt" + "version" or "registry" or "template" mentioned in any component name
    if not registry_ok:
        registry_ok = any(
            "prompt" in name.lower() and any(k in name.lower() for k in
                ["version", "registry", "template", "catalog", "manag"])
            for name in coords
        )
    results.append({"text": "Prompt registry or versioning component exists",
                    "passed": registry_ok,
                    "evidence": "found" if registry_ok else "no prompt registry/versioning"})
    # Eval framework
    eval_ok = any(
        any(k in name.lower() for k in ["eval", "evaluation", "test harness",
                                          "promptfoo", "braintrust", "benchmark"])
        for name in coords
    )
    results.append({"text": "Evaluation framework component exists",
                    "passed": eval_ok, "evidence": "found" if eval_ok else "missing"})
    # Observability / tracing
    obs_ok = any(
        any(k in name.lower() for k in ["observability", "tracing", "trace",
                                          "monitor", "langsmith", "langfuse",
                                          "telemetry", "logging"])
        for name in coords
    )
    results.append({"text": "Observability or tracing component exists",
                    "passed": obs_ok, "evidence": "found" if obs_ok else "missing"})
    # Build/buy/utility recs
    recs_ok = sum(1 for k in ["build", "buy", "utility", "api", "consume", "rent", "saas"]
                  if k in text.lower()) >= 4
    results.append({"text": "Build/buy/utility recommendations per relevant component",
                    "passed": recs_ok, "evidence": "found" if recs_ok else "missing"})
    # Gameplay
    ok, ev = has_gameplay(text)
    results.append({"text": "Cites at least one specific Wardley gameplay by name",
                    "passed": ok, "evidence": ev})
    # Deep placement
    dp_ok = any(k in text.lower() for k in ["deep placement", "deep-placement",
                                              "initial cheat", "shifted from", "shifted to",
                                              "confirmed at", "vendor search", "web search"])
    results.append({"text": "Deep-placement notes present (step 4.5 used)",
                    "passed": dp_ok, "evidence": "found" if dp_ok else "no deep placement"})
    # Caveat
    caveat = ("cannot measure evolution" in text.lower() or
              ("scenario" in text.lower() and "forecast" in text.lower()) or
              "climatic pattern" in text.lower())
    results.append({"text": "Caveat present that evolution is scenario not forecast",
                    "passed": caveat, "evidence": "found" if caveat else "no caveat"})
    return results


GRADERS["eval-prompt-engineering"] = grade_prompt_engineering
