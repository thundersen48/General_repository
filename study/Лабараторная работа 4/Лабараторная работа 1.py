import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(2,3)
y = x**2 - np.log(1+x) - 3
plt.plot(x, y, label='y = x**2 - ln(1+x) - 3 ')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(y=0, color='k', linestyle='--')
plt.title('График функции y = x**2 - ln(1+x) - 3 ')
plt.grid()
plt.legend()
plt.show()
