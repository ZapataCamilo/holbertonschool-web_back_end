#!/usr/bin/env python3
"""
'Hello World!' figue in Python's
documentation for 'asyncio'.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Chooses a random number
    (somewhat) in the range of
    0 and 'max_delay',
    using 'random.uniform'.
    """
    dl: float = random.uniform(0, max_delay)
    await asyncio.sleep(dl)
    return dl
