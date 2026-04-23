import re, sys
path = sys.argv[1]
strict = "--strict" in sys.argv
with open(path) as f:
    text = f.read()
m = re.search(r"```owm\s*\n([\s\S]*?)\n```", text)
if m:
    text = m.group(1)
nodes = []
for raw in text.split("\n"):
    line = raw.strip()
    if not line or line.startswith("//") or line.startswith("#"):
        continue
    mm = re.match(r"^(anchor|component)\s+(.+?)\s*\[\s*([0-9.]+)\s*,\s*([0-9.]+)\s*\]", line)
    if mm:
        v = float(mm.group(3))
        e = float(mm.group(4))
        nodes.append({"kind": mm.group(1), "name": mm.group(2).strip(), "v": v, "e": e})

NEAR = 0.02
BOUND_TOL = 0.01
BOUNDS = [0.25, 0.50, 0.75]
ANCH_HI = 0.98
ANCH_LO = 0.02
COMP_HI = 0.99
COMP_LO = 0.01
STAGE_LIMIT = 0.60

warnings = []

# near-dup pairs
for i in range(len(nodes)):
    for j in range(i+1, len(nodes)):
        a, b = nodes[i], nodes[j]
        if abs(a["v"]-b["v"]) < NEAR and abs(a["e"]-b["e"]) < NEAR:
            warnings.append(f"NEAR-DUP: '{a['name']}' [{a['v']},{a['e']}] ~ '{b['name']}' [{b['v']},{b['e']}]")

# boundary straddle
for n in nodes:
    if n["kind"] == "anchor":
        continue
    for bd in BOUNDS:
        if abs(n["e"] - bd) <= BOUND_TOL:
            warnings.append(f"BOUNDARY: '{n['name']}' e={n['e']} straddles stage boundary {bd}")

# canvas-edge
for n in nodes:
    if n["kind"] == "anchor":
        if n["v"] > ANCH_HI or n["v"] < ANCH_LO:
            warnings.append(f"ANCHOR-CLIP: '{n['name']}' v={n['v']}")
    else:
        if n["e"] > COMP_HI or n["e"] < COMP_LO:
            warnings.append(f"COMPONENT-CLIP: '{n['name']}' e={n['e']}")

# stage distribution
comps = [n for n in nodes if n["kind"] == "component"]
total = len(comps)
counts = [0,0,0,0]
for n in comps:
    e = n["e"]
    if e < 0.25: counts[0]+=1
    elif e < 0.50: counts[1]+=1
    elif e < 0.75: counts[2]+=1
    else: counts[3]+=1
names = ["Genesis","Custom","Product","Commodity"]
print(f"Stage distribution: Genesis={counts[0]}, Custom={counts[1]}, Product={counts[2]}, Commodity={counts[3]} (total {total})")
for i,c in enumerate(counts):
    if c == 0:
        warnings.append(f"STAGE-EMPTY: {names[i]} is empty")
    if c/total > STAGE_LIMIT:
        warnings.append(f"STAGE-IMBALANCE: {names[i]} has {c}/{total} = {c/total:.1%} (>60%)")

if not warnings:
    print("Layout OK - no warnings")
    sys.exit(0)
else:
    print(f"{len(warnings)} warnings:")
    for w in warnings:
        print("  " + w)
    sys.exit(1 if strict else 0)
