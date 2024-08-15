#!/usr/bin/env python3
""" Implementing an expiring web cache and tracker """
import requests
import redis


def get_page(url: str) -> str:
    """
    uses the requests module to obtain the HTML content
    of a particular URL and returns it
    """
    key = f"count:{url}"
    count = redis.Redis().incr(key)
    cached_key = f"html:{url}"
    res = redis.Redis().get(cached_key)
    if res is None:
        res = requests.get(url).text
        redis.Redis().setex(cached_key, 10, res)
    return res
