#!/usr/bin/env python3
''' module for task 1 '''
import asyncio
import typing
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    '''function that spawns wait_random n times with the specified max_delay'''
    tasks: typing.List[float] = []
    lst: typing.List[float] = []
    while n > 0:
        tasks.append(asyncio.create_task(wait_random(max_delay)))
        n -= 1
    for task in asyncio.as_completed(tasks):
        lst.append(await task)
    return lst
