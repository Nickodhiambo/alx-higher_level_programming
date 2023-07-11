#!/usr/bin/python3
"""Supplies one function that reads a file"""


def read_file(filename=""):
    """Reads a textfile and prints it to STDOUT"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
