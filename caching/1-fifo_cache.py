#!/usr/bin/env python3
"""
Create a class FIFOCache that inherits from
BaseCaching and is a caching system:
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Keeps track of key:value pairs
    in a dictionary called 'self.cache_data'.
    """
    def __init__(self) -> None:
        super().__init__()

        self.keys_queue = []
        """
        Should be all of the keys added to
        'self.cache_data' THROUGH 'self.put'.
        """

    def put(self, key, item) -> None:
        """
        If 'key' or 'item' are None,
        this method just returns without doing anything.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.keys_queue.remove(key)

        elif len(self.cache_data) == BaseCaching.MAX_ITEMS:
            OLDEST_KEY = self.keys_queue.pop(0)
            del self.cache_data[OLDEST_KEY]

            print(f"DISCARD: {OLDEST_KEY}")

        self.cache_data[key] = item
        self.keys_queue.append(key)

    def get(self, key):
        """
        If 'key' is None,
        or if 'key' isn't a key in 'self.cache_data',
        just returns None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
