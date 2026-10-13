"""
В множестве данные не повторяются
с помощью операции юнион можно объеденять сеты
0 = False
Всё что выше нуля приравнивается к значению True
"""



my_set = {1,2,3, True , 'Hello', 2, True}
set_2 = {2,3,False}
print(my_set)
print(set_2)
print(my_set.union(set_2))