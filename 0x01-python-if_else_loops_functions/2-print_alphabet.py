#!/usr/bin/python3

"""Prints ASCII alphabet in lowercase followed by a new line"""
for letter in range(97, 123):
    print("{}".format(chr(letter)), end = "")
