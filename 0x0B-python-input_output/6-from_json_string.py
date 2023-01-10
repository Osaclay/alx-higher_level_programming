#!/usr/bin/python3
""" This program returns an object from json string """
import json


def from_json_string(my_str):
    """ this function returns an object (Python data structure)
    represented by a JSON string: """
    return (json.loads(my_str))
