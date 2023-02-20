import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr = np.array(my_data)
d = {'a': 10, 'b': 20, 'c': 30}

series_1 = pd.Series(data=my_data)
print(series_1)
print()

series_2 = pd.Series(data=my_data, index=labels)    # Creating a series with predefined data and labes
print(series_2)
print()

series_3 = pd.Series(my_data, labels)   # Creating a series with predefined data and labes (without using special Series class addnotaions)
print(series_3)
print()

series_4 = pd.Series(arr)
print(series_4)
print()

series_5 = pd.Series(arr, labels)
print(series_5)
print()

series_6 = pd.Series(d)
print(series_6)
print()

ser_1 = pd.Series([1, 2, 3, 4], ['USA', 'Germany', 'Poland', 'Ukraine'])
print(ser_1)
print()

ser_2 = pd.Series([1, 5, 3, 4], ['USA', 'France', 'Poland', 'Ukraine'])
print(ser_2)
print()

print(ser_1['USA'])     # Getting the data from ser_1 under the 'USA' index

ser_3 = pd.Series(data=labels)
print(ser_3)
print()

print(ser_3[0])     # Getting the data from ser_3 under the 0 index

print(ser_1 + ser_2)    # Adding ser_1 and ser_2 datas
