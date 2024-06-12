import pandas as pd
import copy

v = [0.,0.,0.,0.,300.,80.,-1219.,-1.]
a = [[0,1,0,0,-8,-2,30,1/2],
     [1,0,0,0,19/2,5/2,-38,-2/3],
     [0,0,1,0,40,-3,90,1],
     [0,0,0,1,0,0,0,1]
]
b = [0,0,1,1]
#Построение задачи по вектор строкам
def rev(lst):
    return [ -i for i in lst ]

lin_prog = a
lin_prog.insert(4,rev(v))
lin_prog[4].insert(0,0)
for x in range(4):
  lin_prog[x].insert(0,b[x])
task = pd.DataFrame(columns = ['X_','X1','X2','X3','X4','X5','X6','X7','X8'],data = lin_prog)
print(task)
# Симплекс метод
def iter(a):
  max_x = 0
  max_y = 0
  while a[4][max_x]>=0:
    max_x+=1
    if max_x>8:
      print('Оптимальное решение найдено')
      return a
  for x in range(max_x,9):
    if abs(a[4][x])>abs(a[4][max_x]) and a[4][x]<0 and a[4][x]!=0 and  a[1][x]>=0 and  a[2][x]>=0 and  a[3][x]>=0 :
      max_x = x
  while a[max_y][max_x]<=0:
    max_y+=1
  for y in range(5):
    if a[y][max_x] <=0: continue
    if a[y][max_x]>0 and abs(a[y][0]/a[y][max_x])<abs(a[max_y][0]/a[max_y][max_x]): max_y = y
  b = copy.deepcopy(a)
  for i in range(5):
    for j in range(9):
      if i==max_y:
        b[i][j]= a[i][j]/a[max_y][max_x]
      if i!=max_y: b[i][j]=a[i][j]- a[i][max_x]*a[max_y][j]/a[max_y][max_x]
  return b


lin_prog_iter = copy.deepcopy(lin_prog)
for x in range(7):
  print(str(x)+' ITERATION\n')
  df = pd.DataFrame(columns = ['X_','X1','X2','X3','X4','X5','X6','X7','X8'],data = lin_prog_iter)
  print(df,'\n\n')
  lin_prog_iter=iter(lin_prog_iter)