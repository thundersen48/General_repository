import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot()
"""
x = np.arange(-np.pi,np.pi,0.3)
ax.stem(x, np.cos(x),'--r', bottom=0.5)#командой bottom управляем линией уровня
"""




# x = np.arange(-2,2,0.1)
# y1 = np.array([-y**2 for y in x]) + 8
# y2 = np.array([-y**2 for y in x ]) +8
# y3 = np.array([-y**2 for y in x ]) +8
# ax.stackplot(x,y1,y2,y3)#отображение стековых графиков.
# # ax.step(x, x,'-ro',x, np.sin(x),'--x',where='pre')#Where pre график идет по горизонтали,post по вертикали, mid- точки будут распологаться по центру.



z = np.random.normal(0, 2, 500)
y = np.random.normal(0, 2, 500)
ax.scatter(z,y,s=50, c='g', linewidths=1, marker='s', edgecolors='r')
ax.grid()
plt.show()



















"""
stackplot() - графики отображаются друг над другом, и каждый следующий является суммой предыдущего и заданного набора данных
Stem-график выглядит как набор линий от точки с координатами (x, y) до базовой линии, в верхней точке ставится маркер:
plt.scatter(x,y)- Точечный график
"""