#!/usr/bin/env python3
"""
Write a function named index_range that
takes two integer arguments page and page_size.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """

    This function returns the index of the first
    and last article in that page (0-INDEXED).
    """
    START: int = page_size * (page - 1)
    END: int = START + page_size
    return (START, END)
