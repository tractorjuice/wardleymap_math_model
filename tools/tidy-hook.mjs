#!/usr/bin/env node
/**
 * Claude Code PostToolUse hook — tidies wardley-beta map labels after a write.
 *
 * This repo embeds maps as fenced ```mermaid blocks inside `.md` files (after a
 * canonical OWM block), and never writes standalone `.mmd` maps from the skill.
 * So the hook is block-aware:
 *
 *   - `.md` file  — only fenced ```mermaid blocks whose body is a wardley-beta
 *                   map are tidied, spliced back in place. Prose and the OWM
 *                   block are left byte-for-byte untouched.
 *   - `.mmd` file — the whole file is a wardley-beta map and is tidied directly.
 *
 * Tidying shells out to the published `wardley-tidy` tool (single source of
 * truth for the placement engine). Set WARDLEY_TIDY_PKG to override the package
 * spec (e.g. to pin a branch). The hook always exits 0 — a hook failure must
 * never block the tool that triggered it.
 */
import { readFileSync, writeFileSync, mkdtempSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { realpathSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

const TIDY_PKG = process.env.WARDLEY_TIDY_PKG || 'github:tractorjuice/wardley-maps-mermaid';

/**
 * Tidy one chunk of wardley-beta text via the published `wardley-tidy` tool.
 * @param {string} text
 * @returns {string} tidied text (no trailing newline)
 */
export const tidyBlockViaNpx = (text) => {
  const dir = mkdtempSync(join(tmpdir(), 'wardley-tidy-'));
  const file = join(dir, 'map.mmd');
  writeFileSync(file, text, 'utf8');
  const out = execFileSync('npx', ['--yes', TIDY_PKG, 'wardley-tidy', '--stdout', file], {
    encoding: 'utf8',
  });
  return out.replace(/\n$/, '');
};

/**
 * Tidy every fenced ```mermaid block holding a wardley-beta map, in place.
 * Non-mermaid fences and non-wardley mermaid blocks are returned verbatim.
 * @param {string} md markdown source
 * @param {(text: string) => string} tidyBlock
 * @returns {string}
 */
export const tidyMarkdown = (md, tidyBlock) => {
  const fence = /(^|\n)([ \t]*)(`{3,})mermaid[ \t]*\n([\s\S]*?)\n[ \t]*\3/g;
  return md.replace(fence, (whole, pre, indent, ticks, body) => {
    if (!/^\s*wardley-beta\b/m.test(body)) {
      return whole;
    }
    const tidied = tidyBlock(body);
    return `${pre}${indent}${ticks}mermaid\n${tidied}\n${indent}${ticks}`;
  });
};

/**
 * Compute the tidied content for a written file, or null if nothing to do.
 * @param {string} filePath
 * @param {string} content
 * @param {(text: string) => string} tidyBlock
 * @returns {string|null}
 */
export const tidyFileContent = (filePath, content, tidyBlock) => {
  if (/\.mmd$/i.test(filePath)) {
    if (!/^\s*wardley-beta\b/m.test(content)) {
      return null;
    }
    return tidyBlock(content);
  }
  if (/\.md$/i.test(filePath)) {
    return tidyMarkdown(content, tidyBlock);
  }
  return null;
};

const main = () => {
  let payload;
  try {
    payload = JSON.parse(readFileSync(0, 'utf8'));
  } catch {
    return; // no/garbled payload — nothing to do
  }
  const filePath = payload?.tool_input?.file_path ?? payload?.tool_input?.path;
  if (!filePath || !/\.(mmd|md)$/i.test(filePath)) {
    return;
  }
  let content;
  try {
    content = readFileSync(filePath, 'utf8');
  } catch {
    return;
  }
  try {
    const next = tidyFileContent(filePath, content, tidyBlockViaNpx);
    if (next != null && next !== content) {
      writeFileSync(filePath, next, 'utf8');
    }
  } catch {
    // Tidy failed — leave the file as-is, never block the write.
  }
};

const isMain = (() => {
  if (!process.argv[1]) {
    return false;
  }
  try {
    return fileURLToPath(import.meta.url) === realpathSync(process.argv[1]);
  } catch {
    return false;
  }
})();

if (isMain) {
  main();
  process.exit(0);
}
