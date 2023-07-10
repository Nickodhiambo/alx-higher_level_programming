#!/usr/bin/python3
"""Supplies a function that checks if an object is an instance of a class
or if it is an instance of a cf a class that the specified
class inherited from"""


def is_kind_of_class(obj, a_class):
    """ Checks if a function is an instance of, or inherited instance of a
    class"""
    if isinstance(obj, a_class):
        return True
    return False
