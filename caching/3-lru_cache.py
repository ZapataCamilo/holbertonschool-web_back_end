#!/usr/bin/env python3
"""
Create a class LRUCache that inherits
from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    Caching system that uses a dictionary (named 'self.cache_data')
    and a list to keep track of the LRU (least recently used)
    key.
    """
    def __init__(self):
        """
        The list of all of the keys
        in 'self.cache_data',
        in order of LRU to MRU
        (least recently used to most recently used)
        """
        super().__init__()
        self.lru_keys: list = []

    def get(self, key):
        """
        If 'key' is None or if 'key' isn't present in
        'self.cache_data', this method returns None.
        """
        if key is None or key not in self.cache_data:
            return None

        self.lru_keys.remove(key)
        self.lru_keys.append(key)

        return self.cache_data[key]

    def put(self, key, item) -> None:
        """
        If 'key' or 'item' are None,
        this method returns before doing anything else
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.lru_keys.remove(key)

        elif len(self.cache_data) == BaseCaching.MAX_ITEMS:
            LRU_key = self.lru_keys.pop(0)
            del self.cache_data[LRU_key]

            print(f'DISCARD: {LRU_key}')

        self.lru_keys.append(key)
        self.cache_data[key] = item
