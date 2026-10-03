# s = {'apple','orange','apple','pear','orange','banana'}
# s2 = set('hello')
# s3 = {i for i in range(1,11)}
# s4 = set()
#
# print(s)
# print(s2)
# print(s3)
# print(s4)
# nums = [1,2,3,1,2,4,5]
# nums2 = list (set (nums))
# print(nums2)
a = set('abracadabra')
b = set('alacazam')

c =a - b# вычитанием убираем все буквы, которые есть в b
d = a | b# объеденяет буквы из а в б
e = a & b# Пересечение буквы и в а и в b
f = a ^ b# множество из элементов
# print(a,b,c,d,e,f, sep='\n')
s = {'apple','orange','apple','pear','orange','banana'}
if 'apple' in s:
    print('ok')
s.discard('apple')
s2 = s.copy()
print(s, id (s))
print(s2, id (s2))

