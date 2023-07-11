#!/usr/bin/python3
"""Defines a class Student"""


class Student():
    """Models a class student"""
    def __init__(self, first_name, last_name, age):
        """Initializes attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves dictionary representation of student"""
        return self.__dict__
