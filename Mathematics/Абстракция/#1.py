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




