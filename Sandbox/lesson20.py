# t1 = (1,2,3)
# l1 = [1, 2, 3]
# # t1 = 1,2,3
# t1 = (1, 2, 3)
# print(t1.__sizeof__())
# print(l1.__sizeof__())
# t1 = tuple('hello')
# t2 = tuple('world')
# t3 = t1+t2
# print(t3.count('l'))
# if 'l' in t3:
#     print(t3.index('l'))
# else:
#     print('No')
#
# for i in t3:
#     if i == ' ':
#         continue
#     print(f' "{i}"', end=' ')

# t1 = (10,11,[1,2,3],[4,5,6],['hello','world'])
# print(t1,id(t1))
# t1[4][0]= 'new'# обращаемся к 4 элементу,(списку) потом обращаемся к слову hello
# t1[4].append('helo')
# print(t1,id(t1))
# t1 = (1,2,3,)
# x = t1[0]
# y = t1[1]
# z = t1[2]
# print(x,y,z)
# x = 1
# y = 2
# print(x,y)
# x,y = y,x
# print(x,y)
words =['Мадам','топот','test','madam','word']
palindromes = []
for word in words:
    pass
print('test'[::-1])
# my_str =['Око за око','А роза упала на лапу озора','Около Миши молоко']
# x=words[0]
# y=words[1]
# z=words[3]
# print(x,y,z)
palindromes =[word for word in words if word == word[::-1]]
my_str = ['Око за око','А роза упала на лапу озора','Около Миши молоко']
palindromes =[]
print  (my_str[2][::-1])
















