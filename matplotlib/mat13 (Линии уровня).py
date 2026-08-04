import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1,2)

x = np.arange(-2 * np.pi, 2 * np.pi, 0.2)
y = np.arange(-2 * np.pi, 2 * np.pi, 0.2)
xgrid, ygrid = np.meshgrid(x, y)

zgrid = np.sin(xgrid) * np.sin(ygrid) / (xgrid * ygrid)

ax[0].contour(xgrid, ygrid, zgrid)
ax[1].contourf(xgrid, ygrid, zgrid)
plt.show()