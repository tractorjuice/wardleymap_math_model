import re, sys
path = sys.argv[1]
with open(path) as f:
    text = f.read()
m = re.search(r"```owm\s*\n([\s\S]*?)\n```", text)
if m:
    text = m.group(1)
coords = {}
edges = []
for raw in text.split("\n"):
    line = raw.strip()
    if not line or line.startswith("//") or line.startswith("#"):
        continue
    node = re.match(r"^(?:anchor|component)\s+(.+?)\s*\[\s*([0-9.]+)\s*,\s*([0-9.]+)\s*\](?:\s+.*)?$", line)
    if node:
        name = node.group(1).strip()
        v = float(node.group(2))
        e = float(node.group(3))
        coords[name] = (v, e)
        continue
    if "->" in line and not line.startswith("evolve"):
        em = re.match(r"^(.+?)->(.+)$", line)
        if em:
            edges.append((em.group(1).strip(), em.group(2).strip()))
violations = []
for n, (v, e) in coords.items():
    if not (0 <= v <= 1):
        violations.append(f"COORD OUT OF RANGE: '{n}' visibility={v}")
    if not (0 <= e <= 1):
        violations.append(f"COORD OUT OF RANGE: '{n}' evolution={e}")
for s, t in edges:
    if s not in coords:
        violations.append(f"UNKNOWN SOURCE: edge '{s}->{t}' -- '{s}' not declared")
    if t not in coords:
        violations.append(f"UNKNOWN TARGET: edge '{s}->{t}' -- '{t}' not declared")
for s, t in edges:
    if s in coords and t in coords:
        vs = coords[s][0]
        vt = coords[t][0]
        if vs < vt:
            violations.append(f"VISIBILITY VIOLATION: {s}(v={vs}) -> {t}(v={vt}) -- source must be at or above target")
if not violations:
    print(f"OK: {len(coords)} components, {len(edges)} edges -- no violations")
    sys.exit(0)
else:
    print(f"{len(violations)} violations:")
    for v in violations:
        print("  " + v)
    sys.exit(1)
