import test from 'node:test';
import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { mkdtempSync, writeFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { validateOwm } from '../skills/wardley-map/scripts/validate_owm.mjs';

const validator = fileURLToPath(new URL('../skills/wardley-map/scripts/validate_owm.mjs', import.meta.url));
const anchor = 'anchor User [1, 1]\n';
const valid = anchor + 'component Service [0.5, 0.75]\nUser->Service\n';

test('validates a connected map with coordinate boundaries and OWM directives', () => {
  const result = validateOwm(valid + 'component Compute [0, 1]\nService->Compute\nevolve Service 0.9\nstyle wardley\n');
  assert.deepEqual(result.violations, []);
  assert.deepEqual(result.warnings, []);
});

test('rejects negative and out-of-range coordinates instead of dropping nodes', () => {
  for (const coordinates of ['-0.2, 0.5', '0.5, -0.2', '1.2, 0.5', '0.5, 1.2', '1e309, 0.5']) {
    const result = validateOwm(anchor + `component Invalid [${coordinates}]\n`);
    assert.equal(result.coords.size, 2);
    assert.match(result.violations.join('\n'), /COORD OUT OF RANGE/);
  }
});

test('rejects malformed numeric tokens, incomplete declarations and empty names', () => {
  for (const declaration of ['component Bad [0..2, 0.5]', 'component Bad [NaN, 0.5]',
    'component Bad [Infinity, 0.5]', 'component Bad [0.2]', 'component Bad',
    'anchor', 'component "" [0.2, 0.5]']) {
    assert.match(validateOwm(anchor + declaration).violations.join('\n'), /MALFORMED NODE/);
  }
});

test('rejects duplicate names including quoted names and anchor/component collisions', () => {
  const result = validateOwm(valid + 'component "Service" [0.2, 0.3]\ncomponent User [0, 0]\n');
  assert.equal(result.violations.filter(v => v.startsWith('DUPLICATE NODE')).length, 2);
  assert.deepEqual(result.coords.get('Service'), [0.5, 0.75]);
});

test('rejects empty maps and maps without anchors', () => {
  assert.match(validateOwm('// nothing\ntitle Empty').violations.join('\n'), /EMPTY MAP/);
  assert.match(validateOwm('component Orphan [0.5, 0.5]').violations.join('\n'), /MISSING ANCHOR/);
});

test('reports unknown endpoints, malformed edges and upward dependencies', () => {
  const result = validateOwm(valid + 'Missing->Service\nUser->Unknown\nService->User\nUser->\n');
  for (const kind of ['UNKNOWN SOURCE', 'UNKNOWN TARGET', 'VISIBILITY VIOLATION', 'MALFORMED EDGE']) {
    assert.match(result.violations.join('\n'), new RegExp(kind));
  }
});

test('warns about unreachable components without failing a valid map', () => {
  const result = validateOwm(valid + 'component Isolated [0.2, 0.5]\n');
  assert.deepEqual(result.violations, []);
  assert.equal(result.warnings.length, 1);
  assert.match(result.warnings[0], /Isolated/);
});

test('traverses multiple anchors, shortcuts and equal-height dependency cycles', () => {
  const result = validateOwm(anchor + 'anchor Public [1, 0.5]\ncomponent A [0.5, 0.5]\ncomponent B [0.5, 0.6]\nUser->A\nPublic->B\nA->B\nB->A\nUser->B\n');
  assert.deepEqual(result.violations, []);
  assert.deepEqual(result.warnings, []);
});

test('accepts quoted endpoints, labels, inline comments and scientific notation', () => {
  const result = validateOwm('anchor "User Need" [1, 1]\ncomponent "Service" [.5, +7.5e-1] label [-10, 5] // annotation\n"User Need"->"Service" // dependency\n');
  assert.deepEqual(result.violations, []);
  assert.deepEqual(result.warnings, []);
});

test('validates only the OWM fence when given a Markdown draft', () => {
  const result = validateOwm('Prose\n```owm\n' + valid + '```\n```mermaid\ncomponent Bad [-2, 1]\n```');
  assert.equal(result.coords.size, 2);
  assert.deepEqual(result.violations, []);
});

test('CLI exits nonzero for invalid stdin and unreadable files', () => {
  const invalid = spawnSync(process.execPath, [validator], { input: anchor + 'component Invalid [-0.2, 0.5]', encoding: 'utf8' });
  assert.equal(invalid.status, 1);
  assert.match(invalid.stdout, /COORD OUT OF RANGE/);
  const missing = spawnSync(process.execPath, [validator, join(tmpdir(), 'missing-wardley-map', 'map.owm')], { encoding: 'utf8' });
  assert.equal(missing.status, 1);
  assert.match(missing.stderr, /unable to read input/);
});

test('CLI reads files and preserves success with advisory reachability warnings', () => {
  const dir = mkdtempSync(join(tmpdir(), 'wardley-validator-test-'));
  try {
    const path = join(dir, 'map.owm');
    writeFileSync(path, valid + 'component Isolated [0.2, 0.5]\n');
    const result = spawnSync(process.execPath, [validator, path], { encoding: 'utf8' });
    assert.equal(result.status, 0);
    assert.match(result.stdout, /WARNING: UNREACHABLE COMPONENT/);
  } finally {
    rmSync(dir, { recursive: true, force: true });
  }
});
