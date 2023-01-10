#!/usr/bin/python3
""" This program dumps class to Json """


def class_to_json(obj):
    """ this function returns the dictionary description with simple
    data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object """
    return (obj.__dict__)
