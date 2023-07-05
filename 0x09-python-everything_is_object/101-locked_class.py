#!/usr/bin/python3
"""Supplies one class called LockedClass"""


class LockedClass():
    """This class prevents the user from dyanamically creating
    new attributes unless the attribute name is called first_name"""
    __slots__ = ['first_name']
