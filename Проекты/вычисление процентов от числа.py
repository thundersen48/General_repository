connect = True
while connect == True:
    number = input('число:')
    procent = input('Процент :')
    while type (number)!= int: #Равны ли оба операнда, если нет, то истина
        try:
            number = int(number)
            procent = int(procent)
        except valueError: #Исключения данная функция выполняет алгорит, когда не будет соблюдено правило
            print('Вводи целочисленные значения !')
            number = input ('Число:')
            procent = input('Процент:')
    while type(procent) != float:
        try:
            naumber = float(number)
            procent = float(procent)
        except valueError:
            print('Введи цифры !')
            number = input ('Введи число:')
            print()
            procent = input('Введи процент:')
            print()
    finish = number / 100 * procent
    print('Ваш ответ',float(finish))



