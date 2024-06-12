import time
import threading

value = 0
l = threading.Lock()

def inc_value():
    global value # Передаем глабальное значение
    while True:
        l.acquire()# Блокируем доступ к остальным потокам к данной области
        value += 1
        time.sleep(0.01)
        print(value)
        l.release()# Освобождение области от блокировки

for _ in range(5):
    threading.Thread(target=inc_value).start()
