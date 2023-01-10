#!/usr/bin/python3
""" This program writes an Object to a text file,
using a JSON representation """
import json


def save_to_json_file(my_obj, filename):
    """ this function writes an Object to a text file,
    using a JSON representation """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
