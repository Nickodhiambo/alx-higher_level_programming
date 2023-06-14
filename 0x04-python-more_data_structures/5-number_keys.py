#!/usr/bin/python3

def number_keys(a_dictionary):
    """Returns the number of keys in a dictionary"""

    num = 0
    list_of_keys = list(a_dictionary)

    for n in list_of_keys:
        num += 1
    return num
