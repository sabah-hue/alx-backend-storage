#!/usr/bin/env python3
""" changes all topics of a school document based on the name """


def update_topics(mongo_collection, name, topics):
    """ update topics """
    mongo_collection.update_many({name}, {$set: {topics}})
