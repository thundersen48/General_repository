import asyncio
import aiohttp
import time


start_time = time.time()# Инициализация времени начала
all_data = []# Для записи полученных данных

async def get_page_data(session, category: str, page_id: int) -> str:
    if page_id:
        url = f'https://ozon.ru/brand/{category}/?page={page_id}'
    else:
        url = f'https://ozon.ru/brand/{category}/'
    async with session.get(url) as resp: #Получаем данные по этому url
        assert resp.status == 200 # Проверяем статус, если 200 значит он роботоспособный, assert - это условие которое проверяется что утверждение является истинным
        print(f'get url: {url}')
        resp_text = await resp.text()#Ждем текст страницы
        all_data.append(resp_text)#Записываем данные страницы
        return resp_text


async def load_site_data():
    categories_list = ['playstation-79966341', 'adidas-144082850', 'bosch-7577796', 'lego-19159896']
    async with aiohttp.ClientSession() as session: #Мененджер контекста
        tasks = []
        for category in categories_list:
            for page_id in range(100):
                task = asyncio.create_task(get_page_data(session, category, page_id))# Для того чтобы все работало ассинхронно, формируем список задач
                tasks.append(task)
                # process text and do whatever we need...
        await asyncio.gather(*tasks)#Ожидания завершения списка задач, когда она завершится все добавится в tasks=[]


asyncio.run(load_site_data())#Запуск задач

end_time = time.time() - start_time
print(all_data)
print(f"\nExecution time: {end_time} seconds")