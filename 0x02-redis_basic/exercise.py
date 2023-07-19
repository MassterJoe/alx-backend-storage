#!/usr/bin/env python3
"""
Create a Cache class. In the __init__ method,
store an instance of the Redis client as a private variable
 named _redis (using redis.Redis())
and flush the instance using flushdb
"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
        """   count_calls decorator that takes a single method Callable
        argument and returns a Callable """
        @wraps(method)
        def count_calls_inner_function(self, *args, **kwargs):
            """As a key, use the qualified name of method 
            using the __qualname__ dunder method."""
            key = method.__qualname__
            self._redis.incr(key)
            method(self, *args, **kwargs)
        return count_calls_inner_function

class Cache:
    def __init__(self):
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()

    
    @count_calls
    def store(self, data: Union[int, float, bytes, str]) -> str:
        """ takes a data argument and returns a string.
        The method should generate a random key"""

        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self,
            key: str,
            fn: Optional[Callable] = None) -> Union[int, float, bytes, str]:
        """ a get method that take a key string argument and an
        optional Callable argument named fn """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is None:
            return value
        return fn(value)

    def get_str(self, key: str) -> Union[str, None]:
        """returns the value stored in the redis store at the key as str """
        return self.get(key, str)

    def get_int(self, key: int) -> Union[int, None]:
        """returns the value stored in the redis store at the key as int"""
        return self.get(key, int)
