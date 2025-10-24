
import asyncio
import aiohttp
import time

async def fetch(session, url):
    async with session.get(url) as response:
        data = await response.text()
        print(f"Pobrano {len(data)} bajtów z {url}")



async def main():

    urls = [
        "https://python.org",
        "https://wikipedia.org",
        "https://psinf.com",
        "https://python.org",
        "https://wikipedia.org",
        "https://psinf.com",
        "https://python.org",
        "https://wikipedia.org",
        "https://psinf.com",
    ]

    start = time.perf_counter()

    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*(fetch(session, url) for url in urls))

    elapsed = time.perf_counter() - start

    print(f"Czas wykonania (async): {elapsed:.2f} s")

asyncio.run(main())
