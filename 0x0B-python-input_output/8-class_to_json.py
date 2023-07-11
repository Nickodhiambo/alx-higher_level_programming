#!/usr/bin/python3
"""Contains ine function that converts a class to json format"""


def class_to_json(obj):
    """Returns a dictionary representationof a class"""
    return obj.__dict__
