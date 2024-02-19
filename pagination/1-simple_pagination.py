#!/usr/bin/env python3
"""
Make a class to get data from the CSV file
containing the most popular baby names,
and return the data for that page.
"""
from typing import Tuple, List
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Assuming that 'page' represents the current page
    the user is on (1-INDEXED),
    and 'page_size' is the amount of articles per page
    """
    START: int = page_size * (page - 1)
    END: int = START + page_size
    return (START, END)


class Server:
    """
    Caches a file of the top 19419 most popular baby names
    from the CSV file named like the contents of
    'DATA_FILE'.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Returns the cached dataset.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Tries to return the data rows from 'self's data
        belonging to the page numbered 'page',
        using 'index_range'.
        """
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page >= 1
        assert page_size >= 1

        INDEXES: Tuple[int, int] = index_range(page, page_size)

        try:
            return self.dataset()[INDEXES[0]:INDEXES[1]]
        except IndexError:
            return []
