import threading
from time import sleep

total = 100
t_lock = threading.Lock()

def prog(N):
    global total
    t_lock.acquire()
    if total >= N:
        sleep(1)
        total -= N
    t_lock.release()
    print("new thread", total)
# Будем этот принт запускать в отдельном потоке


t = [threading.Thread(target=prog,
    args=[30]) for i in range(10)]
[t1.start() for t1 in t]
[t1.join() for t1 in t]

print('total amount', total)