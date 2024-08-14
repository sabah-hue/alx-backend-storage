#!/usr/bin/env python3
""" strings to Redis """
import uuid
import redis


class Cache:
    """ Cache class """
    def __init__(self):
        """ initiate class """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: UnionOfTypes) -> str:
        """ return string """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
