#!/usr/bin/env python3
""" strings to Redis """
import uuid
import redis
from typing import Union
UTypes = Union[str, bytes, int, float]


class Cache:
    """ Cache class """
    def __init__(self):
        """ initiate class """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: UTypes) -> str:
        """ return string """
        k = str(uuid.uuid4())
        self._redis.mset({k: data})
        return k
