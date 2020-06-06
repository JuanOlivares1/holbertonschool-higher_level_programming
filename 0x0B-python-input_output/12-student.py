#!/usr/bin/python3
"""Module"""


class Student():
    """Class"""
    def __init__(self, first_name, last_name, age):
        """Constructor
        Args:
            first_name (str)
            last_name (str)
            age (int)
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method
        Args:
            attrs (list)
        """
        if attrs is None or type(attrs) != list:
            return self.__dict__

        rtn = {}
        for item in attrs:
            if item in self.__dict__:
                rtn[item] = self.__dict__.get(item)
        return rtn
