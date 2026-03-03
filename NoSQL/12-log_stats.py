#!/usr/bin/env python3
"""Log stats - provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


def nginx_stats():
    """Provides some stats about Nginx logs"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    num_logs = nginx_collection.count_documents({})
    print("{} logs".format(num_logs))

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print("{} status check".format(status_check))


if __name__ == "__main__":
    nginx_stats()
