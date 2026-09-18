import csv, random
WEIGHTS={"C1":20,"C2":20,"C3":20,"C4":15,"C5":10,"C6":10,"C7":5}
TIE_BREAK=["C1","C2","C3","C4","C6"]
def load_matrix(path="SCORE_MATRIX.csv"):
    with open(path, encoding="utf-8-sig") as f:
        rows=list(csv.DictReader(f))
    for r in rows:
        for c in WEIGHTS: r[c]=int(r[c])
    return rows
def weighted_score(row, weights=WEIGHTS):
    return sum(row[c]*weights[c]/5 for c in WEIGHTS)
def ordered(rows, weights=WEIGHTS):
    return sorted(rows,key=lambda r:(-weighted_score(r,weights),*[-r[c] for c in TIE_BREAK],r["participant"]))
rows=load_matrix()
assert sum(WEIGHTS.values())==100
for i,r in enumerate(ordered(rows),1):
    print(i,r["participant"],round(weighted_score(r)))
random.seed(20260918)
runs=50000; ada_first=0; top3_same=0
for _ in range(runs):
    raw={c:WEIGHTS[c]*(1+random.uniform(-0.2,0.2)) for c in WEIGHTS}
    k=100/sum(raw.values()); w={c:v*k for c,v in raw.items()}
    order=ordered(rows,w)
    ada_first += order[0]["participant"]=="Ada Tours"
    top3_same += [r["participant"] for r in order[:3]]==["Ada Tours","LATAM-CLUB","Мачете Тур"]
print("Sensitivity runs:",runs)
print("Ada Tours first:",ada_first)
print("Top-3 order unchanged:",top3_same)
