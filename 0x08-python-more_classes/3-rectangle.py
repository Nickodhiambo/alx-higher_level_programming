#!/usr/bin/python3
"""This module defines a rectangle"""


class Rectangle():
    """Defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes attributes"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Accesses width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """sets value for width"""
        if (not isinstance(value, int)):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Sets value for height"""
        if (not isinstance(value, int)):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Computes area"""
        return (self.height * self.width)

    def perimeter(self):
        """Computes perimeter"""
        if self.height == 0 or self.width == 0:
            return 0
        return (2 * (self.height + self.width))

    def __str__(self):
        """Prints rectangle to STDOUT using #"""
        if self.width or self.height == 0:
            print("")
        rect = []
        for i in range(self.height):
            [rect.append("#") for j in range(self.width)]
            if i != self.height:
                rect.append("\n")
        return ("".join(rect))
