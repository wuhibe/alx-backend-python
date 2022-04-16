#!/usr/bin/env python3
''' module for task 0 '''
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    ''' function that waits a random time b/n 0 and max_delay
    and returns the wait time '''
    r: float = random.uniform(0, max_delay)
    await asyncio.sleep(r)
    return r
