#!/usr/bin/python3
"""Contains a function that converts json string to python
data structure"""
import json


def from_json_string(my_str):
    """Serializes a json string"""
    return json.loads(my_str)
