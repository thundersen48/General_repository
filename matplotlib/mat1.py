import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

ws = [1,2,5]
hs = [2, 0.5]

fig = plt.figure(figure=(7,4))
gs = GridSpec(ncols=3, nrows=2, figure=fig)# 3 столбца и 2 строки

ax1 = plt.subplot(gs[0,0])#Создаем 1 координтную ось
ax1.plot(np.arrange(0, 5, 0.2))# Отображаем график
ax2 = fig
y = np.array([1,2, -6, 0, 4])# Добавляем новую ось
x = np.array([4,5,6,7,8])
plt.plot(x,y)
plt.show()# Показания окна