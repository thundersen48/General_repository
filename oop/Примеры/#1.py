class Phone:
# Инициализатор
    def __init__(self):
        self.is_on = False
# Функция включения телефона
    def turn_on(self):
        pass

    def call(self):
        if self.is_on:
            print("Сделайте звонок")

    # Метод, который выводит короткую сводку по классу Phone
    def info(self):
        print(f'Class name: {Phone.__name__}')
        print(f'If phone is ON: {self.is_on}')


# Унаследованный класс
class MobilePhone(Phone):

    def __init__(self):
        super().__init__()
        self.battery = 0

    # Такой же метод, который выводит короткую сводку по классу MobilePhone
    # Обратите внимание, что названия у методов совпадают - оба метода называются info()
    # Однако их содержимое различается
    def info(self):
        print(f'Class name: {MobilePhone.__name__}')
        print(f'If mobile phone is ON: {self.is_on}')
        print(f'Battery level: {self.battery}')

def show_polymorphism():
    for item in [Phone, MobilePhone]:
        print('-------')
        object = item()
        object.info()
print(show_polymorphism())