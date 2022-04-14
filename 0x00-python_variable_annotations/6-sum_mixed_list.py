#!/usr/bin/env python3
''' module for task 6 '''
import typing


def sum_mixed_list(mxd_list: typing.List[typing.Union[int, float]]) -> float:
    ''' takes a list of ints and floats as argument and returns their sum '''
    return sum(num for num in mxd_list)
