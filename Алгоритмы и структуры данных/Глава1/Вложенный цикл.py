import string
#for i in range(1,4):
    #for j in range(1,6):
        #print(f' i = {i}, j = {j}', end = ' ' )
    #print()


a = [[1,2,3,4],[2,3,4,5],[3,4,5,6]]
b = [[1,2,3,4],[2,3,4,5],[3,4,5,6]]
c = []

#for row in enumerate:
    #print(row, type(row))
    #for x in row:
        #print(x, type(x), end = ' ')
   # print()

def dot(x):
    return 2**2+14*x-30

# lst = [2,4,6,10,12]
#
# a = map(dot,lst)
# print(list(a))

string1 = 'MaksimPuzankov'

#print(list(map(string.capwords,string1)))

M,N = list(map(int,input('Введите M и N: ').split()))

zeros = []

for i in range(M):
    zeros.append([0]*N)

print(zeros)
