import numpy as np

import pandas as pd

"""
Pandas provides two types of classes for handling data:

Series: a one-dimensional labeled array holding data of any type
such as integers, strings, Python objects etc.

DataFrame: a two-dimensional data structure that holds data like a two-dimension array or a table with rows and columns.
"""
s = pd.Series([1, 3, 5, np.nan, 6, 8, None])
print(s)