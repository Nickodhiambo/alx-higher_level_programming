#!/usr/bin/python3

def no_c(my_string):
    """Removes all characters C and c from
    a string"""
    new_string = "".join([char for char in my_string if
                     char != "C" and char != "c"])
    return new_string
