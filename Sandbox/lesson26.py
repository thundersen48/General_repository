# def hello(name, word):
#     print('hello,'+name + 'say'+word)
# hello('Maks',hi)
# hello('Katy',hello)


# def get_sum(a,b):

    
# x=2
# y=5
# get_sum(1,3)
# get_sum(x,y)
# len('hello')
#     return a + b    #Возвращает результат
# print(get_sum(1,5))
# """""
# обязательно нужно возвращать результат! иначе получим некрасивый код с None
# """

# def get_sum(x,y): # задали функцию, после чего указали ее имя, в скобках задаем параметры функции
#     return x*y# тело функции, функция return используется для определения значения, которое возвращает функция при вызове
# result = get_sum(5,6) #сохраняем вывод функции в переменной
# print(result)

# def f(x):
#     return x + 1
# z = f(5)
# if z == 5:
#     print("z равно 5")
# else:
#     print ("z не равно 5")
# def f():
#     return 1 + 1
# result = f()
# print(result)  # 2
# def Scores(student, *scores):
#     print(f"Student Name: {student}")
#     for score in scores:
#         print(score)
# Scores('Maks',100,200,250)
# def petNames(owner,**pets):
#     print(f'owner name:{owner}')
#     for pet,name in pets.items():
#         print(f'{pet}: {name}')
# petNames('Maks', dog='Mops', fish=['Larry','curly'], turtle='Sheldon')

# def user_name(name,age):
#     print(f'hello gandon {name}, my age {age}!')
# user_name('Maks',18)


def petNames(owner,**pets):
    print(f'owner name:{owner}')
    for pet, name in pets.items():
        print(f'{pet}: {name}')
petNames('Maks', dog='Mops', fish=['Larry','curly'], turtle='Sheldon')




