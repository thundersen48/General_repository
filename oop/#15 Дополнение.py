class Car:
    def __init__(self,name):
        #Максимальные скорости
        self._name_speed_dict = {
            'Mercedes': 250,
            'BMW': 300
        }
        self._max_speed = self._define_max_speed(name)

    def  _define_max_speed(self,name): # Метод который возвращать по ключу max скорость
        return self._name_speed_dict.get(name,0)

    def distance_on_max_speed(self,distance):
        if self._max_speed == 0:
            print('speed = 0')
            return 0
        return distance / self._max_speed

car_a = Car(name='BMW')
car_b = Car(name='Mercedes')
print(car_a.distance_time_on_max_speed(distance= 167))# Расчёт MAX time
print(car_b.distance_time_on_max_speed(distance= 167))
