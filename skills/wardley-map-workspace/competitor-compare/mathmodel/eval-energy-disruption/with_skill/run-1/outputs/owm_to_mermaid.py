import re, sys, os
path = sys.argv[1]
with open(path) as f:
    text = f.read()
m = re.search(r"```owm\s*\n([\s\S]*?)\n```", text)
if m:
    text = m.group(1)

def q(name):
    name = name.strip()
    if name.startswith('"') and name.endswith('"'):
        return name
    return '"' + name.replace('"', "'") + '"'

lines = text.split("\n")
out = ["wardley-beta"]
has_title = False
for raw in lines:
    s = raw.strip()
    if not s:
        out.append("")
        continue
    if s.startswith("//"):
        continue
    if re.match(r"^style\s+wardley\s*$", s, re.I):
        continue
    # title
    m1 = re.match(r"^title\s+(.+)$", s, re.I)
    if m1:
        out.append(s)
        out.append("size [1100, 800]")
        has_title = True
        continue
    # anchor
    m1 = re.match(r"^anchor\s+(.+?)\s*(\[[\d.,\s]+\])", s, re.I)
    if m1:
        out.append(f"anchor {q(m1.group(1).strip())} {m1.group(2)}")
        continue
    # component
    m1 = re.match(r"^component\s+(.+?)\s*(\[[\d.,\s]+\])", s, re.I)
    if m1:
        cname = m1.group(1).strip()
        coords = m1.group(2)
        has_inertia = bool(re.search(r"\binertia\s*$", s, re.I))
        line = f"component {q(cname)} {coords}"
        if has_inertia:
            line += " (inertia)"
        out.append(line)
        continue
    # evolve (take last space-separated token as number)
    m1 = re.match(r"^evolve\s+(.+)\s+([\d.]+)\s*$", s, re.I)
    if m1:
        out.append(f"evolve {q(m1.group(1).strip())} {m1.group(2)}")
        continue
    # note
    m1 = re.match(r"^note\s+(.+?)\s+(\[[\d.,\s]+\])\s*$", s, re.I)
    if m1:
        txt = m1.group(1).strip()
        coord = m1.group(2)
        txt = re.sub(r'^"|"$', '', txt)
        out.append(f'note "{txt.replace(chr(34), chr(39))}" {coord}')
        continue
    # edge
    if "->" in s and not re.match(r"^(evolve|component|pipeline|anchor|note)\s", s, re.I):
        if "->" in s:
            left, right = s.split("->", 1)
            out.append(f"{q(left.strip())} -> {q(right.strip())}")
            continue
# Collapse multi blanks
cleaned = []
last_empty = False
for ln in out:
    if ln == "":
        if not last_empty:
            cleaned.append(ln)
        last_empty = True
    else:
        cleaned.append(ln)
        last_empty = False
print("\n".join(cleaned))
