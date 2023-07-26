#!/usr/bin/python3
"""Create a class BasicCache that inherits
from BaseCaching and is a caching system:"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ It inherits from BasicCaching"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key is None or item is None:
            return
        else:
            self.cache_data[key] = item

    def get(self, key):
        if key is not None:
            value = self.cache_data.get(key)
            return value
