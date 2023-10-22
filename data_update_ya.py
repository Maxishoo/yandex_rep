import json
from sys import stdin

file = open(input(), 'r', encoding="UTF-8")
d = json.load(file)
file.close()
lines = []
for line in stdin:
    lines.append(line.rstrip('\n'))
for i in lines:
    d[i.split(" == ")[0]] = i.split(" == ")[1]

file = open('jss.json', 'w', encoding="UTF-8")
json.dump(d, file, ensure_ascii=False, indent=2)
file.close()