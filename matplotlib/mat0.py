import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

ws = [1,2,5]
hs = [2, 0.5]
x = np.arange(-2*np.pi,2*np.pi,0.1)
y = np.cos(x)

# plt.fill_between(x,y,0.5) #Выполняем заливку графика
plt.plot(x,y,'--',color='r')
plt.gird()
plt.show()

fig = plt.figure(figsize=(7,4))
gs = GridSpec(ncols=3, nrows=2, figure=fig)
plt.show()