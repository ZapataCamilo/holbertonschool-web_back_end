#!/usr/bin/env python3
"""
Imports 'wait_n' 1-concurrent_coroutines.py,
'asyncio' and 'time' from 'time'.
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n

tm = float


def measure_time(n: int, max_delay: int) -> tm:
    """
    Runs 'wait_n(n, max_delay)' using asyncio.
    """
    before: tm = time.process_time()
    asyncio.run(wait_n(n, max_delay))
    after: tm = time.process_time()

    total_time: tm = after - before
    return total_time / n
