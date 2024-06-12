from threading import Thread
from time import sleep

counter = 0

def function(x):
    global counter

    local_counter = counter
    local_counter += x
    sleep(0.1)

    counter = local_counter
    print(f' {counter=} ')

t1 = Thread(target= function, args=(10,))
t2 = Thread(target= function, args=(20,))

t1.start()
t2.start()

t1.join()
t2.join()
