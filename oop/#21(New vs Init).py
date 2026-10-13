
class Matryoshka:
    def __init__(self,dress_color,eye_color,name):
        print(f'Запускается метод __init__ и наделяет экземпляр типа __init__{self.__class__} переданными характеристиками')
        self.dress_color = dress_color
        self.eye_color = eye_color
        self.name = name

    def __new__(cls, *args, **kwargs):
        print(f'Запускается метод new, который аллоцирует память для экземпляра типа {cls}')
        res = super().__new__(cls) #Обращаемся к родительскому классу
        return res

    def say_hello(self):
        print(f'Hello, <username> from {self.name}!')

    def __str__(self):
        return f'Matryoshka{self.name}'

print(Matryoshka)
print(type(Matryoshka))
c = Matryoshka('Red','Blue', 'Maria')


"""
Метод __new__  отличается от метода __init__  тем, что __new__ возвращает новый экземпляр класса,
"""

class A(object):
    def __new__(cls):
        obj = super(A, cls).__new__(cls)
        print ('Создаем объект', obj)
        return obj

    def __init__(self):
        print ('Инициализируем объект', self)

print(A())