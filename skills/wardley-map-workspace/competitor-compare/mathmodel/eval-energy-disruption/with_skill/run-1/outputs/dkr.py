import re, sys
path = sys.argv[1]
with open(path) as f:
    text = f.read()
coords = {}
edges = []
anchors = set()
for raw in text.split("\n"):
    s = raw.strip()
    if not s or s.startswith("//") or s.startswith("#"):
        continue
    m = re.match(r"^(anchor|component)\s+(.+?)\s*\[\s*([0-9.]+)\s*,\s*([0-9.]+)\s*\]", s)
    if m:
        name = m.group(2).strip()
        v = float(m.group(3))
        e = float(m.group(4))
        coords[name] = (v, e)
        if m.group(1) == "anchor":
            anchors.add(name)
        continue
    if "->" in s and not s.startswith("evolve"):
        em = re.match(r"^(.+?)->(.+)$", s)
        if em:
            edges.append((em.group(1).strip(), em.group(2).strip()))
# D = v*(1-e)
D = [(n, v*(1-e)) for n,(v,e) in coords.items() if n not in anchors]
D.sort(key=lambda x: -x[1])
print("TOP D (Differentiation pressure = v*(1-e)):")
for n,s in D[:8]:
    v,e = coords[n]
    print(f"  {n:45s} v={v:.2f} e={e:.2f} D={s:.3f}")
# K = (1-v)*e
K = [(n, (1-v)*e) for n,(v,e) in coords.items() if n not in anchors]
K.sort(key=lambda x: -x[1])
print("\nTOP K (Commodity leverage = (1-v)*e):")
for n,s in K[:8]:
    v,e = coords[n]
    print(f"  {n:45s} v={v:.2f} e={e:.2f} K={s:.3f}")
# R = v(src)*(1-e(tgt))
R = []
for s,t in edges:
    if s in coords and t in coords:
        vs = coords[s][0]
        et = coords[t][1]
        R.append((s, t, vs*(1-et)))
R.sort(key=lambda x: -x[2])
print("\nTOP R (Dependency risk = v(src)*(1-e(tgt))):")
for a,b,s in R[:12]:
    print(f"  {a:38s} -> {b:38s} R={s:.3f}")
