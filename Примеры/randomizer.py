import random
print('Рандомайзер')
print()
a = True
while a == True:
    b = input('От:')
    print()
    c = input('До:')
    print()
    finish = random.randint(int(b),int(c))
    print('Ответ:',int(finish))
    print()
input()

