#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list"""

    try:
        for element in my_list[:x]:
            print("{}".format(element), end="")
        return sum(1 for element in my_list[:x])
    except IndexError:
        for element in my_list:
            print("{}".format(element), end="")
        return sum(1 for element in my_list)
