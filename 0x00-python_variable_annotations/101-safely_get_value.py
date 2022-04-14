#!/usr/bin/env python3
''' module for task 11 '''
import typing


def safely_get_value(dct: typing.Mapping, key: typing.Any, default:
                     typing.Union[typing.TypeVar('T'), None] =
                     None) -> typing.Union[typing.Any, typing.TypeVar('T')]:
    ''' function using TypeVar '''
    if key in dct:
        return dct[key]
    else:
        return default
