

class Person:
    age = 0
    def hello (self):
        print('Hello')

class Student(Person):
    pass

s = Student()
#print(dir(s))# посмотрим методы в классе student
print(s.age)
s.hello()
print(s.__dict__)
print(Person.__dict__)
