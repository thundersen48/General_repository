
def get_V(a,b,c, truening = True):
    if truening:
        print(f' a = {a}, b = {b}, c = {c}')
    return a * b * c
#Именнованные параметры - те параметры, которые мы присвавываем аргументы
#
v = get_V(10,15,c =3)

print(v)