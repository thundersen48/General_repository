import numpy as np
"""
a = np.array([1,2,3,4,4,3,2,1])
setA = np.unique(a)# Массив состоит из уникальных элементов
print(setA)
b = np.unique(a, return_counts=True)0#Возвращает  уникальные элементы и их число повторений
print(b)
c = np.unique(a, return_index=True)# Возвращает массив уникальных вхождений и их индексы уникальных значений.
print(c)
setA, indx = np.unique(a, return_inverse=True)# Возвращает индексы по которым можно восстановить исходный массив.
"""
# print(setA)
# print(indx)
# print(setA[indx]) # Восстанавливаем массив A

# x = np.array([[0,1,1,2],[0,1,1,2],[9,1,1,2]])
# print(np.unique(x,axis=1))
x = np.array([0,1,2,3])
y = np.array([1,2,3,4,5,6,7,8])
"""
print(np.in1d(x,y))# Данная функция показывает какие вхождения в массиве x существуют в y.
"""
np.random.shuffle(y)
# print(y)
"""
Порядок значения не имеет ничего общего с функцией np.in1d
имеет значение только их уникальность.
"""
"""
print(np.intersect1d(x,y))# Увидим пересечение элементов, 123 потомучто как 123 входит в 1 массив, так и во второй.
"""
print(np.union1d(x,y))# Объеденение массивов, добавляется элемент 0, который не существует в x
"""
Вычитание массивов происходит с помощью фунцкии np.setdiffi1d(a,b)
"""
print(np.setdiff1d(y,x))
"""
np.setxorld - симметричная разность 
"""
# print(np.setxor1d(x,y))
a = np.array([1,2,3,10,20,30])
b = np.array([2])
print(a*b)

