# Абстракция - это конченый продукт, при котором пользователь не понимает, как он работает(Водителю не нужно знать как работает двигатель внутреннего сгорания, введя при этом машину)
class Core:# Реализация абстракции класса.
    def __init__(self):
        self._types = {
            'A':100,
            'B':300
        }
    def get_salary(self,class_name): # Публичный метод
        return self._types.get(class_name, 0)
class AccountingInterface:  #Интерфейс бухгалтера
    def __init__(self,data):
        self._core = Core() #Атрибут который является объектом класса core
        self._database = data

    def get_salary(self, name):
        class_of_employee  = self._database.get(name) #Объект класса, который предоставляет имена работников
        salary = self._core.get_salary(class_of_employee)
        return salary

dict = {'Maks':'A','Stephan':'B'}
interface = AccountingInterface(data = dict)# Передаем имена в интерфейс
print('Maks salary is {}'.format(interface.get_salary(name ='Maks')))




class People:
    age = 18
    educational_institutes = 'RUT MIIT'
    spesialitet = 'Mechatronics and robotics'
    date_of_brith = '05.08.2005'

    def __init__(self):
        print('Информация')# Конструктор класса!
# Методы класса
    def get_age(self):
        return self.age
    def get_educational(self):
        return self.educational_institutes

    def get_specialitet(self):
        return self.spesialitet

p = People()

# абстракция - это сокрытие целых классов или групп классов путем построения архитектуры програмного продукта


from abc import ABC, abstractmethod

class Vechicle(ABC):

    def go(self):
        pass

class Car(Vechicle):

    def go (self):
        print('Ты водишь машину')

class Motorcycle(Vechicle):