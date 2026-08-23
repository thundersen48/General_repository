#Ипмортирование нескольких классов из модуля.
"""
from car import Car, ElectricCar

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
"""
#Импортирование модуля целиком
import study.import_practice.car as car

#Обращаемя к нужным классам с помощью: имя_модуля.имя_класса 
#my_mustang = car.Car('ford', 'mustang', 2024)
#print(my_mustang.get_descriptive_name())

#my_leaf = car.ElectricCar('nissan', 'leaf', 2024)
#print(my_leaf.get_descriptive_name())

#Импортирование всех классов из модуля
#from car import *# - не рекомендуемый способ, поскольку возможны конфликты имен. Заместо него, если требуется импорти
#ровать все классы, лучше использовать синтаксис описанный выше имя_модуля.имя_класса.

from study.import_practice.electric_car import ElectricCar as EC
from study.import_practice.car import Car

ford = Car('ford', 'mustang', 2025)
print(ford.get_descriptive_name())
ford.read_odometer()
ford.update_odometer(15_000)
ford.read_odometer()

my_leaf = EC('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

import study.import_practice.electric_car as ec# Использование псевдонима.

my_leaf = ec.ElectricCar('nissan', 'leaf', 2024)