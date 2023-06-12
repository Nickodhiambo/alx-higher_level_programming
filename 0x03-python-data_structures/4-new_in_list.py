#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Replaces an element at a specific position
    in a list without modifying the original list"""

    if idx < 0 or idx > (len(my_list) - 1):
        return my_list.copy()
    else:
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
