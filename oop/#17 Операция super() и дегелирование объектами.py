class Person:
    def __init__(self, name):
        self.name = name



class Student(Person):
    def __init__(self,name,surname,Bachelorsdegree):
        super().__init__(name)#Хотим полуить имя, использовав класс Person, чтобы не нарушать правило DRY
        self.surname = surname
        self.Bachelorsdegree = Bachelorsdegree

class Food(Student):
    def __init__(self,name, surname,Bachelorsdegree):
        super().__init__(name)
      

s = Student('Ivan','Ivanov','Мехатроника')
print(s.__dict__)


"""
class Person:
    def hello(self):
        print(f'Связан с {self}')

class Student(Person):
    def hello(self):
        print('Student obj.hello() is called')
        super().hello()

s = Student()
s.hello()#Получим метку, что метод класса был вызван из экземпляра "Student"
print(hex(id(s)))
#Метод был связан с экземпляром класса, который вызывал родительский метод!
"""