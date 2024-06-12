import threading
from time import sleep

def function1():
    print('Функция завершена')

threading.Timer(3,function1).start()
sleep(2)
print('Sleeping for 2 seconds')