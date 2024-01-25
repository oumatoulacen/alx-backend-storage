#!/usr/bin/env python3
'''Writing strings to Redis'''


from typing import Callable, Union
import redis
import uuid


class Cache:
    '''Cache class'''
    def __init__(self):
        '''Constructor'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''Store data in Redis'''
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str, fn: Callable) -> Union[str, bytes, int, float]:
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
