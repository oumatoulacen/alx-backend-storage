#!/usr/bin/env python3
'''stats about Nginx logs stored in MongoDB'''


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

if __name__ == "__main__":
    '''run as main function'''
    nginx_stats()

# #!/usr/bin/env python3
# '''stats about Nginx logs stored in MongoDB'''


# from pymongo import MongoClient


# def nginx_stats():
#     '''provides some stats about Nginx logs stored in MongoDB'''
#     with MongoClient('mongodb://127.0.0.1:27017') as client:
#         db = client.logs
#         collection = db.nginx

#         total_logs = collection.count_documents({})
#         print(f"{total_logs} logs")

#         print("Methods:")
#         print(f'\tmethod GET: {collection.count_documents({"method": "GET"})}')
#         print(f'\tmethod POST: {collection.count_documents({"method": "POST"})}')
#         print(f'\tmethod PUT: {collection.count_documents({"method": "PUT"})}')
#         print(f'\tmethod PATCH: {collection.count_documents({"method": "PATCH"})}')
#         print(f'\tmethod DELETE: {collection.count_documents({"method": "DELETE"})}')

#         status_check_count = collection.count_documents({"method": "GET", "path": "/status"})
#         print(f'{status_check_count} status check')

# if __name__ == "__main__":
#     '''run as main function'''
#     nginx_stats()
