#!/usr/bin/env python3
''' module for task 9 '''
import typing


def element_length(lst: typing.Iterable[typing.Sequence]) -> typing.List[
        typing.Tuple[typing.Sequence, int]]:
    ''' return values with the appropriate types '''
    return (i, len(lst))
