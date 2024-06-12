import numpy as np
import matplotlib.pyplot as plt

# Константы для радиоактивного распада
decay_constant = 0.05  # Константа распада
initial_count = 1000  # Исходное количество атомов
time = np.arange(0, 100, 1)  # Временные отсчеты

# Функция, моделирующая радиоактивный распад
def radioactive_decay(initial_count, decay_constant, time):
    return initial_count * np.exp(-decay_constant * time)

# Получение количества атомов после радиоактивного распада
count = radioactive_decay(initial_count, decay_constant, time)

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(time, count, label='Радиоактивный распад')
plt.xlabel('Время')
plt.ylabel('Количество атомов')
plt.title('Моделирование радиоактивного распада')
plt.legend()
plt.grid(True)
plt.show()