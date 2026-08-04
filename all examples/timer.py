import time

while True:
    i=0 # переменная отвечающая за секунды
    ii=0 #минуты
    iii = 0 # часы
    time_user = int(input('введите кол-во секунд:'))
    comment = str(input('введите комментарий:'))
    for q in range (time_user):
        time.sleep(1)
        i+=1
        print('Прошло секунд :', i)
        if(i % 60) == 0:
            ii+= 1
            print('Прошло минут:',ii)
        if(i % 3600) ==0:
            iii += 1
            print('Прошло часов:', iii)
print('Время окончено')
print('Ваш комментарий:')