#!/usr/bin/env python3
""" strings to Redis """
import uuid
import redis
from typing import Union, Callable, Optional
import functools
import sys
UTypes = Union[str, bytes, int, float]


def count_calls(method: Callable) -> Callable:
    """ decorator """
    key = method.__qualname__
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ decorator """
    key = method.__qualname__
    inpt = f"{key}:inputs"
    outpt = f"{key}:outputs"
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper """
        self._redis.rpush(inpt, str(args))
        r = method(self, *args, **kwargs)
        self._redis.rpush(outpt, str(r))
        return r
    return wrapper


def replay(method: Callable) -> None:
    """ display the history of calls """
    key = method.__qualname__
    inpt = f"{key}:inputs"
    outpt = self._redis.lrange(key, 0, -1)

    print(f"{key} was called {len(outpt)} times:")
    for i, output in enumerate(outpt, start=1):
        decoded_output = output.decode('utf-8')
        print(f"{key}(*({decoded_output},))) -> {output}")


class Cache:
    """ Cache class """
    def __init__(self):
        """ initiate class """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
