import matplotlib.pyplot as plt
import numpy as np
"""
nrows, ncols - Число строк и столбцов; index - индекс текущих координат.
"""
ax1 = plt.subplot(2,3,1)
plt.plot(np.random.random(10))
ax2 = plt.subplot(2, 3, 2)# С помощью данной функции можно нарисовать несколько графиков
plt.plot(np.random.random(10))
ax3 = plt.subplot(2, 3, 3 )
plt.plot(np.random.random(10))
ax4 = plt.subplot(2,1,2)
plt.plot(np.random.random(10))
ax1.grid()#Наложение сетки, она применяется к последней координатной оси.
# ax2.grid()
ax3.grid()

plt.show()

