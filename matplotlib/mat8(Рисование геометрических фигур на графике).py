import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import *# Импортируем все классыл ломанных линий.

l1 = Line2D([1,2,3],[1,2,4])# Объект ломаной создается путем передачи списка координат по x и y конструктору этого класса
rect = Rectangle((0, 0), 2.5, 0.5, facecolor='g')#в начале указываем координаты расположения прямоугольника, а затем, его ширину и высоту
fig = plt.figure(figsize=(7,4))
ax = fig.add_subplot()

line1, = ax.plot(np.arange(0, 5, 0.25), '--o',label='line 1')
line2, = ax.plot(np.arange(0, 10, 0.5),':s', label ='line 2')


ax.add_line(l1)
ax.add_patch(rect)#отобразить этот прямоугольник в координатных осях, нужно взывать метод
# ax.set(xlim=(1, 3), ylim=(1, 3))# Указываем ограничения по оис x и y, при этом без зависимости от графика
plt.show()
"""
Arc Для рисования дуг

Arrow Для рисования стрелок (см. также ConnectionPatch, FancyArrowPatch и FancyArrow в этом же модуле)

Circle Для рисования окружностей

CirclePolygon Для рисования равносторонних многоугольников

Ellipse Для рисования эллипсов

FancyBboxPatch Для рисования прямоугольников с разными типами границ (с закругленными углами, в виде стрелок, с зубчатыми ребрами и т.п.)

PathPatch Для рисования линий или замкнутых областей

Polygon Для рисования многоугольников

Rectangle Для рисования прямоугольников

Wedge Для рисования «клина» (сектора окружности)
"""