import numpy as np

arr = np.arange(6).reshape(3, 2)
print('The original array:')
print(arr, "\n")
print('After applying ravel function:')
print(arr.ravel())

#Maintaining F order
print('ravel function in F-style ordering:')
print(arr.ravel(order='F'))

#K-order preserving the ordering
print("\nnumpy.ravel() function in K-style ordering: ", arr.ravel(order='K'))
print(np.random.randn(5))