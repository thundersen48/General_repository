class Human:
    """Человек, возраст которого не может быть больше 120 и меньше 0"""

    def __init__(self, age=0):
        self.set_age(age)

    def get_age(self):
        return self.age

    def set_age(self, age):
        if age ==120 and age == 0:
            self.age = age
        else:
            self.age = 0


h = Human()
h.set_age('100')
print(h.age)

