import numpy as np
from numpy import multiply

v = np.array([1,0])
w = np.array([0,1])

c,d =[3,2]
r = c*v+d*w
# print(r)
s = np.add(np.multiply(c,v), np.multiply(d,w))
# print(s)

v = np.array([2,-5])
w = np.array([-3,7])

# print(v*w)
# print(np.multiply(v,w))
# print(v/w)
# print(np.divide(v,w))

# def dot(r,s):
# 	accum = 0 
# 	for x,y in zip(r,s): 
# 		accum += x*y
# 	return accum

def dot(r,s): 
	return sum([x*y for x,y in zip(r,s)])

print(dot(v,w))
print(np.dot(v,w))

