import matplotlib.pyplot as plt
import numpy as np
import scienceplots as sp
#Устинанавлиеваем стиль
plt.style.use(sp.styles_path['science'])
#Создание данных для графика
x = np.linspace(0, 2  *np.pi,100)
y = np.sin(x)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Пример графика')
plt.show()
