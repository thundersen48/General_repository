import asyncio, time
async_mode = False

def showjob(jobname, sync_time_seconds = 0):
    """Сколько времни прошло"""
    curtime = time.perf_counter() - start_time
    print(f'{curtime:.2f};\t{jobname}' )
    if sync_time_seconds:
        time.sleep(sync_time_seconds / 60)


async def PourCoffe():
    showjob('Кофе: Ставим чайник наполняться водой',20)
    showjob('Кофе: ждем наполнения чайника водой', 40)
    showjob('Кофе: Ставим чайник нагреваться', 10)
    showjob('Кофе: Ждем пока нагреется чайник',0)
    await asyncio.sleep(3) if async_mode else time.sleep(3)

async def FreEggsAsync(eggs_count):
    showjob('Яичница: Достаем сковородку и ставим на плиту ', 20)
    showjob('Яичница: Наливаем масло и закидываем яйца с овощами',15)
    showjob('Яичница: Ожидаем готовности',300)

async def ToastAsync():
    pass

async def main():
    await asyncio.gather(PourCoffe(), FreEggsAsync(3), ToastAsync())
    #asyncio.gather() - Запуск несколько корутин

start_time = time.perf_counter()
asyncio.run(main())
elapsed = time.perf_counter() - start_time
print('Завтрак готов за', round(elapsed,2), 'минут.')