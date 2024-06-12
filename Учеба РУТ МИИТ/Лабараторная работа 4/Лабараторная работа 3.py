import numpy as np
import matplotlib.pyplot as plt


# axes create
x = np.arange(1,2,(0.05))
y = np.arange(1,2,(0.05))
def func(x,y):
    return (x+np.sin(y**2))/(abs(np.cos(x**2)+y**2))-(np.exp(x+y)*np.cos(2*x**3*y**2))/(x**2+abs(y**3))
#Координатная сетка
x,y = np.meshgrid(x,y)
z = func(x,y)

fig = plt.figure(figsize=(10,6))
ax_3d = fig.add_subplot(projection = '3d')

ax_3d.plot_surface(x,y,z,cmap='plasma')
ax_3d.minorticks_on()
ax_3d.grid(which='major',lw = 1)
ax_3d.grid(which='minor')
plt.show()