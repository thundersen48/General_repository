#Absoulute value
#abs()
# Функция abs - возвращает абсолютные значения числа
class implementABS:
    def __init__(self,string):
        self.string = string

    def __abs__(self):
        return self.string.lower()

custom_obj = implementABS('Hello')

x = abs(-9)
y = abs(-100.876)
z = abs(custom_obj)

print(x)
print(y)
print(z)