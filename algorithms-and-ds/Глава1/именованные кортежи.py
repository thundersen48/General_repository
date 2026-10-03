#позволяют задавать конкретные атрибуты для каждого элемента, что делает код более понятным и удобным для чтения.
# Они часто используются для представления простых структур данных, таких как записи в базе данных, результаты измерений
from collections import namedtuple




Person = namedtuple('Person', ['name', 'age', 'gender'])

person1 = Person(name='Максим', age=18, gender='Мужской')
#print(Person.name)

car = namedtuple(
    'car',[
        'color',
        'mileage'
    ]
)

my_car = car('red', 300)
#print(my_car.color)

'Наследование от именованных кортежей'

car = namedtuple('car','color mileage')

class MyCarWithMethods(car):
    def hexcolor(self):
        if self.color == 'red':
            return '#ff0000'
        else:
            return '#000000'
a = MyCarWithMethods('red',1234)
#print(a.color)

food = namedtuple('vegetables','Fastfood')

"""Чтобы создать иеррархию именнованных кортежей"""

car  = namedtuple('Car', 'color mileage')
ElectricalCar = namedtuple(
    'Electricalcar',car._fields +('charge',))

ElectricalCar('red', 1234, 45.0)
#print(ElectricalCar.__dict__)
"""Вспомогательные методы именованного кортежа"""

print(my_car._asdict()) # Возвращает содержимое именнованного кортежа в виде словаря

"""_replace() - позволяет создать именнованный кортеж, который будет удобен для перезаписи данных"""
s = Stock('ACME', 100, 123.45)
s = s._replace(shares = 75)
print(s)