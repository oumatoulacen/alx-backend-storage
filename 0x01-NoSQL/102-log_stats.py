#!/usr/bin/env python3
'''stats about Nginx logs stored in MongoDB
    and list  most present IPs in the collection
    nginx of the database logs '''


from pymongo import MongoClient


def nginx_stats():
    '''provides some stats about Nginx logs stored in MongoDB'''
    with MongoClient('mongodb://127.0.0.1:27017') as client:
        db = client.logs
        collection = db.nginx
        print(collection.count_documents({}), "logs")
        print("Methods:")
        print('\tmethod GET:', collection.count_documents({'method': 'GET'}))
        print('\tmethod POST:', collection.count_documents({'method': 'POST'}))
        print('\tmethod PUT:', collection.count_documents({'method': 'PUT'}))
        print('\tmethod PATCH:', collection.count_documents({'method': 'PATCH'}))
        print('\tmethod DELETE:', collection.count_documents({'method': 'DELETE'}))
        print(collection.count_documents({'method': 'GET', 'path': '/status'}), 'status check')

        # the most present IPs in the collection nginx of the database logs
        print("IPs:")
        # goup by ip and count the number of times it appears
        pipeline = {'$group': {'_id': '$ip', 'count': {'$sum': 1}}}
        sort = {'$sort': {'count': -1}}
        sorted_ips_count = list(collection.aggregate([pipeline, sort]))
        for ip_c in sorted_ips_count[:10]:
            print('\t', ip_c.get('_id'), ':', ip_c.get('count'))


if __name__ == "__main__":
    '''run as main function'''
    nginx_stats()
