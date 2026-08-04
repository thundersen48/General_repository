#Protected '_' Доступ к защищеным ресурсам, доступен только внутри класса также внутри унаследованных классов.
#Private - '__' - Недоступны извне, с ними можно работать только внутри класса.
#Public - None.

class Student:
    def __init__(self,name,age):
        self._name = name
        self._age = age

S = Student('Maks',18)
S.age = 25
print(S._age)