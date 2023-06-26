#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x elements of a list and only integers"""
    
    num = 0;

    for n in range(x):
        try:
            print("{:d}".format(my_list[n]), end="")
            num += 1
        except (ValueError, TypeError):
            continue;
    print("")
    return num
