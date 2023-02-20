import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])     # Creating the pandas frame (datas are matrix of randn elements with dimentions of 5x4, rows are A, B, ..., collums are W, X, ...
print(df)
print()

print(df['W'])      # Getting the Series of data under W collumn
print(type(df['W']))
print()

print(df[['W', 'Z']])      # Getting the frame of data under in collumns W and Z
print()

df['new'] = df['W'] + df['Y']   # Adding collumn 'new' that holds sums of values of collumns 'W' and 'Y'
print(df)
print()

df.drop('new', axis=1, inplace=True)    # Deleting 'new' collumn (axis=1 means You want to delete collumn not a row, inplace=True means you want to do this permanently
print(df)
print()

print(df.shape)     # Getting dimensions of df frame
print()

print(df.loc['A'])      # Getting the Series of data under A row
print()

print(df.iloc[2])   # Getting the Series of data under C row by its index
print()

print(df.loc['B', 'Y'])     # Getting value in location B, Y
print()

print(df.loc[['A', 'B'], ['W', 'Y']])
print()

bool_df = df > 0
print(bool_df)   # Getting bool values of condition df > 0
print()
print(df[bool_df])   # Replacing data in df according to condition in booldf (we get normal values while condition is met, also we get bool values if its not)
print()
print(df[df > 0])
print()

print(df['W'] > 0)
print()
print(df[df['W'] > 0])      # Getting the Frame that have all rows with values bigger than 0 in W collumn (df without C row)
print()

res_df = df[df['W'] > 0]
print(res_df)
print()
print(df[df['W'] > 0]['X'])
print()

print(df[(df['W'] > 0) & (df['Y'] > 1)])    # Getting frame that mets multiple conditions, & means and, | means or
print(df[(df['W'] > 0) | (df['Y'] > 1)])
print()

print(df.reset_index())     # Showing indexes of rows
print()

newind = 'CA NY WY OR CO'.split()
print(newind)
print()

df['States'] = newind
print(df)
print()

print(df.set_index('States'))       # Converting 'States' collumn into row (at 0 index)
print()

outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))
# print(hier_index)
hier_index = pd.MultiIndex.from_tuples(hier_index)
# print(hier_index)

new_df = pd.DataFrame(randn(6, 2), hier_index, ['A', 'B'])      # Creating data frame with multiple indexes (indexes inside indexes)
print(new_df)
print(new_df.index.names)
new_df.index.names = ['Groups', 'Num']
print(new_df)
print()

print(new_df.loc['G2'].loc[2]['B'])
print()

print(new_df.xs(1, level='Num'))     # Getting values of row 1 in ewery parent row (level='Num' means it takes 1 indexes of 'Num' level
print()
