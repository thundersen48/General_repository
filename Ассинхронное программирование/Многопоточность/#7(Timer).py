import threading
import time


def test():
    while True:
        print("Test")
        time.sleep(1)


t = threading.Timer(10, test).start() # передаем кол-во секунд, передаем функцию

"""Когда проходит 10 секунд мы запускаем поток с использованием функции test"""

while True:
    print('111')
    time.sleep(2)




"""

def delayed():
    th_name = threading.current_thread().name
    print(f'Th:{th_name} Worker запущен')


# Создание и запуск потоков таймеров
t1 = threading.Timer(0.3, delayed)
t1.name = 'Timer-1'
t2 = threading.Timer(0.3, delayed)
t2.name = 'Timer-2'

print('Запуск таймеров')
t1.start()
t2.start()

print(f'Ожидание перед завершением {t2.name}')
time.sleep(0.2)
print(f'Завершение {t2.name}')
t2.cancel()
print('Выполнено')
"""