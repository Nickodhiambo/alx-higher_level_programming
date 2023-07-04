#!/usr/bin/python3
"""This module defines a rectangle"""


class Rectangle():
    """Defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes attributes"""
        Rectangle.number_of_instances += 1
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
        self.__height = value

    def area(self):
        """Computes area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """Computes perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2 * (self.__height + self.__width))

    def __str__(self):
        """Prints rectangle to STDOUT using #"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Returns a string representation of the rectangle"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", "+str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Prints to STDOUT upon deletion of rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
