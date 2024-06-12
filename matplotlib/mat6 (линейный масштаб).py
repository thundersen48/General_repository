import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7,4))
ax = fig.add_subplot()

x = np.arange(-10*np.pi, 10*np.pi, 0.1)
ax.plot(x, np.sinc(x)* np.exp( -np.abs(x/10)))
ax.set_xscale('symlog', linthresh=2)
# ax.set_yscale('symlog', base = 10, subs =[2,5])
ax.grid()

plt.show()