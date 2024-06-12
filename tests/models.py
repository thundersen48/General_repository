class Student:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age
    def set_age(self, value):
        self.age = value

#p = Student(name='Максим', age= 18)
#print(p)