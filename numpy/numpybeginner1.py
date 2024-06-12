import numpy as np
a = np.array([1, 2, 3, True])# создаем  одномерный массив и передаем в него список
print(a.dtype)
print(a[0])
a[1] = 123
print(a)
b = np.array([1,2,3,4,5,6,7,8,9])
print(b[2])
print(b[[1,1,1,1,1,1,1]])
# print(b[[True,False,True,False,True]])
b = a.reshape(2,2)#привращаем одномерный массив в двухмерный.
