#!/usr/bin/env python3
'''Writing strings to Redis'''


import redis
import uuid


class Cache:
    '''Cache class'''
    def __init__(self):
        '''Constructor'''
        self._redis = redis.Redis()
        self._redis.ping()
        self._redis.flushdb()

    def store(self, data):
        '''Store data in Redis'''
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key
