import asyncio
from concurrent.futures import ThreadPoolExecutor
import traceback
import time

executor = ThreadPoolExecutor()


def benchm(to_call):
    def inner1(*args):
        begin = time.perf_counter()
        r = to_call(*args)
        end = time.perf_counter()
        print("Time taken", to_call.__name__, end - begin)
        return r

    return inner1


def abenchmark(runner):
    async def inner2(*blockings):
        blockings = [(benchm(f), *args) for f, *args in blockings]
        begin = time.perf_counter()
        r = await runner(*blockings)
        end = time.perf_counter()
        print("Time taken", runner.__name__, end - begin)
        return r

    return inner2


@abenchmark
async def arun_blockings(*blockings):
    loop = asyncio.get_event_loop()
    tasks = [loop.run_in_executor(executor, *fun) for fun in blockings]
    results = await asyncio.gather(*tasks)
    return results


def arun(coro):
    return asyncio.run(coro)
