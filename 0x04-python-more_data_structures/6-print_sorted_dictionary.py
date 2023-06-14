#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys"""

    ordered_keys = list(a_dictionary)
    ordered_keys.sort()
    for key in ordered_keys:
        print("{}: {}".format(key, a_dictionary.get(key)))
