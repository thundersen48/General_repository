"""Набор классов для представления электромобилей."""

from study.import_practice.car import Car

class Battery:
    """Простая модель аккумулятора электромобиля."""

    def __init__(self, battery_size=40): #Если значение battery_size не присвоено, то этот необязательный параметр задает battery_size значение 40.
        """Инициализирует атрибуты аккумулятора."""
        self.battery_size = battery_size

    #Метод describe_battery также перемещен в этот класс
    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print(f"This car has a {self.battery_size}-kwh battery. ")

    def get_range(self):
        """Выводит данные о приблизительном запасе хода для аккумулятора."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge")

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65
#Классу ElectricCar необходим доступ к классу родителю Car, поэтому класс Car импортируется в этот модуль.
#Необходимо, чтобы модуль car содержал только класс Car.

class ElectricCar(Car):
    """Предоставляет аспекты машины, спецефические для электромобилей."""
    def __init__(self, make, model, year):
        """Инициализирует атрибуты класса-родителя"""
        super().__init__(make, model, year)#Вызываем метод родительского класса, чтобы получить доступ ко всем атрибутам класса-родителя.
        self.battery = Battery()# Создаем новый экземпляр Battery(со значением battery_size по умолчанию равным 40, поскольку значение не задано.)
                                #и сохраняем его в атрибуте экземпляра self.battery. Это будет происходить при каждома вызове __init__().
#Теперь любой экзмепляр ElectricCar будет иметь автоматически создаваемый экземпляр Battery.
    