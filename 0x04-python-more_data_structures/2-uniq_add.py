#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Adds all unique integers in a list"""

    new_list = set(my_list)
    add = 0

    for num in new_list:
        add += num
    return add
