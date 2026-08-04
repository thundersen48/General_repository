import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter, FormatStrFormatter, FuncFormatter, ScalarFormatter, FixedFormatter

"""
Форматы меток координатных осей
Set_xticklabels()
Set_yticklabels()#С помощью этих команд можно отключать о меток графиках
FormatStrFormatter - Устанавливает формат числовых данных, подписей для рисок   
NullFormatter - Отключает вывод подписей у рисок
FuncFormatter - Вызывает функцию для формирования числовых значений. 
ScalarFormatter - Отображает числовые данные, с небольшими манипуляциями
fixedFormator - каждой риске оси присваивает строго определенные значения.
"""
def formatOy(x, pos):
    return f'[{x}]' if x<0 else f'({x})'
fig = plt.figure(figsize=(7,4))
ax = fig.add_subplot()
x = np.arange(-np.pi/2, np.pi, 0.1)
ax.plot(x, np.sin(x) * 1e5)

sf = ScalarFormatter()
sf.set_powerlimits((-6, 6))
ax.yaxis.set_major_formatter(sf)
# ax.plot(x, np.sin(x))

# ax.yaxis.set_major_formatter(sf)#Пропадают значения по оси y
# ax.yaxis.set_major_formatter(FormatStrFormatter("y = %.2f"))#Происходит округление дробных чисел до целого%d, вещественные чила%f
# ax.yaxis.set_major_formatter(FuncFormatter(formatOy))
"""
ax.set_xticklabels([1,-1])#Скрывает значения по оси x и y
ax.set_yticklabels([])
"""

ax.grid()
plt.show()
