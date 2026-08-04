from matplotlib import pyplot as plt
import numpy as np

a = np.array([10,20,30,40,50,60])
np.histogram(a,bins = [0,20,40,60,80,100])
hist,bins = np.histogram(a,bins = [0,20,40,60,80,100])
print (hist)
print (bins)
plt.hist(a, bins = [0,20,40,60,80,100])
plt.title("histogram")
plt.show()
