class Person:
    age: int = 20
    height: int = 170


person_1 = Person()
person_2 = Person()

person_1.height = 160
print(person_1.__dict__)

person_2.haircolor = 'black'
print(person_2.__dict__)

print(Person.__dict__)
#print(Person.hair_color)# Возникнет ошибка потому что hair_color находится в области видимости экземпляра Person_2

class People:
    name = "Maksim"

    def hello():
        print('Hello')

People.hello()