import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter,NullLocator,LinearLocator, MultipleLocator,IndexLocator,FixedLocator,LogLocator,MaxNLocator,FormatStrFormatter, FuncFormatter,AutoLocator
import matplotlib.ticker as ticker
from matplotlib.axis import Axis
from matplotlib import ticker


fig = plt.figure(figsize=(12,6))

ax1 = plt.subplot(2,3,1)
ax1.set_title('Синус')
x = np.arange(-np.pi, np.pi/2,0.1)
x = np.linspace(0,5)
ax1.yaxis.set_major_formatter(FormatStrFormatter('#%s'))
plt.plot(x,np.sin(x), label='line1')
# ax2 = fig.add_subplot()

# ax2.plot(y)
ax2 = plt.subplot(2,3,2)
ax2.set_title('Прямая')
ax2.xaxis.set_major_formatter(ticker.PercentFormatter(xmax=10))
ax2.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=10))
y = np.array([1,2,3,4,5,6,7,8,9,10])
x = np.arange(0, 3*np.pi, 0.1)
plt.rcParams['ytick.right'] = plt.rcParams['ytick.labelright'] = True
plt.rcParams['ytick.left'] = plt.rcParams['ytick.labelleft'] = False
ax2.xaxis.set_major_locator(MaxNLocator(5))
# ax2.set_yscale('log',base=2)

plt.plot(y,label='line2') #Нарисовать точки y



ax3 = plt.subplot(2,3,3)
ax3.set_title('Экспонента')
t = np.arange(0.0, 100.0, 0.1)
s = np.sin(0.1 * np.pi * t) * np.exp(-t * 0.01)
ax3.yaxis.set_major_formatter(FormatStrFormatter('%s'))
plt.rcParams['lines.linewidth'] = 3
plt.text(0,-0.8,'рис.3')

plt.xlim([0,100])#Указываем диапазон ограничения
plt.plot(t, s, label='line3')

ax4 = plt.subplot(2,1,2)
p = np.arange(0, 10, 0.1)
h = np.sin(p)
r = np.cos(p)
plt.plot(h,color='blue', label='Sine wave')
plt.plot(r, color='black', label='Cosine wave')

ax3.xaxis.set_major_locator(MultipleLocator(20))
ax3.xaxis.set_major_formatter('{x:.0f}')
ax3.xaxis.set_minor_locator(MultipleLocator(5))#Указывает максимальное число рисок

fig.set_facecolor('#eee')

ax1.minorticks_on()
ax1.grid(which='major',lw = 2)
ax1.grid(which='minor')


ax2.minorticks_on()
ax2.grid(which='major',lw=1.5)
ax2.grid(which='minor',lw=0.5)

ax3.minorticks_on()
ax3.grid(which='major',lw=1)
ax3.grid(which='minor',lw=0.5)

ax4.minorticks_on()
ax4.grid(which='major',lw=2)
ax4.grid(which='minor',lw=1.5)

ax1.legend(loc='lower left',)
ax2.legend(loc='lower right')
ax3.legend(loc='lower right')
ax4.legend()
plt.show()

