#!/usr/bin/env python3
"""
Make a coroutine called 'async_generator'.
"""
import asyncio
import random

from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
     An async generator that yields 10 floats.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
