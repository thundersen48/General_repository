import numpy as np
from sklearn import preprocessing

input_data = np.array([ [5.1, -2.9, 3.3],
[-1.2, 7.8, -6.1],
[3.9, 0.4, 2.1],
[7.3, -9.9, -4.5]])
#Вывыодим среднее значение и стандартное отклонение
print ("\nBEFORE:")
print("Mean =", input_data.mean(axis=0))# Среднее значение
print("Std deviation =", input_data.std(axis=0))# Стандартное отклонение

#Исключение среднего
data_scaled = preprocessing.scale(input_data)
print ( "\nAFTER: ")
print("Mean =", data_scaled.mean(axis=0))
print("Std deviation =", data_scaled.std(axis=0))
#среднее значение практически равно О, а стандартное отклонение - 1.