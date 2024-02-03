import numpy as np
import pandas as pd


def length_stats(text):
    text = text.lower()
    text2 = ""
    for i in text:
        if i.isalpha() or i == ' ':
            text2 += i
    data1 = {i: len(i) for i in sorted(text2.split()) if len(i) % 2 == 0}
    data2 = {i: len(i) for i in sorted(text2.split()) if len(i) % 2 != 0}
    return (pd.Series(data2, dtype="int64"), pd.Series(data1, dtype="int64"))


odd, even = length_stats('Лес, опушка, странный домик. Лес, опушка и зверушка.')
print(odd)
print(even)
