# Обычные методы класса
# доступны только после создания экземпляра класса, то есть чтобы вызвать такой метод, надо обратиться к экземпляру.

class Phone:

    def __init__(self, color, model):
        self.color = color
        self.model = model

    # Обычный метод
    # Первый параметр метода - self
    def check_sim(self, mobile_operator):
        if self.model == 'I785' and mobile_operator == 'MTS':
            print('Your mobile operator is MTS')

m = Phone('Red', 'I785')
#Статические методы - это обычные функции, которые помещены в класс для удобства и тем самым располагаются в области видимости этого класса
class Phone:

    # Статический метод справочного характера
    # Возвращает хэш по номеру модели
    # self внутри метода отсутствует
    @staticmethod
    def model_hash(model):
        if model == 'I785':
            return 34565
        elif model == 'K498':
            return 45567
        else:
            return None

    # Обычный метод
    def check_sim(self, mobile_operator):
        pass


# Методы класса -такие методы тесно связаны с классом, в котором они определены

class Phone:

    def __init__(self, color, model, os):
        self.color = color
        self.model = model
        self.os = os

    # Метод класса
    # Принимает 1) ссылку на класс Phone и 2) цвет в качестве параметров
    # Создает специфический объект класса Phone(особенность объекта в том, что это игрушечный телефон)
    # При этом вызывается инициализатор класса Phone
    # которому в качестве аргументов мы передаем цвет и модель,
    # соответствующую созданию игрушечного телефона
    @classmethod
    def toy_phone(cls, color):
        toy_phone = cls(color, 'ToyPhone', None) # В классе методе мы сразу задаем параметры, без указания ссылок!
        return toy_phone

    # Статический метод
    @staticmethod
    def model_hash(model):
        pass

    # Обычный метод
    def check_sim(self, mobile_operator):
        pass