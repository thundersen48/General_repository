class Person:
    def hello():
        print("hello")


Person.hello#Создаем атрибут класса
p = Person()
print(p.hello)# На ввыходе получим bound метод он передает метод который зависит от экзмепляра класса
print(hex(id(p)))#Отображаем индификатор p в шестандцитиричной системе
print(type(Person.hello))
print(p.hello.__self__)

class Vechicles:
    def machine(Lamborginy):
        print('Lamborginy')#Lamborginy здесь нужен чтобы получить доступ к экзмеплярам и самим классам.


a = Vechicles()
print(a.machine())
print(a.machine.__self__)
print(hex(id(a)))
"""
Пространство имен класса и пространство имен экзмепляра друг от друга изолированны!

"""

class Student:
    def learner(self):
        pass



p = Student()
p.first_name = 'Maksim'
p.last_name = 'Puzankov'
p.age = 18
p.Bachelor = "Mechatronics and robotics"