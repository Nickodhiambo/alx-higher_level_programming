#!/usr/bin/python3
"""Find the biggest number in a list with lowest search complexity"""


def find_peak(list_of_integers):
    """Find the biggest number in a list with lowest search complexity"""

    # Checks if list is empty
    if list_of_integers == []:
        return None

    list_size = len(list_of_integers)
    if list_size == 1:
        return list_of_integers[0]
    if list_size == 2:
        return max(list_of_integers)

    # get the middle element and assign peak
    mid = int(list_size / 2)
    peak = list_of_integers[mid]

    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak
    elif peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
