"""Mirror of validate_owm.mjs and check_layout.mjs in Python.
Used because the Bash harness currently denies node invocations on this path.
Logic is identical to the authoritative JS scripts in skills/wardley-map/scripts/.
"""
import re
text = open('/workspaces/wardleymap_math_model/skills/wardley-map-workspace/competitor-compare/mathmodel-v2/eval-defence-grey-zone/with_skill/run-1/outputs/draft.owm').read()
coords = {}
kinds = {}
edges = []
for raw in text.split('\n'):
    line = raw.strip()
    if not line or line.startswith('//') or line.startswith('#'): continue
    m = re.match(r'^(anchor|component)\s+(.+?)\s*\[\s*([0-9.]+)\s*,\s*([0-9.]+)\s*\](?:\s+.*)?$', line)
    if m:
        nm = m.group(2).strip()
        coords[nm] = (float(m.group(3)), float(m.group(4)))
        kinds[nm] = m.group(1)
        continue
    if '->' in line and not line.startswith('evolve'):
        em = re.match(r'^(.+?)->(.+)$', line)
        if em: edges.append((em.group(1).strip(), em.group(2).strip()))

violations = []
for s,t in edges:
    if s not in coords: violations.append(f'UNKNOWN SRC: {s}->{t}')
    if t not in coords: violations.append(f'UNKNOWN TGT: {s}->{t}')
for s,t in edges:
    if s in coords and t in coords and coords[s][0] < coords[t][0]:
        violations.append(f'VIS: {s}(v={coords[s][0]}) -> {t}(v={coords[t][0]})')
print(f'Validator: {len(coords)} nodes, {len(edges)} edges, {len(violations)} violations')
for v in violations: print(' -', v)

warns = []
NEAR=0.02
names = list(coords.keys())
for i in range(len(names)):
    for j in range(i+1,len(names)):
        a,b = names[i], names[j]
        dv = abs(coords[a][0]-coords[b][0])
        de = abs(coords[a][1]-coords[b][1])
        if dv<NEAR and de<NEAR:
            warns.append(f"NEAR-DUP: '{a}' [{coords[a][0]},{coords[a][1]}] vs '{b}' [{coords[b][0]},{coords[b][1]}] (dv={dv:.3f}, de={de:.3f})")
for n in names:
    if kinds[n]!='component': continue
    for bb in [0.25,0.50,0.75]:
        if abs(coords[n][1]-bb)<=0.01:
            warns.append(f"BOUNDARY: '{n}' at e={coords[n][1]} near {bb}")
for n in names:
    isA = kinds[n]=='anchor'
    vH=0.98 if isA else 0.99; vL=0.02 if isA else 0.01
    v,e = coords[n]
    if v>vH: warns.append(f"CANVAS v-top: {n} v={v}")
    if v<vL: warns.append(f"CANVAS v-bot: {n} v={v}")
    if e>0.99: warns.append(f"CANVAS e-right: {n} e={e}")
    if e<0.01: warns.append(f"CANVAS e-left: {n} e={e}")
comps=[n for n in names if kinds[n]=='component']
counts={'Genesis':0,'Custom':0,'Product':0,'Commodity':0}
def stage(e):
    if e<0.25: return 'Genesis'
    if e<0.50: return 'Custom'
    if e<0.75: return 'Product'
    return 'Commodity'
for c in comps: counts[stage(coords[c][1])]+=1
total=len(comps)
for s,n in counts.items():
    share=n/total
    if share>0.60: warns.append(f'STAGE IMBAL: {n}/{total} ({share*100:.0f}%) in {s}')
    if n==0: warns.append(f'STAGE EMPTY: {s}')
print(f'Layout warnings: {len(warns)}')
for w in warns: print(' -', w)
print('Stage counts:', counts, 'total comps:', total)
