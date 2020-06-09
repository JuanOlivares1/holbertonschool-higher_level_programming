#!/usr/bin/python3
"""Module - Base class"""
import json


class Base():
    """Class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """constructor
        Args:
            id (int): identificator
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries
        Args:
            list_dictionaries (list)
        Return: JSON string"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)


    @staticmethod
    def to_json_string(list_dictionaries):
        """dict 2 string
        Args:
            list_dictionaries ([type]): [description]
        Returns:
            [type]: [description]
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
