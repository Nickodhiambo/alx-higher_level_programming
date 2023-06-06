#!/usr/bin/python3
# 8-uppercase.py

def uppercase(str):
    """Prints a string in uppercase."""
    for ch in str:
        if ord(ch) >= 97 and ord(ch) <= 122:
            ch = chr(ord(ch) - 32)
        print("{}".format(ch), end="")
    print("")
