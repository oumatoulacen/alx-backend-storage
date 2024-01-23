#!/usr/bin/env python3
'''Python function that lists all documents in a collection'''


import pymongo
from pymongo import MongoClient


def list_all(mongo_collection):
    '''lists all documents in a collection'''
    collections = []
    for collection in mongo_collection.find():
        collections.append(collection)
    return collections
