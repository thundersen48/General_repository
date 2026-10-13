#Any
#Any() - Возвращет True или False если значение итерируемого объекта True или False

a = [1,0,1,2,3]
print(any(a))

b = [True,True, 1, 2]
print(any(b))

c = ["",'a','b']
print(any(c))

d = [[0,0],[0,0],[0,0]]
print(any(d))
e = [[],False,0]
print(any(e))
