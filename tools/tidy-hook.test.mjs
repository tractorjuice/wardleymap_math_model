import test from 'node:test';
import assert from 'node:assert/strict';
import { tidyMarkdown, tidyFileContent } from './tidy-hook.mjs';

// A stub tidy function — wraps the body so we can see exactly what was tidied
// without shelling out to the real placement engine.
const stub = (text) => `TIDIED(${text})`;

test('tidies a fenced mermaid wardley-beta block in markdown', () => {
  const md = [
    '# My Map',
    '',
    'Some prose.',
    '',
    '```mermaid',
    'wardley-beta',
    'component A [0.5, 0.5]',
    '```',
    '',
    'More prose.',
    '',
  ].join('\n');
  const out = tidyMarkdown(md, stub);
  assert.match(out, /```mermaid\nTIDIED\(wardley-beta\ncomponent A \[0\.5, 0\.5\]\)\n```/);
  assert.match(out, /^# My Map$/m);
  assert.match(out, /^Some prose\.$/m);
  assert.match(out, /^More prose\.$/m);
});

test('leaves a non-wardley mermaid block untouched', () => {
  const md = ['```mermaid', 'flowchart TD', 'A --> B', '```', ''].join('\n');
  assert.equal(tidyMarkdown(md, stub), md);
});

test('leaves a non-mermaid fenced block untouched', () => {
  const md = ['```js', 'const wardley-beta = 1;', '```', ''].join('\n');
  assert.equal(tidyMarkdown(md, stub), md);
});

test('does not touch an OWM block that shares component syntax', () => {
  const md = [
    '## OWM',
    '',
    '```',
    'title Canonical',
    'component A [0.5, 0.5]',
    '```',
    '',
    '## Mermaid',
    '',
    '```mermaid',
    'wardley-beta',
    'component A [0.5, 0.5]',
    '```',
    '',
  ].join('\n');
  const out = tidyMarkdown(md, stub);
  // The plain (OWM) fence is verbatim; only the mermaid fence is tidied.
  assert.match(out, /```\ntitle Canonical\ncomponent A \[0\.5, 0\.5\]\n```/);
  assert.match(out, /```mermaid\nTIDIED\(/);
});

test('tidyFileContent tidies a whole standalone .mmd', () => {
  const mmd = 'wardley-beta\ncomponent A [0.5, 0.5]\n';
  assert.equal(tidyFileContent('map.mmd', mmd, stub), `TIDIED(${mmd})`);
});

test('tidyFileContent ignores a .mmd that is not wardley-beta', () => {
  assert.equal(tidyFileContent('chart.mmd', 'flowchart TD\nA --> B\n', stub), null);
});

test('tidyFileContent ignores unrelated extensions', () => {
  assert.equal(tidyFileContent('notes.txt', 'wardley-beta\n', stub), null);
});
