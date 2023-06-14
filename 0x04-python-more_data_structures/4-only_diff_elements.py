#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """ Returns a set of elements present in only one set"""

    one_set = set_1 ^ set_2
    return (one_set)
