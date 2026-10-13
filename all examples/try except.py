def calc(m): #задаем функцию
    #1000:10=m:x
    try:#Верный исход кода
        m = int(m)# присваиваем переменной m целое число
    except ValueError as e: #данный способ обеспечивает бесперебойную работу, здесь мы расматриваем случай в виде ошибки
         print(e)
         m = 0
    except TypeError:
        pass
    except FileNotFoundError:
        pass# заполнитель для команды
        return 10 *m / 1000
    # finally:
    # print('Hi')


print (calc('s'))