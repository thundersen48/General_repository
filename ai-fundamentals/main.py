class Student:
    age = 18
    Universitet = 'RUT MIIT'

class B1:
    pass
class B2:
    pass

def method1(self):
    print(self.__dict__)

a = type("Student",(B1,B2),{'age':18, 'method1': lambda self: self.age})
b = a()
print(b.method1)
c =b.method1()
print(c)

def create_student(name, base, attrs):
    attrs.update({'age':18,'Universitet': 'RUT MIIT'})
    return type(name,base, attrs)

class Create(metaclass = create_student):
    def get_age(self):
        return(18)

d = Create()
print(d.Universitet)