import asyncio

async def do_work(item):
    #Выполнение какой - либо работы
    await asyncio.sleep(1)
    print(f'Работа {item} выполнена')

async def main():
    async with asyncio.TaskGroup() as tg:
        #Создание нескольких задач
        for item in range(3):
            tg.create_task(do_work(item))
        #TaskGroup будет ждать завершения
        #Всех задач, прежде чем выйдет из блока
#Запуск корутины
asyncio.run(main())