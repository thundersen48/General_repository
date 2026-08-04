import random

import numpy as np

#заданные значения
p0 = 1
v0 = 2
a = 10
#Список для хранения значений
data = []


#Расчет

for _ in range(10):
    t = np.random.randint(0,10)
    p = p0 + v0 * t + a * t ** 2 / 2
    data.append(p)

print(f'Массивы данных: \n{data}')

#Определение ко-во четных и нечетных элементов
even = sum(1 for x in data if x % 2 == 0)
odd = sum(1 for x in data if x % 2 != 0)

print(f"Количество четных элементов: {even}")
print(f"Количество нечетных элементов: {odd}")
