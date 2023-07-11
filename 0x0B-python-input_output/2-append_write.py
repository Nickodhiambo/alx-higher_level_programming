#!/usr/bin/python3
"""Contains a function that utilizes append method"""


def append_write(filename="", text=""):
    """Appends text to a file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
