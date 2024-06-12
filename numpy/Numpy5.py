import numpy as np
# a = np.arange(10)
# a.shape = 2,5
#
# b = a.reshape(10)
# b[0] = -1
#
# a.shape = -1,2
#
# b.reshape(1,-1)
# print(b)
# с = a.ravel()# Представление двухмерного массива в одномерный
# # print(с)
# a.shape = -1# Чтобы изменить сам массив
#
# a.resize(3,2, refcheck = False)# Данный метод меняет представление текущего массива
# f = a.T #Операция транспорнирования создает новый массив
# print(f)
x = np.arange(1,10)
x.shape= 1, -1 # Создаем новую ось массива(ось 1 и ось 2)
# print(x.T)
"""
Добавление и удаление осей 
np.exand_dims(a,axis)
np.squeeze(a[,axis])- удаление оси, без удаления элементов
"""
x_test = np.arange(32).reshape(8,2,2)
x_test4 = np.expand_dims(x_test, axis=0) #Создаем новую ось, меняя при этом представление массива
# print(x_test4.shape)
x_test4[0,0,0,0] = -100
# print(x_test)

# print(x_test4.shape)
a = np.append(x_test4, x_test4, axis=0)#Функция добавляет новый элемент, но при условии, что массив должен быть четырёхмерным
# print(a.shape)
b = np.delete(a,0, axis=0)

b = np.expand_dims(x_test4, axis=-1)
"""
 -1 будет добавляться последняя ось.
 -2 будет добавляться предпоследняя ось
"""
# print(b.shape)
c = np.squeeze(b)
# print(c.shape)
f = b[:, np.newaxis]
print(b.shape)
"""
Чтобы увидеть массив одномерным, можно воспользоваться функцией ravel:
"""