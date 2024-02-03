import pandas as pd


def update(data):
    out = data.copy().assign(average=lambda x: (x["maths"] + x["physics"] + x['computer science']) / 3)
    return out.sort_values(["average", "name"], ascending=(False, True))


def best(data):
    return data[(data["maths"] > 3) & (data["physics"] > 3) & (data['computer science'] > 3)]


def need_to_work_better(data):
    return data[(data["maths"] == 2) | (data["physics"] == 2) | (data['computer science'] == 2)]


columns = ['name', 'maths', 'physics', 'computer science']
data = {
    'name': ['Иванов', 'Петров', 'Сидоров', 'Васечкин', 'Николаев'],
    'maths': [5, 4, 5, 2, 4],
    'physics': [4, 4, 4, 5, 5],
    'computer science': [5, 2, 5, 4, 3]
}
journal = pd.DataFrame(data, columns=columns)
filtered = update(journal)
print(journal)
print(filtered)
