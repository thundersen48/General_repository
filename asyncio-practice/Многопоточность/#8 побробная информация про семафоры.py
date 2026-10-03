import asyncio
from asyncio import Semaphore
import time
from random import random


num = 0

async def main_task():
    global num
    asyncio.sleep(random())
    num += 1
    print(f'Производится примерка одежды. На сегодня это уже {num} клиент')



async def get_some_dress(semaphore: Semaphore):
    await semaphore.acquire()# Занимаем примерочную, счётчик свободных примерочных уменьшился на 1
    start = time.time()
    await main_task()
    time_of_work = time.time() - start
    print('Время работы', time_of_work)
    await asyncio.sleep(1 - time_of_work)
    semaphore.release()


async def main():
    semaphore = Semaphore(10) # Распорядитель торгового зала
    tasks_from_customers = [get_some_dress(semaphore) for _ in range(100)]
    await asyncio.wait(tasks_from_customers) # Запускаем задачи

loop = asyncio.get_event_loop()
asyncio.run(main())




