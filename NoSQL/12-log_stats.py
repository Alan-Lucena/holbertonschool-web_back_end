#!/usr/bin/env python3
"""Provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


def main():
    """Main function to display stats
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    print("{} logs".format(collection.count_documents({})))
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))
    print("{} status check".format(
        collection.count_documents({"method": "GET", "path": "/status"})))


if __name__ == "__main__":
    main()
