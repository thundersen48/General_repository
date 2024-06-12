# Инкапсуляция заключается в сборе одно место (класс) данных и методов для работы с ними
import collections
text = collections
text = '123'
#print(dir(text))
print([e for e in dir(text) if not e.startswith('_')])

class Person:
    def __init__(self, first_name, last_name, age):
        self._first_name = first_name
        self._last_name = last_name
        self._age = age

    def describe(self):
        print(f'I am {self._first_name} {self._last_name}, I\'m {self._age} years old!')

if __name__ == '__main__':
    Ivan = Person('Ivan', 'Ivanov', 20)
    Ivan.age = 1000
    Ivan.describe()
