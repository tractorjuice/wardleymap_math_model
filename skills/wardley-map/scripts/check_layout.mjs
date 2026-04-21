#!/usr/bin/env node
/**
 * Advisory layout check for a Wardley Map OWM file.
 *
 * Complements validate_owm.mjs — the validator catches structural errors
 * (coord range, missing endpoints, visibility hard rule violations);
 * this script catches visual/readability issues that render the map
 * correctly but look tangled. It's ADVISORY ONLY and always exits 0
 * unless invoked with `--strict`, in which case warnings become failures.
 *
 * Checks:
 *   1. Near-duplicate coordinates — two nodes at effectively the same
 *      position will render on top of each other. Threshold: |Δν| < 0.02
 *      AND |Δε| < 0.02.
 *   2. Stage-boundary straddling — components within ±0.01 of ε = 0.25,
 *      0.50, or 0.75 render on a band line and look accidentally in
 *      both stages. Suggests nudging away from the boundary.
 *   3. Canvas-edge clipping — anchors with ν > 0.98 or ν < 0.02 get
 *      cut off by the rendered border. Same for any node with ε > 0.99
 *      or ε < 0.01.
 *   4. Stage-distribution imbalance — if > 60% of components fall in
 *      one evolution stage, the map is visually lopsided and may reflect
 *      a missing part of the landscape rather than a genuinely skewed
 *      domain. Advisory.
 *
 * Usage:
 *   node check_layout.mjs [--strict] <map.owm>
 *   node check_layout.mjs [--strict] < map.owm
 *
 * Exit codes:
 *   0 — layout OK (or warnings in non-strict mode)
 *   1 — warnings and --strict was passed
 */
import { readFileSync } from 'node:fs';
import process from 'node:process';

const NEAR_DUP_THRESHOLD  = 0.02;
const BOUNDARY_TOLERANCE  = 0.01;
const BAND_BOUNDARIES     = [0.25, 0.50, 0.75];
const ANCHOR_EDGE_HIGH    = 0.98;
const ANCHOR_EDGE_LOW     = 0.02;
const COMP_EDGE_HIGH      = 0.99;
const COMP_EDGE_LOW       = 0.01;
const STAGE_SHARE_LIMIT   = 0.60;

function parseOwm(text) {
  const nodes = []; // [{kind, name, v, e}]
  for (const rawLine of text.split('\n')) {
    const line = rawLine.trim();
    if (!line || line.startsWith('//') || line.startsWith('#')) continue;
    const m = line.match(
      /^(anchor|component)\s+(.+?)\s*\[\s*([0-9.]+)\s*,\s*([0-9.]+)\s*\]/
    );
    if (m) {
      const v = parseFloat(m[3]);
      const e = parseFloat(m[4]);
      if (!Number.isNaN(v) && !Number.isNaN(e)) {
        nodes.push({ kind: m[1], name: m[2].trim(), v, e });
      }
    }
  }
  return nodes;
}

function stageOf(e) {
  if (e < 0.25) return 'Genesis';
  if (e < 0.50) return 'Custom';
  if (e < 0.75) return 'Product';
  return 'Commodity';
}

function checkNearDuplicates(nodes) {
  const warnings = [];
  for (let i = 0; i < nodes.length; i++) {
    for (let j = i + 1; j < nodes.length; j++) {
      const dv = Math.abs(nodes[i].v - nodes[j].v);
      const de = Math.abs(nodes[i].e - nodes[j].e);
      if (dv < NEAR_DUP_THRESHOLD && de < NEAR_DUP_THRESHOLD) {
        warnings.push(
          `NEAR-DUPLICATE: '${nodes[i].name}' [${nodes[i].v}, ${nodes[i].e}] ` +
          `and '${nodes[j].name}' [${nodes[j].v}, ${nodes[j].e}] ` +
          `will render on top of each other (|Δν|=${dv.toFixed(3)}, |Δε|=${de.toFixed(3)}).`
        );
      }
    }
  }
  return warnings;
}

function checkBoundaryStraddling(nodes) {
  const warnings = [];
  for (const n of nodes) {
    if (n.kind !== 'component') continue;
    for (const b of BAND_BOUNDARIES) {
      if (Math.abs(n.e - b) <= BOUNDARY_TOLERANCE) {
        warnings.push(
          `BOUNDARY STRADDLE: '${n.name}' at ε=${n.e} is within ±${BOUNDARY_TOLERANCE} ` +
          `of the stage boundary ε=${b}. Nudge to ε=${(b - 0.03).toFixed(2)} ` +
          `or ε=${(b + 0.03).toFixed(2)} so the stage is unambiguous.`
        );
      }
    }
  }
  return warnings;
}

function checkCanvasEdges(nodes) {
  const warnings = [];
  for (const n of nodes) {
    const isAnchor = n.kind === 'anchor';
    const vHigh = isAnchor ? ANCHOR_EDGE_HIGH : COMP_EDGE_HIGH;
    const vLow  = isAnchor ? ANCHOR_EDGE_LOW  : COMP_EDGE_LOW;
    if (n.v > vHigh) {
      warnings.push(
        `CANVAS CLIP: ${n.kind} '${n.name}' at ν=${n.v} may be clipped by the top border. ` +
        `Pull back to ν=${(vHigh - 0.02).toFixed(2)}.`
      );
    }
    if (n.v < vLow) {
      warnings.push(
        `CANVAS CLIP: ${n.kind} '${n.name}' at ν=${n.v} may be clipped by the bottom border. ` +
        `Push up to ν=${(vLow + 0.02).toFixed(2)}.`
      );
    }
    if (n.e > COMP_EDGE_HIGH) {
      warnings.push(
        `CANVAS CLIP: ${n.kind} '${n.name}' at ε=${n.e} may be clipped by the right border. ` +
        `Pull back to ε=${(COMP_EDGE_HIGH - 0.02).toFixed(2)}.`
      );
    }
    if (n.e < COMP_EDGE_LOW) {
      warnings.push(
        `CANVAS CLIP: ${n.kind} '${n.name}' at ε=${n.e} may be clipped by the left border. ` +
        `Push right to ε=${(COMP_EDGE_LOW + 0.02).toFixed(2)}.`
      );
    }
  }
  return warnings;
}

function checkStageDistribution(nodes) {
  const comps = nodes.filter(n => n.kind === 'component');
  if (comps.length < 5) return []; // too small to be imbalanced
  const counts = { Genesis: 0, Custom: 0, Product: 0, Commodity: 0 };
  for (const n of comps) counts[stageOf(n.e)]++;
  const total = comps.length;
  const warnings = [];
  for (const [stage, n] of Object.entries(counts)) {
    const share = n / total;
    if (share > STAGE_SHARE_LIMIT) {
      warnings.push(
        `STAGE IMBALANCE: ${n} of ${total} components (${(share * 100).toFixed(0)}%) ` +
        `in ${stage}. Above ${(STAGE_SHARE_LIMIT * 100).toFixed(0)}% suggests either a ` +
        `genuinely skewed domain OR a missing part of the landscape. Re-check.`
      );
    }
  }
  // Also warn on stages with zero components (may be missing coverage)
  for (const [stage, n] of Object.entries(counts)) {
    if (n === 0) {
      warnings.push(
        `STAGE EMPTY: no components in ${stage}. If this domain genuinely has no ` +
        `${stage}-stage components, ignore. Otherwise the landscape may be under-mapped.`
      );
    }
  }
  return warnings;
}

function main() {
  const args = process.argv.slice(2);
  const strict = args.includes('--strict');
  const fileArgs = args.filter(a => !a.startsWith('--'));
  let text;
  if (fileArgs.length > 0) {
    text = readFileSync(fileArgs[0], 'utf8');
  } else {
    text = readFileSync(0, 'utf8');
  }
  // Strip ```owm fences if present
  const fence = text.match(/```owm\s*\n([\s\S]*?)\n```/);
  if (fence) text = fence[1];

  const nodes = parseOwm(text);
  const warnings = [
    ...checkNearDuplicates(nodes),
    ...checkBoundaryStraddling(nodes),
    ...checkCanvasEdges(nodes),
    ...checkStageDistribution(nodes),
  ];

  const anchors = nodes.filter(n => n.kind === 'anchor').length;
  const components = nodes.filter(n => n.kind === 'component').length;

  if (warnings.length === 0) {
    console.log(`LAYOUT OK: ${anchors} anchors, ${components} components — no layout warnings.`);
    process.exit(0);
  }

  console.log(
    `LAYOUT WARNINGS: ${warnings.length} issue(s) in map with ` +
    `${anchors} anchors and ${components} components.`
  );
  console.log();
  for (const w of warnings) console.log(`  - ${w}`);
  console.log();
  console.log(
    'Layout warnings are advisory. Each describes a likely rendering problem. ' +
    'Fix by adjusting coordinates in the OWM draft and re-running. The visibility ' +
    'hard rule ν(a) ≥ ν(b) must still hold after any move — re-run validate_owm.mjs.'
  );
  process.exit(strict ? 1 : 0);
}

main();
