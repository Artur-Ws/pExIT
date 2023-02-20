import numpy as np
import pandas as pd

d = {'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]}
df = pd.DataFrame(d)
print(df)
print()

print(df.dropna())      # It purges data frame from rows that contains NaN values (no value at all)
print()

print(df.dropna(axis=1))        # It purges data frame from collumns that contains NaN values (no value at all)
print()

print(df.dropna(thresh=2))      # It purges data frame from rows that contains more or eqal to 2 NaN values (no value at all)
print()

print(df.fillna(value='Fill value'))        # It fills cells with Nan value with predefined value
print()

print(df['A'].fillna(value=df['A'].mean()))
print()
