import  matplotlib.pyplot as plt
import numpy as np



x = np.arange(-np.pi/2, np.pi, 0.1)
y1 = 4*x
x2 = np.sin(x) * 1e5
y2 = 4*x2

plt.subplot(1, 2, 1)

plt.plot(x,y1 )
plt.grid()
plt.subplot(1, 2, 2)
plt.plot(x2,y2)
plt.grid()

plt.show()