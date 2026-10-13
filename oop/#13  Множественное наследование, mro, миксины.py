class FoodMixin:
    food = None

    def get_food(self):
        if self.food is None:
            raise ValueError('food should be set')
        print(f'я люблю {self.food}')

class Person:
    def hello(self):
        print('I am Person')

class Student(FoodMixin, Person):
    food = 'Котлетки с пюрешкой'
    def hello(self):
        print('I am Student')

class Prof(Person):
    food = 'Пасту карбонару'
    def hello(self):
        print('I am Prof')

class someone(Prof,Student):
    pass

s = someone()
s.hello()
#print(s.__class__.mro())# Узнаем о минерализации классов
s.get_food()