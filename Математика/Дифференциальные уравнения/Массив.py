import numpy as np

a = np.array([[1,2,3,4],
             [5,6,7,8]])

x_test = np.arange(32).reshape(8, 2, 2) # массив 8x2x2

#c = a.ravel()
#a.resize(2*4)
np.expand_dims(a,axis=2)
x_test4 = np.expand_dims(x_test, axis=0)
c = np.squeeze(x_test4, axis=0)
#np.squeeze(a,axis=0)
#print(c)
#print(a)
print(a)

print(x_test4)