#!/usr/bin/python3
"""Supplies one function that returns True if an object is an exact
instance of a specified class"""


def is_same_class(obj, a_class):
    """Checks if an object is an instance of a class"""
    if type(obj) == a_class:
        return True
    return False
