print('Таблица умножения')

for  i in range(1,10):#Внешний цикл
    for k  in range (2,10):#Внутренний цикл
        print(f'{i} * {k} = {i * k}\t', end=' ')
    print('')
else:
    print('well done')
