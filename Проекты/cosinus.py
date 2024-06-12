import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return np.cos(1-x)/2
diap = np.linspace(10, 50, 500)  # 51 точка между 0 и 3
y = f(diap)
plt.plot(diap, y)
plt.show()
