import pandas as pd
import numpy as np


def cheque(prices, **kwargs):
    products = sorted(kwargs.keys())
    data = {
        "product": products,
        "price": [prices[i] for i in products],
        "number": [kwargs[i] for i in products],
        "cost": [prices[i] * kwargs[i] for i in products],
    }
    return pd.DataFrame(data)


products = ['bread', 'milk', 'soda', 'cream']
prices = [37, 58, 99, 72]
price_list = pd.Series(prices, products)
result = cheque(price_list, soda=3, milk=2, cream=1)
print(result)
