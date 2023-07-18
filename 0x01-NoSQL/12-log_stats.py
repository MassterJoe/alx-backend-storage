#!/usr/bin/env python3
""" Nginx logs stored in MongoDB
"""
from pymongo import MongoClient

def log_stat():
    """data logs"""
    myclient = MongoClient("mongodb://localhost:27017/")
    mydb = myclient["logs"]
    mycol = mydb["nginx"]
    total_log = mycol.count_documents({})
    get = mycol.count_documents({"method": "GET"})
    post  = mycol.count_documents({"method": "POST"})
    put = mycol.count_documents({"method": "PUT"})
    patch =  mycol.count_documents({"method": "PATCH"})
    delete = mycol.count_documents({"method": "DELETE"})
    path = mycol.count_documents(
        {"method": "GET", "path": "/status"})


    print(f"{total_log} logs")
    print("Methods:")
    print(f"\tmethod GET: {get}")
    print(f"\tmethod POST: {post}")
    print(f"\tmethod PUT: {put}")
    print(f"\tmethod PATCH: {patch}")
    print(f"\tmethod DELETE: {delete}")
    print(f"{path} status check")


if __name__ == "__main__":
    log_stat()
