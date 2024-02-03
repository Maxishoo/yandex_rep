import pandas as pd

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
data = pd.read_csv("data.csv")
print(data[(data["x"] <= x2) & (data["y"] <= y1) & (data["x"] >= x1) & (data["y"] >= y2)])
