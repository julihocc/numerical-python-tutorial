import numpy as np 
import matplotlib.pyplot as plt 

# a = 0
# b = 1
# num_puntos = 50
# num_subintervalos = num_puntos - 1
# h = (b-a)/num_subintervalos
# print(h)
## 0. -> .5 -> 1.

a = -2*np.pi
b = 2*np.pi 
h = 0.01
num_subintervalos = int(np.ceil((b-a)/h))
num_puntos = num_subintervalos+1
# print(num_puntos)

x = np.linspace(a,b,num=num_puntos)
# y = np.sin(x)
# y = 2*x+np.random.normal(0, 0.5, size = len(x))

def f(x):
	return x**2-1

y = f(x)

plt.plot(x, y)
plt.show()