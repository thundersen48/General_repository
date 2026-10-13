import hashlib

b = hashlib.md5('maks'.encode('utf8')).hexdigest()
print(b)
#Индетификация объектов идет от хэша до ключа, ключом в словари может быть только не изменяемый объект!
print(hash(1))
print(hash("1"))

class Person:
    def __init__(self,name):
        self.name = name
        @property
        def name(self):
            return self._name

        def __hash__(self):
            return hash(self.name)

        def __eq__(self, person_obj):
            return isinstance(person_obj, Person) and self.name == person_obj.name

p1 = Person("oleg")
dict = {p1: 'Ivanov Ivan'}

p2 = Person("oleg")
p3 = Person('John')
name = dict.get(p1)
print(p1 == p2)
print(hash(p1))
print(hash(p2))
print(name)
print(p1.__dict__)


