#!/usr/bin/env node
/**
 * Validate an OWM (Online Wardley Maps) block against structural rules.
 *
 * Usage:
 *   node validate_owm.mjs < map.owm
 *   node validate_owm.mjs map.owm
 *
 * Exit codes:
 *   0 — no violations
 *   1 — violations found (printed to stdout)
 *
 * Extract your OWM block from the draft (everything between ```owm and ```)
 * and pipe it to this script. If it exits non-zero, fix the reported
 * violations and re-run until clean.
 */
import { readFileSync } from 'node:fs';
import process from 'node:process';

function parseOwm(text) {
  const coords = new Map(); // name → [v, e]
  const edges = [];         // [src, tgt]

  for (const rawLine of text.split('\n')) {
    const line = rawLine.trim();
    if (!line || line.startsWith('//') || line.startsWith('#')) continue;

    // anchor or component line
    const node = line.match(
      /^(?:anchor|component)\s+(.+?)\s*\[\s*([0-9.]+)\s*,\s*([0-9.]+)\s*\](?:\s+.*)?$/
    );
    if (node) {
      const name = node[1].trim();
      const v = parseFloat(node[2]);
      const e = parseFloat(node[3]);
      if (!Number.isNaN(v) && !Number.isNaN(e)) {
        coords.set(name, [v, e]);
      }
      continue;
    }

    // dependency edge: "A->B" (but not "evolve X N")
    if (line.includes('->') && !line.startsWith('evolve')) {
      const edge = line.match(/^(.+?)->(.+)$/);
      if (edge) edges.push([edge[1].trim(), edge[2].trim()]);
    }
  }
  return { coords, edges };
}

function validate(coords, edges) {
  const violations = [];

  // 1. Coords in [0, 1]
  for (const [name, [v, e]] of coords) {
    if (!(v >= 0 && v <= 1)) {
      violations.push(`COORD OUT OF RANGE: '${name}' visibility=${v} (must be in [0,1])`);
    }
    if (!(e >= 0 && e <= 1)) {
      violations.push(`COORD OUT OF RANGE: '${name}' evolution=${e} (must be in [0,1])`);
    }
  }

  // 2. Every edge endpoint should exist as a component/anchor
  for (const [src, tgt] of edges) {
    if (!coords.has(src)) {
      violations.push(`UNKNOWN SOURCE: edge '${src}->${tgt}' — '${src}' not declared`);
    }
    if (!coords.has(tgt)) {
      violations.push(`UNKNOWN TARGET: edge '${src}->${tgt}' — '${tgt}' not declared`);
    }
  }

  // 3. Visibility constraint: for every edge a->b, ν(a) >= ν(b)
  for (const [src, tgt] of edges) {
    if (coords.has(src) && coords.has(tgt)) {
      const vSrc = coords.get(src)[0];
      const vTgt = coords.get(tgt)[0];
      if (vSrc < vTgt) {
        violations.push(
          `VISIBILITY VIOLATION: ${src}(ν=${vSrc}) -> ${tgt}(ν=${vTgt})` +
          ` — source must be at or above target`
        );
      }
    }
  }
  return violations;
}

function main() {
  let text;
  if (process.argv.length > 2) {
    text = readFileSync(process.argv[2], 'utf8');
  } else {
    text = readFileSync(0, 'utf8'); // stdin
  }

  // Strip ```owm fences if the caller pasted them
  const fence = text.match(/```owm\s*\n([\s\S]*?)\n```/);
  if (fence) text = fence[1];

  const { coords, edges } = parseOwm(text);
  const violations = validate(coords, edges);

  if (violations.length === 0) {
    console.log(`OK: ${coords.size} components/anchors, ${edges.length} edges — no violations.`);
    process.exit(0);
  }

  console.log(
    `FAIL: ${violations.length} violation(s) found in map with ` +
    `${coords.size} components/anchors and ${edges.length} edges.`
  );
  console.log();
  for (const v of violations) console.log(`  - ${v}`);
  console.log();
  console.log('Fix each violation and re-run. For visibility violations, either:');
  console.log('  (a) raise the source\'s visibility to be >= target\'s, or');
  console.log('  (b) lower the target\'s visibility to be <= source\'s.');
  console.log('After fixing, re-run this script because adjustments can cascade.');
  process.exit(1);
}

main();
