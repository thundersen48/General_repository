matrix = [[0,1,2,3],
          [10,11,12,13],
          [20,21,22,23]
          ]


a = [(i,j) for i in range(3) if i %3 for j in range (4)]
#Преобразуем матрицу в список
c = [x for row in matrix
     for x in row]

b = []
for i in range(3):
    if i % 3:
        for j in range(4):
            b.append(f'{i}*{j} = {i * j}')

# print(a)
# print(b)
# print(c)


M,N = 3,4

matrix = [[a for a in range (M)] for b in range(N)]

print(matrix)

A = [[1,2,3],
     [4,5,6],
     [7,8,9]]

At = [[row[i] for row in A] for i in range(len(A[0]))]
VL = [[x**2 for x in row]for row in A]
print(At)
print(VL)