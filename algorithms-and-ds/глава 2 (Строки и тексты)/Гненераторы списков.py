N: int = 6
# a = [0] * N #Формируем список, состоящий из 0 длиной N
#
# for i in range(N):
#     a[i] = i**2
#
d_inp = input('Целые числа: ')
a = [x ** 2 for x in range(N)]
b = [x % 4 for x in range(N)]
c = [x % 2 for x in range(N)]
d= [int(d) for d in d_inp.split()]
print(a)
print(b)
print(c)
print(d)

