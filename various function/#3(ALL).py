#All - все ли значения в итерируемом объекте являются истинными?

a = [1,0,1,2,3]
print(all(a))

b = [True, True, 1, 2]
print(all(b))

c = ["",'a','b']
print(all(c))

d = [[0,0],[0,0],[0,0]]
print(all(d))
e = [[],[1],True]
print(all(e))