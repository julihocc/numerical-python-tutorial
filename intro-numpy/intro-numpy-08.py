import numpy as np

# subsetting
a = np.arange(11,21)
# print(a)
# print(a[1])

b = np.arange(11,31).reshape(4,5)
# print(b[1,2])
# print(b[1])
# print(b[1][2])

# slicing
# print(a)
# c = a[2:5]
# a[3] = -1
# print(a)
# print(c)

# print(b)
# print(b[2])
# print(b[2][1:3+1])
# print(b[0:2, 1:3])
# print(b[:,2:])

# print(a)
# print(a[1::2])
# print(a[ : :-1])

# np.random.seed(123)
# x = np.random.randint(1,11,size=10)
# print(x)
# x.sort()
# print(x)
# print(x[::-1])

# y = np.random.randint(1,11,size=(4,5))
# print(y)
# y.sort(axis=0)
# print(y)

# print(a)
# pares = a%2==0
# print(pares) 
# print(a[pares])

np.random.seed(123)
x = np.random.randint(1,11,size=10)
print(x)
print(x[x<10])