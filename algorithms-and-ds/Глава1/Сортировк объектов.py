from operator import attrgetter
from operator import itemgetter
from itertools import groupby
from collections import defaultdict

"""Задача: я хочу сортировать объекты одного класса, но они не поддерживают операцию сравнения"""
# В это мне поможет функция sorted()
# Которая принимает аргумент key
class User:
    def __init__(self, user_id):
        self.user_id = user_id
    def __repr__(self):
        return 'User({})'.format(self.user_id)

users = [User(23), User(3),User(99)]
#print(users)
sor = sorted(users,key= lambda u: u.user_id)
#sor = sorted(users,key = attrgetter (u.user_id))#Аналогичная запись
minimum = min(users,key=attrgetter('user_id'))#attrgeter()- создает и возвращает новый объект
print(minimum)
print(sor)
"""Группировка записей на основе полей """
#Задача:У вас есть последовательность словарей или экземпляров, и вы хотите
# итерировать по данным, сгруппированным по значению конкретного поля
#используем функцию itertools.groupby()
rows = [
{'address': '5412 N CLARK', 'date': '07/01/2012'},
{'address': '5148 N CLARK', 'date': '07/04/2012'},
{'address': '5800 E 58TH', 'date': '07/02/2012'},
{'address': '2122 N CLARK', 'date': '07/03/2012'},
{'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
{'address': '1060 W ADDISON', 'date': '07/02/2012'},
{'address': '4801 N BROADWAY', 'date': '07/01/2012'},
{'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]
#Сортировка по нужным полям
rows.sort(key = itemgetter('date'))
#Итеровка в группах Groupby() - создать итератор, который возвращает последовательные ключи и группы из итерируемого объект
#for date, items in groupby(rows, key = itemgetter('date')):
    #print(date)
    #for i in items:
        #print(' ',i)
#Group by() - работет следующим образом сканирует последовательность и ищет последовательные «партии»
# одинаковых значений (или значений, возвращенных переданной
# через key функцией). В каждой итерации функция возвращает значение
# вместе с итератором, который выводит все элементы в группу с одинаковым значением.
#---------------------------------------------------------------------------------------------
#Функция defaultdict - позволяет сгрупировать данные вместе в крупную структуру данных с произвольным доступом
#она позволяет создать мультисловарь

# rows_by_date = defaultdict(list)
# for row in rows:
#     rows_by_date[row['date']].append(row)
#     for r in rows_by_date['07/01/2012']:
#         print(r)

#Фильтрование элементов последовательности

"""Задача: У меня есть данные, внутри последовательности, и вы хотите извлечь значения или
сократить последовательность по какому-либо критерию"""
#Самый простой способ фильтрования последовательности
# использовать генератор списка (list comprehension).
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
sort_list = [n for n in mylist if n > 0]#Список
print(sort_list)
