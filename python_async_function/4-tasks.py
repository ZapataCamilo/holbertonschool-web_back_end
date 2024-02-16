#!/usr/bin/env python3
"""
Take the code from wait_n and alter it into a new function task_wait_n.
The code is nearly identical to wait_n except task_wait_random is being called.
"""

import asyncio
from typing import List
task_wait_random = __import__("3-tasks").task_wait_random

i = float


async def append_wait_n(max_delay: int, li: list):
    """
    Runs 'task_wait_random(max_delay)', awaits its return value,
    and appends its result to 'l'.
    """
    li.append(await task_wait_random(max_delay))


async def task_wait_n(n: int, max_delay: int) -> List[i]:
    """
    This function achieves this, by running an intermediary
    awaitable, 'run_and_append(max_delay, result)',
    that awaits 'task_wait_random(max_delay)', then
    appends its result to 'result', which should be the
    result list.
    """
    r = []
    await asyncio.gather(
        *(
            append_wait_n(max_delay, r)
            for _ in range(n)
        )
    )

    return r
