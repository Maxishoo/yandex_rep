import json
from sys import stdin

with open("jss.json", 'r', encoding="UTF-8") as fscore:
    score = json.load(fscore)
answers = []
for s in stdin:
    answers.append(s.rstrip('\n'))
tecktest = 0
teckblok = 0
oktest = 0
points = 0
for i in answers:
    if tecktest == len(score[teckblok]["tests"]):
        points += score[teckblok]["points"] * (oktest / len(score[teckblok]["tests"]))
        oktest = 0
        teckblok += 1
        tecktest = 0
    if i == score[teckblok]["tests"][tecktest]["pattern"]:
        oktest += 1
    tecktest += 1
if tecktest == len(score[teckblok]["tests"]):
    points += score[teckblok]["points"] * (oktest / len(score[teckblok]["tests"]))
print(int(points))