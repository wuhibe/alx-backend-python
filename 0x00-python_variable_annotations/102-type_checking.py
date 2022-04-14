#!/usr/bin/env python3
''' module for task 12 '''
import typing


def zoom_array(lst: typing.List, factor: typing.Union[float, int] =
               2) -> typing.List:
    ''' function to zoom array '''
    zoomed_in: typing.List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
