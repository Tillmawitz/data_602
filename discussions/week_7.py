import pandas as pd
import numpy as np

# 1
# Pandas is a Python library built on NumPy and Matplotlib intended for working with tabular data. It can be used to easily import, clean, analyze, and visualize datasets.

# 2
read_example = pd.read_csv("example.csv")

# 3
toy_df = pd.DataFrame(np.random.randint(0,100,size=(100,3)), columns=list('ABC'))

print(toy_df.head(10))
print("----------divider----------")

# 4
series_1 = pd.Series([2, 4, 6, 8, 10])
series_2 = pd.Series([1, 3, 5, 7, 10])

print(series_1.compare(series_2))
print("----------divider----------")

# 5
df1 = pd.Series(['hello', 'to', 'cuny', 'class?'])
print(df1.str.capitalize())