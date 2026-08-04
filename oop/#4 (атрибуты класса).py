# 5, 17.8, 'cat',[1,2,3]

a = 5
b = 17.8
animal = 'cat'
c = [1,2,3]
print(isinstance(animal,str))

class Person:
    age = 18
    name = 'Max'
    residence = 'Moscow'


"""
print(getattr(Person,'age'))# Получение атрибута класса.
print(getattr(Person,'x','Все good!'))
"""
"""
Другой способ создания атрибута класса
person.x = 15
print(person.x)
"""
setattr(Person, 'name2',"David")#Устанавливает значения класса.
print(Person.name, Person.name2,sep ='\n')

del Person.age#Удаление атрибута автоматически

delattr(Person, 'residence')#удаление атрибута
print(Person.__dict__)#Вызов словаря
print(Person.age)

