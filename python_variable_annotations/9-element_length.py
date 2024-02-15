#!/usr/bin/env python3
"""
We were provided with the function 'element_length',
and we must annotate it.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples that each contain:
    the corresponding item in 'lst', and its len (int).
    """
    return [(i, len(i)) for i in lst]
