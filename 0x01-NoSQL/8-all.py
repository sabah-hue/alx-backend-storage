#!/usr/bin/env python3
"""  lists all documents in a collection """


def list_all(mongo_collection):
    """ list_all doc """
    return mongo_collection.find()
