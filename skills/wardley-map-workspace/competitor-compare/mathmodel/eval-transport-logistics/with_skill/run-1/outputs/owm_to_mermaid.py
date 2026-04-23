#!/usr/bin/env python3
"""Simplified mirror of skills/wardley-map/scripts/owm_to_mermaid.mjs.

This handles the subset of OWM emitted by the skill for this map: title, style,
anchor, component, edges, evolve, note. Always quotes names with double quotes.
"""
import os
import re
import sys


def quote_name(name):
    name = name.strip()
    if name.startswith('"') and name.endswith('"'):
        return name
    return '"' + name.replace('"', "'") + '"'


def inline_strip(s):
    m = re.match(r'^(.+?)\s+//(?!/)(.*)$', s)
    if m and '://' not in m.group(1):
        return m.group(1).strip()
    return s


COMP_RE = re.compile(r'^component\s+(.+?)\s*(\[[\d.,\s]+\])', re.I)
ANCHOR_RE = re.compile(r'^anchor\s+(.+?)\s*(\[[\d.,\s]+\])', re.I)
EVOLVE_RE = re.compile(r'^evolve\s+(.+?)\s+([\d.]+)', re.I)
NOTE_RE = re.compile(r'^note\s+(.+?)\s+(\[[\d.,\s]+\])\s*$', re.I)


def convert(owm, filename=''):
    out = ['wardley-beta']
    has_title = False
    for raw in owm.split('\n'):
        s = raw.strip()
        if not s:
            out.append('')
            continue
        if s.startswith('//'):
            continue
        s = inline_strip(s)
        if not s:
            continue
        if re.match(r'^style\s+wardley\s*$', s, re.I):
            continue
        if re.match(r'^title\s+', s, re.I):
            out.append(s)
            out.append('size [1100, 800]')
            has_title = True
            continue
        ma = ANCHOR_RE.match(s)
        if ma:
            out.append(f"anchor {quote_name(ma.group(1).strip())} {ma.group(2)}")
            continue
        mc = COMP_RE.match(s)
        if mc:
            cname = mc.group(1).strip()
            coords = mc.group(2)
            has_inertia = bool(re.search(r'\binertia\s*$', s, re.I))
            line = f"component {quote_name(cname)} {coords}"
            if has_inertia:
                line += ' (inertia)'
            out.append(line)
            continue
        mev = EVOLVE_RE.match(s)
        if mev:
            out.append(f"evolve {quote_name(mev.group(1).strip())} {mev.group(2)}")
            continue
        mn = NOTE_RE.match(s)
        if mn:
            text = mn.group(1).strip()
            coord = mn.group(2)
            text = text.strip('"')
            out.append(f'note "{text}" {coord}')
            continue
        if '->' in s and not re.match(r'^(evolve|component|pipeline|anchor|note)\s', s, re.I):
            arrow = s.find('->')
            left = quote_name(s[:arrow].strip())
            right = quote_name(s[arrow + 2:].strip())
            out.append(f"{left} -> {right}")
            continue
    if not has_title and filename:
        base = os.path.basename(filename)
        base = re.sub(r'\.\w+$', '', base).replace('-', ' ').replace('_', ' ')
        out.insert(1, f'title {base}')
        out.insert(2, 'size [1100, 800]')
    # collapse consecutive blanks
    cleaned = []
    last_empty = False
    for ln in out:
        if ln == '':
            if not last_empty:
                cleaned.append(ln)
            last_empty = True
        else:
            cleaned.append(ln)
            last_empty = False
    return '\n'.join(cleaned)


def main():
    src = sys.argv[1]
    with open(src) as f:
        text = f.read()
    print(convert(text, src))


if __name__ == '__main__':
    main()
