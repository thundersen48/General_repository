import numpy as np
import matplotlib.pyplot as plt

"""
сгенерируем вектор из 500 случайных величин и выведем их в виде гистограммы, используя функцию hist()
"""

"""
y = np.random.normal(0, 2, 500)#генерирует случайные значения из нормального (гауссовского) распределения
x = np.linspace(np.min(y),np.max(y),10)
bars = [len(y[np.bitwise_and(y >= x[i], y < x[i+1])]) for i in range(len(x)-1)]

"""
# x = [f'H{i+1}' for i in range(10)]
# y = np.random.randint(-20, 20, len(x))
# ax.bar(x, y, width=0.5, linewidth=2, edgecolor='r', yerr=2, bottom=10)

vals = [10, 40, 23, 30, 7]
vechicles = ['Toyota', 'BMW', 'Lexus', 'Audi', 'Lada']
explodes = [0.1, 0.05,0,0,0]#Разрыв диаграммы
plt.pie(vals, labels=vechicles, explode=explodes, autopct="%.2f%%",pctdistance=0.5,startangle=45)#pctdistance расстояние от центра доли до текстовой метки



# ax.hist(y,50)#формируем значения гистограммы по оси y
# x = [f'H{i+1}' for i in range(10)]
# y = np.random.randint(1, 5, len(x))
# ax.barh(range(len(x)-1), bars)#формирует график путем передачи значений y и x



plt.show()