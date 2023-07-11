#!/usr/bin/python3
"""Defines a function that writes an object to a file using
JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """Writes a json object to a file"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
