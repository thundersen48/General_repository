import time
import asyncio
import aiofiles

filename_main = "test.txt"
semaphore = asyncio.Semaphore(
    5000
)  # Ограничение на количество одновременных операций I/O


async def write(data: str, filename: str):
    """Запись строки в файл"""
    async with semaphore:
        async with aiofiles.open(filename, mode="a") as f:
            await f.write(data + "\n")


async def make_requests():
    tasks = [write(f"Test {_}", filename_main) for _ in range(100000)]
    await asyncio.gather(*tasks)


async def main():
    start_time = time.time()
    await make_requests()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Total execution time: {elapsed_time} seconds")


asyncio.run(main())