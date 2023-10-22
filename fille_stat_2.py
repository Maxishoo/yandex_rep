import json

filer = open(input(), "r", encoding="UTF-8")
filew = open(input(), "w", encoding="UTF-8")
d = {}
a = [int(i) for i in filer.read().split()]
d["count"] = len(a)
kpol = 0
for i in a:
    if i > 0:
        kpol += 1
d["positive_count"] = kpol
d["min"] = min(a)
d["max"] = max(a)
d["sum"] = sum(a)
d["average"] = float(f"{sum(a) / len(a):.2f}")
json.dump(d, filew, ensure_ascii=False, indent=2)
filer.close()
filew.close()