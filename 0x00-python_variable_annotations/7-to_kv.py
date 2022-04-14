#!/usr/bin/env python3
''' module for task 7 '''
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    ''' function to accept int or float and return square with str as tuple '''
    return (k, v**2)
