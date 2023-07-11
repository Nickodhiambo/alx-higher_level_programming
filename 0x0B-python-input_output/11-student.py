#!/usr/bin/python3
"""Defines a class Student"""


class Student():
    """Models a class student"""
    def __init__(self, first_name, last_name, age):
        """Initializes attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves dictionary representation of student
        if attrs is a list of strings, return only attr anmes contained
        in the list
        """
        if (type(attrs) == list and
                all(type(item) == str for item in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the student instance"""
        for key, value in json.items():
            setattr(self, key, value)
