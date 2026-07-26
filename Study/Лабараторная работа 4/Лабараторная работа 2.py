import numpy as np
import matplotlib.pyplot as plt

# Определяем отрезок и значения функции на этом отрезке
x = np.linspace(2, 3, 100)  # задаем значения x на отрезке от 2 до 3
y = x**2 - np.log(1+x) - 3  # вычисляем значения функции x^2 - log(1+x) - 3

# Строим график
plt.plot(x, y, label='x^2 - log(1+x) - 3')
plt.axhline(y=0, color='k', linestyle='--')  # добавляем горизонтальную линию y=0
plt.xlabel('Скорость резки при точении от подачи')
plt.ylabel('Скорость резки')
plt.title('График уравнения x^2 - log(1+x) - 3 = 0')
plt.grid()
plt.legend()
plt.show()