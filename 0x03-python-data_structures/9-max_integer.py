#!/usr/bin/python3

def max_integer(my_list=[]):
    """Finds the biggest integer of a list"""

    if len(my_list) == 0:
        return (None)

    max_int = my_list[0]
    for n in range(len(my_list)):
        if my_list[n] > max_int:
            max_int = my_list[n]
    return (max_int)
