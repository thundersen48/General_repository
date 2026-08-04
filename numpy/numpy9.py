import numpy as np
# a = np.array([1, 2, 3, 10, 20, 30])
# c = a[a > 5]
# print(c)
# b = np.array([1, 2, 3, 4, 5, 6])
# print(a == b)
"""
greater(a, b) – выполняет сравнение a > b;
less(a, b) – выполняет сравнение a < b;
equal(a, b) – выполняет сравнение a == b.
"""
# c = np.greater(a,b)
# print(c)
# d = np.less(a,b)#a<b
# print(d)
# f = np.equal(a,b) #a == b
"""
На выходе получим булев массив,
который не подается власти интерпретатору.
"""
# print(f)
# if np.array_equal(a, b):
#     print('a == b')
#
# d = np.any(a > 5)# хотябы один элемент должен быть равен больше 5
# print(d)
# h = np.all(a>0)
# print(h)
# b = np.array([1, 2, np.nan,np.inf,-np.inf])
# # c = b*0
# # c.sum()
# c = np.isinf(b)# возвращает булев тип и показывает нам, где стоит inf
# print(c)
# z = np.isnan(b)# Возвращает булев тип, где стоит функция none
# print(z)
# indx = np.isinf(b)
# print(indx)
# r = b[~indx]#Инвертируем показания и отбрасываем все значения inf
# print(r)
# a = np.isfinite(b)
"""
Функция isinf помогает определить являются ли значения конечными элементами.
"""
# print(a)
a = np.array([1+2j, 3-4j,5])