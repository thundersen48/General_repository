import numpy as np
a = np.array([1.0,5.55, 123, 0.567, 25.532])

print ('Original array:')
print (a)


print ('After rounding:')
print (np.around(a))
print (np.around(a, decimals = 1))
print (np.around(a, decimals = -1))
"""
numpy.around ()
Это функция, которая возвращает значение, округленное до желаемой точности. Функция принимает следующие параметры.
"""
"""
array(object, …) Преобразует список или кортеж object в массив NumPy.

asanyarray(list, …) Преобразует список list в массив array, сохраняя тип подкласса.

ascontiguousarray(list, …) Возвращает непрерывный массив в памяти, подобно как это организовано в языке C.

asmatrix(list, …) Преобразует входную последовательность list в матрицу NumPy (тип matrix).

copy(list, …) Возвращает копию массива list (если это объект NumPy) или просто создает массив на основе списка языка Python.

frombuffer(buffer, …) Преобразует данные из буфера в массив NumPy

fromfile(file, …) Возвращает массив из данных текстового или бинарного файла file.

fromfunction(func, shape, …) Создает массивразмерностью shape с помощью функции func.

fromiter(iter, …) Создает массив на основе итерируемого объекта.

fromstring(string, …) Создает массив из данных строки.

loadtxt(file, …) Формирует массив из данных текстового файла.
"""