#!/usr/bin/env python3
"""
This time, this file uses
'Tuple' to specify that 'to_kv'
returns a tuple, and 'Union'
for the 'v' parameter.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with:
    'k' as the first item and
    the float representation
    of v squared as the second item.
    """
    return k, float(v ** 2)
