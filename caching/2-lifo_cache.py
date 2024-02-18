#!/usr/bin/env python3
"""
Create a class LIFOCache that inherits from
BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    key:value pair caching system, with a maximum capacity
    equal to 'BaseCaching.MAX_ITEMS'
    """
    def __init__(self):
        super().__init__()

        self.keys_stack = []
        """
        This class keeps track of its instances' stored pairs
        with a dictionary, called 'self.caching_data',
        and keeps track of the most recently added keys
        using 'self.keys_stack', which is a list with the
        least recently added keys first, and the most recently
        added keys last.
        """

    def get(self, key):
        """
        If 'key' is None or not in 'self.cache_data',
        this method just returns None.
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]

    def put(self, key, item) -> None:
        """
        First of all, if 'key' or 'item'
        are None, this method just returns None
        without doing anything.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Mark this key as the most recently added key
            self.keys_stack.remove(key)

        elif len(self.cache_data) == BaseCaching.MAX_ITEMS:
            MOST_RECENT_KEY = self.keys_stack.pop()
            """
            Key that was most recently added to
            'self.cache_data', through this method,
            found in 'self.keys_stack[-1]'.
            """
            del self.cache_data[MOST_RECENT_KEY]

            print(f"DISCARD: {MOST_RECENT_KEY}")

        self.cache_data[key] = item
        # add the key to 'keys_stack',
        # with its position indicating that it's
        # the most recently added key.
        self.keys_stack.append(key)
