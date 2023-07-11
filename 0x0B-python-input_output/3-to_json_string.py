#!/usr/bin/python3
"""Contains a function that deserialize data"""
import json


def to_json_string(my_obj):
    """Converts string to JSON data"""
    return json.dumps(my_obj)
