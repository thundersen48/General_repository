import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullLocator,LinearLocator, MultipleLocator,IndexLocator,FixedLocator,LogLocator,MaxNLocator

fig = plt.figure(figsize=(7,4))
ax = fig.add_subplot()

x = np.arange(-np.pi/2,np.pi,0.1)
ax.plot(x,np.sin(x))

ax.grid()
# ax.xaxis.set_major_locator(LogLocator(base=2))# Откладывание элементов по оси x в стиле логарифма в степени i
ax.xaxis.set_major_locator(MaxNLocator(5))#Указывает максимальное число рисок
#-----------------------------
ax.minorticks_on()
ax.grid(which='major',lw = 2)#Указываем мажорную сетку с линией толщиной 2 пикселя, а minor на 1 пиксель.
ax.grid(which='minor')
#-----------------------------

plt.show()