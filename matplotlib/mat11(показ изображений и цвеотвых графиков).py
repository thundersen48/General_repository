import numpy as np
import matplotlib.pyplot as plt

from PIL import Image

img = np.array(Image.open('Информационные файлы/1598.jpg'))
data = np.random.randint(0,255,(100,100))#Случайные целые числа от 0 до 255 размерностью 100 на 100

plt.imshow(data, cmap='plasma')
# fig = plt.figure(figsize=(7,4))
# ax = fig.add_subplot()
# ax.imshow(img)# Отображаем подготовленное изображение



plt.show()