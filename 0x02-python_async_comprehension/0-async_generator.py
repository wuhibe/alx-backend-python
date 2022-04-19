#!/usr/bin/env python3
''' module for task 0 '''
import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    ''' function that asynchronously waits 1 second,
    then yield a random number between 0 and 10.'''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
