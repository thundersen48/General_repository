from abc import ABCMeta, abstractstaticmethod

class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod
    def print_data():
        """Дочерний класс"""

class PersonSingleton(IPerson):

    __instance = None # Единственный экземпляр
    @staticmethod
    def get_instance():
        if PersonSingleton.__instance == None: # есть ли у класса экземпляр
            PersonSingleton('Имя по умолчанию', 0)
            print('Экземпляр не найден')
        return __instance
    """Присваиваем экземпляру объект"""
    def __init__(self,name,age):
        if PersonSingleton.__instance != None: #Ставим условие существование 1 экземпляра
            raise Exception('Синглетон не может быть создан более 1 раза!')
        else:
            self.name = name
            self.age = age
            PersonSingleton.__instance = self

    @staticmethod
    def print_data():
        print(f'Name:{PersonSingleton.__instance.name}, Age:{PersonSingleton.__instance.age}')

p =PersonSingleton('Maks',18)
print(p)
p.print_data()
p2 = PersonSingleton("Stepan", 16)
print(p2)
