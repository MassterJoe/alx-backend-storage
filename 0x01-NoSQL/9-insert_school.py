#!/usr/bin/env python3
"""
Write a Python function that inserts a new document in a collection based on kwargs:
"""
def insert_school(mongo_collection, **kwargs):
    """Returns the new _id"""
    collections = mongo_collection.insert_one(kwargs)
    return collections.inserted_id
