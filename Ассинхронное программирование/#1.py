import time
import asyncio

def fun1(x):
    print(x**2)
    time.sleep(3)
    print('fun1 завершена')

"""fun2 ждет, когда отработает fun1 полностью"""
def fun2(x):
    print(x**0.5)
    time.sleep(3)
    print('fun2 завершена')

"""Весь процесс занимает 3+3 = 6 секунд."""
def main():
    fun1(4)
    fun2(4)


print(time.strftime('%X'))
main()
print(time.strftime('%X'))
"""Исходный код, но выполненный с помощью библиотеки Asyncio"""

async def fun1(x): # Говорим что функция должна выполняться ассинхронно!
    print(x**2)
    await asyncio.sleep(3) # Не останавливает интерпретатор
    print('fun1 завершена')
"""Fun1 говорит интерпретатору иди дальше я пока посплю"""

async def fun2(x):
    print(x**0.5)
    await asyncio.sleep(3)
    print('fun2 завершена')


async def main():
    task1 = asyncio.create_task(fun1(4))
    task2 = asyncio.create_task(fun2(4))

    await task1
    await task2


print(time.strftime('%X'))

asyncio.run(main())

print(time.strftime('%X'))