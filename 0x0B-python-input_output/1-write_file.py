#!/usr/bin/python3
"""Contains one function that writes into a file and returns
the number of chars written"""


def write_file(filename="", text=""):
    """Writes into a file and returns the no of chars written"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
