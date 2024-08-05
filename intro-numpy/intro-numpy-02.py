import numpy as np

data = [15.10,0.57,11.00,0.75,2.35]

arr01 = np.array(data, dtype=np.float128)
print(arr01)
print(arr01.dtype)

arr02 = arr01.astype(np.float16)
print(arr02)
print(arr02.dtype)

complex_arr = np.array([1+0.5j,2,3], dtype=complex) 
print(complex_arr)

imaginario = np.sqrt([-1], dtype=complex)
print(imaginario)
