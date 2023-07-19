#!/usr/bin/env python3
"""
Create a Cache class. In the __init__ method,
store an instance of the Redis client as a private variable
 named _redis (using redis.Redis())
and flush the instance using flushdb
"""
import redis
import uuid
from typing import Union, Callable, Optional, Any
from functools import wraps


def call_history(method: Callable) -> Callable:
    """ define a call_history decorator to store the history
    of inputs and outputs for a particular function."""
    @wraps(method)
    def call_history_inner_function(self, *args, **kwargs):
        """In call_history, use the decorated functions qualified name
        and append ":inputs" and ":outputs" to create input
        and output list keys, respectively."""
        qual_method = method.__qualname__
        input_key = qual_method + ":inputs"
        output_key = qual_method + ":outputs"
        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, output)
        return output
    return call_history_inner_function


def count_calls(method: Callable) -> Callable:
    """   count_calls decorator that takes a single method Callable
    argument and returns a Callable """
    @wraps(method)
    def count_calls_inner_function(self, *args, **kwargs):
        """As a key, use the qualified name of method
        using the __qualname__ dunder method."""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return count_calls_inner_function


class Cache:
    def __init__(self):
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ takes a data argument and returns a string.
        The method should generate a random key"""

        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self,
            key: str,
            fn: Optional[Callable] = None) -> Union[int,
                                                    float,
                                                    bytes,
                                                    str,
                                                    None]:
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
