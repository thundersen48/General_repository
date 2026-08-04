import numpy as np
b  = np.fromfunction(lambda i, j: i == j, (2, 3), dtype=int)
print(b)

x = np.array([[1, 2], [3, 4]])
m = np.asmatrix(x)
x[0,0] = 5
print(m)
print(x)
