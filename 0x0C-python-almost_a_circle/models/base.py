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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file
        Args:
            cls (class)
            list_objs (list)"""
        li = []
        with open(cls.__name__ + ".json", mode="w") as fl:
            if list_objs is None:
                fl.write(Base.to_json_string(list_objs))
                return
            for i in list_objs:
                li.append(i.to_dictionary())
            fl.write(Base.to_json_string(li))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string
        Args:
            json_string (str)
        Returns: list
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """method"""
        if cls.__name__ == "Square":
            obj = cls(1)
        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)

        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """method"""
        try:
            with open(cls.__name__ + ".json", mode="r") as fl:
                data = cls.from_json_string(fl.read())
                return [cls.create(**dic) for dic in data]
        except FileNotFoundError:
            return []
