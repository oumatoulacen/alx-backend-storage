#!/usr/bin/env python3
'''stats about Nginx logs stored in MongoDB'''


from pymongo import MongoClient


def nginx_stats():
    '''provides some stats about Nginx logs stored in MongoDB'''
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx
    print(collection.count_documents({}), "logs")
    print("Methods:")
    print('    method GET:', collection.count_documents({'method': 'GET'}))
    print('    method POST:', collection.count_documents({'method': 'POST'}))
    print('    method PUT:', collection.count_documents({'method': 'PUT'}))
    print('    method PATCH:', collection.count_documents({'method': 'PATCH'}))
    print('    method DELETE:', collection.count_documents({'method': 'DELETE'}))
    print(collection.count_documents({'method': 'GET', 'path': '/status'}), 'status check')

if __name__ == "__main__":
    '''run as main function'''
    nginx_stats()
