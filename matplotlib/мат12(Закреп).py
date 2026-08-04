import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(7,4))

ax_3d = fig.add_subplot(projection='3d')
x = np.arange(-2*np.pi,2*np.pi,0.2)
y = np.cos(x)
xgrid,ygrid = np.meshgrid(x,y)
zgrid = np.sin(xgrid)*np.cos(ygrid)/(xgrid)
ax_3d.plot_surface(xgrid,ygrid,zgrid)

plt.show()

