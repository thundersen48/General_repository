import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7,4))#Создаем фигуру
# ax1 = fig.add_axes([0.0,0, 1.0, 1.0])#Создаем новые оси и указываем расположение координатных осей
ax1 = fig.add_subplot(1,3,1)
ax1.plot(np.arange(0, 5, 0.2))
# plt.plot(np.arange(0,5,0.2))
"""
f - Фигура
ax - Ось
"""
f, ax = plt.subplots(2,2)

f.set_size_inches(7,4) # Прописываем размер 7x4

f.set_facecolor('#eee')# Прописываем цвет фона (Светлосерый)
ax[0, 0].plot(np.arange(0,5,0.2))# Создаем график от 0 до 5 с шагом 0,2
ax[0,0].grid()
ax[0,1].plot(np.arange(5,0, -0.2))# Создаем вторую координатную ось
ax[0,1].grid()
plt.show()
