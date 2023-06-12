#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """ Finds all multiples of two in a list"""

    two_multiples = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            two_multiples.append(True)
        else:
            two_multiples.append(False)
    return (two_multiples)
