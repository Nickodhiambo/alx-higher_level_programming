#!/usr/bin/python3
"""Supplies a function that checks if an instance
is inherited from another class"""


def inherits_from(obj, a_class):
    """Checks if an object of a class is inherited"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
