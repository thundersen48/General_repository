#Объеденение и разделение массивов
import numpy as np
"""
np.hstack([a,b])- Объединяет массивы по горизонтали
np.vstack([a,b])- Объединяет массивы по вертикали
np.column_stack([a,b])- Объеденение столбцов
np.row_stack([a,b])- Объединяем два верктора по вертикали
"""
# a = np.array([(1,2),(3,4)])
# b = np.array([(5,6),(7,8)])
# c = np.vstack([a,b,b,a])
# print(c)

# a = np.fromiter(range(18), dtype='int32')
# b = np.fromiter(range(18,36),dtype='int32')#int32	Целое число (от -2147483648 до 2147483647)
# a.resize(3,3,2)
# b.resize(3,3,2)
# print(a)
# a = np.fromstring('1 2 3 4',sep = ' ')
# b = np.fromstring('5 6 7 8',sep = ' ')
# c = np.vstack([a,b])
# print(c)
# c = np.column_stack([a,b]) # Объеденение столбцов по вертикали, последовательно
# print(c)
# a = np.arange(1,13)
# b = np.arange(13,26)
# a.resize(3,3,2)
# b.resize(3,3,2)
"""
np.concatenate([])- объеденение массивов a и b вдоль задаваемых осей
"""
# c0 = np.concatenate([a,b],axis=0)#Размерность 6x3x2
# c1 = np.concatenate([a,b], axis=1)#Размерность 3x6x2
# c2 = np.concatenate([a,b],axis=2)#Размерность 3x3x4
# print(c1.shape)
"""
Объекты r_ и c_
r_ - Создает копию массива 
c_ - Работает анологично, только он делает объеденинение по второй оси axis-1
"""
# a = np.r_[[1,2,3],4,5]
# b = np.r_[1:9,90,100]
# print(a)
# print(b)
# a = np.r_[np.array([1,2,3]), np.array([4,5,6])]# объеденение Одномерных массивов по строке
# print(a)
# b = np.r_[[(1,2,3), (4,5,6)],[(7,8,9)]] #Объеденение двухмерных массивов
# print(b)
# x = np.c_[1:5]
# print(x)
# a = np.c_[[1,2,3],[4,5,6]]
# print(a)
# b = np.c_[ [(1,2,3),(4,5,6)],[[7],[8]] ]#Двухмерная матрица и вектор столбец
# print(b)
"""
Разделение массивов
hsplit- делает разделение по горизонтали
vsplit-
np.array_split- Разбивает оси
"""
# a = np.arange(10)
# #
# # b = np.hsplit(a,5)
# # print(b)
# a.shape = 10, -1
# print(a)
a= np.arange(18)
a.resize(3,3,2)
b = (a,2,axis = 0)
print(b)