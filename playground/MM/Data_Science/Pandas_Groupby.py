import pandas as pd
import numpy as np

data = {'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'], 'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'], 'Sales': [200, 120, 340, 124, 243, 350]}

df = pd.DataFrame(data)
print(df)
print()

byCopm = df.groupby('Company')      # Grouping the data frame by 'Company' column
print(byCopm)       # We will display the memory address of this data
print()
print(byCopm.mean(numeric_only=True))        # mean is for displaying mean value for gropued column
print()
print(byCopm.sum(numeric_only=True))        # mean is for displaying sum of values for gropued column
print()
print(byCopm.std(numeric_only=True))        # mean is for displaying standard deviation of values for gropued column
print()

print(byCopm.sum(numeric_only=True).loc['FB'])       # it display sum of sales of 'FB' Company
print()

print(df.groupby('Company').sum(numeric_only=True).loc['FB'])    # We can use one line statement, don't have to store this into new variable
print()

print(df.groupby('Company').count())    # It shows hov many instances we have in group in every column (numeric and non numereic)
print()

print(df.groupby('Company').describe().transpose())    # It shows lots of data Yuo can get from Your grouped Data Frame, transpose rebuild the data frame in different order
print()
