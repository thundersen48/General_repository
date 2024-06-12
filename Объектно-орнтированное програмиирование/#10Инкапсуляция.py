
class Person():
    def __init__(self, name, surname):
        self._name = name#Нижние подчеркивания являются приватными значениями
        self._surname = surname
        self.name = f'{self._name} {self._surname}'#Приватные значения

#Приватные значения- то есть использование экземпляров вне этого класса невозможно!

p = Person('Maksim','Puzankov')
print(p.name)