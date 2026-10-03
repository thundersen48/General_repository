import os
import cv2# Компьютерный анализ(Загрузка и обработка изображений)
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf # Машинное обучение

mnist = tf.keras.dataset.mnist
"""Разделяем данные обучение на данные тестирование"""
(x_train, y_train),(x_test, y_test) = mnist.load_data()# x - это пиксельное изображение; y - классификация
"""Pixel normalization"""
x_train = tf.keras.utils.normalize(x_train, axis = 1)
x_test = tf.keras.utils.normalize(x_test, axis = 1)

"""Нейронная сеть"""
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape = (28,28)))# Сглаживание
model.add(tf.Keras.layers.Dendse(128,activation = 'relu'))
model.add(tf.Keras.layers.Dendse(128,activation = 'relu'))
model.add(tf.Keras.layers.Dendse(10,activation = 'softmax'))# 10 Нейронов складываются воедино

model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])

model.fit(x_train, y_train, epochs = 3)

image_number = 1
while os.path.isfile(f"digits/digit{image_number}.png"):
    try:
        img = cv2.imread(f"digit/digits{image_number}.png")[:,:,0]
        img = np.invert(np.array([img]))
        prediction = model.prediction(img)
        print(f'Это {np.argmax(prediction)}')
        plt.imshow(img[0], cmap=plt.cm.binary)
        plt.show()
    except:
        print('Ошибка!')
    finally:
        image_number += 1

model.save('hand.model')

