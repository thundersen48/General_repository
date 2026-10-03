import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense

# Загрузка и предобработка данных MNIST
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# Создание модели нейронной сети
model = Sequential([
    Flatten(input_shape=(28, 28)),  # Преобразование двумерного изображения в одномерный массив
    Dense(128, activation='relu'),  # Полносвязный слой с 128 нейронами и функцией активации ReLU
    Dense(10, activation='softmax')  # Выходной слой с 10 нейронами (по числу классов) и функцией активации Softmax
])

# Компиляция модели
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Обучение модели
model.fit(x_train, y_train, epochs=5)

# Оценка точности на тестовом наборе
test_loss, test_acc = model.evaluate(x_test, y_test)

print(f'Точность на тестовом наборе данных: {test_acc}')
