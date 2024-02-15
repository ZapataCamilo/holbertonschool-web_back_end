#!/usr/bin/env python3
"""
Here, we use 'typing.Callable' to specify
that we're returning a function.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function named 'multiplier_function'
    that multiplies a float 'x' by 'multiplier'.
    """
    def mulFloat(x: float) -> float:
        """
         Returns x times a closure named 'multiplier'.
        """
        return x * multiplier
    return mulFloat
