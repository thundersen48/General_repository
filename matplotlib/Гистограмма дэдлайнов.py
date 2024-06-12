import numpy as np
import matplotlib.pyplot as plt


#Создаем генератор случайных чисел с использованием алгоритма PCG64
rg = np.random.Generator(np.random.PCG64(5))
x1 = np.linspace(1, 5)
x2 = np.linspace(0, 7, 1)

# Строим основную гистограмму, с диапазоном 0 до 10 столбыцы будут накладываться друг на друга
plt.hist([x1, x2], bins=15, range=(0, 10), stacked=True)
plt.minorticks_on()
plt.xlim((0, 60))
plt.grid(which='major')
plt.grid(which='minor', linestyle=':')

# Строим вторую гистограмму в отдельных осях
plt.axes([.5, .5, .4, .4])
plt.hist([x1, x2], bins=100, stacked=True, range=(9, 11))
plt.grid(which='major')

plt.tight_layout()

# сохраняем диаграмму в файл
plt.savefig('histograms.png')
plt.show()
