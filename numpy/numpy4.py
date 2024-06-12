import numpy as np
# def getRange(a):
#     for i in range(a):
        # yield i #Yield это ключевое слово, которое используется примерно как return — отличие в том, что функция вернёт генератор.
# a = np.fromiter(getRange(4),dtype='int8')# Формирование Массива на основе функции
# print(a)


# a = np.array([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9])
# # a.dtype = np.int8() # Число элементов увеличелось в 8 раз, int8 преобразование в однобайтное представление целого числа
# a.dtype = 'float32'
# print(a)
# print(a.size)
# print(a.itemsize) # Сколько байт занимает 1 элемент в массиве
# print(a.size*a.itemsize)
# b = np.ones((3,4,5))

# print(b.ndim) # узнаем кол-во осей
# print(b.shape) # Узнаем кол-во элементов по каждой оси
# b.shape = 60# Преобразуем в одномерный массив, который содержит 60 едениц
# print(b)
# b.shape = 12,5

# c = b.reshape(3,2,10)
# print(c)
"""
С помощью shape меняется текущее представление массива, а не создается новый массив
"""
# b[0,0] = 10
# print(b)
# c = b.view()

a = np.array([1,2,3,4,5,6,7,8,9])
#
# b = a.view()# здесь мы создаем копию представления массива
# a.shape = 3,3
# print(a)
b = np.array(a)# здесь мы создаем копию массива

a[0] = 100
print(b)
c = a.copy()
print(c)