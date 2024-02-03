import pandas as pd
import numpy as np


def get_long(in_data, min_length=5):
    return pd.Series({i: in_data[i] for i in in_data.index if in_data[i] >= min_length}, dtype="int64")


data = pd.Series([3, 5, 6, 6], ['мир', 'питон', 'привет', 'яндекс'])
filtered = get_long(data, min_length=6)
print(data)
print(filtered)
