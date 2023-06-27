#!/usr/bin/python3
"""Models a square"""


class Square():
    """Models a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes square attributes

        Args:
        size(int): Dimension of new square
        position(int, int): Position of new square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Accesses position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Updates the value of position"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(dgt, int) for dgt in value) or
                not all(dgt >= 0 for dgt in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square to stdout"""
        if self.__size == 0:
            print("")
            return
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for n in range(0, self.__size)]
            print("")
