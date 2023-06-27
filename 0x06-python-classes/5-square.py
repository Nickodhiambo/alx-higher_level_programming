#!/usr/bin/python3
"""Models a square"""


class Square():
    """Models a square"""
    def __init__(self, size=0):
        """Initializes square attributes

        Args:
        size(int): Dimension of new square
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """ Updates the size of the square

        Args:
        value(int): The value to update
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square to stdout"""
        for i in range(self.__size):
            [print("#", end="") for n in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
