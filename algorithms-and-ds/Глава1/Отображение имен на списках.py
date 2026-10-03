#У вас есть код, который осуществляет доступ к элементам в списке или кортеже по
# позиции. Однако такой подход часто делает программу нечитабельной. Также вы
# можете захотеть уменьшить зависимость от позиции в структуре данных путем
# перехода к принципу доступа к элементам по имени.
"""Colection.namedtuple()"""
from collections import namedtuple

subscriber = namedtuple('Subscriper', ['addr', 'joined'])
sub = subscriber('jonesy@example.com', '2012-10-19')
print(sub)
print(sub.addr)
#Пример кода использующий обычные кортежи

def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total

# Пример кода, использующий именнованные кортежи

Stock = namedtuple('Stock', ['name', 'shares', 'price'])

def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total

