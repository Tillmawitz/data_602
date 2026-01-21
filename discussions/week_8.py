import pandas as pd
import numpy as np
from dateutil import parser

toy_df = pd.DataFrame(np.random.randint(0,10,size=(10,3)), columns=list('ABC'), index = list('abcdefghij'))
print(toy_df)
print("----------divider----------")

# 1
# Delete index
toy_df.reset_index(drop = True, inplace = True)
print(toy_df)
print("----------divider----------")

# Delete column
toy_df.drop(columns='B', inplace=True)
print(toy_df)
print("----------divider----------")

# Delete row
toy_df.drop(9, inplace=True)
print(toy_df)
print("----------divider----------")

# 2
# Iterating over the dataframe.
for row in toy_df.itertuples():
    print(f"{row.A} * {row.C} = {row.A * row.C}")
print("----------divider----------")

# 3
# How would you convert a string to a date?
date_str = "2024/08/16"
datetime_obj = parser.parse(date_str)
print(type(datetime_obj))
print(str(datetime_obj))
print("----------divider----------")

# 4
# What is data aggregation?  Give an example in Python. 
# An aggregation is a function performed across the elements of a row or column which produces a single output. Examples are summation or finding the max value.
print(toy_df.agg(['sum', 'min', 'mean']))
print("----------divider----------")

# 5
# groupby() in Pandas is a method of subsetting a dataframe by a particular column or set of columns, usually for the purpose of aggregating by subset or applying a function to a particular subset.
other_df = pd.DataFrame({'Favorite Color': ['Blue', 'Green', 'Blue', 'Green'], 'Age': [5, 8, 9, 4]})
print(other_df)
print(other_df.groupby('Favorite Color').agg(['size', 'mean']))
