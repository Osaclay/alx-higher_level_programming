#!/usr/bin/python3
""" This program serializes an object to JSON string """
import json


def to_json_string(my_obj):
    """ this function returns the JSON representation of an object (string) """
    return (json.dumps(my_obj))
