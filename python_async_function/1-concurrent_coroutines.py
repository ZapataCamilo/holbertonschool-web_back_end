#!/usr/bin/env python3
"""
Creates a coroutine that runs 'wait_random(max_delay)'
n times, all in parallel, and returns a list
of the results of each 'wait_random' call
(which should be the amount of time the coroutine took
ot run)
"""
import asyncio
from typing import List

second = float

wait_random = __import__('0-basic_async_syntax').wait_random


async def run(max: int, li: List) -> None:
    """
    Runs 'wait_random(max_delay)', awaits its return value,
    and appends its result to 'li'
    """
    li.append(await wait_random(max))


async def wait_n(n: int, max_delay: int) -> List[second]:
    """
    Runs 'wait_random(max_delay)' in parallel 'n' times,
    and returns a list of the amount of time
    (in floats representing seconds) each 'wait_random'
    call took, IN THE ORDER THAT THEY FINISHED.
    """
    r = []

    await asyncio.gather(
        *(
            run(max_delay, r)
            for _ in range(n)
        )
    )
    return r
