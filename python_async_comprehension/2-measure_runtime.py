#!/usr/bin/env python3
"""
Import async_comprehension from the previous file and write a measure_runtime
coroutine that will execute async_comprehension four times
in parallel using asyncio.gather.
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Runs 'async_comprehension()'
    4 times in parallel
    (using 'asyncio.gather(async_comprehension(), +3)')
    and returns the amount of time it took.
    """
    b: float = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    a: float = time.perf_counter()

    return a - b
