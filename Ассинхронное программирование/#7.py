import asyncio
import aiohttp
async def download_coroutine(session, url):
    async with session.get(url) as response:
        filename = url.split("/")[-1]
        with open(filename, "wb") as f:
            while True:
                chunk = await.response.content.read(1024)


