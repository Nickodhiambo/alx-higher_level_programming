#!/usr/bin/python3
"""This module defines Square subclass with Rectangle as
superclass
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes attributes of a square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Retrieves size"""
        return self.height

    @size.setter
    def size(self, value):
        """Modifies size"""
        self.width = value
        self.height = value

    def __str__(self):
        """Retruns string representation"""
        return "[Square] ({}) {}/{} - {}".format(
                    self.id,
                    self.x,
                    self.y,
                    self.width)
