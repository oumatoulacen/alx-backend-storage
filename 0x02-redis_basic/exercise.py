#!/usr/bin/env python3
'''Writing strings to Redis'''


from functools import wraps
from typing import Callable, Union, Any
import redis
import uuid


def count_calls(method: Callable) -> Callable:
    '''Count calls decorator'''
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''Wrapper'''
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    """store the history of inputs and outputs"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper for the decorated function"""
        input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)
        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)
        return output

    return wrapper


class Cache:
    '''Cache class'''
    def __init__(self):
        '''Constructor'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''Store data in Redis'''
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(
        self,
        key: str,
        fn: Callable = None
        ) -> Union[str, bytes, int, float]:
        '''Get data from Redis'''
        data = self._redis.get(key)
        if fn is not None:
            return fn(data)
        else:
            return data

    def get_str(self, key: str) -> str:
        '''Retrieve string data from Redis'''
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        '''Retrieve integer data from Redis '''
        return self.get(key, lambda d: int(d))
