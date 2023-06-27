#!/usr/bin/python3
"""Models a square"""


class Square():
    """Models a square"""
    def __init__(self, size=0):
        """Initializes the dimension of a square

        Args:
        size(int): The dimension of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
