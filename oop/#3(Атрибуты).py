class PersianCat:
    breed = 'persian'#Атрибут класса
    age = 12.0 #Float


class SiberianCat:
    breed = 'Siberian'
    age = 0.5 #Float


class BengalCat:
    breed = 'bengal'
    age = 2.0

Tom = PersianCat()# Создаем объекты и присваиваем им имя
Garfield = SiberianCat()
Max = BengalCat()
print(type(Tom),type(Garfield),type(Max), sep='\n')
print(isinstance(Tom,PersianCat))#Том является классом PersianCat




