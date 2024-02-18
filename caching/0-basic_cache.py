#!/usr/bin/env python3
"""
Create a class BasicCache that inherits from
BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Implements the 'get' and 'put'
    methods defined in this class' parent,
    'BaseCaching'.
    """
    MAX_ITEMS = None

    def put(self, key, item) -> None:
        """
         Sets 'self.cache_data[key] = item'.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Returns 'self.cache_data[key]'...
        """
        if key is None or key not in self.cache_data:
            return
        return self.cache_data[key]
