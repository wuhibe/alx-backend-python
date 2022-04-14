#!/usr/bin/env python3
''' module for task 10 '''
import typing


def safe_first_element(lst: typing.Sequence[typing.Any]) -> typing.Union[
        typing.Any, None]:
    ''' function with correct duck-typed annotations '''
    if lst:
        return lst[0]
    else:
        return None
