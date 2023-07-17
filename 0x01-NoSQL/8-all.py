#!/usr/bin/env python3
""" A pthon function that lists all the documents in a collection """
def list_all(mongo_collection):
    """ Return an empty list if no document in the collection """
    return mongo_collection.find()