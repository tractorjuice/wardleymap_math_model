#!/usr/bin/env node
/**
 * Validate the skill's OWM subset: named anchors/components with two coordinates
 * [visibility, evolution], and depends-on edges. Other OWM directives are ignored.
 * Malformed node declarations fail validation rather than disappearing.
 * Usage: node validate_owm.mjs [map.owm] (otherwise reads stdin).
 * Exit 0: no violations; exit 1: violations or unreadable input.
 * Unreachable components are advisory warnings, not hard errors.
 */
import { readFileSync } from 'node:fs';
import { pathToFileURL } from 'node:url';
import process from 'node:process';

const NUMBER = '[+-]?(?:\\d+(?:\\.\\d*)?|\\.\\d+)(?:[eE][+-]?\\d+)?';
const NODE = new RegExp(
  `^(anchor|component)\\s+(.+?)\\s*\\[\\s*(${NUMBER})\\s*,\\s*(${NUMBER})\\s*\\](?:\\s+.*)?$`
);

function nameOf(text) {
  const name = text.trim();
  if ((name.startsWith('"') && name.endsWith('"')) ||
      (name.startsWith("'") && name.endsWith("'"))) {
    return name.slice(1, -1).trim();
  }
  return name;
}

export function validateOwm(text) {
  // Accept a pasted Markdown draft, but validate only its canonical OWM block.
  const fence = text.match(/```owm\s*\n([\s\S]*?)\n```/);
  if (fence) text = fence[1];
  const coords = new Map();
  const anchors = new Set();
  const edges = [];
  const violations = [];
  const warnings = [];

  for (const [index, rawLine] of text.split('\n').entries()) {
    const line = rawLine.replace(/\s+\/\/.*$/, '').trim();
    if (!line || line.startsWith('//') || line.startsWith('#')) continue;

    if (/^(anchor|component)(?:\s|$)/.test(line)) {
      const node = line.match(NODE);
      if (!node || !nameOf(node[2])) {
        violations.push(`MALFORMED NODE at line ${index + 1}: ${line}`);
        continue;
      }
      const [, kind, rawName, visibility, evolution] = node;
      const name = nameOf(rawName);
      if (coords.has(name)) {
        violations.push(`DUPLICATE NODE at line ${index + 1}: '${name}'`);
        continue;
      }
      const v = Number(visibility);
      const e = Number(evolution);
      coords.set(name, [v, e]);
      if (kind === 'anchor') anchors.add(name);
      for (const [axis, value] of [['visibility', v], ['evolution', e]]) {
        if (!Number.isFinite(value) || value < 0 || value > 1) {
          violations.push(`COORD OUT OF RANGE: '${name}' ${axis}=${value} (must be finite and in [0,1])`);
        }
      }
      continue;
    }

    if (line.includes('->') && !/^evolve(?:\s|$)/.test(line)) {
      const edge = line.match(/^(.+?)->(.+)$/);
      if (!edge || !nameOf(edge[1]) || !nameOf(edge[2])) {
        violations.push(`MALFORMED EDGE at line ${index + 1}: ${line}`);
      } else {
        edges.push([nameOf(edge[1]), nameOf(edge[2])]);
      }
    }
  }

  if (coords.size === 0) violations.push('EMPTY MAP: declare at least one anchor.');
  if (anchors.size === 0) violations.push('MISSING ANCHOR: declare at least one user-need anchor.');

  const dependencies = new Map();
  for (const [src, tgt] of edges) {
    if (!coords.has(src)) violations.push(`UNKNOWN SOURCE: edge '${src}->${tgt}' — '${src}' not declared`);
    if (!coords.has(tgt)) violations.push(`UNKNOWN TARGET: edge '${src}->${tgt}' — '${tgt}' not declared`);
    if (!coords.has(src) || !coords.has(tgt)) continue;
    if (coords.get(src)[0] < coords.get(tgt)[0]) {
      violations.push(`VISIBILITY VIOLATION: ${src}(ν=${coords.get(src)[0]}) -> ${tgt}(ν=${coords.get(tgt)[0]}) — source must be at or above target`);
    }
    if (!dependencies.has(src)) dependencies.set(src, []);
    dependencies.get(src).push(tgt);
  }

  if (anchors.size > 0) {
    const reached = new Set(anchors);
    const queue = [...anchors];
    for (let i = 0; i < queue.length; i++) {
      for (const target of dependencies.get(queue[i]) || []) {
        if (reached.has(target)) continue;
        reached.add(target);
        queue.push(target);
      }
    }
    for (const name of coords.keys()) {
      if (!reached.has(name)) warnings.push(`UNREACHABLE COMPONENT: '${name}' has no dependency path from any anchor; review its scope or missing edges.`);
    }
  }
  return { coords, anchors, edges, violations, warnings };
}

function main() {
  let result;
  try {
    result = validateOwm(readFileSync(process.argv[2] || 0, 'utf8'));
  } catch (error) {
    console.error(`FAIL: unable to read input: ${error.message}`);
    process.exitCode = 1;
    return;
  }
  const { coords, edges, violations, warnings } = result;
  console.log(`${violations.length ? 'FAIL' : 'OK'}: ${coords.size} components/anchors, ${edges.length} edges — ${violations.length} violation(s).`);
  for (const violation of violations) console.log(`  - ${violation}`);
  for (const warning of warnings) console.log(`  WARNING: ${warning}`);
  if (violations.length) {
    console.log('Fix the declarations or constraints and re-run; visibility adjustments can cascade.');
    process.exitCode = 1;
  }
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) main();
