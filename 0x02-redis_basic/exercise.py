#!/usr/bin/env python3
""" strings to Redis """
import uuid
import redis
from typing import Union, Callable, Optional
UTypes = Union[str, bytes, int, float]


def count_calls(method: Callable) -> Callable:
    """ decorator """
    key = method.__qualname__
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """ Cache class """
    def __init__(self):
        """ initiate class """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: UTypes) -> str:
        """ return string """
        k = str(uuid.uuid4())
        self._redis.mset({k: data})
        return k

    def get(self, key: str, fn: Optional[Callable] = None) -> UTypes:
        """
        take a key string argument &
        convert the data back to the desired format
        """
        if self._redis.get(key) and fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, value: bytes) -> str:
        """ convert  to string """
        # return value.decode("utf-8")
        return self.get(key, value.decode("utf-8"))

    def get_int(self, value: bytes) -> int:
        """ convert to integer """
        # return int.from_bytes(value, sys.byteorder)
        return self.get(key, int.from_bytes(value, sys.byteorder))
