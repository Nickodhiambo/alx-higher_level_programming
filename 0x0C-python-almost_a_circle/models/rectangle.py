#!/usr/bin/python3
"""Defines a subclass Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Creates a Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets x-coordinate"""
        return self. __x

    @x.setter
    def x(self, value):
        """Sets x coordinate"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets y coordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets y coordinate"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of a rectangle"""
        return (self.width * self.height)

    def display(self):
        """Prints a rectangle representation to stdout using "#" symbol"""
        if self.height == 0 and self.width == 0:
            print("")
            return

        for i in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for j in range(self.width)]
            print("")

    def __str__(self):
        """Returns string representation of a rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                                                    self.id,
                                                    self.x,
                                                    self.y,
                                                    self.width,
                                                    self.height)

    def update(self, *args, **kwargs):
        """Assigns positional and keyword arguments to rectangle instances"""
        if args and len(args) != 0:
            flag = 0
            for arg in args:
                if flag == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif flag == 1:
                    self.width = arg
                elif flag == 2:
                    self.height = arg
                elif flag == 3:
                    self.x = arg
                elif flag == 4:
                    self.y = arg
                flag += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returns dictionary representation of the Rectangle"""
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
