import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

fig = plt.figure(figsize=(7,4))
ax = fig.add_subplot()
x = np.arange(1,10)

I = np.array(Image.open('Информационные файлы/Gird.jpg'))
plt.plot(x)
b = ax.imshow(I,alpha=0.7,cmap= 'plasma')
fig.colorbar(b)#Отображение цветовой карты 

plt.show()