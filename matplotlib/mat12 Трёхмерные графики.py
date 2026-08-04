import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(7,4))
# ax_3d = Axes3D(fig)#Создаем ось класса axes 3D
ax_3d = fig.add_subplot(projection='3d')#Создаем новую ось и с помощью porjection указываем что ось трёхмерная

x = np.arange(-2*np.pi,2*np.pi,0.2)
y = np.arange(-2*np.pi,2*np.pi,0.2)
xgrid,ygrid = np.meshgrid(x,y)#meshrid()- формирует сетку на основе данных.

zgrid = np.sin(xgrid) * np.sin(ygrid) / (xgrid*ygrid)
ax_3d.plot_surface(xgrid,ygrid,zgrid,rstride=5,cstride=5,cmap='plasma')
"""
rstride,cstride - Велечина шага с которым будут выбираться элементы из массивов x и y
"""
ax_3d.set_xlabel('x')
ax_3d.set_ylabel('y')
ax_3d.set_zlabel('z')

plt.show()