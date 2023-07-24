#!/usr/bin/python3
"""Defines a base class"""
import json


class Base:
    """A base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initalizes attributes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Serializes json data format"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes json string representation of json string object to a
        file

        Args:
            list_objs(list): A list of instances that inherit from base
        """
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_items = [item.to_dictionary() for item in list_objs]
                f.write(Base.to_json_string(list_items))
