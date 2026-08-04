class A:
    x: float = 17.8

A.y = 'ingeniring'
print(A.x)
del A.x
print(A.__dict__)


class B:
    x: int = 15
    y: int = 7

print(getattr(B,'x')+getattr(B,'y'))
print(getattr(B,'Z','Ничего не найдено'))


class C:
    pass

setattr(C,'x', 11)
C.y = 'Hello World!'
print(getattr(C,'y').upper())# Вывод строки в верхнем регистре.
print(C.__dict__)#Просмотр атрибутов

class D:
    x: int = 14
    y: float = 15.6


del D.x
print(getattr(D,'x','impossible'))
delattr(D,'y')
print(D.__dict__)
#Убеждаемся что переменной нет в классе
