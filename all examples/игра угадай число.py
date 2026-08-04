import random

x = random.randint(1, 100)
user_num = 0
cnt = 0  # попытки
while True:
    user_num = int(input('я загадал число от 1 до 100 - угадайте:'))
    cnt += 1  # cnt = cnt+1
    if user_num == x:
        print(f'Ты угадал число за {cnt} попыток')
        if input('Сыграем еще?"yes/No":') == 'yes':
            x = random.randint(1, 100)
            cnt = 0
        else:
            print('Спасибо за игру')
            break  # выходим из цикла при срабатывании внешнего условия
    elif user_num > x:
        print('Мое число меньше')
    else:
        print('Мое число больше')
