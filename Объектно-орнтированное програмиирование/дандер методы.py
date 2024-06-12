
class Employe:

    raise_amt = 1.04

    def __init__(self, first,last,pay ):
        self.first = first
        self.last = last
        self.email = first + '.' + '@email.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


emp_1 = Employe('Corey','Ch',5000)
emp_2 = Employe('Test', 'Employee',6000)
print(emp_1.__dict__)

# Двойное подчеркивание необходимо, чтобы предотвратить конфликты имен с другими методами!


# init метод отвечает за инициализацию экземпляра класса
class Square:
    def __init__(self, side_length):
        self.side_length = side_length

sq = Square(1)
print(sq.side_length)
# Call - позволяет создать вызываемые объекты,то есть их можно вызывать как функции.
class CallableObject:
    def __call__(self, x):
        return x ** 2

callable_object = CallableObject()
print(callable_object(5))
#__getitem__ и __setitem__: Методы позволяют обращения к объекту по индексу или ключу, как если бы это был список или словарь.
class MyContainer(object):

    def __init__(self):
        self.storage = {}

    def __setitem__(self, key, value):
        self.storage[key] = value

    def __getitem__(self, key):
        return self.storage[key]


my_container = MyContainer()
my_container['a'] = 'b'
my_container['a']  # b
my_container['q']  # KeyError


class MyDictionary:
    def __init__(self): self.dictionary = {}
    def __getitem__(self, key): return self.dictionary[key]
    def __setitem__(self, key, value): self.dictionary[key] = value


my_dict = MyDictionary()
my_dict["test"] = "value"
print(my_dict["test"])
print(my_dict.__dict__)

class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = list(age)
    def __getitem__(self, item):
        return self.age[item]

S1 = Student('Максон',[15,18,16,14])
print(S1[1])
#4. __iter__ и __next__:
#Эти методы позволяют создавать итерируемые объекты, которые можно использовать в цикле for.
#Iter - Позволяет определить механизм прохода(итерирования) по элементам объекта
# Next - Возвращает следующий элемент в последовательности.
class Mynumbers:
    def __iter__(self):
        self.a = 10
        return self
    def __next__(self):
        x = self.a
        self.a += 15
        return  x

Myclass = Mynumbers()
Myiter = iter(Myclass)
print(next(Myiter))
print(next(Myiter))
print(next(Myiter))
print(next(Myiter))
print(next(Myiter))

# __enter__ и __exit__:
class MyFile():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, type, value, traceback):
        self.file.close()

with MyFile('test.txt', 'w') as myfile:
    myfile.write('Hello, world!')
# Метод __enter__ используется для входа в контекстный блок
# Метод __exit__ Используется для выхода из контекстного блока
