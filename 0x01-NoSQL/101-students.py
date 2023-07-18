#!/usr/bin/env python3
"""
Write a Python function that returns all students sorted by average score:
"""
def top_students(mongo_collection):
    """ The top must be ordered  """
    return mongo_collection.aggregate([{
        "$project": {
        "name": "$name",
      "averageField": { "$avg": "$topics.score" }
    }}, {"$sort": {"averageField": -1}}])
    