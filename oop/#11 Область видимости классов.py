#name = 'John'
class Person:
    name = 'Maks'


#Здесь мы можем только читать свойства
    @classmethod# получим сам класс как объект а не экземпляр класса
    def change_name(cls,name):
        cls.name = name


p = Person()
print(p.__dict__)# получим пустой словарь
p.change_name('имя с используемым class')

print('isinstance dict:', p.__dict__)

print('Person.name:',Person.name)


candy = 5

def get_candy():
    global candy
    candy += 1
    print('У меня столько конфет{}'.format(candy))

get_candy()
get_candy()
print(candy)