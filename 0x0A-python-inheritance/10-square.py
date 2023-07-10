#!/usr/bin/python3
"""Defines a Square class that inherits froma Rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a square"""
    def __init__(self, size):
        """Initalizes square attributes"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
