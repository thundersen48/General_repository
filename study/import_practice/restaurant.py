#9.6. Киоск с мороженым.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Выводит два атрибута экземпляра"""
        print(f"\nВ ресторане: {self.restaurant_name} вид кухни: {self.cuisine_type}.")

    def open_restaurant(self):
        """Выводит сообщение об открытии ресторана"""
        print(f"\nРесторан {self.restaurant_name} открыт с 10:00 до 22:00")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def get_flavors_string(self):
        """Возвращает строку со всеми сортами мороженого через запятую."""
        return ', '.join(self.flavors)

    def save_report_to_file(self,file_name, content):
        with open(file_name, 'w') as f:
            f.write(content)


