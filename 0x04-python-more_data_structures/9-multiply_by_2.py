#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """Returns a new dictionary with all values multiplied
    by 2"""
    new_dict = a_dictionary.copy()
    list_of_keys = list(new_dict)

    for key in list_of_keys:
        new_dict[key] *= 2
    return new_dict
