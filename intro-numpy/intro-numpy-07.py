import numpy as np

# a = [1,2,[4,5]]
# b = a[:]
# a[0] = 6
# c = a[2]
# c[1] = 7
# print(a,b)

a = np.arange(24)
# b = np.copy(a)
# b = a.copy()
# a[0]=24
# print(a, b)

b = a.copy().reshape(6,4)
a[0] = 24
print(b)

