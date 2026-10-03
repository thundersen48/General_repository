 # s = 'Hello world'
# if  ' ' in s:
#     s = s.upper()#перевод строки к верхнему регистру
# else:
#     s=s.lower()# перевод строки к нижнему регистру
# print(s)
# def set_register(s):
#     if ' ' in s:
#         return  s.upper()
#     else:
#         return  s.lower()
# print(set_register('Hello world'))
# print(set_register('helloworld'))

# def get_sum(a,b,c,d):
#     return a+b+c+d
#
#
# print(get_sum(1,2,5,7))
# print('hello',end='',sep='')
#
# def get_sum(*args):        #args- позиционные агрументы, именнованные аргументы
#     return sum(args)
#
# print(get_sum(1,5,10))
# def func(**kwargs):
#     print(kwargs)
# func(a=1,b=5,c=20)
def f(a,x,*args,**kwargs):
    print(a)
    print(x)
    print(args)
    print(kwargs)

f(1, 2 , 3, 4, b = 'test', c='hi')

