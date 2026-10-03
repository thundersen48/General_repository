import matplotlib.pyplot as plt
import numpy as np

delta = np.array([5.5, 7.2, 8.3, 10.5])
L = np.array([977, 746, 647, 512])

plt.figure(figsize=(6, 4))
plt.plot(delta, L, 'o-', color='black', linewidth=1.5, markersize=6)

plt.xlabel('Воздушный зазор δ, мм', fontsize=10)
plt.ylabel('Индуктивность, мГн', fontsize=10)

plt.xticks(delta)
plt.yticks(L)

plt.grid(True)
plt.show()