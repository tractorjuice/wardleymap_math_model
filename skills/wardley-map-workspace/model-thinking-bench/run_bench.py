#!/usr/bin/env python3
"""Model x thinking benchmark for the wardley-map skill.

Iterates a matrix of (model, thinking_state, replicate) on a single scenario
using the Anthropic SDK directly. Inlines the production skill (SKILL.md +
references/) as a cached system prompt, exposes `bash` and `web_search` tools,
and saves each cell's final output + transcript metadata.

Resumable: skips cells whose outputs/output.md already exists.
"""
from __future__ import annotations
import json
import os
import shutil
import subprocess
import sys
import time
import traceback
from pathlib import Path

from anthropic import Anthropic

ROOT = Path(__file__).parent
REPO = ROOT.parents[2]
SKILL_DIR = REPO / "skills" / "wardley-map"
OUTPUTS = ROOT / "outputs"

CONFIG = {
    "models": [
        "claude-opus-4-7",
        "claude-sonnet-4-6",
        "claude-haiku-4-5-20251001",
    ],
    "thinking_states": ["off", "on"],
    "replicates": 3,
    "thinking_budget_tokens": 10000,
    "max_tokens_no_think": 32000,
    "max_tokens_think": 48000,
    "max_agent_turns": 30,
    "web_search_max_uses": 8,
    "bash_timeout_sec": 90,
    "map": {
        "name": "ai-trust",
        "scenario": (
            "It's June 2023. Map the AI trust landscape — what components determine "
            "whether individuals, government, and business can trust AI systems. "
            "Include technical components (models, algorithms, data, compute), "
            "governance components (regulations, audits, benchmarks, policy), "
            "control mechanisms (forensics, feedback loops, constitution), and "
            "outcome components (safety, reputation, competitive advantage). Tell "
            "me what's differentiating vs. commoditising and where trust itself is "
            "fragile."
        ),
    },
}


def build_system_prompt() -> str:
    parts = [
        "You are running as a Wardley-Map generator. Follow the procedure in "
        "the SKILL document below. The references/ bundle is inlined after "
        "SKILL.md so you can rely on those rules without having to re-read "
        "them from disk. You also have a `bash` tool with the production "
        "validator (`scripts/validate_owm.mjs`) available in the working "
        "directory. Iterate to a clean validator pass before finalising. Your "
        "final assistant message must contain the OWM fenced block and the "
        "strategic analysis exactly as the skill specifies."
    ]
    parts.append("\n\n# SKILL.md\n\n" + (SKILL_DIR / "SKILL.md").read_text())
    for ref in sorted((SKILL_DIR / "references").glob("*.md")):
        parts.append(f"\n\n# references/{ref.name}\n\n{ref.read_text()}")
    return "".join(parts)


def prepare_sandbox(cell_dir: Path) -> Path:
    sandbox = cell_dir / "sandbox"
    if sandbox.exists():
        shutil.rmtree(sandbox)
    sandbox.mkdir(parents=True)
    # Copy validator + helpers; copy references so the model can `cat` them if it wants
    shutil.copytree(SKILL_DIR / "scripts", sandbox / "scripts")
    shutil.copytree(SKILL_DIR / "references", sandbox / "references")
    return sandbox


def run_bash(sandbox: Path, command: str, timeout: int) -> str:
    try:
        result = subprocess.run(
            ["bash", "-lc", command],
            cwd=str(sandbox),
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        out = result.stdout
        err = result.stderr
        snippet = f"exit_code: {result.returncode}\n"
        if out:
            snippet += f"stdout:\n{out}\n"
        if err:
            snippet += f"stderr:\n{err}\n"
        if not out and not err:
            snippet += "(no output)\n"
        return snippet[:12000]
    except subprocess.TimeoutExpired:
        return f"ERROR: bash command timed out after {timeout}s"
    except Exception as exc:
        return f"ERROR: {exc!r}"


def make_tools() -> list[dict]:
    return [
        {
            "type": "web_search_20250305",
            "name": "web_search",
            "max_uses": CONFIG["web_search_max_uses"],
        },
        {
            "name": "bash",
            "description": (
                "Run a bash command in the sandbox working directory. "
                "scripts/validate_owm.mjs and the references/ bundle are "
                "available. Use `node scripts/validate_owm.mjs <path>` to "
                "validate an OWM file. 90s timeout."
            ),
            "input_schema": {
                "type": "object",
                "properties": {
                    "command": {"type": "string", "description": "Bash command"}
                },
                "required": ["command"],
            },
        },
    ]


def serialise_block(block) -> dict:
    """Convert an Anthropic content block to a dict suitable for round-tripping."""
    if hasattr(block, "model_dump"):
        return block.model_dump(exclude_none=True)
    return dict(block)


def run_cell(
    client: Anthropic,
    model: str,
    thinking: str,
    rep: int,
    system_prompt: str,
    scenario: str,
) -> dict:
    map_name = CONFIG["map"]["name"]
    cell_dir = OUTPUTS / f"eval-{map_name}" / model / f"thinking-{thinking}" / f"run-{rep}"
    out_md = cell_dir / "outputs" / "output.md"
    if out_md.exists():
        return {"status": "skipped", "cell": str(cell_dir.relative_to(ROOT))}

    cell_dir.mkdir(parents=True, exist_ok=True)
    sandbox = prepare_sandbox(cell_dir)
    tools = make_tools()

    extra_kwargs = {}
    if thinking == "on":
        max_tokens = CONFIG["max_tokens_think"]
        # Opus 4.7 deprecated `thinking.type.enabled` for the new adaptive
        # interface; Sonnet 4.6 and Haiku 4.5 still accept the legacy field.
        if "opus-4-7" in model:
            extra_kwargs["thinking"] = {"type": "adaptive"}
            extra_kwargs["output_config"] = {"effort": "high"}
        else:
            extra_kwargs["thinking"] = {
                "type": "enabled",
                "budget_tokens": CONFIG["thinking_budget_tokens"],
            }
            # Interleaved thinking lets the model think between tool calls;
            # without this beta, thinking only happens before the first tool use.
            extra_kwargs["extra_headers"] = {
                "anthropic-beta": "interleaved-thinking-2025-05-14"
            }
    else:
        max_tokens = CONFIG["max_tokens_no_think"]

    messages = [{"role": "user", "content": scenario}]
    transcript = []
    usage_totals = {
        "input_tokens": 0,
        "output_tokens": 0,
        "cache_creation_input_tokens": 0,
        "cache_read_input_tokens": 0,
    }
    started = time.time()
    final_text = ""
    last_stop = None
    error = None

    try:
        for turn in range(CONFIG["max_agent_turns"]):
            # Streaming is required for high max_tokens (SDK guardrail kicks
            # in around long-running requests). We don't need incremental
            # output here — we just consume the stream and pull the final
            # Message, which has the same shape as the non-streaming response.
            with client.messages.stream(
                model=model,
                max_tokens=max_tokens,
                system=[
                    {
                        "type": "text",
                        "text": system_prompt,
                        "cache_control": {"type": "ephemeral"},
                    }
                ],
                messages=messages,
                tools=tools,
                **extra_kwargs,
            ) as stream:
                resp = stream.get_final_message()
            usage = resp.usage
            for key in usage_totals:
                usage_totals[key] += getattr(usage, key, 0) or 0
            transcript.append(
                {
                    "turn": turn,
                    "stop_reason": resp.stop_reason,
                    "usage": {
                        "input": usage.input_tokens,
                        "output": usage.output_tokens,
                        "cache_creation": getattr(usage, "cache_creation_input_tokens", 0),
                        "cache_read": getattr(usage, "cache_read_input_tokens", 0),
                    },
                    "blocks": [b.type for b in resp.content],
                }
            )
            last_stop = resp.stop_reason

            if resp.stop_reason == "end_turn":
                final_text = "".join(
                    b.text for b in resp.content if b.type == "text"
                )
                break

            if resp.stop_reason == "max_tokens":
                final_text = "".join(
                    b.text for b in resp.content if b.type == "text"
                )
                error = "stopped on max_tokens"
                break

            if resp.stop_reason == "tool_use":
                # Round-trip the assistant turn with all content blocks
                # (text, thinking, server_tool_use, web_search_tool_result,
                # tool_use). The thinking blocks MUST be preserved when the
                # next request uses tool_use with thinking enabled.
                messages.append(
                    {"role": "assistant", "content": [serialise_block(b) for b in resp.content]}
                )
                tool_results = []
                for block in resp.content:
                    if block.type == "tool_use" and block.name == "bash":
                        command = block.input.get("command", "")
                        result_text = run_bash(
                            sandbox, command, CONFIG["bash_timeout_sec"]
                        )
                        tool_results.append(
                            {
                                "type": "tool_result",
                                "tool_use_id": block.id,
                                "content": result_text,
                            }
                        )
                if not tool_results:
                    # No local tool to run — server-side tools were already
                    # resolved; the model must continue. Defensive: break.
                    final_text = "".join(
                        b.text for b in resp.content if b.type == "text"
                    )
                    error = "stop_reason=tool_use but no local tool calls"
                    break
                messages.append({"role": "user", "content": tool_results})
                continue

            # Unexpected stop reason
            final_text = "".join(
                b.text for b in resp.content if b.type == "text"
            )
            error = f"unexpected stop_reason: {resp.stop_reason}"
            break
        else:
            error = f"hit max_agent_turns ({CONFIG['max_agent_turns']})"
    except Exception as exc:
        error = f"{type(exc).__name__}: {exc}"
        transcript.append({"error_traceback": traceback.format_exc()})

    duration = time.time() - started
    (cell_dir / "outputs").mkdir(exist_ok=True)
    out_md.write_text(final_text or "")
    (cell_dir / "timing.json").write_text(
        json.dumps(
            {
                "model": model,
                "thinking": thinking,
                "replicate": rep,
                "duration_sec": round(duration, 2),
                "last_stop": last_stop,
                "error": error,
                "usage_totals": usage_totals,
                "agent_turns": len(transcript),
                "transcript": transcript,
            },
            indent=2,
        )
    )
    return {
        "status": "ok" if not error else "error",
        "cell": str(cell_dir.relative_to(ROOT)),
        "duration_sec": round(duration, 2),
        "usage": usage_totals,
        "error": error,
    }


def main():
    if "ANTHROPIC_API_KEY" not in os.environ:
        sys.exit("ANTHROPIC_API_KEY not set")
    client = Anthropic()
    system_prompt = build_system_prompt()
    print(f"system prompt: {len(system_prompt):,} chars")
    scenario = CONFIG["map"]["scenario"]

    # Allow CLI filtering: --model=opus --thinking=on --rep=0
    filt = {}
    for arg in sys.argv[1:]:
        if arg.startswith("--") and "=" in arg:
            k, v = arg[2:].split("=", 1)
            filt[k] = v

    cells = []
    for model in CONFIG["models"]:
        if "model" in filt and filt["model"] not in model:
            continue
        for thinking in CONFIG["thinking_states"]:
            if "thinking" in filt and filt["thinking"] != thinking:
                continue
            for rep in range(CONFIG["replicates"]):
                if "rep" in filt and int(filt["rep"]) != rep:
                    continue
                cells.append((model, thinking, rep))

    print(f"running {len(cells)} cells")
    summary = []
    for i, (model, thinking, rep) in enumerate(cells, 1):
        label = f"[{i}/{len(cells)}] {model} thinking={thinking} rep={rep}"
        print(f"{label} ...", flush=True)
        result = run_cell(client, model, thinking, rep, system_prompt, scenario)
        summary.append({"model": model, "thinking": thinking, "rep": rep, **result})
        print(
            f"  -> {result['status']} duration={result.get('duration_sec','-')}s "
            f"err={result.get('error')}",
            flush=True,
        )

    (ROOT / "run_summary.json").write_text(json.dumps(summary, indent=2))
    n_ok = sum(1 for s in summary if s["status"] == "ok")
    n_err = sum(1 for s in summary if s["status"] == "error")
    n_skip = sum(1 for s in summary if s["status"] == "skipped")
    print(f"\nDone: {n_ok} ok, {n_err} error, {n_skip} skipped (resumed)")


if __name__ == "__main__":
    main()
