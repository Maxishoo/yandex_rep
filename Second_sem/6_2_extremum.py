import pandas as pd
import numpy

def values(func, start, end, step):
    lst = np.arange(start, end + step, step)
    return pd.Series(lst, index=lst, dtype='float64')


def min_extremum(data):
    return min(data[data == min(data)].index)


def max_extremum(data):
    return max(data[data == max(data)].index)


data = values(lambda x: x ** 2 + 2 * x + 1, -1.5, 1.7, 0.1)
print(data)
print(min_extremum(data))
print(max_extremum(data))
