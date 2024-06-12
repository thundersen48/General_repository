import threading

a = 0
lock = threading.Lock()

def x():
    global a
    for i in range(10000):
        lock.acquire()
        a+= 1
    lock.release()


threads = []

for i in range(5):
    thread = threading.Thread(target=x)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()


print(a)
assert a == 20000 # assert- проверяет является ли результат истинным