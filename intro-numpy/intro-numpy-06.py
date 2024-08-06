import numpy as np

# print(np.sum([0.5, 1.5]))
# print(np.sum([0.5, 0.7, 0.2, 1.5], dtype=np.int32))
# print(np.sum([[0, 1], [0, 5]])) 
# print(np.sum([[0, 1], [0, 5]], axis=0))
# print(np.sum([[0, 1], [0, 5]], axis=1))
# print(np.sum([[0, 1], [np.nan, 5]], where=[False, True], axis=1))

# a = np.array([-1,0,1,2])

# a = np.arange(6).reshape((2,3))
# print(a)
# print(a.min())
# print(np.min(a))
# print(np.min(a, axis=0))
# print(np.min(a, axis=1))
# print(a.min(axis=0))
# print(a.min(axis=1))
# print(a.max())

# b = np.arange(10) 
# print(b)
# print(np.cumsum(b))

# np.random.seed(123)
# c = np.around(np.random.normal(1.7, .15, 325), 2)
# # print(c)
# print(np.mean(c))
# print(np.std(c))
# print(np.median(c))

import matplotlib.pyplot as plt 

x = np.linspace(0,10,21)
ruido = np.random.normal(0,0.35,len(x))
y = 2*x + ruido 

r = np.corrcoef(x,y)
print(r)

plt.scatter(x,y)
plt.show()

