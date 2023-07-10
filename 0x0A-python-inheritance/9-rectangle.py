#!/usr/bin/python3
"""Defines a class Rectangle which inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Models a rectangle object"""
    def __init__(self, width, height):
        """Initializes rectangle attributes"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Computes area"""
        return (self.__width * self.__height)

    def __str__(self):
        """Returns print representation of rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
