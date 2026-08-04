l1 = ['a']
l2 = ['b']
'l1'.__add__('с') # l1 = l1+c

#print(l1+l2)
class Person:
    age = 1
    def __add__(self, value):# Переопределяем свойство add
        self.age += 1
        return self.age

p = Person()
#print(p + 'Hello')
# Применили метод полиморфизма(Перезагрузка), задействуем два аргумента!
class base:
    def __init__(self,a):
        self._a = a #Создание приватного атрибута

    def print_a(self, square = False,multiplier = None):
        if square and not multiplier: # Если квадрат, но не множитель
            print(self._a ** 2)
        elif not square and multiplier: # Если не квадрат, но множитель
            print(square._a *multiplier)
        elif square and multiplier: #Если квадрат и множитель
            print((self._a**2) * multiplier)
        else:
            print(self._a)

base = base(4)
base.print_a(square=True, multiplier= 2)

# Переопределение

class Multiplier:
    def __init__(self,a):
        self._a = a

    def print_a(self,x):
        print(self._a * x)

M = Multiplier(5)
M.print_a(2)
class Exponent(Multiplier):
    def print_a(self,x): #Одинаковые функции выполняют разное значение
        print(self._a ** x)

e = Exponent(4)
e.print_a(2)
"""
Полиморфизм - способен преопределять подкласс методом своего суперкласса с помощью собственной реализации
"""