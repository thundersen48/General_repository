import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullLocator,LinearLocator,MultipleLocator

fig = plt.figure(figsize=(7,4))
ax = fig.add_subplot()
ax.plot(np.arange(1, 5, 0.25))
"""
ax.set(xlim=(-5, 30),ylim=(-1, 6))#Определяем границы по осям x и y.
"""
ax.set_xlim(xmin=-5, xmax=10)# Определяем границу по оси x
ax.set_ylim(ymin=-1, ymax= 10)# Определяем границу по оси y

plt.xlim(-2,30)
plt.ylim(-1,10)

# lc = NullLocator()

ax.grid()
ax.xaxis.set_major_locator(MultipleLocator(base=3.5))#Создамем 5 отметок по оси x

plt.show()
"""
set_major_locator() - Управление рисками крупной сетки.(которая внизу графика)
set_minor_locator()- Управление рисками мелкой сетки.
LinearLocator - Создание меток, по выбранной оси графика
MultipleLocator - задает шаг размеров между рисками(base *i, где i = +-1,+-2,...)
IndexLocator(base*i) base - шаг изменения между соседними рисками, offset- смещение относительно наименьшего значения 
FixedLocator - указывает метки в указанных значениях.
LogLocator - Формирует логарифмические деления по осям
MaxNLocator - Производит разбивку на указанное число рисок 
"""
