#!/usr/bin/env python3
''' module for task 2 '''
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    ''' function that measures runtime of wait_n '''
    t: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    t = time.time() - t
    return t/n
