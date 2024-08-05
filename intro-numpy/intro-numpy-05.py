import numpy as np

a = np.array([1,2,3])
b = np.array([1,2,4])

# mask = a==b
# print(mask) 
# print(a[mask])
# print(b[mask])
# print(~mask)
# print(a[~mask])
# print(b[~mask])
# print(np.all(a==b))
# print(np.any(a==b))
# print(np.sum(mask))
# print(np.sum(a > 2))
# c = np.array([-1,0,1])
# print(1/c)
# print(np.sum(np.isfinite(1/c)))
# print(np.sum(np.isinf(1/c)))

d = [1,np.nan,2,3,np.nan] 
mask = np.isnan(d)
print(mask)
print(np.sum(mask))
print(np.mean(mask))
