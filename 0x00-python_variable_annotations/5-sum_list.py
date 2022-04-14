#!/usr/bin/env python3
''' module for task 5 '''
import typing


def sum_list(input_list: typing.List[float]) -> float:
    ''' takes a list of floats as argument and returns their sum '''
    return sum(fl for fl in input_list)
