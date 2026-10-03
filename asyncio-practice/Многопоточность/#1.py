import os
import threading
import time
from threading import Thread
from tkinter import *
from tkinter import ttk

def waiting (timeout): #Функция ждет кол-во секунд
    while timeout > 0:
        timeout -= 1
        time.sleep(1)
    print('Good!')


def thread_waiting(timeout):
    thread = Thread(target = waiting, args=(timeout,),daemon=True) # В target указываем  функцию которая будет выполняться!
    thread.start()#Производим запуск потока
    return thread

counter = [0]
def inc():
    c = counter[0]
    time.sleep(0.1)
    counter[0] = c + 1

def info():
    pid = os.getpid()
    name = threading.current_thread().name
    print(f'Process {pid}, name {name}')

if __name__ == '__main__':
    """Создание графического окна"""
    tk = Tk()
    button1 = ttk.Button(tk,text = 'WAIT', command=lambda: waiting(3))
    button1.pack(side=LEFT)
    button2 = ttk.Button(tk, text = 'THREAD', command= lambda: thread_waiting(3))
    button2.pack(side = LEFT)
    tk.mainloop()
    info()