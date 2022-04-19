#!/usr/bin/env python3
''' module for task 2 '''

import asyncio
from time import time
import typing
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    ''' measure the total runtime of calling
    async_comprehension 4 times '''
    t: float = time()
    tasks: typing.List[float] = []
    for i in range(4):
        tasks.append(asyncio.create_task(async_comprehension()))
    await asyncio.gather(*tasks)
    t = time() - t
    return t
