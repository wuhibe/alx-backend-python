#!/usr/bin/env python3
''' module for task 8 '''
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    ''' function to return a multiplier function '''
    def multiply(val: float) -> float:
        ''' function to multiply value with multiplier '''
        return multiplier * val
    return multiply
