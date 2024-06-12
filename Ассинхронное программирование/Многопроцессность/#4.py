import threading
import time

def handler(started = 0, finished = 0):
    result = 0
    for i in range (started, finished):
        result += i
        print('value:', result)

params = {'finished': 2**26}

task = threading.Thread(target= handler, kwargs= params) #target- функция, которую мы хотим выполнять параллельно
started_at = time.time()
print('Результат 1')
task.start()
task.join()
print('Time: {}'.format(time,time() - started_at))

results = []
started_at = time.time()
handler(finished= 2**24)
print('Результат 2 ')
print('Time:{}'.format(time.time() - started_at))
print('value:', sum(results))