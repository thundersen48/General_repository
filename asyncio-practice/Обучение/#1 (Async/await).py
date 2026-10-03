import asyncio

async def one():
    return 1

async def greet():
    await asyncio.sleep(2) # Ожидания результата с задержкой 2 секунды
    return 'Hello world!'

# Задаем параллельность вывода результата
"""Await- преостанавилвает значение функции до тех пор, пока не будет получен результат"""
async def main():
    res1 = await one()
    res2 = await greet()
# Печатаем получившиеся значения
    print(res1)
    print(res2)

asyncio.run(main())
