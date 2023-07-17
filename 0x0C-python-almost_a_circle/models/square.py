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

    def update(self, *args, **kwargs):
        """Assigns attributes"""
        if args and len(args) != 0:
            flag = 0
            for arg in args:
                if flag == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif flag == 1:
                    self.size = arg
                elif flag == 2:
                    self.x = arg
                elif flag == 3:
                    self.y = arg
                flag += 1

        else:
            if kwargs and len(kwargs) != 0:
                for key, value in kwargs.items():
                    if key == "id":
                        if value is None:
                            self.__init__(self.size, self.x, self.y)
                        else:
                            self.id = value
                    elif key == "size":
                        self.size = value
                    elif key == "x":
                        self.x = value
                    elif key == "y":
                        self.y = value

    def to_dictionary(self):
        """Returns dict representation oif a square"""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
