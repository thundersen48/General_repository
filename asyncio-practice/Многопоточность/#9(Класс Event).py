from time import sleep
from threading import Thread, Event, current_thread, active_count
"""
Функция current_thread — определяет имя текущего потока, 
функция active_count — сообщает текущее число потоков
"""

event = Event()
# Указываем максимальное кол-во потоков
max_t = 5

def f():
    thr_num = current_thread().name
    print(f"Поток {thr_num} запустился. Но ждёт остальных.")
    event.wait()
    print(f"Событие наступило! Поток {thr_num} продолжил свою работу")


# Запускаем в цикле потоки с задержкой в 0.2 секунды
for i in range(max_t):
    Thread(target=f).start()
    sleep(0.2)
# Как только все потоки будут запущены, устанавливаем флаг event (говорим что событие наступило)
if active_count() >= max_t:
    event.set()