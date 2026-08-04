import numpy as np
import matplotlib.pyplot as plt

# Размеры области
x_min, x_max = -10, 10
y_min, y_max = -10, 10

# Сетка координат
x = np.linspace(x_min, x_max, 400)
y = np.linspace(y_min, y_max, 400)
X, Y = np.meshgrid(x, y)

# Координаты электродов и их потенциалы
electrodes = [
    {"coord": (-5, -5), "potential": 3},
    {"coord": (5, -5), "potential": 5},
    {"coord": (-5, 5), "potential": 7},
    {"coord": (5, 5), "potential": 6},
    {"coord": (0, 0), "potential": 8},
]

# Вычисление потенциалов в точках сетки
Z = np.zeros_like(X)
for electrode in electrodes:
    ex, ey = electrode["coord"]
    ep = electrode["potential"]
    Z += ep / np.sqrt((X - ex) ** 2 + (Y - ey) ** 2)

# Построение эквипотенциальных линий
plt.figure(figsize=(8, 8))
contour = plt.contour(X, Y, Z, levels=[3, 5, 6, 7, 8], colors=['blue', 'green', 'red', 'purple', 'orange'])

# Добавление координат электродов
for electrode in electrodes:
    ex, ey = electrode["coord"]
    plt.plot(ex, ey, 'o', label=f"({ex}, {ey}), φ = {electrode['potential']}V")

# Настройки графика
plt.xlabel('X координата')
plt.ylabel('Y координата')
plt.title('Эквипотенциальные линии электрического поля')
plt.legend()
plt.colorbar(contour, label='Потенциал (В)')
plt.grid(True)
plt.show()
