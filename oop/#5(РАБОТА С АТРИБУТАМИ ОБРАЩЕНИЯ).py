class Person:
    age = 18
    height = 178


a = Person()#Переменная a экземпляра Person
b = Person()

print(a.age, b.height)#Обращаемся через экзмепляр
a.x = 55#Создали рандомный атрибут
print(a.x)
print(Person.__dict__, a.__dict__, sep='\n')
