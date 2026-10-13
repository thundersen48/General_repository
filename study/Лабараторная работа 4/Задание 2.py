import numpy as np
import matplotlib.pyplot as plt
import math as m

t0 = 1
tn = 10
th = 100
s = 0.4

t = np.linspace(t0,th,tn)
v = 31.6/t**0.25*s**0.66


while s > 0.25:
    plt.plot(v,t)
    plt.title('Зависимость скорости резания при точении от подачи')
    plt.xlabel('Подача мм/об')
    plt.ylabel('Скорость резания при точении, м/мин')
    plt.grid()
    plt.show()
else:
    print('Значение s должно быть больше 0.25')

print(t)