import asyncio


async def fun1(x):
    print(x**2)
    await asyncio.sleep(3)
    print('fun1 завершена')


async def fun2(x):
    print(x**0.5)
    await asyncio.sleep(3)
    print('fun2 завершена')


async def main():
    """Создаем конкректые задачи"""
    task1 = asyncio.create_task(fun1(4))
    task2 = asyncio.create_task(fun2(4))
# Указываем переключение к задаче
    print(type(task1))
    print(task1.__class__.__bases__)
    """
    Футура — это оболочка для некой асинхронной сущности
    """

    await task1
    await task2


asyncio.run(main())# Передаем значение асинхронной функции с эвейтами на задачи