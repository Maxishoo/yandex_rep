import numpy as np
import pandas as pd


def length_stats(text):
    text = text.lower()
    text2 = ""
    for i in text:
        if (i >= "a" and i <= "z") or (i >= "а" and i <= "я") or i == ' ':
            text2 += i
    data = {i: len(i) for i in sorted(text2.split())}
    return pd.Series(data)


print(length_stats('Лес, опушка, странный домик. Лес, опушка и зверушка.'))
