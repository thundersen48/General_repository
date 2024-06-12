import asyncio
import time

async def func1(x):
    print(x**2)
    await asyncio.sleep(3)
    print('Fun1 завершена')

async def func2(x):
    print(x**0.5)
    await asyncio.sleep(3)
    print('Fun2 Завершена')

print(time.strftime('%x'))
loop = asyncio.get_event_loop()
task1 = loop.create_task(func1(4))
task2 = loop.create_task(func2(4))
loop.run_until_complete(asyncio.wait([task1, task2]))

print(time.strftime('%X'))
print(type(func1(4)))# получим класс корутину
"""Корутина - это разновидность генератора"""

