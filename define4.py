import asyncio
import aiohttp
from time import perf_counter


def urls(n_reqs: int):
    for _ in range(n_reqs):
        yield "https://python.org"

async def get(session: aiohttp.ClientSession, url: str):
    async with session.get(url) as response:
        _ = await response.text()
             
async def main(n_reqs: int):
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(
            *[get(session, url) for url in urls(n_reqs)]
        )


if __name__ == "__main__":
    n_reqs = 10_000
    
    start = perf_counter()
    asyncio.run(main(n_reqs))
    end = perf_counter()
    
    print(f"{n_reqs / (end - start)} req/s")