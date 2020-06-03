#!/usr/bin/python3
"""Module"""


def add_attribute(obj, name, value):
    """function add_attribute - adds a new attribute to an object
    if it’s possible:
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
