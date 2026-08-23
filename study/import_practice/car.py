
class Car:
    """Простая модель автомобиля."""
    def __init__(self, make, model, year):
        """Инициализирует атрибуты описания автомобиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #Назначили атрибуту значение по умолчанию

    def get_descriptive_name(self):
        """Возвращает отформатированное описание."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Выводит данные о пробеге машины в километрах."""
        """Новый метод read_odometer, упрощает чтение данных о пробеге машины в км. """
        print(f"This car has {self.odometer_reading} km on it.")

    def update_odometer(self, mileage):
        """Устанавливает заданное значение на одометре.
        При попытке обратной прокрутки изменение отклоняется.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage

        else:
            print("Вы не можете подкрутить назад значения одометра!")

    def increment_odometer(self, km):
        """Увеличивает показания одометра с заданным приращением."""
        current_odometer = self.odometer_reading
        new_odometer = km + self.odometer_reading
        if new_odometer >= current_odometer:
            self.odometer_reading = new_odometer
        else:
            print("Вы не можете подкрутить назад значения одометра!")


"""
class Battery:
    

    def __init__(self, battery_size=40): #Если значение battery_size не присвоено, то этот необязательный параметр задает battery_size значение 40.
        
        self.battery_size = battery_size

    #Метод describe_battery также перемещен в этот класс
    def describe_battery(self):
        
        print(f"This car has a {self.battery_size}-kwh battery. ")

    def get_range(self):
      
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge")

class ElectricCar(Car):
    
    def __init__(self, make, model, year):
        
        super().__init__(make, model, year)#Вызываем метод родительского класса, чтобы получить доступ ко всем атрибутам класса-родителя.
        self.battery = Battery()# Создаем новый экземпляр Battery(со значением battery_size по умолчанию равным 40, поскольку значение не задано.)
                                #и сохраняем его в атрибуте экземпляра self.battery. Это будет происходить при каждома вызове __init__().
#Теперь любой экзмепляр ElectricCar будет иметь автоматически создаваемый экземпляр Battery.
"""
    
