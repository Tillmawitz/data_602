import numpy as np

# 3

one_dim = np.arange(10)
print(one_dim)

# 4
array1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
odds = array1[array1 % 2 != 0]
print(odds)

# 5
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
common = np.intersect1d(a, b)
print(common)

# 6
a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])
unique = a[~np.isin(a,b)]
print(unique)

# 7
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])

if (np.isnan(iris).any()):
    print("There is missing data")
else:
    print("There is NOT missing data")
