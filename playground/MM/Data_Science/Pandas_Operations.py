import pandas as pd
import numpy as np

df = pd.DataFrame({'col1': [1, 2, 3, 4], 'col2': [444, 555, 666, 444], 'col3': ['abc', 'def', 'ghi', 'xyz']})
df.head()

print(df)
print()

print(df['col2'].unique())      # Printing out the unique values of specified columns
print()
print(df['col2'].nunique())     # Quantity of unique values of specified column
print()
print(df['col2'].value_counts())    # Quantity of every unique value in specified column
print()

print(df[(df['col1'] > 2) & (df['col2'] == 444)])       # Conditional selection of values in data frame
print()


def times2(x):

    return x*2


print(df['col1'].sum())
print()
print(df['col1'].apply(times2))     # apply lets Yuo apply any function (Yours or build in) on data frame
print()
print(df['col3'].apply(len))
print()
print(df['col2'].apply(lambda x: x*2))
print()

print(df.columns)
print(df.index)
print()

print(df.sort_values('col2'))       # Sort rows of data frame by specified column
print()

print(df.isnull())      # Shows if there is any null value in DF
print()

