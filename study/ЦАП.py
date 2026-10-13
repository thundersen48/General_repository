import matplotlib.pyplot as plt

# Экспериментальные данные
N = [0, 16, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 192, 208, 224, 240, 255]
U = [0.000, 0.313, 0.625, 0.938, 1.250, 1.563, 1.875, 2.188,
     2.500, 2.813, 3.125, 3.438, 3.750, 4.063, 4.375, 4.688, 4.980]

# Создание графика
plt.figure(figsize=(10, 6))

# Ступенчатый график: значение U держится до следующего N (where='post')
plt.step(N, U, where='post', linewidth=2, color='blue')

# Экспериментальные точки поверх ступенек
plt.plot(N, U, 'o', color='blue', markersize=6)

# Добавляем подписи значений напряжения над каждой точкой
for i in range(len(N)):
    plt.text(N[i], U[i] + 0.1, f'{U[i]:.3f}', ha='center', fontsize=9)

# Подписи осей
plt.xlabel('Десятичный код N', fontsize=12)
plt.ylabel('Выходное напряжение Uвых, В', fontsize=12)
#plt.title('Ступенчатая характеристика ЦАП (8 разрядов, Vref = 5 В)', fontsize=14)

# Масштабы и сетка
plt.xlim(0, 260)
plt.xticks(range(0, 273, 16))  # метки через 16
plt.ylim(0, 5.2)
plt.yticks([i/10 for i in range(0, 55, 5)])  # метки через 0.5 В
plt.grid(True, linestyle='--', alpha=0.7)

plt.legend()
plt.tight_layout()
plt.show()