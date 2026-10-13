# # x = 1
# # while x < 1020:
# #     print(x)
# #     x=x+1
# spisok=[12,2023,2024,1560]
# # for number in spisok:
# #     print(number)
# for i in range(0,11):
#     print(i)
# name=('Makson','\n')
# for i in name:
#     if i== 'o':
#         break
#     print(i)

# for i in range(1,10):
#     if i%2 == 0 or i%3 == 0:
#         continue
#     print(i)
# a=('Maksim, тупой дебил')
# for i in a:
#     if i =='':
#         break
#     print(i,end='',sep='')
# else:
#     print('конечно он дебил',sep=' ')
# for i in range(1,1000):
#     for k in range(2,3):
#         print(f'{i}*{k}={i*k}\n',end='')
# print('')

# list = ['123','0-10','2030']
# print(sorted(list))
# n = int(input())
# flag = False
# i = 2
# # while i < n:
#     if n % i ==0:
#         flag = T22rue
#         print(f'{n} делится на {i}')
#     i += 1
# if flag:
#     print(f' {n} не является простым числом')
# else:
#     print(f'{n} - простое число')
# s = 0
# while True:
#     n = int(input())
#     s += n
#     if n == 0:
#         break
# # print(s)
# import random
# lst = [i for i in range(random.randint(5, 500))]
# while True:
#     if not lst:
#         break
#     print(lst.pop())
# n = int(input())
# i = 2
# while True:
#     if n % i == 0:
#         break
#     i += 1
# print(i)
# n = int(input())
# while True:
#     if n == 0:
#         break
#     elif n > 50 or n <= -50:
#         break
#     elif n % 2 == 0:
#         break
#     print(n / 5)
#     n = int(input())
# print('hello {name},my age is {y}'.format(name='Maks',y=18))
# light = ('red')
# if light == ('red'):
#     print('stop')
# elif light ==('green'):
#     print('go go go')
# else:
#     print('что происходит?')

# number = 0
#
# for number in range(10):
#     if number == 5:
#         break
#     print('Number is ' + str(number))
# print('Out ')




# children = ['Puzankov_2005', 'Volodkov_2005','savidchev_2004','troegubov_2004']
# names =[]
# for child_name in children:
#     surname = child_name.split('_')[0].title()
#     # surname = surname.title()
#     print(surname)
#     continue
#     names.append(surname)
#     print(names)


# person={'name':'Maks','surname':'Puzankov',
# 'email': 'dicersmaks@mail.ru'}
# d=dict(name='Maks', tel='89081028340')
# new = {'name':'dima','tel':'89048281853'}
# person.update(new)
# print(person)
# a=50
# b=10
# def calc (a,b):
#     print(a)
#     print(b)
#     return (a+b)

# counter = 10
# while True:
#     print(counter)
#     if counter >=20:
#         break
# file = open('readme.txt')
# data = file.read()
# print(data)
# file.close()


# 1000 : 15 = mass : x
# x = 15*mass/1000
# ingredients = {'salt':15,'pepper':5}
# def get_salt_mass(m):
#     return m * 15/1000
# def get_pepper_mass(m):
#     return m * 5/1000
# def get_ingredients_mass(m ,ingr):
#     return m*ingredients.get(ingr,0)/1000
# print(get_ingredients_mass(1500,'cinnamon'))
#
# def square(x):
#     return (x**2)
# def example ():
#     print(1)
#     print(2)
#     return("hello")
#     print(3)
#     print(4)
# example()
# # a = square(19)
# # print(a)
class graph:
   def __init__(self,gdict=None):
      if gdict is None:
         gdict = {}
      self.gdict = gdict
   def edges(self):
      return self.findedges()
# Add the new edge
   def AddEdge(self, edge):
      edge = set(edge)
      (vrtx1, vrtx2) = tuple(edge)
      if vrtx1 in self.gdict:
         self.gdict[vrtx1].append(vrtx2)
      else:
         self.gdict[vrtx1] = [vrtx2]
# List the edge names
   def findedges(self):
      edgename = []
      for vrtx in self.gdict:
         for nxtvrtx in self.gdict[vrtx]:
            if {nxtvrtx, vrtx} not in edgename:
               edgename.append({vrtx, nxtvrtx})
            return edgename
# Create the dictionary with graph elements
graph_elements = {
   "a" : ["b","c"],
   "b" : ["a", "d"],
   "c" : ["a", "d"],
   "d" : ["e"],
   "e" : ["d"]
}
g = graph(graph_elements)
g.AddEdge({'a','e'})
g.AddEdge({'a','c'})
print(g.edges())


























