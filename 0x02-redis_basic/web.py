#!/usr/bin/env python3
'''Writing strings to Redis'''


import redis


class Cache:
    '''Cache class'''
    def __init__(self):
        '''Constructor'''
        self._redis = redis.Redis()
        self._redis.ping()
        self._redis.flushdb()

    def store(self, data):
        '''Store data in Redis'''
        for key in data:
            self._redis.set(key, data[key])
        return None