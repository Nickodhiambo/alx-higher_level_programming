#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """ Replaces all the occurrences of an item
    by another in a new list"""

    new_list = list(map(lambda x: replace if x == search else x, my_list))
    return (new_list)
