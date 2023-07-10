#!/usr/bin/python3
"""Supplies one class that prints a sorted list"""


class MyList(list):
    """Prints a sorted list"""
    def print_sorted(self):
        """sorts a list"""
        print (sorted(self))
